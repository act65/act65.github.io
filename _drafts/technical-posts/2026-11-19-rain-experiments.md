---
title: Testing the Rain protocol
subtitle: What we want from a reputation system, and how we checked
layout: post
permalink: /rain-experiments/
categories:
    - research
description: "What we want from a reputation system, and the tests and experiments used to check whether Rain delivers it."
takeaways:
  - "Reputation valued by its dividends cannot be good collateral: it must be worth less than it costs or it can be farmed, and the two are the same ratio."
  - "What deters default is losing your place on a ladder of loans you would have to climb again. Dividends are a small part of the cost that is occasionally decisive."
  - "Three rules give reputation a stable value below its cost at all times: a fixed price per point, decay, and fees paid out at the decay rate."
  - "A record is cheap to fake, so it is worth what the reader's trust makes it, and to a stranger what it cost in fees. A newcomer starts on a guarantor's standing and outgrows it."
tags:
  - research
  - trust
  - incentives
  - mechanism-design
  - economics
  - simulation
---

[Rain]({{ site.baseurl }}/rain/) is a public log of promises and a reputation earned by keeping them. This post is about whether it works: what we want from it, how each aim was turned into something that could fail, and what happened. The code, with every experiment's predictions and outcomes, is [here](https://github.com/act65/rain/tree/main/experiments).

The result to remember is this. **Reputation that is valued by the fee income it earns cannot be good collateral, and should not be. What deters default is losing a place on a ladder of loans that would have to be climbed again.** The protocol's job is to keep the record true and to make every line of it cost something. What a line is worth as evidence depends on who is reading: a lender who trusts the counterparty can take it at face value, and one who trusts nobody can take it for what it cost.

{% assign n = site.data.rain %}

## What we are aiming for

Five properties, each stated so that an experiment could contradict it.

1. **Reputation cannot be bought at a profit.** Two colluding accounts can trade empty promises. The reputation they earn must be worth less than the fees they pay, always.
2. **Reputation has a stable value.** If nobody can say what a point is worth, losing it is no threat.
3. **Defaulting costs more than it gains,** at loan sizes people would want.
4. **A new identity gets nothing for free,** so that walking away from a bad record is not costless.
5. **Reputation follows what people do,** not how early they arrived or how large they are.
6. **A record cannot be manufactured at a profit,** and a newcomer still has somewhere to start.

## How we tested

Three layers, each checking the one above it.

- **The contracts** have a conventional test suite: every rule, every permission, and a randomised test that the ledger always agrees with a few lines of arithmetic.
- **A model of the protocol's accounting** in plain Python, with no blockchain. One scenario (a repayment, a default, a reward lost to delinquency, decay, a settlement, two rounds of fee payouts) is replayed through both the contracts and the model, and they must agree to nine decimal places. The model is what makes large simulations cheap.
- **Experiments** run on the model. Where a result can be worked out on paper it is, and the simulation is an independent check of the formula.

Each experiment's predictions were written down, with numbers, before it was run. Each has a control that must fail: for example, with worthless reputation every loan should be defaulted on, and it is. Of {{ n.predictions_total }} predictions, {{ n.predictions_held }} held, {{ n.predictions_partly }} held in part, and {{ n.predictions_wrong }} were wrong. Several of the wrong ones are the most useful results below.

## Aim 2 first: a stable value needs an anchor

The first design set the fee with a *keeper*: a bot that priced the fee at one and a half times the value of the reputation a kept promise earned, with that value estimated from recent payouts. It satisfied aim 1. A kept promise was worth at most {{ n.keeper_max_value_over_fee }} of its fee.

But payouts came only from fees, and the fee was priced from payouts. Nothing in that loop is fixed, and the level drifted to zero.

![The fee under the original keeper falls from 0.1 to almost nothing]({{ site.baseurl }}/assets/rain/keeper-fee.svg)

