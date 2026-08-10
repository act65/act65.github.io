---
layout: page
title: Posts
permalink: /posts/
description: "Every post on the blog, newest first — machine learning, mathematics, economics and politics, philosophy and fiction."
---

<div class="posts">
    {% for post in site.posts %}
        <p>
            <u><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></u>
            <it><date-right>{{ post.date | date: "%B %-d, %Y" }}</date-right></it>
            <br>
            <i>{{ post.subtitle }}</i>
        </p>
        
    {% endfor %}
<div class="posts">    