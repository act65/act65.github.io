---
title: Intelligent Immunity
layout: post
subtitle: What if intelligence evolved within the immune system?
categories:
    - play
---

## I. The immune system is already an information system

Like the nervous system, the immune system runs its own transport infrastructure through the body — lymphatic vessels, the bloodstream, chemical gradients, migrating cells, and nodes where information converges for processing. It is a distributed computational network, nearly as intricate as the brain, with learning, memory, and online adaptation of its own. It simply didn't turn into a general-purpose intelligence.

Why not — and what would it look like if it had? The question factors into four:

1. What computational capabilities does an intelligent agent need?
2. What physical budgets does every biological implementation pay?
3. What environmental pressures select for which implementation, and in what order?
4. How does that path shape the *flavour* of the resulting intelligence?

## II. What an intelligent agent needs

Strip it to the minimum. Any learning agent has to:

- **Sense** — extract relevant features from a high-dimensional environment.
- **Remember** — persist useful information across time, against a substrate that's always turning over.
- **Generalise** — apply learned patterns to novel input.
- **Predict** — build forward models good enough to act on.
- **Act** — influence the world and close the loop.
- **Model itself** — separate self from environment, so the first five don't get confused.

Everything else is plumbing. The interesting design questions sit at each of these six points: what's the mechanism, and what does it cost?

## III. The three budgets every biological design pays

Every living system is priced against the same three budgets — **energy, time, and space** — and the two substrates pay them very differently. The idea of pricing biological designs in common currencies is broader than any one treatment; Sterling & Laughlin's *Principles of Neural Design* is the clearest worked example for the nervous system[^sterling].

**Energy.** Every signal sent, bit stored, and molecule synthesised costs ATP. An organism's information budget is capped by its metabolic budget, so the unit that matters is bits per joule. The human brain is ~2% of body mass but burns ~20% of basal metabolism, most of it on the Na⁺/K⁺ ATPases that restore ion gradients after every action potential[^attwell]. The immune system pays differently: synthesising a cytokine or antibody is expensive once, but the molecule then amortises across every cell that binds it. One system pays per message *delivered*; the other pays per message *type*. If you need a high rate of one-off messages, dedicated wiring is cheaper per bit. If your useful messages repeat and spread across many receivers, broadcast is cheaper.

**Time.** A predator's strike takes a few hundred milliseconds; dodging it demands signalling on tens of milliseconds. A bacterial infection takes hours to days to become dangerous; an antibody response that matures over a week is still fast enough. The signalling infrastructure has to match the timescale of the decisions it supports — otherwise you pay for speed you can't use, or you're too slow for the threats you face.

**Space.** Bodies have finite volume, and wires take up volume. The scaling limit on brains isn't cells but wiring: long-range axons compete with everything else in the skull, which is why connectomes evolved to minimise wire length and why mammalian cortex folds to pack more surface area into a constrained volume. Immune systems don't face this limit. Messages are molecules moving through fluid; "connections" exist only as long as two cells are in contact. The space cost is instead the volume to house and turn over a diverse lymphocyte repertoire (~10¹² cells in an adult) distributed through lymph nodes, spleen, and bone marrow — a cost that doesn't compound with the size or complexity of the receiver pool.

These three budgets are the substrate-level grammar. What an organism actually evolves depends on which environmental pressures make each capability worth paying for.

## IV. Each capability under pressure

For each capability: the pressure, the physics constraint it imposes, and the mechanism that's the only thing left standing once the constraint is taken seriously.

### Sensing

*Pressure.* Organisms have to detect features of their environment. What the environment offers — and what it requires — splits the problem in two:

- **Predator-prey life** runs on mechanical and optical features. A moving target's image translates across the retina at degrees per millisecond, a footfall is a pressure transient tens of milliseconds long, a fly's wingbeat is sub-millisecond. Detect-to-act has to clear in tens of ms — which means signals have to cross body-scale distances (cm) in single-digit ms. The input space is small: a handful of photoreceptor classes, a few mechanoreceptor types, are enough to cover the relevant physics.
- **Pathogen/chemical life** runs on molecular shapes in extracellular fluid. No speed budget — molecules diffuse on their own slow clock — but the *input space is combinatorial*: thousands to millions of distinct biologically relevant shapes, most never seen by any individual. With ~2×10⁴ genes in the genome, a fixed sensor per shape isn't possible.

The two pressures pick out incompatible physics. Take them in turn.

