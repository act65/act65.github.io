---
layout: page
title: Posts
permalink: /posts/
---

<div class="posts">
    {% for post in site.posts %}
        <p><u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u><br><i>{{ post.subtitle }}</i></p>
    {% endfor %}
<div class="posts">    