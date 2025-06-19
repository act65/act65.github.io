---
layout: post
title: Understanding emergent complexity
---

> How does complexity emerge out of simplicity? How do simple structures generate complexity?

Equivalently, you could ask;
- Given a small code, our genome (on the order of mB), how is such complexity generated?
- Given a simple loss function how it can bootstrap itself to generate specialised experts? ... through meta learning?
- Why does the humble natural selection algorithm generate the splendid diversity we see around us?
- ?

<!--
Want some pictures here? Maybe some automata/game of life?
Interactive would be even better!? :)
-->

> At a high level, this is the goal of scientific endeavour. To understand the complex phenomena we experience using simpler concepts.

What is the goal of science? Generate accurate explanations for phenomena we observe. It isnt enough to just fit a model to the observed data, because we almost always do not have access to all of the information and thus we are solvig an underconstrained problem. There are many models that fit the data.


Imagine you want to understand {insert reduction lesson}. An interactive example would be nice!?

This method works well. But, what about when the simple bits are deeply entangled aka emergent behaviour, generative effects, ...?



So the question becomes; which model is the best one?

- Assumption 1: Reducability
If components of a model can independently explain some of the observed phenomena then the composition of those components makes a likely model.
- Assumption 2: Generality (it this different to simplicity? the assumption of an integrated representation of everything)
- Assumption 3: Simplicity (is this equivalent to reducability?)
- Assumption 4: Induction !?
- Assumptin 5: Smoothness/locality. A series of understandable, basic/atomic, steps taken.
- Assumption 6: Necessity implies causality (is that an assumption?!)

[Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016)

TODO Explain the duality between machine learning and science.

***

Show that: optimising a reward, in different environments (aka under different constraints/assumptions) various strategies (memory, safe trade, ...) emerge naturally.

Other ways of stating the same thing;
- Show which environments provide advantages to different strategies when optimising for the same goal.
- Show what is necessary/sufficient for a certain phenomena to emerge


### What does it mean to understand?

Heirarchy of explanation;

1. Predictive (association. could just fit a fn)
2. Generative (?)
3. Disentanglement and reductionism. (this `fn` is sufficient to generate Z from X and Z)
4. Counterfactuals (via ablation) -- can give us necessity (given other assumptions). (X is necessary for Z)
5. Advantages given by bounds on the complexities of resources. (why is X necessary for Z?)
6. A single simple fn being optimised. (aka comression, or value, or ?!?)

Process;

- generate various emergent behaviours.
- study them and find patterns?
- ...?

Questions to answer;

- What is the problem being solved by X?
- And why is X necessary? (comprared to potential alternatives it ...?)
- What can inaccurate models tell us? The models half way along the trajectory?

***

Not only does a model have to be as simple as possible, but it also needs a simple process by which the model can arise. (is that the same as just having a model that is as simple as possible?)

Many models might fit the data. Only consider "constructible" (aka learnable?) models. (aka a bunch to steps from A to B)


Just give the process some names to make things clear.
$$
Data \mathop{\rightarrow}_{Compress} Model \mathop{\rightarrow}_{Formalise} Axioms \\
Data \mathop{\leftarrow}_{Generate} Model \mathop{\leftarrow}_{Construct} Axioms \\
$$

The axioms, given a ???, can construct the model.
The model, given an init, can generate the data.

Ahh, but when we are searching for the right axioms, we still use the data to constrain the space of models.

How can we formalise?
Imagine we have a model of particle physics. How can we find the minimal set of assumptions that (approximately) generate our model?

Nah, formalisation and compression are really the same thing? Take an explicit construction of something (a dataset or a model) and compress it.


# In practice

Imagine we have a model of the brain. Questions we might like to ask would be;

- how much does assumption A effect the accuracy of our model?
- ?

## Computational complexity

> What resources do we need to spend to answer these questions?

The computational complexity of testing the various assumptions!?


## Problems with this approach;

- a trajectory/generative reward only proves sufficiency (or conditional necessity).
- ?

What is necessary to build an explanation?
Generative. Each part is necessary.

This is just the same as all science? Build a model!?! But the how is the important part.
- Reduce to simple testable cases.
- Build up complexity
- Figure out which assumptions are necessary and cut others. Compress!!

# Examples

I see some similarities in the methodology (I would want to use) to understand cooperation, ?, brains.

## Explaining the evolution of XXX

For each arrow we want;
- proof that the step provides an advantage
- the step to be possible via a 'smooth' trajectory
- ?

### The evolution of collaboration
> Reputation -> Money -> Markets.
<!-- Repuation (as a signal for estimating trust) doesn't scale well ($n^{\mathcal O(1)}$) with larger numbers of traders. Money ... scales -->

### The evolution of language
> Planning -> Merge -> Language.

### The evolution of life

> Membrane potentials -> ? -> ?

<!-- Need to re-read the vital question. -->

### The evolution of the brain

> Learning -> ? -> ?

The main question I would want to answer is; what advantage does X brain structure provide? If we are going to include bounary/goal/time cells, or some alternative neural topology between CA1 and grid cells, what advantage do they provide our agent/organism? Can it learn faster? Can it generalise better? ... etc Does the change help make more babies?

So, what I really want to understand is what needs to be done computationally to solve a problem, aka its complexity, and what structures in the brain are necessary/sufficient.

### The construction of the brain

> ? -> ? -> ?

Given a value fn (maybe many?), construct a new loss fn tailored to the environment.

[Prefrontal cortex as a meta-reinforcement learning system](https://www.biorxiv.org/content/early/2018/04/06/295964). A simple(ish) reward, that generates many complex specialists that fit to the environment.

## What about other theories?

What about if we viewed the evolution of theories of gravity in a similar way?!? Always optimising accuracy.

### Relativity

> ? -> Classical mechanics -> Relativity -> ?

First the easily solutions are found and constrained by data.
- Knowledge of `the speed of light` is necessary for learning relativity.
- ?

#### Other possible tools?

Approaches to study this problem.
<!-- (want feedback from david here!!) -->

- Use bprop to estimate the effect of parameters/assumptions!?
- How easily does the phenomena emerge?
- ablation studies to prove necessity?!?
- Bifurications?!?
- Category theory - generative composition
- ?
- tools from many-body particle physics? phases and crystals?
- Relation to combinatorics?
- ?


# Other thoughts

* How you can combine low symmetry objects to make more symmetry. (thus generating info!?)
- the duality of dynamical systems and optimisation (what is a dynamical system optimsing, what is the optimisers dynamics?)
- How does a simple loss lead to complexity? Recursively applying the same target, boostrapping off itself, ...?
- What about the dual problem? What can reduction and disentanglement of complex system teach us about generating complex systems?
