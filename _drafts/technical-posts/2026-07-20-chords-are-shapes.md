---
title: Chords are shapes
subtitle: What an isomorphic keyboard makes visible about harmony
layout: post
categories:
  - play
---

On a piano, a C major chord and a D major chord feel like different animals: different
fingers, different black-and-white pattern, different shape under the hand. That is an
accident of the keyboard, not a fact about harmony. The twelve notes are symmetric —
every key sounds equally "in tune" with its neighbours — but the piano breaks that
symmetry by drawing seven keys white and five black.

![On a piano, C major and D major are different key-patterns]({{ site.baseurl }}/assets/hexboard-theory/piano-contrast.svg)

*C major is three white keys; D major reaches up to a black one. The same chord type, yet
nothing about the hand-shape survives the move.*

An **isomorphic** layout refuses to break it. Put the twelve notes on a hexagonal grid
so that *moving in a fixed direction always changes the pitch by a fixed interval*, and
harmony turns geometric. A chord stops being a fingering and becomes a **shape** — one
you can pick up and slide anywhere without distortion.

> The claim: on an isomorphic grid, a chord *type* is a translation-invariant shape,
> the major/minor duality is a half-turn, symmetric chords are regular figures, and the
> whole system of triads is a group you can see. I built a
> [playable hexboard]({{ site.baseurl }}/hexboard/) — everything below is a picture of
> something you can go and press.

## A chord is a shape

Here is the layout I'll use for most of this post, the **Wicki–Hayden** grid. Step
*right* and the pitch rises a whole tone (+2 semitones); step *up-and-right* and it rises
a perfect fifth (+7); step *up-and-left*, a perfect fourth (+5). Nothing else is needed —
those two directions generate the whole plane.

Because the mapping from position to pitch is the same everywhere, a chord's shape does
not depend on where you put it. A major triad is *this* little three-hex figure, full
stop:

![A major triad is the same shape at any root]({{ site.baseurl }}/assets/hexboard-theory/chord-is-a-shape.svg)

*The same shape at two roots — E major and B♭ major are congruent. Learn one voicing and
you have learned all twelve.*

This is the whole pedagogical pitch of isomorphic instruments: you memorise *shapes*, not
*keys*. A ii–V–I is one gesture you translate around the grid.

## Two diagonals: brightness and darkness

The two "up" diagonals are the interesting ones, because they are the perfect fifth and
the perfect fourth — the intervals harmony is actually built from.

![Fifths up-right, fourths up-left]({{ site.baseurl }}/assets/hexboard-theory/axes-fifths-fourths.svg)

*From any note, up-right stacks fifths (C→G→D→A…), up-left stacks fourths (C→F→B♭→E♭…).*

Jacob Collier likes to describe major and minor as a matter of *direction* — brightness
gained by moving sharpwards (through fifths) and lost by moving flatwards (through
fourths). On this grid that intuition is not a metaphor, it is an axis. And it pays off
immediately, because a **major scale is a straight line**. The seven notes of C major —
{% raw %}F C G D A E B{% endraw %} — are seven consecutive fifths, so they lie in a single
row along the up-right diagonal:

![The C major scale is seven consecutive fifths in a line]({{ site.baseurl }}/assets/hexboard-theory/scale-line.svg)

*Seven notes, one line. The "gaps" between the white-key patterns on a piano are an
artefact; the scale itself is perfectly regular.*

Now the modes fall out for free. A mode is just *where you slide the seven-note window*.
Push the line one fifth sharper and you get Lydian (the brightest mode); pull it flatward,
step by step, and you descend Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian,
losing one sharp — one notch of brightness — at each slide. Collier's brightness spectrum
*is* the position of a rigid line on the lattice.

## Progressions are journeys along the same line

Scales live on the fifths line — and so do chord *progressions*. The strongest move in
tonal harmony is a root falling a fifth; that fall is exactly what a V→I cadence is, and
chaining it gives the ii–V–I and the circle-of-fifths turnarounds under most songs. On the
grid, a fall of a fifth is one step down the up-right axis, so such a progression is a
straight walk home:

![A vi–ii–V–I turnaround walks down the fifths axis to the tonic]({{ site.baseurl }}/assets/hexboard-theory/progression-fifths.svg)

