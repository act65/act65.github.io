---
layout: post
title: Discounting, risk, and uncertainty.
---

Why do we discount future rewards? What priors does it imply?
Should discounting be a function of uncertainty?

### Machine behaviour

Lets just build some intuition for what the discount does, what it controls, etc.

Define depression as:
Define succeptibility to addiction (/ impulsiveness) as:


Want some intuitive examples

## Discounting

__Q:__ Why do we discount? Could use the average reward.

__TODO__ Want to derive the need for a discount when there is noise within the model used by a planner.


### Discounting for uncertainty

$$
\begin{align}
Q(s_t, a_t) &= r(s_t, a_t) + \gamma \mathop{\mathbb E}^{s' \sim P(\cdot | s_t, a_t)}_{a\sim \pi(\cdot| s')} Q(s',a)\\
Q(s_t, a_t) &= r(s_t, a_t) + \gamma \sum_{s'}P(s'|s_t, a_t)\sum_a \pi(a | s') Q(s',a)\\
\end{align}
$$

##### Policy entropy

$$
\begin{align}
Q(s_t, a_t) &= r(s_t, a_t) +  \sum_{s'}P(s'|s_t, a_t) \gamma(s_t)\sum_a \pi(a | s') Q(s',a)\\
\gamma(s) &= 1-\mathop{\mathbb E}_{a\sim\pi(\cdot | s)}[-\log(\pi(a | s))]\\
\end{align}
$$

For many possible actions, this could be expensive to calculate at every step.

Can this still be solved as a set of linear equations?

Take a minimum entropy policy, $H(\pi) = 0$, then $\gamma = 1$. This is a deterministic policy, yielding zero ... making it far easier to plan.

##### Transition entropy

$$
\begin{align}
Q(s_t, a_t) &= r(s_t, a_t) +  \gamma(s_t, a_t)\sum_{s'}P(s'|s_t, a_t) \sum_a \pi(a | s') Q(s',a)\\
\gamma(s, a) &= 1-\mathop{\mathbb E}_{a\sim P(\cdot | s, a)}[-\log(P(s' | s, a))]\\
\end{align}
$$


## Discount rates

Why exponential discounting?


How to deal with uncertainty?

## Uncertain transitions.

We should only get less certain about future states.

$$
H(s_t) \le H(s_{t+1}) \\
$$

Want to enforce this prior.

- In the tabular case, this naturally occurs as a function of the row normalisation.
- In a function approximation case, how can we enforce this prior?

$$
R(s_t, a_t) = \big | \log(\frac{H(\tau(s_t, a_t))}{H(s_t)} ) \big | \\
$$

Properties.
- Asymmetric. Care a lot if $H(s_t) \le H(s_{t+1})$ but not so worried about $H(s_t) \ge H(s_{t+1})$.
- ?

***

- [Hyperbolic Discounting and Learning Over Multiple Horizons](https://openreview.net/forum?id=rkezdaEtvH)
- [Discounted Reinforcement Learning Is Not an Optimization Problem](https://arxiv.org/abs/1910.02140)

***

What about a discount greater than 1?
