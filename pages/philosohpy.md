---
layout: page
title: Philosophy
permalink: /philosophy/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "philosophy"%}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    