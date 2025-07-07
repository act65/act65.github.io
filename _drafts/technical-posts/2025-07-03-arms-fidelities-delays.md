---
layout: post
title: The Price of Precision
subtitle: Introducing the Progressive-Fidelity Bandit Problem
---

In the classic Multi-Armed Bandit (MAB) problem, an agent chooses between several slot machines (or "arms") to maximize its reward. It's a powerful metaphor for decision-making under uncertainty. But what if pulling an arm isn't a single action, but a choice with its own set of costs and information quality? What if, before you pull the real arm, you could pay for a less accurate "test" pull?

This post introduces the **Progressive-Fidelity Bandit**, a variation of the MAB problem where we must balance not just exploration and exploitation, but also the cost and quality of information itself. This concept is often formalized in the literature as the Multi-Fidelity Multi-Armed Bandit (MF-MAB) problem. [^1]

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
| **Best Arm Identification (BAI)** | Identify the single best arm with high confidence, as **cheaply** as possible. | Natural for "find the winner" problems like drug discovery. The objective is clear and focused on exploration. | Ignores rewards gathered *during* the process. Can be inefficient if the best arm is only marginally better than a much cheaper-to-identify alternative. |
| **Cost-in-Regret** | Maximize the cumulative **net reward** (`reward - cost`) over a long time horizon. | Captures the ongoing trade-off between earning and learning at every step. | A naive implementation is paradoxical: it encourages the agent to always choose low-cost, low-reward actions, failing to ever exploit the true best arm. |
| **Budgeted Exploration** | Achieve the best possible outcome within a fixed total **cost budget**. | Highly practical and reflects real-world project constraints. | It's a constraint, not an objective. It creates an artificial "two-phase" system (explore, then exploit) which can be rigid. |

Each of these framings has merit, but they also expose a certain "clunkiness." The BAI and Budgeted models create a hard switch between an exploration phase and an exploitation phase. The Cost-in-Regret model, while trying to be unified, has a fundamental paradox. This suggests we are missing a key ingredient.

### The Elegance of Delays: A Unified Framework

The clunky feeling of the models above comes from trying to separate actions into two distinct types: "probing" (learning) and "pulling" (earning). A more elegant solution is to unify them by introducing a third dimension to the agent's decision: **delay**. This extension is related to the well-studied field of bandits with delayed feedback. [^3]

Instead of just choosing an arm and a fidelity, the agent now chooses a tuple: **(arm $k$, fidelity $m$, delay $d$)**.

*   **Probes are short-delay actions.** A cheap computer simulation ($m=0$) is an action with a short delay ($d=1$). You pay a small cost and get information back quickly, ready to inform your next decision.
*   **Deployments are long-delay actions.** Committing to the best arm is just another action in this unified space. It might correspond to the highest fidelity ($m=M$) and a very long delay ($d=1000$). When you choose this, you are locked in. You pay the cost and must wait $d$ steps for the reward to arrive.

This single change resolves the issues with the previous frameworks:

1.  **It Solves the Cost-in-Regret Paradox:** An agent won't blindly choose a long-delay "deployment" action just because the potential reward is high. It must now factor in the enormous **opportunity cost** of being locked in. For $d$ time steps, it cannot react to new information or explore other promising arms. Therefore, the agent will only commit to a long-delay action when it is highly confident, naturally separating quick probes from high-commitment deployments without needing two different action types.

2.  **It Eliminates Artificial Phases:** There is no longer a hard switch from "exploration" to "exploitation." At every moment, the agent is simply managing a portfolio of possible actions with different time horizons, costs, and potential rewards. The entire process is a single, unified strategy of managing commitment over time.

### The Abstract Problem: A Unified Model

Let's formalize this elegant, unified framework. An agent interacts with an environment defined by three core components:

*   A set of **$K$ arms**, indexed by $k$.
*   A set of **$M$ fidelity levels**, indexed by $m$.
*   A set of **$L$ commitment lengths**, indexed by $l$.

At each decision point $t$, the agent is free to choose an action. If it is not already committed, it selects a single tuple: **$(k, m, l)$**. This choice has three immediate consequences:

