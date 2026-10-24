---
layout: post
title: What money remembers
subtitle: Notes towards explaining how money and reputation are connected
tags:
  - essay
  - open-question
  - trust
  - incentives
  - coordination
  - economics
  - society
---

<!-- TODO: a line on the conversations with Marcus Frean that started this — what he said that stuck? -->

#### The problem underneath

Start with a question that I think is more basic than "markets or the state?":

> How do you get people to do useful things for other people — mostly strangers, people they'll never meet?

Someone has to grow the wheat, fix the pipes, and stay up nights doing the boring part of the vaccine trial. Some people will do some of this out of love, duty or curiosity. But those motives seem to work best among people who know each other, and they don't obviously stretch to a billion strangers.

As far as I can tell, this is the problem capitalism solves, or at least claims to. In [an earlier post]({{ site.baseurl }}/capitalism-core/) I tried to boil capitalism down to four beliefs: private property, the "coin-operated" individual, competition, and prices. The second belief is the one doing the work here. Money is a motive that nearly everyone responds to, so you can build a predictable system on it.

What bothers me is that I haven't seen a good alternative answer. Plenty of critiques from the left point at real failures: inequality, externalities, the way money turns into political power. I agree with most of them. But it's rarely clear to me what would replace money as the *incentive*. "People will contribute because it's right" might be true. I'd like to see it work at the scale of a city before I believe it. Maybe I've just been reading the wrong people. <!-- TODO: anything you HAVE read that tries? Kibbutzim, open source, Ostrom's commons, gift economies — these work at some scale, which is interesting in itself -->

So before asking whether money is good, I want to understand what money *is*. My best guess is that it's a reputation system that has been compressed until it fits in your pocket.

#### A village with chickens and wheat

Imagine a small village. I keep chickens; you grow wheat. I want bread now, but your harvest is months away and my hens lay every day. You want eggs now, and I want wheat later. Swapping is easy when both sides have what the other wants at the same moment. Usually they don't.

So one of us has to go first. I give you eggs today on the understanding that you'll give me wheat in the autumn. Now I'm trusting you. Nothing in the swap itself makes you pay me back.

In a village, something outside the swap does: everyone remembers. If you take my eggs and never deliver the wheat, I'll tell people, and next spring nobody will give you anything on credit. Your *reputation*, the village's shared memory of how you've behaved, is the thing you'd lose. Because losing it costs more than one season's eggs, you deliver the wheat.

As I understand it, this is closer to how early economies actually worked than the textbook story of barter. Anthropologists seem to find very little evidence of societies that ran on barter. What they find is credit, gifts and obligations, all tracked by memory and gossip.[^graeber]

#### Scaling up: gossip doesn't travel

The village ledger works because the village is small. Everyone knows everyone, or knows someone who does. Once there are too many people for that, it breaks:

- I can't check the reputation of a stranger from the next valley.
- A cheat can move on to a place where nobody knows them.
- Remembering who owes what to whom, across thousands of people, is more than gossip can carry.

Here is the move I find beautiful. Suppose that, instead of the village remembering that I gave you eggs, I'm handed a *token* when I give them. The token says, in effect, "this person has done something useful for someone". I can spend it with anyone, including strangers, and they accept it because they know someone else will accept it from them in turn.

The economist Narayana Kocherlakota made this precise in a paper titled, simply, *Money is memory*.[^kocherlakota] Roughly: anything money can achieve could also be achieved by a complete public record of everyone's past behaviour. Money is a cheap substitute for that record. You don't need to know my history. You only need to see my tokens.

Seen this way, money is a portable, anonymous summary of reputation.

<!-- TODO: Marcus's angle on the origins of money goes here. Your own citation of Frean & Marsland (2022), "Holds enable one-shot reciprocal exchange", argues that being able to *hold* something during an exchange is what makes one-shot trades between strangers possible — which looks like the same move: replace a history of interactions with something physical, checkable in the moment. Link the paper(s) of his you mean. -->

<!-- #### Running it backwards

I first ran into this connection from the other side. In [The Offline Economy]({{ site.baseurl }}/reputation-for-rohingya/) I looked at refugee camps that have no internet. There, digital money stops working. Without a connection you can't stop someone spending the same digital dollar twice, so a token on its own isn't enough. The fallback I ended up at was reputation: you can't *prevent* a double-spend, but you can make it cost the cheat something they value more. That became [Rain]({{ site.baseurl }}/rain/), a protocol for staking reputation on your promises.

So the history may run in a loop. Village reputation became money once societies got too big for gossip. When the infrastructure that money relies on fails, you fall back to reputation. That makes me suspect they are two ends of one spectrum: how much memory you keep versus how cheaply you can carry it. -->

