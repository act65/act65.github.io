---
title: The Offline Economy
subtitle: Why financial tools for the unconnected are a genuinely hard problem
layout: post
---

![Kutupalong refugee camp, Bangladesh]({{ site.baseurl }}/assets/offline-economy/kutupalong.jpg)

In southeastern Bangladesh lies Kutupalong, the largest refugee camp in the world. It's a sprawling city of bamboo and tarpaulin, home to nearly a million Rohingya refugees who fled violence in Myanmar. They face immense challenges: precarious shelter, limited access to healthcare, and a future shrouded in uncertainty. But one of their most profound — and most overlooked — challenges is digital exclusion.

The camp exists in a state of near-total internet blackout. Citing security concerns, the government has restricted mobile data and made it illegal for refugees to own SIM cards.[^1] This decision, condemned by human rights groups, effectively cuts off a million people from online education, from the global conversation, and, crucially, from the digital economy. And this situation is not unique. Governments in North Korea, China, Iran, and Eritrea also impose heavy restrictions on internet access, creating vast "digitally dark" regions across the globe.

## People need tools, not just handouts

When faced with a problem of this scale, the instinct is to think of aid — food, water, shelter. These are vital. But that view overlooks a fundamental truth: people are incredibly resilient and capable. Evidence from refugee camps worldwide reveals them as hives of economic activity. In the Rohingya camps a substantial informal economy exists, with refugees and local Bangladeshis running businesses in trade, services, and manufacturing. A 2018 World Bank study found that lending plays a critical role in this economy, with roughly half of all transactions conducted on credit.[^4]

The problem is not a lack of will, but a lack of tools. People don't just need handouts; they need a stable platform on which to build their own lives. And among the tools that platform is built from are basic financial instruments: a safe way to save, a reliable way to transact, a fair way to get a loan, and a predictable way to insure against disaster.

For those of us in the developed world, financial services are like plumbing: invisible, taken for granted, catastrophic when they fail. For the unbanked, their absence is a ceiling on all ambition.

- **Savings provide resilience.** Without a safe place to store value, a single medical emergency or a failed harvest can be ruinous, forcing a family to sell productive assets and fall deeper into poverty. Savings let households smooth consumption and absorb shocks.
- **Credit provides opportunity.** Without access to loans, starting a small business — a food stall, a tailoring service, a repair shop — is nearly impossible. Credit lets people invest in their own productivity and create jobs.
- **Insurance provides security.** In a crowded camp, a single fire can destroy a dozen homes. Insurance lets a family rebuild instead of being wiped out.
- **Payments provide reach.** A trustworthy way to transact lets you trade with people beyond your immediate circle of family and neighbours. Without it, commerce is limited to those you already know well enough to extend credit on a handshake — a small and slow-growing market.

Providing these tools is the fastest way to unlock the economic potential that already exists within the community. So why hasn't someone just done it?

## Can't we just beam in the internet?

The first thought for any tech-savvy person is obvious: can't we just provide connectivity? A solution like Starlink seems perfect. Technically, it would work flawlessly. Politically, it's a non-starter. Internet provision is a sovereign right, and any attempt to bypass national regulations would be shut down — and quite possibly used to justify further crackdowns on the people we were trying to help.

So we have to assume the constraint rather than fight it: **the system must work without the internet.** This points to a concept as old as computing itself — the **"sneakernet."** You physically move data from one place to another. In the camp, anyone with the app could act as a "syncing agent": they collect transaction data from their peers over a local Wi-Fi hotspot and, when they later reach an area with connectivity, upload it to the global network.