*Neural — the speed pressure rules diffusion out, leaving membrane-bound electrical signalling as the only option.* At cm scale, diffusion takes hours (§III). So whatever carries the sensory signal cannot be diffusion. The cell has access to one fast intracellular medium: ion conductance across the membrane, which propagates on millisecond timescales. The job of a neural sensor is therefore to *transduce an external physical quantity into a change in ion conductance, as fast as possible.* The mechanisms are exactly what you'd build under that constraint: rhodopsin's conformational change on photon absorption directly gates ion flow within microseconds; mechanosensitive channels open under membrane tension in microseconds; G-protein-coupled odorant receptors couple binding to ion-channel state in milliseconds. Each is a protein machine optimised for *fast coupling of an external signal to the membrane's electrical state*, because that's the only intracellular currency the rest of the body can read on the required timebase. Downstream stages — local-contrast detectors in retinal ganglion cells, oriented-edge detectors in V1 — re-encode the same fast signal through further conformational machinery, each stage priced against the action-potential budget. The whole architecture is a chain of fast transductions because the predator hasn't waited.

*Immune — speed isn't a constraint, but combinatorial breadth is, which rules a neural approach out and forces shape-discriminative binding.* Trying to detect molecular shapes the neural way fails on two fronts. First, you'd need a dedicated receptor protein per shape — but the input space is 10⁶+ and the genome is 10⁴. Second, even if you could encode them, you'd need each detector hardwired to a central processor through a dedicated axon, multiplied across every site in the body where the molecule might appear. Volumetrically impossible; metabolically catastrophic. So neural physics is excluded by the budgets. What remains is the cheapest readout that discriminates 3D shape directly: binding affinity. A lymphocyte's surface receptor has a 3D pocket; the non-covalent forces between pocket and antigen — hydrogen bonding, hydrophobic packing, electrostatics, shape complementarity — sum to a dissociation constant; the cell uses bound-vs-not-bound as a one-bit output. No transduction step (the input is already in the molecular currency), no dedicated wire, no pre-anticipation of which shapes will arrive.

That last constraint — pre-anticipation is impossible — forces the random repertoire. The genome cannot encode each receptor; instead, during lymphocyte development the receptor-coding gene is physically rearranged, segments cut and religated to generate a unique receptor per cell, ~10⁹ shapes per individual[^vdj]. Most receptors never encounter a matching antigen, but for any incoming shape the chance of *some* cell binding it is high. The ML analogue is random feature methods: a fixed random projection of input space, with downstream "learning" happening through selection on which projections turn out useful, not through smooth updates to the projection itself.

The two substrates are answers to disjoint constraints. Trying to use one for the other's job breaks the physics: a neural shape-detector array is volumetrically impossible, and a diffusion-based predator-escape system is too slow by orders of magnitude.

### Memory

*Pressure.* Memory bridges time. What kind of bridging the rest of the system needs is what selects the mechanism, and the two systems need very different things.

Neural memory has to support behaviour-on-the-fly:

- **Retrieval has to be fast** — single-digit ms — because the live signal and the retrieved one share a circuit, so the latter must be available within the same processing window.
- **Generalisation across similar inputs is essential.** A predator pattern from yesterday has to fire on something like-but-not-identical today. Approximate similarity search, not exact match.
- **Writes are continuous and online**, in flight with the live signal — no separate training phase.
- **Capacity has to scale with experience** without adding cells.

Immune memory has to support pathogen recognition years later:

- **Retrieval can be slow** (hours to mount an antibody response is fine — the threat plays out over days).
- **Exact-match is sufficient.** Each pathogen is its own clone; no blending needed.
- **Writes are batched** through germinal-centre rounds.
- **Persistence has to extend across decades** — longer than any protein, longer than most cell lineages.

*Neural — the fast-retrieval-with-similarity requirement rules out any "stored elsewhere, fetch on cue" scheme, leaving the memory as a property of the live circuit itself.* If retrieval has to land within the live circuit's own ms-scale processing window, the memory cannot be stored at a separate address and read out — the round-trip cost wouldn't fit. The only physics that meets the constraint is one where the memory *changes how the live circuit responds to inputs.* Synaptic strength does this directly: modify the gain on existing connections and the circuit's response to a given input changes, with no retrieval step. Distributing memory across many synapses (rather than one synapse per memory) buys two more required properties at once — capacity quadratic in cell count, and similarity search for free, because similar inputs activate overlapping subsets of the same synapses. The biochemical implementation — AMPA receptor abundance gated by NMDA-receptor Ca²⁺ influx, with CaMKII autophosphorylation locking in the change — is the chemistry that realises the abstract requirement: local, activity-dependent, continuously writable, read-by-default. The metabolic cost is the price of holding the potentiated state actively, and the corollary is that unused memory fades. For online behaviour, fading is a feature: the statistics of the world shift on the same timescale.

