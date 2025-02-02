---
layout: post
title: Requests for research
subtitle: More ideas
permalink: /requests-for-research/02
categories: 
  - "research"
---

To stay sane I needed to write down some of the _actionable_ ideas that occur to me.
Otherwise I have the tendency to hoard them.
So, these are the questions I am not going to answer (argh it hurts!).
They appear to be perfectly good research directions, but "you need to focus" (says pretty much everyone I meet).

# Requests for research

_(the number of stars reflects how open the problem is: 1 star means little room for interpretation, 3 stars mean that there are some complex choices to be made)_

&#9734; __The effect of the positional embeddings__
Positional embedding must be added to the inputs of a transformer as transformers are permutation invariant. How much of the transformer's performance is due to the positional embeddings? 
What if we build a convolutional network and add positional embeddings to the inputs?

&#9734; __Does machine unlearning increase plasticity?__
[Plasticity](https://arxiv.org/abs/2303.01486) is a measure of the ability of a NN to change its predictions in response to new information. Does [Machine unlearning](https://arxiv.org/abs/1912.03817) increase the plasticity of a model?
Broader question: By removing knowledge from a model, can we increase its ability to learn new things?

&#9734; __In-context learning via fine-tuning__
In-context learning is a remarkable ability that some large models have. However, as the context grows, the model's ability to learn new things decreases (it this true?) and it's ability to remember and stay coherent decreases. 
Rather 