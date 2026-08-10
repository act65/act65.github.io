---
title: Designing behind the veil
subtitle: How to choose institutions when you don't know what people will want
layout: post
categories:
    - economic
permalink: /governance-mechanisms/
description: "How to choose institutions when you don't know what people will want. Every answer anyone has given to \"what should society maximise\" was written by..."
---

Every answer anyone has given to "what should society maximise" was written by someone who then turned out to be in it. Salvation of souls, the workers' paradise, aggregate happiness, the coherent extrapolated volition of humanity — each was proposed by people whose own preferences the answer conspicuously served, and each has aged badly in a characteristic way.

That is not an argument that no answer is correct. It is an argument that *betting a durable institution on having found the correct one* is a bad bet, and it has been losing for a long time. Which raises the question this series works on: if you cannot write down what a society should want, what do you build instead?

Some vocabulary first, briefly. **Governance** is the set of rules and procedures by which a collective decides what to do together — to collective decision-making what an algorithm is to computation. The problem has two halves, **choosing the goal** and **achieving the goal** (*goal specification* and *goal pursuit* in the AI alignment vocabulary), and this series works the first almost exclusively.

And here is the reframing everything downstream depends on:

> **The target is some aggregation of the range of things the population might turn out to want. The question is which procedure best serves it.**

Note what the target is not. It is not what people currently report wanting — reports are distorted, and §2 is about the distortions. Nor is it what they *truly* want right now, since institutions outlive the preferences they were built for. It is the spread of things they might want, which is an empirical object about people rather than a moral claim about the good. Most of what follows is the consequence of taking that seriously.

This post is the narrative front door and is deliberately informal. Each move below is worked out properly in a companion post, linked as it comes up. The historical case for why any of it matters is in [why care](/governance-mechanisms/why-care/).

## The argument in five moves

1. Betting on substantive goal-specification is a bad bet.
2. Every proxy for "what the public wants" has failed in a characteristic way, so preferences must be read from the population — through a channel that distorts them, in a population whose preferences the institutions themselves formed. That is three problems, not one.
3. Therefore: design a procedure, not a goal.
4. The decision is *nested*: pick a **social utility function (SUF)** — a design-time target you can actually evaluate — then pick a **mechanism** whose stable behaviour it scores.
5. Since we cannot know what people will want, the target must be something *every* set of preferences has use for — which in turn bounds how much a design may settle in advance.

## 1. Betting on substantive goal-specification is a bad bet

Pick any "what society should maximise" answer that has been seriously proposed: salvation of souls (medieval Christianity), the workers' paradise (Marxism), aggregate hedonic utility (classical utilitarianism), coherent extrapolated volition (Yudkowsky). Each is a *substantive* claim about the good — an attempt to write down the right outcome and engineer toward it.

**The claim here is decision-theoretic, not metaethical**, and the distinction matters because the argument is routinely mistaken for a stronger one it cannot support. I am not claiming that no substantive ethics is correct. I am claiming that *betting the design of a durable institution on having identified the correct one* has bad expected value, and that historically the bet has lost.

Three failure patterns recur. They are not equally strong.

**Capture.** Whoever writes the substantive specification writes their own preferences into it. Shareholder primacy is what this looks like in corporate governance; CEV would be what it looks like at whichever lab builds the first sufficiently capable optimiser. This is the load-bearing objection, and it is aimed at specification directly: the procedure that produces the specification is the attack surface.

**Drift.** Preferences shift in response to events, technology, and the system's own behaviour. A specification correct in 1789 endorses slavery; one correct in 1950 endorses housewife-only employment for women. Note what this actually argues for: *updatability*. A substantive ethics with a revision procedure survives it.

**Diversity.** Humans want different things. Substantive specifications either impose one tribe's preferences or claim a convergence-under-reflection that empirically never happens. This argues for *pluralism*, not against substance — a committed utilitarian can reply that people disagree and most of them are wrong, which is what the theory is for.

So: capture is the objection, drift and diversity constrain the *form* any substantive specification would have to take, and together they make the bet look bad enough that hedging dominates.

Underneath all three is a claim about people — about how much they vary, and how much of that variation the institutions themselves produced. That claim is the real foundation of this move and the next, and it is argued in [a model of human nature](/governance-mechanisms/human-nature/), which reads the canon from Hobbes to Fukuyama as a sequence of bets on exactly this question.

## 2. Why every proxy fails: three layers, not one

If we're not specifying outcomes, we have to estimate what the public wants — and every alternative anyone has tried is a proxy for that estimate. Priests, parties, philosophers, markets, trained models. Each is a measurement with an accuracy. A small expert group is cheap to consult, but its errors are correlated and unaccountable, so they do not average away. A captured proxy — the Party, a shareholder vote — substitutes one group's preferences for everyone's, which is bias by construction. Asking the population directly is noisy per person, but if the individual errors are roughly independent and the aggregation is robust, the noise averages down and what remains is whatever bias the channel itself introduces. That conditional is doing a great deal of work, and Layer 1 below is the reason to doubt it.

