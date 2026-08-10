#!/usr/bin/env python3
"""Give every post an explicit `description:` in its frontmatter.

jekyll-seo-tag builds each page's <meta name="description"> from
`page.description`, falling back to the post's excerpt — the first paragraph.
That fallback fails badly here: most posts open with an image, an HTML comment
or a heading, which strips to nothing, so seo-tag falls back again to
`site.description` and 63 of 119 pages ended up sharing the meta description
"More questions than answers". Another twenty got "Foreword" or "Chapter 1".

Nearly every post already carries a `subtitle:`, which is the summary we want.
This script writes one out:

    description: "Diffusion is just stacked denoising score matching! Our goal
    is to approximate a data distribution p(x) with a model..."

built from the subtitle, topped up from the first real prose paragraph until it
is long enough to serve as a search snippet.

Posts that already have a `description:` are left alone, so hand-written ones
survive and re-running is idempotent. Use --force to regenerate them.

Usage:
    python3 scripts/backfill_descriptions.py            # dry run, show the diff
    python3 scripts/backfill_descriptions.py --write    # actually edit frontmatter
    python3 scripts/backfill_descriptions.py --force --write   # redo existing ones
    python3 scripts/backfill_descriptions.py --write _posts/technical-posts

Descriptions are aimed at roughly 155 characters, which is about what Google
renders before truncating.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# A post's frontmatter block: --- ... --- at the very top of the file.
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?\r?\n)---[ \t]*\r?\n", re.DOTALL)
# An existing `description:` key, including any indented continuation lines.
DESCRIPTION_RE = re.compile(
    r"^description:[^\r\n]*\r?\n(?:[ \t]+[^\r\n]*\r?\n)*", re.MULTILINE
)
# `subtitle: ...` on one line — the value we most want to reuse.
SUBTITLE_RE = re.compile(r"^subtitle:[ \t]*([^\r\n]*)", re.MULTILINE)

TARGET_LENGTH = 155
# Below this, a description is too thin to stand on its own and we top it up.
TOPUP_BELOW = 110

# Paragraphs that carry no summary value and must never seed a description.
SKIP_PARAGRAPH = re.compile(
    r"""
      ^\s*<!--                 # HTML comment
    | ^\s*\#{1,6}\s            # markdown heading
    | ^\s*!\[                  # markdown image
    | ^\s*<img\b               # html image
    | ^\s*<(?:div|figure|table|iframe|video|script|style)\b
    | ^\s*\{%                  # liquid tag ({% cite %}, {% bibliography %}, ...)
    | ^\s*\$\$                 # display math
    | ^\s*\[\^                 # footnote definition
    | ^\s*\|                   # table row
    | ^\s*[-*_]{3,}\s*$        # horizontal rule
    | ^\s*\*\*References\*\*
    # Editorial notes — "_updated (22/07/25). Added refs_", "(edited 22/07/25:
    # used an LLM to rewrite)". They are about the post, not in it.
    | ^\s*[_*(\[]*\s*(?:updated|edited|note|disclaimer|tldr)\b
    """,
    re.VERBOSE | re.IGNORECASE,
)

# Inline markup to unwrap or drop when flattening markdown to plain prose.
INLINE_SUBS = [
    (re.compile(r"\{\{.*?\}\}|\{%.*?%\}", re.DOTALL), ""),   # liquid
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), ""),               # images
    (re.compile(r"\[\^[^\]]*\]"), ""),                       # footnote refs
    (re.compile(r"\[([^\]]*)\]\([^)]*\)"), r"\1"),           # links -> text
    (re.compile(r"`([^`]*)`"), r"\1"),                       # inline code
    (re.compile(r"\$\$?([^$]*)\$\$?"), r"\1"),               # inline math
    (re.compile(r"\*\*([^*]*)\*\*|\*([^*]*)\*"), r"\1\2"),   # bold / italic
    (re.compile(r"__([^_]*)__"), r"\1"),                     # bold
    # _italics_, but only at word boundaries — subscripts in surviving LaTeX
    # (p_\theta, T_{p(x)}) must not be treated as emphasis markers.
    (re.compile(r"(?<![\w\\])_([^_\n]+)_(?!\w)"), r"\1"),
    (re.compile(r"<[^>]+>"), ""),                            # stray html
    (re.compile(r"^\s*>\s*"), ""),                           # blockquote marker
]


def strip_frontmatter(text):
    """Return the post body, with the frontmatter block removed."""
    match = FRONTMATTER_RE.match(text)
    return text[match.end():] if match else text


def flatten(paragraph):
    """Turn one markdown paragraph into a single line of plain prose."""
    text = paragraph
    for pattern, replacement in INLINE_SUBS:
        text = pattern.sub(replacement, text)
    # A trailing backslash is a markdown hard line break; it is punctuation in
    # the source, noise in a snippet.
    text = re.sub(r"\\+[ \t]*$", "", text, flags=re.MULTILINE)
    # Undo markdown escaping, so "\$8 million" reads as "$8 million".
    text = re.sub(r"\\+([$*_#\[\]\\`])", r"\1", text)
    # Curly quotes and dashes are fine in a meta description; runs of
    # whitespace and hard line breaks are not.
    return re.sub(r"\s+", " ", text).strip()


def first_prose(body):
    """The first paragraph of `body` that actually reads as prose."""
    for paragraph in re.split(r"\r?\n\s*\r?\n", body):
        if not paragraph.strip():
            continue
        if SKIP_PARAGRAPH.search(paragraph):
            continue
        flat = flatten(paragraph)
        # A line that survives stripping but is only a few words (a stray
        # caption, an "(edited 22/07/25)" note) is not a summary either.
        if len(flat) < 40:
            continue
        return flat
    return ""


def truncate(text, limit=TARGET_LENGTH):
    """Cut `text` to `limit` characters on a sentence or word boundary."""
    text = text.strip()
    if len(text) <= limit:
        return text
    window = text[: limit + 1]
    # Prefer ending on a sentence if one finishes reasonably late in the window.
    sentence = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if sentence >= limit * 0.6:
        return window[: sentence + 1].strip()
    space = window.rfind(" ")
    return (window[:space] if space > 0 else window[:limit]).rstrip(" ,;:-") + "..."


def subtitle_of(frontmatter):
    """The post's `subtitle:` value, unquoted, or ''."""
    match = SUBTITLE_RE.search(frontmatter)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value.strip()


def build_description(frontmatter, body):
    """Compose a description from the subtitle and the opening prose."""
    subtitle = flatten(subtitle_of(frontmatter))
    prose = first_prose(body)

    if subtitle and len(subtitle) >= TOPUP_BELOW:
        return truncate(subtitle)
    if subtitle and prose:
        # Some posts open by restating their own subtitle; don't say it twice.
        if prose.lower().startswith(subtitle.lower().rstrip(".!?")):
            return truncate(prose)
        # Subtitle first — it is the author's own summary — then as much of the
        # opening paragraph as fits.
        joined = subtitle.rstrip(".!?") + ". " + prose
        return truncate(joined)
    return truncate(subtitle or prose)


def rewrite_frontmatter(frontmatter, description):
    """Return `frontmatter` with its `description:` set, leaving the rest alone.

    No YAML round-trip, so key order, comments and quoting style survive.
    """
    stripped = DESCRIPTION_RE.sub("", frontmatter)
    if not description:
        return stripped
    if stripped and not stripped.endswith("\n"):
        stripped += "\n"
    # json.dumps gives a correctly escaped YAML double-quoted scalar.
    return stripped + "description: " + json.dumps(description, ensure_ascii=False) + "\n"


def process(path, args):
    """Compute and (optionally) write one post's description."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {"path": path, "skipped": "no frontmatter"}

    frontmatter = match.group(1)
    had = DESCRIPTION_RE.search(frontmatter) is not None
    if had and not args.force:
        return {"path": path, "skipped": "already has description", "had": True}

    description = build_description(frontmatter, strip_frontmatter(text))
    if not description:
        return {"path": path, "skipped": "nothing usable to summarise", "had": had}

    new_frontmatter = rewrite_frontmatter(frontmatter, description)
    changed = new_frontmatter != frontmatter
    if changed and args.write:
        path.write_text(
            text[: match.start(1)] + new_frontmatter + text[match.end(1):],
            encoding="utf-8",
        )

    return {"path": path, "description": description, "changed": changed, "had": had}


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", nargs="*", help="posts or directories (default: _posts)")
    parser.add_argument("--write", action="store_true",
                        help="edit the frontmatter; without this it is a dry run")
    parser.add_argument("--force", action="store_true",
                        help="also regenerate descriptions that already exist")
    parser.add_argument("--short", type=int, default=0, metavar="N",
                        help="only report descriptions shorter than N characters")
    args = parser.parse_args(argv)

    repo = Path(__file__).resolve().parent.parent
    roots = [Path(p) for p in args.paths] or [repo / "_posts"]

    posts = []
    for root in roots:
        posts.extend(sorted(root.rglob("*.md")) if root.is_dir() else [root])

    written = skipped = 0
    short = []
    for result in (process(p, args) for p in posts):
        rel = result["path"].relative_to(repo) if result["path"].is_relative_to(repo) else result["path"]
        if "skipped" in result:
            skipped += 1
            if result["skipped"] != "already has description":
                print(f"  SKIP  {rel}  ({result['skipped']})")
            continue
        if result["changed"]:
            written += 1
        description = result["description"]
        if len(description) < 70:
            short.append((rel, description))
        if not args.short or len(description) < args.short:
            print(f"{len(description):4}  {rel}\n      {description}")

    verb = "wrote" if args.write else "would write"
    print(f"\n{verb} {written} descriptions, skipped {skipped}.")
    if short:
        print(f"\n{len(short)} are under 70 characters and worth writing by hand:")
        for rel, description in short:
            print(f"  {rel}\n    {description}")
    if not args.write and written:
        print("Dry run — re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
