---
layout: post
title: In what sense is Bayesian updating optimal?
subtitle: Minimizing Surprise Leads to Bayes' Rule
permalink: bayes-optimal
categories:
    - tutorial
---

<!-- When updating your beliefs in light of new data, you should choose the new belief system that satisfies the data constraints while being as "close" as possible to your original beliefs. You should not add any extra information or assumptions beyond what the data forces you to conclude. -->

You may have heard of Bayesian updating. We start with some prior beliefs, $p(\theta)$, we observe some data $D$, then we want to update our beliefs given this data;

$$
q(\theta) = \frac{p(D\mid\theta) p(\theta)}{p(D)}
$$

### A Simple Example: The Biased Coin

Let's say we're testing a coin for fairness.
*   **Parameter $\theta$**: The unknown probability of getting Heads ($0 \le \theta \le 1$).
*   **Prior $p(\theta)$**: We assume we know nothing, so we use a flat prior: $p(\theta) = 1$.
*   **Data $D$**: We flip the coin 4 times and get **Heads, Heads, Heads, Tails (HHHT)**.
*   **Likelihood $p(D\mid\theta)$**: The probability of seeing HHHT for a given $\theta$ is $p(D\mid\theta) = \theta^3 (1-\theta)^1$.

Our derivation shows that the optimal posterior $q(\theta)$ must be proportional to the prior times the likelihood:

$$
q(\theta) \propto p(\theta) \cdot p(D\mid\theta) = 1 \cdot \theta^3(1-\theta)
$$

The resulting posterior distribution is no longer flat. It now has a peak around $\theta=0.75$, reflecting the evidence from our four flips. This was the most "honest" update possible from our initial state of ignorance.

***

You may also have heard that Bayesian updating is "optimal." But what does that mean? If something is optimal, it must be minimizing or maximizing a specific metric. So, what is Bayes' rule actually optimizing?

It's not minimizing the error of a single prediction. Rather, Bayesian updating is optimal in the sense that it is the **most honest and conservative way to change your mind**. It updates your beliefs by the exact amount required by new evidence—no more, no less.

The metric it minimizes is a measure of "surprise" or "information gain" called the **Kullback-Leibler (KL) Divergence**. Let's dive in and prove this from the ground up using the calculus of variations.

### Background: The Tools We'll Need

Before we get to the main proof, we need to understand two key concepts.

#### 1. Kullback-Leibler (KL) Divergence

Imagine you have a set of beliefs, represented by a probability distribution $p(x)$. Then, you get some new information and update your beliefs to a new distribution, $q(x)$. The KL Divergence, $D_{KL}(q \parallel p)$, measures the "information gain" or "surprise" in moving from your prior beliefs ($p$) to your posterior beliefs ($q$).

$$
D_{KL}(q \parallel p) = \int q(x) \log\left(\frac{q(x)}{p(x)}\right) dx
$$

A key property is that $D_{KL}(q \parallel p) \ge 0$, and it is only zero if $q(x) = p(x)$ everywhere. Our goal will be to find a new belief distribution $q(x)$ that is as close as possible to our prior $p(x)$, meaning it minimizes this KL divergence. We want the least surprising update possible.

<!-- *[Image Description: An abstract, artistic visualization of information theory. Two colorful, flowing probability distributions are shown, a blue one labeled 'Prior p(x)' and a green one labeled 'Posterior q(x)'. Glowing lines of light connect the two distributions, representing the 'distance' or KL divergence between them. The style is sleek and modern.]* -->

#### 2. Lagrangian Multipliers: Optimization Under Constraints

Lagrangian multipliers are a powerful tool for solving optimization problems where you have constraints.

Imagine you want to find the minimum value of a function $f(x)$, but you are constrained to points where another function $g(x)$ equals zero. The core idea is to introduce a new variable, the Lagrange multiplier $\lambda$, and create a new function, the Lagrangian $\mathcal{L}$:

