# Changelog — "The Geometry of Governance"

Applying `notes/review-voting-geom.md` to `_posts/technical-posts/2026-01-03-voting-geom.md`.
Site builds clean (`bundle exec jekyll build`).

## Verification done first

Before editing I re-derived every number the review touches (brute force, `python3`):

- **A1 counterexample.** $p = 0.99$ on $(0,0,0)$, $0.01/7$ on each other corner → $H(p) = 0.1089$ bits,
  $\log_2\lvert\mathrm{supp}\,p\rvert = 3$. Confirmed.
- **A5 table.** Exhaustive search over all codebooks of size $k$ at $n=3$: $k=2 \to 0.75$,
  $k=4 \to 0.5$, $k=8 \to 0$. Inverting $R(D) = 3(1 - H_b(D/3))$ gives $D = 0.5219$ at $R=1$,
  $D = 0.1845$ at $R=2$, $0$ at $R=3$. Confirmed.
- **§6.3 worked example.** Exhaustive search over all $\binom{64}{2}$ codeword pairs on the
  4-type, 6-issue electorate gives 1.5. Confirmed optimal, not just antipodal.
- **Anscombe check.** Outcome $(Y,Y,Y)$ with margins 70/70/60; each of the three blocs loses on
  exactly one of three issues, so no bloc loses on a majority of issues. The reviewer is right
  that Anscombe's paradox does not hold in this example.

All arithmetic in the post was and remains correct.

## A — errors

**A1 (H(p) vs log₂|supp p|).** The central fix, touching every place the claim appeared.

- §1: added support size $\lvert\operatorname{supp} p\rvert$ as a defined quantity alongside
  $H(p)$, with a paragraph explaining that they measure different kinds of diversity and that
  §6/§8 turn on the gap.
- Intro (L11): "matches the entropy of voter preferences, $H(p)$" → "matches the **structure**
  of voter preferences"; "capacity falls short of $H(p)$" → "fewer distinct options than the
  electorate has distinct preference profiles".
- §6 principle box: replaced "The ballot's channel capacity should match $H(p)$" with the
  support-size criterion plus the factorisation criterion, and prefaced it with the
  two-quantities paragraph including the 99%/1% counterexample worked through in the author's
  voice (0.109 bits, still misrepresents 1 in 100, still needs eight platforms).
- §8: "must offer a ballot with channel capacity at least $H(p)$" → capacity at least
  $\log_2\lvert\operatorname{supp} p\rvert$, with the explicit statement that the
  right-to-be-heard standard is the support criterion, not the entropy criterion.
- Summary table: column "$H(p)$" → "Profiles actually held" ($2$, $2^c$, $2^n$,
  $\lvert\operatorname{supp} p\rvert$), bits/voter for the general row →
  $\log_2\lvert\operatorname{supp} p\rvert$. This also fixes the review's L251 point (the
  "$\approx c$" entry was only right for fair coins).
- Closing paragraph: "effective dimensionality is the entropy $H(p)$" → support size, with a
  parenthetical noting $H(p)$ is the average-voter figure and the difference is the tail.
- L137/L139 (independence): rewritten so the curse is driven by *how much of the cube is
  occupied*, with independence demoted to "the cleanest way to get there, but not required".
- L202 (2–4 dominant axes): kept the empirical claim but added that principal components are
  neither bits nor a bound on support size, and that what the evidence supports is a coarse
  *coupling* structure, not a small menu.

Two places where the two measures coincide (§3's uniform example, §6.1's four-type example) now
say so explicitly, so the reader can see when the distinction bites and when it doesn't.

**A2 (Ostrogorski).** Section renamed to "The Limits of Unbundling: The Paradox of Multiple
Elections"; the paradox named as Brams, Kilgour & Zwicker (1998) with the compound-majority /
multiple-election aliases. Added a short paragraph stating what Ostrogorski's paradox actually is
(about parties) and why it is not this, keeping Daudt & Rae (1976) as the reference for that case.
Lacy & Niou (2000) added at the UBI-vs-targeted-welfare example. This now matches
`2026-07-17-ballot-design.md`.

