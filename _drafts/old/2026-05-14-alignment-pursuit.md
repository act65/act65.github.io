---
title: Alignment is alignment is alignment
subtitle: Goal pursuit across corporations, political systems, and AI
layout: post
categories:
    - economic
permalink: /governance-mechanisms/alignment/
---

Given the procedural framework from [Post 0](/governance-mechanisms/), the candidate target from [Post 1](/governance-mechanisms/agency/) (*agency* — the system's capacity to enable goal-pursuit), and the mechanism-design problem from [Post 2](/governance-mechanisms/mechanism-design/), this post takes up the last piece: once a goal is specified, how do we build an optimiser that pursues it without drift or destructive externality, and that can be corrected when its specification turns out to be wrong?

Post 2 ended on the observation that even a perfectly designed aggregation mechanism — one that produces $m^*$, the rule set whose Nash equilibrium maximises $K_{system}$ — is useless if the entity running the mechanism then ignores, drifts away from, or overrides its outputs. Specification is upstream; *pursuit* is downstream; both are required.

The thesis is that the pursuit problem is structurally the same across corporations, political systems, and AI. The techniques used in each domain are recognisably the same techniques. The corporate and political literatures have a head start of decades to centuries on the AI literature, and there are specific transplants worth importing.

This is the second half of the *two distinct problems that get called alignment* framing introduced in Post 0 — *choosing the goal* vs *achieving the goal*, equivalently *specification* vs *pursuit*. Post 2 worked the choosing half; this post works the achieving half. Readers who want the empirical motivation for the series should start with the [why-care](/governance-mechanisms/why-care/) entry point.

## 1. The two failure modes

Given a specified goal, there are two characteristic ways an optimiser can fail to pursue it.

**(a) Drift toward operators' private incentives.** The optimiser nominally serves the specified goal but actually serves whoever runs it day-to-day. In a corporation: executives extract rents at the expense of shareholders. In a government: bureaucrats serve their own career incentives at the expense of policy. In an AI system: lab engineers fine-tune the model toward whatever metrics they're personally evaluated on, even when those metrics drift from the original specification. This is the *principal-agent problem* at scale.

**(b) Destructive externalities.** The optimiser faithfully pursues its specification, but the specification didn't anticipate side-effects on third parties. In a corporation: producing widgets faithfully while dumping waste into the river. In a government: optimising for measured GDP while immiserating sectors that don't enter the measure. In an AI system: optimising helpfulness on the training distribution while producing harm on the deployment distribution. This is the *specification-completeness* problem.

Both failure modes require institutional machinery to detect and correct. The detection/correction stack is what this post calls the *pursuit stack*. The structure of the pursuit stack is roughly the same across all three domains.

## 2. The corporate stack

The corporate pursuit stack has been developed over roughly four centuries and is still imperfect.

For (a) — drift toward executive private incentives:
- Internal audits and compliance functions
- Audit committees with mandatory independent directors
- Performance metrics tied to specification (with all the known Goodhart problems)
- Mandatory disclosure of executive compensation and related-party transactions
- Fiduciary duty to shareholders, enforced through derivative lawsuits

For (b) — destructive externalities to third parties:
- Independent regulators (SEC, EPA, FDA, FTC) with specific subject-matter authority
- Mandatory transparency requirements (financial disclosures, environmental impact reports, drug-trial registration)
- Whistleblower protections (Sarbanes-Oxley §806; Dodd-Frank §922)
- Investigative business journalism as informal third-party audit
- Antitrust enforcement against concentration that defeats competition
- Criminal liability of officers for specific categories of harm (securities fraud, environmental crimes, foreign corruption)

Each is a specific institutional move addressing a specific failure mode. The combination is still capturable — regulatory capture is the canonical critique (Stigler 1971), and the 2008 financial crisis demonstrated that audit, regulation, and criminal liability can all fail simultaneously when strong enough incentives align against them. But the stack exists, has been refined for centuries, and is the most developed of the three.

## 3. The political stack

The political pursuit stack has been developed over roughly two centuries of modern constitutional democracy, on top of older institutional substrates (rule of law, courts, written law).

For (a) — drift toward bureaucratic or elected-official private incentives:
- Politically neutral civil-service watchdogs (inspectors general)
- Periodic elections as performance review (with all the known capture problems from Post 2)
- Internal accountability mechanisms (parliamentary committees, ethics offices)
- Conflict-of-interest disclosure requirements
- Post-employment restrictions on revolving-door behaviour

For (b) — destructive externalities to constituents or third parties:
- Independent courts with judicial review of executive action
- Independent press (constitutionally protected in some jurisdictions)
- FOIA / sunshine laws / transparency of government action
- Separation of powers between executive, legislative, and judicial branches
- Constitutional limits the executive cannot unilaterally override
- Federalism / subsidiarity as a check on central capture

Same characteristic failure modes as the corporate stack: captured courts, captive press, executive overreach, legislative gridlock. Same observation: the stack exists, has been refined for centuries, and is the most developed political-pursuit machinery humans have produced.

## 4. The AI stack

The AI pursuit stack has been developed over roughly a decade and is correspondingly less mature.

For (a) — drift toward lab or operator private incentives:
- Internal red-teaming and evaluations
- Capability evaluations (mandatory in some jurisdictions; voluntary elsewhere)
- Scaling-policy commitments (responsible scaling policies)
- Internal model cards and audit trails

For (b) — destructive externalities to users and third parties:
- Interpretability research (transparency analog, still nascent)
- Independent evaluation organisations (METR, Apollo, others)
- Deployment constraints (use-case restrictions, content policies)
- Constitutional constraints the system cannot unilaterally self-modify (Constitutional AI; the lab still controls the meta-level)
- Voluntary government partnerships (UK AISI, US AISI)

A few years of development. Structurally analogous to the corporate and political stacks but missing layers the others have. The next section makes the comparison concrete.

## 5. Side-by-side

Reading the three stacks at the same level of abstraction:

| Function | Corporate | Political | AI |
|---|---|---|---|
| Internal audit | Audit committee; internal compliance | Inspectors general; ethics offices | Red-teaming; internal evaluations |
| Transparency / inspection | Financial disclosures; environmental impact reports | FOIA; public records; parliamentary records | Interpretability research; model cards |
| External watchdog | Independent regulators (SEC, EPA, FDA) | Independent courts; ombudsmen | Independent evaluation orgs (METR, Apollo); AISI |
| Adversarial press | Investigative business journalism | Free political press | Independent AI journalism (least mature) |
| Whistleblower protection | Sarbanes-Oxley §806; Dodd-Frank §922 | Civil-service protections; public-interest disclosure acts | (largely missing) |
| Anti-concentration | Antitrust enforcement | Separation of powers; federalism | (compute concentration largely unaddressed) |
| Constitutional constraint | Charter / articles of incorporation | Written constitution; judicial review | Constitutional AI — but lab controls the meta-level |
| Individual liability | Officer criminal liability for fraud, environmental crime | Personal liability for malfeasance | (largely missing) |
| Re-specification mechanism | Annual shareholder meetings; board votes | Periodic elections; constitutional amendment | Model updates; RLHF re-training (lab controls) |

Same structural moves under different names. This is not coincidence — it's the same problem instantiated in different substrates. The implication is direct: AI alignment can borrow specific institutional designs that have been developed and tested for decades or centuries in the older substrates. Not in a hand-wave "we should learn from history" way; in a specific *Sarbanes-Oxley §806 protects whistleblowers reporting financial fraud; what would the analogous protection for AI safety reports look like?* way.

## 6. The coupling

Specification and pursuit cannot be cleanly separated.

Goals are implemented over time. The world changes. Preferences change. The optimiser learns. An objective specified at time $t$ becomes the wrong objective at time $t + k$ — sometimes because the original specification produced unintended consequences, sometimes because preferences themselves have shifted in response to what the system has done.

A corporation that perfectly pursued its 1950s shareholder mandate today would be doing something we'd recognise as monstrous (cigarette manufacturers in the 1950s were doing exactly what their charters required). A political system that perfectly pursued 1789 American preferences today would be defending slavery. An AI system that perfectly pursued its 2024 specification in 2030 might be doing something that 2030's specifiers find appalling.

This means the pursuit stack has to do *both* things simultaneously:

1. Pursue the currently-specified goal.
2. Continuously re-specify the goal in response to what is being learned.

Audit reveals problems → next round's specification is updated. Interpretability reveals AI behaviours → the constitution is updated. Voter engagement reveals preferences → policy is updated.

The re-specification *is* a goal-pursuit mechanism, not a separate function. Audit and election are how the system corrects its own specification. Without them, drift accumulates and the system eventually pursues an objective nobody currently endorses.

This is why the Post 2 / Post 3 split is a simplification. Specification and pursuit feed back into each other; the coupling is part of the design, not a complication to be factored out.

## 7. The case studies, revisited

Post 2 introduced four case studies of captured aggregation: the 2008 financial crisis, the opioid epidemic, decades of funded climate-change denial, and tobacco's public-health deception. Those were specification failures — the mechanism that produced the corporation's objective had been captured to serve a narrow set of preferences (shareholders, lobbyists) rather than the broad public the original capitalist claim promised.

Read the same cases from the pursuit angle and they tell a different story.

In each case, the *pursuit machinery worked*. Banks faithfully pursued returns at the cost of systemic risk. Pharmaceutical companies faithfully pursued prescription volume. Oil companies faithfully pursued fossil-fuel revenue. Tobacco companies faithfully pursued cigarette sales. The internal audits, the marketing departments, the legal teams, the executive-compensation structures — every component of the pursuit stack did exactly what it was supposed to do. The horror is that the pursuit machinery *succeeded*. It didn't fail; it succeeded on a misspecified target.

This is the most important lesson for AI alignment: **better pursuit machinery does not fix specification failure**. An AI lab with excellent interpretability, red-teaming, and oversight, deploying a model whose specification was produced by captured aggregation, gets a more-capable version of the corporate failure modes above. The pursuit stack pursues whatever target it is given. The target has to be right.

## 8. AI shareholder primacy at machine speed

The corporate analogy from Post 2 collapses into Post 3 here. The corporation is the AI alignment problem already running, at human speed, with bureaucratic friction as the only brake on its optimisation. A modern algorithmic trading firm is a corporation with the human friction stripped out: an autonomous optimiser pursuing pure profit at machine speed. An AGI deployed under shareholder primacy is the limit case.

The pursuit stack determines the *speed* at which the specified objective is pursued. The specification determines the *target*. Improving the pursuit stack without fixing the specification produces faster pursuit of the wrong target.

Most contemporary AI safety work focuses on the pursuit half — interpretability, red-teaming, evaluations, oversight. This is necessary but insufficient. The specification half from Post 2 is at least as urgent. If Post 2's diagnosis is right (current AI specification mechanisms are captured by lab leadership and capital holders), current pursuit work, however excellent, locks in the captured specification. Better interpretability tools give us a clearer view of a model faithfully serving the wrong people.

## 9. What's missing from the AI pursuit stack

The corporate and political stacks took centuries to develop. The AI stack has had a few years. Specific gaps — each with a specific transplant available from an older stack:

**Criminal liability for AI labs and officers.** When a corporation faithfully pursues its objective and produces harm — securities fraud, environmental damage, foreign corruption — officers can be held personally liable. Sarbanes-Oxley made this explicit for financial misconduct after Enron. The transplant: liability of AI lab officers when their systems cause specific categories of harm (deceptive behaviour at scale, mass fraud facilitation, weapons-system misuse). The corporate-governance literature on officer liability (Bainbridge, Bebchuk) is the relevant source.

**Antitrust analog for compute concentration.** Post 2 cited Khan (2017) and Wu (2018) on antitrust against information-platform concentration. Compute is the more direct case: control of training compute determines who can train frontier models. The transplant: structural separation of compute provision from model development, or — at minimum — mandatory third-party access to compute infrastructure on non-discriminatory terms. Brandeis's "other people's money" framing from 1914 is the older precedent worth re-reading.

**Independent press analog.** The corporate stack has investigative business journalism (Pulitzer-tier reporting on corporate misconduct). The political stack has investigative political journalism. The AI stack currently has lab-funded comms shops, a small number of independent journalists (Karen Hao, Cade Metz, others), and a much larger volume of access-mediated reporting that effectively serves as lab PR. The transplant: foundation-funded investigative journalism focused on AI labs, with the same independence guarantees that protect financial and political reporting. The media-systems literature (Hallin & Mancini 2004) covers analogous arrangements.

**Adversarial transparency.** Current interpretability work is largely *friendly* — lab-internal teams or close collaborators inspect lab-internal models. The corporate analog is closer to a forensic audit by SEC staff who don't work for the audited firm. The transplant: interpretability that hostile actors can use to verify lab claims, not just friendly evaluators. Concretely: standardised interpretability benchmarks; third-party access to model weights under defined evaluation conditions; public reproducibility of capability claims.

**Whistleblower protections.** Sarbanes-Oxley §806 protects employees who report financial fraud; Dodd-Frank §922 expanded this to securities violations broadly. Similar protections exist for civil-service whistleblowers in many jurisdictions. The transplant: explicit legal protections for AI lab employees who report safety violations, with both anti-retaliation provisions and (more difficult) provisions that survive non-disclosure agreements. The whistleblower-law literature (Glazer & Glazer 1989; subsequent work on Sarbanes-Oxley implementation) is the relevant source.

**Contestability of the constitution.** Constitutional AI produces a "constitution" — a set of higher-level principles the model is trained to follow. Currently, the constitution is written and revised by the lab. Constitutional democracies have specific procedures by which the governed can initiate amendment (referendum requirements, supermajority thresholds, federal-state ratification structures). The transplant: a formal procedure by which ordinary users can initiate constitutional revision, with the lab required to respond on a specified timeline and produce reasoned justification for any rejection. Constitutional design literature (Elster's *Securities Against Misrule* 2013; Sunstein's *Designing Democracy* 2001) covers analogous procedures for political constitutions.

Each of these is a hypothesis: borrow the institutional design from the older stack; ask which transplant works. Some will; some won't, because the substrate is different. The point is not that every move from the older stacks transplants cleanly. The point is that the AI alignment field is currently rediscovering questions that have been worked on for decades in the older domains, and explicit borrowing would be a faster path than re-derivation.

## 10. Closing

Pursuit machinery is only as good as the specification it pursues. Better pursuit on a captured specification produces faster pursuit of the wrong target. The two problems are coupled; working on either in isolation is doing it wrong.

The agenda from Post 0 — design a procedural framework that satisfies minimal desiderata, aim it at a candidate target (agency / $K_{system}$), instantiate it in a mechanism (Post 2), and pair the mechanism with pursuit machinery (this post) — is one coherent way to think about the problem of building optimisers that produce outcomes the people subject to them would endorse on reflection.

None of the four posts is finished. Each is a sketch of a research program. The argument across all four is that collective decision-making is an algorithm whose properties are formally analysable; that the algorithm currently in use is failing in characteristically similar ways across corporate governance, parliamentary democracy, and AI deployment; that better algorithms exist; and that designing them is the most important engineering problem of the next decade. Pushback, counter-examples, and specific transplants from literatures I've missed are all welcome.