*The fee in the first design. The keeper's first update cut it from 0.1 to {{ n.keeper_fee_after_first_update }}, and it kept falling as reputation was issued.*

Farming was unprofitable only because both sides of the inequality were heading to zero. Two changes fix this.

- **A fixed price per point.** The fee is a percentage of the amount promised, and a kept promise earns `fee / κ` points, where `κ` is set from outside. There is no keeper.
- **Decay.** Every period all reputation shrinks by a fraction `δ`. Supply then settles where new points replace faded ones, instead of growing for ever.

If fees are paid out to holders, a point that cost `κ` earns `κδ` per period once supply has settled, and to someone who discounts the future at rate `r` it is worth

$$ v = \kappa \, \frac{\delta}{r + \delta} . $$

That is less than `κ` whatever the parameters. With `δ` = 3% and `r` = 5% a point is worth {{ n.steady_value_over_cost }} of its cost. Aims 1 and 2 are met together, with nothing to tune.

## Paying fees out: when, not just how much

The formula holds once supply has settled. Before that, and after any sudden change in activity, it does not: fee income can jump at once, while the supply of points takes about `1/δ` periods to catch up. In between, the points that exist are too few for the money arriving, and each collects more than usual.

![Value of a point over its cost, for three ways of paying out fees]({{ site.baseurl }}/assets/rain/payout-designs.svg)

*The value of a point divided by what it cost, by the cycle in which it was earned, from an empty start and through a tenfold rise in activity at cycle 300. Value is measured with hindsight, which is why the curves rise just before the surge. Orange and green coincide after the start.*

Paying fees out as they arrive fails twice: at the start, where the first points are worth {{ n.asreceived_start }} times their cost, and at the surge, where the peak is {{ n.asreceived_surge_peak }}. An earlier fix, giving the treasury a starting allocation of reputation to dilute the first holders, repaired the start and not the surge ({{ n.genesis_surge_peak }}, above 1 for {{ n.genesis_surge_cycles }} cycles).

What works is to put every fee into a fund and pay out a fixed fraction of the fund each cycle, **the same fraction by which reputation decays**. Dividends and supply then respond to any change at the same speed, and their ratio does not move: {{ n.fund_start }} at the start, {{ n.fund_surge_peak }} through a tenfold rise, {{ n.fund_fall_trough }} through a tenfold fall. In steady state the fund pays out exactly what comes in, so this costs holders nothing.

Two alternatives were tested and set aside. Minting a fixed number of points per cycle also holds the ratio through a surge, but not through a one-off grant ({{ n.issuance_grant_peak }}), and it gives up the fixed price. Making new points wait before they earn works only with a long wait, which every honest newcomer pays for: a ten-cycle wait lowers a point's value to {{ n.vesting10_steady }} of its cost and still lets the surge reach {{ n.vesting10_surge_peak }}. The release rate matters: at ten times the decay rate the surge is back to {{ n.fund_fast_release_peak }}.

## Aim 3: a bond is weak collateral, by design

How large a loan can a bond of reputation secure? A borrower who defaults loses the bond, and the bond is worth `v` per point. So a point backs about `v` of credit, which is {{ n.point_value }} DMD at the demo's parameters. Being trusted with a loan on the strength of a bond alone therefore costs {{ n.fees_per_unit_credit }} times the loan in fees. The second loan in the protocol's own demo is {{ n.demo_oversize }} times larger than its bond makes safe.

This cannot be tuned away. The ratio {{ n.fees_per_unit_credit }} is `(r + δ)/δ`, the reciprocal of the ratio in the previous section. Reputation is hard to farm because a point is worth less than it costs; a bond is weak for exactly the same reason. Lenders who ignore this and lend against the score can be robbed: at the demo's lending ratio an identity that buys its reputation and defaults nets {{ n.bought_identity_naive }} DMD, and the profit per identity does not fall as the attack is repeated.

So the bond is not what makes a loan safe.

## What a default really costs

