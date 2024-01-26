---
layout: post
title: How can randomness make algorithms faster?
subtitle: A brief introduction to randomised algorithms
---

- random quicksort
- miller-rabin primality test

<!-- https://eccc.weizmann.ac.il/report/2023/076/ -->

Randomised algorithms are algorithms that use randomness to solve problems. Can be 'faster' than deterministic algorithms, and sometimes they are the only (known) way to solve a problem.

<!-- probablistic polynomial time, Bounded-error probabilistic polynomial, randomized polynomial time.
unsolved. P = BPP? -->

General intuition:
in the worst case, the use of randomness limits the ability of an adversary to force a bad outcome. (since the adversary does not know the random choices made by the algorithm. what if i randomly choose between k different deterministic algorithms?)


# Examples

## Generating primes

Let's say we want to generate a random prime number. We could try to generate a random number and check whether it is prime. If it is not, we could try again. This would work, but it would be very slow. Instead, we can use a randomised algorithm called the Miller-Rabin primality test.



<!--  The Miller-Rabin primality test is a randomised algorithm that can be used to test whether a number is prime. It is based on Fermat's little theorem, which states that if $p$ is prime, then for any $a$:

$$
a^{p-1} \equiv 1 \pmod{p}
$$

The Miller-Rabin test works by choosing a random $a$ and checking whether this equation holds. If it does not, then $p$ is not prime. If it does, then $p$ is probably prime. The probability that $p$ is not prime but the test says it is is at most $1/4$. -->

https://en.wikipedia.org/wiki/AKS_primality_test


## Finding the median

The median of a list of numbers is the middle number when the list is sorted. For example, the median of $[1, 2, 3, 4, 5]$ is $3$. The median is a useful statistic because it is not affected by outliers. For example, the median of $[1, 2, 3, 4, 1000]$ is still $3$.

