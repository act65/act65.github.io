---
layout: post
title: The natural selection operator
---

We understand the gradient descent operator reasonably well.
We can characterise easy (convex) and hard (non-convex) problems.
We can ...? rates of convergence.
Indctive bias.

$$
x \leftarrow \text{GD}(x) \\
x_{t+1} = x_t -\eta \nabla L(x)
$$


What about the natural selection operator?
$$
x \leftarrow \text{NS}(x) \\
x_{t+1} \sim L(x_t)
$$

- Sample according to fitness.
- Replicate and possibly mutate


Sample complexity of CMA-ES?!?!

***
So.

- Which classes of problems are easy for NS?
- How quickly does it converge?
- What inductive bias does it have?
