---
layout: post
title: Prices are Lagrange Multipliers
subtitle: The socialist calculation debate was an argument about who computes the gradient
---

The great twentieth-century argument about central planning is usually taught as a fight between two moral teams: markets versus the state, freedom versus control. I think that framing hides what the argument was actually about, which is a question in optimisation, and which we are quietly re-running right now with better hardware.

### The debate, briefly

In 1920 Ludwig von Mises made a sharp claim: **rational economic calculation is impossible under socialism.** Not immoral — impossible. If the state owns all the means of production, there is no market for capital goods, hence no prices for them, hence no way to compare two plans and know which wastes less steel. Without prices you are flying blind. You can produce *things*, but you cannot know whether you produced the *right* things.

Hayek sharpened it in the 1930s and 40s into something deeper than "you need prices." His claim was about *knowledge*. The information a planner would need — who wants what, what is scarce where, what a machine's operator learned this morning that isn't written down anywhere — is dispersed across millions of heads, largely tacit, and changing by the minute. No central mind can gather it in time. A price is a device that compresses all of that local, perishable knowledge into a single number that everyone can act on without knowing where it came from. It is a communication protocol, not a moral fact. (This is [belief number four of capitalism's four beliefs]({{ site.baseurl }}/capitalism-core): the all-knowing market.)

Oskar Lange fired back with *market socialism*: fine, the planner doesn't need to *know* the equilibrium prices, the planner can *find* them the way a market does — announce prices, watch which goods pile up unsold and which sell out, nudge the surplus ones down and the scarce ones up, iterate. A Central Planning Board can play auctioneer and grope its way to equilibrium (Walras called it *tâtonnement*, "groping").

### The reframing

Strip the politics and here is the object all three were circling. An economy is trying to solve a constrained optimisation:

$$\max_{\text{plan}} \; \text{(total welfare)} \quad \text{subject to} \quad \text{(you can't use more steel than exists, for every resource).}$$

Write the Lagrangian for that problem. Every resource constraint gets a multiplier. And the multiplier on the steel constraint is precisely the *marginal welfare of one more tonne of steel* — how much better the whole plan could do if the world coughed up one more unit. That number is the price of steel. Not "like" the price. In the KKT conditions of the optimum, the shadow prices *are* the dual variables. Prices are Lagrange multipliers.

This isn't a cute analogy retrofitted afterwards. Leonid Kantorovich discovered linear programming in 1939 doing exactly this — optimising Soviet plywood production — and found the multipliers falling out of the maths. He had to call them "objectively determined valuations," because calling them *prices* was ideologically radioactive in Stalin's USSR. He was sidelined for years for having accidentally re-derived the thing the system was built to abolish, and eventually got a Nobel for it (1975). The dual variables do not care about your politics.

So the whole debate collapses to a single question: **how do you compute the dual variables?**

- The **market** is a decentralised, asynchronous, gradient-free algorithm for finding them. Every agent does local hill-climbing on their own tiny piece; the auction/tâtonnement process converges the multipliers. Nobody computes the whole thing; the computation is smeared across the entire population, running where the data already lives.
- **Central planning** tries to solve the primal problem directly, on one machine, having first shipped all the data to that machine.

In this language Hayek's real claim is a claim about *computational and communication cost*: the problem is too large and too non-stationary to solve centrally within the time you have, and the distributed algorithm wins not because markets are sacred but because it puts the computation where the information is and never has to move the data.

### The modern twist

Which means the answer is not a moral constant. It is an empirical quantity that *moves with the cost of compute and the cost of measurement* — the two things I keep coming back to on this blog.

And both have moved. Walmart and Amazon are internally *planned* economies — larger, by throughput, than the Soviet Union ever was — and they allocate not by internal prices but by algorithm, forecast, and fiat. (This is the argument of *The People's Republic of Walmart*: the most successful capitalists on Earth run their own guts as command economies because, at that scale, planning is now cheaper than internal markets.) The calculation debate is being answered, firm by firm, and part of the answer is turning out to be "centralise it, we have the compute now."

So what still resists central computation? Three things, and naming them tells you exactly where markets are load-bearing and where they are decoration:

1. **Preference and tacit knowledge.** Letting people *buy* is an astonishingly cheap sensor for what they want. Revealed preference costs the planner nothing and can't easily be faked. Surveying it directly is expensive and lossy.
2. **Incentive-compatibility.** The market makes agents *reveal* their private information because lying costs them their own money. A planner has to *extract* that information from agents who have every reason to game the plan — which is [tax law as an adversarial game]({{ site.baseurl }}/adversarial-tax-setting) all over again. This is the failure that sank real planning far more than raw arithmetic did.
3. **Non-convexity.** Increasing returns, externalities, public goods — these break duality. When the problem is non-convex the multiplier may not exist, or may exist and *lie*. Which gives a clean one-line definition worth keeping: **a market failure is a duality gap.** The places where the price is not a valid shadow price are exactly the places the market misprices the world, and they are exactly the places I spend most of the rest of this blog complaining about.

The socialist calculation debate was never socialism versus capitalism as tribes. It was primal versus dual, centralised versus distributed, and the correct answer is a function of two numbers that are still falling. We are re-running the calculation right now — and this time the planner has GPUs.
