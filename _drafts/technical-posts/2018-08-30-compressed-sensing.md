---
layout: post
title: "Compressed Sensing and the Magic of Implicit Regularization"
categories:
    - tutorial
    - machine-learning
    - math
---

Modern deep neural networks have a glaring, fundamental problem: they have millions more parameters than there are data points to train them on. 

By all the classical laws of statistics and linear algebra, these models should be wildly overfitting. They should memorize the training data and fail miserably in the real world. Yet, they don't. They somehow find solutions that generalize beautifully.

Why? The answer lies in the mathematics of taking photos with random noise—a field known as **Compressed Sensing (CS)**. 

In this post, we are going to explore how solving underdetermined systems in compressed sensing gives us the exact mathematical framework to understand why over-parameterized machine learning models actually work.

---

## 1. The Curse of Too Many Unknowns

Imagine a system of linear equations where we have more unknowns than equations. 

$$
y = Ax
$$

If $A$ is a "fat" matrix (more columns than rows), we don't have enough measurements ($y$) to uniquely determine the signal ($x$). Classical linear algebra tells us there are infinitely many valid solutions for $x$. How do we pick the right one?

If we don't know anything else about $x$, we can't. But what if we introduce an **assumption of structure**? What if we assume that the true $x$ is *simple*? 

In the real world, most signals are sparse. An image might have millions of pixels, but when transformed into a wavelet basis (like in JPEG compression), almost all the coefficients are zero. If we know that $x$ is mostly zeros, our infinite pool of solutions suddenly shrinks.

## 2. Measuring Sparsity ($L_0$ vs $L_1$)

To find the sparse solution, we want to minimize the number of non-zero elements in $x$ while still matching our measurements. We mathematically denote the "number of non-zero elements" as the $L_0$ norm. Our optimization problem looks like this:

$$
\min_x \|x\|_0 \quad \text{s.t.} \quad \|Ax - y\|_2 \le \epsilon
$$

There is a huge problem with the $L_0$ norm: it is incredibly brittle and NP-hard to optimize. If an element in $x$ is `1e-8` due to floating-point noise, $L_0$ counts it as a full non-zero element. Furthermore, it's non-convex; you can't use gradient descent on it. You would literally have to test every possible combination of non-zero elements.

What about the standard $L_2$ norm (Euclidean distance)?
$$ \|x\|_2 = \sqrt{ \sum x_i^2 } $$
The $L_2$ norm is wonderfully convex, but it *hates* sparsity. It penalizes large numbers heavily and prefers to spread the values out smoothly. It would rather have a hundred tiny non-zero values than one large one.

**The $L_1$ Miracle:**
The sweet spot is the $L_1$ norm (the sum of absolute values):
$$ \|x\|_1 = \sum |x_i| $$

There is a beautiful mathematical relationship where, under the right conditions, minimizing $L_1$ yields the exact same solution as minimizing $L_0$. $L_1$ is convex (meaning we can easily optimize it with gradient descent), yet its geometric shape (a sharp diamond in multi-dimensional space) naturally forces coefficients to be exactly zero.

