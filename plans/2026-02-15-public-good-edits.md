# Plan: Editing `_drafts/inbetween-posts/2026-02-15-public-good.md`

## 1. MathJax / LaTeX Rendering Fixes

### 1a. Fix `\square` — missing AMSsymbols extension

**File:** `_includes/mathjax.html`

The current MathJax config only loads `tex2jax.js`. The `\square` command (used on lines 322, 361, 391, 423 as QED markers) requires the `AMSsymbols` extension.

**Fix:** Add `TeX: { extensions: ["AMSsymbols.js", "AMSmath.js"] }` to the MathJax config. This also enables `\operatorname`, `\text`, `\tag`, etc. more reliably.

```html
MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\[","\]"], ["\\[","\\]"] ],
      processEscapes: true
    },
    TeX: {
      extensions: ["AMSmath.js", "AMSsymbols.js"]
    },
    messageStyle: "none",
    "HTML-CSS": { availableFonts: ["TeX"] }
});
```

### 1b. Fix `s^{* }` pattern (7 occurrences) — space before closing brace

Kramdown processes `*` as emphasis before MathJax runs. The author worked around this by writing `s^{* }` (space before `}`), but this creates invalid LaTeX — MathJax sees `{* }` which is malformed.

**Affected lines:** 140, 171, 187, 196, 221, 257, 513

**Fix:** Replace `s^{* }` with `s^\ast` or `s^{\ast}`. The `\ast` command is not a markdown special character, so Kramdown won't interfere. Similarly fix `\theta^{* }` → `\theta^{\ast}` and `G^{* }` → `G^{\ast}`.

All occurrences to fix:
- `$\theta^{* }_i$` → `$\theta^{\ast}_i$`
- `$s^{* }$` → `$s^{\ast}$`
- `$G^{* }$` → `$G^{\ast}$`
- `G^{* }` → `G^{\ast}` (in display math too)
- `s^{* }` → `s^{\ast}` (in display math too)

### 1c. Fix inline math on line 159

**Line 159:** `$ \hat{G}_N = \frac{1}{N} \sum_{i=1}^N \hat{\theta}_i $`

The issue is that Kramdown may interpret `_N`, `_{i=1}`, `_i` as emphasis markers inside inline math delimited by `$...$`. The spaces after opening `$` and before closing `$` can also cause issues.

**Fix:** Remove the spaces inside the `$` delimiters and escape underscores, OR better yet, use Kramdown's native `$$...$$` inline math (which Kramdown treats as inline when on the same line, and display when on its own line):

```
The population estimate is $$\hat{G}_N = \frac{1}{N} \sum_{i=1}^N \hat{\theta}_i$$. Its MSE decomposes as:
```

**Note:** This same fix should be applied to ALL inline math using `$...$` that contains underscores. A systematic search-and-replace of `$...$` → `$$...$$` for inline math would be safest, but we should be careful not to break display math blocks.

### 1d. Fix `\square` usage — use Unicode or HTML instead

Since `\square` is used as a QED marker at the end of proof sketches inside `<details>` blocks, an alternative is to just use the Unicode character `□` or `∎` (end of proof) directly, avoiding the need for MathJax entirely in those spots. Or keep `$\square$` but ensure AMSsymbols is loaded (1a above).

**Fix:** Replace `$\square$` with `$\blacksquare$` or simply `∎` (Unicode U+220E). The `$\square$` with AMSsymbols loaded should also work after fix 1a.

---

## 2. Content Revisions Based on Feedback

### 2a. Reframe Theorem 4 (Impossibility of Pure Technocracy) — lines 396–427

**Current problem:** Assumption 4 states `Δ_S ≠ 0` as a given, which makes the "proof" circular — you assume experts are biased, then prove they're biased.

