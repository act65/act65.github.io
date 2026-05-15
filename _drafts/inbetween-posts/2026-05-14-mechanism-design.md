---
title: Mechanism design and preference aggregation
subtitle: How capitalism, democracy, and AI training all become captured
layout: post
categories:
    - economic
permalink: /governance-mechanisms/mechanism-design/
---

[Post 0](/governance-mechanisms/) and [Post 1](/governance-mechanisms/agency/) set the stage: design a *procedure* that aggregates preferences, and aim that procedure at *agency* — the system's capacity to enable its members to pursue their goals. This post takes up the next question: what mechanism produces aggregation that approximates that target, under realistic conditions of scale, capture, and adversarial behaviour?

The argument has four parts. First, why preference aggregation is hard at scale — small-group mechanisms don't generalise. Second, the mechanism-design move: every set of rules implicitly optimises for something, whether anyone designed it to or not. Third, two case studies of captured aggregation — capitalism and democracy — and the structural reason both failed in similar ways. Fourth, a conjecture: something democracy-shaped, but not contemporary parliamentary democracy, emerges from the procedural desiderata laid out in Post 0.

The [why-care](/governance-mechanisms/why-care/) sibling post covers the historical case for why this matters — Acemoglu and Robinson, inclusive vs extractive institutions, the cost in human welfare of getting collective decision-making wrong. This post assumes you're convinced and works the *how*.

## 1. The problem of scale

Most decisions in small groups are easy. Three friends choose a restaurant by talking it through. A village allocates fishing rights by remembering who fished where, for how long, and renegotiating ongoingly. A family of five splits chores the same way. These work because the group is small enough that everyone's preferences fit in everyone's head, monitoring is cheap, and trust accumulates faster than it erodes.

None of these scale. A city of a million people cannot choose a tax rate by talking it through. A continental economy cannot allocate resources by remembering who is owed what. A nation cannot decide foreign policy by renegotiation in someone's living room. The mechanisms that work for three friends or fifty villagers don't scale to a thousand, let alone a million, let alone a billion.

Four things happen as $N$ grows.

- **Preferences become unknowable.** You cannot survey what a million strangers want, let alone weigh it against your own.
- **Monitoring costs explode.** Checking whether decisions are being implemented faithfully requires effort proportional to the population.
- **Individual contributions become invisible.** A single voice in a billion-voice chorus is statistical noise.
- **Capture becomes easy.** The inattentive majority cannot afford to defend itself against the attentive minority, who can specialise in extraction.

So we replace the small-group norms with formal mechanisms. Prices replace personal knowledge of supply. Votes replace face-to-face deliberation. Contracts replace remembered obligations. Each formal mechanism is an attempt to compress a kind of collective decision-making into something that runs at scale.

This is where mechanism design becomes the relevant discipline. Once we accept that we are running collective decision-making *as an algorithm* rather than *as a conversation*, the question becomes which algorithms have which properties.

## 2. The mechanism-design move

**Mechanism design is the inverse problem of optimisation: given a desired outcome, work backwards to a set of rules whose stable behaviour produces that outcome.** Speed limits, fines, and licences are a mechanism designed (imperfectly) to produce safe driving. Patent law is a mechanism designed to produce innovation. Tax brackets are a mechanism designed to produce some pattern of distribution.

It's important to keep in mind the reverse direction:

**Every set of rules implicitly optimises for something, whether anyone designed it to or not.**

Write down the rules of a system. Ask what stable behaviour emerges from rational agents playing under those rules. The implicit objective of the system is whatever its stable behaviour produces — regardless of what its advertised purpose claims. Whether a mechanism is "working" is the question of whether its implicit objective matches its advertised one.

This framing changes how you look at institutions. Corporate governance, parliamentary democracy, RLHF, central banking — each is a set of rules whose stable behaviour you can read off and compare against the stated purpose. Mismatches are not bugs to be fixed; they are the system doing exactly what its actual rules require, which often differs from what its defenders claim.

## 3. Capitalism as captured aggregation

