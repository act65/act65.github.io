---
title: "The Provenance of Capital"
subtitle: "A proposal: a public register tracing stolen wealth to the named entities holding it today"
layout: post
permalink: /wealth-provenance/
categories:
    - proposals
---

If a museum wants to hang a painting, it is expected to document the painting's provenance — an unbroken chain of custody from the artist's studio to the present wall, with special scrutiny of the years 1933–1945. A gap in the chain is a problem. A link that passes through a looter is a claim.

No such norm exists for capital. A company, a trust, a state treasury, a university endowment — none of them is expected to produce a chain of custody, and so the standard defense against historical claims ("we didn't steal it") never has to meet the one thing that would test it: the ledger.

This post is a proposal for building that ledger. Not a reparations campaign, not a court — a **register**: a public database whose only outputs are findings of fact and an accounting. What was taken, from whom, when; the chain through which it moved; and the named, currently existing entity where the chain ends.

## The core object: a flow, not an atrocity

The unit of record is not "colonialism" or even "the Congo Free State." It is a **flow**: a documented movement of value from an identified source, through a chain of custody, to a present-day holder. Something like:

```yaml
flow: congo-free-state/rubber-regime/royal-trust
what_was_taken: forced-labour rubber and ivory extraction, Congo Free State
from: populations of the Congo basin
when: 1885-1908
chain:
  - Congo Free State (personal possession of Leopold II, 1885-1908)
      [Berlin Act 1885; concession decrees; shipping manifests]
  - Fondation de la Couronne (Leopold's asset vehicle)
      [foundation statutes; contemporary litigation records]
  - Donation Royale / Koninklijke Schenking (est. 1903)
      [founding donation act; current Belgian state registry]
ends_at: Donation Royale, Brussels — extant Belgian state institution
status: documented at every link
right_of_reply: none received (requested YYYY-MM-DD)
```

Every edge in the chain cites a primary document. Every chain terminates in a named entity that exists today — a company with a ticker, a trust with a statute, a state, a building, an endowment. A trace that ends in "society in general" is a *failed trace* and is not published. That single rule does most of the work: it converts an abstraction into an address.

Parallel chains from the same source multiply: the same Congo flow also runs through Union Minière du Haut-Katanga (chartered 1906) to its listed corporate descendant, and through the 1908 annexation terms — under which Belgium paid Leopold 50 million francs "in gratitude," charged against the Congo's own future revenues — to the Belgian state itself.

## Why the records exist

The counterintuitive fact that makes this feasible: **the perpetrators were meticulous bookkeepers, and the books mostly survive.** Empires were accounting operations. The VOC's dividend records, charters, and the 1799 nationalization acts (by which the Dutch state accepted its assets *and debts*) are archived. Britain's 1833 slave-owner compensation was administered by a commission that recorded every claimant by name — which is why UCL researchers could publish the complete database in 2013. Haiti's "double debt" ran through French banks whose records let journalists reconstruct the payments 197 years later. Leopold understood this perfectly, which is why he spent eight days burning the Congo Free State's archives — and even that failed, because the counterparties kept copies. Shipping lines, banks, notaries, and probate courts are distributed backup systems for exactly the evidence in question.

## Why now

Three things have changed recently enough that this register wasn't buildable a decade ago:

1. **Machine transcription of archives.** Handwritten-text recognition now works on 17th–19th century hands at scale. The bottleneck of colonial archival research — a human reading one ledger page at a time — is gone. Millions of pages of manifests, probate records, and company minutes are becoming machine-readable.
2. **Entity resolution and graph infrastructure.** The ICIJ processed the Panama and Paradise Papers by loading tens of millions of documents into an entity graph and letting a distributed newsroom query it. Corporate genealogy (who absorbed whom, 1602–present) is a solved data-model problem; OpenCorporates and registry data already cover the modern end of every chain.
3. **Language models as archival readers.** Extracting structured flows ("who paid whom, for what, when") from bulk historical text is now cheap. The extraction must be verified by humans — every published edge still cites its document — but the candidate-generation step, which is 95% of the labour, is automatable.

