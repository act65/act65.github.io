---
title: "PITS for solving inverse problems"
subtitle: "Using a flow to correct for noise"
layout: post
permalink: /pits/inverse
scholar:
  bibliography: "pits.bib"
---

Thus, we implement PITS as:

$$
\begin{align*}
h = f(y) \tag{forward flow}\\
\hat h = \text{proj}(h) \tag{project into typical set}\\
\hat x = f^{-1}(\hat h) \tag{backward flow}
\end{align*}
$$

![]({{site.baseurl}}/assets/pits/pots-diagram.png)


A diagram of the POTS method. We start with the clean signal $x$, shown as a blue dot. The clean signal is then corrupted to produce the observed signal $y$, shown as a red dot. Next, we project the corrupted signal into the typical set to produce our denoised signal $\hat x$, shown as a green dot. The typical set is shown as a teal annulus.
