---
title: Elucidating the Design Space of Governance Mechanisms
subtitle: 
layout: post
---

In our previous post, "[The DAO Proving Ground](%7B%7B%20site.baseurl%20%7D%7D/dao-proving-ground/)", we argued that building aligned DAOs is a critical step toward solving the larger challenge of AI alignment. We introduced a model where a DAO's state converges toward the token-weighted geometric median of its members' beliefs.

However, that model, based on a simple 1-token-1-vote mechanism, represents just one point in a vast and largely unexplored territory. The true power of DAOs lies in their programmability—the ability to experiment with entirely new forms of governance.

To navigate this territory, we need a map. This post introduces a framework for understanding and comparing governance mechanisms, turning a confusing landscape of options into a structured design space. By breaking down governance into its fundamental components, we can begin to engineer organizations with intention.

### A Framework for Governance Design

At its core, any governance system must answer a series of fundamental questions: Who gets to participate? Where does their power come from? How do they express their preferences? How are those preferences combined into a single decision? And when does this all happen?

This gives us a five-part framework for analyzing any governance mechanism:

1.  **Eligibility (`Who can participate?`)**
    This defines the boundaries of the electorate. Is participation open to anyone who holds a token, or is it restricted to those with a verified identity or a proven reputation?

2.  **Power Source (`What gives a vote its weight?`)**
    This determines the distribution of power. Is voting power proportional to capital (tokens held), or does each person have equal weight? Does power come from expertise, or from the long-term commitment of one's stake?

3.  **Expression (`How do participants voice their preference?`)**
    This is the user interface of governance. Do members cast a simple "For/Against" vote, or do they rank a list of options? Can they express the intensity of their preference by staking capital, or express ultimate dissent by exiting the system entirely?

4.  **Aggregation (`How are preferences combined into a decision?`)**
    This is the core logic of the voting system. Is a decision made when a simple majority is reached, or does it require a supermajority? Does a proposal pass when its accumulated support crosses a threshold, or when a prediction market deems it wise?

5.  **Temporality (`When does the decision-making happen?`)**
    This defines the rhythm of governance. Does voting occur in discrete, time-boxed windows, or is it a continuous, ongoing process where support can be expressed and withdrawn at any time?

By using these five dimensions, we can deconstruct, compare, and ultimately design better governance systems.

### Exploring the Design Space: A Gallery of Mechanisms

Let's use this framework to explore some of the most prominent governance mechanisms, from the simple to the radical.

#### 1-Token-1-Vote (1T1V)
*   **The Idea:** The foundational model of DAO governance. Voting power is directly proportional to the number of tokens an agent holds.
*   **Governance Properties:** Simple, decisive, and capitalistic. It aligns decision-making power with economic stake but is vulnerable to plutocracy, where wealthy token-holders can dominate the system.

#### Conviction Voting
*   **The Idea:** A continuous voting mechanism where members stake tokens on proposals they support. The longer a stake is maintained, the more "conviction" (voting weight) it accumulates.
*   **Governance Properties:** It favors proposals with sustained, long-term support over those with fleeting hype. It resists flash attacks and gives persistent minorities a chance to pass proposals over time.

#### Ragequit (Moloch DAO)
*   **The Idea:** The ultimate minority protection. If a member disagrees with a passed proposal, they have a grace period to exit the DAO and withdraw their proportional share of the treasury.
*   **Governance Properties:** This creates a powerful incentive for the majority to avoid tyrannizing the minority. If a proposal is too controversial, the threat of a mass exit (a "bank run") forces compromise and consensus-seeking.

#### Liquid Democracy (Delegative Voting)
*   **The Idea:** A hybrid of direct and representative democracy. Members can either vote directly or delegate their voting power to a trusted expert, revoking this delegation at any time.
*   **Governance Properties:** It allows for specialization and can improve the quality of decision-making on complex topics. However, it can lead to informal centralization around a few popular delegates.

#### Holographic Consensus (DAOstack)
*   **The Idea:** A scalable, two-stage mechanism designed to manage attention. Members first stake tokens on proposals to "boost" them, betting that the wider community will approve them. Only boosted proposals move to a full DAO-wide vote.
*   **Governance Properties:** It acts as a decentralized filter, using economic incentives to surface the most promising proposals in large-scale DAOs where no one can evaluate everything.

### A Comparative View

Using our framework, we can place these mechanisms in a single table to see their design trade-offs at a glance.

| Mechanism | Eligibility | Power Source | Expression | Aggregation | Temporality |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1-Token-1-Vote** | Token-holders | Capital | Binary Choice | Summation | Discrete |
| **Conviction Voting** | Token-holders | Time/Conviction | Staking | Threshold Crossing | Continuous |
| **Ragequit** | Token-holders | Capital | Exit | Implicit Threat | Discrete |
| **Liquid Democracy** | Identity/Token | Presence (Delegatable) | Binary Choice | Summation | Discrete |
| **Holographic Consensus** | Token-holders | Capital (as risk) | Staking & Binary | Threshold & Summation | Two-Stage |

This framework reveals that governance is not a monolithic choice but a modular design space. The path forward is to treat governance as an engineering discipline: to prototype, simulate, and deploy these mechanisms in the real world. The DAO proving ground is open, and by rigorously exploring its design space, we can learn to build the aligned organizations of the future.