---
layout: page
title: Inbetween posts
permalink: /inbetween/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'inbetween-posts' %}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
            {% endif %}
        {% endif %}
    {% endfor %}
<div class="posts">    