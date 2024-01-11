---
layout: post
title: Probabilistic Inference in Reinforcement Learning Done Right
permalink: rl-as-inference
rating: 6
ref: https://arxiv.org/abs/2311.13294
subtitle: Review with some thoughts.
---

## Review

???

<div class="center">
<strong>Rating</strong>: {{ page.rating }} / 10
</div>
<hr>

<!-- https://openreview.net/forum?id=9yQ2aaArDn -->

## Overview

The 'RL as inference' approach frames RL as a probabilistic inference problem by introducing a binary optimality variable. This variable is 1 if the state-action is optimal and 0 otherwise. 

Our goal is to construct posterior

$$
M = \{\mathcal S, A, L, P, R, \rho\}
$$

## Additional thoughts


<!-- ref rl as inference https://arxiv.org/abs/1805.00909 -->
