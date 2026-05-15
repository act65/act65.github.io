---
title: Formalising Curiosity
subtitle: How We Teach RL Agents to Explore
layout: post
---

When we train reinforcement learning (RL) agents, we generally rely on a simple mechanism: give the agent a reward when it does the right thing. It’s classical operant conditioning. But this mechanism breaks down in environments where the reward is a needle in a haystack. 

If we want agents that can navigate complex, open-ended worlds, we can’t rely solely on external rewards. We need to endow them with intrinsic motivation. We need to formalise *curiosity*. 

In this post, I want to take a high-level look at the exploration problem in RL, how researchers have attempted to mathematically define curiosity, the current state of the art, and where the field is heading next. 

### What problem does curiosity solve? 
At its core, curiosity is the solution to the **exploration problem**, specifically in environments with **sparse rewards**.

Imagine dropping an agent into the classic Atari game *Montezuma's Revenge*. To get its first point, the agent must climb down ladders, jump over a skull, pick up a key, retrace its steps, and open a door. If the agent relies on standard random exploration (like $\epsilon$-greedy, where it just takes a random action 10% of the time), the probability of randomly executing this exact sequence of hundreds of actions is practically zero. 

Without a dense breadcrumb trail of rewards guiding it, the agent receives a constant reward of `0`. When the reward is always zero, the gradients are zero. The agent learns nothing. 

Curiosity solves this by providing an **intrinsic reward**. Instead of waiting for the environment to say "good job," the agent rewards itself for discovering new things. Curiosity transforms an uninformative, zero-reward landscape into a rich topography of interestingness, guiding the agent toward the extrinsic reward.

### Alternative Definitions and Algorithms

How do we actually express "interestingness" in math? Over the years, researchers have proposed several definitions of curiosity, each with its own trade-offs.

#### 1. Count-Based Exploration ("Have I been here before?")
The most intuitive definition of curiosity is simply seeking out states you haven't visited often. In classical tabular RL, we literally maintain a tally of how many times the agent has visited state $s$. The intrinsic reward is inversely proportional to the visit count (e.g., $1/\sqrt{n}$).
*   **Pros:** Highly rigorous. In simple environments, count-based exploration comes with strong theoretical guarantees (PAC-MDP) that the agent will explore efficiently. 
*   **Cons:** The real world (and modern RL) is high-dimensional. You will never see the exact same arrangement of pixels twice. While researchers have tried using pseudo-counts via density models, scaling this to complex environments remains computationally difficult. 

#### 2. Prediction Error / Intrinsic Curiosity Module ("Can I predict what happens next?")
Introduced by Pathak et al. (2017), the Intrinsic Curiosity Module (ICM) defines curiosity as **surprise**. The agent has a forward dynamics model that tries to predict the next state given the current state and action. The intrinsic reward is the *error* of that prediction. If the agent can't predict what happens next, it is curious to figure it out.
*   **Pros:** Scales beautifully to deep RL and high-dimensional pixel spaces. It forces the agent to learn how the world works.
*   **Cons:** **The Noisy TV Problem.** If you put a TV playing white noise in front of an ICM agent, it will stare at it forever. Because the white noise is fundamentally unpredictable (aleatoric uncertainty), the prediction error is always high. The agent gets infinitely "rewarded" for watching static, halting all useful exploration.

#### 3. Random Network Distillation ("Is this novel to my neural network?")
To solve the Noisy TV problem, OpenAI introduced RND. Instead of predicting the next state, RND uses two neural networks: a fixed, randomized "target" network, and a "predictor" network. Both networks take the current state as input. The agent's intrinsic reward is how poorly the predictor matches the target. Because the target network is fixed and deterministic, there is no stochastic "noise" to get trapped by.
*   **Pros:** Simple to implement, computationally cheap, and highly resistant to the Noisy TV problem. It was the first algorithm to achieve superhuman performance on *Montezuma’s Revenge*.
*   **Cons:** "Ephemeral novelty." Once the predictor learns the target network's outputs for a given room, the intrinsic reward vanishes permanently. RND struggles if an agent needs to remember that a state is "novel" across long time-horizons or multiple episodes.

### What is the current "best"?

**In Theory: Information Gain**
Theoretically, the gold standard for curiosity is maximizing **Information Gain** (or reducing *epistemic* uncertainty). The math dictates that an agent should only be rewarded for exploring states where it expects to reduce its uncertainty about the environment's underlying rules. This perfectly separates *epistemic uncertainty* (things I don't know but can learn) from *aleatoric uncertainty* (inherent randomness, like the Noisy TV), theoretically solving the exploration-exploitation dilemma. 

**In Practice: Agent57 and the NGU Framework**
In practice, calculating pure Information Gain in deep RL is intractable. The current empirical heavyweight is the architecture behind **Agent57** (the first agent to beat human baselines on all 57 Atari games), which relies on a framework called **Never Give Up (NGU)**. 

NGU realizes that a good curious agent needs two distinct memories:
1.  **Episodic Memory:** "Have I been here *in this current life/run*?" (Prevents the agent from walking in circles in a single episode).
2.  **Lifelong Memory:** "Have I been here across *all* my past training?" (Drives the agent to seek out entirely new rooms/levels).

By dynamically mixing rapid, short-term curiosity with slow-decaying, long-term curiosity—and training a meta-controller to choose *how* curious to be at any given moment—Agent57 achieves the best empirical performance in hard-exploration environments. 

*(Honorable mention to **Go-Explore**, which completely sidesteps the standard RL formulation by simply keeping an archive of all visited states and explicitly teleporting back to the frontier to explore further. It's incredibly powerful in practice, though more of an algorithmic paradigm shift than a pure "curiosity" reward.)*

### Future Work: Where do we go from here?

The formalisation of curiosity is still an active frontier. A few areas stand out as critical next steps:

*   **Safe Exploration:** How do we make an agent curious without being suicidal? If curiosity is just maximizing novelty, a robot exploring a kitchen might discover that setting the house on fire creates a highly novel, unpredictable state. Aligning intrinsic motivation with safety constraints is a major unsolved alignment problem.
*   **Unsupervised / Open-Ended RL:** We are moving toward agents that are dropped into environments with zero extrinsic rewards. The goal is for them to use curiosity to discover a diverse repertoire of "skills" on their own, which can later be fine-tuned for specific human tasks. 
*   **Commonsense Priors from LLMs:** Current curiosity algorithms treat all novelty as equal. But finding a new key is objectively more interesting than staring at a novel pattern of dirt on a wall. Researchers are beginning to use Vision-Language Models (VLMs) and LLMs to provide "commonsense" priors, ensuring agents are curious about semantically meaningful things rather than just pixel-level entropy.

Curiosity used to be a fuzzy psychological concept. Today, it is a mathematically rigorous tool that prevents our agents from flatlining in the face of sparse feedback. As we push toward more autonomous, general-purpose systems, defining exactly what our agents should find "interesting" will be just as important as defining what we want them to achieve.

***

**Notes for you before publishing:**
*   *Links:* You might want to hyperlink *Montezuma's Revenge*, *ICM (Pathak et al.)*, *RND (OpenAI)*, and *Agent57 (DeepMind)* depending on your preference for citations. 
*   *Alignment tie-in:* In the "Safe Exploration" bullet point, I subtly linked curiosity to your ongoing themes of alignment and mechanism design. Feel free to expand this if you want to tie it back to your DAOs/Corporate alignment posts!