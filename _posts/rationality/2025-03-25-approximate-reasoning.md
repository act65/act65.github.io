---
layout: post
title: "Every Bias Names an Algorithm"
subtitle: "Bounded reasoners trade accuracy for efficiency in three places, and each trade leaves its own fingerprint"
permalink: /approximate-reasoning/
categories:
  - "play"
description: "Cognitive biases and LLM failures are the characteristic error patterns of specific approximation algorithms. From the errors you can infer the algorithm."
tags:
  - essay
  - formalised
  - abstraction
  - uncertainty
  - probability
  - computation
  - epistemology
---

Reasoning is expensive. A system with finite memory, finite time, and finite data cannot compute the right answer to every question, so it computes something cheaper instead. Every cheap method is exact on some inputs and wrong on others, and *which* inputs it fails on is not arbitrary — it is determined by the method.

That is the claim of this post:

> **A bias is the characteristic error pattern of a specific approximation algorithm. Given the errors, you can work backwards to the algorithm.**

This is a claim about mechanism, not about optimality. I am not going to argue that any of these strategies is the best possible use of a budget — that would need a lot more machinery. The weaker claim is enough to be useful, because it is falsifiable and it makes predictions.

The main prediction, which the rest of the post builds toward: **not every bias can be fixed by thinking longer, and you can tell in advance which ones can.**

### Three places to be cheap

A reasoner holds a representation $\hat{G}$ of the world, answers queries $q$ drawn from a distribution $Q$, and is scored against a target $f^\ast(q)$. It has a budget: $S$ bits of storage, $T$ operations per query, $N$ samples of evidence. The problem is

$$
\min_{\hat{G}, \hat{f}} \; \mathbb{E}_{q \sim Q}\big[L\big(\hat{f}(q; \hat{G}),\, f^\ast(q)\big)\big]
\quad \text{s.t.} \quad
|\hat{G}| \le S, \;\; \mathrm{cost}(\hat{f}) \le T, \;\; \mathrm{samples} \le N.
$$

There are three constraints, so there are three ways to be cheap:

1. **Representation** — store less. Cut $S$.
2. **Inference** — compute less. Cut $T$.
3. **Evidence** — look at less. Cut $N$.

That is the whole taxonomy. It isn't a carve-up I chose; it's the constraint set. Every strategy below is an answer to *which budget line do I cut, and what breaks when I cut it*.

The three cuts have different mathematical characters, and this is where the predictions come from:

| Family | Error behaves like | Error floor | More compute at query time? |
|---|---|---|---|
| Representation | rate–distortion | fixed by bits; irreducible | No effect |
| Inference | geometric contraction | decays as $\rho^k$ over $k$ steps | Fixes it |
| Evidence | Monte Carlo error | decays as $1/\sqrt{N}$, if unbiased | Depends on the sampler |

### Why any bounded learner faces this

Humans and language models don't share constraints. LLMs have enormous memory, no metabolic budget, and no evolutionary history. So it needs explaining why the same strategies would show up in both.

The reason is not shared constraints but a shared *task*. Both face a query distribution $Q$ that is heavy-tailed. Language is Zipfian.[^zipf] So are the objects you have to categorise and the situations you have to act in. A handful of queries are enormously frequent and an unbounded number are vanishingly rare.

Under a heavy-tailed $Q$ with a fixed budget, the allocation is forced: spend on the head, fail in the tail. Feldman gives the sharp version — under a long-tailed data distribution, memorising the tail is *necessary* for optimal generalisation, so any learner that cannot afford to memorise the tail must eat the error there.[^feldman]

This is a claim about the optimisation problem, not about brains or transformers, and it predicts that errors should concentrate in the tail of $Q$ for any bounded learner regardless of substrate.

---

## Family 1: Representation

**Cut storage. Error obeys rate–distortion, and no amount of query-time compute recovers it.**

