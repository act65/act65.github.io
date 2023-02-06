---
layout: page
title: Personal posts
permalink: /personal/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'personal-posts' %}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
            {% endif %}
        {% endif %}
    {% endfor %}
<div class="posts">
