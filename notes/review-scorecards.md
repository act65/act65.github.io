# Critical review — "What Makes a Good Politician?"

Post: `_posts/inbetween-posts/2026-08-01-scorecards.md`
Repo: `~/Documents/repos/pol-score-cards`

External review. Every statistic was recomputed from the shipped data (`site/static/*.jsonl`),
and ~25 figures verified correct. The problems are not arithmetic.

---

# TIER 1 — Errors and contradictions with the repo. Fix before this stays up.

## 1. The evaluation numbers are measured on invented, non-NZ statements. The post doesn't say so.

**L185:** *"Against small human-labelled test sets, civility comes out at r = 0.88 (average error
0.13 on a 0–1 scale) and veracity at r = 0.73. Good — but those test sets are small."*

The figures match `EVALUATION.md` L55–56 exactly. But that file, under a heading added
**2026-08-01** — the post's own date — says:

> **⚠ The testsets are synthetic — the headline numbers do not measure this task**
> Every row in `testsets/` is an *invented* statement attributed to a fictional politician:
> "Senator Armstrong", "Governor Miller"… **There is no New Zealander in any testset, and not one
> line of Hansard.** … **The number is not evidence about the system we actually run** … treat
> every accuracy figure in this document as unvalidated.

Confirmed against `testsets/civility_testset.jsonl` and `veracity_testset.jsonl`. The post quotes
the invalidated numbers and hedges only on sample size — the one thing that isn't the main problem.
`site/templates/about.html` carries the same stale claim and needs the same fix.

Three further omissions that `EVALUATION.md` documents:
- **n = 14 per attribute.** 95% CI on r=0.88 ≈ 0.65–0.96; on r=0.73 ≈ 0.32–0.91.
- **No inter-rater reliability.** One labeller, no second rater, no kappa.
- **Known prompt/testset leakage** (`EVALUATION.md` L156–158): several prompts embed few-shot
  examples not verified disjoint from the testsets.

**Suggested replacement for L185–186:**

> The scores are **automated estimates, not verdicts** — and I want to be precise about how weak
> the validation currently is. The evaluation I built runs against fourteen hand-labelled
> statements per attribute, and those statements are *invented* — fictional American
> council-meeting speech, not a line of Hansard in them. On that set civility scored r = 0.88 and
> veracity r = 0.73, which sounds reassuring and isn't: it measures the model on a task that is
> not this one. NZ parliamentary speech is a different register and far more adversarial. A
> replacement set drawn from the real corpus is sampled but not yet labelled. **Until it is, treat
> every accuracy figure here — including the two I just quoted — as unvalidated.** There is also
> no second labeller, so I have no inter-rater agreement to report.

## 2. "The number is just the mean of the evidence" is false — and it partly manufactures the headline.

**L69.** `bias_adjust.py` applies **empirical-Bayes shrinkage toward the per-attribute population
mean**; `display_score()` returns the shrunk posterior. The manifest confirms
(`"bias_mitigation": "empirical-Bayes shrinkage per attribute"`).

This undercuts **L84** (*"not one reaches 80"* — correct as displayed). On **raw** means:

| | count |
|---|---|
| displayed ≥ 80 | **0** |
| raw ≥ 80 | **34** |
| raw ≥ 80 with n ≥ 10 statements | **5** |

Paulo Garcia and Greg Fleming both average **86.2** raw civility over 13 statements; Adrian
Rurawhe 82.8 over 29; Vanushi Walters 80.6 over 51. The 79 ceiling is substantially a property of
the estimator.

**L92** misdiagnoses this as "averaging compresses toward the middle". It isn't averaging — it's
deliberate compression, much stronger for thin coverage (largest gap: Jan Tinetti, Forthrightness,
raw 90 → shown 56 on n=1).

**Suggested L69:** "…the number is a shrunk average of the evidence you're looking at — thin
evidence gets pulled toward the middle on purpose, so a single flattering quote can't make a card."

**Suggested L92:** "(Two honest caveats. First, card scores are deliberately pulled toward the
population average in proportion to how little evidence there is behind them — that's the right
call for ranking, but it means the 79 ceiling is partly my estimator and not just Parliament. On
raw unadjusted means, thirty-four MP-attribute scores clear 80, five of them on ten statements or
more. Second, individual statements do hit 100. The claim isn't that no MP is ever exemplary — it's
that none of them sustains it.)"

