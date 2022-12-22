---
layout: post
title: Policy search engine
---

Typical smart city solutions seem to focus on gathering __evidence for/of problems__, i.e. measuring built and social environments. This is useful as it can motivate action and change. However, this problematic data does not help us solve the problems once identified. For this we need __evidence for/of solutions__. How have past policies changed cities? Which policies seem to work? Which policy would be most effective/efficient in this case?

These questions are notoriously hard to answer (_because people don't like being experimented on, because experiments take many years, because there are enormous amounts of uncontrolled variables_). Thus the question becomes; what do we need to answer these questions? In the ideal case we would have a dataset relating; all policies ever implemented, and measures of every variable possible, controlled and uncontrolled (social, environmental, political, economic, ...).

Smart City tech is mostly working towards measures of environmental, economic and some social variables. However, the missing piece is a platform that serves queries about past policies.

__Proposal__: build a search engine that indexes local council and national government policies by:

* the locations they apply,
* the dates they apply,
* the problem they are attempting to fix,
* the type of solution they implement,
* the cost to the council/govt (and it's people),
* the 'success' of the solution.

I imagine a few use cases (need some help here);

1. You want to reduce the traffic in the central city, but are unsure about how to proceed. You have been collecting data on traffic patterns in many cities for years. Using the policy search engine, you can easily find all transport related policies implemented in the cities you have traffic stats on. It turns out that the latest intervention in public transport preceded -- by 2 weeks -- a large increase in public transport use.
* Browsing past polices for inspiration and soft validation. (You could "test drive" a new policy by examining how other cities/governments are trying to solve similar problems.)
* Meta-analysis. Because you know certain `similar` policies correlate with certain outcomes (with a p-value of XX and a sample size of ~100 cities) you can be more confident in applying the policy to achieve that outcome.

A proof of concept could be a search engine that serves queries based on location, date and a class of policy domain -- e.g. public transport.

***

This concept seems feasible as:

* Many cities policies are openly available and collected on their websites. For example; Wellington, Auckland, Syndey.
* Building search engines is not new
* Natural language processing provides off the shelf tools for parsing keywords, entities, ...

Of course, there are some risks and uncertainties

* we do not control the data we are serving (google has a similar issue and solved it by downloading the internet...).
* each council policies are stored differently (different naming conventions, ... will need to automate parsing each one -- is this feasible?)
* the data held by councils may not accurately represent when action was taken on new policies (need to answer/find out how bad this is)
* it is likely there will be a bias towards positive results in the policies reported (not much can be done about that)

***

In the most ideal case we would align this with GDELTs API, thus allowing us to correlate;

* local/national policies (leverage the years of data we already have and experiments already done),
* news worthy happenings (correct for uncontrolled variables),
* the metric we care about.
