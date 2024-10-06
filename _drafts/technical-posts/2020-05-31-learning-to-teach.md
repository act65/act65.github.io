---
layout: post
title: Helping others learn
categories:
    - "proposal"
---

With our greater understanding of learning we can now train dogs to do X. (insert videos of clever dogs) [jenga](https://www.youtube.com/watch?v=1kl3Y82qRDg), [objects](https://www.youtube.com/watch?v=Ip_uVTWfXyI) ...

Given a slow learner. Design a curriculum to help it learn. This isnt about finding the best learning algorithm. It is about taking a suboptimal one and helping it learn more efficiently.

> If a learner sucks at; long term rewards, exploration, partial info, ... does there always exist an easily finable curriculum that will help them achieve high reward?

For some types of learner there may be little we can do, even with an optimal curricula.
Ie. the learner is incapable of learning the optimal policy.

#### Aside: how do people learn?
Interactive. Stories. ...? Easily remember agents and motivations, ...Formal setting

## Formal setting

Sits inbetween the agent and it's environment. Is able to manipulate rewards, generate fake data,

The teacher can only output (s, a, r, s, a) 's. (and by exension, trajectories)

- Agent $\mathcal A: D\to \pi$
- Teacher $\mathcal T: D \times \mathcal E\to D$
- Env $\mathcal E: S \times A \to S, R$
- Worker $\mathcal W: \mathcal E \times \pi \to D$

## What classes of teacher are there.

- online vs offline

What information do they have access to?
- The agent's parameters / model
- The sarsa buffer so far

How much information can they convey to the student?
- Counterfactuals
- Dense v sparse rewards

What does the teacher know?
- The optimal policy is known
- The model / reward is known
- ???

- What types of information can they communicate?
  - Rewards,
- What is the teacher tying to optimise?
  - dRdt?
  - Regret


What if the teacher doesnt know the answer. Only how to find the answer? Can generate artificial rewards showing the process.

Model based teaching?!

- figure out how the shitty learner learns. (separate problem. see reverse engineering a learning algorithm)
- Then design curriculum.

How can the teacher's skills be efficiently distilled? Teacher learns to do X. Attempts to train a different type of learner to do X.

## Examples

- A learner with catastrophic forgetting. The teach can remember and insert old tasks into training.
- A learner that ...???
-

## Forseeable problems


How to reduce potential variance in the learners actions??


***

We are still a while away from robots like seagulls!? I'm watching them gather food, navigate waves, ...

Instead. (Efficiently / automatedly) Teach seagulls to do X.

***

Helping others collaborate?