Reputation would be used for credit the way microfinance uses a track record: each loan a little larger than the last one repaid. Take a ladder starting at 100 DMD, growing 5% per loan to a cap of 5,000. A borrower who defaults on loan number `n` keeps the amount due. They lose three things:

- the **dividends** on the reputation destroyed;
- **access**: the value of carrying on up the ladder, less the value of their best alternative;
- anything else their standing gave them, such as a role that requires it.

The alternative is what matters most. If the defaulter is shut out for good, access is their whole future on the ladder. If they can return under a new identity, it is only the gap between their rung and the bottom.

![Gain from default by loan number, for three cases]({{ site.baseurl }}/assets/rain/default-by-rung.svg)

*Net gain from defaulting on each loan, as a fraction of the amount kept. Below the line, repaying is better. The account behind the chart agrees with a simulation of both strategies to within {{ n.account_error }} of the amount kept.*

- **Access is most of the cost.** On loan 40 ({{ n.r40_loan }} DMD), a borrower who gains 3% per loan and would be shut out loses {{ n.r40_dividends }} DMD of dividends and {{ n.r40_access }} DMD of access.
- **Whether a defaulter can start again matters more than any parameter of the reputation rules.** At a 3% gain, default does not pay on loans {{ n.shut3_safe }} if they are shut out, and only on loans {{ n.again3_safe }} if they can start again. Starting again costs exactly the climb, so a ladder protects its upper rungs and not its first ones.
- **A ladder stops protecting when it stops growing.** At the cap, staying is worth {{ n.cap_stay_value }} DMD to that borrower and leaving is worth {{ n.cap_kept }}.
- **Dividends are small and occasionally decisive.** They are {{ n.dividend_share_r40 }} of the loss on loan 40 and {{ n.dividend_share_cap }} at the cap. In the 6% case with restart, default pays on first reaching the cap (a gain of {{ n.again6_gain_at_81 }} DMD on loan 81) and stops paying a few loans later (a loss of {{ n.again6_gain_at_120 }} DMD by loan 120). The loan is the same size throughout. The only thing that changed is that the borrower's reputation grew, from {{ n.again6_dividends_81 }} to {{ n.again6_dividends_120 }} DMD of dividends at stake. This is the job the dividend was designed for.

How much a lender should advance is the lender's business, and none of this is built into the protocol. What the protocol contributes is the record the ladder is read from, and a cost for every line of it.

## Aim 4: a new identity gets nothing

Under the first design every new identity was given starting reputation. An identity created to attack extracted {{ n.free_identity_naive }} DMD from a lender lending against the score, and {{ n.free_identity_careful }} DMD even from a careful one. Now an identity starts with nothing and can bond nothing. The fee is the price of an identity's record, and the only one.

That leaves the first rung. The ladder chart shows the first loans are unprotected whenever a defaulter can start again. Aim 6, below, is about what can be done there.

## Aim 5: who ends up holding reputation

Two hundred agents, with loan sizes spread over two orders of magnitude, half of them arriving late, a fifth of them defaulting on one loan in ten.

| | fades 3% a period | fades 0.5% | never fades |
|---|---|---|---|
| Late arrivals' standing against early ones, after ~150 periods | {{ n.late_400_d03 }} | {{ n.late_400_d005 }} | {{ n.late_400_d0 }} |
| ...after ~550 periods | {{ n.late_800_d03 }} | {{ n.late_800_d005 }} | {{ n.late_800_d0 }} |
| Standing of agents who default one time in ten | {{ n.unreliable_d03 }} | {{ n.unreliable_d005 }} | {{ n.unreliable_d0 }} |

*Standing is an agent's share of reputation divided by their share of activity. Means over five seeds.*

