---
layout: post
title: Open problems
---

Open problems. Largely biased by what I find interesting and have happened to stumble over.
You can find the repo [here](https://github.com/act65/open-problems).


<div class="posts">
  {% for post in site.posts %}
    {% if post.category contains "openproblem"%}
      <div>
        - <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </div>
    {% endif %}
  {% endfor %}
</div>