1.  **It pays a cost.** A cost function $c(k, m, l)$ determines the price of the action.
2.  **It becomes committed.** The agent enters a "busy" state for $l$ time steps. It cannot take any new actions until time $t + l$. This $l$ is the **commitment length**, and it is the mechanism that models the opportunity cost of the agent's time.
3.  **It schedules a future outcome.** An observation $o$ is scheduled to arrive at time $t + l$. This observation is drawn from the distribution $T_{k,m}$ associated with the chosen arm and fidelity.

This framework naturally handles both exploration and exploitation. A "probe" is simply an action with a small commitment length $l$, while a "deployment" is an action with a large $l$.

The crucial insight is that this final reward is the result of a **sequence of two transformations**: one for fidelity and one for commitment.

#### 1. The Fidelity Transformation ($f_m$)

The fidelity of an observation is determined by a transformation function $f_m$, which adds noise or bias to the arm's true, underlying reward distribution $D_k$:

$$T_{k,m} = f_m(D_k)$$

*   **Accuracy increases with $m$:** A higher fidelity $m$ yields a distribution $T_{k,m}$ that is "closer" to the true distribution $D_k$.
*   **Cost increases with $m$:** The cost of an action, $c(k, m, l)$, will almost always increase with $m$.

#### 2. The Commitment Transformation ($g_l$)

Second, this base reward is then transformed by the chosen commitment length $l$. This function, $g_l$, models the **return on commitment** (or commitment as investment). The final reward the agent receives is:

$$r_{\text{final}} = g_l(r_{\text{base}})$$

The form of $g_l$ defines the nature of the investment:

*   **Exponential Growth (Compounding):** Your suggestion, $g_l(r) = (1.05^l) \cdot r$, is a perfect example. It models scenarios where a longer commitment leads to compounding returns, like market penetration or financial investment.
*   **Diminishing Returns (S-Curve):** A more realistic model might be a sigmoid function, where returns on commitment are initially slow, then accelerate rapidly, and finally plateau as the market becomes saturated.
*   **No Return:** For a pure "probe" action, the function would be $g_l(r) = r$. The reward is not scaled, only delayed.



<!-- #### Commitment Details

This is how we formalize the role of commitment length `l`:

*   **Opportunity Cost:** The primary "cost" of a long commitment is not the direct price paid, but the opportunity cost. By choosing a large `l`, the agent forgoes the ability to take many smaller `l` actions, preventing it from reacting to new information.
*   **Parallel Actions:** In this simple model, the *agent* is busy, so it can only take one action at a time (sequentially). A more advanced model could allow for parallel commitments, where each *arm* can be busy, allowing the agent to manage multiple commitments at once. For clarity, the sequential model is a powerful starting point.
*   **Cost Scaling with Commitment:** How does the cost `c(k, m, l)` depend on `l`? This is a modeling choice.
    *   **Simple Model:** The cost might be independent of `l`, i.e., `c(k, m, l) = c_fidelity(m)`. Here, commitment only represents opportunity cost.
    *   **Complex Model:** The cost could increase with `l`, i.e., `c(k, m, l) = c_fidelity(m) + c_commitment(l)`. This models scenarios where tying up resources over a longer period has an explicit financial cost. -->

#### The Importance of Cost Scaling

The nature of the cost function $c(k, m, l)$ is critical. Consider two scenarios for the fidelity component:

1.  **Logarithmic or Polynomial Cost:** If the price of higher fidelity grows slowly, an agent might be quick to abandon the cheapest probes. The trade-off is still present, but less stark.
2.  **Exponential Cost:** This often mirrors reality. The cost of an RCT in drug discovery can be orders of magnitude greater than a computer simulation. In this regime, the agent *must* be frugal. It cannot afford to run high-fidelity probes on unpromising arms. This steep cost curve makes the problem strategically deep.

#### What's the Goal? Redefining Regret

With actions resolving at different times, we must define success carefully. The goal is to maximize the stream of rewards over time, accounting for both costs and delays. The regret is the difference between the total reward an oracle could achieve and the agent's total net reward.

