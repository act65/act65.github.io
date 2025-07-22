---
title: Uncertainty and graphs
subtitle: From uncertainty over constraints to uncertainty over graphs
categories:
    - research
layout: post
---

_(edited 22/07/25: Used LLM to rewrite and add some refs.)_

![]({{ site.baseurl }}/assets/uncert-graph.png)

## 1. Introduction: The Puzzle of Noisy Clues

Imagine solving a Sudoku puzzle where some of the given numbers are smudged and illegible. You can't be 100% certain if a square contains a '1' or a '7'. This uncertainty propagates through every logical step you take. A similar, but more complex, challenge arises in many scientific fields. In computational chemistry, for instance, determining a molecule's 3D structure from experimental data is a primary goal. [^4] Techniques like Nuclear Magnetic Resonance (NMR) spectroscopy provide a wealth of information, but this data is often noisy and ambiguous. [^1], [^3] The analysis might suggest an 80% chance that atom A is bonded to atom B, and a 20% chance it is not. [^2]

Traditional computational approaches often struggle with this ambiguity. They typically require a definite set of inputs—hard rules or constraints—forcing an analyst to make a judgment call and commit to a single hypothesis, potentially discarding the true structure. But what if we could embrace the uncertainty? [^11] How can we build a model that represents not just one plausible graph (or molecular structure), but a *distribution over all plausible graphs*? This post outlines a formal framework for doing just that. [^7]

## 2. The Classical Approach: Constraint Satisfaction

The conventional way to tackle such problems is by framing them as a **Constraint Satisfaction Problem (CSP)**. [^5] In a CSP, you have:

*   A set of **variables** (e.g., the existence of an edge between each pair of nodes in a graph).
*   A set of **domains** for these variables (e.g., {0, 1} for edge existence).
*   A set of **constraints** that solutions must satisfy (e.g., "the degree of node *vᵢ* must be 4," or "the graph must not contain a 3-cycle").

A CSP solver then finds the set of all assignments of variables that satisfy 100% of the given constraints. [^5] This is a powerful and well-established paradigm. However, its strength is also its weakness: it operates in a binary, all-or-nothing world. It cannot naturally handle a constraint that is only *probably* true.

## 3. A Probabilistic Framework: From Uncertain Constraints to Uncertain Graphs

To handle ambiguity in a principled way, we can extend the CSP framework using probability theory. [^7] The core idea is to map a *distribution over constraints* to a *distribution over graphs*. This process can be broken down into three conceptual steps.

#### Step 1: Model Uncertainty in the Constraints

Instead of starting with a single, fixed set of constraints, we begin with a probability distribution over a space of possible constraints, which we can denote `p(c|D)`. This distribution is conditioned on our observed data `D` (e.g., the NMR spectrum). Each `c` represents a complete, self-consistent set of rules that a graph could follow.

For example, let's say our data is ambiguous about a single edge between nodes 2 and 3. We could define two sets of constraints:
*   `c₁`: {The graph has a 4-cycle, **and** an edge exists between nodes 2 and 3}.
*   `c₂`: {The graph has a 4-cycle, **and** no edge exists between nodes 2 and 3}.

Based on our data `D`, we might assign probabilities `p(c₁|D) = 0.8` and `p(c₂|D) = 0.2`.

#### Step 2: Define the Link from a Constraint to a Graph

For any single, deterministic set of constraints `c`, what is the probability of a specific graph `g`? Let `G(c)` be the set of all graphs that satisfy the constraint set `c`. A natural and unbiased choice, reflecting a state of maximal ignorance beyond the constraint itself, is to assume a uniform probability over these valid graphs. We can write this as:

`p(g|c) = 1 / |G(c)|` if `g` is in `G(c)`, and 0 otherwise.

Here, `|G(c)|` is the total number of graphs that satisfy `c`. This assumption is a form of the principle of maximum entropy. [^6]

#### Step 3: Combine to Get the Final Graph Distribution

Finally, we can define the probability of any graph `g` given our data `D` by summing over all possible constraints, weighted by their probabilities. This is done using the law of total probability: [^7]

$$p(g|D) = \sum_c p(g|c)p(c|D)$$

In plain English, this equation states: "The total probability of a specific graph `g` is the sum of its probabilities under every possible constraint scenario, with each scenario weighted by how likely it is." This gives us our desired result: a full probability distribution over the entire space of graphs, elegantly accounting for the initial uncertainty in our knowledge.

## 4. The Elephant in the Room: Why This is Computationally Hard

While this framework is theoretically sound, implementing it naively is often computationally infeasible for two major reasons.

