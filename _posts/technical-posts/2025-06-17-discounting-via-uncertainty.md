---
layout: post
title: Why are future rewards worth less than present rewards?
subtitle: A Bayesian Derivation of Discounting
categories:
    - research
---

In reinforcement learning, the discount factor, γ, is one of the first things we learn. It's the knob we turn to tell our agent how much it should care about future rewards. We're often given two primary justifications for its existence:

1.  **Mathematical Convenience:** For continuing tasks, an infinite sum of rewards can diverge. Multiplying future rewards by γt ensures the sum converges. A neat mathematical trick.
2.  **Survival Probability:** The agent might "die" at any step. γ is the probability it survives to the next step. A simple, intuitive model of risk.

While useful, these explanations can feel incomplete. They frame γ as an external constraint we impose on the agent. But what if discounting isn't just a trick or a simple model? What if it's a fundamental consequence of making decisions under uncertainty?

In this post, we'll argue that the discount factor can be derived directly from a Bayesian perspective. It is not a hyperparameter we set, but an **emergent property of an agent that rationally accounts for its own uncertainty about the world.**

### The Bayesian Worldview: Embracing Uncertainty

A standard RL agent often assumes it knows the true model of the world (the MDP). A Bayesian agent is more humble. It knows it *doesn't* know the true MDP. Instead, it maintains a posterior probability distribution, $p(M_i | \mathcal{D})$, over a whole space of possible MDPs, $\{M_1, M_2, ...\}$, given the data, $\mathcal{D}$, it has seen so far.

This posterior captures two types of uncertainty:
*   **Aleatoric Uncertainty:** The inherent randomness within a given MDP (e.g., a coin flip).
*   **Epistemic Uncertainty:** The agent's own uncertainty about which MDP is the true one (e.g., "Is the coin fair or biased?").

Practical algorithms like Thompson Sampling leverage this posterior to explore the world efficiently, but our focus here is on what this uncertainty implies for the value function itself.[^1]

### A Better Frame: The "Reward Opportunity"

The "survival of the agent" story is a good start, but it's brittle. A more general and powerful concept is the **"survival of the reward opportunity."**

Think about it. An agent doesn't need to "die" for a future reward to become inaccessible. A path could be blocked, a resource could be depleted by a competitor, or a strategic advantage could be lost. The world is still there, the agent is still active, but the path to the reward you were counting on has vanished.

Let's formalize this. For any state-action pair $(s,a)$, we can partition the agent's entire set of possible worlds into two groups:

1.  **$\mathcal{M}_{good}(s,a)$**: The set of "good" MDPs. In these worlds, taking action $a$ in state $s$ keeps the path to our desired future reward open.
2.  **$\mathcal{M}_{bad}(s,a)$**: The set of "bad" MDPs. In these worlds, taking action $a$ in state $s$ leads to a "dead end"—a transition to a state from which the future reward is permanently inaccessible.

The agent doesn't know which kind of world it's in. It only has its beliefs.

### The Derivation: Gamma as Posterior Belief

A rational Bayesian agent must calculate its Q-value by averaging over all possibilities, weighted by its posterior belief. The value of an action is the expectation of its value across all possible worlds:

$$ Q^{\text{Bayes}}(s, a) = \mathbb{E}_{M_i \sim p(M_i|\mathcal{D})} [ \text{Value if } M_i \text{ is true} ] $$

We can split this expectation over our two sets of models:

$$ Q^{\text{Bayes}}(s, a) = \sum_{M_i \in \mathcal{M}_{good}} p(M_i|\mathcal{D}) \cdot (\text{Value}_i) + \sum_{M_i \in \mathcal{M}_{bad}} p(M_i|\mathcal{D}) \cdot (\text{Value}_i) $$

For the sake of a clear derivation, we'll make a simplifying assumption: in "bad" worlds, the future reward opportunity is gone, so its value is exactly zero. Let's call the value of the future reward stream in the "good" worlds $V_{future}$.

The equation simplifies beautifully:

$$ Q^{\text{Bayes}}(s, a) = \left( \sum_{M_i \in \mathcal{M}_{good}} p(M_i|\mathcal{D}) \right) \cdot V_{future} + \left( \sum_{M_i \in \mathcal{M}_{bad}} p(M_i|\mathcal{D}) \right) \cdot 0 $$

