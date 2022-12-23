---
layout: post
title: Linear Bandits with Stochastic Delayed Feedback
permalink: delayed-bandits
rating: 4
ref: https://arxiv.org/abs/1807.02089
subtitle: Review with some thoughts.
---

## Review

To me, the interesting part of this paper is the setting. Unfortunately for the authors, that isn't new.
I am interested in how to design a learner that exploits some kind of structure within the delayed bandit problem to achieve better performance. This paper provides and characterises a baseline, a learner that does not exploit any structure in the delays.

<div class="center">
<strong>Rating</strong>: {{ page.rating }} / 10
</div>
<hr>

## Overview

<i>Rather than recieving feedback when you want it, in this setting you recieve it after an unknown delay. How do these delays effect your ability to efficiently to learn?</i>

The authors consider an augmented linear bandit with two key additions;

- delayed feedback,
- negative feedback is not observed.

The learners goal is to minimse its regret. Which is the difference between the best fixed choice in hindsight and the actions it chose.

$$
R(T, \theta) = \sum_{t=1}^{T} \langle \theta, A^{* } \rangle - \langle \theta, A_t\rangle
$$

Where $A_t \in \mathcal A\subset \mathbb R^d$ is the action space. And $\theta \in \Theta \subset R^d$ is the parameter space. $X_t\in \{0, 1\}$ are the rewards, and $Y_t\in \{0, 1\}$ are the observed rewards.

$$
\begin{align}
X_t &\sim \mathcal B(\langle A_t, \theta \rangle) \tag{bernoulli linear bandit} \\
D_t &\sim P(D) \tag{sample the delay}\\
C_{s, t} &= \mathbb 1 [D_s \le t-s] \tag{mask of the delays}\\
Y_{s, t} &= C_{s, t} X_s \tag{delayed rewards}
\end{align}
$$

As an example, let's consider what a learner might observe.

$$
\begin{bmatrix}
t=1 \\
2 \\
3 \\
4 \\
5 \\
6 \\
7 \\
8 \\
9 \\
10 \\
- \\
s= \\
\end{bmatrix}
\begin{bmatrix}
0 \\
0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
- & - & - & - & - & - & - & - & - & - \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\end{bmatrix}
$$

The rows correspond to each time step, (indexed by $t$), and the columns correspond to the history (indexed by $s$).

So, for any action that received a reward of zero, $Y_{s, t} = C_{s, t}X_{s} = 0$, we are left wondering; might the reward received convert to $Y_{s, \tau} = C_{s, \tau}X_{s} = 1$ at some future time ($t < \tau$)?

To solve this problem the authors construct;

- a way to estimate each action's payoffs.
- a rational way to pick new actions given our predictions of their payoffs.

And provide an analysis of each.

### Estimation

#### A fixed size memory

To make estimation computationally feasible the authors give the learner access to the last $m$ actions and their results, $\hat Y_{s, t}$ (it is not allowed to remember).

$$
\hat Y_{s, t} = Y_{s, t} \mathbb 1 \{D_s \le m\}
$$

So the learner gets a fixed size buffer of past information. This change has introduced some new problems;

- if the buffer's size is smaller than the expected delay, $m < E[D]$, then the problem is rather unlearnable.
- we are throwing away $1-P(D < m)$ of the data.
- because some rewards might not have converted this will bias our estimates of rewards to be pessimistic.

#### Least squares

The authors decide to estimate the parameters using least squares. By solving the following;

$$
\theta_t = \mathop{\text{argmin}}_{\hat \theta} \sum_{s=1}^{t-1}\parallel \hat Y_{t, s} - A_s\cdot \hat \theta \parallel
$$

This least squares formulation is rather dumb. It doesn't know about the delays, and just tries to fit the action-rewards as they are observed, despite the fact that $\hat Y_{k, t}$ might not have converted.
Despite this, least squares will give small(er) errors when $P(D < m)$ is large. As most rewards will have converted when it comes time to estimate the parameters.

All we are really saying here is; if there are no delays then least squares can fit a linear model. What we really want to know is how well does least squares work with delayed feedback?

<!-- Because this is a linear problem we can solve this analytically, yielding;

$$
\hat \theta_t^{W} = \Bigg( \sum_{s=1}^{t-1} A_S A_S^T + \lambda I \Bigg)^{-1}
\Bigg(\sum_{s=1}^{t-1}\hat Y_{s, t}A_s \Bigg)
$$ -->

#### Confidence

So we want to know if this least squares estimator is accurate in the delayed setting. In Theorem 1., the authors characterise its accuracy using a confidence interval.

<blockquote cite="Vernade 2020">
<strong>Theorem 1.</strong>
Let $\tau_m = P(D \le m)$ and $\delta \in (0, 1)$. Then the following holds for all $t \le T$ with probability at least $1 − 2\delta$

