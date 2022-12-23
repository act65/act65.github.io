---
title: "Principles of neural design"
date: "2018-08-13"
coverImage: "pond.jpg"
layout: post
subtitle: Note from reading the book.
---

![]({{site.baseurl}}/images/{{page.coverImage}})

The books starts with some great questions:

- Why does an animal need a brain?
- Why does it need to be big?

## Why does an animal need a brain?

I learned something important here, brains are not for learning, they are for quickly communicating information from sensor to actuator.

> One impediment to richer behavior is that there is only one cell membrane and thus only one line for fast (electrical) communication.

Consider a small bacterium that bumps into some obstacle, the collision sensor on its head needs to send info to its flagella on it's end. This communication can occur quickly because a bacterium is small and thus chemicals have a small distance to diffuse across. But now consider a multi-celled organism in the same setting, collision sensors and actuator. How can information be quickly communicated between locations many cells apart? Electrical communication is a good candidate as it is fast.

## Why does it need to be big?

> Coordination demands some mechanism with an overview that enables it to weigh alternatives, set priorities, and then exert ultimate authority to execute. Fortunately, the multicellular design that demands such integration also provides a special class of cells to accomplish it. These cells— neurons—now do what Paramecium could not: provide multiple fast lines for communication. In short, for a multicellular organism a brain becomes necessary, possible, and profitable.

In some sense, the ability to adapt to your environment is intelligence.

## The principles of neural design

I really love this. What are the simple principles from which brains emerge?

> For designs to have persisted across this immensity of time and spatial scale implies that they are neither arbitrary nor accidental. Rather, they must have emerged as responses to some broad constraint. That is what elevates the shared responses to the status of principles.

Ok, so they define a 'principle' as a conserved feature across time and space, (and possibly evolutionary time and space).

> send only what is needed; send at the lowest acceptable rate; minimize wire, that is, length and diameter of all neural processes

Ok, so what should these 'principles' explain? What can we do with principles and how can we use them to understand the brain?

> The conservation laws should explain why neurons branch, what limits their individual volumes, their aggregate volumes in local circuits, and their fractional volumes (wire vs. synapses). The same laws should explain specialized substructures of local circuits, such as cortical layers, columns, stripes, pinwheels, and barrels—plus the structure of tracts. At a still larger scale, the laws should explain distinctive patterns of cortical folding, the relationships between cortical areas, and hemispheric specialization.

Here is a more verbose version of the principles.

> ### Compute with chemistry
> 
> Bits per joule approaches lower bound set by thermodynamic limit. Bits per liter reaches lower bound set by protein structure. • Signals are fast at short distances. • Computation is direct.
> 
> Compute directly with analogue primitives • Analogue completes a basic operation in fewer steps than digital. • Analogue is well suited to chemical and electrical computing.
> 
> Combine analogue and pulsatile processing • Analogue processes information at high rates. • Analogue electrical signals are cheaper than pulses. • But stochasticity at all stages (vesicle release, ligand binding, channel opening) accumulates noise. • Therefore, compute locally in analogue; threshold to restore S/N, and send noise-resistant pulses.
> 
> ### Sparsify
> 
> • Signal with proteins in small clusters. • Release vesicles in brief bursts. • Fire spikes in brief bursts. • Maximize information per array for least space and energy: optimize fraction of active neurons; optimize S/N vs redundancy.
> 
> ### Send only what is needed
> 
> • Reduce noise and redundancy. • Sculpt message for downstream users. • Reduce number of signals to save energy and space.
> 
> ### Send at the lowest acceptable rate
> 
> • Higher rates cost disproportionately more.
> 
> ### Minimize wire
> 
> • Space and energy decrease as length and (diameter) 2 . • Small diameter allows few bits per second. • Slowest signals can use zero wire (neuromodulators, hormones). • Shorter wires reduce processing time. To shorten wire: • Organize neurons in maps; • Within a map segregate computations in parallel circuits. • Separate circuits in layers, columns, stripes, barrels. • Arrange maps to interconnect with least wire • Connect neurons by matching their axonal and dendritic meshworks. • Reduce instruction set to send long distance.
> 
> ### Make neural components irreducibly small
> 
> • Smaller reaction vessel allows faster chemistry with fewer molecules. • Lower membrane capacitance charges with smaller current. • Nanoscale molecular components allow smaller axons and synapses.
> 
> ### Complicate
> 
> • Specialize molecules to match signal properties (match molecular binding affinity to temporal bandwidth, protein stability to photon energy). • Specialize neural circuits to match task (rod circuit for starlight, cone circuit for daylight). • Optimize across levels, from molecules to neural circuits.
> 
> ### Adapt, match, learn, and forget
> 
> • Adapt output capacity to predicted range of inputs. • Match capacity across levels (symmorphosis). • Learn in order to improve future predictions. • Forget in order to preserve storage capacity.

