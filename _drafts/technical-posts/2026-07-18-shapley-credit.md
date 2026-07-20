---
layout: post
title: Who Did the Work?
subtitle: The Shapley value — the one fair way to assign credit, and why it's also how we explain machine learning
categories:
  - play
---

Three of you share a taxi home. You'd have paid \$20 alone; the second person's stop adds \$10 to the fare; the third adds another \$6. The total is \$36. How do you split it *fairly*?

"Divide by three" (\$12 each) punishes the person who lived closest. "Everyone pays their own marginal leg" depends on the order you're dropped off, and the last person always gets gouged. Every rule you can think of either ignores someone's contribution or smuggles in an arbitrary ordering. Is there a *right* answer?

There is exactly one, and it was pinned down by Lloyd Shapley in 1953 — not by proposing a formula, but by writing down the properties any fair answer *must* have and proving only one thing satisfies them. It's the same move I love in [the Dutch book argument]({{ site.baseurl }}/uncertainty-via-bets) and [envy-free rent division]({{ site.baseurl }}): don't argue about the answer, argue about the axioms, and let uniqueness do the rest.

### The axioms

Model the situation as a *coalition game*: a set of players $N$, and a function $v(S)$ giving the value any sub-coalition $S$ could produce on its own. (For the taxi, $v$ of a group is the cost of the trip serving exactly those people.) A "solution" hands each player $i$ a number $\phi_i$. Demand four things:

1. **Efficiency.** The shares add up to the whole: $\sum_i \phi_i = v(N)$. Nothing lost, nothing invented.
2. **Symmetry.** If two players contribute identically to every coalition, they get the same share. Names don't matter, only contributions.
3. **Null player.** A player who adds nothing to any coalition gets nothing.
4. **Additivity.** If you run two games at once, each player's share is the sum of their shares in the two games. Credit is linear.

These are hard to argue with — each is close to a definition of "fair." And Shapley's theorem is that **exactly one** assignment satisfies all four.

### The formula, and what it means

$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\bigl[v(S \cup \{i\}) - v(S)\bigr].$$

Don't fight the factorials; read the story they tell. The bracket $v(S\cup\{i\}) - v(S)$ is player $i$'s **marginal contribution** — how much they add when they join the coalition $S$. The messy fraction is just the probability that, if all $n$ players showed up in a uniformly random order, $i$ would arrive to find exactly the group $S$ already there. So:

> **The Shapley value is your average marginal contribution, taken over every possible order in which the players could have arrived.**

That's the whole idea. The unfairness of "marginal cost" was that it depended on the arrival order and stuck the last person with the bill. The fix isn't to pick a better order — it's to average over *all* of them, so no ordering is privileged. The arbitrary choice is integrated away, exactly the trick that rescues [the probabilistic method]({{ site.baseurl }}/probabilistic-method) and Kelly betting.

Run it on the taxi and the closest passenger pays less than \$12 and the farthest more, but nobody is punished for the accident of drop-off order. Try it — it's a satisfying afternoon.

### Why this is really about credit assignment

Strip away "taxi" and "coalition" and this is the general problem of **credit assignment**: a group produced an outcome; how much of it is due to each part? That question shows up everywhere I keep poking at —

- **Machine learning explainability.** Which features drove this prediction? Treat each feature as a player and the model's output as $v$. The Shapley value of a feature is its fair contribution to the prediction — this is precisely **SHAP** (SHapley Additive exPlanations, Lundberg & Lee 2017), now the default tool for explaining black-box models. The fairness axioms become *desiderata for an explanation*: an irrelevant feature gets zero credit (null player), two identical features share credit equally (symmetry).
- **Reinforcement learning.** Which of my past actions deserves credit for this reward? — the [temporal credit-assignment problem]({{ site.baseurl }}) is a coalition game played across time.
- **Science and authorship, cost-sharing, cartel profits, network-toll allocation.** All the same object.

The Shapley value is what "fair share" *means* once you insist on those four axioms. That's why it keeps being rediscovered under different names.

### The catch (which is the interesting part)

The sum runs over every subset $S$ — there are $2^n$ of them. The uniquely fair answer is **exponentially expensive to compute**, and for anything past a couple of dozen players you can't evaluate it exactly. So in practice everyone estimates it by *sampling* random orders — go back to the "average over arrival orders" reading, draw a few thousand orderings at random, average the marginal contributions. Monte Carlo rescues the intractable exact quantity, which is the same bargain as everywhere else: the clean object exists uniquely and provably, and [finding it cheaply is a separate fight]({{ site.baseurl }}/probabilistic-method).

There's even a deeper wrinkle worth a line. The four axioms feel neutral, but the additivity axiom in particular is a real commitment — weaken it, or add a notion of players who *must* cooperate, and you get other solution concepts (the core, the nucleolus, the Banzhaf index). "Fair" was never unconditional; it was always *fair given these axioms*. Which is the honest lesson of the whole exercise: fairness isn't found lying in the world, it's the unique consequence of the properties you were willing to insist on out loud.