*(Placeholder: Insert the classic geometric diagram here showing an $L_2$ circle vs an $L_1$ diamond intersecting a constraint line. The diamond's sharp corners guarantee the intersection happens on an axis, perfectly zeroing out a variable!)*

## 3. How to Sample: The "20 Questions" Analogy

Now that we know how to find a sparse signal mathematically, how should we collect the data ($A$) in the first place? 

Emmanuel Candès and Terence Tao, pioneers of compressed sensing, made a brilliant observation:

> "If your image consists of a few sparse dots... the worst way to sample it is by capturing individual pixels. The best way to sample the image is to compare it with widely spread-out noise functions. One could draw an analogy with the game of '20 questions.' If you have to find a number between 1 and $N$... the worst way to proceed is to guess individual numbers."

**How is comparing against random noise like 20 questions?**

If you sample a single pixel and it's black, you learned almost nothing. You only gained local information. But if you multiply the entire image by a matrix of random noise, *every single measurement contains a tiny bit of information about every single pixel*. 

Just like asking "Is the number less than $N/2$?" cuts your search space in half globally, a random projection cuts the possible vector space down globally. By taking measurements that are completely random, we guarantee that our measurement basis is maximally "incoherent" (dissimilar) to the image's natural basis. 

*(Side note: This global sampling approach has fascinating implications for Reinforcement Learning. Imagine an Atari agent dealing with partial observability. Instead of sampling exact pixels and hoping to see the ball, taking global random projections of the screen ensures no localized event is entirely missed).*

## 4. The Restricted Isometry Property (RIP)

But what if our random measurements scale the signal unpredictably, or blow up when we introduce noise $\epsilon$?

For this to work stably, our random matrix $A$ needs to satisfy the **Restricted Isometry Property (RIP)**:

$$
(1-\delta_S)\|x_T\|_2^2 \;\; \le \;\; \|A_{T}x_T\|_2^2 \;\; \le \;\; (1+\delta_S)\|x_T\|_2^2
$$

In plain English: If you take any sparse subset of columns from $A$ (denoted by $T$), they must behave almost exactly like an orthogonal matrix. They can't stretch or shrink the energy of the signal $x$ by more than a small factor $\delta$. 

Because the signal isn't aggressively scaled down toward zero, inverting the process doesn't require dividing by tiny numbers. Consequently, any noise $\epsilon$ in our measurements remains proportionally small in our reconstruction. The severely ill-posed matrix inversion is magically stabilized by the randomness of $A$.

## 5. The Machine Learning Connection

What does all of this have to do with Machine Learning? Let's look at the mathematical parallel.

In **Compressed Sensing**, to recover a ground truth signal, we solve:
$$ \min_x \|Ax - y\|_2^2 + \lambda \|x\|_1 $$
*(Given data $A$ and labels $y$, find a simple/sparse vector $x$.)*

In **Machine Learning** (e.g., linear networks or matrix sensing), we solve:
$$ \min_W \|XW - y\|_2^2 + \lambda \|W\|_* $$
*(Given data $X$ and labels $y$, find a simple/low-rank weight matrix $W$.)*

It is the exact same problem! In Deep Learning, our network parameters ($W$) vastly outnumber our training data ($X$). We are operating in a severely underdetermined regime. Just like in compressed sensing, there are infinitely many weight configurations that result in $0\%$ training error. 

To stop the network from memorizing noise, classical ML theory tells us we *must* add an explicit regularization term (like an $L_1$ or $L_2$ penalty) to force the model to pick the "simplest" solution.

But here is the mind-bending part: **Modern deep learning often doesn't use explicit regularization.** Yet, the models still generalize.

## 6. Algorithmic Regularization: The Optimizer is the Magic

How do neural networks pick the simple, generalizable solution out of infinite possibilities without us explicitly asking them to?

The answer lies in **Implicit (or Algorithmic) Regularization**. The optimization algorithm itself acts as the regularizer.

Consider a matrix factorization scenario where we parameterize our weights as $W = U U^T$. As Gunasekar et al. [3] point out:

> "The intuition above would still apply if we replace $UU^T$ with a single variable $X$ and run gradient descent... However, it will converge to a solution that doesn’t generalize. The discrepancy comes from another crucial property of the factorized parameterization: it provides a certain denoising effect that encourages the empirical gradient to have a smaller eigenvalue tail."

When we initialize a neural network with small random weights and train it using Gradient Descent, the path the optimizer takes through the loss landscape naturally biases it toward low-rank (simple) matrices. 

Even though we didn't explicitly write $+ \lambda \|W\|_*$ into our loss function, the geometry of gradient descent on factorized parameters essentially does it for us. **The optimizer is secretly doing compressed sensing.** It sifts through the infinite, underdetermined solutions and naturally settles on the one with the lowest complexity.

Ultimately, whether we are trying to reconstruct a high-resolution MRI from a few random samples, or train a billion-parameter language model on a fraction of the internet, the underlying math whispers the same truth: *The universe favors simplicity, and thankfully, our algorithms do too.*

***

### References

1.[Compressed Sensing Makes Every Pixel Count](https://www.ams.org/publicoutreach/math-history/hap7-pixel.pdf) - Emmanuel Candès and Terence Tao
2.[Stable Signal Recovery from Incomplete and Inaccurate Measurements](https://statweb.stanford.edu/~candes/papers/StableRecovery.pdf) - Emmanuel Candès, Justin Romberg, and Terence Tao
3.[Algorithmic Regularization in Over-parameterized Matrix Sensing and Neural Networks with Quadratic Activations](https://arxiv.org/abs/1712.09203) - Suriya Gunasekar, Blake Woodworth, Srinadh Bhojanapalli, Behnam Neyshabur, Nati Srebro

<!-- there's even more research about how NNs learn simple function first. should add that!? -->