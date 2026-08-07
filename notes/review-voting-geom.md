# Critical review — "The Geometry of Governance"

Post: `_posts/technical-posts/2026-01-03-voting-geom.md`

External critical review. The reviewer brute-forced every quantisation problem in the
post: **all arithmetic checks out** (0.75, 0.5, 0, 1.5, the $H(p)$ values, $2^{30}\approx$1bn,
the 70/70/60 majorities). The problems are in the claims, not the sums.

---

## A. Errors

### A1. The load-bearing claim — "capacity ≥ $H(p)$" — is false. (Highest priority.)

Stated four times: L11, L149, L242, L253/255.

Zero distortion requires the codebook to **cover the support** of $p$, i.e.
$k \geq |\mathrm{supp}\,p|$, i.e. capacity $\geq \log_2|\mathrm{supp}\,p|$ — the
Hartley / Rényi-0 entropy, not Shannon entropy.

Counterexample: $p$ puts 0.99 on $(0,0,0)$ and spreads 0.01 uniformly over the other
seven corners. $H(p) = 0.109$ bits. A two-party ballot has capacity 1 bit $\gg H(p)$ —
and still misrepresents 1% of voters, and needs $k=8$ to reach zero. Capacity
$\geq H(p)$ is neither necessary nor sufficient for the property §8 demands.

**The post already gets this right once, then contradicts itself.** L57:

> "**A two-party system can be lossless only when voter preferences concentrate on at
> most two profiles — which forces $H(p) \leq 1$ bit, but is strictly stronger.**"

That sentence is correct and is the negation of the §6/§8 principle. A sceptical reader
notices at L149 and stops trusting the rest.

**The fix is a gift, not a cost.** There *is* a rigorous sense in which $H(p)$ is right —
Shannon source coding with **variable-rate** ballots: a short menu of common platforms
plus a costly write-in, expected ballot length $\to H(p)$. But that theorem is (a)
asymptotic over jointly-coded voters, and (b) *near*-lossless: it buys $H(p)$ bits by
accepting an $\varepsilon$ failure probability, and the failures fall on the
low-probability tail — precisely the population §8 is about. So the honest version is
**stronger than the one written**:

> Two quantities matter, and conflating them is where most reform arguments go wrong. If
> you want *every* voter represented exactly, the ballot needs $\log_2|\mathrm{supp}\,p|$
> bits — the log of the number of distinct preference profiles that actually occur,
> regardless of how rare. If you only want *average* fidelity, $H(p)$ is the right
> budget, and Shannon's source coding theorem says you can hit it. But the gap between
> the two is not a rounding error: it is exactly the tail, and a ballot designed to
> $H(p)$ is a ballot that has decided in advance which minorities to drop. The
> right-to-be-heard standard is the support criterion, not the entropy criterion.

Then §8's "these are not random voters" becomes a theorem about the design, not a
metaphor. Rewrite the L149 box and the L242/L253 claims around this, and define
$\log_2|\mathrm{supp}\,p|$ at L35 alongside $H(p)$.

Downstream consequences of the same conflation:

- **L202**: "roughly 2–4 dominant axes" → "The optimal number of distinct policy packages
  is correspondingly modest." Number of principal components ≠ bits of entropy ≠ log
  support size. Two components explaining 80% of variance does not mean $H(p)\approx 2$,
  and certainly doesn't bound the support.
- **L251**: "Clustered ($c$ axes) | $\approx c$" — only if each axis is a fair coin. A
  cluster split 90/10 contributes 0.47 bits but still needs 2 codewords.
- **L137/L139**: "The curse bites when preferences are **independent** across issues."
  Independence is far stronger than needed — the curse bites whenever the support is
  full, which requires no independence at all.

### A2. The Ostrogorski paradox is misnamed. (L216–228)

The example given — issue-by-issue majorities produce $(Y,Y,Y)$, a bundle **zero voters**
hold — is the **paradox of multiple elections** (Brams, Kilgour & Zwicker 1998, *Social
Choice and Welfare* 15(2):211–236), also called the compound-majority or multiple-election
paradox.

Ostrogorski's paradox is about *parties*: a party preferred by a majority of voters (each
voting for whichever party agrees with them on more issues) loses on a majority of issues,
or vice versa. There are no parties in the post's example. Anscombe's paradox (1976) is a
third, distinct thing — a majority of voters on the losing side of a majority of issues —
and the reviewer checked: it does **not** hold here (every bloc loses on exactly one of
three).

