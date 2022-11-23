---
layout: post
title: Representations in linear algebra
---

Linear algebra and arrays combine to give us a powerful language. Let's explore the power of them represent interesting languages/systems/grammars/algebras...

## Embedded linear operators

One of the cool things about linear algebra is that linear functions can be written as arrays. This representational duality between operator and operand is rather elegant.

<!-- Related to Turing's duality of data and program. Where ... -->

<!-- But are these more that just nice mathematical curiosities? Why is this useful or important? -->

Let start with linear functions of polynomials.

Consider the space of polynomial coefficients, $a \in  {\mathbb R}^{\infty}$. Where $a_i$ is the coefficient for $x^i$. Thus $a = [0, 5, 3, 0, 1, \dots]^T$ represents

$$
0\cdot x^0 + 5\cdot x^1 + 3\cdot x^2 + 0\cdot x^3 + 1\cdot x^4 \\
= x^4 + 3\cdot x^2 + 5\cdot x
$$

##### The differentiation operator

We can define a differentiation operator, $D$, as a matrix.

$$
\begin{align*}
\mathcal D &= \begin{bmatrix}
0 & 1 & 0 & 0 & \dots \\
0 & 0 & 2 & 0 &  \dots \\
0 &0 & 0 & 3 & \dots \\
\vdots & \vdots & \vdots & \vdots & \ddots \\
\end{bmatrix} \\
\end{align*}
$$

And we can 'do' differentiation via matrix multiplying $\frac{d}{dx}a = \mathcal D \cdot a$.
<side>Problem (we need infinite matrices for this to work out...)</side>



This all works out because differentiation is a linear function! Each column is the derivative of a 'basis' function, which in this case is each $x^n$. Now, lets test it out.

$$
\begin{align}
y &= x^4 + 3\cdot x^2 + 5\cdot x \\
a &= [0, 5, 3, 0, 1]^T \\
\frac{d}{dx} a &= \mathcal D \cdot a \\
&= \begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 4 \\
0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix} 0 \\ 5 \\ 3 \\ 0 \\ 1
\end{bmatrix} \\
&= \begin{bmatrix} 5 \\ 2 \cdot 3 \\ 0 \\ 4 \cdot 1 \\ 0 \end{bmatrix} \\
\frac{d}{dx}a &= 4\cdot x^3 + 6\cdot x + 5 \\
\end{align}
$$

<side>Homework: What is the derivative of a derivative, $D \cdot D$? Does it make sense?</side>
Awesome.

#### Integral (of polynomials)

What about integrals, they are linear operators. Can we write them in a similar manner?

$$
\begin{align}
\mathcal I &= \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & \dots \\
1 & 0 & 0 & 0 & 0 & \dots \\
0 & \frac{1}{2} & 0 & 0 & 0 & \dots \\
0 & 0 & \frac{1}{3} & 0 & 0 & \dots \\
0 & 0 & 0 & \frac{1}{4} & 0 & \dots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
\end{bmatrix} \\
\end{align}
$$

So, we can define an integral operator, $\mathcal I$, and apply it via matrix multiplication.

$$
\begin{align}
y &= x^4 + 3\cdot x^2 + 5\cdot x \\
a &= [0, 5, 3, 0, 1]^T \\
\int a \; dx &= \mathcal I \cdot a \\
&= \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 & 0 & 0 \\
0 & 0 & \frac{1}{3} & 0 & 0 & 0 \\
0 & 0 & 0 & \frac{1}{4} & 0 & 0 \\
0 & 0 & 0 & 0 & \frac{1}{5} & 0 \\
\end{bmatrix}
\begin{bmatrix} 0 \\ 5 \\ 3 \\ 0 \\ 1 \\ 0
\end{bmatrix} \\
&= \begin{bmatrix} 0 \\ 0 \\ \frac{5}{2} \\ \frac{3}{3} \\ 0 \\ \frac{1}{5} \end{bmatrix} \\
&=  \frac{1}{5} x^5 + \frac{3}{3} x^3 + \frac{5}{2} x^2\\
\int a \; dx &=  \frac{1}{5} x^5 + \frac{3}{3} x^3 + \frac{5}{2} x^2 + c\\
\end{align}
$$

<side>Ok. So this works, up to an added constant, $c$.</side>

***

Intriguingly, we can relate the integration and differentiation operators via $\mathcal I = \frac{1}{\mathcal D^T}$.

### Linear operations on ???


#### Matrix multiplication

$$
C_{ij} = \sum_k A_{ik}B_{kj} \\
C_{ijk} = T^{MMT}_{ijk} A_{ik}B_{kj}
$$

> The matrix multiplication tensor
https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4


#### Determinant

??? can this be written as a matrix?

## Algebras

And Type-systems (aka algebras?)
Strongly typed …

##### Dual numbers

> the dual numbers extend the real numbers by adjoining one new element $\epsilon$ with the property $\epsilon^2 = 0$.

$$
a + b\epsilon \rightarrow
\begin{bmatrix}
a & b \\
0 & a \\
\end{bmatrix} \\
$$


