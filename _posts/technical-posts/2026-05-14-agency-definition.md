---
title: Agency as the candidate objective
subtitle: Deriving a social utility function from four toy worlds
layout: post
categories:
    - economic
permalink: /governance-mechanisms/agency/
description: "Deriving a social utility function from four toy worlds. Two drivers want the last parking space."
tags:
  - research
  - mechanism-design
  - philosophy
---

Two drivers want the last parking space. Whatever rule the car park runs, one of them will not get it — and how the rule distributes that disappointment is the entire content of "the car park should serve its users well." A lottery and first-come-first-served produce identical totals and different societies.

That toy contains most of the problem. We want to compare institutions without asking which one best realises some particular conception of the good, because whoever writes that conception writes themselves into it — the capture argument, and the reason a durable institution should not bet on it. So we need a score that is neutral about what people ought to want and still discriminates between arrangements. Call it a **social utility function** (SUF).

This post argues for **agency** — the capacity to achieve one's goals — and *derives* the functional form rather than proposing one and checking it against thought experiments. The method: write down what we want in two sentences, build the smallest toy world that discriminates between candidate answers, read off one axiom per toy, and see what the axioms force.

What we want, in two sentences:

1. **Everyone should be freer** — which necessarily means restricting some freedoms, because freedoms conflict.
2. **What matters is the capacity to pursue goals, not which goals are pursued.**

Both sentences have famous statements. Rawls' first principle of justice is the first one:

> Each person is to have an equal right to the most extensive basic liberty compatible with a similar liberty for others.
> <br/>— Rawls, *A Theory of Justice* (1971), §11

And Sen's *agency freedom* is the second:

> A person's "agency freedom" refers to what the person is free to do and achieve in pursuit of whatever goals or values he or she regards as important. […] Agency freedom is freedom to achieve whatever the person, as a responsible agent, decides he or she should achieve. That *open conditionality* makes the nature of agency freedom quite different from that of well-being freedom…
> <br/>— Sen, *Well-Being, Agency and Freedom: The Dewey Lectures 1984*, pp. 203–4

"Open conditionality" is the property this post spends most of its length trying to keep. The claim is that those two sentences, plus a handful of consistency requirements, come close to pinning down a unique functional form.

## 1. Two axes

Debates about "what should society maximise" conflate two distinct axes.

The first axis is *what* is being aggregated: hedonic happiness, suffering, capabilities, goal-achievement, opportunity, preferences.

The second axis is *how* the aggregation works: sum, product, minimum, weighted average.

Most disagreements are about the second axis dressed up as the first. The classical-utilitarian sum is famously vulnerable to the gladiator problem — a thousand people enjoying the suffering of two — which is a complaint about the *aggregator*, not about whether happiness is the right object to aggregate.

The two axes are not fully independent, and it is worth getting the interaction straight early, because it recurs. Set $s_i = -\log u_i$. Then minimising the negative-utilitarian sum $\sum_i s_i$ and maximising the Nash product $\prod_i u_i$ are *the same problem*. The Nash product is sum-utilitarianism applied to log-utility. So a monotonic transformation of the object simulates a change of aggregator, and many apparent disagreements about objective functions are disagreements about utility scales.

This matters for what follows because the definition this post arrives at is a product — and by the identity above, it is therefore also a sum, over log-probabilities. Rather than treat that as an embarrassment, §6 leans into it: agency is utilitarianism where a life's utility is measured in *bits of steering*.

## 2. The evaluation criterion: commit to as little content as possible

