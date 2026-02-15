---
layout: post
title: Defining the Public Good 
subtitle: An Information-Theoretic Framework for Democratic Governance
categories: [governance, social-choice, mechanism-design]
---

We (attempt to) formalise the question "who should define the public good?" as an estimation problem. The public good is defined as an aggregation of individuals' *true* preferences---what they would endorse under full information and unlimited deliberation. Any group's policy output is then an *estimate* of this target, and the question becomes: under what conditions does the full population's estimate dominate that of any expert subgroup?


We decompose individual preferences into four components---core values, factual beliefs, causal models, and deliberative refinement---and show that each component has a distinct error structure. Idiosyncratic value noise washes out with population size, but correlated belief errors and causal-model errors do not. This decomposition yields four main results: (1) a bias-variance characterisation of when population estimates dominate expert estimates; (2) a separation result showing that mechanisms which decouple value-aggregation from fact-finding dominate conflated mechanisms; (3) bounds on safe delegation to experts as a function of expert value bias versus public epistemic bias; and (4) a sampling argument showing that expert subgroups---being small, correlated, non-random samples of the population---cannot reliably estimate population values, regardless of their epistemic advantages.

These results imply a governance architecture in which the public retains authority over values while experts and prediction markets inform beliefs and causal reasoning---a formal justification for separation of concerns in institutional design.

