---
layout: post
title: Regret is a vector
subtitle: Who bears the cost when a collective learns which policy is best?
permalink: /regret-is-a-vector/
description: "When a collective learns by trial and error, regret is not a number but a vector with one entry per person. For any learner that eventually finds the best total, the per-person entries are forced, and they concentrate on whoever loses from near-optimal, contested policies."
tags:
  - research
  - formalised
  - uncertainty
  - aggregation
  - mechanism-design
  - reinforcement-learning
---

A bandit algorithm's regret is a number: how much reward it gave up while learning. That makes sense when one agent chooses and the same agent receives the reward. When a collective chooses a policy that applies to everyone, each person receives a different reward from the same choice, and regret becomes a vector with one entry per person.

This post asks a narrow question about that vector. Suppose a planner learns in the standard way, maximising total welfare. **Who ends up carrying the cost of the learning?**

The answer, under fairly standard assumptions, is exact, and it doesn't depend on which good algorithm the planner uses. The cost concentrates on people who lose from policies that are *nearly optimal in aggregate but contested*. The companion essay, [Who pays for exploration?]({{ site.baseurl }}/who-pays-for-exploration/), discusses what a society might do about it. This post only tries to get the shape of the problem right.

## 1. Setup

$N$ people, $K$ policies (arms). Policy $a$ gives person $i$ an unknown mean reward $\mu_{i,a}$. Each round $t = 1, \dots, T$ the planner chooses one policy $a_t$, which applies to everyone. This is the important difference from a clinical trial: the arm is a *public* good, so the planner cannot give different people different arms.

The planner's objective is utilitarian welfare,

$$W(a) = \sum_{i=1}^N \mu_{i,a},$$

with a unique maximiser $a^\star$. After each round the planner observes a noisy sample of everyone's reward, with independent Gaussian noise of variance $\sigma_i^2$ on person $i$. Write $\sigma^2 = \sum_i \sigma_i^2$.

Define the gaps

$$\delta_{i,a} = \mu_{i,a^\star} - \mu_{i,a}, \qquad \Delta_a = W(a^\star) - W(a) = \sum_i \delta_{i,a}.$$

$\Delta_a > 0$ for every $a \neq a^\star$, but an individual gap $\delta_{i,a}$ can have either sign: some people prefer a policy that is worse in total.

**Per-person regret.** Person $i$'s regret is how much worse off they were during learning, relative to the policy the planner is trying to find:

$$R_i(T) = \sum_{t=1}^T \left(\mu_{i,a^\star} - \mu_{i,a_t}\right) = \sum_{a \neq a^\star} n_a(T)\, \delta_{i,a},$$

where $n_a(T)$ is the number of rounds policy $a$ was used. The usual utilitarian regret is the sum, $R(T) = \sum_i R_i(T) = \sum_a n_a(T)\Delta_a$.

Two things about this definition are worth saying up front.

- $R_i$ is measured against $a^\star$, not against person $i$'s favourite policy. It isolates the cost of *learning*, not the cost of living under a utilitarian choice. Those are different complaints, and this post is only about the first.
- $R_i$ can be negative. Someone who prefers a policy the planner is testing does better while it is being tested. Exploration has winners.

## 2. The shares

Define person $i$'s **share** of policy $a$'s aggregate gap,

$$\kappa_{i,a} = \frac{\delta_{i,a}}{\Delta_a}, \qquad \sum_i \kappa_{i,a} = 1.$$

Each time policy $a$ is tried, the collective loses $\Delta_a$, and person $i$ pays $\kappa_{i,a}$ of it. If everyone is affected equally, $\kappa_{i,a} = 1/N$. If a policy is *polarising* — good for some, bad for others — then some shares are negative and others exceed 1. A person can pay more than the whole collective loses, because others gain.

## 3. The result

**Proposition 1.** For any planner that is asymptotically optimal for utilitarian welfare (in the Lai–Robbins sense; for example KL-UCB or Thompson sampling with known variances),

$$\lim_{T\to\infty} \frac{\mathbb{E}[R_i(T)]}{\log T} = 2\sigma^2 \sum_{a \neq a^\star} \frac{\kappa_{i,a}}{\Delta_a} \;=\; 2\sigma^2 \sum_{a \neq a^\star} \frac{\delta_{i,a}}{\Delta_a^2}.$$

*Proof sketch.* $\mathbb{E}[R_i(T)] = \sum_a \mathbb{E}[n_a(T)]\,\delta_{i,a}$ exactly, because the policy applies to everyone. So the per-person regret is a fixed linear function of the pull counts. For a Gaussian welfare signal, the Lai–Robbins lower bound says any consistent planner must have $\mathbb{E}[n_a(T)] \geq (2\sigma^2/\Delta_a^2)(1 - o(1)) \log T$, and asymptotically optimal planners match it. Observing individual rewards rather than only the total doesn't help: the cheapest way to perturb the instance so that $a$ becomes optimal costs $\Delta_a^2 / (2\sigma^2)$ in KL either way, by minimising $\sum_i d_i^2/(2\sigma_i^2)$ subject to $\sum_i d_i = \Delta_a$. $\square$

<!-- TODO: write out the perturbation argument carefully, and check that the individual observations really give no extra information about which arm is welfare-optimal. -->

Summing over $i$ recovers the familiar $2\sigma^2 \log T \sum_a 1/\Delta_a$. What is new is the distribution.

**Reading it.** Person $i$'s burden is a sum over policies of (their share) × (how hard that policy is to rule out). Policies that are nearly optimal in aggregate, with small $\Delta_a$, have to be tried about $1/\Delta_a^2$ times. If such a policy is also polarising, the people who lose from it pay a share far above $1/N$ of a cost that is already the largest in the sum.

