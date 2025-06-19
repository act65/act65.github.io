---
layout: post
title: A better baseline for RL
---

Using a baseline of a random policy ... doesnt tell us much.

Examples from papers.

Imagine a 'memorizer' that stores past state-action values. For every state-action ever seen, it memorizes the discounted return recieved after finishing the episode. This could be used as an 'expensive oracle' to provide supervision for a learned policy.

Ok. Why doesn't this work?

- Use state-actions to look up a value.
- Use states to look up action values.

We are trying to approximate a $Q$-function with memory. Where $Q(s, a) = V[NN(s)]$


$$
Q(s, a) = V[NN(s;a)], \;\; V \in R^N\\
Q(s, a) = V[NN(s)][a], \;\;V \in R^{N \times |A|} \\
$$


$$
armax {[\sigma (d[NN(s)]) \cdot \sigma (v[NN(s)])]}_{i}
$$


Not going to be sample efficient.

Many neighbors, few neighbors.
Want to generalise... Clearly, to get sample efficiency we need to generalise.

- [Organizing experience](https://arxiv.org/abs/1806.04624)
- [Striving for simplicity in off-policy DRL](https://arxiv.org/abs/1907.04543)
- [Large memory layers with product keys](https://arxiv.org/abs/1907.05242)
- [Search on the Replay Buffer: Bridging Planning and Reinforcement Learning](https://arxiv.org/pdf/1906.05253.pdf)
