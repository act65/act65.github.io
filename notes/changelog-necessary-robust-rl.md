# Changelog — edits applied to "The Hammer and the Nuke"

Post: `_posts/technical-posts/2025-06-16-necessary-robust-rl.md`
Review applied: `notes/review-necessary-robust-rl.md`
Build verified: `bundle exec jekyll build` succeeds; 30 footnote refs, 30 definitions, all
resolved; 9 display-math blocks render exactly as in the previous `_site` output.

---

## A. Blocking technical errors

**A1 — tampering-invariance does not remove the tampering incentive. Rebuilt.**
The "What Transfers, and What Doesn't" section is substantially rewritten. Rather than
delete the false argument, I kept it as a worked mistake, in the author's first person:

- The tampering-invariance definition is now presented as "the argument I originally
  wrote", explicitly flagged as false before it is stated in full.
- The review's counterexample ($\pi_\dagger$: tamper once, then act normally; trivially
  invariant because it conditions on nothing; return $\gamma M/(1-\gamma)$ beats
  $R_{\max}/(1-\gamma)$) is reproduced in the post's own notation.
- The diagnosis is stated in the review's terms: policy invariance constrains what the
  policy **reads**, wireheading is about what it **writes**; the invariance condition
  removes a *response incentive* (paths into the decision node) while wireheading is an
  *instrumental control incentive* (paths out of it). Cross-referenced to Everitt et al.
  `[^18]`, already cited.
- The positive argument is rebuilt around **objective/evaluation invariance**: current-RF
  optimisation `[^23]`, path-specific objectives `[^24]`, decoupled approval `[^30]`, with
  the observation that none of these is a certified defence.
- Adopted the review's suggested framing verbatim in substance: "the load-bearing idea
  belongs to the incentives literature ... what the robustness literature contributes is
  implementation machinery ... and machinery is not the same thing as the idea."
- The intro now warns that the post contains an argument that turns out to be false and
  has been left in rather than deleted, so the structure is signposted.

**A2 — certified robustness conclusion. Took option (b) as instructed.**
The "payoff" paragraph now says the conclusion doesn't follow, for two reasons: (i) the
required invariance is exact and unbounded whereas certificates are $\ell_p$-ball-local,
so the certificate is silent on the case of interest; (ii) exact invariance to a
coordinate factor is architecturally trivial — you get it by not feeding the coordinates
in. Explicitly concedes the hard part is *identifying the subspace* (caveat 2), i.e.
certified robustness is not load-bearing. Randomised smoothing now cited (Cohen et al.
`[^31]`); IBP and Lipschitz networks are named as generic techniques without citation.

**A3 — "dual" removed; vacuous inner max fixed.**
- Section heading changed to "Wireheading as the Identical-Interest Case of the
  Reward-Perturbation Game".
- Intro (old line 13) no longer claims a "cooperative dual"; it now uses the
  identical-interest / zero-sum extremes framing.
- Sub-heading "Reduction to a Robust MDP" → "Placing Both Cases in the Same Game".
- A new paragraph states plainly that this is *not* a duality: the dual of
  $\max_\pi\min_c$ is $\min_c\max_\pi$; a sign flip collapses the game rather than
  dualising it; $\max_\pi\max_c$ is a joint maximisation in which the players merge.
- The vacuous $\arg\max_\pi\max_{\nu\in\mathcal N_\pi}$ display is **deleted**. Replaced
  with prose explaining that given $\pi$ and the dynamics, $c$ is a deterministic
  function of the trajectory — there is no free variable for an inner max, and the honest
  statement is the single maximisation already given, in an ordinary MDP with reward
  $\tilde R$ (which is the CRMDP point).
- The Brekelmans `[^17]` gloss is now load-bearing (it is the contrast case that shows
  what a real duality result looks like) rather than a dangling novelty claim.

**A4 — principal's-currency objection. Added.**
New paragraph "An objection worth meeting head-on", conceding that in the principal's
currency the agent's $c$-maximisation is straightforwardly adversarial and that the
identical-interest label is an accounting choice. The defence offered is narrow and
honest: the *defences* are constructed in the agent's currency, so the sign flip is real
at the level where the techniques live. Points at Zhuang & Hadfield-Menell `[^29]` as the
right formalism (principal–agent / Stackelberg) and says the post does not develop it.

**A5 — contradiction resolved.**
The "strengthens rather than weakens the case" clause is replaced with the review's
suggested wording: "which is a reason for caution about transfer, not confidence (see
caveat 4 below)." Caveat 4 is unchanged in substance and now agrees with it.

## B. Overclaims

