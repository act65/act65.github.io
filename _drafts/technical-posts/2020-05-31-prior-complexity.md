


***

Of course. This is the right way to build a solid piece of research. Let's integrate the foundational justification and refine the derivation into a clear, well-argued technical note.

***

### **Technical Note: Deriving the Implicit Prior of SGD from its Distributional Dynamics**

**Author:** Gemini
**Date:** November 16, 2025

**Abstract**
The remarkable generalization ability of deep neural networks is often attributed to an implicit inductive bias imparted by the Stochastic Gradient Descent (SGD) optimizer. This bias is qualitatively understood as a "preference for flat minima." This note provides a rigorous derivation of this implicit bias by modeling SGD as a continuous-time stochastic process. We begin by establishing the foundational link between such processes and Bayesian posteriors, inspired by work on Stochastic Gradient Langevin Dynamics. We then use this framework to treat the stationary distribution of the SGD process as an effective posterior. By disentangling the forces of the data likelihood from the total dynamics, we derive a closed-form expression for the score function of SGD's implicit prior. This result formalizes the inductive bias, showing it to be a non-uniform, geometry-aware prior whose influence is governed by the covariance of the mini-batch gradients.

---

### **1. Motivation: The Puzzle of SGD's Inductive Bias**

A purely deterministic analysis of vanilla Gradient Descent suggests it is a form of Maximum Likelihood Estimation, which corresponds to assuming a uniform (uninformative) prior on the model parameters. This conclusion is at odds with the empirical reality that SGD, without any explicit regularization, is a powerful regularizer in its own right. The source of this regularization lies in its stochastic nature. Our goal is to move beyond qualitative descriptions and derive a precise mathematical expression for the implicit prior that SGD imposes.

---

### **2. The Foundational Link: SDEs and Bayesian Posteriors**

The validity of our entire approach rests on a foundational link between Stochastic Differential Equations (SDEs) and Bayesian posterior distributions, famously solidified by Welling and Teh (2011) in their work on Stochastic Gradient Langevin Dynamics (SGLD).

The SGLD work demonstrated a **constructive, "forward" proof**:
1.  They started with a known target Bayesian posterior, `p(θ|D)`.
2.  They engineered a specific SDE (SGD with injected Gaussian noise).
3.  They proved that the stationary distribution of this SDE converges exactly to the target posterior.

This establishes a firm equivalence: **the stationary distribution of a Langevin-type SDE has the mathematical structure of a Bayesian posterior.**

We will use this established link in **reverse**.
1.  We start with a known process: standard SGD, with its inherent mini-batch noise.
2.  We model this process as an SDE.
3.  We then analyze the resulting stationary distribution, `p_s(θ)`, treating it as an **effective posterior**.

The SGLD result gives us the theoretical confidence to do this. It justifies treating `p_s(θ)` as a valid posterior distribution, allowing us to apply the standard rules of Bayesian inference, such as the additive property of score functions.

---

### **3. A Rigorous Derivation of the Implicit Prior**

The derivation proceeds in four clear steps.

#### **Step 3.1: The Target Framework (Ideal Bayesian Dynamics)**

In a Bayesian setting, the posterior is related to the likelihood and prior by `p(θ|D) ∝ p(D|θ)p(θ)`. The dynamics of sampling from this distribution can be described by its score function (the gradient of its log-probability). This gives us a simple additive relationship:
$$
\nabla_\theta \log p(\theta|D) = \nabla_\theta \log p(D|\theta) + \nabla_\theta \log p(\theta)
$$
Let's define our terms:
*   `Score_Posterior(θ)`: The ideal vector field for the posterior.
*   `Score_Likelihood(θ)`: The vector field from the data.
*   `Score_Prior(θ)`: The vector field from the prior.

This gives our target equation:
$$
\text{Score_Posterior}(\theta) = \text{Score_Likelihood}(\theta) + \text{Score_Prior}(\theta) \quad (*_1)
$$
**Assumption:** We connect this to machine learning by assuming the full-batch loss function, `L_full(θ)`, is the negative log-likelihood of the data `D`.
$$
L_{full}(\theta) \equiv -\log p(D|\theta)
$$
Under this standard assumption, the likelihood score is the negative gradient of the full loss:
$$
\text{Score_Likelihood}(\theta) = -\nabla_\theta L_{full}(\theta) \quad (*_2)
$$

