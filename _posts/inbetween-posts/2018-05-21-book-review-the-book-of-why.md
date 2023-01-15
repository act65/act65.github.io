---
title: "The book of why"
date: "2018-05-21"
coverImage: "why.jpg"
layout: post
subtitle: A couple of notes
---

![]({{site.baseurl}}/images/{{page.coverImage}})

Pretty much, I need to read the book again. There were a couple of parts I just pushed through. As a first pass here are some things I picked out as being interesting.

### Why causal models?

- They provide a nice representation that allows us to ask many different questions. A kind if transfer of knowledge between experiments, and queries.
- The assumptions made are clear. Graphs are intuitive.
- Allow us to make strong inferences from data.

### Inferring the causal graph

A recurring question I had was: but how do we know our causal model is correct? and what guarantees on inference are there if it is mostly correct, except for a couple of mistakes?

I want to know how to falsify a proposed graph. Which experiments/queries/estimands can I use? Which ones are the cheapest?

It seems interesting to note that we use all sorts of heuristics to help us infer a causal graph. Temporal and spatial proximity, simplicity, egocentric biases, ...

### Skeptical

I thought I was skeptical of scientific research already, but this takes me to a whole new level. The examples Judea gave highlight new ways (at least to me) that we can fool ourselves.

- Simpsons paradox was ... Depending on your causal model, the data will support either conclusion.
- Confounder on an indirect mediator
- ...

### Calculus

How does all of this relate to calculus?

If two variables correlate then that means we can fit a linear model to them. This is pretty much the definition of a derivative, the slope of a linear approximation at x. So when we ask if two variables are independent we are asking if their gradient w.r.t each other is zero. Similarly, with direct/indirect mediation, we are doing a sensitivity analysis. If y = g(x, z), z = f(x), then we want to know dy/dx and dy/dfz (partial derivatives).

And how do counterfactuals relate to finite differences? Imagine a world where ... counterfactual = f(x=1) - f(x=0). Which, in this case, IS a finite difference!

I am interested in exploring these connections further.

### Automated science

I love the idea of a robot systematically trying to understand the world. Conjuring hypotheses and designing experiments.

- How can agents use the do operator to collect data about their environments? (aka active learning)
- How can agents use models of their environments to achieve more efficient learning through counterfactuals? (aka model based learning)

### Questions and thoughts

I got lost in a few places. I plan on working through the math/details of;

- simple examples
- non linear causal models and 'interaction'
- the back and front door adjustments
- sufficient and necessary...
- natural and controlled effect
- how causes from two nodes combine to produce the caused node.

So, pretty much everything... Next goal is to write a tutorial on these.

Other thoughts

- I am still not sure of what I think about Judea's solution to uncertainty in causal models: add noise.
- Judea made a comment about how information about a variable that cannot be measured can leak through controlled proxies. Want to look into this.
