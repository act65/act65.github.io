---
title: Agency as the candidate objective
subtitle: Translating philosophical objectives into mathematics
layout: post
categories:
    - economic
permalink: /governance-mechanisms/agency/
---

Given the procedural framework from [Post 0](/governance-mechanisms/), the next question is which **social utility function (SUF)** the procedure should optimise. What is the target of the aggregation?

This post argues for **agency** — the capacity to achieve one's goals — as a strong candidate SUF. The argument has four parts. First, recall the evaluation criterion: a good SUF is *minimal-under-robustness* — it commits to as little content as possible while still guiding mechanism choice, because preferences are unknown and dynamic. Second, formalise the standard philosophical alternatives — happiness-maximisation, suffering-minimisation, opportunity-equality — and show how each fails. Third, define agency to capture what those failures point at. Fourth, check that agency scores well on the minimality-under-robustness criterion.

A companion post on the [derivation of agency](/governance-mechanisms/agency-derivation/) (Post 1b) walks the false starts and dead ends. This post moves directly to the result. Readers who want the empirical motivation for the whole series — why institutional design matters at all — should start with the [why-care](/governance-mechanisms/why-care/) entry point.

## 1. Two axes

Debates about "what should society maximise" usually conflate two distinct axes.

The first axis is *what* is being aggregated: hedonic happiness, suffering, capabilities, goal-achievement, opportunity, preferences.

The second axis is *how* the aggregation works: sum, product, minimum, weighted average.

Most disagreements are about the second axis dressed up as the first. The classical-utilitarian sum is famously vulnerable to the gladiator problem — a thousand people enjoying the suffering of two — which is a complaint about the *aggregator*, not about whether happiness is the right object to aggregate. Mixing the axes muddies the debate.

The argument here is mostly about the *what* axis: agency over happiness, suffering, capability. Aggregator choices are flagged where they bite but are not the central object.

## 2. The evaluation criterion: minimality under robustness

[Post 0](/governance-mechanisms/) argued that a good SUF is *minimal* — it constrains the collective's content as little as possible while still enabling decision-making. The motivation: preferences are both **unknown** (we don't fully observe them) and **dynamic** (they shift over time). At design time we have, at best, a hyperprior $\mathcal{H}$ over preference distributions $\Pi$ — a model of "what humans might want," not knowledge of any specific $\Pi$.

Under that uncertainty, a SUF that commits hard to one view of value (e.g., "maximise hedonic utility") performs well when $\Pi$ matches its assumed content but badly under other $\Pi$ in $\text{supp}(\mathcal{H})$. A minimal SUF — one whose action-rankings remain meaningful across many $\Pi$ in the support — generalises across the uncertainty set, even if it isn't maximal under any single $\Pi$.

This is the **minimality-under-robustness** criterion: a good SUF is one whose induced ranking of actions stays useful across the support of $\mathcal{H}$, not one that's optimal under a single assumed $\Pi$. A separate research note (*Minimality from Robustness*) develops the formal claim and a conjecture that as $\mathcal{H}$ widens, the optimal SUF $S^*$ becomes more invariant. This post takes the criterion as given and uses it to evaluate candidates.

The headline result: by this criterion, agency does well precisely because it rewards *capacity to pursue whatever preferences arise*, not any specific content. The sections below work through the alternatives first, then return to agency.

## 3. "Maximise happiness" — and what goes wrong

Classical utilitarianism formalises happiness-maximisation as

$$W(s) = \sum_i u_i(s)$$

where $u_i$ is a hedonic utility function and $s$ is the state of the world. The procedure picks $s$ to maximise $W$.

Five standard failure modes:

**Hedonic adaptation.** The unit being summed drifts. People adapt to circumstances; $u_i$ tomorrow is not $u_i$ today. Long-run optimisation against a moving target is ill-posed.

**Wireheading.** A sufficiently capable optimiser maximises $u_i$ by modifying the substrate that produces it. Optimal under this objective is everyone in a vat, on permanent positive stimulation. The achievable-state set collapses to one point.

**Repugnant conclusion (Parfit).** A very large population with lives barely worth living dominates a smaller population with very good lives, because the sum is larger.

**Gladiator problem.** A thousand people deriving small pleasures from the extreme suffering of two can outweigh the suffering on the sum. Sum-aggregation tolerates crushing minorities for majority benefit.

**Preference vs experience.** Does $u_i$ measure what people feel or what they want? The two diverge sharply when people want things that won't make them feel good.

The point of listing them is to notice that *some* are about happiness as the object (hedonic adaptation, wireheading, preference/experience) while others are about the aggregator (Parfit, gladiator). Different fixes apply.

## 4. Switching the aggregator: $\prod_i u_i$

Replace the sum with a product:

$$W(s) = \prod_i u_i(s)$$

This is the Nash social welfare function. It fixes some failure modes. The gladiator problem disappears: if even one person's $u_i$ is very low, the product is very low, regardless of the others. The repugnant conclusion gets harder to construct: a population with $u_i$ all barely above zero produces a near-zero product, not a large sum.

The product introduces its own failure modes:

