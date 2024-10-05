---
title: "What makes something true?"
date: "2020-08-18"
coverImage: "public-engagement-science-comms-hero.jpg"
layout: post
subtitle: How does deductive truth (ie math) relate to inductive truth (ie science)?
---

# What makes something true?

<!-- a poem pointing out math->truth
science->likely to be true -->

> Mathematics can derive the truth,\
trustworthy proof.\
Science only reduces our uncertainty,\
guessing nervously.

<lside>Deduction</lside>
What is 'proof'? In mathematics a proof means that we can agree upon a starting point and some determistic rules, and with those rules we can find (aka 'prove') statements that are true! This is also known as deductive reasoning.

<div markdown="1" class="code"> 
<lside>Examples</lside>
For example, _chess_.
Given a chess position, the one shown below, it is true that white can checkmate in 3 moves (if we follow the rules of chess). (Wf4->h6, Bg8->h6, Wd2->h6, Bf8->g8, Wf6->f7)

<img src="{{site.baseurl}}/assets/what-makes-something-true/image.png" alt="chess position" style="height: 300px;"/>

There are many other true statements that can be proven given this starting point (and following the rules of chess).

- The white queen is at f4.
- The white king can move to d1.
- Black has 7 pawns.

Similar to how we use the rules of chess to derive things that are true about a given chess game. 
We can agree on objects called _integers_, {0, 1, 2, 3, 4, ...}, and agree on rules for adding and multiplying them, **+**, **x**. From these integers and their rules we can derive [prime numbers](https://en.wikipedia.org/wiki/Prime_number).

[Euclidian geometry](https://en.wikipedia.org/wiki/Euclidean_geometry) is another example of a system of rules that can be used to derive true statements. 
Given the 5 postulates of Euclidian geometry, (basic equality rule, equality through operations, equality based on coincidence, universality of right angles, parallelism) we can derive the Pythagorean theorem, and other familiar 'true' statements, such as the sum of the angles in a triangle is 180 degrees.
</div>

<lside>Bounded resources</lside>
But, not all statements have known proofs. For example, the [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis) is a statement about the distribution of prime numbers. It is not known if this statement is true or false.

We have not yet found a proof for the Riemann hypothesis. This is a problem of bounded resources. We have not yet imagined all the possible proofs.
Similarly, in chess, 

So mathematics can make statements that are __true__, given a starting point and some rules. But, not all statements have known proofs.

> However, the real world is not like chess, integers or Euclidean geometry.
(1.) We do not start by agreeing to any rules, (2.) and we have an imperfect view.

<lside>Induction</lside>
The universe does not come equipped with a rule book for us.
We need to start by making some assumptions.

- the laws of the universe do not change with time. They are the same today as they are tomorrow, and the next day.
- the observations we made are not interfered with ( there doesn't exist an adversary manipulating our observations )

Note that, these assumptions cannot be proven to be true, and therefore we cannot claim that science gives us the truth.
We make these assumptions on the basis of our experience. We have not yet observed the laws of the universe to change, and we have not yet observed an adversary manipulating our observations.

<div markdown="1" class="code">
Everyday, a farmer feeds his pigs at 7am. He has done this for the past 30 weeks years. The pigs assume this is a law of the universe, that the farmer will feed them at 7am. But, one day the farmer instead loads them into a truck and takes them to the meatworks.

You have observed the sun rise every morning for the past 30 years. You assume that the sun will rise tomorrow.

Every swan you have ever seen is white. So you guess that all swans are white. You would be wrong.

</div>
Induction is the name for making generalisations from specific observations.
I have not seen all swans, yet, based on the swans I have seen, I assume that all swans are white.

<lside>An imperfect view</lside>
<img src="{{site.baseurl}}/assets/what-makes-something-true/chess-window.png" alt="imperfect chess view" style="height: 300px;"/>

The next issue, we have an imperfect view of the world. We do not see everything, and what we do see is noisy.

If we imagine an imperfect view of chess it might look like the following.

You never get to observe the board directly, rather;

- through a small window, where you can only see a few squares at a time (I can see g2 square, but not the b7 square) (_imperfect information_)
- the window is also foggy (I'm pretty sure that's a pawn at g2, but it might be a bishop)  (_measurement noise_)

<!-- how do these cause issues? -->
Imperfect information means we may be missing relevant information.
For example, the existence of black swans.

Measurement noise means we may be misinterpreting the information we do have. For example, 
<!-- Maybe you have discovered life on the moon, or maybe there is a life-like smudge on your telesope. You are uncertain. -->

<lside>Science</lside>
> This imperfect view is the problem science solves. 

Science attempts to systematically reduce our uncertainty about the truths determined by the physical rules of our universe. However, science only reduces uncertainty (rather than eliminates it), science cannot answer '_What makes something true?_', instead, science focuses on a different question.

> _What makes something likely to be true?_



<div markdown="1" class="code">
Consider the question; _is the theory of general relativity likely to be true?_

![]({{site.baseurl}}/assets/what-makes-something-true/einstein-s-theory-of-relativity.jpg){:height="200px"}

![]({{site.baseurl}}/assets/what-makes-something-true/189-1896015_law-of-gravity-equation.png){:height="200px"}

Science can tell us;

1. it is more likely to be true than Newton's theory of gravity because it reliably makes more accurate predictions about celestial mechanics (the [Eddington experiment](https://en.wikipedia.org/wiki/Eddington_experiment)), as well as making predictions about other observations ( black holes, light, ... ) ( it's the current best hypothesis we have constructed, but there may exist others, that explain even more - ie dark matter )

2. it is more likely to be true because it has generalised. It has made accurate predictions about new observations (Einstein predicted gravitational waves in 1915). This tells us that, at least in this case, we didn't overfit to our existing observations. But, we have no clue how this theory will generalise to other unobserved phenomena.

3. it is more likely to be true because it explains our observations in a 'simple manner' ( ie Occam's razor ). General relativity can be derived from statement that "the laws of physics are invariant in all inertial frames of reference".

But these successes of general relativity are not sufficient to answer _is the theory of general relativity likely to be true?_ with much certainty.

</div>

Our estimate of likelihood is based on our history (the data we happen to have collected), our imagination (the equations and models we have constructed, so far) and some assumptions.

But, our history could have been different: __imperfect view__.
This means that science cannot actually answer "_What makes something likely to be true?_". Rather, the best science can do is;

> Given what we have observed, what is the most likely thing to be true?

<!-- (and how hard have we tried to find new data?) -->

But, our limited imagination means we may not have imagined the most likely answer: __bounded resources__. There is always a chance that our search finds a new, more likely to be true, theory. So we arrive at;

> _Given what we have observed and the answers we have imagined, what is the most likely thing to be true?_

Note that as science progresses, as new observations and new theories are imagined, our best guess at what is likely to be true should change.
This is the essence of the scientific method.

Science is a best guess, nervously hoping that we have not missed something important.