- **Arriving late is forgiven at the decay rate.** Without decay it never is.
- **Size does not compound.** The largest tenth of agents hold {{ n.top_tenth_reputation }} of the reputation and {{ n.top_tenth_activity }} of the activity; inequality of reputation equals inequality of activity ({{ n.gini_reputation }} against {{ n.gini_activity }}, Gini).
- **Behaviour is what separates people.** An agent who defaults one time in ten gets {{ n.unreliable_dividends_over_fees }} of their fees back in dividends. A reliable one gets {{ n.reliable_dividends_over_fees }}: for them the fee is close to a deposit, returned as their reputation fades.
- **The decay rate is also the forgiveness rate.** Slower decay makes a bad record last, which is a reason not to make it very slow.

## Aim 6: the record, and where a newcomer starts

The derivations behind this section are in [Reputation as a belief]({{ site.baseurl }}/reputation-as-belief/). Here are the tests.

**Faking a record.** Two colluding accounts pass a loan back and forth. Each round costs {{ n.wash_cost }} of the amount: the fee, less the part that returns as dividends. A lender who reads the whole log as evidence is robbed without limit. After one wash of 10,000 it accepts {{ n.naive_bank_due }} and loses it. The control (a lender that believes everything must lose) failed as it should.

**Reading a record.** A reader weighs each kept promise by its trust that the counterparty was independent of the promisor.

- With no trust in counterparties it does not know, a lender gains the attacker nothing; their best move is not to bother.
- Partial trust is worth little in either direction. One half-trusted confederate raises the loan by a factor of {{ n.half_trust_multiple }} at most. And an honest borrower who repaid 10,000 to another lender is offered {{ n.portable_99 }} by a lender who trusts that one at 99%, against {{ n.portable_full }} at full trust.
- Many identities are the danger. Twenty, each half-trusted, take {{ n.sybil20_multiple }} times a stranger's loan, unless the lender knows they are one group.
- The fee buys a margin. We predicted that any trust in unknown counterparties could be exploited with enough identities. It cannot: below about {{ n.safe_trust_ratio }} times the fee rate, the fees on the fake loans exceed the take.

**The first loan.** A search over every sequence of loan sizes, for a lender facing strangers of whom some take the first loan and vanish.

- The first loan is made at an expected loss. With 20% vanishing, the best first loan is {{ n.first_due_20 }} where everyone genuine is good for 100. It expects to lose {{ n.first_alone_20 }}, and the stranger is worth {{ n.first_value_20 }} overall.
- The lender then raises each loan by the interest rate until it reaches what the borrower is known to be good for, and not beyond. The ladder of the earlier section is such a climb.
- A lender that accepts a fixed 10% risk on every loan, which earlier experiments here assumed, loses {{ n.risk_ladder_value }} per stranger. Their conclusions concern the borrower and do not depend on it.
- If those who vanish can return under a new name, the first loan is at most what a new identity costs. With free identities it is nothing.

**A guarantor.** So a newcomer needs someone to answer for them. A second reference script records a guaranteed loan as two promises, the borrower's to the guarantor and the guarantor's to the lender. If the borrower defaults, the claim on them passes to the guarantor, who pays the lender or becomes its defaulter. The newcomer borrows 10,000 on the first day.

- A guarantee counts against the guarantor's own credit. Then a guarantor who lets twenty guaranteed loans default takes {{ n.vouch_burn_loss }}, one loan's worth. Without that rule it is {{ n.vouch_burn_loss_uncounted }}.
- A guaranteed repayment is a promise kept *to the guarantor*, so a lender who trusts only its own dealings learns nothing about the borrower from it. A lender who counts it loses {{ n.vouch_naive_gain }} per fake borrower.
- A vouch for 10,000 costs the guarantor {{ n.vouch_cost_sure }} if they are sure of the borrower and {{ n.vouch_cost_10 }} if they think there is a one in ten chance of an opportunist.

**Outgrowing the guarantor.** A lender who trusts nobody can still use a record, for what it cost. It accepts, unsecured, the smaller of the largest amount the borrower has repaid to anyone, and `(1 + interest) × the largest repaid to itself + fees sunk since`.

