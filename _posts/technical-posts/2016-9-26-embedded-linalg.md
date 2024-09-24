---
layout: post
title: Representations within linear algebra
subtitle: We can use linear algebra to represent; linear operators, algebras, computations, symmetry and more.
---

Linear algebra is a powerful language! It turns out you can do some strange and fun things with it.
Let's explore using linear algebra to represent;

- [linear operators](#linear-operators) (differentiation and integration, matrix multiplication, the determinant, convolution, the laplacian)
- [algebra](#algebras) (dual numbers, complex numbers, and more)
- [computation](#computation) (logic, quantum computation)
- [symmetry groups](#symmetry-groups) (discrete, continuous)

<!-- 
this blog is just a collection of fun cases of linear algebra.
 -->

## Linear algebra

Linear functions can be written as arrays.\
Linear functions can be applied to arrays.

This representational duality between operator and operand reminds me of the duality between data and program in Turing's ideas of computation.
This duality is what we will explore in this blog.
<!-- mainly we consider writing operands as matrices.
what about viewing data / vectors as operators?
 -->

For example, we can have a map that tells us how to pair the integers $[0,1,2,3,4]$ with the integers $[0,1,2,3,4]$.

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

Matrix multiplication is also a linear operator. Well, technically it's a bilinear operator. But that's just a linear operator that takes two arguments. We can represent it as a 3 dimensional tensor.

$$
\begin{align*}
C_{ij} &= \sum_k A_{ik}B_{kj} \\
C_{ij} &= \sum_k T^{MMT}_{ijk} A_{ik}B_{kj} \\
\end{align*}
$$

> The matrix multiplication tensor
https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4

<script src="https://gist.github.com/act65/f956cc1ce73aca4fe435f225f8970ac4.js"></script>

Because matrix multiplication can be represented as the MMT, we can treat is as an operand, and do / ask seemingly strange things like;

- What is MMT $\cdot$ MMT?
- what is $\text{det}(MMT)$?
- what is the rank of the matrix $MMT$? (incidentally, the rank tells us how many multiplications are required to compute the multiplication of two matrices if size $n \times n$)

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
\end{bmatrix} C +
\begin{bmatrix}
0 & 0 & -1 \\
0 & -1 & 0 \\
-1 & 0 & 0 \\
\end{bmatrix} C +
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & -1 \\
\end{bmatrix} C +
\begin{bmatrix}
-1 & 0 & 0 \\
0 & 0 & -1 \\
0 & -1 & 0 \\
\end{bmatrix} C
\end{align}
$$

We could write the determinant as a tensor, $D$, which contains the 6 matrices written above.

$$
D = \sum_i \text{DET}^n_{i} C
$$

Really, this $\text{DET}^n$ is a tensor containing all possible permutation matrices $C$ (of size nxn).

<!-- Can we recursively apply the determinant operator?

https://en.wikipedia.org/wiki/Laplace_expansion -->

### Convolution

Convolution is a linear operator.

$$
\begin{align}
f \ast g &= \sum_{i=0}^{n-1} f[i]g[n-i] \\
\end{align}
$$

We can represent the convolution as a matrix.

$$
\begin{align}
f \ast g &= \begin{bmatrix}
f[0] & f[1] & f[2] & f[3] & f[4] \\
f[1] & f[2] & f[3] & f[4] & f[0] \\
f[2] & f[3] & f[4] & f[0] & f[1] \\
f[3] & f[4] & f[0] & f[1] & f[2] \\
f[4] & f[0] & f[1] & f[2] & f[3] \\
\end{bmatrix}
\begin{bmatrix}
g[0] \\
g[1] \\
g[2] \\
g[3] \\
g[4] \\
\end{bmatrix} \\
\end{align}
$$

Calculating a convolution this way is possible, but inefficient. 
Treating the convolution operator as a matrix, it can be decomposed into factors, where $D$ is a diagonal matrix of the DFT of the convolution kernel, $P$ is a permutation matrix, and $F$ is the DFT matrix.

$$
\begin{align}
F_{2n} = \begin{bmatrix}
I & D \\
D & I \\
\end{bmatrix}
\begin{bmatrix}
F_n & 0 \\
0 & F_n \\
\end{bmatrix}
P
\end{align}
$$

### The laplacian operator

The laplacian operator is a sum of second derivatives.
It is used in the heat equation, wave equation, and laplace's equation.

$$
\begin{align}
\Delta &= \nabla \cdot \nabla \\
&= \sum \frac{\partial^2}{\partial x_i^2}
\end{align}
$$

$$
\begin{align}
\Delta x &= \begin{bmatrix}
-4 & 1 & 0 & 0 & 1 \\
1 & -4 & 1 & 0 & 0 \\
0 & 1 & -4 & 1 & 0 \\
0 & 0 & 1 & -4 & 1 \\
1 & 0 & 0 & 1 & -4 \\
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5 \\
\end{bmatrix} \\
\end{align}
$$

<!-- 
Note, the Laplacian matrix is heavily used in graph signal processing. -->

## Algebras

An algebra is a set containing a set of elements, and rules for combining them $\{A, +, \times\}$.
For example, the real numbers, $\mathbb R$, equipped with the rules, addition and multiplication, $\{ \mathbb R, +, \times \}$.

##### Dual numbers

> the dual numbers extend the real numbers by adjoining one new element $\epsilon$ with the property $\epsilon^2 = 0$.

For example,

$$
\begin{align*}
a + c &\downarrow \\
(a + b\epsilon) + (c + d\epsilon) &= a + c + (b + d)\epsilon \\
\\
a \times c &\downarrow \\
(a + b\epsilon)(c + d\epsilon) &= ac + ad\epsilon + bc\epsilon + bd\epsilon^2\\
&= ac + (ad + bc)\epsilon \\
\end{align*} \\
$$

We can represent the dual numbers as a 2x2 matrix.

$$
1 \equiv \begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix},\quad
\epsilon \equiv \begin{bmatrix}
0 & 1 \\
0 & 0 \\
\end{bmatrix} \\
a + b\epsilon \rightarrow
\begin{bmatrix}
a & b \\
0 & a \\
\end{bmatrix} \\
$$


$$
\begin{align*}
(a + b\epsilon)(c + d\epsilon) &=
\begin{bmatrix}
  a & b \\
  0 & a \\
\end{bmatrix}
\begin{bmatrix}
  c & d \\
  0 & c \\
\end{bmatrix} \\
&=
\begin{bmatrix}
  ac & ad + bc \\
  0 & ac \\
\end{bmatrix} \\
&=  ac + (ad + bc)\epsilon
\end{align*} \\
$$

A cool property of dual numbers is that they track the derivative of the composed variables.

Let's work through an example. Let $y = x^2 + 3x + 5$. 
With derivative $\frac{dy}{dx} = 2x + 3$.

$$
\begin{align}
y &= x^2 + 3x + 5 \\
y(x + \epsilon) &= (x + \epsilon)^2 + 3(x + \epsilon) + 5 \\
&= x^2 + 2x\epsilon + \epsilon^2 + 3x + 3\epsilon + 5 \\
&= x^2 + 3x + 5 + (2x + 3)\epsilon \\
\end{align}
$$



$$
\begin{align}
y &= x^2 + 3x + 5 \\
y &= 
\begin{bmatrix}
  x & 1 \\
  0 & x \\
\end{bmatrix}
\begin{bmatrix}
  x & 1 \\
  0 & x \\
\end{bmatrix}
+ 3\begin{bmatrix}
  x & 1 \\
  0 & x \\
\end{bmatrix}
+ 5\begin{bmatrix}
  1 & 0 \\
  0 & 1 \\
\end{bmatrix} \\
&= \begin{bmatrix}
  x^2 & 2x \\
  0 & x^2 \\
\end{bmatrix}
+ \begin{bmatrix}
  3x & 3 \\
  0 & 3x \\
\end{bmatrix}
+ \begin{bmatrix}
  5 & 0 \\
  0 & 5 \\
\end{bmatrix} \\
&= (x^2 + 2x\epsilon) + (3x + 3\epsilon) + 5 \\
&= x^2 + 3x + 5 + (2x + 3)\epsilon \\
\end{align}
$$


<side>Homework: Show that the dual numbers capture the sum, product and chain rule of derivatives.</side>

##### Complex numbers

> the complex numbers extend the real numbers by adjoining one new element $i$ with the property $i^2 = -1$.

For example, instead of $a \times c$, we have;

$$
\begin{align}
(a + b i)(c + d i) &= ac + adi + bci - bd \\
&= ac - bd + (ad + bc)i \\
\end{align}
$$

We can represent the complex numbers as a 2x2 matrix.

$$
\begin{align}
1 &\equiv \begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix},\quad
i \equiv \begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix} \\
\end{align}
$$

$$
\begin{align}
\begin{bmatrix}
a & -b \\
b & a \\
\end{bmatrix}
\begin{bmatrix}
c & -d \\
d & c \\
\end{bmatrix} &=
\begin{bmatrix}
ac - bd &  -(ad + bc)\\
ad + bc & ac - bd \\
\end{bmatrix}\\
&= (ac - bd)\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix} +
(ad + bc)\begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix} \\
&= ac - bd + (ad + bc)i \\
\end{align}
$$

