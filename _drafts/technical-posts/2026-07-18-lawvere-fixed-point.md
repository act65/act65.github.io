---
layout: post
title: One Theorem to Break Them All
subtitle: Cantor, Russell, Gödel, Turing, Tarski — five impossibilities that are secretly a single diagonal argument
categories:
  - play
---

There are more real numbers than natural numbers. No program can decide whether an arbitrary program halts. No formal system rich enough to do arithmetic can prove all its own truths. "Truth" cannot be defined inside the language it's about. The set of all sets that don't contain themselves cannot exist.

These are five of the deepest facts in mathematics, from five different fields, proved across seventy years by Cantor, Russell, Gödel, Turing, and Tarski. And they are all — provably, not poetically — **the same theorem**. There is one argument. It has five costumes. Once you've seen the argument naked you can never un-see it, and every one of these results collapses into a single line about a single missing fixed point.

This is exactly the kind of thing I can't leave alone: five things that look unrelated turning out to be one thing. The unification is due to F. William Lawvere (1969), and the clearest exposition is Noson Yanofsky's (2003).

### The one move: diagonalisation

Every one of these proofs does the same two things.

**First, self-reference.** You arrange for a system to be able to talk about *itself* — for its objects to encode its own maps. Cantor lets a set index subsets of itself. Gödel numbers let arithmetic encode statements *about* arithmetic. A universal Turing machine is a program that takes programs as input. In each case there's an object rich enough to parametrise all the functions from itself to something — call that "the system can see its own diagonal."

**Second, negation.** You apply an operation that has *no fixed point* — something that always changes its input. Logical **NOT** (true↔false) is the workhorse: nothing equals its own negation. "Halts" flipped to "loops." "Is provable" flipped to "is not provable." "Is in the set" flipped to "is not in the set."

The whole trick is to run the diagonal *against* the negation — to build the object that says of itself the thing the negation forbids. And the punchline is always: **that object both must and cannot exist, so one of your assumptions was false.**

Lawvere's theorem states this once, abstractly, and it reads (in plain terms):

> If a system is rich enough to encode all of its own maps $A \to B$ using its own points $A$, then **every** map $g: B \to B$ has a fixed point.

Read the contrapositive and you have the universal weapon:

> If there is *any* operation $g: B \to B$ with **no** fixed point, then the system **cannot** encode all of its own maps $A \to B$. The self-reference you wanted is impossible.

That's it. That's Cantor, Russell, Gödel, Turing, and Tarski. Now watch them fall.

### The five costumes

**Cantor** — *no set surjects onto its own powerset.* Take $B = \{\text{true}, \text{false}\}$ and $g = \text{NOT}$, which has no fixed point. If a set $X$ could index all its subsets (all maps $X \to \{\text{t}, \text{f}\}$) by its own elements, Lawvere says NOT would need a fixed point. It doesn't. So $X$ can't — there are strictly more subsets than elements. Do it to the naturals and you've built the reals; do it forever and you get the infinite tower of infinities.

**Russell** — *no set of all sets.* The operation is again "not": the set of all sets that do **not** contain themselves. Ask whether it contains itself and you're asking NOT for a fixed point. It has none, so the universal set can't exist. The paradox that broke naïve set theory is the same missing fixed point.

**Turing** — *no general halting decider.* Suppose a program $H$ could decide, for any program, whether it halts. Build a program that asks $H$ about *itself* and then does the opposite — halts if $H$ says it loops, loops if $H$ says it halts. That "do the opposite" is the fixed-point-free negation; the self-application is the diagonal. The contradiction kills $H$. Undecidability is Cantor's diagonal wearing a computer.

**Gödel** — *arithmetic can't prove all its truths.* Gödel numbering is the self-reference (arithmetic encoding statements about arithmetic); the diagonal lemma builds a sentence $G$ that says *"$G$ is not provable."* Provability flipped by "not" is the fixed-point-free operation. $G$ can be neither provably true nor provably false without contradiction, so it's true-but-unprovable. Incompleteness is the halting problem in the language of number theory.

**Tarski** — *truth is undefinable.* The same construction with "provable" replaced by "true" gives "this sentence is false" — the Liar — and shows no language can contain its own truth predicate. The oldest paradox in philosophy is the youngest costume of the same theorem.

### The twist: the *same* theorem builds recursion

Here's the part that turns a party trick into something profound. Lawvere's theorem is an *if–then*: rich self-reference **implies** every operation has a fixed point. The impossibility results are what you get by running it in reverse — pick an operation with *no* fixed point (negation) and conclude the self-reference must fail.

But point it the other way. In a system where the self-reference genuinely *does* hold — like the untyped lambda calculus, the mathematics under every programming language — the theorem fires *forwards*: **every** operation has a fixed point, *including* the useful ones. That fixed point is the **Y combinator**, the device that makes recursion possible: a function can refer to itself, call itself, define itself in terms of itself.

So the very same structure that makes the Liar paradox, Gödel's ghost, and the halting problem is the structure that makes recursion, self-improvement, and a program that can read its own source. Self-reference is one capability with two faces: aimed at negation it detonates into paradox and impossibility; aimed at anything with a fixed point it becomes the engine of computation. The line between a system that can improve itself and a system that can destroy itself with a sentence is exactly the fixed point of the operation you hand it.

That's the whole of it. One diagonal, one missing fixed point, five impossibilities and the possibility of recursion itself — all the same theorem, just a question of what you feed it.
