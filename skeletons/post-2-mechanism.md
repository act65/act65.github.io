# Post 2 — Mechanism design and preference aggregation (skeleton)

**Working title:** TBD (placeholder — candidate: "The upstream problem" or "Politics as mechanism design")
**Slug:** TBD
**Role in series:** The "goal specification" half of alignment. How should the mechanism that selects collective goals be designed?
**Target length when written:** ~3500-4500 words.

---

## Section 1 — Frame (one paragraph)
- Given Post 0 (procedural framework) and Post 1 (agency as candidate target), this post asks how the *mechanism* that aggregates preferences should be designed.
- The Thiel hook can live here as an opener if useful — "democracy and freedom no longer compatible" sets up "let's analyse democracy as one mechanism among many."
<!-- not sure about this Thiel hook? -->

## Section 2 — The problem of scale
- (Reuse upstream-v6 §1 nearly verbatim.)
- Small groups solve preference aggregation by face-to-face talk + memory + ongoing renegotiation. None of these scale.
- As populations grow: preferences become unknowable to participants; monitoring costs explode; individual contributions become invisible; small coordinated groups capture the inattentive majority.
- So we replace simple mechanisms with formal ones. Prices, votes, contracts. Each is a *compression* — and each compression loses information.


<!-- yes, this section is very important! need to motivate the problem -->

## Section 3 — The mechanism-design move
- (Reuse upstream-v6 §2 opening.)
- The shared move across capitalism and democracy: rather than specify the right *outcome* (which we can't — see Post 0), specify a *procedure* that aggregates preferences.
- Mechanism design = the inverse problem of optimisation: given a desired outcome, work backwards to rules whose stable behaviour produces it.
- **Load-bearing line:** "every set of rules implicitly optimises for something, whether or not anyone designed it to." Keep this prominent. Whether a mechanism is "working" = whether its implicit objective matches its advertised one.

## Section 4 — Capitalism as case study (specification failure)
- (Reuse upstream-v6 §2 "Capitalism's failure mode".)
- Advertised mechanism: markets aggregating consumer preferences.
- Actual mechanism: boards aggregating *shareholder* preferences (legal doctrine of shareholder primacy).
- The mechanism is *working*; it's just optimising for the wrong thing.
- Case studies (2008, opioids, climate denial, tobacco) — introduce here, will be reread in Post 3 from the pursuit angle.
- The capture happens at the level of *rules*. Shareholder primacy, limited liability, board structure. Each was added for defensible reasons; the combination is the captured mechanism.

## Section 5 — Democracy as case study (specification failure)
- (Reuse upstream-v6 §2 "Democracy's failure mode".)
- Advertised: citizens vote, representatives implement.
- Distortion vectors: lobbying, campaign finance, gerrymandering, $k$-party compression (link voting-geom post), strategic voting, agenda manipulation, deliberate complexification.
- Each is a *rule* or absence of one.
- Empirical record: Acemoglu/Robinson natural experiments show institutional design matters; but China/India/US complicate the "democracy reliably produces good outcomes" claim. The procedural form of democracy is intact in the US while substantive aggregation has decoupled.
- Honest reading: institutional design matters enormously, but the mapping from "broad preference aggregation" to "good outcomes" depends sensitively on the specific mechanism.

## Section 6 — AI as next instance (specification half only)
- (Reuse upstream-v6 §3, but trim the "captor" / pursuit material — that's Post 3.)
- AI alignment: the goal has to come from somewhere outside the AI. *Which* humans, *by what procedure*?
- RLHF aggregates from a small set of annotators. Constitutional AI from a small set of researchers. Industry from a small set of executives.
- Structurally identical to corporate aggregation: small input set, opaque method, advertised aggregation ("aligned with human values") much narrower than claimed.
- Forward link: if the *pursuit* machinery is good (Post 3), a captured specification produces a powerful optimiser faithfully serving captors.

## Section 7 — The design space
- Near-term reform proposals as hypotheses in the design space:
  - Quadratic voting / quadratic funding.
  - Proportional veto core / Glen Weyl-style work.
  - Liquid democracy.
  - Public campaign financing.
  - Stakeholder governance (beyond shareholder primacy).
  - Antitrust reform.
  - Citizens' assemblies / sortition.
- Each is a candidate mechanism. None is *the* answer; each is a testable hypothesis about which rules are robust to which failure modes.

<!-- great! -->

## Section 8 — Why something democracy-like emerges
- This is the user's "and eventually something democracy-like emerges" beat.
- Argue: the desiderata from Post 0 (pluralism, updatability, robustness, transparency, non-domination) tend to force certain structural features:
  - **Broad input** — pluralism + non-domination forbid narrow input sets.
  - **Periodic re-specification** — updatability forbids one-shot oracular specifications.
  - **Separation of powers** — robustness forbids concentrating capture-vectors.
  - **Contestability** — transparency requires inspection rights.
- These properties don't fix one specific mechanism, but they rule out monarchy, dictatorship, technocracy without contestation, and rule-by-private-corporation. What's *left* in the design space looks democracy-shaped.
- Important caveat: democracy-shaped ≠ contemporary Western parliamentary democracy. The design space includes systems we haven't tried.

<!-- we can write this as a conjecture/hypothesis!?
 -->

## Section 9 — Open research questions
- What's the right aggregation rule under cardinal preferences? (Range, QV, etc.)
- How robust to capture is each candidate mechanism, formally?
- When do Arrow / Gibbard-Satterthwaite / Sen's liberal paradox bite, and where can their assumptions be relaxed?
- Coupling: how does the mechanism interact with $K_{system}$? Does designing $m$ to maximise $K_{system}(m)$ converge, or oscillate?
- Empirical: can we run candidate mechanisms in DAOs / small-scale deployments? (Link align-dao post.)

## Section 10 — Closing
- A mechanism that specifies a goal still needs machinery to *pursue* the goal once specified.
- Forward link → Post 3.

## Cross-references
- Back → Post 0 (procedural framework, desiderata), Post 1 ($K_{system}$ as objective).
- Forward → Post 3 (pursuit machinery).
- Outside: voting-geom, sct, align-dao.

## What to reuse from existing material
- `upstream-v6.md` §1, §2 (both failure-mode subsections), §3 (specification half only), §6 near-term project list.
- `_posts/inbetween-posts/2025-10-23-agency.md`: "Designing the Game of Society" closing section + the $m^* = \arg\max_m K_{system}(m)$ formulation. Lift into Section 7 or 8.

## Open questions before writing
- Where does the Thiel hook go — opening, or buried? Recommend: opening, but explicitly framed as "I'm not litigating Thiel's claim; I'm asking what would make it answerable."
- How much of the empirical record (Acemoglu/Robinson, China/India) to keep? Recommend: keep the honest reading paragraph; cut detailed exegesis.
<!-- heh, maybe yet another post? history / Acemoglu/Robinson is what originally inspired this work. it's what answers, why should i care? history shows us the importance of 'good' political systems! it's har to imagine a prosperous future without inclusive economic/political systems - inclusive meaning you have some say in the future! -->
- Section 8's "democracy-like emerges" — is the argument rigorous enough to make in a blog post, or is it a hand-wave? Worth flagging to user. Currently it's a sketch, not a proof. Honest framing: "these properties *constrain* the design space toward democracy-shaped systems" rather than "force."
