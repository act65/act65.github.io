---
layout: post
title: Gradient diversity and generalisation
---

> General features are learned first/faster because the intra (and inter) batch examples positively interfere along their shared (aka general) features and negatively interfere along the features specific to one/a subset of the examples.

<side>Need to empirically validate, and possibly prove?</side>
This property (above) is the result of averaging the gradients of a batch together (really just a property of commutativity!?).

![pic]({{site.baseurl}}\images/svd-grad.png)

However, there is a problem with just averaging; A single pathological example (maybe a noised label) could arbitrarily skew the direction of the mean.

So, assuming this claim is true, and this problem does exist, the next question in my mind is to ask; Can we learn to generalise better/faster, and/or prevent over fitting, by clipping the weaker directions?

### Possible solutions

Use streaming PCA to project the gradients into a lower rank space, preserving the top-k directions of constructive interference while clipping the directions of less general use.

A couple of problems come up with naive implementations of this idea;

* need a buffer of gradients to be stored. So what is the trade-off between memory buffer and/or learning rate?
* each variable is possibly a different shape. So how can we project the gradients efficiently?

### Questions

* What problem could PCA projected gradients solve? If we assumed that the communication channel for the gradients was noisy then a possible solution would be to de-noise them, which PCA can be used to do. Does this have an information theoretic motivation, or a biological one?
* Does momentum approximate (or vice versa) the projection of the gradients onto their principle components. And is this why momentum helps us find good local minima?
* Is there a way to build the protection of the graphs into the structure of the network? Similar to how whitening can be built into a neural network. [Natural neural networks](https://arxiv.org/abs/1507.00210)
* Could we swap PCA for a linear layer between each node the gradients are propagated through? Aka train linear autoencoders, online, to project the gradients into a lower rank space.
* How does this relate to the much sought after low-variance gradients?


### Background reading

* [Deep Learning is Robust to Massive Label Noise](https://arxiv.org/abs/1705.10694)
* [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530)
* Recent paper that I cant find that clips low magnitude values of the gradients.