## Anticipatory regulation

Homeostatic regulation is reactive, a change in your environment changes your internal state (change in temp). Given this change to the new environment (hotter) you must adapt (pump blood to extremities). However, because the response was reactive there will be a delay and possibly overshoot.

The advantage of anticipatory regulation (allostasis) is that (assuming you can accurately predict the future) you can start adapting before a change (pumping blood to extremities before you get too hot).

I would like a simple example showing homeostatic versus anticipatory regulation. **Q:** When is one optimal? What if these regulators are (not) given access to an accurate clock? How does this change the pros/cons of the two methods. And what alternatives are there?

> Flies too show anticipatory behavior—to a level consonant with their life span and environmental reach. A fly need not wait for its blood sugar to fall dangerously low, nor for its temperature to soar dangerously high, before taking action. Instead its brain expresses prewired commands: Find fruit! In a cool spot!"

## Active sensors

> The motor stratum of the superior colliculus represents an intermediate level pattern generator. It is tweaked by succinct executive decisions from above and delivers succinct instructions to low-level pattern generators. But it must also fulfill one more responsibility—to inform higher levels that its order: “Look!” has been sent. 16 This signal, termed corollary discharge , informs frontal cortex that the sensor is being repositioned. Why is this signal needed?

**Q:** When are mobile sensors more efficient? And what problems does this introduce? (The need to predict/compensate for movement, ???)

> For most sensors the spike rates are still too high for direct relay to cortex, so a central integrator ( thalamus ) is interposed to concentrate the message, that is, more bits per spike (figure 3.5C). This allows a twoto fourfold reduction in mean spike rate on the path to cortex. The thalamus is also used by other brain regions, such as cerebellum, striatum , and superior colliculus, for the same function (Bartlett & Wang, 2011; Sommer & Wurtz, 2004). 18 The computational strategy and synaptic mechanisms to achieve this function are described in chapter 12. The exceptions to this design are the olfactory sensors which signal at such low rates that, following a single stage of preprocessing in the olfactory bulb , they are allowed to skip the thalamic relay and ascend directly to cortex (Friedrich & Laurent, 2001).

**Q:** Is corollary discharge necessary? What problem does it solve?

## Chemical computation

Computing with analogue signals. Hmm. Need to think about this.

I would love to see a diagram of the state transitions of an adrenaline receptor! It seems super complex, an this is just one receptor...!!! Are the visualisations as well?

**Q:** How can you do functional programming with chemicals? The problem seems to be that the computations might not be safe. They might be effected by chemicals diffusing from other areas!? You really need to be able to isolate the reactions (via orthogonal chemical pathways, or distance or time or constraining reactions to certain surfaces/ volumes or ?).

> The number of channels is limited by membrane space for pumps. A pump molecule has approximately the same footprint as a channel, but, operating at 200 cycles s –1 , it extrudes only 600 sodium ions s –1 . To match the throughput of one open sodium channel (6 × 10 6 sodium ions s –1 ) requires 10,000 pump molecules, which occupy 4 μ m 2 of membrane. Thus the density of open channels that a neuron can sustain is reduced to one channel per 4 μ m 2 , 10,000-fold less than their maximum packing density. This translates into a 10,000-fold lower bandwidth and a 100-fold reduction in S/N. Being proportional to bandwidth and log 2 (S/N), the sustainable information rate is cut by almost five orders of magnitude. Placing the circuit’s battery chargers (pumps) alongside the circuit’s transistors (ion channels) limits a neuron’s ability to process information, but cell biology offers few alternatives.

