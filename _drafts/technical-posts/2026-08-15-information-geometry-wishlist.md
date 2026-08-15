---
title: The Information Geometry Wishlist
subtitle: Everything we would want from the geometry of a model reduces to two capabilities we do not have.
layout: post
categories:
    - proposal
description: "A companion to the Bayesian computation wishlist. Information geometry says there is a uniquely correct way to measure distance between models, take a step, and project onto a family. Almost all of it reduces to two primitives — estimating the metric, and solving the geodesic boundary value problem — and neither is affordable."
tags:
  - notes
  - information-theory
  - machine-learning
  - mathematics
---

This is a companion to [the Bayesian computation wishlist]({{site.baseurl}}/modern-ml-prob-utils/), and it has the same shape. There, the story was: here are theorems saying this is the right thing to do, here is what we would do if we could, and here is the integral that stops us. This one is about geometry rather than inference, but it ends at the same kind of wall — and possibly at exactly the same integral.

The setup is this. A statistical model is a set of probability distributions. The parameters $\theta$ are just coordinates we put on that set, and the choice of coordinates is arbitrary. But almost every algorithm we actually run is written in those coordinates:

- Gradient descent steps along $-\nabla_\theta L$, which presumes a unit step in $\theta_1$ and a unit step in $\theta_2$ are somehow comparable.
- $L_2$ regularisation penalises $\|\theta\|^2$, which presumes the same thing.
- Early stopping, trust regions, and "the distance between two checkpoints" all quietly assume a notion of distance.

Reparameterise the model — swap variance for log-variance, rescale a layer — and the *set of distributions is unchanged* while the algorithm's trajectory changes. That should be uncomfortable. It means some fraction of what our optimisers do is an artefact of notation.

Information geometry is the claim that there's a better answer available: put the geometry on the *distributions*, not on the coordinates. What makes this more than an aesthetic preference is that the choice turns out to be forced.

### The theorems that make this non-optional

Three results do most of the work, and they play the role Bayes' theorem and Wald's complete class theorem play in the other post.

**Chentsov's theorem.** [^chentsov] If you ask for a Riemannian metric on a space of distributions that is invariant under sufficient statistics — a notion of distance that doesn't change when you process the data in a way that loses no information — then on a finite sample space the Fisher information metric is the *only* one, up to an overall scale. Chentsov proved a matching uniqueness result for the affine connections: the $\alpha$-connections are the only invariant ones. Campbell extended this to unnormalised measures, and Ay, Jost, Lê and Schwachhöfer to infinite sample spaces. [^campbell] [^ay]

This is the most persuasive fact in the area. The Fisher metric isn't a convenient choice; it's the unique choice consistent with a very weak-sounding requirement. Euclidean geometry on $\theta$ does not satisfy that requirement, so every optimiser we run is knowingly using the wrong one.

**Eguchi's construction.** [^eguchi] Any smooth divergence $D(p \| q)$ induces a metric (from its second derivative at $p=q$) and a *dual pair* of connections (from its third derivatives). A divergence and a geometry are the same object seen from two sides — so choosing an objective function *is* choosing a geometry, whether or not you meant to.

**Amari's dually flat structure.** [^amari-nagaoka] For an exponential family the geometry has two flat coordinate systems at once — natural parameters $\theta$ and expectation parameters $\eta = \mathbb{E}[T(x)]$, related by a Legendre transform. In such a space you get a generalised Pythagorean theorem and a projection theorem: $D(p\|r) = D(p\|q) + D(q\|r)$ exactly, when the relevant geodesics meet at right angles, plus uniqueness of projections onto flat submanifolds.

That last one is why this isn't decoration. Maximum likelihood, maximum entropy, EM, moment matching and variational inference all turn out to be *projections* in this geometry, and the Pythagorean theorem is exact bookkeeping for what each of them throws away.

### The two things we cannot do

Having spent some time writing code for this, I've come to think the wishlist below is misleadingly long. Nearly every item reduces to one or both of two capabilities, and it's cleaner to state those first and treat the rest as consequences.

*   **Primitive 1: evaluate the metric at a point.**
    Given $\theta$, produce $g_{ij}(\theta) = \mathbb{E}_{x\sim p_\theta}[\partial_i \log p_\theta(x)\,\partial_j \log p_\theta(x)]$ — or, more modestly, the scalar $v^\top g(\theta) v$ for a given direction. This is the *local* capability: it tells you the shape of the space in an infinitesimal neighbourhood.