$$\text{Regret}(T) = (\text{Oracle's Total Reward at } T) - (\text{Agent's Total Net Reward at } T)$$

The agent's net reward is $(\sum \text{rewards\_received}) - (\sum \text{costs\_paid})$. The key challenge is that a reward from a long-commitment action taken at time $t$ won't arrive until $t+l$, while the cost is paid at $t$. The agent must be forward-looking, effectively maximizing the **Net Present Value** of its actions. It has to learn that a small reward today can be better than a slightly larger reward a year from now.

Furthermore, we can add a "bankruptcy" constraint: the agent's cumulative net reward cannot fall below a certain threshold. This prevents the agent from taking on too much "debt" by running many expensive experiments before seeing any returns.

### A Concrete Example: The Gaussian Case

Let's make this more concrete. Assume the true reward for each arm $k$ comes from a Gaussian distribution with an unknown mean $\mu_k$ and a known variance $\sigma_k^2$. Our goal is to find and exploit the arm with the highest $\mu_k$.

The reward from probing arm $k$ at fidelity level $m$ is a sample from a noisier distribution: $T_{k,m} = \mathcal{N}(\mu_k, \sigma_k^2 + v_m)$, where the added noise $v_m$ decreases as fidelity $m$ increases.

Here's a detailed breakdown of the two scenarios you asked about.

#### Scenario 1: One Arm, No Delays ($K=1, L=1$)

In this simplified world, there's only one arm to investigate, so the "which arm" question is gone. We also remove the complexity of delays ($L=1$), so there is no opportunity cost of time. The only decision left is: **which fidelity level $m$ should we use to measure the arm?**

Let's formalize this:

*   **The Arm:** There is a single process (a drug candidate, a website feature) with a true, unknown mean reward $\mu$.
*   **The Fidelity Levels:** To learn about $\mu$, we can pay a cost $c(m)$ to get a sample from a Gaussian distribution $\mathcal{N}(\mu, \sigma^2 + v_m)$.
    *   $v_m$ is the noise added by fidelity level $m$. A higher fidelity $m$ means a lower $v_m$.
    *   $c(m)$ is the cost of choosing fidelity $m$. A higher fidelity $m$ means a higher $c(m)$.
*   **The Goal:** We want to find an estimate of $\mu$ that is within $\epsilon$ of the true value, and we want to do it as **cheaply as possible**.

This is a pure "Best Arm Identification" problem, but since there's only one arm, it's really "Best Mean Identification".

The agent's strategy is to pick one fidelity level, $m$, and draw $n$ samples until its estimate is good enough. The Standard Error of the mean after $n$ samples from fidelity level $m$ is $SE = \sqrt{(\sigma^2 + v_m) / n}$.

To achieve our desired precision $\epsilon$, we set $SE = \epsilon$ and solve for $n$, the number of samples required:

$$ \epsilon = \sqrt{\frac{\sigma^2 + v_m}{n}} \implies \epsilon^2 = \frac{\sigma^2 + v_m}{n} \implies n = \frac{\sigma^2 + v_m}{\epsilon^2} $$

The total cost to reach this precision $\epsilon$ using fidelity $m$ is $\text{TotalCost}(m) = n \cdot c(m)$. Substituting our formula for $n$:

$$ \text{TotalCost}(m) = \left[ \frac{\sigma^2 + v_m}{\epsilon^2} \right] \cdot c(m) $$

Since our goal is to minimize this total cost, and $\epsilon^2$ is a constant goal, the agent should choose the fidelity level $m$ that minimizes the product of its variance and its cost: **$(\sigma^2 + v_m) \cdot c(m)$**.

**Insight:** This simple case reveals a crucial trade-off. The optimal choice is neither the cheapest probe (which might be so noisy that you need millions of samples) nor the most accurate probe (which might be prohibitively expensive). It's the one with the best "bang for your buck" in terms of the cost to reduce variance—the best cost-to-sample-complexity ratio. An agent in this setting must find the sweet spot between information quality and information cost.

