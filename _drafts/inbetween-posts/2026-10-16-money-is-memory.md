---
layout: post
title: Money is memory
subtitle: A small model of why tokens can stand in for a ledger, and what they forget
tags:
  - essay
  - formalised
  - trust
  - coordination
  - economics
  - mechanism-design
---

In [What money remembers]({{ site.baseurl }}/money-and-reputation/) I argued, loosely, that money is reputation compressed until it fits in your pocket. This post tries to say that more carefully, with a toy model. Most of the ideas are borrowed. The central one is from Narayana Kocherlakota's 1998 paper *Money is memory*.[^kocherlakota]

#### A world with no double coincidence

Take $N$ people. Each period they are paired off at random. In each pair, one person (chosen at random) is able to make something the other wants. Making it costs the producer $c$, and it is worth $u$ to the receiver, with $u > c > 0$. Everyone discounts the future by a factor $\delta < 1$ per period.

Nobody ever has what their partner wants *and* wants what their partner has at the same time. So there's no barter. The only way anything happens is a gift: the producer pays $c$ now and gets nothing back in this meeting.

If the meeting is all there is, nobody gives anything. Paying $c$ for nothing is a bad deal. Everyone ends up with zero, even though each gift creates $u - c$ of value. The question is what could make gifts worth giving.

#### Option one: everyone remembers

Suppose there's a perfect public record of every meeting, and everyone follows a simple rule:

> Give to your partner, unless they have ever refused to give. Anyone who has refused gets nothing, ever again.

Is it worth following? Someone in good standing is a receiver half the time and a producer half the time, so each period is worth $(u - c)/2$ on average. Over a lifetime that is

$$V = \frac{u - c}{2(1 - \delta)}.$$

When it's your turn to produce, giving costs $c$ now and keeps $V$ from next period on. Refusing saves $c$ and costs you everything afterwards. So you give whenever

$$\delta V \ge c \quad\Longleftrightarrow\quad \delta\,(u - c) \ge 2c\,(1 - \delta).$$

This holds if people are patient enough, or if the gift is worth enough compared with what it costs. The important thing is that **$N$ doesn't appear.** With perfect memory, a population of a billion can cooperate as easily as a village of fifty.

The catch is the record. It holds every meeting of every person, forever. If you write down who you met and whether you gave, that is about $\log_2 N + 1$ bits per person per period, and it keeps growing.

#### Option two: nobody remembers, but rumour spreads

Now take the record away. You don't know your partner's history. You only know how *you* have been treated.

Michihiro Kandori showed that cooperation can still survive here, through a kind of contagion.[^kandori] Everyone gives until someone refuses them. After that, they stop giving to anyone. One refusal sets off a cascade that eventually reaches the person who started it.

The trouble is the word "eventually". In a population of $N$, the cascade takes longer to come back round to the cheat as $N$ grows. For any fixed level of patience, there's a population size beyond which the punishment arrives too late to matter. This is, I think, the precise version of "gossip doesn't travel": community enforcement works, and it stops working as the community gets larger.

#### Option three: tokens

Give everyone a token at the start, and change the rule:

> Give to your partner if, and only if, they hand you a token.

Now look at what a person's token count measures. Every time you give, you gain a token. Every time you receive, you lose one. So, at any time,

$$m_i(t) = m_i(0) + (\text{gifts } i \text{ has given}) - (\text{gifts } i \text{ has received}).$$

That's a summary of your history. It doesn't say who you gave to, or when, or whether you were pleasant about it. It records one number: how far ahead you are on giving versus taking. And it's all the producer needs to know. If you have a token, you've given at least as much as you've taken (plus your starting gift), so it's safe to give to you.

Three things have changed compared with the village:

- **Nobody stores anything.** The record is carried by the people it describes, in their pockets. Instead of a history that keeps growing, each person holds about $\log_2(\text{balance})$ bits.
- **Nobody needs punishing.** A cheat in the village had to be found and shut out. Here there's nothing to cheat: if you won't pay, you don't get served. The token turns a trust problem into a swap made on the spot.
- **Strangers are fine.** The producer doesn't need to know who you are. Anonymity is no longer a weakness.

