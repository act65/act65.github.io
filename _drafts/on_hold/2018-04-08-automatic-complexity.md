---
layout: post
title: Automatic computational complexity
---

__TODO__ Need to understand AD better.

> Can we automatically bound the complexity of algorithms?

Trivially, yes. We can just time the algorithm, we can track the amount of memory it used, ... But; that requires input from humans, and, it is not efficient. Can we efficiently automate this process?

Want to make it symbolic!!

## Desiderdata

Knowing the absolute time and memory usage of an algorithm is nice [memory profiler](https://pypi.org/project/memory_profiler/). But what I am really interested in is how do these resources scale.
Want a model of the computation so we can ask counterfactual queries. What if I had twice as much data/memory/...?


What would automatic computational complexity do and be?

* __Accurate__:
  * Want the lowest upper bound. That might take some work to find!?
* __Understandable__:
  Want the bound to be expressed in an 'intuitive' way (w.r.t inputs and ?).
* __Efficient__:
  * must be more efficient than just running the program at various `n` (which would be the baseline). Is there any existing work on this?
  * must have low overhead so it can passively exist in the background.
* __General__:
  * works on arbitrary programs
* ?

__TODO__ maybe python is the wrong language to work with? we have abstracted away from the basis calls. Memory indexes, processes, ...
__TODO__ problem is how different compilers deal with operations... But that is why we are dealing with bounds!?

```python
import bound
from bound import complexity_measures as cplx

def sort_list(length):
  unsorted_list = random_list(length)
  sorted_list = []

  with bound.scope():
    for _ in range(length):
      x = min(unsorted_list)
      sorted_list.append(x)
      unsorted_list.remove(x)

    return sorted_list

>>> b = bound.upper(sort_list, measure=cplx.memory)
>>> print(b)
"O(n)"

>>> b = bound.upper(sort_list, measure=cplx.time)
>>> print(b)
"O(n**2)"
```

## Computational complexity

Intro/motivation and Worked examples

What is it complexity theorists do?
Some examples, calculated via proof, and empirically backed up.
Why do we care about computational complexity?

## Implementation

I imagine it would work similar to how automatic differentiation (AD) works: derivatives, chain rule, checkpointing, reverse-mode, segmentation, ?.

At a high level, AD works by defining a derivative for every operation. A computational graph of a function can then be transformed into a graph of the derivative of the fn using the defined gradient for each operation and using the sum, product and chain rules ...

I imagine that we could define a set of basis operations, where each one has its complexity defined (memory, time, parallel, energy, latency, ...). As these basis ops are composed we can propagate these complexities via a chain rule.

### Differential computational complexity

We want to know the CC of $f(n)$ for other arbitrary values of $n$.
For example, want to know how the memory usage changes with different inputs, $\frac{d\; \text{memory}}{d\;\text{inputs}}$.

Knowing $\frac{d\; \text{memory}}{d\;\text{inputs}}$ would allow us to estimate the memory complexity at other n.

***
Actually, I would be pretty happy with;

$\text{memory} = g_f(p), p = h(\text{inputs})$ (the memory complexity of $f$ as a function of some property $p$ of the inputs, e.g. their size, location, ...).

Or, $\text{memory} = g_f(p), p = h(\text{outputs})$ (the memory complexity of $f$ as a function of some property $p$ of the outputs, e.g. the error, latency, ...).

That seems closer to what we want?
***

A similar problem occurs in calculus. Want to know other values of $y$ where $y = f(x)$.

So we want to know;

$$
\begin{align}
y = f(n) \\
\frac{d \mathcal R_m}{dn} \tag{change in memory wrt n}\\
\end{align}
$$

Two ways to frame!? $f(n)$. Or $f(x)$, where we also have some measure $g(x) = n$ that gives us the complexty of the input. (length, number of bits, ...?)

#### Chain rule

Chain rule takes nested function composition and gives multiplication. This is a property of the linearity of the gradients.

<side>
AD is efficient because ? (is it? only reverse is - memory - efficient)
Reverse AD is efficient because ?
</side>

Dont have a chain rule because they are not linear?!?

The key is the memoization?!? The reuse of

#### Reverse-AB (automatic bounding)

Question. Does the complexity of one hyperparameters tells us something about others!?

Can we come up with some sort of chain rule here?
The theorem we are after is something like

__Conjecture__: These exists a 'chain rule' for resource use.

$$
\begin{align}
\mathcal R &:= \{ \text{Memory}, \text{Time}, ... \} \\
r \in \mathcal R \\
if \quad h &= g \circ f\\
\mathcal B_{r}(g) \circ \mathcal B_{r}(f) &= \mathcal B_{r}(g \circ f) \tag{!!!} \\
\end{align}
$$



Examples

$$
\begin{align}
f(n) &= m \\
g(m) &= z \\
h(n) &= g \circ f \;\;(n) \tag{chained functions} \\
\\
\mathcal B_{mem}(f) &= O(log(n)) \tag{CC of f}\\
\mathcal B_{mem}(g) &= O(m^2) \tag{CC of g}\\
&= O(log(n)^2) \\
\end{align}
$$
***
$$
\begin{align}
m_1 &= f_1(n_1) \\
m_2 &= f_2(n_2) \\
z &= g(m_1 + m_2) \\
\mathcal B_{mem}(f_1) &= O(log(n_1)) \\
\mathcal B_{mem}(f_2) &= O(1) \\
\mathcal B_{mem}(g) &= O(m^2) \\
\\
\mathcal B_{mem}(g \circ f_1) &= \\
&= O(log(n)^2) \\
\mathcal B_{mem}(g \circ f_2) &= O(1) \\
\end{align}
$$
$g \circ f_1$ doesnt work here!? it is more like $\mathcal B_{mem}(z \leftarrow n_1), z = g(m_1, m_2)$ the complexity of $z$ w.r.t $n_1$.

## How accurate?

But what about the compiler?! Different optimisations are possible depending on data type, size, ...? So the complexity changes based on how various hardware is targeted etc...

Worst case versus expected case versus best case versus !? case.

Extra compute could be spent to find tight(er) bounds!? Sounding like we would need an automated proof assistant?

## Use case?

If we have, say, 10 hyperparameters, we might care about how our algorithms scales each of them and with each other?!

Doesnt actually need to run the algorithm, only construct the computation graph and then !?!?

## Minimal proof of concept

Lets make some ops with their complexity defined and compose them together.

```python
class Operation(object):
  def __call__(self, *args, **kwargs):
    raise NotImplementedError

  @static_method
  def memory_complexity(self):
    """
    Do I want this to return a general fn for the complexity,
    or to simply return the value of this ops complexity!?
    """
    raise NotImplementedError

class Square(Operation):
  def __call__(self, x):
    self.x = x
    return np.pow(x, 2)

  @static_method
    def memory_complexity(self):
      return len(self.x)  # or lambda n: n
```

## Future work

* Use this to fill out Scott Aaronson's zoo of algols.
* What about using this to help you make tradeoffs? Needs access to alternatives?!?
* What about sample, accuracy, energy, parallel, latency, reversible, ... complexity?
