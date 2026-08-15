---
title: Minimality from uncertainty
subtitle: How much of an action set should be foreclosed before you can learn?
layout: post
categories:
    - economic
permalink: /minimality-from-uncertainty/
description: "How much of an action set should be foreclosed before you can learn. Here is a problem that shows up whenever a rule has to be written before the thing it..."
tags:
  - research
  - mechanism-design
  - probability
---

Here is a problem that shows up whenever a rule has to be written before the thing it governs can be observed.

You have $K$ available options. Before you may take any of them, you must commit to a *subset* — the options that remain permissible. Only then do you begin choosing among them, learning as you go which are good. Restricting the set is valuable, because every option you leave available is one you will waste effort exploring. Restricting it is also dangerous, because you might delete the best one before finding out that it was.

**How aggressively should you prune, and on what criterion?**

The answer is exact, and the interesting part is how it depends on uncertainty: an option you are *unsure* about is one you cannot afford to remove, no matter how bad you expect it to be.

A word on the title, since "minimality" gets used loosely elsewhere. Here it means one thing only: **how much of the decision you decline to make in advance** — the size of the permitted set you leave behind, not the character of what you choose from it. A more minimal commitment forecloses fewer options. It says nothing about which option is good.

## 1. Setup

$K$ arms with unknown means $\mu_1, \dots, \mu_K$. A prior $\mu_i \sim \mathcal{N}(m_i, \sigma_i^2)$, independent across arms. Horizon $T$.

The problem is two-stage:

- **Stage 0 (commitment).** Choose $S \subseteq [K]$, the permitted set. This is fixed for the duration.
- **Stage 1 (operation).** Run a bandit algorithm on $S$ for $T$ rounds.

Measure everything against an oracle with access to all $K$ arms. The Bayesian regret of a commitment $S$ decomposes into two terms with opposite signs in $|S|$:

$$\mathrm{BR}(S) \;=\; \underbrace{T\cdot \mathbb{E}\Bigl[\max_{i\in[K]}\mu_i \;-\; \max_{i\in S}\mu_i\Bigr]}_{\text{exclusion cost}} \;\;+\;\; \underbrace{\rho\bigl(|S|,\,T\bigr)}_{\text{exploration cost}}$$

The **exclusion cost** is what you lose by having deleted the best arm before you knew which it was. It decreases as $S$ grows. The **exploration cost** is what a bandit algorithm must pay to identify the best arm within $S$. Take $\rho(k,T) = O(\sqrt{kT})$, the prior-free bound; note this is an upper bound and, being prior-free, is treated below as independent of the $\sigma_i$ — an assumption §6 returns to.

Note what this buys us. In problems of this shape one usually has to *posit* a cost for leaving a question open. Here it is derived: keeping an option available means paying to learn about it, and the price is set by the regret bound.

## 2. The value of keeping an option

Write $f(S) = \mathbb{E}[\max_{i \in S}\mu_i]$, with the convention $\max_{i\in\varnothing}\mu_i = 0$ so that $f(\varnothing)=0$ — equivalently, a null arm of known value zero is always available. The exclusion cost is $T\,(f([K]) - f(S))$, and minimising regret means maximising $g(S) = T f(S) - \rho(|S|,T)$.

**Proposition 1.** *$f$ is monotone and submodular, and its marginal gains are expected improvements:*

$$f(S \cup \{i\}) - f(S) \;=\; \mathbb{E}\bigl[(\mu_i - \textstyle\max_{j\in S}\mu_j)^{+}\bigr]$$

*Proof.* The marginal identity is $\max(y, x) - y = (x-y)^+$ applied pointwise with $y = \max_{j\in S}\mu_j$, then taking expectations. Monotonicity is immediate. For submodularity, let $A \subseteq B$ and $i \notin B$; write $\alpha = \max_A \mu$, $\beta = \max_B \mu$, so $\alpha \le \beta$ pointwise. Then $(\mu_i - \alpha)^+ \ge (\mu_i - \beta)^+$ pointwise, and taking expectations gives $f(A\cup i) - f(A) \ge f(B \cup i) - f(B)$. $\;\blacksquare$

Two consequences.

