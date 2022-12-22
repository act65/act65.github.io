---
layout: post
title: Causal calculus
---

I recently read Judea's [book](https://www.goodreads.com/book/show/36204378-the-book-of-why
) on Causal Inference (you should to). I noticed another interpretation of a couple of the formulas.

## Causal inference

What we care about is the ability to estimate causal relationships from data. Here we consider two methods to estimate a causal relationship using observed data; the front and back door adjustments.

<side>Note: Causal relationships can sometimes be estimated from the data's correlation, but if a confounder is present it complicates the analysis. This is the problem that the front/back door adjustment solve.</side>

![pic]({{site.baseurl}}\images/smoking.png)


(_$X$ stands for Smoking, $Y$ stands for Cancer, $Z$ stands for Tar and $U$ stands for Smoking gene._)

<side>For more info see Chapter 7. in The Book of Why.
</side>

#### The back door adjustment

If we are able to close all the back doors (control/remove all paths into $X$ that connect to $Y$) then the causal relationship between $X$ and $Y$ is simply their correlation.

$$
\begin{align}
P(Y \mid do(X)) &= \sum_U P(Y \mid X, U=u) P(U=u) \tag{iff all back doors are shut} \\
&= \mathbb E_{u\sim U}[P(Y \mid X, U=u)] \\
P(Y \mid X, U=u) &=  \frac{\mathbb E_{(x, y)\sim X, Y, U=u} [(x -\mu_x)(y-\mu_y)]}{\sigma_x} \tag{correlation}  \\
\\
Y &= aX + bU + c \tag{assume linear relationships} \\
a&= (Y-bU + c)X^{-1} \\
\end{align}
$$


#### The front door adjustment

Now, let's consider the case where we do not have measurements on the confounder, $U$ but still want to estimate $P(Y \mid do(X))$. Is it still possible? Surprisingly, yes.

a) We can simply estimate the effect of smoking on tar from their correlation as there are no confounders.
b) And we can estimate the effect of tar on cancer by blocking the backdoor, through controlling for smoking.

Or as eqns;

$$
\begin{align}
P(Z \mid do(X)) &= P(Z, X) \tag{no back doors to close}\\
P(Y \mid do(Z)) &= \sum_X P(Y, Z, X=x) P(X=x) \tag{close backdoor $Z \to X\to U\to Y$}\\
P(Y \mid do(X)) &= \sum_Z P(Z=z\mid do(X)) \cdot P(Y \mid do(Z=z)) \tag{product rule!?!?}\\
&= \sum_Z P(Z=z, X) \sum_X P(Y\mid X=x, Z=z) P(X=x) \\
\end{align}
$$



## Expected gradients

Cool, now here is the nice part. It all started from the realisation that the correlation coefficient can be rewritten as the expected gradient. I think this generalisation gives the ability to think about causal relationships between cts non-linear relationships between random variables (?).

#### Correlation and gradients

The conditional correlation of two variables is simply the gradient.

$$
\begin{align}
P(Y \mid X) &= \mathbb E\big[\frac{(X -\mu_X)(Y-\mu_Y)}{(X -\mu_X)^2} \big] \\
&= \mathbb E\frac{Y-\mu_Y}{X -\mu_X} \\
&= \mathbb E\frac{\Delta Y}{\Delta X} \\
&= \text{expected } \frac{\text{rise}}{\text{run}} \\
&\approx \frac{\partial y}{\partial x} \\
\end{align}
$$

Cool, now let's use this to reinterpret the front and back door adjustments as expectations of gradients.


__The backdoor adjustment__

$$
\begin{align}
P(Y \mid do(X)) &= \mathbb E_u [\frac{\partial y}{\partial x}(u)]  \\
\end{align}
$$


__The front door adjustment__

$$
\begin{align}
P(Y \mid do(X)) &= \mathbb E_z [\frac{\partial y}{\partial z}(z) \cdot\frac{\partial z}{\partial x}(x)] \\
\end{align}
$$

So the front door adjustment is the application of [chain rule](https://en.wikipedia.org/wiki/Chain_rule), nice.


## Total causal effect

Not sure if this works as expected. _work in progress..._

<side>Something is missing here? Would like a measure that returns be between 0-1. Between: does-not-cause vs totally-determined-by. Adding noise should reduce the causal effect.</side>

Want to get an estimate of whether $x$ 'causes' $y$. (_specifically sufficient causes_)

__Desiderata:__

1. If changes in $x$ almost always cause large changes $y$ this should yield high measure of a causal relationship
2. If there exists a value of $x$ that cause large changes $y$ but it almost never occurs, then $X$ is not a 'sufficient cause' of $y$.
3. the direction of the gradient doesn't matter, only the magnitude
4. only deterministic fns make sense (otherwise the grads are not accurate), aka noise must be an argument.

$$
c_{x\to y} = \mathbb E [\parallel \frac{\partial y}{\partial x} \parallel_p]
$$


* Explore relationship to [Integrated Gradients](https://arxiv.org/abs/1703.01365)
* This captures the notion of sufficient causation(?), what about higher order gradients? Could they be used to capture neseccary casues? $\frac{\partial f^2}{\partial x \partial y}$
* Let's test this out with some simple fns.$f(x) = x^2$, $f(x,y) =x^T A y$. Want some empirical validation, just for sanity.
