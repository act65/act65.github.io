---
layout: page
title: Play
permalink: /play/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "play" %}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    