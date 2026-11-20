---
title: Reputation as a belief
subtitle: A Bayesian reading of decay, loan size, trust and vouching
layout: post
permalink: /reputation-as-belief/
categories:
    - research
description: "Starting from one question, how likely is this person to keep their next promise, and deriving why reputation should decay, whose evidence counts, what a first loan is for, and how a newcomer can start."
takeaways:
  - "If people can change, old evidence about them survives with a probability that shrinks with its age, so an estimate of their reliability regresses to the prior at the rate people change."
  - "Two decaying counters recover most of what the exact Bayesian filter knows, but they should forget several times faster than people change."
  - "A kept promise is evidence only to a reader who trusts that the counterparty was independent. An extraordinary record needs extraordinary trust."
  - "To a reader who trusts nobody, a record is worth what it cost in fees. That is enough for a newcomer with a guarantor to outgrow them."
  - "Trust is the amount put at risk on a belief. A confident belief comes from evidence about the person or from incentives that bind anyone; for loan size the two describe the same behaviour."
tags:
  - research
  - formalised
  - uncertainty
  - probability
  - trust
  - mechanism-design
---

A lender deciding whether to trust someone wants to know one thing:

> How likely is this person to keep their next promise?

Trust is what the lender does with the answer: the amount they are willing to put at risk on it. Someone about whom nothing can be predicted cannot be trusted with much. Prediction alone is not enough, though, because someone certain to default is perfectly predictable. The lender needs a confident prediction that the promise will be kept, and there are two ways to come by one. Evidence narrows down what kind of person this is. Incentives make keeping the promise the better choice whatever kind they are. Both appear below, and for the size of a loan they describe the same behaviour.

This post works out a rational answer and compares it with the rules of [Rain]({{ site.baseurl }}/rain/). It has two parts, because the question has two.

**Will they keep it?** If people can change, an estimate of their reliability drifts back to what we believe about a stranger, at the rate people change. So reputation should fade, and how fast it fades is a statement about people.

**How much can they be trusted with?** Someone who always repays 100 may not repay 10,000. A record answers this with a credit limit, a little above the largest amount the person has repaid. The second half of the post is about that limit: when a lender should raise it, what a first loan to a stranger is for, whose word counts as evidence, how one person can vouch for another, and what happens when several creditors cannot see each other.

{% assign n = site.data.rain %}

## If people never changed

Let $\theta$ be the probability that a given person keeps a promise. Across the population $\theta$ varies; say it follows $\mathrm{Beta}(a_0, b_0)$. That is the prior, what we believe about a stranger. After watching someone keep $K$ promises and break $B$,

$$ \theta \mid \text{data} \sim \mathrm{Beta}(a_0 + K,\; b_0 + B), \qquad \hat p = \frac{a_0 + K}{a_0 + b_0 + K + B} . $$

So reputation is two counts and a prior. Nothing fades: a promise kept ten years ago weighs the same as one kept yesterday. That is correct only if $\theta$ is fixed for life.

## People change, so evidence has to survive

Suppose that between any two promises, with a small probability $h$, a person's circumstances change and their $\theta$ is drawn afresh from the population. A promise kept $\tau$ steps ago is then evidence about the person in front of you only if no change has happened since, which has probability $\gamma^{\tau}$ with $\gamma = 1 - h$.

Split the possible worlds into those where this is still the person the evidence describes and worlds where it is not. In the first we have the posterior. In the second we have only the prior. So before the next promise

$$ p(\theta_{t+1} \mid \text{data}) \;=\; \gamma \, p(\theta_t \mid \text{data}) \;+\; (1-\gamma)\, \pi(\theta), $$

and the mean obeys

$$ \hat p_{t+1} = \gamma\, \hat p_t + (1 - \gamma)\, p_0 . $$

**With no new evidence, the estimate drifts back to what we would believe about a stranger, geometrically.** The step is exact, and the rate of decay, $1 - \gamma$, is the probability $h$ that a person changes.

## What a contract can afford

Carrying that forward exactly is expensive. The mixture is not a Beta distribution, and each new promise adds a component: the exact estimate tracks a whole distribution over how long ago the last change happened.