**Fix:** Reframe as a sampling/statistical argument:
- Remove the assumption that `Δ_S ≠ 0` is given.
- Instead, frame it probabilistically: "Given a random selection of k experts from a population of N, the probability that their mean value converges to the population mean is..."
- Use the Central Limit Theorem: if expert values are drawn from a subpopulation distribution, the sampling error on values is `O(1/√k)` which is large when `k ≪ N`.
- The key insight becomes: experts have LOW sampling error on facts (because they have access to ground truth, not because there are many of them) but HIGH sampling error on values (because they are a small, non-random sample).
- This avoids assuming "experts are evil/biased" — it's just that small samples have high variance, and self-selected samples have bias.

**Your note aligns:** "We just need to focus on experts being a small subpopulation, and therefore will have some bias (and large variance) in their value estimates."

### 2b. Add MSE / quadratic loss caveats — after Theorem 1 (around line 326)

**Current problem:** MSE implies symmetric quadratic loss. In social choice, losses are rarely symmetric — the public may prefer a slightly wrong policy that preserves rights over a perfectly efficient one that violates them.

**Fix:** Add a remark after Theorem 1 acknowledging:
- MSE is a proxy for "regret" but doesn't capture asymmetric preferences or catastrophic tail risks.
- Under non-quadratic loss (e.g., lexicographic preferences, rights constraints), the bias-variance trade-off changes qualitatively.
- This is a limitation of the linear model; the qualitative insight (experts trade value-bias for epistemic-accuracy) holds under more general loss functions.

### 2c. Add discussion of non-continuous value functions — after Theorem 2 (around line 364)

**Current problem:** Theorem 2 relies on Lipschitz continuity of `v_i`. This ignores "cliffs" — sacred values or taboos where a small change in outcome causes massive utility loss.

**Fix:** Add a remark discussing:
- If value functions have discontinuities (sacred values, taboos, lexicographic preferences), the Lipschitz bound breaks.
- A small expert error in the causal model that crosses a taboo line could cause unbounded utility loss.
- This is a genuine limitation: the separation theorem is most reliable for "smooth" policy domains and less reliable for domains involving rights, taboos, or sacred values.
- In those domains, additional safeguards (constitutional constraints, veto mechanisms) are needed.

### 2d. Distinguish additive vs structural causal-model errors — Section 2.4 / 3.4

**Current problem:** The paper treats belief errors and causal-model errors similarly (additive error terms in equation 10). But causal model errors are often multiplicative or structural — getting the *sign* of a derivative wrong is qualitatively different from getting the magnitude slightly wrong.

**Fix:** Add a paragraph in Section 3.4 (after line 206) discussing:
- The linear approximation in equation (10) treats causal-model error as additive: `Ĉ_i = C + ε_C`.
- In reality, causal model errors can be structural: e.g., believing printing money causes deflation (wrong sign) vs. getting the inflation rate slightly wrong (magnitude error).
- Structural errors correspond to `Ĉ_i ≈ -C` rather than `Ĉ_i ≈ C + ε`, which the linear model doesn't capture.
- This makes the case for expert input on causal models even stronger — structural errors are precisely the kind that don't wash out under aggregation and that experts are best positioned to correct.
- Acknowledge this as a limitation of the additive model.

### 2e. Reframe Section 4.4 expert bias — lines 247–259

**Current framing:** "experts are not a representative sample of the population's values. The shared training, professional culture, and self-selection..."

**Your preferred framing:** Focus on experts being a small subpopulation → inherent sampling bias and large variance in value estimates.

**Fix:** Rewrite Section 4.4 to lead with the statistical argument:
- Any subgroup of size `k ≪ N` drawn from a heterogeneous population will have sampling error in its value distribution.
- Expert groups are additionally non-random (self-selected, trained), which introduces systematic bias on top of sampling variance.
- The correlation of values within the expert group (from shared training) further reduces the effective sample size.
- This framing is more neutral — it doesn't require assuming experts are "biased" in a pejorative sense, just that they're a small, correlated sample.

### 2f. Expand on detecting value leakage — after Theorem 3 (around line 394)

**Current problem:** Theorem 3 introduces value leakage `λ` but doesn't discuss how to detect it in practice. Smart experts can hide value judgments inside complex causal models.