First, greedy is tractable where the exact problem — a search over $2^K$ subsets — is not. But the familiar $(1-1/e)$ guarantee does **not** transfer to $g$, and the reason is worth stating. Nemhauser–Wolsey–Fisher covers $\max\{f(S):|S|\le k\}$ for monotone submodular $f$; here the maximisation is unconstrained and $g$ is neither monotone nor submodular, since $\rho$ is concave in $|S|$, making $S\mapsto\rho(|S|)$ submodular and $-\rho(|S|)$ *super*modular. Nor does subtracting a penalty preserve a ratio: $g(\mathrm{OPT})$ can be small or negative.

What does hold: because $\rho$ depends on $S$ only through $|S|$, run greedy on $f$ alone at each cardinality $k \le K$ and keep the best result. Proposition 1 makes $f$ monotone submodular, so each run is within $(1-1/e)$ of the best set of that size — a guarantee on the **exclusion term**, not on the net objective. The sweep over $k$ matters: since marginal gain and marginal cost both decline in $k$, the increment to $g$ can turn negative and then positive again, so "add arms while the criterion holds, then stop" is not a valid rule.

Second, and more useful: the greedy criterion *is* **expected improvement**. The marginal value of keeping an option is exactly its expected improvement over the best of the alternatives you have already kept. EI is familiar as an acquisition heuristic in Bayesian optimisation; here it is not a heuristic but the exact marginal value in the commitment problem.

## 3. Uncertainty makes an option unprunable

Fix the incumbent level $z = \max_{j \in S}\mu_j$ at a constant — exact if $S$'s best is known, a standard approximation otherwise. For $\mu_i \sim \mathcal{N}(m, \sigma^2)$ and $\delta = (m - z)/\sigma$,

$$\mathrm{EI}(m, \sigma) \;=\; (m - z)\,\Phi(\delta) \;+\; \sigma\,\varphi(\delta)$$

**Theorem 2.** *$\mathrm{EI}$ is strictly increasing in $\sigma$, with*

$$\frac{\partial\,\mathrm{EI}}{\partial\sigma} \;=\; \varphi(\delta) \;>\; 0$$

*Proof.* Write $u = m - z$, so $\delta = u/\sigma$ and $\partial\delta/\partial\sigma = -u/\sigma^2$. Using $\varphi'(x) = -x\varphi(x)$,

$$\frac{\partial}{\partial\sigma}\bigl[u\,\Phi(\delta)\bigr] = -\frac{u^2}{\sigma^2}\varphi(\delta), \qquad \frac{\partial}{\partial\sigma}\bigl[\sigma\varphi(\delta)\bigr] = \varphi(\delta) + \frac{u^2}{\sigma^2}\varphi(\delta)$$

The second terms cancel, leaving $\varphi(\delta)$. $\;\blacksquare$

This is the result the setup was built for. **Uncertainty about an option strictly increases the cost of removing it — whatever you expect that option to be worth.** Not "uncertainty is a reason for caution" as a disposition, but an exact derivative, positive everywhere, with no dependence on the sign of $m - z$. An option you confidently believe is terrible but know little about is worth keeping; an option you confidently believe is mediocre and know a great deal about is not.

**Corollary 3 (you may prune only what you are confident is bad).** Along $m < z$: as $\sigma \to 0$, $\delta \to -\infty$ and $\mathrm{EI} \to 0$; as $\sigma \to \infty$, $\delta \to 0$ and $\mathrm{EI} \to \sigma\varphi(0) \to \infty$. So a prune is justified only in the corner where the mean is low *and* the variance is small. Low expected value alone never suffices.

## 4. Comparative statics

Greedy keeps arm $i$ when $T$ times its expected improvement exceeds the marginal exploration cost. With $\rho(k,T) = \tfrac12 c\sqrt{kT}$, the marginal cost of the $k$-th arm is $\tfrac{c}{4}\sqrt{T/k}$, so the criterion is

$$\mathrm{EI}_i \;>\; \frac{c}{4}\sqrt{\frac{1}{kT}}$$

**In uncertainty.** The threshold does not depend on $\sigma$, and by Theorem 2 the left side is increasing in it. So raising prior uncertainty — on any arm, or uniformly — weakly enlarges the permitted set. *More uncertainty forces a smaller commitment.*

**In horizon.** The threshold falls like $T^{-1/2}$. As $T$ grows, exploration amortises over more rounds while a wrongly excluded arm costs proportionally to $T$ forever, so the exclusion term dominates. **The longer the commitment will bind, the less it should foreclose.** A rule written for a decade should prune more aggressively than the same rule written for a century.

