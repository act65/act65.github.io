# Changelog — edits to `_posts/inbetween-posts/2025-07-24-agi-game.md`

Applied against `notes/review-agi-game.md`, in the review's suggested revision order.
Keyed to the review's item labels. `bundle exec jekyll build` passes (only the pre-existing
Sass `@import` deprecation warnings).

New file: `_bibliography/agi-game.bib` (13 entries). Post frontmatter gained
`scholar: bibliography: "agi-game.bib"`; a `## Bibliography` section with
`{% bibliography -f agi-game --cited %}` was added at the end, matching the pattern in
`_posts/technical-posts/2024-08-10-scoredd.md`. All 13 citations resolve and render.

---

## 1. A2 — Chicken vs Prisoner's Dilemma

**Done.** New `#### Or is it Chicken?` subsection immediately after the AGI matrix. Uses the
review's drafted paragraph nearly verbatim, plus an explicit Chicken matrix:

| | B: Cooperate | B: Defect |
|---|---|---|
| **A: Cooperate** | (3, 3, 4) | (2, 4, 2) |
| **A: Defect** | (4, 2, 2) | **(1, 1, 1)** |

Recomputed: row payoffs are T=4 > R=3 > S=2 > P=1. If B cooperates, A prefers D (4 > 3); if B
defects, A prefers C (2 > 1). No dominant strategy; pure equilibria at (D,C) and (C,D); a mixed
equilibrium exists. Confirmed Chicken, not a PD. Humanity's column is unchanged (4/2/2/1) — mutual
ruin is still humanity's worst.

Ends by stating explicitly that the post takes the positional reading for the rest of the argument,
and that this is an assumption carrying the argument. The Schelling commitment point is cited.

## 2. C5 — the empirical baseline