**Q:** Ok, wait a minute, how do ion pores work? Why don't they just get blocked!?

> The NMDA receptor’s ability to detect and signal coincidence equips a neuron for pattern recognition and learning (chapter 14). An active receptor emphasizes the coincidence by amplifying and extending a synapse’s excitatory input; moreover, it marks the synapses whose signals coincide. Only synapses that recently delivered glutamate have NMDA receptors primed for action. When these receptors are unblocked by depolarization, they admit chemical messengers (calcium ions) that initiate structural change. Because an action potential also depolarizes synapses, the NMDA receptor enables a neuron to take a first step in learning; it can identify and modify those synapses whose inputs coincide with a definitive output. The duration of an NMDA receptor’s time window is critical for learning. Shorter would increase false negatives—the receptor would miss correlations between events that take longer to unfold. Longer would increase false positives—more unrelated events would occur in the same time window. The NMDA receptor’s OFF rate creates the 100-ms time window that seems about right for many of life’s more immediate events.
> 
> the glutamate receptor families enable a neuron to process on different timescales by producing synaptic responses of different durations.

So these glutamate receptors are doing something like a fft!? Decompsing a signal into energies of different frequencies.

**Q:** Where can I find a collection of the different chemical implementations of AND, amplify, x, + /, log, ...? It would be cool to make a library of these.

> One key is a glutamate receptor of astonishingly clever design. When an NMDA receptor binds a quantum of glutamate, its cation channel admits only a modest current because the channel’s mouth is partially blocked by a magnesium ion. However, if a different input excites the neuron to fire a spike, the strong depolarization pops the magnesium from the channel, allowing an inward surge of current carrying calcium (figure 14.5). This pulse of calcium initiates LTP.

## Dendritic computation

> A dendrite does not transmit far: rM is too low because potassium channels stay open to maintain resting potential, and rcyt is too high because hydrated ions in cytoplasm conduct poorly. Therefore, a dendrite’s length constant is generally less than 1 mm, and dendrites preserve signal amplitude by staying shorter than their length constant. A dendrite may increase its length constant by growing thicker, thus reducing rcyt , but the improvement goes only as the square root of diameter (Koch, 1999). With length constant increasing as √ d and volume increasing as d 2 × length , the total cost of space and materials increases as ( length ) 5 .

Huh. So dendrites only integrate local information by necessity!

> Nodal spacing increases directly with axon diameter. This works because thicker axons produce larger nodal currents and increase the number of myelin wraps, further increasing the space constant. In systems where spike arrival time is critical, nodal spacing can be tweaked to compensate for different conduction distances (Cheng & Carr, 2007; Carr & Boudreau, 1993).

Huh, I wonder how much learning can be done by adapting these arrival times!?

Subtle things like changing the diameter of dendrites, or the location of spines and have computationally significant consequences. Fascinating, want to investigate further.

## Information and noise

This was a large theme through out the book. How are signals encoded efficiently? How is ???

> For example, an enzyme generates a product at a finite rate, so it requires time to change the product’s concentration in a compartment of given volume; similarly an electrical current supplied through a resistor requires time to charge a capacitor. Thus, the number of different states to which a signal can jump in one time interval, Δ t , is limited by the rate at which the signal can change, but given sufficient time, it can move to any state. This time dependency complicates the calculation of information rates. Shannon solved this problem by using the Fourier transform to convert the continuous analogue signal and noise into their frequency components. Each frequency component is independent, in the sense that changing the amplitude or phase of one frequency component has no effect on any other frequency; consequently, every frequency carries its own information. I = \\int^{co}\_{0} log 2 \[1 + S ( f ) / N ( f )\] df

We want to design a communication channel that is invariant to noise, so if we are computing with chemistry, we need to increase the activation energy of the receptor to reduce the chance of random activation.  (Was probably some nice quotes about this!?)

