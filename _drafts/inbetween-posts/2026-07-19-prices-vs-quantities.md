---
layout: post
title: Fix the Price, or Fix the Amount?
subtitle: Carbon tax versus cap-and-trade is not an ideology. It's a second derivative.
---

Suppose you want to cut pollution. You have two instruments. You can set a **price** — a tax of so many dollars per tonne emitted — and let firms decide how much to emit. Or you can set a **quantity** — a hard cap of so many tonnes, sliced into tradeable permits — and let the market decide the price. Carbon tax, or cap-and-trade.

These get argued about as though they were tribal totems: the tax a blunt statist levy, the cap a clever market. But the actual difference between them is a piece of mathematics so clean it's almost rude, and it turns out to hinge on the *curvature* of a damage curve. Let me build it up, because it's a lovely instance of a duality I've written about before quietly breaking under uncertainty.

### Under certainty, they're the same thing

Start with the easy case: the regulator knows everything — the firms' costs of abating, the damage each tonne does. Then there is an optimal amount of pollution (where the marginal cost of cutting one more tonne equals the marginal damage that tonne causes), and you can hit it *either way*. Set the cap at that quantity, or set the tax at that marginal-damage price, and you land on the identical point. The optimal tax and the optimal cap are two names for one outcome.

This is exactly the [primal/dual duality from the socialist-calculation problem]({{ site.baseurl }}): the cap is the **primal** instrument — you fix the *quantity* directly — and the tax is the **dual** instrument — you fix the *shadow price*, the Lagrange multiplier on the pollution constraint, and let the quantity fall out. Set either optimally and the other is implied. Under perfect information, choosing between a price and a quantity is like choosing whether to describe a rectangle by its width or its area. Same rectangle.

### Uncertainty breaks the symmetry

Now take away the regulator's crystal ball. In practice they *don't* know the firms' abatement-cost curve — how expensive it really is to cut the next tonne. And the moment there's uncertainty, the two instruments stop being the same act:

- Set a **tax**: firms abate up to where their marginal cost meets the tax, so the *price* is nailed down but the *quantity* floats, wherever the unknown cost curve happens to put it.
- Set a **cap**: the *quantity* is nailed down but the marginal cost — the permit price — floats, wherever the unknown cost curve happens to put it.

You are no longer choosing a description of a known rectangle. You are choosing **which variable to leave exposed to the uncertainty.** One of price and quantity will come out wrong; you get to pick which.

### Weitzman's answer: it's the slopes

So which should you leave to chance? Martin Weitzman answered this in 1974, and the answer is entirely about the *relative slopes* of the marginal-benefit (avoided-damage) and marginal-cost curves near the optimum.

The intuition is a story about the cost of a mistake. Whichever instrument you pick, you'll misjudge the cost curve and end up off the optimum, eating some deadweight loss — a little triangle of wasted welfare. The size of that triangle depends on how steep the *other* curve is:

- If the **marginal damage curve is steep** — a threshold, a tipping point, where a bit too much pollution is catastrophic and a bit too little is nearly free — then getting the *quantity* wrong is ruinous. **Use a cap.** Nail the amount; let the price take the strain. (This is the ozone/CFC case: there's a cliff, so you fix the quantity and phase it to zero.)
- If the **marginal damage curve is flat** — a stock pollutant, where one year's emissions barely move an accumulated total, so the exact amount this year hardly matters — then quantity errors are cheap, but forcing firms into wildly expensive abatement under a rigid cap in a bad-luck year is very costly. **Use a tax.** Nail the price; let the amount take the strain.

That's the whole theorem: **pick the instrument that fixes the variable whose curve is steep, and leaves exposed the variable whose curve is flat.**

### Which makes carbon a tax problem

Carbon dioxide is close to a pure *stock* pollutant. What harms the climate is the total accumulated in the atmosphere over a century; a single year's emissions are a rounding error on that stock. So the marginal-damage curve, over any one year's range, is nearly **flat** — and Weitzman's rule says: fix the price. A carbon **tax** dominates a hard annual cap, because the thing you don't want floating around is the *cost* to the economy, not the exact tonnage in any given year.

And the practical punchline is the best part, because it dissolves the whole tax-versus-cap fight. The efficient design is a **hybrid**: a permit market (a quantity instrument) with a price *floor* and *ceiling* — a "safety valve." Read it in the duality language and it's exactly right: you fix the primal quantity for the long run, but you **clamp the dual variable** whenever it strays too far, capping how high or low the shadow price is allowed to go. Best of both, and it's what real systems (the EU ETS, California) have drifted toward.

### The thing worth taking away

Here's the idea I actually care about, stripped of pollution. Under certainty, "fix the price" and "fix the quantity" are the *same decision* — primal and dual, two faces of one optimum. Under uncertainty they come apart, and **which of the two you should pin down is decided by the curvature of the objective** — the second derivative of the damage function. Not by politics, not by whether you trust markets or the state. By a Hessian.

Most of the time, when two camps are shouting about instruments — tax or cap, rules or discretion, price or quantity — they're fighting about ideology over the top of a question that has a real answer, and the answer is a shape: how sharply does it hurt to be wrong in each direction? Draw the two curves, look at which one is steeper, and the argument is over.