$$
\mathcal{L}(x, \lambda) = f(x) + \lambda g(x)
$$

The brilliant insight is that the solution to the constrained problem can be found at a **saddle point** of the Lagrangian. We are looking for a point where the gradient is zero with respect to both $x$ and $\lambda$. This means we are simultaneously trying to minimize $\mathcal{L}$ with respect to $x$ and maximize it with respect to $\lambda$. The full optimization problem is:

$$
\min_{x} \max_{\lambda} \mathcal{L}(x, \lambda)
$$

By finding the point where $\nabla \mathcal{L} = 0$, we find the minimum of $f(x)$ that also satisfies the constraint $g(x)=0$. We will use a more advanced version of this, the calculus of variations, to find an entire *function* that optimizes our objective.

<!-- *[Image Description: A 3D surface plot representing a Lagrangian function. The surface has a distinct saddle point. One axis is labeled 'Parameters x', another 'Lagrange Multiplier λ'. An arrow points to the saddle point, labeled 'Optimal Solution'. This visualizes the concept of finding a saddle point in a constrained optimization problem.]* -->

### The Proof: Minimizing Surprise Leads to Bayes' Rule

Our goal is to find the updated belief distribution $q(\theta)$ that minimizes the KL divergence from our prior $p(\theta)$, subject to what we learned from new data $D$.

**Objective:** Find $q(\theta)$ that minimizes $D_{KL}(q \parallel p) = \int q(\theta) \log\left(\frac{q(\theta)}{p(\theta)}\right) d\theta$.

**Constraints:**
1.  The new distribution $q(\theta)$ must be a valid probability distribution, meaning it must integrate to 1.
    $$ \int q(\theta) d\theta = 1 $$
2.  The new distribution must be consistent with the observed data $D$. We enforce this by requiring that the average log-likelihood of the data under our new beliefs is equal to some constant value, $L_D$, that represents the information in our observation.
    $$ \int q(\theta) \log(p(D\mid\theta)) d\theta = L_D $$

Now, we build the Lagrangian functional using two multipliers, $\lambda_1$ and $\lambda_2$:

$$
\mathcal{L} = \int q(\theta) \log\left(\frac{q(\theta)}{p(\theta)}\right) d\theta + \lambda_1 \left( \int q(\theta) d\theta - 1 \right) + \lambda_2 \left( \int q(\theta) \log(p(D\mid\theta)) d\theta - L_D \right)
$$

To find the function $q(\theta)$ that minimizes this, we use the calculus of variations and set the functional derivative of the integrand with respect to $q(\theta)$ to zero. This simplifies to taking the partial derivative of the terms inside the integral with respect to $q$ and setting it to zero:

$$
\frac{\partial}{\partial q} \left[ q\log q - q\log p + \lambda_1 q + \lambda_2 q\log(p(D\mid\theta)) \right] = 0
$$

$$
(\log q + 1) - \log p + \lambda_1 + \lambda_2 \log(p(D\mid\theta)) = 0
$$

Now, we solve for $q(\theta)$:

$$
\log q(\theta) = \log p(\theta) - \lambda_2 \log(p(D\mid\theta)) - (1 + \lambda_1)
$$

Exponentiating both sides gives us the form of the solution:

$$
q(\theta) = \exp(\log p(\theta)) \cdot \exp(-\lambda_2 \log(p(D\mid\theta))) \cdot \exp(-(1+\lambda_1))
$$

$$
q(\theta) = p(\theta) \cdot p(D\mid\theta)^{-\lambda_2} \cdot C
$$

where $C = \exp(-(1+\lambda_1))$ is just a normalization constant.

The constant $C$ is determined by the first constraint (that the distribution integrates to 1). This forces $C$ to be the reciprocal of the integral of the remaining terms:

$$
C = \frac{1}{\int p(\theta) p(D\mid\theta)^{-\lambda_2} d\theta}
$$

The denominator is the definition of the marginal likelihood, or evidence, $p(D)$. Substituting this back in, we arrive at our final result:

$$
q(\theta) = \frac{p(D\mid\theta) p(\theta)^{-\lambda_2}}{p(D)}
$$

<!-- *[Image Description: A graph with three curves. The first, labeled 'Prior', is a flat horizontal line, representing uniform belief. The second, labeled 'Likelihood', is a curve that starts at zero, peaks at θ=0.75, and goes back to zero, representing the evidence from the data. The third, labeled 'Posterior', is a curve identical in shape to the likelihood (since the prior was flat), representing our new, updated beliefs.]* -->

### The Crucial Question: How to Choose $\lambda_2$?

We've arrived at the general form of the solution, which depends on the Lagrange multiplier $\lambda_2$:

$$
q(\theta) \propto p(\theta)p(D\mid \theta)^{-\lambda_2}
$$

This equation represents a family of possible update rules, all of which are "informationally conservative." The parameter $lambda_2$ acts as a knob controlling the balance between our prior beliefs and the new evidence.

The most conservative choice being $lambda_2=0$, meaning we completely ignore the observed data and just use the prior.

The least conservative choice being a large magnitude, eg $lambda_2=-100$ meaning we ...

<!-- note we could also set $lambda_2 to be positive? What would this do!? -->

TODO!!

<!-- Now, why should it match Bayes Rule??? Derive $\lambda_2 = -1$ as optimal for the case where; we've picked a scoring fn, assume access to accurate likelihood fn and not-too-wrong prior. Prove argmin_{lambda_2} Score(lambda_2) = -1  -->

<!-- after derivation of l_2 = -1 , then we can move to the following l_2 != -1 arguments. -->

### Afterthought: Deviating from Optimality for Better Results

So if Bayes' rule ($\lambda_2 = -1$) is optimal, why would we ever choose anything else? In modern machine learning, we sometimes do, trading theoretical optimality for pragmatic goals.

Let's define a guidance scale $\gamma = -\lambda_2$. The standard Bayesian update corresponds to $\gamma=1$.

#### The Case for Stronger Guidance ($\gamma > 1$)

In large-scale generative models like Stable Diffusion or Imagen, the goal is to generate an output (an image) given a condition (a text prompt). The model must balance its prior knowledge of what "natural images" look like with the likelihood that an image matches the prompt.

Researchers found that using the "optimal" $\gamma=1$ often produced images that were plausible but uninspired or didn't match the prompt very well. By choosing $\gamma > 1$ (e.g., $\gamma=7.5$), they force the model to pay much more attention to the prompt. This "sharpens" the posterior, leading to images that are a much better fit for the text, even if it means sacrificing some of the diversity from the prior. This technique is known as **classifier-free guidance**.[^1][^2]

#### The Case for Weaker Guidance ($0 < \gamma < 1$)

What about the other direction? When would we want to trust the data *less*?

This corresponds to choosing $\gamma < 1$. We might do this if we have reason to distrust the source of our data. For example:
*   The data comes from a noisy sensor.
*   We suspect the data was produced by an adversary trying to fool our model.
*   Our likelihood model $p(D\mid\theta)$ is known to be misspecified or overly confident.

In these cases, we can temper the influence of the data by setting $\gamma < 1$, which pushes our posterior closer to our prior beliefs, effectively saying, "I see the data, but I'm taking it with a grain of salt."

### Conclusion

Bayesian inference isn't just a useful formula; it's the unique, mathematically optimal solution to the problem of learning from evidence in the most conservative way possible. It is the benchmark for rational belief updating. And, fascinatingly, by understanding exactly what it optimizes, we also understand how and why we might choose to deviate from it, giving us powerful tools to control the behavior of modern AI systems.

---
#### References
[^1]: Ho, J., & Salimans, T. (2022). Classifier-Free Diffusion Guidance. *arXiv preprint arXiv:2207.12598*.
[^2]: Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., ... & Norouzi, M. (2022). Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding. *arXiv preprint arXiv:2205.11487*.