---
title: "Projects"
date: "2017-05-03"
layout: post
---

![]({{site.baseurl}}/images/{{page.coverImage}})

What are the deepest problems we do not understand?

## Physical trade-offs of learning

Claim: Algorithmic complexity is conserved over algorithms for a given problem.

While a new algorithm may be proposed for matmul that requires O(n^2.73) (rather than the naive O(n^3)) I claim that the complexity has been smuggled elsewhere. We happen not to be measuring (say) the energy cost of the algorithm, or is ability to be parallelised, or its robustness to perturbation, or ...???

In my mind everything can be reduced to physics. So without grounding the analysis of algorithms in physics the design of an algorithms seems baseless and we can get away with unfair comparisons. This means that every algorithm (for a given problem) is of equivalent complexity, and we can trade-off different resources as we like.

Specifically, I am interested in;

- the conservation of complexity in learning algorithms, where you can trade memory for time complexity, data complexity for accuracy, ... but what about trading accuracy for energy complexity?
- the limits of these trade-offs, and finding optimal trade-offs for practical use.

##  Evolution

Sure, evolution occurred, but by what process? Before we can prove that natural selection, or any other process, was the mechanism behind evolution we need to show that it could have acted at a fast enough rate to evolve the complexity we see.

## Collaboration

The next benchmark for AI should be football? I am imagining a team of humans being beaten by a team of robots (using similar energy requirements and learning time).

These artificial players would need to;

- communicate with each other over a noisy and bandwidth-limited channel,
- trade-off computational requirements for acting and learning,
- be energy efficient enough to last 90 mins of activity,
- learn to collaborate and specialise to optimise a global reward,
- act in real time with very few computational resources.