#### What gets lost in the compression

If money is compressed reputation, it should be worth asking what the compression throws away. Here are a few things I can see:

| | reputation | money |
|---|---|---|
| Who can hold it | only you (it's about *you*) | anyone it's handed to |
| What it records | many things: honest, skilled, reliable, kind | one number |
| Context | "good plumber, terrible with deadlines" | none |
| Over time | fades if you stop being good | keeps, or *grows* |
| Where it came from | visible: people remember | invisible: money doesn't remember where it's been |

Almost every row looks to me like the source of a familiar complaint about money.

#### The lovely idea, and where it breaks

Somewhere I read the strong version of this idea, and I can't now find where. It goes like this: money is a ledger of how much good you've done. People give you money when you help them, so whoever has more money has helped more people. On this view wealth *is* moral standing, measured.

I find this genuinely beautiful, and I think it holds a grain of truth. A baker with a full till has, in a literal sense, fed many people. But reading down the table above, the idea fails in at least four places.

**Money that grows on its own.** Reputation fades if you stop being good. Money doesn't; with interest and capital gains it compounds. Someone can be rich today because of help their grandparents gave, or because their money was lent to someone else who did the helping. The ledger keeps counting long after the good deeds stopped. (Whether the *lending* counts as a good deed is a fair question. Sometimes it does.)

**Money can be handed on.** Reputation can't be transferred, which is the point of the "soulbound" tokens in Rain. Money can be, so you can inherit a ledger you didn't fill in.

**"Helping" means "giving people what they'll pay for".** Money records that someone was willing to pay you. It doesn't record whether what you gave them was good for them. If many people want something perverse, harmful or addictive, you can grow very rich, and on this view very "reputable", by supplying it. Village gossip would at least have an opinion about the person selling poison. A coin doesn't.

**Some people's thanks count for more.** A rich person's willingness to pay counts for more than a poor person's need. So the ledger is weighted: helping one billionaire can earn you more than helping a thousand people with nothing. That's "one dollar, one vote", not "one person, one vote".

To these I'd add the harms the ledger never sees at all. When a deal hurts someone outside it, nobody pays and nothing is written down.

So my current guess is that money is a reputation, just a narrower one than the lovely idea claims. It records *how much people with money valued what you gave them*, and it keeps that record forever, and anyone can carry it. That's a real measure of something. It isn't a measure of goodness.

#### Where this leaves me

If this is right, the left argument and the capitalist argument might partly be talking past each other. One side says money is the only incentive that scales. The other says money measures the wrong thing. Both could be true. In that case the interesting question isn't "money or no money" but:

- Can we keep the scaling and put back some of what the compression threw away? Reputations that fade, that can't be passed on, that carry more than one dimension.
- Or fix the ledger at the edges, with taxes on inheritance and on harms to third parties, which are the corrections we already make?
- Or is the compression the *point*? Maybe a lot of money's usefulness comes from forgetting: that a stranger can trade with you without knowing or judging your history.

I don't know. I suspect the last one matters more than I'd like.

<!--
OTHER ANGLES — possible follow-up posts, each could stand alone:

1. "What would replace the incentive?" A fair survey of non-money answers to "how do we get people to do useful things": gift economies, open source, kibbutzim, Ostrom's commons, status/honour cultures, planned economies (link the socialist-calculation draft — Kantorovich/Lange is the *allocation* half; this would be the *motivation* half). At what scale does each break?

2. "Money is memory" — a more technical post. Kocherlakota's result properly, the Frean & Marsland holds paper, the CAP theorem as the reason memory can't be perfect, and Rain as a point between "full memory" and "a token". Could be a tutorial.

3. "Wealth as moral status" — the ethics post. Take the lovely idea seriously as a steelman (like capitalism-core does) then go through interest, inheritance, perverse demand, weighted votes, externalities. Pairs with Karma and merit + The Unfair Lottery.

4. "Reputations that fade" — a proposal post. What would a decaying, non-transferable, multi-dimensional currency look like (demurrage / Gesell's Freigeld, local currencies, Rain's SBTs)? What breaks?
-->

---

[^graeber]: Graeber, D. (2011). *Debt: The First 5,000 Years*. Melville House. Chapter 2, "The Myth of Barter", is the relevant part. <!-- TODO: check whether you'd rather cite Humphrey (1985) "Barter and economic disintegration" directly -->
[^kocherlakota]: Kocherlakota, N. R. (1998). Money is memory. *Journal of Economic Theory*, 81(2), 232–251.
