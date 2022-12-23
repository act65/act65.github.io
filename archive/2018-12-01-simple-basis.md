---
layout: post
title: Representations
---

It is surprising how many different techniques in applied mathematics can be reduced back to a simple equation.

Really the key to representation learning.

$$
\textbf  y = f(\textbf x, \epsilon) \\
$$

| Description | y | f | x | $\epsilon$ | Loss |
| ------ | ------ | ------ | ------ | ------ | ------ |
| PCA | None | Linear, Orthogonal | None | Additive, Gaussian, Stationary | $\parallel SV^Tx - y \parallel_2^2$ |
| ICA | None | Linear | statistically independent, p(x) | No noise | $H(p(Y=y)) - \sum_i H(p(Y_i=y_i))$ |
| FFT/wavelets | Sparse, complex | Linear, complex | None | No noise | ??? |
| Compressed sensing | None | Linear, Approximately orthogonal | Sparse | Additive, Gaussian, Stationary | $\parallel Ax - y \parallel_2 + \parallel x \parallel_1$ |
| 1-step graph propagation | None | Linear, Normalised rows | None | None | None |
| Dictionary learning | ? | ? | ? | ? |
| Random matrix theory | None | Linear, Random | |  
| Clustering | Discrete |
| Non-negative matrix factorisation | None | Non-negative, linear | None |

It makes me wonder what other combinations there are left to study and which other properties we could enforce.

What if
- $X/Y$ are ordered $\forall i: x_i < x_{i+1}$
- have symmetries (say between 2 dims - momentum/energy in dim i) that need to be preserved
- $X/Y$ is structured. A set of graphs, trees, groups...
- low rank, symmetric, positive semi definite, block, ...?
- noise can change, or be correlated with x?!
- uniformly distributed. the spaces came with measures as well.
-


What all of this is really about is how we can transform from one basis to another. Want better intuition here!
What are the best ways to interpret a vector over a basis? Depends on how they are allowed to be combined? As an attention over possibilities?



Are there any nonlinear examples that we can tractably analyse?

<!-- What about a taxonomy of all the problems related to;
- z* = argmax f(x) st y. LP, QP, ???. Wasserstein. Gumbel trick. ...!? (this would be a long list!?)
- L = minmax f(x, y). Minimax games, xAy...
- $\frac{dx}{dt} = f(x, t)$. ODEs, gradient descent, ...
  -->
