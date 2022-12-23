---
layout: post
title: Confidence estimates via bets
---

Question that is bugging be;
what are the 'right' confidence estimates?

Well... that depends on ???
- the assumptions you make about the noise in the data!?
- incomplete coverage of the domain,
-

(Un)certainty via probabilities confuses me.
Given a fixed dataset, and some x, what is f(x)?
What is your uncertanty in that prediction?

Probabilities assume some inherent stochasticity.
What is the stochasticity in the model above?
We deterministically compute the output from the input.
We deterministically compute the model from the dataset.


But it isnt actually deterministic?!
- Random init of parameter effects the minima we descend to.
- ?

Does interpreting these as probabilities lead to any pathologies?

$$
\mathop{\text{min}}_{\theta} \mathop{\mathbb E}_{P(x, t)} \ell(x, t, \theta) \\
\mathop{\text{min}}_{\theta} \mathop{\mathbb E}_{D \sim \mathcal D} \sum_{(x, t) \sim D} \ell(x, t, \theta) \\
$$

### Bayes

$$
P(h| D) = \frac{P(D | h)P(h)}{\sum_H P(D| h) P(h)}
$$

Uncertainty over potential hypotheses.
Given P(h|D), how do we convert that into an uncertainty estimate for a single $x$?

$$
P(x, y | D) = \sum_H P(x, y | h) P(h|D)
$$

When is this computable!?!?

### Confidence via bets

Rather. We can ?? our confidence by betting on it.
For a given input, x, and some chosen label, y, we make a bet f(x, y). On whether the chosen label is the same as the true label, t.

$$
y, t \in \mathbb Z^n, x \in \mathbb R^d \\
\delta_{ij} =
\begin{cases}
    1,& \text{if } i == j\\
    -1,              & \text{otherwise}
\end{cases}
\\
\mathop{\text{max}}_{\theta} \sum_{(x, t)\sim D} \sum_y \delta_{yt} f(x, y, \theta)
$$



***

Relationship to;
- cross entropy?
- risk minimsation?
- probablistic uncertainty?

What notion of (un)certainty makes the most sense?
What properties should it have?