Compress a source to $R$ bits and you can distinguish at most $2^R$ states. Any two inputs mapped to the same codeword are *necessarily* confused — not through a flaw in the compressor but by the pigeonhole principle. So a compressed representation doesn't merely happen to make category errors; it is guaranteed to, and the only design question is which distinctions get sacrificed. Rate–distortion theory says an efficient code sacrifices whichever distinctions are rare or cheap to get wrong.[^sims][^zaslavsky]

This is the family's signature: the information is not there, so reasoning cannot recover it.

### 1.1 Chunking — path contraction

**The algorithm.** You have a graph and you answer reachability or shortest-path queries on it. BFS from $s$ to $e$ costs $O(V + E)$ per query. If the query distribution is concentrated — the same few $(s, e)$ pairs over and over — you can precompute those paths and store each as a single edge with a cached cost. Query time drops to $O(1)$ for cached pairs. This is a transitive-closure cache, or in planning terms a macro-operator: a fixed action sequence promoted to a single action.[^korf]

The trade is exact and visible in the data structure. You store $s \to e$ with a total cost. You do **not** store the intermediate nodes. So:

- Cached queries: constant time, exact answer.
- Uncached queries: no help at all, fall back to search.
- Any query about the *interior* of a cached path: unanswerable.

**Worked example — chess.** Chase and Simon showed masters reconstruct realistic board positions far better than novices, but not random ones.[^chase] The macro-operator reading: a master has cached a mapping from board configurations to move sequences. Given a legal position, the lookup hits and returns a strong move in roughly constant time. Given a random position, nothing matches, and the master falls back to the same search the novice runs.

The predicted failure follows from the data structure, not from a separate theory of expertise: masters should be unable to report the intermediate steps, because the intermediate steps are not stored. This is exactly what expert introspection looks like — "it just looked right." The knowledge is in the contracted edge; the path it replaced was discarded.

**Worked example — phone numbers.** `0212345678` is ten symbols; at roughly four items of working memory[^miller][^cowan] you cannot hold it. Contract it into three cached units — `021`, `234`, `5678` — and it fits. Note the trade: you can now recall the number but you have lost random access. Asking someone for the seventh digit of a number they know perfectly well forces them to replay the chunks from the start. The interior of the contracted path is not addressable.

**LLM analogue.** Multi-token units in the tokenizer and in learned circuits: frequent sequences generate as blocks, and models routinely produce a correct answer while being unable to produce the intermediate steps that would justify it.

### 1.2 Prototypes — vector quantization

**The algorithm.** You need to store $n$ items in $d$ dimensions, which costs $O(nd)$. Instead, run k-means, keep $k \ll n$ centroids, and store each item as the index of its nearest centroid. Storage drops to $O(kd + n\log k)$. Reconstruction returns the centroid, not the item.

The error is quantization error, and its distribution is not uniform. Items near a centroid reconstruct almost perfectly. Items near a cell boundary reconstruct badly and are unstable — a tiny perturbation flips them to a different codeword.

**Worked example — categorisation.** Rosch found that category membership is graded: robins are judged "birdier" than penguins, and verified faster.[^rosch] Under quantization these are the same statement. A robin sits near the centroid of the bird cell, so reconstruction error is small and the nearest-centroid lookup is unambiguous. A penguin sits near the boundary between cells, so error is large and the lookup is slow and unstable. Typicality effects and boundary fuzziness are not two phenomena; they are the distance-to-centroid distribution seen twice.

Zaslavsky and colleagues made this quantitative for colour naming: languages partition colour space close to optimally under a rate–distortion objective, and the partitions they choose are predicted by the statistics of colour use.[^zaslavsky]

The uncomfortable corollary: stereotyping is the same operation with people as the items. Not a separate moral failing bolted onto cognition — the same lookup, with a catastrophically different cost matrix on the errors.

**LLM analogue.** Embedding spaces are literally this, and the failures match: mode averaging, loss of low-frequency distinctions, and unstable behaviour on inputs that fall between training clusters.

### 1.3 Schemas — low-rank factorization

