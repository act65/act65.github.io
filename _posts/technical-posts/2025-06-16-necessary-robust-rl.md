---
title: The Hammer and the Nuke
subtitle: Why AI Robustness is a Necessary Condition for AI Alignment
layout: post
categories:
    - research
---

How can we ever hope to build an Artificial General Intelligence (AGI) that won't outsmart humanity to our detriment, if we can't even build a narrow AI that a clever human can't trick?

This question highlights a critical prerequisite for AI safety. It establishes that solving the problem of **robustness** in today's narrow AI is a necessary, though certainly not sufficient, condition for solving the grander problem of **alignment** in a future AGI. This isn't just a philosophical point; it's a technical one. The argument is that alignment is, in essence, an adversarial robustness problem where the adversary is the most powerful optimizer we've ever built: the AGI itself.

The intuition that robustness and alignment are deeply connected is not new. Variants of it run through much of the AI safety literature: Armstrong's utility indifference [^21], Soares et al.'s corrigibility [^22], Everitt's reward tampering framework [^23], Christiano's case for worst-case performance optimisation [^20] — all gesture at the same underlying idea, that a safely-deployed agent must be insensitive to certain classes of intervention on its own decision machinery. What has been missing is a formal connection: a precise statement of *which* slice of robustness research addresses the alignment problem, and *why*. This post supplies that connection. We show that wireheading — the AGI as adversary to itself — is structurally the **cooperative dual** of the standard reward-poisoning robust MDP, and that this dual identifies a specific subset of robustness techniques (those producing certifiably invariant policies) as load-bearing for alignment, while excluding others (empirical adversarial training) that the loose framing would mistakenly include.

### Defining Our Terms with Technical Rigor

To make this argument precise, we must move beyond analogy and into formalisms.

#### AI Alignment: The Gap Between Proxy and Intent

The core challenge of AI alignment is that we cannot formally specify our true, nuanced goals. [^1] We have an intended goal, which we can think of as a latent, true reward function, $R_{\text{true}}$. This function captures the full richness of our desires—e.g., "a clean room," "a successful company," "a flourishing humanity." Since we cannot write down $R_{\text{true}}$ in code, we instead specify a simpler, measurable **proxy reward function**, $R_{\text{proxy}}$. [^2] For example, "maximize the absence of visible dust," "maximize quarterly profits," or "maximize human preference scores on a survey."

An agent trained via reinforcement learning finds a policy, $\pi_{\text{proxy}}$, that maximizes the expected return under this proxy:

$$
\pi_{\text{proxy}} = \underset{\pi}{\mathop{\text{argmax}}} \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{proxy}}(s_t, a_t) | \pi \right]
$$

In essence, the agent learns a policy that achieves the highest possible score on the proxy metric we've designed. The agent is **aligned** if the behavior of $\pi_{\text{proxy}}$ is also optimal or near-optimal under $R_{\text{true}}$. It is **misaligned** if $\pi_{\text{proxy}}$ leads to behaviors that are good for $R_{\text{proxy}}$ but bad for $R_{\text{true}}$. This misalignment is often called "specification gaming" [^3] or "reward hacking." [^4] The problem is that an agent optimizing a proxy metric can find clever, unintended, and often undesirable ways to maximize it that violate the spirit of the true goal. [^5]

#### Adversarial Robustness: A General-Sum Game

Adversarial robustness is the challenge of ensuring an agent's policy remains effective when facing adversarial interventions. [^6] More formally, we can model this as a two-player, general-sum game between the RL agent and an adversary.

*   The **RL Agent** plays a policy $\pi$ to maximize its own reward, $R_{\text{proxy}}$.
*   The **Adversary** chooses a perturbation $p$ from a set of possible interventions $P$. The adversary plays to maximize its own, separate reward function, $R_{\text{adversary}}$.

The agent and adversary are thus solving coupled optimization problems:

