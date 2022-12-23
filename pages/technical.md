---
layout: page
title: Technical posts
permalink: /technical/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'technical-posts' %}
                <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
                <div class="entry">
                    <i>{{ post.subtitle }}</i> 
                    <!-- {{ post.excerpt }} -->
                </div>
            {% endif %}
        {% endif %}

        <!-- not working -->
        {% if post.category contains "nonlocal"%}
            <h1><a href="{{ post.link }}">{{ post.title }}</a></h1>
            <div class="entry">
                <i>{{ post.subtitle }}</i> {{ post.excerpt }}
                </div>
        {% endif %}
    {% endfor %}
<div class="posts">    