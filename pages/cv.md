---
layout: page
title: CV
permalink: /cv/
description: "CV of Alexander Telfar: machine learning research, and work on governance mechanisms, social choice and AI governance."
---

<!-- Generated from life-admin/cv-v2.md. Edit there and regenerate, or edit here and keep them in sync. -->

## Selected research output

**Structured Flows for Causal Modelling and Statistical Inference** (TMLR, 2026) — first author, accepted.\\
[OpenReview](https://openreview.net/forum?id=5cFwygAUFt) · [Library](https://github.com/AI4PSE/structflows) · [Paper code](https://github.com/AI4PSE/structflows-tmlr)\\
Answering causal questions needs more than correlations. You need to ask what would happen
if you intervened, and what would have happened otherwise: this is Pearl's causal ladder. Graphical models describe that cause-and-effect structure, but their classical forms are too rigid for complex, high-dimensional data such as images. Normalizing flows are built for
such data, but ignore the structure. StructFlow compiles a graphical model into a flow
that provably respects the causes and effects. The same graph yields either a model that runs forward through the
causes, for interventions and counterfactuals, or one that runs backward from observations to
their likely causes, for inference.

**NZ Politician Scorecards** (2026) — sole developer. (work in progress)\\
[Live site](https://nz-politician-scorecards.onrender.com/) · [Code](https://github.com/act65/pol-score-cards)\\
An evidence-linked accountability platform scoring the MPs of the 54th New Zealand Parliament
on six conduct attributes (specificity, civility, …) from 45,477 statements
scraped from Hansard, Beehive releases, party press releases and RNZ reporting. Every score
links to the statement behind it. Scoring is LLM-based against a fixed rubric, with an
evaluation harness whose findings are published including where they are unflattering — the
current test sets are synthetic, so the accuracy figures do not yet validate the live task;
several attributes are near-duplicates; and the source mix varies by party. Open method, open
evaluation, open code.

**Writing**\\
Governance mechanisms and AI safety, worked from first principles:

- [Designing behind the veil](https://act65.github.io/governance-mechanisms/) — a research programme linking political philosophy, governance and AI safety through mechanism design: *if you can't write down what a society should want, what do you build instead?*
- [The Geometry of Governance](https://act65.github.io/voting-geom/) — vote aggregation as a rate–distortion problem
- [Global coordination problems via game theory](https://act65.github.io/agi-game/) — why AGI is not like climate change
- [The Alignment Problem](https://act65.github.io/alignment/) — corporate misalignment as the live version of the problem
- More technical: [Goal Hijacking](https://act65.github.io/reward-hijacking/) · [The Hammer and the Nuke](https://act65.github.io/necessary-robust-rl/)

---

## Experience

**Research Associate — Forschungszentrum Jülich, IAS-9** · *Nov 2025 – present*\\
Generative flows and probabilistic modelling, including StructFlow (TMLR 2026, above).

**Independent writing — governance and AI** · *Mar – Nov 2025*\\
Essays on institutions, incentives and AI safety.

**Machine Learning Consultant — Sparsity** · *Jan – Mar 2025*\\
Built reinforcement learning and federated learning demonstrations for a
high-throughput blockchain platform.

**Graduate Researcher, Speech & Image Processing — Victoria University of Wellington** · *Jul 2023 – Sep 2024*\\
Explored a novel method for inverse problems using stochastic interpolants
(neural flows), demonstrated on image denoising.

**Graduate Researcher, Computational Chemistry — University of Glasgow** · *Sep 2020 – Dec 2022*\\
Built a machine-translation pipeline converting natural-language chemical syntheses
into executable robotic programs (XDL); uncorrected translations ran successfully on a
synthesis robot. Designed a graph-generation algorithm to elucidate molecular
structures from NMR spectra by programmatically extracting and applying constraints.

**Research Assistant, Robotics & RL — Victoria University of Wellington** · *Mar – Jun 2020, part time*\\
Docker-based simulation pipeline to parallelise RL experiments for a simulated Mars
rover in ROS/Gazebo; implemented and tested the RL algorithms for autonomous navigation.

**Student Lead, iGEM — Victoria University of Wellington** · *Jan – Oct 2019* · [Write-up](https://act65.github.io/igem-2019/)\\
Student 'lead' of the VUW team building a glycerol-based enzymatic fuel cell. Identified the
rate-limiting reaction in an existing oxidation pathway and substituted a faster
natural enzyme, which we characterised and validated.

**Research Assistant, Medical Imaging — Victoria University of Wellington** · *Jun – Aug 2018, part time* · [Code](https://github.com/act65/mri-reconstruction)\\
Evaluated generative models for efficient MRI analytics; showed GANs were unreliable
for the task and implemented a normalising-flow alternative. Reported the negative
result.

**Machine Learning Developer — NEC** · *Nov 2016 – Dec 2017*\\
Built and deployed a semi-supervised satellite-image classifier and an audio
classifier for native bird-song identification. Managed ML infrastructure
(TensorFlow, Docker, AWS).

---

## Education

**MSc, Computer Science** — Victoria University of Wellington, 2020\\
Thesis: [*Abstraction for efficient reinforcement learning*](https://openaccess.wgtn.ac.nz/articles/thesis/Absraction_for_Efficient_Reinforcement_Learning/17147651?file=31706501)

**PGDip, Computer Science** — Victoria University of Wellington, 2016\\
Project: anomaly detection using generative methods

**BE (Hons), Engineering** — University of Canterbury, 2013\\
Focus: control systems and biological modelling

---

## Technical

Probabilistic modelling · generative flows (normalising flows, flow matching,
stochastic interpolants) · inverse problems · reinforcement learning · causal
inference · mechanism design and social choice · LLM evaluation and rubric design ·
Python, JAX/PyTorch, Docker

Referees available on request.
