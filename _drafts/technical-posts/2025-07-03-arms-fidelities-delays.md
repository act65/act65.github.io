---
layout: post
title: The Price of Precision
subtitle: A Unified Model for Multi-Fidelity Bandits
categories: research
---

In the classic Multi-Armed Bandit (MAB) problem, an agent chooses between several slot machines (or "arms") to maximize its reward. It's a powerful metaphor for decision-making under uncertainty. But what if pulling an arm isn't a single action, but a choice with its own set of costs and information quality? What if, before you pull the real arm, you could pay for a less accurate "test" pull?

This post introduces the **Progressive-Fidelity Bandit**, a framework for balancing not just exploration and exploitation, but also the cost and quality of information itself. This problem is often formalized in the literature as the Multi-Fidelity Multi-Armed Bandit (MF-MAB) problem [^1], and our goal is to propose an elegant, unified way to think about it by introducing a new strategic dimension: **commitment**.

<!-- need to rework this intro!?!
MAB -> MF-MAB -> Commited-MF-MAB -->

### The Motivation: When Information Isn't Free

In many real-world scenarios, we have access to a hierarchy of information sources, each with its own cost and accuracy.

1.  **Drug Discovery:** A pharmaceutical company can use cheap, fast, but inaccurate computer simulations to predict a drug candidate's efficacy. More accurate quantum mechanics-based simulations are more expensive. Animal testing is even more so. Finally, a full Randomized Controlled Trial (RCT) on humans is incredibly expensive but provides the most accurate data. The "arm" is the drug candidate, and the "fidelity level" is the evaluation method.

2.  **A/B Testing in Tech:** A company wants to test a new feature on its website (the "arm"). It could start with an internal simulation of user behavior (very cheap, low fidelity). It could then run a small-scale "canary" test on 1% of its users (more expensive, more accurate). Finally, it could roll it out to 50% of users in a full A/B test (most expensive, most accurate).

3.  **Minimum Viable Product (MVP) Development:** A startup building a new software product has an idea for a core feature ("the arm"). Instead of building the full, polished version, they can test the waters with progressively higher-fidelity versions. A low-fidelity probe could be a simple landing page describing the feature to gauge interest. A medium-fidelity probe might be an interactive prototype. The highest-fidelity action is developing and launching the actual MVP.

4.  **Resource Exploration:** An energy company is searching for oil. The "arms" are different geographical locations. The company can use cheap satellite imagery to get a rough idea of the geology. This is a low-cost, low-fidelity probe. Based on those results, it can conduct more expensive and detailed seismic surveys. Finally, the most expensive and accurate action is to drill an exploratory well.

In all these cases, the core decision is not just *which* arm to investigate, but *how much* to pay for the quality of that investigation. This is closely related to the problem of bandits with costly probes, where an agent can pay a fee to observe an arm's reward before committing to a pull. [^2]

### How Do We Measure Success? Framing the Goal

Before we can solve this problem, we must define what "winning" looks like. The cost and quality of information introduce new strategic trade-offs, leading to several ways to frame the agent's objective.

| Framing | The Goal | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Best Arm Identification (BAI)** | Identify the single best arm with high confidence, as **cheaply** as possible. | Natural for "find the winner" problems like drug discovery. The objective is clear and focused on exploration. | Ignores rewards (and costs) accrued *during* the process. Can be inefficient if the best arm is only marginally better than a much cheaper-to-identify alternative. |
| **Cost-in-Regret** | Maximize the cumulative **net reward** (`reward - cost`) over a long time horizon. | Captures the ongoing trade-off between earning and learning at every step. | A naive implementation encourages the agent to choose low-fidelity actions (which have low-cost) in the long term. |
| **Budgeted Exploration** | Achieve the best possible outcome within a fixed total **cost budget**. | Highly practical and reflects real-world project constraints. | It's a constraint, not an objective. It creates an artificial "two-phase" system (explore, then exploit) which can be rigid. |

