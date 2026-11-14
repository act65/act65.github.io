---
layout: page
title: CV
permalink: /cv/
description: "CV of Alexander Telfar: machine learning research, and work on governance mechanisms, social choice and AI governance."
---

<!-- Web version, reorganised from life-admin/cv-v2.md (which keeps the long form for applications). -->

## Publications

- **Structured Flows for Causal Modelling and Statistical Inference.** *TMLR*, 2026. First author.\\
  [OpenReview](https://openreview.net/forum?id=5cFwygAUFt) · [Library](https://github.com/AI4PSE/structflows) · [Code](https://github.com/AI4PSE/structflows-tmlr)\\
  Compiles a causal graphical model into a normalizing flow, so one flexible model can answer interventional and counterfactual queries, or be reorganised for fast inference.
- **Ballot Structure from the Preference-Dependency Graph.** Preprint (not peer reviewed), 2026. Sole author.\\
  [Zenodo](https://zenodo.org/records/21409990) · [Code](https://github.com/act65/ballot-structure) · [Post]({{ site.baseurl }}/ballot-design/)\\
  Which questions should a ballot ask together? Estimates the dependencies between voters' preferences from Polis votes, and designs the ballot to match.
- **Abstraction for efficient reinforcement learning.** MSc thesis, Victoria University of Wellington, 2020. [Thesis](https://openaccess.wgtn.ac.nz/articles/thesis/Absraction_for_Efficient_Reinforcement_Learning/17147651?file=31706501)

## Projects

**Research tools**
- **NZ Politician Scorecards** (2026, in progress). An evidence-linked platform that scores NZ MPs on conduct attributes, using LLMs against a fixed rubric, from 45,477 sourced statements. Method, evaluation and code are open. [Site](https://nz-politician-scorecards.onrender.com/) · [Code](https://github.com/act65/pol-score-cards)
- **Bandit browser** (2026). A machine-readable atlas of theoretical results: LLMs parse settings, algorithms and bounds from papers into a graph. Piloted on bandits. [Code](https://github.com/act65/bandit-browser)
- **Stochastic interpolants** (2025). A library of interpolant variants and couplings for neural flows. [Code](https://github.com/act65/sinterp)
- **MRI reconstruction** (2018). Showed GANs were unreliable for efficient MRI analytics, and built a normalizing-flow alternative. [Code](https://github.com/act65/mri-reconstruction)

**Games and other builds**
- **Turing vs Scherbius** (2025). A two-player card game about the codebreaking duel of WWII, with a companion tutorial on ciphers. [Post]({{ site.baseurl }}/turing-vs-scherbius/) · [Tutorial]({{ site.baseurl }}/turing-vs-scherbius/enigma/) · [Code](https://github.com/act65/turing-vs-scherbius)
- **Rain Protocol** (2025). Reputation as a financial primitive: a framework for verifiable promises between strangers. [Post]({{ site.baseurl }}/rain/) · [Code](https://github.com/act65/rain)
- **Hexboard** (2026). An isomorphic keyboard in the browser, where every chord has one shape. [Post]({{ site.baseurl }}/chords-are-shapes/) · [Code](https://github.com/act65/hexboard)
- **iGEM** (2019), student lead. A glycerol-based enzymatic fuel cell: found the rate-limiting step and swapped in a faster enzyme. [Write-up]({{ site.baseurl }}/igem-2019/)

## Technical writing highlights

**Governance and AI**
- [Designing behind the veil]({{ site.baseurl }}/governance-mechanisms/): a research programme linking political philosophy, governance and AI safety through mechanism design. *If you can't write down what a society should want, what do you build instead?*
- [Minimality from uncertainty]({{ site.baseurl }}/minimality-from-uncertainty/): how much should a constitution rule out before anyone can learn?
- [The Geometry of Governance]({{ site.baseurl }}/voting-geom/): vote aggregation as a rate–distortion problem.
- [Global coordination problems via game theory]({{ site.baseurl }}/agi-game/): why AGI is not like climate change.

**Decisions, learning and RL**
- [Every Bias Names an Algorithm]({{ site.baseurl }}/approximate-reasoning/): cognitive biases and LLM failures as the signatures of specific approximation algorithms.
- [In what sense is Bayesian updating optimal?]({{ site.baseurl }}/bayes-optimal/): minimising surprise leads to Bayes' rule.
- [Why are future rewards worth less than present rewards?]({{ site.baseurl }}/discounting-via-uncertainty/): a Bayesian derivation of discounting from uncertainty.
- [Committed to Fidelity]({{ site.baseurl }}/arms-fidelities-delays/): a unified model for multi-fidelity bandits.
- [Goal Hijacking]({{ site.baseurl }}/reward-hijacking/) · [The Hammer and the Nuke]({{ site.baseurl }}/necessary-robust-rl/): on RL safety.

**ML methods and tutorials**
- [Score functions, denoising and diffusion]({{ site.baseurl }}/scoredd/): diffusion is stacked denoising score matching.
- [Typicality]({{ site.baseurl }}/typicality/): in high dimensions, typical is unintuitive.
- [The behaviour of neural flows]({{ site.baseurl }}/si-in-practice/): why networks struggle with simple flows.
- [Bayesian Belief Bellman equations]({{ site.baseurl }}/bbb-ids/): a non-standard introduction, with information-directed sampling.

## Experience

- **Research Associate**, Forschungszentrum Jülich (IAS-9) · *Nov 2025 – present*. Generative flows and probabilistic modelling.
- **Independent writing**, governance and AI · *Mar – Nov 2025*.
- **ML Consultant**, Sparsity · *Jan – Mar 2025*. RL and federated-learning demonstrations for a blockchain platform.
- **Graduate Researcher**, Speech & Image Processing, Victoria University of Wellington · *2023 – 2024*. Stochastic interpolants for inverse problems.
- **Graduate Researcher**, Computational Chemistry, University of Glasgow · *2020 – 2022*. Translating natural-language syntheses into robot programs; structure elucidation from NMR spectra.
- **Research Assistant**, Robotics & RL, Victoria University of Wellington · *2020*. RL navigation for a simulated Mars rover.
- **Research Assistant**, Medical Imaging, Victoria University of Wellington · *2018*.
- **ML Developer**, NEC · *2016 – 2017*. Satellite-image and bird-song classifiers in production.

## Education

- **MSc, Computer Science**, Victoria University of Wellington, 2020
- **PGDip, Computer Science**, Victoria University of Wellington, 2016
- **BE (Hons), Engineering**, University of Canterbury, 2013

## Skills

Probabilistic and causal modelling · generative flows (normalizing flows, flow matching, stochastic interpolants) · inverse problems · reinforcement learning · mechanism design and social choice · LLM evaluation · Python, JAX, PyTorch, Docker
