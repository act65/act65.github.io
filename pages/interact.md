---
layout: page
title: Intract with me
permalink: /interact/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "interact"%}
            <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    