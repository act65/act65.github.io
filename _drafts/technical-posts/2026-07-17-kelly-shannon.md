---
layout: post
title: The Interest Rate of Belief
subtitle: Kelly, Shannon, and why information is literally compound interest
categories:
  - play
---

In [The Price of Belief]({{ site.baseurl }}/uncertainty-via-bets) I argued that the axioms of probability fall out of one demand: set your betting odds so that no one can arrange a guaranteed profit against you. That fixes what you may *believe*. It says nothing about what you should *do* when your beliefs are actually better than the market's. You have an edge. How much do you bet?

The answer connects gambling to information theory by an exact equality, and it is one of my favourite facts in either subject.

### How much to bet

Start with the simplest case: an even-money bet you win with probability $p > 1/2$. You will play it over and over. Each round you wager a fraction $f$ of your current wealth. After $n$ rounds with $W$ wins and $n-W$ losses, your wealth is

$$W_0 \,(1+f)^{W} (1-f)^{n-W}.$$

The naive move is to maximise *expected* wealth. That tells you to bet everything, $f = 1$ — and then a single loss wipes you out. Over many rounds the expected-wealth maximiser goes broke almost surely, while a vanishing set of impossibly lucky paths carry all the expectation. The mean is a liar here.

What you actually want to maximise is the *growth rate per round* — the time-average, not the ensemble-average:

$$g(f) = p \log(1+f) + q\log(1-f), \qquad q = 1-p.$$

Differentiate, set to zero, and you get the Kelly fraction:

$$f^\star = p - q = 2p - 1.$$

Bet your edge. With general odds $b$-to-one it becomes $f^\star = p - q/b$ — edge divided by odds. Bet more when you're more sure and when the payout is fatter; bet nothing when your edge is zero; and never bet so much that a bad run can ruin you, because $\log(0) = -\infty$ and the log never forgives ruin.

> That last point is the whole reason the log appears. Maximising $\mathbb{E}[\log W]$ instead of $\mathbb{E}[W]$ is the same move as caring about the *time-average* growth of one gambler living through the sequence, rather than the average over a fictional ensemble of a million parallel gamblers. Life is lived along the time-axis, one path, and the two averages are not equal. This is the ergodicity point, and it is the same reason [one round of poker is not the same game as a thousand]({{ site.baseurl }}/poker-eval).

### The bridge to Shannon

Now the horse race, which is where Kelly ([1956](https://en.wikipedia.org/wiki/Kelly_criterion), a colleague of Shannon's at Bell Labs) made the connection explicit.

There are horses $i$ with true win probabilities $p_i$, and the track offers odds $o_i$. You split your whole wealth across horses in proportions $b_i$. The growth rate of your wealth is

$$g = \sum_i p_i \log(b_i\, o_i).$$

Maximising over the $b_i$ gives a clean answer: **bet your beliefs**, $b_i = p_i$. Proportional gambling is optimal. Pour your money onto each horse in proportion to how likely you think it is to win — no more, no less.

Here is the payoff. Suppose you also get to see a signal $Y$ before betting — a tipster, a track condition, a tell. You now bet your *conditional* beliefs $p_{i \mid Y}$. Kelly's result is that the increase in your growth rate from having seen $Y$ is exactly the **mutual information** between the outcome $X$ and the signal $Y$:

$$\Delta g = I(X; Y).$$

Not proportional to. *Equal to.* The extra doubling-rate of your money, measured in bits, is the number of bits the signal tells you about the world. A bit of information is worth one doubling of your capital. The mutual information between your signal and reality is the interest rate your beliefs pay out.

Information theory and investment theory are the same theorem wearing different costumes. Shannon's channel capacity — the maximum bits per symbol you can pull through a noisy channel — is the maximum growth rate of a gambler with that channel as a side-informant. The quantity Shannon invented to count bits is the quantity Kelly re-derived to count money.

### A number, to make it concrete

Two horses, you think it's a coin flip, $p = (0.5, 0.5)$, and the track offers fair even odds. With no information your optimal growth rate is zero — you can't beat a fair coin. Now a tipster tells you the winner correctly $80\%$ of the time. The mutual information between "tipster says A" and "A wins" is

$$I = 1 - H(0.8) = 1 - 0.72 = 0.28 \text{ bits}.$$

So betting your updated beliefs grows your wealth at $0.28$ bits per race — your money multiplies by $2^{0.28} \approx 1.21$ each race, on average, in the only average that matters. The tipster is worth exactly $0.28$ bits, and $0.28$ bits is worth exactly $21\%$ per race. The exchange rate is fixed by nature.

### The caveats, which are the interesting part

- **Kelly is savage.** Full Kelly maximises long-run growth but the ride is violent — routine drawdowns of 50% or more. Most practitioners bet *fractional* Kelly (a half, a quarter) and trade a little growth for a lot less nausea.
- **It assumes you know $p$.** You don't. Kelly with an over-estimated edge over-bets, and over-betting is punished asymmetrically — the downside of $f$ too big is much worse than $f$ too small. Uncertainty about your own probabilities should shrink your bets, which is a nice second-order echo of the whole [belief-as-betting]({{ site.baseurl }}/uncertainty-via-bets) picture.
- **It assumes the game repeats.** The optimality is a statement about the time-average over many rounds. For a genuinely one-shot bet — most of the big bets in a life — the ergodic argument doesn't apply and you should be more conservative than Kelly, for the same reason [luck dominates skill over a single hand]({{ site.baseurl }}/poker-eval).

The Price of Belief told you which odds you may quote without being robbed. This tells you how much to stake once your map of the world is genuinely sharper than the market's — and that the answer, denominated correctly, is measured in bits.
