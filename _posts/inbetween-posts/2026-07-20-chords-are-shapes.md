---
title: Chords are shapes
subtitle: What an isomorphic keyboard makes visible about harmony
layout: post
categories:
  - play
description: "What an isomorphic keyboard makes visible about harmony. On a piano, C major and D major are played with different hand-shapes: a different mix of black..."
tags:
  - essay
  - music
  - mathematics
---

On a piano, C major and D major are played with different hand-shapes: a different mix of
black and white keys, different fingering. That is an accident of the keyboard, not a
fact about harmony. The twelve notes are symmetric — transposing a piece changes nothing
about its structure — but the piano breaks the symmetry by colouring seven keys white and
five black.

![On a piano, C major and D major are different key-patterns]({{ site.baseurl }}/assets/hexboard-theory/piano-contrast.svg)

*C major is three white keys; D major reaches up to a black one. Same chord type; nothing
about the hand-shape survives.*

An **isomorphic** layout keeps the symmetry: put the twelve notes on a hexagonal grid so
that *moving in a fixed direction always changes the pitch by a fixed interval*.
Transposition becomes translation. A chord stops being a fingering and becomes a
**shape** — the same shape at every root.

> The claim: on an isomorphic grid, a chord *type* is a translation-invariant shape, a
> scale is a straight line, a progression is a walk, and the major/minor duality is a
> half-turn. I built a [playable hexboard]({{ site.baseurl }}/hexboard/) — everything
> below is a picture of something you can press.

## A chord is a shape

The layout in this post is the **Wicki–Hayden** grid: one step *right* raises the pitch a
whole tone (+2 semitones), *up-right* a perfect fifth (+7), *up-left* a perfect fourth
(+5). Those two directions generate the whole plane.

The position→pitch map is the same everywhere, so a chord's shape does not depend on its
root. A major triad is one three-hex figure:

![A major triad is the same shape at any root]({{ site.baseurl }}/assets/hexboard-theory/chord-is-a-shape.svg)

*The same shape at two roots — E major and B♭ major are congruent. Learn one voicing,
learn all twelve.*

That is the pedagogical pitch of isomorphic instruments: you memorise *shapes*, not
*keys*. A ii–V–I is one gesture, translated around the grid.

## Two diagonals, one circle

The two "up" diagonals are the perfect fifth and the perfect fourth — the intervals
harmony is built from.

![Fifths up-right, fourths up-left]({{ site.baseurl }}/assets/hexboard-theory/axes-fifths-fourths.svg)

*From any note, up-right stacks fifths (C→G→D→A…), up-left stacks fourths (C→F→B♭→E♭…).*

The two diagonals are not independent ladders. A fourth is an inverted fifth — up a
fourth (C→F) is the same note-name as down a fifth — so both diagonals walk the same
sequence of twelve notes, in opposite directions. Twelve steps along either one visits
every note once and comes home. The closed loop is the **circle of fifths**:

![The circle of fifths, with C major as one seven-note arc]({{ site.baseurl }}/assets/hexboard-theory/circle-of-fifths.svg)

*One loop, two directions: clockwise is the grid's up-right diagonal, counter-clockwise
the up-left. Each clockwise step adds one sharp to the key signature (G major has one,
D major two, …) and each counter-clockwise step adds one flat — so I'll call the two
directions **sharpward** and **flatward** from here on. The fifths diagonal on the grid is
just this circle unrolled into a straight line.*

A **major scale is seven consecutive notes on the circle of fifths** — the highlighted
arc. C major = {% raw %}F C G D A E B{% endraw %}. And since the circle unrolls into the
grid's diagonal, a scale is a straight line:

![The C major scale is seven consecutive fifths in a line]({{ site.baseurl }}/assets/hexboard-theory/scale-line.svg)

*Seven notes, one line. The "gaps" between the white-key patterns on a piano are an
artefact; the scale itself is perfectly regular.*

Direction doesn't matter: seven steps flatward from C (C F B♭ E♭ A♭ D♭ G♭) is also a
major scale — D♭ major. Any seven-in-a-row works. Two separate questions are hiding here:

- **Which seven notes?** The *position of the window* on the circle. Sliding it sharpward
  or flatward changes key (C major → G major → …).
- **Which note is home?** The same seven notes {% raw %}F C G D A E B{% endraw %} played
  with C as home are C major; with A as home, A minor; with D as home, D dorian. The
  *tonic's position inside the window* picks the mode.

Brightness — Jacob Collier's term for this — is the second question. Fix the tonic and
slide the window sharpward one notch: Lydian, the brightest mode. Slide it flatward,
notch by notch: Ionian → Mixolydian → Dorian → Aeolian → Phrygian → Locrian, one sharp —
one notch of brightness — lost per slide. The brightness spectrum *is* the position of a
rigid line on the lattice, relative to home.

(That is the *relative* minor: A minor as a re-rooting of C major's line. The *parallel*
minor — C major versus C **minor** — is a different relationship; it gets its own section
below.)

