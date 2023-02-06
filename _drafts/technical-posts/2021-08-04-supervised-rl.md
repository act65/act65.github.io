---
layout: post
title: Supervised learning is* all you need (for RL)
permalink: supervised-rl
---

# Supervised learning is* all you need (for RL)

*well we don't know that for certain. It just makes a good title...

Not. It's an argument of sufficiency, not necessity.

## Unsupervised learning

Before autoencoders and contrastive losses, there was; boltzman machines, clustering, self-organising maps, ...
But these didnt work well. Why not?

It's not immediately clear that unsupervised learning can be formulated as a supervised learning problem.
Fundamentally, unsupervised learning lacks supervision. In unsupervised learning, we care about inferring patters / regularities in the data.
There is no teacher that can supervised: letting us know which patterns or regularities are 'correct'.



Supervised learning coverges quicker.


## Reinforcement learning

Attempts at SL RL.

- ?
- upside down
- hindsight
- ?

#### BC and dataset optimisation


<!-- #### Behavioural cloning

https://ml.berkeley.edu/blog/posts/bc/ -->


$$
J(\theta)= \mathop{\mathbb E}_{\pi_{\theta}} \Big [R(\tau) \Big] \\
J'(\theta, q) = \mathop{\mathbb E}_{q} \Big [\frac{\pi(\tau)}{q(\tau)} R(\tau) \Big] \\
\theta^{* } = \mathop{\text{argmax}}_{\theta} J'(\theta, q) \\
q^{* } = \mathop{\text{argmax}}_{q} J'(\theta, q) \\
$$

But now. we want to find maxmax?

Where $q$ is the distribution over data.


- Policy learns to copy the data. Learning a policy becomes a supervised learning problem.
- Need to collect a 'good' dataset.


https://bair.berkeley.edu/blog/2020/10/13/supervised-rl/

Havent we just moved the 'hard' oprimisation problem to constructing a good dataset?
Or is there actually some advantage of this framing?

#### Upside-Down Reinforcement Learning

[https://arxiv.org/pdf/1912.02877.pdf](https://arxiv.org/pdf/1912.02877.pdf)



#### Hindsight replay...?



Hrmm. Not sure about this? Policy will attempt clone the best trajectories. Not act optimally?!<br>If there are two suboptimal trajectories (whose union could make an optimal trajectory), ...!?



How tight is this lower bound? Why is it not exact?  

Want to understand. How is behavioural cloning on a 'good' dataset, the same as maximising expected return?


Can RL be framed as a sueprvised problem? If not, why not?





****


#### Iterated supervised learning

But the supervised learning is really <i>iterated</i> supervised learning. Doesn't this suffer the same problems RL does?

Open quiestions

- How much harder is iterated supervised learning than supervised learning?
- ?
