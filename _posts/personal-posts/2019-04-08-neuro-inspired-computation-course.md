---
title: "Neuro-inspired computation course"
categories: 
  - "experience"
coverImage: "ircn.png"
layout: post
subtitle: I visited IRCN.
---

![]({{site.baseurl}}/assets/neuro-inspired-computation-course/{{page.coverImage}})

I was lucky enough to be invited to [IRCN's](https://ircn.jp/en/) [neuro-inspired computation course](https://ircn.jp/en/neuro_inspired) in Tokyo. I decided to accept their offer to come to Tokyo and learn about the brain, computers and something inbetween.

![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_071842.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_072835.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_090703.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_090741.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_092225.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_091757.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_091420.jpg)

I got the chance to do a little exploring of the city;

- We visited Akihabara. Notably, a 5 story building full of arcade games, where we played Dance Dance revolution amongst other things.
- I took the metro at rush hour, it was a squeeze. Also, we wondered why there were only women on the carriage, and realised we had made a mistake... and hastily made an exit.
- I took a roller-coaster. Note: don't take a roller-coaster when you really need to go pee. It was a distressing ride.
- We saw the start of the sakura (cherry blossom), which only lasts around a week of the year!

![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190321_210234.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190321_202935.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190322_214449.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190322_184410.jpg)

## The course

I found the content of the course to be ok. Some of the lecturers took the opportunity to give a tour of everything they had done in the last 20 years (not very interesting as there was little detail.) And other lecturers did not take into account that they were lecturing an interdisciplinary group (not very interesting, as I was lost from the introduction). But, I was pleasantly surprised by a few of the talks;

[Extremely Scalable Spiking Neuronal Network Simulation Code](https://www.frontiersin.org/articles/10.3389/fninf.2018.00002/full?utm_source=G-BLO&utm_medium=WEXT&utm_campaign=ECO_FNINF_20180302_exascale-brain),) by Markus Diesmann.

How do models of the brain (specifically the memory required) scale with the number of neurons? "_Most simulation time is currently spent on delivering spikes from the MPI receive buffers to the target neurons through the connection infrastructure and synapse objects_". Their solution was to design a new kernel for `MPI_ALLtoaLL` that takes advantage of the massive amounts of connectivity sparsity in large spiking neural networks.

However, the `MPI_ALLtoaLL` operation is a global one, and does not scale well with the number of computation nodes. Future improvements could be made by exploiting larger scale sparsity structure in the network: "_The network model we consider here represents a worst-case scenario in terms of connectivity, since all pairs of neurons have the same probability of forming a connection. Biological neuronal networks larger than the cortical microcircuit, however, exhibit spatial organization on multiple levels._"

[Error-Gated Hebbian Rule](https://www.nature.com/articles/s41598-018-20082-0) by Taro Toyoizumi.

How does the brain learn? The authors construct a biologically plausible unsupervised learning rule, which is a linear combination of PCA and ICA. They rewrite the typical PCA cost function as minimizing the difference between the variance of the inputs and the outputs. And they rewrite the ICA cost function as minimizing the mean and variance from uniform, independent prior.

I am not entirely sure what makes these learning rules 'biologically plausible'. They claim that these learning rules are local, but I find that hard to see, as they require 'global' information from all output nodes!? I guess I am missing something.

[Emergent elasticity in the neural code for space](https://www.biorxiv.org/content/biorxiv/early/2018/05/21/326793.full.pdf) Surya Ganguli.

Two puzzles from cognitive science; How can a map be constructed by neural circuits? Why is the activation of grid cells soo stable?

The authors show that "_the emergence of this map can be understood as an elastic relaxation process between landmark cells mediated by an attractor network_". The landmarks (maybe boundaries), A and B, pin an attractor network to two certain states, and then cells oscillates between them, thus generating a grid.

They go on to show that a ring attractor network, with short range excitation and long range inhibition, generates 1D grid cells.

Serotonin mediates temporal discounting by Kenji Doya (it seems his talk was based on unpublished work?)

What does the behaviour of an agent with a low temporal discount look like? It will have a bias towards short term rewards, they will be impulsive, and they will not be able to 'see' large payoffs far into the future, the will be depressed. We know that impulsivity and depression are liked to serotonin, so Kenji et al. explore how serotonin modulates temporal discounting.

[Learning from weak supervision](https://arxiv.org/abs/1810.00846) by Masashi Sugiyama.

What if you only have positive labels and unlabeled data? Can you achieve better or worse performance than if you had negative labels instead of the unlabeled data? The answer is; it depends on how much unlabeled data you have.

### Team projects

I quite enjoyed the final part of the course; work with a few other students and present a proposal combining your interests and skills. Our team's proposal was cringe worthy, the two paragraphs contained little content and could have been summarized by the platitude; "we are going to find neural correlates with deep learning". Despite that, I think it was a cool concept, and given more time we could have come up with something more interesting.

## The people

I met some cool people and made some friends!

The most interesting student work I came across was [Hypergraph Laplace Operators](https://arxiv.org/abs/1804.01474) by Raffaella Mulas et al. and [Symmetry Learning for Function Approximation in RL](https://arxiv.org/abs/1706.02999) by Theja Tulabandhula et al.

![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_153643.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_153557.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_172305.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_180347.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_154841.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190324_174923.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190325_093704.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190325_104249.jpg)
![]({{site.baseurl}}/assets/neuro-inspired-computation-course/20190325_093410.jpg)

## Other observations / thoughts

- The Japanese people seemed very polite.
- Most of the students there didn't seem to be asking fundamental / deep questions (myself included).
- The people at Oxford or UCL or MPI or (insert prestigious university) ... did not, on average, seem so different to me. Maybe I have a chance?
- I received a nice reminder that there are people much smarter and more motivated than me.
