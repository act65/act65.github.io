#!/usr/bin/env python3
"""The single source of truth for every post's `tags:` key.

Tags run on four facets. A post gets one FORM tag, any number of MODE, THEME and
COLLECTION tags, and one or more SUBJECT tags.

  FORM        what kind of thing the post is
  MODE        how it is done — does it derive, cite data, lean on history, admit
              it is unfinished
  THEME       the preoccupations that recur across the blog regardless of subject
  SUBJECT     what it is about
  COLLECTION  small hand-picked groupings that no facet captures

The script rewrites the tags block of every post from the table below and nothing
else, so it is idempotent and the table is the only place to edit.

    python3 scripts/tag_posts.py            # dry run + facet counts
    python3 scripts/tag_posts.py --write    # apply
    python3 scripts/tag_posts.py --stats    # co-occurrence report
"""
import glob
import os
import re
import sys
from collections import Counter, defaultdict

FORM = {"tutorial", "essay", "research", "proposal", "notes", "fiction",
        "story-prompt", "personal", "lyrics", "game"}
MODE = {"formalised", "data", "historical", "speculation", "open-question",
        "sketch", "wip"}
THEME = {"measurement", "incentives", "aggregation", "uncertainty", "rights",
         "power", "luck", "coordination", "trust", "introspection",
         "abstraction", "alignment", "inequality"}
SUBJECT = {"machine-learning", "reinforcement-learning", "probability",
           "information-theory", "mathematics", "computation", "physics",
           "biology", "chemistry", "economics", "finance", "politics",
           "mechanism-design", "ai-safety", "philosophy", "ethics",
           "epistemology", "environment", "society", "technology", "music",
           "travel", "new-zealand", "meta"}
COLLECTION = {"built", "historical-fiction", "curiosity"}
VOCAB = FORM | MODE | THEME | SUBJECT | COLLECTION