## 3. Divination does not measure whether predictions come true. The post says it does, twice.

**L62** and **L120.** `prompts/divination.txt` ends:

> **GROUNDING CAVEAT (v3.0): Divination is currently an UNGROUNDED, text-only judgement — you are
> scoring the quality and falsifiability of a prediction, NOT whether it came true.**

Duncan Webb's 10/100 was assigned on prior plausibility at time of speaking, *not* because the bill
was voted down. (The fact checks out — `divisions.jsonl` division `2025-07-30-001`, Property Law
(Sunset Clauses) Amendment Bill, lost 54–68. The causal story about the score is wrong.) This is
the one place a reader concludes the pipeline verifies things against reality.

**Divination also carries no signal:** across 126 MPs the card range is **43 to 54** — an 11-point
spread, tighter than the median confidence interval — and it is one of nine terms in the geometric
mean determining every rank in the post.

**Fix:** L62 → "**Divination** — are their predictions specific enough to be checked, and plausible
on the evidence at the time?" Reframe or cut the Webb example. Add to "What it isn't": *"Divination
in particular is close to inert: every MP lands between 43 and 54, which is what you'd expect from
a model asked to rate plausibility with no outcomes to check against. It shouldn't be in the
geometric mean until it's grounded, and it currently is."*

## 4. "94,429 individually scored statements" double-counts.

**L78.** That's the row count of `examples.jsonl` — *(statement × attribute)* pairs. Distinct
statements: **45,450**. (7,362 scored on one attribute, 28,098 on two, 9,387 on three, 630 on 4+.)

**Fix:** "**45,450 statements, scored 94,429 times** (most statements are relevant to more than one
attribute)."

## 5. "204 sitting days" describes the scrape, not the scored data.

**L78.** `HANSARD_COVERAGE.md` splits 204 into 14 days of the 53rd Parliament (pre-election) and 190
of the 54th. The shipped dataset has exactly **190** distinct Hansard URLs. (~7.5M words is fine —
`dataset_stats.json` gives 7,500,644.) **Fix:** "190 sitting days of the current Parliament".

## 6. "135 people we elected" — New Zealand elected 123.

**L197**, also L78 and L96. The 54th Parliament has 123 seats; the 135-name roster spans the term
including departures and list replacements. Separately **L96** is wrong about the site: `app.py`
sets `MIN_ATTRIBUTES = 6`, so **130** cards appear on the grid.

**Fix:** L197 → "not one of the 135 people who have sat in this Parliament is meeting it."
L96 → "the site has 130 cards on the front page".

## 7. The "Seven ways to fail" wrap-up contradicts itself.

**L134** says Authenticity is missing from the list. It isn't — it's at L125 (Goldsmith). The two
genuinely absent are **Strength and Charisma**, and Charisma is never mentioned. Also *"roughly four
times as often"*: `EVALUATION.md` L208–212 gives Authenticity 9.8% vs 2.4% (**4.1×**) but Strength
4.7% vs 0.6% (**7.8×**).

**Suggested rewrite:** see the reviewer's version — leads with Charisma being a near-duplicate of
Civility, keeps the attribution bug, and gives both multipliers.

## 8. "He did it an hour before the second."

**L153.** `examples.jsonl` carries dates, not times; both Simon Court quotes are stamped
`2026-03-31` with no ordering. **Fix:** "He did it in the same debate, to the same person."

---

# TIER 2 — Measurement validity

## 9. There are not nine attributes. There are about three, and one is counted three times.

**Statement level:** Civility~Charisma **r=0.96** (n=3,383); Civility~Rigor **0.85** (n=5,328);
Rigor~Charisma **0.84** (n=1,291). **Card level:** 0.82 / 0.60 / 0.59, Civility~Veracity 0.63.

Visible in the prompts: `civility.txt` penalises "strawmanning" and "hyperbole"; `rigor.txt` lists
strawman and ad hominem first; `charisma.txt` says "crowd-pleasing attacks on opponents are not
charisma — score them low." **One insult knocks down three of nine attributes**, and the geometric
mean compounds it.

Direct consequence for **L173**: "the bottom of the table is the leadership" may be almost entirely
*party leaders make more adversarial attacks, and the ranking triple-weights adversarial attacks*.