<!-- Note: $\mathcal R(i)$ is skew-symmetric.

__Q__: How can we see that multiplying by an imaginary number rotates the vector? -->

#### Quarternions

Next, we have the quarternions, $\mathbb H$, which extend the reals numbers by adjoining three new elements $i, j, k$ with the properties $i^2 = j^2 = k^2 = ijk = -1$, and $ij = k$.

We can represent the quarternions using 4x4 matrices.

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
Q &= a + bi + cj + dk \\
&= \begin{bmatrix}
a & -b & -c & -d \\
b & a & -d & c \\
c & d & a & -b \\
d & -c & b & a \\
\end{bmatrix} \\
\end{align}
$$


<side>Feel free to verify that (say) $k \cdot j = -i$</side>

The really cool part is that we can construct the quarternions, $\mathbb Q$, from a basis of 2x2 matrices.

$$
\begin{align}
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix}, \quad
\begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix}, \quad
\begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}, \quad
\begin{bmatrix}
1 & 0 \\
0 & -1 \\
\end{bmatrix} \\
\end{align}
$$


$$
\begin{align}
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix}
\otimes
\begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix} &=
\begin{bmatrix}
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix} =i\\
\end{align}
$$

$$
\begin{align}
\begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix}
\otimes
\begin{bmatrix}
1 & 0 \\
0 & -1 \\
\end{bmatrix} &=
\begin{bmatrix}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
\end{bmatrix} = j \\
\end{align}
$$