**A3 (false "by definition").** Replaced with the honest weaker claim: separability is a property
of an individual ordering, dependence a property of the population distribution; non-separability
usually induces dependence but different voters non-separable in different directions can leave
the marginals independent. Added the counterfactual point (you cannot recover a CP-net from
marginal correlations) and closed with "the paradox *usually* does not arise. 'Usually' is doing
real work in that sentence" instead of "the paradox dissolves". Added the literature paragraph
(Boutilier et al. on CP-nets; Lang & Xia 2009; Ahn & Oliveros 2012) acknowledging §6.2's principle
as a rediscovery.

**A4 (issue list).** §1's list replaced with the figure's three issues, with polarity stated:
$1$ = low tax / minimal welfare / restricted borders. **I did not use the reviewer's suggested
polarity** — see "Disagreements" below.

**A5 (R(D) table).** Added a fourth column, "$D$ permitted by $R(D)$" (0.522 / 0.185 / 0), and
relabelled the third as "Exact optimum, $n=3$". Replaced the "tighter" sentence with the review's
suggested paragraph, adapted: the gap is not slack, closing it would need many voters coded
*jointly*, the applicable theory is one-shot vector quantisation. Also reframed the formula as
readable in both directions so the table follows from it.

**A6 (figure caption).** Applied points 1 and 3 only, plus the requested note that the drawn line
is illustrative: caption now says the cube compresses onto the **two endpoints** of a diagonal,
notes that the dashed line and perpendicular "geometric error" are the continuous spatial picture
while the model assigns to the nearest labelled *corner* under Hamming distance, and notes that
only two of the six orphaned corners are named. Also changed "under high-entropy preferences" to
"when preferences are spread across the cube" (A1 hygiene). The PNG is unchanged — see
Outstanding.

**A7 (notation).**
- L51: "carries exactly 1 bit" → "at most 1 bit", with the fair-coin condition stated.
- Added the source-coding-vs-channel-coding declaration in §3, once, as suggested.
- $H_b(p)$ → $H_b(x)$ with a parenthetical noting $p$ is spoken for.
- The `\\{` "rendering bug": **not applied as written** — see Disagreements.

## B — overclaims

- **B1.** §8's minority paragraph replaced with the narrower/sharper version: codebooks chase
  mass, so the *persistently* misrepresented are small off-axis clusters; whether they coincide
  with demographic minorities is empirical, not a theorem, with the reason to expect overlap kept.
  "Disenfranchisement" → "misrepresentation" throughout §8, with one sentence explaining why the
  distinction matters. The closing paragraph's "predictable minorities" softened to "the small,
  cross-cutting clusters".
- **B2.** New paragraph after the 0.75 result: the numbers assume a benevolent quantiser; real
  parties are competitors; Hotelling–Downs convergence; no generic equilibrium in ≥2 dimensions
  (Plott, McKelvey); real distortion is worse, which is another sense in which this is a lower
  bound.
- **B3.** Added the menu-items clause to §5: $2^n$ options is not the problem, $2^n *mutually
  exclusive* menu items is, and §6 turns on that distinction. "Inescapable dilemma" → "dilemma".
- **B4.** New paragraph in §5 on coalitions: the effective codebook of a parliamentary system is
  the set of feasible coalition programmes, but the enlargement is not voter-controlled — capacity
  up, control down. Written with a nod to MMP since the author lives under it.
- **B5.** Opening paragraph rewritten to the review's framing (record before aggregate; the ballot
  is the recording device). The "issue-by-issue matches the entropy exactly, zero distortion"
  claim is now folded into the condensed §6 opening with the honest caveat that zero distortion
  for a name-your-own-vector ballot is a fact about the §2 definition, not a discovery — the post
  measures expressiveness, not governance quality.
