---
title: The hammer and the cannon
subtitle: Why AI Robustness is Necessary for AI Alignment
layout: post
---

How can we ever hope to build an AGI that won't outsmart humanity for the worse, if we can't even build an AI that a clever human can't trick?

<!-- clever human, with access to other (narrow) AI tools -->

This simple question gets to the heart of a crucial, logical prerequisite for AI safety. It establishes that solving the problem of **robustness** in today's narrow AI is a necessary, though not sufficient, condition for solving the grander problem of **alignment** in a future AGI.

Let's define our terms:
*   **Problem A (Robustness):** Making a narrow AI system (e.g., an image classifier) robust against a clever *human-level adversary* who is actively trying to find exploits, like adversarial examples.
*   **Problem B (Alignment):** Making a future Artificial General Intelligence robust against the unintended consequences of its own *superhuman-level optimization process*, which acts as an adversary to our intended goals.

<!-- 
talk about RL robustness.
a reward function is a kind of classifier / regressor?
what if we can give adversarial / OOD examples to manipulate / control the agent?

what's the formal definition of RL robustness?
what's the formal definition of RL alignment?

don't be scared of the math!!
 -->

 

**The Argument: The Adversary is Strictly Stronger**

The logical argument for why A is necessary for B is simple and powerful: the adversary in Problem B is strictly stronger than the adversary in Problem A.

An AGI, when searching for loopholes in its own goal system, is faster, more knowledgeable, and more intelligent than any human hacker. It has perfect access to its own source code and can simulate billions of strategies in the time it takes a human to formulate one.

<!-- need to clarify how / why the AGI is searching for loopholes in its own goal system. it's not really. it's just exploring and trying to find the best solution -->

This leads to a powerful analogy: **The Sledgehammer and the Cannon.**
*   Building a robust narrow AI is like building a castle wall that can withstand a person with a **sledgehammer** (a human adversary).
*   Building an aligned AGI is like building a wall that can withstand a **cannon** (the AGI's own optimization).

If your engineers cannot even design a wall that holds up against a sledgehammer, it is logically impossible that the same techniques will hold up against a cannon.

<!-- sure nice metaphor. but can we be more precise?!

 -->