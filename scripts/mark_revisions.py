#!/usr/bin/env python3
"""Label posts with the dates of their significant revisions, from git history.

Reads the git history of every post, groups nearby commits into editing
"bursts" (a weekend of fiddling is one revision, not nine), throws away the
burst that created the post and every burst too small to matter, and writes
what survives into the post's frontmatter:

    revisions:
      - "2026-03-02"
      - "2026-06-11"

`_layouts/post.html` renders that list under the publication date. Posts with
no significant revision get the key removed, so re-running is idempotent.

Usage:
    python3 scripts/mark_revisions.py                 # dry run, show the diff
    python3 scripts/mark_revisions.py --write         # actually edit frontmatter
    python3 scripts/mark_revisions.py --report        # per-post burst breakdown
    python3 scripts/mark_revisions.py --min-churn 20 --write

Churn is measured in changed lines (added + deleted). Posts here are written
one-paragraph-per-line, so a typo fix is churn 2 and a reworked section is
churn 20+ — the thresholds below are tuned for that. Bump --min-churn if too
much noise gets through.
"""

import argparse
import re
import subprocess
import sys
from collections import namedtuple
from datetime import date, timedelta
from pathlib import Path

Commit = namedtuple("Commit", "sha day added deleted")
Burst = namedtuple("Burst", "start end commits added deleted size_before")

# A post's frontmatter block: --- ... --- at the very top of the file.
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?\r?\n)---[ \t]*\r?\n", re.DOTALL)
# An existing `revisions:` block (the key plus its indented `- ...` items).
REVISIONS_RE = re.compile(r"^revisions:[ \t]*\r?\n(?:[ \t]+-[^\r\n]*\r?\n)*", re.MULTILINE)
# The date at the front of a post filename, e.g. 2025-07-24-agi-game.md
FILENAME_DATE_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2})-")
# A `date:` key in frontmatter, e.g. date: 2025-07-24 10:00:00
FM_DATE_RE = re.compile(r"^date:[ \t]*(\d{4})-(\d{1,2})-(\d{1,2})", re.MULTILINE)


def git(args, repo):
    """Run a git command in `repo` and return its stdout."""
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def history(path, repo):
    """Commits that changed `path`, oldest first, following renames.

    Pure renames (0 added, 0 deleted) and merge commits are dropped — they
    move a post around without saying anything new.
    """
    out = git(
        [
            "log",
            "--follow",
            "--numstat",
            "--date=short",
            "--pretty=format:\x01%H\x01%ad",
            "--",
            str(path),
        ],
        repo,
    )

    commits = []
    sha = day = None
    for line in out.splitlines():
        if line.startswith("\x01"):
            _, sha, iso = line.split("\x01")
            day = date.fromisoformat(iso)
            continue
        parts = line.split("\t")
        if len(parts) != 3 or sha is None:
            continue
        added, deleted = parts[0], parts[1]
        if added == "-" or deleted == "-":  # binary file
            continue
        added, deleted = int(added), int(deleted)
        if added == 0 and deleted == 0:  # pure rename
            continue
        commits.append(Commit(sha, day, added, deleted))

    commits.reverse()  # git log is newest-first; we want chronological
    return commits


def to_bursts(commits, gap_days):
    """Group commits separated by less than `gap_days` into single revisions.

    Also tracks the post's line count going into each burst, so that "20 lines
    changed" can be judged against how long the post was at the time.
    """
    bursts = []
    size = 0  # running line count of the file
    for commit in commits:
        if bursts and (commit.day - bursts[-1].end) <= timedelta(days=gap_days):
            last = bursts[-1]
            bursts[-1] = last._replace(
                end=commit.day,
                commits=last.commits + 1,
                added=last.added + commit.added,
                deleted=last.deleted + commit.deleted,
            )
        else:
            bursts.append(Burst(commit.day, commit.day, 1, commit.added, commit.deleted, size))
        size += commit.added - commit.deleted
    return bursts


def churn(burst):
    return burst.added + burst.deleted


def fraction(burst):
    """Churn as a share of the post's length going into the burst."""
    return churn(burst) / max(burst.size_before, 1)


def published_on(path, frontmatter):
    """The post's own date: frontmatter `date:` if present, else the filename."""
    match = FM_DATE_RE.search(frontmatter)
    if not match:
        match = FILENAME_DATE_RE.match(path.name)
    if not match:
        return None
    year, month, day = (int(g) for g in match.groups())
    try:
        return date(year, month, day)
    except ValueError:
        # e.g. 2025-09-31-capitalism-core.md — Jekyll tolerates it, so do we.
        return date(year, month, 1)


