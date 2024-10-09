---
title: "Typicality"
subtitle: "In high dimensions, typical is unintuitive"
layout: post
permalink: /pits/typical
categories: 
  - "tutorial"
scholar:
  bibliography: "pits.bib"
---

> What is likely is not (necessarily) typical.

Let's start with a motivating example:
We have a biased coin $p(\text{Heads}) = 0.8$ which we flip $n=100$ times. The most likely outcome is 100 heads, with probability $0.8^{100}=2.037036 \times 10^{-10}$, a small number. So the vast majority of the time, we will observe something else.
Most of these other outcomes will be in the range of 70-90 heads. We call these outcomes 'typical'.

Using the Binomial distribution, we can calculate and plot the probability of k heads as;

$$
p(k) = \left( 100 \; \text{choose} \; k \right)0.8^k0.2^{100-k}
$$

<img src="{{ site.baseurl }}/assets/pits/binomial-100.png">
<figcaption>The probability of k heads.</figcaption>

The potentially counter intuitive part being that each individual outcome (with with ~70-90 heads) is less likely than 100 heads, yet, they are the ones we observe.

The exaplanation is that there is only 1 way to get 100 heads, but MANY ways to get (say) 80 heads ($100 \; \text{choose} \; 80 = 5.3598337 \times 10^{20}$).

***

__Definition__ (for discrete random variables)

The typical set $\mathcal T (p(x))_{\epsilon}$ is the set of sequences $(x_1,x_2,...,x_n) \in X_n$ with the property 

$$
2^{−n(H (X)+\epsilon)} \le p(x_1,x_2,...,x_n) \le 2^{−n(H (X)-\epsilon)} \\
$$

From {% cite coverthomas2006 %} page 59.

***

So for our coin flipping example, let's pick $\epsilon = 0.1$ and calculate the typical set.

<img src="{{ site.baseurl }}/assets/pits/binomial-100-H.png">
<figcaption>Here we plot the probability of individual outcomes $p(x)$, in blue, the probability of k heads $p(\text{Heads})$, in orange, for $n=10$ coin flips. The axis for $p(x)$ in on the left, and the axis for $p(\text{Heads})$ is on the right. The grey box shows how the intersection of $p(x)$ and the lower / upper bounds on entropy constrain $p(\text{Heads})$ </figcaption>

***

A more practical example; a survey.

We have a survey with 100 binary questions.

- Do you consider yourself to be a morning or night person?
- Do you prefer cats or dogs?
- Do you prefer tea or coffee?
- Do you prefer to read or watch TV?
- Do you vote left or right?
- ... etc

We can collect the data, and we may see that;

- 60% of people consider themselves to be morning people
- 70% of people prefer dogs
- 80% of people prefer coffee
- 60% of people prefer to read
- 50% of people vote left
- etc...

From this data we can construct an archetype of a person who took the survey. This person would be a morning person, prefer dogs, prefer coffee, prefer to read, and vote left. This person is the most likely person to have taken the survey. But they are unlikely to exist!

<!-- designing things for this archetype would be a bad idea -->

***

<!-- more on entropy? -->

If we rearange the definition of discrete typical sets, we can find a close connection to the definiiton of entropy.

$$
\begin{align*}
H (X)-\epsilon \le \frac{1}{n} \log p(x_1,x_2,...,x_n) &\le H (X)+\epsilon \\
\log p(x_1,x_2,...,x_n) &= \log \prod_{i=1}^n p(x_i) \\
&= \sum_{i=1}^n \log p(x_i) \\
H(X) &= - \sum_{x \in X} p(x) \log p(x)
\end{align*}
$$


***

__Definition__ (for continuous random variables)

The typical set $\mathcal T (p(x))_{\epsilon}$ is the set of sequences $(x_1,x_2,...,x_n) \in X_n$ with the property

$$
A_{\epsilon}^{(N)} = \{x \in S^N: \mid - \frac{1}{N} \log p(x) - H(X) \mid \le \epsilon\} \\
p(x) = \prod_{i=1}^{N} p(x_i)
$$


***

Let's work through a continuous example. A Gaussian distribution in d-dimensions.

$$
p(x) = \frac{1}{(2\pi)^{d/2}} \exp \left( - \frac{1}{2} x^T x \right)
$$


<img src="{{ site.baseurl }}/assets/pits/gaussian-typical.png">

This leads us to a well known result, the __Gaussian Annulus Theorem__

For a d-dimensional spherical Gaussian with unit variance in each direction, for any $\beta \le \sqrt{d}$, all but at most $3e^{−c\beta^2}$ of the probability mass lies within the annulus $\sqrt{d} - \beta \le |x| \le \sqrt{d} + \beta$, where c is a fixed positive
constant.

***

Much like our discrete example (but replace probability mass with probability density and binomial counts with volume), the most likely outcome has small probability density. And as we move outward, the volume increases exponentially. Thus even though the probability density is small, the volume is large, and we are likely to observe points in this region.

## Bibliography

{% bibliography --cited %}