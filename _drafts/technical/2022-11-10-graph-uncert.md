---
layout: post
title: Solving uncertain CSPs
permalink: graph-uncert
---

INCLUDE pics!

Given uncertain inferences from (noisy) data about the structure / properties of a graph, we want to construct a distribution over likely / plausible graphs.

For example we may;
- have high confidence that; the graph has a cycle, contains subgraph X,
- be uncertain whether; node 1 is bonded node 2, ...
- ?

<!-- $$
\begin{align}
p_{g'}(g' \subset g) &\quad\quad g \in ?? \tag{$p$ that $g'$ is in $g$}\\
p_x(f(g), x) \tag{$p$ that $f(g) = x$}\\
p_x(deg(v_i), x) &\quad\quad x \in \mathcal Z\\
p(e_{ij} \in g) &\quad\quad  e_{ij} \in \{0,1\}
\end{align}
$$ -->


In the simplest case, we can make inferences with 100% certainty. This allows us to directly solve the CSP.

- the graph has A) a 3-cycle and B) subgraph g. Therefore slove the CSP with the constraint given A, B. 

But when we are uncertain.

- the data suggests the graph probably has an edge between nodes 2,3. But it may not. 80%:20%.
- ?

## Constrained distributions

> Map a distribution over constraints to a distribution over graphs.

Let there be a space of constraints $c \in \mathcal C$. For example, the constraint that a graph must have a node with degree 5.
And there is a CSP solver that maps these constraints $c$ to a set of graphs.
We write this as $CSP(c) = \{ g : \text{if} \;\; c(g) \} $

Let $p(c\mid D)$ be a distribution over constraints, possibly informed by data. 

We define the probability of a graph given a constraint to be 

$$p(g\mid c) = \frac{\mathbf 1_{g \in \mathcal CSP(c)}}{\mid CSP(c) \mid}$$

Aka. A uniform distrubution over all satisfying graphs.

Then we can write $p(g\mid D)$ as;

$$
\begin{aligned}
p(g|D) &= \sum_c p(g|c)p(c|D) \\
\end{aligned}
$$


***

What's the probability of a constraint given a distribution over graphs?
(take the count of graphs that satisfy the constraint, and multiply by the likeliood of each graph)
$$
\begin{aligned}
p(c|g)p(g) &= \sum_g 1_{g \in G(c)}p(g) \\
\end{aligned}
$$

***

Alternative way to write as a sum
$$
\begin{aligned}
p(g|c) &= \frac{\mathbf 1_{g \in \mathcal G(c)}}{|G(c)|} \\
&= \sum_{g' \in G(c)} \frac{1_{g=g'}}{|G(c)|}
\end{aligned}
$$


## Background / application

The tradition approach to NMR for graph structure elucidation is to infer connectivity from the 2D NMR experiments. These experiments tell us things like; carbon 1 and hydrogen 3 are connected, ...

This information can then be used to generate all graphs that satisfy these conditions. There generated graph are the plausible structures of the imaged sample.  

## Computational problems.

What about when the set of possible constraints is very large?

In the NMR setting we have access to a subset of the pairwise node connectivities ($2^{\frac{n(n-1)}{2}}$ different constraints). And a subset of the pairwise node distances (???).


Lots of possible constraints.
Lots of possible graphs.

We dont want to construct all of them, and then sum over them.
Rather. Solve CSP without uncertain constraints. Then filter / apply later?

#### The space of constraints

Each constraint is independent?
So the space of constraints is the outer product of the constraints?!
How does this scale with graph size?

$$
\mathcal C = c_1 \times c_2 \times \dots
$$

Example.
Connectivity constraints.
Each possible edge, could be $[-1, 0, 1, 2, 3, ..., k]$.
Each edge is independent from others.
Therefore, the number possible constraints is $(k+1)^{n^2}$.


#### Generating the graphs

Problem is generating

$$
\{G(c): p(c) > 0 \forall c \in \mathcal C\}
$$

Great. But how to actually construct this...
This is where the problem lies! How to actually compute with these structures efficiently!


## Efficient computation


#### Sparsity?

The support of these distributions should be small?
So we dont need to sum over all graphs. Only the ones with non zero probability. But how could we know / isolate this set efficiently?

Depends on the support of the constraints... Need them to have small support!?

For each supported constraint. Find graphs that satisfy these constraints. Hope that this set is much smaller than the set of all possible graphs.

This requires us to solve many SAT problems, one for each constraint...

$$
G' = \cup_c G(c)
$$

#### Approximate sampling

Does there exist some kind of efficient MC sampler that can be proven to be unbiased?
That's what I want?!

#### Compositional structure within constraints

$$
C = C_{degree} \times C_{connect} \times C_{neighbor} \\
c^a = c_{degree}^i \circ c_{connect}^j \circ c_{neighbor}^k \\
c^b = c_{degree}^i \circ c_{connect}^j \circ c_{neighbor}^{k+1} \\
\dots
$$

***

Notes

- It's easy to calculate $g \in G(c)$, as we only need to calculate whether g satisfies the constraint, $f(g) = c$.

***


$$
p(\mathbf g | \mathbf c) = M_c^g p(\mathbf c) \\
\begin{bmatrix}
\mathbb 1_{c_1(g_1)} & \mathbb 1_{c_1(g_2)} & \mathbb 1_{c_1(g_3)} \\
\mathbb 1_{c_2(g_1)} & \mathbb 1_{c_2(g_2)} & \mathbb 1_{c_2(g_3)} \\
\mathbb 1_{c_3(g_1)} & \mathbb 1_{c_3(g_2)} & \mathbb 1_{c_3(g_3)} \\
\end{bmatrix}
\begin{bmatrix}
\mathbb p(c_1) \\
\mathbb p(c_2)\\
\mathbb p(c_3) \\
\end{bmatrix}
$$


***

Future work
- Allow the number of nodes to be uncertain.


Non-square det https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=non+square+determinant&btnG=

Dist over graphs https://mathoverflow.net/questions/385330/how-to-define-probability-over-graphs
