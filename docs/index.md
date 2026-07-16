---
layout: default
title: Home
---

# AI掘金

<p class="site-tagline">挖掘 GitHub 与 Hacker News 上有实践意义的 AI 项目：爆火项目、有趣可延伸的小项目、有变现潜力的工具。每日午间更新。</p>

<div id="lang-zh" class="lang-section" markdown="1">

## 📊 每日速递

<ul class="daily-digest-list">
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% for post in zh_posts limit:10 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }} · {{ post.title }}</a>
    </li>
  {% else %}
    <li><em>暂无内容</em></li>
  {% endfor %}
</ul>

## 🗂️ 项目档案库

<div class="project-grid">
  {% assign zh_projects = site.projects | sort: "date" | reverse %}
  {% for project in zh_projects %}
    <div class="project-card">
      <a href="{{ project.url | relative_url }}" class="project-card-title">
        {{ project.title | strip_html }}
      </a>
      {% if project.summary %}
        <p class="project-card-summary">{{ project.summary | strip_html | truncate: 120 }}</p>
      {% endif %}
      <div class="project-card-meta">
        <span class="meta-date">📅 {{ project.discovered_date | default: project.date | date: "%Y-%m-%d" }}</span>
        {% if project.ai_score %}
          <span class="meta-score">⭐ {{ project.ai_score }}</span>
        {% endif %}
        {% if project.stars %}
          <span class="meta-stars">★ {{ project.stars }}</span>
        {% endif %}
        {% if project.source %}
          <span class="meta-source">{{ project.source }}</span>
        {% endif %}
      </div>
      {% if project.tags %}
        <div class="project-card-tags">
          {% assign tag_list = project.tags | split: ", " %}
          {% for tag in tag_list %}
            <span class="project-tag">{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% else %}
    <p><em>暂无项目档案</em></p>
  {% endfor %}
</div>

</div>

<div id="lang-en" class="lang-section" markdown="1">

## 📊 Daily Digest

<ul class="daily-digest-list">
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% for post in en_posts limit:10 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }} · {{ post.title }}</a>
    </li>
  {% else %}
    <li><em>No posts yet</em></li>
  {% endfor %}
</ul>

## 🗂️ Project Archive

<div class="project-grid">
  {% assign en_projects = site.projects | sort: "date" | reverse %}
  {% for project in en_projects %}
    <div class="project-card">
      <a href="{{ project.url | relative_url }}" class="project-card-title">
        {{ project.title | strip_html }}
      </a>
      {% if project.summary %}
        <p class="project-card-summary">{{ project.summary | strip_html | truncate: 120 }}</p>
      {% endif %}
      <div class="project-card-meta">
        <span class="meta-date">📅 {{ project.discovered_date | default: project.date | date: "%Y-%m-%d" }}</span>
        {% if project.ai_score %}
          <span class="meta-score">⭐ {{ project.ai_score }}</span>
        {% endif %}
        {% if project.stars %}
          <span class="meta-stars">★ {{ project.stars }}</span>
        {% endif %}
        {% if project.source %}
          <span class="meta-source">{{ project.source }}</span>
        {% endif %}
      </div>
      {% if project.tags %}
        <div class="project-card-tags">
          {% assign tag_list = project.tags | split: ", " %}
          {% for tag in tag_list %}
            <span class="project-tag">{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% else %}
    <p><em>No project archives yet</em></p>
  {% endfor %}
</div>

</div>
