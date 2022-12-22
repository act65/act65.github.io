---
title: "Another proposal: Science!"
date: "2018-08-22"
coverImage: "69116666-a-mandelbrot-set-zoom-image-created-in-a-fractal-generated.jpg"
layout: post
---

![]({{site.baseurl}}/images/{{page.coverImage}})

_(Wrote this for an application, which didn't end up working out. Was a real struggle to keep under the max word count.)_

> _How can we discover structure in complex systems?_ _How can we exploit the structure to achieve our goals?_

## Introduction

The goal of inferring causal relationships from observable phenomena is an old goal. Socrates, Democritus, … to the invention of modern science! We have come a long way, science has discovered many causes and this knowledge allows us to plan a better future.

In brief, the goal of this PhD is;

> _To understand the limits on efficiently learning an accurate, exploitable, model of an agent's environment._

## Motivating scenarios

1. I imagine an agent as a scientist, one that attempts to; tease apart distinct concepts, combine them into new hypotheses, design experiments to falsify the hypothesis and eventually recover the true dynamics.
2. I imagine an agent in a classroom, its goal is to stack the blocks on the floor into the tallest possible tower. This agent has access to a perfect model of its environment. But, why should the agent bother simulating the spins of atoms, the chemical composition of the wallpaper, the scattering of light, … We only want to simulate the details that are likely to significantly influence or be influenced by our actions. The positions of the blocks and their likelihood of falling.

## Related work

Model based reinforcement learning such as [1](https://worldmodels.github.io/), [2](https://arxiv.org/abs/1806.01363) has been shown to work effectively. What is exciting about this approach is that the learned models of an environment and the policies are disentangled. Thus models are transferable to different tasks, and policies are transferable to different environments, making learning more efficient.

Symbolic AI is an old field consisting of reasoning, planning and heuristic search. But recently it has been shown that search heuristics (for reasoning/planning) can be learned [3](https://arxiv.org/abs/1806.05898), [4](http://nature.com/articles/doi:10.1038/nature24270). This is exciting because it has hinted at  the possibility of integrating neural and symbolic systems (aka learned models and planners). There has been a flurry amount of work in this area [5](https://arxiv.org/abs/1711.03902). In my opinion, learning structured representations [6](https://arxiv.org/abs/1806.01242) is a promising research direction, as they provide interpretable and exploitable representations. The key problems can be summarised as; learning to reason [7](https://arxiv.org/abs/1705.11040), learning to reason with learned representations [8](https://arxiv.org/abs/1707.03389).

## Our approach

As may have been noted from the section on existing research, this is a popular field. My hope is to consider the problems a little more abstractly and to contribute understanding. Specifically, the types of question I want to answer are from the point of view of computational complexity.

### Representations

I am interested in exploring the advantage(s) provided by different representations of an environment. Having a model allows planning, but in situations when fast, probably approximately correct actions are sufficient, a model-free representation may achieve better results. **Q:** What are the advantages of different representations? **Q:** Is it possible to design a representation and can flexibly trade-off resources (memory/time, accuracy, latency, parallelism, samples, generalisation, …).

Relatedly, humans are hypothesised to have many different representations of information (or forms of memory; episodic, declarative, working, spatial, ...). **Q:** What problems do these representations solve and what advantage is provided?

### Optimisation (search)

Having a representation class that is efficient to run, or has the ability to approximate with arbitrary precision is nice, but is it possible to find those representations? **Q:** How could the class of representations be found by evolution, and how can a representation be optimised given data? **Q:** Under which circumstances is the true model efficiently recoverable via optimisation? **Q:** Which inductive biases in learning dynamics and representation lead to models that generalise?

If we have a system with multiple agents; a perceptual learner that disentangles inputs, a model learner generates a structured representation of its environment, a planner that attempts to exploit a model to optimise its reward, … (and possibly more agents) **Q:** what are the dynamics of the system? **Q:** When do exploitable representations emerge? **Q:** How does intelligence emerge from these agents collaborating to achieve their goals?

### Compression

The more you can compress a representation, while maintaining its predictive power, the closer it must be to the truth. This belief of underlying simplicity (or beauty if you are a physicist) is deeply rooted in the sciences. But what makes this a useful heuristic? The fact that phenomena are made up of simple parts can be exploited for efficient learning!

**Q:** How should you measure and optimise compression progress? **Q:** How can we learn representations that are incrementally built from simple parts? **Q:** How can we build biases towards simplicity into our learners?

## Summary

So whether we have learned a model that a Planner can exploit, or one that humans can wield, the value of an accurate, interpretable model that captures truth would be valuable for all, virtual agents and humans alike.
