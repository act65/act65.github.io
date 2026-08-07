# Changelog — corrections to "What Makes a Good Politician?"

Applied 2026-08-07 against `notes/review-scorecards.md`.
Files edited:

- `_posts/inbetween-posts/2026-08-01-scorecards.md` (this repo)
- `~/Documents/repos/pol-score-cards/site/templates/about.html`
- `~/Documents/repos/pol-score-cards/attribute-extraction/bias_adjust.py` (docstring only)
- `~/Documents/repos/pol-score-cards/attribute-extraction/build_v2_dataset.py` + the three
  `attributes.jsonl` copies + `site/static/manifest.json` (Divination definition; see item 3)

`bundle exec jekyll build` passes clean (only the pre-existing Sass `@import` deprecation
warnings). Front matter, the inline-SVG attribute list, and every existing link are untouched.

---

## Correction policy

CLAUDE.md documents no convention for corrections to published posts, and no existing post in
`_posts/` carries one. I chose **visible correction**: a dated `**Corrections, 7 August 2026**`
block at the end of the post, after the "Have a look" line, listing the substantive factual
changes and linking to the two sections that were rewritten. It leads with the Willie Jackson
removal and includes an apology. The opening of the post is left intact so the piece still reads
as written. **Author decision needed:** if you'd rather this convention live somewhere else (a
`corrections:` front-matter key, an `_includes/correction.html`), it is one block to move.

---

## Tier 5, item 20 — the Willie Jackson veracity example (done first)

**Cut.** Agreed with the review entirely, and the repo backs it: `examples.jsonl` scores the
isolated string `"Fifty percent of Māori are in jails at the moment"` at 10 with the explanation
"Demonstrably false as stated", and the surrounding Hansard sentences are about Corrections and
Māori disparity. Word-order slip, ungrounded attribute, named person, published under a
**Veracity — 10/100** heading. Removed.

**Replacement found and used.** Shane Jones, Hansard 2025-02-11, Veracity **5/100**:

> "I may make a few remarks about a dolphin that doesn't exist, otherwise known as the Māui
> dolphin. It was a contrivance, a fiction, put together by some underemployed academic down in
> the South Island."

Why this one clears the bar the Jackson example failed:

- It is the **lowest veracity score in the whole dataset** (verified: only two examples score 5;
  this is one of them), so it genuinely is "the clearest illustration I could find".
- It is not a disfluency. He states the claim and then builds a second sentence elaborating it
  ("a contrivance, a fiction, put together by…"). There is no reading on which it is a slip.
- The underlying fact requires no fact-checking corpus — the Māui dolphin is a described,
  recognised subspecies of Hector's dolphin. This is the one class of veracity claim the ungrounded
  attribute can actually be trusted on, and I say so in the post rather than leaving it implied.
- It is a widely reported public statement, not a private or incidental remark.

I also added the plausibility-vs-truth caveat **inline, immediately under the example**, rather
than leaving it eighty lines away in "What it isn't" — that was the structural half of item 20.

---

## Tier 1

**1. Synthetic test sets.** The "What it isn't" validation paragraph is rewritten on the review's
suggested wording. It now names the test sets as invented American council-meeting speech, keeps
the r = 0.88 / r = 0.73 figures but states plainly they measure a different task, and adds the
single-labeller / no-inter-rater point and the known prompt-leakage caveat. Also added a **two-line
version immediately after the first big number** in "Nobody passes" (this was the last Tier 6
bullet) so a reader who stops at the headline still sees it. Listed in the corrections block.

**2. Shrinkage.** Three changes. "The number is just the mean of the evidence" → "a *shrunk*
average… thin evidence gets pulled toward the population middle on purpose". The "averaging
compresses toward the middle" caveat is replaced with the correct diagnosis and the raw figures
(34 raw ≥ 80, 5 of them on n ≥ 10, Garcia and Fleming at 86 raw over 13 statements). Recomputed
and confirmed — see "Figures I recomputed" below.

