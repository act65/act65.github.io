# Hexboard theory posts — researched ideas backlog

Synthesis of a three-way literature survey (2026-07-24): academic geometric music
theory (Tymoczko, Clough–Douthett, Toussaint, Balzano, Carey–Clampitt), the standard
theory curriculum (Open Music Theory, musictheory.net, Benson's *Music: A Mathematical
Offering*, jazz wiki), and isomorphic-instrument community lore (Lumatone, KOOP,
Shiverware, Striso, concertina/Hayden world, musicnotation.org).

Post 1 = "Chords are shapes" (Wicki–Hayden). Post 2 = "Chords are triangles" (Tonnetz).
Post 3 = "Scales are pixels" (drafted 2026-07-24).

STATUS: implemented in Post 1 — items 2, 3, 5 (deep-scale caption), 6, and one-off 23
(five-features nod in the outro). Implemented in Post 3 — items 8, 9, 10, 11
(light-touch: 41/53 mentioned), 12, plus "the grid is a temperament" framing.
CUT after user review (2026-08-01): items 1 (whole-tone rows / French sixth) and 4
(chromatic zigzag + jammer lore) — drafted as "The humble row" and "The long way
round", judged lacklustre, removed (SVGs wholetone-rows / french-sixth / chromatic-path
still exist in assets, unreferenced). Item 22's Tymoczko voice-leading-is-hand-distance
insight was moved out of Post 1 into the isokeys repo's IDEAS.md (layout-compression
future work) at the user's request; the Science-paper anchor in negative harmony stays.
Still open: 7 (mode-mixture windows), 13 (Shepard helix figure), 14 (two clocks/M7),
15–21, 24–26.

---

## A. Cheap wins that fit Post 1's existing narrative

1. **The humble row: whole-tone scales are literal rows.** Each WH row is one of the
   two whole-tone collections (Jankó 6-6 structure; Wicki's 1896 patent was a hex
   Jankó for bandoneon). Explains at a glance why the whole-tone scale has no tonic
   (perfect translational symmetry ⇒ no distinguished point) and why there are only
   two. Bonus in the same figure family: augmented triad = every-other-button in a
   row; tritone = 3 right; the **French sixth** (A♭ C D F♯ = {8,0,2,6}) lies in ONE
   row and is symmetric under 3-right translation — *it is its own tritone sub*,
   visible at a glance. Fits right after the tritone-sub section.
   Sources: en.wikipedia.org/wiki/Wicki–Hayden_note_layout, /Augmented_sixth_chord.

2. **Pentatonic = a shorter segment of the same line.** Major pentatonic = 5
   consecutive fifths (C G D A E) — a sub-segment of the 7-segment major scale. Its
   complement (the other 5-of-12 after removing a 7-window) is... also a pentatonic —
   the black keys. Complement of maximally-even is maximally-even (Clough–Douthett).
   Blues notes render as outlier dots far off the segment ("outside" color, literally
   outside). One diagram, fits right after scale-line.
   Sources: koopinstruments.com/information/wicki-hayden-scales-modes,
   en.wikipedia.org/wiki/Maximal_evenness.

