---
layout: post
title: Adversarial RL
subtitle: Some ideas
---

In the last few years there has been a lot of study of adversarial machine learning. Adversarial pertubations, adversarial training, adversarial examples, adversarial attacks, adversarial defenses, etc.

What are the motivations for this research?
- To protect industrial applications of ML / RL. Aka security.
- To understand 
- 


## Settings

### A single state-action reward pertubations

The attacker is allowed to insert one large, erroneous reward.

- for a fixed reward. for a single s,a we get to pick the reward.
- for an adaptive reward. for each episode, we get alter the reward for a single s,a.
- 

How much can this slow learning?

When does the optimal policy maximise the true reward function, (as well as) the observed reward function?

### 

## References

- [Making machine learning robust against adversarial inputs](https://dl.acm.org/doi/10.1145/3134599)
- [Manipulating SGD with Data Ordering Attacks](https://arxiv.org/abs/2104.09667)