**Suggested addition to "Where the failures cluster":**

> One caution before the guesses. The nine attributes are not nine independent things. Civility and
> Charisma correlate at 0.96 at the statement level; Rigor with each of them at about 0.85. All
> three penalise the same move — the personal attack. So a single jibe costs an MP a third of their
> card, and the geometric mean compounds it. Whatever the bottom of the table is measuring, it is
> measuring it three times.

## 10. The rubric's midpoint is *acceptable* conduct — which breaks the "pass mark is 100" frame.

**L39–41, L90.** `prompts/civility.txt` anchors **~0.5 — harsh but legitimate criticism of policies,
ideas, or actions**. Same in `rigor.txt` and `specificity.txt`. And the few-shot cap: civility's 0.9
exemplar is near-ideal parliamentary speech, so the rubric never expected 1.0.

The instrument was never built as 0-fails/100-passes. "Nobody passes" is partly retrofitting. This
is the argument that does most damage if a critic makes it first — so make it yourself.

**Suggested addition:** see reviewer's paragraph — owns that the pass mark is the author's framing,
not the rubric's, and keeps the distribution tail as the real finding.

## 11. The LLM chooses which statements to score, and the anti-cherry-picking argument ignores that.

**L69** says "score each one". `extract.py` asks the model to *find* qualifying statements
(L192–198: "extract EVERY qualifying statement… not only the most striking"). Nothing validates
compliance. 45,450 statements from 8.7M words ≈ **5 per 1,000 words** — the model does 99%+ of the
filtering, unmeasured.

That breaks **L88**'s "so the impression I got from the clips wasn't a selection artefact. It's
roughly the base rate." The 11.1% is verified correct — but it's the base rate *among statements a
model chose to flag as civility-relevant*, the class most likely over-sampled at the extremes. In
absolute terms ~1,115 insults across 190 sitting days ≈ six a day.

**Suggested replacement for L88's last two sentences:**

> …which is to say, is essentially just an insult. About six a sitting day. I can't tell you that's
> the base rate in the chamber, because the model chooses which statements to surface and I haven't
> measured whether it samples evenly — that's the next thing I'd validate. What I can say is that
> the insults aren't rare enough to need hunting for.

## 12. Verbatim speech contains slips, and a text-only judge reads them literally.

Hansard is lightly-edited spoken language. A statement-level scorer with no discourse context reads
inversions and self-corrections at face value. Deserves a line in "What it isn't" — see item 20.

---

# TIER 3 — Selection and sampling bias

## 13. Source mix differs enormously by party, and scores differ enormously by source.

| party | Hansard | Party releases | Pressers | % releases |
|---|---:|---:|---:|---:|
| National | 27,664 | 7,390 | 5,269 | 18.3% |
| Labour | 16,672 | 5,450 | 0 | 24.6% |
| Green | 7,165 | 4,081 | 0 | 36.3% |
| **ACT** | 5,988 | 4,957 | 24 | **45.2%** |
| NZ First | 5,229 | 1,077 | 126 | 16.7% |
| Te Pāti Māori | 2,355 | 980 | 0 | 29.4% |

| attribute | Hansard | Party releases | gap |
|---|---:|---:|---:|
| **Forthrightness** | 47.5 | 65.1 | **+17.6** |
| Specificity | 65.0 | 55.7 | −9.3 |
| Civility | 51.4 | 44.2 | −7.2 |
| Rigor | 52.6 | 46.5 | −6.1 |

Those gaps are the size of the entire 44.5–66 league-table range. Pressers are effectively
government-only (5,269 National; **zero** for Labour, Green, TPM).

**Note:** `bias_adjust.py`'s docstring claims *"Hansard-only v2.0 removes the source-mix confound…
that bias, the worst one, is gone by construction."* True of v2. **Not true** of the dataset the
site now serves, which added 23,935 press-release statements. The stated mitigation no longer
applies and nothing replaced it.

## 14. Forthrightness is structurally a minister-only measure.

Only **104 of 135** MPs have one. `prompts/forthrightness.txt` scores only "instances where a
politician is asked a question" — overwhelmingly ministers at oral questions. And it has the largest
source gap (47.5 vs 65.1). L177 half-acknowledges this as a passing guess, not as a reason the
attribute isn't comparable.

## 15. Specificity, Strength and Divination structurally favour the executive.