*   **Primitive 2: solve the geodesic boundary value problem.**
    Given two points $\theta_0, \theta_1$, find the geodesic connecting them — the curve minimising $\int_0^1 \|\dot\theta\|^2_{g(\theta)}\,dt$, equivalently the solution of $\ddot\theta^k = -\Gamma^k_{ij}\dot\theta^i\dot\theta^j$ with both endpoints pinned. This is the *connecting* capability: distance, interpolation, the log map, and every projection are downstream of it.

Neither is available in general, and they fail for different reasons.

**Why the metric is hard.** It's a $d\times d$ object; at $d=10^9$ that's $10^{18}$ entries before you invert anything. But the deeper problem at small $d$ is that the expectation is over the *model's own* distribution, so you're estimating it by Monte Carlo, and a Monte Carlo metric is a noisy metric. Two things I did not expect until I hit them:

- Bad metric estimates fail *silently*. I had a bug where a Gaussian-mixture family received the same random key for every Monte Carlo sample, so all of them selected the same mixture component and the estimator was measuring one Gaussian's Fisher metric rather than the mixture's. The result was about 19% off. It did not look wrong: the numbers were finite, smooth, of plausible magnitude, and the estimator's *variance went down*, because there was only one source of randomness left. A metric you cannot check is worse than no metric.
- Substituting observed data for model samples — the "empirical Fisher" — gives a genuinely different matrix that can behave badly as a stand-in, in ways that are also not locally visible. [^kunstner]

**Why the BVP is hard.** Forward integration is fine: given a point and a velocity, integrating the geodesic ODE forward (the initial value problem, the exponential map) is a standard ODE solve. Pinning *both* ends is a different animal. Shooting methods optimise the initial velocity until you land on the target and diverge readily when the endpoints are far apart; variational methods parameterise the path and minimise its energy, which can't diverge but converges to something that is only approximately a geodesic. In a library I've been writing, the fast variational solver costs on the order of 100 ms per jitted solve, the hybrid solver (variational warm start, Newton polish) costs seconds, and naive shooting costs tens of seconds. A flow-matching training loop wants one of these per sample per step. Do that arithmetic and the geometry dominates the cost of everything else by orders of magnitude.

And the accuracy is not reliable either. A trap that cost me real debugging time: **an endpoint residual does not establish a geodesic.** A solver can hit both endpoints to $10^{-6}$ and return a curve carrying four hundred times the energy of the straight chord. You have to check endpoint error, speed constancy *and* energy, and on a Gaussian mixture with the Fisher–Rao metric I did not find a solver configuration that returned an actual geodesic by all three.

The practical consequence: that library now essentially only supports closed-form manifolds. Not by design — by attrition. Where a closed form exists you get both primitives for free and everything works; where it doesn't, the estimated versions are too slow and too quietly wrong to build on.

**What buys you both at once.** The Legendre map $\theta \leftrightarrow \eta$, $\eta = \nabla\psi(\theta)$. In a dually flat space the metric is $g = \nabla^2\psi$ and the dual geodesics are *straight lines* — in $\eta$ coordinates for m-geodesics, in $\theta$ coordinates for e-geodesics — so the BVP becomes linear interpolation in the right chart. Both primitives collapse to closed forms simultaneously.

But $\psi(\theta) = \log\int e^{\theta\cdot T(x)}d\nu(x)$ is the log-partition function, and computing $\nabla\psi$ is computing the model's moments, which is inference. **The Legendre transform is exactly as expensive as the marginalisation problem from the other post.** That's the link between the two posts, and it's tight: when you can do inference in closed form you get the geometry for free, and when you can't, you get neither.

One caveat worth stating because it surprised me: dual flatness buys you the $\pm 1$-geodesics, not the Levi-Civita ones. Fisher–Rao distance uses the $\alpha=0$ connection, which is *not* flat even in an exponential family. This is why the Fisher–Rao distance between two multivariate Gaussians — as canonical an exponential family as exists — still has no known closed form and remains the subject of approximation papers. [^nielsen-fr]

### What derives from what

With that framing, the rest of the wishlist is bookkeeping. The useful column is the last one.

| Operation | Needs metric | Needs BVP |
|---|---|---|
| Natural gradient | ✓ (and its inverse) | — |
| Volume element / Jeffreys prior | ✓ (determinant) | — |
| Curvature | ✓ (derivatives of) | — |
| Exponential map / geodesic step | ✓ | — (IVP only) |
| Fisher–Rao distance | ✓ | ✓ |
| Log map, geodesic interpolation | ✓ | ✓ |
| Parallel transport between two points | ✓ | ✓ |
| m-projection and e-projection | ✓ | ✓ |
| Pythagorean decomposition | ✓ | ✓ |

