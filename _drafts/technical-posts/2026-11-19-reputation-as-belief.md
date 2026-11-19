---
title: Reputation as a belief
subtitle: A Bayesian reading of decay, loan size and what a score should be
layout: post
permalink: /reputation-as-belief/
categories:
    - research
description: "Starting from one question, how likely is this person to keep their next promise, and deriving why reputation should decay and how large the next loan can be."
takeaways:
  - "If people can change, old evidence about them survives with a probability that shrinks with its age, so an estimate of their reliability regresses to the prior. Decay is derived, not chosen."
  - "Two decaying counters recover most of what the exact Bayesian filter knows, but they should forget several times faster than people change."
  - "If repaying reveals a threshold, the largest amount repaid is the statistic that matters, and a risk tolerance fixes how fast a ladder of loans may grow."
tags:
  - research
  - formalised
  - uncertainty
  - probability
  - trust
  - mechanism-design
---

A reputation score is usually designed: add some points for good behaviour, remove more for bad, tune until it feels right. [Rain]({{ site.baseurl }}/rain/) started that way too, with 25 points for a kept promise and 100 off for a broken one.

This post starts somewhere else, with the question a lender actually has:

> How likely is this person to keep their next promise?

and asks what a rational answer looks like. Two features of Rain that could have been design choices turn out to be consequences: that reputation fades, and that credit should grow step by step. The argument for the first is the one in [Why are future rewards worth less than present rewards?]({{ site.baseurl }}/discounting-via-uncertainty/), pointed at the past instead of the future.

{% assign n = site.data.rain %}

## If people never changed

Let $\theta$ be the probability that a given person keeps a promise. Across the population $\theta$ varies; say it follows $\mathrm{Beta}(a_0, b_0)$. That is the prior, what we believe about a stranger. After watching someone keep $K$ promises and break $B$,

$$ \theta \mid \text{data} \sim \mathrm{Beta}(a_0 + K,\; b_0 + B), \qquad \hat p = \frac{a_0 + K}{a_0 + b_0 + K + B} . $$

So reputation is two counts and a prior. Nothing fades: a promise kept ten years ago weighs the same as one kept yesterday. That is correct only if $\theta$ is fixed for life.

## People change, so evidence has to survive

Suppose that between any two promises, with a small probability $h$, a person's circumstances change and their $\theta$ is drawn afresh from the population. A promise kept $\tau$ steps ago is then evidence about the person in front of you only if no change has happened since, which has probability $\gamma^{\tau}$ with $\gamma = 1 - h$.

In the discounting post the possible worlds were split into those where a future reward survives an action and those where it does not, and the discount factor was the belief in the first set. Here the split is between worlds where this is still the person the evidence describes and worlds where it is not. In the first we have the posterior. In the second we have only the prior. So before the next promise

$$ p(\theta_{t+1} \mid \text{data}) \;=\; \gamma \, p(\theta_t \mid \text{data}) \;+\; (1-\gamma)\, \pi(\theta), $$

and the mean obeys

$$ \hat p_{t+1} = \gamma\, \hat p_t + (1 - \gamma)\, p_0 . $$

**With no new evidence, the estimate drifts back to what we would believe about a stranger, geometrically.** This step is exact. The decay rate is not a knob; it is a belief about how fast people change.

## What a contract can afford

Carrying that forward exactly is expensive. The mixture is not a Beta distribution, and each new promise adds a component: the exact estimate tracks a whole distribution over how long ago the last change happened.

A contract can store two counters per person and shrink both each step:

$$ K \leftarrow \gamma K, \qquad B \leftarrow \gamma B . $$

This is a different pooling of posterior and prior from the one above. It is their geometric mean, $p(\theta \mid \text{data})^{\gamma}\,\pi(\theta)^{1-\gamma}$, where the exact step is their arithmetic mean. Equivalently it is the distribution closest, in a weighted Kullback-Leibler sense, to both what the data said and to knowing nothing. Both versions regress to the prior. They differ in how.

How much does the cheap version lose? On data simulated from the model, scored by how well each method predicts the next outcome:

| How often people change, $h$ | Gap closed with $\gamma = 1 - h$ | Best $\gamma$ | Gap closed with the best $\gamma$ |
|---|---|---|---|
| 0.005 | {{ n.gap_matched_h005 }} | {{ n.best_gamma_h005 }} | {{ n.gap_best_h005 }} |
| 0.02 | {{ n.gap_matched_h02 }} | {{ n.best_gamma_h02 }} | {{ n.gap_best_h02 }} |
| 0.05 | {{ n.gap_matched_h05 }} | {{ n.best_gamma_h05 }} (edge of the range tried) | {{ n.gap_best_h05 }} |

*"Gap closed" is the share of the difference in prediction error between never forgetting and the exact filter. 2,000 simulated people, 300 promises each, five seeds.*

![Prediction error against forgetting rate, for three rates of change]({{ site.baseurl }}/assets/rain/forgetting-rate.svg)

Two things follow.

- **Two decaying counters are enough**, provided the decay rate is chosen well.
- **The right decay rate is not the rate of change.** I expected $\gamma = 1 - h$ to be best, and it was not: the counters should forget two to six times faster than people change. The reason is a trade-off. Forgetting faster makes the estimate noisier, in proportion to $1 - \gamma$. Forgetting slower leaves in evidence about someone who no longer exists, in proportion to $h/(1-\gamma)$. The sum is smallest when $1 - \gamma$ is proportional to $\sqrt{h}$, and the three optima sit close to $0.42\sqrt{h}$. That explanation came after the result, and the constant is fitted to three points.

