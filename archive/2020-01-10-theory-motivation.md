---
layout: post
title: Motivating theory
---

> What is theory, and why do we need it?

A case study, theory for ML/DL/RL.

How can theory help clean the mess that is arxiv?
How does this lead to studying MDPs and Bandits?
What do we want? To organise, to explain, to compress, to ???.

### Benchmarks

DL doesnt have a good record.
https://arxiv.org/abs/1907.06902v2
https://arxiv.org/abs/1711.10337
Benchmarking
- [Benchmarking Bonus-Based Exploration Methods on the Arcade Learning Environment](https://arxiv.org/abs/1908.02388]
[Benchmarking Model-Based Reinforcement Learning](https://arxiv.org/abs/1907.02057)
[Benchmarking Reinforcement Learning Algorithms on Real-World Robots](https://arxiv.org/abs/1809.07731)
[Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778)

For instance,  [Uber](https://github.com/uber-research/atari-model-zoo), [OpenAI](https://github.com/openai/baselines), [Google](https://github.com/google/dopamine), [DeepMind](https://github.com/deepmind/bsuite).

Why? Instability, non-convex, hyper parameter searches, subtle design decisions, not analysing the variance, computational cost, ...
Each of these benchmarking tools is an attempt to remove some of the variations in implementation.

Also. Seed tuning...
- [Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](https://arxiv.org/pdf/1910.10897.pdf)

Hyper parameter searches confound the issue.
Need a test set. To verify.
But in DRL we train and test on the same problem. Does that really make sense?


The point is that doing science on DRL;
- requires lots of compute,
- is currently flawed
- ?

Just take a look at some recent papers...

### How does theory help?

In RL there are a few well known theoretical results to build on!
Examples. Convergence of VI. TD. Optimality of ...

### Evaluating our models

What we want to know. Our models ability to generalise beyond our data.

https://arxiv.org/pdf/1905.12580.pdf
https://arxiv.org/pdf/1502.04585.pdf
https://arxiv.org/pdf/1905.10360.pdf

### Generalisation in RL

This is what we are trying to measure.

But. Does it even make sense?
How do we test this? [CoinRun](https://arxiv.org/pdf/1812.02341.pdf)

https://bair.berkeley.edu/blog/2019/03/18/rl-generalization/


### Understanding Reinforcement learning

What are its goals. Its definitions. It methods?

- Optimality
- Model based
- Complexity
- Abstraction

But. It is possible that this representation achieves no compression of
the state space, making the statement rather vacuous. Further more, it
consider how easy it is to find the optimal policy in each of the two
representations. It is possible to learn a representation that makes the
optimal control problem harder. For example. TODO

Current theory does not take into account the structure within a RL
problem.

The bounds are typically for the worst case. But these bounds could be
tighter if we exploited the structure tht exists in natural problems.
The topology of the transition function; its, sparsity, low rankness,
locality, The symmetries of the reward function. ??? (what about both?!)

### Bad examples

That isnt to say that theory is all good.
Examples of bad theory. Unrealistic assumptions. Symbolics for the sake of symbols.