The brightness axis also explains *chord quality*. A triad's root and fifth form a spine;
major and minor differ only in where the third sits:

![The major third leans sharpward of the root–fifth spine; the minor third flatward]({{ site.baseurl }}/assets/hexboard-theory/third-side.svg)

*Same spine, two thirds. The major third (E) sits two steps to the **right** of the root;
the minor third (E♭) two steps to the **left** of the fifth. And right/left here is the
sharp/flat divide in disguise: one step right is a whole tone, which is two consecutive
fifths (C→G→D), i.e. two clockwise notches round the circle — so rightward of the spine
is the sharp side, leftward the flat side. A chord is major or minor according to which
side its third leans; "bright chord" and "dark chord" are literal directions.*

## The pentatonic is a shorter line

If seven-in-a-row is a scale, what is five-in-a-row? Trim one note off each end of the C
major line:

![The major pentatonic is the scale-line with its two ends trimmed]({{ site.baseurl }}/assets/hexboard-theory/pentatonic-line.svg)

*C G D A E — the **major pentatonic**. The trimmed pair, F and B, is the scale's only
tritone (six semitones — the octave's dissonant halfway point). The pentatonic is the
major scale minus its single harshest interval, which is why nothing in it clashes.*

This is the geometry under "you can't play a wrong note on the black keys": the black
keys *are* a pentatonic. The five notes left over when C major's seven are removed —
F♯ C♯ G♯ D♯ A♯ — are five-in-a-row further along the same line (G♭ major pentatonic).
Remove a window; the complement is a window. Blues notes are the opposite move — notes
far *off* the segment. "Outside" playing is literally outside.

## Progressions walk the same line

The strongest root motion in tonal harmony is a fall of a fifth — on the grid, one step
down the up-right axis. A progression built by chaining fifth-falls is a straight walk to
the tonic:

![A vi–ii–V–I turnaround walks down the fifths axis to the tonic]({{ site.baseurl }}/assets/hexboard-theory/progression-fifths.svg)

*One colour per chord: Am (vi, gold) → Dm (ii, green) → G (V, blue) → C (I, terracotta),
each root a perfect fifth below the last, arriving home on the tonic. The split-coloured
hexes are the notes two neighbouring chords share — a common tone literally handed from
one chord to the next as the walk descends.*

Most named progressions in jazz and pop are pieces of this one walk:

- **V–I** (G → C) is the last step alone: the perfect cadence, the strongest single move
  in tonal music.
- **ii–V–I** (Dm7 → G7 → Cmaj7) is the last *two* steps — jazz's default cadence, the
  cell most standards are stitched from.
- **vi–ii–V–I** (Am → Dm → G → C) adds one more and is the classic **turnaround** that
  loops the band back to the top of the form.
- Keep extending backwards and you get the full **circle-of-fifths sequence**: tunes like
  *Autumn Leaves* and *Fly Me to the Moon* run six or seven fifth-falls in a row — their
  whole chord chart is one long slide down this diagonal.
- A **IV–V–I** cadence is the same fifth-fall into I, approached by one whole-tone step
  (one hex to the right) from IV up to V.

The turnaround needs only two stamps: the minor-triad shape (vi, ii) and the major-triad
shape (V, I), each pressing slid one notch down the line, overlapping the next on the
shared note.

Classical theory calls "repeat a pattern, transposed by a fixed interval" a **sequence**;
on this grid a sequence is rubber-stamping — one shape, one translation vector, pressed
repeatedly. The strongest case is the chain of applied dominants (ragtime turnarounds,
jazz cycles): each chord is the dominant of the next, so one dominant-seventh stamp
marches down the fifths axis until it lands home:

![A chain of applied dominants: one dom7 shape stamped down the fifths axis]({{ site.baseurl }}/assets/hexboard-theory/dominant-chain.svg)

*A7 (gold) → D7 (green) → G7 (blue) → C (terracotta): three pressings of the same
four-note stamp, one step down-left each time. As before, the split-coloured hexes are
the common tones each chord hands to the next. On a staff this is four different chords
to spell; here it is one gesture, repeated.*

## Neighbouring keys are neighbouring lines

A key's seven notes are a seven-fifths line; the next key round the circle is the same
line slid one notch. So C major and G major overlap in six of their seven notes:

![C major and G major share six notes; only the ends differ]({{ site.baseurl }}/assets/hexboard-theory/key-distance.svg)

*C major = F + the shared six; G major = the shared six + F♯. Modulating up a fifth is
sliding the line by one. Keys a tritone apart are far-apart lines — which is exactly why
they sound distant.*

The arithmetic is exact: slide the window by k fifths and the two keys share 7−k notes,
every k giving a different overlap. That perfectly graded family of distances is special
to the diatonic scale (a *deep scale*, in the jargon) — most seven-note sets don't
measure key distance this cleanly.

## Minor is major, turned upside down

If sharp/flat is a direction, what is major/minor? **A half-turn.**

This is the geometry of *negative harmony* (Ernst Levy's idea, popularised by Collier).
In pitch: flip each note to the note the same distance the *other* side of the point
midway between tonic and dominant,
$x \mapsto (\text{tonic} + \text{dominant}) - x = 7 - x$ for C. Tonic and fifth swap
(C↔G); the major third folds onto the minor third (E↔E♭); C major becomes C minor.

One subtlety, which the grid makes honest. In one-dimensional pitch that flip is a
*reflection about a point*. On the two-dimensional lattice it is **not** a mirror across
a line: the swapped pairs (C–G, E–E♭, …) run in different directions, so no single line
bisects them all. The map that realises it is a **180° rotation about a centre** — the ⊕
below, between E♭ and E. "Flipping the chord upside down" is literal: a half-turn.

![C major turned 180° about the centre gives C minor]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony.svg)

*Every note sits diametrically opposite its partner through the ⊕ centre. C and G swap
across the shared edge; E turns over to E♭. The result is C minor.*

Because it is a rotation, it acts on *any* voicing — an inversion half-turns onto a
re-voiced minor chord, about the same centre:

![A first-inversion C major turned about the same centre]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony-inv.svg)