Each of these framings has merit, but they also expose a certain "clunkiness." The BAI and Budgeted models create a hard switch between an exploration phase and an exploitation phase. The Cost-in-Regret model, while trying to be unified, has a fundamental paradox: once the agent identifies the best arm, it may choose to repeatedly pull a low-cost, low-reward version of it forever, because the net reward (`reward - cost`) is positive. It never graduates to the high-cost, high-reward "deployment" action that represents true exploitation. This suggests we are missing a key ingredient.

### The Elegance of Commitments: A Unified Framework

The solution to the Cost-in-Regret paradox and the rigidity of other models is to introduce a third dimension to the agent's decision: **commitment**, modeled as a **delay**ed reward.

This concept is related to, but critically different from, the field of bandits with delayed feedback [^3]. In that setting, the delay is an environmental factor you cannot control, and the agent is free to take other actions while waiting for information. In our model, the delay is a **strategic choice** that makes the agent **busy**. This busyness is the mechanism that represents the **opportunity cost** of the agent's time.

Instead of just choosing an arm and a fidelity, the agent now chooses a tuple: **(arm $k$, fidelity $m$, commitment length $l$)**.

*   **Probes are short-commitment actions.** A cheap computer simulation ($m=0$) is an action with a short commitment ($l=1$). You pay a small cost and get information back quickly, ready to inform your next decision.
*   **Deployments are long-commitment actions.** Committing to the best arm is just another action in this unified space. It might correspond to the highest fidelity ($m=M$) and a very long commitment ($l=1000$). When you choose this, you are locked in. You pay the cost and must wait $l$ steps for the reward to arrive.

This single change resolves the issues with the previous frameworks:

1.  **It Solves the Cost-in-Regret Paradox:** An agent won't blindly choose a long-commitment "deployment" action just because the potential reward is high. It must now factor in the enormous **opportunity cost** of being locked in. For $l$ time steps, it cannot react to new information or explore other promising arms. Therefore, the agent will only commit to a long-commitment action when it is highly confident, naturally separating quick probes from high-commitment deployments without needing two different action types.

2.  **It Eliminates Artificial Phases:** There is no longer a hard switch from "exploration" to "exploitation." At every moment, the agent is simply managing a portfolio of possible actions with different time horizons, costs, and potential rewards. The entire process is a single, unified strategy of managing commitment over time.

### The Abstract Problem: A Unified Model

Let's formalize this elegant, unified framework. An agent interacts with an environment defined by three core components:

*   A set of **$K$ arms**, indexed by $k$.
*   A set of **$M$ fidelity levels**, indexed by $m$.
*   A set of **$L$ commitment lengths**, indexed by $l$.

At each decision point $t$, the agent is free to choose an action. If it is not already committed, it selects a single tuple: **$(k, m, l)$**. This choice has three immediate consequences:

1.  **It pays a cost.** A cost function $c(k, m, l)$ determines the price of the action.
2.  **It becomes committed.** The agent enters a "busy" state for $l$ time steps. It cannot take any new actions until time $t + l$.
3.  **It schedules a future outcome.** An observation $o$ is scheduled to arrive at time $t + l$. This observation is drawn from a distribution $T_{k,m}$ associated with the chosen arm and fidelity.

The crucial insight is that the final reward is the result of a **sequence of two transformations**: one for fidelity and one for commitment.

#### 1. The Fidelity Transformation ($f_m$)

The fidelity of an observation is determined by a transformation function $f_m$, which adds noise or bias to the arm's true, underlying reward distribution $D_k$:

$$T_{k,m} = f_m(D_k)$$

*   **Accuracy increases with $m$:** A higher fidelity $m$ yields a distribution $T_{k,m}$ that is "closer" to the true distribution $D_k$.
*   **Cost increases with $m$:** The cost of an action, $c(k, m, l)$, will almost always increase with $m$.

<!-- fidelity transform is independent from commitment! that seems right!?-->

