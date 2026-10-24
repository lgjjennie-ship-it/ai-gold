---
layout: default
title: "Corgi：终端人机工程学代理多路复用器"
date: 2026-10-24T12:00:00+00:00
discovered_date: 2026-10-24
slug: 2026-10-24-show-hn-corgi-a-helpful-agent-terminal-multiplexer
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Corgi 是一个代理多路复用器，通过统一的启动器、快速搜索和内联使用跟踪等功能增强了终端的人机工程学。 Corgi 在 Hacker News 上获得了 77 分的参与度评分和 22 条评论，表明社区对其有中等兴趣。它为终端多路复用和代理管理提供了独特的人机工程学改进，这对开发者来说非常有价值。 该项目是开源的，处于生产阶段，部署复杂度适中，没有特定的硬件要求。它与 Codex 和 Claude 等人工智能代理集成。"
tags: "Terminal, Agent, Multiplexer, Ergonomics, Tools"
---

# Corgi：终端人机工程学代理多路复用器


> Corgi 是一个代理多路复用器，通过统一的启动器、快速搜索和内联使用跟踪等功能增强了终端的人机工程学。 Corgi 在 Hacker News 上获得了 77 分的参与度评分和 22 条评论，表明社区对其有中等兴趣。它为终端多路复用和代理管理提供了独特的人机工程学改进，这对开发者来说非常有价值。 该项目是开源的，处于生产阶段，部署复杂度适中，没有特定的硬件要求。它与 Codex 和 Claude


**项目链接**：https://corgi.computer/
**作者**：eiopa
**发布时间**：2026-10-23T19:46:38Z
**挖掘日期**：2026-10-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Terminal, Agent, Multiplexer, Ergonomics, Tools


## 📌 项目详解

Corgi 是一个代理多路复用器，通过统一的启动器、快速搜索和内联使用跟踪等功能增强了终端的人机工程学。 Corgi 在 Hacker News 上获得了 77 分的参与度评分和 22 条评论，表明社区对其有中等兴趣。它为终端多路复用和代理管理提供了独特的人机工程学改进，这对开发者来说非常有价值。 该项目是开源的，处于生产阶段，部署复杂度适中，没有特定的硬件要求。它与 Codex 和 Claude 等人工智能代理集成。


## 🌐 背景与生态

代理多路复用器从一个控制面板运行和管理多个 AI 编码代理，改进工作流程。Corgi 旨在增强终端的人机工程学，填补了开发者工具领域的空白。


## 💬 社区讨论

社区评论积极，用户对快速搜索和图像粘贴等功能感到兴奋。有些人提到与另一家 YC 公司的名称混淆。


## 🚀 应用前景

Corgi 可用于软件开发和 AI 研究中，以高效管理多个代理。作为 SaaS 或 API 服务具有潜在的盈利能力。


## 🔧 技术栈

Corgi 使用 Python 并与 Codex 和 Claude 等人工智能代理集成。它利用 Docker 进行部署。


## 🎯 上手难度

入门评级为进阶。前提条件包括 Python 和对 AI 推理的访问。大致步骤包括安装和配置。


## 👥 目标用户

目标用户是与 AI 代理一起工作并需要高效终端管理的开发者和研究人员。


## ⚖️ 类似项目对比

类似项目包括 Herdr 和 Tortie。Corgi 通过专注于人机工程学和统一代理管理而有所不同。


## 📚 参考链接

- [Agent Multiplexer — What It Is and Why It Matters (2026)](https://amux.io/glossary/agent-multiplexer/)
- [What Is an Agent Multiplexer? Herdr, Tortie, Claude Squad and ...](https://runpane.com/what-is-an-agent-multiplexer)
- [What Is an Agent Multiplexer? Managing Multiple AI Agents](https://ainanza.com/glossary/agent-multiplexer/)

<details><summary>📄 查看原文内容</summary>


Hey everyone,<p>Inspired by Herdr, I&#x27;ve built an agent multiplexer that I&#x27;ve been using as my daily driver for a few weeks now.<p>I think I improved on the concept in a few ways, focusing on the ergonomics I always wished I had:<p>I show you what the agents are up to, along with a running feed of their activity.
There&#x27;s also a simple shortcut (F1) to go to the next unread agent.<p>I use multiple accounts, so I&#x27;ve added unified launcher for Codex&#x2F;Claude Code&#x2F;Pi.
Theres some careful ergonomics there: fast search and resume over sessions, inline usage tracking etc.<p>Many small quality of life improvements to the terminal experience:
- Links can be copied with a click, so no need to drag-select over many lines
- cmd+v just pastes images (even on SSH)
- images have a thumbnail preview.
- Built-in CPU&#x2F;Memory&#x2F;GPU usage tracking, broken down by workspace<p>I assume you have access to cheap inference (Luna&#x2F;Haiku&#x2F;etc).
It just reuses the agents to organize things for you: what is this http link? what is this worktree about? what is each agent doing? 
It&#x27;s small but it made my environment feel more cozy.<p>On a personal note, I&#x27;ve been on a frustrating sick leave for a while now.
I created Corgi to challenge myself, and see if I can go back.
The answer is more mixed than I had hoped, but I am happy with the result and thankful for the experience.<p>I hope you like it! a few friends &amp; myself have been using it for a few weeks and it&#x27;s been pretty nice.
There&#x27;s still a lot to improve and some rough edges, so feedback would be greatly appreciated.<p>Thank you :)


--- Top Comments ---

[dewey]: I know naming is hard, but there&#x27;s another YC company with that name from a recent batch:  https:&#x2F;&#x2F;www.ycombinator.com&#x2F;companies&#x2F;corgi-insurance

[JakeSc]: Looks awesome! Will give it a try. I&#x27;ve built something similar, just open-sourced it:  https:&#x2F;&#x2F;exawatt.ai  I&#x27;m big on agent ergonomics. Cool to see what others are doing in the space.

[troupo]: &gt; cmd+v just pastes images (even on SSH) This is such an useful feature and I&#x27;m surprised so few tools bother to implement it.

[xfalcox]: I&#x27;ve been using herdr and this looks like a v2 of it. Will give it a try.

[pokpokpok]: Been using this for about a month, for me it’s been a great replacement for cmux with good simple design

</details>