**3. Divination.** Attribute-list definition changed to "are their predictions specific enough to
be checked, and plausible on the evidence at the time?". Added the inertness finding (43–54 across
126 cards) and the "shouldn't be in the geometric mean until it's grounded" line to "What it
isn't". **I partly disagreed with the review on the Webb example — see "Where I disagreed" below**
— so it is reframed rather than cut, and the reframing is stronger than the review's version.

**4. Double-counting.** Now "45,477 statements scored 94,429 times — most statements bear on more
than one attribute". **Note: 45,477, not the review's 45,450.** The review's own per-attribute
breakdown sums to 45,477; see "Where I disagreed".

**5. 204 sitting days.** → "190 sitting days of the current Parliament". Confirmed both ways:
`HANSARD_COVERAGE.md` splits 204 into 14 (53rd) + 190 (54th), and the shipped `examples.jsonl` has
exactly 190 distinct Hansard URLs. The ~7.5M words figure is left as-is —
`dataset_stats.json` gives `corpus.approx_words = 7,500,644`.

**6. 135 / 130.** The closing line is now "not one of the 135 people who have sat in this
Parliament". The "site has all 135 cards" line is now "130 cards on the front page (every MP with
at least six of the nine attributes scored)" — `app.py:105` sets `MIN_ATTRIBUTES = 6`, and 130
verified from the data. The data paragraph now says "135 MPs who have sat in this Parliament".

