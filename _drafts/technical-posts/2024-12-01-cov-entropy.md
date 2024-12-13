---
title: A change of variables formula for entropy
subtitle: The propagation of uncertainty
layout: post
permalink: cov-entropy
categories:
    - "technical"
---

One way to quantify the uncertainty in a random variable is through its entropy.
A random variable with more possible outcomes has higher entropy.
For example, a dice with 6 sides (a cube) has higher entropy than a dice with 4 sides (a tetrahedron).

Ideally we would like a formula for the entropy of $Y$ in terms of the entropy of $X$ and the properties of $f$.
<!-- why
- a change of variable formula can be chained together to give the entropy of complex functions without needing to compute any integrals.
- computing integrals is expensive
 -->

Given a function $f: \mathbb R^n \to \mathbb R^m$, let's compute the entropy of the output, $H(f(x))$.

We assume;

- n = m
- $f$ is invertible
- $f$ is differentiable
- The Jacobian determinant is non-zero


The entropy of a random variable $x$ is defined as

$$
H(x) = - \int p(x) \log p(x) dx
$$

The change of variables formula for probability distributions is

$$
p(y) = p(x) |\det J_{f^{-1}}| = \frac{p(x)}{|\det J_f|}
$$

Therefore, the entropy of $y = f(x)$ is

$$
\begin{aligned}
H(y) &= - \int p(y) \log p(y) dy \\
dy &= |\det J_f| dx \\
&= - \int \frac{p(x)}{|\det J_f|} \log \left(\frac{p(x)}{|\det J_f|}\right) |\det J_f| dx \\
&= - \int p(x) \log \left(\frac{p(x)}{|\det J_f|}\right) dx \\
&= - \int p(x) \left(\log p(x) - \log |\det J_f|\right) dx \\
&= - \int p(x) \log p(x) dx + \int p(x) \log |\det J_f| dx \\
&= H(x) + \mathbb{E}[\log |\det J_f|]
\end{aligned}
$$

If $f$ is linear, then

$$
\mathbb{E}[\log |\det J_f|] = \log |\det J_f| \\
H(y) = H(x) + \log |\det J_f|
$$

If $f(x) = e^x$, then

$$
\begin{aligned}
\mathbb{E}[\log |\det J_f|] &= \mathbb{E}[\log e^x] \\
&= \mathbb{E}[x] \\
&= \mu_x \\
H(y) &= H(x) + \mu_x
\end{aligned}
$$

If $f(x) = x^a$, then

$$
\begin{aligned}
\mathbb{E}[\log |\det J_f|] &= \mathbb{E}[\log a x^{a-1}] \\
&= \mathbb{E}[\log a + (a-1) \log x] \\
&= \log a + (a-1) \mathbb{E}[\log x] \\
\end{aligned}
$$

Cannot simplfy further without knowing the distribution of $x$. 
Or evaluating the integral in the expectation (which we don't want to do).

If $f(x) = \log x$, then

$$
\begin{aligned}
\mathbb{E}[\log |\det J_f|] &= \mathbb{E}[\log \frac{1}{x}] \\
&= \mathbb{E}[-\log x] \\
&= -\mathbb{E}[\log x] \\
\end{aligned}
$$

What???

<!-- For the $x^a$ case: You could add some special cases:

For $x > 0$ and $a = 2$, if $x$ follows a log-normal distribution, $\mathbb{E}[\log x]$ has a closed form
For positive random variables, Jensen's inequality could provide bounds -->

<!-- If we know x follows a specific distribution (like lognormal), we could evaluate E[log |x|] explicitly. But in the general case, this is as far as we can simplify.
Would you like to explore what happens with specific input distributions, or are you interested in other functional forms? -->


<!-- It might be worth considering what happens when we compose transformations. The chain rule for Jacobians might give interesting results. -->

What if f = relu?

$$
\begin{aligned}
f(x) &= \begin{cases}
    x, \text{if } x > 0 \\
    0, \text{otherwise}
\end{cases} \\
J_f &= \begin{cases}
    1, \text{if } x > 0 \\
    0, \text{otherwise}
\end{cases} \\
\end{aligned}
$$

$$
\begin{aligned}
\mathbb{E}[\log |\det J_f|] &= \mathbb{E}[\log J_f] \\
&= \mathbb{E}[\log 1] \\
&= ???
\end{aligned}
$$

If we knew the cdf of x, then could calculate p(x>0) = 1 - cdf(0).
E[log 1] = p(x>0) log 1 