$$
\begin{align*}
(a + b\epsilon)(c + d\epsilon) &= ac + ad\epsilon + bc\epsilon + bd\epsilon^2\\
&= ac + (ad + bc)\epsilon \\
\begin{bmatrix}
  a & b \\
  0 & a \\
\end{bmatrix}
\begin{bmatrix}
  c & d \\
  0 & c \\
\end{bmatrix}
&=
\begin{bmatrix}
  ac & ad + bc \\
  0 & ac \\
\end{bmatrix} \\
&\rightarrow  ac + (ad + bc)\epsilon
\end{align*} \\
$$


Dual numbers actually happen to capture the product, sum and chain rules.!!! __TODO__.

##### Complex numbers

$$
\begin{align}
1 &\equiv \begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix},\quad
i \equiv \begin{bmatrix}
0 & 1 \\
-1 & 0 \\
\end{bmatrix} \\
a + b i &=
a\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix} +
b\begin{bmatrix}
0 & 1 \\
-1 & 0 \\
\end{bmatrix} \\
&= \begin{bmatrix}
a & b \\
-b & a \\
\end{bmatrix}
\end{align}
$$

$$
\begin{align}
(a + b i)(c + d i) &= ac + adi + bci - bd \\
&= ac - bd + (ad - bc)i \\
\begin{bmatrix}
a & b \\
-b & a \\
\end{bmatrix}
\begin{bmatrix}
c & d \\
-d & c \\
\end{bmatrix} &=
\begin{bmatrix}
ac - bd &  ad - bc\\
-(ad - bc) & ac - bd \\
\end{bmatrix}\\
&= (ac - bd)\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix} +
(ad - bc)\begin{bmatrix}
0 & 1 \\
-1 & 0 \\
\end{bmatrix}
\end{align}
$$

- __Q__ What does the fact that complex numbers can be represented as a 2 variable, 2x2 matrix? What does it imply about the types of transforms it can do?




#### Quarternions

$$
\begin{align}
1 &= \begin{bmatrix}
\;1 & 0 & 0 & 0 \\
0 & \;1 & 0 & 0 \\
0 & 0 & \;1 & 0 \\
0 & 0 & 0 & \;1 \\
\end{bmatrix},\quad
i = \begin{bmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix} \\
j &= \begin{bmatrix}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
\end{bmatrix},\quad
k = \begin{bmatrix}
0 & 0 & 0 & -1 \\
0 & 0 & -1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix} \\
\end{align}
$$

and the negatives, $-1, -i, -j, k$ are simple derived by taking the element wise negative of the linear representations.


<side>Feel free to verify that (say) $k \cdot j = -i$</side>


$$
\begin{align}
i \cdot j &= \begin{bmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix} \cdot
\begin{bmatrix}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
\end{bmatrix} \\
&= \begin{bmatrix}
0 & 0 & 0 & -1 \\
0 & 0 & -1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix} \\
&= k \\
\end{align}
$$

The really cool part is that the quarternions, $\mathbb Q$, can be generated by taking the outer product of the complex numbers with themselves, $\mathbb C \otimes \mathbb C$. And this still works for these linear representations.

$$
\begin{align}
1_C \otimes 1_C &= 1_Q \\
1_C \otimes i_C &= i_Q \\
i_C \otimes i_C &= j_Q \\
i_C \otimes 1_C &= k_Q \\
\end{align}
$$


More info [here](https://groupprops.subwiki.org/wiki/Linear_representation_theory_of_quaternion_group)

#### Octonions

The pattern continues!

***

- Clifford algebras?
- ?

### Computation
##### Logic

We have two bits, $xy$. We can encode the 4 possible arangements $00, 01, 10, 11$ in a four dimensional space, $\mathbb R^4$. Let $a \in \mathbb R^4$, then $a_0 = a(00), a_1 = a(01), a_2 = a(10), a_3 = a(11)$. Now we require all operations to be unitary and all vectors to be within the basis, $a_0, ..., a_n$.

$$
\begin{align}
CNOT \equiv
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}
\end{align}
$$

#### (quantum) computation


### Memory

[Holographic reduced representations](http://www2.fiit.stuba.sk/~kvasnicka/CognitiveScience/6.prednaska/plate.ieee95.pdf)

### Graphs
(`matmul -> message passing`)

!?? Can represent graphs in linalg.

Other

* Seripinski triangle

# Thoughts

- Why is linear algebra such an effective language for thinking about and expressing structure in systems?
- What makes it so good? Is it really that great?
- The duality between representations and functions. A (linear) function can be written as a matrix. __Q__ For what other classes of function can we find dual representations?
- What alternatives are there to representing information that rival linear algebra? Other data structures, trees, graphs, !??
- in some representations, matmul ends up capturing another operation in the original representation. other times, the arguments capture the operations.

<!--
- could talk about "Concrete models and empirical evaluations for the categorical compositional distributional model of meaning". -->