**Veto.** Any single $u_i = 0$ zeroes the entire score. A person whose utility is unachievable obliterates the procedure's evaluation of every other state.

**Floor sensitivity.** The product effectively weights each person's utility by $1/u_i$ — improving the worst-off person dominates any improvement at the top. The behaviour is Rawlsian-flavoured: it inherits the strong-fairness virtue and the criticism that improvements above the floor are heavily discounted. Tradeoffs are still possible (raising one person from 1 to 3 can be worth lowering another from 10 to 5, since $5 \times 3 > 10 \times 1$), but the procedure systematically prefers raising the bottom over enriching the top.

**Fragility.** Small changes in the worst-off person's utility cause large changes in the score — and the score is sensitive to where you set zero. The product is not invariant under additive shifts of utility; a procedure that recommends one action under one zero-point can recommend a different action when the zero-point moves.

The product is not strictly better than the sum. It encodes different fairness properties and incurs different costs. **Choosing the aggregator is a substantive commitment** — exactly the kind of choice the framework post flagged as unavoidable. There is no neutral aggregator.

## 5. "Minimise suffering"

A different translation. Negative utilitarianism — Pearce explicitly, Popper often credited — replaces

$$\text{maximise} \sum_i u_i \quad \text{with} \quad \text{minimise} \sum_i \text{suffering}_i$$

These are *not* equivalent. The colloquial conflation ("we just want everyone to be okay") does real damage. Negative utilitarianism has characteristic conclusions:

**Antinatalism.** No humans means no suffering. A procedure aiming at minimum suffering should prefer a world with no future people to a world with any.

**World-destroyer button.** Press a button that ends sentient life on Earth: future suffering goes to zero. NU endorses pressing the button.

**Asymmetric weighting.** Tradeoffs between suffering reduction and happiness increase always resolve in favour of suffering reduction. Positive-sum interventions involving any new suffering are ruled out.

These conclusions are not bugs that the right NU variant fixes. They are the load-bearing consequences of choosing "no suffering" as the optimisation target. Variants exist (threshold NU, lexical NU, NU with side-constraints) that suppress them — but each variant adds *substantive* claims back in, undoing the apparent simplicity that motivated NU in the first place.

**An aside on connections.** Minimising $\sum_i s_i$ (NU-sum) and maximising $\prod_i u_i$ (Nash product) are more closely related than they look. Setting $s_i = -\log u_i$ makes the two equivalent: the Nash product is sum-utilitarianism applied to log-utility. The *what* axis and the *how* axis are not fully independent — a monotonic transformation of the object simulates a change of aggregator. Many apparent disagreements about objective functions turn out, on inspection, to be disagreements about utility scales.

## 6. "Equality of opportunity"

The phrase points at two distinct mathematical objects.

**Rawlsian maximin.**

$$W(s) = \min_i u_i(s)$$

Maximise $u_i$ of the worst-off member, where $u_i$ stands in for whatever notion of individual welfare you adopt — primary goods for Rawls, hedonic utility for utilitarians, basic capabilities for Sen. The maximin operator runs on top of whatever object you've chosen. Sensitive only to the floor; improvements above it are invisible. Strong fairness floor, weak ability to compare outcomes that share a floor.

**Capabilities approach (Sen, Nussbaum).** The object of evaluation is not realised welfare but the *set of states a person can reach*. A society in which everyone *can* read but few choose to is not worse than one in which everyone reads. The procedure values *freedom to achieve*, not achievement.

The capabilities approach is the direct ancestor of the agency definition that follows. What matters is not what people end up with but what they *could* end up with — the openness of their possibility space.

The catch is computability. Sen and Nussbaum present capabilities as a normative framework, not a computable objective. Translating capabilities into something a mechanism designer can optimise against is non-trivial.

## 7. Agency

Take the capabilities intuition seriously and try to formalise it. The target candidate is

$$K_{system} = \sum_{\gamma} \prod_i P(g_i \mid \sigma^*(\gamma))$$

Unpacking:

- A **joint goal vector** $\gamma = (g_1, \ldots, g_n)$ assigns one goal to each member of society. The outer sum ranges over all such vectors (in practice a distribution over them).
- For each $\gamma$, individuals act according to a strategy profile. The stable outcome is the **Nash equilibrium** $\sigma^*(\gamma)$ — the strategies where no individual can do better by deviating unilaterally.
- At that equilibrium, each individual has some probability $P(g_i \mid \sigma^*(\gamma))$ of achieving their goal. The **product** across individuals scores the joint outcome.
- The outer sum scores the system's general capacity to handle the goals its members might hold.

The companion post on the [derivation of agency](/governance-mechanisms/agency-derivation/) walks through why simpler definitions fail (count of immediate actions, count of futures, probability-weighted futures, individual achievability). The short version: any definition that scores agency *per individual* misses the fact that achievability depends on other people's strategies. Whether you can park in the last spot at the destination is determined by whether someone else also wants it.

The product-of-probabilities is the Nash social welfare function applied to *goal-achievement probabilities*. It inherits the fairness properties of Section 4 and their costs. This is a choice; alternatives (geometric mean, weighted product, min over goals) make different tradeoffs.