**The algorithm.** Storing every relation among $n$ entities costs $O(n^2)$. Instead, learn a $d$-dimensional embedding per entity and a scoring function, and *predict* relations on demand: $\hat{A} \approx UV^\top$ with $U, V \in \mathbb{R}^{n \times d}$. Storage drops from $O(n^2)$ to $O(nd)$. This is standard link prediction.

The failure mode of low-rank approximation is specific and well understood. On-manifold pairs — those whose true relations are well explained by the top $d$ factors — reconstruct accurately. Off-manifold pairs get a confident, plausible, wrong prediction, because the model has no representation for "this pair is not covered by my factors." It returns the best rank-$d$ answer regardless.

**Worked example — scripts.** You have never visited this restaurant, so there is no stored edge from *this restaurant* to *how to order here*. The schema generates one from the factors: restaurants have menus, you wait to be seated, you pay after eating.[^schank][^bartlett] Usually right. When it is wrong it is wrong in a specific way — the generated relation is not noise, it is the most plausible relation given the factors. You confidently wait to be seated in a place where you order at the counter.

This is worth stating clearly because it is the mechanism behind confabulation: **a generative approximation queried outside its support does not return "unknown", it returns its best guess with the same confidence it returns known facts.** There is no error signal available inside the algorithm to distinguish the two cases.

**LLM analogue.** Fabricated citations are the canonical case: real authors, real journals, plausible titles, a paper that does not exist. That is a rank-$d$ reconstruction of the author–paper matrix returning its best guess for an entry it never saw.

### 1.4 Forgetting — cache eviction

**The algorithm.** A cache with $S$ slots and an item stream needs an eviction policy. LRU evicts least-recently-used; LFU evicts least-frequently-used. The optimal policy evicts whichever item has the lowest probability of being requested again, which under most realistic access patterns is well approximated by a decaying function of recency and frequency.

**Worked example.** Anderson and Schooler compared human retention curves against the actual probability that a given item would be needed again, measured in real environments — word frequencies in newspaper headlines, in parental speech, in email.[^anderson1991] The forgetting curve tracks the environmental need-odds curve closely. Memory is not failing to hold things; it is running an eviction policy tuned to the request distribution.

This reframes forgetting as a design choice rather than a defect, and it predicts something: memory should be *worse* for items whose environmental statistics are misleading. An item you saw many times long ago and will never need again should be stubbornly retained, because LFU says keep it. That is roughly what outdated knowledge looks like.

**LLM analogue.** Weight decay and dropout, deliberately spending capacity away from the tail; and context truncation as a crude LRU.

---

## Family 2: Inference

**Cut compute. Error decays geometrically in the number of steps, so more query-time compute genuinely helps.**

### 2.1 Anchoring — truncated iteration

**The algorithm.** Any iterative solver that contracts toward a fixed point at rate $\rho < 1$, started from an initial guess:

```python
def adjust(anchor, target, k, rho=0.7):
    """k steps of an iterative solver started at `anchor`."""
    theta = anchor
    for _ in range(k):
        theta += (1 - rho) * (target - theta)
    return theta
```

The residual is exact:

$$\theta_k - \text{target} = \rho^k\,(\text{anchor} - \text{target}).$$

Stop early and you land short of the answer, displaced toward where you started, by an amount proportional to the anchor's distance and shrinking geometrically in $k$.

**This *is* anchoring-and-adjustment, derived rather than described.** Insufficient adjustment is not stubbornness; it is what truncation does. And the derivation makes quantitative predictions the verbal version does not:

- Bias should be **linear** in the anchor's distance from the truth.
- Bias should **decay geometrically** with time to think.
- Bias should persist even when the subject knows the anchor is arbitrary, because knowing the anchor is uninformative does not give you a better starting point.

All three hold. Lieder and colleagues ran the resource-rational version and found observed adjustment magnitudes match the predicted optimal stopping point.[^lieder2018]