*A → D → G → C (vi–ii–V–I): each root a fifth below the last, arriving on the tonic (the
terracotta I). Keep going and you are simply walking the circle of fifths. A IV–V–I cadence
is the same fifth-fall into I, with one whole-tone step from IV up to V.*

And the shapes come along for free: each root carries the same little triad, translated one
notch down the line — so a whole progression is one shape sliding down a straight road.

## Neighbouring keys are neighbouring lines

The same picture measures how *related* two keys are. A key's seven notes are a seven-fifths
line; the next key round the circle is that same line slid one notch. So C major and G major
overlap in six of their seven notes — they differ only at the ends:

![C major and G major share six notes; only the ends differ]({{ site.baseurl }}/assets/hexboard-theory/key-distance.svg)

*C major = F + the shared six; G major = the shared six + F♯. Modulating up a fifth is
sliding the line by one. Keys a tritone apart are far-apart lines — which is exactly why
they sound distant.*

## Minor is major, turned upside down

If sharp/flat is a direction, what is major/minor? **A half-turn.**

This is the geometric content of *negative harmony* (Ernst Levy's idea, which Collier
popularised). In pitch, you flip each note to the note the same distance the *other* side
of the point halfway between the tonic and its dominant:
$x \mapsto (\text{tonic} + \text{dominant}) - x = 7 - x$ for C. The tonic and fifth swap
(C↔G), and the major third folds onto the minor third (E↔E♭), turning C major into C minor.

Here is the subtlety the grid makes honest. In one-dimensional pitch that flip is a
*reflection about a point*. Lifted onto the two-dimensional lattice it is **not** a mirror
across a line — the swapped pairs (C–G, E–E♭, …) run in *different directions*, so no
single line bisects them all. What actually realises it is a **180° rotation about a
centre** — the ⊕ below, sitting between E♭ and E. "Flipping the chord upside down" turns
out to be exactly that: a half-turn.

![C major turned 180° about the centre gives C minor]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony.svg)

*Every note sits diametrically opposite its partner through the ⊕ centre. C and G swap
across the shared edge; E turns over to E♭. The result is C minor.*

Because it is a genuine rotation of the shape, it turns *any* voicing over — an inversion
half-turns onto a re-voiced minor chord, about the very same centre:

![A first-inversion C major turned about the same centre]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony-inv.svg)

*Same ⊕, different voicing: C major in first inversion (E4–G4–C5) half-turns onto a
C-minor voicing (G3–C4–E♭4) — the highest note lands as the lowest.*

Apply the same half-turn to a whole progression and it turns harmonic *function* inside
out: the dominant and subdominant trade places, a perfect cadence becomes its negative.
But the atom is the picture above — the major/minor duality is one half-turn.

## One more relationship: the tritone sub

Two dominant chords a tritone apart share the same tritone — their 3rd and 7th, the notes
that actually create the pull to resolve. G7 and D♭7 both contain B and F, so either will
lean into C. That is the jazz **tritone substitution**, and on the grid it is two roots
hanging off one shared edge:

![G7 and D♭7 share the tritone B–F]({{ site.baseurl }}/assets/hexboard-theory/tritone-sub.svg)

*G and D♭ sit a tritone apart, but both reach the same B–F tritone. Swap one dominant for
the other and the guide tones do not move — only the bass drops a semitone.*

## Go press some hexes

Everything above lives on a single layout, Wicki–Hayden, where the two "up" diagonals are
the fifth and the fourth. But *which* intervals you assign to the directions is a free
choice, and a different choice exposes different structure. In a
[follow-up post]({{ site.baseurl }}/chords-are-triangles/) I swap to the **Tonnetz**,
where every triad becomes a little triangle — and symmetric chords turn into regular
figures, extended chords into staircases, and the whole system of 24 triads into a group
you can see.

But reading about a lattice is a poor substitute for leaning on it. The
[hexboard]({{ site.baseurl }}/hexboard/) lets you switch layouts, slide a chord shape
around, and hear that it really is the same chord everywhere. Try Wicki–Hayden for the
scales-as-lines above; the theory here is just a set of captions for what your hands will
find in about a minute.

*The diagrams were generated by
[`code/hexboard-theory/gen_diagrams.py`](https://github.com/act65/act65.github.io/blob/master/code/hexboard-theory/gen_diagrams.py).*
