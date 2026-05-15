---
title: Governance mechanisms — a procedural framework
subtitle: Why design the procedure that picks the goal, not the goal itself
layout: post
categories:
    - economic
permalink: /governance-mechanisms/
---

The **collective decision-making problem** is: how does a group of people decide what to do together, given that they have different preferences, beliefs, and stakes? Examples are everywhere — a nation choosing a tax rate, a corporation choosing whether to invest, a research community choosing which papers to publish, an AI model choosing which response to generate when its raters disagree.

**Governance** is the set of rules, institutions, and procedures by which a collective makes those decisions. Governance is to collective decision-making what an algorithm is to computation: the procedure that turns inputs (preferences, beliefs, information) into outputs (decisions, actions, policies).

The problem has two halves: **choosing the goal**, and **achieving the goal**. In the AI alignment literature these are called *goal specification* and *goal pursuit*; the rest of the series uses both pairs of terms interchangeably. Most failure modes of capitalism, democracy, corporate governance, and AI alignment can be located in one half or the other.

This post lays out the framework the rest of the series uses to ask those questions. It is the philosophical scaffolding; the empirical motivation is in the [why-care](/governance-mechanisms/why-care/) sibling post. Subsequent posts apply the framework: *agency* ([Post 1](/governance-mechanisms/agency/)) as one candidate **social utility function** (SUF) among many, *mechanism design* ([Post 2](/governance-mechanisms/mechanism-design/)) as the next-stage question of which procedure picks goals for the collective, and *pursuit* ([Post 3](/governance-mechanisms/alignment/)) as the machinery of achieving once those goals are specified.

The framework rests on five moves:

1. Substantive goal-specification fails.
2. No proxy is accurate enough — we have to read preferences from the population, through imperfect elicitation.
3. Therefore: design a procedure, not a goal.
4. The decision is *nested*: pick a **social utility function (SUF)**, then pick a **mechanism** whose job is to pick goals for the collective. Good SUFs are *minimal* — because preferences are unknown and dynamic, the SUF must produce mechanisms that perform well across many plausible preference distributions, not just one. Minimality *is* robustness.
5. The connection between SUF and mechanism is the work, not the answer. Be explicit at each stage about what's being optimised and what tradeoffs are accepted.

That's the whole post. The rest is unpacking.

## 1. Substantive goal-specification fails

Pick any "what society should maximise" answer that has been seriously proposed: salvation of souls (medieval Christianity), the workers' paradise (Marxism), aggregate hedonic utility (classical utilitarianism), coherent extrapolated volition (Yudkowsky). Each is a *substantive* claim about the good — an attempt to write down the right outcome and engineer toward it.

Three failure patterns recur.

**Diversity.** Humans want different things. Substantive specifications either pick one tribe's preferences and impose them (the Church, the Party), or claim convergence-under-reflection that empirically never happens (CEV).

**Drift.** Preferences shift over time, in response to events, technology, and the system's own behaviour. A specification correct in 1789 endorses slavery; one correct in 1950 endorses housewife-only employment for women. The specification doesn't update; the world does.

**Capture.** Whoever gets to write the substantive specification gets to write their preferences into it. Shareholder primacy is what this looks like in corporate governance. CEV would be what this looks like at the lab that builds the first sufficiently capable optimiser.

None of these are arguments that *no* substantive ethics is correct. They are arguments that *betting the future on getting the substantive ethics right* is an unwarranted gamble — and that the bet has been losing.

## 2. No proxy will do

If we're not specifying outcomes, we have to estimate what the public wants — and every alternative we've tried is a proxy for it. Priests, parties, philosophers, markets, and trained models all claim to speak for the many. Each is a measurement of an underlying thing, and each has an accuracy. The empirical record is that no proxy has been accurate enough: each smuggles its own substitution into the signal it claims to represent.

This reframes the problem statistically rather than philosophically. The target is some aggregation of the population's true preferences. The question is which mechanism best *estimates* it. A small expert group has low variance but its biases are correlated and unaccountable. A captured proxy — the Party, the Church, a shareholder vote — has low variance and an explicit substitution. Asking the population directly has high per-individual variance but, under decorrelated errors and robust aggregation, low aggregate bias. The framework starts here: ask the source, knowing the source is itself a noisy channel.

What the public wants is what we'll call *preferences* — and the word is doing more than it looks. A preference is intangible: private, often unstable, sometimes unknown even to its owner. We never see preferences directly. We see only what people *report* through some elicitation mechanism — a vote, a price they pay, a survey answer, a ranking under RLHF. Every such mechanism gives a biased, incomplete, possibly distorted view of the thing it is trying to read out.