Which explains something I'd previously filed as an accident. **The natural gradient is the only item from this list that made it into practice, and it is exactly the item that needs no BVP.** It needs a metric–vector product at the current point and then takes a straight step. Everything requiring two points to be connected has stayed in the papers.

### The items themselves

*   **1. The natural gradient** — steepest descent in the Fisher metric, $\tilde\nabla L = g^{-1}\nabla L$: the step that most reduces the loss per unit change *in the distribution*, rather than per unit change in the numbers. It's invariant to reparameterisation, which is the property we wanted at the start, and Amari showed it's asymptotically Fisher-efficient in the online setting. [^amari-ng] K-FAC, natural policy gradients, TRPO and natural evolution strategies are all attempts to approximate it, [^martens] [^kfac] [^kakade] and mirror descent turns out to be natural gradient descent in the dual coordinates. [^raskutti] The cost is the $g^{-1}$: exact inversion is $O(d^3)$, so everything practical is a structural lie about $g$ that makes it invertible — block-diagonal by layer, Kronecker-factored, or diagonal. Adam is arguably the crudest and most successful member of that family, and one reading of the last decade of optimiser research is a search for the best affordable approximation to a matrix nobody can write down.

*   **2. Fisher–Rao distance** — the unique invariant, symmetric, coordinate-free distance between two distributions. Every time we compare two models we currently do something indefensible: Euclidean distance in weight space, or a KL divergence that's asymmetric and violates the triangle inequality. Fisher–Rao is the honest answer, and the one that would let us say "these two checkpoints are the same model" without qualification. Closed forms exist for a handful of families: on the simplex the geometry is a sphere under $p\mapsto 2\sqrt p$, giving $2\arccos\sum_i\sqrt{p_iq_i}$, and the univariate normal family is the hyperbolic plane in disguise. Everywhere else it's Primitive 2, with all the caveats above.

*   **3. The volume element $\sqrt{\det g}$** — the invariant measure on the model manifold, i.e. how much room a region of parameter space actually occupies in *distribution* space. It's Jeffreys' prior, and it appears in Rissanen's stochastic complexity, where $\log\int\sqrt{\det g}\,d\theta$ measures how many *distinguishable* models a family contains. [^rissanen] That's the right way to think about model complexity; parameter counting is a coordinate artefact. Needs a determinant of a matrix you can't store, integrated over parameter space, and frequently divergent anyway.

*   **4. Curvature** — how far the model is from flat. Efron called the statistical version the curvature of the estimation problem. [^efron] It controls second-order effects: the bias of maximum likelihood, how much information a first-order method discards, whether asymptotic normality is any good at your sample size. Exponential families are flat, which is why everything works there; the models we care about are not. The Riemann tensor has $O(d^4)$ components, and I've never seen it computed for a model of any size.

*   **5. Geodesic steps and parallel transport** — actually following the curved manifold when you step, and moving a vector (a momentum buffer, a previous gradient) between points without it silently changing meaning. Natural gradient descent still takes *straight* steps in a curved space: it corrects the metric but not the path. Momentum, conjugate gradients and quasi-Newton methods all accumulate vectors computed at different points as though they lived in the same space, which they don't. Transport along a *known* geodesic is an IVP and affordable; transport between two given points is not.

*   **6. The m-projection** — $\arg\min_{p\in M} D(q\|p)$, reached by an m-geodesic meeting $M$ orthogonally. Maximum likelihood *is* the m-projection of the empirical distribution onto the model; so is moment matching, and so is the expectation-propagation update. Fitting a model isn't analogous to a projection, it is one. In an exponential family this reduces to solving $\nabla\psi(\theta)=\hat\eta$ — the Legendre map, i.e. inference again.

*   **7. The e-projection** — the same thing with the arguments reversed, $\arg\min_{p\in M} D(p\|q)$. This is variational inference. It's also maximum entropy under moment constraints, which is the e-projection of the uniform distribution onto an m-flat constraint set. The mode-seeking behaviour everyone complains about in VI isn't a bug in the algorithm; it's what this projection is.

*   **8. The Pythagorean decomposition** — when the m-geodesic from $p$ to $q$ meets the e-geodesic from $q$ to $r$ at right angles, $D(p\|r)=D(p\|q)+D(q\|r)$ exactly. It turns approximation error into an additive budget, and it's the cleanest way to see EM, which Amari and Csiszár–Tusnády describe as alternating projections between a data manifold and a model manifold. [^amari-em] [^csiszar] EM's monotone convergence stops being a lemma and becomes a picture. You need both projections, and the orthogonality holds under flatness conditions neural networks do not satisfy.