Capitalism's advertised mechanism is *markets aggregating consumer preferences*. Prices carry information about supply and demand; competition rewards firms in proportion to the public good they provide; the invisible hand converts individual preferences into a collective outcome. Smith's argument was, in modern terms, a claim about a *distributed mechanism* for preference aggregation.

The actual mechanism is different. Inside any corporation of meaningful size, the aggregation that determines its behaviour is between *shareholders*, not consumers. Boards aggregate shareholder preferences; executives implement; consumer "votes" via purchase are noisy, lagged, and frequently overridden by marketing, regulatory capture, and asymmetric information. The legal doctrine of *shareholder primacy* makes the substitution formal — directors have a fiduciary duty to shareholders, not to the broader public the original capitalist argument claimed they served.

The mechanism is working. It is *successfully* aligning the corporation with the preferences of a small set of investors. The problem is that the implicit objective it optimises for (shareholder return) is not the advertised one (broad consumer welfare through preference aggregation). The mechanism delivers what its rules require. The rules require the wrong thing.

The consequences are familiar: the 2008 financial crisis, decades of funded climate-change denial, the opioid epidemic, tobacco's public-health deception. These outcomes are what *maximise returns to a small set of investors* produces when executed faithfully under modern conditions. The optimiser performs exactly as its objective function requires. The objective function is wrong because the procedure that produced it was captured.

The capture happens at the level of the *rules*. Shareholder primacy is a rule. Limited liability is a rule. The structure of corporate boards is a rule. Fiduciary duty is a rule. Each was added at some point, often for defensible reasons, and the combination produces a mechanism whose actual aggregation behaviour differs sharply from what the original capitalist claim advertised.

Fixing this is mechanism design: which combination of rules produces a mechanism whose implicit objective is the broad consumer and worker preferences capitalism was supposed to aggregate?

## 4. Democracy as captured aggregation

Democracy has the same structure of failure, with different specifics.

The advertised mechanism is *citizens vote, representatives implement*. The actual mechanism is compromised by a list of capture vectors, each of which acts as a rule (or the absence of a rule) inside the system:

- **Lobbying** systematically reweights legislator attention toward concentrated interests.
- **Campaign finance** ties political success to donor preferences.
- **Gerrymandering** decouples electoral outcomes from voter preferences.
- **$k$-party compression** flattens voter preferences past the point of usability, with [precise information-theoretic limits](https://act65.github.io/voting-geom).
- **Strategic voting** induces voters to misreport preferences to avoid worse outcomes.
- **Agenda manipulation** lets whoever controls the order of votes determine the result.
- **Deliberate policy complexification** defeats voter understanding.

Each is a rule or the absence of one. The combination produces a mechanism whose implicit objective — read off its stable behaviour — is closer to "serve concentrated donor and lobby preferences" than to "serve aggregate voter preferences."

The mechanism is working. It is just optimising for the wrong thing. The procedural form of democracy is intact while the substantive aggregation has decoupled from voter preferences.

The historical record is messier than either democratic advocates or critics admit. Some democracies have produced excellent outcomes for their citizens; some have produced catastrophic ones. Some non-democracies have lifted hundreds of millions out of poverty; some have killed tens of millions. The cleanest reading is that *institutional design matters enormously*, and the mapping from "broad preference aggregation" to "good outcomes" depends sensitively on the specific mechanism. The sibling post on the historical record takes that thread; here it's a footnote.

## 5. AI as the next instance

The AI alignment problem is the same move again, at higher stakes.

For an AI, the goal has to come from somewhere outside itself. (An AI that generates its own terminal goals is a separate and serious problem — also worth working on, but outside the scope of this post; here we assume the goal is specified externally.) The question is then which humans, and by what procedure. RLHF aggregates preferences from a small set of annotators into a reward model. Constitutional AI aggregates them from a small set of researchers writing the constitution. Industry deployments aggregate them from a small set of executives setting product objectives. Each is a preference-aggregation procedure with a small, opaque input set.

This is structurally identical to corporate aggregation. The advertised aggregation ("aligned with human values") is much narrower than its advocates suggest. The actual aggregation is over a tiny in-group: lab leadership, contracted annotators, occasionally a customer advisory board. The mechanism is currently doing exactly what its rules require — aggregating preferences from a small set of capital holders and their employees — and the result is faithfully delivered.

If the corporate analogy holds, the long-run outcome of current AI development is the AI version of shareholder primacy: a powerful optimiser whose specified objective is the preferences of a small set of capital holders, executed faithfully at machine speed under conditions the specifiers didn't anticipate. The corporation is the AI alignment problem already running, at human speed, with bureaucratic friction as the only brake. A modern algorithmic trading firm is a corporation with the human friction stripped out: an autonomous optimiser pursuing pure profit at machine speed. The conceptual distance from there to a misaligned AGI is short.

The sharper version of the worry: an AGI developed inside a corporation under shareholder primacy will inherit shareholder preferences as its specified objective, faithfully. Shareholders have a poor historical record of choosing for the broader public good — that's the lesson of §3. There is no current mechanism through which the broader public's preferences enter the AGI's specification, and no current force compelling lab leadership to install one. The corporate alignment problem is the engine that is actively building the AI alignment problem. (Earlier post: [*The Alignment Problem: Future AI Overlords vs. Present Corporate Greed*](/the-alignment-problem/).)

The pursuit half of this — what happens once the goal is specified — is the topic of [Post 3](/governance-mechanisms/alignment/). For now the relevant point is that preference aggregation is *upstream* of AI alignment, because the AI inherits whatever goal-specification procedure produces its objective. If the procedure is captured, the AI faithfully serves the captor.

## 6. The design space

Candidate mechanisms exist. None has been adequately tested at scale, but each is a hypothesis about which combination of rules is robust to which failure modes.

- **Quadratic voting / quadratic funding.**[^qv] Voters get a budget of credits; the cost of expressing $k$ units of preference for an issue is $k^2$. Reduces the dominance of intensity over consensus. Used in some governance experiments and in Gitcoin grants.
- **Proportional veto.**[^pv] Decisions are valid only if no large minority strongly opposes them. Forces majorities to compromise rather than override.
- **Liquid democracy.**[^liquid] Each voter can either vote directly or delegate their vote to a chosen expert. Delegations are transitive and revocable. Hybridises direct and representative democracy.
- **Sortition.**[^sort] Decisions are made by randomly-selected citizen panels rather than elections. Removes campaign finance and gerrymandering as capture vectors. Used in recent Irish and French constitutional processes.
- **Stakeholder governance.**[^stake] Corporate boards include labour, environmental, and consumer representatives, not only shareholders. Reshapes the actual aggregation behind the advertised one.
- **Public campaign finance and lobbying caps.**[^cf] Restricts the donor-preference channel that distorts contemporary democracy.
- **Antitrust reform.**[^anti] Treats concentrated economic power as a capture vector against the aggregation procedure itself.

None of these is *the* answer. Each is a hypothesis about which combination of rules is robust to which failure mode. The right research move is not to advocate one but to test them as candidate mechanisms in environments where computation is tractable — DAOs, small-scale governance experiments, simulations — and observe their implicit objectives and properties (robustness to manipulation, fairness floors, computational cost, behaviour under preference-distribution shift). The existing post on [the DAO proving ground](/align-dao/) takes one step in this direction.

## 7. Conjecture: something democracy-shaped emerges

The desiderata from Post 0 — pluralism, updatability, robustness, transparency, computability, non-domination — appear to constrain the design space toward certain structural features. The following is offered as a *conjecture* to be tested by the research program above, not a theorem.

**Conjecture.** A mechanism that satisfies the Post 0 desiderata simultaneously has roughly the following structural features:

- **Broad input.** Pluralism plus non-domination forbid narrow input sets. Mechanisms that aggregate preferences from only a small group fail the floor on whose interests count.
- **Periodic re-specification.** Updatability forbids one-shot oracular specifications. The mechanism must include its own revision procedure.
- **Separation of powers.** Robustness forbids concentrating capture-vectors. A mechanism whose adjudication, execution, and revision functions are run by the same actors is one capture event away from failure.
- **Contestability.** Transparency requires that those subject to the mechanism can inspect and challenge it. Black-box aggregation rules out accountability.
- **Cardinal preference channels.** Computability plus pluralism push toward mechanisms that allow intensity information, not only ordinal rankings. Pure ordinal mechanisms are constrained by Arrow's theorem; pure cardinal mechanisms face Gibbard-Satterthwaite-style strategy-proofness limits. The design space lives in some hybrid.

If the conjecture holds, what's left in the design space *looks* democracy-shaped: broadly inclusive input, periodic revision, separated powers, contestable rules. The caveat is important: democracy-shaped *does not* mean contemporary parliamentary democracy. The design space includes mechanisms we haven't yet tried — hybrids of representative and sortition, cardinal voting at scale, decision rules with explicit non-domination floors — and excludes monarchy, single-party rule, technocracy-without-contest, and rule-by-private-corporation. The conjecture does not single out any specific existing democracy as $m^*$.

The conjecture is testable in the same sense the candidate mechanisms above are: pick a structural feature, formalise it as a constraint on the rule set, simulate the induced game, evaluate the resulting Nash equilibrium against $K_{system}$, vary the desiderata weights, observe which features hold up.

## 8. Open research questions

- What is the right aggregation rule under cardinal preferences? Range voting, quadratic voting, score voting, and Harsanyi's social aggregation theorem all give different answers. None is dominant.
- How robust is each candidate mechanism to capture? Formal models of capture are sparse; most existing analyses are post-hoc.
- When do Arrow / Gibbard-Satterthwaite / Sen's liberal paradox bite, and where can their assumptions be relaxed?
- How does the mechanism couple back to $K_{system}$? Designing $m$ to maximise $K_{system}(m)$ may not converge — the mechanism that produces good aggregation under one preference distribution may produce poor aggregation when the distribution shifts.
- Can candidate mechanisms be run in DAOs or small-scale governance experiments? The DAO proving ground post takes a first cut.
- What's the relationship between preference *formation* (adaptive preferences, education, free press) and preference *aggregation*? The two are not separable — the same institutional choices condition both.

## 9. Closing

A mechanism that specifies a goal still needs machinery to *pursue* it. A perfectly designed aggregation procedure that produces $m^*$ but whose outputs are then ignored, drift away, or are overridden by the entity running the mechanism, is no better than no procedure at all. The pursuit half — corporate audits, political watchdogs, AI interpretability — is the topic of [Post 3](/governance-mechanisms/alignment/).

The argument so far: collective decision-making at scale is an algorithm; its properties are formally analysable; the algorithm currently in use across capitalism, democracy, and AI is captured in characteristically similar ways; and the research program is to design uncaptured mechanisms whose stable behaviour approximates the procedural desiderata of Post 0. Whether that program succeeds depends in part on questions that have been worked on for seventy years under the name *social choice theory*, and in part on questions that are new because the substrate — machine-speed optimisation — is new.

---

[^qv]: Lalley & Weyl (2018), *Quadratic Voting: How Mechanism Design Can Radicalize Democracy*; Posner & Weyl, *Radical Markets* (2018), chapter on quadratic voting and quadratic funding.
[^pv]: Moulin (1981) on the proportional veto core; contemporary variants discussed by Buterin under "quadratic payments" and related governance writing.
[^liquid]: Ford (2002), *Delegative Democracy*; Behrens, Kistner, Nitsche, and Swierczek (2014), *The Principles of LiquidFeedback*.
[^sort]: Van Reybrouck (2016), *Against Elections: The Case for Democracy*. Notable real-world instances: the Irish Citizens' Assembly (2016–2018) and the French Convention Citoyenne pour le Climat (2019–2020).
[^stake]: German *Mitbestimmungsgesetz* (1976) as the canonical statutory codetermination model; Edmans (2020), *Grow the Pie*, for a contemporary defence.
[^cf]: Lessig (2011), *Republic, Lost: How Money Corrupts Congress — and a Plan to Stop It*.
[^anti]: Khan (2017), *Amazon's Antitrust Paradox*, Yale Law Journal 126(3); Wu (2018), *The Curse of Bigness: Antitrust in the New Gilded Age*.