TAGS = {
 # ---------------------------------------------------------------- fiction --
 "alien-treaty": "fiction historical power rights trust politics new-zealand society historical-fiction",
 "cargo": "fiction historical power trust society economics historical-fiction",
 "math-origins": "fiction historical measurement abstraction power mathematics historical-fiction",
 "brand-new-world": "fiction incentives power economics society",
 "outsourced": "fiction trust incentives technology society",
 "fusion-pollution": "story-prompt sketch environment physics",
 "humanitys-legacy": "story-prompt sketch environment",
 "white-mars": "story-prompt sketch society biology",
 "howard": "fiction coordination ethics society",
 "julian": "fiction luck ethics philosophy",
 "lyra": "fiction music ethics",
 "story-utility": "essay introspection philosophy meta",
 # ------------------------------------------------- governance mechanisms --
 "framework": "essay uncertainty rights power aggregation mechanism-design politics philosophy",
 "why-care": "essay historical data power coordination mechanism-design politics society",
 "human-nature": "essay historical uncertainty power mechanism-design philosophy",
 "agency-definition": "research formalised rights aggregation uncertainty mechanism-design philosophy",
 "minimality": "research formalised uncertainty rights mechanism-design probability",
 "voting-geom": "research formalised aggregation abstraction rights mechanism-design mathematics politics information-theory",
 "ballot-design": "research formalised aggregation measurement mechanism-design mathematics politics",
 # ------------------------------------------------------------ built ------
 "tvs": "game computation machine-learning built",
 "rain": "proposal trust incentives coordination mechanism-design economics technology built",
 "scorecards": "essay data measurement power politics new-zealand mechanism-design built",
 "chords-are-shapes": "essay abstraction music mathematics built curiosity",
 "enumerating-graphs": "tutorial formalised abstraction mathematics computation built curiosity",
 # ------------------------------------------------------------- essays ----
 "freedom-adjusted-life-years": "proposal formalised data measurement rights inequality ethics mechanism-design politics",
 "capitalism-core": "essay power incentives economics philosophy",
 "ea-to-ai": "essay measurement alignment ethics ai-safety",
 "a-guide-to-regulation": "essay sketch measurement incentives economics mechanism-design",
 "regulating-markets-to-remove-inefficiencies": "essay sketch data incentives measurement economics mechanism-design",
 "adversarial-tax-setting": "proposal incentives power economics mechanism-design machine-learning",
 "capitalism-solves-capitalism": "essay incentives power economics mechanism-design",
 "efficient-markets": "essay formalised aggregation uncertainty economics probability",
 "attention": "essay data measurement power economics society",
 "iffs": "essay data power trust inequality finance politics society",
 "reputation-for-rohingya": "essay trust coordination inequality economics technology society",
 "a-tripping-point": "essay sketch data formalised measurement economics society",
 "ubi": "essay sketch inequality economics politics technology",
 "affirm-ml": "essay formalised data measurement inequality rights society ethics machine-learning",
 "life-as-a-minority": "essay sketch luck inequality rights society ethics",
 "karma-and-merit-they-deserve-it": "essay sketch luck inequality ethics society",
 "luck-morality": "essay luck inequality ethics philosophy",
 "poker-eval": "essay formalised luck measurement probability ethics",
 "determinism": "essay luck philosophy epistemology",
 "humble": "essay sketch introspection epistemology philosophy",
 "what-makes-something-true": "essay epistemology mathematics",
 "proving-anthopogenic-global-warming": "essay trust epistemology environment",
 "market-politics": "proposal aggregation incentives mechanism-design epistemology politics",
 "sct": "research formalised aggregation mechanism-design probability politics",
 "conserve-v-progress": "essay uncertainty politics philosophy machine-learning",
 "entropism": "essay speculation philosophy physics",
 "alignment": "essay alignment incentives power ai-safety economics",
 "agi-game": "essay formalised coordination alignment incentives ai-safety economics politics",
 "align-dao": "proposal formalised aggregation alignment incentives mechanism-design ai-safety economics",
 "measuring-people": "essay sketch speculation measurement society technology",
 "policy-search-engine": "proposal sketch speculation measurement politics technology",
 "the-future-of-environmental-sciences": "essay sketch speculation measurement environment technology",
 "palm-oil-in-nzs-dairy": "essay sketch data environment economics new-zealand",
 "divest-milk-and-the-nz-economy": "essay sketch economics new-zealand environment",
 "nz26": "essay sketch data politics new-zealand",
 "notes-principles-of-neural-design": "notes abstraction biology computation",
 # ----------------------------------------------------------- personal ----
 "why-write": "personal sketch introspection meta",
 "telling-myself-stories": "personal sketch introspection meta",
 "letter-from-my-future-self-a-failure": "personal sketch introspection meta",
 "future-smarter-telf": "personal sketch speculation introspection meta technology",
 "grassy-dreams": "personal sketch introspection meta",
 "needing-purpose": "personal sketch introspection ethics",
 "open-minded-a-game": "personal sketch introspection meta epistemology",
 "adversarial-collaboration-contest": "personal sketch introspection meta epistemology",
 "right-beliefs-wrong-reasons": "personal sketch introspection epistemology",
 "my-childhood-struggles-with-the-truth": "personal introspection epistemology",
 "people-are-shit": "personal sketch ethics society",
 "dope-i-am-addicted": "personal sketch biology ethics",
 "hosting-on-airbnb": "personal society",
 "igem-2019": "personal biology chemistry",
 "neuro-inspired-computation-course": "personal travel biology computation",
 "acl2018": "notes introspection machine-learning",
 "covering-letter-for-my-first-phd-proposal": "personal introspection machine-learning meta",
 "meditation-retreat": "personal introspection travel",
 "first-few-days-in-india-absolutely-pooped": "personal sketch travel",
 "the-house-of-hope": "personal inequality luck travel society",
 "nelson-lakes-abel-tasman-and-golden-bay": "personal sketch travel new-zealand",
 "hate": "lyrics music ethics",
 "all-along": "lyrics music",
 # --------------------------------------------------------- rationality ---
 "approximate-reasoning": "essay formalised abstraction uncertainty probability computation epistemology",
 "bayes-optimal": "tutorial formalised uncertainty probability information-theory",
 "uncertainty-via-bets": "tutorial formalised uncertainty probability philosophy",
 "discounting-via-uncertainty": "research formalised uncertainty reinforcement-learning probability",
 "arms-fidelities-delays": "research formalised uncertainty measurement reinforcement-learning probability",
 "modern-ml-prob-utils": "notes formalised uncertainty probability machine-learning",
 # ----------------------------------------------------------- technical ---
 "embedded-linalg": "tutorial formalised abstraction mathematics computation curiosity",
 "engima": "tutorial formalised computation mathematics curiosity",
 "mean": "tutorial formalised measurement mathematics curiosity",
 "typicality": "tutorial formalised probability information-theory curiosity",
 "stoch-calc": "tutorial formalised mathematics probability",
 "causal-calculus": "tutorial formalised probability mathematics",
 "scoredd": "tutorial formalised machine-learning probability",
 "bbb-ids": "tutorial formalised uncertainty reinforcement-learning probability",
 "deeplearning": "tutorial sketch machine-learning",
 "saddle-splitter": "research formalised abstraction machine-learning mathematics",
 "neural-si": "research wip sketch machine-learning mathematics",
 "aligning-datasets": "research formalised abstraction probability mathematics",
 "graph-uncert": "research formalised uncertainty probability mathematics",
 "real-time-RL": "research formalised open-question uncertainty reinforcement-learning",
 "backwards-with-benefits": "research sketch open-question abstraction reinforcement-learning computation",
 "conserved-complexity": "research sketch speculation open-question abstraction computation information-theory",
 "reward-hijacking": "research formalised alignment incentives reinforcement-learning ai-safety",
 "necessary-robust-rl": "essay formalised alignment uncertainty ai-safety reinforcement-learning",
 "intelligent-immune": "essay speculation abstraction biology computation",
 "the-fable-of-the-caterpillar": "tutorial abstraction reinforcement-learning",
 "automated-science": "proposal abstraction machine-learning reinforcement-learning epistemology",
 "unsupervised-laddernet": "proposal sketch open-question abstraction machine-learning",
 "fat": "proposal sketch open-question abstraction machine-learning mathematics",
 "autoint": "proposal wip sketch open-question mathematics computation",
 "lm-chem": "proposal machine-learning chemistry",
 "inference-via-interference": "proposal sketch speculation open-question biology computation",
 "pilot-waves-proposal": "proposal speculation open-question physics",
 "requests-for-research": "notes open-question machine-learning",
}
TAGS = {k: v.split() for k, v in TAGS.items()}

