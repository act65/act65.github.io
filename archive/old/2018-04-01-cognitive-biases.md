---
layout: post
title: Computational cognitive biases
---

Computational explanations for our cognitive biases.
You can find the repo [here](https://github.com/act65/computational-cognitive-bias).

<div class="posts">
  {% for post in site.posts %}
    {% if post.category contains "cognitivebias"%}
      <div>
        - <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </div>
    {% endif %}
  {% endfor %}
</div>
