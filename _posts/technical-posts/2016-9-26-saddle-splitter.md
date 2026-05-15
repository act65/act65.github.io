---
title: Saddles, Splitting, and Reparameterization
subtitle: Dynamically Growing Neural Networks
layout: post
categories:
    - research
---

(updated with the help of a LLM 21/03/26)

A common heuristic in both human and machine learning is to build incrementally from the simple to the complex. In modern deep learning, we see this principle applied to the *training process* in a few different ways:

- **Curriculum Learning**: Providing the network with data or loss functions of increasing complexity, gradually ramping up the difficulty as the model learns the basics.
- **Boosting**: Iteratively learning new, simple functions to fit the residual errors of earlier learners, combining them into a powerful ensemble.

But what if we apply this incremental approach directly to the **architecture** of the network itself? Instead of initializing a massive, overparameterized network from scratch—which is computationally expensive and memory-intensive—can we start with a shallow, simple network and dynamically grow it? 

By doing so, we might be able to allocate compute only where it is strictly necessary, while actively navigating around obstacles in the loss landscape. In this post, we'll look at how network splitting and reparameterization allow us to "transfer" knowledge from simpler architectures to more complex ones, and how this technique can help us break out of optimization traps.

---

### Transferring Knowledge to Deeper Networks

Imagine we want to learn a deep network, but the loss function is highly non-convex. Training it from a random initialization is difficult; the optimizer might get trapped in local minima or plateau on flat saddle points. Conversely, a shallower network might optimize easily, but lack the representational capacity to solve the task accurately.

How about transferring knowledge from the simple learner to the complex one? Instead of starting from scratch, we can use the easier loss landscape of the shallow network as a stepping stone. 

Historically, several approaches have tackled this kind of architectural transfer:

* **[FitNets / Reverse Distillation](https://arxiv.org/abs/1503.02531):** Rather than traditional distillation (where a small network mimics a large one), we can train a deep(er) network to mimic the intermediate feature maps of a previously trained simpler network. 
* **[Mollifying Networks](https://arxiv.org/abs/1608.04980):** This technique transfers knowledge by starting with a heavily smoothed (mollified) objective function—which is nearly convex—and gradually annealing the smoothing to reveal the true, complex non-linear objective.
* **[FractalNet](https://arxiv.org/abs/1605.07648):** Fractal networks use a stochastic "drop-path" algorithm during training. This allows simpler, shallower sub-paths within the architecture to learn the core representations, which are then naturally transferred to deeper, more complex paths via horizontal connections.
* **[Network Morphism](https://arxiv.org/abs/1603.01670):** This involves applying a strict mathematical transformation to a layer that expands its size (width or depth) *without changing the output of the function*. It solves a matrix decomposition problem to ensure the network instantly performs exactly as it did before the growth, allowing training to resume seamlessly.

---

### The "Splitter" Algorithm

Inspired by classic incremental growing algorithms like the [Upstart algorithm](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1990.2.2.198) (1990) and more recent work like [Splitting Steepest Descent for Growing Neural Architectures](https://arxiv.org/abs/1910.02366), how can we use network morphism to actively guide optimization?

Consider a dynamic training loop:

```python
# Conceptual dynamic training loop
while Net.accuracy() < target_accuracy:
    Net.train_step()
    
    for layer in Net.Layers:
        # If the loss gradient is stagnating (stuck in a local minimum/saddle)
        if layer.dloss_buffer < tol:
            # Split the layer to add capacity and dimensions
            layer.split_morphism()  
```

This algorithm is theoretically elegant because it increases complexity *only as necessary* to accurately learn our target function. In an ideal world, the algorithm learns the shallowest, narrowest network capable of solving the task. 

But *why* does splitting a layer help optimization? If the network is stuck, why doesn't the expanded network just stay stuck?

---

### Reparameterization and Saddle Breaking

The key to understanding why dynamic growth works lies in the topology of the loss landscape.

Imagine we have a simple linear autoencoder, and our loss is:

$$ \mathcal{L} = \| x - ABx \|_2^2 $$

During training, the loss stops decreasing. The gradients are near zero, but the error is still high. We are stuck in a local minimum. To escape, we split the matrix $B$ into two new matrices, $C$ and $D$, such that $B = CD$. 

Does this reparameterization help us learn faster? Intuitively, yes. This feels conceptually similar to the **kernel trick** in SVMs: we are using the extra dimensionality of the reparameterized space ($CD$) to step around obstacles. 

In optimization theory, this phenomenon is known as **saddle breaking**. What appears to be a strict local minimum in a lower-dimensional space often transforms into a saddle point when embedded in a higher-dimensional space. 

Think of it like being stuck at the bottom of a 2D bowl. If we suddenly add a third dimension (by expanding the layer), the "bowl" might actually be shaped like a horse's saddle in that new dimension. The optimizer can now slide down the side of the saddle, continuing its descent. By splitting the layer and adding a tiny amount of symmetry-breaking noise, we create new descent directions.

---

### A Caveat on Linear Networks and Local Minima

There is an interesting, albeit counterintuitive, proof regarding this in the appendices of[Deep learning without poor local minima](https://arxiv.org/abs/1605.07110) (Kawaguchi, 2016). The author sets up a proof by contradiction to show that a collapsed linear network does *not* have the same loss surface as its deep counterpart, even though they represent the same function:

> Consider $f(w) = W_3W_2W_1 = 2w^2 + w^3$, where $W_1 = [w, w, w]$, $W_2 = [1, 1, w]^T$ and $W_3 = w$. Then, let us collapse the model as $a := W_3W_2W_1$ and $g(a) = a$. As a result, what $f(w)$ can represent is the same as what $g(a)$ can represent (i.e., any element in $\mathbb{R}$) [...]. We can conclude that every local minimum of $f(w)$ corresponds to a local minimum of $w=0$. However, this is clearly false, as $f(w)$ is a non-convex function with a local minimum at $w = 0$ that is not a global minimum, while $g(a)$ is linear without any local minima.

While the math is correct, we should be highly skeptical of applying this specific proof to standard deep learning optimization. Notice how the parameter $w$ is exactly shared across all three layers. This strict parameter sharing creates a highly artificial mathematical constraint, forcing non-convexity. 

In standard deep networks, weights are independent across layers. Adding independent parameters (overparameterization) doesn't trap us in artificial local minima like in Kawaguchi's toy example—rather, it provides the extra degrees of freedom necessary to escape them.

---

### Adding Depth vs. Adding Width

If we are going to dynamically split networks, we face a critical architectural choice: do we split to make the network *wider*, or do we split to make the network *deeper*? Each solves a fundamentally different problem in the loss landscape.

#### 1. Adding Width (Splitting Neurons)
Splitting neurons to make a layer wider primarily **smooths the loss landscape**. Theoretical results in the overparameterization literature (and the Neural Tangent Kernel regime) show that sufficiently wide networks eliminate suboptimal strict local minima entirely. They turn isolated valleys of good solutions into wide, connected basins (mode connectivity). If your optimizer is oscillating or stuck in a sharp ravine, adding width gives it the room to find a wider, flatter, and more generalizable minimum.

#### 2. Adding Depth (Splitting Layers Sequentially)
Splitting a layer into two sequential layers increases the **expressivity** and compositional power of the network. It allows the network to learn more complex, highly non-linear decision boundaries. However, adding depth without care can make optimization *harder* by shattering gradients and making the loss landscape more chaotic. 
If we add depth dynamically, we generally need to include residual skip-connections (like ResNets). Skip connections preserve a shallow "fallback" path, allowing the network to leverage the smooth landscape of the shallow network while gradually utilizing the newly added depth.

---

### Final Thoughts

This idea of dynamic network growth shares a beautiful mathematical symmetry with **Hierarchical Tucker decomposition** in tensor math, where you start with a massive, unwieldy tensor and recursively split it into a tree of smaller matrices. 

By running this process in reverse—dynamically splitting and growing our networks during training—we might be able to marry the computational efficiency of small networks with the smooth, easily navigable loss landscapes of highly overparameterized ones. It's a fascinating area of research that sits right at the intersection of Neural Architecture Search (NAS) and pure optimization theory. 
