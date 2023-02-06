---
layout: page
title: Technical posts
permalink: /technical/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'technical-posts' %}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
            {% endif %}
        {% endif %}

        <!-- not working -->
        {% if post.category contains "nonlocal"%}
            <p><u><a href="{{ post.link }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    