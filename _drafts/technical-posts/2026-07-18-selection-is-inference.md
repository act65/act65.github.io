---
layout: post
title: The Same Update
subtitle: Natural selection, Bayesian inference, and online learning are one equation
categories:
  - play
---

Here are three updates from three fields that have almost nothing to do with each other.

**Evolution.** A population has types $i$ with frequencies $x_i$ and fitnesses $f_i$. Next generation, the fit breed more:

$$x_i \;\leftarrow\; \frac{x_i\, f_i}{\sum_j x_j\, f_j}.$$

**Bayesian inference.** You have hypotheses $i$ with prior probabilities $x_i$, and each assigns likelihood $f_i$ to the data you just saw. The posterior is:

$$x_i \;\leftarrow\; \frac{x_i\, f_i}{\sum_j x_j\, f_j}.$$

**Online learning.** You have experts $i$ with weights $x_i$, and each just earned reward with "multiplier" $f_i$. The multiplicative-weights update is:

$$x_i \;\leftarrow\; \frac{x_i\, f_i}{\sum_j x_j\, f_j}.$$

Look at them. They are not analogous. They are not similar. They are the *same equation* — the identical operation performed on a distribution: multiply every component by a per-component factor, then renormalise. Natural selection, Bayes' rule, and multiplicative weights are one update wearing three lab coats, and once you see it you get a genuinely strange sentence for free: **evolution is doing statistical inference, and inference is a kind of evolution.**

### What the dictionary translates

If it's one equation, then every noun in one field must have a twin in the others, and it does:

| Evolution | Bayes | Online learning |
|---|---|---|
| population of types | distribution over hypotheses | weighting over experts |
| frequency $x_i$ | probability of hypothesis $i$ | weight of expert $i$ |
| fitness $f_i$ | likelihood $p(\text{data} \mid i)$ | reward multiplier |
| a generation | one observation | one round |
| selection | conditioning | the update |
| the fittest type takes over | the posterior concentrates on the truth | the best expert dominates |

So a population *is* a posterior over genotypes, and the environment is the data. Every generation, nature runs one step of Bayesian conditioning: the "data" is *who survived*, the "likelihood" of a genotype is how well it survives, and selection is the update. Fisher's fundamental theorem of natural selection — that the rate of increase in mean fitness equals the *variance* in fitness — is the biologist's version of the statistician's fact that you learn fastest when your hypotheses most disagree. Same theorem. It even has the same proof, if you write it in the right coordinates.

> This isn't hand-waving; it's a proved correspondence. Cosma Shalizi (2009) showed Bayesian updating *is* a replicator equation — natural selection operating on a population of hypotheses, with likelihood as fitness. Marc Harper worked the same identity from the other side, reading the replicator dynamics as an inference procedure. The equation doesn't know which field it's in.

### Why it *had* to be the same

The reason isn't a coincidence, and seeing it is the satisfying part. Take logarithms. Multiplying-and-renormalising becomes *adding*:

$$\log x_i \;\leftarrow\; \log x_i + \log f_i - (\text{normaliser}).$$

In the log domain, every one of these updates is **accumulate the evidence**: log-posterior is log-prior plus log-likelihood; log-frequency is old log-frequency plus log-fitness; log-weight grows by log-reward. Repeated conditioning, repeated breeding, and repeated reward are all just *summing log-scores* and keeping a running tally — which is why they all converge on whichever option has the best average log-score, and why they all converge *exponentially*. The winner's lead compounds because it's a sum in the exponent.

And there's a cleaner way to say what that summation *is*: it's **mirror descent on the simplex with an entropic penalty** — gradient ascent, done in the natural geometry of probability distributions rather than flat Euclidean space. All three updates are the same optimiser (minimise expected surprise / maximise expected log-score) taking a step in the same curved space. The "diamond" of probability distributions has a preferred way to move downhill, and evolution, Bayes, and multiplicative weights all found it independently.

### The payoff, and a shot at my own past drafts

Two things fall out that I care about.

First, the framing dissolves a fight I've picked before. I've been [rude about evolutionary computation]({{ site.baseurl }}) — random mutation and selection looking hopeless next to gradient descent. But if the replicator equation *is* mirror descent, then selection was never the *opposite* of gradient methods; it's a gradient method in disguise, just one that pays for its geometry in variance and can only estimate the gradient by sampling. The honest version of "EC is dead" isn't "selection is dumb"; it's "selection is a high-variance, black-box estimate of a gradient the fit already know how to follow." That's a much more interesting claim, and it's the [natural-selection-as-an-operator]({{ site.baseurl }}) question answered: the operator is Bayesian conditioning.

Second, it tells you what learning and life have in common at the root. To learn is to keep a distribution over possibilities and let the evidence reweight it. Evolution keeps that distribution in flesh and updates it with death; a brain keeps it in synapses and updates it with surprise; a Bayesian keeps it in a prior and updates it with data. Three substrates, three timescales, one update. The universe, it turns out, only knows how to do one kind of learning — it just runs it on different hardware.
