# Post 0 — Why a procedural framework? (skeleton)

**Working title:** TBD (placeholder)
**Slug:** TBD
**Role in series:** Justifies the assumptions baked into Posts 1-3. Should be read first.
**Target length when written:** ~1500-2000 words.

---

## Section 1 — The problem with substantive goals

<!-- earlier in our convo you wrote "2. Preferences are the right input. Not virtues, not Maslovian needs, not revealed flourishing. Sen's "adaptive
  preferences" critique bites here — oppressed people may prefer their oppression.
" I like this! work it in!? -->

- Humans are diverse; preferences are heterogeneous and they shift over time.
- Specifying a fixed substantive goal for society ("maximise happiness", "obey the Ten Commandments", "achieve the workers' paradise", "implement CEV") is a category error: it assumes either (a) we know the good, or (b) we'll converge on it under reflection.
- Both assumptions are doing too much work. Empirically, reflection has not produced convergence. Substantive ethical specifications either get captured by their specifiers or fail to track preferences that didn't exist when they were written.
- *Therefore:* don't specify the goal. Specify the *procedure* that picks the goal.

## Section 2 — The procedural turn
- Rawls' veil of ignorance is the canonical version: design the rules from a position where you don't know which member of society you'll be.
- Mechanism design generalises this: design the rules of the game, observe what stable behaviour emerges, evaluate that behaviour against your desiderata.
- Capitalism and democracy are two large-scale attempts at procedural turns (markets and voting as preference aggregators). Both visibly failing — but the *kind* of move was right; the *specific mechanisms* have known flaws. (Hand-wave; full argument in Post 2.)
- Position this as a research program in the Rawls/Sen lineage. Name predecessors explicitly.

## Section 3 — What properties should the framework have?
Six desiderata, each one sentence + one example of how it might fail:
1. **Pluralism** — treats heterogeneous preferences without privileging one substantive view.
2. **Updatability** — re-specifies as world / preferences change. Static specifications go stale (1789 American preferences would defend slavery today).
3. **Robustness** — resistant to capture, strategic manipulation, distortion. (Shareholder primacy is what capture looks like.)
4. **Transparency** — inspectable and contestable by those subject to it.
5. **Computability** — runnable at scale; preference-elicitation overhead must be sublinear in population.
6. **Some non-domination property** — no person's outcomes can be obliterated for others' benefit.

## Section 4 — Honest caveat: procedural ≠ neutral
- Choosing pluralism is itself an ethical stance.
- Choosing non-domination is itself an ethical stance.
- The framework is *procedurally minimal*, not value-free.
<!-- i like this. the goal here is to find a minimal set of axioms to start from.
with as few value statements / ethical stances take which allow everyone down stream to express their own value statements / ethical stances -->
- **Family of impossibility results:** Arrow (ordinal aggregation), Gibbard-Satterthwaite (strategy-proofness), Sen's liberal paradox, Hylland-Zeckhauser, Myerson-Satterthwaite. Cardinal mechanisms (range voting, QV, Harsanyi) escape Arrow but face their own constraints. The honest claim: every aggregator embeds structural tradeoffs; the choice of which tradeoffs to accept *is* a substantive commitment.
- This doesn't undermine the framework. It just means we're honest about what we're committing to. Procedural minimalism gives you more pluralism than substantive ethics; it gives you less than impossible-to-achieve neutrality.

## Section 5 — What this framework is not
- Not a refutation of substantive ethics. If you think CEV / classical utilitarianism / virtue ethics / religious ethics can specify the good directly, this whole agenda is moot — but the historical record is not on your side.
<!-- might be good to walk through some examples? the church...? -->
- Not a defence of any specific existing mechanism. Capitalism and democracy are case studies of procedural attempts, not destinations.
- Not assuming preferences are sacred. Sen's adaptive-preferences critique bites; preferences formed under oppression may endorse the oppression. The framework needs an answer (probably: process must include preference-formation conditions, not just preference-aggregation). Flag this, defer full treatment.

## Section 6 — Roadmap
- Post 1: what's the right *target* for the aggregation procedure? Argues for agency.
- Post 2: how should the *specification mechanism* be designed? Argues something democracy-like emerges from the desiderata, but contemporary democracies are captured implementations.
<!-- democracy-like, with key differences/improvements! -->
- Post 3: given a specified goal, how do we *pursue* it without drift? Same problem in AI, corporations, and politics — same techniques (transparency, audit, watchdogs, iterative feedback).

## Cross-references
- Forward → Posts 1, 2, 3.
- Outside posts: existing voting-geom, sct, align-dao posts can be linked from Section 2 and Section 3.

## What to reuse from existing material
- Nothing directly; this post is new. Some framing from upstream-v6 §6 ("the agenda") fits the roadmap.

## Open questions before writing
- How explicit to be about Rawlsian lineage? (Recommend: explicit but brief; don't get bogged down in Rawls exegesis.)
- Where to place Sen's adaptive-preferences critique? (Section 5 as flagged, or expand into its own section?)
- Tone: "research agenda" vs "philosophical essay"? Recommend research-agenda — terser, less pretension.