3. **Major leans bright, minor leans flat.** A triad's root and fifth form a vertical
   spine; the only note that differs between major and minor is the third — and it
   sits on the *sharpward* side of the spine for major (E = 2 steps right of C), the
   *flatward* side for minor (E♭ = left). Chord quality is literally which side of
   the brightness axis the third falls on. Community mnemonic ("major chords build to
   the right of the root; minor to the left" — Lumatone docs) upgraded into the
   post's brightness story. One small figure in the diagonals section.
   Source: lumatone.io/playmodes.

4. **Sequences and dominant chains = rubber-stamping.** A harmonic sequence is
   "select shape, translate by fixed vector, repeat" — the concept the grid was born
   for. Descending-fifths sequence / chain of applied dominants (III7–VI7–II7–V7–I) =
   one dom7 shape stamped repeatedly one step down the fifths axis into the tonic.
   Extends the existing progressions section with one staircase figure.
   Sources: openmusictheory.github.io (Applied chords; sequences),
   musictheory.net (Circle Progressions).

5. **Deep-scale one-liner (caption upgrade, no new figure).** Sliding the 7-fifth
   window by k fifths leaves exactly 7−k common tones — common-tone count is monotone
   in circle-of-fifths distance, a property essentially unique to the diatonic set
   (Forte's "deep scale"; interval vector ⟨254361⟩ — verify before citing). One
   sentence under the key-distance figure.

6. **Chromatic = the long way round.** The layout's known "weakness" — semitones are
   long knight-moves — reframed as the point: the piano sorts notes by pitch
   (semitone neighbors, harmonic strangers adjacent); WH sorts by harmonic kinship
   (fifths/fourths adjacent, semitones far). Diatonic relationships are short
   vectors, chromatic ones long — the geometric reason chromatic harmony "sounds
   far". Draw the chromatic scale as the zigzag it is. Could close Post 1's diagonals
   section or open a mixture/chromaticism section.
   Sources: WH Wikipedia (criticism section), encyc.org mirror.

7. **Mode mixture = two windows, one tonic.** Parallel major/minor are 7-windows
   offset 3 steps flatward, pinned at the same tonic; borrowed chords (♭III ♭VI ♭VII
   iv ii°) are exactly the shapes falling in the flat-side extension. Complements the
   negative-harmony section (parallel minor two ways: slide the window vs half-turn
   the chord). Source: openmusictheory.github.io (Modal mixture).

## B. Bigger set pieces — probably a Post 3 ("scales" / "why 12 notes")

8. **The major scale is a Euclidean rhythm.** E(7,12) via Bjorklund/Euclid =
   maximally even 7-of-12 = the diatonic set; E(3,8) = tresillo etc. Killer figure:
   the bembé bell-pattern necklace and the major-scale pitch clock side by side —
   *the same picture*, one in time, one in log-frequency. Most shareable single
   image found. Source: Toussaint, cgm.cs.mcgill.ca/~godfried/publications/banff.pdf.

9. **The scale is a pixelated straight line (Bresenham).** Plot the ideal line of
   slope 7/12 on grid paper; the forced stair-steps are LLsLLLs. "The major scale is
   the pixel-art rendering of a perfectly even line." Ties the maximal-evenness story
   to the post's scale-= -line theme. Source: en.wikipedia.org/wiki/Maximal_evenness
   (Clough–Douthett floor formula).

10. **The line never closes: commas.** Walk 12 pure fifths and you overshoot 7
    octaves by the Pythagorean comma (~23.5¢); the circle of fifths is really a
    spiral, and the grid can show the seam that equal temperament glues shut.
    Quotienting the infinite lattice by the "comma vector" = choosing a temperament
    (Benson §6.8, Fokker periodicity blocks made physical). Syntonic comma variant:
    E reached as 2-right vs 4-fifths-minus-2-octaves — same button in 12-TET, ~21.5¢
    apart in just intonation; heat-map the grid's cents-error per tuning.
    Source: Benson *Music: A Mathematical Offering* ch. 5, §6.2–6.8.

11. **Why 5, 7, 12 (and then 19, 31)?** Carey–Clampitt well-formed scales: stack
    fifths and stop at 5, 7, 12 — the lengths where the set nearly closes (continued
    -fraction convergents of log₂(3/2)). Spiral-of-fifths figure that almost bites
    its tail. Explains why pentatonic/diatonic/chromatic recur across cultures.
    Source: en.wikipedia.org/wiki/Generated_collection; Carey & Clampitt 1989.

12. **Tuning invariance — the second invariance.** Milne/Sethares/Plamondon: on a
    fifth-generated layout the same finger-shapes stay valid across the syntonic
    continuum (12/19/31-TET, meantone) — transposition invariance across keys AND
    tuning invariance across temperaments. "Same scale shape, three tunings" figure.
    Source: sethares.engr.wisc.edu/paperspdf/InvariantFingering.pdf.

13. **Roll the grid up: Shepard's double helix.** Vertical = octave, rows = the two
    whole-tone scales; glue octave-equivalent cells and the WH grid becomes a
    cylinder — Shepard's (1982) double helix of whole-tone strands wound over the
    circle of fifths. The cleanest "the grid is secretly a torus" figure.
    Source: en.wikipedia.org/wiki/Pitch_space.

14. **Two clocks, same dots (M5/M7).** Chromatic circle and circle of fifths are the
    same 12 points wired as dodecagon vs {12/7} star; multiplication by 7 mod 12
    swaps semitone↔fifth while FIXING the whole tone (7·2≡2) — the algebraic reason
    the WH grid treats the two diagonals as one circle in two directions.
    Source: en.wikipedia.org/wiki/Multiplication_(music).

## C. Ideas for Post 2 (Tonnetz) or a jazz post

15. **All the famous lattices are one lattice (change of basis).** WH = basis {2,7},
    Tonnetz = {4,7} (≅{3,4}), Balzano thirds-torus = {3,4}, LinnStrument fourths =
    {1,5}. Any generating pair of Z₁₂ gives an isomorphic layout; the historical
    layouts are linear relabelings of each other. Balzano: Z₁₂ ≅ Z₃×Z₄, "12 = 3×4"
    (present as his argument, it's contested). Unifying punchline joining the two
    posts. Sources: Balzano CMJ 4(4) 1980; Pearce exposition.

16. **Coltrane changes march along a row.** M3 = 2-right, so Giant Steps' tonic
    cycle B–G–E♭ = every-other-button, three strides = octave; ii–V connectors move
    along the fifths diagonal ⇒ the tune is an axis-alternating zigzag you can draw.
    (M3 is a single step on the Tonnetz, so maybe Post 2.) Source:
    en.wikipedia.org/wiki/Coltrane_changes.

17. **Chromatic mediants = nearest same-quality translates.** Same triad shape
    translated one M3/m3 vector; overlap = the common tone. "Distant yet smooth"
    becomes: far on the fifths axis, near on the thirds axis. Film-score chord
    pairs (C→A♭) as two overlapping shapes. Source: en.wikipedia.org/wiki/Chromatic_mediant.

18. **Dim7 tiling / coloring schemes.** Color the 12 pcs by dim7 membership → the
    grid tiles into 3 interleaved sublattices (4-4-4); by aug membership → 4
    sublattices (3-3-3-3). These are actual community coloring schemes for WH boards
    (plus 7-5 piano-ish and 6-6 whole-tone). Could ALSO ship as app color schemes.
    One dim7 shape sits equidistant from 4 tonics = the enharmonic-modulation
    teleporter. Sources: encyc.org WH mirror; musicnotation.org.

19. **Upper structures = shape + offset table.** Fix the dom7 shell (tritone = 3
    right), hover the familiar major-triad shape at each usable offset: D/C7 = 13♯11,
    E♭/C7 = 7♯9, G♭/C7 = 7♭9♯11. Replaces voicing charts with one shape and a
    vector table. Source: en.wikipedia.org/wiki/Upper_structure.

20. **Pop-loop field guide.** Doo-wop I–vi–IV–V, 12-bar blues, lament bass as small
    closed polygons on the grid — a comparative gallery of famous loops.
    Source: openmusictheory.github.io (pop/rock harmony).

21. **Neapolitan ♭II.** Parked 5 flatward of the tonic, resolving with the longest
    single jump in tonal syntax (6 fifths to V). Good drama, one figure.
    Source: musictheory.net (Neapolitan unit).

## D. Framing / sidebar material

22. **Voice-leading distance ≈ hand distance.** Tymoczko (Science 2006): efficient
    voice leading exists because triads/sevenths are nearly even; on an isomorphic
    layout voice-leading size is literal hand displacement — functional progressions
    are short arrows. His own inversional-symmetry example is the post's G7↔Dm7♭5
    pair (academic anchor for the negative-harmony section). Also: the piano's
    consonance-adjacency is inverted on WH — neighbors are consonant, so "wrong
    notes are consonant" (community "jammer" lore). Possible neighborhood-consonance
    heat-map figure. Source: dmitri.mycpanel.princeton.edu/files/publications/science.pdf.

23. **Tymoczko's five features of tonality as a closing frame.** Conjunct motion =
    short arrows; harmonic consistency = translation-invariant shapes; limited
    macroharmony = the 7-window; centricity = a marked home cell. The post's
    pictures ARE the five features — name them and cite.

24. **History sidebar.** Jankó 1882 → Wicki 1896 (bandoneon) → Hayden 1986
    (concertina, independent reinvention) → Thummer/jammers → Lumatone/HexBoard.
    46-button Hayden concertinas famously omit a left-hand B♭; big models add
    wraparound duplicate columns because distant keys are literally distant.
    Source: people.well.com/user/jax/rcfb/hayden_duet.html; WH Wikipedia.

25. **Reading-rules caveat.** Eye-tracking work (Besada et al. 2024) shows novices
    read lattice diagrams as shapes, not pitch content — teach the reading rules
    explicitly (the post's step-legends already do this; keep them).
    Source: journals.sagepub.com/doi/10.1177/20592043241246515.

26. **Scale = two-row block.** The WH octave is FGAB stacked over CDE (3+4
    parallelogram); playing a scale is a two-row zigzag. Companion view to
    "scale = line of fifths" — same set, two projections. Also: I–IV–V roots form
    the same compact triangle as a sus4 chord ("one shape, two zoom levels" —
    Shiverware). Sources: encyc.org WH mirror; shiverware.com/musixpro/wicki/chords.html.