A contract can store two counters per person and shrink both each step:

$$ K \leftarrow \gamma K, \qquad B \leftarrow \gamma B . $$

This is a different pooling of posterior and prior from the one above. It is their geometric mean, $p(\theta \mid \text{data})^{\gamma}\,\pi(\theta)^{1-\gamma}$, where the exact step is their arithmetic mean. Equivalently it is the distribution closest, in a weighted Kullback-Leibler sense, to both what the data said and to knowing nothing. Both regress to the prior.

How much does the cheap version lose? On data simulated from the model, scored by how well each method predicts the next outcome:

| How often people change, $h$ | Gap closed with $\gamma = 1 - h$ | Best $\gamma$ | Gap closed with the best $\gamma$ |
|---|---|---|---|
| 0.005 | {{ n.gap_matched_h005 }} | {{ n.best_gamma_h005 }} | {{ n.gap_best_h005 }} |
| 0.02 | {{ n.gap_matched_h02 }} | {{ n.best_gamma_h02 }} | {{ n.gap_best_h02 }} |
| 0.05 | {{ n.gap_matched_h05 }} | {{ n.best_gamma_h05 }} (edge of the range tried) | {{ n.gap_best_h05 }} |

*"Gap closed" is the share of the difference in prediction error between never forgetting and the exact filter. 2,000 simulated people, 300 promises each, five seeds.*

![Prediction error against forgetting rate, for three rates of change]({{ site.baseurl }}/assets/rain/forgetting-rate.svg)

- **Two decaying counters are enough**, provided the decay rate is chosen well.
- **The best decay rate is faster than the rate of change.** The counters should forget two to six times faster than people change. Forgetting faster makes the estimate noisier, in proportion to $1 - \gamma$. Forgetting slower leaves in evidence about someone who no longer exists, in proportion to $h/(1-\gamma)$. The sum is smallest when $1 - \gamma$ is proportional to $\sqrt{h}$, and the three optima sit close to $0.42\sqrt{h}$. The trade-off is a heuristic argument, and the constant is fitted to three points.

Decay is as slow as people are stable. If someone's reliability changes about once in 200 promises, the best memory is about 33 promises. With real data the rate should be fitted by asking which $\gamma$ predicts best. And never forgetting is close to useless once people change at all: at $h = 0.05$ it predicts barely better than ignoring the person's history ({{ n.static_loss_h05 }} against {{ n.prior_loss_h05 }}).

## How much? The size of a promise

The model so far treats a promise to repay 10 and a promise to repay 10,000 as the same kind of evidence. They are not, and treating them alike is how a long record of small kept promises becomes the cheapest preparation for one large default. So the question changes from *will they keep it?* to *how much will they keep?*

**The model.** Each borrower has a private threshold $c$: the most they would repay sooner than lose their standing. They repay any amount up to $c$ and default on anything above it, apart from a small probability $q$ of a shock that makes them default regardless. The lender does not know $c$.

**What a repayment shows.** Repaying an amount $M$ shows that $c \ge M$. Nothing else in a clean record matters, so the record is summarised by one number: **the largest amount repaid**.

**What the lender believes about the rest.** Thresholds differ between people. Let them follow a Pareto distribution, $P(c > x) = (x_{\min}/x)^{a}$, which has no built-in scale: someone good for 1,000 is as likely to be good for 2,000 as someone good for 10 is to be good for 20. Then for an amount $X \ge M$

$$ P(\text{repay } X \mid \text{largest repaid } M) \;=\; (1 - q)\left(\frac{M}{X}\right)^{a} . $$

**An example.** Take $a = 1$ and $q$ = 2%, and someone who has repaid 1,000. Asked for 1,000 again they repay with probability 98%. Asked for 2,000, {{ n.size_example_double }}. A lender who accepts a 10% chance of default can let them owe {{ n.size_example_limit }}, which is {{ n.k_screen }} times what they have shown. A stranger, about whom the lender knows only that people are good for at least 100, gets {{ n.off_stranger_limit }}.

![Chance of repayment against the amount due, for a stranger and for someone who has repaid 1,000]({{ site.baseurl }}/assets/rain/belief-by-size.svg)