$$
\begin{align}
\begin{bmatrix}
0 & -1 \\
1 & 0 \\
\end{bmatrix}
\otimes
\begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix} &=
\begin{bmatrix}
0 & 0 & 0 & -1 \\
0 & 0 & -1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix} = k \\
\end{align}
$$

This hints that there is some deeper structure to the quarternions.
We can do a block decomposition of the quarternions into 2x2 matrices

$$
\begin{align}
Q = \begin{bmatrix}
\begin{bmatrix}
a & -b \\
b & a \\
\end{bmatrix} &
\begin{bmatrix}
-c & -d \\
-d & c \\
\end{bmatrix} \\
\begin{bmatrix}
c & d \\
d & -c \\
\end{bmatrix} &
\begin{bmatrix}
a & -b \\
b & a \\
\end{bmatrix} \\
\end{bmatrix} = 
\begin{bmatrix}
\alpha & -\beta \\
\beta & \alpha \\
\end{bmatrix}
\end{align}
$$

and we see that the quarternions are really two layers of nested complex numbers.


<!-- More info [here](https://groupprops.subwiki.org/wiki/Linear_representation_theory_of_quaternion_group) -->

<!-- https://math.stackexchange.com/questions/1916870/what-is-the-relation-between-quaternions-and-imaginary-numbers -->
<!-- The connection between SO(3) and SU (2) -->

<!-- https://core.ac.uk/download/pdf/82668219.pdf -->

<!-- <side>Homework: Show that the pattern continues for octonions.</side> -->



<!-- Restrictions on the algebras by using the linear representation?

- must be associative
- must be closed under multiplication
- must be closed under addition
- must have an identity element
- must have inverses
- must be distributive
- must be commutative -->

## Computation
### Logic

We have two bits, $x,y$. We can encode the 4 possible arangements $00, 01, 10, 11$ in a four dimensional space, $\mathbb \{0,1\}^4$ using a one-hot encoding.
Where $00 \rightarrow [1, 0, 0, 0]^T$, $01 \rightarrow [0, 1, 0, 0]^T$, $10 \rightarrow [0, 0, 1, 0]^T$, $11 \rightarrow [0, 0, 0, 1]^T$.

Now we require all operations to be unitary and all vectors to be within the basis, $a_0, ..., a_n$.

$$
\begin{align}
NOT \equiv
\begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}
\end{align}
$$

