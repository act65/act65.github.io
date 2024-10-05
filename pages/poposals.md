---
layout: page
title: Proposals
permalink: /proposals/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "proposal"%}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    