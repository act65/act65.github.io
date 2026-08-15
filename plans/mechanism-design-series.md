# Plan: a first-principles series on mechanism design, inverse game theory, and collective decision making

Scratch planning file. Posts live in `_drafts/mechanism-design/`, permalink prefix
`/mechanism-design/`. Follows the `autoint/` pattern (topic folder + lit-review post),
and the `/governance-mechanisms/` pattern for cross-linking (shared prefix, mutual links,
no site-level series machinery — that was tried and rejected).

---

## 1. What already exists, so the series doesn't repeat it

**Published, closest to the topic:**

| Post | What it already does | Relation to the series |
|---|---|---|
| [Designing behind the veil](/governance-mechanisms/) | The nested SUF → mechanism decision; three layers (formation / elicitation / aggregation); minimal settling | The *philosophical* front door. The new series is the *technical* one. Should link both ways. |
| [A Decision-Theoretic Take on Social Choice](/sct/) | Cardinal utilities, L1 vs L2 normalisation, dilution, Arrow-escape-via-cardinal | Overlaps A4/A5 and B2. See §6 — the normalisation question is exactly what distortion theory measures, and that follow-up is unwritten. |
| [The Geometry of Governance](/voting-geom/) | Rate–distortion view of parties; factorisation; multiple-election paradox; "the right to be heard" | §8 is an informal statement of a *justified representation* axiom. B3 gives it its formal home. |
| [Ballot Structure from the Preference-Dependency Graph](/ballot-design/) | Ballots as graphical-model structure selection | B1 is the missing foundation under it: dimensionality is the design variable. |
| [A Market for 'Truth'](/market-politics/), [Global coordination via game theory](/agi-game/), [Tax optimisation as an adversarial game](/adversarial-tax-setting/) | Game-theoretic framing, prediction markets | Reference points, not overlaps. |

**Drafts already in flight that this series absorbs or supersedes:**

- `_drafts/technical-posts/2025-07-20-gov-elucid-space.md` — the five-part
  (eligibility / power / expression / aggregation / temporality) design-space framework.
  This is good and shouldn't be lost. It fits naturally as the bridge post between Arc B
  and Arc C, or as the intro to C4. It currently opens with a reference to a "DAO Proving
  Ground" post that doesn't exist.
- `_drafts/technical-posts/2026-06-08-tech-gov-reading.md` — an empty reading-course stub.
  §5 below should just replace it.
- `_drafts/inbetween-posts/2026-07-19-apportionment.md`, `2026-07-19-prices-vs-quantities.md`,
  `2026-02-15-public-good.md` — adjacent, keep separate.
- `_drafts/old/2026-05-14-mechanism-design.md` — the essay-register version of "every set of
  rules implicitly optimises for something". That sentence is the *thesis of Arc C*; the
  new series is the technical discharge of it.

**In `~/Documents/repos/govern-mechanisms`:** the `govern/` rule library
(aggregation / expression / eligibility / power / temporal / ties), the `ballot/` package
with real Polis datasets, the 8-direction research agenda, and two flagship paper drafts.
Arc C4 and Arc D1 are the posts that make that code visible.

---

## 2. What the series is for

Three things it does that the existing writing doesn't:

1. **Builds the vocabulary the essays already assume.** The governance-mechanisms series
   uses "mechanism", "strategyproof", "Arrow", "surrogate loss for a social objective" as
   load-bearing terms without ever defining them. This series is the thing to link to.
2. **Takes the inverse direction seriously.** The research agenda's bottom-up half
   ("read the implicit SUF off an existing mechanism") has a large, mostly-unread literature
   behind it — revealed preference, inverse game theory, Roberts' theorem. Arc C is the part
   of this series that isn't available anywhere else in this shape.
3. **Establishes what's actually known before proposing anything.** Several existing posts
   propose a fix (L2 normalisation, dependency-graph ballots) to a problem the literature
   has a named, quantified treatment of. Writing the foundations first makes the proposals
   land harder, not softer.

**Register.** Tutorials, so theorems get stated as theorems. But the framing and the
"why this matters" paragraphs should keep the existing voice — tentative, no confident
claims about what should be done. The pattern that works well in `mean.md`: open with
"here are some things I found surprising", then be precise.