#### Scenario 2: No Fidelity, No Delays ($M=1, L=1$)

Now, let's remove fidelity from the equation ($M=1$) but reintroduce multiple arms ($K > 1$). We are still in a world without delays ($L=1$).

This setup strips our problem down to its essentials, returning us to the classic Multi-Armed Bandit, but with a simple twist: **pulling each arm has a cost.**

*   **The Arms:** We have $K$ arms. Arm $k$ provides a reward from a Gaussian distribution $\mathcal{N}(\mu_k, \sigma_k^2)$.
*   **The Cost:** Pulling arm $k$ costs $c_k$.
*   **The Action:** At each step $t$, the agent chooses an arm $k$, pays the cost $c_k$, and receives a reward $r_t$. The agent's net reward for this step is $r_t - c_k$.

**The Goal:** The agent wants to maximize its cumulative **net reward** over many pulls. This is the classic MAB problem, where the reward distribution for each arm is simply shifted by its cost. Standard algorithms like Upper Confidence Bound (UCB) can be applied directly. The UCB1 algorithm, for instance, would choose the arm $k$ that maximizes:

$$ \text{UCB1-NetReward}_k = (\text{AvgNetReward}_k) + \sqrt{\frac{2 \log t}{N_k}} $$

where $\text{AvgNetReward}_k$ is the average net reward observed from arm $k$ so far, $N_k$ is the number of times arm $k$ has been pulled, and $t$ is the total number of pulls.

**Insight:** This is the foundational explore-exploit problem. The $\text{AvgNetReward}_k$ term encourages **exploitation** (picking the arm that has performed best so far), while the $\sqrt{\log(t) / N_k}$ term encourages **exploration** (giving a bonus to arms that haven't been tried recently). This simple model forms the baseline that the Progressive-Fidelity Bandit problem builds upon, showing how the core MAB framework is about learning and exploiting expected values, which in this case are explicitly defined as `reward - cost`.

<!-- 
TODO explore;
- delay+fidelity, one arm. (progressively choose larger commitments are we become more certain?)
- delay+arms, no fidelity. this is the delayed bandits setting. include refs.
 -->

### The Path Forward

By incorporating delays and variable fidelity, the Progressive-Fidelity Bandit problem becomes a much richer and more realistic model of decision-making. This problem can be viewed as a $K \times M \times L$ MAB problem, but this ignores the crucial structure: learning from $(k, m_1)$ also tells you something about $(k, m_2)$. Efficient algorithms must exploit this shared information.

The path forward involves designing algorithms that can navigate this complex, three-dimensional action space. This opens the door to adapting more advanced techniques from information theory and sequential planning, creating agents that understand that the most valuable resource they manage is not just their budget, but their time.

---
### References

[^1]: Kandasamy, K., Dasarathy, G., Oliva, J. B., & Schneider, J. (2016). The Multi-fidelity Multi-armed Bandit. In *Advances in Neural Information Processing Systems 29*.
[^2]: El Mahdaouy, A., El Frayty, O., & El Aroussi, M. (2024). Multi-armed Bandits with Costly Probes. *IEEE Transactions on Information Theory*.
[^3]: Pike-Burke, C., & Grunewalder, S. (2019). Best arm identification in multi-armed bandits with delayed feedback. In *The 22nd International Conference on Artificial Intelligence and Statistics*.
[^4]: Russo, D., & Van Roy, B. (2018). Learning to Optimize via Information-Directed Sampling. *Operations Research, 66*(6), 1575-1590.


<!-- 
seeing r_t = 0 is different to seeing r_t = (r_t - c_t)!? 
-->


<!-- 
what insights can we expect from this analysis?

in some cases it's optimal to follow a kind of curriculum? which cases!?
by curriculum i mean: start with low fidelity on many arms. only progress to higher fidelity after finished low fidelity? use the info from the earlier exploration to decide to skip higher fidelity tests for some arms.

in the earlier single gaussian arm setting, i think it's clear there will be one fidelity that is optimal. shouldn't bother with the rest.

???
-->