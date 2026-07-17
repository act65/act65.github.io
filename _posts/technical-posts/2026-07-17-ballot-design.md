---
title: Ballot Structure from the Preference-Dependency Graph
subtitle: Which questions should a ballot ask together? The votes can tell us.
layout: post
categories:
  - research
---

A ballot is a design. It fixes which issues are decided together, which separately, and what each question may be contingent on. Yet nearly every voting system picks one of two extremes without asking: direct democracy decides every issue on its own; party or platform voting bundles everything into a few take-it-or-leave-it packages.

Each extreme is the right design for exactly one kind of electorate. If preferences are independent across issues, issue-by-issue voting is perfect --- and cheapest. But once issues are coupled ("I want the carbon tax *only if* the revenue is rebated"), deciding them separately can elect a package a majority dislikes. Bundling everything avoids that, but scales badly: a bundle over $m$ issues has $2^m$ combinations, so real ballots offer a short menu of them, and every preferred combination left off the menu goes unexpressed.

I've just published v2 of a paper (and an open-source pipeline) that treats the ballot as an object to be *designed* from the electorate's preference structure --- estimated from nothing more than Polis-style agree/disagree votes.

> A ballot fixes which issues are decided together, which separately, and what each question may be contingent on --- and almost every voting system picks one of two extremes. Direct democracy asks every issue alone: optimal when preferences are independent across issues, but able to elect a package a majority dislikes once they are coupled (the multiple-election paradox). Platform voting bundles everything into a few take-it-or-leave-it packages: faithful to any structure, but forced to offer a short menu of the $2^m$ combinations, leaving preferred combinations unexpressed. We treat the ballot as an object to be *designed* from the electorate's preference structure. A ballot, in general, is a rooted forest of contingent questions --- "if the tax passes, should the rebate follow?" --- with the familiar designs as its contingency-free special cases. Any ballot forgoes welfare in exactly two ways --- *separability-distortion*, from deciding coupled issues in separate questions, and *menu-distortion*, from offering fewer combinations than voters demand --- and both are governed by the dependency graph of voter preferences. Losses come only from couplings the questions fail to cover: they vanish entirely under coverage and, on today's partition ballots, are bounded by the severed coupling mass. Contingent questions decide chain- and tree-structured coupling exactly at cost linear in the number of issues --- the cost of a faithful ballot is exponential only in the graph's treewidth, not in the size of its coupled blocks. Because the graph is latent, we estimate it from Polis-style agree/disagree votes and read the ballot off the estimate, provably exactly when the structure is clean. We show who pays when a budget forces a cut, and how ballots are attacked (duplicate-flooding the agenda; menu riders) and repaired. The pipeline is validated on synthetic electorates and real Polis conversations --- including vTaiwan's Uber deliberation, where the ballot recovered from votes alone matches, in outline, the agenda Taiwan ratified in 2016.

![The design space of a four-issue example]({{site.baseurl}}/images/ballot-design-space.png)

*The whole design space of a four-issue example: welfare forgone against ballot size, one point per ballot. The frontier steps down as each extra question "buys" one more respected coupling --- issue-by-issue severs everything and pays the most; the ballot matched to the preference-dependency graph reaches zero at a fraction of the full bundle's size.*

### Links

- **Paper (v2):** [zenodo.org/records/21409990](https://zenodo.org/records/21409990)
- **Code:** [github.com/act65/ballot-structure](https://github.com/act65/ballot-structure) --- every figure and number in the paper is reproducible from it
- **All versions:** [doi.org/10.5281/zenodo.20819571](https://doi.org/10.5281/zenodo.20819571)

Comments, counterexamples, and pointers to related work are very welcome.

```bibtex
@misc{telfar_2026_21409990,
  author       = {Telfar, Alexander},
  title        = {Ballot Structure from the Preference-Dependency Graph},
  month        = jul,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v2},
  doi          = {10.5281/zenodo.21409990},
  url          = {https://doi.org/10.5281/zenodo.21409990},
}
```
