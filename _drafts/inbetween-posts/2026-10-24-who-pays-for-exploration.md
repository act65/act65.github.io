---
layout: post
title: Who pays for exploration?
subtitle: A society has to try new things, and someone always bears the cost of trying
permalink: /who-pays-for-exploration/
description: "A learning agent pays for its own mistakes. A society doesn't: its regret is a list, one entry per person, and turning that list into a single number is already a political choice."
tags:
  - essay
  - open-question
  - uncertainty
  - aggregation
  - power
  - politics
  - reinforcement-learning
---

A reinforcement learning agent that wants to do well has to try things it isn't sure about. Some of those tries will be bad, and the agent will do worse in the short run than if it had stuck with what it knew. This shortfall is called regret, and the theory of exploration is mostly about how to keep it small.

What the theory takes for granted is that the agent pays its own regret. The one deciding to explore is the one who eats the bad outcome. That is what makes optimism reasonable: if I try the unfamiliar restaurant and it is terrible, I have had one bad dinner, I learned something, and nobody else was involved.

A society doesn't work like that. When a country tries a new tax, a new curriculum, a new way of running its hospitals, the people who choose the experiment are usually not the people who bear its cost. I've started to think this is a large part of what the argument between "conservatives" and "progressives" is actually about, and that it gets lost when the argument is framed as a disagreement about whether change is good.

<!-- TODO: consider opening with a clinical trial instead — a patient randomised to the arm that turns out worse is the cleanest picture of someone paying for an experiment. -->

### Regret becomes a list

For a single agent, regret is a number. For a society, it is a list: one entry for each person, recording how much worse off they were while the society was finding out.

The usual way to judge a collective decision is to add the list up. That is fine for asking how expensive the learning was. It throws away who paid. Two ways of learning the same thing can have the same total cost, with one spreading it thinly and the other landing it all on a few people.

So the step from one agent to many isn't just more agents. Choosing how to turn the list into a number — add it up, look at the worst-off entry, something in between — is itself a social choice. And I suspect that a lot of political disagreement that looks like it is about change is really about that choice.

There is a further thing the list makes visible: some entries are negative. While a society experiments, some people do *better* than they would have under the status quo. Exploration has winners as well as losers, and they are rarely the same people.

### It cuts both ways

The obvious version is the reformer who imposes risk on others. New Zealand's economic reforms from 1984 onwards were designed by a small group in the Treasury and the Labour cabinet and implemented fast, partly so that they couldn't be unpicked. Whatever you think of the result overall, the cost of the transition was not spread evenly. It landed on particular towns, particular industries, and particular people — forestry and rail workers, many of them Māori — who were not asked.
<!-- TODO: check the specifics (Forest Service corporatisation 1987, Māori unemployment figures) before publishing. -->

But the status quo is not a neutral choice either. It is an experiment that has been running for a while, and its costs also land on particular people. Before 1986, sex between men was a crime in New Zealand. Keeping that law was the cautious option, and the people paying for the caution were gay men, who had not signed up for it either.

So the reformer spends other people's risk, and the conservative spends other people's opportunity. Both are putting entries on someone else's list.

And there is a cost flowing the other way too. Whoever tries something new also produces information that everyone else gets for free. Economists who study this, under the name *strategic experimentation*, find the predictable result: when the explorer pays and everyone learns, there is too little exploring. So the explorer is imposing risk on others and handing them knowledge at the same time, and I don't know how to net those off.

### When to be optimistic

There is still something useful in the single-agent picture, as long as you are careful about which part.

In *offline* reinforcement learning, where an agent has to learn from a fixed record and can't try anything, the good algorithms are pessimistic. Conservative Q-learning, for example, assumes anything it hasn't seen work is probably bad. This is Chesterton's fence: don't take down the fence until you know why it was put up, because you won't get a second chance to find out.

In *online* learning, where an agent can try something and see what happens, the good algorithms are optimistic. Upper confidence bound methods treat uncertainty as a reason to try a thing rather than avoid it, because trying is how you learn, and a bad try is recoverable.

So the right amount of optimism doesn't depend on whether change is good. It depends on whether mistakes can be seen and undone. (I tried to make this precise for constitutions in [Minimality from uncertainty]({{ site.baseurl }}/minimality-from-uncertainty/). One result is that the longer a rule will bind, the less it should rule out.)

That tells you *when* to explore, but not who carries it. I tried to work out who carries it when a society learns the "efficient" way, by maximising the total, and the answer is in [a companion post]({{ site.baseurl }}/regret-is-a-vector/). Roughly: the cost concentrates on whoever loses from policies that are *nearly* as good as the best one on average, but contested. Those are the policies a good learner has to try most often to rule out, and the people who lose from them pay most. That is often a minority. And this isn't a flaw of a particular algorithm: any learner that eventually finds the best total has to impose it.

So the question I actually care about is: what can a society do to shape who carries its regret?

