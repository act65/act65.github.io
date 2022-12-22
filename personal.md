---
layout: page
title: Personal posts
permalink: /personal/
---

<div class="posts">
    {% for post in site.posts %}
        {% if post.category contains "main"%}
            {% if post.path contains 'personal-posts' %}
                
                <div class="entry">
                    <i>{{ post.subtitle }}</i> 
                     <h1>
                        <img src="{{ site.baseurl }}/images/{{ post.coverImage }}" width="100">
                        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>

                     </h1>
                </div>
                
                <br>
            {% endif %}
        {% endif %}
    {% endfor %}
<div class="posts">
