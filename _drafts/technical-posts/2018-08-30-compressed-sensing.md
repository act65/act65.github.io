---
layout: post
title: Compressed sensing and machine learning
---

This post is about;

* how to make maximally informative queries
* ??
* ??

***

Only sample your environment to tell you what you need to know.

The problem is that we only have a few samples, they could have come from many places.
- how can we select a candidate from many?
- how can we pick samples to minimse the set of candidates?
- ?
(how general is this to partial information -- is it possible to apply to to Atari?)


$$
\begin{align}
\text{min} \parallel R(x) \parallel_1 \;\;\text{s.t.}\;\; \parallel f(x) - y \parallel_2 \le \epsilon \\
\end{align}
$$

$$
\begin{align}
f \perp g \\
\text{min} \parallel g(z) \parallel_1  + \lambda \parallel f(g(z)) - y \parallel_2 \\
\end{align}
$$


<side>The fact that we must mix the pixels feels like a cheat. We still need to physically interact with all the pixels, many times... But maybe mixing is cheap and measuring is not!?</side>

* Why doesnt the order matter?!?

Problem is; we have an image that may be sparse in a basis. How do we find which elements are non zero?
- Could search through them all,
-

> If your image consists of a few sparse dots or a few sharp lines, the worst way to sample it is by capturing individual pixels (the way a regular camera works!). The best way to sample the image is to compare it with widely spread-out noise functions. One could draw an analogy with the game of “20 questions.” If you have to find a number between 1 and $N$, the worst way to proceed is to guess individual numbers (the analog of measuring individual pixels). On average, it will take you $N$/2 guesses. By contrast, if you ask questions like, “Is the number less than $N$/2?” and then “Is the number less than $N $/4?” and so on, you can find the concealed number with at most $log_2 N$ questions.

hmmm. How is asking "is the number less than N/4?" like comparing against a random signal?
"How much of the image vector points in this, random, direction?"
If you know after 2 measurements that an image is partially similar to up/left, and up/right then you should conclude up.

> Notice that the “20 questions” strategy is adaptive: you are allowed to adapt your questions in light of the previous answers. To be practically relevant, Candes and Tao needed to make the measurement process nonadaptive, yet with the same guaranteed performance as the adaptive strategy just described. In other words, they needed to find out ahead of time what would be the most informative questions about the signal x.

How is this related to a hash fn?!

## Assumption of structure

What other possible kinds of structure are there?!


## Measures of sparsity

What we need is a measure of sparsity.
Better than that want one that can handle approximate sparsity/noise.

$$
\begin{align}
\parallel x \parallel_0 &= \sum_{i=0}^n x_i^0 \tag{assuming $0^0=0$}\\
\parallel x \parallel_1 &= \sum_{i=0}^n \mid x_i \mid \\
\parallel x \parallel_2 &= \sqrt{ \sum_{i=0}^n  x_i^2 } \\
\end{align}
$$

Problem with $L_0$ is that it doesnt tell use how close we are to a sparse solution.
One of the elements might be $= 1e-8$ yet, it is still counted as a non-zero element.


<side>does this relationship generalise to higher $L_P$ norms?</side>
There is a nice relationship between $L_0$ and $L_1$ minimisers

$$
\begin{align}
\forall b_i \in \{?!? \}, A = \in \{?!? \} \\
\mathop{\text{min}}_{A, b} \parallel Ax + b \parallel_0 &= \mathop{\text{min}}_{A, b} \parallel Ax + b \parallel_1
\end{align}
$$

Probability of sampling a line that intersects the origin. How can this be proved?

Can be easily understood geometrically as ... (insert image)


## Randomness and mixing

Two uses. L_0 = L_1 AND dissimilarity to image basis (make sure you get a good mixture).


I wonder if existing physical processes might do the mixing for us? E.g. An EEG of the brain represents a local mixture of electric potentials. Can this be used to do compressed sensing?

## Restricted Isometry
(the formalisation of our concept of mixing!?)

$$
\begin{align}
d_Y(f(a), f(b)) = d_X(a, b)
\end{align}
$$

$$
\begin{align}
(1-\delta)\parallel y \parallel_2^2 \le \parallel Ay \parallel_2^2 \le (1+\delta)\parallel y \parallel^2_2
\end{align}
$$

<side>What goes wrong if the signals can be scaled?</side>
Doesnt tend to change the magnitiude of the vector $y$, aka A must be approximately a rotation (no scaling), ie an orthogonal transformation.

