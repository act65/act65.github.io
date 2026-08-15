---
title: What does this institution maximise?
subtitle: Reading the objective off a mechanism, and why it is usually the wrong question
layout: post
permalink: /mechanism-design/inverse-mechanism-design/
tags:
  - research
  - mechanism-design
  - politics
  - mathematics
---

<!-- Arc C, post 3. Plan: plans/mechanism-design-series.md
     The post that only this blog would write. -->

<!-- Opening claim, borrowed from _drafts/old/2026-05-14-mechanism-design.md:
     every set of rules implicitly optimises for something, whether anyone designed
     it to or not. This post asks whether that something can be recovered. -->

## Three inverse problems that get conflated

| | Observe | Infer | Field |
|---|---|---|---|
| Inverse decision theory | one agent's choices | their utility | revealed preference |
| Inverse game theory | equilibrium play | everyone's payoffs | inverse game theory, multi-agent IRL |
| Inverse mechanism design | a mechanism's input–output map | the objective it serves | mostly open |

<!-- The third is the one wanted here, and it is structurally different: the "agent"
     is the mechanism, the "behaviour" is the social choice function, and the "reward"
     is a social welfare function over the population. -->

## The ceiling: Roberts' theorem

<!-- Roberts 1979. On an unrestricted domain of quasilinear valuations with at least
     three outcomes, every onto, dominant-strategy-implementable social choice function
     is an affine maximiser:

     $$f(v) = \arg\max_a \Big[ \sum_i w_i v_i(a) + \kappa(a) \Big]$$

     Read this as an answer to the inverse question and it is deflationary: on
     unrestricted domains the implicit objective is *always* weighted utilitarian, so
     the only thing to recover is the weights and the constant.

     Which is the useful part. It says the inverse question is only interesting on
     restricted domains — and that is exactly where real institutions live, since no
     real ballot admits arbitrary valuations. So domain restriction goes from a
     technical caveat to the thing the whole enterprise depends on. -->

## The other direction: Maskin monotonicity

<!-- Which social choice rules can be implemented at all. Monotonicity is necessary
     for Nash implementation; with no-veto-power and n >= 3 it is sufficient.

     This bounds the *reachable* objectives. A top-down programme that picks a social
     utility function and then searches for a mechanism serving it needs this, because
     a non-monotone target is not merely hard to hit, it is unreachable. -->

## What identification actually requires

<!-- Carry the Afriat lesson forward: expect a large answer set.
     What shrinks it — observing the mechanism off its typical profiles, observing it
     across varied populations, and structural assumptions stated as assumptions.
     What does not shrink it — more data of the same kind. -->

## The computational version

<!-- Data-driven mechanism design via multi-agent revealed preferences (2404.15391);
     differentiable inverse mechanism learning. Where these help and where they
     inherit the identification problem rather than solving it. -->

## What this would say about a real rule

<!-- Sketch only; the experiment belongs in /mechanism-design/reading-objectives/.
     Candidates worth the exercise: plurality, Borda, MMP, the proportional veto core. -->

## References