*Immune — the decades-long persistence requirement rules out active maintenance, leaving DNA as the only medium and cells as the unit of memory.* Holding information actively for fifty years compounds the metabolic cost at every site, every day. No active-state biochemistry can be afforded over that horizon. The only molecular form that lasts effectively indefinitely without active rewriting is DNA, which forces memory to live in DNA, which forces the unit of memory to be a cell carrying that DNA. The cell can then be replicated to replace losses, indefinitely, at the per-cell cost of slow homeostatic cytokine support (IL-7, IL-15). Yellow-fever-specific T cells have been detected 50+ years after a single vaccination[^yellowfever]. Generalisation across similar inputs isn't required (each clone is a separate sufficient memory), and retrieval latency isn't required (the response unfolds over days anyway), so the substrate doesn't have to provide them — and doesn't.

The two strategies are matched, point-for-point, to what each system actually needs. Trying to use immune-style memory for behaviour gives you exact-match recall on hour-long latencies; trying to use neural-style memory for fifty-year pathogen recognition exceeds any plausible metabolic budget.

### Generalisation and adaptation

*Pressure.* The world produces variants — new pathogen strains, new predator tactics, new versions of familiar inputs. To improve with experience, the system must update *something* in response to outcomes, which is the credit-assignment problem: which parts to change to do better next time. Two physics questions decide the answer:

- **Is the unit of change individually addressable?** If yes, hill-climb in parameter space. If no, hill-climb in population space — keep good copies, drop bad ones.
- **Can an error signal physically reach the unit of change?** If the system is wired, yes; if not, only an indirect proxy (binding success, survival) can play the role.

*Neural — wires already exist for signalling (§Signalling), so plasticity along those wires is essentially free.* Once the connectivity infrastructure is paid for, modifying connection gain costs almost nothing extra: the synapse is already there, just change its weight. The local rule is roughly Hebbian — coincident pre- and post-synaptic activity, sensed through NMDA-receptor Ca²⁺ influx, drives strengthening or weakening — and turning this local rule into *global* credit assignment requires error information to reach the synapses that need updating. The wire infrastructure makes that possible: candidate mechanisms include neuromodulatory broadcasts (dopamine, acetylcholine) gating whether local changes consolidate, feedback connections carrying local approximations to error gradients, and energy-based schemes like equilibrium propagation in which the network's settling dynamics implicitly encode a gradient. All of these are *only available because the network is connected* — they're consequences of the same infrastructure that solved signalling.

*Immune — no wires, so an error signal has nothing to travel along, forcing the unit of change to be the whole cell with credit assigned via differential reproduction.* If two cells need to compare receptor quality, they can't exchange a comparison signal directly. The substitute is competition for a shared limiting resource: antigen displayed by follicular dendritic cells. When a B cell is activated, it enters a germinal centre; its receptor gene mutates at ~10⁶× the genomic background rate[^shm]; daughter cells with different mutated receptors compete for limited antigen; higher-affinity binders capture more, receive stronger survival signals, divide more. Over days, binding affinity climbs by two or three orders of magnitude. This is clonal selection[^burnet] — hill-climbing in receptor-sequence space, implemented as differential reproduction because the substrate cannot deliver a per-parameter update.

The pattern is the same in both cases: the credit-assignment algorithm follows from whether wires exist. Where they do, plasticity lives in the wires. Where they don't, plasticity lives in populations.

### Signalling

*Pressure.* Information has to move from sensors to effectors and between distant cells. Speed × distance × cost together set the budget, and the budget itself comes from the pressures on sensing and action:

- Predator-prey life needs cm-in-ms latency. Fick's law (§III) excludes diffusion at that scale — a 1 mm diffusion path takes hours.
- Pathogen response unfolds over hours to days. The rate-limiting steps elsewhere (cell recruitment, protein synthesis, division) are themselves slow, so any signalling faster than seconds buys nothing the rest of the response can use.

