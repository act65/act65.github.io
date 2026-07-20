---
title: Chords are triangles
subtitle: A second map of harmony — the Tonnetz, symmetry, and the group behind the triads
layout: post
categories:
  - play
---

In an [earlier post]({{ site.baseurl }}/chords-are-shapes/) I put the twelve notes on
an isomorphic hex grid — the **Wicki–Hayden** layout — so that moving in a fixed direction
always changes the pitch by a fixed interval. Harmony turned geometric: a chord became a
translation-invariant **shape**, a scale became a straight line of fifths, and the
major/minor duality became a half-turn.

But *which* intervals you assign to the two directions is a free choice, and a different
choice exposes different structure. This post swaps to a second map — Euler's **Tonnetz** —
and follows it all the way down to the group theory underneath.

> If you have not read the first post, the one thing to carry over: on an isomorphic grid a
> chord *type* is a fixed shape you can slide anywhere. Here that shape becomes a triangle,
> and the moves between triangles turn out to *be* a mathematical group. There is a
> [playable hexboard]({{ site.baseurl }}/hexboard/) — everything below is a picture of
> something you can go and press.

## A second map: the Tonnetz

Swap to the **Tonnetz** — Euler's lattice from 1739 — chosen so that the three directions
are exactly the three intervals *inside* a triad: a **major third** one way, a **minor
third** another, a **perfect fifth** the third.

![The Tonnetz: the three directions are a triad's three intervals]({{ site.baseurl }}/assets/hexboard-theory/tonnetz-intro.svg)

*Watch the step sizes (top of each figure from here on): a rightward step is now a **major
third**, not the whole tone it was on Wicki–Hayden.* Because a major triad is root + major
third + fifth, and those live along three adjacent directions, **a triad becomes a little
triangle** — major triads pointing one way, minor triads the other. Several things now fall
out of the picture.

## Symmetric chords are regular figures

Some chords look the same no matter how you slide them. Stack a single interval over and
over, and if it divides the octave evenly you arrive back where you started — the chord is
*symmetric*, and transposing it by that interval maps it onto itself.

The **augmented** triad is three stacked major thirds — so on the Tonnetz it is a straight
line along the major-third direction, closing up after three steps (C E G♯ back to C):

![Augmented triad: stacked major thirds]({{ site.baseurl }}/assets/hexboard-theory/symmetric-aug.svg)

The **diminished-seventh** is four stacked minor thirds — a line that closes after four
(C E♭ G♭ A):

![Diminished seventh: stacked minor thirds]({{ site.baseurl }}/assets/hexboard-theory/symmetric-dim.svg)

Because they are built from one repeating step, transposing them just slides the figure
onto itself: there are only **four** distinct augmented triads and **three** distinct
diminished sevenths in all twelve keys. (This is exactly Messiaen's *modes of limited
transposition*, seen as translational symmetry of a shape.)

## Taller chords are longer stacks

Because thirds are unit steps here, building a chord by stacking thirds draws a staircase —
and the "tall" jazz chords are simply longer ones. Keep stacking above a C major triad and
you add the 7th, 9th, 11th and 13th in turn:

![7th, 9th, 11th, 13th extend the triad into a staircase of thirds]({{ site.baseurl }}/assets/hexboard-theory/extended-thirds.svg)

*C–E–G is the triad; each further step up the staircase adds the next odd extension. A 13th
chord is seven notes — the whole diatonic scale, re-stacked as thirds.*

## Triangles that flip: P, L, R

Neighbouring triangles share edges, and a shared edge is two notes held in common. The
three **neo-Riemannian** transforms — **P**arallel, **L**eading-tone, **R**elative — are
precisely the three ways to flip a triad-triangle across one of its edges, i.e. the three
ways to keep two notes and move the third by the smallest possible step:

![P, L, R as the three edge-flips of a triad-triangle]({{ site.baseurl }}/assets/hexboard-theory/tonnetz-plr.svg)

*C major flipped across its three edges: **P** (share C–G) gives C minor, **L** (share E–G)
gives E minor, **R** (share C–E) gives A minor. Each move changes exactly one note by a
step.*

Chain these flips and you walk the space of triads by minimal voice-leading. `P` then `L`,
repeated, cycles through a **hexatonic** system of six triads; `L` then `R` traces an
**octatonic** one. Chord progressions become paths on a surface (it closes up into a
torus).

## A key is a region

Zoom out from a single triad and a whole *key* is a compact patch of the Tonnetz: its seven
notes cluster together, and its diatonic chords are the little triangles tiling that patch.

![The seven notes of C major form a compact region]({{ site.baseurl }}/assets/hexboard-theory/key-region.svg)

*C major's seven notes, with the tonic triad picked out, sit in one small region. Modulating
to a near key nudges the region a little; a distant key moves it far — the same key-distance
the first post measured as sliding lines, now seen as area.*

## Let's get mathematical

All of this is one group acting on one set, made visible.

Take the 24 consonant triads — twelve major, twelve minor. Two different symmetry groups
act on them, and they act *transitively* (you can get from any triad to any other):

- the **T/I group** of the twelve pitch classes: transpositions $T_n$ and inversions
  $I_n$. It is the dihedral group $D_{12}$ of order 24 — the symmetry group of the
  regular 12-gon (the clock face of pitch classes).
- the **PLR group** generated by the three edge-flips. It too is a dihedral group of
  order 24, and it acts *simply transitively* — exactly one sequence of flips connects any
  two triads.

So the 24 triads are a
[torsor](https://en.wikipedia.org/wiki/Principal_homogeneous_space) for $D_{12}$: a copy
of the group with the identity rubbed out. And here is the punchline (Lewin; Hook): these
two $D_{12}$ actions are **dual** — each is the centraliser of the other inside the group
of all permutations of the 24 triads. Transposition/inversion moves triads "from the
outside" (relabel the notes); PLR moves them "from the inside" (voice-leading). They
commute, and together they pin the structure down completely.

$$ 24 = 12 \text{ keys} \times 2 \text{ qualities} = |D_{12}|. $$

None of this is new — it is Euler's *Tonnetz* (1739), Riemann's dualism, and the
neo-Riemannian theory of Lewin, Cohn and Hook. What the hexboard adds is only that you can
*see* the group elements as moves of a shape, and *hear* them under your fingers.

## Go press some hexes

Reading about a lattice is a poor substitute for leaning on it. The
[hexboard]({{ site.baseurl }}/hexboard/) lets you switch layouts (try the **Tonnetz
(Harmonic Table)** layout for the triangles above, and Wicki–Hayden for the
[scales-as-lines]({{ site.baseurl }}/chords-are-shapes/) of the first post), slide a
chord shape around, and hear that it really is the same chord everywhere. The theory here is
just a set of captions for what your hands will find in about a minute.

*The diagrams were generated by
[`code/hexboard-theory/gen_diagrams.py`](https://github.com/act65/act65.github.io/blob/master/code/hexboard-theory/gen_diagrams.py).*