*The belief as a curve. Up to the largest amount repaid, only a shock stops repayment. Above it the chance falls in proportion. The credit limit is where the curve crosses the risk the lender accepts, and each repayment moves the whole curve to the right.*

Everything after this section is a question about that curve: when to move along it, where a stranger's curve comes from, and whose reports are allowed to move it.

## Several creditors at once

The threshold is on everything a borrower owes at once. One lender sees all of it. Where several creditors cannot see each other, each sees a part.

That is the situation of shops accepting payments with no connection. A payment that cannot be checked is a loan, and a double spend is a default. If each of $m$ shops accepts the whole limit, the payer can owe $m$ times it.

![Default rate against the number of shops, with and without dividing the limit]({{ site.baseurl }}/assets/rain/offline-exposure.svg)

*Payers drawn from the model, each taking everything on offer. Shops that each accept the whole limit meant to accept a 10% chance of default; with two shops it is {{ n.off_default_2 }} and with five {{ n.off_default_5 }}. Shops that each accept a fifth are back at {{ n.off_split_default_all }} when the payer visits five.*

So each shop should accept a share $1/m$, or all should ask one local hub that sees the total.

The same fact runs the other way. Amounts that were owed at once and all paid are evidence of their total, to a reader who believes every one of them. After {{ n.off_windows }} rounds, a payer spending at five shops has a limit of {{ n.off_growth_concurrent }} if the shops count totals and trust each other fully. If they count only the largest note it is {{ n.off_growth_default }}, a stranger's.

## When should the next loan be larger?

Take the lender's side. It earns interest $i$ on a loan that is repaid and loses the principal otherwise, and discounts at $r$ per loan. A borrower known to repay an amount is then worth, per unit of that amount,

$$ v = \frac{(1-q)\,i - q}{(1+i)\left(1 - \frac{1-q}{1+r}\right)} , $$

which is {{ n.repeat_value }} with $i = r$ = 5% and $q$ = 2%. Raising the loan from $M$ to $kM$ multiplies the chance of repayment by $k^{-a}$ and the principal at risk by $k$. With $a = 1$ the expected amount repaid does not change and the amount at risk grows, so **a lender who maximises profit never raises a loan above what the borrower has shown**. Raising pays only when thresholds are heavy-tailed,

$$ (1-q)(1-a)(1+i)\left(1 + \frac{v}{1+r}\right) > 1 , $$

which at 5% interest means a tail index below {{ n.growth_tail_5 }}. A search over every sequence of loan sizes agrees. A lender who accepts a fixed 10% risk on each loan, raising it {{ n.k_screen }} times each step, loses {{ n.risk_ladder_value }} per stranger where repeating the same loan earns {{ n.repeat_floor_value }}.

The borrower's side gives two more bounds on a step $k$.

- **Honest borrowers must want to stay.** With a gain of $\sigma$ per unit borrowed, repaying is better than leaving when
  $$ k \;\ge\; \frac{(1+i)(1+r)}{1 + i + \sigma} , $$
  which is {{ n.k_stay }} with $\sigma$ = 3%. The loan size cancels.
- **Climbing in order to default must not pay.** A borrower who repays every loan and defaults on the last has, when each loan is $1 + i$ times the one before, received nothing along the way: each new loan exactly repays the old. Their whole take is the first loan. So $k \le 1 + i$, and the first loan is the whole exposure.

These come from two models: in the first a threshold is given, and in the second the borrower chooses. The next section derives the first from the second.

## Where the threshold comes from

Give a borrower a *capacity* $K$, the amount of borrowed money they can put to use, and a net return $\sigma$ on it per loan (what it earns beyond the interest). Each period they either repay or keep the principal and are shut out.

Offered the same loan again each period, a borrower within their capacity repays when

$$ \sigma \;\ge\; \sigma^* \approx r + q , $$

their discount rate plus the chance that a shock ends the relationship anyway. With fees and interest it is {{ n.return_threshold }} here, against {{ n.discount_plus_shock }} for $r + q$. The size of the loan cancels: whether such a loan is repaid depends on the borrower's return, not on the amount.