**Your own later post gets this right** — `2026-07-17-ballot-design.md` L15 says "able to
elect a package a majority dislikes once they are coupled (the multiple-election
paradox)". Make this post match.

Fix: rename, cite Brams–Kilgour–Zwicker, keep Daudt & Rae parenthetically as the related
Ostrogorski result. Add Lacy & Niou (2000), "A Problem with Referendums," *JTP* — the
canonical treatment of non-separable preferences in issue-by-issue referendums, which is
exactly the "UBI vs targeted welfare" example at L212.

### A3. The §7 rescue rests on a false "by definition". (L226)

> "**Non-separable issues are, by definition, not conditionally independent — and
> therefore belong in the same cluster.**"

Not a definition; a claim, and false in the direction the argument needs. Separability is
a property of an individual voter's **preference ordering** (does my ranking on issue $i$
depend on the outcome of $j$?). Conditional independence is a property of the
**population distribution $p$ over realised top choices**. Different objects, and the map
between them is not injective.

Counterexample: let every voter be non-separable in $(A,B)$ — each wants exactly one of
the two, so each individual's admissible top choices exclude one corner. But different
voters exclude different corners. Mix four such types so the population's top choices are
uniform over $\{0,1\}^2$: marginals independent, dependence zero, §6.4 diagnostic sees
nothing. Yet every voter is non-separable, and issue-by-issue voting will burn them.

Deeper problem: the diagnostic at L200/L226 is a **correlation test on observed ballots**,
and non-separability lives in counterfactual structure (what I'd want *if* the other
passed) that observed ballots do not contain. You cannot recover a CP-net from marginal
correlations.

Suggested replacement for L226–228:

> Non-separability and statistical dependence are related but not the same: the first is a
> property of an individual's preference ordering, the second of the population's
> distribution over top choices. Non-separable preferences usually *induce* dependence — a
> voter who wants exactly one of UBI and targeted welfare never lands on the (1,1) corner
> — so the §6.4 diagnostic will often catch it. But it can be fooled: an electorate in
> which every voter is non-separable can still show independent marginals if different
> voters are non-separable in different directions. Correlation between ballots is
> evidence about coupling, not proof of its absence. Detecting non-separability properly
> requires eliciting conditional preferences, not just observing marginals — a strictly
> harder measurement problem than anything else in this post.

This weakens §7, but "the paradox dissolves" (L228) was overclaiming anyway. Literature to
name: Boutilier et al. on CP-nets; Lang & Xia (2009), "Sequential composition of voting
rules in multi-issue domains"; Ahn & Oliveros (2012), "Combinatorial Voting,"
*Econometrica*. §6.4's "conditional-independence graph" principle is a rediscovery of this
field's central idea — say so, it costs nothing and buys credibility.

### A4. The issue list changes silently between §1, §3, and the figure.

L21–25 defines the issues as **wealth tax / nuclear power / UBI**. But L73 glosses
$(1,0,1)$ as "a 'Libertarian' who wants low taxes and minimal welfare but open
immigration" — immigration isn't one of the three, nuclear power has vanished, and the
polarity flipped ($1$ = *low* tax, whereas L23 asks "Progressive Wealth Tax? (Y/N)"). The
figure's axes read TAXES / WELFARE / IMMIGRATION, so §3 and the figure agree and §1 is the
odd one out. L61 is also self-inconsistent under §1's list: $(0,0,0)$ = "The Left" would
be no wealth tax, no nuclear, no UBI.

Fix: change L23–25 to the figure's three issues — **Wealth Tax? / Welfare Expansion? /
Open Immigration?** — with $1$ = low tax, minimal welfare, open borders stated explicitly,
so $(0,0,0)$ is genuinely "The Left" as drawn. Then §3 and §8 need no edits.

### A5. The $R(D)$ formula and the table beneath it are inconsistent. (L104–116)

L106: "To achieve distortion $D$, you need at least $R(D)$ bits — i.e., at least
$2^{R(D)}$ parties." The table then lists 0.75 / 0.5 / 0 — the **exact finite-$n$
quantiser optima**, not values of the stated formula:

| $k$ | $R$ | Table (exact VQ optimum, verified) | $R(D)$ formula |
|---|---|---|---|
| 2 | 1 | 0.75 | 0.522 |
| 4 | 2 | 0.5 | 0.185 |
| 8 | 3 | 0 | 0 |

