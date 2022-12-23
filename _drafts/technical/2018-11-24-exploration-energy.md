---
layout: post
title: The complexity of exploration
---

This setting is inspired by the problems faced in science, especially economics and medicine. There are some experiments that are not feasible, or legal, or would take extraordinary amounts of organisation and energy. For example, a randomised controlled trial of the unconditional benefit would require: many countries to spend $$$ on an unconditional benefit, which they may be unwilling to do (and obviously there is no way of running is as a blinded experiment).

At some point we will want to automate the application of statistics to economics and healthcare. Unsupervised (machine) learning is to pattern recognitio, as supervised (machine) learning is to predictive intelligence, as reinforcement (machine) learning is to actionable intelligence. We will want this automated statistics to be able to find algorithms that explore and do experiments! But... This has two problems. Safety, which is considered here. Want to build AI with a bias to simple cheap experiments.

## Examples

> Want to do experiments on particle physics. The explorer could; organise and convince tens of countries to support the construct a hadron collider the size of a country. Or we could spend those resources on searching for a cheaper experiment, like the wakefield accelerator.

Ok, this has an interesting property. Multiple ways to learn the same thing. We want to pick the cheapest...

> What is the effect of the quality of local libraries on the national economy? To answer this we could: do an experiment on ~20 countries, varying the quality of the local libraries, controlling for potential confounders like, national policy, culture, ... and measure the effect over 50 years. Or, we could approximate that experiment with ...? A set of local experiments, stimulus-response, measure and correct for confounders and correlates, ...?



***

__Hypothesis:__ Simple, local, exploration strategies will naturally emerge from optimising for novelty (and/or compression?). They are easier to learn and yield a higher rate of return.

The low hanging fruit!

## Sample complexity of option's effects

Some states are harder to reach (and stay there). This means they are harder to explore.

Have a set of options. Each option has an associated energy cost (could simply be the length...).


- Write $\tau(\tau(s_t, a_i), a_j) \equiv \tau(s_t, [a_i, a_j])$.
  - When does $\tau(s_t, [a_1, a_2, a_3]) \neq \tau(s_t, [a_1, a_3, a_2])$?
  - How hard is this to learn as $a_n$ increases?
- Write $\Delta \tau(s_t, a_i) \equiv \tau(s_t, a_i)- s_t$.
  - When does $\Delta \tau(s_t, a_n) \neq \tau(s_t, [a_i, \dots, a_{i+n}]) - \tau(s_t, [a_{j+n}, \dots, a_{n-1}])$?
  - How hard is this to learn as $a_n$ increases?

Where $a_i\in O$ are options (not just actions).

When is it efficient/possible to learn a complex/global function from simple/local actions/experiments?

Can have arbitrary (normalised?) functions that assign costs to options. What we are really interested in is not the absolute values of the costs, but how they scale with different types of problem.

Reasons a state can be hard to reach. (really we care about reaching a pair of states, so we can compare the difference. and do science)

- trajectory is sensitive to noise (and few possible trajectories)
- trajectories are long (want thing to capture having to gather resources for a task. eg we can easily buy a new iphone, just walk down to the store. but that doesnt include the required effort to earn the captial - financial capital, social capital, intellectual capital, ...)
- other agents are attempting to move the state elsewhere. (thus you need to compete/convince/kill/?)
- ?

## Limited capacity gradient estimation

The state space is large.
Pertubation
$$
\begin{align}
y &= f(x) \\
\frac{df}{dx} &= f(P(x)) \\
P(x) &= x + \Delta x \tag{pertubation} \\
??? &= f(C(x))) \tag{control}\\
\end{align}
$$

Could simply measure the number of dimensions perturbed or controlled. Energy, $E=\mid P \mid + \mid C \mid$.

Related to [Blackbox bprop and jacobian sensing](https://papers.nips.cc/paper/7230-on-blackbox-backpropagation-and-jacobian-sensing.pdf).


Have some finite/limited capacity and/or attention to;
- apply preturbations and controls. Can weakly control many things, or strongly control few dimensions.
- measure outcomes. Can accurately measure few outputs, or inaccurately measure many.

(I am imagining a juggler trying to juggle 100 balls, or one of those music men buskers wih ~10 instruments).

This gives a kind of local-global tradeoff. (relationship to fourier transform and uncertainty principle)

The limits of limited capacity.

- Measure and correct for confounders. We cannot measure everything during a single experiment... We are not sure if there is another hidden variable that is confounding our experiment.
- Control is only necessary when correlated? For other independent variables we would only control for efficiency? Could still estimate, but would want to reduce variance.

***

Rather than global perturbations being a linear fn of the number of pertubations made, there is some higher order function that calculates the cost of many pertubations.

***

- What about time-memory complexity? (to explore efficiently there is a fundamental tradeoff between time/samples and memory. Need to remember where I have been if I want to avoid repeating it...)