Lent more than they can use, they keep repaying up to a principal of

$$ c \;=\; K\,\frac{\sigma + i}{\sigma^* + i} , $$

which is {{ n.capacity_ratio_15 }} times capacity at a return of 15%. So the threshold is capacity, scaled, and has the same tail.

- **The borrowers who "take the first loan and vanish" in the next section are those with a return below $\sigma^*$.** Their share is a property of the applicants, not a free input.
- **Growth holds a low-return borrower only while it lasts.** While each loan is larger than the last they repay, and when growth stops they default. A lender has no reason to want them, which is why it is no contradiction that borrowers want growth and lenders do not offer it.
- **A higher interest rate does not help.** The net return needed barely moves with the rate, so the gross return needed rises one for one: {{ n.gross_needed_5 }} at 5% interest and {{ n.gross_needed_10 }} at 10%. Raising the rate turns more borrowers into defaulters.

## The first loan is a purchase of information

A lender learns about a stranger only by lending. Suppose a share $\pi_0$ of strangers take the first loan and vanish, and the rest are good for at least a floor amount. Lending the floor is expected to lose money by itself once $\pi_0$ exceeds $m/(1+m)$, with $m = (1-q)i - q$: {{ n.first_loan_loses_above }} here. It is still worth doing, because a survivor is worth $v$ per unit from then on.

How large should it be? Smaller screens more cheaply. But the lender can then raise the loan by at most $1 + i$ each time (the bound above), so a smaller start takes longer to reach the floor. The best first loan, as a share of the floor:

| Strangers who vanish | Best first loan (floor = 100) |
|---|---|
| 10% | {{ n.first_due_10 }} |
| 20% | {{ n.first_due_20 }} |
| 30% | {{ n.first_due_30 }} |

At 20% the first loan is expected to lose {{ n.first_alone_20 }} and the stranger is worth {{ n.first_value_20 }} overall. **The expected loss on the first loan is the price of learning who is genuine.** After it the lender raises each loan by exactly $1 + i$ until the floor and never after.

If those who vanish can return under a new name, they will, for as long as the first loan exceeds what a new identity costs. The first loan is then bounded by the price of an identity, and with free identities a stranger can be lent nothing.

## Whose evidence?

Two people can pass a loan back and forth. Each round costs {{ n.wash_cost }} of the amount (the fee, less what returns as dividends) and puts a kept promise on the log. So a kept promise is evidence about the promisor only if the counterparty was independent of them, and that is something each reader has to judge.

Let $t$ be a reader's probability that a counterparty is independent. A repayment of $M$ to them then says "the threshold is at least $M$" with probability $t$ and nothing otherwise, so it multiplies the likelihood of every threshold below $M$ by $1 - t$. With prior survival $S(x) = P(c \ge x)$, for an amount $X \le M$:

$$ P(c \ge X \mid \text{repaid } M) \;=\; \frac{(1-t)\,\big(S(X) - S(M)\big) + S(M)}{(1-t)\,\big(1 - S(M)\big) + S(M)} . $$

![Chance of repayment against the amount due, for one record seen by readers with different trust in the counterparty]({{ site.baseurl }}/assets/rain/belief-by-trust.svg)

*One record, 10,000 repaid to one counterparty. A reader who trusts that counterparty fully lends up to {{ n.portable_full }}. At 99.9% trust the limit is {{ n.portable_999 }}, and at 99% it is {{ n.portable_99 }}, close to a stranger's.*

With $t = 1$ this is 1, and with $t = 0$ it is the prior. In between it stays close to the prior whenever $S(M)$ is small. **An extraordinary record needs extraordinary trust.** A repayment a hundred times what a stranger is thought good for moves a reader who trusts the counterparty at 99% from 109 to {{ n.portable_99 }}; at 99.9%, to {{ n.portable_999 }}; full trust gives {{ n.portable_full }}.

