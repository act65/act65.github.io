---
title: The Geometry of Governance
subtitle: Voting as a compression problem, and the right to be heard
layout: post
categories:
    - economic
description: "A ballot is a recording device, and most ballots are too narrow to record what voters want. The opinions lost are those of small groups whose views cut across the main dividing line."
takeaways:
  - "A ballot can only record so much: with three yes/no issues there are eight positions, and a two-party ballot names two of them."
  - "Neither two parties nor issue-by-issue voting is universally right: the ballot should bundle issues that travel together and separate those that don't."
  - "The voters a narrow ballot fails to record are predictably the small groups whose mix of views cuts across the main dividing line."
tags:
  - essay
  - aggregation
  - abstraction
  - rights
  - mechanism-design
  - politics
revisions:
  - "2026-02-15"
  - "2026-05-25"
  - "2026-08-15"
---

Before a voting system can add up what people want, it has to record what they want. The ballot is the recording device, and it can only hold so much. When it holds less than the electorate's range of opinion, the people it fails to record are not a random sample. They are the small groups whose mix of views cuts across the main political dividing line. This post outlines that argument and what I'll call the right to be heard: everyone should be able to cast a vote that says what they mean.

The outline treats every issue as a yes-or-no question that all voters care about equally, and assumes people vote sincerely. Real opinion is messier on all three counts, and each one makes the recording problem harder. The formal version, with a method for designing ballots from voting data, is in the paper [Ballot Structure from the Preference-Dependency Graph](https://doi.org/10.5281/zenodo.20819571).

## A cube of opinions

Take three yes-or-no questions: lower taxes? cut welfare? restrict immigration? There are eight ways to answer all three, and they can be drawn as the eight corners of a cube. Each corner is a different political position.

![]({{site.baseurl}}/images/voting-cube.png)

> Three yes/no issues make a cube with eight corners. A two-party system names two of them. A voter standing on any of the other six has to pick whichever named corner is closer.

A two-party ballot lets a voter say one of two things. If the whole country stands on two opposite corners (everyone is yes-yes-yes or no-no-no), nothing is lost and two parties are the right design. If people are spread around the cube, six of the eight positions have no name. Someone who wants low taxes, little welfare and open borders cannot say so. Whichever box they tick endorses something they oppose, and their disagreement is not recorded anywhere.

## Two repairs that don't work

**More parties.** Three issues need eight parties to name every corner. Ten issues need about a thousand, and thirty need about a billion. Coalition governments help a little, because the programme a coalition negotiates need not be any one party's platform, but voters do not control the negotiation.

**Voting on every issue separately.** Now every corner can be expressed, but opinions on different issues are often tangled. I might support raising targeted benefits unless a universal basic income is on offer, in which case I want that and not both. Two separate questions cannot record the "unless". The result can be a package that no voter wanted. Suppose three groups each want exactly two of three proposals, a different pair for each group. Each proposal then has majority support, all three pass, and the outcome is one that nobody voted for. This is the paradox of multiple elections.

## Match the ballot to the electorate

Each familiar design fits one kind of electorate. Two parties fit a country split along a single line. Issue-by-issue voting fits a country where every opinion is independent of every other. Real electorates probably sit in between, with some issues that move together and others that don't.

A ballot can follow that shape: bundle the issues that move together, and ask separately about the ones that don't. Suppose views on tax, welfare and public healthcare come as one package, views on drugs, immigration and surveillance come as another, and the two packages are unrelated. Then two questions record what would otherwise take six questions or four parties.

The difficulty is that designing such a ballot requires knowing how opinions are tangled, and the ballot is the main instrument for finding out. A two-party ballot returns two-party-shaped data.

## The right to be heard

A ballot that is too narrow loses the opinions furthest from the options on offer. Any group large enough to be worth a party will tend to get one, so the people left unrecorded are those in small groups whose views cut across the main dividing line. A voter who says "no party represents me" may be describing where they stand on the cube.

Whether a ballot looks adequate depends on whether one counts the average voter or every voter. If ninety-nine people in a hundred agree, a two-option ballot is more than enough on average, and it still offers nothing to the hundredth. A ballot sized for the average voter has settled in advance who goes unrecorded.

The right to be heard is the stricter standard: the ballot should have an option for every position that anyone holds. It is not a right to get one's way. A minority that is recorded perfectly can still lose every vote, and how to weigh opinions once they are recorded is a separate question. Recording comes first, though, since a system cannot weigh what it has not recorded.

## Further reading

- [Ballot Structure from the Preference-Dependency Graph](https://doi.org/10.5281/zenodo.20819571) (Zenodo). The paper estimates how issues are tangled from agree/disagree votes, builds the matching ballot, and measures who bears the loss when the ballot has to be kept small.
- [A short post introducing the paper]({{site.baseurl}}/ballot-design/), with links to the code.
