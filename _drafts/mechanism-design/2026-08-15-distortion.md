---
title: How bad is a ranking?
subtitle: Putting a number on what ordinal ballots throw away
layout: post
permalink: /mechanism-design/distortion/
tags:
  - tutorial
  - mechanism-design
  - mathematics
  - politics
---

<!-- Arc B, post 2. Plan: plans/mechanism-design-series.md

     Why this post matters to the rest of the blog: /governance-mechanisms/ argues the
     social utility function is a *surrogate loss* for regret, and asks the right
     questions about surrogates (is it calibrated, how big is the gap). Distortion is
     that gap, for the specific surrogate "ordinal rule standing in for cardinal
     welfare". It is the one place the framework's question already has an answer. -->

## The question

<!-- Voters have cardinal utilities. Ballots collect rankings. The rule picks a winner
     from rankings. How much welfare can that lose, in the worst case?

     distortion(rule) = sup over profiles of [ max_x sum_i u_i(x) ] / [ sum_i u_i(rule(profile)) ] -->

## Unrestricted utilities: the bad news

<!-- Procaccia & Rosenschein 2006. With only a normalisation constraint, distortion
     grows with the number of alternatives — Omega(m^2) for deterministic rules.
     So the answer to "how much does ordinality cost" is, unrestrictedly, "a lot". -->

## Metric utilities: the good news

<!-- Anshelevich, Bhardwaj & Postl 2015. Assume voters and candidates sit in a metric
     space and utility is minus distance — the spatial model that /voting-geom/ already
     assumes. Now distortion is bounded by a constant.

     Copeland gives 5. The lower bound for any deterministic rule is 3.
     Gkatzelis, Halpern & Shah (2020) close the gap with a rule achieving exactly 3. -->

## The rule that achieves 3

<!-- Plurality Veto / plurality matching. Worth describing in full because it is short,
     it is not one of the classical rules, and its optimality is not obvious. -->

## How much should we ask voters to say?

<!-- The distortion–communication tradeoff (Caragiannis–Procaccia and successors).
     Distortion as a function of bits elicited per voter. This is the same axis as
     the rate–distortion framing in /voting-geom/ — worth making the connection
     explicit, and worth being careful that the two "distortions" are different
     quantities that happen to trade off against the same resource. -->

## Back to normalisation

<!-- The open question left by /sct/: L1 vs L2 normalisation of cardinal ballots was
     argued there on a single constructed profile. Distortion is the tool that decides
     it properly, and the answer may not be the one that post assumed. -->

## References
