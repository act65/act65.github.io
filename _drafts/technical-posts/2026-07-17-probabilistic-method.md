---
layout: post
title: Proof by Lottery
subtitle: How to prove a thing exists by refusing to build it
categories:
  - play
---

Here is a move that should not be allowed.

You want to prove that some object exists — a graph with a certain property, a colouring with no bad pattern, a code that survives noise. The honest way is to build one and hold it up. The probabilistic method does something else. It reaches into a bag of *random* objects, and shows that a random one has the property you want with probability greater than zero. And then it stops, because it is done.

If a randomly chosen object has property $P$ with probability $> 0$, then at least one object with property $P$ must exist. Otherwise the probability would be exactly zero. You never saw the object. You never built it. You proved it is out there by proving the lottery has at least one winning ticket — without scratching a single one.

Erdős made this into an industry. Let me show you the trick on something small, then on something that runs your phone.

### The warm-up: a cut with half the edges

Take any graph with $m$ edges. Claim: you can split its vertices into two groups so that at least $m/2$ of the edges go *between* the groups (a "cut").

Proof: flip a coin for each vertex — heads left, tails right. Any given edge is cut exactly when its two endpoints land on opposite sides, which happens with probability $1/2$. So the expected number of cut edges is $m/2$. 
<!-- 
i dont understand this step, m/2 edges cut in expectation.
this seems wrong, or at least non trivial?!
 -->
A random variable cannot always be below its own mean — so *some* coin-flip outcome gives a cut of size at least $m/2$. Done. We never found the cut. We proved it exists by averaging.

> This still feels like cheating, and it is worth being clear about why it isn't. Averaging gives a *lower bound on the maximum*: if the mean is $m/2$, the best case is at least $m/2$. The method only ever proves *existence*. It will never hand you the object, never tell you it is unique, never tell you how to find it. It cleanly separates *is there one?* from *find me one* — two questions we usually smear together without noticing.

<!-- 
this final statement; 
- existence (is there one) vs construction (show me one)
this seems like the KEY insight.
existence is strictly easier than construction?!
but how can you know something exists without having seen/constructed it?
 -->

<!-- 
the argument above is actually stronger than just p>0?
or that there exists a cut st >= m/2 edges go between groups.
rather this proves > m/2 edges go between groups?!
(assuming variance greater than zero)

ah wait, we are dealing with discrete variables / integers.
 -->

<!-- 
other thoughts 

are there other non-constructive proof strategies?
-->

### The deep one: Ramsey numbers

Colour every edge of the complete graph on $n$ vertices red or blue, however you like. Ramsey's theorem says that if $n$ is big enough, you are forced to create a monochromatic clique of size $k$ — $k$ vertices all joined by edges of one colour. Order is unavoidable. The question is *how big* $n$ has to be, $R(k,k)$.

Erdős (1947) bounded it from below by lottery. Colour each edge red or blue by a fair coin. Fix any $k$ vertices; the probability all $\binom{k}{2}$ edges among them come out the same colour is $2 \cdot 2^{-\binom{k}{2}}$. There are $\binom{n}{k}$ such sets, so the expected number of monochromatic $k$-cliques is

$$\binom{n}{k}\, 2^{1-\binom{k}{2}}.$$

If that expectation is less than $1$, then *some* colouring has zero monochromatic $k$-cliques — because you can't have fewer than one on average and never zero. Grinding the arithmetic gives $R(k,k) > 2^{k/2}$ (roughly): there exist colourings of graphs on $2^{k/2}$ vertices with no monochromatic $k$-clique.

Here is the part that should keep you up at night. That was 1947. We have known for nearly eighty years that these good colourings *exist*, in overwhelming abundance — a random colouring works. And to this day nobody can *construct* one that comes close. The best explicit constructions are exponentially worse than what the coin flips prove is sitting right there. We can prove the haystack is almost entirely needles and still not pick one up.

### The crown jewel: why your phone works

Shannon's channel coding theorem (1948) is the same trick, and the entire digital world is built on it.

You want to send bits over a noisy channel. To do it reliably near the channel's capacity $C$, you need a good *codebook* — a cleverly spread-out set of messages that noise can't smear into each other. Shannon did not construct one. He showed that a codebook drawn *at random* — messages picked by coin flip — achieves capacity with probability approaching $1$ as the block length grows. A random code is, almost surely, a nearly optimal code.

So the promise underneath every modem, hard drive, deep-space probe, and QR code is a probabilistic-method existence proof. And — the pattern again — *constructing* codes that actually reach capacity took another fifty years of work (turbo codes, LDPC, polar codes). Existence in 1948; construction in the late 1990s. Half a century sitting inside the gap between "one exists" and "here is one."

### The gap is the whole point

That gap is the thing I keep circling back to. Sometimes it closes: the *method of conditional expectations* turns an averaging argument into an algorithm. You build the object one decision at a time, and at each step you pick the branch that keeps the conditional expectation on the good side of the line. The average was a lower bound on the max; you greedily walk toward the max. Existence becomes construction, for free.

And sometimes — Ramsey — it stubbornly refuses to close, and the resistance is itself the interesting object of study. *Exists cheaply* and *can be built with bounded resources* are different questions, and the probabilistic method is the sharpest tool I know for prying them apart.

Luck, it turns out, is a proof technique. You don't need to be able to find the winning ticket. You only need to prove the lottery isn't rigged against you — that the winners have positive measure — and existence follows for free. The universe is full of objects we are certain exist and cannot point to.
