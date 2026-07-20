---
layout: post
title: Hearing Through the Hiss
subtitle: Stochastic resonance — when adding noise to a system lets you detect a signal you otherwise couldn't
categories:
  - play
---

Everything you know about noise says it is the enemy of signal. Noise is what you filter out, average away, shield against; it's the static that buries the message. So here is a fact that should feel wrong: for a large class of systems, adding a carefully chosen amount of noise makes a weak signal **more** detectable, not less. Turn the randomness up from zero and the signal *appears*. Turn it up too far and it drowns. Somewhere in between is a sweet spot — a *resonance* — where the noise is doing you a favour.

This is stochastic resonance, and once you see the mechanism it stops being paradoxical and becomes almost obvious. But it rearranges how you think about noise, so it's worth doing slowly.

### The mechanism: a threshold you can't reach

The key ingredient is a **threshold**. Consider a detector that only registers when its input crosses some level — it fires, or it doesn't. A neuron is like this. So is any sensor with a trigger point.

Now feed it a weak periodic signal — a gentle sine wave — that is *entirely below* the threshold. It never crosses. The detector sits silent. The signal is there, carrying real information, and the detector is blind to it, forever. No amount of patience helps: sub-threshold means invisible.

Now add noise on top of the signal. On its own the noise is just random jitter. But *added to the signal*, the combined jitter-plus-wave will occasionally poke above the threshold — and here's the whole trick: **it pokes above more often when the signal is near its peak** than when the signal is in its trough, because up there it needs less of a lucky noise spike to get over the line. So the *times* at which the detector fires become correlated with the signal. The crossings cluster at the crests. Collect enough of them and the hidden sine wave reappears in the *statistics of the firing times*, even though no single crossing was "the signal."

The noise didn't add information. It acted as a ladder, lifting a sub-threshold signal over the wall in a signal-correlated way, converting something the detector couldn't see into a pattern of events it can.

### Why there's a sweet spot

This immediately explains the resonance — the fact that there's an *optimal* noise level, not just "more is better":

- **Too little noise:** the combined signal still rarely clears the threshold. Few crossings, little information. (At exactly zero noise, back to silence.)
- **Too much noise:** the detector fires constantly, at crests *and* troughs alike, and the firing times become as random as the noise. The signal-correlation drowns.
- **Just right:** enough noise to get the crests over the wall, not so much that the troughs get over too. The mutual information between signal and output **peaks at an intermediate noise level**.

That non-monotonic curve — detection rising, peaking, then falling as you add noise — is the fingerprint of stochastic resonance, and it's genuinely counterintuitive the first time you plot it.

### Where the universe uses it

This isn't a curiosity; it's load-bearing in real systems, several of which sit right in the middle of things I care about:

- **Neurons.** Sensory neurons are threshold devices, and the nervous system is *noisy* — and it turns out that noise helps. Paddlefish and crayfish detect the faint electric fields of prey better in the presence of ambient noise; experiments show a resonance peak. Sub-threshold stimuli become detectable *because* the neural hardware is noisy.
- **Medicine.** Noise-enhanced balance: vibrating insoles that add random mechanical noise to the soles of the feet measurably improve balance in the elderly and in patients with neuropathy — the weak pressure signals from the skin get lifted over threshold. Similar ideas appear in cochlear-implant coding.
- **Climate.** The idea was *introduced* (Benzi, Sutera, Vulpiani, 1981) to explain the roughly 100,000-year rhythm of the ice ages: the astronomical (Milankovitch) forcing is too weak on its own to flip the climate between glacial and interglacial states, but weak periodic forcing *plus* climate noise can produce regular switching — stochastic resonance at planetary scale.
- **Engineering.** It's the respectable cousin of [dithering]({{ site.baseurl }}): deliberately injecting noise before quantisation to pull detail out from under the bit-depth.

### The honest caveats

Two, and they matter for keeping this from sounding like magic. First, stochastic resonance is a **nonlinear** phenomenon — it needs that threshold, or some other nonlinearity. In a purely linear system, noise just adds to noise and never helps; you can't dither your way to a free lunch in a straight line. Second, and relatedly, the noise is **not creating information** out of nothing — that would violate the data-processing story from ["garbage in, garbage out"]({{ site.baseurl }}). The information was always in the sub-threshold signal; the noise merely *re-encodes* it into a form the nonlinear detector can register. What peaks at the optimal noise level is how much of the already-present signal makes it *through the nonlinearity*, not the signal itself.

### The reframe

Which is the thing I like about it. We treat noise as pure subtraction — something that can only ever destroy. Stochastic resonance says that in a world full of thresholds, noise is also what carries the faint things across. The predator's whisper of an electric field, the planet's weak astronomical nudge, the pressure of the ground on a numb foot — some signals are too quiet to be heard in a perfectly quiet system, and are audible only because the world is noisy enough to lift them over the edge. Sometimes the static *is* the reason you can hear.