$$ Q^{\text{Bayes}}(s, a) = \left( \sum_{M_i \in \mathcal{M}_{good}(s,a)} p(M_i | \mathcal{D}) \right) \cdot V_{future} $$

Look closely at the term in the parenthesis. It is the agent's total belief—its summed posterior probability—that it is currently in a "good" world where the reward opportunity will continue.

This is our emergent discount factor. We can define a state-and-action-dependent discount factor, $\gamma(s,a)$, as precisely this belief:

$$ \gamma(s,a) \equiv \sum_{M_i \in \mathcal{M}_{good}(s,a)} p(M_i | \mathcal{D}) $$

The Bellman equation for our rational Bayesian agent becomes:

$$ Q^{\text{Bayes}}(s, a) = \text{ImmediateReward}(s,a) + \gamma(s,a) \cdot V_{future} $$

The discount factor is no longer an external parameter. It is the agent's own rational, data-driven assessment of the risk that its plan will be invalidated.

### An Example: The Two Caves

Let's make this concrete. An agent stands at the entrance of a cave system. It knows from a tattered map that there are two possible layouts:

*   **Cave A (Model $M_A$):** A short path leads to a treasure of +100.
*   **Cave B (Model $M_B$):** The path leads to a dead-end pitfall (future value 0).

The agent sees some claw marks on the entrance wall. Based on this data $\mathcal{D}$, it updates its posterior belief:

*   $p(M_A | \mathcal{D}) = 0.6$ (60% chance it's the treasure cave)
*   $p(M_B | \mathcal{D}) = 0.4$ (40% chance it's the pitfall cave)

The agent considers the action "Walk forward."
*   The set of "good" models for this action is $\mathcal{M}_{good} = \{M_A\}$.
*   The set of "bad" models is $\mathcal{M}_{bad} = \{M_B\}$.

The effective discount factor for this specific action is the agent's belief that it's in the good cave:

$$ \gamma(\text{entrance}, \text{walk}) = p(M_A | \mathcal{D}) = 0.6 $$

The rational value of walking forward is not the full +100. It is the value of the future reward, discounted by the agent's profound uncertainty about the world's structure:

$$ Q(\text{entrance}, \text{walk}) = 0.6 \times (+100) = 60 $$

If the agent takes a step and sees a gold coin, its posterior for $M_A$ might jump to 0.95. Its γ for the *next* step would then become 0.95. The agent becomes more "patient" as its epistemic uncertainty reduces.

### A More Rational Gamma

This derivation reframes discounting from a simple heuristic to a cornerstone of rational agency.

1.  **Source:** Discounting arises from the agent's **epistemic uncertainty** ($p(M|\mathcal{D})$) about the world's true model.
2.  **Mechanism:** This uncertainty is resolved over underlying environments that contain **aleatoric uncertainty**, where reward opportunities can live or die.
3.  **Dynamic Nature:** This stands in contrast to the single, fixed discount factor used in most RL algorithms. A constant γ implies the agent believes the risk of losing a reward opportunity is the same everywhere, for every action. The Bayesian perspective reveals that a truly rational agent should have a dynamic and nuanced sense of risk, becoming more "patient" (higher γ) in situations it understands well, and more "impatient" (lower γ) when facing high uncertainty.
4.  **Result:** The discount factor $\gamma(s,a)$ is an **emergent property of Bayesian inference**. It is the agent's rational, data-driven assessment of risk for every single decision it makes.

So the next time you set a `gamma` in your code, remember what it truly represents: a belief about the future. And perhaps the ultimate goal is not to tune γ, but to build agents that can learn their own γ from experience.

***

#### References
[^1]: For a thorough introduction to Thompson Sampling and its application in reinforcement learning, see "A Tutorial on Thompson Sampling" by Russo et al., 2018. It provides a great overview of how posterior sampling can be used to balance exploration and exploitation.
[^2]: Dearden, R., Friedman, N., & Russell, S. (1998). "Bayesian Q-learning." Proceedings of the Fifteenth National Conference on Artificial Intelligence. This is a foundational paper on incorporating Bayesian methods directly into Q-learning.
[^3]: Guez, A., Silver, D., & Dayan, P. (2012). "Efficient Bayes-Adaptive Reinforcement Learning using Sample-Based Search." Proceedings of the 26th Annual Conference on Neural Information Processing Systems. This paper explores practical methods for acting in a Bayes-optimal way.