---

## 3. The arc

Sixteen posts across four arcs. That's a menu, not a commitment — §4 has the cut.

### Arc A — Foundations: the information problem

**A1. What a mechanism actually is** — `/mechanism-design/what-is-a-mechanism/`

The setup, built from nothing: agents, private types, an outcome space, a social choice
function, a game form, an equilibrium concept. The central observation to earn: *nothing
here is hard until information is private*. If a planner knew everyone's type, mechanism
design would be optimisation. Then the **revelation principle** — a theorem about search
spaces, which is the framing a CS reader will find satisfying: whatever any mechanism
achieves in equilibrium, some direct truthful mechanism achieves. It collapses an
unbounded space of game forms into a space of functions with a constraint.
Worked example throughout: three flatmates and one room.

**A2. Two worlds: with money and without** — `/mechanism-design/money/`

The fork in the road that explains why auction theory has clean positive results and
voting theory has impossibilities. With transferable utility: Vickrey → Clarke → Groves →
VCG, derived rather than stated, then Myerson's revenue-optimal auction as the second
canonical result. Without: the same questions become Gibbard–Satterthwaite. The honest
question at the end — what exactly does politics buy by refusing to price votes, and what
does it pay? (Sets up B5.)

**A3. Strategyproofness is a menu** — `/mechanism-design/menus/`

The **taxation principle**: a mechanism is strategyproof iff each agent faces a menu of
options that does not depend on their own report, and gets their favourite from it. This
reframing makes strategyproofness geometric rather than axiomatic, and makes most
strategyproofness proofs one line. Then the cleanest positive result in the no-money
world: **Moulin (1980)** — on single-peaked domains the strategyproof, anonymous,
efficient rules are exactly the generalised medians with phantom voters. A whole family,
constructively described. This is the post that shows impossibility is domain-dependent.

**A4. Arrow, from the top** — `/mechanism-design/impossibility/`

The **ultrafilter proof** (Kirman–Sondermann 1972): an Arrovian welfare function
corresponds to an ultrafilter on the set of voters; on a finite set every ultrafilter is
principal; a principal ultrafilter is a dictator. This is the "first principles" proof —
it says what Arrow's theorem *is* rather than verifying it. Bonus: with infinitely many
voters you get a non-principal ultrafilter — an "invisible dictator" — which is a nice
sanity check on what finiteness was doing. Then Gibbard–Satterthwaite as a relative,
Sen's liberal paradox as the one that bites differently, and **judgement aggregation**
(List–Pettit, Dietrich–List) as the generalisation that subsumes all of them — worth
naming because the multiple-referendum paradox in `voting-geom` is a judgement-aggregation
result and the field has a name.

**A5. Five ways out** — `/mechanism-design/escapes/`

The map post. Each escape from impossibility opens a real subfield:

| Escape | Give up | Where it leads |
|---|---|---|
| Randomise | determinism | random dictatorship, maximal lotteries, sortition (B4) |
| Restrict the domain | universality | single-peaked, median rules (A3), CP-nets, ballot design |
| Go cardinal | ordinality, non-comparability | score voting, QV (B5), the SUF framework |
| Approximate | exactness | distortion (B2) |
| Make manipulation hard | worst-case guarantees | Bartholdi–Tovey–Trick, and why this escape is the weakest |

The honest note this post should carry: the last row is where a lot of 2000s COMSOC went
and it has largely not held up — worst-case hardness doesn't stop typical-case manipulation.

### Arc B — Collective decision making

**B1. One dimension is easy, two is chaos** — `/mechanism-design/dimensions/`

Black's median voter theorem in 1D. Then **McKelvey (1976)**: in two or more dimensions,
generically the majority-rule top cycle is the *entire space* — an agenda setter can drive
the outcome anywhere by choosing the sequence of pairwise votes. So "the will of the
majority" is well-defined in 1D and essentially undefined above it. The design consequence
is the one the existing writing needs: *the dimensionality of the issue space is a design
variable, not a given*, which is what `ballot-design` is really about, and what parties do
in `voting-geom` (a party system is a projection to low dimension). Plott's symmetry
conditions for when a core exists at all.

**B2. How bad is a ranking?** — `/mechanism-design/distortion/`

