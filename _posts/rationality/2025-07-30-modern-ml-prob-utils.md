---
title: The Bayesian Computation Wishlist
subtitle: The fundamental operations that define the practice of Bayesian inference — and the one integral that stops us doing any of them.
layout: post
categories:
    - proposal
description: "The core quantities and operations that form the toolkit of a Bayesian practitioner, organised by what actually makes them hard: two primitives, one intractable integral, and a sharp line between what samples give you for free and what they never will."
tags:
  - notes
  - formalised
  - uncertainty
  - probability
  - machine-learning
---

This is a list of the core quantities and operations that form the toolkit of a Bayesian practitioner. It's a "wishlist" because, while these operations are what we *want* to do, performing them directly is often computationally intractable. The story of modern Bayesian methods is the story of finding clever ways to approximate these fundamental goals.

### The theorems that make this non-optional

It's worth being clear about why one would want this toolkit rather than some other one, because the answer is stronger than "it seems reasonable".

**Bayes' theorem** itself is the easy part — it's an identity, not a discovery:

$$p(\theta \mid D) = \frac{p(D \mid \theta)\, p(\theta)}{p(D)}, \qquad p(D) = \int p(D\mid\theta)\, p(\theta)\, d\theta$$

Everything below is a consequence of taking that seriously, and everything hard below is a consequence of that denominator.

What makes it more than a definitional rearrangement is a family of results saying that if you want to reason under uncertainty at all, you end up here whether you meant to or not:

- **Cox's theorem.** [^cox] If degrees of belief are real numbers, and you ask for a few consistency desiderata — that a belief depends only on the information you have, that it varies smoothly, that two valid routes to the same conclusion agree — then the calculus you get is probability theory, up to a rescaling. There are known gaps in Cox's original argument and in the desiderata as usually stated, [^halpern] so I'd treat this as suggestive rather than settled.
- **The Dutch book argument.** [^definetti] If your betting quotients violate the probability axioms, there is a set of bets you'd each accept individually that together lose you money with certainty. This one is narrower but airtight.
- **Wald's complete class theorem.** [^wald] This is the strongest of the three, and the one I find most persuasive. Under regularity conditions, every admissible decision rule — every rule not uniformly beaten by some other rule — is a Bayes rule with respect to *some* prior. You cannot escape being Bayesian by refusing to pick a prior; you can only be Bayesian with respect to a prior you didn't choose deliberately.

So the position is not "Bayesian inference is a nice framework". It is closer to: this is what coherent reasoning under uncertainty *is*, and the only open question is what it costs.

The answer is that it costs an integral over the entire parameter space, and the unifying theme of everything below is that **nearly every desirable operation reduces to a high-dimensional integral that is intractable with classical methods.** This is the wall we hit, and this is the wall that modern techniques from machine learning are designed to break down.

### How the list is organised

The original version of this list ran through the operations in roughly textbook order, which obscured the thing that actually matters. There are really only two capabilities, and then three tiers of consequence:

- **Two primitives:** evaluating a likelihood, and drawing samples.
- **One wall:** the evidence `p(D)`, the normalising integral.
- **The free tier:** everything that is an expectation of a *known* function under the posterior. Once you have samples, these are averages. They are on the list for completeness, not because they're hard.
- **The still-hard tier:** everything that needs the *normalised density itself* — entropy, divergences, evidence, information gain. Samples do not give you these, and this is the distinction the original list blurred.

That last split is the useful one. If you can write your quantity as `E[f(θ)]` for an `f` you can evaluate, you're done. If `f` involves `log p(θ|D)`, you're not, because you only ever know the posterior up to a constant — and that constant is the wall.

### Category 0: The primitives

Before we can even speak of inference, we need two fundamental abilities. Everything else is built on them.

*   **1. Evaluating the Likelihood `p(D|θ)`**
    *   **What it is:** The ability to compute the probability (or probability density) of our observed data `D` for a *single, specific setting* of our model's parameters `θ`.
    *   **Why it's important:** The likelihood is the bridge from our parameters to our data. It's the component that allows data to "speak" and influence our beliefs. Without it, we can't perform Bayesian updating in its standard form.
    *   **The ML Connection:** This is a core competency of many models. Normalizing flows are a class of generative models specifically designed to provide a tractable and computable likelihood for any data point, [^flows] which is a real advantage over generative models where the likelihood is intractable.
    *   **When you don't have it:** For many interesting models — epidemiological simulators, climate models, anything defined by a piece of code rather than a formula — you can *simulate* `x ~ p(x|θ)` but never *evaluate* `p(D|θ)`. This is the domain of simulation-based inference: ABC, and more recently neural approaches that learn the likelihood, the likelihood ratio, or the posterior directly from simulated pairs. [^sbi] It's a large hole in the list above, and worth knowing exists.

