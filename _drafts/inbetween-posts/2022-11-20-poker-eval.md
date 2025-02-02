---
layout: post
title: Why does poker have many rounds?
permalink: poker-eval
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

Instead, poker is played over many rounds.

> But how many rounds should be played?

The answer to this question depends on the chance we are willing to take that the best player does not win.
<!-- Are tournaments the best way to eval? -->

Should poker be a game of luck or skill?
<!-- Is this fair? Or is this just gambling masquerading as skill? -->

***

To understand why multiple rounds matter, let’s simplify the game. 
Enter Kuhn Poker: a stripped-down version where we can mathematically model luck vs. skill.

Kuhn poker (3-card poker) is the simplest nontrivial poker game:

- Cards: J, Q, K (ranked low to high)
- Players: 2
- Rounds: 1 betting round, but multiple game rounds (hands) determine the winner

Game Flow:

- Each antes 1 unit
- Each gets 1 card (3rd card unused)
- Player 1 acts first: check or bet 1
    - If checked, Player 2 can check (showdown) or bet 1
    - If bet, Player 2 can fold (P1 wins) or call (showdown)

![]({{ site.baseurl }}/assets/poker-eval/Kuhn_poker_tree.svg){:width="200%"}
By Petr Kadlec - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=48757606


Strategy Representation


NOte. We model a player's strategy as a fixed, mixed policy. 

- Fixed: a player's strategy is fixed before the game starts and does not change during the game, nor between rounds.
- Mixed: a player's strategy is a probability distribution over the possible actions.

A player’s strategy is defined by probabilities for each decision node. For example:

- Player A (Rational):
    - Bets 100% with K (bluff-catcher), 50% with Q (balance), 0% with J
    - Calls 75% when facing a bet with Q/J
- Player B (random):
    - Bets / calls 50% of the time
    - Fold / check 50% of the time

We’ll quantify how many rounds it takes for Player A’s superior strategy to dominate.
Mathematical Framework
Expected Value Per Hand

For any card matchup (e.g., Player A has K, Player B has Q), we calculate:

- All possible action sequences (check-check, bet-call, etc.)
- Probability of each sequence (based on strategies)
- Payoff for each outcome

Example Calculation (A has K, B has Q):

- A’s strategy: 100% bet
- B’s strategy: 100% call
- Result: A wins 2 units (pot size 4, net +2)
- Probability: 1 (certainty)

![]({{ site.baseurl }}/assets/poker-eval/poker-n-rounds.png){:width="100%"}

In this case, with these players, we need 777 rounds to reach 99% confidence that Player A will win.
While we know that Player A has a better strategy, it takes many rounds for this to be reflected in the results.

***

Philosophical aside: This idea of fairness in poker raises a bigger question

> How should we deal with the inherent randomness of life?

Life is like poker with only 1 round. You get dealt a hand; your genes, your parents, your socio-economic status, a crazy investor, ... cancer.
<!-- a picture of this would be nice! what pic tho?-->
If it's a bad hand. You don't get to fold and try again. 
__The end.__

There are two attitudes we can take to this situation.

1. that's the hand you are dealt. If it's bad, tough luck. (in poker, accepts the initial deal and plays it out)
2. attempt to fix the game. Make it fairer. (in poker, represented by adding more rounds, seeks to mitigate the impact of a bad initial deal)

The first attitude is common to hear in pop culture. It minimises the role of luck in success and failure.
- "You make your own luck."
- "Life is unfair. But if you work hard, you can overcome it."

The second ...?

When thinking about 'fixing' the game (of life). A useful concept is 'the veil of ignorance'. It's a thought experiment where you design a society without knowing what your position in it will be.

Similar to how, in a poker game, we don't know what hand we will be dealt. We don't know if we will be born rich or poor, healthy or sick, smart or dumb.

<!-- want to reduce the variance? want to make the game invariant to initial conditions. then there is no luck?! -->
Unlike poker, life cannot be played many times. Another approach to fairness is to reduce the risk of bad hands.
Insurance is an example of the second attitude.

<!-- just as insurance redistributes risk in life, multiple poker rounds redistribute luck—giving skill room to breathe. -->

1-round Poker with insurance.
How would this work?
I am insured against bad hands. If I am dealt a bad hand, I get compensated.

This would make for a boring poker game.

In the past... 

- (before 1921 when insulin was discovered and later synthesised) diabetes was a losing hand. Your life was just a few months (max) after diagnosis.
- (before 1943 when penicillin was discovered) bacterial infections were a losing hand. Your life was just a few weeks (max) after diagnosis.
- 

No matter how good a player you were. You could not win with these hands.

Today, these hands are not so bad. You can win with them.

***
