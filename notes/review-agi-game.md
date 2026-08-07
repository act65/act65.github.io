# Critical review — "Global coordination problems via game theory"

Post: `_posts/inbetween-posts/2025-07-24-agi-game.md`

External review. Every matrix was recomputed. **The arithmetic is correct as written** — the
short-term overfishing and climate matrices are valid PDs (T=4 > R=3 > P=2 > S=1, unique NE at
mutual defection); the long-term matrices are valid stag hunts; the AGI matrix is a valid PD with
Defect strictly dominant. The errors are about what the matrices are being asked to *do*.

---

# A. Game-theoretic errors

## A1. "Humanity" is not a player, and calling it one is a category error

**L13:** *"Adding humanity as a third player is the trick — it lets us see exactly where individual
incentives and collective welfare come apart."*

Humanity has no strategy set. It never moves, has no row or column, and its payoff is a pure
function of A's and B's choices. A real three-player normal form would be a 2×2×2 array.

Worse, the column carries **zero information**:

| Matrix | Humanity: CC / CD / DC / DD |
|---|---|
| Fishing short-term | 3 / 2 / 2 / 1 |
| Fishing long-term | 4 / 2 / 2 / 1 |
| Climate short-term | 3 / 2 / 2 / 1 |
| Climate long-term | 4 / 2 / 2 / 1 |
| AGI | 4 / 2 / 2 / 1 |

The same monotone function every time: CC > {CD, DC} > DD. "More cooperation is better for
humanity" is its entire content, and it makes no distinction between any two games in the post.

**Fix, pick one:**

1. *Honest downgrade.* Replace L13 with: "Each cell is written `(Player A, Player B, Humanity)`,
   where the third entry is not a player's payoff but a welfare ranking — how good the outcome is
   for everyone not at the table. It has no strategies; it is a scorecard, not a participant."