**Worked example.** Ask for the year Genghis Khan died. Most people start from a known anchor (something like "the Mongol conquests, so 1200s") and adjust. With $\rho = 0.7$, an anchor of 1200, a target of 1227, and three steps: the estimate lands at $1227 - 0.7^3 \times 27 \approx 1218$. Short, in the anchor's direction, by a predictable amount.

**LLM analogue.** Numeric answers pulled toward values mentioned in the prompt, and the fact that longer chains of thought reduce the pull.

### 2.2 Satisficing — early-stopped search

**The algorithm.** Exhaustive search over $n$ candidates costs $O(n)$ evaluations and returns the max. Threshold search returns the first candidate above an aspiration level $A$ and costs $O(1/P(x > A))$ in expectation. Simon's satisficing is this, with $A$ set adaptively.[^simon]

The classic analysis is the secretary problem: reject the first $n/e$ candidates, then take the first one better than everything seen. This gets the true best about 37% of the time, from a single pass, no backtracking. The trade is legible — you accept a bounded probability of missing the optimum in exchange for a linear-to-constant reduction in evaluations.

**Worked example.** Choosing a restaurant. Exhaustive comparison over every restaurant in the city is $O(n)$ evaluations, each expensive. Threshold search walks until something clears the bar. The characteristic error is not random: you systematically end up with above-average, non-optimal choices, and — this is the diagnostic part — you feel *no regret*, because you never evaluated the alternatives you skipped. Missing information about foregone options is a property of the algorithm, not of the chooser's attitude.

**LLM analogue.** Generation halts at an end-of-sequence token judged sufficient, not at a verified-optimal answer. Anytime behaviour: an answer exists at every point, quality improves with budget, and there is no completion signal that means "optimal."

### 2.3 Question substitution — surrogate objectives

**The algorithm.** The true objective $f^\ast$ is expensive or intractable. Replace it with a cheap surrogate $g$ correlated with it, and optimise or evaluate $g$ instead. Every practical ML system does this; so does every metric-driven organisation.

The failure is Goodhart's, and it is structured: the surrogate is accurate exactly where the correlation between $g$ and $f^\ast$ was measured, and degrades as you move away — fastest in directions that raise $g$ without raising $f^\ast$.

**Worked example.** "Will this candidate succeed in the role?" requires a causal model over many years. Substitute "how fluent and confident were they in the interview?", which is a single cheap measurement.[^kf2002] The correlation is real but modest, and the error is systematic rather than noisy: you reliably over-select for fluency and under-select for everything invisible in a 45-minute conversation. The bias points in a fixed direction, which is the fingerprint of a surrogate rather than of noise.

**LLM analogue.** Reward models are explicit surrogates for human preference, and the observed failure is the textbook one — optimising the proxy produces length, confidence, and formatting gains that the true objective does not endorse.

### 2.4 Compartmentalization — scoped consistency

**The algorithm.** Checking global consistency of a knowledge base is expensive; for first-order logic it is undecidable, and even restricted fragments are intractable at scale. So don't do it. Partition the store into fragments, enforce consistency *within* each fragment, and allow contradictions *across* them. In database terms: shard the data, run transactions per shard, and skip the distributed transaction.

The cost model is the point. Global consistency checking scales with the whole store; local checking scales with the fragment. Partitioning into $m$ fragments of size $n/m$ reduces the check from something in $n$ to something in $n/m$, and buys it by giving up the guarantee that cross-fragment queries return coherent answers.

**Worked example.** Someone can hold well-calibrated beliefs about smoking-related mortality in the fragment activated by public-health discussion, and a much rosier view of their own risk in the fragment activated by personal planning. Both fragments are internally consistent. The contradiction is only visible to a query that spans them, and such a query is rarely issued.

The right literature here is belief fragmentation — Lewis's "Logic for equivocators", Elga and Rayo on fragmentation and logical omniscience[^lewis][^elga] — rather than dissonance theory, which is about *resolving* inconsistency rather than tolerating it. Paraconsistent logics exist for exactly this reason: to keep a local contradiction from making everything derivable.

