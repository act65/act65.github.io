---
layout: post
title: Causal calculus
subtitle: A connection between causal inference and gradients?
categories:
    - tutorial
---

_updated (22/07/25). Added refs, made assumption of linear model clearer_

# Causal Calculus: A Gradient-Based Interpretation

I recently read Judea Pearl's *The Book of Why*[^1], and it clarified many intuitions about causal inference. It also let me to wonder: is there a connection between the *do*-calculus of causal inference and the familiar gradients of machine learning?

## The Goal: Estimating Causal Effects

The central goal of causal inference is to distinguish correlation from causation. We want to estimate the true effect of an intervention, which Pearl denotes with the `do()` operator. For example, what is the effect on cancer rates, `P(Y)`, if we *force* a population to smoke, `do(X)`?

This is different from the observational probability, `P(Y|X)`, which simply tells us the cancer rate among people who already smoke. If a hidden "smoking gene" (`U`) both encourages smoking and causes cancer, the observed correlation will be misleading.

This is the problem that causal adjustment formulas solve. Let's consider the two most common methods.

![pic]({{site.baseurl}}\images/smoking.png)
(_$X$ is Smoking, $Y$ is Cancer, $Z$ is Tar, and $U$ is a confounding Smoking Gene._)

#### The Back-Door Adjustment

If we can observe and control for all confounding variables—that is, all variables that provide a "back-door" path from `X` to `Y`—we can isolate the causal effect. In our diagram, the gene `U` is a confounder. If we can measure it, we can control for it by averaging its effect across all its values.

The back-door adjustment formula is:

$$
P(Y \mid do(X)) = \sum_u P(Y \mid X, U=u) P(U=u) = \mathbb E_{u\sim U}[P(Y \mid X, U=u)]
$$

This formula allows us to calculate the causal effect of `X` on `Y` by using only observational data, provided we have measured the confounder `U`.

#### The Front-Door Adjustment

What if the confounder `U` is unobservable? Surprisingly, we can still estimate the causal effect if we can find a mediating variable `Z` that is *only* influenced by `X`. In our example, `Tar` is a perfect mediator. The effect of `X` on `Y` is fully transmitted through `Z`.

The front-door adjustment is a two-step process:
1.  Estimate the causal effect of `X` on `Z`. Since there are no back-doors into `X` from `Z`, this is just their observed correlation.
2.  Estimate the causal effect of `Z` on `Y`. To do this, we must block the back-door path from `Z` back to `Y` (i.e., `Z ← X ← U → Y`) by controlling for `X`.

This gives us the front-door formula:

$$
P(Y \mid do(X)) = \sum_z P(Z=z \mid do(X)) \cdot P(Y \mid do(Z=z))
$$
Which expands to:
$$
P(Y \mid do(X)) = \sum_z P(Z=z \mid X) \sum_x P(Y \mid X=x, Z=z) P(X=x)
$$

## A New Interpretation: Expected Gradients

Here's the interesting part. Let's reconsider these formulas through the lens of gradients.

#### From Correlation to Gradients

While a conditional probability `P(Y|X)` is a full distribution, if we assume a simple linear relationship, `Y = aX + b`, the coefficient `a` represents the strength of the connection. This coefficient is what we calculate with a linear regression, and it can be expressed as:

$$
a = \frac{\mathbb E[(X -\mu_X)(Y-\mu_Y)]}{\mathbb E[(X -\mu_X)^2]} = \mathbb E\bigg[\frac{Y-\mu_Y}{X -\mu_X}\bigg]
$$

This expression is essentially the expected "rise over run" between the variables. For any function `y = f(x)`, this is the definition of the gradient, `∂y/∂x`.

So, under the assumption of local linear relationships, we can reinterpret the causal effect as an **expected gradient**.

Let's apply this intuition to the adjustment formulas.

#### The Back-Door Adjustment as an Expected Gradient

The back-door formula `E_u[P(Y|X, U=u)]` tells us to calculate the relationship between `Y` and `X` at each value `u` of the confounder and then average. In our new interpretation, this is simply the **confounder-averaged expected gradient**:

$$
\frac{\partial y}{\partial x_{\text{causal}}} = \mathbb E_u \bigg[\frac{\partial y}{\partial x}(u)\bigg]
$$

#### The Front-Door Adjustment as the Chain Rule

The front-door adjustment involves combining the effect of `X` on `Z` and the effect of `Z` on `Y`. If we represent these effects as gradients, the formula becomes a product of expected gradients, summed over the mediator `Z`:
$$
\frac{\partial y}{\partial x_{\text{causal}}} = \mathbb E_z \bigg[\frac{\partial y}{\partial z}(z) \cdot \frac{\partial z}{\partial x}(x)\bigg]
$$
This is exactly the **chain rule** from calculus, averaged over all possible values of the mediator `z`. The intuition holds beautifully.

## Towards a "Total Causal Effect" Metric

This gradient-based view allows us to propose a measure of causal strength for continuous, non-linear functions.

**Desiderata:**
1.  If small changes in `x` consistently cause large changes in `y`, the measure should be high.
2.  The direction of change shouldn't matter, only the magnitude.
3.  The measure should be normalized, perhaps between 0 and 1.

A simple starting point is the expected magnitude of the gradient:
$$
c_{x\to y} = \mathbb E \bigg[\parallel \frac{\partial y}{\partial x} \parallel\bigg]
$$
To normalize this, we can express it as a proportion of the total influence on `y`. If `y` is a function of multiple variables `x_1, x_2, ..., x_n`, we could define the causal contribution of `x_i` as:

$$
c_{x_i \to y} = \frac{\mathbb E \big[\parallel \frac{\partial y}{\partial x_i} \parallel\big]}{\sum_{j=1}^n \mathbb E \big[\parallel \frac{\partial y}{\partial x_j} \parallel\big]}
$$

This gives us a bounded measure of "sufficient cause" that accounts for the sensitivity of `y` to changes in `x_i` relative to its other causes.

## Connection to Modern ML Research

It turns out these ideas are not entirely new, which is exciting! A growing body of research in machine learning uses gradients for causal discovery. Frameworks now exist that treat learning a causal graph as a continuous optimization problem, where gradients are used to find the most likely causal structure from data. [^1] [^2]

One of the most fascinating applications is in active learning for causal discovery. Methods like Gradient-based Intervention Targeting (GIT) use the gradients of a causal model to decide which real-world experiment would be most informative for uncovering the true causal graph, thereby minimizing costly data collection. [^3] [^4] [^5] This "Trust Your ∇" approach shows that the connection between gradients and causality is not just an intuition, but a practical tool for scientific discovery.

This is a work in progress, but the initial connection seems powerful. Re-framing causal calculus in the language of gradients provides a new way to think about these problems and connects them directly to the tools we use every day in machine learning.

---
### References
[^1]: Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. Basic Books.
[^2]: Zheng, X., et al. (2020). "Learning linear non-Gaussian acyclic models in the presence of arbitrary unobserved confounding". *arXiv preprint arXiv:2007.01754*.
[^3]: Brouillard, P., et al. (2020). "Differentiable causal discovery from interventional data". *arXiv preprint arXiv:2007.01754*.
[^4]: Lachapelle, S., et al. (2020). "Gradient-Based Neural DAG Learning". *International Conference on Learning Representations*.
[^5]: Khemakhem, I., et al. (2022). "Trust Your ∇: Gradient-based Intervention Targeting for Causal Discovery". *arXiv preprint arXiv:2211.13715*.