2. *Make it earn its place (stronger).* Give humanity a **non-monotone** ranking somewhere. Natural
   candidate: for AGI, does humanity really prefer stalemate to "one safety-conscious actor gets
   there first"? Bostrom's singleton argument says no. Set humanity's (Defect, Cooperate) payoff
   above (Cooperate, Cooperate) in some branch and the column starts discriminating. Or make
   humanity a real third player with strategies {Regulate, Don't}.

## A2. "Mutual Ruin" at (2,2,1) is inconsistent with the post's own stakes — this is Chicken, not a PD

**Most serious finding.** The matrix assigns players P=2 and S=1: **being beaten to AGI is worse for
you than a mutual race that might destroy everyone.** That assumption generates the PD and the whole
thesis rests on it. But the post insists elsewhere that a botched race is existentially catastrophic
(L101 "a racer is more likely to lose control of what they build"; L114 "your own creation destroys
you"). If mutual racing risks extinction, the racers are *in* the set of people who die. Then P < S
and the ordering is **T > R > S > P** — **Chicken**, not a Prisoner's Dilemma.

What changes:
- No dominant strategy.
- Two asymmetric pure equilibria plus a mixed one.
- The mixed equilibrium puts positive probability on catastrophe — risk is *endogenous*.
- The prescription flips from "build common knowledge" to **credible commitment and brinkmanship**
  (Schelling). Being visibly, irrevocably committed to racing becomes a winning move — the opposite
  of the post's recommendations.

The post never considers Chicken, never names it, never defends P > S.

**Fix — add immediately after the AGI matrix:**

> This matrix encodes one strong assumption: that being beaten to AGI (1) is worse *for a player*
> than a mutual race (2). That is only true if players' payoffs are purely positional — if they
> value relative standing and do not internalise their own share of the catastrophe. Nations and
> firms often do behave this way. But if the actors take the extinction risk personally, the
> ordering flips to T > R > S > P and the game becomes Chicken: no dominant strategy, two asymmetric
> equilibria, and a mixed equilibrium in which the catastrophe happens with positive probability.
> Chicken is a *worse* game to be in, in some ways — it rewards visible, irrevocable commitment to
> racing — and it makes "build common knowledge" the wrong prescription. Which game we are in
> depends entirely on whether decision-makers price their own deaths into the payoff.

## A3. The long-term fishing matrix contradicts the mechanism given for it

**L35:** *"the resource itself degrades as defection accumulates, shrinking the defector's prize over
time (**an overfished sea pays nobody**)."*

Take that seriously and the outcome most degraded by depletion is mutual overfishing. So R=4 (both
sustain), T=3 (you overfish, they sustain), S=2 (they overfish, you don't — degraded but you still
land fish), **P=1** (collapse, "pays nobody"). That is **R > T > S > P** — a **harmony game**:
sustainable fishing is strictly dominant, there is no dilemma, no trust-building needed.

The post's matrix has S=1 < P=2 — the lone conservationist does worse than universal collapse. Not
implied by "an overfished sea pays nobody"; it contradicts it.

**Fix:** either (a) use the harmony ordering and reframe as "depletion doesn't turn the PD into a
stag hunt, it dissolves the dilemma outright" — cleaner, and sharpens the AGI contrast; or (b) keep
the stag hunt and justify S < P: "the lone conservationist loses twice — the stock collapses anyway
and someone else caught the last of it." Not both.

## A4. Ordinal payoffs are declared, then used cardinally in three places

**L13** disclaims interpersonally comparable utilities. But:

- **L101:** *"the true expected payoff for 'Defect while the other cooperates' is closer to (1) than
  (4)."* You cannot take an expectation over ordinal ranks. Genuine technical error, in the post's
  most important section.
- **L78–79:** comparing (4,4,4) in one matrix to (3,3,4) in another invites the illegitimate reading
  that humanity's 4 is the same quantity across matrices.
- **L35/L55:** "give players the confidence to aim for the long-term (4,4,4) prize" appeals to **risk
  dominance**, undefined without cardinal payoffs. Worse, the numbers make the stag hunt exactly
  knife-edge: R−T = 1 and P−S = 1, so *neither* equilibrium risk-dominates. The optimistic reading
  is not in the numbers.

**Fix:** add at the top of "The escape hatch": *"Up to here the payoffs have been ordinal — ranks,
not magnitudes. To talk about expected payoffs we need cardinal utilities, so for this section read
the numbers as rough utilities rather than ranks."* And soften L35/L55 to "make (4,4,4) the focal
point — the stag hunt has *two* equilibria, and mutual defection remains one of them."

## A5. Humanity's 1–4 scale is applied inconsistently

Humanity's best available outcome is 3 in the short-term fishing matrix and 4 in the AGI matrix. If
the scale is within-matrix ordinal (as L13 says), short-term fishing should read (3,3,**4**). Using 3
smuggles in a cross-matrix comparison — exactly the cardinality L13 disclaims. Every matrix also
skips a rank: {3,2,2,1} in two, {4,2,2,1} in three.

**Fix:** normalise to a within-matrix ranking everywhere, or state up front that humanity's number is
on a single fixed scale across all five matrices while the players' are within-matrix ranks.

## A6. The stag hunt's second equilibrium is never mentioned

Both "long term" sections present the stag hunt as resolving the problem. Mutual defection (2,2,1)
is still a Nash equilibrium of both. The stag hunt is an *equilibrium selection* problem, not a
solved game.

**Suggested replacement for L35's last sentence:**

> The transformation doesn't solve anything by itself: mutual overfishing is still a Nash equilibrium
> of the long-term game. What changes is that cooperation becomes self-enforcing *once reached* —
> nobody wants to be the first to break it. The job of fisheries institutions is equilibrium
> selection, not payoff engineering: getting everyone to believe everyone else is aiming at the same
> cell.

## A7. "No shift in time horizon changes this" is false on the post's own terms

**L87.** The folk theorem: cooperation is sustainable as a subgame-perfect equilibrium of an
*unchanged* PD, repeated indefinitely, with patient enough players. T does not need to shrink. The
post conflates repetition and prize-shrinkage. If the argument is "no repeated rounds" (L62), say
that.

**Fix:** *"Unlike fisheries or climate, the (4) temptation doesn't shrink as the game plays out.
Repetition could still sustain cooperation in a fixed Prisoner's Dilemma — that's the folk theorem —
but only if the players expect enough future rounds to matter. That's the bet the next section
examines."*

---

# B. Is the central claim supported?

## B1. The matrices are decorative — the AGI matrix is numerically identical to short-run overfishing

Fishing short-term (L25–26): `(3,3) (1,4) / (4,1) (2,2)`
AGI (L71–72): `(3,3) (1,4) / (4,1) (2,2)`

Identical. The only difference in the whole post is one entry in the non-strategic welfare column
(humanity 3 → 4). **The model contains no information distinguishing AGI from overfishing.** The
thesis is carried entirely by three prose bullets at L61–63.

**Fix — own it, right after L72:**

> Note what's happened here: the player payoffs in this matrix are identical to the short-run
> overfishing matrix above. That's the point — and also the limit of what a payoff matrix can show.
> The matrix doesn't prove AGI is different; it just records that I think the *same* short-run game
> persists at long horizons, where in fisheries it doesn't. The argument for that is in the three
> bullets above, not in the numbers.

## B2. "The misalignment is structural" is question-begging

**L74, L81.** Two problems. First, "the game is built so that they can't" is literally true and is
the objection: *you built it that way*. The misalignment is an **input** — players whose payoffs
don't internalise humanity's welfare — presented as an **output**. Second, the property isn't
distinctive to AGI: "at mutual cooperation each player sees a higher payoff they could grab by
defecting" is the *definition* of a PD (T > R), equally true of the short-term overfishing matrix.

**Fix — retitle to "The misalignment is an assumption, and it's the important one" and rewrite L81:**

> That gap is the misalignment — but be clear about where it comes from. It isn't derived; it's
> assumed, in the decision to give players payoffs that don't include humanity's. That assumption is
> the substantive claim of this whole post. It's defensible: firms answer to shareholders and states
> to citizens, and neither is "humanity". But it is the input, not the output, and everything
> downstream depends on it.

## B3. The thesis and the escape hatch contradict each other

L11 asserts "a permanent Prisoner's Dilemma". L101 concedes "the matrix starts to collapse toward a
Stag Hunt". L103 re-asserts the conditional. So the actual claim is *AGI is a PD iff decision-makers
believe P(alignment succeeds | racing) is high enough* — but the post structures the unconditional
claim as the thesis with the conditional as a late concession.

The conditional version is stronger and **computable in one paragraph**. Let *p* be the probability a
racer loses control, *W* the value of winning with a controlled AGI, *C* mutual cooperation, *L* the
catastrophe. Defection dominates iff (1−p)W + pL > C, i.e. iff **p < (W − C)/(W − L)**. Now the post
has a spine: everything in "What could change the game" is an intervention on *p*, on beliefs about
*p*, or on *W*; and "Why the prize looks absolute" becomes an argument about why decision-makers
currently estimate *p* below the threshold.

**Fix:** promote the conditional to the thesis. L11 → "What's left is a Prisoner's Dilemma that
doesn't dissolve on its own — and it stays one for exactly as long as the people racing believe they
can race and win." Add the threshold inequality to the escape-hatch section.

## B4. The three "why AGI is different" bullets are weaker than stated

- **L61 "No resource depletion."** Capability doesn't deplete, but the *inputs* are rival and scarce:
  leading-edge fabrication, HBM, power, grid interconnects, a small talent pool. Export controls are
  precisely a resource-restriction mechanism. **Rewrite:** "No depletion of the *prize*. Overfishing
  shrinks the pot; AGI capability doesn't. Compute and talent are rival and contestable — which is
  why export controls bite — but no amount of racing makes the winner's prize smaller."
- **L62 "No repeated rounds."** Concedes its own weakness ("the most pessimistic"). The AGI decision
  is *embedded* in a dense repeated relationship — trade, chips, tariffs, standards bodies, talent
  mobility, publication norms, joint safety evaluations. Issue linkage can sustain cooperation on a
  one-shot issue. This is Askell, Brundage & Hadfield's argument and the strongest counterargument to
  the post. Add a fourth bullet acknowledging it and explaining why you think it's insufficient.
- **L63 "No visible degradation."** The best of the three — expand it, since it also does the work in
  the nukes section.

---

# C. The empirical premise about other coordination problems

## C5. "Most global coordination problems get easier with time" — the track record is roughly the opposite

**L9.** This is the baseline the title depends on, asserted with no evidence.

**Fisheries.** Northern cod collapsed in 1992 and has still not recovered thirty years on — the
long-term stag hunt never arrived, the resource simply ended. Peruvian anchoveta (1972) and Atlantic
bluefin tell similar stories. FAO assessments show the fraction of stocks fished at biologically
unsustainable levels rising from roughly 10% in 1974 to the mid-to-high 30s today (direction and
rough magnitude confident; **check the current SOFIA report for the exact figure before printing**).
Monotone in the wrong direction. The genuine successes — Alaska pollock, Icelandic and NZ quota
systems, the partial bluefin rebound — came from rights-based management with real enforcement, not
from damage becoming visible (Costello et al., PNAS 2016; Worm et al., Science 2009).

**Climate.** Kyoto: US never ratified, Canada withdrew. Paris: non-binding. Global CO₂ has risen in
nearly every non-recession year since 1992. The one unambiguous success, Montreal, succeeded on Scott
Barrett's analysis because abatement costs were low, substitutes existed, and producers were few.
Barrett's central result in *Environment and Statecraft* (2003) is that international environmental
agreements are self-enforcing **only when the gains from cooperation are small** — a direct inversion
of the post's mechanism ("the catastrophic costs make a stable planet the ultimate prize"). That
deserves an answer.

**Ostrom cuts against you more interestingly than expected.** *Governing the Commons* (1990)
documents hundreds of commons managed successfully for centuries — and the mechanism is **not**
"degraded until cooperation became visibly worth it". It is clear boundaries, congruence with local
conditions, collective-choice arrangements, **monitoring**, **graduated sanctions**, conflict
resolution, recognised rights to organise, nested enterprises. Successful communities act *before*
collapse.

So Ostrom undermines the causal story about fisheries — and then supports the AGI conclusion for a
different reason: monitoring and graduated sanctions don't scale to a global, low-observability,
high-stakes domain. But that is *also* true of climate. Ostrom herself (2009 World Bank WP; 2010
Nobel lecture) argued the global climate commons resists the design principles that work locally,
which is why she advocated **polycentric** governance. **The uncomfortable implication: climate may
be much closer to AGI than the title allows.**

**Fix — L9:** *"Some global coordination problems get easier with time. Overfishing and climate
change look like Prisoner's Dilemmas in the short run, and the standard hope is that the game
transforms once mutual defection has done enough damage to make cooperation visibly worth it. The
hard part of governance is buying enough time and trust for that transformation to happen — and it
often doesn't happen in time."*

**Fix — new subsection after L55:**

> **How well does this story actually hold?** Not that well. Northern cod collapsed in 1992 and
> hasn't recovered; the fraction of fish stocks fished unsustainably has risen steadily since the
> 1970s. Emissions have risen through three decades of climate diplomacy. And Elinor Ostrom's work on
> common-pool resources, which documents the commons problems that *do* get solved, points at a
> different mechanism than the one I've described: successful commons are governed through clear
> boundaries, monitoring, and graduated sanctions applied *before* collapse — not through damage
> becoming visible after it. Ostrom's own view was that these design principles don't scale
> straightforwardly to global commons, which is why she argued for polycentric climate governance
> rather than a grand treaty. Scott Barrett's finding is sharper still: environmental treaties tend
> to be self-enforcing only when the gains from cooperation are *small*. If all that is right, then
> climate is a weaker baseline than I've made it look, and the honest version of this post's claim is
> narrower: AGI lacks the transformation mechanism, but so, largely, does climate. What AGI
> additionally lacks is time.

That move *strengthens* the post — it converts a vulnerable comparison into a sharper claim.

---

# D. Literature

## C1. The post cites nothing and reinvents published results

In priority order:

1. **Armstrong, Bostrom & Shulman, "Racing to the Precipice: a Model of Artificial Intelligence
   Development" (AI & Society, 2016).** Models exactly this. Two results the post needs: risk
   increases with the number of teams, and **more information about competitors' relative positions
   can *increase* danger**, because a team that knows it is behind takes bigger risks. That directly
   complicates the "verifiable compute monitoring" recommendation at L122. Single most important
   paper to engage. *(Counterintuitive and it cuts against the post's own recommendation — read it in
   the original before relying on it.)*
2. **Askell, Brundage & Hadfield, "The Role of Cooperation in Responsible AI Development" (2019).**
   The strongest direct rebuttal to L62's "no repeated rounds". Name and answer it.
3. **Han, Pereira, Lenaerts & Santos, "To Regulate or Not: A Social Dynamics Analysis of an Idealised
   AI Race" (JAIR 69, 2020).** Derives *when* the AI race is a dilemma vs a coordination game as a
   function of the risk/speed ratio — essentially the post's thesis, formalised, with a threshold.
4. **Naudé & Dimitri, "The race for an artificial general intelligence: implications for public
   policy" (AI & Society, 2020).** Models the race as a contest/all-pay auction rather than a PD.
5. **Dafoe, "AI Governance: A Research Agenda" (2018)**; **Zwetsloot & Dafoe, "Thinking About Risks
   From AI: Accidents, Misuse and Structure" (2019)**.
6. **Cave & ÓhÉigeartaigh, "An AI Race for Strategic Advantage: Rhetoric and Risks" (AIES 2018).**
   Argues the race framing is partly self-fulfilling — that writing posts like this one helps create
   the game it describes. Uncomfortable; the post is stronger for facing it.
7. **Bostrom, Douglas & Sandberg, "The Unilateralist's Curse" (Social Epistemology, 2016)** for the
   n-player generalisation.

Non-AI sections: **Hardin (1968)**, **Ostrom (1990, 2009)**, **Barrett (1994, 2003)**, **Jervis,
"Cooperation Under the Security Dilemma" (World Politics, 1978)** — the nukes section *is* the
security dilemma and should say so — and **Schelling (1960)** for commitment and focal points.

The repo has `_bibliography/*.bib` with `jekyll-scholar` wired up, so `{% cite %}` is available.

## C2. Vague appeal to unnamed models

**L62:** *"The most pessimistic AGI race models look more like a single round."* Which models? Cite
Armstrong/Bostrom/Shulman or state it as your own assumption.

---

# E. Unstated assumptions

- **D1. n = 2.** The world has several states and a dozen-plus frontier labs. In an n-player version
  cooperation requires unanimity while defection requires one defector — the unilateralist's curse.
  Armstrong et al. find risk rising in team count. Two-player analysis *understates* the problem, so
  saying this helps your case.
- **D2. Who is the player?** L69–72 says "Player A / Player B"; L95 says "your nation, culture, or
  company". Labs and states are not interchangeable. If states are the players, labs aren't strategic
  actors and this is a two-level game (Putnam 1988). If labs are, the "existential security" bullet
  at L93 doesn't apply to them. Suggest stating it as states-with-labs-as-instruments.
- **D3. Binary strategies.** The real decision variable is a continuous safety-versus-speed dial, and
  every model in the race literature treats it continuously. Binarising discards the thing you most
  want to talk about.
- **D4. Simultaneous vs sequential.** The normal form implies simultaneous one-shot moves; L62, L93
  and the whole race framing describe a sequential race with a stochastic finish line — a
  stopping-time or contest problem. Never reconciled.
- **D5. Common knowledge assumed and denied.** L63 explicitly asserts incomplete information; the
  analysis is complete-information normal form. This is a Bayesian game, and the escape hatch is
  entirely about beliefs. At minimum name the tension.
- **D6. A single decisive moment.** "Whoever gets there first locks in" assumes discontinuous takeoff
  and durable lock-in. L124 *concedes* the winner may not stay a winner and doesn't propagate it back
  — if so, T isn't 4.

**Fix:** a "What this model assumes" subsection before "Why AGI Is Different". Six bullets, one line
each, ~120 words. Pre-empts most objections a knowledgeable reader will raise.

---

# F. Clarity and structure

- **E1. Cut the climate matrices entirely.** L43–46 is numerically identical to L23–26, and L50–53 to
  L30–33. Replace with: "Climate has the same structure: short-run, the matrix is identical to the
  overfishing one above, with 'pollute' in place of 'overfish' and nations in place of boats.
  Long-run, it's the same stag hunt." Saves ~15 lines and reads as confidence rather than repetition.
- **E2.** L13 declares `(Player A, Player B, Humanity)` but the fishing and climate tables are
  labelled "You" and "Others". Add "(You, Others, Humanity)" above the first table. Also: collapsing
  all other fishers into one "Others" player eliminates the free-rider structure that makes commons
  problems hard — worth a clause.
- **E3. Define the PD condition once**, after L13: "A Prisoner's Dilemma is any game with the ordering
  Temptation (4) > Reward (3) > Punishment (2) > Sucker (1); a Stag Hunt swaps the top two, so mutual
  cooperation (4) beats unilateral defection (3)." Now readers can check your work — which you want.
- **E4.** L101's "collapse toward a Stag Hunt" is vague at the crux. Say what happens: "T falls below
  R, defection stops being dominant, and mutual cooperation becomes the payoff-dominant equilibrium
  of a two-equilibrium coordination game. Cooperation becomes achievable — not automatic."
- **E5.** The nukes section is longer and better than the climate section the title advertises.
  Consider: "Why AGI is not like climate change — it's like nukes without the stabilisers."
- **E6. L97 is the real thesis and is buried:** *"These claims are contested in detail, but they don't
  have to be true to drive the game. They only have to be believed by the people making the
  build-or-cooperate decision."* Best sentence in the post. Move a version of it into the opening.

---

# G. What works — don't touch

- **The nuclear weapons section (L105–116)** is the strongest part. The four disanalogies — no second
  strike, hard to verify, faster timelines, self-destruction rather than deterrence — are sharp,
  correct and non-obvious. "AGI is nukes with several of the stabilizers missing" is a good line.
  (One addition: name Jervis's security dilemma.)
- **The "escape hatch" section (L99–103)** — steelmanning your own strongest counterargument, and
  correctly identifying that the transformation must come from persuasion rather than physics, is the
  most intellectually honest thing in the post. It should be *promoted*, not cut.
- **"What could change the game" (L118–127)** is concrete and policy-relevant. (Caveat: Armstrong et
  al. suggests more information about relative position can increase risk-taking by trailing teams.)
- **The prose.** Brisk, unpadded, no throat-clearing.
- **The core intuition** — that AGI lacks the self-correcting dynamics of other commons problems — is
  worth defending. The objection is that it's underdetermined by the model presented, not that it's
  wrong.

---

# Suggested revision order

1. **A2** (Chicken vs PD) — highest value, changes the analysis.
2. **C5** (the empirical baseline + Ostrom/Barrett) — most vulnerable to a knowledgeable reader.
3. **B3** (conditional thesis + the *p* threshold) — gives the post a spine.
4. **A1 + B2** (humanity isn't a player; the misalignment is assumed).
5. **C1** (cite Armstrong/Bostrom/Shulman, Askell et al., Han et al.) — cheap, large credibility gain.
6. **D1–D6** (assumptions subsection).
7. **A3, A4, A5, A6, A7** (matrix and convention corrections).
8. **E1–E6** (structure and trims).
