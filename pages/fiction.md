---
layout: page
title: Fiction
permalink: /fiction/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "sci-fi"%}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
        {% if post.categories contains "fiction"%}
            <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    