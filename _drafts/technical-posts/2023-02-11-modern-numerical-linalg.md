---
layout: post
title: test
subtitle: test 
permalink: jax-stack
---

How to write good jax code?
Fast, readable, ...?

What's with this syntax?

```python
updated_array = jax_array.at[1, :].set(1.0)
```

***

> Note: It is natural to express finite difference methods as convolutions, but here we intentionally avoid convolutions in favor of array indexing/arithmetic. This is because "batch" and "feature" dimensions in TPU convolutions are padded to multiples of either 8 and 128, but in our case both these dimensions are effectively of size 1.

https://github.com/google/jax/blob/main/cloud_tpu_colabs/Wave_Equation.ipynb


## jit compilation





## PRNG

(is this really that important to cover here?)

```python
from jax import random
key = random.PRNGKey(0)
```


Resources

- https://jax.readthedocs.io/en/latest/pytrees.html
- https://jax.readthedocs.io/en/latest/type_promotion.html
- https://jax.readthedocs.io/en/latest/async_dispatch.html