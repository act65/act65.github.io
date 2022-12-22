---
title: "#Apaperaday. Week 1"
date: "2018-08-05"
layout: post
---

![]({{site.baseurl}}/images/{{page.coverImage}})

https://twitter.com/telfarac/status/1024546114127556608

<blockquote class="twitter-tweet"><p dir="ltr" lang="en"><a href="https://twitter.com/hashtag/apaperaday?src=hash&amp;ref_src=twsrc%5Etfw">#apaperaday</a> 2. <a href="https://t.co/xAKtVwRvKf">https://t.co/xAKtVwRvKf</a> Construct a 'scene' representation (using context) and use it to condition a generative model. These ideas are not new, but integrating them in model that works on complex envs is new.</p>— Alexander Telfar (@telfarac) <a href="https://twitter.com/telfarac/status/1023832947139309568?ref_src=twsrc%5Etfw">July 30, 2018</a></blockquote>

<blockquote class="twitter-tweet"><p dir="ltr" lang="en"><a href="https://twitter.com/hashtag/apaperaday?src=hash&amp;ref_src=twsrc%5Etfw">#apaperaday</a> 3. <a href="https://t.co/URpaQusdLD">https://t.co/URpaQusdLD</a> Expected Info + Guassian process + constrained optimisation + noise + distributed + cts variables.</p>I am not confident I understood the contributions of this paper. GPs still confuse me.<div></div>— Alexander Telfar (@telfarac) <a href="https://twitter.com/telfarac/status/1024195890699849730?ref_src=twsrc%5Etfw">July 31, 2018</a></blockquote>

<blockquote class="twitter-tweet"><p dir="ltr" lang="en"><a href="https://twitter.com/hashtag/apaperaday?src=hash&amp;ref_src=twsrc%5Etfw">#apaperaday</a> 4. The Emergence of Organizing Structure in Representations - <a href="https://t.co/u4YWvQVdbC">https://t.co/u4YWvQVdbC</a>. Great question: How can you learn struct representations of struct data? Hard because; - we often want to recover the true struct - variable sized struct - discrete choices - ???</p>— Alexander Telfar (@telfarac) <a href="https://twitter.com/telfarac/status/1025289934901395457?ref_src=twsrc%5Etfw">August 3, 2018</a></blockquote>

<blockquote class="twitter-tweet"><p dir="ltr" lang="en"><a href="https://twitter.com/hashtag/apaperaday5?src=hash&amp;ref_src=twsrc%5Etfw">#apaperaday5</a>. Equilibrium propagation - <a href="https://t.co/358Vm8lOUX">https://t.co/358Vm8lOUX</a>. Instead of AD to calculate derivatives, they can be approx with a finite difference of SS solutions. This removes the need for a dedicated set of 'backward' connections (famously not present in the brain).</p>— Alexander Telfar (@telfarac) <a href="https://twitter.com/telfarac/status/1025498533216972800?ref_src=twsrc%5Etfw">August 3, 2018</a></blockquote>Ok, five papers down, a thousand to go...

### This weeks [pick](https://arxiv.org/abs/1801.02144)

![Screenshot 2018-08-05 at 1.48.56 PM.png]({{site.baseurl}}/images/screenshot-2018-08-05-at-1-48-56-pm.png)

(_picked as the paper I want to spend more time understanding, not necessarily the best_)

Why do we care?

> Graph learning is not the only domain where invariance and multiscale structure are important: the most commonly cited reasons for the success of convolutional neural networks (CNNs) in image tasks is their ability to address exactly these two criteria in the vision context

Ok, that makes sense to me. So, what is their contribution?

> MPNNs deal with the permutation invariance issue in graphs simply by summing the messages coming from each neighbor. In this paper we argue that this is a serious limitation that restricts the representation power of MPNNs.

## Background: Invariance

Given a function `f: X -> Y`, and a transform `t: X -> X`.

- Invariance ​​`f(x) = f(t(x))`.
- Equivariance `t(f(x)) = f(t(x))`
- Steerability `t(f(x)) = f(R(t(x)))`

Such that `R` is some reversible function `R: X -> X` (this paper restricts `R` to be linear)

 

![Screenshot 2018-08-05 at 12.42.17 PM.png]({{site.baseurl}}/images/screenshot-2018-08-05-at-12-42-17-pm.png)

Ohh! You cannot have both, translational and rotational invariance in a CNN.

