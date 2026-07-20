---
layout: post
title: What's the Future Worth?
subtitle: The entire economic argument over climate change is a fight about one number
---

The public climate debate pretends to be about science — how much will it warm, how bad will it get. But the science, for policy purposes, has been settled enough for years. The fight that actually determines what we *do* — how fast to decarbonise, how many trillions to spend now — happens one level downstream, in economics. And the economics, when you chase it to the bottom, reduces to a single number. Not a fact about the atmosphere. A number about how much we care.

That number is the **discount rate**, and I find it the cleanest example I know of a civilisation-scale argument that is secretly a disagreement about one parameter — with an ethical choice smuggled inside it, doing all the work while dressed as a technical input.

### Why there's a number at all

Climate policy is a trade: pay costs *now* (build the grid, retire the coal) to avoid damages *later* (decades, centuries out). To decide whether the trade is worth it you have to put present costs and future benefits in the same units, and that means converting future value into present value — *discounting*. A dollar of damage in year $t$ is worth $(1+r)^{-t}$ today, where $r$ is the discount rate.

The trouble is that discounting is *exponential*, so over climate timescales tiny differences in $r$ explode. Take \$100 of damage a century from now. At a discount rate of 1.4% it's worth about \$25 today. At 4.3% it's worth about \$1.45. Same damage, same century — a **seventeen-fold** difference in how much we should spend to prevent it, from nothing but the choice of rate. Push it to two centuries and the gap becomes astronomical. The "social cost of carbon" — the dollar damage of emitting one more tonne — swings by an order of magnitude on this one dial. It's the [compounding I keep coming back to]({{ site.baseurl }}/poker-eval): small rates, long times, enormous stakes.

### Splitting the number into ethics and fact

The Ramsey equation decomposes the discount rate:

$$r = \delta + \eta\, g.$$

- $\delta$ is **pure time preference** — how much less you weight future welfare *just because it's in the future*. Raw impatience.
- $\eta$ is how fast the marginal value of a dollar falls as people get richer (an inequality-aversion knob).
- $g$ is the expected growth rate of consumption — future people will probably be richer, so a dollar means less to them.

The important thing about this split is that $g$ is *empirical* — you can go and measure growth — but $\delta$ and $\eta$ are *ethical*. They are not facts about the world; they are statements about how much strangers in the future are worth to you. And that's where the whole debate actually lives.

### The two camps ran the same model and got opposite answers

The **Stern Review** (2006) set $\delta \approx 0.1\%$ — essentially zero. Stern's argument was moral: to discount a future person's welfare simply because they are born later is, in his words, ethically indefensible — a bias, not a rate. The *only* legitimate reason to discount pure welfare is the small chance that humanity isn't around to collect, an extinction hazard. With near-zero impatience the discount rate comes out around **1.4%**, and the conclusion is: act hard, act now, the future damage is enormous in today's money.

**William Nordhaus** (Nobel, 2018) took the descriptive route: set $\delta$ to match the impatience that markets *actually reveal* through observed interest rates, around 1.5%, giving a discount rate near **4.3%**. The conclusion is a gentle "policy ramp" — decarbonise, but gradually; the far-future damages, discounted at market rates, just aren't worth vast spending today.

Same climate science. Same economics. Same equations. The multi-trillion-dollar difference in what they tell us to do is *almost entirely* the choice of $\delta$ — a parameter encoding how much a person in 2200 is worth relative to you. The argument about whether to save the world is, underneath the models, an argument about a decimal place.

### The thing hiding in the parameter

Here is why I don't think this is a technical question that happens to have ethical flavour. It is an ethical question wearing a technical disguise, and you can see it in the descriptive-versus-prescriptive split. Nordhaus says: use the rate markets reveal. But the rate markets reveal is the impatience of *the currently living* — and the people the decision most affects, the ones in 2200, are not in the market. They can't bid, can't vote, can't bargain. A positive pure-time-preference is a tax we levy on people for the accident of [being born later]({{ site.baseurl }}), set unilaterally by us, the only party in the room.

My own bias here is not neutral, and it's worth stating because it comes from a completely different direction. In [why future rewards are worth less]({{ site.baseurl }}/discounting-via-uncertainty) I argued that the discount factor in reinforcement learning isn't impatience at all — it's the Bayesian probability that the reward opportunity *survives* to be collected. Read that way, the only defensible $\delta$ is genuine survival risk: the chance the future doesn't arrive. "Caring less just because it's later" has no home in that account — it isn't a rate, it's a distortion. Which is Stern's ethical claim, re-derived from an entirely unrelated corner of maths. When the reinforcement-learning story and the moral-philosophy story point at the same near-zero $\delta$, I start to believe it.

And uncertainty pushes the same way twice over. If future growth $g$ is itself uncertain, the *effective* discount rate should **decline** over time (Weitzman, Gollier) — the far future gets *more* weight, not less, because you must hedge against exactly the low-growth worlds where the damages bite hardest. Worse, Weitzman's "dismal theorem" shows that fat-tailed catastrophe risk can make expected damages blow up, breaking marginal cost-benefit analysis altogether: when ruin has non-negligible probability, the possibility of ruin dominates any discount rate you choose. Honest [uncertainty]({{ site.baseurl }}/danger-of-utility), the great solvent, dissolves the case for a high rate from a second direction.

### The number is where the ethics went to hide

None of this makes the discount rate *unimportant* — it makes it the most important number in the debate, and the one least examined in public, precisely because it's buried in an appendix labelled "assumptions." We have taken the largest moral question of the era — *how much do we owe people who do not yet exist?* — converted it into an actuarial parameter, and then argued about the parameter as though it were a fact about compound interest.

It isn't. Name it out loud and the climate debate stops being about science and becomes what it always was underneath: a question about how much a stranger in the future is worth to you, right now, in dollars. Everyone has an answer to that. Most people have just never been told that theirs is spelled $\delta$.
