---
title: "A guide to regulation"
date: "2017-10-31"
coverImage: "admin-1.jpg"
layout: post
---

![]({{site.baseurl}}/images/{{page.coverImage}})

(Disclaimer: I have no experience in regulating anything other than the amount of time I spend on youtube - and I almost never meet my targets...)

In my mind, regulation is the (or a?) solution to externalised costs. Because petrol produces CO2 and particulate matter (which effect our climate and our health and cost $$$ bills to fix) the cost of petrol should incorporate these costs to ensure fair competition (why is this important -- need better motivation?).

There are a couple of problems that occur when trying to regulate these external costs; we have no ground truth for the magnitude of the costs for these external costs, we don't always know the external costs before (or even years after) a product is sold/operated.

When we try to quantify how large these costs actually are, we don't have an authoritative ground truth. The sellers of petrol have large incentives to debate the evidence (and even manipulate it) as they will surely make large(r) amounts of money, and it is entirely reasonable for them to spend large amounts of money to influence .

### Measure the world

Often the problem isn't even that we don't have an authoritative ground truth, but that we just don't have any data at all. For example, to fairly regulate run-off (from dairy farms -- a contentious policy in NZ) we would need to measure the run-off in multiple locations on each farm, that is a lot of sensors!

In my mind there are two approaches that the government could take gathering this data, but both require large amounts of sensors that would send data to the cloud, like some internet-of-things platform. (1) Be unfair and pessimistic by default. By default apply a flat tax that is priced waaay too high (an order of magnitude), but if a farmer can sufficiently prove that their run-off is approximately X, then we can tax them on X.  (but they have an incentive to cheat?? -- but that would be detectable assuming we could get a baseline) (2) The more common approach (why?) seems to be that the government funds the measurement of the run-off. This costs them large amounts of money, takes time to set up and has little buy-in from the farmers.

Another new technology that can help us measure the previously unmeasured is machine learning. For example, wind turbines are thought to kill many birds and this cost to the environment should be incorporated (via tax) into the power they supply. How can we count the number of birds killed? We could get a person to sit at each of the turbines and look out for such killings, however that would be very costly. Machine learning gives us the ability to learn a classifier that might receive audio and vibrations and predict if a bird has been killed. Given the right training data I would expect that we could achieve high classification accuracy, thus giving us a way to cheaply scale (just a couple of sensors) the measurement of bird deaths caused by wind turbines.

Blockchain could be used to securely keep track of manufacturing processes and distribution chains. This sort of tool seems like it would independently useful for shipping companies (a secure/verifiable ledger of their inventories). If we knew; where the materials were mined to make the product, the exact vehicle used to transport the product, ... then we could start to think about fairly taxing most products.

The benefits of these approaches are that they give us data. Data is hard(er) to argue with, and as much as companies might try to lobby for their interests (less tax), we would have the evidence to back up the taxation rates.

### Retrospective tax

(now for the more ambitious idea) Back in the 1900s when we first started selling coal we didn't understand the effects that it would have on the environment or our health. But now, we are starting to understand the magnitude of carbon based fuel's costs.

So after years of making obscene amounts of money from selling carbon based fuels (partially due to their large, unaccounted for, external costs), we would really like to be able to retroactively apply tax on all the sold fuel. I believe this would be possible if we recorded all transactions/purchases in a blockchain (I haven't worked any details yet).