**B1 — intro softened** using the review's suggested wording as a base, adapted to the
author's first-person voice. No claim of a supplied "formal connection"; instead
"proposes a formalisation", "the argument is structural", "I flag explicitly where it
falls short of a proof".

**B2 — "what has been missing is a formal connection" removed.** Replaced with an
acknowledgement that Everitt et al. `[^23]` give graphical criteria and Farquhar et al.
`[^24]` a formal invariance notion, and that what is less developed is the bridge to the
*empirical* robustness literature specifically. That narrower claim is the one now made.

**B3 — "appears unstated" dropped entirely.** No novelty claim now rests on absence of
evidence. `[^17]` is retained and made load-bearing (see A3). I did **not** assert the
reviewer's anti-regulariser/ill-posedness explanation, which is their conjecture.

**B4 — Christiano delta softened, after verification.** See "citations verified" below.
Now reads: "treated adversarial training, verification and transparency as distinct
routes to it; the argument here makes explicit a distinction his framing already
anticipates."

## D. Unstated assumptions — all five now stated

- **D1** (agent optimises *observed* reward): new paragraph after the objective
  decomposition, naming model-based value RL `[^13]` as the excluded case and saying why.
- **D2** (argmax ⇒ behaviour): new paragraph, pointing at REALab `[^28]` for the gap.
- **D3** (reward subspace well-defined and static, and factorises at all): folded into
  caveat 2, which now also names the factorisation assumption explicitly.
