---
layout: default
title: Home
---

# AI掘金

<p class="site-tagline">挖掘 GitHub 与 Hacker News 上有实践意义的 AI 项目，每个项目都有独立的深度档案。每日午间更新。</p>

<div id="lang-zh" class="lang-section" markdown="1">

## 🗂️ 项目档案库

<p class="section-intro section-intro-primary">所有挖掘项目的深度档案，持续累积，新增在前。点击卡片查看<span class="intro-emph">项目详解、背景生态、社区讨论</span>。</p>

<div class="project-grid">
  {% assign zh_projects = site.projects | where: "lang", "zh" | sort: "date" | reverse %}
  {% if zh_projects.size == 0 %}
    {% assign zh_projects = site.projects | sort: "date" | reverse %}
  {% endif %}
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

---

## 📊 每日速递

<p class="section-intro section-intro-secondary">每日午间汇总当日新挖掘项目的简要列表与评分。点击查看当日<span class="intro-emph">完整日报</span>（含所有项目的集中分析）。</p>

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

</div>

<div id="lang-en" class="lang-section" markdown="1">

## 🗂️ Project Archive

<p class="section-intro section-intro-primary">Deep archives of every mined project, continuously accumulated, newest first. Click a card for <span class="intro-emph">project breakdown, ecosystem context, and community discussion</span>.</p>

<div class="project-grid">
  {% assign en_projects = site.projects | where: "lang", "en" | sort: "date" | reverse %}
  {% if en_projects.size == 0 %}
    {% assign en_projects = site.projects | sort: "date" | reverse %}
  {% endif %}
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

---

## 📊 Daily Digest

<p class="section-intro section-intro-secondary">A midday list of newly mined projects with scores. Click for the <span class="intro-emph">full daily report</span> (consolidated analysis of all projects that day).</p>

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

</div>
