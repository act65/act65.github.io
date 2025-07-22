### AM's connections to the median and mode

Knowing the center (mean) tells us nothing directly about the most likely value (the mode) or the value that divides the distribution in half (the median).

<!-- Th -->
 <!-- L_p Norms and -->
<!-- Measures of Central Tendency -->

Let's break this down. For a given set of data points $D_n = \{a_1, a_2, ..., a_n\}$, we are looking for a single value, let's call it $m$, that best represents the "center" of this data. The way we define "best" can be framed as minimizing some measure of the total "distance" or "error" between $m$ and each data point $a_i$. This is where L_p norms come in.

The L_p norm of the differences between the data points and $m$ is given by:
$$ L_p(D_n, m) = \left( \sum_{i=1}^n |a_i - m|^p \right)^{1/p} $$
Often, for minimization purposes, we work with the sum of the p-th powers of the differences, as minimizing this sum is equivalent to minimizing the L_p norm itself (since the $1/p$ power is monotonic for positive values). So we aim to minimize:
$$ S_p(m) = \sum_{i=1}^n |a_i - m|^p $$

Here's how different values of $p$ relate to different measures of central tendency:

*   **L2 Norm ($p=2$) $\rightarrow$ Arithmetic Mean:**
    When $p=2$, we are minimizing the sum of the squared differences:
    $$ S_2(m) = \sum_{i=1}^n (a_i - m)^2 $$
    As we showed in the blog post, the value of $m$ that minimizes this sum is the **arithmetic mean** ($\mathcal{A}$). This is why the arithmetic mean is often associated with "least squares." The L2 norm is also known as the Euclidean norm.

*   **L1 Norm ($p=1$) $\rightarrow$ Median:**
    When $p=1$, we are minimizing the sum of the absolute differences:
    $$ S_1(m) = \sum_{i=1}^n |a_i - m| $$
    The value of $m$ that minimizes this sum is the **median** of the dataset. This makes the median more robust to outliers than the arithmetic mean, because it doesn't square the differences, thus giving less weight to large deviations.

<!-- important to note that we also require the median to be one of the original data points?! 

let's rewrite these as;

AM = argmin_{x\in \mathbb R} L_2(D, x)
Median = argmin_{x\in D} L_1(D, x)
Mode = argmin_{x\in D} L_0(D, x)
-->

*   **L0 "Norm" ($p \rightarrow 0$) $\rightarrow$ Mode:**
    The L0 "norm" is a bit of a special case because it's not technically a norm in the strict mathematical sense (it doesn't satisfy all norm properties, like homogeneity). It's typically defined as the count of non-zero elements. In the context of minimizing differences, we can think of it as finding an $m$ that is *exactly equal* to as many data points $a_i$ as possible.
    Consider minimizing $\sum_{i=1}^n |a_i - m|^0$. If $a_i \neq m$, then $|a_i - m|^0 = 1$. If $a_i = m$, then $|a_i - m|^0 = 0$.
    So, minimizing this sum is equivalent to minimizing the number of data points $a_i$ that are *not* equal to $m$. This, in turn, means we are maximizing the number of data points that *are* equal to $m$. The value of $m$ that achieves this is the **mode** – the most frequent value in the dataset.

**In summary:**
*   **Arithmetic Mean** minimizes the sum of **squared** deviations (L2).
*   **Median** minimizes the sum of **absolute** deviations (L1).
*   **Mode** minimizes the count of **non-zero** deviations (L0).
