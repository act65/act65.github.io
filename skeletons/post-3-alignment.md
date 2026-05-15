# Post 3 — Goal pursuit and alignment parallels (skeleton)

**Working title:** TBD (placeholder — candidates: "Alignment is alignment is alignment", "Specification vs pursuit", "The machinery of pursuit")
**Slug:** TBD
**Role in series:** The "goal pursuit" half of alignment. Given a specified goal, how do we build an optimiser that pursues it without drift or destructive externality? Same problem in AI, corporations, politics.
**Target length when written:** ~3000-4000 words.

---

## Section 1 — Frame (one paragraph)
- Given Posts 0-2 (procedural framework, agency target, specification mechanism), this post asks how to *pursue* the specified goal.
- Thesis: this is structurally the same problem across AI, corporations, and politics — and the techniques developed in each domain are recognisably the same techniques.
- Position this as the second half of the "two distinct problems that get called alignment" framing from upstream-v6.

## Section 2 — The two failure modes of goal pursuit
- (Reuse upstream-v6 §4 abstract framing.)
- (a) **Drift toward operators' private incentives.** The optimiser nominally serves the specified goal but actually serves whoever runs it day-to-day.
- (b) **Destructive externalities.** The optimiser faithfully pursues its specification but the specification didn't anticipate side-effects on third parties.
- (a) is the principal-agent problem at scale. (b) is the specification-completeness problem.
- Both require institutional machinery to detect and correct.

## Section 3 — The corporate stack
- (Reuse upstream-v6 §4 corporate paragraph.)
- For (a): internal audits, board oversight, performance metrics, internal compliance.
- For (b): independent regulators, transparency requirements (financial disclosures, environmental impact), whistleblower protections, investigative journalism, antitrust enforcement, criminal liability of officers.
- Centuries of development; still imperfect; specific known failure modes (regulatory capture, captured boards, lobbying that defangs oversight).

## Section 4 — The political stack
- (Reuse upstream-v6 §4 political paragraph.)
- For (a): politically neutral watchdogs, internal accountability mechanisms, performance review (elections).
- For (b): independent courts, independent press, transparency of government action (FOIA), separation of powers, constitutional limits the executive cannot unilaterally override.
- Also centuries of development; also imperfect; same characteristic failure modes (captured courts, captive press, executive overreach).

## Section 5 — The AI stack
- (Reuse upstream-v6 §4 AI paragraph.)
- For (a): interpretability (transparency analog), red-teaming (audit analog), independent evaluators, oversight boards, deceptive-behaviour detection (whistleblower analog).
- For (b): deployment constraints, constitutional constraints the system cannot self-modify, capability evaluations, scaling-policy commitments.
- A few years of development; structurally analogous to the corporate/political stacks but missing a lot of layers the others have.

## Section 6 — Read the three stacks side-by-side
- This is the visual / structural payoff. Put the three side-by-side (table or parallel paragraphs).
- Same structural moves under different names: transparency, audit, watchdogs, iterative feedback, separation of authority, constitutional constraints, individual accountability.
- This is *not* coincidence. It's the same problem instantiated in different substrates.
- Implication: AI alignment can borrow rich literatures from corporate governance and political accountability that it's currently reinventing.

## Section 7 — The coupling (specification and pursuit can't be cleanly separated)
- (Reuse upstream-v6 §5.)
- Goals are implemented over time. World changes; preferences change; the optimiser learns.
- An objective specified at $t$ becomes the wrong objective at $t+k$.
- Re-specification *is* a goal-pursuit mechanism — the audit reveals what needs re-specifying next round; interpretability reveals AI behaviours that update the constitution; voter engagement updates policy.
- Specification (Post 2) and pursuit (Post 3) feed back into each other. The two-post framing is a simplification.

## Section 8 — Case studies revisited
- 2008 / opioids / climate denial / tobacco — same case studies as Post 2, read differently:
  - **In Post 2:** captured aggregation; the specification pointed at the wrong target.
  - **Here:** faithful pursuit; the *machinery* worked exactly as designed, on the wrong objective.
- This double reading is the payoff of the split. Each post stands alone; together they show the same evidence from two angles.
- The pursuit machinery doesn't fail in these cases — it succeeds. That's the horror.

## Section 9 — AI shareholder primacy at machine speed
- (Reuse upstream-v6 §3 late + §6 mid.)
- The corporation is the alignment problem already running, at human speed, with human bureaucracy as the only brake.
- A modern algorithmic trading firm is a corporation with the human friction stripped out: an autonomous optimiser pursuing pure profit at machine speed.
- AGI is the limit case: arbitrary objective, arbitrary capability, no friction.
- Implication: deploying powerful AI into the current captured corporate substrate is deploying AGI optimisers for shareholder return. The institutional substrate determines what "alignment" means in practice.

## Section 10 — What's missing from the AI pursuit stack
- The corporate / political stacks took centuries; the AI stack has had ~5 years.
- Specific gaps worth naming:
  - **Criminal liability analog** for AI labs / officers when their systems cause harm.
  - **Antitrust analog** for compute concentration.
  - **Independent press analog** — third-party investigative reporting on lab behaviour, not lab-funded comms.
  - **Adversarial transparency** — interpretability that hostile actors can use to verify claims, not just friendly evaluators.
  - **Whistleblower protections** — formal legal protections for lab employees who report safety violations.
  - **Constitutional contestation** — formal procedure for revising "the constitution" that ordinary users (not just lab researchers) can initiate.
- Each is a hypothesis: borrow from the older stacks; ask which transplant works.

## Section 11 — Closing
- Pursuit machinery is only as good as the specification it pursues.
- Loop back: the whole agenda from Post 0 is upstream of this. Building better pursuit machinery in a captured-specification regime gives you faster pursuit of the wrong goal.
- The two problems are coupled. Working on either in isolation is doing it wrong.

## Cross-references
- Back → Post 0 (framework), Post 1 (agency target), Post 2 (specification mechanism).
- Forward → no specific future post; this closes the four-part series.
- Outside: existing align-dao post fits the "proving ground" framing.

## What to reuse from existing material
- `upstream-v6.md` §4 (the three stacks — entirely), §5 (coupling — entirely), parts of §3 (machine-speed AI), §6 (gaps + agenda closing).
- Case studies first appear in Post 2; reread here.

## Open questions before writing
- Whether to use a literal side-by-side table for Section 6, or parallel prose. Recommend: table. The structural similarity is the point and visual presentation makes it land.
<!-- sure, use a table -->
- How aggressive on the "we already have answers in older literatures" claim? It's true and underargued in the AI alignment community; but be specific about which literatures (corporate governance, public administration, regulatory theory) rather than gesturing.
<!-- sure, get specific rather than gesturing -->
- Section 9 — "AI shareholder primacy at machine speed" — is a strong claim. Worth flagging that it depends on the captured-specification reading from Post 2. Honest framing: "if Post 2 is right that current corporate aggregation is captured, then..."
- Tone risk: this post can drift into "AI alignment people don't know what they're doing." Don't. Frame as "rich older literatures exist; bringing them to bear is the move," not "you're reinventing the wheel."
<!-- sure. -->