*   **2. Sampling from a Distribution `x ~ p(x)`**
    *   **What it is:** The ability to generate new samples that follow a given probability distribution.
    *   **Why it's important:** Sampling is the language of modern computation. If you can draw samples from a distribution, you can approximate most quantities you care about — with the specific exception of the ones in Category 3 below. It turns hard calculus problems into easier programming problems.
    *   **The ML Connection:** This is the flagship capability of modern generative AI. Diffusion models generate high-quality samples from complex, high-dimensional distributions, starting from noise and iteratively refining it. [^ddpm] Normalizing flows can also sample efficiently.

### Category 1: The wall

*   **3. Calculating the Evidence (or Marginal Likelihood)**
    *   **What it is:** Computing the normalisation constant `p(D) = ∫ p(D|θ)p(θ) dθ`.
    *   **Why it's important:** It's the probability of the data *under our model*. A model that assigns higher probability to the data we actually saw is a better model, which makes this the cornerstone of model comparison. [^kass] But its real significance is structural: it is the single quantity that everything else in the list is trying to avoid.
    *   **The Challenge:** A high-dimensional integral over all parameters, dominated by a region of parameter space that may be a vanishingly small fraction of the prior's volume. Usually the hardest single quantity here.
    *   **The ML Connection:** More developed than it's often given credit for. Nested sampling reparameterises the integral by likelihood level-set volume; [^skilling] annealed importance sampling and thermodynamic integration bridge from prior to posterior through a sequence of tempered distributions, paying for the estimate in compute; [^neal-ais] and variational inference gives you the ELBO, which is a *lower bound* on `log p(D)` and is often used as a stand-in. None of these is cheap, and their error bars are hard to trust.

*   **4. Bayesian Updating (Calculating the Posterior)**
    *   **What it is:** Computing the posterior distribution `p(θ|D)` from the prior and the likelihood.
    *   **Why it's important:** The central goal of Bayesian inference. The posterior represents our complete state of knowledge about `θ` after observing `D`.
    *   **The Challenge & ML Connection:** This is the same wall as #3 — but with a way around it. Because MCMC and most variational methods only need the *unnormalised* posterior, they sidestep `p(D)` entirely, which is why they work at all. More recently, diffusion models can be guided during sampling: by injecting likelihood information at each denoising step, they can be steered to produce samples from the posterior rather than the prior. [^dps] It's an appealing route, though the guidance term is itself an approximation (the likelihood of a noised intermediate is not available in closed form), so it inherits an error that's hard to characterise. MCMC and VI remain the workhorses.

### Category 2: Free once you can sample

Every item here is `E[f(θ)]` for a function you can evaluate. Given posterior samples `θ_i`, each is a one-line average. They are worth listing because they are what we actually want from the posterior — but they are not where the difficulty lives.

*   **5. Expectations.** `E[f(θ)] ≈ (1/N) Σ f(θ_i)`. Means (`f(θ) = θ`), variances, and any other summary you care to name.
*   **6. Marginalisation.** `p(θ_1|D)` from the joint posterior. With joint samples this is: ignore the columns you don't want.
*   **7. Credible intervals and CDFs.** The CDF is `F(x) = P(θ ≤ x)`, an expectation of an indicator function. A 95% interval is the 2.5th and 97.5th sample percentiles.
*   **8. The posterior predictive.** `p(x_new|D) = ∫ p(x_new|θ)p(θ|D) dθ`. Draw `θ_i` from your posterior samples, then draw `x_new ~ p(x_new|θ_i)`. This is how predictions get made, and it's how model uncertainty gets into them. [^bda]

The one genuine caveat is that "given posterior samples" is doing enormous work — it is exactly capability #2 applied to the hardest distribution in the problem. Monte Carlo error is `O(1/√N)` in the number of *effective* samples, and a badly mixing chain can give you a million samples worth about twelve.

*   **9. Finding Modes (Maximum a Posteriori)**
    *   This one doesn't fit the pattern and deserves its own note. `argmax_θ p(θ|D)` needs neither samples nor the normalising constant — it's optimisation on the unnormalised log posterior, which is why it's the cheapest thing on this list and why it's what most of machine learning actually does. It is also the least trustworthy summary: in high dimensions the mode is typically nowhere near the region where the posterior mass lives.

### Category 3: Still hard, even with samples

These involve the log-density of the posterior, not just functions of `θ`. Since we only know the posterior up to the constant `p(D)`, samples alone don't deliver them. This is the tier the original version of this list under-served.

*   **10. Entropy**
    *   **What it is:** `H(p) = -∫ p(θ) log p(θ) dθ` — the total uncertainty or "volume" of a distribution.
    *   **Why it's important:** A single number for how spread out our beliefs are. Sharp posterior, low entropy; diffuse prior, high entropy.
    *   **The Challenge:** It's an expectation of `log p`, and `log p` is exactly what we don't know. Estimating it from samples requires density estimation, which is its own hard problem, and nearest-neighbour estimators degrade badly with dimension.