### Shaping the list

Here are the options I can think of. None of them fully works, which is perhaps why the argument never ends.

**Only experiment when you genuinely don't know.** Medicine has the most developed answer to this, because clinical trials face the problem directly. A trial may only randomise patients when the relevant experts are genuinely uncertain which treatment is better — a principle called *equipoise*. Then nobody is knowingly given the worse option. Trials also get consent, and they are watched by a monitoring board that stops the trial early once one arm is clearly winning, which caps how much any participant can lose. I find it striking how much of this has no counterpart in how we change laws.

**Spread it at random.** A trial can randomise *who* gets the experimental treatment, so the cost is shared out by lottery rather than landing on whoever happens to be nearby. There is a stranger version in economics: if people won't volunteer to explore, a planner can manage what each person is told, so that nobody can tell whether they are being asked to try the new thing or the known-good one. The cost gets spread thinly and blindly, behind a kind of veil. It is fair in a sense, and it is also, quite literally, conscripting people into experiments.

The catch is that this only works when the thing being tested can be given to individuals. A drug can. A tax law, a curriculum, or an air-quality standard applies to everyone at once. You can't randomise who lives under it.

**Run many small experiments instead of one big one.** This is the nearest a public policy gets to randomising. Federal systems try different policies in different places; Louis Brandeis called the states "laboratories" of democracy. A bad experiment only hurts one place, and the rest can watch.

Where it breaks: the people in the experimenting place still didn't choose individually. Moving away is expensive, and least possible for the people most likely to be hurt. Many effects cross borders, and some policies only work at scale.

**Make it opt-in.** Pilot programmes with sign-up, charter cities people choose to move to.

Where it breaks: volunteers aren't typical, so the results may not hold for everyone else. Much of what a government does can't be opt-in. And consent from people with no good alternatives is a strange kind of consent.

**Make it reversible.** Sunset clauses, trial periods, pilots with a planned end. This tries to move a policy from the offline regime into the online one, where optimism is reasonable.

Where it breaks: temporary things stick. People make plans around the change, a constituency forms that depends on it, and the sunset gets renewed. Some of the US Patriot Act's "temporary" provisions were renewed repeatedly.
<!-- TODO: get a cleaner example, or a count. -->

There is a symmetric version I find more interesting: sunset clauses on *old* laws. If a law had to be re-justified every twenty years, the status quo would have to keep earning its place too.

**Cap anyone's share.** If losing your job in a failed reform means a lean few months and retraining, rather than losing your house, then the worst entry on the list is bounded. Denmark's "flexicurity" — easy to fire, generous support when you're out of work — reads to me as roughly this trade. It is the society-sized version of the trial's stopping rule.

Where it breaks: a safety net covers money better than it covers place, status, or community. And it is itself paid for by someone.

**Pay it back.** If a change makes most people better off and some worse off, the winners could compensate the losers. If compensation were easy and complete, who paid wouldn't matter: you could always even the list out afterwards. So in a sense the whole problem exists because compensation is hard.

Where it breaks: compensation is usually promised and rarely paid. It's hard to find the losers, especially later. Some losses aren't about money.
<!-- TODO: US Trade Adjustment Assistance is probably the standard example of compensation that was promised and underdelivered. Check. -->

**Make the explorer carry it.** Liability, insurance requirements, bonds posted up front. A mining company in many places has to post a bond to cover cleanup before it starts digging.

Where it breaks: the harm often shows up after the explorer is gone, bankrupt, or protected by limited liability. And for governments it mostly can't apply — the people who chose the policy have usually left office before the bill comes in.

### What I don't know

I don't know how to compare the risk a reformer imposes with the opportunity a conservative denies. They should be entries on the same list, and I'm not sure they can be measured in the same units.

I don't know whether consent is the right frame. If doing nothing is also an experiment, then every option puts costs on someone, and the question becomes how to share them out rather than how to avoid imposing them.

And I suspect most of the mechanisms above are really ways of making the list *visible*: knowing who is in an experiment, what it is costing them, and when it ends. Medicine does that. Legislation mostly doesn't. That might be most of the work.

<!--
Related posts to maybe link:
- In what sense is Bayesian updating optimal? (/bayes-optimal/) - minimal change in beliefs as the uncontroversial kind of conservatism
- Designing behind the veil (/governance-mechanisms/) - the veil connection in "spread it at random"
- Ten Sacks (/ten-sacks/) - who bears a flood's cost

Literature:
- Hossain, Micha & Shah (2021), Fair algorithms for multi-agent multi-armed bandits - regret in Nash welfare
- Kremer, Mansour & Perry (2014), Implementing the "wisdom of the crowd", JPE - incentivized exploration
- Bolton & Harris (1999); Keller, Rady & Cripps (2005) - strategic experimentation, under-exploration
- Freedman (1987), Equipoise and the ethics of clinical research, NEJM
-->