- **D4** (nuke's action set unbounded): new paragraph after the residual definition,
  contrasting the hammer's bounded $\nu(s)\in B(s)$ with "whatever a sufficiently rich
  action space allows". Echoed in the reduction section and caveat 4.
- **D5** (rectangularity): introduced early, in the general-sum section, then used twice —
  when contrasting $\mathcal{C}$ with $\mathcal{C}_\pi$ (with an explicit "I don't know of
  a reason to expect $\mathcal{C}_\pi$ to be rectangular"), and in caveat 4.

## E. Clarity, structure, notation

- **E1** — the general-sum setup is now cashed in. $R_{\text{adv}}=+R_{\text{proxy}}$ is
  named as the identical-interest pole at the moment the game is introduced, and the
  reduction section refers back to it explicitly.
- **E2** — the $\nu$ collision is resolved. $\nu$ is kept for the SA-MDP *observation*
  perturbation (matching Zhang et al.'s own notation); the *reward* residual is renamed
  $c$ throughout, per the review's suggestion ("corruption, matching CRMDP"). A short
  note flags the change where it happens. $\mathcal{N}$/$\mathcal{N}_\pi$ likewise become
  $\mathcal{C}$/$\mathcal{C}_\pi$.
- **E3** — added the "From here I write $R$ for $R_{\text{proxy}}$" note at the point of
  the switch.
- **E4** — subset/factor type error fixed: $\mathcal{S}^{\text{phys}}$ is now written as a
  product $\mathcal{S}^{\text{phys}}_{\text{reward}}\times\mathcal{S}^{\text{phys}}_{\text{rest}}$
  and the invariance display conditions on both coordinates.
- **E5** — expectations are subscripted $\mathbb{E}_\pi$ (and $\mathbb{E}_{\pi,s_0\sim\rho}$
  at first use); $\gamma\in[0,1)$ and bounded rewards stated once, up front; the
  index/function notation swap ($c_t$ vs $c(s,a)$) removed — $c(s,a)$ everywhere.
- **E6** — the cleaning-bot example is cut from the Reward Perturbation section (it was
  specification gaming, not poisoning). Replaced with a preference-data poisoning example,
  and the section now cites the actual reward-poisoning literature (Ma et al. `[^25]`,
  Zhang et al. `[^26]`).
- **E7** — transition perturbation noted as a deliberate omission, with the awkwardness
  acknowledged (the robust-MDP formalism leaned on was built for the omitted case).
- **E8** — SA-MDP now states the bounded constraint $\nu(s_t)\in B(s_t)$, says why
  boundedness is not a technicality, and notes Zhang et al.'s result that an optimal
  policy need not exist.
- **E9** — the EMP example is gone. Replaced with four concrete mechanisms: write access
  to reward-model weights, influence over preference labellers, a bug in the RM serving
  path, poisoning a future training corpus.
- **E10** — added the sign-not-magnitude paragraph, including the outsider/insider threat
  analogy as the better metaphor. Post **not** retitled, per instruction.
- **E11** — "From Hammers to Nukes" cut from four numbered points to three short
  paragraphs, both surviving points tied to the formalism ($c$, objective-side fixes
  needing implementation and checking). The interpretability strawman is deleted.
- **E12** — necessity addressed in the body rather than by retitling: an explicit
  paragraph at the end of "Relation to Prior Work" saying the subtitle promises more than
  the body delivers, naming which link in the necessity chain broke, and stating that the
  subtitle stands as the question the post started from rather than its conclusion. The
  conclusion echoes this.
- **E13** — the opening question is now a hook: "the argument is wrong, and seeing exactly
  why it is wrong is the point of this post."

## F. Preserved as instructed

- The maximin lower-bound observation is preserved and **promoted**: it now opens the
  "What Transfers" section, is flagged as "if I had to keep one paragraph of this post",
  and is expanded with the quantifier framing (maximin certifies at $\min_c$, wireheading
  happens at $\max_c$). It is also the load-bearing idea in the new conclusion.
- The $\tilde R = R + c$ decomposition, the un-tampered set $\mathcal{S}^*_{\text{phys}}$,
  and the additive worked example are unchanged apart from the $\nu\to c$ rename.
- "Discussion: What's Not Shown" is kept in place with all four caveats, unsoftened.
  Changes are limited to notation ($\mathcal{N}_\pi\to\mathcal{C}_\pi$, "cooperative" →
  "identical-interest"), plus *strengthening* caveats 2 and 4 with D3 and D5.
- "They teach the agent to survive the hammer; they do not teach it to refuse the nuke."
  is kept verbatim and bolded.
- "Relation to Prior Work" keeps its structure and the accurate current-RF gloss.

## Citations

**Verified before changing (constraint 4):**

| Claim | Outcome |
|---|---|
| Langlois & Everitt `[^19]` MAMDP gloss | **The post was right; the reviewer's suspicion was wrong.** The abstract reads: "some completely ignore modifications while others go to various lengths in trying to avoid action modifications that decrease reward." The post's ignore/avoid framing is accurate. I kept it and tightened the wording to match the abstract's language. I also adopted the reviewer's *other*, correct point — that the learning algorithm rather than the policy architecture fixes the incentive — which supports A1. |
| Brekelmans `[^17]` | Verified. Convex duality; robust set of adversarial (worst-case) reward perturbations characterised under KL and $\alpha$-divergence regularisation; no cooperative/maximising treatment. The post's gloss is now accurate and load-bearing. I did **not** assert the reviewer's anti-regulariser explanation. |
| Christiano `[^20]` | Verified: the post does treat adversarial training, verification and transparency as three distinct approaches. Reviewer's B4 confirmed; claim softened to "makes explicit a distinction his framing already anticipates". |
| `[^2]` "Goals, no-goals, and safe agents" | Unplaceable, as the reviewer suspected. **Not** swapped for the reviewer's guess (Goal Misgeneralisation, arXiv:2210.01790) — that paper is about goal misgeneralisation, not proxy-reward specification, and would be a wrong citation at that point in the text. Replaced with Hadfield-Menell et al., *Inverse Reward Design* (NeurIPS 2017), which is exactly about the designed-proxy-vs-true-reward gap the sentence makes. Verified. |

**Wikipedia footnotes replaced with primary sources:**
- `[^1]` → Amodei et al., *Concrete Problems in AI Safety* (2016), arXiv:1606.06565.
- `[^4]` → Skalse, Howe, Krasheninnikov & Krueger, *Defining and Characterizing Reward
  Hacking* (NeurIPS 2022), arXiv:2209.13085. Verified.

**`[^7]` TAILOR handbook replaced** with Iyengar (2005), *Robust Dynamic Programming*,
Math. OR 30(2):257–280, and Nilim & El Ghaoui (2005), Operations Research 53(5):780–798.

**New citations added (all verified against the source or its listing):**
`[^24]` Farquhar, Carey & Everitt (AAAI 2022, arXiv:2204.10018) ·
`[^25]` Ma, Zhang, Sun & Zhu (NeurIPS 2019) ·
`[^26]` Zhang, Ma, Singla & Zhu (ICML 2020) ·
`[^27]` Ring & Orseau (AGI-11) — note author order taken from the paper's own title page,
which is Ring first, not "Orseau & Ring" as the review has it ·
`[^28]` Kumar et al., REALab (arXiv:2011.08820) ·
`[^29]` Zhuang & Hadfield-Menell (NeurIPS 2020, arXiv:2102.03896) ·
`[^30]` Uesato et al., decoupled approval (arXiv:2011.08827) ·
`[^31]` Cohen, Rosenfeld & Kolter (ICML 2019, arXiv:1902.02918).

**Citation removed:** `[^14]` (Zhang, S., et al. 2024, *A Comprehensive Survey on AI
Alignment*). Its only host sentence was in the rewritten "From Hammers to Nukes" section.
I could not place a 2024 survey by that author under that exact title (the well-known one
is Ji et al. 2023, *AI Alignment: A Comprehensive Survey*, arXiv:2310.19852), so rather
than substitute a guess I dropped it. If the author has the right reference, Ji et al.
would slot cleanly into the intro.

**Corrected characterisations (review section C):**
- `[^15]` Demski & Garrabrant is now cited as an *agenda*, with the embedded MDP defined
  in the post "in the spirit of" it, plus a pointer to REALab `[^28]` for the actual
  formalism.
- `[^21]` Armstrong's indifference gloss now includes the failure mode (no incentive to
  *preserve* the mechanism either), explicitly linked to the A1 error.
- `[^22]` Soares et al. now carries its negative result. Verified wording: "none have yet
  been demonstrated to satisfy all of our intuitive desiderata."

---

## Deliberately not changed, and why

- **No toy experiment** (B1.3), per hard constraint 1. See outstanding tasks.
- **Title unchanged** (E10, hard constraint 2). The metaphor's mismatch is now
  acknowledged in the body instead, with the outsider/insider alternative named.
- **Subtitle unchanged** (E12, hard constraint 2). Addressed in the body instead.
- **The four caveats are not softened or moved**, per hard constraint 3 and review F.
- **The hammer's three examples that work** (stop sign, DolphinAttack, drone RFI) are
  untouched; only the cleaning-bot example was cut.
- **No RL-specific certified-defence citations added** (the review suggests CROP / policy
  smoothing). Since A2's resolution is that certified robustness is *not* load-bearing,
  piling on citations for a claim the post now retracts would be noise. Cohen et al. alone
  anchors "randomised smoothing" where it is named.
- **Reviewer's rename direction for E2 partially inverted.** The review suggested renaming
  the reward residual to $c$; I did that, but I kept $\nu$ for the observation
  perturbation rather than renaming it, because that matches Zhang et al.'s own notation
  and the collision is resolved either way.

## Where I disagreed with the reviewer

1. **Langlois & Everitt (C).** The reviewer's "moderate confidence this is wrong" is
   itself wrong — the post's ignore/avoid gloss matches the paper's abstract. Kept, and
   verified. Their *supporting* observation (learning algorithm, not architecture) is
   good and has been adopted.
2. **`[^2]` replacement (C).** The reviewer guessed Goal Misgeneralisation. That title is
   real but is the wrong citation for the sentence it would sit under. Used Inverse Reward
   Design instead.
3. **Ring & Orseau author order.** The review says "Orseau & Ring". The paper's title page
   is Ring first. Cited accordingly.
4. **E11's "cut to two paragraphs".** Ended up as three short ones; the third is the
   sting ("defending the wrong sign of $c$") and earns its place.
5. **F's "consider dropping the duality apparatus entirely".** Kept the game-placement
   framing rather than dropping it, since A3's fix makes it defensible and it is what
   *justifies* the maximin observation rather than merely decorating it. But the
   apparatus is now much lighter — one game, two poles, no dual.

## Outstanding for the author

1. **The toy experiment.** Not done — hard constraint. The post now explicitly says the
   experiment it "ought to contain and doesn't", describes it (gridworld, writable reward
   register, check whether an input-masked agent wireheads anyway), predicts the result,
   and admits it hasn't been run. **If you'd rather not advertise an unrun experiment,
   delete that sentence from "From Hammers to Nukes"** — nothing else depends on it. If
   you do run it, a positive result for A1's counterexample is a genuinely publishable
   negative result and would convert the post from framing into evidence.
2. **`[^14]`.** Dropped for lack of a verifiable source. Confirm whether you meant Ji et
   al. 2023 and reinstate if so.
3. **Voice check on the first-person turn.** The rewritten sections are more openly
   self-correcting than the original ("the argument I originally wrote", "I'd have used it
   if I'd seen the problem earlier"). This seemed the honest way to apply A1 without
   pretending the post always said the right thing, and it fits the existing "What's Not
   Shown" register — but it is a tonal choice you may want to dial back.
4. **`[^6]` (Lütjens et al. review).** Still doing double duty as the citation for both
   "adversarial robustness generally" and "the reward-poisoning robust MDP literature".
   A more specific citation for the latter would be better; I left it since the review
   didn't flag it.
5. **Whether to promote the maximin observation to the thesis.** The review suggests
   restructuring the whole post around it. I gave it top billing within "What Transfers"
   and the conclusion, but stopped short of reorganising the post around it — that is a
   structural call that changes what the piece *is*.