Ask someone at a dinner table what they want and they'll defer to whoever asked. Tell them what their neighbour bought and they'll buy it too. Ask them to rate two AI responses and they'll prefer whichever is longer and more confident. Survey them on a socially unpopular view and they'll under-report. The signal we read is always shaped by the channel we read it through — and never identical to whatever is on the other side.

This splits the design problem into two layers:

- **Elicitation.** Build mechanisms that surface preferences honestly and faithfully. Strategic voting, market manipulation, advertising-induced wants, and model sycophancy are all elicitation failures — distortions between the preference and its report.
- **Aggregation.** Combine the elicited reports into a collective decision. Arrow, Gibbard-Satterthwaite, and the rest live here.

The caveat: even asking the source isn't sufficient — the source can be corrupted upstream of any elicitation mechanism. Sen's adaptive-preferences critique bites here. People formed under oppression may endorse the oppression; people raised under saturating advertising may prefer what they're sold to want. A complete framework needs *preference-formation* conditions — free press, education, exposure to alternatives, protection of dissent — alongside elicitation and aggregation. Three layers, not two. This series mostly works on aggregation. Flag, defer.

## 3. The procedural turn

The move shared by Rawls, mechanism design, social choice theory, and modern preference-elicitation work is the same: rather than specify the right outcome, specify the *rules of the game*. Observe what stable behaviour emerges from rational agents playing under those rules. Evaluate the stable behaviour against your desiderata. Iterate the rules.

Rawls is the canonical version. Design society from a position where you don't know which member of it you'll be. The argument is that *whatever* substantive notion of the good you hold privately, you'll agree to certain procedural protections against the version of society where you turn out to be the worst-off member.

Mechanism design generalises this. Capitalism and democracy are two real-world attempts: prices and votes as aggregation procedures. Both visibly failing — but the *kind* of move addresses the right problem; the specific mechanisms have known flaws. Diagnosing those flaws is the work of Post 2.

## 4. SUF → mechanism

Two facts about preferences set the framing.

1. **Preferences are unknown.** We don't fully observe what individuals want; §2 made the case that the only credible source is the population itself, read through imperfect elicitation.
2. **Preferences are dynamic.** They shift over time — generations turn over, technology changes what's wanted, social structures reshape what's valued.

Together: at design time, we don't have a fixed preference distribution to optimise against. What we have, at best, is a *distribution over plausible preference distributions* $\mathcal{H}$ — a hyperprior capturing what we believe about what people might want, across current and counterfactual worlds. $\mathcal{H}$ is, in effect, a model of **human nature**: it encodes the patterns we believe are invariant across plausible $\Pi$, even when we can't pin down any specific one. A hyperprior that puts mass on "humans value autonomy" or "humans are tribal" or "humans seek status" is not anthropologically neutral — it's an empirical claim about people, and it's where psychology, anthropology, and evolutionary biology earn their keep. Specifying $\mathcal{H}$ honestly is itself a research problem; choosing it badly (e.g., assuming away tribalism) silently propagates into whichever SUF the framework recommends.

This makes the design problem one of **robustness**. A good **social utility function (SUF)** — the function the framework optimises — should produce mechanisms that perform well across the plausible space $\mathcal{H}$, not mechanisms over-fit to a particular $\Pi$.

**Minimality emerges from robustness.** A prescriptive SUF (e.g. "maximise hedonic utility") fixes one view of what's worth pursuing. If preferences shift, or were never well-described by hedonic utility in the first place, the induced mechanism becomes badly miscalibrated. A minimal SUF (e.g. "preserve agency") prescribes less, and its induced mechanism remains responsive to whatever $\Pi$ obtains. Minimality *is* robustness under preference uncertainty.

The nested decision problem.

**Stage 1.** The designer has access to $\mathcal{H}$ — a distribution over preference distributions $\Pi$. This is what's empirically tractable: a hyperprior about what humans might want, including future and counterfactual possibilities.

**Stage 2.** Pick the SUF given $\mathcal{H}$. Minimal-but-functional. Candidates: agency, aggregate happiness, suffering minimisation, capabilities, and others.

**Stage 3.** Pick the mechanism given the SUF. The mechanism's job is to pick goals for the collective; it takes preferences (or capabilities, or deliberative outputs — depending on its class) as inputs and emits collective goals as outputs:

$$m^*(\text{SUF}) \;=\; \arg\max_{m} \; \mathbb{E}_{\Pi \sim \mathcal{H}}\, \mathbb{E}_{\theta \sim \Pi}\!\left[\, \text{SUF}(m(\theta),\, \theta) \,\right]$$

**Stage 4.** The mechanism operates on realised preferences $\theta$ (drawn from whichever $\Pi$ actually obtains, itself drawn from $\mathcal{H}$). It emits collective goals. Those goals are pursued ([Post 3](/governance-mechanisms/alignment/) covers pursuit). Outcomes follow.

