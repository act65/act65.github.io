# Post 1 — Agency as candidate objective (skeleton)

**Working title:** TBD (placeholder — currently "Is democracy the optimal algorithm for collective freedom?")
**Slug:** TBD (current: agency)
**Role in series:** Defines the target of preference aggregation. Translates philosophical objectives into mathematics.
**Target length when written:** ~3000-4000 words.

---

## Section 1 — Frame (one paragraph)
- Given Post 0's procedural framework, the next question is what we're aggregating *toward*.
- This post translates vague philosophical notions into precise mathematical objectives, critiques each, and lands on **agency** (capacity to achieve one's goals) as the candidate that survives.
- Drop the Thiel framing — it belongs in Post 2.

<!-- let's get formal with each of these translations! 
start with th abstract philosophical notion, then we end up with an equation!

(will want to walk through some consequences of these definitions. also there might be multiple formal defintions, some working 'better' than others)
-->

## Section 2 — Translation 1: "Maximise happiness"
- Classical utilitarianism. Sum (or average) of individual utility / hedonic states.
- Failure modes:
  - Hedonic adaptation: the unit you're maximising drifts over time.
  - Wireheading: a happiness-only optimiser collapses the achievable-state set to a single state.
  - Repugnant conclusion (Parfit): "very large population with lives barely worth living" dominates.
  - Preference vs experience: do you maximise what people *want* or what they *feel*? Diverge sharply.

<!-- do we also need to add a conversation about nash utility (using a product instead of sum?).
this fixes some issues with max happiness (the gladiator problem - 1000 people enjoying watch 2 people suffer). but introduces other issues? now everyone has a veto? cannot ever make someone unhappy for the greater good.
 -->

## Section 3 — Translation 2: "Minimise suffering"
- Negative utilitarianism (Pearce; sometimes attributed to Popper).
- *Not equivalent to maximise happiness.* Flag this explicitly — colloquial conflation is doing real damage.
- Failure modes:
  - Antinatalism (no humans = no suffering).
  - "World-destroyer button" — pressing it minimises future suffering to zero.
  - Asymmetry of weight: rules out positive-sum tradeoffs.

## Section 4 — Translation 3: "Equality of opportunity"
- Splits into two distinct mathematical objects:
  - **Rawlsian maximin**: maximise the worst-off person's welfare. Sensitive only to the worst-off; insensitive to improvements elsewhere.
  - **Sen / Nussbaum capabilities**: the set of states (functionings) a person can reach. Concerned with *freedom to achieve*, not realised welfare.
- Capabilities is the direct ancestor of the agency definition. Name the lineage; this is where the post earns its philosophical credentials.

## Section 5 — From capabilities to formal agency
- Translate Sen's capabilities into something computable. Need a multi-agent universe to make this concrete.
- Running example: commuters on a grid. (Inherited from existing post.)
- The four-attempts ladder (tightened version of current Attempts 1-4):
  1. Count immediate actions → myopic.
  2. Count unique futures → ignores probability.
  3. Weight futures by probability → passive; ignores intent.
  4. Achievable goals → entangles with others' goals.
- Each attempt is wrong for an identifiable reason; the failures cumulatively force a system-level view.

<!-- maybe we need yet another post?
i think this post should just present our definition of agency?
the derivation of our definition / exploring dead ends can be in another post? (the original agency post?)
 -->

## Section 6 — The pivot
- Attempt 4's failure isn't a refinement — it's a categorical wrong move. Agency cannot be an individual quantity because achievability depends on others' strategies.
- The parking-spot example from current post is doing real work here; keep it.
- Therefore: define agency at the level of the *system*.

## Section 7 — $K_{system}$
- Joint goal vector $\gamma = (g_1, ..., g_n)$.
- Each individual plays a non-cooperative game; stable outcome is Nash equilibrium $\sigma^*(\gamma)$.
- Success score for joint goal $\gamma$ is $\prod_i P(g_i \mid s_t, \sigma^*(\gamma))$.
- $K_{system} = \sum_\gamma \prod_i P(g_i \mid \sigma^*(\gamma))$.
- Reuse current LaTeX, but fix `\sigma^{* }` spacing artefacts and the unmatched `**` on "controllability".
- Treat the sum honestly: it's a measure / distribution over goal vectors, not a count. One sentence to disclaim infeasibility.

## Section 8 — The Legg-Hutter parallel
- Same structure: sum over goals × success score, weighted by complexity (LH) or feasibility (us).
- Position agency as "Legg-Hutter intelligence, applied to a society instead of an agent."
- Keep brief. It's a sidebar that earns the title connection but shouldn't dominate.
<!-- could leave this in the agency derivation post -->

## Section 9 — Why the product (Nash social welfare)
- Sum aggregator: tolerates crushing some for benefit of others.
- Product aggregator: penalises any $P(g_i) = 0$ — bakes in non-domination directly.
- Honest discussion: the product is *fragile*. A single unachievable goal ("be immortal") zeroes out the joint term.
- Alternatives worth naming: geometric mean (normalised product), weighted product (per-individual priors), Rawlsian min. Each makes different tradeoffs.
- Defer choice to Post 0's "every aggregator embeds tradeoffs" — note that *choosing* an aggregator is the meta-decision, not the framework.

## Section 10 — Loop back: how does $K_{system}$ behave on the failure modes?
- Maximise happiness: wireheading collapses achievable-state set → $K_{system}$ low. Good.
- Minimise suffering: world-destroyer button → all $P(g_i) = 0$ → $K_{system} \to 0$. Good.
- Rawlsian maximin: similar non-domination flavour but only sees the worst-off; $K_{system}$ penalises any imbalance proportionally. Different objects.
- Capabilities: $K_{system}$ is a way of *making capabilities computable*. Same intuition, formalised.

## Section 11 — Honest limitations
- **Adaptive preferences** (Sen's own critique of utility): goals formed under oppression may endorse the oppression. The framework as written takes goals as exogenous; this is a real gap. Flag, don't pretend to solve.
- **Future people / non-agents.** Children, future generations, animals — do their goals enter the sum? Defer.
- **Measurement infeasibility.** $K_{system}$ is a *conceptual objective function*; it lets us study toy systems and ask formal questions about mechanism design. Lift this sentence from the existing post — it's load-bearing.
- **Goal-formation depends on the mechanism.** Means $K_{system}(m)$ is not separable from $m$. Forward link to Post 2.

## Section 12 — Closing
- $K_{system}$ is the candidate aggregation target for the procedural framework.
- Whether democracy-like mechanisms approximately maximise it is the question Post 2 takes up.

## Cross-references
- Back → Post 0 (framework, desiderata, "every aggregator embeds tradeoffs").
- Forward → Post 2 (mechanism that produces the goal); Post 3 (mechanism that pursues it).
- Outside: Legg-Hutter citation already in current footnote 1.

## What to reuse from existing material
- `_posts/inbetween-posts/2025-10-23-agency.md`: Sections 5-7 (commuter example, four attempts, system-level pivot, $K_{system}$ formula, Legg-Hutter parallel, product/Nash welfare). Most of the existing prose can be lifted with minor edits.
- New material needed: Sections 2-4 (utilitarian / NU / capabilities translations), Section 10 (loop back), Section 11 (adaptive preferences flag).
- Material to drop or move: Thiel framing → Post 2. "Designing the game of society" closing → Post 2.

## Open questions before writing
- Keep commuters example or swap for one that extends to Post 2? Recommend keep — switching mid-series loses the inherited intuition, and Post 2 doesn't need the commuter example.
- How deep into the capabilities literature? Recommend: name Sen and Nussbaum, cite *Development as Freedom*, one paragraph; don't summarise the literature.
- Defend the product aggregator more or less? Currently the existing post embraces it; the honest move is to present it as *one defensible choice* and link to Post 0 for the meta-argument.
