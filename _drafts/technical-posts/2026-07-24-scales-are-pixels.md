---
title: Scales are pixels
subtitle: Why seven notes, why twelve semitones — evenness, Euclid, and the comma
layout: post
categories:
  - play
---

Two earlier posts treated the major scale as a given and asked what it looks like on an
isomorphic grid: [a straight line of fifths]({{ site.baseurl }}/chords-are-shapes/), and
[a compact region of triangles]({{ site.baseurl }}/chords-are-triangles/). This one digs
a level deeper and asks why the scale is what it is at all. Why *seven* notes? Why pick
*these* seven of the twelve? And why does an octave have twelve semitones in the first
place?

The answers turn out to be geometric too — and oddly familiar: the major scale is what a
computer scientist would call a **rasterized line**, and what a drummer would call a
**bell pattern**.

## The fairest way to pick seven

Start with the choosing problem. Twelve pitch classes sit on a circle; you want seven of
them. If you cluster them (seven semitones in a row) you get mud — everything rubs
against its neighbour. The natural opposite is to *spread them out as evenly as seven
points can go on twelve slots*. Seven doesn't divide twelve, so perfect evenness is
impossible; do the best you can and something remarkable happens — up to rotation there
is exactly **one** answer, and it is the major scale:

![Spreading 7 of 12 as evenly as possible forces the major scale]({{ site.baseurl }}/assets/hexboard-theory/evenness-clock.svg)

*The most even 7-of-12. The gaps come out as five whole steps and two half steps — the
familiar **L L s L L L s** — with the two short gaps pushed as far from each other as
possible. And the five leftovers are themselves spread as evenly as five can go: the
black keys, a pentatonic. Remove the fairest seven and the remainder is the fairest
five.*

Music theorists call this property *maximal evenness* (Clough & Douthett proved the
uniqueness). It is why the scale's step pattern is so nearly-but-not-quite regular: it is
the closest a 7-note pattern can get to regular inside 12.

## A scale is a rhythm

Here is where it gets fun. "Distribute k things as evenly as possible among n slots" is
not a music problem — it's the problem **Euclid's algorithm** solves. Run it for 3 in 8
and you get the Cuban tresillo; 5 in 8, the cinquillo; Godfried Toussaint showed that
[one little algorithm generates a world atlas of rhythms](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf).
Run it for **7 in 12** and you get a classic 12-pulse West-African bell pattern — and
also, on the other axis, the major scale:

![E(7,12) as a bell rhythm and as the major scale — the same necklace]({{ site.baseurl }}/assets/hexboard-theory/euclid-pair.svg)

*The same necklace, worn two ways. Read the circle as twelve pulses of time and the seven
onsets are a bell pattern you can clap; read it as twelve pitch classes and they are C
major. The major scale **is** a Euclidean rhythm — in pitch instead of time.*

One structure, two ears. Whatever it is that makes maximally even patterns satisfying —
regular enough to predict, irregular enough to orient yourself by — rhythm and harmony
both found it.

## A scale is a pixelated line

The first post drew the major scale as a straight line — seven consecutive fifths along
one diagonal of the hexboard. Here is a second, stranger sense in which the scale is a
straight line. Climb an octave (12 semitones) in 7 equal steps and each step would be
12/7 ≈ 1.7 semitones — which doesn't exist. The scale has to approximate that ideal ramp
using whole numbers of semitones, taking steps of 2 where it can and 1 where it must:

![The major scale as the pixel-staircase of an ideal 12/7 line]({{ site.baseurl }}/assets/hexboard-theory/bresenham-line.svg)

*The dashed line is the ideal: perfectly even, slope 12/7. The staircase is the best
integer rendering of it — risers of 2, 2, 1, 2, 2, 2, 1. If you have ever seen a computer
draw a slanted line on square pixels (Bresenham's algorithm), this is that, exactly. The
major scale is the pixel art of an even ramp.*

Maximal evenness, the Euclidean rhythm, and the pixel staircase are three costumes on one
theorem: **LLsLLLs is the best integer approximation to perfect evenness.** The scale
isn't an arbitrary convention that children memorise; it's the forced answer to a
rounding problem.

## Why twelve? The spiral that doesn't close

All of the above took the twelve-slot circle for granted. But *twelve* is itself the
answer to a question. The engine of everything in these posts has been the fifth — stack
fifths and you generate new notes. So stack pure ones (frequency ratio 3:2) and watch
what happens. Each fifth is not quite 7/12 of an octave, so the walk never lands exactly
on a stack of octaves — after twelve fifths you arrive not at C but at B♯, a whisker
sharp of it:

![Twelve pure fifths overshoot seven octaves by the Pythagorean comma]({{ site.baseurl }}/assets/hexboard-theory/spiral-fifths.svg)

*Twelve pure fifths versus seven octaves: the famous circle is honestly a **spiral**, and
the miss — about a quarter of a semitone — is the **Pythagorean comma**. (The star the
hops trace is pretty, but the important thing is the seam at the top.)*

So why do 5-note, 7-note and 12-note scales keep turning up, across centuries and
cultures? Because those are exactly the stack lengths at which the spiral *nearly*
closes — each one the best approximation so far, each better than the last. Stop at 5
and the leftover gap is big (the pentatonic); at 7, smaller (the diatonic); at 12,
small enough that you can cheat: shave each fifth by a fiftieth of a semitone and the
spiral snaps shut into a circle. That cheat is **equal temperament**. (The next lengths
where the spiral nearly closes are 41 and 53 — theorists have built such systems, but
53 keys per octave asks a lot of a hand.)

## The grid is a temperament

Which lands on a confession about the hexboard itself. The grid's whole geometry assumed
that 12 fifths *equals* 7 octaves — that B♯ and C are the same button. On the grid,
walking four fifths up and two octaves down lands on the same hex as walking a major
third right; in pure tuning those two routes differ by yet another comma (the syntonic
one, the reason choirs drift). An isomorphic layout doesn't just display harmony — **it
quietly commits to a temperament**, gluing the spiral's loose ends together so that the
lattice closes into a torus.

The remarkable part is that the *commitment is adjustable*. Because the layout is
generated by just two intervals, you can retune those two intervals — flatten the fifth
toward meantone, or move to 19- or 31-tone equal temperament — and every fingering
pattern in these three posts survives unchanged: same scale-lines, same chord shapes,
same stamps ([Milne, Sethares & Plamondon call this *tuning
invariance*](https://sethares.engr.wisc.edu/paperspdf/InvariantFingering.pdf)). A piano
fingering is married to one tuning; a hexboard fingering is married only to the
*structure* — which is, after all, the isomorphic promise: learn the shape once, and it
holds everywhere. Even across tunings.

## Go press some hexes

The [hexboard]({{ site.baseurl }}/hexboard/) won't retune itself (yet), but everything
else above is under your fingers: play along a single row (every row is a whole-tone
scale — six notes, perfectly even) and hear the placeless shimmer that perfect evenness
buys; play the major scale and hear near-evenness give you a home; count L's and s's as your fingers climb. The scale stops being a list you memorised
and starts being what it always was — the best possible rounding of a line too smooth
for this world.

*The diagrams were generated by
[`code/hexboard-theory/gen_diagrams.py`](https://github.com/act65/act65.github.io/blob/master/code/hexboard-theory/gen_diagrams.py).*