<!-- ## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Model](#2-model)
  - [2.1 Individuals and Preferences](#21-individuals-and-preferences)
  - [2.2 The Public Good](#22-the-public-good)
  - [2.3 The Estimation Problem](#23-the-estimation-problem)
  - [2.4 Decomposing Preferences](#24-decomposing-preferences)
- [3. Sources of Estimation Error](#3-sources-of-estimation-error)
  - [3.1 Additive Error Model](#31-additive-error-model)
  - [3.2 Idiosyncratic Noise and the Wisdom of Crowds](#32-idiosyncratic-noise-and-the-wisdom-of-crowds)
  - [3.3 Correlated Bias via Social Influence](#33-correlated-bias-via-social-influence)
  - [3.4 Systematic Belief and Causal-Model Errors](#34-systematic-belief-and-causal-model-errors)
- [4. The Role of Experts](#4-the-role-of-experts)
  - [4.1 Informational Advantage](#41-informational-advantage)
  - [4.2 Computational Advantage](#42-computational-advantage)
  - [4.3 Deliberative Advantage](#43-deliberative-advantage)
  - [4.4 The Expert Value Bias Problem](#44-the-expert-value-bias-problem)
- [5. Decomposition of the Decision Problem](#5-decomposition-of-the-decision-problem)
- [6. Main Results](#6-main-results)
  - [6.1 Bias-Variance Characterisation](#61-bias-variance-characterisation)
  - [6.2 Separation of Values and Beliefs](#62-separation-of-values-and-beliefs)
  - [6.3 Delegation Bounds](#63-delegation-bounds)
  - [6.4 Impossibility of Pure Technocracy](#64-impossibility-of-pure-technocracy)
  - [6.5 Deliberation as Debiasing](#65-deliberation-as-debiasing)
- [7. Governance Architecture](#7-governance-architecture)
  - [7.1 Component-Authority Mapping](#71-component-authority-mapping)
  - [7.2 The Problem of Future Preferences](#72-the-problem-of-future-preferences)
  - [7.3 Design Requirements](#73-design-requirements)
- [8. Discussion](#8-discussion)
- [9. Conclusion](#9-conclusion)
- [References](#references)

--- -->

## 1. Introduction

A foundational question in political philosophy and mechanism design is whether the public good can be determined by the public itself, or whether it requires expert guidance. The democratic tradition holds that legitimacy flows from the consent of the governed---that "only the public can define the public good." The epistocratic tradition, articulated recently by Brennan (2016), counters that the public is too ignorant, irrational, or manipulable to identify its own interests reliably.

This paper argues that both positions are partially correct, and that the tension between them can be resolved by decomposing the problem. We propose a formal framework in which:

1. The *public good* is defined as an aggregation of individuals' idealised preferences---what each person would want under full information and unlimited reflection.
2. Any governance mechanism produces an *estimate* of this public good, using the stated preferences and information available to its participants.
3. The question "who should decide?" becomes a statistical question: which group's estimate has the lowest expected error?

This reframing transforms a normative impasse into a tractable analytical problem. The answer, we show, depends critically on the *error structure* of individual preferences. We identify four distinct components of preference---core values, factual beliefs, causal models, and deliberative refinement---and show that each has different properties with respect to aggregation and expertise.

Our main contributions are:

- A formal model decomposing preferences into value, epistemic, and deliberative components ([Section 2](#2-model)).
- An analysis of four distinct error sources and their behaviour under aggregation ([Section 3](#3-sources-of-estimation-error)).
- A characterisation of three distinct mechanisms by which experts can outperform the public, and the fundamental tension between expertise and representativeness ([Section 4](#4-the-role-of-experts)).
- Four formal results: a bias-variance characterisation, a separation result, delegation bounds, and a sampling-based argument for the limits of pure technocracy ([Section 6](#6-main-results)).
- A governance architecture derived from the formal framework, mapping decision components to appropriate institutional mechanisms ([Section 7](#7-governance-architecture)).

The paper proceeds as follows. [Section 2](#2-model) introduces the formal model. [Section 3](#3-sources-of-estimation-error) analyses sources of estimation error. [Section 4](#4-the-role-of-experts) examines the role of experts. [Section 5](#5-decomposition-of-the-decision-problem) presents the key decomposition of the decision problem. [Section 6](#6-main-results) states the main results. [Section 7](#7-governance-architecture) derives governance implications. [Section 8](#8-discussion) discusses limitations and future work. [Section 9](#9-conclusion) concludes.

---

## 2. Model

### 2.1 Individuals and Preferences

Consider a population of $N$ individuals indexed by $i \in \{1, \ldots, N\}$. Each individual $i$ possesses:

> **Definition 1 (True preference).** The *true preference* of individual $i$ is $\theta^*_i \in \Theta \subseteq \mathbb{R}^d$, representing what individual $i$ would endorse if they had unlimited cognitive resources, complete information about the state of the world, and unlimited time for reflection. The true preference is never directly observable, even by the individual themselves.

> **Definition 2 (Stated preference).** The *stated preference* of individual $i$ is $\hat{\theta}_i \in \Theta$, representing what individual $i$ actually reports or acts upon. It is a noisy, potentially biased function of $\theta^*_i$.

The gap between true and stated preferences arises from bounded rationality, incomplete information, social influence, and limited deliberation. Modelling this gap precisely is the central challenge of the paper.

### 2.2 The Public Good

> **Definition 3 (Public good).** Given an aggregation function $f: \Theta^N \to \Theta$, the *public good* is
>
> $$G^{\ast}= f(\theta^*_1, \theta^*_2, \ldots, \theta^*_N). \tag{1}$$

The aggregation function $f$ may be the arithmetic mean, geometric median, a social welfare function in the sense of Harsanyi (1955), or any other mapping from the profile of individual preferences to a social outcome. The choice of $f$ is itself a normative question---we bracket it and take $f$ as given throughout.

> **Remark.** The definition of $G^*$ aggregates over *true* preferences, not stated ones. This is deliberate: the public good is what the public *would* want, not what it currently says it wants. This distinction is what makes the estimation problem non-trivial.

### 2.3 The Estimation Problem

Any group $S \subseteq \{1, \ldots, N\}$ produces an estimate $\hat{G}_S$ of $G^*$ using whatever information, preferences, and aggregation mechanism are available to it.

> **Definition 4 (Estimation error).** The estimation error of group $S$ is measured by
>
> $$\operatorname{MSE}(\hat{G}_S) = \mathbb{E}\left[\|\hat{G}_S - G^*\|^2\right] = \|\operatorname{Bias}(\hat{G}_S)\|^2 + \operatorname{tr}(\operatorname{Var}(\hat{G}_S)), \tag{2}$$
>
> where the expectation is over the randomness in stated preferences, information, and any stochastic elements of the aggregation mechanism.

The central question of this paper is:

> *Under what conditions does the full-population estimate $\hat{G}_{\{1,\ldots,N\}}$ have lower MSE than the estimate $\hat{G}_S$ produced by any strict subgroup $S \subset \{1,\ldots,N\}$?*

This is *not* obviously true. The full population has more data points (lower variance) but may have higher systematic bias. Experts have fewer data points (higher variance on the value dimension) but may have lower bias on factual and causal dimensions. The answer depends on the error structure, which we now develop.

### 2.4 Decomposing Preferences

We decompose each individual's preference into four components:

> **Definition 5 (Preference decomposition).** Each individual $i$ is characterised by:
>
> **(a) Core values** $v_i: \Theta_{\text{outcomes}} \to \mathbb{R}$ --- a utility function over outcomes, representing what individual $i$ fundamentally cares about (equality, freedom, security, etc.). These are *authoritative*: no external party has standing to override them.
>
> **(b) Beliefs** $\hat{s}_i \in \mathcal{S}$ --- individual $i$'s model of the current state of the world. The true state is $s^{\ast}\in \mathcal{S}$.
>
> **(c) Causal model** $\hat{C}_i: \mathcal{A} \times \mathcal{S} \to \Theta_{\text{outcomes}}$ --- individual $i$'s understanding of how policy actions $a \in \mathcal{A}$ map to outcomes, given the state of the world. The true consequence function is $C: \mathcal{A} \times \mathcal{S} \to \Theta_{\text{outcomes}}$.
>
> **(d) Deliberative refinement** $r_i \in [0,1]$ --- the degree to which individual $i$ has reflected on the specific issue. When $r_i = 1$, the individual's expressed values coincide with their idealised values; when $r_i = 0$, expressed values are maximally unreflective.

The *stated preference* of individual $i$ over policy action $a$ is then:

$$\hat{\theta}_i(a) = \hat{v}_i\!\left(\hat{C}_i(a \mid \hat{s}_i),\; r_i\right), \tag{3}$$

where $\hat{v}_i$ denotes the individual's expressed (possibly unreflective) value function.

The *true preference*---the target of aggregation---is:

$$\theta^*_i(a) = v_i\!\left(C(a \mid s^*),\; r_i = 1\right). \tag{4}$$

The public good is therefore:

$$G^*(a) = f\!\left(v_1(C(a \mid s^*), 1),\; \ldots,\; v_N(C(a \mid s^*), 1)\right). \tag{5}$$

This decomposition makes explicit that the gap between $\hat{\theta}_i$ and $\theta^{\ast}_i$ can arise from three distinct sources: wrong beliefs ($\hat{s}_i \neq s^{\ast}$), wrong causal model ($\hat{C}_i \neq C$), or insufficient deliberation ($r_i < 1$). Each source has different properties under aggregation, as we now show.

---

## 3. Sources of Estimation Error

To analyse the estimation problem, we consider a simplified linear model that captures the essential structure. Suppose $\Theta = \mathbb{R}$ and the aggregation function is the mean: $f(\theta_1, \ldots, \theta_N) = \frac{1}{N}\sum_i \theta_i$.

> **Remark (Scope of the linear model).** We develop the analysis for the arithmetic mean because it yields clean, interpretable results. How far do these insights generalise? For any aggregation function that can be written as a weighted average---including trimmed means, weighted voting rules, and many robust estimators---the bias-variance decomposition has essentially the same structure (with weights modifying the effective sample size). For non-linear aggregation functions such as the median or Rawlsian maximin, the error structure changes: bias in the *tails* of the preference distribution matters more than bias in the mean, and the variance reduction from aggregation follows different scaling laws. The qualitative insight---that correlated errors do not wash out, and that separating values from facts helps---holds broadly, but the quantitative bounds we derive are specific to the mean. Extending the formal results to general aggregation functions is an important direction for future work. See [Section 8](#8-discussion) for further discussion.

### 3.1 Additive Error Model

We model the gap between stated and true preferences additively:

$$\hat{\theta}_i = \theta^*_i + \epsilon_i + b_i, \tag{6}$$

where:

- $\epsilon_i$ is *idiosyncratic noise*---zero-mean, independent across individuals, with variance $\sigma^2_\epsilon$. This captures bounded rationality, limited attention, and random errors in preference expression.
- $b_i$ is *systematic bias*---potentially correlated across individuals. This captures shared misinformation, common cognitive biases, and the effects of social influence.

The population estimate is $$\hat{G}_N = \frac{1}{N} \sum_{i=1}^N \hat{\theta}_i$$. Its MSE decomposes as:

$$
\operatorname{MSE}(\hat{G}_N) = \underbrace{\left(\frac{1}{N}\sum_{i=1}^N \mathbb{E}[b_i]\right)^2}_{\text{squared bias}} + \underbrace{\frac{\sigma^2_\epsilon}{N}}_{\text{idiosyncratic variance}} + \underbrace{\frac{1}{N^2}\sum_{i,j} \operatorname{Cov}(b_i, b_j)}_{\text{systematic bias variance}}. \tag{7}
$$

The second term vanishes as $N \to \infty$---this is the "wisdom of crowds" effect (Galton, 1907; Surowiecki, 2004). The first and third terms, however, do *not* vanish with $N$. They represent the irreducible cost of correlated errors.

### 3.2 Idiosyncratic Noise and the Wisdom of Crowds

When biases are absent ($b_i = 0$ for all $i$), the population estimate converges to the true public good:

$$\hat{G}_N = G^{\ast} + \frac{1}{N}\sum_{i=1}^N \epsilon_i \xrightarrow{N \to \infty} G^{\ast}.$$

This is the classical wisdom-of-crowds result: if individual errors are independent and zero-mean, the aggregate is remarkably accurate regardless of individual accuracy (Surowiecki, 2004). The rate of convergence is $O(1/N)$ in MSE.

### 3.3 Correlated Bias via Social Influence

Now suppose individuals are subject to social influence. Following a standard persuasion model, each person's stated preference is a convex combination of their true preference and an external signal:

$$\hat{\theta}_i = (1 - \alpha_i) \cdot \theta^*_i + \alpha_i \cdot m(i), \tag{8}$$

where $\alpha_i \in [0,1]$ is individual $i$'s susceptibility to influence and $m(i)$ is the message they receive from media, peers, or propaganda.

If the influence signal is *correlated* across individuals---as with mass media, where $m(i) = m$ for all $i$---then the population estimate converges not to $G^*$ but to a biased target:

$$\hat{G}_N \xrightarrow{N \to \infty} (1 - \bar{\alpha}) \cdot G^{\ast}+ \bar{\alpha} \cdot m, \tag{9}$$

where $\bar{\alpha} = \frac{1}{N}\sum_i \alpha_i$ is the average susceptibility. The bias $\bar{\alpha}(m - G^{\ast})$ does not diminish with population size. This is the formal version of the "preference formation" objection to democracy: *the public's estimate can be systematically manipulated, and increasing the population does not help when the manipulation is correlated* (Sunstein, 2002).

> **Remark.** This structure is precisely that of the Condorcet Jury Theorem and its failure modes (Condorcet, 1785; Ladha, 1992; Austen-Smith & Banks, 1996). The theorem guarantees that majority rule converges to the correct answer when voters are independent and each individually more likely to be correct than not. With correlated errors---induced by a shared media environment---the theorem breaks down. Our framework generalises this from binary decisions to continuous preference aggregation.

### 3.4 Systematic Belief and Causal-Model Errors

Returning to the preference decomposition of [Section 2.4](#24-decomposing-preferences), we can identify the bias term $b_i$ more precisely. Linearising around the true state and true consequence function:

$$
b_i \approx \underbrace{\nabla_s v_i \cdot (\hat{s}_i - s^{\ast})}_{\text{belief error}} + \underbrace{\nabla_C v_i \cdot (\hat{C}_i - C)}_{\text{causal model error}} + \underbrace{(1 - r_i) \cdot \delta_i}_{\text{deliberative gap}}, \tag{10}
$$

where $\delta_i$ captures the difference between individual $i$'s unreflective and reflective values.

The correlation structure of each term determines whether it washes out under aggregation:

1. **Belief errors** $(\hat{s}_i - s^*)$: If the population shares a common misconception (e.g., about the state of the economy), these errors are highly correlated and do not wash out. An expert who knows $s^*$ can correct this.
2. **Causal model errors** $(\hat{C}_i - C)$: If the population shares a common but incorrect causal theory (e.g., "tariffs protect domestic jobs"), these errors are correlated and do not wash out. An expert who can compute $C$ can correct this.
3. **Deliberative gaps** $(1 - r_i)\delta_i$: The correlation structure depends on whether unreflective values are biased in a common direction. If deliberation moves people in diverse directions, the gap may partially wash out; if it moves them in a common direction (e.g., toward greater empathy after exposure to affected populations), it does not.

> **Remark (Additive vs. structural errors).** The linearisation in equation (10) treats causal-model error as an additive perturbation: $$\hat{C}_i \approx C + \epsilon_C$$. This is a reasonable approximation when the error is *small*---e.g., an individual slightly over- or under-estimates the inflation rate. But causal model errors are often *structural*: believing that printing money causes deflation (wrong sign on the derivative) is qualitatively different from getting the inflation rate slightly wrong. A structural error corresponds to something like $$\hat{C}_i \approx -C$$ rather than $$\hat{C}_i \approx C + \epsilon$$. The linear model cannot capture this distinction---it treats a sign error and a magnitude error identically. This limitation actually *strengthens* the case for expert input on causal models: structural errors are precisely the kind that (a) do not wash out under aggregation (if many people share the same wrong causal theory), and (b) experts are best positioned to correct. However, it also means our quantitative bounds may understate the true cost of public causal-model errors. A richer model would distinguish magnitude errors (additive, potentially small) from structural errors (multiplicative or sign-flipping, potentially catastrophic).

---

## 4. The Role of Experts

The preceding analysis shows that correlated errors---in beliefs, causal models, and deliberation---are the Achilles' heel of democratic aggregation. Experts can potentially address these errors, but through three distinct mechanisms with very different formal structures.

### 4.1 Informational Advantage

The most straightforward expert advantage is superior knowledge of the state of the world $s^*$. A climate scientist knows the radiative forcing coefficient of CO₂; an epidemiologist knows the transmission rate of a pathogen. These are factual inputs to preference formation, not preferences themselves.

Formally, each individual's true preference is a function of both their values and the true state:

$$\theta^*_i = v_i(s^*).$$

But individual $i$ does not observe $s^{\ast}$ ---they observe a noisy signal $\hat{s}_i$ and act on $v_i(\hat{s}_i)$. An expert $e$ has a much more accurate estimate $\hat{s}_e \approx s^{\ast}$.

The crucial insight is that the expert is not overriding the public's *values*---they are correcting the public's *beliefs*. The public has authority over $v_i$; experts have authority over $s^*$. No amount of aggregation over poorly-informed beliefs produces a good estimate of the true state---this is a bias problem, not a variance problem, and it does not diminish with $N$.

This observation immediately suggests a governance architecture: *separate the "what do we want?" question (aggregate over the public's values) from the "what is true?" question (defer to experts or prediction markets)*. This is essentially the principle behind Hanson's *futarchy*: "vote on values, bet on beliefs" (Hanson, 2013).

### 4.2 Computational Advantage

Even if every individual had perfect knowledge of $s^*$, policy questions involve reasoning about complex causal chains. The true preference over a policy action $a$ is:

$$\theta^*_i = v_i(C(a \mid s^*)),$$

where $C: \mathcal{A} \times \mathcal{S} \to \Theta_{\text{outcomes}}$ is the consequence function mapping actions to outcomes. Computing $C$ may require expertise in economics, engineering, ecology, or other domains.

The public uses a heuristic $\hat{C}_i(a \mid \hat{s}_i)$ that may be systematically wrong. For example, the public may believe that rent control reduces housing costs, when the equilibrium effect is the opposite (Kahneman, 2011). This is not ignorance of facts but inability to trace causal chains---a bounded rationality problem.

This means that even with perfect value aggregation and perfect factual information, the public's *policy preferences* can be systematically wrong because they cannot compute the mapping from policies to outcomes.

### 4.3 Deliberative Advantage

A more controversial expert advantage is that deep engagement with a domain can *refine* one's values. Someone who has spent twenty years working on criminal justice may have different moral intuitions about punishment than they did initially---not because they were manipulated, but because sustained reflection changes what one endorses.

This connects to the philosophical concept of *laundered* or *informed preferences*---what an individual would want if they fully understood the situation (Rawls, 1971; Sen, 1999). In our model, this corresponds to the deliberative refinement parameter: experts on a specific topic are closer to $r_i = 1$ *on that topic* because they have effectively done more of the deliberation that defines $\theta^*_i$.

> **Remark.** This advantage is the most difficult to formalise cleanly, because it blurs the line between "the expert knows better" and "the expert has different values." We treat it as a genuine but limited advantage: experts may be closer to their own $\theta^*_i$ on their topic of expertise, but this does not give them authority over *other people's* $\theta^*_j$.

### 4.4 The Expert Value Bias Problem

Against these advantages stands a fundamental problem: *experts are a small subpopulation, and any small subpopulation will be an imperfect sample of the full population's values*.

This is, at root, a sampling problem. If we draw $k$ individuals from a population of $N$ to estimate the population's mean value, the sampling error on the mean is $$O(1/\sqrt{k})$$. When $k \ll N$, this error is large. But expert groups are not even a *random* sample---they are self-selected and shaped by shared training. This introduces two additional problems beyond sampling variance:

1. **Systematic bias.** Professional training and self-selection correlate expert values. Doctors value health more than the general population; economists value efficiency more; military officers value security more; environmental scientists value conservation more. These are not epistemic advantages---they are value shifts induced by professional immersion and self-selection into the profession.
2. **Reduced effective sample size.** Because expert values are correlated (from shared training and culture), the effective sample size for estimating population values is much smaller than $k$. High within-group correlation $\rho_S$ means that adding more experts from the same professional community yields diminishing returns.

Formally, let $S \subset \{1, \ldots, N\}$ be an expert group of size $k$ with shared professional training. The within-group value correlation satisfies:

$$\operatorname{Corr}(v_i, v_j) \geq \rho_S > 0 \quad \text{for } i, j \in S. \tag{11}$$

The variance of the expert group's mean value estimate is then $$\frac{\sigma^2_v}{k}(1 + (k-1)\rho_S)$$, which converges to $$\rho_S \sigma^2_v$$ as $k \to \infty$ rather than to zero. Combined with any systematic shift $$\Delta_S = \mathbb{E}[v_i \mid i \in S] - \mathbb{E}[v_i]$$, this means the expert group's estimate of the population's values has an irreducible error floor---even if every expert has perfect factual knowledge.

> **Remark.** This framing avoids assuming that experts are "biased" in a pejorative sense. The point is simply statistical: a small, correlated, non-random sample cannot reliably estimate a population mean. The same shared training that gives experts their epistemic advantage (access to ground truth about $s^\ast$ and $C$) is what makes them a non-representative sample of values. Expertise and representativeness are in structural tension, and any governance mechanism must navigate this trade-off.

---

## 5. Decomposition of the Decision Problem

The analysis of [Sections 3](#3-sources-of-estimation-error) and [4](#4-the-role-of-experts) reveals that the question "who should decide?" does not have a single answer. Different components of the decision problem have different error structures, and different groups have epistemic advantages on different components.

The following table summarises the key relationships.

| **Error source** | **Washes out with $N$?** | **Experts help?** |
|---|---|---|
| Idiosyncratic value noise | Yes | No |
| Correlated belief errors ($\hat{s}_i \neq s^*$) | No | Yes |
| Correlated causal-model errors ($\hat{C}_i \neq C$) | No | Yes |
| Deliberative gap ($r_i < 1$) | Partially | Partially |
| Expert value bias ($v_i$ correlated in $S$) | N/A | *Harmful* |

**Table 1.** Error sources, their behaviour under aggregation, and the role of expertise.

The table reveals a clean separation principle: *the public has unique authority over the value component, while experts have epistemic advantages on the belief and causal-model components*. Neither group dominates across all components.

This decomposition connects to Hanson's futarchy principle (Hanson, 2013): "vote on values, bet on beliefs." Our framework extends this by adding the causal-model component (which is neither a pure value nor a pure belief) and the deliberative component (which is a value that requires epistemic input to refine).

The optimal governance mechanism, therefore, does not ask "who should decide?" but rather "*how should the decision be decomposed, and who should have authority over each component?*"

---

## 6. Main Results

We now state the main results of the paper. At their core, these results are properties of averages---they follow from the bias-variance decomposition applied to different estimation scenarios. We state them formally to make the conditions and trade-offs precise, but the underlying intuitions are straightforward. Each result is accompanied by a proof sketch and a simulation illustrating the key trade-off (simulation code forthcoming).

### 6.1 Bias-Variance Characterisation

The first result characterises when the full population's estimate dominates an expert subgroup's estimate, as a function of the bias correlation structure.

> **Assumption 1.** Preferences lie in $\Theta = \mathbb{R}^d$, the aggregation function is the componentwise mean, and the additive error model (6) holds. Idiosyncratic errors $\epsilon_i$ are i.i.d. with mean zero and covariance $\Sigma_\epsilon$. Systematic biases $b_i$ have mean $\mu_b \in \mathbb{R}^d$ and pairwise correlation $\rho_b$.

> **Assumption 2.** An expert subgroup $S$ of size $k \ll N$ has no systematic epistemic bias ($b_i = 0$ for $i \in S$) but has idiosyncratic noise with covariance $\Sigma_e$ where $\operatorname{tr}(\Sigma_e) \leq \operatorname{tr}(\Sigma_\epsilon)$. However, the expert subgroup has a value bias: $\mathbb{E}[\theta^\ast_i \mid i \in S] = G^{\ast} + \Delta_S$, where $\Delta_S \in \mathbb{R}^d$ reflects the non-representativeness of expert values.

> **Proposition 1 (Bias-Variance Characterisation).** Under Assumptions 1 and 2, the full-population estimate $\hat{G}_N$ has lower MSE than the expert estimate $\hat{G}_S$ if and only if
>
> $$\|\Delta_S\|^2 + \frac{\operatorname{tr}(\Sigma_e)}{k} > \|\mu_b\|^2 + \rho_b \operatorname{tr}(\Sigma_b) + \frac{\operatorname{tr}(\Sigma_\epsilon)}{N}, \tag{12}$$
>
> where $\Sigma_b = \operatorname{Var}(b_i)$.
>
> Equivalently, the population dominates when the expert's value bias $\|\Delta_S\|^2$ exceeds the population's epistemic bias $\|\mu_b\|^2 + \rho_b \operatorname{tr}(\Sigma_b)$, after accounting for the variance terms.

<details>
<summary><strong>Proof sketch</strong></summary>

The MSE of the population estimate is:

$$\operatorname{MSE}(\hat{G}_N) = \|\mu_b\|^2 + \rho_b \operatorname{tr}(\Sigma_b) + \frac{\operatorname{tr}(\Sigma_\epsilon) + (1-\rho_b)\operatorname{tr}(\Sigma_b)}{N}.$$

The first two terms are the irreducible bias from correlated systematic errors. The third term is the variance, which vanishes as $N \to \infty$.

The MSE of the expert estimate is:

$$\operatorname{MSE}(\hat{G}_S) = \|\Delta_S\|^2 + \frac{\operatorname{tr}(\Sigma_e)}{k}.$$

The first term is the squared value bias from non-representativeness. The second term is the variance from the small expert sample. Experts have no systematic epistemic bias by assumption, so there is no analogue of the $\|\mu_b\|^2 + \rho_b \operatorname{tr}(\Sigma_b)$ terms.

The condition $\operatorname{MSE}(\hat{G}_N) < \operatorname{MSE}(\hat{G}_S)$ yields (12) directly. $\blacksquare$
</details>

> **Remark.** Proposition 1 formalises the intuition that the population dominates when (a) expert value bias is large relative to population epistemic bias, and (b) the population is large enough that idiosyncratic noise is negligible. In the limit $N \to \infty$, the condition simplifies to $\|\Delta_S\|^2 + \operatorname{tr}(\Sigma_e) / k > \|\mu_b\|^2 + \rho_b \operatorname{tr}(\Sigma_b)$: the population wins whenever the expert's value distortion exceeds the population's correlated epistemic distortion.
>
> Conversely, experts dominate when the population's epistemic bias is large and correlated (high $\|\mu_b\|$, high $\rho_b$) and the expert group is sufficiently representative in values (low $\|\Delta_S\|$). This corresponds to technical domains where the public has systematic misconceptions but experts share the public's values.

> **Remark (On the choice of MSE).** The use of MSE (equivalently, quadratic loss) implies that over-estimation and under-estimation are equally costly, and that errors scale smoothly. In social choice, loss functions are rarely symmetric: the public may prefer a slightly suboptimal policy that preserves rights over a more "efficient" policy that violates them. Under non-quadratic loss---e.g., lexicographic preferences where rights violations incur infinite cost---the bias-variance trade-off changes qualitatively. MSE should be understood as a tractable proxy for "regret," not as a claim that all errors are equally bad. The qualitative insight (experts trade value-bias for epistemic-accuracy) holds under more general loss functions, but the precise crossover condition (12) is specific to quadratic loss.

![Figure 1: MSE of population estimate vs. expert estimate]({{site.baseurl}}/images/public-good/fig1_bias_variance.png)

*Figure 1: MSE of population estimate vs. expert estimate as a function of expert value bias $$\|\Delta_S\|$$ and population epistemic bias $$\|\mu_b\|$$. The crossover surface shows where the two estimates are equally accurate.*

### 6.2 Separation of Values and Beliefs

The second result shows that governance mechanisms which *separate* value-aggregation from fact-finding dominate those which conflate them.

> **Definition 6 (Conflated mechanism).** A *conflated mechanism* $\mathcal{M}_C$ asks each individual to report a policy preference $\hat{\theta}_i(a)$ that bundles together their values, beliefs, and causal reasoning, and aggregates these directly: $\hat{G}_C = f(\hat{\theta}_1, \ldots, \hat{\theta}_N)$.

> **Definition 7 (Separated mechanism).** A *separated mechanism* $\mathcal{M}_S$ decomposes the decision into:
>
> 1. A *value-aggregation* step: collect $\{v_i\}_{i=1}^N$ and compute $\bar{v} = g(v_1, \ldots, v_N)$ for some value-aggregation function $g$.
> 2. A *fact-finding* step: obtain an estimate $\hat{s}_E$ of $s^*$ from experts or prediction markets.
> 3. A *consequence-computation* step: obtain an estimate $\hat{C}_E$ of $C$ from experts or models.
> 4. A *combination* step: compute $\hat{G}_S = \bar{v}(\hat{C}_E(a \mid \hat{s}_E))$.

> **Assumption 3.** The value-aggregation function $g$ is unbiased for the population's true aggregated values: $\mathbb{E}[g(v_1, \ldots, v_N)] = f(v_1, \ldots, v_N)$. The expert estimates satisfy $\|\hat{s}_E - s^{\ast}\| < \|\bar{\hat{s}} - s^{\ast}\|$ and $\|\hat{C}_E - C\| < \|\bar{\hat{C}} - C\|$, where $\bar{\hat{s}}$ and $\bar{\hat{C}}$ are the population averages of beliefs and causal models respectively.

> **Theorem 2 (Separation Dominance).** Under Assumption 3, and assuming that value functions $v_i$ are Lipschitz continuous with constant $L$, the separated mechanism $\mathcal{M}_S$ has lower MSE than the conflated mechanism $\mathcal{M}_C$:
>
> $$\operatorname{MSE}(\hat{G}_{\mathcal{M}_S}) \leq \operatorname{MSE}(\hat{G}_{\mathcal{M}_C}).$$
>
> The improvement is strict whenever the expert estimates of $s^*$ and $C$ are strictly better than the population averages.

<details>
<summary><strong>Proof sketch</strong></summary>

The conflated mechanism's error combines value noise, belief error, and causal-model error in a single aggregate. By the decomposition in (10), the MSE of the conflated mechanism includes cross-terms between value noise and epistemic errors.

The separated mechanism eliminates the epistemic error components by substituting expert estimates, retaining only the (unbiased, low-variance) value aggregation error. By the Lipschitz assumption, the error in the combination step is bounded by $L \cdot (\|\hat{s}_E - s^*\| + \|\hat{C}_E - C\|)$, which is smaller than the corresponding population-level epistemic error by Assumption 3.

Formally, let $\hat{G}_C = \frac{1}{N}\sum_i v_i(\hat{C}_i(a \mid \hat{s}_i))$ and $\hat{G}_S = \frac{1}{N}\sum_i v_i(\hat{C}_E(a \mid \hat{s}_E))$. Then:

$$\|\hat{G}_S - G^*\| = \left\|\frac{1}{N}\sum_i \left[v_i(\hat{C}_E(a \mid \hat{s}_E)) - v_i(C(a \mid s^*))\right]\right\| \leq L \cdot \|\hat{C}_E(a \mid \hat{s}_E) - C(a \mid s^*)\|,$$

which depends only on the expert's epistemic error, not the population's. The conflated mechanism's error additionally includes the population's epistemic errors, which are larger by assumption. $\blacksquare$
</details>

> **Remark.** Theorem 2 provides a formal justification for the institutional separation of powers---not as a political compromise, but as an information-theoretic optimality result. The mechanism is more accurate precisely because it routes each component of the decision to the group with the relevant epistemic advantage.

> **Remark (Lipschitz assumption and sacred values).** The Lipschitz continuity assumption on $v_i$ rules out "cliffs" in value functions---sacred values, taboos, or lexicographic preferences where a small change in outcome causes a massive drop in utility. If an expert makes a *small* error in the causal model $C$ that crosses a taboo line (e.g., a policy that was just below a rights-violation threshold now just exceeds it), the public's utility loss could be unbounded, breaking the Lipschitz bound. In domains involving rights, sacred values, or bright-line rules, the separation theorem is less reliable, and additional safeguards---constitutional constraints, veto mechanisms, or explicit taboo-checking---are needed on top of the separated mechanism.

![Figure 2: Conflated vs separated mechanisms]({{site.baseurl}}/images/public-good/fig2_separation.png)

*Figure 2: Comparing MSE of conflated vs. separated mechanisms across varying levels of public epistemic error, with expert epistemic error held fixed.*

### 6.3 Delegation Bounds

The separation theorem assumes that experts provide only epistemic inputs and do not inject their own values. In practice, the boundary between "facts" and "values" is porous: experts may smuggle value judgments into ostensibly factual recommendations. The third result characterises how much authority can be safely delegated.

> **Definition 8 (Value leakage).** An expert's recommendation exhibits *value leakage* of magnitude $\lambda \geq 0$ if their reported belief or causal model is biased toward their own preferred outcome:
>
> $$\hat{s}_E = s^{\ast}+ \lambda \cdot \nabla_s v_E(s^*),$$
>
> where $v_E$ is the expert's value function. That is, the expert (consciously or unconsciously) distorts their factual report in the direction that favours their preferred policy.

> **Theorem 3 (Delegation Bounds).** Under the model of Definition 8, delegation to experts reduces MSE relative to the conflated mechanism if and only if the value leakage is bounded:
>
> $$\lambda < \frac{\|\bar{\hat{s}} - s^*\|}{L \cdot \|\nabla_s v_E(s^*)\|}, \tag{13}$$
>
> where $\bar{\hat{s}} = \frac{1}{N}\sum_i \hat{s}_i$ is the population's average belief and $L$ is the Lipschitz constant of the aggregated value function.
>
> When (13) is violated, the expert's value-contaminated recommendation is *worse* than the population's epistemically noisy but value-representative estimate.

<details>
<summary><strong>Proof sketch</strong></summary>

The separated mechanism with value leakage produces an estimate with error:

$$\hat{G}_S - G^{\ast}\approx L \cdot \lambda \cdot \nabla_s v_E(s^*).$$

The conflated mechanism produces an estimate with error approximately $L \cdot (\bar{\hat{s}} - s^\ast)$. The separated mechanism dominates when $\lambda \|\nabla_s v_E\| < \|\bar{\hat{s}} - s^\ast\|$, yielding (13). $\blacksquare$
</details>

> **Remark.** Theorem 3 formalises the intuition that delegation is safe when experts are honest (low $\lambda$), the public is ignorant (high $\|\bar{\hat{s}} - s^\ast\|$), and the expert's values are not too extreme (low $\|\nabla_s v_E\|$). It also suggests institutional designs that reduce $\lambda$: transparency requirements, adversarial expert panels, and prediction markets (which aggregate expert beliefs without giving any single expert the ability to inject values).

> **Remark (Detecting value leakage).** A practical challenge is that sophisticated experts can embed value judgments inside complex causal models where they are difficult to detect. For example, the choice of discount rate in a cost-benefit analysis, the welfare weights in an economic model, or the risk threshold in a safety assessment all encode values disguised as technical parameters. Possible detection mechanisms include: (a) *adversarial expert panels*, where experts with different values review each other's models and flag assumptions that encode contested values; (b) *model transparency*, requiring experts to submit full models (not just conclusions) so that assumptions can be audited; (c) *sensitivity analysis*, systematically varying model assumptions to identify which ones drive the policy recommendation; and (d) *prediction market cross-checks*, where expert factual claims are tested against market prices. The fundamental challenge remains: the more complex the causal model, the more places values can hide. This motivates institutional designs that structurally separate model-building from value-weighting, rather than relying on post-hoc detection.

![Figure 3: Delegation benefit vs value leakage]({{site.baseurl}}/images/public-good/fig3_delegation.png)

*Figure 3: Delegation benefit (reduction in MSE) as a function of value leakage $$\lambda$$, showing the crossover point where delegation becomes harmful.*

### 6.4 Limits of Pure Technocracy

The fourth result shows that pure technocracy---governance by experts alone---is fundamentally limited by the fact that experts are a small, non-random subpopulation.

> **Assumption 4.** Expert group $S$ of size $k$ is formed by a selection process (education, professional training, self-selection into a field). We assume:
>
> 1. Epistemic ability is high: $\hat{s}_i = s^\ast$ and $\hat{C}_i = C$ for $i \in S$ (perfect beliefs and causal models).
> 2. Expert values $\{v_i\}_{i \in S}$ are drawn from a subpopulation distribution $\mathcal{D}_S$ that may differ from the population distribution $\mathcal{D}$. Let $$\Delta_S = \mathbb{E}_{\mathcal{D}_S}[v_i] - \mathbb{E}_{\mathcal{D}}[v_i]$$ denote the mean value shift.
> 3. The within-group value correlation satisfies $\operatorname{Corr}(v_i, v_j) \geq \rho_S > 0$ for $i, j \in S$.
>
> Note that we do *not* assume $\Delta_S \neq 0$. Instead, we show that $\Delta_S = 0$ is statistically unlikely for any non-random selection process.

> **Proposition 4 (Limits of Pure Technocracy).** Under Assumption 4, for any expert group $S$ of size $k$:
>
> **(a)** The expert estimate satisfies:
>
> $$\operatorname{MSE}(\hat{G}_S) = \Delta_S^2 + \frac{\operatorname{Var}_{\mathcal{D}_S}(v_i)}{k}\left(1 + (k-1)\rho_S\right),$$
>
> which converges to $\Delta_S^2 + \rho_S \cdot \operatorname{Var}_{\mathcal{D}_S}(v_i) > 0$ as $k \to \infty$, regardless of epistemic perfection.
>
> **(b)** Even if experts were a random sample ($\Delta_S = 0$ in expectation), the probability that their sample mean value is within $\epsilon$ of the population mean is bounded by:
>
> $$P\!\left(\|\bar{v}_S - \bar{v}_N\| < \epsilon\right) \leq \frac{\operatorname{Var}_{\mathcal{D}}(v_i)}{k_{\text{eff}} \cdot \epsilon^2}, \quad \text{where } k_{\text{eff}} = \frac{k}{1 + (k-1)\rho_S}.$$
>
> When $\rho_S$ is large (shared training correlates values), the effective sample size $k_{\text{eff}}$ can be much smaller than $k$, making accurate value estimation unlikely.
>
> **(c)** In contrast, the expert estimate of *facts* has low error because experts have access to ground truth ($\hat{s}_i = s^\ast$), not because there are many of them. The asymmetry is: experts are accurate on facts *by training*, but inaccurate on values *by sampling*.

<details>
<summary><strong>Proof sketch</strong></summary>

Since experts have perfect beliefs and causal models, their stated preferences equal $\hat{\theta}_i = v_i(C(a \mid s^\ast))$ for $i \in S$. The expert estimate is $\hat{G}_S = \frac{1}{k}\sum_{i \in S} v_i(C(a \mid s^\ast))$.

The MSE decomposes as:

$$\operatorname{MSE}(\hat{G}_S) = \left(\mathbb{E}[\hat{G}_S] - G^\ast\right)^2 + \operatorname{Var}(\hat{G}_S) = \Delta_S^2 + \frac{\operatorname{Var}_{\mathcal{D}_S}(v_i)}{k}\left(1 + (k-1)\rho_S\right).$$

The first term is the squared value bias from non-representativeness. The second term is the sampling variance, inflated by within-group correlation. As $k \to \infty$, the variance term converges to $\rho_S \cdot \operatorname{Var}_{\mathcal{D}_S}(v_i)$ rather than zero.

For part (b), by Chebyshev's inequality applied to the sample mean with effective sample size $k_{\text{eff}} = k / (1 + (k-1)\rho_S)$, the probability of the sample mean being close to the population mean is bounded as stated. When $\rho_S \to 1$, we have $k_{\text{eff}} \to 1$ regardless of $k$---the entire expert group behaves like a single draw from the value distribution. $\blacksquare$
</details>

> **Remark.** Proposition 4 reframes the technocracy problem as a *sampling* problem rather than assuming experts are biased. We do not need to claim that experts are "biased" in a pejorative sense---only that they are a small, correlated, non-random sample of the population. By the Central Limit Theorem, any subgroup of size $k$ drawn from a heterogeneous population will have sampling error $$O(1/\sqrt{k_{\text{eff}}})$$ in its value estimates. The shared training that gives experts epistemic advantages simultaneously reduces $k_{\text{eff}}$ by correlating their values. This is not a moral failing but a statistical inevitability: small correlated samples have high variance.

![Figure 4: Expert MSE vs group size]({{site.baseurl}}/images/public-good/fig4_technocracy.png)

*Figure 4: Expert group MSE as a function of group size $k$ for different within-group correlations $$\rho_S$$, showing the irreducible error floor from value correlation. Compare with the population MSE (which decreases as $$1/N$$).*

### 6.5 Deliberation as Debiasing

Finally, we consider whether deliberative processes can reduce the errors identified above.

> **Definition 9 (Citizens' assembly).** A *citizens' assembly* is a mechanism that:
>
> 1. Selects a random sample $A \subset \{1, \ldots, N\}$ of size $n$ (sortition).
> 2. Provides participants with expert briefings, increasing their deliberative refinement from $r_i$ to $r_i' \geq r_i$ and improving their beliefs from $\hat{s}_i$ to $\hat{s}_i'$ with $\|\hat{s}_i' - s^*\| \leq \|\hat{s}_i - s^*\|$.
> 3. Facilitates structured deliberation among participants.

> **Conjecture 1 (Deliberation as Debiasing).** Under a citizens' assembly mechanism (Definition 9), if the deliberation process satisfies:
>
> **(a) Epistemic improvement:** $\mathbb{E}[\|\hat{s}_i' - s^*\|^2] < \mathbb{E}[\|\hat{s}_i - s^*\|^2]$ for $i \in A$ (beliefs improve).
>
> **(b) Causal model improvement:** $\mathbb{E}[\|\hat{C}_i' - C\|^2] < \mathbb{E}[\|\hat{C}_i - C\|^2]$ for $i \in A$ (causal understanding improves).
>
> **(c) Value preservation:** The distribution of $\{v_i\}_{i \in A}$ remains representative of $\{v_i\}_{i=1}^N$ after deliberation (values are not homogenised).
>
> **(d) Decorrelation:** The pairwise correlation of post-deliberation causal-model errors $\operatorname{Corr}(\hat{C}_i' - C, \hat{C}_j' - C)$ is lower than the pre-deliberation correlation, for $i, j \in A$.
>
> Then the citizens' assembly estimate $\hat{G}_A$ has lower MSE than both the raw population estimate $\hat{G}_N$ and the expert estimate $\hat{G}_S$, provided $n$ is sufficiently large.

> **Remark.** We state this as a conjecture rather than a theorem because conditions (c) and (d) are empirical claims about the effects of deliberation that cannot be derived from the model alone. There is substantial empirical evidence that well-designed deliberative processes satisfy these conditions (Fishkin, 2009; Landemore, 2012), but a formal proof would require a specific model of how deliberation transforms beliefs and causal models.
>
> The conjecture provides a formal justification for sortition combined with deliberation: random selection ensures value representativeness (addressing the expert sampling problem of Proposition 4), while structured deliberation reduces epistemic errors (addressing the correlated bias problem of [Section 3.3](#33-correlated-bias-via-social-influence)). This combination achieves what neither pure democracy nor pure technocracy can: representative values *and* informed beliefs.

---

## 7. Governance Architecture

The results of [Section 6](#6-main-results) imply a specific governance architecture. Rather than asking "who should decide?" the framework asks "how should the decision be decomposed, and who should have authority over each component?"

### 7.1 Component-Authority Mapping

The following table maps each decision component to the group with the appropriate epistemic advantage and the institutional mechanism best suited to elicit that group's input.

| **Component** | **Authority** | **Mechanism** | **Justification** |
|---|---|---|---|
| Values ($v_i$) | The public | Voting, quadratic voting | Proposition 4 |
| Facts ($s^*$) | Experts / Markets | Prediction markets, peer review | Theorem 2 |
| Consequences ($C$) | Experts / Models | Impact assessments, simulations | Theorem 2 |
| Deliberation | Public after deliberation | Citizens' assemblies | Conjecture 1 |

**Table 2.** Governance architecture: mapping decision components to authorities and mechanisms.

This architecture is not merely a political compromise---it is an *information-theoretic optimality result*. Each component is routed to the group that minimises the expected estimation error for that component, subject to the constraint that no group's values are substituted for the population's.

### 7.2 Design Requirements

The formal results translate into concrete institutional design requirements:

1. **Media plurality and anti-manipulation measures** (Proposition 1): The population's estimate is good only when systematic biases are sufficiently uncorrelated. This requires diverse information sources and resistance to coordinated propaganda. Formally, the goal is to minimise $\rho_b$---the pairwise correlation of systematic biases.

2. **Robust aggregation rules** (Proposition 1): The choice of aggregation function $f$ matters. Robust estimators such as the geometric median are more resistant to correlated manipulation than the arithmetic mean, because they down-weight outliers that may result from coordinated influence campaigns.

3. **Transparent expert institutions with adversarial oversight** (Theorem 3): Delegation to experts is safe only when value leakage $\lambda$ is small. Institutional designs that reduce $\lambda$ include: transparency requirements, adversarial expert panels (where experts with different values check each other), and prediction markets (which aggregate beliefs without giving any individual the power to inject values).

4. **Constitutional structures** ([Section 7.2](#72-the-problem-of-future-preferences)): Constraints that limit what the current majority can decide, protecting dimensions where systematic bias is known to be high (expert domains, future interests, minority rights).

5. **Deliberative institutions** (Conjecture 1): Citizens' assemblies and structured deliberation as mechanisms for reducing epistemic errors while preserving value diversity.

---

## 8. Discussion

### Relationship to Existing Frameworks

Our framework connects to and extends several existing lines of work:

**Condorcet Jury Theorem.** The classical result (Condorcet, 1785) shows that majority rule converges to the correct answer when voters are independent and individually more likely to be correct than not. Our Proposition 1 generalises this from binary decisions to continuous preference aggregation and explicitly characterises the failure mode: correlated errors. The Condorcet theorem is a special case of our framework where there is no value disagreement (everyone wants the "correct" answer) and the only question is epistemic.

**Arrow's Impossibility Theorem.** Arrow (1951) shows that no aggregation function satisfies a set of desirable axioms simultaneously. Our framework sidesteps this by taking $f$ as given and asking the *estimation* question: given $f$, who best estimates $f(\theta^*_1, \ldots, \theta^*_N)$? The choice of $f$ remains a normative question that our framework does not resolve.

**Futarchy.** Hanson's proposal to "vote on values, bet on beliefs" (Hanson, 2013) is a special case of our separated mechanism (Definition 7). Our framework extends futarchy by (a) adding the causal-model component, which is neither a pure value nor a pure belief, (b) providing formal conditions under which separation dominates (Theorem 2), and (c) characterising the limits of delegation (Theorem 3).

**Epistemic democracy.** Landemore (2012) and List & Goodin (2001) argue that democratic procedures have epistemic virtues---they tend to produce good decisions, not just legitimate ones. Our framework provides a formal basis for this claim: democratic aggregation is epistemically optimal for the *value component* of decisions, precisely because the population is the only unbiased sample of its own values (Proposition 4).

**Epistocracy.** Brennan (2016) argues that the public is too ignorant to govern well. Our framework partially vindicates this concern: the public *is* systematically wrong about facts and causal models ([Section 3.4](#34-systematic-belief-and-causal-model-errors)). But it also shows that the epistocratic solution---replacing public authority with expert authority---introduces a different and equally serious error: value sampling bias (Proposition 4). The resolution is not to choose between democracy and epistocracy but to decompose the decision and allocate each component appropriately.

### Limitations

Several important limitations should be noted:

1. **The choice of $f$ is normative.** Our framework takes the aggregation function as given. But the choice between utilitarian aggregation, Rawlsian maximin, and other social welfare functions is itself a deep normative question (Rawls, 1971; Harsanyi, 1955). Our results hold for any $f$, but the practical implications depend on which $f$ is chosen.

2. **True preferences are unobservable.** The definition of $\theta^{\ast}_i$ as what individual $i$ would want under ideal conditions is a theoretical construct. It cannot be directly measured, and it is not clear that it is even well-defined (preferences may not converge under unlimited reflection). Our framework requires only that $\theta^{\ast}_i$ is a useful idealisation, not that it is precisely defined.

3. **The linear model is restrictive.** The additive error model of [Section 3.1](#31-additive-error-model) and the Lipschitz assumptions in the proofs are simplifications. Real preference formation involves nonlinear interactions between values, beliefs, and social context. Extending the results to more realistic models is an important direction for future work.

4. **Separability may not hold.** The decomposition into values, beliefs, and causal models assumes these components are separable. In practice, values and beliefs are often entangled---people's factual beliefs may be motivated by their values, and their values may be shaped by their factual understanding (Kahneman, 2011). The separation theorem (Theorem 2) is most useful when this entanglement is weak.

5. **Strategic behaviour is not modelled.** We assume individuals report preferences sincerely. In practice, strategic misreporting is a major concern (Gibbard, 1973; Satterthwaite, 1975). Extending the framework to account for strategic behaviour is an important open problem.

### Future Work

Several directions for future research emerge from this framework:

1. **Full formal proofs.** The theorems in [Section 6](#6-main-results) are stated with proof sketches. Completing the proofs---particularly for the separation theorem under weaker assumptions---is a priority.

2. **Robustness of aggregation functions.** Characterising which aggregation functions $f$ are most resistant to correlated manipulation. The geometric median is a natural candidate, as it is robust to outliers and has been studied in the context of decentralised governance.

3. **Mechanism design for bias decorrelation.** What institutional designs minimise the correlation of systematic biases $\rho_b$? Does deliberation before voting decorrelate errors? Can this be proved in a formal model? This connects the philosophical claim to concrete institutional design.

4. **Empirical validation.** Testing the predictions of the framework against data from citizens' assemblies, prediction markets, and expert panels. The key empirical question is whether the error decomposition of Table 1 holds in practice.

5. **Dynamic models.** Extending the framework to account for preference change over time, learning, and the co-evolution of values and beliefs.

---

## 9. Conclusion

We have proposed a formal framework for the question "who should define the public good?" by recasting it as an estimation problem. The public good is defined as an aggregation of individuals' idealised preferences, and any governance mechanism produces an estimate of this target.

The key insight is that individual preferences decompose into four components---core values, factual beliefs, causal models, and deliberative refinement---each with a distinct error structure. Idiosyncratic value noise washes out with population size, but correlated belief and causal-model errors do not. This decomposition yields a precise answer to the motivating question:

> *The public has unique and irreplaceable authority over the value component of the public good. No expert subgroup can substitute for the population's values without introducing systematic bias. However, the public's policy preferences---which combine values with beliefs and causal reasoning---can be systematically wrong. Experts dominate for the belief and causal-model components.*

The optimal governance mechanism therefore *decomposes* decisions into value-components (aggregated democratically) and epistemic-components (informed by experts or markets), and combines them. This is not "democracy versus technocracy" but a principled division of labour grounded in information theory.

The public defines what is good. Experts help determine how to get there. The governance mechanism's job is to implement this separation cleanly.

---

## References

- Arrow, K. J. (1951). *Social Choice and Individual Values*. Wiley.
- Austen-Smith, D. & Banks, J. S. (1996). Information Aggregation, Rationality, and the Condorcet Jury Theorem. *American Political Science Review*, 90(1), 34–45.
- Brennan, J. (2016). *Against Democracy*. Princeton University Press.
- Condorcet, Marquis de (1785). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*. Imprimerie Royale.
- Fishkin, J. S. (2009). *When the People Speak: Deliberative Democracy and Public Consultation*. Oxford University Press.
- Galton, F. (1907). Vox Populi. *Nature*, 75, 450–451.
- Gibbard, A. (1973). Manipulation of Voting Schemes: A General Result. *Econometrica*, 41(4), 587–601.
- Hanson, R. (2013). Shall We Vote on Values, But Bet on Beliefs? *Journal of Political Philosophy*, 21(2), 151–178.
- Harsanyi, J. C. (1955). Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility. *Journal of Political Economy*, 63(4), 309–321.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Ladha, K. K. (1992). The Condorcet Jury Theorem, Free Speech, and Correlated Votes. *American Journal of Political Science*, 36(3), 617–634.
- Landemore, H. (2012). *Democratic Reason: Politics, Collective Intelligence, and the Rule of the Many*. Princeton University Press.
- List, C. & Goodin, R. E. (2001). Epistemic Democracy: Generalizing the Condorcet Jury Theorem. *Journal of Political Philosophy*, 9(3), 277–306.
- Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
- Satterthwaite, M. A. (1975). Strategy-Proofness and Arrow's Conditions: Existence and Correspondence Theorems for Voting Procedures and Social Welfare Functions. *Journal of Economic Theory*, 10(2), 187–217.
- Sen, A. (1999). *Development as Freedom*. Oxford University Press.
- Sunstein, C. R. (2002). The Law of Group Polarization. *Journal of Political Philosophy*, 10(2), 175–195.
- Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday.
- Weitzman, M. L. (1998). Why the Far-Distant Future Should Be Discounted at Its Lowest Possible Rate. *Journal of Environmental Economics and Management*, 36(3), 201–208.