$$
\parallel \hat \theta^W_t − \tau_m \theta \parallel_{V_t(\lambda)} \le 2f_{t,\delta} + \sum_{s=t-m}^{t-1} \parallel A_s \parallel_{V_t(\lambda)^{-1}}
$$

where

$$
f_{t,\delta} = \sqrt{2\log(\frac{1}{\delta}) + d \log(\frac{ d\lambda + t}{d\lambda})}
$$
</blockquote>

Great. But what does that actually say?

__1)__ Is this estimator accurate in the applications we planning on using it? <br>
__2)__ How is this a confidence interval? <br>
__3)__ How is the confidence influenced by the problem?

__1)__ As indicated earlier, when $P(D < m)$ is large, $\tau_m \theta \approx \theta$, which means we are bounding the distance between the true parameters and our estimate. Indicating that least squares should work when $m$ is large relative to the likely delay.

__2)__ From theorem 1. it can be seen that;

$$
\alpha_{t, \delta} =  2 f_{t, \delta} + \sum_{s=t-m}^{t-1} \parallel A_s \parallel_{V_T(\lambda)^{-1}} \\
\alpha_{t, \delta} \ge \parallel \hat \theta^W_t − \tau_m \theta \parallel_{V_t(\lambda)}
$$

In high dimensions confidence intervals can be written as;

$$
\begin{align}
\alpha_\delta &\ge (\theta - \hat \theta)^T C(\theta)^{-1} (\theta - \hat \theta)  \\
&\ge \parallel \theta - \hat \theta \parallel_{C(\theta)^{-1}}
\end{align}
$$

<side>
This doesnt really make sense to me. The covariance of the parameters. They are not random variables.
</side>

Where $C(\theta)$ is the covariance of the estimated parameters. This equation says that: there is a $1-\delta$ probability that the true parameters lie within a distance $\alpha_{\delta}$ of the estimated parameters. Intuitively this makes sense as $C(\theta)$'s role is to downweight directions with higher variance. Allowing $\theta$ to be further away from $\hat \theta$ in those directions.

__3)__ By a happy coincidence of linearity, the covariance of our parameters can be easily calculated.

$$
\begin{align}
C(\theta) &\approx V_t(\lambda)^{-1} \\
&= \Bigg( \sum_{s=1}^{t-1} A_sA_s^T + \lambda  I \Bigg)^{-1}
\end{align}
$$

So if we consider the confidence interval $\alpha_{\delta}$ we see the term $\parallel A \parallel_{V_t(\lambda)^{-1}}$. This term is large(r) when $A$ points in a direction that most other past actions do not.

Note that $2f_{t, \delta}$ is the confidence interval from vanilla least squares, and the added term is due to the delay.

### Control

Now that we have an estimate and we can quantify our confidence, we can rationally choose actions.
We want to pick actions that maximise the reward. But we don't know how to do that yet. Rather, we must fist pick actions that "explore" and allow us to estimate the parameters of the problem.

We set the utility of an action to be the best reward we can confidently expect. Also known as optimisim in the face of uncertainty.

Fortunately, the authors have already characterised the confidence we ought to have in our estimate. We can use this confidence to pick our exploratory actions. Also known as; the upper confidence bound method, or UCB.

$$
\begin{align}
U(a) &=  \mathop{\text{max}}_{\theta} \langle a, \theta \rangle \\ &\text{s.t.} \;\;\parallel\theta-\hat \theta^W_t\parallel_{V_t(\lambda)} \le \alpha_\delta\\
A_t &= \mathop{\text{argmax}}_a U(a) \\
\end{align}
$$

We can upper bound $U(a)$ with a simpler to calculate function, $\hat U(a)$.

$$
\begin{align}
U(a) &= \langle a, \hat \theta^W_t +  e_a^{* } \rangle \\
&= \langle a, \hat \theta^W_t \rangle +  \langle a, e_a^{* } \rangle \tag{linear fn}\\
&\le  \langle a, \hat \theta^W_t \rangle +  \parallel e_a^{* } \parallel_{V_t(\lambda)^{-1}} \parallel a \parallel_{V_t(\lambda)^{-1}} \tag{Cauchy–Schwarz}\\
\hat U(a) &:= \langle a, \hat \theta^W_t \rangle + \Bigg( f_{t, \delta} + \sum_{s=t-m}^{t-1}\parallel A \parallel_{V_t(\lambda)^{-1}}\Bigg) \parallel a \parallel_{V_t(\lambda)^{-1}} \tag{theorem 1.}\\
\end{align}
$$

Where $e_a^{* }$ is a vector pointing to from the current estimate to the parameters with highest reward (under action $a$) that are within the $\delta$-confidence set.

