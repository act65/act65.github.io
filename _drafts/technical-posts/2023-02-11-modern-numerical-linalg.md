---
layout: post
title: Jax
subtitle: Rading the docs 
permalink: jax-stack
---

> Why spend 5 mins reading the docs when you can spend 5 hours debugging?

https://jax.readthedocs.io/en/latest/autodidax.html
https://jax.readthedocs.io/en/latest/user_guides.html#
!!!


WANT to contribute?!

- look at issues (try solving some?)
- add a new diferentiable op? (sorting, LP, ?)
- ?

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
***

In Numpy, you are used to errors being thrown when you index an array outside of its bounds, like this:

np.arange(10)[11]

IndexError: index 11 is out of bounds for axis 0 with size 10

However, raising an error from code running on an accelerator can be difficult or impossible.


***

```
make_jaxpr(permissive_sum)(x)
```

***

To get a view of your Python code that is valid for many different argument values, JAX traces it on abstract values that represent sets of possible inputs. There are multiple different levels of abstraction, and different transformations use different abstraction levels.

Resources

- https://jax.readthedocs.io/en/latest/pytrees.html
- https://jax.readthedocs.io/en/latest/type_promotion.html
- https://jax.readthedocs.io/en/latest/async_dispatch.html
- https://jax.readthedocs.io/en/latest/notebooks/thinking_in_jax.html#static-vs-traced-operations !?!?
- https://jax.readthedocs.io/en/latest/jep/14273-shard-map.html