**7. "Seven ways to fail" wrap-up.** Rewritten. Charisma now leads, framed as a near-duplicate of
Civility (r = 0.96 at statement level, plus the prompt's own "crowd-pleasing attacks on opponents
are not charisma — score them low"). Strength follows with the attribution bug. Both multipliers
now given separately: Authenticity 9.8% vs 2.4% = **4.1×**, Strength 4.7% vs 0.6% = **7.8×**. The
volunteered-bug instinct is preserved intact, as instructed.

**8. "An hour before the second."** Removed — `examples.jsonl` carries dates only, both Court
quotes stamped `2026-03-31` with no ordering. Now "in the same debate, to the same person". Also
fixed a second instance in the same passage: "to the same colleague" → "to the same member"
(Tamatha Paul is Green, Court is ACT — same error as item 21's Seymour line).

---

## Tier 2

**9. Attribute non-independence.** New paragraph opening "Where the failures cluster", with the
verified statement-level correlations (Civility~Charisma 0.96, Civility~Rigor 0.85,
Rigor~Charisma 0.84) and the prompt evidence that all three penalise the personal attack. Ends on
the review's line: "Whatever the bottom of the table is measuring, it is measuring it about three
times." This is then load-bearing for the party-tails paragraph (item 17b) and the Charisma
explanation (item 7), so it earns its place three times over.

**10. Rubric midpoint.** New closing paragraph in "Nobody passes" owning that "pass mark is 100"
is the author's framing and not the rubric's — quotes civility's own 0.5 anchor ("harsh but
legitimate criticism of policies, ideas, or actions"), notes the 0.9 exemplar cap, concedes the
critic's reading, and keeps the distribution tail as the surviving finding.

**11. The LLM chooses what to score.** "score each one" → "have an LLM pull out the ones that bear
on an attribute and score each". The "It's roughly the base rate" claim is replaced with the
review's wording, including the absolute framing (~1,115 insults / 190 sitting days ≈ six a day —
recomputed, see below).

**12. Verbatim slips.** New paragraph in "What it isn't" on Hansard being lightly-edited spoken
language and a statement-level scorer reading inversions literally, ending on why the
evidence-linking design is the mitigation. This is the general lesson of item 20, and putting it
in the post is better than silently dropping the example.

---

## Tier 3

**13–15.** New section, **"The comparison isn't fair yet"**, placed after "Where the failures
cluster" as the review suggested. Three subheads, all figures verified from the shipped data:

- source gaps (Forthrightness +17.6, Specificity −9.3, Civility −7.2, Rigor −6.1) against the
  21.5-point league-table span; source mix by party (ACT 45% releases vs NZ First 17%,
  National 18%); pressers effectively government-only (5,269 National, 126 NZ First, 24 ACT, zero
  Labour / Green / Te Pāti Māori); and the explicit admission that the Hansard-only mitigation
  stopped applying when 23,935 press-release statements were added
- Forthrightness as a minister-only measure (104 of 135 MPs have one; largest source gap of the
  nine)
- Specificity / Strength / Divination favouring the executive, citing the repo's own `VOTES.md`
  delivery-scope-gate note

The section closes without over-conceding: the distribution finding survives, but the difference
between 110th and 120th does not.

**16. r = −0.25 confounded.** Rewritten on the review's wording — negative correlation, the
estimator's contribution, weakening to about −0.10 among the 21 most-covered MPs, and the blunter
fact (top-20 mean rank 86.85) kept.

---

## Tier 4

**17. The framing claim.** (a) New qualification in "The one standard we can all agree on" owning
that the rubric has a house style — rewards figures, mechanisms, named policies; marks down
hyperbole — which is a preference for the technocratic voice over the moral or oratorical, and
saying it is defensible but chosen. (b) New paragraph in "Where the failures cluster" showing the
party tails (top 20: 11 Labour, 5 National; bottom 20: 5 National, 4 TPM, 3 each Green/ACT/NZ
First, 2 Labour; TPM 4 of 7 in the bottom 20, none in the top), and attributing the pattern to
rhetorical register plus the triple-counting from item 9, explicitly not to honesty.

**18. "Answer the question" is not uncontested.** Added: NZ Standing Orders require a Minister to
*address* the question, not answer it; the Speaker rules on the distinction regularly; scoring
forthrightness holds MPs to a stricter standard than the House does.

---

## Tier 5 (remaining)

**19. Rank precision.** "The bottom of the table is the leadership" rewritten on the review's
version. Peters (44.5), Jones (44.6) and Waititi (48.1) are named as clearly below the pack; the
individual ranks of Davidson, Luxon, Seymour and Ngarewa-Packer are **removed** and replaced with
the band description (25 places inside 3.1 points, against a median per-attribute CI of ±4).
Hipkins (82nd) and Swarbrick (89th) are kept as ranks because they're far enough from the pack to
survive, and because the point being made is "bottom half", not a precise place.

**21a. Peters press release.** Added "Not in the House, this one — a party press release, where
nobody is arguing back."

**21b. "Colleague".** → "another member", in the opening line. Same fix applied to the Simon Court
passage (see item 8).

**21c. Asymmetric citation.** Bishop, Walters and Andersen now carry Hansard links and their
scores, matching the criticism examples. All three verified in `examples.jsonl`: Bishop Civility 95
(2025-04-08), Walters 90 (2025-08-21), Andersen 90 (2025-08-21). I swapped the Andersen paraphrase
for her verbatim quote so it can actually be checked against the link.

---

## Tier 6 — structure

- **Caption vs "top-ranked card".** Fixed by explaining the bug rather than hiding it. The caption
  now says cards rank on the geometric mean of *whatever subset was scored*, gives the medians
  (8 attributes → 45th, 9 → 71st), and says that's why Rurawhe is shown rather than the actual
  number-one card. Verified: Walters is 1st on 8 attributes, Salesa 2nd on 8, Rurawhe 3rd and the
  highest card with all nine.
- **The long opening.** Trimmed rather than cut 40%. The Burke *block quote* is gone (the review
  says it does least work) but the what/how distinction and the "reason and judgment" idea survive,
  now folded into one sentence. "They represent you" and "How do you want your side to win?" are
  untouched, as instructed. Net: the run-up to the first data is ~4 lines shorter, offset by the
  two new qualifications in item 17/18 — so the section is *not* 40% shorter, deliberately. See
  "Outstanding" below.
- **"Here is the entire result"** → "here is the headline".
- **Nine-attribute list.** No table — restructuring would have meant dropping the inline SVGs,
  which the constraints protect. Instead a short prose paragraph after the list sorts the nine into
  *judged from the text alone* (Forthrightness, Civility, Rigor, Specificity, Charisma), *needs an
  external record the pipeline doesn't consult* (Veracity, Strength, Authenticity), and *not
  grounded at all* (Divination). This does the retiring-later-hedging job the review wanted.
- **"What it isn't" placement.** Left where it is, but the two-line version now appears right after
  the first big number (see item 1).

---

## The live site

`site/templates/about.html` — the Methodology section's stale sentence ("We hold out a small
labelled test set and measure how well the model's scores agree with human judgement") is replaced
with a new **"How well does it work? We don't know yet."** section that:

1. states plainly that the scoring is not currently validated, and why (invented statements,
   fictional politicians, no NZ speaker, n = 14, one labeller)
2. gives the grounding split across the nine attributes
3. names the two known defects affecting live data — the Strength/Authenticity subject-attribution
   bug, and the source-mix confound

**Other user-facing copy checked.** I grepped `site/templates/*.html` for validation language
(`hold out`, `test set`, `human judg`, `correlat`, `accura`, `validat`, `reliab`). Nothing else
carries the claim. The footer's "Prototype… not verified fact" line was already correct and is
untouched.

**One further stale claim found, not in the review.** The shipped `attributes.jsonl` — which
renders on the about page, the cards, and every attribute detail page — defined Divination as
*"How often the politician's predictions about future events have proven accurate."* That is the
same claim as review item 3, live on the site, and directly contradicted by `divination.txt`'s own
grounding caveat. Changed to *"Whether the politician's predictions are specific enough to be
checked, and plausible on the evidence at the time. Not yet grounded against outcomes."* Updated in
the generator (`build_v2_dataset.py:29`) and in all three shipped copies, and refreshed the
`attributes.jsonl` sha256 in `site/static/manifest.json` so the manifest stays honest.
`README.md:33` carries the same wording and I left it — see "Outstanding".

---

## `bias_adjust.py`

Docstring only; **no behaviour change** (verified: module imports and `adjust_scores` returns
identical output on a smoke input). The parenthetical claiming the source-mix confound is "gone by
construction" is replaced with a third numbered bias, explicitly marked **NOT MITIGATED**, giving
the actual served mix (65,075 Hansard / 23,935 releases / 5,419 pressers), the size and direction
of the source gaps, the by-party mix skew, the fact that shrinkage is fit over pooled scores and
cannot see source, and the two ways to actually fix it. It now reads as an open defect rather than
a solved one.

---

## Figures I recomputed, and how

All from `site/static/examples.jsonl` (94,429 rows), `scores.jsonl` (135 rows) and
`politicians.jsonl`, with card scores as the geometric mean over scored attributes and the 130-card
grid reproduced by applying `app.py`'s `MIN_ATTRIBUTES = 6`.

| Claim | Review said | I computed | Used |
|---|---|---|---|
| distinct statements | 45,450 | **45,477** | 45,477 |
| distinct Hansard URLs | 190 | 190 | ✓ |
| MP-attribute scores / max | 1,150 / 79 | 1,150 / 79 (Rurawhe Civility) | ✓ |
| displayed ≥ 80 | 0 | 0 | ✓ |
| raw ≥ 80 | 34 | 34 | ✓ |
| raw ≥ 80 with n ≥ 10 | 5 | 5 (Walters 80.6/51, Rurawhe 82.8/29, O'Connor 84.1/17, Fleming 86.2/13, Garcia 86.2/13) | ✓ |
| Tinetti Forthrightness raw→shown | 90 → 56 on n=1 | 90 → 56 on n=1 | (not used in post) |
| best / worst card | 66.01 Walters / 44.52 Peters | same | ✓ |
| Divination card range | 43–54 over 126 | 43–54 over 126 | ✓ |
| Civility ≤ 20 in Hansard | 11.1% | 1,115 / 10,061 = **11.08%** | 6/sitting day |
| Rigor ≥ 90 / ≥ 95 | 3 / 0 of 14,503 | 3 / 0 of 14,503 | ✓ |
| stmt Civility~Charisma | 0.96 | 0.958 (n=3,383) | 0.96 |
| stmt Civility~Rigor | 0.85 | 0.851 (n=5,328) | 0.85 |
| stmt Rigor~Charisma | 0.84 | 0.835 (n=1,291) | ~0.85 |
| r(n statements, card) | −0.254 | −0.254 | −0.25 |
| same, n ≥ 1,000 | −0.10 (k=21) | −0.099 (k=21) | −0.10 |
| top-20-quoted mean rank | 86.85 | 86.85 | 87th |
| median rank, 8 vs 9 attrs | 45th / 71st | 45.0 / 71.0 | ✓ |
| top-20 / bottom-20 by party | as tabled | reproduced exactly | ✓ |
| Forthrightness coverage | 104 of 135 | 104 | ✓ |
| source gaps H vs releases | +17.6 / −9.3 / −7.2 / −6.1 | +17.5 / −9.3 / −7.2 / −6.2 | review's rounding kept |
| source mix by party | as tabled | reproduced exactly | ✓ |
| presser counts | 5,269 Nat, 0 Lab/Grn/TPM | 5,269 / 126 NZF / 24 ACT / 0 others | added NZF+ACT |
| median per-attribute CI | ±4 (mean ±5.3, max ±18) | median 4, mean 5.27, max 18 | ±4 |
| ranks 100/110/120/125 | 54.0 / 53.0 / 52.1 / 50.9 | same | 25 places in 3.1 pts |

**Newly computed for this edit (not in the review):**

- **Divination-specific CIs.** median ±4, mean ±3.56, max ±5 across the 126 scored cards. This
  matters — see "Where I disagreed" #3.
- **Statement extraction density.** 45,477 statements over 9,118,460 corpus words
  (`dataset_stats.json`: 7,500,644 + 1,164,029 + 453,787) ≈ **5.0 per 1,000 words**. The review
  used 8.7M words for the same ratio. I didn't put the number in the post — the qualitative claim
  ("the model does the filtering, unmeasured") carries it — but it's here if you want it.
- **Card ordering by attribute count.** Walters 1st on 8, Salesa 2nd on 8, Rurawhe 3rd and the
  first card with all nine. Confirms the caption's hedge and the Tier 6 bug.

---

## Where I disagreed with the reviewer

**1. Distinct statements is 45,477, not 45,450.** The review's figure comes from de-duplicating on
statement *text alone*, which collapses identical strings said by different MPs (procedural
boilerplate, mostly). De-duplicating on (speaker, text) — which is what "distinct statements"
should mean when the unit of analysis is an MP-statement — gives 45,477. The review's own
breakdown proves the point: 7,362 + 28,098 + 9,387 + 630 = **45,477**, not 45,450. Its per-bucket
counts are all exactly right; the total is a slip. The post uses 45,477.

**2. The Webb divination example is more interesting than the review allows, and I kept it.**
The review says the 10/100 "was assigned on prior plausibility at time of speaking, *not* because
the bill was voted down". The model's stored explanation says otherwise — verbatim:

> "A falsifiable near-term prediction that failed the same day: National (49), ACT (11) and NZ
> First (8) all voted the bill down at first reading. Partly rhetorical, but as a forecast it was
> contradicted by the known coalition position."

So the model *did* reach for the outcome, unprompted, from its own recall. That doesn't rescue the
post's original claim — the **pipeline** performs no outcome check, the prompt explicitly forbids
one, and an unverified model recollection is not verification — but it means "the score was
assigned on plausibility alone" is also not quite what happened. The post now says the precise
true thing: the forecast was implausible when made (the coalition position was known), the
division record separately confirms the 68–54 defeat, and **the pipeline has no outcome-checking
step**. That is more accurate than either the original or the review's replacement, and it keeps a
good example. The vote itself is confirmed in `data/corpus/divisions.jsonl`, division
`2025-07-30-001`.

**3. "An 11-point spread, tighter than the median confidence interval" is not right.** The review
compares Divination's 43–54 range to the median per-attribute CI. But the CI is reported as a
half-width: median ±4 is an 8-point interval, and Divination's own CIs are median ±4 / max ±5. An
11-point spread is *wider* than 8, so the sentence as drafted would have been a new error in a
correction. The post makes the defensible version of the same point instead: "an eleven-point
spread for the whole Parliament, when a typical single card's own confidence interval on
divination is ±4". The conclusion — Divination carries almost no signal — is unchanged and correct.

**4. I did not cut the opening by 40%.** The review is right that the Burke block quote does least
work, and it's gone. But items 17b and 18 both required *adding* honest qualification to exactly
that stretch of the post, and cutting to target would have meant losing the "they represent you"
build-up or the "how do you want your side to win?" turn, which the constraints protect. Net effect
is roughly neutral in length and better in content. Flagged as an open editorial call.

**5. On overcorrection.** I've kept the post's confidence where the review says it's warranted. The
"nobody clears 80" finding, the evidence-linking design, "It isn't that they can't", the Simon
Court pair, and the closing argument are all intact and unhedged. The new caveats are placed so
they qualify specific claims rather than the whole enterprise, and both new sections end by saying
what survives the caveat rather than trailing off into apology.

---

## Outstanding, for the author

**Post / blog**

1. Decide whether the corrections block belongs at the end of the post or somewhere systematic
   (front-matter key + include), and whether it should be dated to first publication or to today.
2. The opening (`## What should we expect?` → `## The one standard we can all agree on`) is still
   long. I trimmed rather than cut. If you want the review's 40%, the candidates are the
   "Legislate, scrutinise the executive, represent" sentence and one of the two rhetorical
   questions at the end of "How do you want your side to win?".
3. Consider whether the veracity caveat now sitting inside "Seven ways to fail" is one interruption
   too many in that list. It's there because item 20's real lesson is about placement.

**Repo**

4. **`README.md:33`** still defines Divination as "Tracks how often the politician's predictions
   about future events… have proven to be accurate." I fixed the three shipped `attributes.jsonl`
   files and the generator, but left the README — it's a bigger doc rewrite and not user-facing on
   the site. Worth a pass.
5. **`site/static/attributes.jsonl` is now out of step with the built data.** I edited it in place
   so the live site is correct today. If you re-run `build_v2_dataset.py` the new definition comes
   through (I changed the generator too), but any other data regeneration should be checked.
6. **The Strength/Authenticity subject-attribution fix.** `extract.py` already carries the
   `subject: speaker|other` instruction in `build_combined_system`, but the *shipped* dataset
   predates it — which is why the bug is still live. `EVALUATION.md`'s fix option 1 (a cheap Haiku
   pass over the ~8k explanations, filtered at build time) would repair the site without a re-run.
   Until that lands the post's "discount heavily" caveat has to stay.
7. **The source-mix confound has no mitigation at all.** The `bias_adjust.py` docstring now says so
   honestly, but saying so isn't fixing it. Either score per source and reweight to a common mix,
   or restrict cross-MP ranking to Hansard-only. This is the single largest threat to the league
   table's validity.
8. **Ranking over incomplete cards.** Cards with 8 attributes have a median rank of 45th vs 71st
   for complete cards — a missing attribute is worth ~26 places. Either restrict the ranking to
   complete cards or normalise. The post now discloses this; the site does not.
9. **Divination in the geometric mean.** It contributes 11 points of spread across 126 MPs and is
   ungrounded by its own prompt. Dropping it from the rank until it's grounded would change the
   league table and would be defensible; the post says it shouldn't be in there.
10. **Label the v3 test pool.** `build_testsets.py` has sampled 120 items from the real corpus,
    unlabelled. Everything in item 1 stays true until that's done — and a second labeller would
    give the inter-rater number the post currently has to admit it lacks.
