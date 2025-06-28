---
title: The Price of Belief
subtitle: Deriving Probability from Rationality
layout: post
categories:
    - play
---

We are often told that probabilities are one of two things:
1.  **Frequentist:** An objective property of the world, like the long-run frequency of a coin landing heads.
2.  **Bayesian:** A subjective degree of belief in a proposition, a property of an observer's mind.

This apparent split can be confusing. How can something as rigorous as mathematics be based on a "subjective belief"?

The answer lies in a powerful argument that bridges the gap. We can derive all the rules of probability from a single, operational premise: **a rational agent will not willingly construct a set of beliefs that guarantees they will lose money.** This is known as being immune to a "Dutch Book," and it provides the logical foundation for the Bayesian framework. It ensures that subjective beliefs are at least coherent.

Let's build our system.

#### The Setup: The Rules of the Game

Imagine a market where we can trade contracts based on any well-defined event, E.

1.  **The Contracts:** For any event E, we can create two types of shares:
    *   A **YES(E)** share that pays **$1** if E occurs, and $0 otherwise.
    *   A **NO(E)** share that pays **$1** if E does *not* occur, and $0 otherwise.

2.  **The Price:** The price of a share is the amount a rational agent is willing to pay for it. We will call the price of a YES(E) share **p(E)**. This price represents the agent's personal probability of the event.

3.  **The Rational Agent:** Our agent is rational. This doesn't mean they are always right; it simply means they are **coherent**. They will not set prices for bets in such a way that a clever bookie can guarantee a profit by trading with them. A set of bets that leads to a guaranteed loss is called a "Dutch Book." Our agent's goal is to be immune to being Dutch Booked.

From these simple rules, we can derive the three core axioms of probability theory.

---

### The Derivation

#### Axiom 1: Probability is between 0 and 1. (0 ≤ p(E) ≤ 1)

*   **Can the price p(E) be greater than $1?**
    Suppose our agent sets the price of a YES(E) share at $1.10. A bookie could sell them this share. The agent pays $1.10. The best possible outcome for the agent is that E happens and they receive $1.00. They have suffered a guaranteed loss of $0.10. This violates our rule of rationality. Therefore, **p(E) ≤ 1**.

*   **Can the price p(E) be less than $0?**
    Suppose our agent sets the price at -$0.10. This would mean they would pay a bookie $0.10 to take the share off their hands. The bookie now has an asset that will either be worth $0 or $1, and they were paid to take it. This is a guaranteed profit for the bookie and a guaranteed loss for the agent. Therefore, **p(E) ≥ 0**.

Thus, to avoid a guaranteed loss, the price an agent assigns to any event must be between $0 and $1.

#### Axiom 2: The probability of a certain event is 1. (p(CERTAIN_EVENT) = 1)

Let E be an event that is *guaranteed* to happen. A perfect example is a tautology, like "a standard six-sided die will land on 1, 2, 3, 4, 5, or 6."
*   The YES(E) share is a guaranteed $1 payout. What is its fair price?
*   If the agent sets the price p(E) at anything less than $1, say $0.99, a bookie could buy the share. They pay $0.99 and are guaranteed to receive $1.00, for a risk-free profit of $0.01. The agent has accepted a guaranteed loss.
*   To be coherent, the agent must set the price of a guaranteed $1 payout to be exactly $1.

Thus, the probability of a certain event must be 1.

#### Axiom 3: The Addition Rule for Mutually Exclusive Events. (If A and B cannot both happen, then p(A or B) = p(A) + p(B))

Let A and B be two mutually exclusive events (e.g., A = "a die roll is 1", B = "a die roll is 2").

Consider two possible investment portfolios.

*   **Portfolio 1:** Buy one share of **YES(A or B)**.
    *   **Cost:** p(A or B)
    *   **Payout:** If A happens, you get $1. If B happens, you get $1. If neither happens, you get $0.

*   **Portfolio 2:** Buy one share of **YES(A)** and one share of **YES(B)**.
    *   **Cost:** p(A) + p(B)
    *   **Payout:** If A happens, the YES(A) share pays $1 and the YES(B) share pays $0 (since they are mutually exclusive). Total payout is $1. If B happens, the YES(B) share pays $1 and the YES(A) share pays $0. Total payout is $1. If neither happens, both pay $0.

Notice that the payout for Portfolio 1 and Portfolio 2 is **identical** in every possible future.

A rational agent must value two portfolios with the exact same payout at the exact same price. If they didn't—for instance, if they priced Portfolio 1 cheaper than Portfolio 2—a bookie could buy Portfolio 1 from them and sell them Portfolio 2, locking in a risk-free profit.

Therefore, to avoid being Dutch Booked, the costs must be equal:
**p(A or B) = p(A) + p(B)**

### Conclusion: Probability as Coherent Betting

We have started with a simple idea—don't build a system of bets that guarantees a loss—and derived the three fundamental axioms of probability.

This operational viewpoint, often called the Dutch Book argument, shows that probability isn't just an abstract feature of the world (the Frequentist view) or a purely arbitrary feature of the mind (a common mischaracterization of the Bayesian view).

Instead, it reveals the laws of probability as **the necessary logic for coherent reasoning under uncertainty**. They are the rules anyone must follow to ensure their personal, subjective beliefs don't contradict each other. It provides a powerful answer to the question, "Why should my degree of belief follow the probability axioms?"

The answer is simple: If they don't, you're guaranteed to lose.