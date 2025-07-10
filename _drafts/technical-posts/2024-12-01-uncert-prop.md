---
title: The propagation of uncertainty
subtitle: 
layout: post
permalink: uncert-prop
categories:
    - "technical"
---

What do we mean by uncertainty?

- uncertainty in the data
- uncertainty in the model
- uncertainty in the parameters

<!-- aleoteric vs epistemic -->

Aleotric

$$
y = f(x, \theta) \\
p(y | x, \theta) = \frac{p(y, x, \theta)}{p(x, \theta)}
$$

***

What do we mean by probability?

For aleoteric uncertainty, the frequentist interpretation makes the most sense.
There is noise in the data, we can sample many times and count the number of times (the frequency) we get a certain value.

For epistemic uncertainty, the bayesian interpretation makes the most sense.
We must act despite missing information, so we must pick the 'best' option. 


***

In Machine Learning, there are several methods for uncertainty propagation. Here are the main approaches:

Monte Carlo (MC) Methods:


Simple MC sampling
Latin Hypercube Sampling
Importance sampling
Advantages: Simple to implement, works with any model
Disadvantages: Computationally expensive, requires many samples


Analytical Methods:


Delta Method (First-order Taylor expansion)
Error propagation formula
Advantages: Fast, exact for linear systems
Disadvantages: Only works for simple functions, assumes Gaussian distributions


Bayesian Methods:


Bayesian Neural Networks
Gaussian Processes
Variational Inference
Advantages: Provides full probability distributions
Disadvantages: Can be computationally intensive


Ensemble Methods:


Bootstrap
Dropout as uncertainty
Multiple models with different initializations
Advantages: Can capture model uncertainty
Disadvantages: Requires training multiple models


Interval Arithmetic:


Range propagation
Affine arithmetic
Advantages: Provides guaranteed bounds
Disadvantages: 
    Can be overly conservative
    Dependency problem (treating same variable as independent)
    Wrapping effect (overestimation in multiple dimensions)


Polynomial Chaos Expansion:


Represents uncertainty using orthogonal polynomials
Advantages: Efficient for certain types of problems
Disadvantages: Complex implementation