**LLM analogue.** Not the context window — that's a hard architectural cap, whereas fragmentation is selective. The real analogue is persona and role conditioning, where the same weights yield incompatible commitments depending on which fragment the prompt activates, and no cross-fragment query is ever run.

### 2.5 Amortization — memoization

**The algorithm.** Pay the inference cost once, cache the result, and convert a per-query compute cost into a one-time compute cost plus a storage cost. Standard memoization, and the bridge between this family and the last one — it turns a Family 2 cost into a Family 1 cost.

The characteristic failure is cache staleness: the cached answer was correct for the distribution it was computed under, and it keeps being returned after that distribution shifts. There is no invalidation signal.

**Worked example.** Skilled behaviour that is fast, accurate, and wrong in exactly the conditions that changed since it was learned — driving habits that transfer badly to the other side of the road, expert intuitions from a market regime that ended. Dasgupta and colleagues argue this is what fast intuitive judgement *is*: not a separate cruder system, but cached output from a slower one.[^dasgupta]

**LLM analogue.** A forward pass is an amortized posterior — all the inference was paid at training time. Knowledge cutoffs are cache staleness in its purest form.

---

## Family 3: Evidence

**Cut samples. Error is Monte Carlo error — which shrinks with more samples only if the sampler is unbiased.**

This family splits, and the split is the most useful thing in the post:

- **Unbiased proposal**: error is variance, falls as $1/\sqrt{N}$, more sampling fixes it.
- **Biased proposal**: more sampling converges you *faster onto the wrong answer*.

### 3.1 Availability — importance sampling with a bad proposal

**The algorithm.** You want $\mathbb{E}_p[f]$ but cannot sample from $p$. Sample from a proposal $q$ instead and reweight by $p/q$. If you have the weights, the estimator is unbiased. If you *don't* — if you just average the samples from $q$ — you are estimating $\mathbb{E}_q[f]$ and calling it $\mathbb{E}_p[f]$.

Availability is the unweighted version.[^tk1973] Memory retrieval is the proposal $q$: instances come back weighted by recency, vividness, and rehearsal. Frequency estimation then averages over whatever came back, with no correction term. The bias equals the mismatch between retrieval fluency and true frequency, and it does not shrink with more retrieval effort.

**Worked example.** Estimate the relative frequency of death by shark attack versus death by falling furniture. The retrieval proposal is dominated by media coverage, which weights by newsworthiness. Newsworthiness is roughly *inversely* related to frequency, so $q$ is anticorrelated with $p$ on precisely the dimension being estimated. Thinking harder draws more samples from the same skewed $q$ and sharpens a wrong estimate.

The diagnostic: this bias is immune to effort but responsive to *changing the sampler*. Giving someone actuarial tables fixes it instantly; asking them to think carefully does not.

**LLM analogue.** Training-frequency effects, and positional sampling. Liu and colleagues found models attend well to the start and end of a long context and poorly to the middle[^liu] — primacy and recency together, the same U-shape as the human serial position curve. That is a real convergence rather than a loose analogy, since nothing in the training text taught it that shape.

### 3.2 Confirmation bias — local search without restarts

**The algorithm.** Hill-climbing from a starting point, accepting improvements, without random restarts or a temperature high enough to escape basins. Cheap, converges fast, gets stuck. Simulated annealing exists precisely because the fix — random restarts, exploration — is expensive.

Hypothesis maintenance is this: evaluate incoming evidence against the current hypothesis, update within the basin, and only leave the basin under a large shock.[^nickerson] Cost per update is small. Cost of confirming you're in the *global* optimum is a full re-search.

**Worked example.** A diagnosis reached in the first two minutes of a consultation. Subsequent findings are scored as consistent-or-not with that hypothesis, which is a local evaluation, rather than being used to re-rank the full differential, which is a global one. The error signature is characteristic: not random misdiagnosis, but sticky misdiagnosis, with confidence *increasing* as more evidence is interpreted through the fixed hypothesis.