files = sorted(glob.glob("_posts/**/*.md", recursive=True))
slugs = {re.sub(r"^\d{4}-\d{1,2}-\d{1,2}-", "", os.path.basename(f)[:-3]): f for f in files}

errs = []
for label, xs in [
    ("untagged posts", sorted(set(slugs) - set(TAGS))),
    ("slugs matching no post", sorted(set(TAGS) - set(slugs))),
    ("tags outside the vocabulary", sorted({t for ts in TAGS.values() for t in ts} - VOCAB)),
    ("posts without exactly one FORM tag", sorted(s for s, ts in TAGS.items() if len(FORM & set(ts)) != 1)),
    ("posts with no SUBJECT tag", sorted(s for s, ts in TAGS.items() if not SUBJECT & set(ts))),
]:
    if xs:
        errs.append(f"{label}: {xs}")
if errs:
    print("\n".join(errs), file=sys.stderr)
    sys.exit(1)

write = "--write" in sys.argv
changed = 0
for slug, path in slugs.items():
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        print(f"no frontmatter: {path}", file=sys.stderr)
        continue
    fm = m.group(1)
    tm = re.search(r"^tags:\n((?:  - .+\n?)*)", fm, re.M)
    have = [l.strip()[2:] for l in tm.group(1).splitlines() if l.strip()] if tm else []
    if have == TAGS[slug]:
        continue
    changed += 1
    block = "tags:\n" + "".join(f"  - {t}\n" for t in TAGS[slug])
    new_fm = (fm[:tm.start()] + block.rstrip("\n") + fm[tm.end():].rstrip("\n")) if tm \
        else fm.rstrip("\n") + "\n" + block.rstrip("\n")
    if write:
        open(path, "w", encoding="utf-8").write(f"---\n{new_fm}\n---\n" + txt[m.end():])

counts = Counter(t for ts in TAGS.values() for t in ts)
print(f"{'WROTE' if write else 'DRY RUN'}: {len(TAGS)} posts, {changed} changed, "
      f"{sum(counts.values())} tag applications, "
      f"{sum(counts.values())/len(TAGS):.1f} per post\n")
for facet, name in [(FORM, "FORM"), (MODE, "MODE"), (THEME, "THEME"),
                    (COLLECTION, "COLLECTION"), (SUBJECT, "SUBJECT")]:
    print(f"-- {name}")
    for t, c in sorted(((t, c) for t, c in counts.items() if t in facet), key=lambda x: -x[1]):
        print(f"   {c:4d}  {t}")
    missing = sorted(facet - set(counts))
    if missing:
        print(f"   (unused: {', '.join(missing)})")
    print()

if "--stats" in sys.argv:
    n = len(TAGS)
    pair = Counter()
    for ts in TAGS.values():
        s = sorted(set(ts))
        for i, a in enumerate(s):
            for b in s[i + 1:]:
                pair[(a, b)] += 1
    print("-- pairs that travel together (lift = P(a,b) / P(a)P(b), min 4 posts)")
    scored = []
    for (a, b), c in pair.items():
        if c < 4:
            continue
        lift = (c / n) / ((counts[a] / n) * (counts[b] / n))
        scored.append((lift, c, a, b))
    for lift, c, a, b in sorted(scored, reverse=True)[:30]:
        print(f"   {c:3d} posts  lift {lift:5.2f}   {a} + {b}")