- **A ring with one half-trusted member gains little**: at most {{ n.half_trust_multiple }} times a stranger's loan, by claiming about that much and no more.
- **An honest record is portable only along trust.** A new lender can use a history made elsewhere only if it trusts the counterparties in it almost completely.
- **Independence is the assumption that matters.** Witnesses multiply: with $n$ independent counterparties the doubt is $(1-t)^n$. Twenty half-trusted identities take {{ n.sybil20_multiple }} times a stranger's loan, unless the reader knows they are one group, in which case they count as one.
- **The fee buys a margin.** Each fake witness costs a fee. No ring of any size profits while a reader's trust in unknown counterparties is below about {{ n.safe_trust_ratio }} times the fee rate. At 1% trust, reaching a hundred times a stranger's loan takes {{ n.small_trust_confederates }} confederates and loses {{ n.small_trust_loss }}.

## Vouching

If a stranger can be lent nothing, a newcomer needs someone to answer for them. A guarantee is two promises of the same amount: the borrower's to the guarantor, and the guarantor's to the lender. If the borrower defaults, the guarantor pays or becomes the lender's defaulter.

![A guaranteed loan is two promises]({{ site.baseurl }}/assets/rain/rain-guarantee.svg)

The lender now needs no belief about the newcomer. It needs one about the guarantor, and it has one. What the guarantor believes shows in their price. They pay when the borrower does not, so for an amount $X$ the least they can charge is

$$ \big(\pi + (1-\pi)\,q\big)\,X \;+\; \text{the fee they sink} , $$

where $\pi$ is their own probability that the borrower will vanish: {{ n.vouch_cost_sure }} on 10,000 if they are sure of the borrower, {{ n.vouch_cost_10 }} at 10%, {{ n.vouch_cost_50 }} at 50%. A vouch is evidence because the person giving it bears the cost of being wrong.

The reading above applies without change. The guarantee is the guarantor's own promise, so it counts against what the lender will let the guarantor owe. And the borrower's kept promise was to the guarantor, so a lender who trusts only its own dealings gives it no weight as evidence about the borrower.

## A record is worth what it cost

That last point leaves the newcomer needing the guarantor for ever. The way out does not use belief at all.

A lender can accept from a borrower, unsecured, up to

$$ \min\Big(\; \text{evidence},\;\; (1+i) \times \text{own} \;+\; \text{fees sunk since} \;\Big) , $$

where *evidence* is the largest amount they have repaid to anyone, *own* the largest they have repaid to this lender, and *fees sunk since* the fees on promises they have kept since that loan was made, less the share that returns as dividends ({{ n.sunk_fee_share }} is sunk).

The argument is about cash, not probability. A ring is free to manufacture any record. Under this rule each unit of credit it gains has cost it a unit of fees, and each repayment to the lender buys a next loan that just repays it. So being fake does not pay, and a record's holder is either genuine, in which case *evidence* is what they are good for, or losing money. An honest borrower pays the same fees as a by-product of loans that are worth having.

A newcomer who borrows 10,000 a cycle under a guarantee is offered 100 unsecured at first, {{ n.graduation_offer_40 }} by the fortieth loan, and needs no guarantor from loan {{ n.graduation_cycles }}. To a lender who knows nothing else, a point of reputation is worth {{ n.credit_per_point }} of unsecured credit.

![Unsecured credit offered to a newcomer by loan number]({{ site.baseurl }}/assets/rain/graduation.svg)

*The unsecured credit offered to a newcomer who borrows 10,000 a cycle under a guarantee. The guarantee supplies the evidence at once; each loan repaid adds the fees sunk in it. Without a guarantor the same newcomer is offered 100 and stays there.*

Two qualifications.