So the formula is introduced and immediately not used, and a reader trying to reproduce
the table from it will fail. L116 acknowledges this with the wrong word — "the
rate–distortion bound is asymptotic over many blocks and is **tighter** than what any
finite codebook attains". "Tighter" reads as backwards; $R(D)$ gives a *lower* (more
optimistic, unattainable) distortion. "Blocks" also needs unpacking: the blocks would be
**many voters coded jointly**, which no ballot can do, since each voter maps to a codeword
independently.

Suggested replacement for L116:

> The middle column is the exact optimum over all codebooks of size $k$ for $n=3$; the
> right column is what asymptotic rate–distortion theory says is achievable. The gap is
> large, and it is not slack in the analysis — closing it would require coding many voters
> *jointly* into a single codeword, which no ballot can do, since every voter must
> independently select from the same fixed menu. Rate–distortion theory gives a valid
> lower bound on the distortion of a $k$-party system, but a badly loose one at $n=3$. The
> relevant theory here is one-shot vector quantisation, not Shannon's asymptotic result.

Adding the right-hand column makes the point better than the prose does. Cover & Thomas
Ch. 10 is the correct chapter for the 2nd edition.

### A6. The figure illustrates a Euclidean model, not the Hamming model in the text.

The figure draws a dashed "1D Party Line" through the cube and marks "Geometric Error" as
a **perpendicular drop from an orphan corner onto that line** — the continuous
spatial-voting model. The text's model is **nearest of two codewords under Hamming
distance**: the orphan snaps to a *vertex*, not to a point on a segment. L17's caption
reinforces the wrong reading ("compresses this cube onto a single **diagonal line**").

Fixes in order of value:
1. Caption: "compresses this cube onto the **two endpoints** of a single diagonal — voters
   do not land somewhere along the line; they land on one of two corners."
2. Redraw error indicators as arrows from each orphan corner to its *nearest labelled
   corner*, length 1 edge.
3. The caption says 6 of 8 positions are unrepresented but the figure names only 2 and
   greys the rest. Label all six — §8's argument is about who they are ("eco-socialists,
   religious progressives", L236).

### A7. Smaller technical points

- **L51**: "the voter's ballot carries **exactly 1 bit**" → at *most* 1 bit; equal only if
  the vote is a fair coin across the electorate. L11's "$\log_2 k$ bits of capacity" is
  fine — capacity is the right word — so make L51 consistent with it.
- **Channel vs source coding.** The post uses channel language ("1-bit channel",
  "capacity", "routing an $n$-bit signal through a 1-bit channel") for what is entirely a
  **lossy source coding / quantisation** problem. A ballot is a noiseless encoder with a
  $k$-symbol alphabet, not a noisy channel. Harmless if declared once — add at L51:
  "Throughout, 'capacity' means $\log_2$ of the number of distinct ballots a voter can
  cast; the ballot is a noiseless encoder, and the relevant theory is lossy source coding,
  not channel coding."
- **L106 notation collision**: $H_b(p) = -p\log_2 p - (1-p)\log_2(1-p)$ — $p$ already
  denotes the electorate distribution from L29. Rename the argument to $x$ or $\delta$.
- **L39 rendering bug**: `$\\{c_1, \ldots, c_k\\} \subset \{0,1\}^n$` — doubled
  backslashes inconsistent with `\{0,1\}` in the same expression. (Confirmed: this is the
  one the PDF build has to patch.)

---

## B. Overstated / unsupported

### B1. The minority-status paragraph is the weakest in the post. (L240)

Three problems. (i) "Whoever sits off that axis loses — and the people off that axis tend
to be those whose interests don't align with the majority bundle" is **circular**: "off
the axis" is *defined* as not aligning with the dominant bundle. (ii) The mechanism is
about **preference geometry** and says nothing about demographic minority status;
majority-group voters are frequently off-axis, and in several Western electorates the
left-economics/right-social quadrant is a *plurality*. (iii) The model implies something
sharper and *narrower*: if an off-axis cluster were large, distortion-minimising placement
(or electoral competition) would move a codeword toward it. So the model predicts the
silenced are **numerically small** clusters. Also "disenfranchisement" means denial of the
franchise; the post means misrepresentation.

Suggested replacement:

> The model says something narrower but sharper than "minorities lose."
> Distortion-minimising codebooks chase mass: any off-axis cluster large enough to be worth
> a platform will eventually get one. What the geometry guarantees is that the
> *persistently* misrepresented are the numerically small, off-axis clusters — small enough
> that no competitor gains by moving toward them, and cross-cutting enough that neither
> existing platform covers them. Whether those clusters coincide with demographic
> minorities is an empirical question, not a theorem. But there is a reason to expect it
> often does: a group whose distinctive policy concerns cut across the dominant cleavage is
> by construction off-axis, and being small is what made the cleavage get drawn elsewhere
> in the first place.

### B2. Party positions are treated as chosen by a benevolent quantiser. (Load-bearing, unstated.)

Every distortion number assumes codewords placed to **minimise expected distortion** —
Lloyd's algorithm run by a designer who wants voters represented. Real parties are
competitors trying to win. This cuts *against* the post's optimism:

- Hotelling–Downs convergence: two vote-maximising parties move *toward each other*,
  collapsing the codebook's spread. In the limit both codewords coincide — a 1-bit ballot
  carrying 0 bits of policy difference, distortion strictly worse than the VQ optimum.
- In ≥2 dimensions there is generically **no** majority-rule equilibrium: Plott (1967)
  knife-edge conditions, McKelvey (1976) chaos theorem. "Optimal 2-party placement" at L77
  is not a prediction about any actual political system.

Add after L77: "These are the placements a benevolent designer would choose. Parties are
not benevolent designers — under Downsian competition they converge toward each other
(Hotelling 1929; Downs 1957), and in two or more dimensions no equilibrium platform pair
generically exists at all (Plott 1967; McKelvey 1976). Real distortion is therefore *worse*
than the numbers below, which is another sense in which this analysis is a lower bound."

### B3. "We cannot 'party' our way out" (L133) is true; "inescapable" (L128) overstates.

The curse is a curse only if the ballot is a **menu of mutually exclusive options**.
Approval voting over $k$ parties carries $k$ bits, not $\log_2 k$. Ranked ballots carry
$\log_2 k!$. MMP gives two votes. §6 does supply the resolution, but a reader who knows
approval voting objects before reaching it. One clause fixes it: "...impossible. Not, note,
because $2^n$ *options* is impossible — a ballot with $n$ checkboxes offers exactly that
many — but because $2^n$ mutually exclusive *menu items* is. §6 turns on that distinction."

### B4. Real multiparty systems output coalitions, not one of $k$ platforms.

The effective codebook of a parliamentary system is the set of feasible coalition
programmes — combinatorially larger than $k$. The most obvious objection from a
comparative-politics reader, and close to home given NZ's MMP. The honest answer is
interesting: coalition bargaining enlarges the codebook but the enlargement is *not
voter-controlled*, so it raises representational capacity while lowering the voter's
control over which codeword they get. A distinction the framework can express.

### B5. Aggregation vs representation: the opening promises one and delivers the other.

L9 promises "how do you aggregate the distinct preferences of millions of people into a
single output — **policy**?" But L47 defines distortion as distance to the *nearest
available platform*, not to the winner. That's the right clarification — but it means the
post measures **ballot expressiveness**, not governance quality. Consequence at L165:
"Issue-by-issue voting matches the entropy exactly: 3 bits in, 3 bits out, **zero
distortion**." Under L47's definition, direct democracy trivially achieves zero distortion
for *any* $p$, because your nearest available platform is your own vector. Not a finding —
the definition. Which makes "unbundling wins" (L167) less impressive than it reads.

Fix L9: "...at its core, governance faces a **compression problem**: before you can
aggregate preferences you have to *record* them, and the ballot is the recording device.
This post is about the recording step — how much of a voter's preference a ballot can
physically carry — and about who gets truncated when it can't carry enough."

### B6. "Liquid Democracy falls out as a natural refinement" (L204). It doesn't.

Asserted, not derived, and the justification breaks the model: "they **import a more
informed codebook** for dimensions they don't follow." The post models pure *preference*
aggregation, in which nobody knows your preferences better than you. The delegation
argument silently switches to an epistemic-democracy frame. Either drop it or flag the
switch: "Note this argument leaves the pure-preference frame: delegation helps only if
there are *facts* about a policy domain that a delegate knows better, not merely
preferences. That is a different — and contestable — model of what voting is for."

### B7. L75 quietly repudiates the post's own loss function.

> "Hamming distance 1 makes this sound like a small error. From the voter's side it is total."

If Hamming understates harm, every number understates it. L13's lower-bound framing partly
covers this, but as written it reads as a rhetorical escape hatch. Convert to a stated
limitation: "Hamming charges 1 for this. The voter would charge more — a wrong vote cast in
your name on an issue you care about is not a fraction of a grievance. Hamming is the *most
forgiving* loss function available; the numbers below are floors, not estimates."

