---
layout: post
title: Rounding a Democracy
subtitle: Turning votes into whole seats is primary-school arithmetic with its own impossibility theorem
---

Here is a problem that sounds too simple to write about. A parliament has 100 seats. Three parties win 43.6%, 34.9%, and 21.5% of the vote. How many seats does each get?

Multiply out and their "fair shares" are 43.6, 34.9, and 21.5 seats. But seats come in whole numbers, so you have to round — and the rounded numbers have to still add up to exactly 100. That's it. That's the whole problem. It is rounding, the most boring operation in arithmetic.

It is also a minefield with paradoxes that broke the United States Congress, three competing "fair" methods that disagree, and its own impossibility theorem — an Arrow's theorem for division. Every democracy that turns votes into seats has quietly chosen which unfairness it can live with, and most of their citizens have no idea a choice was made.

### The obvious method, and the trap

The natural approach is **Hamilton's method** (largest remainders). Give every party its share rounded *down* — 43, 34, 21, using 98 seats — then hand the 2 leftover seats to the parties with the largest fractional remainders (here .9 and .6). Simple, intuitive, obviously fair.

And then, in 1880, the chief clerk of the US Census Office sat down to compute what would happen at various House sizes, and found something that shouldn't be possible. Under Hamilton's method, **Alabama would receive 8 seats if the House had 299 members — but only 7 seats if the House had 300.** Adding a seat to the total took a seat *away* from Alabama.

This is the **Alabama paradox**, and it is not a rounding error; it's a structural feature of the method. Grow the whole, and a part can shrink. It sinks any intuition that seats behave like a sensible allocation of stuff — you cannot even reliably say that a bigger legislature is better for everyone.

Hamilton's method has relatives, too. The **population paradox**: a state whose population is *growing faster* than another's can nonetheless *lose* a seat to the slower-growing one. And the **new-state paradox**: when Oklahoma joined the Union in 1907 with a fair allocation of 5 seats, adding it and its seats *changed the allocation among the existing states* — states that had nothing to do with Oklahoma swapped seats because Oklahoma existed.

### The other family, and its own sin

To escape the paradoxes, you switch to a **divisor method**. Instead of rounding shares directly, pick a divisor $D$ (roughly "people per seat"), give each state $\text{round}(\text{population}/D)$, and adjust $D$ up or down until the seats happen to sum to the right total. These methods — associated with Jefferson, Webster, and Huntington–Hill (which the US House has used since 1941), differing only in *how* they round at the boundary — are provably **free of the Alabama and population paradoxes**. Grow the house or a population, and nobody loses a seat they shouldn't.

But they buy that with a different flaw: they can **violate quota**. A party with a fair share of 34.9 seats might get 36, or 33 — more or less than its share rounded either way. Jefferson's method, notoriously, systematically favours large parties (which is why versions of it, under the name d'Hondt, are popular with big parties across Europe). You've cured the paradoxes and caught a new disease: the allocation can drift away from what the raw numbers say each party deserves.

### The impossibility

By now you can feel where this is going, because it's the shape of every result I'm drawn to. In the 1980s Michel Balinski and Peyton Young proved it: **no apportionment method can both stay within quota and avoid the population paradox.** Pick either fairness property and you can have it — but not both, ever, by any method. It is Arrow's impossibility theorem transplanted from *ordering preferences* to *rounding numbers*: a short list of things any fair rule obviously ought to do, and a proof that nothing does all of them at once.

So there is no correct answer. There is only a menu of methods, each sacrificing a different fairness axiom, and every country has picked one — usually without the electorate ever being told that "how we round" was a values question with no clean solution.

### Why this belongs here

Two reasons I can't leave it alone. First, it's the same creature as [voting-as-lossy-compression]({{ site.baseurl }}/voting-geom): you're taking a continuous thing (vote shares, a distribution) and forcing it into a coarse discrete grid (whole seats), and the paradoxes are *quantisation artefacts* — the unavoidable damage of rounding a smooth quantity to integers. The "unfairness" isn't corruption; it's the information you destroy the moment you demand integers.

Second, it's not abstract, and it's not only American. Aotearoa's MMP system allocates its list seats by the **Sainte-Laguë method** — which is exactly Webster's divisor method, the paradox-free-but-quota-violating one. When you vote here, a nineteenth-century American argument about how to round Alabama is quietly deciding, at the boundary, who gets the last seat in our Parliament. The most boring operation in arithmetic has no fair implementation, and we are all, always, living inside somebody's choice of which unfairness to accept.