- **B6.** Liquid Democracy: "falls out as a natural refinement" → "a plausible refinement", plus
  the flag that the argument leaves the pure-preference frame and needs an epistemic premise.
- **B7.** L75 converted from rhetorical aside to stated limitation: Hamming is the most forgiving
  loss function available, so every number below is a floor.

## C — unstated assumptions

- **C1.** New paragraph in §2 on equal issue weights: weighted Hamming decouples distortion from
  the bit accounting, neither entropy nor support size knows about salience, and this is the gap
  intensity mechanisms like quadratic voting fill.
- **C2.** New paragraph in §6.2: factoring the ballot to match $p$ needs $p$, and the ballot is
  the only instrument, which the endogeneity argument says distorts what it measures. Forward
  link to `/ballot-design/` with its sharper vocabulary (separability-distortion vs
  menu-distortion, treewidth rather than "clusters").
- **C3.** Added the strategic-reporting caveat in §6.2 naming Gibbard–Satterthwaite, noting
  reporting a profile is less manipulable than choosing among outcomes but not immune.
- **C4.** Thorburn et al. now used in §2 to justify Hamming over Euclidean, phrased so it makes no
  claim about the paper's findings beyond "how well the Euclidean model fits real preference data
  is contested".

## D — structure

- **D1.** §6.1 (aligned) and §6.2 (independent) cut and folded into two sentences of the §6
  opening ("§3 already gave the two extremes... Both are special cases of one principle"). §6
  now opens at the genuinely new material. Old §6.3 → **§6.1**, old §6.4 → **§6.2**; §7's
  cross-references updated to match.
- **D2.** §5's "When does the curse bite?" subsection removed as a heading and merged into §6's
  opening, dissolving the redundancy with the old L145. L141 (endogeneity) moved with it,
  unchanged.
- **D5.** "The mistake at both extremes is the same..." moved from the end of §7 to be its
  opening paragraph, with a half-clause added to hand off to the paradox.
- D3 and D4 covered by A3 and A4 as instructed; §7 was **not** moved before §6.4 (out of scope
  per the brief).

## Deliberately not changed

- Everything in section E: L47's nearest-platform vs winner disambiguation, L57's "at most two
  profiles / strictly stronger" box (now explicitly the thing §6 and §8 build on), L244's
  heard-vs-obeyed caveat (untouched, still in place), L141's endogeneity paragraph (moved intact
  as part of D2, wording unchanged), §6.3's worked example including the 6-issue construction and
  the 1.5 (heading renumbered to 6.1, arithmetic and table untouched).
- Thesis, section count, and section order otherwise unchanged.
- The channel metaphor is kept rather than purged — A7 says it is harmless once declared, so it
  is declared once in §3 and left alone.
- YAML front matter, image path, MathJax delimiters untouched.

## Disagreements with the reviewer

**1. A7's `\\{` "rendering bug" is backwards. Not applied; the opposite fix was applied instead.**

This site's kramdown is configured with `input: GFM` and inline math is left to MathJax's
`tex2jax` at runtime, not processed by kramdown. So kramdown treats `$...$` as ordinary text and
consumes the markdown escape: inline `\{` renders as a bare `{`, which MathJax reads as a grouping
brace and draws nothing. Verified against the built HTML:

- before: `$\{c_1, \ldots, c_k\}$` → `${c_1, \ldots, c_k}$` in `_site` (braces lost)
- after: `$\\{c_1, \ldots, c_k\\}$` → `$\{c_1, \ldots, c_k\}$` (correct)

Display math (`$$...$$`) *is* handled by kramdown and passes through verbatim, so single
backslashes are correct there. The author's original `\\{` at L39 was right; the single-backslash
instances elsewhere were the broken ones. I have therefore normalised **all inline** occurrences
to `\\{` / `\\}` (lines 29, 31, 41, 112, and my new one in §7) and left display math alone. The
reviewer's note that "the PDF build has to patch it" is consistent with this — the PDF pipeline
uses a different markdown processor with different escaping, so the two builds will always
disagree here. Worth a `_plugins` fix or a switch to `\lbrace`/`\rbrace` if you want one source
that works for both.