So is decay slow? It is as slow as people are stable. If someone's reliability changes about once in 200 promises, the best memory is about 33 promises. With real data the rate should be fitted by asking which $\gamma$ predicts best. And never forgetting is close to useless once people change at all: at $h = 0.05$ it predicts barely better than ignoring the person's history ({{ n.static_loss_h05 }} against {{ n.prior_loss_h05 }}).

## Size

The model so far treats a promise to repay 10 and a promise to repay 10,000 as the same kind of evidence. They are not, and treating them alike is how a long record of small kept promises becomes the cheapest preparation for one large default.

Here is a model in which size matters. Each borrower has a private cost of defaulting, $c$: what their standing is worth to them. They repay when the amount due is at most $c$, apart from a small probability $q$ of a shock that makes them default regardless. Then repaying an amount $M$ reveals that $c \ge M$, and what a clean record tells you is not how many promises were kept but **the largest amount repaid**.

Let $c$ follow a Pareto distribution across borrowers, $P(c > x) = (x_{\min}/x)^{a}$, which has no built-in scale. Then for $X \ge M$

$$ P(\text{repay } X \mid \text{largest repaid } M) \;=\; (1 - q)\left(\frac{M}{X}\right)^{a} . $$

## How big can the next loan be?

A lender who accepts a probability $\rho$ of default on each loan can let the amount due grow to

$$ k_{\text{screen}} = \left(\frac{1 - q}{1 - \rho}\right)^{1/a} $$

times the largest amount repaid. This is lending on a ladder, with the size of the step derived from a risk tolerance. With $q$ = 2%, $\rho$ = 10% and $a$ = 1 it is {{ n.k_screen }}: nine percent a step. Doubling each time, with the same $q$ and $a$, means accepting a {{ n.doubling_risk }} chance of default.

That is the lender's side. The borrower's side bounds the step from below and above.

- **Honest borrowers must want to stay.** With interest $i$, a gain of $\sigma$ per unit borrowed and discount rate $r$, repaying is better than leaving when
  $$ k \;\ge\; \frac{(1+i)(1+r)}{1 + i + \sigma} . $$
  The loan size cancels, which is why this deterrent scales.
- **Climbing in order to default must not pay.** Someone with no use for the money who repays every rung and defaults on the last has paid interest on the way up. For a long ladder the interest exceeds the take when $k \le 1 + i$. At exactly $k = 1 + i$ the profit is the first loan, whatever the length: the first rung is the whole exposure.

With $i = r = 5\%$ and $\sigma = 3\%$ the step must lie between {{ n.k_stay }} and 1.05. Such a step exists exactly when

$$ \sigma + i \;\ge\; r , $$

that is, when what a borrower earns on borrowed money covers their own discount rate.

None of this is part of Rain. The log records the amount, deadline and outcome of every promise, and each lender can read $K$, $B$ and $M$ from it and apply whatever rule they like. This is one rule with its reasoning shown.

## What this says about Rain's score

- **It fades, and that is right.** Rain multiplies every score by a fixed fraction each period.
- **It is weighted by size, roughly.** A kept promise earns reputation in proportion to the fee paid on it, and the fee is a percentage of the amount. That is a sum, where the argument above wants a maximum; a lender can compute the maximum from the log.
- **It is one number where two are wanted.** A single score cannot tell a stranger from someone with a long mixed record. Rain's on-chain score counts kept promises only; broken ones are in the log.
- **The harsher penalty for a broken promise has no place in the belief.** A broken promise is one observation, as a kept one is. A lender who loses more from a default than they gain from a repayment should say so in the risk $\rho$ they accept.

## What else might follow from the same question

These are directions, not results. None has been derived or tested.

| Feature | The Bayesian reading it might have |
|---|---|
| The first loan to a stranger | Its expected loss is the price of information: what a lender should be willing to pay to learn which side of a threshold a borrower is on. That would fix the size of the first rung. |
| Vouching | A sponsor staking their own standing is evidence, with a likelihood ratio that depends on how much they stake and how good their own judgement has been. |
| Fees | A record is only as informative as it is costly to fake. The fee bounds how cheaply a false history can be manufactured, and so how much weight each entry can bear. |
| Who the promise was to | Promises kept to people you trust are better evidence than promises kept to strangers, who may be confederates. Each reader of the log could weigh it differently. |
| A decay rate per person | Some people's circumstances are more stable than others'. The rate of change could itself be inferred, person by person. |
| One model, not two | The first half of this post models unreliable people and the second half strategic ones. A threshold that drifts, with shocks, would be both. |

## What is established

| Claim | Status |
|---|---|
| If people change with probability $h$, the estimate regresses to the prior at rate $1 - h$ | Derived; exact for the mean. |
| Decayed counts are the geometric pooling of posterior and prior | Derived; exact for the Beta family. |
| Decayed counts predict nearly as well as the exact filter | Measured on data simulated from the model. |
| The best decay is faster than $h$, roughly as $\sqrt{h}$ | Observed at three values; explained afterwards. |
| Largest amount repaid is the statistic; the three bounds on the step | Derived from the threshold model and checked against it. Whether real borrowers have such thresholds is not known. |

The code is in [`rain/belief.py` and `rain/ladder.py`](https://github.com/act65/rain/tree/main/rain), and the experiment in [`experiments/bayes_decay`](https://github.com/act65/rain/tree/main/experiments/bayes_decay).