`specificity.txt` rewards "figures, mechanisms, timeframes, or named policies" — what a minister
announcing a programme produces. `strength.txt` measures delivery, which only ministers and members
in charge of bills can do. The repo's own `data/VOTES.md` names this: *"Strength needs a
delivery-scope gate… scoring an opposition backbencher low for not delivering repeats the
subject-attribution error in a new form."* None of this is in the post.

**The post needs a section, not a sentence.** Suggested placement after "Where the failures
cluster" — see reviewer's full draft, "The comparison isn't fair yet".

## 16. The r = −0.25 finding is confounded by the shrinkage.

**L175.** Both figures reproduce (r = −0.254; mean rank 86.85). But shrinkage pulls thin coverage
toward ~56, *above* the 53.8 average of the 21 most-covered MPs — so the estimator mechanically
produces a negative n-vs-score correlation. Restricting to n ≥ 1,000 statements, r falls to
**−0.10** (k=21); at n≥500 it holds at −0.235, so something real is probably underneath.

**Fix:** *"…correlates negatively with how much an MP talks (r = −0.25) — though some of that is my
own estimator, which pulls thinly-covered MPs toward the average; among the twenty-one most-covered
MPs it weakens to about −0.10. The blunter fact survives: the twenty most-quoted MPs average 87th
of 130."*

---

# TIER 4 — The framing claim

## 17. "The one standard we can all agree on" is doing more work than the instrument can bear.

**(a) The rubric encodes a rhetorical preference.** `civility.txt` marks down "sensationalism,
hyperbole, and exaggeration"; `specificity.txt` rewards figures and named policies. Together they
reward a technocratic register and punish a moral or oratorical one.

**(b) The tails are strongly party-patterned**, which L171's "top five" cut obscures:

| | Labour | National | Green | ACT | NZ First | TPM |
|---|---:|---:|---:|---:|---:|---:|
| **top 20** | 11 | 5 | 2 | **0** | 2 | **0** |
| **bottom 20** | 2 | 5 | 3 | 3 | 3 | **4** |
| roster | 39 | 49 | 18 | 12 | 9 | 7 |

Te Pāti Māori: **4 of 7 MPs in the bottom 20, none in the top 20.** Party *means* are within a few
points — honest — but the extremes, which is what the post names people over, are not.

**Suggested addition** — see reviewer's paragraph, which owns the pattern and attributes it to
rhetorical register rather than honesty.

## 18. "Answer the question" is not uncontested.

**L37, L47, L49.** NZ Standing Orders require a Minister to *address* the question, not answer it,
and Speakers rule on the distinction regularly. One clause fixes it.

---

# TIER 5 — Fairness to named individuals

## 19. Ranks are reported to a precision the data doesn't support.

**L173** names seven MPs with exact ranks. Rank 100 = 54.0, 110 = 53.0, 120 = 52.1, 125 = 50.9 —
**25 ranks inside 3.1 points**, against a median per-attribute CI of ±4 (mean ±5.3, max ±18, and
these are on the site already). "Ngarewa-Packer (122nd)" and "Seymour (124th)" are not
distinguishable from each other or from 105th.

Defensible claim: the bottom three — Peters 44.5, Jones 44.6, Waititi 48.1 — sit clearly below a
pack starting at 50.3.

**Suggested rewrite:** *"**The bottom of the table is the leadership.** Three cards sit clearly below
the rest: Winston Peters (44.5), Shane Jones (44.6) and Rawiri Waititi (48.1). After that the table
compresses so tightly that individual ranks stop meaning much — twenty-five places separated by
three points, against confidence intervals of ±4 — so read the band rather than the number. The last
ten places hold the Prime Minister, a Cabinet minister, and five party leaders and co-leaders; Chris
Hipkins and Chlöe Swarbrick are in the bottom half."*

## 20. The Willie Jackson veracity example — cut it.

**L105–108.** In context (`hansard.json`, 2024-07-24):

> *"They told Corrections to no longer have Treaty provisions in their legislation. Can we believe
> that? **Fifty percent of Māori are in jails at the moment**, but this Government now doesn't want
> to consider the Treaty. And the most recent nonsense: directing Pharmac to stop wasting time on
> the Treaty. That's unbelievable when you look at the disparity in terms of Māori."*

