---
title: "What Makes a Good Politician?"
subtitle: "The one standard we can all agree on, and how our MPs score against it"
layout: post
description: "Every word of the 54th New Zealand Parliament, scored for how MPs argue rather than what they believe. Nobody passes."
tags:
  - essay
  - data
  - measurement
  - power
  - politics
  - new-zealand
  - mechanism-design
  - built
---

Here is the Deputy Prime Minister, in the House, on the record, describing another member:

> "If this guy opened a funeral parlour, nobody would die. He can screw up anything—"
> — David Seymour ([Hansard, 10 Mar 2026](https://hansard.parliament.nz/hansard-transcript/2026-03-10))

And here is a Cabinet minister, asked in the House to explain what systemic bias is:

> "Well, systemic bias is bias that's systemic."
> — Mark Mitchell ([Hansard, 29 Aug 2024](https://hansard.parliament.nz/hansard-transcript/2024-08-29))

I came across a run of clips like this — first from the UK Parliament, then ours — and the thing that surprised me wasn't that politics is rude. It was the setting. This is not a campaign rally or a late-night panel show. This is them **at work**, in the chamber, doing the job we elected them to do, and the record of it is kept forever.

Is that really how they behave while working? I couldn't tell from clips, because clips are selected to be bad. So I went and measured it.

## What should we expect?

Before measuring anything I had to decide what "good" even means here, and the distinction that makes it tractable is between **what** a politician believes and **how** they conduct themselves.

*What* they believe is legitimately contested. Capital gains tax, the road, the tunnel — that's what elections are for. I can't score it without just scoring "agrees with me," and neither can anyone else.

*How* they conduct themselves is a different kind of question — and if government and legislation really are matters of reason and judgment, as Burke told the voters of Bristol in 1774, then how an MP argues isn't decoration on top of the job. It *is* the job. We don't send them to Wellington to hold opinions; we send them to sit through the select committee, read the officials' advice, hear the submitters, and reason their way to a decision. Legislate, scrutinise the executive, represent. Everything else is downstream.

## The one standard we can all agree on

Here's the part I keep coming back to.

Take a handful of plain expectations of conduct. Get your facts right. Argue from evidence rather than fallacy. Say something, rather than something-shaped. Argue about the policy, not the other team. Attack the argument, not the person.

**A good politician scores 100 on every one of them.**

Not "better than the other lot." Not "about average for Parliament." One hundred. Every one is a floor rather than a stretch goal, and I don't think there's a voter in the country who'd call any of them unreasonable.

That's what makes conduct worth measuring when policy isn't. You and I might disagree completely about tax, immigration, Te Tiriti, the lot — and still agree, without argument, that the person making our case should answer the question and tell the truth while doing it.

And it's worth being blunt about why this matters, because it isn't a preference for good manners. **They are representing you.** That's the whole arrangement: they carry your interests into a room you're not in, and they speak with your authority when they get there. When the MP you voted for sneers at the other side, ducks a question, or reaches for a number nobody checked, that is done in your name.

So the question isn't the comfortable one — whether you think politicians in general are a bit much. It's narrower and it's aimed at you. **How do you want your side to win?** Is it fine for them to fight dirty, as long as they're fighting for something you believe in? Is a lie acceptable if it advances your goals?

Almost nobody, asked that directly, says yes. And no party campaigns on dodging or on getting the facts wrong — every one of them claims the opposite. It is the one standard in politics that isn't up for grabs.

So it should be possible to check. And mostly it isn't — fact-checks are one-off and forgotten inside a week, and there's no durable record of how an MP conducts themselves on the boring Tuesdays, only the clips that go viral. That's the gap I tried to fill.

## Measuring it

[**NZ Politician Scorecards**](https://nz-politician-scorecards.onrender.com/) gives every MP a trading card. Six attributes, scored 0–100, all oriented so higher is better, all measuring conduct rather than policy:

<ul style="list-style:none; padding-left:0; margin:1.2rem 0;">
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><path d='M12 3 L19 6 V12 C19 16 16 19 12 21 C8 19 5 16 5 12 V6 Z'/><polyline points='9 12 11 14 15 9'/></svg><span><strong>Veracity</strong> — are the factual premises accurate?</span></li>
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='9.5' r='5.5'/><path d='M12 7 L12.8 9 L14.8 9.8 L12.8 10.6 L12 12.6 L11.2 10.6 L9.2 9.8 L11.2 9 Z' fill='currentColor' stroke='none'/><path d='M8 16.5 H16 M9.5 16.5 L8.6 20 H15.4 L14.5 16.5'/></svg><span><strong>Divination</strong> — did the prediction come true?</span></li>
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><path d='M10 4 C13.5 7 13.5 17 10 20 C6.5 17 6.5 7 10 4 Z'/><line x1='2' y1='8' x2='7.2' y2='8'/><line x1='2' y1='12' x2='6.6' y2='12'/><line x1='2' y1='16' x2='7.2' y2='16'/><line x1='12.6' y1='8.4' x2='18.6' y2='11.6'/><line x1='13' y1='12' x2='18.6' y2='12'/><line x1='12.6' y1='15.6' x2='18.6' y2='12.4'/><circle cx='20' cy='12' r='1.3' fill='currentColor' stroke='none'/></svg><span><strong>Focus</strong> — is this about the policy, or about the other team?</span></li>
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><path d='M5 20 C8 16 11 11 13 4'/><path d='M13 4 C15.5 4.2 16.2 6.6 14.8 8 C12.7 7.8 12 5.2 13 4 Z'/><path d='M11.4 8.6 C13.9 8.8 14.6 11.2 13.2 12.6 C11.1 12.4 10.4 9.8 11.4 8.6 Z'/><path d='M9.4 13.2 C11.9 13.4 12.6 15.8 11.2 17.2 C9.1 17 8.4 14.4 9.4 13.2 Z'/></svg><span><strong>Civility</strong> — is the attack on the argument, or on the person?</span></li>
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><line x1='12' y1='4' x2='12' y2='20'/><line x1='4' y1='7' x2='20' y2='7'/><circle cx='12' cy='5.4' r='1' fill='currentColor' stroke='none'/><line x1='8' y1='20' x2='16' y2='20'/><path d='M1.5 8 C1.5 11 6.5 11 6.5 8'/><path d='M17.5 8 C17.5 11 22.5 11 22.5 8'/><line x1='4' y1='7' x2='4' y2='8'/><line x1='20' y1='7' x2='20' y2='8'/></svg><span><strong>Rigor</strong> — does the conclusion follow from the premises?</span></li>
  <li style="display:flex; gap:0.7rem; align-items:flex-start; margin:0.5rem 0;"><svg width="22" height="22" aria-hidden="true" style="flex:none; margin-top:0.16em;" viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='8.5'/><circle cx='12' cy='12' r='4.8'/><circle cx='12' cy='12' r='1.5' fill='currentColor' stroke='none'/></svg><span><strong>Specificity</strong> — is there checkable content in the sentence?</span></li>
</ul>

Every score comes from **Hansard**, the verbatim parliamentary record, and nothing else. The transcript of this Parliament is cut into windows of debate; each window goes to a large language model, which pulls out the statements bearing on an attribute and scores each against a fixed rubric; the scores average up to a card.

**One source, on purpose.** Hansard is the only record that is adversarial, on the record, and covers every MP equally. A party press release tells you what a party wants you to think; Hansard tells you how they behave when someone is arguing back. Measuring everyone in the same room is what makes two cards comparable at all.

The part I care about is that **every score links back to the statements behind it** — click any stat and you get the quotes, each with its own score, the reasoning, the date, and a link to Hansard. Nothing reaches the site unless it is a verbatim quote from that day's transcript, checked automatically, every time.

Four of the six — Civility, Rigor, Specificity and Focus — can be judged from the sentence itself, and everything in this post is drawn from those four.

The data: **133 MPs** who have sat in this Parliament, **78,196 scored statements** across **170 sitting days** of Hansard.

<div style="display:flex; gap:2rem; justify-content:center; flex-wrap:wrap; margin:2rem 0;">
  <img src="{{site.baseurl}}/assets/scorecards/card-top.png" alt="Scorecard for Vanushi Walters" style="width:240px; max-width:45%;">
  <img src="{{site.baseurl}}/assets/scorecards/card-bottom.png" alt="Scorecard for Winston Peters" style="width:240px; max-width:45%;">
</div>

> **Top and bottom.** Left: the highest-ranked card in Parliament, Vanushi Walters. Right: the lowest of the 132 ranked cards. The six icons read left-to-right and top-to-bottom in the order listed above; card rank is the geometric mean, so one bad attribute drags the whole card down. The **?** on Veracity marks it as the model's estimate rather than a check. Portraits from Wikimedia Commons.

## Nobody passes

Against a pass mark of 100, here is the headline.

**The best card in Parliament is 74. The worst is 43.** The highest score any MP holds on any single attribute is a 90 — Vanushi Walters, on Focus. Nobody else in the building reaches it on anything. Individual *statements* hit 100 all the time; the point is that nobody sustains it.

**Rigor is the bleakest of the six.** Of 12,515 statements scored for whether they argue from evidence rather than fallacy, **fifty clear 90. One clears 95. None reaches 100.** The average is 47. No MP's Rigor score exceeds 64 — on the attribute that is closest to a description of the actual job, the best card in Parliament is a bare pass.

**Civility averages 60, and 488 scored statements land at 20 or below** — which is to say, are essentially just an insult. Across 170 sitting days that's about **three a day**, and I wasn't hunting for them.

And they don't come evenly. Of those 488, **Winston Peters accounts for 109** — more than the next two MPs combined, who are Willie Jackson and David Seymour. It crosses the aisle and it concentrates in a handful of people.

The league table on the site is therefore a bit misleading, and I want to say so plainly: it isn't a ranking of good MPs and bad MPs. Everybody fails. The ranking is just the order they fail in.

## Four ways to fail

One example per grounded attribute, all verbatim, all from Hansard, all linked. The number is the score that statement received. These are the clearest illustrations I could find rather than a balanced sample — the site has 132 cards on the front page if you want to check your own team.

**Rigor — 5/100.** The Mitchell tautology from the top of this post. Asked to explain a term, he defines it with itself; there is no inference in the sentence to follow.

**Civility — 10/100, and Focus — 0/100.** The Seymour funeral-parlour line, also from the top. It scores twice, for two different failures: it is an attack on a person rather than an argument, and it is about the other team rather than about any policy.

**Specificity — 5/100.** A whole sentence, committing to nothing:

> "We are confident we will have effective legislation that will deliver good outcomes."
> — Casey Costello, NZ First ([Hansard, 27 Feb 2024](https://hansard.parliament.nz/hansard-transcript/2024-02-27))

**Focus — 5/100.** Not an insult, and not untrue. Simply not about anything that could be legislated:

> "They start the blame game. They blame Labour for everything. They blame us for absolutely everything."
> — Peeni Henare, Labour ([Hansard, 23 Jul 2025](https://hansard.parliament.nz/hansard-transcript/2025-07-23))

## It isn't that they can't

All of which would be unfair if the standard were unreachable. It isn't — and the clearest evidence is that the same people who sit at the bottom of the table reach it.

Winston Peters has the lowest card in Parliament and a third of his scored civility statements are personal attacks. Here he is at 95, conceding a point to an industry he was there to regulate:

> "The industry has made genuine efforts, particularly within recent years, to address the animal welfare issues, and this should be acknowledged, especially in regard to dog deaths."
> — Winston Peters, NZ First ([Hansard, 10 Dec 2024](https://hansard.parliament.nz/hansard-transcript/2024-12-10))

Shane Jones has the second-lowest card. Here he is at 100, to a Labour minister, mid-debate:

> "The former Minister, the Hon Dr Megan Woods, makes a very good point. There was an egregious case of that."
> — Shane Jones, NZ First ([Hansard, 19 Nov 2024](https://hansard.parliament.nz/hansard-transcript/2024-11-19))

And then the single clearest illustration in the dataset, which is one MP, in one debate, on one afternoon. Simon Court, on the Resource Management Act, 31 March 2026 — scored **100**:

> "I probably shouldn't be admitting that as an ACT MP, but the National Policy Statement on Urban Development, Mr Twyford, actually set the scene for why it's important to build up around these expensive investments in transport, like the City Rail Link, and to build up around our town centres so that—for people like me, who live within a five-minute walk of the supermarket in the town centre—those benefits are extended to many, many more people in affordable homes."

and, in the same debate, to a member sitting opposite — scored **30**:

> "Now, there are so many examples, but, essentially, failing to provide that balance between plan-enabled growth—in other words, what you SimCity obsessed planning nerds believe should be the right number of houses, Tamatha Paul—versus the amount of infrastructure that's needed to support that growth is still the problem to solve."
> — Simon Court, ACT ([Hansard, 31 Mar 2026](https://hansard.parliament.nz/hansard-transcript/2026-03-31))

He is plainly capable of the first. He was capable of it on the same afternoon, in the same debate — and did the second anyway.

Neither of these costs anything except the momentary pleasure of not conceding.

## Where the failures cluster

One pattern, and it's a big one: **government MPs score lower than opposition MPs.** Government averages 58, opposition 64, and that is not a rounding artefact. The spread inside each group is about four points, so the gap between them is larger than the typical distance between two MPs on the same bench. Only four of the sixty-five opposition MPs fall below the government average. About a third of all the variation between cards is accounted for by which side of the House someone sits on. Knowing an MP's actual party on top of that buys you almost nothing — another five points of variance, from six parties instead of two sides.

<div style="margin:2rem 0;">
  <img src="{{site.baseurl}}/assets/scorecards/party-cards.png" alt="Aggregated scorecards for the six parties" style="width:100%;">
</div>

> **One card per caucus**, aggregated over its MPs. The bars show each party's distance from the House average on each attribute, because the headline numbers barely separate — every caucus lands between 57 and 65.

**I can't tell you what that gap means, and I want to be straight about why.** In this Parliament the opposition is Labour, the Greens and Te Pāti Māori. "Government versus opposition" and "right versus left" are the same line drawn twice, and one term of data cannot pull them apart. If you came here wanting the numbers to say the left argues better, they are consistent with that. They are equally consistent with something much duller: that the opposition's job in the chamber is to attack government policy, which is exactly what Focus rewards, while the government's job includes defending itself against the opposition, which is exactly what Focus punishes. A rubric that asks "are you talking about the policy or the other team" hands points to whoever is structurally obliged to talk about policy.

There is one small crack in the ideological reading. Te Pāti Māori are in opposition, and on the usual axis they sit furthest from the government — so they should be at the top. They aren't. They come fifth of six, level with the government parties. That's the wrong way round for a story about left and right, and the right way round for a story about rhetorical register. It is also seven MPs, so treat it as a hint rather than a result.

**It is not seniority.** *Within* the government, MPs holding a ministerial or leadership role average 58.3, and government backbenchers average 58.3. Whatever is going on, it isn't that power corrodes conduct. Nor is it about how much an MP talks: the correlation between how much evidence a card rests on and how well it scores is 0.02, which is nothing.

What is true, and is a fact about names rather than a finding about power: four of the five lowest cards in Parliament belong to the Prime Minister, the Deputy Prime Minister, the Foreign Minister and the Minister for Resources. The top of the table is backbenchers and select committee workhorses — mostly people you'd struggle to name. The most visible part of our politics is the worst-behaved part of it, whatever the reason turns out to be.

## One thing to hold on to

Every score here was produced by a language model reading Hansard against a rubric. **That makes it an estimate, not a verdict**, and models get things wrong in ways that are hard to predict from the outside — a word-order slip in live speech can read as a false claim, and a sentence lifted out of a debate can lose the thing that made it reasonable.

Which is why the number is never the point. Every score on the site links straight to the statements it came from — the quote, the date, the reasoning, the Hansard link. If a card looks wrong to you, two clicks will show you whether it is. I'd rather you checked than believed me.

Two of the six attributes need a further warning. **Veracity and Divination are the ones a model can't settle by reading**, because deciding whether a claim is true means going and looking it up. A search step does that, and it hasn't finished running — so those two are currently the model's own estimate, marked on every card with a **?**. Read them as a guess. Nothing in this post rests on them.

## Why bother

Measurement won't fix politics. But notice how much we already measure about our politicians — polling, preferred PM, seat projections — and how little of it is about whether they're doing the job well. We measure *popularity* with great precision and *conduct* not at all.

Which is a shame, because conduct is the one thing we could actually agree on. You and I can disagree completely about tax and still both want the person arguing our side to answer the question, get their facts right, and skip the jokes about hair. That's a standard with no political side to it — and right now, on the public record, in our name, not one of the 133 people who have sat in this Parliament is meeting it.

There's an election in November. It would be nice to be able to ask.

**Have a look:** [nz-politician-scorecards.onrender.com](https://nz-politician-scorecards.onrender.com/) — cards on the front page, [party scorecards](https://nz-politician-scorecards.onrender.com/party), [the dataset](https://nz-politician-scorecards.onrender.com/data) for full stats and downloads, [about](https://nz-politician-scorecards.onrender.com/about) for method and caveats. It's on free hosting, so the first visit after a quiet period takes a few seconds to wake up.
