---
layout: post
title: Molecule generation
subtitle: Generating small molecules
permalink: molecule-generation
---

Structure elucidation is the problem of determining the structure of a molecule given some analytical data.
One way to frame this problem is as a constrained generation problem.
Where the data provides constraints on the structure of the molecule.

NMR data can tell us information about the CH3, CH2, CH, and C atoms in a molecule.

## Constrained molecule generation

Using the orderly enumeration algorithm, we can generate graphs.

Small molecules can be represented as graphs, where the nodes are atoms and the edges are bonds.
Thus we needed to support colored nodes with degree constraints and colored edges.

![](assets/graph_enum/c-2-h-2-O-1.png)
*For example, if we start with 2 carbons, 2 hydrogrens and an oxygen. We can ask to generate all possible unique molecules.*

![](assets/graph_enum/ch-2-ch2-2-O-2.png)
*I also added support for 