A good objective should commit to as little as it can about *what* people ought to value, while still discriminating between institutions. The motivation is that preferences are both **unknown** (we don't fully observe them) and **dynamic** (they shift). At design time we have, at best, a hyperprior $\mathcal{H}$ over preference distributions $\Pi$ — a model of what humans might want, not knowledge of any specific $\Pi$. An objective that commits hard to one view of value does well when $\Pi$ matches its assumption and badly elsewhere in the support; one that commits to less keeps its ranking meaningful across the range.

The argument has a formal ancestor. Kreps (1979) shows that preferences over *menus* satisfying preference for flexibility and an ordinal submodularity condition are represented by $U(B) = \sum_{s\in S}\max_{x\in B} u(x,s)$ over a subjective state space of possible future tastes: a menu's value is the expected max, and uncertainty about your own future preferences is exactly what makes option value nonzero. (Two caveats, since the result is routinely overstated: the monotonicity is an axiom rather than a conclusion, and it bites only on *nested* menus — preferring a strict subset is a different phenomenon, formalised by Gul and Pesendorfer in 2001.) Rawls' veil is the same move in a different register: not knowing your conception of the good, you bargain for all-purpose means.

## 3. The object: probability of achieving a goal

Before choosing an aggregator, choose what is being aggregated. The proposal: $P(g_i)$, the probability that individual $i$ achieves goal $g_i$. Three reasons.

**It has a canonical zero and a canonical unit.** This is not a small thing. The Nash social welfare function is invariant to rescaling each person's utility — that is one of its defining axioms — but it is *not* invariant to additive shifts: move the zero point and the recommended action changes. Probabilities have no free zero. $P = 0$ means *cannot*, $P = 1$ means *certainly*, in every society, for every person. So choosing probability as the object buys translation-invariance, which is precisely the invariance the Nash product lacks. Choosing probability as the object buys off an entire class of objections to the multiplicative aggregators considered below.

**It is content-free in Sen's sense.** $P(g_i)$ does not ask whether $g_i$ is a good goal. Open conditionality is preserved by construction.

**And it costs less generality than it appears to.** Talking about *goals* rather than *preferences* looks like a large restriction — most of what people want is a matter of degree, and a probability needs a binary event. It isn't, provided goals are read as **upper contour sets**: let $g_\tau = \{s : \mathrm{pref}_i(s) \ge \tau\}$, the event "reach a state at least this good." Three things follow. The family $\{g_\tau\}$ over all thresholds is informationally equivalent to the preference ordering, since $\tau \mapsto P(\mathrm{pref}_i \ge \tau)$ is just the survival function of achieved utility, so nothing is discarded. Each $g_\tau$ is a well-defined event with a non-degenerate probability — unlike the tempting alternative of identifying a goal with $\arg\max_s \mathrm{pref}_i(s)$, which sends $P(g_i)$ to nearly zero for everyone and needs a topology on world states to make "local" mean anything. And upper contour sets are invariant under any strictly increasing transformation of $\mathrm{pref}_i$, so the objective stays purely *ordinal* in each person's preferences, which is the content-freeness the post is trying to keep.

The cost is a measure over thresholds — where in each person's preference ordering to place the bar. That is another unforced choice and §8 counts it.

**The goals must be counterfactual, not reported.** This is the single most important commitment in the post. If $\gamma$ is drawn from what people *currently say they want*, then the objective is maximised by shrinking goals to fit — the contented-slave objection, and the reason Sen rejects utility as an informational basis:

> Person $A$ is starving because she is very poor and lacks the means to command food. Person $B$ is starving out of choice, because of his religious beliefs […] In terms of the misery caused by the starvation, we learn that there is no difference between $A$'s experience and $B$'s. […] There would nevertheless remain an important difference between the two cases, viz., $B$ *could have*, in a straightforward sense, chosen an alternative life style which $A$ could not have chosen.
> <br/>— Sen, Dewey Lectures, p. 201

So the goal vector $\gamma$ is drawn from $\mathcal{H}$ — the hyperprior over what people *might* want, across current and counterfactual worlds — not from elicited preferences. Wireheading then scores badly for the right reason: the person in the vat achieves the one goal they have, but fails almost every goal in $\text{supp}(\mathcal{H})$. Without this move the wireheading argument does not work at all, and the vat is optimal.

**Related work.** Two literatures outside social choice have converged on this object independently, and neither is cited in the usual political-philosophy treatment.

The comparison to the AI-safety literature is developed in §6, once the definition is on the table; one piece of it belongs here, because it bears on the choice of object. *Empowerment* (Klyubin, Polani and Nehmzow; later Salge and Polani) defines an agent's power over its environment as the channel capacity from its actions to its future observations,

$$\mathfrak{E}(s) = \max_{p(a^n)}\, I(A^n; S' \mid s)$$

— a goal-independent intrinsic motivation, explicitly proposed as a *substitute* for hand-specified objectives. Note the difference in how it handles the unknown-goal problem: empowerment takes a **max** over input distributions rather than an expectation under a prior. That is a substantive alternative to the $\mathbb{E}_{\gamma\sim\mathcal{H}}$ used here, and it is not obvious which is right.

## 4. Four toy worlds

Each toy is the smallest world that discriminates between two candidate answers. Each yields one axiom.

### Toy 1 — The last parking space

Two drivers, one remaining space. Both want it. Exactly one can have it.

Its first lesson is that *individual* agency is not well-defined: driver 1's probability of success is entirely determined by driver 2's intent. Any score assigned to an individual in isolation is measuring the wrong object.

Its second lesson is sharper. Compare two rules:

| Rule | $P_1$ | $P_2$ | $\sum_i P_i$ | $\prod_i P_i$ |
|---|---|---|---|---|
| Lottery | 0.5 | 0.5 | 1.0 | 0.25 |
| First-come-first-served, driver 1 is faster | 1.0 | 0.0 | 1.0 | 0.00 |

The sum cannot tell these apart. That is Rawls' first principle in miniature: freedoms conflict, so a rule must restrict someone, and the whole content of "everyone should be freer" lives in *how* the restriction is distributed — which is precisely the information the sum discards.

> **Axiom A5 (inequality aversion).** Moving probability from a higher-$P$ individual to a lower-$P$ one, holding the total fixed, must not decrease the score. (Pigou–Dalton.)

### Toy 2 — The arena

*(The utilitarian objection usually called the Roman-arena case. "Gladiator problem" is avoided here: it already names something else in probability theory.)*

One thousand spectators, two victims. The spectators' goal is entertainment; satisfying it drops the victims from $P = 0.5$ to $P = 0.01$ on everything they care about.

The sum is defeated immediately, which is the standard result. But it is worth checking whether the *product* actually rescues us, because it is widely assumed to. In log form:

$$\Delta \log \prod_i P_i = \underbrace{2\bigl(\log 0.01 - \log 0.5\bigr)}_{\text{victims}} + \underbrace{1000 \cdot \log\!\frac{0.5+\varepsilon}{0.5}}_{\text{spectators}} \approx -7.82 + 2000\,\varepsilon$$

Break-even at $\varepsilon \approx 0.004$. **If each spectator's goal-achievement probability rises from 0.500 to 0.504, the arena is worth it.** The product does not abolish the gladiator problem; it rescales it. The log punishment for crushing someone grows only *logarithmically* as $P \to 0$, while the spectators' gain grows *linearly* in their number. Numbers always win eventually.

The honest statement is a small impossibility: no separable, continuous aggregator can give an absolute veto, because separability means each person contributes a finite additive term and continuity means that term is finite for $P > 0$. Absolute non-domination requires either abandoning separability (a lexical or maximin structure) or accepting that the veto only triggers at $P$ exactly zero. This post keeps separability and accepts the weakened protection — but the choice should be visible, and §8 revisits it.

### Toy 3 — The locked room

One person in the society has a goal that no institution can serve: they want to travel faster than light. $P = 0$ for them under every mechanism $m$.

Under the raw product, *every* mechanism scores exactly zero. The objective becomes totally indifferent between a free society and a tyranny. One unsatisfiable person destroys the ranking.

This is the "veto" failure of the Nash product, and it is the same mathematical fact that Toy 2 wanted as a feature. The resolution is that a zero is only informative *relative to what was achievable* — an impossible goal is impossible under the baseline too, and should therefore be silent rather than catastrophic.

> **Axiom A6 (difficulty invariance).** If person $i$'s goals become uniformly harder — $P_i$ and the baseline $P_i^0$ both scaled by $\lambda_i$ — the score is unchanged.

### Toy 4 — The extra colonist

An island of $n$ settlers. A child is born.

Under the raw product $\prod_i P_i$, every factor is below 1, so **every** additional person lowers the score. Agency-as-product is more strongly antinatalist than the negative utilitarianism it was introduced to escape; taken literally it recommends the world-destroyer button, since the empty product is 1 and 1 is the maximum. (This is not a subtlety about limits. It is what the formula says.)

The obvious repair — divide by $n$, i.e. use the geometric mean — is worse in a different direction. For fixed $n$ the geometric mean is a monotone transform of the product, so it changes nothing about Toys 1–3; the only thing it changes is population comparisons, and it changes them into average utilitarianism, under which removing anyone below average raises the score.

Both failures share a diagnosis: they place the "neutral" life at $P = 1$ and $P = \bar{P}$ respectively, and neither is defensible. What we want is a *critical level* — a $P$ at which adding a person is neither good nor bad.

A warning before the axiom, because it is easy to over-read what follows. Fixing the neutral point makes the objective *well-behaved* when population changes incidentally — a birth, a death — which is all Toy 4 asks for. It does not settle population ethics, and §7 shows that it cannot.

> **Axiom A7 (population neutrality at baseline).** Adding an individual whom the institution serves exactly as well as no institution at all leaves the score unchanged.

#### The same axiom from the other side: two planets

Two planets run identical constitutions. On planet A, people want ordinary things. On planet B, every inhabitant's single goal is to become sole ruler of the planet — mutually exclusive by construction, so $P_i \approx 1/n$ for everyone.

Planet B scores catastrophically lower. But the *institutions are the same*. The objective is measuring the difficulty of the population's goals, not the quality of the institutions — and since the whole point of a SUF is to write $m^* = \arg\max_m K(m)$, that confound is fatal.

This is A6 again: what we want to score is the institution's *contribution*, a comparison against a counterfactual rather than an absolute level. It is the same axiom, which is why it gets no separate number.

Plus four requirements too boring to need toys — with one exception, noted:

> **A1 Anonymity.** Permuting individuals does not change the score.
> **A2 Monotonicity.** Raising any $P_i$ raises the score.
> **A3 Continuity.**
> **A4 Separability.** Individuals whose $P$ is unchanged do not affect the ranking of two states. *(The contested one — Toy 2 showed what it costs.)*

## 5. What the axioms force

**Step 1 — additive form.** A1–A4 with $n \ge 3$ give, by the standard additive-separability theorem (Debreu 1960; Gorman 1968), a representation

$$W = \sum_i f(P_i)$$

unique up to a common positive scale and individual additive constants — under anonymity, $f \mapsto af + b$ with $a>0$, so $W \mapsto aW + nb$. Note that $b$ is *not* an innocuous normalisation once $n$ varies, which is exactly why the population question of Toy 4 has real content. Separability is what does this: it is the reason "which aggregator?" has far fewer answers than it appears to.

**Step 2 — concavity.** A5 (Pigou–Dalton) forces $f$ concave.

**Step 3 — the functional equation.** Score a mechanism against a baseline, $W(m) - W(\varnothing) = \sum_i \bigl[f(P_i) - f(P_i^0)\bigr]$. A6 requires this to be invariant under $P_i \mapsto \lambda_i P_i,\ P_i^0 \mapsto \lambda_i P_i^0$:

$$f(\lambda P) - f(\lambda P^0) = f(P) - f(P^0) \qquad \forall\, \lambda, P, P^0$$

So $f(\lambda P) - f(P)$ is independent of $P$; call it $g(\lambda)$. Then $f(\lambda P) = f(P) + g(\lambda)$, a Pexider equation whose only continuous solution is

$$f(x) = a\log x + b, \qquad a > 0$$

**Step 4 — the population axiom comes free.** With $f = \log$, adding a person at $P_i = P_i^0$ contributes $\log(P_i/P_i^0) = 0$. A7 is satisfied automatically. And $\log$ is concave, so A5 is satisfied automatically too.

That is worth pausing on, and also worth being careful about. **The population fix and the goal-difficulty fix are the same fix** — A7 costs nothing once A6 has forced the log.

But note precisely where the resulting critical level sits. A person is neutral when $P_i = P_i^0$: when the institution serves them exactly as well as no institution would. In the vocabulary of population ethics that is a critical level *at* neutrality, $\alpha = 0$ — which is not critical-level utilitarianism at all, but plain total utilitarianism in log-ratio coordinates. Blackorby, Bossert and Donaldson show that a critical level at or below neutrality implies the repugnant conclusion, and one strictly above it implies the sadistic conclusion. $K$ sits on the repugnant horn. (Their family assumes a single critical level common to everyone, where ours is person-specific, so the theorem does not transfer automatically — but §7 derives the consequence directly and does not need it.)

## 6. The definition

$$\boxed{\;\log K(m) \;=\; \mathbb{E}_{\Pi \sim \mathcal{H}}\;\mathbb{E}_{\gamma \sim \Pi}\;\sum_{i}\; \log \frac{P\bigl(g_i \mid \sigma^*(\gamma, m)\bigr)}{P\bigl(g_i \mid \sigma^*(\gamma, \varnothing)\bigr)}\;}$$

Unpacking:

- A **joint goal vector** $\gamma = (g_1, \ldots, g_n)$ assigns one goal to each member of society. The nesting matters: a preference distribution $\Pi$ is drawn from the hyperprior $\mathcal{H}$, and $\gamma$ from $\Pi$ — the goals people *might* hold, not the ones they report (§3).
- $\sigma^*(\gamma, m)$ is the equilibrium strategy profile of the game that mechanism $m$ induces when the population holds goals $\gamma$.
- $\varnothing$ is the **baseline** mechanism: no institution, the state of nature, or whatever null comparator the problem makes natural.
- The ratio $P_i(m)/P_i^0$ is how much more likely the institution makes person $i$'s goal. Its log in base 2 is a convenient shorthand — *bits of steering* handed to person $i$ — but the metaphor should not be pressed: this is a pointwise log-ratio, not a KL divergence or a mutual information, and so not the same species of object as the empowerment measure in §3.
- The sum over $i$ is a baseline-normalised Nash social welfare function in log form — a product of ratios, not the Nash bargaining product $\prod_i(u_i-d_i)$; the expectation over $\gamma$ is what makes it a measure of general capacity rather than of one situation.

Three features are worth marking, because each is forced by a toy rather than chosen for convenience: it is an **expectation** over $\gamma$ rather than a sum, which would diverge; the goals are drawn from $\mathcal{H}$ rather than from reported preferences; and everything is measured **relative to a baseline**.

**What the objective is scoped to.** $K$ ranks mechanisms for a *given* population. That restriction is not a dodge; it is what $m^* = \arg\max_m K(m)$ actually does, since $m$ does not change who exists. Two consequences follow and both should be visible. First, within that scope $\sum_i \log P_i^0$ is an additive constant, so **the baseline cannot change the ranking of mechanisms** — it earns its keep on Toy 5, comparing societies whose goals differ in difficulty, and on incidental population change, not on the choice of institution for a fixed society. Second, the moment you use $K$ to compare populations of different sizes you are doing population ethics, and it does not do that well. §7 is explicit about how badly.

**Where this lands relative to the AI-safety literature.** Three measures are worth comparing, and the comparison is sharper than a family resemblance.

*Attainable Utility Preservation* (Turner) penalises an agent for changing its ability to achieve a set of auxiliary goals relative to doing nothing:

$$R_{\text{AUP}}(s,a) = R(s,a) - \lambda\,\bigl|\,Q^*_{R_{\text{aux}}}(s,a) - Q^*_{R_{\text{aux}}}(s,\varnothing)\,\bigr|$$

Note the absolute value. AUP is **two-sided by design**: it charges the agent for *gaining* attainable utility exactly as much as for losing it, because its purpose is to stop an optimiser accumulating power. The objective built below does the opposite — it rewards increases. No choice of norm reconciles the two, since every norm is even: replacing $|\cdot|$ with a squared or $\ell_2$ penalty sharpens the symmetry rather than removing it.

The one-sided cousin is *relative reachability* (Krakovna, Orseau, Martic and Legg, 2018), whose penalty takes the form $\max(0,\, \gamma_{\text{baseline}} - \gamma_{\text{current}})$ and so charges only for *reductions* in what remains reachable. That is the shape §6 arrives at. And Turner's related *POWER* — the average optimal value over a distribution of reward functions — is the closest analogue of the expectation over goals, carrying neither a baseline nor an absolute value.

So: the expectation over a distribution of goals is close to POWER. The baseline-relative, one-sided structure is relative reachability's. What $K$ is emphatically *not* is AUP: AUP's absolute value penalises an agent for gaining attainable utility, where $K$ rewards people for gaining it.

The shapes agree and the signs do not, and the disagreement is more informative than a convergence would have been. Both literatures reach a baseline-relative measure of how much a set of goals can be achieved; they differ on **whose** power is being measured, and therefore on whether more of it is good. Restraining an optimiser and empowering a principal are the same quantity with opposite sign — which is exactly the question the bystander-disempowerment result in §9 turns on.

And note the reading of the whole object: it is a sum of log-likelihood-ratios, which is to say **agency is classical utilitarianism where the utility of a life is measured in bits of steering that the institution provides.** §1 warned that a product is also a sum. This is the sum it is.

## 7. Checking the toys

| | Raw product $\prod P_i$ | Geometric mean | $K(m)$ |
|---|---|---|---|
| Parking (lottery vs FCFS) | ✓ prefers lottery | ✓ | ✓ |
| Arena | partial — rescales | partial | partial (§8) |
| Locked room | ✗ all mechanisms score 0 | ✗ | ✓ impossible goal contributes $\log 1 = 0$ |
| Extra colonist | ✗ antinatalist | ✗ kills below-average | partial — neutral at baseline, but see below |
| Two planets | ✗ confounded | ✗ confounded | ✓ difficulty cancels |

And the standard objections, redone with arithmetic rather than assertion:

**World-destroyer button.** The empty world scores $K = 1$ (empty product). So does the null mechanism. Every institution that helps someone and harms nobody scores strictly above 1 (one that raises a person's ratio while lowering another's can score below it). Destroying the world is therefore *tied with doing nothing* and strictly dominated by any beneficial institution. Under the old definition it was optimal; this is the repair working.

**Repugnant conclusion.** It goes through, and there is no use pretending otherwise. In log form the objective is a *sum* over people, so adding $N$ individuals whom the institution helps only slightly — ratio $1+\varepsilon$ apiece — contributes $N\log(1+\varepsilon)$, which grows without bound in $N$. Enough barely-helped people dominate any smaller population the institution serves well. This is the same arithmetic as Toy 2: numbers always win against a bounded per-person term, and the log form does not escape it.

**Wireheading.** The vat resident achieves their one goal with certainty. But $\gamma$ is drawn through $\mathcal{H}$, and against the goals they *might* have had, the vat resident's ratios are far below 1. Scores badly. This argument depends entirely on the counterfactual-goals move in §3; drop it and wireheading is optimal.

**Gladiator.** Still tradeable, as computed in Toy 2. The victims' terms are large and negative but finite; enough spectators buy them. The correct statement is *this objective provides strong but bounded protection against domination*, and if you want an absolute veto you must give up separability.

**Killing.** Removing anyone the institution serves ($P_i > P_i^0$) strictly lowers $K$. Removing someone the institution serves *worse than the state of nature* raises it. That is the ordinary total-utilitarian implication about lives below neutrality — not, as an earlier reading of this had it, the sadistic conclusion, which is the different and worse claim that adding badly-off people can beat adding well-off ones. $K$ does not have that. The mitigating reading of what it does have: $K$ is at least reporting the right diagnosis, since an institution serving someone worse than nothing is failing them, and improving it dominates removing them.

### The population boundary

Put the last three bullets together and the shape of the problem is clear. $K$ is total utilitarianism in log-ratio coordinates. Total utilitarianism gets the repugnant conclusion. Every repair on offer costs something specific and known:

| Repair | Buys | Costs |
|---|---|---|
| Critical level $c^* > 1$ | avoids the repugnant conclusion | the sadistic conclusion; $c^*$ is a free parameter, losing the one thing the derivation gained |
| Per-capita average | avoids the repugnant conclusion | average utilitarianism: removing anyone below average raises the score |
| Bounded $f$ | nothing | a sum of bounded positive terms still diverges in $n$ |

This is not bad luck. **Arrhenius's impossibility theorems show that no population axiology satisfies all of a small set of individually compelling adequacy conditions**, and every one of those results turns on a condition ruling out the repugnant conclusion. There is no repair, here or anywhere, that pays nothing.

So the honest position is a boundary rather than a fix: **$K$ is a mechanism-ranking objective at fixed population, and it is not a population axiology.** Within its scope — which institution should this society adopt — the repugnant conclusion cannot be stated, because $m$ does not change who exists. Outside it, $K$ inherits the standard impossibility and lands on the repugnant horn, and anyone extending it to variable-population comparisons should say which horn they are choosing.

I would rather state that plainly than advertise a solved problem. Deriving an objective from axioms makes it very easy to imply that the axioms did more work than they did; here they fixed the aggregator and left population ethics exactly where they found it.

## 8. What the axioms do *not* settle

Five residual commitments, and one objection I have no answer to. Naming them is the point; pretending the objective is free of them is not available.

**The objection first, because it is the sharpest.** $K$ is an expectation over $\mathcal{H}$, so it does not depend on the *realised* preference profile at all. At the level of ranking institutions that is the entire point — it is what content-freeness means. But it has an awkward consequence one level down. A social choice rule that is constant in the realised profile is trivially monotonic in Maskin's sense, hence trivially implementable, and that should provoke suspicion rather than relief: a mechanism has to be responsive to what people actually want, and that responsiveness cannot come from an objective which is by construction blind to it. Something else must supply it. The most plausible candidate is letting $\mathcal{H}$ be updated by observed preferences, which reintroduces exactly the formation loop §9 says is unresolved. I do not know how to close this.

**The outer expectation.** A1–A7 constrain aggregation *across individuals* at a fixed goal vector. Nothing in them says how to aggregate across $\gamma$. Writing $\mathbb{E}_\gamma[\log K]$ rather than $\log \mathbb{E}_\gamma[K]$, or a minimum over the support, encodes a different attitude to goal uncertainty, and no axiom here selects among them. Having spent §4–§5 arguing that the choice of aggregator is the whole ballgame, it would be poor form not to admit that this one was picked silently.

**The threshold measure.** §3's reading of goals as upper contour sets needs a measure over thresholds — how demanding a bar counts as "the goal." Different measures rank institutions differently.

**The hyperprior $\mathcal{H}$.** "Content-free" is true only *conditional on a measure over goals*. Choosing $\mathcal{H}$ is a theory of human nature and therefore substantive. Everyone in this space pays this bill and it is instructive to see how differently: Legg and Hutter pay it with a Solomonoff prior $2^{-K(\mu)}$, arbitrary up to choice of universal machine; empowerment pays it by taking a max over input distributions instead of an expectation; AUP pays it with a set of randomly sampled auxiliary reward functions. That last one comes with encouraging news for §9's despair about tractability — in Turner's experiments, five uniformly random auxiliary goals sufficed in gridworlds, and in SafeLife a **single** randomly generated goal from a 16-dimensional VAE latent matched vanilla PPO while avoiding side effects. Coarse sampling of goal-space may be enough.

**The baseline $\varnothing$.** "State of nature" is not well-defined for a real society, and different baselines rank mechanisms differently. AUP has the identical problem and found that a *stepwise inaction* baseline worked best empirically. This is probably the weakest joint in the derivation.

**Separability.** Kept in A4, and Toy 2 showed the price: no absolute protection of the worst-off. Dropping it gives Rawlsian maximin, which buys the veto and pays by becoming blind to everything above the floor. The two candidates sit at different points on the same frontier, and this post does not claim the choice is forced.

**Equilibrium selection.** $\sigma^*(\gamma, m)$ is not a function when the induced game has multiple Nash equilibria, so $K$ is not well-defined without a selection rule — and selection is substantive. Worse, Nash equilibrium presumes purely non-cooperative play, which is a strange primitive for a *social* objective, since coalitions, contracts and institutions are exactly what one would want to design. Correlated equilibrium is the natural relaxation. Computing a Nash equilibrium is PPAD-complete, so "tractable on toy systems" means genuinely tiny ones — which is a further argument for the relaxation, since a correlated equilibrium of a normal-form game is computable in polynomial time by linear programming.

## 9. Limitations

**Population comparisons.** $K$ ranks mechanisms for a fixed population and is not a population axiology; the boundary and its cost are set out at the end of §7.

**Adaptive preferences, again.** §3's counterfactual-goals move handles wireheading, but it relocates the problem rather than dissolving it: $\mathcal{H}$ must itself be estimated, and estimating "what humans might want" from a population whose wants were formed under existing institutions is circular. Sen's own critique bites here.

**Goal formation is not separable from the mechanism.** The mechanism that aggregates preferences also *shapes* the preferences it aggregates — free press, education, market structure all condition the goals that arrive at the aggregator. Sen himself refuses to specify which capabilities matter, holding that the list should come from public reasoning. On that view the choice of objective and the design of the mechanism cannot be separated at all.

**Measurement infeasibility.** Computing $K(m)$ for a real society requires an expectation over an effectively infinite goal space and equilibria of games with billions of players. It is a *conceptual objective function*. Its value is in letting us study toy systems and ask formal questions about which mechanisms maximise it.

**One agent's agency is another's cage.** The most direct empirical warning comes from Yang et al., *When Empowerment Disempowers*: an assistant optimising a single human's empowerment measurably reduces a bystander's, in 27–96% of procedurally generated multi-agent gridworlds. This is exactly the failure the system-level definition was built to avoid, confirmed experimentally — and it is also a caution, because it shows that moving to an aggregate does not *automatically* fix it. Whether the specific aggregator derived here does is an empirical question that their Disempower-Grid suite is close to being able to answer. At societal scale the same worry is the subject of Kulveit et al., *Gradual Disempowerment*.

## 10. Closing

The two sentences at the top — everyone freer, capacity not content — plus anonymity, monotonicity, continuity, separability, Pigou–Dalton, difficulty invariance and population neutrality, force

$$\log K(m) = \mathbb{E}_{\Pi \sim \mathcal{H}}\,\mathbb{E}_{\gamma \sim \Pi}\sum_i \log \frac{P_i(m)}{P_i^0}$$

up to affine transformation. It is not a proposal checked against thought experiments; it is what the requirements leave standing. Four commitments remain unforced (§8) and should be argued about explicitly rather than smuggled.

**A note on the literature.** Most of the material above has been worked on for seventy years under the name *social choice theory* — Arrow, Sen, Harsanyi, Nash, Rawls, Parfit, Gibbard — and for thirty years under *intrinsic motivation* and *AI safety* — Klyubin, Polani, Salge, Legg, Hutter, Turner. Neither literature routinely cites the other, which is the actual gap this post is trying to stand in. The candidate function is not novel; what may be novel is deriving it from social-choice axioms and finding AUP's structure at the end.

Worth reading, roughly in order of how directly they bear:

- Sen, *Well-Being, Agency and Freedom* (1985) — the concept, and the argument that it can't be reduced to utility. Also his *Impossibility of a Paretian Liberal* (1970), which is a genuine impossibility result aimed at agency-preserving objectives and which this post has not yet met.
- Kreps, *A Representation Theorem for "Preference for Flexibility"* (1979) — why uncertainty about future tastes creates option value.
- Pattanaik and Xu (1990) on ranking opportunity sets — the axiomatic home of the per-individual dead ends behind Toy 1.
- Blackorby, Bossert and Donaldson on critical-level utilitarianism — the population-ethics machinery §5 rediscovers.
- Turner et al., *Optimal Policies Tend to Seek Power*, and the AUP empirical results — the closest formal cousin, with experiments.
- Salge and Polani, *Empowerment as Replacement for the Three Laws of Robotics*; Myers et al., *Learning to Assist Humans without Inferring Rewards* — the same move made at the level of a single assisted human.
- Yang et al., *When Empowerment Disempowers* — the counterexample, and the nearest thing to the benchmark this post asks for.
- Van Parijs, *Real Freedom for All* — maximin over real freedom, with a derived mechanism (basic income), and therefore a worked example of the objective→mechanism step this post stops short of.

**What would falsify this.** Three concrete predictions, offered so the position is refutable:

1. On a benchmark of toy societies, mechanisms ranked highly by $K$ should also rank highly on independently-measured outcomes (inequality, mobility, resilience to capture). If the rankings are uncorrelated, $K$ is measuring nothing.
2. $K$'s ranking of mechanisms should be *stable* under coarse random sampling of $\mathcal{H}$, as AUP's was. If the ranking flips when you resample the goal prior, the content-freeness claim is empty and $\mathcal{H}$ is doing all the work.
3. In multi-agent settings of the Disempower-Grid kind, an assistant optimising $K$ should exhibit measurably less bystander disempowerment than one optimising a single user's empowerment. If it doesn't, the aggregator isn't earning its keep.

Producing that benchmark is the open problem this series leaves on the table.

---

*This post is part of a series on [governance mechanisms](/governance-mechanisms/). The uncertainty about human goals that §2 takes as its starting point is argued for in the [model of human nature](/governance-mechanisms/human-nature/); and how much a designer may commit to in advance is derived in [minimality from uncertainty](/minimality-from-uncertainty).*
