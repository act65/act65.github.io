---
layout: post
title: Convince Me, Teach Me Nothing
subtitle: How to prove you know a secret while revealing not one bit of it
categories:
  - play
---

Almost everything on this blog about records and power runs one way: whoever holds the ledger holds the truth, and to prove a fact you have to *show* it. [Ikram's tablet]({{ site.baseurl }}/math-origins) is authoritative because you can read the count off it. The [treaty]({{ site.baseurl }}/cargo), the manifest, the deed — proof means disclosure, and disclosure is the moment the powerful get to see your cards.

Zero-knowledge proofs break that link, and when I first understood how, it felt illegal. They let you prove a statement is true while revealing *nothing whatsoever* beyond the fact that it's true. Prove you know the password without transmitting the password. Prove your company is solvent without opening your books. Prove you're over eighteen without showing your birthday, your name, or anything else on the card. Convince me completely — and leave me no wiser about *why*.

### The cave

The standard story (Quisquater and Guillou, who wrote it up for children) is a cave shaped like a ring. At the back, where the two passages meet, there's a door that only opens for someone who knows the magic word. Peggy claims she knows it. Victor wants proof, but Peggy won't say the word — that's the whole point.

So: Victor waits at the entrance. Peggy walks in and picks a passage, left or right, out of his sight. Then Victor walks to the fork and shouts which side he wants her to emerge from. If Peggy really knows the word, she can always comply — if she's on the wrong side, she just opens the door and walks through. If she *doesn't* know the word, she can only come back the way she went in, so she has a 50% chance of being on the side Victor happened to name.

Once looks like luck. Do it twenty times and the chance she fools him every round by guessing is $2^{-20}$, less than one in a million. Victor walks away *convinced* Peggy knows the word.

And here is the magic: he has learned nothing about the word itself. Every single round, all he ever saw was Peggy walking out of the side he asked for. He could have predicted the entire experience in advance. He's certain, and he's ignorant, at the same time.

### The three demands, and the strange one

A zero-knowledge proof has to satisfy three properties:

1. **Completeness** — if the statement is true and both play honestly, the verifier is convinced.
2. **Soundness** — if the statement is false, a cheating prover gets caught with high probability (the $2^{-20}$).
3. **Zero-knowledge** — the verifier learns nothing except that the statement is true.

The first two are what any proof system needs. The third is the weird one, and the deep question is: what could "learns nothing" possibly *mean* formally? The answer is the most beautiful idea in the subject.

> **A protocol is zero-knowledge if the verifier could have produced the entire transcript by himself, alone, without the prover and without the secret.**

Think about the cave film. Suppose Victor records the whole thing — his shouts, Peggy strolling out the correct side, twenty times. That tape looks like ironclad proof. But Victor could *fake an identical tape* with an actress who knows no magic word at all: film a round, and every time she comes out the wrong side, delete it and re-shoot. Edit together only the lucky takes and you get a tape indistinguishable from the real one — twenty perfect rounds — produced with zero knowledge of the word. If a convincing transcript can be manufactured from nothing, then the transcript *contains* nothing. That's the definition: a proof is zero-knowledge when there exists a "simulator" that fakes real-looking transcripts without the secret. Knowledge you could have invented yourself is no knowledge at all.

### The bombshell: everything provable is provable this way

The cave is a parable. Here's a real one. Suppose I want to prove a map (a graph) can be coloured with three colours so no two touching regions match — without showing you the colouring.

I secretly colour it, then put a locked box on every region hiding its colour, and — the crucial move — I randomly *permute* which actual colour is which each time. You point at any one border. I unlock exactly the two boxes on either side of it. You check: two different colours. Good. We reset, I re-permute and re-lock, you pick a different border. Each round you learn only that *those two* regions differ — which tells you nothing about the global colouring, since the colours are freshly randomised every time. But if the map *weren't* properly 3-colourable, some border would have matching colours, and enough random probes would eventually catch it.

Now the punchline that made me sit down. Graph 3-colouring is **NP-complete** — every problem in NP can be re-encoded as one. So Goldreich, Micali, and Wigderson (1986) got, for free, a staggering theorem: **every statement that can be verified at all can be proven in zero knowledge.** Anything you could prove by showing your work, you can instead prove while showing nothing. Verification and disclosure, which looked welded together, come apart completely.

### Making it a thing you can hold

The cave needs Victor there, shouting. The Fiat–Shamir trick removes him: replace the verifier's random challenges with a *hash* of the prover's own commitments. A hash is unpredictable enough to stand in for a coin flip, so the prover can generate the challenges himself and bundle the whole exchange into a single string anyone can check later, with nobody live on the other end. That's what turns this from a chat into a **zk-SNARK** — a compact certificate you can post publicly. It's the machinery under private cryptocurrencies, under "rollups" that prove a million transactions were computed correctly without redoing them, under anonymous credentials that prove you're allowed in without saying who you are.

### The catch, and the vertigo

The honest caveats: the efficient versions are *arguments*, not proofs — sound only against an adversary without unlimited compute (they lean on cryptographic assumptions, on one-way functions existing). Some constructions need a "trusted setup" whose leftover randomness, if kept, could forge proofs. And zero-knowledge proves only the *statement* — it says nothing about whether the statement was worth proving.

But step back from the machinery and there's something genuinely dizzying here about knowledge itself. We usually assume that to make someone certain of a fact, you have to hand them the reason — that conviction and understanding travel together. Zero-knowledge proofs sever them. I can make you mathematically certain I'm right and leave you with no more insight into *why* than you had before. For a blog that keeps finding [the ledger holding all the power]({{ site.baseurl }}/math-origins), this is the one technology that flips it: at last, a way to prove the count is honest without ever showing the count.
