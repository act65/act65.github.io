---
layout: page
title: Personal posts
permalink: /personal/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'personal-posts' %}
                
                <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
                <div class="entry">
                    <i>{{ post.subtitle }}</i> 
                    <!-- {{ post.excerpt }} -->
                </div>
            {% endif %}
        {% endif %}
    {% endfor %}
<div class="posts">
