---
layout: post
title: What is the difference between credit assignment and causal inference?
---

- Eligibility traces -> gradient of policy. + Kickback + !?
- Differentiation $\neq$ credit assignment. Credit assignment is a counterfactual notion. Differentiation has no concept of priors, and what might have happened if a parameter was a different value. Or does it!?
- Alternative ways to assign credit!?
- Why we need stochastic variables for discrete credit assignment.
- !?

If your fault.

Legal.
Nesessary and sufficient causation.


Only want to assign credit to causes, not correlates?!


## Eligibility traces

Given the typical temporal difference update (for a tabular representation) we could augment it with a 'trace', $e_t(s_t, a_t)$.
$$
\begin{align}
Q_{t+1} &= Q_t + \alpha \delta_t e_t \\
\Delta Q &= \alpha \delta_t e_t \\
e_t[s, a] &=
\gamma \lambda e_{t-1}[s, a] + \mathbf 1_{s=s_t, a=a_t}\\
\end{align}
$$

What is this 'trace' doing? Well, it's an exponentially decaying variable, but for a given state-action pair, if they are used at time t, we reset the 'trace' to one.

We can interpret this as keeping a (decaying) memory of the state-action pair, or is exponentially decaying recency. Thus a trace.

***

But what if we want to use some sort of function approximation to represent $Q(s_t, a_t)$, rather than tables? We can generalise the definition above to;

$$
\begin{align}
e_t(s_t, a_t) &= \gamma \lambda e_{t-1}(s_t, a_t) + \nabla_{\theta_t} Q_t(s_t, a_t)\\
\end{align}
$$

This generalised definition recovers the tabular case, as $\nabla_{\theta_t} Q_t[s_t, a_t] = \mathbf 1_{s=s_t, a=a_t}$.

However, we have introduced a new problem. We need to update all of the state-action pairs. In the tabular case, this was possible (but maybe not a good idea), as we could iterate through all the distinct state-action pairs. But how can we efficiently make this update for an infinite number of state-action pairs?  

***

A quick aside.

What are we doing here? What is $\nabla_{\theta_t} Q_t(s_t, a_t)$?

We are keeping an exponential average of the gradient of the state-action value with respect to each parameter. Which tells us: how did each parameter contribute to the estimated value. That feels a lot like assigning credit to different parameters.


Forward vs backward views. Why are these attractive? Keeps the trace of a trajectory lingering. Could simply use the trajectory, but it needs to be feed in, thus we need to store the obs and action. Rather the trace and be stored internally, (hopefully more cheaply!?).

https://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es2007-49.pdf

***

Ok, so is there a difference to momentum?
https://distill.pub/2017/momentum/

$$
\begin{align}
\frac{\partial L}{\partial \theta_t} = \frac{\partial L}{\partial Q} \frac{\partial Q}{\partial \theta}
\end{align}
$$

A kind of momentum?






***

Integrated gradients = causal effect = eligibility trace?

https://arxiv.org/abs/1703.01365


***

Resources

- http://incompleteideas.net/book/ebook/node72.html
- http://pierrelucbacon.com/
- http://web.eecs.umich.edu/~baveja/Papers/ICML98_LS.pdf
- https://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es2007-49.pdf
- https://amreis.github.io/ml/reinf-learn/2017/11/02/reinforcement-learning-eligibility-traces.html
- http://rl.cs.mcgill.ca/tracesgroup/