The pieces exist separately: LBS proved archive→database→named-institutions for one country and one compensation event; provenance research does it object-by-object for art; ICIJ does it leak-by-leak for the present. Nobody has built the general instrument.

## Design rules

**1. No remedies.** The register computes and publishes. It demands nothing, sues nobody, proposes no figure of what is owed. Every standard objection to reparations — "it was long ago," "I didn't do it," "the sum is incalculable" — is an objection to a remedy. None of them is an objection to an audit.

**2. Documents over narrative.** The register asserts only what its cited documents show. Where a link is inferred rather than documented, it is marked as such and graded (documented / probable / contested / broken). A chain is only as strong as its weakest published grade, and the grade is displayed, not hidden.

**3. Right of reply, inline and permanent.** Every named terminal entity is notified and offered a response, published unedited alongside the entry. A response becomes part of the record. So does its absence.

**4. Start narrow.** The first cases should be ones where wrongfulness is not the contested question: flows the perpetrator state itself later condemned or admitted (the Congo Free State, slavery compensation, confiscations with surviving legal records). The register's early credibility is worth more than its early coverage. Contested categories can come once the methodology has survived attack.

**5. The traceability threshold answers the regress.** The obvious objection: "go back far enough and all property is theft — where does this end?" It ends where the documents end. The register doesn't claim all wealth is stolen; it publishes chains in which every link is documented. "Everything is theft eventually" is an argument against a philosophy. It is not an argument against entry #4471 and its eleven cited sources.

## The hard problems (and why they're survivable)

**Fungibility.** Money commingles; once a flow enters a general treasury, you cannot follow a particular guilder. But the register's claim is at the entity level — "this entity absorbed this flow" — not the banknote level. And where finer tracing matters, the legal technology already exists: equity's tracing rules (following misapplied funds through mixed accounts) were developed by trust law for precisely this problem, centuries ago.

**Valuation.** What is a 1621 nutmeg monopoly worth today? The register's answer: that is a *view*, not a *record*. The record is the nominal flow and its dates. Valuations — under stated compounding conventions and counterfactual assumptions — are computed on top, published as ranges with the assumptions exposed, the way the *Times*' Haiti analysis published $21–115 billion rather than one false-precision number.

**Dissolved chains.** Some chains end in entities that died without successors. That's still a finding — recorded as *extinguished* — and the pattern of which fortunes survived versus evaporated is itself information.

**Libel.** Publish documents; assert only what they show; grade everything; host in a strong-speech jurisdiction; give the right of reply. The LBS database has operated for over a decade naming banks, colleges, and families, and has been contested on interpretation but not destroyed on fact — because compensation ledgers are hard to sue.

**Who runs it.** The workable shape is probably the ICIJ model wrapped around an academic core: a small editorial spine (archivists, forensic accountants, historians) setting evidence standards; distributed contributors (the genealogy and local-history communities are an enormous unpaid research corps that already does adjacent work); newsroom partners for the launches. Funding from foundations — with the irony that most philanthropic capital would itself be traceable, duly noted, and honestly the register should trace its own funders first. It would be the cheapest possible demonstration of good faith and of the method.

## What success looks like

Not lawsuits. The measurable outcome is a change in what the named entities *say*. Before the LBS database, British institutions' position on slavery wealth was a vague "those were different times." After it, the position became "yes, entry such-and-such is us, and here is our response" — apology, research programme, funding commitment, or stonewall, but in every case *engagement with a specific record*. The general claim invites the general denial. The itemised claim does not.

"We didn't steal it" is true, and it answers a question nobody asked. The register asks the answerable one: *what are you holding, and what is its provenance?* For a painting, we already agree that question deserves a documented answer. This proposal just extends the norm from the canvas to everything else the same ships carried.

---

*Related: I'm exploring the same mechanism in fiction — a 1947 tribunal whose only power is publishing an accounting. And the register's patron saint is E. D. Morel, the shipping clerk who reconstructed the Congo atrocity from cargo manifests alone: the original proof that when the harm is unmeasurable, you audit the beneficiary.*