But "ask the source" hides a structure. A preference is intangible: private, often unstable, sometimes unknown to its owner. We never observe preferences — only what people *report* through some channel. Ask someone at a dinner table what they want and they'll defer to whoever asked. Tell them what their neighbour bought and they'll buy it too. Ask them to rate two AI responses and they'll prefer whichever is longer and more confident.

And the channel is not the only distortion. What people want was itself produced by the institutions they grew up inside.

**Three layers, and the framework needs all of them:**

**Layer 1 — Formation.** What produces the preferences in the first place. Free press, education, exposure to alternatives, protection of dissent; and negatively, saturating advertising, oppression, engineered dependency. Sen's adaptive-preferences critique lives here: people formed under oppression may endorse the oppression.

**Layer 2 — Elicitation.** How preferences are surfaced. Votes, prices, surveys, RLHF rankings. Strategic voting, market manipulation and model sycophancy are elicitation failures — distortions between the preference and its report.

**Layer 3 — Aggregation.** How reports combine into a decision. Arrow, Gibbard–Satterthwaite and the rest live here.

It is tempting to work only on aggregation, and it does not survive contact with the other two. The [agency](/governance-mechanisms/agency/) post turns on the claim that the goals we score must be *counterfactual* rather than reported — a formation claim. And a mechanism and the preferences it induces turn out to be a joint fixed point rather than two separable design problems — an argument made in [a model of human nature](/governance-mechanisms/human-nature/), and the reason the third layer cannot simply be deferred. The layers are coupled, and the coupling is where the hard problems are.

## 3. The procedural turn

The move shared by Rawls, mechanism design, social choice theory, and modern preference-elicitation work is the same: rather than specify the right outcome, specify the *rules of the game*. Observe what stable behaviour emerges from rational agents playing under those rules. Evaluate that behaviour against your desiderata. Iterate the rules.

Rawls is the canonical version, and his device is the one to keep in mind for the rest of this post. Behind the **veil of ignorance**, you design a society without knowing which position in it you will occupy — your class, your talents, your circumstances, and crucially your *conception of the good*. You do not know what you will want.

Two things follow, and the second is the one usually missed. First, you will insist on protections against ending up as the worst-off member, because you might be. Second, and more useful here: you will choose institutions that serve *whatever* you turn out to want, because you cannot bet on a particular answer. Rawls calls the resulting currency **primary goods** — all-purpose means, useful under every conception of the good. Rights, liberties, opportunities, income, the social bases of self-respect. He did not choose these because they are the most valuable things a life can contain. He chose them because they are the things that are useful *whichever* valuable things your life turns out to contain.

That is the shape of the whole framework. The veil is a device for deliberately widening one's uncertainty about human preferences until only robust arrangements survive.

Mechanism design generalises the move: announce the rules, let agents best-respond, and evaluate the equilibrium rather than the intention. Capitalism and democracy are two real-world attempts — prices and votes as aggregation procedures — and both are visibly strained, though diagnosing how is a separate job from this post's.

**The objection that has to be conceded here.** Hayek called this whole move *constructivist rationalism*: the error of assuming that because institutions serve human purposes, they must be susceptible to deliberate design. His claim is not that design is undesirable but that the knowledge it requires — dispersed across participants, much of it tacit — is constitutionally unavailable to any designer. The historical record is uncomfortably compatible with him. Nearly every institutional success one can point to is a narrow intervention against an identified externality with a clear causal model; there is no clean case of anyone designing an *aggregation mechanism* from a specification of what it should aggregate toward, which is what the rest of this series proposes doing. I do not think this sinks the programme, but it sets the burden, and the series does not discharge it.

## 4. The nested decision

At design time there is no fixed preference distribution to optimise against. Preferences are **unknown** and **dynamic**. What we have at best is a model of the *range* of things a population might turn out to want — which is to say, a model of human nature. Moves 1 and 2 above are really claims about that model, and it is the most load-bearing object in the framework.

Given it, the problem nests:

- **Pick a SUF** — a design-time target, a function you can evaluate when choosing between institutions.
- **Pick a mechanism** — the rule set whose stable behaviour the SUF scores, and whose job is to pick goals for the collective.
- **Measure regret** against what people actually turned out to want.

The subtlety is that the SUF and the regret are *different objects*, deliberately. Regret is what we care about but cannot evaluate at design time — it is defined against preferences realised only after the institution has run for decades. The SUF is what we can evaluate instead.