*Same ⊕, different voicing: C major in first inversion (E4–G4–C5) half-turns onto a
C-minor voicing (G3–C4–E♭4) — the highest note lands as the lowest.*

Seventh chords sort into two classes under the half-turn. A **major-seventh** chord turns
over into another major-seventh — Cmaj7 onto A♭maj7:

![C maj7 half-turned about the same centre gives A♭ maj7]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony-maj7.svg)

*C maj7 (C E G B) and A♭ maj7 (A♭ C E♭ G) are point-reflections of each other, still
sharing C and G. The chord type survives the flip because a maj7 is a **palindrome** of
stacked thirds — major·minor·major reads the same upside down. (Minor sevenths are
palindromes too: minor·major·minor. And it works from any root — B maj7 half-turns onto
A maj7 the same way.)*

A **dominant seventh** is *not* a palindrome — major·minor·minor upside down is
minor·minor·major, a half-diminished chord. G7 turns over onto Dm7♭5:

![G7 half-turned about the same centre gives Dm7♭5]({{ site.baseurl }}/assets/hexboard-theory/negative-harmony-dom7.svg)

*G7 (G B D F) half-turns onto Dm7♭5 (D F A♭ C) — no common notes, one shape upside
down.* Those two chords are the V and ii of a minor-key ii–V. The half-turn sends
dominant function onto subdominant function — which is why negative harmony turns
perfect cadences plagal. (The dominant-seventh/half-diminished pair is also the example
of inversion-related chords in Tymoczko's
[*Science* paper](https://dmitri.mycpanel.princeton.edu/files/publications/science.pdf).)

Applied to a whole progression, the half-turn swaps dominant and subdominant function
throughout. The atom, though, is the pictures above: the major/minor duality is one
half-turn.

## The tritone sub

A **tritone** is three whole tones — six semitones, exactly half the octave. C major
contains exactly one: F–B, the pair the pentatonic trimmed away. It is the engine inside
a dominant chord: G7's third and seventh are B and F, each a semitone from a note of the
tonic triad — B below C (the leading tone, pulling up), F above E (pulling down). Resolve
both and the tritone collapses onto C and E. That squeeze is why V7 resolves to I.

Because the tritone is half the octave, two dominant chords a tritone apart contain the
*same* tritone: D♭7 spells D♭–F–A♭–C♭, and C♭ is B — so G7 and D♭7 share exactly the
pair (B, F) that does the pulling. Either resolves to C. That is the jazz **tritone
substitution**, and on the grid it is two roots hanging off one shared edge:

![G7 and D♭7 share the tritone B–F]({{ site.baseurl }}/assets/hexboard-theory/tritone-sub.svg)

*G and D♭ sit a tritone apart, but both reach the same B–F tritone. Swap one dominant for
the other and the guide tones do not move — only the bass drops a semitone.*

## Go press some hexes

Everything above lives on a single layout, Wicki–Hayden, where the two "up" diagonals are
the fifth and the fourth. But *which* intervals you assign to the directions is a free choice, and a different choice exposes different structure. 

<!-- In a [follow-up post]({{ site.baseurl }}/chords-are-triangles/) I swap to the **Tonnetz**, where every triad becomes a little triangle — and symmetric chords turn into regular figures, extended chords into staircases, and the whole system of 24 triads into a group you can see.  -->

<!-- And a [third post]({{ site.baseurl }}/scales-are-pixels/) digs under the
scale itself: why seven notes, why twelve semitones, and why the circle of fifths is secretly a spiral that doesn't quite close. -->

Have a go yourself. The
[hexboard]({{ site.baseurl }}/hexboard/) lets you switch layouts, slide a chord shape
around, and hear that it really is the same chord everywhere.