- **How much of a fee is sunk depends on who paid it.** A fee returns over time as dividends, so to someone who discounts at $r$ the sunk share is $r/(r+\delta)$, and a ring more patient than the lender assumed is credited too much. With the share set for 5%, a ring that discounts at 4% gains {{ n.patient_gain_4 }} of the fees it pays, and one that does not discount at all gains {{ n.patient_gain_0 }}. The safe setting is the rate of the most patient attacker allowed for. Zero is always safe, and the rule still works: each loan may grow by the interest rate up to the evidence, which needs no assumption about anyone. The newcomer then needs the guarantor for {{ n.graduation_cycles_zero }} loans instead of {{ n.graduation_cycles }}. So the guarantee supplies the evidence at once, and the fees only set the speed.
- **A lender will not drop a guarantor for nothing.** The guarantor was carrying the risk of a shock. At the same interest the lender is {{ n.lender_loss_from_graduating }} worse off letting the borrower graduate. Paid for the risk, at {{ n.unsecured_rate_lender }} on the unsecured part, it is indifferent, and the borrower is still better off up to {{ n.unsecured_rate_borrower }}: the guarantor's fee no longer has to be sunk by anyone. At the higher rate each loan may also grow faster, and the guarantee is gone in {{ n.graduation_cycles_premium }} loans.

## What this says about Rain's score

- **It fades.** Rain multiplies every score by a fixed fraction each period.
- **It is two numbers.** Each account has a counter for promises kept and one for promises broken, in the same unit and fading together. The contract returns the posterior mean for whatever prior the reader supplies.
- **A broken promise is one observation.** There is no extra penalty. A lender who loses more from a default than it gains from a repayment says so in the risk it accepts.
- **It is weighted by size, roughly.** A promise counts in proportion to its fee, which is a percentage of the amount. That is a sum, where the threshold model wants a maximum; a reader can compute the maximum from the log.
- **It does not turn strangers into trusted parties.** A stranger starts at the floor, with a first loan that is a purchase of information. What the record changes is the cost of building trust from there, and the cost of faking it.
- **It is a count of fees, and says so.** The counters treat every counterparty alike, so they are what a reader who trusts everyone would compute. To anyone else they are a receipt for cost, which the last section shows how to use.

## What is established

| Claim | Status |
|---|---|
| If people change with probability $h$, the estimate regresses to the prior at rate $1 - h$ | Derived; exact for the mean. |
| Decayed counts are the geometric pooling of posterior and prior | Derived; exact for the Beta family. |
| Decayed counts predict nearly as well as the exact filter; the best decay is faster than $h$, roughly as $\sqrt{h}$ | Measured on data simulated from the model, at three values of $h$. |
| Largest amount repaid is the statistic; the two bounds on a step | Derived from the threshold model and checked against it. |
| A lender never raises a loan above the evidence unless the tail index is small | Derived; confirmed by a search over all loan sequences. |
| The first loan's size and expected loss | Computed by that search and confirmed by simulating borrowers. The share of strangers who vanish is an input. |
| The belief under partial trust; the bounds on what a ring can take | Derived; checked by Monte Carlo and against a model of the contracts. |
| The margin of safe trust, {{ n.safe_trust_ratio }} times the fee rate | Computed after the experiment was run; no prediction was made. |
| Guarantees: what a guarantor can lose a lender, what a vouch costs | Derived; checked against a model of the contracts, which is checked against the contracts. |
| A record is worth what it cost; no ring profits | A cash-flow argument; no profitable strategy among {{ n.graduation_strategies }} searched, for a ring no more patient than assumed. |
| The threshold is capacity, scaled; repaying depends on return and not on size | Derived; confirmed by comparing the two strategies directly. |
| Creditors who cannot see each other multiply the exposure; dividing the limit restores it; amounts owed at once count for their total | Derived; checked on payers drawn from the model and against a model of the contracts. One prediction was wrong: partial trust between shops caps the growth of credit, where we expected it to slow it. |
| A lender and a borrower both prefer graduation over a range of rates | Derived; the lender's side confirmed by simulating borrowers with shocks. |

Not established: how capacities and returns are spread among real borrowers, or how often people change. Every rate above is assumed. Still open are a decay rate per person, borrowers who can start again under a new name in the model of the last few sections, a lender choosing its policy against borrowers who choose theirs, and a version of *evidence* that adds up loans carried at once.

The code is in [`rain/belief.py`, `rain/ladder.py` and `rain/record.py`](https://github.com/act65/rain/tree/main/rain), and the experiments in [`experiments/`](https://github.com/act65/rain/tree/main/experiments) (`bayes_decay`, `strategic_borrower`, `first_loan`, `collusion`, `vouching`, `graduation`, `guarantor_exit`, `patient_ring`).