**Distortion** (Procaccia–Rosenschein 2006): the worst-case ratio between the social
welfare of the winner an ordinal rule picks and the welfare of the best outcome. This is
the *surrogate-loss gap* from the framework post, made a number. Then **metric
distortion** (Anshelevich et al. 2015) and its resolution — Gkatzelis–Halpern–Shah 2020
give a rule with distortion exactly 3, matching the lower bound. Plus the
distortion–communication tradeoff (Caragiannis–Procaccia), which quantifies "how much
should we ask voters to say".

This is the highest-value tutorial in Arc B, for two reasons: it directly answers the
question the framework post poses and leaves open, and it is the right frame for revisiting
the L1-vs-L2 argument in `sct`.

**B3. The right to be heard, formally** — `/mechanism-design/proportionality/`

The proportionality literature that `voting-geom` §8 was reaching for without knowing it:
**justified representation** and its strengthenings (JR / PJR / EJR, Aziz et al. 2017),
the **core** for committee selection, and the **method of equal shares** (Peters,
Pierczyński, Skowron) — which is simple enough to teach in a paragraph, has an EJR
guarantee, and is actually deployed in participatory budgeting. Then Moulin's
**proportional veto core**, connecting to the existing PVC work. Peters–Skowron on
proportionality vs welfarism is the tension worth ending on: you cannot have both, and
the framework's SUF-maximising stance quietly picks a side.

**B4. Flip a coin** — `/mechanism-design/lotteries/`

Gibbard (1977) on strategyproof random rules. **Maximal lotteries** (Fishburn 1984;
Brandl–Brandt–Seedig) — Condorcet-consistent, well-axiomatised, and barely known outside
COMSOC. Sortition: Flanigan et al. (Nature 2021) on selecting representative citizens'
assemblies, which is a real deployed algorithm. The theme: randomisation buys
strategyproofness and proportionality cheaply, and is systematically underused.

**B5. Buying influence** — `/mechanism-design/quadratic/`

Quadratic voting derived rather than asserted: why quadratic and not linear or cubic, what
the large-population efficiency result needs, and the three assumptions that break it
(collusion, wealth effects, and the fact that the efficiency result is about *aggregate*
welfare with money weighting). Pairs with A2. The `notes.md` gini-ratio idea
(`gini(tokens paid) / gini(votes)`) belongs here.

### Arc C — The inverse problems

This is the part that isn't written elsewhere. Its thesis is the sentence from
`_drafts/old/2026-05-14-mechanism-design.md`: *every set of rules implicitly optimises for
something, whether anyone designed it to or not.* Arc C asks whether you can recover that
something, and the answer is a qualified no with an interesting structure to the failure.

The important upfront move: **three inverse problems get conflated and shouldn't be.**

| | Observe | Infer | Field |
|---|---|---|---|
| Inverse decision theory | one agent's choices | their utility | revealed preference (C1) |
| Inverse game theory | equilibrium play | everyone's payoffs | inverse game theory / MAIRL (C2) |
| Inverse mechanism design | a mechanism's input–output map | the objective it maximises | mostly open (C3) |

The third is the one the research agenda needs, and it's the least developed. Its "agent"
is the mechanism, its "behaviour" is the social choice function, and its "reward" is the SUF.

**C1. Revealed preference: the original inverse problem** — `/mechanism-design/revealed-preference/`

