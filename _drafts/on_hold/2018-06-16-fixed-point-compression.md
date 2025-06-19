---
layout: post
title: Fixed point compression
---

This is an attempt to extend compressed sensing to more stuctured priors. A combinaton of compressed sensing, graph signal processing and dynamical systems.

<!-- related https://onlinelibrary.wiley.com/doi/book/10.1002/0471732672 ??? -->

## Setting/Motivation.

Imagine we have a model of the dynamics of a system, $f_{dynamics}(\theta): V \to V$, and we can project a signal into our system $f_{x\to v}: X \to V$.

$f_{dynamics}(\theta): V \to V$ is defined as a graph. Where the edges capture the dynamics of the system and a single step is simulated by propagating a node's value to its neighbors.

$f_{x\to v}: X \to V$ takes the raw measurments and projects them into a signal on the graph.

In the setting of MRI we might have a dynamical model of the biological system, $f_{dynamics}$, simply set $f_{x\to v}$ to the identity (?!).

Finally, the traditional compressed sensing problem can be written as;

$$
\begin{align}
\hat x &= \mathop{\text{argmin}}_{\hat x}\parallel f(x) - \hat x\parallel_2 + P(\hat x) \\
P(\hat x) &=   \parallel \phi(\hat x) \parallel_1 \tag{a sparse basis}\\
\end{align}
$$

What I am proposing would replace the sparse basis with the distance from the nearest stable point. This can be written as;

$$
\begin{align}
v &= f_{x\to v}(\hat x) \\
h(v) &= d(V_{minima}, v) \\
P(\hat x) &= \parallel h(v) \parallel_1\\
\end{align}
$$

This regulariser is sparse because the are $n$ disctinct local minima. The minima can be found offline by randomly simulating the dynamical system $v_{t+1} = f_{dynamics}(v_t)$.

### Problems!?
- If the graph is not stochastic, the the same $v_0$ will always converge to the same local minima. Actually that seems fine.
- FFT can have a distribution of mass over many bases. Only one minima ...?
- optimising through an unrolled dynamical system... expensive. no we dont need to!?
- total distance to nearest local minima is a measure of plausibility!?
- if the dynamics diverge!? then just use a random distance...
- not sure dot product is the right measure of similarity. want the distance along the manifold, with some notion of the vector field!?
- $V_{minima}$ could be REALLY large. even for a minima that is a line we have an infinite set...
-


## Intuition.

* The sparse basis in CS projects a signal into basis where noise can be separated from the signal.
* Initialising the dynamical system 'near' a fixed point means the distance from the fixed point will be minimised as the system is allowed to evolve. Correcting the 'error' in the initialisation.
The set of fixed points of the dynamical system (defined by a graph) is our sparse basis.
* Each measurement is transformed into a signal on a graph (the dynamical model).


Need a broader defition of fixed points. Include any stable oscillations (of length < t). But they dont really have a location...
Unless we measure $h$ as the 1/distance of $v$ from each local minima.

### Linear measurements

$$
\begin{align}
f: X &\to Y \\
f(x) &= A \cdot x  + \epsilon \\
\end{align}
$$

### Linear dynamics

https://en.wikipedia.org/wiki/Power_iteration
Oh, does it only converge to the principle eigenvector!??

$$
\begin{align}
x_{t+1} &= x_t + \eta Wx_t \\
H(t) &= -x^T(t)Wx(t) \\
\Delta x &= Wx_t \\
\end{align}
$$

Wait a minute.!?

$$
\mathop{lim}_{n\to \infty} (I - W^n) = W^{-1}
$$


The 'dynamical system' will converge to the closest (? depends on relative strength??) eigenvector if $t\to \infty$.

So the fixed points of the dynamical system are the $k$ eigenvectors of $W$. Giving us our sparse basis.

##### Relationship to the graph fourier transform

$$
\begin{align}
L &= D-W \\
L &= U\Lambda V^T \\
v &= U \cdot x \\
\end{align}
$$

### Non-linear dynamics

Now. Want to generalise to a non-linear model, e.g. the dynamics of the human body.

Each local minima is one of our bases.

$$
\begin{align}
im \in \mathbb I &= \mathbb R^{h \times w \times c} \tag{image}\\
v \in \mathbb V &= \{\mathbb R^{\mid V\mid}\} \tag{graph}\\
f: \mathbb I &\to \mathbb G \\
v_0 &= f_{measure}(im) \\
H(t) &= f_{dynamics}(t) \\
v^* &= \mathop{\text{min}}_v H(t) \\
\end{align}
$$


## Resources

- [The Emerging Field of Signal Processing on Graphs](https://arxiv.org/abs/1211.0053)
- [Equilibrium propagation]()
- [Hopfield networks]()
- [Dynamical systems]()
