---
title: "Inference via interference"
date: "2018-08-28"
coverImage: "50336420-9c31-4ced-9c99-f3c114395f96-640-white-matter-fibers.jpg"
layout: post
subtitle: Learning by controlling the propagation speed of signals.
---

![]({{site.baseurl}}/images/{{page.coverImage}})

Myelin makes up 50% of the brains mass. This is a large investment for us to make! Pair this with the fact that humans are one of the few animals that have heavily myelinated brains, and it leads to the conclusion that it must have some important function!?

Myelin is used to insulate axons which increases the conduction speed at which a spike travels. But what if myelin has another function?

**Question:** Can myelin's ability to change the speed of information propagation be used to learn arbitrary patterns?

_Imagine: a fixed connectome (like a reservoir net) that can change the relative spike timing between neurons, by adding (or removing) myelin. If many spikes arrive to a target neuron at the same time they will likely activate (or deactivate) the target neuron. Instead, if we changed the relative timing so that the spikes arrive in a distributed in time, then the neuron will be harder to activate (for each individual) (bc decay of potential over time). Thus by altering the relative timing of spikes we can strategically interfere (constructively or destructively) travelling information._

**More Questions**: What is the representational power of adaptive timing? How does its representational power scale with; the size of a network, the number of possible delays, ... Does inhibition give something extra? Does it only work with large networks?

Finally, what is the relationship between myelination and travelling waves? A travelling wave is the synchronous activation of a set of local (in time and space) neurons. Yet waves can be constructively and destructively interfered. Thus, ... How are waves propagated across neural networks and how can myelin control this? Is the ability to control waves equivalent to being about to control activation threshold of a neuron?

In summary, the key questions are;

- how can myelination control the dynamics of a non-linear network?
- how can the dynamics of a non-linear network be used for learning?
