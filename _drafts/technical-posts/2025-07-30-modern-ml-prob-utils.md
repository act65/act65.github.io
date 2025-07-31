---
title: The Bayesian Computation Wishlist
subtitle: The fundamental operations that define the practice of Bayesian inference.
layout: post
categories:
    - proposal
---

This is a list of the core quantities and operations that form the toolkit of a Bayesian practitioner. It's a "wishlist" because, while these operations are what we *want* to do, performing them directly is often computationally intractable. The story of modern Bayesian methods is the story of finding clever ways to approximate these fundamental goals.

The unifying theme is clear: **nearly every one of these desirable operations is defined by a high-dimensional integral that is intractable with classical methods.** This is the wall we hit, and this is the wall that modern techniques from machine learning are designed to break down.

### Category 0: The Foundational Toolkit (The Primitives)

Before we can even speak of inference, we need two fundamental abilities. These are the absolute basics that everything else is built upon.

*   **1. Evaluating the Likelihood `p(D|θ)`**
    *   **What it is:** The ability to compute the probability (or probability density) of our observed data `D` for a *single, specific setting* of our model's parameters `θ`.
    *   **Why it's important:** The likelihood is the bridge from our parameters to our data. It's the component that allows data to "speak" and influence our beliefs. Without it, we can't perform Bayesian updating in its standard form.
    *   **The ML Connection:** This is a core competency of many models. Normalizing flows, for instance, are a class of generative models specifically designed to provide a tractable and computable likelihood for any data point. [^1] This is a significant advantage over other generative models where the likelihood is often intractable.

*   **2. Sampling from a Distribution `x ~ p(x)`**
    *   **What it is:** The ability to generate new samples (or examples) that follow a given probability distribution.
    *   **Why it's important:** Sampling is the language of modern computation. If you can draw samples from a distribution, you can approximate almost any other quantity you care about (like expectations or marginals). It turns hard calculus problems into easier programming problems.
    *   **The ML Connection:** This is the flagship capability of modern generative AI. Diffusion models have shown an incredible ability to generate high-quality samples from complex, high-dimensional distributions, starting from simple noise and iteratively refining it. [^2] Normalizing flows can also be used for efficient sampling.

### Category 1: The Core of Inference (Finding Our Beliefs)

These are the absolute essentials for getting from a prior to a posterior.

*   **3. Bayesian Updating (Calculating the Posterior)**
    *   **What it is:** The process of computing the posterior distribution `p(θ|D)` from the prior `p(θ)` and the likelihood `p(D|θ)`.
    *   **Why it's important:** This is the central goal of all Bayesian inference. The posterior distribution represents our complete state of knowledge about the parameters `θ` after observing the data `D`.
    *   **The Challenge & ML Connection:** The `p(D)` normalization constant is usually intractable. However, the ML world has developed a remarkable workaround. Diffusion models can be "guided" during their sampling process. By injecting information from the likelihood at each step, they can be steered to produce samples not from the prior, but directly from the posterior `p(θ|D)`. This "diffusion posterior sampling" is a revolutionary way to perform Bayesian updating without ever explicitly calculating the evidence. [^3]

*   **4. Calculating the Evidence (or Marginal Likelihood)**
    *   **What it is:** Computing the normalization constant `p(D) = ∫ p(D|θ)p(θ) dθ`.
    *   **Why it's important:** While we often try to *avoid* computing it for updating, the evidence itself is a crucial quantity. It represents the probability of the data *under our model*. A model that assigns a higher probability to the data we actually saw is a better model. This makes it the cornerstone of model comparison. [^4]
    *   **The Challenge:** A high-dimensional integral over all parameters; often the hardest single quantity to compute.

### Category 2: Interrogating the Posterior (Understanding Our Beliefs)

Once we have a way to represent the posterior (often as a set of samples), we need to ask it questions to extract meaningful insights. Most of these questions are applications of two powerful, general operations: marginalization and expectation.

*   **5. Marginalization**
    *   **What it is:** Taking the full joint posterior `p(θ_1, θ_2, ... θ_n | D)` and finding the distribution of a single parameter or a small subset, e.g., `p(θ_1 | D)`.
    *   **Why it's important:** We are rarely interested in all one million weights of a neural network simultaneously. We want to isolate specific parts of the model to understand their individual behavior and uncertainty. This is done by "integrating out" the nuisance parameters we don't care about.
    *   **The Challenge:** Involves integrating out all the other parameters. If we have samples from the joint posterior, however, this becomes trivial: we simply ignore the columns corresponding to the parameters we don't care about.

*   **6. Calculating Expectations**
    *   **What it is:** Computing the average value of a function `f(θ)` over the posterior distribution: `E[f(θ)] = ∫ f(θ) p(θ|D) dθ`.
    *   **Why it's important:** This is how we get concrete, single-number summaries from our posterior. If we have samples `θ_i` from the posterior, we can approximate this integral with a simple average: `E[f(θ)] ≈ (1/N) Σ f(θ_i)`. This is the foundation for many other queries:
        *   The **mean** of a parameter (`f(θ) = θ`).
        *   The **variance** of a parameter (`f(θ) = (θ - E[θ])²`), which quantifies its uncertainty.
    *   **The Challenge:** Requires integrating over the full posterior, which is made easy by sampling.