**Agency under the minimality-under-robustness criterion.** Agency-as-SUF is *content-free*: it doesn't commit to which goals should be pursued, only to preserving the capacity to pursue *whatever* goals arise from whichever $\Pi$ obtains. Under hyperprior uncertainty over $\Pi$, this is exactly the structure §2 argued is robust — a SUF whose action-ranking remains meaningful across many possible preference distributions rather than being tuned to one. Maximise-hedonic-utility commits to which preferences "really" count; minimise-suffering prioritises one axis; agency does neither. That is why agency tends to do well as $\mathcal{H}$ widens. Rawlsian maximin shares the structure for the same reason — protecting the worst-off is also content-free — and the two candidates can be located near each other on the minimality–informativeness frontier.

## 8. How agency behaves on the failure modes

**Wireheading.** An optimiser maximising hedonic utility collapses everyone to a single state. Their goal-achievement probabilities, evaluated over the space of plausible goals, drop sharply — they can no longer pursue anything except continued stimulation. $K_{system}$ scores this low.

**Repugnant conclusion.** Classical utilitarianism endorses creating a huge population with lives barely worth living, because the sum of low utilities can be made arbitrarily large. Under agency, each individual in such a population has low $P(g_i)$ for almost any goal — there isn't enough slack in a life barely worth living to support meaningful goal-pursuit. The product of many small numbers is very small, so $K_{system}$ does not recommend the trade.

**Gladiator problem.** The two suffering individuals have $P(g_i)$ near zero for any plausible goal. The product across the whole society goes to zero. Even with many high-utility spectators, the arrangement scores poorly.

**World-destroyer button.** Ending sentient life sets $P(g_i)$ to zero for everyone with a goal. $K_{system} \to 0$.

Agency inherits these properties because its aggregator is a product (non-domination) and its target is the *space of achievable goals* rather than realised utility. It is not the only definition that has these properties — Rawlsian maximin shares some — but it differs in what it sees inside the space of "agents doing well": maximin sees only the worst-off; the product is sensitive to imbalance everywhere.

## 9. Limitations

**Adaptive preferences.** Goals are taken as exogenous; the formalisation does not specify where they come from. Sen's own critique applies: goals formed under oppression may endorse the oppression. This is the *preference-elicitation* problem in another guise — the mechanism doesn't just aggregate preferences, it conditions their formation. [Post 2](/governance-mechanisms/mechanism-design/) takes this up directly: a good aggregation mechanism is also a good preference-formation mechanism, and the two cannot be designed separately.

**Goal formation is not separable from the mechanism.** The mechanism that aggregates preferences is also one of the things that *shapes* the preferences it aggregates. Free press, education, market structure all condition the goals that arrive at the aggregator. $K_{system}(m)$ is not separable into "the goal set" times "the mechanism." Forward link to [Post 2](/governance-mechanisms/mechanism-design/).

**Measurement infeasibility.** Computing $K_{system}$ for a real society requires summing over an effectively infinite space of joint goal vectors and finding Nash equilibria for games with billions of players. $K_{system}$ is a *conceptual objective function*, not a measurable quantity. Its value is in letting us study toy systems and ask formal questions about which mechanisms maximise it.

## 10. Closing

Agency is a strong candidate SUF under the minimality-under-robustness criterion: *the system's capacity to enable its members to achieve their goals, weighted by a product across individuals to penalise domination*. It survives the failure modes of happiness-maximisation, suffering-minimisation, and the simpler readings of equality-of-opportunity, while inheriting the capabilities-approach intuition that what matters is what people *can* do, not just what they end up with. Crucially, it is content-free — it doesn't commit to which preferences should be pursued, only to preserving the capacity to pursue whatever preferences arise — which is the structural reason it generalises across uncertain $\Pi$.

It is not the only candidate. Future work should compare it directly against the alternatives — including hybrid objectives that take parts from several — on a common set of toy systems where computation is tractable.

**A note on the literature.** Most of the material above has been worked on for seventy years under the name *social choice theory*. Arrow, Sen, Harsanyi, Nash, Rawls, Parfit, Gibbard — these are the names. The candidate functions tested here are not novel. What may be novel is the framing: treating the choice of objective as input to a downstream mechanism-design optimisation, and treating *agency* (the Nash product of goal-achievement probabilities at equilibrium) as a specific computable instantiation of Sen and Nussbaum's capabilities approach. The [companion derivation post](/governance-mechanisms/agency-derivation/) and [Post 2](/governance-mechanisms/mechanism-design/) give more pointers into the literature.

**A research note.** The comparison above relies on a small set of thought experiments — gladiator, repugnant conclusion, world-destroyer, wireheading. These work as sanity checks but are not a real evaluation. A proper test of candidate objective functions would need a *benchmark*: a structured set of toy systems and conditions, each probing a specific property (fairness, robustness to capture, behaviour under uncertainty, sensitivity to scale, etc.). Producing that benchmark — and running candidate objectives against it — is one of the open problems this series leaves on the table.

The next question, given the candidate target, is what kind of mechanism aggregates preferences toward it. [Post 2](/governance-mechanisms/mechanism-design/) takes that up.
