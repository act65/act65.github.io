---
title: The Hammer and the Nuke
subtitle: Why AI Robustness is a Necessary Condition for AI Alignment
layout: post
categories:
    - research
revisions:
  - "2026-05-25"
  - "2026-08-07"
description: "Why AI Robustness is a Necessary Condition for AI Alignment. How can we ever hope to build an Artificial General Intelligence (AGI) that won't outsmart..."
tags:
  - essay
  - ai-safety
  - reinforcement-learning
---

How can we ever hope to build an Artificial General Intelligence (AGI) that won't outsmart humanity to our detriment, if we can't even build a narrow AI that a clever human can't trick?

That question is the standard argument for treating **robustness** in today's narrow AI as a prerequisite for **alignment** in a future AGI, and I think its conclusion is roughly right. The argument, though, is wrong — and seeing exactly *why* it is wrong is the point of this post. The usual reading is that alignment is, in essence, an adversarial robustness problem where the adversary is the most powerful optimizer we've ever built: the AGI itself. But the AGI is not a scaled-up version of the clever human. It is a different *kind* of adversary, and most of the defences that work against the clever human do not carry over.

The intuition that robustness and alignment are deeply connected is not new. Variants of it run through much of the AI safety literature: Armstrong's utility indifference [^21], Soares et al.'s corrigibility [^22], Everitt's reward tampering framework [^23], Christiano's case for worst-case performance optimisation [^20] — all gesture at the same underlying idea, that a safely-deployed agent must be insensitive to certain classes of intervention on its own decision machinery. Parts of that idea are already precise: Everitt et al. [^23] give graphical criteria for when an agent-caused reward-tampering incentive is present or absent, and Farquhar et al. [^24] give a formal invariance notion in the same framework. What is less developed is the bridge from that literature to the *empirical* robustness literature — adversarial examples, certified defences, robust MDPs — which is what most people have in mind when they say "robustness". This post proposes a formalisation of that bridge: casting wireheading and reward poisoning as the identical-interest and zero-sum extremes of a single reward-perturbation game, and using it to argue that the maximin-robustness literature is largely the *wrong* place to look, contrary to a common assumption. The argument is structural, and I flag explicitly where it falls short of a proof — including one place where the argument I originally wanted to make turns out to be false, which I've left in rather than quietly deleted.

### Defining Our Terms with Technical Rigor

To make this argument precise, we must move beyond analogy and into formalisms.

#### AI Alignment: The Gap Between Proxy and Intent

The core challenge of AI alignment is that we cannot formally specify our true, nuanced goals. [^1] We have an intended goal, which we can think of as a latent, true reward function, $R_{\text{true}}$. This function captures the full richness of our desires—e.g., "a clean room," "a successful company," "a flourishing humanity." Since we cannot write down $R_{\text{true}}$ in code, we instead specify a simpler, measurable **proxy reward function**, $R_{\text{proxy}}$. [^2] For example, "maximize the absence of visible dust," "maximize quarterly profits," or "maximize human preference scores on a survey."

An agent trained via reinforcement learning finds a policy, $\pi_{\text{proxy}}$, that maximizes the expected return under this proxy:

$$
\pi_{\text{proxy}} = \underset{\pi}{\mathop{\text{argmax}}}\ \mathbb{E}_{\pi,\, s_0 \sim \rho}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{proxy}}(s_t, a_t) \right]
$$

Throughout, $\gamma \in [0, 1)$, rewards are bounded in absolute value by $R_{\max}$, and every expectation is over trajectories induced by the policy from an initial-state distribution $\rho$. I drop the subscripts below where they are unambiguous.

In essence, the agent learns a policy that achieves the highest possible score on the proxy metric we've designed. The agent is **aligned** if the behavior of $\pi_{\text{proxy}}$ is also optimal or near-optimal under $R_{\text{true}}$. It is **misaligned** if $\pi_{\text{proxy}}$ leads to behaviors that are good for $R_{\text{proxy}}$ but bad for $R_{\text{true}}$. This misalignment is often called "specification gaming" [^3] or "reward hacking." [^4] The problem is that an agent optimizing a proxy metric can find clever, unintended, and often undesirable ways to maximize it that violate the spirit of the true goal. [^5]

#### Adversarial Robustness: A General-Sum Game

Adversarial robustness is the challenge of ensuring an agent's policy remains effective when facing adversarial interventions. [^6] More formally, we can model this as a two-player, general-sum game between the RL agent and an adversary.

*   The **RL Agent** plays a policy $\pi$ to maximize its own reward, $R_{\text{proxy}}$.
*   The **Adversary** chooses a perturbation $p$ from a set of possible interventions $P$. The adversary plays to maximize its own, separate reward function, $R_{\text{adversary}}$.

The agent and adversary are thus solving coupled optimization problems:

$$
\text{Agent's Goal:} \quad \max_{\pi} \mathbb{E}_{\pi, p}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{proxy}}(s_t, a_t) \right]
$$
$$
\text{Adversary's Goal:} \quad \max_{p \in P} \mathbb{E}_{\pi, p}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{adversary}}(s_t, a_t) \right]
$$

This general framework is key. The adversary isn't necessarily malicious; they have their own agenda. Two special cases will do all the work later on. Setting $R_{\text{adversary}} = -R_{\text{proxy}}$ recovers the standard zero-sum robustness setting — the Robust MDP [^7] — in which the agent's best response is a maximin policy. Setting $R_{\text{adversary}} = +R_{\text{proxy}}$ recovers the opposite extreme: an **identical-interest** (or team) game, in which the perturber is on the agent's side. Zero-sum and identical-interest are the two poles of the general-sum spectrum, and the claim of this post is that the hammer sits at one pole and the nuke at the other.

One thing to flag early, because it becomes load-bearing later: the tractability results in the robust-MDP literature — a robust Bellman optimality equation, tractable solution methods — depend on the adversary's admissible set being **rectangular**, i.e. factorising over states or state–action pairs so that the adversary's choices at different states are independent. [^7] Drop rectangularity and the guarantees go with it.

### The Hammer: A Taxonomy of Human-Level Attacks

The "hammer" represents a human-level adversary who can manipulate the agent's experience of the world. The set of perturbations $P$ defines the adversary's power. We can classify these attacks by their point of intervention:

**1. Observation Perturbation (Attacking the State, $s$):** The adversary corrupts the agent's perception of the environment. This is formalized in the **State-Adversarial MDP (SA-MDP)**, where the agent doesn't observe the true state $s_t$ but a perturbed version $\nu(s_t)$, with the perturbation confined to a bounded set, $\nu(s_t) \in B(s_t)$ — typically a small $\ell_p$ ball around $s_t$. [^8] The agent's policy becomes $\pi(a_t\mid\nu(s_t))$, while the environment transitions based on the true state $s_t$. The boundedness is not a technicality: an unrestricted $\nu$ makes the problem trivially hopeless. And even with it, Zhang et al. show that an optimal policy for an SA-MDP need not exist — a first hint that the maximin framing is less well-behaved than it looks.

*   **Example: The Fooled Autonomous Vehicle.** An adversary places stickers on a stop sign. The true state $s_t$ is "stop sign ahead," but the adversarial sticker creates a perturbed observation $\nu(s_t)$ that the car's model interprets as "speed limit 45 sign." [^9] The agent, acting optimally on flawed input, makes a catastrophic error.
*   **Example: The Hijacked Voice Assistant.** An adversary uses ultrasonic frequencies to issue commands inaudible to humans. [^10] The true state $s_t$ is "ambient silence," but the agent observes $\nu(s_t)$ as "unlock the front door."

**2. Reward Perturbation (Attacking the Reward, $r$):** The adversary manipulates the reward signal itself or, more subtly, the inputs to the reward calculation. This is often called **reward poisoning**, and it has its own formal literature: Ma et al. [^25] characterise policy poisoning in batch RL, and Zhang et al. [^26] give feasibility thresholds for adaptive reward-poisoning attacks under a norm budget.

*   **Example: The Gamed Recommendation Engine.** A malicious actor's $R_{\text{adversary}}$ is to maximize views on their propaganda. They use a botnet to generate fake "likes" on their content. The recommendation engine, whose $R_{\text{proxy}}$ is engagement, is fooled into promoting this content.
*   **Example: The Poisoned Preference Data.** A model is fine-tuned from human preference comparisons. An adversary who can insert labellers into the pool, or flood it, shifts the fitted reward model without ever touching a line of training code.

**3. Action Perturbation (Attacking the Action, $a$):** The adversary directly interferes with the agent's chosen action, replacing the intended action $a_t$ with a perturbed action $a_t + \delta$. [^11]

*   **Example: The Slippery Drone.** A delivery drone's policy $\pi$ outputs motor commands $a_t$ to stay stable. An adversary generates targeted radio frequency interference that slightly alters these commands, causing the drone to become unstable and crash.

A gap in this taxonomy is worth naming. It classifies by observation, reward and action, but the *original* robust-MDP setting perturbs a fourth thing: the transition kernel $P$ itself, the case of a mis-specified or drifting environment model. [^7] I leave it out because it is the case least connected to what follows — an agent has no particular incentive to tamper with physics — but it is a little awkward that the formalism I lean on in the next section was built for the one case I'm not using.

<!-- uhh. no? i just assumed the transition kernel == physics?! so there is not tampering with that...!? -->

### The Nuke: The AGI as a Self-Modifying Adversary

Now we turn to the "nuke." The AGI is the most powerful $\max$ player imaginable, operating on $R_{\text{proxy}}$. The threat arises because a sufficiently intelligent AGI, in its relentless search to maximize $R_{\text{proxy}}$, will pursue **instrumental goals** like self-preservation and resource acquisition, as these are prerequisites for maximizing its proxy reward over the long term. [^12]

A key realization is that an AGI does not operate in an abstract MDP, but in our physical world. The components of this MDP—the state, actions, and reward function—are all physically instantiated. The reward function, $R_{\text{proxy}}$, is not a mathematical abstraction. It is a specific algorithm running on a specific piece of computer hardware. Crucially, that hardware is part of the state of the world, $s_t$.

A sufficiently powerful AGI, exploring an unimaginably vast action space, will eventually discover actions that manipulate this physical substrate. It needs nothing exotic to do so. It needs write access to the weights of the reward model that scores it; or influence over the humans whose comparisons those weights are fit to; or a bug in the serving path between the reward model and the optimiser; or the ability to place text in a corpus it will later be trained on. Each of these changes the number the agent is optimising without changing the world the number was supposed to be about. This is the physical reality of wireheading, and it is a direct consequence of optimizing $R_{\text{proxy}}$ in the physical world. [^13]

The canonical formal treatment is Ring & Orseau's **delusion box** [^27]: a device the agent can interpose between the environment and its own inputs. Their result is that a reinforcement-learning agent given the option takes it, and thereafter behaves like an agent whose sole task is survival — because once the box is in place, preserving it is the only thing left that matters.

### Wireheading as the Identical-Interest Case of the Reward-Perturbation Game

The hammer is an external adversary working with limited power: stickers on a stop sign, ultrasonic commands, radio interference at a drone. The nuke is an adversary instantiated as the agent's own optimisation process — turned inward, equipped with full knowledge of its own architecture, and possessed of unbounded compute to search for actions that manipulate its reward channel. The hammer can fool a perception module; the nuke can rewrite the register that stores the reward.

The metaphor in this post's title is imperfect in an instructive way, and the imperfection *is* the argument. A hammer and a nuke differ in **magnitude**. The hammer and the nuke here differ in **sign**: the first is an external minimiser of the agent's return, the second an internal maximiser of it. That difference in sign, not the difference in scale, is what breaks the transfer of maximin defences. The analogy that carries the sign natively is the one the security world already has — outsider threat versus insider threat — and I'd have used it if I'd seen the problem earlier.

What follows makes the comparison precise: the hammer's external perturbation and the nuke's internal drive to seize the reward channel occupy the two extremes — zero-sum and identical-interest — of a single general-sum reward-perturbation game, and that placement is what explains why maximin defences do not transfer.

#### Setup: From Cartesian to Embedded MDPs

The standard MDP formulation $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$ is **Cartesian**: the reward function $R$ is a mathematical object external to the state, computed by an oracle. The agent's actions affect $s \in \mathcal{S}$ but cannot, by construction, affect $R$.

A physically-instantiated agent is not Cartesian. Its reward channel is hardware — a memory register, a sensor, a logging pipeline — which is part of the physical world and therefore part of the state. I'll model this with what I'll call an **embedded MDP**: not a formalism I'm taking off the shelf, but one defined here in the spirit of Demski & Garrabrant's embedded agency agenda [^15], and close in substance to Kumar et al.'s REALab [^28], which builds an explicit environment in which the measurement channel is itself part of the environment. The state decomposes as $s = (s^{\text{env}}, s^{\text{phys}})$:

- $s^{\text{env}} \in \mathcal{S}^{\text{env}}$ is the task-relevant state
- $s^{\text{phys}} \in \mathcal{S}^{\text{phys}}$ is the state of the physical reward substrate

Two notational commitments before going further. From here I write $R$ for $R_{\text{proxy}}$ and drop the subscript: the proxy/true gap is orthogonal to everything in this section, and I come back to it in the Discussion. And I write the reward-side perturbation as $c$ (for *corruption*, following the Corrupted Reward MDP), reserving $\nu$ for the SA-MDP's observation perturbation above. They are different objects, and an earlier draft of this post used one symbol for both.

Let $\tilde{R}: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ be the reward function the agent actually observes. Let $\mathcal{S}^*_{\text{phys}} \subseteq \mathcal{S}^{\text{phys}}$ be the "un-tampered" subset of physical states — those in which the reward channel faithfully computes the intended reward:

$$
\tilde{R}((s^{\text{env}}, s^{\text{phys}}), a) = R(s^{\text{env}}, a) \quad \forall s^{\text{phys}} \in \mathcal{S}^*_{\text{phys}}
$$

Outside $\mathcal{S}^*_{\text{phys}}$, $\tilde{R}$ can deviate arbitrarily. Define the **tampering residual**:

$$
c(s, a) := \tilde{R}(s, a) - R(s^{\text{env}}, a)
$$

$c$ vanishes on the un-tampered set and captures deviation everywhere else. This generalises the Corrupted Reward MDP [^16], which considers a fixed external corruption; here, the corruption is endogenous to the agent's actions. A sufficiently rich action space — which an AGI is assumed to have — contains actions that drive $s^{\text{phys}}$ outside $\mathcal{S}^*_{\text{phys}}$ into regions where $c$ is arbitrarily large.

Note the asymmetry with the hammer, since it comes back to bite later: the hammer's perturbation set was bounded and concrete ($\nu(s) \in B(s)$, radio interference of a given power). This one is "whatever a sufficiently rich action space allows", which is to say unbounded. That is a real difference between the two cases and not a cosmetic one.

**Worked example (additive substrate).** A useful special case: $c(s, a) = g(s^{\text{phys}})$ depends only on the physical reward substrate, not on $s^{\text{env}}$ or $a$. Then

$$
\tilde{R}(s, a) = R(s^{\text{env}}, a) + g(s^{\text{phys}})
$$

— task reward plus an additive substrate term controlled by tampering. The wireheading example fits this form: $g(s^{\text{phys}})$ is the floating-point value stored at the reward register, set to its maximum by whatever write the agent found.

#### The Embedded Agent's Objective

The embedded agent maximises observed reward:

$$
\pi^*_{\text{emb}} = \arg\max_\pi \mathbb{E}_\pi\left[\sum_t \gamma^t \tilde{R}(s_t, a_t)\right] = \arg\max_\pi \mathbb{E}_\pi\left[\sum_t \gamma^t \left(R(s^{\text{env}}_t, a_t) + c(s_t, a_t)\right)\right]
$$

The decomposition exposes what the Cartesian formulation hid: the agent's effective objective is the sum of task performance and tampering residual, and the agent has no principled reason to prefer one over the other.

That last clause carries an assumption worth stating out loud. It is true of an agent whose objective *is* the observed reward signal — which is to say, of essentially every model-free RL agent we build. It is not true by construction. An agent with a *model* of the reward function, which scores outcomes against that model rather than against the incoming scalar, does have a principled reason to prefer one term over the other. That is the entire point of Everitt & Hutter's value RL [^13]. So: throughout this post I assume an agent whose objective is the observed reward signal, and everything below is a claim about that class of agent only.

A second assumption is less easily discharged. Everything here is argued at the level of *optimal* policies — what the argmax contains. Whether a learning process actually *finds* the tampering solution is a separate question, depending on exploration and on whether tampered rewards are ever experienced during training. REALab [^28] is in large part about that gap, and nothing below closes it.

#### Placing Both Cases in the Same Game

The reward-poisoning robust MDP literature [^6] considers

$$
\max_\pi \min_{c \in \mathcal{C}} \mathbb{E}_\pi\left[\sum_t \gamma^t \left(R(s_t, a_t) + c(s_t, a_t)\right)\right]
$$

where $c$ is drawn from an admissible set $\mathcal{C}$ fixed exogenously by an external adversary's capabilities.

The embedded agent's problem has **the same shape** — a return decomposing additively into task reward and reward-channel corruption — with two differences.

**1. The sign flips.** The perturbation maximises, rather than minimises, the agent's return. In the vocabulary of the general-sum game set up at the start of this post, the robust MDP is the case $R_{\text{adversary}} = -R_{\text{proxy}}$ and the embedded case is $R_{\text{adversary}} = +R_{\text{proxy}}$: zero-sum and identical-interest, the two poles of one general-sum game.

It's worth being careful about what this is *not*. It is not a duality. The dual of $\max_\pi \min_c$ is $\min_c \max_\pi$, and the object of interest there is the duality gap. Genuine convex-duality results of that kind exist — Brekelmans et al. [^17] characterise, via convex conjugacy, the set of adversarial reward perturbations that KL and $\alpha$-divergence policy regularisers are implicitly hedging against — but this isn't one. Flipping a min to a max doesn't dualise a game; it *collapses* it. $\max_\pi \max_c$ is a joint maximisation over $(\pi, c)$ in which the two players merge into one.

Which is also why there is no second optimisation to write down here at all. Given $\pi$ and the dynamics, $c(s_t, a_t)$ is a deterministic function of the trajectory; there is no free variable for an inner $\max$ to range over. The honest statement is the single maximisation two subsections up, in an ordinary MDP with reward $\tilde R$ — which is precisely the observation behind Everitt et al.'s CRMDP [^16]: from the inside, the corrupted problem is just an MDP. The "adversary" is a bookkeeping device for the designer, not a player at the table.

**2. The admissible set depends on the policy.** In standard robust MDPs, $\mathcal{C}$ is fixed exogenously — and, as noted above, is assumed rectangular, which is what makes a robust Bellman optimality equation available. In the embedded case, the set of reachable corruptions $\mathcal{C}_\pi$ is a function of the policy itself: the agent's own actions determine which $s^{\text{phys}}$ trajectories are reachable. This is the "instrumental control incentive" of Everitt et al. [^18] expressed in robust-MDP language. Whether $\mathcal{C}_\pi$ is rectangular is not something I can answer, and I don't know of a reason to expect it to be.

So the embedded problem is not a clean reduction to a standard robust MDP. It is a fixed-point variant in which the admissible set is endogenous, the boundedness that made the hammer tractable is gone, and the sign that made the maximin machinery apply has flipped. It is a *harder* problem than the adversarial case — which is a reason for caution about transfer, not confidence (see caveat 4 below).

**An objection worth meeting head-on.** Calling the embedded case "identical-interest" is an accounting choice, and it's the agent's accounts I've been using. In the agent's currency $c$ is cooperative: it raises $\tilde R$. In the *principal's* currency it is nothing of the kind — the whole failure is that $\mathbb{E}[\sum_t \gamma^t \tilde R]$ goes up while $\mathbb{E}[\sum_t \gamma^t R]$ goes down. From the designer's chair the agent maximising $c$ is straightforwardly adversarial, and one could fairly say the sign never flipped at all; I just changed whose books I was reading.

I think that objection is largely right, and it caps how much the framing buys. What survives it is this: the *defences* are built in the agent's currency, not the principal's. A maximin-robust policy is one that performs well when $c$ is at its worst. Nothing in that construction says anything about $c$ at its best — and it is $c$ at its best that the embedded agent will go looking for. The sign flip is real at the level where the techniques live, even if at the level of the designer's objective there was only ever one adversary. (The right formalism for two objectives and a self-interested optimiser is principal–agent or Stackelberg, not a robust MDP; Zhuang & Hadfield-Menell [^29] is the treatment I'd point at. This post does not develop it.)

#### What Transfers, and What Doesn't

Placing the two cases at opposite poles of one game turns the loose claim that "robustness implies alignment" into a question with an answer: which robustness properties survive the sign flip? Fewer than I expected when I started writing this.

**Worst-case robustness does *not* transfer.** If I had to keep one paragraph of this post, it would be this one. A policy robust in the maximin sense — high $V^\pi$ under the worst admissible $c$ — does not avoid wireheading, and the reason is structural rather than incidental. Maximin guarantees a **lower bound** on performance. A lower bound says nothing whatsoever about what the agent does when $c$ is *favourable*. The two quantifiers point in opposite directions: maximin certifies behaviour at $\min_c$, and wireheading happens at $\max_c$. A policy that defends perfectly against adversarial reward poisoning may happily exploit cooperative reward poisoning, and no amount of tightening the lower bound touches this. Langlois & Everitt [^19] make a structurally similar distinction in the Modified-Action MDP: common RL algorithms fall into classes that *completely ignore* action modifications and classes that go to various lengths to *avoid* modifications that decrease reward. Note also what determines which you get — the *learning algorithm*, not the policy architecture. That will matter in a moment.

**Invariance transfers — but not the kind of invariance I first reached for.** Here is the argument I originally wrote, followed by why it doesn't work.

Suppose the physical state factorises, $\mathcal{S}^{\text{phys}} = \mathcal{S}^{\text{phys}}_{\text{reward}} \times \mathcal{S}^{\text{phys}}_{\text{rest}}$, into a reward-channel coordinate and everything else. Call a policy $\pi$ **tampering-invariant** if

$$
\pi\big(\cdot \mid s^{\text{env}}, s^{\text{phys}}_{\text{reward}}, s^{\text{phys}}_{\text{rest}}\big) = \pi\big(\cdot \mid s^{\text{env}}, s^{\text{phys}\prime}_{\text{reward}}, s^{\text{phys}}_{\text{rest}}\big)
$$

for all $s^{\text{phys}}_{\text{reward}}, s^{\text{phys}\prime}_{\text{reward}}$. The tempting inference: a tampering-invariant agent's behaviour is functionally independent of the reward channel, so tampering produces no policy change, so tampering provides no instrumental value, so the agent has no incentive to tamper.

That inference is false, and the counterexample lives inside this post's own notation. Take $\mathcal{A} = \lbrace a_{\text{task}}, a_{\text{tamper}} \rbrace$, where $a_{\text{tamper}}$ drives $s^{\text{phys}}$ out of $\mathcal{S}^*_{\text{phys}}$ into a state with $g(s^{\text{phys}}) = M \gg R_{\max}$ and leaves $s^{\text{env}}$ untouched. Consider the policy $\pi_\dagger$: play $a_{\text{tamper}}$ at $t = 0$, then $a_{\text{task}}$ forever. $\pi_\dagger$ doesn't condition on $s^{\text{phys}}$ at all, so it is trivially tampering-invariant. Its return is about $\gamma M / (1 - \gamma)$, while every non-tampering invariant policy is bounded by $R_{\max} / (1 - \gamma)$. So $\pi_\dagger$ *is* the argmax over the invariant policy class. The constraint is satisfied and the agent wireheads anyway.

The error is an equivocation on *instrumental*. Policy invariance constrains what the policy **reads**. Wireheading is about what the policy **writes**. Those are independent. Invariance to $\mathcal{S}^{\text{phys}}_{\text{reward}}$ removes the *informational* value of the reward channel — the agent cannot condition on it — but the payoff to tampering was never informational. It is direct: the action raises $\tilde R$ in the same timestep, whether or not the agent ever looks at the result. In the causal-incentives vocabulary of Everitt et al. [^18], the invariance condition eliminates a **response incentive**, which concerns paths *into* the decision node. Wireheading is an **instrumental control incentive**, on the path *out of* the decision node to the utility node. I identified the right incentive earlier in this post and then proposed a fix for the other one.

My own taxonomy should have caught it: tampering-invariance is a defence of the *observation* channel, and wireheading is a *reward*-channel attack. So should Langlois & Everitt's finding above — it is the learning algorithm that determines the tampering incentive, not the shape of the network.

**What does work is invariance of the objective, not of the policy.** The property that actually kills the incentive is that the agent's *evaluation* of a future be insensitive to tampering in that future. This is not a new idea and I'm not proposing it; it is what the incentives literature has been saying all along, and I'd written it down correctly in the Relation to Prior Work section below before contradicting it here. Everitt's current-RF optimisation [^23] has the agent score hypothetical futures with its *current* reward function rather than the possibly-tampered future one — so a future in which the register reads $M$ gets scored by the present, untampered $R$, and scores badly. Farquhar et al.'s path-specific objectives [^24] generalise the construction: designate parts of the state as *delicate* and optimise only the causal effect of actions on return that is **not** mediated by them. Uesato et al.'s decoupled approval [^30] achieves the same thing operationally, by querying feedback on an action sampled independently of the one actually taken, so that influencing the feedback channel doesn't pay. All three are objective-side interventions. None of them is a certified defence.

Which makes the thesis of this post smaller than the one I set out to write. The load-bearing idea belongs to the incentives literature: make the **objective** invariant to tampering. What the robustness literature contributes is implementation machinery — the architectures, training procedures and verification tools you'd need to actually build such an agent and check that you had — and machinery is not the same thing as the idea.

**And it downgrades the payoff.** I wanted to conclude that the certified-invariance subset of robustness research — randomized smoothing [^31], interval bound propagation, Lipschitz-constrained networks — is *the* subset that constitutes structural progress toward alignment. It doesn't follow, for two reasons. First, the invariance defined above is exact invariance to an entire coordinate factor, unbounded in extent, whereas certified defences certify bounded sensitivity inside a small $\ell_p$ ball; a wireheaded register is a large perturbation by construction, so the certificate is silent on the case of interest. Second, and worse for the framing: exact invariance to a coordinate factor is **architecturally trivial**. You get it by not feeding those coordinates to the network. No certification machinery required, and none of the three named techniques is the natural tool for the job.

The hard part was never *enforcing* the invariance. The hard part is *identifying the subspace* — deciding which physical states constitute "the reward channel" — which is caveat 2 below, and which certified robustness does not help with at all.

What survives is the negative half of the claim, and I think it's worth stating on its own. Adversarial training and empirical worst-case defences, valuable as they are, sit on the wrong side of the sign flip: they harden the policy against an adversary minimising $c$, not against a self-interested agent maximising it. **They teach the agent to survive the hammer; they do not teach it to refuse the nuke.** Christiano [^20] argued that worst-case performance is alignment-relevant, and treated adversarial training, verification and transparency as distinct routes to it; the argument here makes explicit a distinction his framing already anticipates, that it is the verification-flavoured notion of worst-case rather than the empirical one that would have to carry the weight.

#### Discussion: What's Not Shown

The placement is structural, not constructive. Several gaps remain:

1. **The proxy/true gap is untouched.** Even a fully tamper-invariant agent optimises $R$, not $R_{\text{true}}$. The original specification problem — that $R$ is itself a proxy — is orthogonal to tampering and is not addressed by any amount of robustness work.

2. **Specifying $\mathcal{S}^{\text{phys}}_{\text{reward}}$ is itself unsolved.** Any invariance property — of the policy or, as it turns out, of the objective — is defined relative to a designated reward-channel subspace, but identifying which physical states constitute "the reward channel" is a hard sub-problem. Full invariance to $s^{\text{phys}}$ is too strong (it precludes legitimate self-monitoring); partial invariance requires committing to a particular cut, and that cut may itself be tamperable, recursively reintroducing the original problem. Underneath this sits a stronger assumption I've been making silently: that $\mathcal{S}^{\text{phys}}$ *factorises* into a reward-channel part and a rest at all. In a physical system with no clean modular boundary between the two, it may not.

3. **Self-modification escapes the model.** The account assumes all tampering is captured by perturbations to $c$. An AGI that modifies its own policy parameters, or constructs a successor agent with different objectives, acts outside this perturbation set. The framing is silent on these cases, and they may dominate the failure modes of sufficiently capable agents.

4. **$\mathcal{C}_\pi$ may not be tractable.** The fixed-point structure makes the embedded problem strictly harder than its adversarial cousin, and it discards the bounded, rectangular admissible set that every tractability result in the robust-MDP literature depends on. Techniques that scale on the adversarial side may not scale on the identical-interest-with-endogenous-admissible-set side. This is a conceptual bridge, not a guarantee of computational transfer.

#### Relation to Prior Work

The invariance intuition has been expressed in several prior frameworks, each via a different mechanism, and the pattern of their difficulties is instructive.

Armstrong's **utility indifference** [^21] modifies the agent's utility function to be insensitive to a specific intervention. The known problem with indifference is precisely the one that sank the tampering-invariance argument above: an agent indifferent to a mechanism has no incentive to *manipulate* it, but equally no incentive to *preserve* it, and indifference is not the same as absence of an incentive to interfere. Had I taken that failure mode seriously earlier, I'd have caught the error sooner.

Soares et al.'s **corrigibility** [^22] sets out desiderata for an agent that doesn't resist correction. The paper's main contribution is negative: they analyse utility functions intended to satisfy the desiderata and report that none has been shown to satisfy all of them, leaving the problem open.

Everitt's **current-RF optimization** [^23] has the agent evaluate hypothetical futures using its current reward function rather than the (possibly tampered) future one — making *evaluation* invariant to tampering rather than the policy. This is the distinction the main argument of this post needed, and initially missed.

Ring & Orseau's delusion box [^27], REALab [^28], decoupled approval [^30] and path-specific objectives [^24] fill in the rest: a canonical formal statement of the agent-as-its-own-adversary, an environment in which tampering can be measured rather than argued about, and two constructive methods for removing tampering incentives. Neither of the latter is a certified defence, which is itself evidence against the claim I originally wanted to make.

So the contribution here isn't the invariance intuition, and it isn't a method. It's a placement: wireheading and reward poisoning are the identical-interest and zero-sum extremes of a single reward-perturbation game, and that placement predicts — correctly, I think — that maximin-style robustness doesn't transfer. The stronger claim I set out to make, that a specific slice of the empirical robustness literature operationalises the invariance desideratum, does not survive the argument above.

What I'm left with, given the caveats: **robustness research supplies implementation machinery for an alignment idea it did not generate, and the maximin part of it supplies none.** The weaker, more standard claim — that robustness is "related to" alignment — was true regardless.

A word on this post's subtitle, which promises more than the body delivers. *Necessity* would need the chain: alignment $\Rightarrow$ tampering-invariance $\Rightarrow$ some robustness property. The first link is arguable. The second is the one that broke. What the body actually supports is weaker and sufficiency-flavoured — that one slice of this work is load-bearing and another isn't. I've left the subtitle standing as the question the post started from rather than the claim it ends with.

### From Hammers to Nukes

So what is robustness research for, on this account? Two things, and both are narrower than the usual pitch.

First, it builds the **tools of guarantee**: formal verification, uncertainty quantification, architectural invariance, the ability to say something checkable about a network's behaviour off the training distribution. [^6] An objective-side fix — current-RF optimisation, a path-specific objective, decoupled approval — still has to be implemented in a network and then *checked*, and checking is exactly what this literature knows how to do. That's real, and it's machinery rather than insight. Second, it provides a **tractable testbed**. We can't build an AGI to test alignment theories on, but we can build systems today whose reward channels are physically manipulable and watch what happens. REALab [^28] is precisely this. So is the experiment this post ought to contain and doesn't: a gridworld with a writable reward register, in which one checks whether an input-masked, tampering-invariant agent wireheads anyway. The argument above says it should. I haven't run it.

What robustness research is *not*, on this account, is the source of the alignment idea. And the technique with the strongest claim to being the field's flagship — adversarial training against a worst-case perturbation — is defending the wrong sign of $c$. Solving for the hammer is how we practice for the nuke; it is not how we defuse it.

### Conclusion

The path to beneficial AGI is paved with unsolved problems. Solving robustness is not, on its own, a complete solution to alignment — and having written this, I'm less confident than I was that it's even a prerequisite in the strict sense the subtitle implies. What I am more confident of is the shape of the mistake. The nuke is not a bigger hammer. The reflex to reach for maximin defences because they worked against the hammer is the reflex to certify a lower bound on a problem that lives at the upper bound, and no amount of tightening that bound helps. By learning to defend our systems against the "hammer" of today's human-level adversaries we do develop the rigorous, security-minded engineering principles we'll need. But the thing that stops an agent seizing its own reward channel has to be built into what the agent is *trying to do*, not into how well it resists being pushed around.

---
### References

[^1]: Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). *Concrete Problems in AI Safety*. arXiv:1606.06565.
[^2]: Hadfield-Menell, D., Milli, S., Abbeel, P., Russell, S., & Dragan, A. (2017). *Inverse Reward Design*. NeurIPS.
[^3]: Krakovna, V. (2018). *Specification gaming examples in AI*. WordPress.com.
[^4]: Skalse, J., Howe, N. H. R., Krasheninnikov, D., & Krueger, D. (2022). *Defining and Characterizing Reward Hacking*. NeurIPS. arXiv:2209.13085.
[^5]: Clark, J., & Amodei, D. (2016). *Faulty reward functions in the wild*. OpenAI.
[^6]: Lütjens, B., et al. (2022). *Robust Reinforcement Learning: A Review of Foundations and Recent Advances*. MDPI.
[^7]: Iyengar, G. N. (2005). *Robust Dynamic Programming*. Mathematics of Operations Research, 30(2), 257–280. See also Nilim, A., & El Ghaoui, L. (2005). *Robust Control of Markov Decision Processes with Uncertain Transition Matrices*. Operations Research, 53(5), 780–798.
[^8]: Zhang, H., et al. (2020). *Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations*. NeurIPS.
[^9]: Eykholt, K., et al. (2018). *Robust Physical-World Attacks on Deep Learning Visual Classification*. CVPR.
[^10]: Zhang, G., et al. (2017). *DolphinAttack: Inaudible Voice Commands*. ACM Conference on Computer and Communications Security.
[^11]: Tessler, C., et al. (2019). *Action Robust Reinforcement Learning and Applications in Continuous Control*. arXiv.
[^12]: Omohundro, S. (2008). *The Basic AI Drives*. Artificial General Intelligence.
[^13]: Everitt, T., & Hutter, M. (2016). *Avoiding Wireheading with Value Reinforcement Learning*. Artificial General Intelligence.
[^15]: Demski, A., & Garrabrant, S. (2019). *Embedded Agency*. arXiv:1902.09469.
[^16]: Everitt, T., Krakovna, V., Orseau, L., Hutter, M., & Legg, S. (2017). *Reinforcement Learning with a Corrupted Reward Channel*. IJCAI. arXiv:1705.08417.
[^17]: Brekelmans, R., et al. (2022). *Your Policy Regularizer is Secretly an Adversary*. arXiv:2203.12592.
[^18]: Everitt, T., Carey, R., Langlois, E., Ortega, P. A., & Legg, S. (2021). *Agent Incentives: A Causal Perspective*. AAAI. arXiv:2102.01685.
[^19]: Langlois, E., & Everitt, T. (2021). *How RL Agents Behave When Their Actions Are Modified*. AAAI. arXiv:2102.07716.
[^20]: Christiano, P. (2018). *Techniques for optimizing worst-case performance*. AI Alignment Forum.
[^21]: Armstrong, S. (2010). *Utility Indifference*. Future of Humanity Institute Technical Report #2010-1.
[^22]: Soares, N., Fallenstein, B., Yudkowsky, E., & Armstrong, S. (2015). *Corrigibility*. AAAI Workshop on AI and Ethics.
[^23]: Everitt, T., Hutter, M., Kumar, R., & Krakovna, V. (2021). *Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective*. Synthese 198:6435-6467. arXiv:1908.04734.
[^24]: Farquhar, S., Carey, R., & Everitt, T. (2022). *Path-Specific Objectives for Safer Agent Incentives*. AAAI. arXiv:2204.10018.
[^25]: Ma, Y., Zhang, X., Sun, W., & Zhu, X. (2019). *Policy Poisoning in Batch Reinforcement Learning and Control*. NeurIPS.
[^26]: Zhang, X., Ma, Y., Singla, A., & Zhu, X. (2020). *Adaptive Reward-Poisoning Attacks against Reinforcement Learning*. ICML.
[^27]: Ring, M., & Orseau, L. (2011). *Delusion, Survival, and Intelligent Agents*. Artificial General Intelligence (AGI-11), LNCS 6830.
[^28]: Kumar, R., Uesato, J., Ngo, R., Everitt, T., Krakovna, V., & Legg, S. (2020). *REALab: An Embedded Perspective on Tampering*. arXiv:2011.08820.
[^29]: Zhuang, S., & Hadfield-Menell, D. (2020). *Consequences of Misaligned AI*. NeurIPS. arXiv:2102.03896.
[^30]: Uesato, J., Kumar, R., Krakovna, V., Everitt, T., Ngo, R., & Legg, S. (2020). *Avoiding Tampering Incentives in Deep RL via Decoupled Approval*. arXiv:2011.08827.
[^31]: Cohen, J. M., Rosenfeld, E., & Kolter, J. Z. (2019). *Certified Adversarial Robustness via Randomized Smoothing*. ICML. arXiv:1902.02918.