### The obstacle that isn't computational

Everything above is a cost problem, and cost problems sometimes yield. This one doesn't.

Neural networks are *singular* models: permuting hidden units or rescaling across a ReLU changes $\theta$ without changing $p_\theta$, so the map from parameters to distributions isn't injective and the Fisher matrix is degenerate on sets of positive dimension. [^watanabe] The model isn't a manifold. Both primitives above presuppose that it is — a degenerate metric has no inverse, so no natural gradient; a non-manifold has no unique geodesic, so no BVP to solve.

Watanabe's response replaces the parameter count in BIC with a learning coefficient obtained by resolution of singularities, which suggests the fix is real but lives in algebraic geometry rather than Riemannian geometry. I don't understand this well enough to say more, and it's the direction I'd want to read next.

---

A caveat I should state plainly, because the post above is more enthusiastic than my actual confidence. Information geometry's practical yield so far is roughly one idea — the natural gradient — plus the reframing of things we already knew how to do. The Pythagorean theorem has not, as far as I can tell, made anyone's model better.

The table gives me a slightly better guess as to why than "it's expensive". Everything that shipped needs only a local metric–vector product; everything that didn't needs two points connected. That's a specific missing capability rather than a vague one, and it's at least the kind of thing that could be attacked — better BVP solvers, or families engineered so the closed forms exist. Whether that's worth attacking depends on whether the coordinate-invariance argument is as load-bearing as Chentsov makes it sound. If it is, every algorithm that steps in $\theta$ is making an arbitrary choice, and arbitrary choices usually cost something. But "usually" is doing work there, and I can't demonstrate the cost.

---
### References

[^chentsov]: Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society. (Russian original 1972.)
[^campbell]: Campbell, L. L. (1986). An extended Čencov characterization of the information metric. *Proceedings of the American Mathematical Society, 98*(1), 135–141.
[^ay]: Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). *Information Geometry*. Springer.
[^eguchi]: Eguchi, S. (1992). Geometry of minimum contrast. *Hiroshima Mathematical Journal, 22*(3), 631–647.
[^amari-nagaoka]: Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society / Oxford University Press. Nielsen, F. (2020). An elementary introduction to information geometry. *Entropy, 22*(10), 1100 — is the gentler entry point.
[^kunstner]: Kunstner, F., Balles, L., & Hennig, P. (2019). Limitations of the empirical Fisher approximation for natural gradient descent. *Advances in Neural Information Processing Systems, 32*.
[^nielsen-fr]: Nielsen, F. (2023). A simple approximation method for the Fisher–Rao distance between multivariate normal distributions. *Entropy, 25*(4), 654.
[^amari-ng]: Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation, 10*(2), 251–276.
[^martens]: Martens, J. (2020). New insights and perspectives on the natural gradient method. *Journal of Machine Learning Research, 21*(146), 1–76.
[^kfac]: Martens, J., & Grosse, R. (2015). Optimizing neural networks with Kronecker-factored approximate curvature. *International Conference on Machine Learning*.
[^kakade]: Kakade, S. (2001). A natural policy gradient. *Advances in Neural Information Processing Systems, 14*. See also Schulman, J., Levine, S., Moritz, P., Jordan, M., & Abbeel, P. (2015). Trust region policy optimization. *ICML*.
[^raskutti]: Raskutti, G., & Mukherjee, S. (2015). The information geometry of mirror descent. *IEEE Transactions on Information Theory, 61*(3), 1451–1457.
[^rissanen]: Rissanen, J. (1996). Fisher information and stochastic complexity. *IEEE Transactions on Information Theory, 42*(1), 40–47.
[^efron]: Efron, B. (1975). Defining the curvature of a statistical problem (with applications to second order efficiency). *The Annals of Statistics, 3*(6), 1189–1242.
[^amari-em]: Amari, S. (1995). Information geometry of the EM and em algorithms for neural networks. *Neural Networks, 8*(9), 1379–1408.
[^csiszar]: Csiszár, I., & Tusnády, G. (1984). Information geometry and alternating minimization procedures. *Statistics and Decisions, Supplement Issue 1*, 205–237.
[^watanabe]: Watanabe, S. (2009). *Algebraic Geometry and Statistical Learning Theory*. Cambridge University Press.