What does it mean to do a rotation? The basis you use to descibe Y is ?!?! relation to X.


But RIP is (how much if at all!?!?) weaker than requiring an orthogonality.

> This property essentially requires that every set of columns with cardinality less than S approximately behaves like an orthonormal system

I see how it requires every set of columns with cardinality less that S approximately behaves like a normal system, but not orthonormal.


$$
\begin{align}
(1-\delta_S)\parallel y_T \parallel_2^2 \;\; &\le \;\;\parallel A_{:, T}y_T \parallel_2^2 \;\; \le \;\; (1+\delta_S)\parallel y_T \parallel^2_2 \\
\forall T &\subseteq \{1, \dots n\} \;\; \text{s.t.} \;\; \mid T \mid \; = S \\
\end{align}
$$

Questions;

- why forall T?
- what value of y is used?
- ?

***

>  There are no known large matrices with bounded restricted isometry constants (computing these constants is strongly NP-hard,3 and is hard to approximate as well 4)  - https://en.wikipedia.org/wiki/Restricted_isometry_property

## Stable recovery from incomplete and noisy measurements

> How can we possibly hope to recover our signal when not only the available information is severely incomplete but in addition, the few available observations are also inaccurate?

>  To be broadly applicable, our recovery procedure must be stable: small changes in the observations should result in small changes in the recovery.

__Theorem 1.__ (from [2](#2))

Let $S$ be such that $\delta_{3S} + 3\delta_{4S} < 2$. Then for any signal $x_0$ suported on $T_0$ with $\mid T_0 \mid \le S$ and any pertubation $e$ with $\parallel e \parallel_2 \le \epsilon$, the solution $\hat x$ to ($P_2$) obeys

$$
\parallel \hat x - x_0 \parallel_2 \le C_S \cdot \epsilon \\
$$

__Q__ what is C? how does it depend on S?

Note:

* Any $\epsilon$. Hmm. Generalsing this to ML, we might have some issues. Needs to be stable to pertubations, but adversarial examples would break this...
* Where does $\delta_{3S} + 3\delta_{4S} < 2$ come from, seems rather weird!?
*

> The fact that the severely ill-posed matrix inversion keeps the perturbation from “blowing up” is rather remarkable and perhaps unexpected

<aside>
Why is the inversion of a rectangular matrix (and/or low rank) sensitive to pertubations?

...?!?
</aside>

> no recovery method can perform fundamentally better for arbitrary perturbations of size $\epsilon$ ... obtaining a
reconstruction with an error term whose size is guaranteed to be proportional to the noise level is the best one can hope for.



## Relationship to machine learning

To recover some ground truth, we are allowed to take measurements.
But which measurements should be taken? The above tells us they should be maximally inoherent with ???.

Then $A$ is our data, $y$ the labels, and $x$ is function we want to recover.

$$
\begin{align}
x &\in \mathbb R^n, y_i \in \mathbb R, A \in \mathbb R^{m \times n}  \\
y_i &= \langle A_i, x \rangle \tag{compressed sensing}\\
\mathop{\text{min}}_x & \parallel Ax - y \parallel_2 + R(x) \\
\\
x_i &\in \mathbb R^n, y_i \in \mathbb R^m, A \in \mathbb R^{m \times n}\\
y_i &= \langle A, x_i \rangle \tag{machine learning} \\
\mathop{\text{min}}_A & \parallel Ax - y \parallel_2 + R(A) \\
\end{align}
$$

Neither can be solved by gaussian elimination (or other methods -- which are!?!?) because they are ...?

* Is there a way to incorporate beliefs about noise the data to ML?

***

> We note that the factorized parameterization also plays an i mportant role here.  The intuition above would still apply if we replace U U ⊤ with a single variable X and run gradient descent in the space of X with small enough initialization.  However, it will converg e to a solution that doesn’t generalize.  The discrepancy comes from another crucial property of the factorized parameterization:  it provides certain denoising effect that encourages th e empirical gradient to have a smaller eigenvalue tail.

## References

1. <a name="1">[Compressed Sensing Makes Every Pixel Count](https://www.ams.org/publicoutreach/math-history/hap7-pixel.pdf)</a>
2. <a name="2">[Stable Signal Recovery from Incomplete and Inaccurate Measurements](https://statweb.stanford.edu/~candes/papers/StableRecovery.pdf)</a>
3. [Algorithmic Regularization in Over-parameterized Matrix Sensing and Neural Networks with Quadratic Activations](https://arxiv.org/abs/1712.09203)
