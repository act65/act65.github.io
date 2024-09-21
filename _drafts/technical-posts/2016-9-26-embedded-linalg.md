---
layout: post
title: Representations within linear algebra
subtitle: We can use linear algebra to represent; linear operators, algebras, computations, symmetry and more.
---

Linear algebra and arrays combine to give us a powerful language. Here we explore using linear algebra to represent;

- [linear operators](#linear-operators) (differentiation and integration, matrix multiplication, the determinant, convolution, the laplacian)
- [algebra](#algebras) (dual numbers, complex numbers, and more)
- [computation](#computation) (logic, automata, quantum computation)
- [symmetry groups](#symmetry-groups) (discrete, continuious)
- and more.

## Linear operators

Linear functions can be written as arrays.
Linear functions can be applied to arrays.

<!-- what is an array
- elements must be of the same type
- 
 -->

An operator is a mapping from one space to another. For example, we can have a map that tells us how to pair the integers $[0,1,2,3,4]$ with the integers $[0,1,2,3,4]$.

We start by representing the integers as 'one-hot' vectors. For example, the integer 2 is represented as $[0, 0, 1, 0, 0]^T$ and the integer 4 is represented as $[0, 0, 0, 0, 1]^T$.

We can represent an operator as a matrix. Consider the mapping $0\to1, 1\to2, 2\to3, 3\to4, 4\to0$. We can write this as;

$$
\begin{align}
\begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
\end{align}
$$

This representational duality between operator and operand reminds me of the duality between data and program in Turing's ideas of computation.

### Polynomial functions

<!-- But are these more that just nice mathematical curiosities? Why is this useful or important? -->

Let's represent a polynomial as an infinite array $a \in  {\mathbb R}^{\infty}$. Where $a_i$ is the coefficient for $x^i$. Thus $a(x) = [0, 5, 3, 0, 1, \dots]^T$ represents

$$
0\cdot x^0 + 5\cdot x^1 + 3\cdot x^2 + 0\cdot x^3 + 1\cdot x^4 \\
a(x) = x^4 + 3\cdot x^2 + 5\cdot x
$$

#### A differentiation operator for polynomials

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

And we can differentiate via matrix multiplying $\frac{d}{dx}a(x) = \mathcal D \cdot a(x)$.
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

What about;

- negative powers of $x$?
- fractional powers of $x$?

#### An integration operator for polynomials

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

#### Matrix multiplication

Matrix multiplication is also a linear operator. Well, technically it's a bilinear operator. But that's just a linear operator that takes two arguments. We can represent it as a 3D tensor.

$$
\begin{align*}
C = 
C_{ij} = \sum_k A_{ik}B_{kj} \\
C_{ij} = \sum_k T^{MMT}_{ijk} A_{ik}B_{kj} \\
\end{align*}
$$

> The matrix multiplication tensor
https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4

<script src="https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4.js"></script>

Because matrix multiplication can be represented as the MMT, we can treat is as an operand, and do / ask seemingly strange things like;

- What is MMT $\cdot$ MMT?
- what is $\text{det}(MMT)$?
- what is the rank of the matrix $MMT$? (incidentally, the rank tells us how many multiplications are required to compute the multiplication of two matrices if size $n \times n$)
- let's construct the matrix $MMT + D$ (where $D$ is the differentiation operator).

#### Determinant

The determinant is a linear operator. It can also be represented as a tensor.

<!-- \mid A \mid &= \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n A_{i,\sigma_i} \\ -->

$$
\begin{align}
\det \begin{bmatrix}
a&b\\
c&d\\
\end{bmatrix} &= ad-bc \\
&= \begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
a & b \\
c & d \\
\end{bmatrix}
- \begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
a & b \\
c & d \\
\end{bmatrix}
\end{align}
$$


$$
\begin{align}
\begin{bmatrix}
a&b&c\\
d&e&f\\
g&h&i\\
\end{bmatrix}&=aei+bfg+cdh-ceg-bdi-afh \\
&= \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix} C +
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0 \\
\end{bmatrix} C +
\begin{bmatrix}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
\end{bmatrix} C -
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
\end{bmatrix} C -
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1 \\
\end{bmatrix} C -
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 1 & 0 \\
\end{bmatrix} C
\end{align}
$$

We could write the determinant as a tensor, $D$, which contains the 6 matrices written above.

$$
D = \sum \text{DET}^n_{ij} C
$$

Really, this $\text{DET}^n$ is a tensor containing all possible permutations of the matrix $C$ (of size nxn).
(constrained to picking full rank matrices)

***

Can we recursively apply the determinant operator?
we have a 4x4 matrix, $M$ which we rewrite as a 2x2 matrix, $M'$, where each element is a 2x2 submatrix of $M$.

$$
\begin{align}
M &= \begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44} \\
\end{bmatrix} \\
M' &=
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{bmatrix} \\
b_{11} &= \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix} \\
\end{align}
$$

### Convolution

$$
\begin{bmatrix}
k_0 & k_1 & k_2 & 0 & 0 & 0 & 0 \\
0 & k_0 & k_1 & k_2 & 0 & 0 & 0 \\
0 & 0 & k_0 & k_1 & k_2 & 0 & 0 \\
0 & 0 & 0 & k_0 & k_1 & k_2 & 0 \\
0 & 0 & 0 & 0 & k_0 & k_1 & k_2 \\
\end{bmatrix}
$$

FFT, DFT

<!-- <script src="https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4.js"></script> -->

### The laplacian operator

The laplacian operator is a second derivative.

$$
\begin{align}
\Delta &= \nabla \cdot \nabla \\
&= \sum \frac{\partial^2}{\partial x_i^2}
\end{align}
$$

$$
\begin{align}
\mathcal L &= \begin{bmatrix}
0 & 1 & 0 & 0 & 0 \\
1 & -4 & 1 & 0 & 0 \\
0 & 1 & -4 & 1 & 0 \\
0 & 0 & 1 & -4 & 1 \\
0 & 0 & 0 & 1 & 0 \\
\end{bmatrix}
\end{align}
$$

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


## Computation
### Logic

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

### Seripinski triangle


### (quantum) computation

?

## Symmetry groups

Finally we arrive at so called "representation theory".
Symmetry groups are defined as sets of transformations that leave some property invariant. For example, the set of all rotations of a circle leave the circle invariant. The set of all 90 degree rotations of a square leave the square invariant.



***

Weird things like. Neural network architectures. fat.

<!-- - The duality between representations and functions. A (linear) function can be written as a matrix. __Q__ For what other classes of function can we find dual representations? -->