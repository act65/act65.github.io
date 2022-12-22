---
layout: post
title: Requests for research from my masters
---

To stay sane I needed to write down some of the _actionable_ ideas that occur to me.
Otherwise I have the tendency to hoard them.
So, these are the questions I am not going to answer (argh it hurts!).
They appear to be perfectly good research directions, but "you need to focus" (says pretty much everyone I meet).

# Requests for research

_(the number of stars reflects how open the problem is:, 1 star means little room for interpretation, 3 stars mean that there are some complex choices to be made)_

&#9734; __Controlled implicit qualtiles__ Extend [Implicit quantile RL](https://arxiv.org/abs/1806.06923) (which works suprisingly well) to use [control](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.43.7441&rep=rep1&type=pdf) [variates](https://arxiv.org/abs/0802.2426).

&#9734; __Atari-onomy__ Make a [taskonomy](http://taskonomy.stanford.edu/) of the [Atari](https://gym.openai.com/envs/#atari) games, showing how 'similar' each game is to others.

&#9734; &#9734; &#9734; __Learner discrimination__ Just by observing a player learn, can we identify the learning algorithm is it using to learn? For example, can we distinguish the learners in [OpenAI's baselines](https://github.com/openai/baselines/), PPO, AC2, AKTR, ...?

&#9734; &#9734; __Meta learning from temporal decompositions__ [Meta-RL](https://arxiv.org/abs/1611.05763) trains a learner on the aggregated return over many episodes (a larger time scale). If we construct a temporal decomposition (moving averages at different time-scales) of rewards and aproximate them with a set of value functions, does this produce a heirarchy of meta learners? (will need a way to aggregate actions chosen in different time scales, for example $\pi(s_t) = g(\sum_k f_k(z_t))$)