*   **7. Finding Modes (Maximum a Posteriori)**
    *   **What it is:** Finding the peak(s) of the posterior distribution, i.e., the most probable value(s) for the parameters `θ`. This is an optimization problem: `argmax_θ p(θ|D)`.
    *   **Why it's important:** Provides a simple point estimate summary of the posterior. It's often easier to find than the full distribution and is closely related to standard machine learning optimization (Maximum Likelihood Estimation).
    *   **The Challenge:** The posterior can have many modes, and finding the global maximum in a high-dimensional space is non-trivial.

*   **8. Quantifying Uncertainty (Credible Intervals & CDFs)**
    *   **What it is:** Finding a range that contains the true value with a certain probability (e.g., 95%). This is formally based on the **Cumulative Distribution Function (CDF)**, `F(x) = P(θ ≤ x) = ∫_{-∞}^{x} p(θ|D) dθ`.
    *   **Why it's important:** This is the Bayesian answer to "how sure are you?" It's more intuitive than a frequentist confidence interval and is a primary reason for using Bayesian methods. The CDF allows us to answer direct probability questions like, "What is the probability the effect is greater than zero?"
    *   **The Challenge:** Requires knowing the shape of the (marginal) posterior distribution. With samples, we can approximate the CDF and find credible intervals easily by looking at the empirical distribution of our samples (e.g., for a 95% interval, we can take the 2.5th and 97.5th percentiles).

### Category 3: Making Predictions and Comparing Models

This is where we use our beliefs to make decisions in the real world.

*   **9. The Posterior Predictive Distribution**
    *   **What it is:** The distribution of a *new, unseen data point* `x_new`, given our observations so far: `p(x_new|D) = ∫ p(x_new|θ)p(θ|D) dθ`.
    *   **Why it's important:** This is how we make predictions. It automatically averages the predictions of all possible parameter settings, weighted by their posterior probability. This naturally incorporates model uncertainty into our predictions. [^5]
    *   **The Challenge:** Another high-dimensional integral. But again, with posterior samples `θ_i`, this becomes a simple simulation: draw a `θ_i` from your posterior samples, then draw a `x_new` from `p(x_new|θ_i)`. Repeat many times to get a sample from the posterior predictive distribution.

*   **10. Bayes Factors for Model Selection**
    *   **What it is:** A ratio of the evidence of two competing models: `K = p(D|Model_1) / p(D|Model_2)`.
    *   **Why it's important:** This is the gold standard for Bayesian model comparison. It tells us how much the data has shifted our belief from one model to another. It has a built-in Occam's Razor, automatically penalizing overly complex models. [^6]
    *   **The Challenge:** Requires calculating the evidence for each model, which, as noted in #4, is very hard.

### Category 4: Information-Theoretic Quantities

These quantities measure information, surprise, and uncertainty in a formal way.

*   **11. Entropy**
    *   **What it is:** A measure of the total uncertainty or "volume" of a probability distribution: `H(p) = -∫ p(θ) log p(θ) dθ`.
    *   **Why it's important:** It gives us a single number to describe how "spread out" our beliefs are. A sharp posterior has low entropy; a diffuse prior has high entropy.
    *   **The Challenge:** Requires an integral over the log of the density itself.

*   **12. KL Divergence**
    *   **What it is:** A measure of the "distance" or information gain between two distributions, `p` and `q`: `D_KL(q || p) = ∫ q(θ) log(q(θ)/p(θ)) dθ`.
    *   **Why it's important:** It can measure the information gained by moving from the prior to the posterior. It's also the objective function in Variational Inference, a major alternative to MCMC for approximating posteriors. [^7]
    *   **The Challenge:** An integral involving two different distributions.

---
### References

[^1]: Papamakarios, G., Nalisnick, E., Rezende, D. J., Mohamed, S., & Lakshminarayanan, B. (2021). Normalizing Flows for Probabilistic Modeling and Inference. *Journal of Machine Learning Research, 22*(57), 1-64.
[^2]: Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. *Advances in Neural Information Processing Systems, 33*, 6840-6851.
[^3]: Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. *International Conference on Learning Representations*.
[^4]: Kass, R. E., & Raftery, A. E. (1995). Bayes Factors. *Journal of the American Statistical Association, 90*(430), 773-795.
[^5]: Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis, Third Edition*. CRC Press. (Chapter 7 covers posterior predictive checking).
[^6]: MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. (Chapter 28 provides a classic explanation of Bayes factors and Occam's Razor).
[^7]: Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). Variational Inference: A Review for Statisticians. *Journal of the American Statistical Association, 112*(518), 859-877.