---

## C. Unstated assumptions doing real work

1. **Equal issue weights.** Hamming charges the same for every issue. A voter with one
   overriding concern and two she's indifferent about is badly modelled. Weighted Hamming
   is the obvious fix but it **decouples distortion from the bit accounting** — $H(p)$
   doesn't know about salience — arguably the deepest limitation of the framing, and
   exactly the gap intensity mechanisms (quadratic voting) exist to fill. Worth one honest
   paragraph; the first objection a mechanism-design reader raises.
2. **The designer must know $p$.** §6 requires knowing the conditional-independence
   structure, but the ballot is the only instrument for measuring it — and L141 already
   argues the ballot *distorts* what it measures. The post makes this point against
   two-party systems without noticing it undercuts its own recommendation. This is what
   `2026-07-17-ballot-design.md` solves (estimate the dependency graph from Polis-style
   votes) — add the caveat *and* the forward link. That paper also supplies sharper
   vocabulary (separability-distortion vs menu-distortion, treewidth rather than "clusters").
3. **No strategic reporting.** Gibbard–Satterthwaite never mentioned. Reporting a
   preference profile is less manipulable than choosing among outcomes, but a per-cluster
   ballot with known aggregation is manipulable, and a social-choice reader expects
   acknowledgement.
4. **Thorburn et al. is cited but never used.** A paper about error in the Euclidean
   preference model — highly relevant to A6 and to the Hamming-vs-Euclidean choice, but it
   appears only in the reference list. Use it in §2 to justify Hamming over Euclidean, or
   drop it.

---

## D. Structure and clarity

1. **§6.1 and §6.2 duplicate §3's two subsections almost exactly.** L155 restates L61–65
   in content; L163 restates L71–96. ~35 lines of repetition landing where the post should
   be accelerating. Cut both to two sentences ("§3 gave the two extremes... Both are
   special cases of one principle.") and open §6 at what is currently §6.3 — the genuinely
   new material.
2. **§5's "When does the curse bite?" pre-empts §6** and makes L145 redundant. Merge into
   §6's opening.
3. **§7's placement is odd.** An objection to §6.2 arriving after §6.4's synthesis, whose
   resolution (A3) doesn't hold. Move the non-separability discussion *before* §6.4 so the
   principle is stated once with its limits already known, rather than stated, undermined,
   then patched.
4. **The two-issue-set switch (A4) actively confuses** readers who scroll back to check
   what $(1,0,1)$ means. Fixing A4 fixes clarity, not just correctness.
5. Stylistic: L230 ("The mistake at both extremes is the same...") is the best-turned
   paragraph in §7 and is buried after the paradox discussion. Would make a strong section
   opener.

---

## E. What works — don't touch

- **L47**, distinguishing distortion-from-nearest-platform vs distortion-from-winner.
  Exactly the right disambiguation, made early and unprompted. Most posts never make it.
- **L57**, the "at most two profiles... strictly stronger" box. The correct statement, and
  the one to build §6 and §8 on (A1).
- **L244**, the heard-vs-obeyed caveat. Strongest paragraph in the post; pre-empts the most
  common objection. Keep exactly where it is.
- **L141**, endogeneity — preferences appearing correlated because the party system only
  offers correlated bundles. Genuinely good, rarely stated.
- **L13**, the lower-bound framing. Right instinct; invoke it more often (B7).
- **§6.3's worked example.** The 6-issue two-cluster construction is the clearest thing in
  the post, and the 1.5 was verified by exhaustive search over all $\binom{64}{2}$ codeword
  pairs — exactly optimal, not just the antipodal choice.
- **All arithmetic.**

---

## Top five

1. Fix the $H(p)$ vs $\log_2|\mathrm{supp}\,p|$ conflation (A1) — and use the fix to
   *strengthen* §8.
2. Rename the Ostrogorski paradox to the paradox of multiple elections (A2), matching your
   own later post.
3. Replace the false "by definition" in §7 (A3) with the honest weaker claim.
4. Reconcile the §1 issue list with §3 and the figure (A4).
5. Add the $R(D)$ column to the §4 table and fix "tighter" (A5).

One file-level note: `2026-07-17-ballot-design.md` and the linked paper supersede large
parts of §6 and §7 with a more rigorous treatment. Whatever else changes, this post should
link forward to it.
