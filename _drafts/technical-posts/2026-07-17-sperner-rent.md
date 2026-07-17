---
layout: post
title: Start With a Triangle
subtitle: A colouring lemma that divides the rent so nobody envies anyone
categories:
  - play
---

Three friends rent a flat with three unequal rooms — one big and bright, one small, one next to the bathroom. They have to split the rent. Every scheme they try ends the same way: someone mutters that they got the bad end of the deal, and someone else secretly agrees. Is there a division where *nobody* would rather have someone else's room at someone else's price?

There is, always, and the proof is a lemma about colouring triangles. It's one of my favourite examples of a piece of pure combinatorics turning out to *be* a piece of practical fairness — not by analogy, but literally.

### Sperner's lemma

Take a big triangle and chop it into lots of small triangles (a *triangulation*). Now colour every vertex with one of three colours — call them **1**, **2**, **3** — under one restriction, the *Sperner condition*:

- the three main corners get the three different colours (one **1**, one **2**, one **3**);
- along the edge joining the corner-**1** and corner-**2**, every vertex must be a **1** or a **2** — never a **3**. Same for the other two edges: a vertex on an edge may only wear the colours of that edge's two endpoints;
- vertices strictly *inside* can be any of the three colours, no restriction.

**Sperner's lemma:** any such colouring contains a small triangle whose three vertices carry all three colours — a *rainbow* triangle. In fact it contains an **odd** number of them, so there's always at least one.

![A triangulated triangle, Sperner-coloured, with a rainbow sub-triangle highlighted]({{ site.baseurl }}/assets/sperner/triangulation.svg)
*Placeholder — a triangulation with corners coloured 1/2/3, edges obeying the Sperner condition, and at least one fully-coloured small triangle picked out.*

### Why it's true — a door-counting argument

The proof is a little gem; you can do it in your head. Call an edge of a small triangle a **door** if its two endpoints are coloured **1** and **2**. We'll count doors.

Look at any small triangle. How many **1–2** doors does it have?

- If its three vertices are coloured $\{1,1,2\}$ or $\{1,2,2\}$ — exactly **two** doors.
- If it's a rainbow $\{1,2,3\}$ — exactly **one** door.
- Anything else (no **1** and **2** both present) — **zero** doors.

So a small triangle has an odd number of **1–2** doors *if and only if* it's a rainbow triangle. Now count doors from the outside. An interior door is shared by two triangles, so it contributes to two triangles' counts; a door on the boundary of the big triangle belongs to just one. The only place **1–2** doors can sit on the outer boundary is the corner-**1**–to–corner-**2** edge (the other two outer edges forbid one of the colours). And on that edge the colours start at **1**, end at **2**, so the number of times the colour flips from **1** to **2** — the number of boundary doors — is **odd**.

Add it up with a parity argument (this is really the one-dimensional Sperner lemma doing the work): an odd number of boundary doors forces an odd number of triangles with an odd door-count — that is, an odd number of rainbow triangles. Odd is never zero. One must exist. $\blacksquare$

> Sperner's lemma is the discrete skeleton of the **Brouwer fixed-point theorem** — the "you can't comb a hairy ball / stir your coffee without leaving a point unmoved" theorem. Refine the triangulation infinitely and the rainbow triangles shrink to a fixed point. Fairness, below, is going to inherit its existence from exactly this.

### From triangles to rent

Here's the move that still feels like a magic trick to me.

A split of the rent among three rooms is three non-negative numbers that add to the total. Normalise the rent to 1, and a split is a point $(x_1, x_2, x_3)$ with $x_i \ge 0$ and $x_1 + x_2 + x_3 = 1$ — room $i$ costs $x_i$. But that set — non-negative coordinates summing to one — **is a triangle** (a 2-simplex). Every point of the triangle is a way to divide the rent. The three corners are the degenerate splits "one room costs the whole rent, the other two are free."

Now triangulate that triangle finely, and at each vertex — each candidate price-split — walk up to one of the housemates and ask a single question:

> *At these prices, which room would you choose?*

Colour that vertex by their answer: **1** if they'd take room 1, **2** for room 2, **3** for room 3. (Rotate through the three friends as you visit vertices, one person per vertex — the theorem is generous about which.) Assume only that each person always wants *some* room, and — the one substantive assumption — that **nobody turns down a free room**: if a room's price is 0, a rational tenant will never prefer a room they'd have to pay for.

That "nobody refuses a free room" assumption is *exactly* the Sperner boundary condition in disguise. On the edge where room 3 is free ($x_3 = 0$), nobody picks... wait — they'd happily pick the free room 3, so that edge never forces a 3? Look again: on the edge where room 3 costs the *whole* rent ($x_3 = 1$, so $x_1 = x_2 = 0$) rooms 1 and 2 are both free and nobody will choose the maximally-expensive room 3 — so every vertex there is coloured **1** or **2**, never **3**. That's the Sperner edge condition, forced by preferences. The corners and the other edges line up the same way.

So the colouring is a legal Sperner colouring — and Sperner's lemma hands you a **rainbow triangle**: a tiny cluster of three almost-identical price-splits at which the three housemates each choose a **different** room. Someone wants room 1, someone room 2, someone room 3, at essentially the same prices.

That is an **envy-free** division. Each person gets a different room, and — because they *chose* it as their favourite at those prices — nobody prefers anyone else's room-at-its-price to their own. Shrink the triangulation and the rainbow triangle shrinks to a single perfectly envy-free split. Fairness exists for the same reason a stirred coffee has a still point.

### It runs deeper than a metaphor

This isn't a loose "rent is kind of like a triangle" gesture. The set of divisions genuinely *is* the simplex; the housemates' preferences genuinely *are* a Sperner colouring; and the guaranteed existence of a fair split is the guaranteed existence of the rainbow triangle, which is Brouwer's fixed point in combinatorial clothing. Francis Su turned this into the actual algorithm (*"Rental Harmony," 1999*), and he and Alina Peysakhovich built it into the *New York Times*' "To Divide the Rent, Start With a Triangle" calculator (2014) — you answer "which room would you pick?" a few times and it walks the triangulation to your envy-free rent.

The assumptions are worth knowing, because they're where reality can bite: preferences must be well-defined at every price (no "I'm not sure"), and "never refuse a free room" quietly assumes the rooms are goods, not bads — if a room is so awful someone would pay to *avoid* it, the boundary condition breaks. But within those bounds the guarantee is absolute: a colouring lemma about triangles proves that three friends can always split the rent so that nobody, honestly asked, would trade.

*If you'd like, the natural companion to this post is a live triangle you can drag — I can build the interactive solver as a follow-up.*
