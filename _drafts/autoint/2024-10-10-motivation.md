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



Problems that people cared about

- surges in electrical wires
- predicting tides
- missile guidance

https://americanhistory.si.edu/collections/object-groups/mechanical-integrators/harmonic-analyzers-and-synthesizers

<!-- and how did they solve them? mechanical integration? -->

## Applications

### Tides

Laplace's tidal equations
https://www.whoi.edu/cms/files/lecture03_21374.pdf
https://www.google.com.au/books/edition/Tides/78bE5U7TVuIC?hl=en&bshm=rime/1

### Planetary motion

Antikythera
http://dlib.nyu.edu/awdl/isaw/isaw-papers/4/

### Bomb / missile guidance

https://www.amazon.com/Bomber-Mafia-Temptation-Longest-Second/dp/0316296619


Green's theorem

Ball-and-disk integrator

- the water integrator
- the mechanical integrator https://www.youtube.com/watch?v=s-y_lnzWQjk
- ford's integrator
- planimeter
- harmonic analyser
- longimeter https://en.wikipedia.org/wiki/Steinhaus_longimeter

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


<!-- entropy -->