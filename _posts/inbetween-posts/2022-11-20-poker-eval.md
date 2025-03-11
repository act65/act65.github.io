---
layout: post
title: Why does poker have many rounds?
permalink: poker-eval
categories: 
  - "philosophy"
---

Imagine that the [World series of Poker](https://www.wsop.com/) (with potential winnings of ~\\$8 million) only had 1 round.
Here we are playing Texas Hold'em, with 8 players.

You have paid the \\$1,000,000 entry. You've scraped and saved for this moment. You are confident in your ability to read the other players, to bluff, to know when to fold, when to raise.

Here comes your hand; you are dealt 2 clubs and 7 spades (the worst hand possible).

![]({{ site.baseurl }}/assets/poker-eval/2_of_clubs.png){:width="100px"}
![]({{ site.baseurl }}/assets/poker-eval/7_of_spades.png){:width="100px"}

And the flop is 3 clubs, J hearts, 10 clubs. The turn and river are; J spades, 9 hearts.

![]({{ site.baseurl }}/assets/poker-eval/3_of_clubs.png){:width="100px"}
![]({{ site.baseurl }}/assets/poker-eval/jack_of_hearts.png){:width="100px"}
![]({{ site.baseurl }}/assets/poker-eval/10_of_clubs.png){:width="100px"}
![]({{ site.baseurl }}/assets/poker-eval/jack_of_spades.png){:width="100px"}
![]({{ site.baseurl }}/assets/poker-eval/9_of_hearts.png){:width="100px"}

SHIT.

You lose the hand and are out of the tournament (remember, it's only 1 round).

The winner, who had the Queen of clubs and the 10 of hearts, takes home \\$8 million.

__The end.__

***

Many would consider this, 1-round poker, to be an unfair game. It is based, __too much__, on chance.
Whom ever was dealt a good has a BIG advantage.

Instead, poker is played over many rounds. _But how many rounds should be played?_

The answer to this question depends on the chance we are willing to take that the best player does not win.
<!-- Are tournaments the best way to eval? -->

How should the game of poker balance luck and skill? Let's explore this using Kuhn Poker: a stripped-down version where we can mathematically model luck vs. skill.

Kuhn poker (3-card poker) is the simplest nontrivial poker game:

- Cards: J, Q, K (ranked low to high)
- Players: 2
- Steps: 1 betting step

Game Flow:

- Each antes 1 unit
- Each gets 1 card (3rd card unused)
- Player 1 acts first: check or bet 1
    - If checked, Player 2 can check (showdown) or bet 1
    - If bet, Player 2 can fold (P1 wins) or call (showdown)

We can model the game as a decision tree. See below.

![]({{ site.baseurl }}/assets/poker-eval/Kuhn_poker_tree.svg){:width="200%"}
By Petr Kadlec - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=48757606

And we can model each players's strategy as a probability distribution (aka policy) over the possible actions.

<div class="code" markdown="1">

Note. We model a player's strategy as a fixed, mixed policy. 

- Fixed: a player's strategy is fixed before the game starts and does not change during the game, nor between rounds.
- Mixed: a player's strategy is a probability distribution over the possible actions.

This is a simplification. In reality, a player's strategy is dynamic and can adapt to the opponent's strategy.

</div>

A player’s strategy is defined by probabilities for each decision node. For example:

```python
# Returns [prob_check, prob_bet]
def player_a_strategy(card): 
    # rational strategy
    if card == 0:  # J
        return [0.85, 0.15]  # probably check
    elif card == 1:  # Q
        return [0.5, 0.5] 
    else:  # K
        return [0.1, 0.9] # probably bet

def player_b_strategy(card): 
    # Random strategy
    return [0.5, 0.5]  # Mix
```

<!-- Let's quantify how many rounds it takes for Player A’s superior strategy to dominate. -->
Our goal in the following calculations is to calculate the expected win rate for each player's policy.
How likely is player A to win a round?

To calculate this, we;

- enumerate all 6 possible card matchups (JvQ, JvK, QvJ, QvK, KvJ, KvQ)
- enumerate all action sequences (check-check, bet-fold, etc.).
- Compute probabilities using each player’s policy.
- accumulate expected values (EV) for each action sequence / card matchup.

```python
def calculate_ev(player1_strat, player2_strat):
    cards = [0, 1, 2]  # J, Q, K
    total_ev = 0
    n_combos = 0
    
    for p1_card, p2_card in permutations(cards, 2):
        prob_deal = 1 / 6  # 6 possible card matchups
        
        # Get strategies for this hand
        p1_act = player1_strat(p1_card)
        p2_act = player2_strat(p2_card)
        
        # --- Action Sequence 1: P1 checks -> P2 checks ---
        prob = p1_act[0] * p2_act[0]  # Both check
        if p1_card > p2_card:
            payoff = 1  # P1 wins ante
        else:
            payoff = -1
        total_ev += prob_deal * prob * payoff
        
        # --- Action Sequence 2: P1 checks -> P2 bets -> P1 calls ---
        prob = p1_act[0] * p2_act[1] * 1.0
        if p1_card > p2_card:
            payoff = 2  # Pot size 4, net +2
        else:
            payoff = -2
        total_ev += prob_deal * prob * payoff
        
        # --- Action Sequence 3: P1 bets -> P2 calls ---
        prob = p1_act[1] * 1.0
        if p1_card > p2_card:
            payoff = 2
        else:
            payoff = -2
        total_ev += prob_deal * prob * payoff
        
    return total_ev
```

With the policies above (rational and random), we can calulate that Player A is 53.1% likely to win a round.

Next, by treating each round as a biased coin flip (53.1% - heads vs. 46.9 - tails), we cam calculate the number of rounds needed to be 99% sure Player A wins.

<div class="code" markdown="1">

A quick reminder, the probability of getting k heads in n coin flips is given by the binomial distribution:

$$
p(k, n) = {n \choose k} p^k (1-p)^{n-k} \\
{n \choose k} = \frac{n!}{k!(n-k)!}
$$

where ${n \choose k}$ returns the binomial coefficient, $p$ is the probability of heads, and $1-p$ is the probability of tails, $n$ is the number of coin flips, and $k$ is the number of heads.

</div>

![]({{ site.baseurl }}/assets/poker-eval/poker-n-rounds.png){:width="100%"}

While we know that Player A has a better strategy, it takes many rounds for this to be reflected in the results.
With these player strategies, we need 1447 rounds to reach 99% confidence that Player A will win. Or in other words, the probability of player A being 'unlucky' and player B being 'lucky' is \<1%. 


***

Philosophical aside: This idea of fairness in poker raises a bigger question

> How should we deal with the inherent randomness of life?

Life is like poker with only 1 round. You get dealt a hand; 
- your genes, 
- your parents, 
- your socio-economic status, 
- a crazy investor,
- cancer.
<!-- a picture of this would be nice! what pic tho?-->

If it's a bad hand, tough luck. You lose. 

__The end.__

<!-- There are two attitudes we can take to this situation.

1. Acceptance: that's the hand you are dealt. Do your best.
2. Mitigation: attempt to minimise the effects of luck / randomness.

The acceptance mindset dominates self-help rhetoric. It glorifies individual agency while downplaying systemic luck. Quotes like;
- "You make your own luck."
- "Life is unfair. But if you work hard, you can overcome it."
- “Hard work beats talent”
imply that outcomes are meritocratic, ignoring how a single bad “flop” (e.g., poverty, illness) can derail even the most skilled players.

The mitigation mindset is less popular but more realistic.
This approach asks: How can we reduce the stakes of bad luck? It acknowledges that no amount of skill can overcome certain starting conditions.
Examples include social safety nets, universal healthcare, or inheritance taxes. These systems act like “insurance” against life’s worst hands, redistributing luck to give skill a fighting chance. -->

***


<!-- veil -->
Earlier, we asked: How many rounds should poker have to balance luck and skill? But the deeper question is: Who gets to decide?

Enter philosopher John Rawls’ veil of ignorance. Imagine designing the rules of poker—or society—without knowing what hand you’ll be dealt. Will you be the pro with a stacked deck or the novice with 2-7 off-suit? Will you inherit wealth or face systemic bias?

Under this veil, rational players wouldn’t tolerate 1-round poker. Why? Because a single bad deal could ruin them. Instead, they’d demand:

- Multiple rounds (skill over time)
- Ante redistribution (shared stakes)
- Insurance (protection from ruin)

Sound familiar? These are the same principles behind progressive taxation, public education, and healthcare. The veil forces us to design systems that we’d accept if we might be the unluckiest player.


***

<!-- 1 round poker -->
Unlike poker, life cannot be played many times. So what would a 'fair' game of 1 round poker look like?

In standard poker, luck is hoarded: if you’re dealt a royal flush, you keep all its power. But imagine a variant where, after the river, players must discard one card into a shared "community deck." Over time, this deck grows, and anyone dealt a historically bad hand (like 2-7 off-suit) can draw from it.

The game stays competitive, but no one’s doomed by a single bad deal. Sound far-fetched? This is how societal redistribution works:

- Progressive taxation is the "discard" phase—those with good hands (wealth, health, privilege) contribute more to the communal stack.
- Social programs act as the redraws—unemployment benefits, public schools, food stamps let people refresh their hands.
- Anti-monopoly laws prevent any player from hoarding all the Kings.

This would make poker "less fun." But life isn’t a game; when luck is concentrated, the table empties. Redistribution ensures the game continues—not because everyone wins, but because everyone gets to keep playing.

***

History is littered with “bad hands” that were once death sentences but are now manageable:

- Polio: Before the 1950s vaccine, polio paralyzed or killed thousands annually. A diagnosis meant life in an iron lung or early death. Today, it’s nearly eradicated. (Vaccines act like a communal redraw—giving everyone a chance to discard the “polio card” from their hand.)
- Childbirth: In 1900, 6–9% of pregnancies ended in maternal death. Modern medicine dropped this to 0.02%—turning a common “bad hand” into a routine event.
- Bankruptcy: Before bankruptcy laws, debtors faced prison. Now, legal frameworks let individuals and businesses “fold” without lifelong ruin, preserving their ability to reenter the game.

These advances didn’t eliminate luck—they reduced its cruelty. 