**Fix:** Add a discussion paragraph covering:
- Detection is hard when experts embed values in model assumptions (choice of discount rate, welfare weights, risk thresholds).
- Possible detection mechanisms: adversarial expert panels, requiring experts to submit models (not just conclusions), prediction market cross-checks, sensitivity analysis on model assumptions.
- The fundamental challenge: the more complex the causal model, the more places values can hide.
- This motivates institutional designs that separate model-building from value-weighting.

### 2g. Add discussion of aggregation function generality — Section 3 or Section 8

**Your concern:** "Does this analysis really apply to an aggregation fn?! Can we have more explanation of this!"

**Fix:** Add a paragraph (probably in Section 3, around line 146, or as a new subsection) discussing:
- The results are derived for the mean aggregation function. How do they generalise?
- For any aggregation function that is a weighted average (including median-like robust estimators), the bias-variance decomposition has a similar structure.
- For non-linear aggregation functions (e.g., maximin/Rawlsian), the error structure changes — bias in the tails matters more than bias in the mean.
- The qualitative insight (separate values from facts) holds for any aggregation function, but the quantitative bounds are specific to the mean.
- This is acknowledged as a limitation and direction for future work.

### 2h. Simplify overly-formal theorems with simulation references

**Your concern:** "Some of these theorems seem a little over-the-top / obvious? Maybe simple simulations would be better? They are just simple properties of averages?"

**Fix:** 
- Add a note at the start of Section 6 acknowledging that these results are, in a sense, "obvious" properties of averages — the contribution is making them precise and showing how they interact.
- For each theorem, add a forward reference to a simulation figure that illustrates the result empirically.
- Consider softening the language: instead of "Theorem" for the more straightforward results, use "Proposition" or "Result".

### 2i. Generalise Theorem 1 from scalar to vector — lines 291–327

**Fix:** Update Assumption 1 to use `Θ = ℝ^d` instead of `Θ = ℝ`. The MSE becomes trace of covariance matrices:
- `MSE(Ĝ_S) = ‖Bias(Ĝ_S)‖² + tr(Var(Ĝ_S))`
- The condition becomes: `‖Δ_S‖² + tr(Σ_e)/k > ‖μ_b‖² + tr(Σ_b^corr) + tr(Σ_ε)/N`
- The math is effectively the same but looks more professional and general.

---

## 3. Add Placeholder Simulation Figures

Add placeholder figures (with descriptive captions) at key points:

### Figure 1: After Theorem 1 (~line 327)
**Caption:** "Simulation: MSE of population estimate vs. expert estimate as a function of expert value bias Δ_S and population epistemic bias μ_b. [Placeholder — simulation code TBD]"

### Figure 2: After Theorem 2 (~line 364)  
**Caption:** "Simulation: Comparing conflated vs. separated mechanisms across varying levels of public epistemic error. [Placeholder — simulation code TBD]"

### Figure 3: After Theorem 3 (~line 394)
**Caption:** "Simulation: Delegation benefit as a function of value leakage λ, showing the crossover point where delegation becomes harmful. [Placeholder — simulation code TBD]"

### Figure 4: After Theorem 4 (~line 427)
**Caption:** "Simulation: Expert group MSE as a function of group size k, showing the irreducible error floor from value bias and correlation. [Placeholder — simulation code TBD]"

---

## 4. Minor Copy-Editing

- **Line 4:** Remove stray `"` in subtitle: `subtitle: An Information-Theoretic Framework for Democratic Governance"` → remove trailing quote.
- **`$\square$` → `$\blacksquare$`** or Unicode `∎` on lines 322, 361, 391, 423.
- Consistent use of `$$...$$` for inline math (Kramdown-safe) throughout.

---

## Summary of Files to Edit

| File | Changes |
|------|---------|
| `_includes/mathjax.html` | Add AMSmath + AMSsymbols extensions |
| `_drafts/inbetween-posts/2026-02-15-public-good.md` | All content fixes above |