**Stage 5.** Regret is observed against actual preferences: how well do the realised collective goals serve what people actually wanted? Regret is measured against $\theta$, not against the SUF — the SUF is a *design proxy* the mechanism designer uses to choose between mechanisms; what ultimately matters is preference-satisfaction.

The SUF design problem:

$$\text{SUF}^* \;=\; \arg\min_{\text{SUF}} \; \mathbb{E}_{\Pi \sim \mathcal{H}}\, \mathbb{E}_{\theta \sim \Pi}\!\left[\, \text{regret}\bigl(\theta,\, m^*(\text{SUF})(\theta)\bigr) \,\right]$$

Minimal SUFs win here because they generalise across $\mathcal{H}$. A SUF that prescribes a lot performs brilliantly under one $\Pi$ and disastrously under another; averaged across $\mathcal{H}$, it loses to a SUF that performs adequately everywhere. This is the formal reason agency and Rawls' maximin do well: both preserve the collective's capacity to handle whatever $\Pi$ obtains, rather than locking in one view of value.

[Post 1](/governance-mechanisms/agency/) takes up Stage 2: the design space of SUFs, and analyses agency, happiness, suffering, and capabilities by the minimality-under-robustness criterion. [Post 2](/governance-mechanisms/mechanism-design/) takes up Stage 3 in both directions: top-down (given a SUF, what mechanisms serve it?) and bottom-up (read off the implicit SUF that capitalism, parliamentary democracy, or current AI training actually serves).

**One clarification.** §2 above sketches what *preference-aggregation*-style mechanisms commit to: read preferences from the population, aggregate them, emit collective goals. Other mechanism classes exist — sortition + structured deliberation generates goals via discussion rather than aggregation; futarchy decomposes decisions into values (voted) and beliefs (markets); pure expert councils skip broad input entirely. The framework does not pre-commit to any class. Impossibility results that constrain the Stage 3 search (Arrow, Gibbard-Satterthwaite, and the rest) are developed in Post 2 in their natural home.

## 5. What this framework is not

**Not a refutation of substantive ethics.** If you think the Church or classical utilitarianism or virtue ethics can specify the good directly and durably, this research program is moot for you — and the historical record will have to argue with you, not me. The framework is one response among others to the empirical observation that substantive specifications keep failing in characteristic ways.

**Not a defence of any specific existing mechanism.** Contemporary parliamentary democracy, market capitalism, RLHF, constitutional AI — these are all instances of preference-aggregation procedures, and the framework is largely critical of each. The point is to characterise the design space, not to canonise any current implementation.

**Not a claim that preferences are sacred.** Adaptive preferences are real. The framework needs preference-formation conditions alongside preference-aggregation rules. This series mostly handles aggregation; preference formation deserves its own treatment.

**Not a complete theory.** This is a research agenda. The pieces of the theory are scattered across social choice, mechanism design, public choice, information theory, the capabilities approach, and the empirical literature on institutional design. Bringing them together is the work.

## 6. Roadmap

- **Upstream entry point — [why care](/governance-mechanisms/why-care/):** the historical and empirical motivation. Acemoglu and Robinson, inclusive vs extractive institutions, the cost in human welfare of getting collective decision-making wrong.
- **[Post 1 — agency](/governance-mechanisms/agency/):** explores Stage 2 — the design space of **SUFs**. Translates "maximise happiness," "minimise suffering," and "equality of opportunity" into mathematics, and argues for *agency* — the capacity to achieve one's goals — as a strong candidate under the minimality-under-robustness criterion. Does *not* claim agency forces any specific mechanism. The companion [Post 1b](/governance-mechanisms/agency-derivation/) walks the derivation of agency's formal expression.
- **[Post 2 — mechanism design](/governance-mechanisms/mechanism-design/):** explores Stage 3 — the design space of **mechanisms**. Bottom-up: reads off the implicit SUF that capitalism, parliamentary democracy, and current AI training actually serve (often: a small shareholder/donor group's preferences). Top-down: sketches structural features — broad input, periodic re-specification, contestability — that a mechanism would need to serve a non-captured SUF. The design heuristics (pluralism, non-domination, transparency, updatability, robustness, computability) are developed here in their natural home, alongside the impossibility results (Arrow, Gibbard-Satterthwaite, and the rest).
- **[Post 3 — pursuit](/governance-mechanisms/alignment/):** given a specified collective goal, how do we build an optimiser that pursues it without drift? The same problem in AI, corporations, and politics — and recognisably the same techniques (transparency, audit, watchdogs, iterative feedback) in each.

The series is the agenda. None of it is finished. Each post is a sketch of a research program. Pushback, counter-examples, and missing predecessors welcome.