The more noise in a signal, the less information.

Need to think more about analogue versus discrete. Multiple pros/cons for each!? Invariance to noise/stability, metabolic cost, ...? Key is what can be recovered by the receiver.

## Efficient wiring layout

> axons branch at an acute angle rather than a right angle ( Y vs. T ). Also they tend to leave the parent neuron at the point nearest to their destination. Such savings may seem inconsequential, but they add up: the 5 μ m saved at 10 axonal branchings by each of 10 10 cerebrocortical neurons reduces wire by 500 km.

Similar problems to embedded circuit board design!!! Reminds me of some sort of graph structure we are optimising edge weights to minimise transport costs. I wonder how general this problem can be made.

> neurons that fire together should locate together

Thus a way of learning could by physically moving neurons!?

**Q:** If wiring is so expensive, why is the visual cortex so far away from the eyes!!?!?!?!

> In short, the layout of cerebellar cortex mixes cell bodies with circuits to minimize total wire. It also arranges the sequence of layers so that the thinnest traversing axons are the longest and the thickest traversing axons are the sparsest. This allows a granule-to-Purkinje convergence of nearly 200,000, roughly 20-fold greater than for any other circuit, 7 an upper bound to neural connectivity.

Omg, I get why the cerebellum is design as it is. High rate neurons such as the inputs and outputs want to minimise their wiring, its expensive. So move the intermediate layer to be the furthest away. I had assumed that this layout was just one of evolution's sub-optimal quirks. But, it turns out evolution is smarter than I am. Awesome.

Also, folds allow greater surface area while minimising the length of connections.

> Thalamocortical axons fire at far lower rates than the cerebellum’s primary inputs, so they are thinner. Consequently, unlike the cerebellum’s thick mossy fibers, which must terminate immediately upon exiting the white matter (figure 13.9), thalamocortical axons can track through the deep cortical layers to arborize in the middle and upper layers (figures 12.6 and 13.17). The thinnest thalamic axons reach the uppermost cortical layer, taking the longest course through gray matter, whereas the thicker ones branch in the middle, taking the shortest course (figure 12.8).

Want to communicate info over distance at a high rate. Can use many neurons that sparsely activate, or few neurons with high freq activations.

> Larger neurons reside in the deeper layers—where their thicker output axons least disturb the circuitry. This reverses the cerebellar layering (small neurons deep), but it satisfies the rule for optimizing the interface with white matter. Deep neurons distribute to subcortical structures and are diverse (chapters 4 and 12). Therefore, they should distribute their axon diameters log-normally, a prediction supported by measurements of the long descending tract from frontal and parietal cortex to spinal cord (chapters 3 and 4).

There is a lot of talk, but few proofs about the optimal layouts given various constraints... It would be fun to take something like C elegans and measure how far its connectome is from optimal!? But also, it would be interesting to explore the different wiring patterns within the brain and to explore from which constraints these emerge as optimal solutions.

## Learning

> An important constraint on learning is space. The adult brain is jammed with circuits and tracts, and it cannot expand. So learning must conserve space with a design that: (1) is spatially specific; (2) stores only what is needed; (3) stores only for as long as needed (i.e., selectively forgets); (4) stores and retrieves information at the site where it is processed; (5) optimizes the units of storage (size and number); and (6) optimizes a “teaching signal” for the real world, which is an environment rich in small surprises.

This is cool, I had never really considered the space issues with respect to learning. Memories are physical things and thus take space, and energy to maintain.

> The obvious site to compactly store information is at the synapse. Storage occurs by changing its transfer “weight,” that is, its ability to excite or inhibit a postsynaptic neuron. Since the synapse is the key site for processing information, storing it there avoids additional wire for relay. Moreover, information stored directly at a synapse can be retrieved directly—also avoiding additional wire. In short, as we peruse a blueprint of brain design, we should not seek a special organ for “information storage”—it is stored, as it should be, in every circuit.

I am not really sure how/why a synapse is "a key sure for processing information".