<!-- what if we added a transform that severly undervalued / biased some arms. how does this change the problem? what a real world example of this? -->

#### 2. The Commitment Transformation ($g_l$)

Second, the base reward drawn from $T_{k,m}$ is then transformed by the chosen commitment length $l$. This function, $g_l$, models the **return on commitment**, where commitment acts as an investment. The final reward the agent receives is:

$$r_{\text{final}} = g_l(r_{\text{base}})$$

The form of $g_l$ defines the nature of the investment:

*   **Exponential Growth (Compounding):** A function like $g_l(r) = (1.05^l) \cdot r$ models scenarios where a longer commitment leads to compounding returns.
*   **Diminishing Returns (S-Curve):** A more realistic model might be a sigmoid function, where returns on commitment are initially slow, then accelerate rapidly, and finally plateau.
*   **No Return:** For a pure "probe" action, the function would be $g_l(r) = r$. The reward is not scaled, only delayed.

<!-- so commiting to a low fidelity action is like commiting to uncertainty. you've go no idea what you're going to get!? tho in expectation it will give the same return as the high fidelity action - if the fidelity transform is unbiased -->

#### The Importance of Cost Scaling

The nature of the cost function $c(k, m, l)$ is critical. Consider two scenarios for the fidelity component:

1.  **Logarithmic or Polynomial Cost:** If the price of higher fidelity grows slowly, an agent might be quick to abandon the cheapest probes. The trade-off is still present, but less stark.
2.  **Exponential Cost:** This often mirrors reality. The cost of an RCT in drug discovery can be orders of magnitude greater than a computer simulation. In this regime, the agent *must* be frugal. It cannot afford to run high-fidelity probes on unpromising arms. This steep cost curve makes the problem strategically deep.

#### What's the Goal? Redefining Regret

With actions resolving at different times, we must define success carefully. The goal is to maximize the stream of rewards over time, accounting for both costs and delays. The regret is the difference between the total reward an oracle could achieve and the agent's total net reward.

$$\text{Regret}(T) = (\text{Oracle's Total Reward at } T) - (\text{Agent's Total Net Reward at } T)$$

The agent's net reward is $(\sum \text{rewards\_received}) - (\sum \text{costs\_paid})$. The key challenge is that a reward from a long-commitment action taken at time $t$ won't arrive until $t+l$, while the cost is paid at $t$. The agent must be forward-looking, effectively maximizing the **Net Present Value** of its actions. It has to learn that a small reward today can be better than a slightly larger reward a year from now, especially when the opportunity cost of being busy is high.

Furthermore, we can add a "bankruptcy" constraint: the agent's cumulative net reward cannot fall below a certain threshold. This prevents the agent from taking on too much "debt" by running many expensive experiments before seeing any returns.

### A Concrete Example: The Gaussian Case

Let's make this more concrete. Assume the true reward for each arm $k$ comes from a Gaussian distribution with an unknown mean $\mu_k$ and a known variance $\sigma_k^2$. Our goal is to find and exploit the arm with the highest $\mu_k$.

The reward from probing arm $k$ at fidelity level $m$ is a sample from a noisier distribution: $T_{k,m} = \mathcal{N}(\mu_k, \sigma_k^2 + v_m)$, where the added noise $v_m$ decreases as fidelity $m$ increases.

By analyzing simplified versions of our framework, we can build intuition for the strategic trade-offs at play.

#### Scenario 1: Fidelity only

In this simplified world, there's only one arm to investigate and no commitment ($L=1$). The only decision is: **which fidelity level $m$ should we use to measure the arm?**

*   **The Setup:** There is a single process with a true, unknown mean reward $\mu$. To learn about $\mu$, we can pay a cost $c(m)$ to get a sample from a Gaussian distribution $\mathcal{N}(\mu, \sigma^2 + v_m)$, where $v_m$ is the noise added by fidelity level $m$.
*   **The Goal:** Find an estimate of $\mu$ that is within $\epsilon$ of the true value, as **cheaply as possible**. This is a pure "Best Arm Identification" problem for a single arm.