Projects like [Internet-in-a-Box](https://internet-in-a-box.org/) already do exactly this. But they move *information*, which is abundant. You can copy Wikipedia a million times and lose nothing.

Money is different. Money is defined by its scarcity. You cannot send the same dollar to two different people. This is the **double-spend problem**, and it is what makes building offline financial tools a fundamentally hard problem — not an engineering inconvenience, but a deep one.

## Why the obvious solutions fall short

Before reaching for something new, it's worth understanding why the existing options don't fit.

**Centralized IOU systems.** The most straightforward approach is for a trusted entity — say, an NGO — to run a simple database tracking debts and credits.[^5] Easy to build, but fundamentally brittle. It is a single point of failure and control: the NGO can censor transactions or freeze accounts, users have no true ownership of their financial lives, and if the NGO leaves or its server goes down, the economy collapses with it. Worse, that single point of control is also a single point of *leverage* — an NGO operating on a government's soil is subject to its laws and its pressure, and can be compelled to hand over data, freeze accounts, or shut the whole thing down. It is a top-down solution to a problem that demands bottom-up resilience.

**Connected blockchains (Celo, Stellar, …).** Projects like Celo have made real strides in making crypto accessible — for instance, by letting you send money to a phone number.[^6] But they are designed for the *connected*. They need an active internet connection to submit transactions for validation. They lower the barrier for people who already have data; they do nothing for the nearly billion people who live in digitally dark regions.

The failure of both is not a failure of effort. It is a direct consequence of a foundational result in distributed-systems design: the **CAP theorem**.

## The CAP theorem makes this unavoidable

The CAP theorem[^2] states that a distributed system can provide at most two of the following three guarantees:

1. **Consistency (C):** every user sees the same, up-to-date data. No double-spends are possible.
2. **Availability (A):** the system is always working and able to process requests.
3. **Partition tolerance (P):** the system keeps working even when parts of it are disconnected from each other — that is, *offline*.

To see why this bites, imagine a simple ledger for a village market that is temporarily offline. Alice has \$10. She buys bread from Bob for \$10, and her phone records it. A moment later she runs into Charlie and buys vegetables for \$10; her phone records that too. Both Bob and Charlie have accepted her payment. When the system comes back online and syncs, the server sees two transactions spending the same \$10. To stay **consistent**, it must reject one. But in the offline world, to stay **available** to both Bob and Charlie, it had to accept both — and so an inconsistency was born.

An offline system, by definition, *must* tolerate partitions. That forces a brutal trade-off. A traditional bank or a connected blockchain is a **CP system**: it chooses consistency over availability, so when it can't reach the central ledger, it simply stops working. A system for the camp has no such luxury. It must keep working while disconnected, which makes it an **AP system** — and an AP system is *forced* to accept the risk of temporary inconsistency.

This is the uncomfortable conclusion, and it's worth stating plainly: **in an offline AP system, a double-spend cannot be technically prevented at the moment it happens.** Unlike systems that can place a hold on funds during a transaction,[^3] an offline system has no way to stop a determined user from promising the same digital dollar to twenty different merchants before the next sync. The fraud only becomes visible later, when the data finally reconciles.

So the question is not *how do we prevent double-spending?* We've just shown we can't. The real question is:

> How do you build a trustworthy economy on top of a system where cheating is always physically possible?

## Maybe this is a problem reputation can solve

If you can't *prevent* bad behaviour, the only lever left is to *make it not worth it.* You shift from prevention to deterrence: detect the fraud after the fact, and attach a cost to it that is larger than anything the fraudster could gain in the moment.

But a cost to *what*, exactly? Money can be cashed out and walked away from. What you need is something that (a) accrues value over time through honest participation, (b) can't simply be abandoned and re-created from scratch, and (c) becomes worthless the moment you're caught cheating.

That something is **reputation**. A system that records your past actions to determine your future privileges is, almost by definition, a reputation system — and it turns out to be the natural answer to the constraints the CAP theorem hands us. It doesn't "solve" CAP; nothing does. Instead it makes living in the AP world safe, by ensuring that the value of a good standing always exceeds the one-time payoff of betraying it.

How you actually build such a thing — how reputation is earned, how it's slashed, how you give it tangible value so the threat of losing it bites, and how all of this composes into loans, insurance, and offline trade — is the subject of a separate piece: [the Rain protocol]({% post_url technical-posts/2025-06-26-rain %}).

The Rohingya camps are an extreme case, but the underlying problem is general. Wherever connectivity is unreliable, contested, or simply absent, the same trade-off appears. Getting it right matters far beyond one camp in Bangladesh.

---
[^1]: Human Rights Watch. (2021). *Bangladesh: Internet Ban in Rohingya Camps Endangers Lives*. [hrw.org](https://www.hrw.org/news/2021/06/01/bangladesh-internet-ban-rohingya-camps-endangers-lives)
[^2]: Gilbert, S., & Lynch, N. (2002). Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, 33(2), 51–59.
[^3]: Frean, M., & Marsland, S. (2022). Holds enable one-shot reciprocal exchange. *Proc. R. Soc. B*, 289(1980), 20220723. [doi.org/10.1098/rspb.2022.0723](https://doi.org/10.1098/rspb.2022.0723). (The value of *holds* in enabling exchange is exactly what an offline AP system gives up — which is why it needs a reputation system to manage the risk of delayed settlement.)
[^4]: World Bank & UNHCR. (2020). *Refugees Who Mean Business: Economic Activities in and Around the Rohingya Settlements in Bangladesh*. [worldbank.org](https://documents1.worldbank.org/curated/en/313391599041125574/pdf/Refugees-Who-Mean-Business-Economic-Activities-in-and-Around-the-Rohingya-Settlements-in-Bangladesh.pdf)
[^5]: An IOU ("I Owe You") system is a basic ledger that tracks debt obligations; in a centralized digital context, a simple database managed by a single entity.
[^6]: Celo is a mobile-first blockchain platform designed to make decentralized financial tools accessible via smartphone, often by mapping wallet addresses to phone numbers.
