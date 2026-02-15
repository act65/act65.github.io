"""
Generate Figures 1–4 for "Defining the Public Good" blog post.

Each figure illustrates a key result from the paper:
  Figure 1 (Prop 1):  Bias-variance characterisation – MSE crossover surface
  Figure 2 (Thm 2):   Separation dominance – conflated vs separated mechanisms
  Figure 3 (Thm 3):   Delegation bounds – MSE vs value leakage λ
  Figure 4 (Prop 4):  Limits of pure technocracy – expert MSE vs group size k

Dependencies: jax, jaxlib, matplotlib, numpy
"""

import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pathlib import Path

# ── Style ────────────────────────────────────────────────────────────────────
mpl.rcParams.update({
    "figure.dpi": 150,
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "figure.figsize": (7, 5),
})

OUT_DIR = Path("../images/public-good")
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════════════
# Figure 1 – Bias-Variance Characterisation (Proposition 1)
#
# MSE_pop  = ‖μ_b‖² + ρ_b·σ²_b + σ²_ε / N
# MSE_exp  = ‖Δ_S‖² + σ²_e / k
#
# We plot both as functions of ‖Δ_S‖ for several values of ‖μ_b‖,
# and mark the crossover where MSE_pop = MSE_exp.
# ═══════════════════════════════════════════════════════════════════════════════

