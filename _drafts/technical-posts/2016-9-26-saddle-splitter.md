---
layout: post
title: Saddles, splitting and reparameterisation
---
<!-- Core idea is path distillation! -->
A heuristic used when learning, is to incrementally build from simple to complex? There seems to be two approaches to gradually building the complexity required;
- [curriculum learning]() provides loss functions with increasing complexity (while each intermediate loss function is somehow related to your true goal).
- [boosting]()
<!-- - [] incremental learning the NNs do!?-->

Another approach/point of view is a type of [transfer learning]() between the simpler learners (/loss function) to the more complex.

In the image below, we want to learn the deep network, the one on the right labelled $L4$. But the loss function (shown underneath in magenta) is just too complex, so how can we do it? How about transferring some knowledge of the task from simpler learners? (ignore the horizontal lines for now)

<side>Boosting acheives this transfer by reusing the eariler learners and learning functions to fit the residual.</side>

![pic]({{site.baseurl}}\images/Curriculum.png)

In general, there are a few different methods that can be used to transfer knowledge from simple learners to more complex;

<side>Would like a more comprehensive list!</side>
* [Mollifying networks](https://arxiv.org/abs/1608.04980) transfer knowledge continuously (?) from linear to (more) non-linear networks using ??!
* Reverse [Distillation](https://arxiv.org/abs/1503.02531) by training a deep(er) network to mimic a simpler one, similar to feature matching
* In essence [Network morphism](https://arxiv.org/abs/1603.01670) solves a matrix decomposition of a layer (which can get complicated for non-linear layers)
* For those of you who have seen it before, the above picture may remind you of the [Fractal net](https://arxiv.org/abs/1605.07648) architecture. Interestingly, the fractal network uses a stoachastic path picking algorithm which allows the simpler networks to transfer their knowledge. (paths are randomly picked through each of the four learners by using the horizontal connections)

### Splitter

Inspired by the [Upstart](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1990.2.2.198?journalCode=neco#.V-9IzZN96zY) algorithm, how can we use the above ideals and techniques to learn a more complex net from simpler ones?

```python
# while learning
while Net.accuracy() < tol:
    Net.train_step()
    for layer in Net.Layers:
        # if the loss is not changing much in a given layerW
        if layer.dloss_buffer < tol:
            # split the layer in two using network morphism
            Net.layer.split()  
```

<side>Hmm, I wonder what guarauntees could be given on the depth of the network learned!?</side>
This algorithm is nice because we are increasing complexity only as necessary to accurately learn our target function. In an ideal world the algorithm would learn the shallowest network capable of accurately approximating our target function.

### Reparameterising linear networks

[Deep learning without poor local minima](https://arxiv.org/abs/1605.07110) has an interesting note buried in its appendices about the implications w.r.t optimisation of a linear network's ability to be collapsed.

$$
\begin{align}
y &= f_{W_{1:N}}(x) \\
&= W_1\dots W_i \dots W_nx \\
&= Ax \tag{collapse the matrices}\\
&= f_A(x) \\
\end{align}
$$

And while it is true that these two networks ($f_{W_{1-N}}, f_A$) can represent the same transformations, linear ones. It is not true that they have the same loss surfaces, see the proof via contradiction below.

<side>Not sold on this proof. It shares a parameter through the layers, which seems like a different thing to the original argument!?</side>
> Consider $f(w) = W_3W_2W_1 = 2w^2 + w^3$, where $W_1 = [w, w ,w]$, $W_2 = [1, 1, w]^T$ and $W_3 = w$. Then, let us collapse the model as $a:= W_3W_2W_1$ and $g(a) = a$. As a result, what $f(w)$ can represent is the same as waht $g(a)$ can represent(i.e. any element in $\mathbb R$) with the same rank restriction. Thus with the same reasoning, we can conclude that every local inimum of f(w) corresponds to a local minimum of $w=0$. However, htis is clearly false, as $f(w)$ is a non-convex function with a local minimum at $w = 0$ that is not a global minimum, while $g(a)$ is linear (convex and concave) without any local minima.

### Saddle breaking

The main question (for me) that comes of out this insight is whether reparameterising a weight matrix can free us from an obstacle in the loss surface. For example, if we have a simple linear autoencoder

$$\mathcal L = \parallel x - ABx\parallel_2^2$$

and we split $B$ into $CD$ such that $B = CD$ then does it help us learn faster? Intuitively, this feels somewhat like the kernel trick, where we can use the extra dimensionality of the reparameterised $CD$ to make our way around saddles or other obstacles in the loss surface.

__ TODO Adding depth versus adding width! What problem do they solve?__

### Notes

This also reminds me of the Hierarchical Tucker decompsition. Start with a big wide tensor. Recursively split the wide net into two matrices. Not sure what do do with that...

- [Splitting Steepest Descent for Growing Neural Architectures](https://arxiv.org/abs/1910.02366)
