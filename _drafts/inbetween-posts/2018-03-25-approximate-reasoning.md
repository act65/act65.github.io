---
layout: post
title: Approximate reasoning with incomplete models
---

When reasoning, in some cases we might want to trade-off accuracy for other resources; latency, memory, time, ... What does this trade cost in (approximate) reasoning systems?

<side>These questions were inspired by how people tend to reason inconsistently, and I wondered what advantages our inconsistency might give</side>

> First let's get our heads around what I mean by reasoning.

# Reasoning

In the most abstract sense, I define reasoning as finding a path through a graph, from priors to posteriors, from ...?

- _Algebraically manipulating previously acquired knowledge in order to answer a new question_ [Bottou 2011](?)
- _Using a formal system to derive consequents from antecedents (ways of doing this are; deduction, induction, abduction)_
- ?


##### Knowledge bases

Let $K$ be a <u>relational knowledge base</u>, represented as a graph, $G(v, e)$. Now, imagine we want to get from $a\rightarrow b$ such that ($a,b \in V$). We need to find a path (a series of edges in, $e \in E$) that connect $a$ and $b$.

##### Arguments

Let $C$ be a set of concepts, and $R$ be a set of reasons that allow you to get from one concept to another, $r(x) = y: r\in R, x,y \in C$.

Now, imagine that we form an argument about why $b$ is true, based on the assumption of $a$. An argument is a chain of reason, $r \in R$, such that they connect $a, b$.

##### Transitional models

Let $M$ be a <u>model of state transitions</u> that takes a state, $s_t$ to the next state (possibly given some action, but for now we are just going to assume that is part of the state), $s_{t+1} = M(s_t)$. So a model explains the pair (a, b) if the model can be initialised in state $a$ ($s_0 = a$), and after some finite amounts of timesteps, the state either passes through $b$ or approaches it.

<side>TODO Are these really the same? Need to show more rigorously. What type of graph?</side>

<!-- For example AlphaGo. -->

## [Completeness](https://en.wikipedia.org/wiki/Completeness_(logic))

> The most simple example of a proof system that is {consistent} but not complete would be the one that has no inference rules at all! It proves nothing except whichever non-logical axioms your theory has, so in particular it doesn't prove anything that risks being false -- so it is {consistent}. But it is very much not complete. [Makholm on SE](https://math.stackexchange.com/questions/2256054/what-would-be-an-example-of-a-proof-system-being-sound-but-not-complete)

For example we have a knowledgebase where father/mother/child...?
Or ...

```python
Mary = true
Jasmine = true
Katsumoto = true

# not included
# true/false = is_mother(Mary, Katsumoto)  # meaning: is Mary Katsumoto's mother?
```



## [Consistency](https://en.wikipedia.org/wiki/Consistency)

<side>When computer scientists say consistent, they really mean coherence, but I will continue ...</side>

TODO Need a definition here

> What happens if we have multiple paths between $a$ and $b$?

People tend to be able to give multiple reasons for why the rain yesterday explains the prescence of a god. Or why the cute-boy-next-door's actions indicate that he likes you.

<side>The mistake we make is that we easily confuse related concepts, .</side>
For now, let's only condsider well defined reasoning. (meaning?)

* What does connectedness imply?
* What does it mean to be the shortest path? (it depends on the basis)

Does having two paths ($p_1, p_2$) from $a\rightarrow b$ imply that $p_1$ is equivalent to $p_2$?
If we have two models, $m_1$ and $m_2$ that explain (a, b), which one is right?

They are equivalent w.r.t the data we have, need to collect more data, use another measure to compare them, such as the `simplicity` of each model/path.

<side>This means $a$ may not imply $b$, but isn't that what we just showed by finding a path from $a\rightarrow b$?</side>
Given a path $a \rightarrow b$, what if we can use the database to find a path from $\neg a\rightarrow b$? How do we resolve this?

This property, __inconsistency__, is normally avoided in most reasoning systems [ref 1](?), [ref 2](2), ... A lot of time has been spent on this problem?

$$
\text{example of an inconsistent system} \\
a \rightarrow x \\
x \rightarrow c \\
a \rightarrow y \\
y \rightarrow \neg c \\
$$