**Done.** L9 replaced with the review's drafted softening ("Some global coordination problems get
easier with time… and it often doesn't happen in time"). New `#### How well does this story
actually hold?` subsection after the climate section, built from the review's draft, with Ostrom
(1990 design principles; 2010 polycentric), Barrett (2003), Kyoto/Paris/Montreal, and northern cod.

**On the FAO figure — verified, not omitted.** The review flagged this for checking, so I checked.
The current report is **SOFIA 2026** (published June 2026), not the 2024 edition the review's
numbers came from. SOFIA 2026 puts biologically sustainable stocks at **62.4%** (2023 data), i.e.
~37.6% unsustainable, down from 64.5% in the previous edition. SOFIA 2024 had reported 62.3%
sustainable / 37.7% unsustainable for 2021. The 1974 baseline of ~10% unsustainable is stable
across editions.

I printed it as **"from around 10% in the mid-1970s to roughly 37% in the FAO's latest
assessment"** — deliberately rounded and hedged, because FAO itself notes the between-edition
change partly reflects assessment revisions, methodological updates and newly included stocks
rather than pure deterioration. The direction and rough magnitude are safe; a two-decimal figure
would not be. **Author task:** if you want the exact number, quote SOFIA 2026's 62.4% sustainable
figure directly rather than my subtraction.

I dropped the review's Costello et al. and Worm et al. citations — the sentence they supported
(rights-based management vs. visible damage) was folded into the Ostrom paragraph, which makes the
same point with a source I verified.

## 3. B3 — conditional thesis + threshold inequality

**Done.**
- L11 rewritten: "a Prisoner's Dilemma that doesn't dissolve on its own… and it stays a Prisoner's
  Dilemma for exactly as long as the people racing believe they can race and win."
- The threshold added to the escape hatch, derived in place:
  $(1-p)W + pL > C \iff p < (W-C)/(W-L)$. Checked: $W - pW + pL > C \Rightarrow W - C > p(W-L)
  \Rightarrow p < (W-C)/(W-L)$, valid for $W > L$.
- The inequality is used as the post's spine: "Why the prize looks absolute" is reframed as an
  argument about why decision-makers put $p$ below the threshold, and "What could change the game"
  as interventions on $p$, beliefs about $p$, or $W$. The closing section restates it.
- Han et al. cited as the proper derivation.
- Display math uses `$$…$$` (renders to `\[…\]`); inline uses `$…$`, which is the repo's existing
  convention and is handled by the `inlineMath` rule in `_includes/mathjax.html`.

## 4. A1 and B2

- **A1 — done, via the review's "honest downgrade" (option 1).** L13 now says humanity is a welfare
  ranking, has no strategies, never moves, and is "a scorecard, not a participant". I did *not*
  take option 2 (make humanity non-monotone or a real third player): it would require re-deriving
  five matrices and re-arguing Bostrom's singleton claim, which is a different post. **Author
  task:** option 2 is the more interesting version if you ever want to expand this.
- **B2 — done.** Section retitled "The misalignment is an assumption, and it's the important one";
  L81 replaced with the review's draft. Added the second half of B2's objection too: the T > R gap
  is just the definition of a PD and isn't distinctive to AGI — what's distinctive is the claim
  that this one doesn't transform.

## 5. C1 — citations

All 13 entries verified against primary or archival sources before being written into
`_bibliography/agi-game.bib`. Volume/issue/page numbers were only entered where I confirmed them;
none were guessed.

| Key | Placement | Verified against |
|---|---|---|
| `armstrong2016racing` | "no repeated rounds" bullet; information caveat | Oxford Research Archive record; AI & Society 31(2), 201–206 |
| `askell2019cooperation` | new issue-linkage paragraph | arXiv:1907.04534 |
| `han2020regulate` | escape hatch, threshold | JAIR 69, 881–921, doi 10.1613/jair.1.12225 |
| `naude2020race` | "no repeated rounds" bullet | AI & Society 35, 367–379 |
| `dafoe2018governance` | "What could change the game" intro | FHI 2018; no vol/pages entered |
| `cave2018race` | after the preserved L97 sentence | AIES 2018 proceedings, 36–40, doi 10.1145/3278721.3278780 |
| `bostrom2016unilateralist` | assumptions, n=2 bullet | Social Epistemology 30(4), 350–371 |
| `ostrom1990governing` | new empirical subsection | book |
| `ostrom2010polycentric` | new empirical subsection | Global Env. Change 20, 550–557 |
| `barrett2003statecraft` | new empirical subsection | OUP 2003 |
| `jervis1978security` | nukes section, one added sentence | World Politics 30(2), 167–214 |
| `schelling1960strategy` | focal points (fisheries); commitment (Chicken) | book |
| `hardin1968tragedy` | overfishing intro | Science 162(3859), 1243–1248 |
| `fao2026sofia` | new empirical subsection | FAO SOFIA 2026 |

I omitted **Zwetsloot & Dafoe (2019)** — the Dafoe agenda already carries that slot and the post
doesn't make a structural-risk argument that needs it. **Author task:** add it if you expand the
"what could change the game" section.

**On the hard constraint about the Armstrong et al. information result — I verified it, and I
assert it.** The Oxford Research Archive record for the paper carries the abstract verbatim:
*"Surprisingly, information also increases the risks: the more teams know about each others'
capabilities (and about their own), the more the danger increases."* That is the paper's own
abstract, not a secondary summary, so it is stated in the post as an established finding of that
model. I have **not** read the full derivation, so the post attributes it to the model rather than
asserting it as a general truth about monitoring: "In Armstrong, Bostrom and Shulman's race
model…". **Author task:** read the paper before defending it in a comment thread.

The caveat is placed directly under "What could change the game" and is allowed to bite the
compute-monitoring recommendation rather than being buried. I added the distinction that saves the
recommendation: monitoring that reveals *relative standings* is not the same as monitoring that
verifies compliance with a ceiling without revealing who is ahead.

## 6. D1–D6 — assumptions subsection

**Done.** New `### What this model assumes` before "Why AGI Is Different", six bullets, ~150 words
(slightly over the review's ~120 — the n=2 and complete-information bullets each needed a clause to
land). All six items covered: n=2 with the unilateralist's curse, states-as-players-with-labs-as-
instruments (D2, resolved the review's way), binary strategies, simultaneous one-shot moves,
complete information vs. the "no visible degradation" bullet, single decisive moment with the
knock-on that lock-in failure means T isn't a 4.

## 7. A3–A7 — matrix and convention corrections

- **A3 — done, but I took option (b), not (a), and this is a deliberate disagreement with the
  reviewer's preference.** The review calls the harmony-game reframe "cleaner"; it is also a
  rewrite of the whole "standard pattern" arc, because it dissolves the dilemma that the climate
  parallel and the AGI contrast both depend on. So I kept the stag hunt and paid the debt the
  review identified: the "an overfished sea pays nobody" clause is gone, replaced with a mechanism
  that actually generates T falling 4 → 3 ("the boat that overfishes a depleted stock lands much
  less than the boat that overfished a healthy one"), and S=1 < P=2 is now explicitly defended
  rather than smuggled — "you lose twice, because the fishery goes anyway and somebody else landed
  the last of it." Matrices unchanged and rechecked: short-run is T=4 > R=3 > P=2 > S=1, D
  strictly dominant, unique NE at (2,2,1) — a valid PD. Long-run is R=4 > T=3 > P=2 > S=1 with
  pure NE at (C,C) and (D,D) — a valid stag hunt.
- **A4 — done.** The cardinal-utility disclaimer opens the escape hatch verbatim from the review's
  draft. L35/L55's risk-dominance language is gone: the fisheries paragraph now says institutions
  do *equilibrium selection*, "making (4,4,4) the focal point", and the climate paragraph says
  "the cell everyone would like to coordinate on". No claim now rests on risk dominance.
  Confirmed the reviewer's knife-edge arithmetic: R−T = 1 and P−S = 1, so neither equilibrium risk-
  dominates and the optimistic reading genuinely was not in the numbers.
- **A5 — done, via the review's second option.** The intro now states that players' numbers are
  ranks within their own matrix while humanity's sit on one fixed scale across all matrices, and
  that ties are deliberate. A one-line note after the short-run fishing matrix explains why
  humanity gets 3 there and 4 in the long-run matrix. I did not renumber, because renumbering
  would have destroyed the only cross-matrix comparison the post actually wants to make.
- **A6 — done.** The review's replacement paragraph is in, naming (2,2,1) as a surviving Nash
  equilibrium of the long-run game and reframing institutions as equilibrium selection.
- **A7 — done.** L87's "no shift in time horizon changes this" is gone. Replaced with the folk
  theorem correction, separating prize-shrinkage from repetition and conceding that only one of
  the two escape routes has been closed.

## 8. E1–E6 — structure

- **E1 — done.** Both climate matrices cut; replaced with the review's four-sentence prose
  substitute. Saves ~14 lines. The remaining tables are now 2 fishing + 2 AGI (PD and Chicken).
- **E2 — done.** "Cells below read `(You, Others, Humanity)`" added above the first table, with the
  clause about collapsing all other fishers into one "Others" player removing the free-rider
  structure.
- **E3 — done.** PD and stag hunt orderings defined once in the intro, with the invitation to check
  the work.
- **E4 — done.** "collapse toward a Stag Hunt" replaced with the precise version: T falls below R,
  defection stops being dominant, mutual cooperation becomes the payoff-dominant equilibrium of a
  two-equilibrium coordination game, and mutual defection is still an equilibrium of the new game.
- **E5 — not done.** The review only says "consider" the retitle. I left the subtitle as "Why AGI
  is not like climate change" because the new C5 subsection now argues climate is a *weak*
  baseline, which makes "not like climate change" ambiguous in an interesting way rather than
  wrong. **Author task:** your call. "Nukes without the stabilisers" is a better description of
  where the post's weight actually sits.
- **E6 — done.** A version of L97 is now in the second paragraph of the opening ("The beliefs
  holding the game in place don't have to be true; they only have to be believed by the people
  making the build-or-cooperate decision"). The original L97 sentence is preserved verbatim in
  place — see section G below.

---

## Section G — preserved

- **Nuclear weapons section.** All four disanalogy bullets untouched, word for word, including the
  "AGI is nukes with several of the stabilizers missing" line and the closing paragraph. The only
  change is one added sentence naming Jervis's security dilemma, which the review itself requested.
- **The escape hatch.** *Promoted*, as instructed: it was a `####` subsection buried inside "Why
  AGI Is Different"; it is now a top-level `###` section of its own, it carries the post's central
  inequality, and the closing section builds on it. Nothing was cut from it.
- **L97's sentence** — *"These claims are contested in detail, but they don't have to be true to
  drive the game. They only have to be* believed *by the people making the build-or-cooperate
  decision."* — preserved verbatim, in place.
- **"What could change the game"** — all four bullets preserved verbatim; the Armstrong caveat was
  added after them, not woven into them.
- **The prose.** No padding added. Every new passage is either the review's own drafted text or
  written to match the existing register.

## Deliberate omissions

- **B4 (the three "why AGI is different" bullets are weaker than stated).** Not on the apply list,
  so I did not do the full rewrite. But C1's instruction to "name and answer" Askell et al. forced
  half of it, so the issue-linkage counterargument now has its own paragraph after the three
  bullets, with the reason I think it's insufficient (linkage works when the linked stakes are
  comparable, and nothing in the trade relationship is worth what the winner believes they're
  getting). **Author task:** B4's first and third bullets (export controls as resource restriction;
  expanding "no visible degradation") are still outstanding.
- **C2** — folded into C1. L62's "the most pessimistic AGI race models" now names Armstrong et al.
  and Naudé & Dimitri.
- **A1 option 2** and **E5** — see above.

## Outstanding tasks for the author

1. Read Armstrong, Bostrom & Shulman in the original before defending the information result.
2. Decide whether to quote SOFIA 2026's 62.4%-sustainable figure directly instead of my rounded
   "roughly 37% unsustainable".
3. Decide on the E5 retitle.
4. B4 bullets 1 and 3.
5. Consider whether the Chicken subsection should be promoted further — it is arguably the most
   important thing in the post now, and it currently sits mid-document.