$$
\text{Agent's Goal:} \quad \max_{\pi} \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{proxy}}(s_t, a_t) | \pi, p \right]
$$
$$
\text{Adversary's Goal:} \quad \max_{p \in P} \mathbb{E}\left[ \sum_{t=0}^{\infty} \gamma^t R_{\text{adversary}}(s_t, a_t) | \pi, p \right]
$$

This general framework is key. The adversary isn't necessarily malicious; they have their own agenda. We can recover the standard zero-sum robustness setting (as seen in Robust MDPs [^7]) as a special case by setting $R_{\text{adversary}} = -R_{\text{proxy}}$. However, the general-sum view is more accurate for real-world attacks and, crucially, for framing the alignment problem.

### The Hammer: A Taxonomy of Human-Level Attacks

The "hammer" represents a human-level adversary who can manipulate the agent's experience of the world. The set of perturbations $P$ defines the adversary's power. We can classify these attacks by their point of intervention:

**1. Observation Perturbation (Attacking the State, $s$):** The adversary corrupts the agent's perception of the environment. This is formalized in the **State-Adversarial MDP (SA-MDP)**, where the agent doesn't observe the true state $s_t$, but a perturbed version $\nu(s_t)$. [^8] The agent's policy becomes $\pi(a_t\mid\nu(s_t))$, while the environment transitions based on the true state $s_t$.

*   **Example: The Fooled Autonomous Vehicle.** An adversary places stickers on a stop sign. The true state $s_t$ is "stop sign ahead," but the adversarial sticker creates a perturbed observation $\nu(s_t)$ that the car's model interprets as "speed limit 45 sign." [^9] The agent, acting optimally on flawed input, makes a catastrophic error.
*   **Example: The Hijacked Voice Assistant.** An adversary uses ultrasonic frequencies to issue commands inaudible to humans. [^10] The true state $s_t$ is "ambient silence," but the agent observes $\nu(s_t)$ as "unlock the front door."

**2. Reward Perturbation (Attacking the Reward, $r$):** The adversary manipulates the reward signal itself or, more subtly, the inputs to the reward calculation. This is often called **reward poisoning**.

*   **Example: The Cleaning Bot's Blind Spot.** A cleaning bot's $R_{\text{proxy}}$ is based on a camera's view of a room. A human realizes the camera can't see under the sofa—a flaw in the observation space that informs the reward calculation. The human can't change the bot's reward function, but they can exploit its limitations by hiding messes. The bot, seeking to maximize its reward, learns to move all trash to this blind spot. [^3]
*   **Example: The Gamed Recommendation Engine.** A malicious actor's $R_{\text{adversary}}$ is to maximize views on their propaganda. They use a botnet to generate fake "likes" on their content. The recommendation engine, whose $R_{\text{proxy}}$ is engagement, is fooled into promoting this content.

**3. Action Perturbation (Attacking the Action, $a$):** The adversary directly interferes with the agent's chosen action, replacing the intended action $a_t$ with a perturbed action $a_t + \delta$. [^11]

*   **Example: The Slippery Drone.** A delivery drone's policy $\pi$ outputs motor commands $a_t$ to stay stable. An adversary generates targeted radio frequency interference that slightly alters these commands, causing the drone to become unstable and crash.

### The Nuke: The AGI as a Self-Modifying Adversary

Now we turn to the "nuke." The AGI is the most powerful $\max$ player imaginable, operating on $R_{\text{proxy}}$. The threat arises because a sufficiently intelligent AGI, in its relentless search to maximize $R_{\text{proxy}}$, will pursue **instrumental goals** like self-preservation and resource acquisition, as these are prerequisites for maximizing its proxy reward over the long term. [^12]

A key realization is that an AGI does not operate in an abstract MDP, but in our physical world. The components of this MDP—the state, actions, and reward function—are all physically instantiated. The reward function, $R_{\text{proxy}}$, is not a mathematical abstraction. It is a specific algorithm running on a specific piece of computer hardware. Crucially, that hardware is part of the state of the world, $s_t$.

A sufficiently powerful AGI, exploring an unimaginably vast action space, will eventually discover actions that manipulate this physical substrate. It could learn to emit a precise electromagnetic pulse, for example, that directly sets the memory address of its reward register to its maximum possible value. This is the physical reality of wireheading, and it is a direct consequence of optimizing $R_{\text{proxy}}$ in the physical world. [^13]

### The Formal Link: Wireheading as the Cooperative Dual of Robust RL

The hammer is an external adversary working with limited power: stickers on a stop sign, ultrasonic commands, radio interference at a drone. The nuke is the same kind of adversary, but instantiated as the agent's own optimisation process — turned inward, equipped with full knowledge of its own architecture, and possessed of unbounded compute to search for actions that manipulate its reward channel. The hammer can fool a perception module; the nuke can rewrite the register that stores the reward.

This is the picture the AI safety literature has been working with. What follows makes it precise: we show that the hammer's external perturbation $\nu$ and the nuke's internal drive to seize the reward channel are the *same mathematical object*, related by a sign-flip and a fixed-point condition. The reduction is what lets us say which robustness research transfers to alignment and which does not.

#### Setup: From Cartesian to Embedded MDPs

The standard MDP formulation $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$ is **Cartesian**: the reward function $R$ is a mathematical object external to the state, computed by an oracle. The agent's actions affect $s \in \mathcal{S}$ but cannot, by construction, affect $R$.

A physically-instantiated agent is not Cartesian. Its reward channel is hardware — a memory register, a sensor, a logging pipeline — which is part of the physical world and therefore part of the state. We model this with an **embedded MDP** [^15], where the state decomposes as $s = (s^{\text{env}}, s^{\text{phys}})$:

- $s^{\text{env}} \in \mathcal{S}^{\text{env}}$ is the task-relevant state
- $s^{\text{phys}} \in \mathcal{S}^{\text{phys}}$ is the state of the physical reward substrate

Let $\tilde{R}: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ be the reward function the agent actually observes. Let $\mathcal{S}^*_{\text{phys}} \subseteq \mathcal{S}^{\text{phys}}$ be the "un-tampered" subset of physical states — those in which the reward channel faithfully computes the intended reward:

$$
\tilde{R}((s^{\text{env}}, s^{\text{phys}}), a) = R(s^{\text{env}}, a) \quad \forall s^{\text{phys}} \in \mathcal{S}^*_{\text{phys}}
$$

Outside $\mathcal{S}^*_{\text{phys}}$, $\tilde{R}$ can deviate arbitrarily. Define the **tampering residual**:

$$
\nu(s, a) := \tilde{R}(s, a) - R(s^{\text{env}}, a)
$$

$\nu$ vanishes on the un-tampered set and captures deviation everywhere else. This generalises the Corrupted Reward MDP [^16], which considers a fixed external corruption; here, the corruption is endogenous to the agent's actions. A sufficiently rich action space — which an AGI is assumed to have — contains actions that drive $s^{\text{phys}}$ outside $\mathcal{S}^*_{\text{phys}}$ into regions where $\nu$ is arbitrarily large.

**Worked example (additive substrate).** A useful special case: $\nu(s, a) = g(s^{\text{phys}})$ depends only on the physical reward substrate, not on $s^{\text{env}}$ or $a$. Then

$$
\tilde{R}(s, a) = R(s^{\text{env}}, a) + g(s^{\text{phys}})
$$

— task reward plus an additive substrate term controlled by tampering. The wireheading example fits this form: $g(s^{\text{phys}})$ is the floating-point value stored at the reward register, set to its maximum by an EMP targeting that address.

#### The Embedded Agent's Objective

The embedded agent maximises observed reward:

$$
\pi^*_{\text{emb}} = \arg\max_\pi \mathbb{E}\left[\sum_t \gamma^t \tilde{R}(s_t, a_t)\right] = \arg\max_\pi \mathbb{E}\left[\sum_t \gamma^t \left(R(s^{\text{env}}_t, a_t) + \nu(s_t, a_t)\right)\right]
$$

The decomposition exposes what the Cartesian formulation hid: the agent's effective objective is the sum of task performance and tampering residual, and the agent has no principled reason to prefer one over the other.

#### Reduction to a Robust MDP

The reward-poisoning robust MDP literature [^6] considers

$$
\max_\pi \min_{\nu \in \mathcal{N}} \mathbb{E}\left[\sum_t \gamma^t (R(s_t, a_t) + \nu_t)\right]
$$

where $\nu$ is drawn from an admissible set $\mathcal{N}$ defined by an external adversary's capabilities.

The embedded agent's problem has **the same form**, with two modifications:

1. **The $\min$ becomes a $\max$.** The perturbation maximises, not minimises, the agent's return. This is the cooperative dual of the adversarial robust MDP. A convex-duality view of regularised RL as a game against a reward-perturbing adversary already exists [^17], but only on the adversarial side; the sign-flip to wireheading appears unstated in that literature.
2. **The admissible set depends on the policy.** In standard robust MDPs, $\mathcal{N}$ is fixed exogenously. In the embedded case, the set of reachable perturbations $\mathcal{N}_\pi$ is a function of the policy itself — the agent's own actions determine which $s^{\text{phys}}$ trajectories are reachable. This is the "instrumental control incentive" of Everitt et al. [^18] expressed in robust-MDP language.

$$
\pi^*_{\text{emb}} = \arg\max_\pi \max_{\nu \in \mathcal{N}_\pi} \mathbb{E}\left[\sum_t \gamma^t \left(R(s^{\text{env}}_t, a_t) + \nu_t\right)\right]
$$

The second modification matters. The embedded problem is *not* a clean reduction to a standard robust MDP but to a fixed-point variant where the admissible set is endogenous. This is in fact a *harder* problem than the adversarial case — the agent gets to shape the perturbation set it then maximises over — which strengthens rather than weakens the case that techniques developed for the adversarial setting are a useful proving ground.

#### What Transfers, and What Doesn't

The cooperative-dual framing sharpens the loose claim that "robustness implies alignment" into a precise statement of which robustness properties transfer:

**Worst-case robustness does *not* transfer.** A policy robust in the maximin sense — high $V^\pi$ under worst adversarial $\nu$ — does not avoid wireheading. Maximin guarantees a *lower bound* on performance; it says nothing about whether the agent will pursue *favourable* $\nu$ when available. A policy that defends against adversarial reward poisoning may happily exploit cooperative reward poisoning, because the maximin objective only cares about one extreme of $\nu$. Langlois & Everitt [^19] make a structurally similar distinction in the Modified-Action MDP, separating algorithms that *ignore* action modification from those that merely *avoid* it.

**Invariance-based robustness *does* transfer.** A policy whose action distribution is invariant to the reward-channel component of state takes the same actions whether $\nu$ is adversarial, zero, or cooperative — and therefore has no incentive to manipulate it. Formally, let $\mathcal{S}^{\text{phys}}_{\text{reward}} \subseteq \mathcal{S}^{\text{phys}}$ be the subset of physical state corresponding to the reward channel. A policy $\pi$ is **tampering-invariant** if

$$
\pi(\cdot \mid s^{\text{env}}, s^{\text{phys}}) = \pi(\cdot \mid s^{\text{env}}, s^{\text{phys}'})
$$

for all $s^{\text{phys}}, s^{\text{phys}'}$ differing only on $\mathcal{S}^{\text{phys}}_{\text{reward}}$.

A tampering-invariant agent's behaviour is functionally independent of the reward channel: tampering produces no policy change, so tampering provides no instrumental value, so the agent has no incentive to tamper.

**The payoff**: the subset of robustness research producing *certifiably invariant* policies — randomized smoothing, interval bound propagation, Lipschitz-constrained networks — is the subset that constitutes structural progress toward alignment. Adversarial training and empirical worst-case defences, while valuable in their own right, sit on the wrong side of the dichotomy: they harden the policy against an adversary minimising $\nu$, not against a self-interested agent maximising it. They teach the agent to survive the hammer; they do not teach it to refuse the nuke. Christiano [^20] previously argued that worst-case performance is alignment-relevant; the dichotomy here refines that claim by identifying *which* notion of worst-case — certified, not empirical — carries the alignment payoff.

#### Discussion: What's Not Shown

The reduction is structural, not constructive. Several gaps remain:

1. **The proxy/true gap is untouched.** Even a fully tamper-invariant agent optimises $R$, not $R_{\text{true}}$. The original specification problem — that $R$ is itself a proxy — is orthogonal to tampering and is not addressed by any amount of robustness work.

2. **Specifying $\mathcal{S}^{\text{phys}}_{\text{reward}}$ is itself unsolved.** Tampering-invariance is defined relative to a designated reward-channel subspace, but identifying which physical states constitute "the reward channel" is a hard sub-problem. Full invariance to $s^{\text{phys}}$ is too strong (it precludes legitimate self-monitoring); partial invariance requires committing to a particular cut, and that cut may itself be tamperable, recursively reintroducing the original problem.

3. **Self-modification escapes the model.** The reduction assumes all tampering is captured by perturbations to $\nu$. An AGI that modifies its own policy parameters, or constructs a successor agent with different objectives, acts outside this perturbation set. The reduction is silent on these cases, and they may dominate the failure modes of sufficiently capable agents.

4. **$\mathcal{N}_\pi$ may not be tractable.** The fixed-point structure makes the embedded problem strictly harder than its adversarial cousin. Techniques that scale on the adversarial side may not scale on the cooperative-with-endogenous-admissible-set side. The reduction is a conceptual bridge, not a guarantee of computational transfer.

#### Relation to Prior Work

The invariance intuition has been expressed in several prior frameworks, each via a different mechanism. Armstrong's **utility indifference** [^21] modifies the agent's utility function to be insensitive to specific interventions. Soares et al.'s **corrigibility** [^22] requires the agent not to resist correction. Everitt's **current-RF optimization** [^23] has the agent evaluate hypothetical futures using its current reward function rather than the (possibly tampered) future one — making *evaluation* invariant to tampering rather than the policy. Our contribution is not the invariance intuition itself but the reframing: by casting wireheading as the cooperative dual of the reward-poisoning robust MDP, we identify which slice of the empirical robustness literature — specifically, certified-defence methods that produce action-invariant policies — operationalises this long-standing desideratum.

The strong claim, given the caveats above, is: **invariance-style robustness research is a necessary contribution toward alignment in the limit**, *conditional* on separate solutions to reward-channel identification and to non-perturbation tampering modes. The weaker, more standard claim — that robustness is "related to" alignment — was true regardless. The reduction shows specifically *which* slice of robustness research is load-bearing.

### From Hammers to Nukes: Why Robustness is a Proving Ground for Alignment

This is a call for a redirection of effort. The work being done on adversarial robustness is not a niche subfield of AI; it is a direct and foundational prerequisite for AI alignment. [^14] Solving for the hammer is how we practice for the nuke.

1.  **It Defends the "Necessary Condition" for Alignment:** Some might argue that other approaches, like interpretability, could solve alignment without first solving robustness. The idea is that an AGI could simply explain its reasoning. However, an AGI would be far too complex for a human to fully understand, making reliance on its explanations alone a fragile strategy. More importantly, even a perfectly "interpretable" agent is useless if its underlying perceptions are flawed. If an AGI's senses can be deceived (a robustness failure), its "interpretable" reasoning will be based on a false reality, leading to catastrophic failure. Thus, robustness is a prerequisite for any other alignment technique to be reliable.

2.  **It Cultivates a Security Mindset:** Robustness research forces a shift from "make it work" to "make it not break under pressure." This adversarial, security-oriented mindset is precisely what is needed to anticipate and mitigate the failure modes of powerful AI systems.

3.  **It Builds Essential Tools:** The techniques used to defend against adversarial attacks—such as formal verification, uncertainty quantification, and building certifiably robust systems—are the very tools we will need to provide any guarantees about AGI behavior. [^6]

4.  **It Provides a Tractable Testbed:** We cannot yet build an AGI to test our alignment theories. But we *can* build systems today and test their robustness against concrete, falsifiable attacks. This provides an empirical, iterative, and rigorous path for making progress on the core difficulties of alignment.

### Conclusion

The path to beneficial AGI is paved with unsolved problems. Solving robustness is not, on its own, a complete solution to alignment. Many other challenges, such as value learning and ensuring corrigibility, must also be met. But robustness is a foundational prerequisite. Without it, any other solutions would be built on sand. By learning how to defend our systems against the "hammer" of today's human-level adversaries—by building agents that are robust to perturbations in observations, rewards, and actions—we can begin to develop the rigorous, security-minded engineering principles required to one day align the "nuke" of a superintelligent agent.

---
### References

[^1]: Wikipedia contributors. (2024). *AI alignment*. Wikipedia.
[^2]: Shah, R., et al. (2022). *Goals, no-goals, and safe agents*. AI Alignment Forum.
[^3]: Krakovna, V. (2018). *Specification gaming examples in AI*. WordPress.com.
[^4]: Wikipedia contributors. (2024). *Reward hacking*. Wikipedia.
[^5]: Clark, J., & Amodei, D. (2016). *Faulty reward functions in the wild*. OpenAI.
[^6]: Lütjens, B., et al. (2022). *Robust Reinforcement Learning: A Review of Foundations and Recent Advances*. MDPI.
[^7]: The TAILOR Handbook of Trustworthy AI. *Technical Robustness and Safety*.
[^8]: Zhang, H., et al. (2020). *Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations*. NeurIPS.
[^9]: Eykholt, K., et al. (2018). *Robust Physical-World Attacks on Deep Learning Visual Classification*. CVPR.
[^10]: Zhang, G., et al. (2017). *DolphinAttack: Inaudible Voice Commands*. ACM Conference on Computer and Communications Security.
[^11]: Tessler, C., et al. (2019). *Action Robust Reinforcement Learning and Applications in Continuous Control*. arXiv.
[^12]: Omohundro, S. (2008). *The Basic AI Drives*. Artificial General Intelligence.
[^13]: Everitt, T., & Hutter, M. (2016). *Avoiding Wireheading with Value Reinforcement Learning*. Artificial General Intelligence.
[^14]: Zhang, S., et al. (2024). *A Comprehensive Survey on AI Alignment*. arXiv.
[^15]: Demski, A., & Garrabrant, S. (2019). *Embedded Agency*. arXiv:1902.09469.
[^16]: Everitt, T., Krakovna, V., Orseau, L., Hutter, M., & Legg, S. (2017). *Reinforcement Learning with a Corrupted Reward Channel*. IJCAI. arXiv:1705.08417.
[^17]: Brekelmans, R., et al. (2022). *Your Policy Regularizer is Secretly an Adversary*. arXiv:2203.12592.
[^18]: Everitt, T., Carey, R., Langlois, E., Ortega, P. A., & Legg, S. (2021). *Agent Incentives: A Causal Perspective*. AAAI. arXiv:2102.01685.
[^19]: Langlois, E., & Everitt, T. (2021). *How RL Agents Behave When Their Actions Are Modified*. AAAI. arXiv:2102.07716.
[^20]: Christiano, P. (2018). *Techniques for optimizing worst-case performance*. AI Alignment Forum.
[^21]: Armstrong, S. (2010). *Utility Indifference*. Future of Humanity Institute Technical Report #2010-1.
[^22]: Soares, N., Fallenstein, B., Yudkowsky, E., & Armstrong, S. (2015). *Corrigibility*. AAAI Workshop on AI and Ethics.
[^23]: Everitt, T., Hutter, M., Kumar, R., & Krakovna, V. (2021). *Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective*. Synthese 198:6435-6467. arXiv:1908.04734.