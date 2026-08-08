---
title: From objective to mechanism
subtitle: The social utility function as a surrogate loss
layout: post
categories:
    - economic
permalink: /governance-mechanisms/suf-to-mechanism/
---

Suppose you have decided not to specify what a society should aim at, and to design the *procedure* that picks its goals instead. Two questions follow immediately, and they are usually run together:

- What target do you evaluate candidate procedures against?
- Which procedure wins, given that target?

Call the first object a **social utility function** (SUF) — a function that scores institutions — and the second a **mechanism** — a rule set that takes preferences as input and emits collective goals. The design problem is nested: pick a SUF, then pick a mechanism the SUF rates highly.

This post is about the link between the two stages, which usually gets asserted rather than argued. Three questions:

1. **Why a SUF at all?** If what we care about is how badly the institution serves people's actual preferences, the SUF is a detour. Why take it?
2. **Which impossibility theorems bite, and where?** Arrow and Gibbard–Satterthwaite get cited loosely in this area. They constrain one stage and not the other, and the distinction does real work.
3. **How much should a design fix in advance?** There is a clean mathematical answer to this, and reading it back into institutions turns out to reproduce the constitution/legislation split.
4. **What happens when you optimise a SUF hard?**

The short version: **the SUF is a surrogate loss.** Everything useful follows from taking that seriously, including the bad news.

## 1. Why a proxy at all?

Write the thing we actually care about as **regret**: how badly the collective goals a mechanism produces serve the preferences people turn out to have. There is then an obvious objection to the nesting. If regret is the true objective, why not skip a level and pick $m^* = \arg\min_m \mathbb{E}[\text{regret}]$ directly? The SUF appears on both sides and cancels.

The answer is that **regret is not available at design time.** It is defined against preferences realised after the institution has run for years or decades. You cannot evaluate it, simulate it, or argue about it in a committee. The SUF is what you *can* evaluate — a function of observable structure rather than of unobserved future preferences.

That is the structure of a **surrogate loss**: you want 0-1 classification error, cannot optimise it, so you optimise logistic loss and hope the argmin transfers. Three things follow, and they are the reason the reframing is worth anything:

- **Consistency.** A surrogate is *calibrated* if driving it to its optimum drives the true risk to its optimum too (Bartlett, Jordan and McAuliffe, 2006). The corresponding question — *does maximising this SUF actually minimise regret?* — is what decides whether choosing a SUF was worth the effort, and it is almost never asked of a political objective.
- **The surrogate gap.** Even a calibrated surrogate has a finite gap at finite optimisation pressure. Bounding it is the useful form of "how wrong can this go."
- **Goodhart.** Divergence between surrogate and target under optimisation pressure (§5).

There is also a consequence for how the objective should be argued about. Surrogates are not true or false; they are calibrated or not, and calibration is a property of the *pair* (surrogate, target) together with the space of things you optimise over. So no candidate SUF — agency, welfare, capabilities, maximin — is the correct theory of the good, and defending one as though it were is a category error. The available claim is narrower: *among functions we can evaluate at design time, this one's argmax over the feasible mechanism space is closest to regret's argmin.* That is empirical, and checkable on small systems.

## 2. Two stages, and which theorems bite where

There is a distinction here that is easy to slide over and that turns out to matter.

**Stage 1 — the mechanism.** $m: \theta \mapsto$ collective goal. A social choice rule in the classical sense: it maps a profile of individual preferences to an outcome.

**Stage 2 — the SUF.** $S$ ranks *mechanisms*, not outcomes. $S(m)$ is a number attached to a rule.

The impossibility theorems everyone reaches for live at **Stage 1**:

- **Arrow (1951).** No social choice rule over three or more alternatives satisfies unrestricted domain, Pareto, independence of irrelevant alternatives and non-dictatorship — for *ordinal* preferences.
- **Gibbard–Satterthwaite (1973/75).** Any non-dictatorial, onto, deterministic rule over three or more alternatives is manipulable.
- **Myerson–Satterthwaite (1983).** No mechanism achieves efficient bilateral trade with voluntary participation, incentive compatibility and budget balance.
- **Sen (1970), the impossibility of a Paretian liberal.** No rule satisfies unrestricted domain, Pareto, and even minimal liberalism — giving each of two people decisive power over one private pair. This one is aimed squarely at objectives built around individual freedom, and anyone proposing such an objective owes it an answer.

None of these says anything about Stage 2. A SUF is not a social choice rule; nothing stops you having a complete, transitive, non-dictatorial ranking over mechanisms. **The impossibility results do not constrain the SUF. They carve out the feasible set the SUF ranks over:**

$$m^*(S) = \arg\max_{m \,\in\, \mathcal{M}_{\text{feasible}}} S(m)$$

They are not obstacles to the programme. They are its constraint-set specification, and unusually precise ones.

**The bridge result: Maskin monotonicity.** One theorem genuinely spans both stages, and it is the right tool here. Maskin (1977, published 1999): if a social choice rule is implementable in Nash equilibrium, it is **monotonic** — if outcome $a$ is selected at profile $\theta$, and at $\theta'$ nobody has moved $a$ down relative to any alternative, then $a$ must still be selected at $\theta'$. With three or more players and no-veto-power, monotonicity is sufficient as well.

This gives a concrete, checkable test on any proposed SUF: **is the rule it endorses Maskin monotonic?** If not, no mechanism Nash-implements it and the SUF has specified an unreachable target. It is the kind of question settled by a proof or a counterexample rather than by argument, which makes it the most tractable open problem in this area.

**A warning about content-free objectives specifically.** A SUF designed to be neutral about which goals people hold is typically written as an expectation over a *prior* about what people might want, rather than as a function of the preferences actually reported. Such a SUF does not depend on the realised profile $\theta$ at all. At Stage 2 that is the entire point — it is what content-freeness *means*. But it has an awkward consequence at Stage 1: the rule such a SUF endorses is constant in $\theta$, hence trivially monotonic and trivially implementable, which should provoke suspicion rather than relief. A mechanism has to be responsive to what people actually want, and that responsiveness cannot come from an objective that is by construction blind to it. Something else has to supply it — most plausibly, letting the prior be updated by observed preferences, which reintroduces the feedback loop of §6.

## 3. How much should be fixed in advance

An institution fixes some things and defers others. A constitution settles a small number of questions permanently and hands the rest to a legislature; articles of incorporation fix less than employment contracts, which fix less than day-to-day management. How much should be fixed, and which parts?

There is an exact answer under assumptions clean enough to state. Model the situation as a two-stage bandit. A society faces $K$ possible arrangements. Before it can try any of them it must commit to a permitted subset — that is the constitution — and only then does it begin choosing among the survivors, learning as it goes which are good. It has a prior over how good each arrangement is: a mean $m_i$ and an uncertainty $\sigma_i$ reflecting genuine disagreement and genuine ignorance about what people will turn out to want.

The trade is between two costs. Keeping an option available means paying to explore it — deliberation, experimentation, the risk of trying something bad. Removing an option risks deleting the best arrangement before anyone discovers it was the best. The [companion post](/governance-mechanisms/minimality/) derives the resolution. Four readings.

**Constitutions consist of prohibitions, not prescriptions — and now we know why.** The criterion for pruning an option is that its *expected improvement* over the retained set falls below the marginal cost of exploring it, and expected improvement vanishes only when the mean is low **and** the uncertainty is small. So you may foreclose an arrangement only when you are confident it is bad. You may never enshrine one on the grounds that you are confident it is good, because that is a different and stronger claim than the model licenses.

Look at what constitutions actually contain and this is what you find: prohibitions on murder, torture, arbitrary detention, retroactive punishment, seizure without process. Lists of what may not be done. The prescriptive content is thin by comparison and mostly procedural — how to decide, not what to decide. Confidence about badness is cheaper to come by than confidence about goodness, and the model says only the first kind licenses a permanent commitment.

