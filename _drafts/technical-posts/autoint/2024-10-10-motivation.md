---
layout: post
title: "Vision for automatic integration"
subtitle: "What could it do for us?"
permalink: /autoint/motivation/
categories:
    - "proposal"
scholar:
    bibliography: "auto-int.bib"
---

# Motivation

<!-- uses / motivation -->

Firstly, what kind of problems could automatic integration solve?

<!-- bayesian -->
Two distributions.

$$
\begin{align}
p(y| x) &= \frac{p(x| y) p(y)}{p(x)} \\
p(x) &= \int p(x| y) p(y) dy
\end{align}
$$

For example, we have a prior distribution over likely diseases $p(y)$ and a likelihood function $p(x| y)$ which tells us how likely the observed MRI $x$ is given the disease $y$.
Where $p(y)$ is derived from the population statistics. And $p(x | y)$ is a generative model learning from data.
<!-- y= discrete variable. 1000 different potential diseases -->
<!-- y= continuous variable. how long are they likely to survive / how long until surgery is needed. measured in weeks. e.g 10.24 weeks. -->





$$
\int p(x; \theta) f(x; \phi) dx
$$

where $p(x; \theta)$ is a probability distribution and $f(x; \phi)$ is a function.
{% cite JMLR:v21:19-346 %}

or the Wave equation

$$
\frac{\partial^2 u}{\partial x^2} = c^2 \Delta u
$$

where $u$ is a function and $\Delta$ is the Laplacian operator.
And in general, any PDE.


# Vision

<!-- uses / vision -->

Slot into existing autograd frameworks.