The total cost to reach precision $\epsilon$ using fidelity $m$ is $\text{TotalCost}(m) = n \cdot c(m)$, where $n = (\sigma^2 + v_m) / \epsilon^2$ is the number of samples required. The agent should choose the fidelity level $m$ that minimizes the product of its variance and its cost: **$(\sigma^2 + v_m) \cdot c(m)$**.

**Insight:** This simple case reveals a crucial trade-off. The optimal choice is neither the cheapest probe (which might be too noisy) nor the most accurate (which might be too expensive). It's the one with the best "bang for your buck" in terms of the cost to reduce variance. This is a core problem in multi-fidelity optimization. [^4]

#### Scenario 2: Arms only. No Fidelity, No Delays ($M=1, L=1$).

This setup strips our problem down to the classic Multi-Armed Bandit with a simple twist: **pulling each arm has a cost.**

*   **The Setup:** We have $K$ arms. Arm $k$ provides a reward from $\mathcal{N}(\mu_k, \sigma_k^2)$ and costs $c_k$ to pull.
*   **The Goal:** Maximize cumulative **net reward** ($r_t - c_k$).

This is the classic MAB problem where the reward distribution for each arm is simply shifted by its cost. Standard algorithms like Upper Confidence Bound (UCB) can be applied directly by choosing the arm that maximizes $(\text{AvgNetReward}_k) + \sqrt{2 \log t / N_k}$.

**Insight:** This is the foundational explore-exploit problem. The model must be able to gracefully handle this simple case, which forms the baseline that our full framework builds upon.

#### Scenario 3: One Arm, with Fidelity and Delay ($K=1, L>1, M>1$)

Let's isolate the trade-off between information quality and commitment. Imagine there is only one project to pursue. The core question becomes: **"How should I investigate this single option?"**

*   **The Setup:** We have one arm with an unknown true mean reward $\mu$. We can choose an action $(m, l)$.
    *   A low-fidelity, short-commitment action is a **quick, cheap prototype**.
    *   A high-fidelity, long-commitment action is a **full product launch**.
*   **The Dilemma:** Should the agent immediately commit to the high-cost, high-reward "launch"? Or should it start with the cheap prototype?

**Insight: The Value of Information for a Go/No-Go Decision**
While a formal proof is a topic for future research, we can reason about the strategic incentives. The agent's optimal strategy is not to pick one fixed action, but to follow a **curriculum of escalating commitment**.

The key is understanding the **value of information**. With only one arm, the information isn't for choosing between arms, but for choosing between future high-stakes actions: **launch or abandon**. A cheap probe provides a noisy signal about the project's true potential (`μ`).
1.  If the probe suggests `μ` is low, the agent can abandon the project, saving it from a catastrophic loss on a full launch.
2.  If the probe suggests `μ` is high, the agent's confidence grows. It has now "earned the right" to make a bigger investment. It becomes rational to select an action with higher fidelity and longer commitment to capitalize on the potential.

The framework naturally models strategic patience. The agent avoids a risky, long-term commitment by first using cheap probes to de-risk the final, high-stakes decision.

<!-- well, this is conjecture, not proof. need to weaken the language -->

#### Scenario 4: Multiple Arms, with Delay, No Fidelity ($K>1, L>1, M=1$)

Now, let's remove fidelity and focus on the interaction between multiple arms and commitment.

*   **The Setup:** We have $K$ arms, each with a different unknown mean reward $\mu_k$. For any arm, we can choose a commitment length $l$.
*   **The Dilemma:** "Should I spend my time trying out all the arms with short-term projects? Or should I pick the one that seems best and commit to it for a long time?"