**Uncertainty about an option makes it unremovable, however bad it looks.** The derivative of expected improvement with respect to uncertainty is $\varphi(\delta) > 0$ everywhere — strictly positive regardless of whether the option is expected to be good or bad. An arrangement widely believed to be terrible but never tried is one a society cannot afford to foreclose; an arrangement believed to be mediocre and thoroughly understood is one it can. This cuts directly against the intuition that we should ban what we most dislike. What licenses a ban is not the strength of the disapproval but the *narrowness of the uncertainty*, and those come apart most sharply exactly where feelings run hardest.

**The longer a rule will bind, the less it should foreclose.** The keep-threshold falls with the horizon $T$: exploration costs amortise over the life of the institution, while an arrangement wrongly excluded costs proportionally to that life, forever. A rule written for a decade should prune more aggressively than the same rule written for a century. Constitutional entrenchment — commitment with an unusually long horizon — should therefore be unusually sparse, and the practice of making entrenched provisions short and general rather than detailed is what the model recommends.

**And minimality is not a virtue to be maximised.** The optimal permitted set is a strict subset whenever any option is confidently bad and the horizon is finite. A design that forecloses nothing is making the same kind of error as one that forecloses everything. This is worth stating plainly because the argument from uncertainty is usually deployed as a counsel of restraint, and it does not license unlimited restraint — it locates a line.

Two caveats on transferring the result. The model prices exploration as the cost of learning which arrangement is good, which for a society means the cost of *actually living under* an arrangement long enough to find out — a much larger and less reversible cost than the bandit framing suggests, pushing toward more pruning than the arithmetic implies. And the prior is assumed exogenous, when in fact the permitted set shapes what the next generation believes and wants about the options that were removed. That second gap is the fixed-point problem of §6, and it means a prohibition that suppresses disagreement about its own subject becomes self-justifying.

## 4. Does the SUF even change the answer?

A deflationary possibility worth taking seriously. The map $S \mapsto m^*(S)$ need not be injective. If the feasible mechanism space is small and coarse — and §2's impossibility results make it small — then many different SUFs induce the same mechanism.

If so, much of the ethical argument is idle. You do not need to settle whether the right target is agency or welfare or capabilities if all three pick the same institution. It is also the cheap way to find out whether the SUF argument matters at all.

This suggests a research move cheaper than settling ethics and more informative: **compute the invariance classes.** Take a small mechanism space and a set of candidate SUFs, and map which SUFs induce which mechanisms. The useful output is not a winner but a partition — and any SUF disagreement falling inside a single cell can be set aside permanently.

## 5. Goodhart

A surrogate optimised hard diverges from what it proxies. Manheim and Garrabrant (2018) give four mechanisms; all four have institutional instances.

**Regressional.** Selecting mechanisms by *estimated* SUF selects partly for estimation error. The mechanism that scores best is disproportionately the one we mismeasured most favourably. With a noisy simulation-based estimate over a large mechanism space, this is the default outcome, not an edge case.

**Extremal.** Optimisation pushes into regimes where surrogate and target decouple. A concrete and important instance: any SUF measured *relative to a baseline*. Objectives of the form

$$S(m) = \prod_i \frac{P_i(m)}{P_i^0}$$

— where $P_i(m)$ is how well the institution serves person $i$ and $P_i^0$ is a no-institution counterfactual — are attractive because the baseline cancels out differences in how hard people's goals are, and because they behave sensibly when the population changes size. But such an objective rises if you raise the numerator **or lower the denominator**. An institution that first degrades people's unaided capacity and then supplies the remedy scores enormously well. This is not contrived; it is a recognisable description of dependency-creating institutions, from company towns to platform lock-in. Any usable baseline-relative SUF needs $P^0$ pinned to a counterfactual the mechanism cannot influence, and it is not obvious such a counterfactual exists.

**Causal.** Intervening on something correlated with the SUF that does not cause it. Institutional reform is full of this: adopting the visible features of well-scoring systems — an elected chamber, a written constitution — without the structure that made them work.