- Of {{ n.graduation_strategies }} strategies for a ring (guaranteed loans or washes, of three sizes, once or every cycle, defaulting on any of the first 61 loans), none beats simply taking a stranger's loan.
- Each of the rule's three parts is needed. Dropping one costs the lender up to {{ n.graduation_control_loss }}.
- An honest newcomer borrowing 10,000 a cycle needs no guarantor from loan {{ n.graduation_cycles }}.
- To a lender who knows nothing else, a point of reputation is worth {{ n.credit_per_point }} DMD of unsecured credit. Beside a share of fees and a standing to lose, reputation is a receipt for cost.
- The rule assumes a ring is no more patient than the lender. Fees return over time as dividends, so a ring that discounts at 4% where the lender assumed 5% gains {{ n.patient_gain_4 }} of the fees it pays, and one that does not discount at all gains {{ n.patient_gain_0 }}. Crediting nothing for fees is safe against any ring; each loan then grows only by the interest rate, and the newcomer needs the guarantor for {{ n.graduation_cycles_zero }} loans.
- A lender gives something up by letting the guarantor go: {{ n.lender_loss_from_graduating }} of what the newcomer is worth to it, at equal interest. At {{ n.unsecured_rate_lender }} on the unsecured part it is indifferent, and the borrower prefers graduating up to {{ n.unsecured_rate_borrower }}.

**Where thresholds come from.** The lender's model above takes it as given that a borrower repays up to a private threshold. A borrower who weighs repaying against keeping the money produces the same behaviour. They repay a loan that will be offered again when their net return on it is at least {{ n.return_threshold }}, whatever its size, and their threshold is their capacity to use the money, scaled ({{ n.capacity_ratio_15 }} times it at a 15% return). Those below that return are the ones who vanish. The borrowers assumed in the ladder section, at 3% and 6%, are all below it, which is why they default when the ladder stops growing.

## One more: the oracle

Reputation is computed off-chain by an oracle that reads the log. If it runs `L` periods late, established honest users are unaffected and newcomers receive everything they earn `L` periods late, a loss of {{ n.lag1_newcomer }} per period of lag at these rates.

The experiment also found a rule nobody had designed. A reward was refused if its earner was delinquent *when the oracle ran*, so promises kept honestly just before a default went unrewarded if the oracle was slow, and the size of the penalty depended on the oracle's schedule. Rewards are now decided by the earner's status at the moment the promise was kept.

## What this does not show

- **The numbers that matter most are inputs.** How much a borrower gains from a loan, and how they discount the future, are assumed. The conclusions are about which way things move and where the thresholds are.
- **Activity is exogenous.** Nobody in the simulations borrows more because they hold reputation, and no lender rations credit by it. If they did, arriving early could matter again.
- **Shocks are steps.** Gradual growth in activity was not tested; it should be easier than a step.
- **Identity is assumed away or assumed free.** The truth is in between and outside the protocol.
- **How borrowers differ is assumed.** How capacities and returns are spread among borrowers is an input to everything in aim 6 except the last rule, which needs neither.
- **One lender, no competition.** A rival could wait for the first lender to pay for the information and then poach the survivors. How the gain from graduating is split is not determined either.
- **Settlement after default is not modelled.** A defaulter who pays the debt and returns as themselves is treated as never returning.
- **The dividend to defaulters.** A default costs the bond and a mark on a second counter that readers can see. It no longer takes any other reputation, so a defaulter keeps the dividends on what was not bonded.

## Reproducing it

```
uv sync
uv run ape test                                       # contracts, model, and model-against-contracts
uv run python experiments/standing_value/run.py      # any experiment; each writes its own results
uv run python experiments/blog/make_assets.py out/   # the charts and every number quoted here
```

Every number in this post is read from a file that the last command generates (commit `{{ n.commit }}`).
