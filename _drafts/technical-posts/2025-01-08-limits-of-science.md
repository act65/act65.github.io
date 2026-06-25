---
layout: post
title: "Three Kinds of Unknowable"
subtitle: "What the aleatoric/epistemic split looks like at the limits of science"
date: 2026-06-15
---

There is a tidy story machine-learning people tell about uncertainty. You split
it in two. *Aleatoric* uncertainty is the irreducible noise in the world — the
randomness you'd still face even with a perfect model. *Epistemic* uncertainty
is your own ignorance — the part that more data, or a better model, would melt
away. AU and EU. Noise and ignorance. It's a useful split, and most days I'm
happy to use it.

But it has a soft underbelly, and once you push on it the whole thing starts to
slide.

## The slide

Take a die. The textbook move is to call it aleatoric: a fair die is a uniform
random variable over `{1,...,6}`, and that's that. But of course a die is just a
chunk of plastic obeying Newtonian mechanics. Given the initial position,
velocity, spin, the table's restitution, the air — the outcome is *determined*.
The randomness isn't in the die; it's in my ignorance of the initial
conditions. So the die is epistemic after all.

Which is it? The honest answer is that it depends on what you allow yourself to
model and what you allow yourself to measure. Fix the hypothesis space to
"uniform distributions over six faces" and the uncertainty is aleatoric. Expand
it to "Newtonian rigid-body dynamics with measurable initial conditions" and the
very same uncertainty becomes epistemic. The split is a property of the *model*,
not of the die. It's relative, like velocity is relative to a reference frame.

And there's a direction to the relativity. Enrich your model — add variables,
condition on more — and uncertainty only ever flows *from* aleatoric *to*
epistemic. In information-theoretic terms, conditioning on more never raises
entropy: every covariate you add lowers the irreducible-noise floor and moves
that mass into the reducible-ignorance bucket. Run the argument to its end and
you reach a seductive conclusion:

> In the limit, all uncertainty is epistemic. There is no real noise floor —
> only knowledge we don't yet have.

This is the Laplace's-demon view, and it's where I want to start arguing,
because I think it's wrong — but wrong in an *interesting* way that tells you
something about the actual shape of the unknowable.

## Two premises doing the work

The slide to "it's all epistemic" smuggles in two assumptions.

**One: that the world is deterministic at the bottom.** That a perfectly
fine-grained deterministic model even *exists* to converge to. This is not a
settled fact — it's a bet on the interpretation of quantum mechanics. Standard
QM has irreducible, ontic randomness baked in. And Bell's theorem closes the
obvious escape hatch: you can't recover the missing determinism with *local*
hidden variables. So "all uncertainty is reducible in principle" is a
metaphysical wager, not a theorem.

**Two: that the fine-grained model is accessible.** Even granting determinism,
you have to be able to *acquire* the initial conditions and *run* the model.
Dice are chaotic; the measurement precision you'd need grows exponentially with
how far ahead you want to predict. There is a horizon past which the information
isn't merely expensive but physically out of reach.

Drop either premise and a genuine, irreducible floor survives. So the
interesting question isn't "is it all epistemic?" It's: **if we push the
hypothesis space all the way out to *anything formalizable*, and push the
accessible information all the way out to *anything physics permits us to
measure*, what is left over?**

That residue is the real limit of science. Let me try to enumerate it. The
surprise — at least it surprised me — is that it isn't one thing.

## A tour of the walls

I'll group the limits by *where they live*: in the world, in our access to it,
in our budget, in our logic, in our inferences, and in the awkward fact that
we're part of the system we're studying.

### In the world

This is aleatoric uncertainty in its purest form: cases where a probability
distribution really is the complete truth, with nothing hiding behind it.

- **Quantum measurement.** In standard QM, individual outcomes are
  irreducibly random — the wavefunction is the whole story. The crucial point,
  for our purposes, is Bell's theorem: you cannot reinterpret this as ordinary
  ignorance of some local hidden value. The noise is not standing in for a fact.
- **Heisenberg.** Conjugate quantities — position and momentum, energy and time
  — can't both be sharp. There is no joint value to be ignorant *of*; the
  fuzziness is in the state of affairs, not in your knowledge of it.
- **No-cloning.** You can't copy an unknown quantum state, which means you can't
  beat its noise by measuring many copies. The classic route out of aleatoric
  uncertainty — just repeat the experiment — is physically blocked.

### In our access

Here's where it gets subtle, and where the previous essay's point about
relativity comes back with physical teeth. These are facts that genuinely
*exist* but that no observer can ever reach. Call it **frozen epistemic
uncertainty**: there is a fact of the matter, it is simply locked away forever.

- **The cosmic event horizon.** Dark energy is accelerating the expansion of
  the universe. Galaxies beyond a certain distance are receding faster than
  light and will never send us another photon. Worse, the boundary is closing
  in: in comoving terms the observable universe is *shrinking*. The set of
  knowable things is monotonically decreasing. Information is leaving.
- **The last-scattering wall.** The universe was opaque to light until about
  380,000 years after the Big Bang. You cannot look earlier with telescopes —
  the cosmic microwave background is a literal wall. (In principle the neutrino
  or gravitational-wave backgrounds reach behind it; in practice, mostly not.)
- **The erased past.** The second law of thermodynamics throws away microscopic
  information as systems mix. The detailed past microstate genuinely existed,
  but it cannot be reconstructed from the present macrostate. Likewise whatever
  falls behind a black hole's horizon.

