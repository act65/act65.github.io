---
layout: post
title: Tax optimisation as an adversarial game
subtitle: A new perspective on tax law
categories: 
  - "economic"
---

## Introduction

Have you ever wondered how Artificial Intelligence (AI) could be used to improve tax laws? While it might seem like a futuristic concept, framing tax optimization as an adversarial game between taxpayers and tax authorities offers a unique perspective.

## The New Zealand Context

New Zealand's General Anti-Avoidance Rule (GAAR) relies on judges interpreting the law, creating a system where precedent sets future rulings. This lack of clear, unambiguous rules makes it challenging to achieve fairness and efficiency in tax collection.

## The Challenge of Incomplete Laws:

Our current tax laws are incomplete, representing an approximation of an ideal system that rewards contribution, protects individuals, and ensures fairness. Mistakes and loopholes exist, allowing some taxpayers (with help from accountants and lawyers) to exploit these weaknesses.

## Tax Optimization as an Adversarial Game

Imagine a game between the Inland Revenue Department (IRD) and taxpayers. The IRD writes and passes tax legislation, taxpayers organize their finances to minimize tax burden (legally, of course!), and the IRD observes the aggregate tax loss. They can then choose to consult the "oracle" (judges) at a high cost to determine if a taxpayer's strategy is legal.

## The Difficulties

This game presents several challenges:

- Computation Asymmetry: Taxpayers only need one strategy - minimize tax legally. The IRD needs to find and close all potential loopholes.
- Memory Asymmetry: Taxpayers can easily track changes in tax law, potentially collaborating to find new strategies. The IRD struggles to model and track the financial maneuvers of countless taxpayers.

## The Learning Curve:

We're essentially trying to approximate the ideal tax system with limited information. As the IRD learns and improves its tax laws, taxpayers adapt their strategies. The key is to find a balance between learning efficient tax collection and minimizing loopholes exploitable by taxpayers.

## Open Questions

- Can we design un-exploitable tax laws (a truly complete set of rules)?
- Is designing a secure system inherently harder than finding ways to exploit it?
- How can we prove a tax strategy is truly un-exploitable?
- Could we measure "gameability" to assess loopholes' ease of exploitation?
- How can we analyze historical data to see how quickly the IRD learns compared to taxpayer adaptation?

## Conclusion

Exploring tax optimization through an AI and game theory lens offers new perspectives on creating a fairer and more efficient tax system. By understanding the challenges and open questions, we can move towards a future where technology helps us achieve a more balanced approach to tax collection.

<!-- I came across a new adversarial setting (at least new to me...) while getting curious about how to apply AI/ML to complete tax law and how to regulate tax optimisation (aka avoidance in my mind, sigh).

Some background:

> NZ uses a General Anti-Avoidance Rule (GAAR). In practice this means judiciaries end up making the law. Aka, there doesnt exist a set of well-specified laws, so judges must interpret the GAAR. The rulings are then used as precedent for the future.

what does this really have to do with the game between taxpayers versus tax gatherers

Ok, so this post focuses on completing tax law. 

## Completing tax law

We want to design a society which (amongst other things) A) rewards people for their contributions, B) protects individuals from bad actors, C). But we do not know which set of unambiguous rules will necessarily yeild A, B, C.

Our current tax law is incomplete, we have an incomplete approximation of some ideal set of tax laws. To complete these tax laws, we query judiciaries and they act as our oracles.

Worse than than, in our attempt to build this ideal, complete knot of tax laws. Mistakes have been made, where behaviours deemed illegal by the ideal tax laws, are deemed legal, by current tax laws.

We occasionally see these cases resolved by a high court.

These loopholes in the ideal tax knot are what private accountants and lawyers like to pull on.

### Adversarial accounting

Imagine a game between [IRD](https://www.ird.govt.nz/) (the NZ tax gatherers) and a taxpayer. 

(from the perspective of IRD)

1. You reveal your move (write and pass some tax legislation).
2. Your adversary (a taxpayer) organises its finances to minimise tax paid (legally or not, that is a question for another day).
3. You recieve the aggregated loss over all taxpayers (you can choose to query an expensive oracle -- judges/court -- to check whether your adversary has made a legal move).

What makes this setting hard?

- __Computation asymmetry__. The adversary needs to find a single strategy to minimise tax (that is also legal). You need to find and subvert all potential strategies to avoid paying tax.
- __Memory asymmetry__. In the multiplayer setting (many adversaries), it is easy(er) for each adversary to model and track changes in tax law (maybe they even collaborate...). But it is hard(er) for you to model and track changes to thousands, or more, adversaries (changes in a corporations finances my be indicative of avoidance).

### Related: Adversarial examples

What if you know that your adversary is going to be given your current model? How would you design your model given that information? Design a model so that it is stable under an informed adversarial attack.

The loss is revealed to the adversary (they avoided $x$ dollars of tax). 

So, in summary. There is an unknown set of ideal rules (implicitly known by judges in the high court), which captures tax law. We are trying to approximate that implicit knowledge with few samples. But, as we learn our approximation, our adversaries (taxpayers) adapt their strategies. So, while learning to approximate the target function we also want to minimise the taxpayers ability to exploit our approximation.

Questions raised;

* How can we design an un-exploitable model, or what might be called a complete set of laws?
* How much harder is it to design un-exploitable systems than to game that system?
* How would you even prove that a strategy is un-exploitable?
* Is there a measure of gameability? The ability to __easily__ find hacks/strategies?
* This can actually be formalised as the 'regret' of the tax laws. This raises the question of; how the losses of the adaptive policies that are used to set tax law have scaled in the past.
* If we look at the history of tax laws ....? How quickly is IRD learning? How quickly are individuals adapting?
 -->