**Corollary (forced).** Because the lower bound holds for every consistent planner, this burden is not a choice of algorithm. Any planner that eventually finds the welfare-optimal policy must impose, asymptotically, at least the burden in Proposition 1 on the losers from each policy. Planners can differ only in lower-order terms.

That last statement needs care for people with mixed signs: a planner could in principle over-test a policy person $i$ likes and so reduce $R_i$. But that raises utilitarian regret by a $\log T$-order amount, so it is not available to an asymptotically optimal planner.

## 4. An example

Three people, three policies.

| Policy | person 1 | person 2 | person 3 | $W$ | $\Delta$ |
|---|---|---|---|---|---|
| $a^\star$ | 1.0 | 1.0 | 1.0 | 3.0 | — |
| $b$ (polarising) | 1.5 | 1.5 | −0.1 | 2.9 | 0.1 |
| $c$ (uniformly worse) | 0.5 | 0.5 | 0.5 | 1.5 | 1.5 |

For $b$: $\delta = (-0.5, -0.5, 1.1)$, so $\kappa = (-5, -5, 11)$. For $c$: $\kappa = (1/3, 1/3, 1/3)$.

Per-person burden, in units of $2\sigma^2 \log T$:

- person 1: $-0.5/0.01 + 0.5/2.25 \approx -49.8$
- person 2: the same, $\approx -49.8$
- person 3: $1.1/0.01 + 0.5/2.25 \approx 110.2$

Total: about $10.7$. The collective's learning cost is about 11 units. Person 3 pays about 110, and persons 1 and 2 come out about 50 ahead each. Almost all of it comes from ruling out $b$, a policy that is nearly as good in total and very bad for one person.

So whether a learning process looks cheap depends a lot on which number you look at. The total says this is easy. Person 3 would not agree.

## 5. What can be done, in this model

**Transfers.** If utility were transferable, the planner could even out the realised vector after the fact, and only the total would matter. So the distribution of regret matters to exactly the extent that compensation is impossible. In this model the who-pays problem *is* the failure of transferability.

**Per-person budgets.** Suppose person $i$ is guaranteed $R_i(T) \leq B_i$, a kind of right not to be experimented on too much. If $B_i$ is below the forced burden in Proposition 1, no consistent utilitarian planner can honour it. Something has to give: stop learning (and accept regret linear in $T$), change the objective, or forbid the offending policy outright.

**Foreclosure.** Forbidding $b$ in advance removes person 3's burden entirely. But $b$ is unknown — that's why it needs testing — and if it is actually optimal, forbidding it costs $T$ times its advantage, forever. This is the trade-off in [Minimality from uncertainty]({{ site.baseurl }}/minimality-from-uncertainty/), and it points the other way: uncertainty about a policy is a reason *not* to forbid it. So a right not to be experimented on, which seems natural, is equivalent here to foreclosing exactly the uncertain, contested policies that the minimality argument says should stay open. I don't know how to resolve that.

**Changing the aggregator.** A weighted sum $W_w(a) = \sum_i w_i \mu_{i,a}$ changes both $\Delta_a$ and the shares, so it changes which policies count as nearly optimal and therefore who pays. Raising $w_3$ in the example makes $b$ clearly worse, so it is ruled out quickly. Something like max-min welfare doesn't fit the linear decomposition, and I haven't worked out what happens. Nash welfare regret, in the multi-agent bandit setting of Hossain, Micha & Shah (2021), is the nearest existing work, but there the regret is still collapsed to a single number.

**Partitioning.** If the population can be split into groups that each run their own policy (federalism), each group is a separate bandit, and a group's members only pay for policies tested on them. The cost is learning more slowly in each group, since each sees less data, unless information is shared between groups. I haven't worked this out either.

## 6. Assumptions, roughly in order of how much they matter

**Public arms.** Everything above relies on one policy applying to everyone. With private arms — different treatments for different people, as in a clinical trial — the planner can randomise *who* is exposed, and the burden can be equalised in expectation (though not after the fact). The gap between trials and legislation is largely this one assumption.

**Utilitarian target.** The planner wants $a^\star = \arg\max W$. A planner aiming at something else has different gaps and different forced burdens. The general point should survive: whatever is being maximised, the near-ties under that objective get explored most, and whoever is hurt by them pays most.

**Regret against $a^\star$.** Measuring against the welfare-optimal policy is a choice. Measuring against the status quo instead would ask a different question: who was made worse off by trying anything at all? I suspect that is closer to what people mean when they complain about reform, and it would be worth doing.

**Stationarity and asymptotics.** Means are fixed, and the result is a $\log T$ limit. Real policy runs for a handful of rounds, not asymptotically many, and the world shifts under it. The finite-$T$ picture is probably dominated by which policies get tried at all, which this analysis says nothing about.

**No strategic behaviour.** People report rewards honestly and stay put. In reality the losers from $b$ would object, organise, or move, which is to say they would change the information the planner sees. Incentivized exploration (Kremer, Mansour & Perry 2014) studies the case where people can refuse to explore. Combining that with per-person accounting looks like the natural next step.

## References

- Lai, T. L., & Robbins, H. (1985). Asymptotically efficient adaptive allocation rules. *Advances in Applied Mathematics*, 6(1), 4–22.
- Hossain, S., Micha, E., & Shah, N. (2021). Fair algorithms for multi-agent multi-armed bandits. *NeurIPS*.
- Kremer, I., Mansour, Y., & Perry, M. (2014). Implementing the "wisdom of the crowd". *Journal of Political Economy*, 122(5), 988–1012.
