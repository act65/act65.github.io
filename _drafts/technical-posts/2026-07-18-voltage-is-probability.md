---
layout: post
title: Voltage is a Probability
subtitle: A drunkard, a resistor network, a soap film, and a differential equation are the same object
categories:
  - play
---

Draw a graph — dots joined by lines. Now consider four completely different questions about it.

1. **A drunkard** starts at a node and staggers to a random neighbour each step. Starting from node $x$, what's the chance he reaches the pub (node $A$) before home (node $B$)?
2. **An electrician** wires a 1-volt battery across $A$ and $B$, a resistor on every edge. What's the voltage at node $x$?
3. **A physicist** holds $A$ at one temperature and $B$ at another and lets heat settle. What's the steady temperature at $x$?
4. **A mathematician** solves the discrete Laplace equation on the graph with those boundary values. What's the solution at $x$?

These look like four subjects. They are four names for **one number**. The voltage *is* the probability *is* the temperature *is* the harmonic function — not approximately, not by analogy, but identically. This is the most beautiful unification I know that you can prove on the back of an envelope, and it's the subject of Doyle and Snell's little classic *Random Walks and Electric Networks*.

### The one property: being your own average

A function $u$ on the graph is **harmonic** at a node if its value there equals the average of its values at the neighbours (weighted, if edges differ):

$$u(x) = \frac{1}{\deg(x)} \sum_{y \sim x} u(y).$$

That's the discrete Laplace equation, $\Delta u = 0$. Fix the values on a boundary (here, $u(A)$ and $u(B)$) and there is exactly *one* harmonic function on the interior with those boundary values. **Uniqueness is the whole engine**: any two of our four questions, once you show each is harmonic with the same boundary values, must give the same answer, because there's only one function to give.

So watch all four turn out to be their own average.

**The electrician.** Kirchhoff's current law says the net current into a node is zero; Ohm's law says current on an edge is the voltage difference over the resistance. Put them together and the voltage at each internal node is forced to be the (conductance-weighted) average of its neighbours' voltages. Voltage is harmonic. It equals 1 at $A$, 0 at $B$.

**The drunkard.** Condition on his first step. From $x$ he goes to a uniformly random neighbour $y$, and from there his chance of reaching $A$ first is $p(y)$. So

$$p(x) = \frac{1}{\deg(x)}\sum_{y\sim x} p(y)$$

— the probability of hitting $A$ before $B$ is *also* harmonic, and it's 1 at $A$ (already there) and 0 at $B$. Same equation, same boundary values.

By uniqueness, they're the same function. **The voltage at $x$, with $A$ at one volt and $B$ at zero, is exactly the probability that a random walk from $x$ reaches $A$ before $B$.** A voltmeter is a probability meter. Heat flow and the Laplace-equation solution join by the identical argument.

> This is not a party trick you do once; it's a machine. Any question you can phrase as "hitting probability of a random walk" you can *answer* by building a circuit and reading a voltage — and any circuit fact (series and parallel resistors, symmetry) becomes a theorem about random walks. Two toolkits, fused, each covering the other's blind spots.

### Cashing it in: why a drunk man gets home but a drunk bird might not

The fused picture pays a famous dividend. Push $B$ off to infinity and ask: will the walker *ever* get home, or can he wander off forever? In circuit language that's asking whether the **effective resistance from a node to infinity** is finite or infinite. And there's a clean fact — more resistance means less escaping current means the walker keeps coming back.

- On the 2D grid $\mathbb{Z}^2$, the effective resistance to infinity is **infinite**. The walk is **recurrent**: with probability 1 he returns to the start, over and over, forever.
- On the 3D grid $\mathbb{Z}^3$, the resistance to infinity is **finite**. The walk is **transient**: there's a positive chance he wanders off and never comes back.

This is Pólya's theorem (1921), and the slick proof is pure circuit-shrinking (Rayleigh's monotonicity: gluing nodes or cutting edges only moves resistance one way). Shizuo Kakutani's summary is unbeatable: *"a drunk man will find his way home, but a drunk bird may get lost forever."* The dimensionality of space decides whether you can go home again — proved with Ohm's law.

There's more in the same vein: the **commute time** between two nodes (there and back) equals $2m \cdot R_{\text{eff}}$, where $m$ counts the edges and $R_{\text{eff}}$ is the effective resistance between them. A hard question about the timing of a stochastic process is answered by measuring a resistance.

### Why it's one object, really

Underneath all four is a single operator: the graph **Laplacian** $L = D - A$ (degrees minus adjacencies), the discrete cousin of the $\nabla^2$ that runs heat, waves, and potentials in physics — the same operator I've [pulled apart via volumes and determinants before]({{ site.baseurl }}). Harmonic means "in the kernel of $L$ on the interior." Every one of our four questions is *solve $Lu = 0$ with these boundary values*, and they differ only in the story they tell about the answer.

And it has a variational soul, which I can't resist flagging. **Thomson's principle**: of all the ways current *could* flow from $A$ to $B$, the real one is the one that **minimises the energy dissipated** — the electrician's world is quietly solving a [calculus-of-variations]({{ site.baseurl }}) problem, and the harmonic function is its minimiser. Nature routes the current, settles the heat, and steers the drunkard by minimising the same energy, three times over, without knowing it's doing the same sum thrice.

That's the thing I keep chasing on this blog, in its cleanest form: not four subjects that resemble each other, but one operator that four subjects are each a dialect of. Learn to read a resistor network and you've learned to read a random walk, a heat equation, and a Laplace solver — because they were never really different.