Samuelson (1938) and the weak axiom. **GARP**, and then **Afriat's theorem** (1967): a
finite set of observed choices is rationalisable by *some* well-behaved concave monotone
utility iff the data satisfy cyclical consistency — and the proof is constructive, it hands
you the utility. This is the template for everything in Arc C, and it establishes both
halves of the pattern: a crisp rationalisability condition, and massive
underdetermination (Afriat's construction is one of infinitely many). Varian (1982) for
the nonparametric machinery. Worth stating plainly what Afriat means for the bottom-up
programme: *the question "what does this mechanism maximise" almost always has an answer,
so the interesting question is what constrains the answer set.*

**C2. Inverse game theory** — `/mechanism-design/inverse-game-theory/`

Infer payoffs from observed play, assuming the observations are (approximate) equilibria.
The central fact is **underdetermination**: many games rationalise the same equilibrium.
The devices that restore identification are the content — off-equilibrium observations,
bounded-rationality or entropy-regularisation assumptions (which turn a set-valued problem
into a likelihood), and multiple observations across varied conditions. Connect to inverse
reinforcement learning, which is the same problem with different vocabulary and a much
larger literature.

**C3. What does this institution maximise?** — `/mechanism-design/inverse-mechanism-design/`

The core post. Two classical results are the frame:

- **Roberts' theorem (1979).** On an unrestricted quasilinear domain with ≥3 outcomes,
  every dominant-strategy-implementable social choice function is an *affine maximiser*:
  $\arg\max_a [\sum_i w_i v_i(a) + \kappa(a)]$. So on unrestricted domains the inverse
  problem is *solved and boring* — the implicit objective is always weighted utilitarian.
  Which means: **the inverse question is only interesting on restricted domains**, and that
  is a precise statement of where to look.
- **Maskin monotonicity.** From the other direction: which social choice rules are Nash
  implementable at all. Monotonicity is necessary; with no-veto-power and $n \geq 3$ it's
  sufficient. This bounds which SUFs are even reachable by a mechanism, which the top-down
  half of the agenda needs and currently doesn't use.

Then the modern computational version: Data-Driven Mechanism Design via Multi-Agent
Revealed Preferences (2404.15391), and differentiable inverse mechanism learning.

**C4. Worked example: reading the objective off a voting rule** — `/mechanism-design/reading-objectives/`

The empirical post, using `govern/`. Take plurality, Borda, Copeland, PVC, MMP; generate
preference profiles; fit an SUF whose argmax matches each rule's output; report what's
identifiable and what isn't. The negative results are the interesting content — where the
fit is poor, the mechanism isn't maximising anything nice, which is itself a finding. This
is also the natural home for the five-dimension design-space framework currently sitting in
`gov-elucid-space.md`.

Honest scoping note: this post needs code that mostly doesn't exist yet. It's the one to
schedule last, or to publish as an incomplete experiment with the negative results shown.

### Arc D — Where it goes

**D1. Automated mechanism design** — `/mechanism-design/automated/`

Three eras: Conitzer–Sandholm's LP formulation (2002), the sample-complexity /
learning-theory phase (Balcan–Sandholm–Vitercik), and **differentiable economics**
(RegretNet and successors) — parameterise the mechanism as a network, hard-code the easy
constraints in the architecture, enforce strategyproofness with a Lagrangian penalty. What
this buys and what it gives up: approximate incentive compatibility is a genuinely
different object from the exact kind, and the field is not always careful about it.
Curry et al.'s 2025 survey is the spine.

**D2. Alignment is a social choice problem** — `/mechanism-design/alignment/`

RLHF and DPO as preference aggregation rules that nobody chose deliberately. The specific
result worth the post: Bradley–Terry–Luce preference modelling over heterogeneous
annotators implicitly performs something Borda-like, which inherits Borda's known failures
(clone sensitivity, no Condorcet consistency). Then the axiomatic critiques and the
distortion-of-alignment work. This is the most topical post in the series and the easiest
to place in front of an audience that isn't already reading about voting.

**D3. Designed or evolved?** — `/mechanism-design/designed-or-evolved/`

The counterweight, and the one that partly discharges the burden the framework post sets
itself in §3. Hayek's constructivist-rationalism objection says the knowledge required to
design an aggregation mechanism is unavailable in principle. **Ostrom** is the reply that
isn't usually made: her design principles for common-pool resources were *extracted from
institutions nobody designed*, by fieldwork, and they generalise. So the method isn't
"specify and build", it's "observe what survived and characterise it" — which is Arc C's
inverse problem carried out by anthropology instead of regression. Whether that's a real
reply or a redescription is the post's open question.

**Lit review** — `/mechanism-design/lit-review/` — §5 below, as a standing post that gets
updated. Replaces `2026-06-08-tech-gov-reading.md`.

---

## 4. If the series is cut down

**The six that carry it:**

1. **A1** — what a mechanism is. Nothing works without it.
2. **A4** — Arrow from the top. The ultrafilter proof is a good enough post to stand alone.
3. **A5** — five ways out. Highest utility-per-word; a map readers will return to.
4. **B2** — distortion. Answers the open question in the framework post.
5. **C1** — revealed preference / Afriat. The foundation for the whole inverse programme.
6. **C3** — inverse mechanism design. The post that only this blog would write.

That's a coherent short series: what the problem is, why it's impossible, how people escape,
how to measure the escape, and then the inverse direction in two posts.

**Write-order suggestion**, which is not the reading order: **A5 first**. It's the map, it's
the most reusable, and writing it will tell you which of the others you actually want.
Then C1 and C3 while the inverse material is fresh, then A1 and A4, then B2.

**Highest independent value if you only write one:** D2 (alignment as social choice) for
reach, C3 for originality.

---

## 5. Reading list

### Start here (books and surveys, all free online)

- **Brandt, Conitzer, Endriss, Lang, Procaccia (eds), *Handbook of Computational Social
  Choice* (CUP 2016)** — the field's reference. Ch. 1–2 (intro, tournament solutions),
  6 (barriers to manipulation), 10 (fair allocation). You already have the Conitzer intro
  chapter in `notes/lit-review.md`; the full handbook is better.
- **Nisan, Roughgarden, Tardos, Vazirani, *Algorithmic Game Theory* (CUP 2007)**, Part II —
  free PDF. Ch. 9 (intro to mechanism design), 10 (mechanism design without money),
  12 (distributed algorithmic mechanism design).
- **Hartline, *Mechanism Design and Approximation*** — free book draft. The best treatment
  of approximation as a design philosophy rather than a compromise.
- **Börgers, *An Introduction to the Theory of Mechanism Design* (OUP 2015)** — the
  economist's version, short and clean. Best single source for A1–A3.
- **Moulin, *Fair Division and Collective Welfare* (MIT 2003)** — the bridge between welfare
  economics and the algorithmic literature. Relevant given the SUF framing.
- **Curry, Fan, Jiang, Ravindranath, Wang, Parkes, "Automated Mechanism Design: A Survey",
  *SIGecom Exchanges* 22(2), 2025** — <https://www.sigecom.org/exchanges/volume_22/2/CURRY.pdf>.
  Read before D1.
- **Saari, *Basic Geometry of Voting* (1995)** / ***Chaotic Elections!* (2001)** — given
  `voting-geom` exists, this is the most surprising gap. Saari decomposes profile space
  into components and shows *why* paradoxes occur: there is a "Condorcet component" that
  every positional rule should ignore, and Borda is the unique positional rule that does.
  Directly relevant, probably not read yet.

### Foundations (Arc A)

- Arrow, *Social Choice and Individual Values* (1951/1963).
- **Kirman & Sondermann, "Arrow's theorem, many agents, and invisible dictators", *JET* 1972**
  — the ultrafilter proof. This is A4.
- Gibbard (1973), *Econometrica*; Satterthwaite (1975), *JET*.
- Vickrey (1961); Clarke (1971); Groves (1973); **Myerson, "Optimal Auction Design" (1981)**.
- **Moulin, "On strategy-proofness and single peakedness", *Public Choice* 1980** — the
  generalised median characterisation. This is A3.
- Barberà, "Strategy-proof social choice", *Handbook of Social Choice and Welfare* vol. 2 —
  the survey that makes the taxation principle central.
- Sen, "The Impossibility of a Paretian Liberal", *JPE* 1970.
- **List & Pettit (2002)** and **Dietrich & List (2007)** on judgement aggregation.
- Harsanyi (1955) — the aggregation theorem, i.e. the axiomatic derivation of weighted
  utilitarianism. Directly relevant to choosing a SUF, and its critics (Sen, Weymark) more so.
- Bartholdi, Tovey & Trick (1989) — manipulation as a computational problem.

### Collective decision making (Arc B)

- Black (1948); **McKelvey, "Intransitivities in multidimensional voting models", *JET* 1976**;
  Plott (1967) on core existence conditions.
- **Procaccia & Rosenschein (2006)** — distortion, the original.
- **Anshelevich, Bhardwaj & Postl (2015)** — metric distortion.
- **Gkatzelis, Halpern & Shah, "Resolving the optimal metric distortion conjecture" (FOCS 2020)**
  — the tight factor of 3. This is B2's centrepiece.
- **Aziz, Brill, Conitzer, Elkind, Freeman & Walsh, "Justified representation in
  approval-based committee voting" (2017)**.
- **Peters, Pierczyński & Skowron — the method of equal shares** (NeurIPS 2021 and the
  `equalshares.net` write-up).
- Peters & Skowron, "Proportionality and the limits of welfarism" (EC 2020) — the tension
  worth ending B3 on.
- Moulin, "The proportional veto principle" (*RES* 1981); Ianovski & Kondratev on computing
  the PVC (2003.09153) — already in your list.
- **Brandl, Brandt & Seedig, "Consistent probabilistic social choice", *Econometrica* 2016**
  — maximal lotteries.
- **Flanigan, Gölz, Gupta, Hennig & Procaccia, "Fair algorithms for selecting citizens'
  assemblies", *Nature* 2021**.
- Caragiannis, Kurokawa, Moulin, Procaccia, Shah & Wang, "The unreasonable fairness of
  maximum Nash welfare" — max Nash welfare gives EF1 *and* Pareto optimality. The concrete
  payoff for the Nash-product SUF you keep circling.
- Lalley & Weyl on quadratic voting; Posner & Weyl, *Radical Markets* for the argument in
  its expansive form.
- Kahng, Mackenzie & Procaccia, "Liquid democracy: an algorithmic perspective"; Caragiannis
  & Micha, "A contribution to the critique of liquid democracy" (IJCAI 2019).
- Gale & Shapley (1962); Bogomolnaia & Moulin (2001) on probabilistic serial — matching as
  the other half of "mechanism design without money".

### The inverse problems (Arc C)

- Samuelson (1938); Houthakker (1950); **Afriat, "The construction of utility functions from
  expenditure data", *IER* 1967**; Varian, "The nonparametric approach to demand analysis",
  *Econometrica* 1982.
- **Roberts, "The characterization of implementable choice rules" (1979)** — the affine
  maximiser theorem. The single most important citation for the bottom-up half of the
  research agenda, and it isn't in the agenda yet.
- **Maskin, "Nash equilibrium and welfare optimality", *RES* 1999** (circulated 1977).
- Kuleshov & Schrijvers, "Inverse game theory: learning utilities in succinct games" (WINE 2015).
- Ling, Fang & Kolter — differentiable equilibrium solving / "What game are we playing?" (IJCAI 2018).
- **"Data-Driven Mechanism Design via Multi-Agent Revealed Preferences"** —
  <https://arxiv.org/abs/2404.15391>. The closest existing work to C3.
- **"Efficient Inverse Multiagent Learning"** — <https://arxiv.org/abs/2502.14160> (ICLR 2025).
- "Blind Inverse Game Theory: Jointly Decoding Rewards and Rationality in
  Entropy-Regularized Competitive Games" — <https://arxiv.org/abs/2511.05640>. The
  identification-via-bounded-rationality move, which is C2's key idea.
- "Inverse Concave-Utility RL is Inverse Game Theory" — <https://arxiv.org/abs/2405.19024>.
- Hadfield-Menell, Milli, Abbeel, Russell & Dragan, "Inverse Reward Design" (NeurIPS 2017) —
  <https://arxiv.org/abs/1711.02827>. The alignment-side cousin.
- On Inverse RL for multi-agent systems — <https://arxiv.org/abs/2411.15046>.

### Learning and alignment (Arc D)

- Conitzer & Sandholm, "Complexity of mechanism design" (UAI 2002) — the origin of AMD.
- Balcan, Sandholm & Vitercik on sample complexity; "Sample Complexity of Automated
  Mechanism Design" — <https://arxiv.org/abs/1606.04145> (already in your list).
- Dütting, Feng, Narasimhan, Parkes & Ravindranath, "Optimal Auctions through Deep Learning"
  (ICML 2019 / JACM 2024) — RegretNet, the founding differentiable-economics paper.
- "Deep Learning Meets Mechanism Design: A Survey" — <https://arxiv.org/abs/2401.05683>.
- **"Open Problems in Differentiable Social Choice: Learning Mechanisms, Decisions, and
  Alignment"** — <https://arxiv.org/abs/2602.03003>. Reads like it was written for this
  project; check it for collisions with the research agenda before writing D1 or D2.
- **"Social Environment Design"** — <https://arxiv.org/abs/2402.14090>. RL for economic-policy
  mechanism design; the closest thing to the agenda's top-down search over mechanism space.
- "Deep Incentive Design with Differentiable Equilibrium Blocks" —
  <https://arxiv.org/abs/2603.07705>.
- Conitzer, Freedman, Heitzig, Holliday, Jacobs, Lambert, Mossé, Pacuit, Russell, Schoelkopf,
  Tewolde & Zwicker, "Social Choice Should Guide AI Alignment in Dealing with Diverse Human
  Feedback" (ICML 2024) — <https://arxiv.org/abs/2404.10271>. Already in `awesome-papers.md`.
- **Halpern, "AI Alignment From Social Choice Perspectives"** — <https://arxiv.org/abs/2606.21550>.
  The current survey; read before D2.
- "Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?" —
  <https://arxiv.org/abs/2505.23749>. Ties Arc B's distortion directly to D2.
- "Beyond RLHF and NLHF: Population-Proportional Alignment under an Axiomatic Framework" —
  <https://arxiv.org/abs/2506.05619>.

### Institutions and the empirical side (Arc D3)

- **Ostrom, *Governing the Commons* (1990)** and "Beyond Markets and States" (AER 2010).
- Hayek, "The Use of Knowledge in Society" (1945); *Law, Legislation and Liberty* vol. 1
  for constructivist rationalism in its explicit form.
- Acemoglu & Robinson, "Weak, Despotic, or Inclusive?" (APSR 2023) — already in the agenda.
- Moulin & Peleg on effectivity functions — already in the agenda, and the right formal
  language for "power" in both.

---

## 6. Loose ends worth turning into posts

Things noticed while reading the existing material that don't have a home yet.

1. **The `sct` follow-up.** The L2-normalisation post makes its case on one hand-chosen
   profile and doesn't examine the resulting rule's strategyproofness or its worst-case
   behaviour. Distortion theory is the tool for exactly this: "which normalisation of
   cardinal ballots minimises distortion" is a well-posed question with published answers,
   and it would either vindicate or complicate the L2 argument. Either outcome is a good post.
2. **`voting-geom` §8 has a name.** The "right to be heard" is close to justified
   representation. Worth a short retrofit link rather than a new post.
3. **Roberts' theorem is missing from the research agenda.** It changes the shape of the
   bottom-up programme: on unrestricted domains the implicit objective is always a weighted
   utilitarian sum, so the whole enterprise lives or dies on domain restriction. That's a
   sharpening, not an obstacle, but it should be stated in the agenda.
4. **Afriat is the right precedent for the bottom-up tool.** The agenda describes fitting an
   SUF to a mechanism's I/O behaviour as an open problem. It's the social-choice analogue of
   Afriat's construction, and Afriat's answer — rationalisable almost always, uniquely
   almost never — predicts the shape of the result before any code runs.
5. **The three-inverse-problems table** in Arc C is probably a post on its own if C3 gets
   too long, and it's the kind of clarification that gets linked to.
6. **Ostrom vs Hayek** partially answers a burden the framework post explicitly declines to
   discharge. Worth writing even outside this series.

---

## 7. Decisions to make before starting

- **How much maths.** `voting-geom` is fairly heavy, `sct` is light. The tutorials work
  better heavy, but each should have a stated prerequisite line and a worked toy example.
- **Where posts live.** `_drafts/mechanism-design/` for now. On publication: technical-posts
  for Arc A–C, inbetween-posts for D2/D3.
- **Whether to use jekyll-scholar.** `autoint` uses a `.bib`; the recent governance posts use
  a plain `## References` section. Given how many citations this series carries, a
  `_bibliography/mechanism-design.bib` shared across all sixteen posts would pay for itself.
- **Whether C4 blocks on code.** It does, and that's the one dependency on
  `govern-mechanisms` progress. Everything else can be written from reading alone.
- **Tags.** `tutorial` + `mechanism-design` + one subject tag from the existing vocabulary
  (`mathematics`, `politics`, `economics`). Arc C/D posts get `research` instead of `tutorial`.
