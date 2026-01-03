---
title: Tradition and Change
subtitle: Why We Need Both Conservatism and Progressiveness
layout: post
categories:
    - economic
---

In the public sphere, "conservatism" and "progressiveness" are viewed as warring tribes—mutually exclusive identities defined by opposing lists of policy preferences. You are either for the status quo, or you are for change.

However, if we strip away the political culture war and view these concepts through the lens of **machine learning and decision theory**, a different picture emerges. They stop being opposing ideologies and start looking like distinct functional modules required for an intelligent agent to survive.

The core argument of this post is simple: **To build a robust intelligence, you need to be conservative in your *beliefs*, but progressive in your *actions*.**

## Defining Terms: A Technical approach

Before proceeding, we must clear the semantic minefield. In this post, I am decoupling these terms from their typical left-right political associations (taxes, social issues, etc.). Instead, I am using them to describe mathematical strategies for handling information and uncertainty:

*   **Conservatism:** A bias toward "priors" (previous knowledge) and risk minimization. It prioritizes the stability of the model and prevents overreaction to noise.
*   **Progressiveness:** A bias toward "novelty" and exploration. It prioritizes the discovery of new optima, even at the cost of short-term regret or uncertainty.

In the language of Reinforcement Learning (RL), this is not a battle for dominance. It is the negotiation between **Exploitation** (leveraging what we know) and **Exploration** (learning what we don't).

## Conservatism: The Anchor of Belief

In a probabilistic framework, conservatism is the mechanism that prevents your worldview from collapsing every time you see an outlier. It is the domain of **Belief Updating**.

### The Bayesian Conservative
Consider **Bayes' Theorem**. When we update our beliefs, we calculate a posterior distribution $P(\theta|D)$ by combining our prior beliefs $P(\theta)$ with new evidence $D$.

There is a formal sense in which Bayesian updating is the "most conservative" possible strategy. The Principle of Minimum Cross-Entropy states that when we update a probability distribution to satisfy new constraints (data), we should choose the distribution that is "closest" to our prior. Mathematically, Bayes' rule minimizes the **Kullback-Leibler (KL) Divergence** between the new posterior and the old prior.

$$ P_{\text{new}} = \underset{Q}{\arg\min} \ KL(Q || P_{\text{prior}}) $$

In plain English: **Bayes' rule takes the smallest possible step away from your existing worldview necessary to account for the new data.**

This mathematical conservatism is a feature, not a bug. Without it, an agent suffers from "catastrophic forgetting"—it chases the most recent data point, ignoring the sum total of its past experiences.

### Learning from History (Offline RL)
We see this need for conservatism most clearly in **Offline Reinforcement Learning**. Here, an agent must learn a policy solely from a static dataset of past experiences (history), without the ability to interact with the world.

If such an agent is "optimistic" about states it hasn't seen, it will hallucinate value in the unknown and likely fail. Algorithms like **Conservative Q-Learning (CQL)** solve this by explicitly penalizing the value of unseen actions. They compute a lower bound on value, effectively saying: *"If I haven't seen it work in the past, I will assume it is dangerous until proven otherwise."*

This mirrors **Chesterton’s Fence**, the famous parable by G.K. Chesterton: if you see a fence blocking a road, you should not remove it until you understand *why* it was put there. In ML terms: the fence represents a high-value prior derived from a historical reward function. Ignoring it is a failure to model the system dynamics.

## Progressiveness: The Engine of Action

If conservatism builds the map, progressiveness is required to walk the territory. While conservatism is necessary for *modeling* the world, it is often suboptimal for *acting* within it.

### Optimism in the Face of Uncertainty
If an agent acts purely conservatively, it will get stuck in a "local optimum." It will repeat the same "safe" actions forever, never discovering that a much better reward exists just slightly off the beaten path.

To solve this, we need **Progressiveness**—often formalized as **Optimism in the Face of Uncertainty (OFU)**.

Consider the **Upper Confidence Bound (UCB)** algorithm. When deciding which action to take, the agent doesn't just look at the average expected reward ($\mu$). It adds an exploration bonus based on uncertainty ($\sigma$):

$$ \text{Value} = \mu(a) + \beta \cdot \sigma(a) $$

The agent effectively says: *"I am uncertain about this new path; therefore, I will assume it is excellent."*

This is the progressive instinct. It values the *potential* upside of the unknown more than the safety of the known. Without this bias toward novelty, efficient exploration is impossible.

## The Synthesis: Beliefs vs. Actions

The mistake in political discourse is thinking we must choose to be *either* a Conservative *or* a Progressive. In machine learning, we see that successful agents assign these roles to different parts of their architecture.

### 1. Be Conservative in your Beliefs (The Model)
When trying to understand what is true, we should be Bayesian. We should be skeptical of new claims that violate strong priors. We should learn from history (Offline RL) with a pessimistic bias, assuming that norms and traditions (Chesterton’s Fences) exist for a reason. This prevents us from being "fooled by randomness."

### 2. Be Progressive in your Actions (The Policy)
When deciding what to *do*, however, we must be optimistic. Provided we have a safety constraint (we shouldn't take risks that lead to total ruin), we should explore the unknown. We should act *as if* the unverified path might hold the solution. This is the only way to gather the new data required to update our conservative models.

### Conclusion

A system that is purely conservative in its actions will survive, but it will never improve. A system that is purely progressive in its beliefs will chase ghosts and eventually self-destruct.

The solution is not a "centrist" mix, but a dynamic tension. We need the mathematical rigor of conservatism to respect what we have learned so far, and the algorithmic optimism of progressiveness to find out what we might learn next.