#### **Step 3.2: The Algorithmic Reality (SGD Dynamics)**

We model the discrete SGD updates as a continuous-time SDE, which is accurate for small learning rates `η`:
$$
d\theta = \mu(\theta) dt + \sigma(\theta) dW_t
$$
The **drift `μ(θ)`** is the average update direction over all mini-batches `b`:
$$
\mu(\theta) = \mathbb{E}_b[-\eta \nabla L(\theta; b)] = -\eta \nabla L_{full}(\theta) \quad (*_3)
$$
The **diffusion matrix `D(θ)`** captures the noise from mini-batch sampling. It is the covariance of the gradient updates, where `D(θ) = σ(θ)σ(θ)^T`:
$$
D(\theta) = \eta^2 \text{Cov}_b[\nabla L(\theta; b)] \quad (*_4)
$$

#### **Step 3.3: Connecting Reality to the Framework**

The SDE process converges to a stationary distribution, `p_s(θ)`. As justified in Section 2, we treat this as our effective posterior. The score function of this stationary distribution is given by the Fokker-Planck equation's steady-state condition, which relates it to the drift and diffusion:
$$
\nabla_\theta \log p_s(\theta) = 2 D(\theta)^{-1} \mu(\theta) \quad (*_5)
$$

#### **Step 3.4: The Disentanglement (Solving for the Implicit Prior)**

We now equate the ideal posterior with the effective posterior by setting their scores equal. We start with our target equation `(*_1)` and substitute the score of the effective posterior `p_s(θ)` on the left-hand side:
$$
\nabla_\theta \log p_s(\theta) = \text{ScoreLikelihood}(\theta) + \text{Score_Implicit_Prior}(\theta)
$$
Using `(*_5)`, this becomes:
$$
2 D(\theta)^{-1} \mu(\theta) = \text{ScoreLikelihood}(\theta) + \text{ScoreImplicitPrior}(\theta)
$$
We now solve for the `Score_Implicit_Prior(θ)`:
$$
\text{ScoreImplicitPrior}(\theta) = 2 D(\theta)^{-1} \mu(\theta) - \text{ScoreLikelihood}(\theta)
$$
Finally, we substitute the explicit formulas for the drift `μ(θ)` from `(*_3)` and the likelihood score from `(*_2)`:
$$
\text{ScoreImplicitPrior}(\theta) = 2 D(\theta)^{-1} (-\eta \nabla L_{full}(\theta)) - (-\nabla L_{full}(\theta))
$$
Factoring out the `∇L_full(θ)` term gives our final result:

$$
\text{ScoreImplicitPrior}(\theta) = \left(I - 2\eta D(\theta)^{-1}\right) \nabla L_{full}(\theta)
$$

---

### **4. Interpretation and Discussion**

This result provides a concrete mathematical form for the inductive bias of SGD.

*   **The Prior is Not Uniform:** The score is clearly non-zero, confirming that SGD imposes a non-trivial prior. This prior adds a "force" that modifies the standard gradient descent trajectory.

*   **The Bias is Geometry-Aware:** The prior's score depends on `D(θ)⁻¹`, the inverse of the gradient covariance matrix. This means the prior is shaped by the local geometry of the loss landscape.

*   **Formalizing the "Preference for Flat Minima":**
    *   In a **wide, flat minimum**, the loss surface has low curvature. The gradients from different mini-batches are consistent, making the covariance `D(θ)` small. Consequently, its inverse `D(θ)⁻¹` is very large. The prior's score is dominated by the `-2η D(θ)⁻¹ ∇L_full` term, which acts as a strong regularizing force pushing against the likelihood gradient.
    *   In a **sharp, narrow minimum**, the loss has high curvature. Gradients are chaotic and vary wildly between mini-batches, making `D(θ)` large and `D(θ)⁻¹` small. The prior's influence diminishes, but the large diffusion `D(θ)` makes it easy for the parameters to be stochastically "kicked out" of such a sharp valley.

The combined effect is that the stationary distribution `p_s(θ)` concentrates its probability mass in wide, flat regions where the regularizing force of the prior is strong and the escaping force of diffusion is relatively weak. This provides a formal mechanism for the widely observed phenomenon that SGD favors solutions that generalize well.