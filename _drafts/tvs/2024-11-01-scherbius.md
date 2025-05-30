---
title: "How to play as Scherbius"
subtitle: "Being bayesian"
layout: post
permalink: /turing-vs-scherbius/scherbius/
categories:
    - "tutorial"
---

## Tutorial for Scherbius: The Art of Deception & Paranoia

Greetings, Agent Scherbius. You wield the mighty `EasyEnigma` to shield your strategies from Turing's prying eyes. But encryption is a cat-and-mouse game. Turing *will* try to break your code. Your challenge: know when he's succeeded, or when he's just lucky, and decide if it's time to pay the cost and re-encrypt.

**The Core Problem: Has Turing Cracked Your Code?**

When Turing wins a battle. Is it because:
1.  **He's lucky?**
2.  **He's broken your current Enigma settings and knows your *true* cards?**

You need to maintain a "belief state" – a running assessment of how likely it is that Turing has compromised your current encryption. This is like being a (Bayesian) spy master.

So, how do these two different states appear different?

1. Turing doesn't know your cards, and ...

We can calculate his chance of wining;

we know
<!-- want to use inequalities to bound!? -->


2. Turing does know you cards and is taking the minimax actions (minimum number of wins that maximise the chance of winning).

(this is where the real mind games come in. as maximising the chance of winning might include losing lots so instill false confidence in your current encryption)