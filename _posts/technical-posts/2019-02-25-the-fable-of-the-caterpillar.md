---
title: "The fable of the caterpillar"
date: "2019-02-25"
coverImage: "caterpillar-a.png"
layout: post
subtitle: A fun intro to my masters topic; abstraction for efficient reinforcment learning.
categories: 
  - "tutorial"
---

(This is my current focus - kinda - for my masters. The (art)work was done in prep for a conference poster)

![caterpillar-g]({{site.baseurl}}/assets/the-fable-of-the-caterpillar/caterpillar-g.png)

A green leaf, <br>
is too far, out of reach, <br>
What you want, is in front, <br>
take the steps.

> You move your first leg up<br>
You move your second leg left<br>
You move your eleventh leg up<br>
You move your twelfth leg right

![caterpillar-g-1]({{site.baseurl}}/assets/the-fable-of-the-caterpillar/move-g-1.png)

Many legs burden the act, <br>
Unless coordinated in abstract.

The words in this new abstract language, Should be as few as we can manage.

> "left", "right", "forward", "backward"

This time, <br>
the act is rather brief, <br>
"forward", to reach the tasty leaf.

On the left, the caterpillar must command every leg independently. It must move each leg up or down or left or right. Thus there are many possible commands it could give (aka many actions it could take). But many of these complicated actions result in nothing, or elicit a similar result. Similar results from different actions hint at an underlying structure that might be exploited (there may be many commands that result in forward movement, we dont need to know all of them!).

On the right, the caterpillar has learned an 'abstract representation' (aka high level actions) of actions. These higher level actions can be mapped back into the complicated action space (left). This abstract representation might make life easier for the caterpillar. Now it can design plans (sequences of actions) and assign credit (which action was responsible for X?) using less effort (because there are fewer possible actions).

### Questions

- How can an agent (efficiently) learn a language (aka an abstract action space) for (efficiently) describing what they want?
- If an agent has access to an abstract action space (with certain properties), what advantage might it provide (in its environment)?
- Under what environmental conditions does abstraction naturally emerge?
- How is the structure of an agent's environment reflected in the 'grammar' of its abstract action space?

### Properties of abstract action spaces

To understand abstract action spaces, we really need to understand their properties and how they lead to; faster learning, better generalisation, efficient control, ... So what are properties of action spaces we could explore?

- Disentangled (different actions effect the state independently)
- Regular (an action changes the state in a regular/consistent way)
- Composable (actions can be composed into valid sequences)
- Efficient/Simple (require few actions for typical tasks)
- Expressive (all/most states are reachable)

![caterpillar-a.png]({{site.baseurl}}/assets/the-fable-of-the-caterpillar/caterpillar-a.png)