def figure1():
    N = 10_000          # population size
    k = 50              # expert group size
    sigma2_eps = 1.0    # idiosyncratic noise variance (population)
    sigma2_e = 0.3      # idiosyncratic noise variance (experts, lower)
    rho_b = 0.05        # pairwise correlation of systematic biases
    sigma2_b = 1.0      # variance of systematic biases

    delta_S = jnp.linspace(0, 3, 300)  # expert value bias ‖Δ_S‖

    mse_exp = delta_S**2 + sigma2_e / k  # expert MSE

    mu_b_values = [0.0, 0.5, 1.0, 1.5, 2.0]
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, len(mu_b_values)))

    fig, ax = plt.subplots()
    for mu_b, c in zip(mu_b_values, colors):
        mse_pop = mu_b**2 + rho_b * sigma2_b + sigma2_eps / N
        ax.axhline(mse_pop, color=c, ls="--", alpha=0.6,
                    label=rf"Pop MSE ($\|\mu_b\|={mu_b:.1f}$)")

    ax.plot(delta_S, mse_exp, "k-", lw=2, label=r"Expert MSE")

    ax.set_xlabel(r"Expert value bias $\|\Delta_S\|$")
    ax.set_ylabel("MSE")
    ax.set_title("Figure 1: Population vs Expert MSE\n(Bias-Variance Characterisation)")
    ax.legend(loc="upper left", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_bias_variance.png")
    plt.close(fig)
    print(f"  Saved {OUT_DIR / 'fig1_bias_variance.png'}")


# ═══════════════════════════════════════════════════════════════════════════════
# Figure 2 – Separation Dominance (Theorem 2)
#
# Conflated mechanism: each person reports θ̂_i = v_i(Ĉ_i(a | ŝ_i))
#   MSE_conflated ≈ L² · (σ²_s_pub + σ²_C_pub) + σ²_v / N
#
# Separated mechanism: values from public, facts/causal from experts
#   MSE_separated ≈ L² · (σ²_s_exp + σ²_C_exp) + σ²_v / N
#
# We sweep public epistemic error while holding expert epistemic error fixed.
# ═══════════════════════════════════════════════════════════════════════════════

def figure2():
    N = 10_000
    L = 1.0                     # Lipschitz constant
    sigma2_v = 1.0              # value noise variance
    sigma2_s_exp = 0.01         # expert belief error (small, fixed)
    sigma2_C_exp = 0.02         # expert causal-model error (small, fixed)

    # public epistemic error (swept)
    pub_epistemic = jnp.linspace(0, 3, 300)
    # assume belief and causal errors are equal for simplicity
    sigma2_s_pub = pub_epistemic**2 / 2
    sigma2_C_pub = pub_epistemic**2 / 2

    mse_conflated = L**2 * (sigma2_s_pub + sigma2_C_pub) + sigma2_v / N
    mse_separated = L**2 * (sigma2_s_exp + sigma2_C_exp) + sigma2_v / N

    fig, ax = plt.subplots()
    ax.plot(pub_epistemic, mse_conflated, "r-", lw=2,
            label="Conflated mechanism")
    mse_sep_val = float(L**2 * (sigma2_s_exp + sigma2_C_exp) + sigma2_v / N)
    ax.axhline(mse_sep_val, color="b", ls="-", lw=2,
               label="Separated mechanism")
    ax.fill_between(np.array(pub_epistemic),
                    np.array(mse_separated),
                    np.array(mse_conflated),
                    alpha=0.15, color="green",
                    label="Separation advantage")

    ax.set_xlabel(r"Public epistemic error $\|\hat{s} - s^*\|$")
    ax.set_ylabel("MSE")
    ax.set_title("Figure 2: Conflated vs Separated Mechanisms\n(Separation Dominance)")
    ax.legend(loc="upper left", framealpha=0.9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig2_separation.png")
    plt.close(fig)
    print(f"  Saved {OUT_DIR / 'fig2_separation.png'}")


# ═══════════════════════════════════════════════════════════════════════════════
# Figure 3 – Delegation Bounds (Theorem 3)
#
# With value leakage λ, the separated mechanism's error becomes:
#   MSE_sep(λ) ≈ L² · λ² · ‖∇v_E‖² + σ²_v / N
#
# The conflated mechanism's error is:
#   MSE_conf ≈ L² · ‖s̄ - s*‖² + σ²_v / N
#
# Delegation benefit = MSE_conf − MSE_sep(λ).
# Crossover at λ* = ‖s̄ - s*‖ / (L · ‖∇v_E‖).
# ═══════════════════════════════════════════════════════════════════════════════

def figure3():
    N = 10_000
    L = 1.0
    sigma2_v = 1.0
    grad_v_E_norms = [0.5, 1.0, 2.0]  # different expert value gradient magnitudes
    pub_belief_error = 1.5             # ‖s̄ − s*‖

    lam = jnp.linspace(0, 3, 300)

    mse_conf = L**2 * pub_belief_error**2 + sigma2_v / N

    colors = ["#2196F3", "#FF9800", "#E91E63"]
    fig, ax = plt.subplots()

    for grad_norm, c in zip(grad_v_E_norms, colors):
        mse_sep = L**2 * lam**2 * grad_norm**2 + sigma2_v / N
        benefit = mse_conf - mse_sep

        ax.plot(lam, benefit, color=c, lw=2,
                label=rf"$\|\nabla v_E\| = {grad_norm}$")

        # mark crossover
        lam_star = pub_belief_error / (L * grad_norm)
        if lam_star <= 3.0:
            ax.plot(lam_star, 0, "o", color=c, ms=8, zorder=5)

    ax.axhline(0, color="gray", ls=":", lw=1)
    ax.fill_between([0, 3], [0, 0], [-5, -5], alpha=0.06, color="red")
    ax.text(2.5, -0.3, "Delegation\nharmful", ha="center", color="red",
            fontsize=9, style="italic")
    ax.text(0.3, 1.5, "Delegation\nbeneficial", ha="center", color="green",
            fontsize=9, style="italic")

    ax.set_xlabel(r"Value leakage $\lambda$")
    ax.set_ylabel(r"Delegation benefit (MSE$_{\mathrm{conf}}$ − MSE$_{\mathrm{sep}}$)")
    ax.set_title("Figure 3: Delegation Benefit vs Value Leakage\n(Delegation Bounds)")
    ax.legend(loc="upper right", framealpha=0.9)
    ax.set_ylim(-2, mse_conf + 0.5)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig3_delegation.png")
    plt.close(fig)
    print(f"  Saved {OUT_DIR / 'fig3_delegation.png'}")


# ═══════════════════════════════════════════════════════════════════════════════
# Figure 4 – Limits of Pure Technocracy (Proposition 4)
#
# MSE_expert(k) = Δ_S² + (σ²_v / k) · (1 + (k−1)·ρ_S)
#               → Δ_S² + ρ_S · σ²_v   as k → ∞
#
# Population MSE (value component only, no epistemic bias for comparison):
#   MSE_pop(N) = σ²_v / N
#
# We plot expert MSE vs k for several ρ_S, and overlay population MSE.
# ═══════════════════════════════════════════════════════════════════════════════

def figure4():
    sigma2_v = 1.0      # value variance
    Delta_S = 0.5       # expert value bias (moderate)

    k_vals = jnp.arange(1, 501)
    rho_values = [0.0, 0.1, 0.3, 0.5, 0.8]
    colors = plt.cm.magma(np.linspace(0.15, 0.85, len(rho_values)))

    # population MSE (value-only, no epistemic bias, for comparison)
    N_vals = jnp.arange(1, 501)
    mse_pop = sigma2_v / N_vals

    fig, ax = plt.subplots()

    for rho, c in zip(rho_values, colors):
        mse_exp = Delta_S**2 + (sigma2_v / k_vals) * (1 + (k_vals - 1) * rho)
        ax.plot(k_vals, mse_exp, color=c, lw=2,
                label=rf"Expert ($\rho_S = {rho}$)")
        # show asymptote
        floor = Delta_S**2 + rho * sigma2_v
        ax.axhline(floor, color=c, ls=":", lw=0.8, alpha=0.5)

    ax.plot(N_vals, mse_pop, "k--", lw=2, label=r"Population ($\rho=0$, no bias)")

    ax.set_xlabel(r"Group size $k$ (experts) / $N$ (population)")
    ax.set_ylabel("MSE (value component)")
    ax.set_title("Figure 4: Expert MSE vs Group Size\n(Limits of Pure Technocracy)")
    ax.legend(loc="upper right", framealpha=0.9, ncol=2)
    ax.set_ylim(0, 3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig4_technocracy.png")
    plt.close(fig)
    print(f"  Saved {OUT_DIR / 'fig4_technocracy.png'}")


# ── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating figures for 'Defining the Public Good'…")
    figure1()
    figure2()
    figure3()
    figure4()
    print("Done.")