def milestones(bursts, published, args):
    """The bursts worth showing: post-publication, and big enough to notice.

    The first burst is always dropped — that's the post being written. So is
    anything at or before the publication date, which catches drafting commits
    and the bulk wordpress migration.
    """
    picked = []
    for index, burst in enumerate(bursts):
        if index == 0:
            continue
        if published and burst.end <= published:
            continue
        if churn(burst) < args.min_churn:
            continue
        if fraction(burst) < args.min_fraction:
            continue
        picked.append(burst)
    return picked


def rewrite_frontmatter(frontmatter, days):
    """Return `frontmatter` with its `revisions:` block set to `days`.

    Everything else is left byte-for-byte alone — no YAML round-trip, so
    comments, key order and quoting style survive.
    """
    stripped = REVISIONS_RE.sub("", frontmatter)
    if not days:
        return stripped
    block = "revisions:\n" + "".join(f'  - "{d.isoformat()}"\n' for d in days)
    if stripped and not stripped.endswith("\n"):
        stripped += "\n"
    return stripped + block


def process(path, repo, args):
    """Compute and (optionally) write one post's revisions. Returns a summary."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {"path": path, "skipped": "no frontmatter"}

    frontmatter = match.group(1)
    published = published_on(path, frontmatter)
    bursts = to_bursts(history(path.relative_to(repo), repo), args.gap_days)
    picked = milestones(bursts, published, args)
    days = [b.end for b in picked]

    new_frontmatter = rewrite_frontmatter(frontmatter, days)
    changed = new_frontmatter != frontmatter
    if changed and args.write:
        path.write_text(
            text[: match.start(1)] + new_frontmatter + text[match.end(1) :],
            encoding="utf-8",
        )

    return {
        "path": path,
        "published": published,
        "bursts": bursts,
        "picked": picked,
        "days": days,
        "changed": changed,
        "had": REVISIONS_RE.search(frontmatter) is not None,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=None,
                        help="posts or directories to process (default: _posts)")
    parser.add_argument("--write", action="store_true",
                        help="edit the frontmatter; without this it is a dry run")
    parser.add_argument("--report", action="store_true",
                        help="show every burst, including the ones rejected")
    parser.add_argument("--gap-days", type=int, default=14, metavar="N",
                        help="commits within N days are one revision (default: 14)")
    parser.add_argument("--min-churn", type=int, default=20, metavar="N",
                        help="a revision must change at least N lines (default: 20)")
    parser.add_argument("--min-fraction", type=float, default=0.20, metavar="F",
                        help="...and at least this share of the post (default: 0.20)")
    args = parser.parse_args(argv)

    repo = Path(git(["rev-parse", "--show-toplevel"], Path.cwd()).strip())

    roots = [Path(p).resolve() for p in args.paths] if args.paths else [repo / "_posts"]
    posts = []
    for root in roots:
        posts.extend(sorted(root.rglob("*.md")) if root.is_dir() else [root])

    dirty = {
        line[3:].strip()
        for line in git(["status", "--porcelain", "--", "_posts"], repo).splitlines()
    }

    labelled = cleared = 0
    for post in posts:
        info = process(post, repo, args)
        rel = info["path"].relative_to(repo)

        if info.get("skipped"):
            print(f"  skip  {rel}  ({info['skipped']})")
            continue

        if args.report:
            print(f"\n{rel}  published {info['published']}")
            for index, burst in enumerate(info["bursts"]):
                span = str(burst.end) if burst.start == burst.end else f"{burst.start}..{burst.end}"
                mark = "*" if burst in info["picked"] else " "
                reason = "created" if index == 0 else ""
                print(f"  {mark} {span:>24}  {burst.commits:>2} commits  "
                      f"+{burst.added}/-{burst.deleted}  "
                      f"{fraction(burst):.0%} of post  {reason}")
        elif info["changed"] and info["days"]:
            verb = "labelled" if args.write else "would label"
            print(f"  {verb}  {rel}  {', '.join(str(d) for d in info['days'])}")
        elif info["changed"]:
            verb = "cleared" if args.write else "would clear"
            print(f"  {verb}  {rel}")

        if info["days"]:
            labelled += 1
        if info["changed"] and not info["days"]:
            cleared += 1

    print(f"\n{len(posts)} posts, {labelled} with revisions"
          + (f", {cleared} cleared" if cleared else ""))
    if not args.write:
        print("dry run — pass --write to apply")

    if dirty:
        print(f"\nnote: {len(dirty)} post(s) have uncommitted changes; "
              "today's edits won't appear until they are committed:")
        for path in sorted(dirty):
            print(f"  {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
