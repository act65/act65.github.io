---
layout: page
title: Economics and politics
permalink: /economics-politics/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.categories contains "economic"%}
                <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
        {% endif %}
    {% endfor %}
<div class="posts">    