Not only applies to a single bit. To apply NOT to the first bit of our 2 bit system, we can use the kronecker product.

$$
\begin{align}
NOT \otimes I &= 
\begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}
\otimes
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix} \\
&=
\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
\end{bmatrix}
\end{align}
$$

Binary operations can be represented as 4x4 matrices. For example, the CNOT gate (which we can use to implement XOR) is represented as;

$$
\begin{align}
CNOT &= 
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0\end{bmatrix}
\end{align}
$$

*** 

Note, this implementation of logic requires the use of reversible gates. 
This is because we require the operation to be unitary, and thus invertible.
No information can be lost.

### Quantum computation

Quantum computation extends this representation of logic to allow for superposition and entanglement.
We allow for complex numbers in our representation, such that $\mid a \mid = 1$ (the Born rule).

For example, we can now have a state;

$$
\begin{align}
\begin{bmatrix}
\frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} \\
\end{bmatrix}
\end{align}
$$

Which represents a superposition of the states $0$ and $1$ with equal probability, $=\frac{1}{2}$.

For example, the Hadamard gate (used to create superposition) is represented as;

$$
\begin{align}
H \equiv
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix}
\end{align}
$$

<!-- these gates also form a basis? / algebra!? are they complete? -->

## Symmetry groups

Finally we arrive at so called "representation theory".

A group is a set of elements, $G$ and a binary operation, $\cdot$, that satisfies the following properties;

- closure
- associativity
- identity element
- invertibility

For example, a finite cyclic group, say $Z_5$, is a group of 5 elements, $\{0, 1, 2, 3, 4 \}$ with the operation of addition modulo 5.
Therefore, $3 \cdot 2 = 0$. $0$ is the identity element. We can write the generator of the group as a 5x5 matrix.

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


Or the symmetric group in 3 dimensions, $S_3$, which is the group of all permutations of 3 elements, $\{1, 2, 3\}$.
We can represent the group as a set of 3x3 permutation matrices.

$$
\begin{align}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix},\quad
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1 \\
\end{bmatrix},\quad
\begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
\end{bmatrix},\dots
\end{align}
$$

If we move to continuous groups, we can represent the group of rotations in 2 dimensions, $SO(2)$ (aka the orthogonal group in two dimensions), as a 2x2 matrix.

$$
\begin{align}
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) \\
\sin(\theta) & \cos(\theta) \\
\end{bmatrix}
\end{align}
$$

Or the group of rotations, scales and shifts in 2 dimensions, $GL(2)$ (aka the general linear group in two dimensions), as arbitrary 2x2 matrices.

<!-- https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group -->