*   **The Constraint Explosion:** The space of possible constraints can be astronomically large. If we consider just the presence or absence of edges in a graph with *n* nodes, there are `n(n-1)/2` possible edges. If each edge's existence is an independent constraint, the total number of constraint sets is `2^(n(n-1)/2)`, a number that grows superexponentially.
*   **The Generation and Counting Problem:** The term `|G(c)|` in our equation requires us to *count* the number of graphs that satisfy a given set of constraints. This is a classic model counting problem, which for most non-trivial constraints falls into the complexity class **#P-hard** (pronounced "sharp-P hard"). [^8] This class of problems, which involves counting the number of solutions to problems in NP, is believed to be even harder than NP-complete problems. A polynomial-time algorithm for a #P-complete problem has not been found, and if one were, it would imply that P=NP. [^8]

## 5. Strategies for Practical Computation

The computational hurdles are significant, but not insurmountable. Several strategies can make this framework practical for real-world applications.

#### Strategy 1: Assume Sparsity

In many real-world scenarios, the distribution `p(c|D)` will be sparse. That is, the data will suggest that only a very small number of constraint sets are plausible, with all others having a probability at or near zero. This allows us to drastically reduce the number of terms in our summation, focusing computational effort only on the constraints that matter.

#### Strategy 2: Approximate Sampling with MCMC

Instead of trying to calculate `p(g|D)` for every single graph, we can try to draw samples from this distribution. [^9] This is precisely the kind of problem that **Markov Chain Monte Carlo (MCMC)** methods are designed to solve. [^9], [^10] An MCMC algorithm could work as follows:
1.  Start with a random graph.
2.  Propose a small change (e.g., add or remove an edge).
3.  Calculate how this change affects the graph's total probability `p(g|D)`. This still requires evaluating the sum, but it can often be done more efficiently than a full enumeration.
4.  Accept or reject the change based on this new probability.

By repeating this process, the algorithm explores the space of graphs, preferentially visiting those with higher probability. [^10] After many steps, the collection of visited graphs provides a faithful approximation of the true distribution.

#### Strategy 3: Exploit Compositional Structure

Constraints are not always monolithic. They can often be decomposed into independent or modular components (e.g., constraints on node degrees, connectivity, and the presence of specific subgraphs). By solving or analyzing these smaller, independent constraint systems separately, it may be possible to combine their solutions in a way that is far more efficient than tackling the full, combined problem at once.

## 6. Conclusion and The Road Ahead

The challenge of reasoning with noisy data is universal. [^11] When the goal is to uncover an underlying structure, like a molecule or a network, this noise translates into uncertainty about the rules that govern the structure. Traditional methods often force a premature decision, picking one set of rules and ignoring all other possibilities.

This post outlined a more principled alternative: a probabilistic framework that embraces uncertainty from the start. By defining a probability distribution over possible constraints, we can derive a full, posterior probability distribution over all possible graphs. This approach formally captures our state of knowledge, and our ignorance, in a way that binary models cannot.

While the computational cost of this method is high—rooted in the #P-hard problem of counting solutions—it is not a dead end. Practical strategies such as assuming sparse constraints, leveraging MCMC for approximate sampling, and exploiting the modular nature of the problem can make it tractable. [^9] The road ahead lies in developing more sophisticated algorithms that can navigate these complexities, ultimately allowing for more accurate and honest structural insights from ambiguous real-world data.

***
### References

[^1]: Y. Li, et al. (2023). Review on NMR as a tool to analyse natural products extract directly: Molecular structure elucidation and biological activity analysis. *Journal of Pharmaceutical and Biomedical Analysis*.
[^2]: F. Hu, et al. (2023). Accurate and efficient structure elucidation from routine one-dimensional NMR spectra using multitask machine learning. *Nature Communications*.
[^3]: S. L. Wessjohann, et al. (2022). Liquid Nuclear Magnetic Resonance (NMR) Spectroscopy in Transition—From Structure Elucidation to Multi-Analysis Method. *Applied Sciences*.
[^4]: E. Breitmaier (2002). *Structure Elucidation by NMR in Organic Chemistry: A Practical Guide*. Wiley.
[^5]: R. Dechter (2003). *Constraint Processing*. Morgan Kaufmann.
[^6]: M. J. Wainwright, M. I. Jordan (2008). Graphical models, exponential families, and variational inference. *Foundations and Trends® in Machine Learning*.
[^7]: D. Koller, N. Friedman (2009). *Probabilistic Graphical Models: Principles and Techniques*. MIT Press.
[^8]: L. G. Valiant (1979). The Complexity of Computing the Permanent. *Theoretical Computer Science*.
[^9]: M. R. Jerrum, A. Sinclair (1996). The Markov chain Monte Carlo method: an approach to approximate counting and integration. *Approximation algorithms for NP-hard problems*.
[^10]: C. J. P. van Ruiten (2019). Markov Chain Monte Carlo sampling of graphs. *Journal of Physics: Complexity*.
[^11]: D. A. C. Beck, et al. (2021). Uncertainty quantification in classical molecular dynamics. *Philosophical Transactions of the Royal Society A*.