**The SUF is a surrogate loss**, in exactly the sense that logistic loss is a surrogate for classification error. The right questions about it are the ones you ask of any surrogate: is it calibrated, how large is the gap, and what happens when you optimise it hard. The impossibility results everyone reaches for here do bite, but not all in the same place. Gibbard–Satterthwaite is about mechanisms: any non-dictatorial rule can be manipulated. Arrow and Sen's liberal paradox are about the aggregation rule itself, so they constrain what a target can coherently ask for. The standard escape from Arrow is to give up purely ordinal, non-comparable inputs, which is what any objective built on cardinal and interpersonally comparable quantities does. Sen's is harder, and the [agency post](/governance-mechanisms/agency/) does not claim to have met it.

It also lowers the stakes of the objective-choosing argument, correctly I think. No candidate SUF is being offered as the true theory of the good. The claim is only that among functions we can evaluate at design time, this one picks the best institution actually available. That is a smaller claim, and a checkable one.

## 5. Aim at what every preference has use for — and settle no more than you must

Now the constraint that does the real work.

We do not know what people want, and we know that what they want will change. So the target cannot be *any particular thing people might want* — every such choice is a bet, and §1 says the bet loses. **The only targets available are the ones we believe are useful across the whole range of things people might want.**

This is not a compromise or a hedge in the pejorative sense. It is the only kind of answer the epistemic situation permits. Rawls' primary goods are one instance. Money is another, more mundane one: it is not what anybody ultimately wants, which is exactly why it is useful to everybody. The pattern generalises — under uncertainty about ends, you accumulate means.

But "aim at means, not ends" is a slogan until you can say *how much* to leave open. That question has a real answer, and it is worth stating because it turns out to explain something about constitutions that is otherwise just a curiosity.

Think of a society as facing a set of possible arrangements it might adopt. It cannot try them all, and before it tries any it must fix which ones remain permissible — that is what a constitution does. Leaving an arrangement available is costly, because a society that keeps its options open has to spend real time and real damage discovering which are bad. Removing one is also costly, because you might be deleting the best arrangement before anyone found out it was the best.

The resolution, [derived here](/minimality-from-uncertainty), is a threshold with an unexpected shape: **you may foreclose an option only when you are confident it is bad.** Uncertainty about an option strictly increases the cost of removing it, whatever you expect that option to be worth. So an arrangement widely disliked but never tried is one a society should hesitate to ban: it is not the strength of the disapproval that licenses a ban, but the narrowness of the uncertainty, and those come apart most sharply where feelings run hardest.

That is why constitutions are lists of **prohibitions** rather than prescriptions, and the asymmetry is derivable rather than accidental. Forbidding one arrangement requires confidence that *it* is bad. Mandating one requires foreclosing every alternative to it — confidence that *all of them* are bad, a far stronger claim and much harder to come by. Hence murder, torture, arbitrary detention, retroactive punishment, seizure without process, and very few entries of the form "society shall pursue X."

Two consequences worth carrying. **The longer a rule will bind, the less it should foreclose** — the cost of exploring an option is paid once and amortises over the life of an institution, while a wrongly excluded option costs proportionally to that life, forever. (That holds if the cost of keeping an option open is one-off; if it recurs every period, the horizon washes out.) And **restraint is not a virtue to be maximised**: the optimal amount of foreclosure is strictly positive, so a design that forbids nothing is making the same kind of error as one that forbids everything. The argument from uncertainty locates a line; it does not point in a direction.

What such a target looks like when written down carefully is the subject of [agency](/governance-mechanisms/agency/): the capacity to achieve one's goals, whatever those goals happen to be. It is derived there from a handful of small worlds rather than proposed and defended, and the derivation constrains the functional form much more tightly than one might expect.

## 6. The argument, end to end

We cannot write down what a society should aim at, because whoever writes it writes themselves into it. So the aim has to be read off the population instead. But we never see what people want — only what they report, through channels that distort, in a population whose wants the institutions already shaped. So we stop specifying the outcome and specify the procedure. A procedure still has to be chosen against something, and that something cannot be a guess about what people want, because the guess is precisely what we just gave up on. What survives are the targets that serve every want rather than any particular one: means, capacity, room to act.

So the framework is one long argument for aiming at means rather than ends — not because ends don't matter, but because we don't know them, won't be told, and will be wrong about them by the time the institution matures. Rawls reached the same place through fairness. This route reaches it through ignorance, which is a weaker premise and therefore a stronger argument: you do not have to accept anything about justice to accept that you cannot predict what your grandchildren will want.

And that returns us to the claim at the top. Choosing the target remains a moral question — §1 does not dissolve it, and the companion posts are explicit about the commitments left unforced. But once the target is fixed, the *residual* question is an estimation problem, and estimation problems can be got wrong in ways you can detect. That is the only real advantage this framing has over the four centuries of argument it is trying to join.