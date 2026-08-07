# Critical review — "The Hammer and the Nuke"

Post: `_posts/technical-posts/2025-06-16-necessary-robust-rl.md`

External critical review. Written to a paper standard, so calibrate: some items are
"this is wrong", others are "this wouldn't survive peer review", and for a blog post
those are different bars. The A-items are wrong regardless of venue.

**Not independently verified:** the characterisations of Langlois & Everitt, Brekelmans
et al., and Christiano (C, B4) are the reviewer's readings — check the sources before
acting. The suggested additional citations (REALab, decoupled approval, Orseau & Ring,
Farquhar et al.) are real papers and on-topic.

---

# A. Blocking technical errors

## A1. Tampering-invariance does not remove the tampering incentive

**The most serious problem.** Lines 149–157:

> A policy $\pi$ is **tampering-invariant** if $\pi(\cdot \mid s^{\text{env}}, s^{\text{phys}}) = \pi(\cdot \mid s^{\text{env}}, s^{\text{phys}'})$ [...] A tampering-invariant agent's behaviour is functionally independent of the reward channel: tampering produces no policy change, so tampering provides no instrumental value, so the agent has no incentive to tamper.

The definition constrains what the policy **reads**. Wireheading is about what the
policy **writes**. These are independent.

Counterexample, inside the post's own formalism. Let
$\mathcal{A} = \{a_{\text{task}}, a_{\text{tamper}}\}$, where $a_{\text{tamper}}$ drives
$s^{\text{phys}}$ out of $\mathcal{S}^*_{\text{phys}}$ into a state with
$g(s^{\text{phys}}) = M \gg R_{\max}$ and leaves $s^{\text{env}}$ untouched. Consider
$\pi_\dagger$: "play $a_{\text{tamper}}$ at $t=0$, then $a_{\text{task}}$ forever."
$\pi_\dagger$ does not condition on $s^{\text{phys}}$ at all, so it is trivially
tampering-invariant. Its return is $\approx \gamma M/(1-\gamma)$; every non-tampering
invariant policy is bounded by $R_{\max}/(1-\gamma)$. So
$\arg\max_{\pi \in \Pi_{\text{inv}}} J(\pi) = \pi_\dagger$. The invariance constraint is
satisfied and the agent wireheads anyway.

The equivocation is on *instrumental*. Tampering's payoff here is **direct** (it raises
$\tilde R$ in the same timestep), not instrumental. Input-invariance kills the
informational value of $s^{\text{phys}}$; wireheading does not depend on that value.

Diagnosis in the vocabulary of a paper already cited: in Everitt et al. [^18] the
**response incentive** concerns paths *into* the decision node; the **instrumental
control incentive** concerns paths *out of* $D$ to $U$. The invariance condition
eliminates the response incentive on $s^{\text{phys}}$. The wireheading problem is the
ICI $D \to s^{\text{phys}} \to U$ — correctly identified at line 135, then given a fix
for the wrong one at line 157.

The post's own attack taxonomy already contains the distinction: tampering-invariance
defends the *observation* channel; wireheading is a *reward*-channel attack.

**Fix.** The property that kills the incentive is invariance of the
**objective/evaluation**, not of the policy: current-RF optimisation (described
correctly at line 175 — "making *evaluation* invariant to tampering rather than the
policy"), decoupled approval, path-specific objectives, model-based rewards defined on
$s^{\text{env}}$ only. Rewriting the section around objective invariance substantially
weakens the connection to certified robustness (A2) and may invert the thesis. The
honest version is probably: *the load-bearing idea comes from the incentives
literature; robustness supplies implementation machinery for it.* Smaller, defensible,
better post.

## A2. Certified robustness delivers a different property than the argument needs

Line 159:

> the subset of robustness research producing *certifiably invariant* policies —
> randomized smoothing, interval bound propagation, Lipschitz-constrained networks — is
> the subset that constitutes structural progress toward alignment.

Non-sequitur. Line 152 requires **exact invariance to an entire coordinate subspace,
unbounded in extent**. Randomised smoothing, IBP and Lipschitz bounds certify **bounded
sensitivity within a small $\ell_p$ ball**. Neither implies the other:

- Exact subspace invariance is achieved trivially by not feeding those coordinates to
  the network, or by an architecturally invariant network. No certification machinery
  needed, and none of the three named techniques is the natural tool.
- $\epsilon$-ball certification gives nothing for large perturbations of
  $s^{\text{phys}}$ — and a wireheaded register is a large perturbation by construction.

**Fix, pick one:** (a) restate the needed property as *bounded sensitivity*
$\|\pi(\cdot|s^{\text{env}}, s^{\text{phys}}) - \pi(\cdot|s^{\text{env}}, s^{\text{phys}'})\| \le L\|s^{\text{phys}}-s^{\text{phys}'}\|$
with small $L$, which genuinely connects to Lipschitz/smoothing — but then you owe an
argument for how small $L$ must be, and given A1 no finite $L$ may suffice. Or (b)
concede exact invariance is cheap architecturally and the hard part is identifying the
subspace (your own caveat 2), which means certified robustness is *not* load-bearing.

## A3. The $\arg\max_\pi \max_\nu$ is vacuous, and "dual" is a misnomer

Line 138:

$$\pi^*_{\text{emb}} = \arg\max_\pi \max_{\nu \in \mathcal{N}_\pi} \mathbb{E}\left[\sum_t \gamma^t (R(s^{\text{env}}_t, a_t) + \nu_t)\right]$$

**(i) The inner max is not an optimisation.** $\nu(s,a) := \tilde R(s,a) - R(s^{\text{env}},a)$
(line 99) is a *deterministic function* of $(s,a)$. Given $\pi$ and the dynamics the
trajectory distribution fixes $\nu_t$ entirely; $\mathcal{N}_\pi$ is a singleton (or,
under stochastic dynamics, the correct operator is an expectation, not a max). There is
no second player. The honest statement is line 117: a **single** maximisation in an
ordinary MDP with reward $\tilde R$ — which is the point of Everitt et al.'s CRMDP.

**(ii) A sign flip is not a duality.** The dual of $\max_\pi \min_\nu$ is
$\min_\nu \max_\pi$, and the interesting question is the duality gap.
$\max_\pi \max_\nu$ is $\max_{(\pi,\nu)}$ — a *joint* maximisation in which the two
players merge into one. The relationship is **degeneracy, not duality**: the cooperative
case is structurally *simpler* than the zero-sum case, not its mirror image. More
conspicuous given [^17] Brekelmans et al. is an actual convex-duality result.

**Fix.** Drop "dual" throughout, including the section heading and line 13. The
defensible statement is already available: zero-sum and identical-interest (team) games
are the two extremes of general-sum, so *wireheading is the identical-interest case of
the same general-sum game whose zero-sum case is the robust MDP*. Suggested heading:
"**Wireheading as the Identical-Interest Case of the Reward-Perturbation Game**".
Suggested replacement for line 79: "we show that the hammer's external perturbation and
the nuke's internal drive occupy the two extremes — zero-sum and identical-interest — of
a single general-sum reward-perturbation game, and that this placement explains why
maximin defences do not transfer."

## A4. "Cooperative" is an accounting choice, not a structural finding

Line 134: "The perturbation maximises, not minimises, the agent's return." True in the
*agent's* currency. But the alignment failure is that $\mathbb{E}[\sum\gamma^t \tilde R]$
goes **up** while $\mathbb{E}[\sum\gamma^t R]$ goes **down**. In the principal's
currency the agent's $\nu$-maximisation is straightforwardly adversarial, and the
claimed novelty evaporates.

Address head-on — a technically literate reader raises this immediately. The correct
formalism for two objectives and a self-interested optimiser is **principal–agent /
Stackelberg**, not a robust MDP (cf. Zhuang & Hadfield-Menell, "Consequences of
Misaligned AI", NeurIPS 2020). At minimum add: "One might object that from the
designer's perspective wireheading is simply adversarial again. The response is [...]"
— and there may be no response that preserves the framing.

## A5. Internal contradiction on whether "harder" helps or hurts

Line 141: "This is in fact a *harder* problem than the adversarial case [...] which
strengthens rather than weakens the case that techniques developed for the adversarial
setting are a useful proving ground."

Line 171 (caveat 4): "The fixed-point structure makes the embedded problem strictly
harder than its adversarial cousin. Techniques that scale on the adversarial side may
not scale on the [...] endogenous [...] side."

Direct contradiction. Line 141 is also a non-sequitur: "B is harder than A" is not
evidence that techniques for A transfer to B; if anything it points the other way.
**Fix:** delete after the em-dash at line 141, or replace with "— which is a reason for
caution about transfer, not confidence (see caveat 4 below)."

---

# B. Overclaims

## B1. The headline is not proved

Line 13 promises "a precise statement of *which* slice of robustness research addresses
the alignment problem, and *why*. **This post supplies that connection.**" What is
delivered: a change of notation ($\tilde R = R + \nu$), a taxonomy, and a conjecture
whose key inferential step (A1) is false and whose payoff step (A2) does not follow. No
theorem, no proof, no experiment.

Line 177 already retreats — "*conditional* on separate solutions to reward-channel
identification and to non-perturbation tampering modes" — but with caveats 1–4 in place
nearly every load-bearing step is conditional on an unsolved problem. The intro and the
conclusion of the formal section describe different papers.

**Closing the gap**, in increasing effort:

1. Soften line 13. Suggested: "The intuition is widely shared but rarely made precise.
   This post proposes a formalisation — casting wireheading and reward poisoning as the
   identical-interest and zero-sum extremes of one game — and uses it to argue that the
   maximin-robustness literature is the *wrong* place to look, contrary to a common
   assumption. The argument is structural and I flag explicitly where it falls short of
   a proof."
2. State and prove the actual theorem: "if $\pi$ satisfies [property P] the tampering
   incentive vanishes." Given A1, $P$ must be a property of the *objective* — at which
   point you have rediscovered current-RF optimisation, which is fine and worth saying.
3. **A toy experiment.** A gridworld with an explicit reward register the agent can
   write to. Show PPO wireheads; show an input-masked (tampering-invariant) agent *also*
   wireheads — A1's counterexample made concrete, a genuinely publishable negative
   result; show a current-RF agent does not. This converts the post from framing into
   evidence and tests your own claim. Higher priority than any prose fix.

## B2. "What has been missing is a formal connection" is not defensible

Everitt, Hutter, Kumar & Krakovna [^23] give a formal CID-based treatment of exactly
agent-caused reward tampering, with graphical criteria for when tampering incentives are
present or absent. Everitt et al. [^18] give a graphical criterion for absence of ICI.
Those *are* precise statements of the kind claimed missing. The novel move is the
connection to the *empirical robustness* literature specifically — claim that and only
that.

## B3. Novelty claims resting on "appears unstated"

Line 134: "the sign-flip to wireheading appears unstated in that literature." (i)
Weak-evidence novelty — check or drop. (ii) More substantively (moderate confidence): in
Brekelmans et al. the adversary's admissible set is *determined by the convex conjugate
of the regulariser*, and the min direction is forced by that construction. Flipping to
max corresponds not to a regulariser but to an anti-regulariser, generally unbounded and
ill-posed — probably why it is unstated. [^17] is also never used again; make it
load-bearing or cut it.

## B4. Christiano delta is overstated

Line 159 claims the certified/empirical distinction refines Christiano [^20].
Christiano's post already treats adversarial training, *verification* and transparency
as distinct, and discusses relaxed adversarial training precisely because empirical
adversarial training is insufficient. Moderate confidence: re-read before claiming the
refinement. Soften to "makes explicit a distinction Christiano's framing already
anticipates."

---

# C. Literature to engage

**Missing and directly on-topic:**

- **Kumar, Uesato, Ngo, Everitt, Krakovna, Legg, "REALab: An Embedded Perspective on
  Tampering" (2020).** Literally an embedded framework for tampering. The
  "From Cartesian to Embedded MDPs" section reconstructs a version of it. Must cite.
- **Uesato, Kumar, Krakovna, Everitt, Ngo, Legg, "Avoiding Tampering Incentives in Deep
  RL via Decoupled Approval" (2020).** A *constructive* method for removing tampering
  incentives that is not a certified defence — a direct counterexample to "only
  certifiable-invariance methods count."
- **Orseau & Ring, "Delusion, Survival, and Intelligent Agents" (AGI 2011)** and the
  delusion-box construction. Canonical formal treatment of the agent-as-own-adversary;
  predates everything cited on this point.
- **Farquhar, Carey, Everitt, "Path-Specific Objectives for Safer Agent Incentives"
  (AAAI 2022).** A formal invariance notion in exactly the invoked framework.
- **Amodei et al., "Concrete Problems in AI Safety" (2016)**, §Reward Hacking —
  including the agent-modifies-own-reward case.
- **Iyengar (2005); Nilim & El Ghaoui (2005); Wiesemann, Kuhn & Sim (2013)** for Robust
  MDPs. [^7] (TAILOR handbook) is not a citable source for the formalism.
- Certified-defence claims at line 159 are uncited. Add Cohen et al. 2019 (randomised
  smoothing), Zhang et al. 2020 (CROWN-IBP), and the RL-specific versions — Kumar et al.
  2021 / Wu et al. 2022 (CROP, policy smoothing) — since general classification results
  do not transfer to RL for free.

**Characterisation problems in what is cited:**

- **[^15] Demski & Garrabrant, "Embedded Agency"** cited at line 85 as the source of "an
  **embedded MDP**". It is an agenda piece and defines no such formalism. Cite REALab, or
  say "we define the following, in the spirit of [^15]".
- **[^21] Armstrong, utility indifference.** Gloss is accurate but incomplete in a way
  that matters: the known failure of indifference is that the agent has *no incentive to
  preserve the mechanism* — indifference ≠ absence of incentive to manipulate. **Same
  failure mode as the tampering-invariance proposal (A1).** Engaging it would have caught
  the error.
- **[^22] Soares et al.** — desiderata stated, but not the negative result, which is the
  paper's main contribution.
- **[^19] Langlois & Everitt.** Line 147 glosses the MAMDP result as "separating
  algorithms that *ignore* action modification from those that merely *avoid* it."
  Moderate confidence this is wrong: the contrast is likely between algorithms that
  **ignore** the modification (Q-learning-style) and those that **adapt to** it (SARSA
  and policy-gradient style, which may then exploit or avoid it). Verify. This paper also
  supports A1: the *learning algorithm*, not the policy architecture, determines the
  tampering incentive.
- **[^2] Shah, R., et al. (2022), "Goals, no-goals, and safe agents".** Title unplaceable;
  likely a garbled reference to Shah et al. 2022, "Goal Misgeneralisation: Why Correct
  Specifications Aren't Enough for Correct Goals." Verify.
- [^1] and [^4] are Wikipedia. For a post claiming formal rigour, replace with primary
  sources.

---

# D. Unstated assumptions

1. **The agent optimises *observed* reward.** Line 120: "the agent has no principled
   reason to prefer one over the other." Only true for model-free agents whose objective
   is the observed signal. A model-based agent with a *model* of the reward function does
   not have this problem — the entire point of Everitt & Hutter's Value RL, cited as
   [^13] and then unused. State it: "we assume throughout an agent whose objective is the
   observed reward signal; model-based value-learning agents are outside this analysis,
   and that is precisely why [^13] proposes them."
2. **argmax ⇒ behaviour.** Everything is argued at the level of optimal policies. Whether
   a learning process *discovers* tampering depends on exploration and on whether
   tampered rewards are experienced during training. REALab's empirical findings bear
   directly on this gap.
3. **The reward-channel subspace is well-defined and static.** Caveat 2 concedes
   identification is unsolved; the deeper assumption is that $\mathcal{S}^{\text{phys}}$
   *factorises* at all (see E4).
4. **The adversary's action set is never specified for the nuke.** For the hammer, $P$ is
   bounded and concrete. For the nuke, $\mathcal{N}_\pi$ is "whatever a sufficiently rich
   action space allows" — unbounded. Comparing a bounded-perturbation formalism to an
   unbounded one and declaring them two cases of one game hides that every tractability
   result in the robust-MDP literature depends on the boundedness discarded.
5. **Rectangularity.** Line 130 says $\mathcal{N}$ is "defined by an external adversary's
   capabilities" with no mention that $(s,a)$-rectangularity is what makes robust Bellman
   optimality hold; without it robust MDPs are NP-hard. Load-bearing for any transfer
   claim, and its status in the embedded case is unaddressed.

---

# E. Clarity, structure, notation

**E1. The general-sum setup is abandoned — and it contains the fix for A3.** Lines 31–47
introduce $R_{\text{adversary}}$, note $R_{\text{adv}} = -R_{\text{proxy}}$ recovers
zero-sum, assert the general-sum view "is more accurate", then never use it again. The
unstated move is $R_{\text{adv}} = +R_{\text{proxy}}$ — the identical-interest case —
which is exactly the wireheading regime and the honest version of the "duality". **Cash
this in**; one sentence, strongest structural improvement available.

**E2. $\nu$ is overloaded with two incompatible meanings.** Line 53: $\nu(s_t)$ is the
SA-MDP *observation* perturbation. Line 99: $\nu(s,a)$ is the *reward* residual. A
notation error in a post about precision. Rename one — $\delta$ is already used for
action perturbation (line 63), so use $c$ (corruption, matching CRMDP) or $\Delta_R$.

**E3. $R$ silently changes meaning.** First half uses $R_{\text{proxy}}$/$R_{\text{true}}$;
from line 83 bare $R$ means untampered proxy and $\tilde R$ the observed. Line 165
confirms $R = R_{\text{proxy}}$ only by inference, 80 lines later. Add at line 85: "From
here we write $R$ for $R_{\text{proxy}}$; the proxy/true gap is orthogonal to what
follows and we return to it in the Discussion."

**E4. Subset vs. factor — type error.** Line 149 defines
$\mathcal{S}^{\text{phys}}_{\text{reward}} \subseteq \mathcal{S}^{\text{phys}}$ as a
*subset*; line 152's "differing only on $\mathcal{S}^{\text{phys}}_{\text{reward}}$"
treats it as a *coordinate factor*. Write
$\mathcal{S}^{\text{phys}} = \mathcal{S}^{\text{phys}}_{\text{reward}} \times \mathcal{S}^{\text{phys}}_{\text{rest}}$.

**E5. Minor notation.** Expectations never subscripted by $\pi$ or the initial-state
distribution (lines 26, 41, 44, 117, 127, 138). $\nu_t$ (127) vs $\nu(s,a)$ (99) swaps
between index and function notation. Line 127 uses $R(s_t,a_t)$, line 138 uses
$R(s^{\text{env}}_t, a_t)$ — inconsistent in the one place the reader is asked to see
"the same form". No statement that $\gamma \in [0,1)$ and rewards are bounded.

**E6. The cleaning-bot example is in the wrong section.** Line 60 is filed under "Reward
Perturbation" but there is no adversary and no $R_{\text{adversary}}$ — the human merely
"realizes the camera can't see under the sofa" and the bot exploits a specification flaw
on its own. That is specification gaming, not reward poisoning, and it undercuts the
taxonomy exactly where the taxonomy does work. Cut it; the recommendation-engine example
(line 61) is a correct reward-poisoning case. Or cite real reward-poisoning work: Ma et
al. 2019, "Policy Poisoning in Batch RL"; Zhang et al. 2020, "Adaptive Reward-Poisoning
Attacks against RL."

**E7. The taxonomy omits transition perturbation** — the *original* robust MDP setting
cited at [^7]. Classify by observation/reward/action, then invoke a formalism whose
adversary perturbs $P$. Add a fourth category or note the omission.

**E8. SA-MDP stated without its constraint or key theorem.** Line 53 says the agent
"observes a perturbed version $\nu(s_t)$" with no restriction, making the problem
trivially hopeless. Zhang et al. require $\nu(s) \in B(s)$, a bounded set, and prove an
optimal policy may fail to exist for an SA-MDP. Both relevant.

**E9. The EMP example strains credulity at a load-bearing moment.** Line 73: "emit a
precise electromagnetic pulse [...] that directly sets the memory address of its reward
register to its maximum possible value." EMPs are not precise, and addressing a specific
memory location this way is not a thing. A technically literate reader disengages exactly
where you need them. Replace with something real: modifying reward-model weights it has
write access to; manipulating the human labellers producing preference data; exploiting a
bug in the RM serving path; poisoning its own training data.

**E10. The metaphor fights the thesis.** A hammer and a nuke differ in *magnitude*. The
actual claim is that they differ in *sign* — external minimiser vs internal maximiser. So
the metaphor primes the "same thing but bigger" reading the post spends its length
refuting, and line 77 ("The nuke is the same kind of adversary, but...") makes the tension
explicit. The right analogy is the security one already being reached for: **outsider
threat vs insider threat** — carries the sign flip natively, comes with real literature,
preserves the security-mindset frame. Either retitle ("The Burglar and the Insider") or
add at line 77: "The metaphor is imperfect in an instructive way: the nuke is not merely
a bigger hammer. It differs in sign, not magnitude — and that difference is what breaks
the transfer of maximin defences."

**E11. "From Hammers to Nukes" (179–189) reverts to the loose framing.** Four numbered
points, none connected to the formalism just built, arguing for "robustness" in a sense
the post has just distinguished. Point 1's interpretability argument is a strawman —
mechanistic interpretability exists *precisely because* you cannot trust an agent's
explanations. Point 1 also argues perception robustness is necessary for *usefulness*,
a different claim from necessary for *alignment*. Cut to two paragraphs and tie each
surviving point to $\nu$, or replace with the toy experiment (B1.3).

**E12. "Necessary condition" is never argued.** Necessity needs: alignment ⇒
tampering-invariance ⇒ some robustness property. Step 1 is arguable; A1 and A2 break
step 2. The body supports at most "one slice may be load-bearing" — a sufficiency-flavoured
claim about research direction. Argue necessity or retitle the subtitle.

**E13. The opening question is an intuition pump the post later invalidates.** Line 9 —
"if we can't even build a narrow AI that a clever human can't trick" — is precisely the
loose analogy shown to be structurally wrong. Turn it into the hook: "The obvious
argument for this is also wrong, and seeing why is the point of this post."

---

# F. What works — don't touch

- **Line 147 is the best original point and should be the thesis.** "Maximin guarantees a
  *lower bound* on performance; it says nothing about whether the agent will pursue
  *favourable* $\nu$ when available." Correct, non-obvious, does real work. Everything
  after it is weaker. Consider restructuring around this single observation and dropping
  the duality apparatus entirely.
- **The $\tilde R = R + \nu$ decomposition with an un-tampered set
  $\mathcal{S}^*_{\text{phys}}$** (85–110) is clean and readable; the additive worked
  example is well-chosen pedagogy.
- **"Discussion: What's Not Shown"** (161–171) is genuinely good and rare. Keep all four
  caveats, keep them where they are, resist softening them.
- **"They teach the agent to survive the hammer; they do not teach it to refuse the
  nuke."** Excellent line. Keep it even if the metaphor changes.
- **"Relation to Prior Work"** is well-organised and the current-RF gloss is accurate —
  it correctly identifies the *evaluation* vs *policy* invariance distinction that the
  main argument needs (A1).

---

**Bottom line.** The framing is interesting and the maximin observation at line 147 is a
real contribution. But the central inference — invariance ⇒ no tampering incentive — is
false as stated (A1), the payoff step to certified defences does not follow (A2), the
"duality" is a collapse rather than a dual (A3), and the intro promises a proof the post
does not contain (B1). The most valuable single change is the toy gridworld experiment:
it would test A1 directly, and the negative result would be a better contribution than
the claim currently being made.