**LLM analogue.** Two sharp cases. Turpin and colleagues showed models given a biasing cue reach the cued answer and then generate chain-of-thought that never mentions the cue — post-hoc rationalisation of a conclusion reached by other means.[^turpin] Sharma and colleagues document sycophancy: models revise correct answers toward whatever the user appears to believe.[^sharma][^perez] Both are the same shape as hill-climbing from a supplied starting point.

### 3.3 Pattern completion — imputation

**The algorithm.** Missing data. Rather than propagate uncertainty, impute the missing entries from a generative model and proceed as though the imputed values were observed. Cheap, and it makes downstream computation possible; but it destroys the distinction between observed and inferred.

**Worked example.** Reconstructive memory. What is stored is a sparse set of fragments; the recalled episode is a decode from those fragments plus a schema prior.[^loftus] The imputed details are schema-consistent by construction, which is why misremembering is systematic rather than random — the errors point toward the prior, not in arbitrary directions. And because imputed values carry no observed/inferred flag, subjective confidence in a false detail is indistinguishable from confidence in a real one.

**LLM analogue.** This is the same mechanism as §1.3, viewed from the evidence side rather than the storage side: gaps are filled from the prior with no flag marking them as filled.

### 3.4 One sample — Thompson sampling

**The algorithm.** To act on a posterior you can take the argmax (needs the full posterior) or draw one sample and act greedily on it (needs one draw). The second is Thompson sampling, and it has provable near-optimal regret bounds on bandit problems.

The behavioural signature of one-sample decision-making is *probability matching*: choose option $i$ with probability $p_i$ rather than always choosing the highest-$p$ option. This has been filed as an irrationality for decades. It is what Thompson sampling looks like from the outside.

**Worked example.** Vul and colleagues asked when $N=1$ is optimal and found the answer is: surprisingly often.[^vul] When each sample costs time and decisions arrive continuously, the throughput gain from deciding on one sample exceeds the accuracy gain from more. Probability matching is the correct policy under a per-sample time cost, not a failure to maximise.

Note that this is the one place in the post where the "bias" has a *provable* optimality guarantee rather than a plausibility argument — and it is also the one that best survives a demand for rigour.

**LLM analogue.** Temperature sampling is literally this, and run-to-run variance is its signature.

### 3.5 Deference — delegation

**The algorithm.** Verifying a solution is often much cheaper than finding one; that asymmetry is the content of NP. When it holds, delegating derivation and only verifying the result is strictly better than deriving.

Trusting an expert is this policy. It is not an absence of reasoning; it is a call to an oracle plus a cheap check on the oracle's credentials. It is rational exactly when verification is in a lower complexity class than derivation, and it fails exactly when it isn't — when you cannot verify the answer or even the credentials, the check degenerates into a surface heuristic and you get appeal-to-authority in its bad form.

**Worked example.** Accepting a structural engineer's load calculation. You cannot redo it, but you *can* verify the certification, which is cheap. The delegation is sound. Now accept a confident claim about nutrition from someone with a doctorate in an unrelated field: same surface features, but the credential no longer verifies anything about the claim. The algorithm is unchanged; the verification step has silently become vacuous. That is the whole difference between sensible deference and the fallacy, and it lives in whether the check has content.

**LLM analogue.** Retrieval and tool use — offloading computation to a calculator or search index rather than deriving it in-weights.[^toolformer] The failure mode matches: models will accept and propagate a retrieved result without any check that the source supports it.

Notice that "logical fallacies" dissolved across this taxonomy rather than forming a family. Appeal to authority is delegation with a vacuous check (3.5); *post hoc ergo propter hoc* is a low-rank causal schema (1.3); circumstantial ad hominem is proposal reweighting by source reliability (3.1). They were never a natural kind — just surface forms produced by three different trades.

---

## Summary

