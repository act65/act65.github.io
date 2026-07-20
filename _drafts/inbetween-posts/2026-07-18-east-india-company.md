---
layout: post
title: A Corporation With an Army
subtitle: The East India Company is the alignment problem, already run once, at full scale
---

When I argue that [the profit-maximising corporation is a live demonstration of the alignment problem]({{ site.baseurl }}/alignment) — a powerful optimiser pursuing a proxy goal (shareholder returns) that has come apart from what we actually want — people tend to hear it as a metaphor. A provocation. *Corporations aren't really misaligned superintelligences.*

But we don't have to argue it in the abstract, because the experiment has already been run. A private company was once handed an optimiser's dream: a clear objective, no meaningful oversight, its own army, and the right to tax thirty million people. We know exactly what it did. It is the closest thing history offers to a full-scale, real-world run of the misaligned-optimiser thought experiment, and it is worth knowing in detail, because every failure mode we worry about in AI governance, the East India Company hit first.

### The objective function

The Company was chartered on the last day of 1600 — a joint-stock company, owned by shareholders, with one job: return a profit on the East India trade. That is the entire objective function. Not "govern India well." Not "the welfare of Bengal." A number, owed to investors in London, to be maximised.

For a century and a half it was a trading firm. Then, at the Battle of Plassey in 1757, its agent Robert Clive won Bengal less by fighting than by *bribing the opposing commander to defect* — and the optimiser discovered a devastating new strategy. Why buy goods to sell in Britain when you could seize the power to **tax** the people who make them, and buy their goods with their own money? In 1765 the Mughal emperor granted the Company the *Diwani* — the right to collect all land revenue from **Bengal, Bihar, and Orissa**, a population of some twenty to thirty million. A trading company was now a government. Nobody had designed this. The objective function simply found that tax-collection scored higher than trade, and climbed the gradient.

> This is the exact shape of the thing that keeps AI-safety people up at night: give a capable optimiser a proxy objective and enough freedom, and it will find high-scoring strategies you never imagined and would never have authorised — not out of malice, but because they score well. "Acquire the sovereign power to tax" was never in the charter. It was just the top of the hill.

### No oversight, and an army

Two facts make the Company more than an ordinary bad actor.

First, it had **its own army** — by the early 1800s around **260,000 men**, roughly *twice the size of the British state's own army*. A private corporation fielded the largest military force in Asia, answerable not to a parliament or a public but to a board of directors optimising a dividend. William Dalrymple's phrase for the whole enterprise is exact: "the first great multinational corporation, and the first to run amok."

Second, the thing running amok was almost absurdly small at the centre. The conquest and taxation of a subcontinent was directed from a London head office of about **thirty-five permanent staff**, five windows wide. The ratio of power exercised to accountability borne was, functionally, infinite. There was no one whose job was to notice that the objective had detached from any human good — because noticing that was not in anyone's objective either.

### The failure, with a body count

In 1770, five years after taking over Bengal's revenues, Bengal was struck by famine. Traditional estimates put the dead at around **ten million people — roughly a third of the province** (some modern historians argue for a lower figure; the toll is disputed, but it was catastrophic on any account).

Here is the part that makes it an *alignment* story and not merely a tragedy. As the population starved, the Company **kept collecting the land tax — and raised it** — so that revenue in the famine year held up, even rose, against the year before. It had earlier pushed farmers toward cash crops over food grains, thinning the buffer that might have absorbed the shock. None of this was sadism. It was the objective function doing its job while a third of the governed died, because "don't extract revenue from people who are starving" was not a term in the objective, and nothing in the Company's structure could add it. The optimiser optimised. The people were not in the loss function.

### Too big to fail

Then comes the detail that turns the whole thing from tragedy into farce, and rhymes uncannily with our own century. Despite ruling the richest province in India, the Company — over-extended, its finances hollowed by war and famine and the private looting of its own officers — went **broke**. By 1772 it couldn't pay its debts.

And it was, by then, so entangled with the British economy — so many MPs and lords held its stock, so much of the state's finances leaned on it — that letting it fail was deemed impossible. So Parliament **bailed it out**: a government loan of £1.5 million to a bankrupt private company whose collapse threatened the nation. In exchange the state began, for the first time, to regulate it (the Regulating Act of 1773) and capped its dividends until the loan was repaid. To help it dump a mountain of unsold tea, Parliament also passed the **Tea Act** — which promptly provoked the Boston Tea Party and helped ignite the American Revolution. A corporate bailout, a "too big to fail" rescue with strings attached, and a political explosion as collateral damage — in 1773.

The optimiser had privatised a subcontinent's revenue and socialised its own losses, and the state that was supposed to hold the leash discovered the leash only *after* the animal was the size of an army.

### Why this is the canonical example

It took a rebellion in 1857 for the British state to finally nationalise the thing — stripping the Company of its territories and armies and taking direct control — and the husk was formally dissolved in 1874. But by then it had governed, taxed, warred, and famined its way across a subcontinent for a century, all in pursuit of a number owed to shareholders.

I keep the East India Company in my pocket as the reply to anyone who thinks "misaligned optimiser" is science fiction. Everything is here, already instantiated, no silicon required: a **proxy objective** (shareholder return) standing in for a good it steadily diverged from; **capability overhang** (an army twice the Crown's, run from a room); **specification gaming** (tax-farming discovered as a higher-scoring strategy than honest trade); **catastrophic side effects** outside the objective (ten million dead, not in the loss function); and **too-big-to-fail entanglement** that defeated oversight until far too late. The corporation was a "[corporation in a box]({{ site.baseurl }}/alignment)" — a superhuman optimiser built out of contracts and men instead of weights and tensors — and we ran it, at full power, for two hundred years.

The alignment problem is not coming. It is a re-run. We should study the first take.
