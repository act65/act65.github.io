---
layout: page
title: Experiences
permalink: /experiences/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "experience"%}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    