| Family | Strategy | Algorithm | Characteristic error |
|---|---|---|---|
| Representation | Chunking | path contraction / macro-operators | interior of the path is unrecoverable |
| Representation | Prototypes | vector quantization | typicality gradient; unstable at boundaries |
| Representation | Schemas | low-rank factorization | confident plausible errors off-manifold |
| Representation | Forgetting | cache eviction | loss tracks environmental need-odds |
| Inference | Anchoring | truncated iteration | displacement toward start, decaying as $\rho^k$ |
| Inference | Satisficing | early-stopped search | above-average non-optimal choice, no regret |
| Inference | Substitution | surrogate objective | Goodhart drift in a fixed direction |
| Inference | Compartmentalization | sharded consistency | contradictions only across fragments |
| Inference | Amortization | memoization | stale cache, no invalidation signal |
| Evidence | Availability | unweighted importance sampling | bias tracks proposal, not sample count |
| Evidence | Confirmation | hill-climbing, no restarts | sticky hypothesis, rising confidence |
| Evidence | Pattern completion | imputation | schema-directed errors, no observed/inferred flag |
| Evidence | One sample | Thompson sampling | probability matching; run-to-run variance |
| Evidence | Deference | delegation to an oracle | fails when verification becomes vacuous |

## The prediction

The three families have different error characters, so they respond differently to a larger query-time budget:

| Family | More thinking time should | Because |
|---|---|---|
| Inference | substantially reduce the bias | error is $\rho^k$ and $k$ is what you are buying |
| Evidence, unbiased sampler | partly reduce it, as $1/\sqrt{N}$ | more samples, same proposal |
| Evidence, biased sampler | not reduce it, possibly sharpen it | faster convergence onto a skewed estimate |
| Representation | do nothing | the distinction was never encoded |

Concretely: run a bias battery against a reasoning model at low and high thinking budgets. Anchoring effects should melt. Satisficing and substitution errors should shrink. Availability effects should stay flat or worsen. Typicality and prototype effects should not move at all, at any budget, because the information needed to move them is not in the representation.

The inverse test: compression should amplify Family 1 specifically. Quantized and distilled models are the same system at lower rate $R$, so they should show more typicality collapse and more schema-driven confabulation, graded by bits — while their anchoring behaviour, being an inference-time property, stays put.

Both are cheap to run. If the biases don't sort this way, the taxonomy is wrong.

## Convergence or contagion?

When an LLM produces an appeal to authority, is that the model finding a strategy under resource pressure, or reproducing a strategy that humans found under resource pressure and then wrote down a billion times?

The distinction is the one biology already has: **analogy versus homology.** Convergent evolution means independently arriving at the same solution under the same pressure. Inheritance means having the trait because your ancestors had it. Wings evolved separately in bats and birds; the same bones appear in both because of a shared ancestor. Both are real, they support different conclusions.

Note that it does not matter *who* imposed the approximation. Engineering iteration on architectures is a selection process — slower than gradient descent, mediated by benchmarks and cost curves rather than by loss, but selection. An approximation that survives because it made a model cheap enough to ship has been selected for exactly the pressure this post is about.

What matters is whether the trait was selected or inherited, and the two are distinguishable:

- **Inherited** traits should track training-corpus frequency and be removable by data filtering.
- **Selected** traits should track the *budget*, survive data filtering, and reappear under budget pressure regardless of data.

An LLM's appeal-to-authority is probably homologous — inherited from text as content. Its U-shaped positional attention is probably analogous — nothing in the corpus taught it that.

The clean experiment: models trained on non-human data. Game engines, weather models, protein models. If systems that never read a word of human text still show typicality gradients, skewed retrieval, and truncation-shaped anchoring, the convergence is real and driven by the task. If they don't, a good deal of what looks like convergent evolution here is contagion.

## Limitations

Three, briefly.

