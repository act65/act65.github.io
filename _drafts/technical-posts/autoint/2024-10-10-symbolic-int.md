---
title: Introduction to Symbolic integration
subtitle: "A review of symbolic integration"
layout: post
categories:
    - "tutorial"
scholar:
    bibliography: "auto-int.bib"
---

## Introduction



<!-- the problem -->
## We want to solve integrals!

In physics, machine learning, ...

Examples!!


## What makes integration hard?

> The main problem in the classical approach of symbolic integration is that, if a function is represented in closed form, then, in general, its antiderivative has not a similar representation. In other words, the class of functions that can be represented in closed form is not closed under antiderivation. 

## Non elementary integrals

https://en.wikipedia.org/wiki/Nonelementary_integral

Why cant some integrals be represented in closed form?

If the function contains a singularity, then the integral will also contain a singularity.


### DEMONSTRATE



### Applications

Why do we care about automatic integration?
What applications might it help us solve?

### Expectations
Want to be able to eval;

$$
\int p(x)f_{\theta}(x) dx \\
\int p_{\theta}(x)f(x) dx \\
\int p_{\theta}(x)f_{\psi}(x) dx \\
$$

Traditional solution

$$
\int p(x)f_{\theta}(x) dx = \sum_{x \in D} p(x)f_{\theta}(x) \\
$$

### Dynamical systems