**Insight: Commitment Raises the Stakes of Exploration**
This is not just a standard MAB. The strategic choice of delay `l` fundamentally changes the nature of exploration. In a classic MAB, the cost of one bad exploratory pull is small—one time step of suboptimal reward. In this model, the cost of committing to a bad arm for `l=100` steps is enormous: it's the **opportunity cost** of being unable to explore *any other arm* for that entire duration.

A rational agent must therefore be far more certain before making a long-term commitment. An exploration algorithm like UCB would need to be adapted. The exploration bonus would need to be scaled by the commitment length `l`, creating a "commitment-averse" strategy that favors short-term probes until confidence in the best arm is overwhelmingly high.

<!-- not sure this statement is correct?!
wouldn't it depend on the interest that can be earned by commiting?
 -->

#### Scenario 5: Recovering Best Arm Identification with Two Delays

The power of a general model is its ability to recover specific problems as special cases. The rigid, two-phase structure of Best Arm Identification (BAI) emerges naturally if we simply restrict the available actions.

*   **The Setup:** Imagine an environment with multiple arms and fidelities, but only **two possible commitment lengths**:
    1.  A "Probe" action: `l=1`. Its reward is defined to be zero, only its cost is paid.
    2.  A "Deploy" action: `l=∞`. This action is irreversible, ends the game, and provides a massive prize.
*   **The Goal:** Maximize total reward, which is equivalent to identifying and deploying the best arm.

**Insight: BAI as an Emergent Property**
Faced with these limited choices, a rational agent is forced into a classic two-phase strategy:
1.  **Phase 1: Pure Exploration.** The agent exclusively chooses "Probe" actions (`l=1`). It would be irrational to deploy without high confidence. It uses this phase to gather information as cheaply as possible, using the logic from Scenario 1 to find the most cost-effective fidelity. [^4]
2.  **Phase 2: Pure Exploitation.** Once confident that arm $k^*$ is the best, the agent plays the one "Deploy" action available: $(k^*, m_{best}, l=∞)$.

This demonstrates that the rigid "explore-then-exploit" model of BAI isn't a fundamental law, but an emergent behavior of a highly restricted action space. Our sequential commitment framework is more general, bridging the gap between pure exploration and pure exploitation.

### The Path Forward

By incorporating fidelity, cost, and a strategic notion of commitment-as-delay, the Progressive-Fidelity Bandit becomes a richer, more realistic model of decision-making.

This single model allows us to:

*   **Solve the Cost-in-Regret Paradox:** The opportunity cost of long commitments naturally incentivizes graduating from cheap probes to high-reward deployments.
*   **Dissolve Artificial Phases:** The hard switch between exploration and exploitation vanishes, replaced by a smooth continuum of commitment.
*   **Capture Classic Models:** The rigid structure of BAI is recovered as a special, restricted case of this more general framework.

The agent's task is no longer a simple choice of which arm to pull, but a sophisticated decision about how much confidence to buy and how much time to invest. The challenge, then, is to design algorithms that can navigate this complex, three-dimensional action space, explicitly exploiting its structure. This opens the door to creating agents that are not just optimizers, but true strategists, capable of understanding that the most valuable resource they manage is not just their budget, but their time.

---
### References

[^1]: Kandasamy, K., Dasarathy, G., Oliva, J. B., & Schneider, J. (2016). The Multi-fidelity Multi-armed Bandit. In *Advances in Neural Information Processing Systems 29*.
[^2]: El Mahdaouy, A., El Frayty, O., & El Aroussi, M. (2024). Multi-armed Bandits with Costly Probes. *IEEE Transactions on Information Theory*.
[^3]: Pike-Burke, C., & Grunewalder, S. (2019). Best arm identification in multi-armed bandits with delayed feedback. In *The 22nd International Conference on Artificial Intelligence and Statistics*.
[^4]: Poiani, M., Gagliolo, M., & Bisi, L. (2024). Optimal Multi-Fidelity Best-Arm Identification. *arXiv preprint arXiv:2406.03033*.