This is a transparent word-order slip in live speech for "fifty percent of [people in] jails [are]
Māori" — the surrounding sentences are about Corrections and Māori disparity. The model scored the
literal string in isolation: 10/100, *"Demonstrably false as stated."*

So the post takes an unvalidated instrument (item 1), on an attribute whose own prompt flags it as
ungrounded, applies it to a verbal slip, and publishes a named MP under **Veracity — 10/100** with a
correction implying he got a fact about Māori incarceration badly wrong. The "plausibility not
truth" caveat doesn't appear until L187, eighty lines later.

**Preferred fix: cut it**, use a Veracity example where the claim is a considered assertion and the
fact independently checked.

**If kept, reframe as an instrument failure** — which is more interesting anyway. See reviewer's
"**Veracity — 10/100, and the model is wrong**" version.

## 21. Smaller fairness points.

- **L110–113 (Peters, Rigor 5).** From an NZ First press release, correctly labelled — but the
  post's premise (L17) is "this is them **at work**, in the chamber". Add: "not in the House, this
  one — a party press release, where nobody is arguing back."
- **L7–10 (Seymour).** "describing a colleague" reads as a fellow ACT member; the data doesn't
  identify the target. Use "describing another member".
- **L142.** Praise examples (Bishop, Walters, Andersen) carry no links while criticism is fully
  cited "all verbatim, all linked". Asymmetric citation of praise vs criticism is a bad look. All
  three check out — Bishop Civility 95 (2025-04-08), Walters 90 (2025-08-21), Andersen 90
  (2025-08-21) — so just add the links.

---

# TIER 6 — Structure

- **L76 caption fights L142.** Rurawhe presented as "top" (hedged: highest-ranked card with all nine
  scored), then Walters called "the top-ranked card". Both true. **The hedge points at a real bug:**
  cards rank by geometric mean over *whatever subset was scored*, so a missing attribute — often the
  weakest — advantages an MP. Median rank: **8 attributes → 45th; 9 → 71st.** The top two cards both
  have 8. Restrict ranking to complete cards or say so.
- **L21–51 is long** — ~30 lines before any data. The Burke quote (L27–31) does least work; the
  "they represent you, this is done in your name" passage (L45–47) is stronger and survives alone.
  Cut ~40%.
- **L82 "here is the entire result"** then four numbers, then two more results sections. Use "here is
  the headline".
- **The nine-attribute list (L57–67)** — Charisma and Strength never reappear. Consider a table with
  a fourth column: "judged from the text / needs external checking / not grounded yet", which
  retires much of the later hedging.
- **"What it isn't" (L181–191) is second-to-last.** Given how severe those caveats are, a two-line
  version belongs immediately after the first big number at L84.

---

# What works — don't touch

- **The arithmetic.** Independently verified: 1,150 MP-attribute scores ✓; max 79 ✓; best card 66.01
  (Walters) ✓; worst 44.52 (Peters) ✓; 130 ranked cards ✓; Rigor n=14,503 with exactly 3 at ≥90 and
  0 at ≥95 ✓; civility card-average 54.1 ✓; 11.1% of Hansard civility ≤20 ✓; Hansard 68.9% ✓; 2,976
  releases ✓; 65 pressers ✓; date range ✓; r = −0.254 ✓; top-20 mean rank 86.85 ✓; every bottom-ten
  rank ✓; Hipkins 82nd ✓; Swarbrick 89th ✓; top five = 3 Labour / 1 National / 1 NZ First ✓. Every
  quoted statement matches `examples.jsonl`, and the Webb bill really was voted down 54–68. An
  unusually clean record.
- **The what/how distinction (L23–31)** is the right frame.
- **"How do you want your side to win?" (L47)** is the best line in the piece.
- **"It isn't that they can't" (L136–165)** is the strongest section — the Simon Court pair is
  genuinely persuasive, and praise examples from every party are what make the rest credible.
- **Volunteering the attribution bug (L134)** is exactly the right instinct. The three suppressed
  caveats in Tier 1 are the same kind of finding and would land the same way.
- **The evidence-linking design** is what makes the project worth taking seriously.

---

**If you fix only five:** the synthetic testsets (#1), the shrinkage claim (#2), Divination's
grounding (#3), the Willie Jackson example (#20), and add a real selection-bias section (#15).
Those five turn the biggest attack surfaces into the post's most credible passages.