*Neural — diffusion is too slow at body scale, leaving active propagation along a dedicated medium as the only physics that delivers the latency.* The chosen medium is the membrane, threaded with voltage-gated Na⁺ and K⁺ channels. A local depolarisation opens Na⁺ channels; influx further depolarises; a self-propagating wavefront — the action potential — travels at 0.5–120 m/s, set by axon diameter and myelination. The metabolic price for that speed is paid afterward by Na⁺/K⁺ ATPases pumping ions back to restore the gradient (~10⁻¹⁰ J per spike), and upfront by the volume cost of the axon itself. The whole infrastructure exists *because* nothing cheaper meets the latency requirement.

*Immune — the latency requirement is slack, so paying for active propagation would be wasted ATP, leaving free diffusion as the cheapest medium that suffices.* For a small protein with *D* ≈ 10⁻⁶ cm²/s, Fick's law gives characteristic time *d²/(2D)*: ~10 μm in a second, ~1 mm in hours, ~1 cm in days[^diffusion]. Bulk transport via the circulatory system (~cm/s) and active cell migration (~10 μm/min in tissue) extend the effective range, keeping round-trip latencies in the seconds-to-hours band — well within the response's own time constants. Reception requires only that a target cell express the matching receptor: no dedicated channel, no pre-existing connection. The infrastructure cost is near zero, and the vocabulary is large for free — each cytokine species is its own "word," with the body using dozens.

Each substrate is the cheapest physics that meets its latency bar. A neural-style wired system for immune signalling would burn enormous metabolic resources on speed the response can't consume. A diffusion-based system for predator escape arrives hours after the predator.

### Self-modeling

*Pressure.* A system whose effectors can damage itself has to distinguish self from non-self. How strictly that has to be enforced depends on the cost of a false positive:

- For the nervous system, a body-schema error produces a brief mismatch: bump into a wall, update the model, move on. Errors are short-timescale and reversible.
- For the immune system, a single false positive deletes a tissue. A cytotoxic T cell mistaking β-cells for foreign causes type 1 diabetes; a B cell mistaking myelin causes multiple sclerosis. Recognition leads directly to destruction, and destruction is irreversible. The cost asymmetry between false positive and false negative is inverted from typical learning.

*Neural — errors are cheap and recoverable, so an online running estimate is sufficient; no special infrastructure is needed.* Motor commands produce efference copies sent to sensory regions; expected re-afferent input is subtracted out, so only unpredicted sensation carries information. A body schema built from proprioception and motor experience maintains a continuously updated estimate of limb positions. The model lives in the same circuits that drive motor control, and updates within the same ms-scale loop — because nothing about the cost structure demands more.

*Immune — a single false positive is unrecoverable, ruling out online learning that might mistake self for non-self even once, leaving pre-deployment filtering as the only safe option.* You cannot afford to "learn from the mistake" when the mistake destroys a tissue. The only safe move is to filter the random repertoire *before* any cell can act. The thymus does exactly this: immature T cells are exposed to self-peptides presented on MHC molecules; T cells whose receptors bind above a threshold affinity are induced to apoptose; T cells that bind nothing at all are also eliminated; only T cells that bind *something* but not *self* enter circulation[^thymus]. The computational move — a curated set of hard negatives filtering a candidate population before deployment — is the same shape as contrastive pre-training in ML, but here the contrast set is fundamental to *safety* rather than to performance.

The strictness of the thymic filter is a direct consequence of the cost asymmetry. §V comes back to this — it's the central bound on how far an immune-based intelligence can scale.

### Action

*Pressure.* Close the loop in the environment. Two regimes mirror sensing:

- **Mechanical action** — flee, fight, manipulate — runs on the same ms-to-s budget as fast sensing. Body-scale speed again rules out diffusion; the actuator has to be drivable by a fast wire.
- **Chemical action** — kill a microbe, recruit a partner cell, alter a microbial community — runs on hours-to-days. Speed isn't bought at any cost, but specificity (kill *this* cell, not that one) and irreversibility (kill = stay killed) often matter more.

*Neural — the mechanical-speed requirement forces an electrically-driven actuator coupled directly to the signalling wire.* The actuator is muscle, and the coupling is engineered for transduction at the same ms timebase as the rest of the system: a motor neuron's action potential releases acetylcholine at the neuromuscular junction; nicotinic receptors on the muscle fibre depolarise; Ca²⁺ release from the sarcoplasmic reticulum binds troponin, exposing actin-myosin binding sites; cross-bridge cycling contracts the fibre. The full chain runs in ms, matching sensing, and is reversible — the muscle relaxes when input stops, so corrective commands can be issued continuously.