**Adversarial.** Once the SUF is a published target, agents optimise against it. This is capture. The structural point: **a SUF is a public target, and publishing a target changes the game.** Any SUF that is robust in analysis but not robust to being known is useless.

## 6. The fixed point

The deepest problem, and the one I cannot resolve. A mechanism that aggregates preferences also *forms* them. Free press, education and market structure all condition the goals that arrive at the aggregator. So the prior the designer optimises against is not exogenous: it is a function of the mechanism.

That makes the design problem a **fixed-point problem, not an optimisation**, and the difference is not cosmetic:

- A fixed point may not exist, or may not be unique. Multiple self-consistent institution/preference pairs is a formal statement of something historians already believe — that societies lock into mutually reinforcing configurations, and that both good and bad ones are stable.
- Iterating "design against the preferences you currently observe" need not converge; where it does, it need not converge to the best available fixed point.

This structure has a recent formalism in machine learning: **performative prediction** (Perdomo, Zrnic, Mendler-Dünner and Hardt, 2020), where a deployed model changes the distribution it predicts. Their distinction transfers directly:

- A **performatively stable** point is a fixed point of repeated retraining — you design for the preferences you induce, self-consistently.
- A **performatively optimal** point minimises loss over the *joint* choice of model and induced distribution.

These differ, and repeated retraining converges (under smoothness and strong-convexity conditions) to the stable point, not the optimal one. Translated: **iterative institutional reform converges at best to a self-consistent institution — not to a good one.** Reaching the performatively optimal institution requires reasoning about the preferences a mechanism will *create*, which no existing reform process does.

There is also a nasty interaction with the argument for minimality, which runs from uncertainty being wide. But if a mechanism shapes preferences, a sufficiently powerful one can *narrow* that uncertainty — produce a population that reliably wants what it supplies. By the threshold condition, such an institution would then be justified in becoming more prescriptive. **A mechanism that homogenises its population earns, by this criterion, the right to commit harder to a substantive target.** That is a coherent description of a totalitarian equilibrium, and nothing above rules it out. The only defence I can see is to pin the prior to a counterfactual estimate the mechanism cannot influence — the same unresolved move that §5's extremal-Goodhart attack demands for the baseline. One hole, appearing twice.

## 7. Open problems

Ranked by tractability rather than importance.

1. **Is a given SUF's induced rule Maskin monotonic?** Settled by a proof or a counterexample.
2. **Compute the invariance classes** (§4) on a small mechanism space. Tells us how much of the ethical argument is idle.
3. **Is a given SUF calibrated for regret?** Build a toy society where both are computable and check whether the argmax of one tracks the argmin of the other.
4. **Pin down the baseline** against the extremal-Goodhart attack of §5.
5. **Characterise the fixed points** of the mechanism/preference loop (§6). Hardest, most important, no clear line of attack.

## 8. Closing

The SUF is a surrogate loss. That single reframing does most of the work here: it explains why the nested structure isn't redundant (§1), sorts out which theorems constrain the mechanism and which constrain the objective (§2), says how much a design should fix in advance (§3), suggests that many disagreements about the objective may be idle (§4), and supplies the right vocabulary for how the whole thing fails under pressure (§5–§6).

It also lowers the stakes of the objective-choosing argument, correctly I think. A candidate SUF is not a theory of the good. It is a design-time function whose argmax, over the mechanisms that are actually feasible, is hoped to track the argmin of a regret we can only measure in retrospect. That is a much smaller claim — and a checkable one.

---

*This post is part of a series on [governance mechanisms](/governance-mechanisms/). It takes for granted that we are designing procedures rather than specifying outcomes; the case for that move rests on a [model of human nature](/governance-mechanisms/human-nature/). The commitment result §3 interprets is derived in [minimality from uncertainty](/governance-mechanisms/minimality/), and a worked candidate SUF in [agency](/governance-mechanisms/agency/).*