The philosophical status of this category is the most interesting thing in the
whole taxonomy. Probabilistically it is *indistinguishable* from aleatoric
uncertainty — you must put a distribution over it and you can never sharpen the
distribution. But *ontologically* it is epistemic: there was a value. This is
exactly the relativity from before, except now the access bound is set by physics
itself rather than by a modelling choice. Epistemic uncertainty, frozen by the
universe into something that behaves like noise.

### In our budget

Even where information is in principle accessible and determinate, *getting* it
costs resources, and the universe's resources are finite.

- **The holographic bound.** The information you can pack into a region of space
  is finite and scales with its surface area, not its volume. There is a maximum
  resolution to any physical description — which means the "anything
  formalizable" hypothesis space isn't actually unbounded.
- **Compute limits.** There are hard ceilings on how many operations a given
  amount of energy and time can perform (Bremermann, Margolus–Levitin). A finite
  universe heading toward heat death can only ever compute finitely much.
- **Landauer's principle.** Erasing a bit of information costs a minimum amount
  of energy. Measurement and the resetting of apparatus have an irreducible
  thermodynamic price. Knowledge is not free, even in principle.
- **Chaos and computational irreducibility.** Our die, made rigorous. To predict
  a chaotic system you need initial precision exponential in the prediction
  horizon. And some systems are computationally irreducible — there is no
  shortcut, the fastest way to find out what they do is to let them do it. The
  uncertainty is "reducible" only at a cost that diverges, which operationally
  is no different from a wall.

### In our logic

Our hypothesis space was "anything formalizable." Gödel tells us that set is
strictly smaller than "anything true" — and *this* is where the
aleatoric/epistemic frame quietly breaks.

- **Incompleteness.** Any sufficiently expressive consistent formal system
  contains true statements it cannot prove. These are unknowable from the
  inside — but they are not *random*, and they are not *ignorance* that data
  could fix. There is no distribution here at all. AU/EU has no coordinate for
  them.
- **Undecidability in physics.** This isn't just abstract logic. Whether a
  quantum many-body system has an energy gap above its ground state — the
  spectral gap problem — was shown to be *undecidable* (Cubitt, Pérez-García &
  Wolf, 2015). A perfectly well-posed physical question for which no algorithm
  can exist in general. Many prediction problems reduce to the halting problem.
- **Algorithmic randomness.** Chaitin's constant Ω is a perfectly well-defined
  number whose binary digits are incompressible and individually unprovable.
  Maximal randomness that is nonetheless a fixed mathematical object.

### In our inferences

Some limits show up even granting infinite, perfect data.

- **Non-identifiability.** Different parameter settings can produce *identical*
  observable distributions. No amount of data separates them — a flat direction
  in the likelihood that never resolves. This is permanent epistemic uncertainty
  that behaves, forever, like aleatoric.
- **Underdetermination.** Any finite set of observations is consistent with
  infinitely many theories (Duhem–Quine), and you can never test a hypothesis in
  isolation from its auxiliary assumptions.
- **The sample size of one.** We have a single universe and a single history.
  Any claim that some cosmological constant is "a draw from a distribution" is
  untestable — you cannot do statistics on an ensemble of size one. The anthropic
  puzzles all live here.

### In the mirror

Finally: the observer is *inside* the system. You can't measure the universe
from outside it. Measurement has back-action. And a system cannot contain a
complete and accurate model of itself — a physical cousin of Gödel's and
Turing's results (Breuer, 1995). Some of the unknowable is unknowable precisely
because you are made of the same stuff you are trying to know.

## The payoff: unknowable is not one thing

I started wanting to test the slogan *aleatoric = unknowable, epistemic =
whatever science can determine.* Walking the walls dissolves the left-hand side
into at least three genuinely different things:

1. **Irreducible randomness** (quantum). True aleatoric uncertainty: a
   distribution is the complete and final truth.
2. **Frozen epistemic uncertainty** (horizons, erased pasts, resource bounds,
   non-identifiability). Determinate facts, permanently locked away. They look
   exactly like noise from the inside, but there *is* a fact of the matter — you
   just can't have it.
3. **Undecidable truths** (Gödel, the spectral gap, Ω). Not noise and not
   ignorance. Well-posed truths that no formal procedure reaches. These don't
   live on the aleatoric/epistemic axis at all; they're off the plane.

And then the genuinely vertiginous part. For a given lump of residual
uncertainty, *deciding which of the three kinds it is* can itself be
unanswerable. Is the Born rule irreducible randomness, or our ignorance of a
deeper variable? Bell narrows the options but does not settle them; the answer
is interpretation-dependent and arguably beyond experiment. So the boundary
between aleatoric and epistemic, out at the limit of science, is not merely
*relative* — in places it is *formally undecidable*. You cannot always know
whether you've hit the noise floor of the world or merely a wall you might, in
some other frame, have seen past.

So I'd retire the clean dichotomy. The better picture, I think, is this: science
can chip away at epistemic uncertainty more or less indefinitely, but what
remains when it is done is not a single aleatoric floor. It is a *stratified*
unknowable — irreducibly random in one place, determinate-but-locked in another,
formally undecidable in a third — and the borders between those strata are
themselves, sometimes, among the things we cannot know.

---

*This grew out of a conversation about why the aleatoric/epistemic split in
machine-learning uncertainty quantification is a modelling choice rather than a
fact about the world. The short version: it's relative to your model — and at the
limit, even the relativity runs out.*
