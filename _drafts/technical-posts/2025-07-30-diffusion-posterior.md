---
title: Steering the Noise
subtitle: How Diffusion Models Unlock Bayesian Inference
layout: post
categories:
    - tutorial
---

Diffusion models have taken the world of generative AI by storm, creating stunningly realistic images, audio, and even video from simple text prompts. At their core, they are masters of synthesis, learning to sculpt pure noise into samples from a complex data distribution.

But what if we could use this power for more than just random generation? What if we could steer this sculpting process with data, guiding the model to generate samples that not only look plausible but also explain specific observations we've made?

This is the gateway to a new paradigm for Bayesian inference. By reframing a diffusion model as a highly expressive **prior** and guiding it with a **likelihood**, we can sample from complex, high-dimensional **posterior** distributions. This post explores how this works, right down to a subtle but elegant trick that makes the whole process computationally feasible.

### Step 1: A Diffusion Model is an Expressive Prior

First, let's reframe what a standard diffusion model does in the language of Bayesian statistics. A diffusion model is trained on a large dataset (e.g., millions of images) to learn the underlying structure of that data. When you ask it to generate a new image, it's effectively drawing a sample from the distribution it has learned.

In Bayesian terms, this learned distribution is our **prior**, `p(θ)`. It represents our belief about what a plausible parameter `θ` (in this case, an image) looks like before we've seen any specific data. The magic of diffusion models is that this prior can be incredibly complex, multi-modal, and high-dimensional—far beyond what traditional conjugate priors like Gaussians can represent.

The model's key component is a neural network, often called a **score model**, `s_θ(x_t, t)`. Its job is to predict the direction to nudge a noisy sample `x_t` at time `t` to make it slightly less noisy. Formally, this score is the gradient of the log-probability of the noisy data:

`s_θ(x_t, t) = ∇_xt log p(x_t)`

Think of the score as a compass, always pointing the way from noise back to the manifold of plausible data.

### Step 2: From Prior to Posterior with Bayes' Rule

Now, let's introduce data. Suppose we have some observations, and we have a **likelihood function**, `p(data | θ)`, that tells us how probable those observations are given a specific parameter `θ`. Our goal is no longer to sample from the prior `p(θ)`, but from the **posterior** `p(θ | data)`.

Bayes' rule is our bridge:

`p(θ | data) ∝ p(data | θ) * p(θ)`

This formula is elegant but often intractable to work with directly. However, things become much simpler if we move to the space of log-probabilities and their gradients (the scores). Taking the log and then the gradient with respect to `θ` gives us a beautiful result:

`∇_θ log p(θ | data) = ∇_θ log p(data | θ) + ∇_θ log p(θ)`

Let's translate this equation:

> **Score of the Posterior = Score of the Likelihood + Score of the Prior**

This is a profound insight. It suggests that to guide our diffusion process towards the posterior, we just need to add the gradient of our log-likelihood to the score our neural network already provides. Our new, guided compass should point in a direction that is a compromise between what the prior thinks is plausible and what the likelihood says fits the data.

The proposed sampling process looks like this: at each denoising step, we calculate the new drift direction by simply summing the two scores.

```python
# The conceptual update rule inside the sampler
prior_score = score_nn(x_t, t)
likelihood_score = grad(log_likelihood_fn)(x_t) # <-- The problem is here!

posterior_score = prior_score + likelihood_score
x_t = update_step(x_t, posterior_score)
```

This seems almost too easy. And, as you might suspect, there's a subtle catch.

### The Subtle Problem: A Mismatch in Time

The equation for the posterior score is perfectly correct, but it applies to the final, clean sample `θ` (which we call `x_0` in diffusion terminology).

However, our sampling process doesn't operate on `x_0` until the very end. For the vast majority of the time, it's working with a **noisy intermediate sample `x_t`**.

This reveals a critical mismatch:
*   Our **prior score** is a function of the noisy sample: `s_θ(x_t, t) = ∇_xt log p(x_t)`. This is what our network is trained to do.
*   Our **likelihood score** is a function of the clean sample: `∇_x0 log p(data | x_0)`. We have no analytical way to calculate `∇_xt log p(data | x_t)`, the score of the likelihood given a *noisy* input. This would require solving a difficult integral over all possible clean `x_0`'s that could have produced the noisy `x_t`.

So, the simple addition in our pseudocode is comparing apples and oranges. We can't directly add a gradient with respect to `x_0` to a gradient with respect to `x_t`.

### The Elegant Solution: Guiding with a Lookahead

This is where a powerful and practical approximation comes into play, making the entire guidance procedure feasible. Instead of trying to compute the intractable `∇_xt log p(data | x_t)`, we approximate it using the gradient we *can* compute.

The logic is as follows:

1.  **Predict the Final Sample:** At any step `t` with noisy sample `x_t`, we can use the diffusion model's mathematics (specifically, a relationship known as Tweedie's formula) to make a one-step prediction of what the final, clean sample `x_0` will look like. Let's call this `x0_pred(x_t)`.

2.  **Calculate the Gradient There:** We then take our known log-likelihood function and calculate its gradient at this *predicted* clean sample: `∇_x0 log p(data | x_0)` evaluated at `x_0 = x0_pred(x_t)`.

3.  **Apply the Gradient Here:** Finally, we use this gradient as a direct proxy for the one we need. We "nudge" our current noisy sample `x_t` using the guidance direction we calculated from its predicted future self.

> **The Trick:** We approximate `∇_xt log p(data | x_t)` with `∇_x0 log p(data | x_0) |_{x_0 = x0_pred(x_t)}`.

This might seem "weird," as if we're cheating by looking ahead. But it works remarkably well.

*   **When `t` is small (close to 0):** The sample `x_t` is already almost clean. The prediction `x0_pred(x_t)` is very accurate, so the approximation is excellent.
*   **When `t` is large (close to 1):** The sample `x_t` is mostly noise. The prediction `x0_pred(x_t)` is very blurry, but it's still centered on the most likely regions of the data manifold. The likelihood gradient provides a crucial, albeit approximate, push towards the parts of that manifold that agree with our data, preventing the model from wandering off.

### Conclusion: A New Frontier for Inference

By combining a powerful score-based prior with a likelihood function, we can perform Bayesian inference in a way that was previously unimaginable. The process is a beautiful dance between two forces:

1.  The **prior score**, learned from a massive dataset, ensures the sample remains plausible and high-quality.
2.  The **likelihood score**, calculated on-the-fly, steers the sample towards a solution that explains the specific data we have observed.

The subtle trick of using a predicted `x_0` to calculate the likelihood gradient is the key that unlocks this process, allowing us to guide the diffusion sampler at every step of its journey from noise to a meaningful posterior sample. This opens the door to tackling complex inverse problems, enabling more powerful forms of reinforcement learning (like the Thompson sampling that inspired this discussion), and fusing the power of deep generative models with the rigorous principles of Bayesian statistics.