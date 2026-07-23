---
layout: default
title: "Bento：单个HTML文件中的PowerPoint"
date: 2026-07-23T12:00:00+00:00
discovered_date: 2026-07-23
slug: 2026-07-23-show-hn-bento-an-entire-powerpoint-in-one-html-file-edit-view-data-collab
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Bento是一个单个HTML文件，允许用户在本地创建、编辑、演示和协作PowerPoint风格的幻灯片，无需互联网连接或安装，使用reveal.js和Claude Code等技术。 Bento通过提供一个本地可运行、协作的工具解决了复杂幻灯片编辑的痛点，在Hacker News上获得了高关注度，表明了强烈的市场需求，并通过SaaS或工具化具有潜在的盈利能力。 Bento在MIT许可证下，目前处于生产成熟度，无需安装。它在HTML文件中使用base64编码的应用程序，并使用加密的盲中继进行共享编辑，没有外部依赖。"
tags: "Presentation, Web, Local, Collaboration, HTML"
---

# Bento：单个HTML文件中的PowerPoint


> Bento是一个单个HTML文件，允许用户在本地创建、编辑、演示和协作PowerPoint风格的幻灯片，无需互联网连接或安装，使用reveal.js和Claude Code等技术。 Bento通过提供一个本地可运行、协作的工具解决了复杂幻灯片编辑的痛点，在Hacker News上获得了高关注度，表明了强烈的市场需求，并通过SaaS或工具化具有潜在的盈利能力。 Bento在MIT许可证下，目前处于生


**项目链接**：https://bento.page/slides/
**作者**：starfallg
**发布时间**：2026-07-22T15:19:23Z
**挖掘日期**：2026-07-23
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Presentation, Web, Local, Collaboration, HTML


## 📌 项目详解

Bento是一个单个HTML文件，允许用户在本地创建、编辑、演示和协作PowerPoint风格的幻灯片，无需互联网连接或安装，使用reveal.js和Claude Code等技术。 Bento通过提供一个本地可运行、协作的工具解决了复杂幻灯片编辑的痛点，在Hacker News上获得了高关注度，表明了强烈的市场需求，并通过SaaS或工具化具有潜在的盈利能力。 Bento在MIT许可证下，目前处于生产成熟度，无需安装。它在HTML文件中使用base64编码的应用程序，并使用加密的盲中继进行共享编辑，没有外部依赖。


## 🌐 背景与生态

随着远程工作的普及，对本地协作演示工具的需求增长，Bento通过将演示、编辑和协作结合在一个自包含的HTML文件中，利用现有的网络技术填补了这一空白。


## 💬 社区讨论

社区评论强调了该工具的易用性、广泛采用的潜力，以及建议改进无障碍功能。


## 🚀 应用前景

Bento可用于教育、商业演示和内部沟通等领域，其中本地控制和协作受到重视。盈利模式可能来自SaaS订阅或其他工具的集成。


## 🔧 技术栈

技术栈包括HTML、CSS、JavaScript、reveal.js和Claude Code，用于本地状态管理和功能。


## 🎯 上手难度

入门评级为入门级。用户需要现代浏览器，通过打开HTML文件即可开始编辑。无需额外设置。


## 👥 目标用户

目标用户包括需要本地创建和共享演示的个人开发者、教育工作者和商业专业人士。


## ⚖️ 类似项目对比

竞品包括Google Slides（基于网络）、Microsoft PowerPoint（可安装）以及像Marp（单文件Markdown到幻灯片）这样的工具。Bento的区别在于完全自包含且支持离线使用。


## 📚 参考链接

- [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
- [How Claude Code works - Claude Code Docs](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code: What It Is, How It's Different, and Why Non-Technical ...](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)

<details><summary>📄 查看原文内容</summary>


Over the past few months, our team has been building more and more slidedecks using web frontend technologies with coding harnesses like Claude Code, but a common complaint is to make even small edits we need to edit the code either manually or via the harness.<p>To avoid this loop, I ended up creating Bento, a single HTML file with everything you need in a slide tool including animations and shared editing. There&#x27;s no install or cloud login, everything works offline. The default deck is around 560 KB and it doesn&#x27;t need to fetch anything once you got it.<p>Open it in a browser and then you can edit, present, print and save. Share it via email or via Airdrop and all they need is a browser to edit, present and also do live collab on the slides. Drop it in to Claude or ChatGPT to transform existing pptx files into Bento slides. There is no cloud involved, only an encrypted blind relay to allow for shared editing. The relay doesn&#x27;t see any of the data.<p>Check it out at <a href="https:&#x2F;&#x2F;bento.page&#x2F;slides&#x2F;" rel="nofollow">https:&#x2F;&#x2F;bento.page&#x2F;slides&#x2F;</a> which takes you straight to the editor.<p>Go to <a href="https:&#x2F;&#x2F;bento.page&#x2F;guestbook&#x2F;" rel="nofollow">https:&#x2F;&#x2F;bento.page&#x2F;guestbook&#x2F;</a> to try out the live guestbook to experience share editing &#x2F; collab.<p>There is also a gallery with some sample decks on the website - <a href="https:&#x2F;&#x2F;bento.page&#x2F;" rel="nofollow">https:&#x2F;&#x2F;bento.page&#x2F;</a><p>All the code is MIT licensed and you can find it here - <a href="https:&#x2F;&#x2F;github.com&#x2F;nyblnet&#x2F;bento" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;nyblnet&#x2F;bento</a> . I used reveal.js with several other libraries (including some homegrown ones), and Claude Code.


--- Top Comments ---

[starfallg]: Hi, I&#x27;m the creator of Bento. Just wanted to share a bit more about how I created it beyond what&#x27;s in Github. The file contains more or less two sections. There is a plain block of JSON near the top of the file which is the slide data. You can read, grep, or point a harness at it. The app itself is in a base64 blob that loads through a small shim which deflates in the browser with DecompressionStream, which keeps the package small and so that we don&#x27;t need to fetch any external...

[praveer13]: This is amazing. I also think this will become more common. I feel there is a lot of software that can just be served locally via html&#x2F;typescript&#x2F;react etc and even have local state. There&#x27;s just not been an economic incentive till now. I am personally using kimi k3 to create a mobile friendly set of games, starting from math like linear algebra to quantum physics - neurodivergent friendly, completely local state, served from github pages -  to get someone interested in the fie...

[maxloh]: HTML and CSS feel fundamentally better suited for slide decks than JSON. At their core, most slides just boil down to simple flexbox structures:     ┌──────────────────────────────────────────────┐
  │ ┌─ Row 1 Container ────────────────────────┐ │
  │ │ ┌─ 4-way padding ──────────────────────┐ │ │
  │ │ │ [ Text Content ]  (sole child node)  │ │ │
  │ │ └──────────────────────────────────────┘ │ │
  │ └──────────────────────────────────────────┘ │
  │                    ↕ gap                ...

[calebm]: Awesome. I&#x27;ve been trying to promote this kind of Single-File Web Apps as a concept - feel free to add this to the proposed Wikipedia page:  https:&#x2F;&#x2F;en.wikipedia.org&#x2F;wiki&#x2F;Draft:Single_File_Web_Apps

[jimmar]: Nice work! But...I added an image to see what options it gave me. There was no way to add alt text, which leads me to believe that accessibility was not a priority. Unless passing accessibility checks is a feature, this isn&#x27;t something I could use.

</details>