### Analysis

Great. Now we have a learner with the authors name OTFLinUCB.

<side>
Because the actual algorithm is implemented in an incremental fashion, how does this change the estimator? As data older than $m$ can still influence the estimation.
</side>
- estimate $\theta_t$ from observations using least squares,
- calculate our confidence $a_\delta$,
- pick a new action, $A_t$ using our utility function, $U$.

But how does this algorithm perform?

<blockquote cite="Vernade 2020">
<strong>Theorem 2.</strong>
With probability at least $1 − 2\delta$ the regret of OTFLinUCB satisfies

$$
R(T, θ) \le \frac{4 f_{n, \delta}}{\tau_m} \sqrt{2dT\log\Big(\frac{d\lambda + T}{d \lambda} \Big)}\\+ \frac{4md}{\tau_m}\log \Big( \frac{d\lambda
+ T}{d \lambda}\Big)
$$
</blockquote>

This theorem provides the authors with the understanding that;

<side>
The lower order term makes little sense to me. How can more data, and more converted rewards (by using a larger $m$) hurt performance?
</side>

<blockquote cite="Vernade 2020">
The choice of $m$ is left to the learner. It influences the bound in two ways: (1) The lower-order term is linear in $m$, which prevents the user from choosing $m$ very large. On the other hand, $\tau_m$ is increasing in $m$, which pushes the user in the opposite direction. Designing an adaptive algorithm that optimizes the choice of $m$ online remains a challenge for the future
</blockquote>

They also compare the performance of OTFLinUCB to a lower bound on the delayed bernoulli linear bandit setting.

<blockquote cite="Vernade 2020">
<strong>Theorem 3.</strong>
For any policy $\pi$ and $K > 1$ and $T \ge 1$ and
$\tau \in (0, 1)$ there exists a $K$-armed Bernoulli bandit such that $R(T, \theta) \ge c\text{min}(T, \sqrt{\frac{TK}{\tau_m}})$, where $c>0$ is a
universal constant.
</blockquote>

We can see that $\sqrt{T}$ performance is possible, while the OTFLinUCB learner achieves approximately $\sqrt{T\log T}$.

<hr>
## Additional thoughts

### A prior on delay distributions

In this setting it seems there is a natural prior;
the distribution over delays, $D$, probably has a long tail that exponentially decays.

$$
p(D) \propto e^{-D} \\
$$

This prior suggests an alternative approach.
The more time that passes after we have chosen an action, the less likely it is we that we are going to see a reward.

<side>there is probably a more principled way, via Bayes, to derive this, or something like it.</side>

$$
\hat Y_{s, t} = e^{-\beta (t-s) (1-Y_{s, t})} \\
$$


This starts by assuming each action is likely to give a reward of $1$, but the longer that $1$ is not observed, the more we decay it's value.

Rather than needing to act optimistically with respect to an estimated model. This approach builds optimisim into the model.

### Setting extensions

#### Allow delays to be action dependent

In the delayed linear bandit problem, delays are sampled from the distribution $D_t \sim p(\mathcal D)$. This could be easily extended to $D_t \sim p( \mathcal D \mid A_t)$.

This setting is interesting as the learner must;

- model the delays.
- tradeoff near-term performance gains via feedback from actions with small delay vs potential performance gains from feedback about actions with longer delays.

Intuitively, a good heuristic might be: pick actions with long delays first. And while they take their time to convert, pick the actions with shorter delays.
Otherwise, if we pick actions with short delays first then we are left with nothing to do while we wait for actions with long delays to convert.

#### Delayed and accumulating rewards

Rather than the Bernoulli rewards in $\{0, 1\}$ for a past action which gets revealed  after some delay.
How about an accumulating reward?

After taking an action, at time $s$, we observe the future rewards ${y_t(a_s)}$s. We care about maximising the accumulation of all those rewards incurred by the action $A_s$, ie $r(A_s) = \sum_{0}^{\infty} y_t(A_s)$.

In this setting we would require;

- actions do not effect the outcomes of other actions,
- the accumulated rewards are bounded $\sum_{0}^{\infty} y_t(A_s) < \infty$.


<!-- #### Delayed and aggregated rewards

Rather than $y_s^t$, we recieve $\hat y^t = \sum_s y_s^t$

Now we have a credit assignment problem. Leaving the player wondering;

<blockquote cite='Mr. Nobody'>
What did I do to deserve this?
</blockquote>

Without some kind of structure in the problem, learning is impossible!?
Unless we add a noop action? Can simply wait??
If we get a reward and have only take a single action then we can assign credit.
If we have taken n actions and recieve a reward then we can rule out actions that were not taken, and assign credit based on how long ago the actions were taken?!! -->