> if we rotate the input image by, e.g., 90 degrees, not only will the part of the image that fell in the receptive field of a particular neuron n \`i,j move to the receptive field of a different neuron n\` j,−i , but the orientation of the receptive field will also change (Figure 4). Consequently, features which were, for example, previously picked up by horizontal filters will now be picked up by vertical filters. Therefore, in general, f 0\` j,−i 6=f \` i,j . It can be shown that one cannot construct a CNN for images that behaves in a quasi-invariant way with respect to both translations and rotations unless every filter is directionless.

Functions on graphs should be invariant to the labelling/numbering/ordering of the nodes.

## Quasi-invariance

> Quasi-invariance in comp-nets is equivalent to the assertion that the activation fi at any given node must only depend on Pi = {ej1 , . . . , ejk} as a set, and not on the internal ordering of the atoms ej1 , . . . , ejk making up the receptive field. At first sight this seems desirable, since it is exactly what we expect from the overall representation φ(G). On closer examination, however, we realize that this property is potentially problematic, since it means that ni has lost all information about which vertex in its receptive field has contributed what to the aggregate information fi. In the CNN analogy, we can say that we have lost information about the orientation of the receptive field. In particular, if, further upstream, fi is combined with some other feature vector fj from a node with an overlapping receptive field, the aggregation process has no way of taking into account which parts of the information in fi and fj come from shared vertices and which parts do not (Figure 5).

Not convinced! According to them, we need to be able to distinguish f maps from different levels of the hierarchy. Where did this problem come from?

By using composition schemes we allowed connections between non-successive layers. Thus an aggregation fn might have inputs from many different layers of the hierarchy. But is this a problem?

![Screenshot 2018-08-05 at 12.55.21 PM.png]({{site.baseurl}}/images/screenshot-2018-08-05-at-12-55-21-pm.png)

For a linear aggregation fn: if `f` is the sum of its inputs then we have `f(f(a, b), f(c, d)) = f(f(a), f(b,c,d)) = ...` . But this isn't true in the non linear case, so...?

But residual nets allow different layers of a CNNs hierarchy to be composed irreversibly and they dont seem to suffer any reduction in representational power!? What is the deal??

**Q:** But why does invariance to the hierarchy matter?

If two features have the same receptive field then they will have the same activation. Meaning that at the highest level of the hierarchy there is zero variance in each feature.

**Q:** So how does this actually effect the representational capacity? I want more details.

### Possible solutions

(_to a problem that might not be a problem???_)

1. use ordered sets to represent P\_i,
2. use non linear functions,
3. use different aggregation fns per layer and/or input the level of the hierarchy to the aggregation fn (aka allocate some dims of the feature representation to encode info about corresponding levels in the hierarchy)

The authors choose solution (1), which leads them to...

### Covariant networks

`1. Collect children of the composition scheme for the given node 2. Reorder fmaps into a consistent basis using permutations 3. Stack fmaps into a k+1-tensor 4. Propagate info using the relevant edges 5. Contract along some dimensions and mix 6. Return nodes fmap`

So if a single permutation (used in a first order covariant net) allows you to rename all the nodes (as it is a representation of S\_n) then what does the composition of two permutations allow (P x P)? Oh, it allows us to generalise to higher dimensional inputs, such as k-tensors. Ok, fine. Being able to handle high dim data is nice.

Why do we want to take a mixture of various contractions (/aggregations) of a tensor? Not really sure, I dont have any good intuition. In a CNN this might mean pooling over space versus pooling over features? Reminds me of [this article](https://distill.pub/2018/building-blocks/) (img below).

![Screenshot 2018-08-05 at 9.02.47 PM.png]({{site.baseurl}}/images/screenshot-2018-08-05-at-9-02-47-pm.png)

Yea, and they get some results. Meh. It is hard to interpret them as they do not give confidence intervals or comparison between amount of computational resources used. It's unclear whether I should care...

### Questions

- What are the fns that an invariant MPNN cannot represent?
- Where does the composition scheme come from, how can it be computed?
- Still a bit confused about tensors that "transform in a specific way" as according to permutation matrices. Todo.
- Why do we care about steerabilty and quasi-invariance? How are they useful?

## Thoughts

The original goal was to build multi-scale and invariant representations. Has that been achieved?

Yea? The multi-scale part of a CCN was the composition scheme which was abstracted away. And the invariant part was loosened to steerability (in which it's utility is still unclear to me).

## Next time

There seems to be a subtle art to doing this well. I want to try adding more structure to my tweets;

1. a compressed summary
2. why do we care? the motivation.
3. which parts are interesting? key insights/contributions
4. questions
5. future work

To try add some photos and equations.