*Immune — slow chemical effectors are sufficient because the threat timescale is hours-to-days, and irreversibility is acceptable (often desirable) given the nature of the targets.* Antibodies opsonise pathogens for phagocytic uptake; cytokines recruit and activate other immune cells; antimicrobial peptides disrupt microbial membranes; perforin and granzymes induce apoptosis in target cells. Deployment is slow (cytokine-mediated recruitment unfolds over hours) and much of it is irreversible — killed cells stay killed, which is what was wanted. At longer timescales, immune effectors are the organism's main interface for shaping its microbial environment: tuning IgA production to select gut commensals, signalling across the host-microbiome boundary.

Neural action projects into rapid, reversible, physical space. Immune action projects into slow, irreversible, chemical space. Each effector matches the timescale and the reversibility profile of the threat it answers.

---

Across all six capabilities the argument has the same shape: state the pressure, identify the physics constraint it imposes, and show that the implementation is what's left once the constraint is enforced. The computational problem is substrate-independent; the substrate decides which physics is even available; the environment decides which constraints get applied.

## V. Where the immune path could lead

Physics tells us what each substrate *can* do. The environment tells us which capabilities *pay off*, and in what order.

Under the predator-prey regime that shaped animal bodies, neural signalling wins decisively: milliseconds matter, spatial targeting matters, and the volumetric cost of wiring is tolerable. The immune branch simply can't compete on that timescale. That's why general intelligence, in our lineage, evolved on the neural side.

But the immune profile — slow, diffusive, shape-specific, durable — matches a different kind of niche: one where threats are combinatorially diverse in shape rather than fast in motion, and where mistakes play out over days rather than seconds. In such a niche, a stepwise path from an extant immune system toward general-purpose computation becomes plausible, one capability at a time.

### A. What bounds the path: the overfitting problem

Every learning system has to balance specificity (recognise only what it's seen before) against generalisation (recognise novel things that resemble what it's seen). In typical ML settings, the two kinds of error cost roughly the same. For the immune system they don't: missing a pathogen that mimics self costs one infection; classifying your own pancreatic β-cells as foreign costs you the organism.

Autoimmunity is the immune learner's overfitting problem with the asymmetry inverted — over-generalisation is catastrophic in a way under-generalisation isn't. Evolution keeps the decision threshold conservative as a result.

This is the central constraint on an immune-based intelligence. To generalise further, it has to generalise *safely*: test novel recognition patterns in compartments before deploying them; run them through multiple self-tolerance checkpoints; gate activation on context signals confirming a genuine threat (the costimulatory signals a T cell needs before firing already do this). Calibrated uncertainty and robustness to distribution shift aren't extras on an immune learner; they're load-bearing.

### B. A sequence of pressures

The first three pressures below are already satisfied in extant immune systems. The later four are nascent — biological implementations exist but are weak — and extrapolating them is what gets to something like general intelligence.

**1. A large, varying pathogen population → broad recognition.** VDJ recombination generating a ~10⁹-shape repertoire. Done.

**2. Threats that recur over time → long-term memory.** Memory B and T cells. Done.

**3. Threats that arrive together → associative memory.** If pathogen A reliably precedes pathogen B, priming for B on seeing A pays. Partially present: trained immunity epigenetically primes the innate response to unrelated later challenges for weeks to months[^trained], and cross-reactive T-cell memory provides some antigen-specific linkage. But nothing as rich as the associative learning neurons do. The missing piece is a flexible mechanism for linking specific memory populations. Plausible substrates exist — paracrine signalling between memory compartments, shared epigenetic states, follicular-dendritic-cell scaffolds co-presenting related antigens — but would need to scale into general-purpose associative machinery.

**4. Rapidly-evolving threats → generalisation to novel variants.** Fast-mutating pathogens defeat exact-match memory. The biological answer is broadly-neutralising antibodies — receptors binding regions conserved across variants. They exist (notably against HIV and influenza) but are rare and take years to develop, because the conserved pathogen region often resembles self, and the generalised receptor has to be shepherded past tolerance checkpoints by iterated germinal-centre rounds on variant antigens. This is the specificity/generalisation tradeoff made concrete: the system *can* generalise, but only via costly pathways that bleed off autoreactive variants along the way. Routine generalisation would require this machinery scaled up — parallel lineages with separate self-tolerance thresholds, or architectural separation of "exploratory" and "deployed" recognition.

