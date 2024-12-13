---
title: "Typical set of arbitrary distributions"
subtitle: "Constructing the typical set for arbitrary distributions"
layout: post
permalink: /pits/arbitrary-typical
scholar:
  bibliography: "pits.bib"
---

<!-- % TODO in which cases does $x - f^{-1}(\alpha f(x))$ approximate $\nabla_x p_f(x)$?? -->

In general, the typical set, $\mathcal T_{p(x)}^{\epsilon}$, is intractable to compute for arbitrary continuous distributions.
<!-- (why?) -->
However, we can approximate the typical set, using a rectified flow that maps from a target data distribution to a Gaussian source distribution.

We back up this claim in two parts:

- a derivation [showing]({{ site.baseurl }}/pits/arbitrary-typical-proof) that;
  - for linear transformations the image of the typical set equals the typical set of the image.
  - for general flows they are not generally equal.
- experimental evidence [showing]({{ site.baseurl }}/pits/arbitrary-typical-experiments) that;
  - (WIP) the closer to flow is to being linear, the more accurate the typical set approximation.