**2. A4's suggested polarity contradicts §3, §8, and the figure. Used a different one.**

The review proposes $1$ = low tax, minimal welfare, **open borders**, and says "§3 and §8 need no
edits". They do. Under that polarity the Libertarian (low tax, minimal welfare, open borders) is
$(1,1,1)$ — a *codeword*, not an orphan — which destroys both §3's worked example and §8's list of
silenced corners.

I checked the PNG. Its axes are High(Redistrib.)→Low(Market) tax, High(Universal)→Low(Minimal)
welfare, Open(Liberal)→Restricted(National) immigration, with THE LEFT and THE RIGHT at opposite
corners and The Libertarian / The Left-Nationalist as the two named orphans. The polarity that
matches the drawing is $1$ = low tax / minimal welfare / **restricted** borders. That is what I
used. It gives $(0,0,0)$ = The Left, $(1,1,1)$ = The Right, Libertarian = $(1,1,0)$,
Left-Nationalist = $(0,0,1)$ — both at Hamming distance 1 from a codeword, exactly as the argument
needs.

Consequently §3 *did* need two small edits, contrary to the review: the example voters at L73 are
now $(1,1,0)$ and $(0,0,1)$ instead of $(1,0,1)$ and $(0,1,0)$, and the two "voting for $c_A$ /
$c_B$ endorses..." clauses are swapped to match. The distortion table below it is unaffected — both
new corners have $\min$ distance 1, same as the old ones, so $D = 0.75$ is unchanged. §8 needed no
edits: its parenthetical glosses (libertarians = low tax, low welfare, open immigration;
left-nationalists = high tax, strong welfare, closed borders) are already correct under this
polarity.

**3. Minor: the review's A5 table column is mislabelled.** Its header reads "$R(D)$ formula" but
the values 0.522 and 0.185 are *distortions* obtained by inverting $R(D)$ at $R = 1$ and $R = 2$,
not rates. The values are right; I labelled the new column "$D$ permitted by $R(D)$" accordingly.

## Outstanding for the author

1. **Figure redraw (A6 point 2, not applied).** `images/voting-cube.png` still draws a dashed
   party line through the cube with a perpendicular "Geometric Error" drop — the continuous
   spatial model, not the Hamming model in the text. The caption now flags this, but the honest
   fix is to redraw: error indicators as arrows from each orphan corner to its *nearest labelled
   corner*, length one edge. While redrawing, label all six orphaned corners rather than two
   (A6 point 3) — §8's argument is about who they are. There is no generating script for this
   figure under `code/`; it looks like matplotlib 3D, so it will need rewriting from scratch.
2. **Citations I could not fully verify.** I added author, year, title and venue only, and
   deliberately did **not** invent volume or page numbers for: Lacy & Niou (2000, *JTP*);
   Boutilier et al. (2004, *JAIR*); Lang & Xia (2009, *Mathematical Social Sciences*); Ahn &
   Oliveros (2012, *Econometrica*); Hotelling (1929, *Economic Journal*); Plott (1967, *AER*);
   McKelvey (1976, *JET*). Brams, Kilgour & Zwicker carries the full 15(2):211–236 the review
   supplied. Worth a pass with a reference manager before publishing, particularly the Lang & Xia
   venue.
3. **`_bibliography/`.** This post uses a hand-written References list rather than
   `jekyll-scholar`; the list has grown to thirteen entries. If you want `{% cite %}` here it
   would now be worth a `.bib` file.
4. **Consider the review's D3** (moving the non-separability discussion before §6.2 so the
   principle is stated once with its limits known). Out of scope for this pass and it would mean
   restructuring, but the point stands: §7 currently states a principle, undermines it, then
   qualifies it.
