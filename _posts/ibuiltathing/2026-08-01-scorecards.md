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

One honest qualification, since I'm claiming this is the uncontested part: any rubric written down has a house style, and mine has one. It rewards figures, mechanisms and named policies, and marks down hyperbole. That's a preference for the technocratic voice over the moral or the oratorical, and it isn't neutral. I'd defend it as the right register for a legislature. I wouldn't pretend I hadn't chosen it, and I come back to what it costs at the end.

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

**One source, on purpose.** An earlier version of this blended in party press releases and post-Cabinet press conferences, and that turned out to change a score more than the speaker did — the same MP scored several points higher in a release than in the House, and the mix of sources differed sharply by party. So comparing two MPs was really comparing two different tests. Hansard is the only source that is adversarial, on the record, and covers every MP equally. Press releases tell you what a party wants you to think; Hansard tells you how they behave when someone is arguing back.

The part I care about is that **every score links back to the statements behind it** — click any stat and you get the quotes, each with its own score, the reasoning, the date, and a link to the source. A quote has to survive a check against its own transcript before it reaches the site: anything not verbatim, spliced together from fragments, or not beginning and ending on a sentence boundary is dropped. The number itself is a *shrunk* average of the evidence you're looking at — thin evidence gets pulled toward the population middle on purpose, so a single flattering quote can't make a card. If you think it's wrong, go and check.

**Four of the six are judgeable from the text alone** — Civility, Rigor, Specificity and Focus. Everything you need to score them is in the sentence.

**Veracity and Divination are not.** Deciding whether a claim is true, or whether a forecast came off, means going and checking a source. Both now emit a specific claim plus what would falsify it, and a separate step searches for evidence and assigns the real score. That step hasn't finished running. Until it does, both are shown from the model's own unaided estimate, and every one of those is marked on the card with a superscript **?**, a dimmed number and an "unverified" note. **Read a ? as the model's guess, not as a fact-check.** Everything below is drawn from the four grounded attributes.

The data: **133 MPs** who have sat in this Parliament, **78,196 scored statements** across **170 sitting days** of Hansard.

<div style="display:flex; gap:2rem; justify-content:center; flex-wrap:wrap; margin:2rem 0;">
  <img src="{{site.baseurl}}/assets/scorecards/card-top.png" alt="Scorecard for Vanushi Walters" style="width:240px; max-width:45%;">
  <img src="{{site.baseurl}}/assets/scorecards/card-bottom.png" alt="Scorecard for Winston Peters" style="width:240px; max-width:45%;">
</div>

> **Top and bottom.** Left: the highest-ranked card in Parliament, Vanushi Walters. Right: the lowest of the 132 ranked cards. The six icons read left-to-right and top-to-bottom in the order listed above; card rank is the geometric mean, so one bad attribute drags the whole card down. The **?** on Veracity marks it as the model's estimate rather than a check. Portraits from Wikimedia Commons.

## Nobody passes

Against a pass mark of 100, here is the headline.

**The best card in Parliament is 74. The worst is 43.** The highest score any MP holds on any single attribute is a 90 — Vanushi Walters, on Focus. Nobody else in the building reaches it on anything.

One caveat that belongs here rather than at the bottom of the page: the displayed numbers are **deliberately compressed**, because thin evidence is shrunk toward the population average. That's the right call for ranking and it means the ceiling is partly my estimator rather than just Parliament. Individual statements do hit 100. The claim isn't that no MP is ever exemplary; it's that none of them sustains it.

**Rigor is the bleakest of the six.** Of 12,515 statements scored for whether they argue from evidence rather than fallacy, **fifty clear 90. One clears 95. None reaches 100.** The average is 47. No MP's Rigor score exceeds 64 — on the attribute that is closest to a description of the actual job, the best card in Parliament is a bare pass.

**Civility averages 60, and 488 scored statements land at 20 or below** — which is to say, are essentially just an insult. Across 170 sitting days that's about **three a day**. I can't tell you that's the base rate in the chamber, because the model chooses which statements to surface and I haven't measured whether it samples evenly. What I can say is that they aren't rare enough to need hunting for.

And they don't come evenly. Of those 488, **Winston Peters accounts for 109** — more than the next two MPs combined, who are Willie Jackson and David Seymour. It crosses the aisle and it concentrates in a handful of people.

The league table on the site is therefore a bit misleading, and I want to say so plainly: it isn't a ranking of good MPs and bad MPs. Everybody fails. The ranking is just the order they fail in.

Though I should own where that framing comes from, because it's mine and not the instrument's. The rubrics weren't built as 0-fails/100-passes. Civility's midpoint is anchored at "harsh but legitimate criticism of policies, ideas, or actions" — which is *acceptable* conduct, not failure — and the same is true of Rigor and Specificity. If you want to argue that a 60 means "mostly legitimate criticism with a bad day in it", the rubric is on your side and I'm not going to pretend otherwise. What survives the argument is the tail, and the Rigor ceiling.

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

Two patterns, and I can describe both better than I can explain them.

**It isn't left versus right.** I assumed the data would sort the parties along the usual axis. It doesn't. Every caucus lands between 57 and 65, and MPs vary far more *within* each party than the parties do between themselves. Whichever team you came here to have confirmed, it won't be.