<!-- TODO: the Frean & Marsland "holds" result belongs here. As I understand your gloss in The Offline Economy: being able to hold something of the other party's during an exchange is what makes one-shot reciprocal exchange possible. That looks like the same move as the token — the record of the past is replaced by something checkable in the moment. Worth stating their result in your own words and saying whether it's the same move or a different one. -->

Kocherlakota's result, roughly, is that the arrows only go one way. Any outcome money can achieve can also be achieved with memory, because a perfect record can always compute the token balance from history. But memory can achieve outcomes money can't. For example, it can treat two people with the same balance differently because of *how* they got it. Money is a particular, lossy function of memory.

So if memory is strictly more powerful, why do we use money? The model's answer, I think, is cost. Memory is expensive to keep, to share and to keep consistent. Tokens are cheap.

#### The catch: tokens have to be uncopyable

All of this assumes tokens can't be copied or forged. If they can, $m_i(t)$ stops meaning anything, because you could hand out a token you never earned.

Physical money gets this from physics, more or less: coins are hard to forge, and you can't give the same coin to two people. Digital money doesn't get it for free. A digital token is just bits, and bits copy. The usual fix is a ledger: a record, kept somewhere, of who holds which token. Bank accounts are this. So are blockchains, which keep a fully public record of every transaction ever made in order to simulate a token that can't be spent twice.

That seems to me a nice irony. To make digital cash work, we rebuilt the village's memory, at enormous cost, so that people could carry on not remembering each other.

#### When the ledger can't be kept

And sometimes the ledger can't be kept. In [The Offline Economy]({{ site.baseurl }}/reputation-for-rohingya/) I looked at places without internet. There, the CAP theorem says that a system which keeps working while disconnected can't also guarantee that everyone's view of the ledger agrees. A token can be spent twice before anyone finds out.

Then you're back to option one, with a lag. You can't stop the double-spend, but once it's discovered you can make it cost more than it gained. If cheating gains $g$ and the cheat loses a stake worth $s$, you need $s \ge g$. This is the village condition $\delta V \ge c$ again, with a reputation stake in place of the value of good standing. [Rain]({{ site.baseurl }}/rain/) is an attempt to build exactly that.

#### A spectrum

Put together, the options form a spectrum between remembering everything and remembering one number.

| | what's recorded | who holds it | anonymous? | needs punishment? |
|---|---|---|---|---|
| Village gossip | everything, roughly | everyone, roughly | no | yes |
| Credit bureau | repayment history | a firm | no | yes (exclusion) |
| Rain-style reputation | promises kept and broken | a shared ledger | pseudonymous | yes (slashing) |
| Bank account | balance and transactions | the bank | no | rarely |
| Blockchain | every transaction | everyone | pseudonymous | no |
| Cash | a balance | you | yes | no |

Moving down the table, less is remembered about *you*, and less enforcement is needed. That's the trade money makes. Everything I complained about in the previous post (money passed on to heirs, money growing on its own, money that can't tell a good deed from a profitable one) seems to me to come from the same move: throwing away the history and keeping one number.

#### Questions I haven't resolved

- The toy model has a single good and equal-sized gifts. With different goods, a single balance loses even more. Is there a natural "second number" worth keeping?
- Kandori's contagion fails as $N$ grows. Where does the cut-off sit for realistic patience, and does it line up with anything like Dunbar's number?
- Could a token *decay*, so that the balance tracks recent giving rather than lifetime giving? Silvio Gesell proposed money that loses value over time, for different reasons. What does decay do to the incentive to give?

<!-- TODO (figure): a small simulation in code/ comparing cooperation rate vs N under (1) public memory, (2) contagion, (3) tokens, for a fixed delta. Would make the "N doesn't appear" point visible. -->

---

[^kocherlakota]: Kocherlakota, N. R. (1998). Money is memory. *Journal of Economic Theory*, 81(2), 232–251.
[^kandori]: Kandori, M. (1992). Social norms and community enforcement. *Review of Economic Studies*, 59(1), 63–80.
