---
layout: post
title: Variance reduction for faster learning
---

### How does variance effect the speed of learning?




### How can we reduce variance?

Importance sampling and control variates.





Estimating the mean of a function. Not trivial?
How to do efficiently?

When there is high variance in the function ...?

$$
\begin{align}
m^* = m + a(t - \tau) \\
a^* = -\frac{Cov(m, t)}{Var(t)} \\
\end{align}
$$

Estimating the mean in an incremental fashion

$$
\begin{align}
\mu_t &= \sum_{i=0}^t x_i \tag{average}\\
\mu_{t+1} &= \mu_t + a(\mu_t - x_t) \\
a &= \frac{1}{t+1} \\
\end{align}
$$



$$
\begin{align}
\mu_t &= \sum_{i=0}^t \gamma^ix_i \tag{exponential moving average}\\
\mu_{t+1} &= \mu_t + a(\mu_t - x_t) \\
a &= \beta \tag{some constant value} \\
\end{align}
$$

what about other relationships? what would they mean? exp, log, sin,...?

$$
\begin{align}
a &=
\end{align}
$$


TODO want some images for intuition.
- correction of a fn
- effect of variance on accuracy

***

What if we care about more than just the mean?
- What complicates estimating the variance of a function? Higher order moments? (can we recursively use control variates for each higher order!?)
- What if we want to estimate the entire distribution? Is there a way to use
- what about other p norms? $\mu = \mathop{\text{argmin}}_y \sum_{i=0}^t \parallel x_i-y\parallel_2$.

***

- Touch on A2C?
- What about control variates for gradient estimation? (could use synthetic grads?)


$$
\begin{align}
max E_{s\sim\pi}[R(s)] \\
\\
&= -\nabla log(\pi(s)) R \\
\end{align}
$$


<side>(why does less variance me faster learning!? need to motivate)</side>
Advantage actor critic (A2C) improves this byredicng the variance of the gradient estimation  
