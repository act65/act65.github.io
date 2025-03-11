---
title: Delayed directions
subtitle: Your lost, and trying to find your way
layout: post
permalink: /delayed-directions/
categories: 
  - "play"
---

Imagine, a Neptune rover navigating the surface of the planet.
It's goal is to find the highest point so that it can set up a communication relay.
However, the rover only has access to local measurements, and it can only communicate with the base station on Earth (which takes 2.5 hours for a signal to reach).

A similar scenario might be;

you are lost, but can message a friend that gives you directions.
However, there is a significant delay in the communication (since your fiend is busy and can only respond every 30 minutes).
And your friend only gives you directions to the nearest landmark (again, since they are busy and can't provide detailed directions).

In each case; you / the rover / ??? want to reach the destination as fast as possible, but you also want to minimize the number of times you have to call the oracle.

Oracle;
- only allowed to provide local information / directions
- maybe noisy

Delay;
- random delays 
- or fixed delays
- would like some creative kinds of delays

This is a metaphor for asynchronous SGD.

Potential solutions;

- "call and wait" - you call the oracle, and wait for the response before you take the next step.
- "call and continue" - you call the oracle, and continue on your path, and when the oracle responds, you adjust your path. (why doesn't this work?)