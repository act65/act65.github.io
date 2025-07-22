---
title: How can you enforce imperfect rules?
subtitle: 
layout: post
---

(think laws or smart contracts)

Issues with counter-party trust.
How can you verify the promise state (pending, fulfilled, defaulted) in a relaible / trustworthy way?

***

The problem: contracts are partially specified. 
For any real world implementation details will be missed.
This means...?

***


Let's frame this as;

- a blockchain to record state,
- a trusted virtual machine to exectue smart contracts,
- ??

There are a set of possible world states.
The contract should specific the outcome (promise fulfilled vs defaulted). Because the contract doesn't specific the outcome label for all states (partial specification), some states will lead to dispute and / or unfair losses for either side.

We have;
- a promisor
- a promisee
- a 3rd party reporter (takes offchain data and writes / reports the data onchain)

<!-- sure. 
this seems ok?
if we pin the contract to a specific piece of offchain code (how???) then this could work? however, this is the high specification cost setting.

for lower specification cost we can rely on bonds and markets?
 -->


***

Let's walk through a simple example;

Alice is purchasing a bicycle from Bob.
The contract is as follows;

```solidity


```

But! 

- what IS a bike?
- how can we confirm that Bob delivered the bike / Alice has recieved the bike? (issues with trusted data!)

***

Another example;

something from finance?


***

Something like minimise   p·D + r·C?


p = probability of landing on an unlabelled state. (the distribution over states would be unknown to each party?)
D = 

***


Solution space;

- bonds / collateral,
- specificity of the contract, (costs gas)
- markets? (to estimate p?)