**In the number of options.** The threshold falls in $k$, and the direction repays care. Since $\mathrm{d}\rho/\mathrm{d}k = \tfrac{c}{4}\sqrt{T/k}$ is *decreasing* in $k$, the exploration saved by removing one more option is **largest** when the permitted set is already small: pruning has increasing returns, not diminishing ones. What rises instead is the exclusion risk, because greedy prunes in increasing order of expected improvement, so each successive cut costs more than the last. Breadth is cheap to extend and expensive to abandon.

## 5. What the model does not cover

**Exploration cost depends on $S$ only through $|S|$.** The strongest assumption here, and it runs in the direction of the conclusion, so it belongs first. High-$\sigma$ arms are precisely the expensive ones to explore; writing the cost as $\rho(|S|,T)$ assumes that away. A cost growing with the retained arms' uncertainty would push against keeping them, partly offsetting Theorem 2. Relatedly, $O(\sqrt{kT})$ is a prior-free upper bound, so §4's comparative statics are conditional on that functional form and the optimised value is a lower bound rather than the optimum.

**Bounded support.** Corollary 3's $\sigma\to\infty$ limit relies on Gaussian tails. If arm values are bounded — as they are in any application — EI is bounded above and a sufficiently bad high-variance option *can* be pruned. The claim then weakens from *uncertainty makes an option unprunable* to *uncertainty raises the bar for pruning it*: the same direction as Theorem 2, but a smaller assertion.

**The commitment is irrevocable.** Stage 0 is fixed for the duration. Constitutions get amended. Allowing revision at a cost softens every conclusion here, because a wrong prune can be undone.

**The incumbent level $z$ is treated as fixed.** §3 conditions on the best of the retained set. The exact greedy step compares against a random maximum, which couples the arms; Proposition 1 is exact, Theorem 2 is exact given $z$, and the composition is the standard EI approximation rather than a theorem.

**Independent priors.** Less is lost here than one might expect: Proposition 1's proof is pointwise in $\mu$, so the marginal-gain identity and submodularity both survive arbitrary dependence. What correlation breaks is the closed-form Gaussian expression in §3 — the marginal becomes an expectation under the joint law — and the assumption that exploration cost depends on $S$ only through $|S|$, since learning about one option informs you about its neighbours.

**The commitment is a subset.** Real restrictions are richer than deletions: conditional permissions, quantitative limits, and constraints on *combinations* of options. The subset model is the crudest possible commitment language.

**Stationarity.** $\mu$ is fixed while the algorithm runs. Drift cuts both ways and I do not know the net sign: an option pruned at time 0 may be best by time $T$, which argues for keeping more, but non-stationarity also raises exploration cost — regret with $L$ switches is $\Theta(\sqrt{kLT})$ — which lifts the threshold and argues for pruning more.

**Exogenous prior.** The most serious gap. The prior is assumed unaffected by the commitment. If foreclosing an option changes what is subsequently believed or wanted about it — plausible whenever the commitment is a rule that people live under — then $\sigma_i$ depends on $S$, and a prune that suppresses variance along its own dimension becomes self-justifying. The problem is then a fixed point rather than an optimisation and Theorem 2 no longer says what it appears to.

## 6. Summary

Given $K$ options, a prior over their values, and a requirement to fix the permitted set before learning anything:

- The marginal value of keeping an option is its **expected improvement** over the best option already kept. The exclusion cost is monotone submodular, so greedy-by-EI is $(1-1/e)$-optimal *on that term* at each fixed cardinality.
- $\partial\,\mathrm{EI}/\partial\sigma = \varphi(\delta) > 0$: **uncertainty about an option strictly increases the cost of removing it**, independent of how bad the option is expected to be. You may prune only what you are confident is bad.
- The permitted set grows with prior uncertainty and with the horizon over which the commitment binds: minimality, in the sense fixed above, is forced upward by both.

The last point is the one to carry away, and it inverts a common reading. "Under uncertainty, commit to less" is usually offered as humility. It is not a disposition but a threshold, and the threshold cuts both ways: when an option is confidently bad and the horizon is short, foreclosing it is not timidity avoided but the correct decision. **There is an optimal amount of commitment, it is strictly positive, and leaving everything open is as much an error as leaving nothing open.**