> For example, restrict visual input to one eye, and within days the geniculocortical synapses for that eye are expanding in V1’s ocular dominance stripes. Simultaneously synapses for the deprived eye are retracting. 5 Or, shift the wavelength of chromatic input to one eye with a tinted contact lens for a few days, and color perception shifts for several weeks (Neitz et al., 2002). Sew two fingers together so that their surfaces function as one, and the primary somatosensory cortex (S1) soon resculpts the sensory map of the hand from five fingers to four (Clark et al., 1988).

Ok, I didnt realise it would be that fast. Cool.

> The cheapest route to inform large volumes of neural tissue would be to broadcast a neuroendocrine signal via the circulation, that is, wireless signaling (chapter 4). However, that would be too slow; moreover, it would smear the critical temporal differences. On the other hand, to implement extremely sharp timing would require that a “teaching synapse” contact every learning synapse—at a huge cost in space. But the teaching signal does not require extremely sharp timing. It can be roughly 100-fold broader than, for example, an auditory signal. Consequently, the teaching signal can be sent by wire to within a few micrometers of some learning synapses and there release a well-timed pulse of chemical transmitter into the extracellular space. Transmitter is allowed to diffuse over micrometers to reach multiple synapses. Diffusion over a few micrometers allows sharp enough timing, and the spatial blurring from diffusion doesn’t matter because only synapses that are already potentiated will respond (figure 14.3).

**Q:** Huh, so how is credit assignment done in such a non-specific way? If it is allowed to diffuse over large (relatively) spatial scales then it can influence many synapses. I guess the relative timing between is what makes the difference, but because of the lag as a signal diffuses other synapse could receive a signal... that doesnt seem particularly safe?

> Temporal-difference learning is, from a theoretical perspective, a highly efficient design (Glimcher, 2011). Moreover, the brain executes it efficiently via dopamine neurons that fire brief bursts of slow action potentials to deliver, quasi-wirelessly, a pulse of subjective well-being that encodes a positive surprise as the teaching signal. This works brilliantly in natural environments because they are unpredictable and therefore provide diverse small surprises and frequent pulses of subjective well-being. But modern environments are crafted to be highly predictable. For the temporal difference design, this creates two huge problems. First, because the teaching signal needs to be brief, the sense of wellbeing—what Freud termed “happiness”— must be episodic. This is bearable when the environment delivers small reward-prediction error signals with some frequency. However, as the environment grows more predictable, sources of these signals shrink, and the intervals between episodes of satisfaction lengthen. The efficient design for learning in an unpredictable environment becomes in a predictable environment—zoo or modern city—an efficient design for existential angst.

Oh yea, interesting theory... Not quite sure it works like that?!?

## Computational tradeoffs

> “As information rate rises, costs rise disproportionately.” For example, to transmit more information by spikes requires a higher spike rate. Axon diameter rises linearly with spike rate, but axon volume and energy consumption rise as the diameter squared. Thus, the essence of neural design: “Send only information that is needed, and send it as slowly as possible”

**Q:** What is better/more efficient?!? Lots of cheap cars than can be redesigned as needed, or more expensive, adaptable cars? Under which circumstances is one strategy dominant?

> how fast does a neuron send information (bits per second) and how efficiently (bits per spike)? And at what cost in space (bits per cubic millimeter) and energy (bits per molecule of adenosine tri-phosphate)?

I love this!

> The inescapable cost of sending any information and the disproportionate cost of sending at higher rates lead to three design principles: send only what is needed ; send at the lowest acceptable rate ; minimize wire, that is, length and diameter of all neural processes.

Higher info rates (more bits per second) require disproportionately more energy and space because they need thicker axons—for which both space and energy rise as the diameter squared. Would be cool to study how different systems scale as they process information. What rate do computer architectures scale at? Bit rate = O(??).

> The genius of this wireless system lies partly with the receivers. Although all somatic cells are exposed to all hormones, only certain cell types download a given message. To do so, they produce a specific molecular receptor that binds a particular hormone and triggers a particular intracellular response. Thus, information broadcast diffusely to the whole body can be read out by a restricted number of cell types—whose responses to the signal are thereby coordinated.