**5. Temporally structured environment → prediction.** Pathogens on seasonal or diurnal schedules select for pre-emptive defence. The immune system already cycles weakly on a 24-hour clock — neutrophil traffic, cytokine production, and response intensity all vary with circadian rhythm. Extending to longer and richer periodicity requires plugging environmental sensors into the regulatory networks that already gate immune activation. Mechanistically, the wiring is already there.

**6. Novel chemistry → sandboxed experimentation.** An organism confronting unknown molecules benefits from testing them in isolated compartments before committing systemically. Germinal centres already do exactly this at the receptor level — a protected sandbox for directed evolution on receptors. Generalising the same principle to other machinery (digestive enzymes, signalling molecules) is an architectural change, not a new mechanism.

**7. Proactive niche construction → goal-directed action.** Shaping the environment — secreting molecules to suppress competitors, recruit symbionts, remodel local chemistry — requires selecting actions from predicted outcomes. Elements exist: biofilm formation, quorum sensing, host-microbiome signalling. What's absent is an explicit forward model — "if I secrete X, [Y] falls, and the consortium I prefer will thrive." Building one requires associating action with outcome via memory, which is capability (3) pointing outward rather than inward.

Run the full sequence and you have diverse recognition, long-term memory, associative memory, motif-level generalisation, prediction, sandboxed experimentation, and goal-directed action. Most of what any learning agent needs.

### C. Where the niche is

The immune route to general intelligence gets selected for only where:

- The dominant selection pressure is molecular, not mechanical — pathogens, symbionts, and chemical resources matter more than predators and prey.
- Macroscopic movement is unhelpful: sessile, colonial, or ultra-slow lifestyles.
- The environment is dense with molecular information and temporally structured, so prediction and memory pay off.
- Threats arrive in combinatorial diversity, forcing continued investment in recognition breadth.

Real-world analogues that meet most of these: hydrothermal vent communities, coral holobionts, bivalve-chemosymbiont systems, mangrove root microbiomes, deep biofilms. These already host sophisticated chemical signalling and ecological engineering. What they lack — and what the sequence above would have to provide — is centralised model-based decision-making layered on top.

## VI. The flavour of an immune-branch intelligence

What would such an organism actually be? Not what our nervous system does well. Real-time motor control, fast sensory discrimination, predator evasion — the physics rule them out.

What it *would* do is the chemistry of its environment, at scale and over time. Discriminate thousands of molecular species. Maintain self-integrity across centuries. Design and deploy novel compounds via directed evolution. Engineer its microbial neighbourhood strategically rather than reactively. Its agency runs on minutes-to-days time constants, with memory stretching to decades. It wouldn't dart, grab, or flinch; it would cultivate, synthesise, and remember.

The recurring idea: the computational needs don't change. Sensing, memory, generalisation, prediction, action, self-modeling — any learner has to solve all six. The substrate decides what's cheap. The environment decides which capabilities are worth paying for, and in what order. Neurons win on speed and spatial precision; immune cells win on molecular specificity, durability, and freedom from wire constraints. Intelligence is what you get when something has to solve the whole list.

---

**References**

[^sterling]: Sterling & Laughlin, *Principles of Neural Design*, MIT Press, 2015.
[^attwell]: Attwell & Laughlin, "An Energy Budget for Signaling in the Grey Matter of the Brain", *JCBFM* 21(10), 2001.
[^diffusion]: Diffusion time scales as d²/(2D); in tissue, effective D is typically an order of magnitude lower than in water because of obstacles and binding, so these are optimistic.
[^yellowfever]: Akondy et al., *Nature* 552, 2017 — yellow-fever-specific memory T cells traced in humans decades after a single vaccination.
[^burnet]: Burnet, "A modification of Jerne's theory of antibody production using the concept of clonal selection", *Australian Journal of Science* 20, 1957.
[^vdj]: Estimates vary with how junctional and pairing diversity are counted; ~10⁹ is a conservative figure for the measured circulating repertoire in an adult, with theoretical potential ~10¹¹ or higher.
[^thymus]: Klein et al., "Positive and negative selection of the T cell repertoire", *Nat. Rev. Immunol.* 14, 2014.
[^shm]: Somatic hypermutation runs at ~10⁻³ per base per cell division in germinal centres, vs. ~10⁻⁹ for most of the genome.
[^trained]: Netea et al., "Trained immunity: A program of innate immune memory in health and disease", *Science* 352, 2016.
