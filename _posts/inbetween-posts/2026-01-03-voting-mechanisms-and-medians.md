---
title: The Geometry of Governance 
subtitle: A derivation / motivation of Liquid democracy via Vetor Quantisation
layout: post
categories:
    - economic
---

We often talk about politics in terms of ideology, history, or tribalism. But at its core, governance is an optimization problem. It is the challenge of aggregating the distinct, high-dimensional preferences of millions of people into a single output: policy.

If we strip away the campaign slogans and look at the math, we find that many of our frustrations with modern democracy—polarization, the "lesser of two evils," and the feeling of being unheard—are not bugs. They are geometric inevitabilities of the mechanisms we use.

In this post, I want to explore a formal framework for voting, show why the "Two-Party System" is mathematically equivalent to a lossy compression algorithm, and explore how we might break the "Curse of Dimensionality."

## 1. The Setup: Voters as Vectors

Let’s model the political compass not as a flat square, but as a high-dimensional space.

*   **The Space:** Imagine a space with $d$ dimensions. Each dimension represents a specific policy issue (e.g., Tax Rate, AI Regulation, Zoning Laws).
*   **The Voter ($v$):** Every citizen is a point in this space, represented by a vector $v \in \mathbb{R}^d$. This vector encodes their ideal preferences on every issue.
*   **The Society:** The electorate is a cloud of $m$ points distributed throughout this space.

The goal of any governance mechanism is to select a policy outcome—let’s call it vector $P$—that minimizes the collective unhappiness of the society. In geometry, "unhappiness" is simply distance. The further the outcome $P$ is from your position $v$, the more dissatisfied you are.

Ideally, we want to find the **Geometric Median**: the point $P$ that minimizes the sum of distances to all voters:

$$ \min_P \sum_{i=1}^m \| v_i - P \| $$

If we could achieve this, we would have the "most representative" compromise for society. So, how do we get there?

## 2. The Two-Party Trap ($k=2$)

In most modern democracies, we don't calculate the median directly. We use intermediaries: Political Parties.

A party is essentially a pre-packaged bundle of policies—a single "codeword" vector $c$ in that $d$-dimensional space. In a two-party system, the voter is presented with exactly two options: $c_A$ and $c_B$.

The voter’s job is simple: vote for the one closest to them.
The system’s job is effectively **k-means clustering** (with $k=2$). It tries to find the two centroids that minimize the error for their respective halves of the population.

### The Dimensionality Collapse
While this sounds efficient, it introduces a catastrophic mathematical flaw: **Dimensionality Collapse.**

Any two points ($c_A$ and $c_B$) define a straight line. By forcing voters to choose between them, the system projects the complex, $d$-dimensional variance of the population onto a **1-dimensional axis**.

*   If you care about an issue that aligns with this axis (e.g., "Left vs. Right"), you are represented.
*   If you care about an issue *orthogonal* (perpendicular) to this axis—say, a specific tech policy that neither party talks about—your preference is mathematically invisible.

To the system, your vote is just a single bit of information (0 or 1). It cannot capture the nuance of a $d$-dimensional vector. This leads to high **Distortion**—the gap between what voters want and what they get is mathematically guaranteed to be high.

## 3. Why not just add more parties? ($k=2^d$)

If $k=2$ is too crude, the natural intuition is to increase $k$. Why not have 5, 10, or 20 parties?

We see this in systems using **Mixed-Member Proportional (MMP)** representation or pure proportional representation (like in Germany, New Zealand, or the Netherlands). These parliaments often have 10+ parties, offering voters a wider menu than the binary choice in the US.

As we add more centroids (parties), the representation error does decrease (this is known as *Zador’s Bound* in quantization theory). However, even with 15 parties, we run into a hard limit: **The Curse of Dimensionality**.

Let’s assume distinct policy issues are binary (Yes/No). Let's take just three issues:
1.  **Progressive Wealth Tax?** (Y/N)
2.  **Nuclear Power Expansion?** (Y/N)
3.  **Universal Basic Income?** (Y/N)

*   To represent a voter who wants [Yes, Yes, Yes], you need a party with that exact platform.
*   To represent a voter who wants [Yes, **No**, Yes], you need a completely different party.

If a Green party supports the Tax and UBI but opposes Nuclear, the pro-Nuclear environmentalist is stranded. They must compromise.

To guarantee that *every* voter can find a party that represents their views on just $d=30$ binary issues, we would need a party for every possible combination. That is $2^{30}$ parties.

$$ 2^{30} \approx 1 \text{ Billion Parties} $$

This creates a paradox:
1.  **Few Parties ($k=2$):** Low choice cost, but terrible representation accuracy (high error).
2.  **Many Parties ($k \to \infty$):** Perfect representation, but impossible cognitive load (infinite search cost).

We cannot "party" our way out of this problem.

## 4. The Information Bottleneck

The fundamental problem here is **Information Theory**.

Traditional voting treats governance as a **Vector Quantization** problem. We are trying to compress the infinite complexity of human preference into a discrete, finite set of "buckets" (parties).

In a high-dimensional world (where $d$ is large), bundling issues together is an incredibly inefficient way to transmit information.
*   **Bundling:** "You must buy the whole menu. If you want the salad, you have to eat the steak."
*   **Result:** You throw away the steak. That is waste (or in our model, "dissatisfaction").

We need a mechanism that breaks the bundle.

## 5. The Solution: Unbundling (Liquid Democracy)

To break the curse of dimensionality, we must switch from **selecting** a vector to **constructing** one.

Instead of asking the voter to pick one of $k$ pre-fabricated bundles, we can decompose the vote into its $d$ constituent dimensions. This is the promise of **Liquid Democracy**.

In this framework:
1.  The system doesn't solve one massive clustering problem in $d$-dimensional space.
2.  It solves $d$ tiny clustering problems in 1-dimensional space.

If you care about Dimension 1 (Environment), you vote (or delegate) on that. If you are indifferent about Dimension 2 (Tax), you abstain or delegate to someone else.

Mathematically, this changes the scaling of the error. We no longer need $2^d$ parties to cover the space. By treating the policies as an **orthogonal basis**—building the policy vector element-by-element—we allow the voter to express a precise location in high-dimensional space without requiring an infinite menu of options.

### Summary
*   **Preferences** are high-dimensional vectors.
*   **Two-Party Systems** compress these vectors onto a single line, discarding most of the information.
*   **Multi-Party Systems** fail to scale because the volume of the space grows exponentially ($2^d$).
*   **Optimal Governance** requires unbundling: treating dimensions independently.

The math suggests that as long as we rely on bundling (rigid parties), we will always suffer from high distortion. To align governance with voter will, we don't need *better* parties; we need a mechanism that transcends them.