*   **11. KL Divergence**
    *   **What it is:** `D_KL(q‖p) = ∫ q(θ) log(q(θ)/p(θ)) dθ` — the information gained by moving from one distribution to another.
    *   **Why it's important:** It measures what the data told us, as the divergence from prior to posterior. It's also the objective in variational inference. [^vi]
    *   **The Challenge:** Same problem, twice over. In VI it works only because the intractable part of the objective is a constant with respect to the thing being optimised — which is a trick, not a solution.

*   **12. Bayes factors for model selection**
    *   **What it is:** `K = p(D|M_1) / p(D|M_2)`.
    *   **Why it's important:** The standard route to Bayesian model comparison, with a built-in Occam's razor: it penalises models that spread their predictive mass thinly. [^mackay]
    *   **The Challenge:** Two evidence calculations, so twice #3. Also notoriously sensitive to the prior in a way the posterior isn't, which limits how much weight the answer deserves.

*   **13. Expected information gain**
    *   **What it is:** The mutual information between a future observation and the parameters: `EIG(d) = E_{x~p(x|d)}[ H(p(θ|D)) - H(p(θ|D, x)) ]`, the expected reduction in posterior entropy from running experiment `d`.
    *   **Why it's important:** This is the one I'd most want and it wasn't on the original list, which was an omission. It is the formal answer to "what should I do next" — the basis of Bayesian experimental design and of active learning, and the quantity that justifies maintaining a full posterior rather than a point estimate. If you only ever report a mean, you never needed any of this machinery.
    *   **The Challenge:** The worst on the list. It is a *nested* integral — an expectation over hypothetical future data of a quantity that itself requires a full posterior update, for every candidate experiment. Naive estimators are doubly-nested Monte Carlo with `O(1/√N)` bias as well as variance. The variational bounds that make it tractable at all are relatively recent. [^foster]

---

There's a companion to this post on [information geometry]({{site.baseurl}}/information-geometry-wishlist/), which has the same shape — a set of theorems saying there's a uniquely correct way to do something, and a computational wall that stops us. It may be the *same* wall: for an exponential family the whole geometry is the derivative tower of the log-normaliser, which is this post's `p(D)`.

---
### References

[^cox]: Cox, R. T. (1946). Probability, frequency and reasonable expectation. *American Journal of Physics, 14*(1), 1–13.
[^halpern]: Halpern, J. Y. (1999). A counterexample to theorems of Cox and Fine. *Journal of Artificial Intelligence Research, 10*, 67–85.
[^definetti]: de Finetti, B. (1937). La prévision: ses lois logiques, ses sources subjectives. *Annales de l'Institut Henri Poincaré, 7*(1), 1–68.
[^wald]: Wald, A. (1950). *Statistical Decision Functions*. Wiley. See also Berger, J. O. (1985). *Statistical Decision Theory and Bayesian Analysis*, 2nd ed., Springer, §8.
[^flows]: Papamakarios, G., Nalisnick, E., Rezende, D. J., Mohamed, S., & Lakshminarayanan, B. (2021). Normalizing flows for probabilistic modeling and inference. *Journal of Machine Learning Research, 22*(57), 1–64.
[^sbi]: Cranmer, K., Brehmer, J., & Louppe, G. (2020). The frontier of simulation-based inference. *Proceedings of the National Academy of Sciences, 117*(48), 30055–30062.
[^ddpm]: Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *Advances in Neural Information Processing Systems, 33*, 6840–6851.
[^kass]: Kass, R. E., & Raftery, A. E. (1995). Bayes factors. *Journal of the American Statistical Association, 90*(430), 773–795.
[^skilling]: Skilling, J. (2006). Nested sampling for general Bayesian computation. *Bayesian Analysis, 1*(4), 833–859.
[^neal-ais]: Neal, R. M. (2001). Annealed importance sampling. *Statistics and Computing, 11*(2), 125–139.
[^dps]: Chung, H., Kim, J., McCann, M. T., Klasky, M. L., & Ye, J. C. (2023). Diffusion posterior sampling for general noisy inverse problems. *International Conference on Learning Representations*. The underlying score-based framework is Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-based generative modeling through stochastic differential equations. *ICLR*.
[^bda]: Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian Data Analysis*, 3rd ed. CRC Press. (Chapter 7 covers posterior predictive checking.)
[^vi]: Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). Variational inference: a review for statisticians. *Journal of the American Statistical Association, 112*(518), 859–877.
[^mackay]: MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. (Chapter 28 on Bayes factors and Occam's razor.)
[^foster]: Foster, A., Jankowiak, M., Bingham, E., Horsfall, P., Teh, Y. W., Rainforth, T., & Goodman, N. (2019). Variational Bayesian optimal experimental design. *Advances in Neural Information Processing Systems, 32*. See also Rainforth, T., Foster, A., Ivanova, D. R., & Bickford Smith, F. (2024). Modern Bayesian experimental design. *Statistical Science, 39*(1), 100–114.