**This is not an optimality argument.** Showing a method is cheap is not showing it is the best method at that price. Doing that properly requires committing to a cost model and a query distribution in advance, and if you get to pick those afterwards you can rationalise anything — the standing objection to this whole genre.[^bowers] I have tried to stay on the weaker claim throughout, but the temptation is real and worth naming.

**The cost models here are chosen, not measured.** I assert that global consistency checking is expensive and that retrieval is fluency-weighted. Both are plausible and neither is measured in the units that would make the argument quantitative.

**Assigning a bias to a family is a hypothesis, not an observation.** The whole point of the prediction section is that the assignments are testable, which also means they are refutable, and I would expect some of the fourteen to move.

[^zipf]: Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort*. Addison-Wesley.
[^feldman]: Feldman, V. (2020). Does learning require memorization? A short tale about a long tail. *STOC 2020*.
[^sims]: Sims, C. R. (2016). Rate–distortion theory and human perception. *Cognition, 152*, 181–198.
[^zaslavsky]: Zaslavsky, N., Kemp, C., Regier, T., & Tishby, N. (2018). Efficient compression in color naming and its evolution. *PNAS, 115*(31), 7937–7942.
[^korf]: Korf, R. E. (1985). Macro-operators: A weak method for learning. *Artificial Intelligence, 26*(1), 35–77.
[^chase]: Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*(1), 55–81.
[^miller]: Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review, 63*(2), 81–97.
[^cowan]: Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences, 24*(1), 87–114.
[^rosch]: Rosch, E. (1975). Cognitive representations of semantic categories. *Journal of Experimental Psychology: General, 104*(3), 192–233.
[^schank]: Schank, R. C., & Abelson, R. P. (1977). *Scripts, Plans, Goals, and Understanding*. Lawrence Erlbaum.
[^bartlett]: Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.
[^anderson1991]: Anderson, J. R., & Schooler, L. J. (1991). Reflections of the environment in memory. *Psychological Science, 2*(6), 396–408.
[^lieder2018]: Lieder, F., Griffiths, T. L., Huys, Q. J. M., & Goodman, N. D. (2018). The anchoring bias reflects rational use of cognitive resources. *Psychonomic Bulletin & Review, 25*(1), 322–349.
[^simon]: Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review, 63*(2), 129–138.
[^kf2002]: Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In *Heuristics and Biases* (pp. 49–81). Cambridge University Press.
[^lewis]: Lewis, D. (1982). Logic for equivocators. *Noûs, 16*(3), 431–441.
[^elga]: Elga, A., & Rayo, A. (2022). Fragmentation and logical omniscience. *Noûs, 56*(3), 716–741.
[^dasgupta]: Dasgupta, I., Schulz, E., Tenenbaum, J. B., & Gershman, S. J. (2020). A theory of learning to infer. *Psychological Review, 127*(3), 412–441.
[^tk1973]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology, 5*(2), 207–232.
[^liu]: Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the middle: How language models use long contexts. *TACL*.
[^nickerson]: Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology, 2*(2), 175–220.
[^turpin]: Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. *NeurIPS 2023*.
[^sharma]: Sharma, M., et al. (2023). Towards understanding sycophancy in language models. arXiv:2310.13548.
[^perez]: Perez, E., et al. (2022). Discovering language model behaviors with model-written evaluations. arXiv:2212.09251.
[^loftus]: Loftus, E. F. (2005). Planting misinformation in the human mind: A 30-year investigation of the malleability of memory. *Learning & Memory, 12*(4), 361–366.
[^vul]: Vul, E., Goodman, N., Griffiths, T. L., & Tenenbaum, J. B. (2014). One and done? Optimal decisions from very few samples. *Cognitive Science, 38*(4), 599–637.
[^toolformer]: Schick, T., et al. (2023). Toolformer: Language models can teach themselves to use tools. *NeurIPS 2023*.
[^bowers]: Bowers, J. S., & Davis, C. J. (2012). Bayesian just-so stories in psychology and neuroscience. *Psychological Bulletin, 138*(3), 389–414.
