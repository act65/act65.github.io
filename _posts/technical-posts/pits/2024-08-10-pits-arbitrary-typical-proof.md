---
title: "Typical set of arbitrary distributions"
subtitle: "Proving that the image of the typical set is the typical set of the image"
layout: post
permalink: /pits/arbitrary-typical-proof
scholar:
  bibliography: "pits.bib"
---

Question:
Given a flow, is the image of the typical set (in X) the same as the typical set (in Y)?

More formally;

- We have a random variable $\textbf X$ with distribution $\rho_X$.
- We have a flow $f$ that maps from $X$ to $Y$. 
- The typical set of $\textbf Z$ is defined as $\mathcal T_\epsilon(\textbf Z) = \{z\in Z: \mid - \frac{1}{N} \log p(z) - h(Z) \mid \le \epsilon \}$.

Does the image of the typical set in $\textbf X$, $\{f(x): x\in \mathcal T(\textbf X)\}$, equal the typical set of Y, $\mathcal T(Y)$ under the distribution $\rho_Y = f^{push}\rho_X$?

***

Need to show that: $\forall x \in T(\mathbf X)$ we have $f(x) \in T(\mathbf Y)$ and vice versa. 

$$
\begin{align*}
p_Y(f(x)) &= \frac{p_X(x)}{|\det J(x)|} \tag{change of variables eqn}\\
 \log p_y(y) &= \log \frac{p_x(x)}{|\det J(x)|} \\
&= \log p_x(x) - \log |\det J(x)| \\
\end{align*}
$$

$$
\begin{align*}
H(\mathbf Y) &= \int p(y) \log p(y) dy \tag{defn of entropy} \\
&= \int \frac{p(x)}{|\det J(x)|} \log \frac{p(x)}{|\det J(x)|} |\det J(x)| dx \\
&= \int p(x) \log p(x)  - \log |\det J(x)| dx\\
&= H(\mathbf X) - \mathbb E[\log |\det J(x)|]\\
\end{align*}
$$

$$
\begin{align*}
T_\epsilon(\mathbf Y) &= \{y\in \mathbf Y: \mid - \frac{1}{N} \log p(y) - H(\mathbf Y) \mid \le \epsilon \} \\
&= \{x\in \mathbf X: \mid - \frac{1}{N} (\log p_x(x) - \log |\det J(x)|) - (H(\mathbf X) + \mathbb E[\log |\det J(x)|]) \mid \le \epsilon \} \\
\end{align*}
$$

$T_\epsilon(Y)$ is not generally equal to $T_\epsilon(X)$ because of the terms involving the Jacobian determinant. For equality to hold, we would need:

$$
\begin{align*}
\mathbb E[\log |\det J(x)|] = \log |\det J(x)|
\end{align*}
$$

then the two terms involving the Jacobian determinant would cancel out, leaving 

$$
\begin{align*}
T_\epsilon(\mathbf Y) &= \{x\in \mathbf X: \mid - \frac{1}{N} \log p_x(x) - H(\mathbf X) \mid \le \epsilon \} \\
&= T_\epsilon(\mathbf X) \\
\end{align*}
$$

***

Therefore, the answer to the original question is:

- For linear transformations (constant Jacobian determinant): Yes, the image of the typical set equals the typical set of the image.
- For general flows: No, they are not generally equal, due to the varying Jacobian determinant.