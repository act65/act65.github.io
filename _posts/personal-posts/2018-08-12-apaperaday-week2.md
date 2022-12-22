---
title: "#Apaperaday. Week2"
date: "2018-08-12"
coverImage: "screenshot-2018-08-12-at-10-08-02-pm.png"
layout: post
---

![]({{site.baseurl}}/images/{{page.coverImage}})

https://twitter.com/telfarac/status/1026623209188122626

https://twitter.com/telfarac/status/1027120627335880704

https://twitter.com/telfarac/status/1027443517616869383

https://twitter.com/telfarac/status/1028071445165891584

https://twitter.com/telfarac/status/1028435977541283842

## [Structural rounding](https://arxiv.org/abs/1806.02771): Approximation algols for graphs near an algorithmically tractable class

> Specifically, if a problem Π has an approximation algorithm in structural class C, the problem and its solutions are “stable” under an edit operation, and there is an α-approximate algorithm for editing to C, then we get an approximation algorithm for solving Π on graphs γ-close to C.

Well, that pretty much sums the paper up... Ok, here are some questions/quotes/thoughts, in no particular order.

> ..., we hypothesize that most real-world networks are in fact small perturbations of graphs from a structural class

Well, that can be shown empirically.

Regardless, this is an I\\interesting way to frame generalisation. If we have existing knowledge, and we want  leverage that existing knowledge, a solution (what other alternatives are there?) is to map problems with unknown solutions into problems with known solutions. Ie "_when asked a question you don't know, answer a related, but different, question that you do know_". And then account of the different between then problems, the residual.

**Q:** If we increase the number of structural classes then does this make it easier to handle arbitrary graphs? Or are the structural classes used 'complete' (in what sense!?!?)?

> Formally, a graph is γ-close to a structural class C, where γ ∈ N, if some γ edits (e.g., vertex deletions, edge deletions, or edge contractions) bring the graph into class C.

Huh, that seems like an unusual definition? Why do we hot have the ability to add nodes or edges? This property seems to work quite nicely in a few of the proofs: because we know nodes (or edges) have only been removed it guarantees that a nodes neighborhood can either stay the same or decrease, thus a solution to (say) Independent Set is still valid.

I had to look up [bicriterion](https://cs.stackexchange.com/questions/26028/what-is-a-bicriteria-approximation-algorithm). Still not sure what it is all about.

> A graph property π is non-trivial if and only if infinitely many graphs satisfy π and infinitely many do not, and π is hereditary if G satisfying π implies that every induced subgraph of G satisfies π.

Hereditary seems like a hard constraint to satisfy. **Q:** What is an example of a property that is hereditary? Oh, max degree is. Any subgraph of a k-degree graph must have k-degree or less. Wait, nope. As it isn't inherited by all subgraphs? I am confused...

> Our framework supports arbitrary graph edit operations and both minimization and maximization problems, provided they jointly satisfy two properties: a combinatorial property called “stability” and an algorithmic property called “structural lifting”. Roughly, these properties bound the amount of change that OPT can undergo from each edit operation, but they are also parameterized to enable us to derive tighter bounds when the problem has additional structure. With the right definitions in place, the framework is simple: edit to the target class, apply an existing approximation algorithm, and lift.

Hmm, I am interested in this notion of stability. I have seem something like this appear in many proofs and am yet to really understand it.

![Screenshot 2018-08-12 at 10.05.28 PM.png]({{site.baseurl}}/images/screenshot-2018-08-12-at-10-05-28-pm.png)