Cool, but now there is a different cost compared to electrical transmission. We need to make a lot of these hormones (and receptors) because they diffuse any/everywhere.

But yea, the different neurons with different receptors is cool, like a type system?

> combine many synaptic inputs to produce an output within milliseconds. This rapid many-to-one integration, which serves behavioral requirements for prompt decision, would be difficult to implement with a chemical circuit. The many-to-one ability is further exploited by joining several dendrites to the cell body or an integrating segment to form a final common output

huh, so some types of physics (for compute) might scale better/worse to higher dims!?

I liked that when considering chemical computation, more practical costs were considered, the cost/time to reset the state, to be invariant to noise within some tolerance, activation speed, ...

## Notes on evolution

Ok, I thought I understood evolution. Turns out I was wrong. I thought that is was as simple as a preference towards traits that give a competitive advantage. But it isn't quite that simple.

> The worm’s enlarged territory and its locomotion through a labyrinthine matrix with persistent chemical traces warrant an upgrade.

What is the advantage of a plant being able to move? It no longer has to compete with other plants, it can simply move to a location with more light. Thus it has removed itself from the competition and found a new energy source to exploit. A kind of positive sum mutation, where the mutated plant benefits (its own patch) and the un-mutated plants benefit (less competition).

> Because most worms use the same foraging circuits, they accumulate at the same sites—like undergraduates at a good café. And the subtext is similar: a place to feed is also a place to find mates.

Consider a worn and a bacteria. The worm and the bacteria are not really competing, as the worm is exploiting another source of energy difference that the bacteria cannot.

> Moths are hunted by bats using echolocation. So the moth invests in a pair of simple ears, each with only one or two sensors, and couples their outputs to a simple pattern generator for evasive flight. When the sensors detect a bat’s ultrasonic chirp, evasive flight is engaged, and the moth dives to the ground (Roeder, 1967). This system provides a cheap answer to the bat’s high-tech, super-expensive sonar.

**Q:** So a 'good' adaptation is one that is not easily exploited!? There is a notion in game theory of exploitability, ... (is this the same?)

> But thermal events increase proportionally with the number of (n); whereas the number of captured photons increases according to law of diminishing returns because each disc added to the bottom of stack is shielded by the discs above. So in mammals the upper limit is about 900 discs.

## Thoughts/questions/quotes/...

> To ensure that an organism will execute these orders, there are neural mechanisms to make it “feel bad” when a job is undone and “feel good” when it has succeeded. These are circuits whose activity humans experience, respectively, as “anxiety” and “pleasure.” Of course, we cannot know what worms or flies experience—but the same neurochemicals drive similar behaviors

> The output of a single pixel changes over time as the eye moves across a scene and objects move within a scene. These temporal signals are also correlated. Movement converts spatial correlation into temporal correlation and, analogous to the optical point spread function, the photoreceptor flash response spreads signals over time, leaving traces of the past in the present

> London taxi drivers, who visually navigate a complex cityscape, expand their hippocampal gray matter (Maguire et al., 2000). This occurs gradually with practice over several years. Piano tuners, who acoustically navigate a complex soundscape, also gradually expand their hippocampal gray matter (Teki et al., 2012), along with auditory areas in the temporal and frontal lobes.

> Thus, the brain follows a core principle that serves all biological systems: use current conditions to predict future needs and revise circuits accordingly.

**Q:** Does it use any kind of acceleration? If bones keep getting broken, do they get built exp stronger each time?

> One neuron can alternately serve two different circuits: one during daylight and another during starlight.

**Q:** So could we design computers that share transistors!? Need to ensure there are no collisions!? We already do this to the extreme!?

## Future computers, inspired by the brain

Want computers that use heterogeneous compute on a nano scale. Every operation is embedded in the 'right' physics given the operation, and its performance requirements! Sequential computations should be co-located, but they might be computed in different physical phenomena. But there will be losses from transfering info from one representation to another. So what is the optimal architecture?

One of a brain's main advantages is that it can be built using easily accessible materials. How can we engineer computers using common materials. Even better, what about self assembling and self repairing computers. Imagine growing a computer in your backyard.