How is this related to many-to-one versus one-to-many functions?
- a + b = 3 and a + b = 4 are inconsistent (there are no values of a, b that satisfy these equations. so inconsistency is equivalent to satisfiability?)
- but 4 + a = b and

Humans tend to have inconsistent beliefs. We will reason about why X implies Y and about how Y implies Z, but disagree that X implies Z. (TODO want a better example)
That example. If two people are rational and agree on the prior assumptions/axoims then they cannot disagree. But this requires them to ... Could take too long to make any useful decisions.

What I am curious about is; _can we trade consistency for other measures of efficiency?_


## Approximate reasoning

> __Q:__ What happens when the database is incomplete, our model is approximate, our argument is i natural language, ... We are required to trade-off accuracy for reduced latency, lower computation, ...?

<side>TODO Are these really the same? Need to show more rigorously.</side>
Incomplete database aka approximate reasoning aka reasoning with an imperfect model.

Consider some strategies for reducing the complexity (memory, latency, time, ...) of a reasoning system.
Some examples of instances where we might encounter/want incomplete models.

##### Online learning

Need to make predictions before a model has been learned. Maybe the model is too large to every be learned, ...

##### Factoring links into a model

Instead of storing all the links, we could generate them as required. This could cut down the memory requirements of large databases. The problem being that the number of possible links/edges scales with $\mathcal O (\mid V \mid^2)$. So if we have a thousand nodes, the maximum number of edges is a million (if we are talking about an undirected graph with a single edge type).

So instead of representing links as an array that we index $L[i, j]$, we could represent the links as a function $f(i, j)$ that generalises any patterns found in the links.

##### Sketched nodes

<side>Reducible: Inspired by reductionism. Reduce complexity into a small number of atomic units</side>
Rather than storing all $N$ nodes. Factorise them into a hierarchy of basis nodes and
Some may not be `reducible` into the basis, so must be memorised, for now.
Problem is that this hierarchy needs to be

This is a data structure that contains;
* Basis: $\mathcal B$ the set of basis nodes (need basis edges as well???)
* Generated: $\mathcal F$ the ordered set of functions that take the basis and produce new nodes. $f\in F: f(\mathcal B) \rightarrow V$
  * $C = \{\}$
* Memorised: $M = $
* $V = C \cup \mathcal B \cup M$

<side>TODO How does this help? I am not sure it does!? What does it buy us?!?</side>
Thus requiring ??? rather than ???.

##### High-level linkages.

<side>Inspired by chunking and variable rate coding.</side>
If a path $a\rightarrow b$ (of length $k$) is traversed many times then maybe it should be summarised as a single link, thus allowing $\mathcal O(1)$ steps to reason about the relationship between $a$ and $b$.

A path is more likely to be true if it is more specific. (aka not high level)
Specificity is measured by ???.
The length of the path?
How close the nodes visited are to being basis nodes.

##### Node-edge duality

Factorise the ???. You drink drinks, so we can compress this into a single concept. Drink, which captures the name of the drink (the noun -- node), and the act of drinking (the verb -- edge).

__TODO__ Need a toy model that is incomplete (aka approximate) and then ...

## The advantages of inconsistency

Now, the real question; (How) did each of these strategies sacrifice consistency for greater efficiency?

__Conjecture__: Inconsistency is a necessary result of attempting to reason with incomplete models.

Define incomplete models.



### A measure of consistency

<side>Ok, there must be some existing work on this? Non trivial in the cts domain...</side>
__Definition__: The coherence of a database is defined as the total number of contradictions it makes.


Desiderdata;

* If $A \rightarrow B$ then $\neg A \not \rightarrow B$ (aka a one to one mapping?)
* The a measure of consistency would give large values for


<side>How is this related to disentanglement?</side>
Let $h$ be some hidden space, and $D(h) = x$ be some decoder.

$$
C: D \rightarrow \mathbb R \\
c_i = \mathbb E_{z \sim \mathcal N} \parallel D(h_{i=1}+z)- D(h_{i=-1}+z) \parallel \\
C = ... \\
$$

Aka, $h_i$'s effect on  doesnt


So, we would want to maximise this?

$$
\mathop{argmax}_{\theta} \mathcal C(D_{\theta})
$$



***

When working with approximates.
Multiple reasons leading to the same conclusion should increase the plasubility?
