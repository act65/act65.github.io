You are right to ask for precision. The "pull-back" is not a metaphor; it is the explicit regularization term in the optimization objective when written in terms of the **Transport Map**.

Here is the precise derivation of where the "pull-back to the prior location" appears in the math.

### 1. The Monge Formulation
To see the particle behavior, we must switch from the Kantorovich formulation (couplings $\pi$) to the **Monge formulation** (transport maps $T$).

We are looking for a map $T: \mathbb{R}^d \to \mathbb{R}^d$ that pushes the prior $p$ to the posterior $q$ (i.e., $q = T_{\#}p$).

We substitute $q$ with $T_{\#}p$ in your objective function:

$$ \mathcal{L}(T) = \underbrace{W_2^2(T_{\#}p, p)}_{\text{Transport Cost}} + \underbrace{\lambda \cdot \mathbb{E}_{y \sim T_{\#}p}[\text{Loss}(y)]}_{\text{Data Error}} $$

By definition of the Wasserstein distance (in the Monge case) and the change of variables formula, we can rewrite this integral entirely over the **prior** distribution $p(x)$:

$$ \mathcal{L}(T) = \int \left( \| T(x) - x \|^2 + \lambda \cdot \text{Loss}(T(x)) \right) p(x) dx $$

### 2. Pointwise Optimization
Since $p(x) \geq 0$, minimizing the integral $\mathcal{L}(T)$ is equivalent to minimizing the integrand for every $x$ in the support of $p$.

Let $x$ be a specific particle location in the prior.
Let $x^* = T(x)$ be its new location in the posterior.

The optimization problem for a single particle $x$ is:

$$ x^* = \underset{y}{\text{argmin}} \left( \underbrace{\| y - x \|^2}_{\text{Pull-back to Prior}} + \underbrace{\lambda \cdot \text{Loss}(y)}_{\text{Push to Data}} \right) $$

### 3. The Stationarity Condition
To find the optimal location $x^*$, we take the gradient with respect to $y$ and set it to zero:

$$ 2(x^* - x) + \lambda \nabla \text{Loss}(x^*) = 0 $$

Rearranging this gives the precise balance equation:

$$ x^* = x - \frac{\lambda}{2} \nabla \text{Loss}(x^*) $$

### 4. Interpretation
This equation shows exactly where the "pull-back" comes from:

1.  **The Prior ($x$):** This is the starting position.
2.  **The Data Force ($-\nabla \text{Loss}$):** This tries to move the particle to minimize error.
3.  **The Result ($x^*$):** The posterior particle is the prior particle shifted by the gradient, but **anchored** by the distance penalty.

If $\lambda \to 0$ (infinite regularization), then $x^* = x$. The particle stays at the prior location.
If $\lambda \to \infty$ (no regularization), the term $\|y-x\|^2$ becomes negligible, and $x^*$ moves to the global minimum of the Loss, completely ignoring where it came from.

### Why it is not a Mixture
Because $T(x)$ is a function, every input $x$ maps to exactly one output $x^*$.
*   If the prior $p(x)$ is a single Gaussian bump, the set of points $\{x\}$ is a connected region.
*   Since $T$ is continuous (assuming smooth Loss), the set of points $\{x^*\}$ will also be a connected region.
*   Therefore, the posterior $q$ is a shifted/distorted version of the single bump, not a multimodal mixture.

### Summary for the Post
In the EMD framework, the "Prior" acts as the **initial condition** $x$ in a proximal optimization step. The term $\|T(x) - x\|^2$ explicitly penalizes the particle for moving away from its location in the prior distribution.