<div style="margin:2rem 0;">
  <img src="{{site.baseurl}}/assets/scorecards/party-cards.png" alt="Aggregated scorecards for the six parties" style="width:100%;">
</div>

> **One card per caucus**, aggregated over its MPs. Because the headline numbers barely differ, the bars show each party's distance from the House average on each attribute rather than the number itself — which is where the differences actually are.

**It is government versus opposition.** Government MPs average 58, opposition MPs 64, and that gap is larger than any gap between the parties within each bloc.

Before reading anything into that: I think there's a real chance it is my instrument rather than the MPs. The opposition's job in the chamber is to attack government *policy*, which is exactly what Focus rewards. The government's job includes defending itself against the opposition, which is exactly what Focus punishes. A rubric that scores "are you talking about the policy or the other team" will hand points to whoever is structurally obliged to talk about the policy. I don't know how much of the six-point gap is conduct and how much is seating plan, and I'd rather flag that than bank it.

**It is not seniority.** This one I did expect, and the data took it off me. An earlier version of this project found the bottom of the table was the leadership — the Prime Minister, party leaders, senior ministers — and that reads as a satisfying story about how people rise. It doesn't survive. *Within* the government, MPs holding a ministerial or leadership role average **58.3**, and government backbenchers average **58.3**. The entire effect was which benches they sit on. It is also not about how much an MP talks: the correlation between how much evidence a card rests on and how well it scores is **0.02**, which is nothing.

What is true, and is just a fact about names rather than a finding about power: four of the five lowest cards in Parliament belong to the Prime Minister, the Deputy Prime Minister, the Foreign Minister and the Minister for Resources. The top of the table is backbenchers and select committee workhorses — mostly people you'd struggle to name. The visible part of our politics is the worst part of it, even if the reason is the job and not the person.

## What it isn't

A prototype, and I'd rather undersell it.

The scores are **automated estimates, not verdicts**, and the validation is the weakest part. The evaluation harness runs against hand-labelled statements, and the set it currently has is not fit for the job — a replacement sampled from the real corpus has been drawn but is **not yet labelled**. Until it is, treat every accuracy figure as unmeasured. There is also only one labeller, so there is no inter-rater agreement to report.

**Two of the six attributes are unchecked.** Veracity and Divination are shown from the model's own estimate, marked with a **?** on every card, until the resolver finishes searching for evidence. 260 of the 787 MP-attribute scores on the site carry that mark. Don't quote them as fact-checks; I haven't.

**Three attributes that used to be here are not**, for three different reasons, and the reasons are more interesting than the attributes.

*Charisma* was cut. It correlated with Civility at 0.96 — a charisma failure was almost always the same insult, counted a second time, and then compounded by the geometric mean used for card rank.

*Strength* (do promises turn into policy?) and *Authenticity* (do words inside the House match words outside it?) are on hold until the voting, bill and promise records they need are joined properly. Both had a defect worth naming: they filed a low score under the *speaker* even when the statement was describing someone else's broken promise, which penalised MPs for the act of scrutinising opponents.

*Forthrightness* — do they answer the question actually asked? — is the one I most wanted to keep, and it is measured but not shown. It is scored over question-and-answer pairs, and in the House, only ministers answer questions. Of the MPs with enough evidence to score it, **every single one sat on the government benches.** However well it's extracted, on a 133-card grid it would be a measure of whether you're in government. It stays in the pipeline because it is a good measure *of the executive*, which is worth its own page one day.

**Reading verbatim speech literally is a hazard.** Hansard is lightly-edited spoken language, full of inversions, self-corrections and half-finished sentences, and a scorer that sees one statement with no surrounding discourse takes all of them at face value. A word-order slip reads as a false claim. A single low score on a single sentence is not evidence of anything, and the reason every number links to its quote is so you can see which kind you're looking at.

**And the rubric has a politics of its own.** It rewards figures, mechanisms and named policies; it marks down hyperbole and moral register. That is a choice, and it is not costless: an instrument built this way will rank the most rhetorically confrontational MPs lowest, and a party whose role in the chamber is confrontation with the Crown is going to sit badly with it. That's a limit of what I've built rather than a verdict on anyone.

Nothing here is an accusation of wrongdoing. It's a starting point for looking, and the evidence is one click away.

## Why bother

Measurement won't fix politics. But notice how much we already measure about our politicians — polling, preferred PM, seat projections — and how little of it is about whether they're doing the job well. We measure *popularity* with great precision and *conduct* not at all.

Which is a shame, because conduct is the one thing we could actually agree on. You and I can disagree completely about tax and still both want the person arguing our side to answer the question, get their facts right, and skip the jokes about hair. That's a standard with no political side to it — and right now, on the public record, in our name, not one of the 133 people who have sat in this Parliament is meeting it.

There's an election in November. It would be nice to be able to ask.

**Have a look:** [nz-politician-scorecards.onrender.com](https://nz-politician-scorecards.onrender.com/) — cards on the front page, [party scorecards](https://nz-politician-scorecards.onrender.com/party), [the dataset](https://nz-politician-scorecards.onrender.com/data) for full stats and downloads, [about](https://nz-politician-scorecards.onrender.com/about) for method and caveats. It's on free hosting, so the first visit after a quiet period takes a few seconds to wake up.
