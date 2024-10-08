---
title: "The future of Model based RL?"
coverImage: "reinforcement_learning_diagram.png"
permalink: /models-for-hire/
layout: post
---

Let's imagine RL models as a service.

You are an enterprising individual, and have some problems to solve;

- generating new anti cancer drugs
- a bedroom that needs cleaning,
- explaining gradient descent to a friend that studies history,
- driving to the pub,
- poverty.

What service would help you solve them? Well, if you had an accurate, efficient model of the world, you could plan for the outcomes you want. For example, with a model of quantum physics, chemistry and human biology we could simulate the effect of various drugs and search for ones that will cure cancer(s)!

We could have models for;

- generalised chemical reactions, human biology, ...
- Classical physics, mechanics, human behaviour, my timetable, ...
- human learning, common knowledge, mathematics, history, ...
- classical physics, road rules and human behaviour, ...
- the world economy, people's response to incentives, ...

### The service: Models for hire

Given a domain specification: the state space, action space, a high level description of the task, and your resources (e.g. computation budget, accuracy requirements), we supply a (quickly adaptable) model of internal and external dynamics.

Question: why would anyone trust our models?

Because there exists an independent rating agency that requests models and reviews their accuracy.

### But what about learning new environments?

Our other product, an explorer. You put our explorer in the desired environment, say your laboratory, and you step back, well back, into the next room, then out the door and down the road. It quickly constructs a model of its environment. Disclaimer: May break some things. We accept no responsibility.

For example; if given access to a mechanical workshop, it might build a 'high level' model of mechanics and materials.

* * *

What I have described is also known as science, and it's free and already exists! But we have a long way to go making our models; reliable, robust and accessible.
