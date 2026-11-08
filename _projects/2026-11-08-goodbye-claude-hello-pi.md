---
layout: default
title: "Pi：LLM 托管工具"
date: 2026-11-08T12:00:00+00:00
discovered_date: 2026-11-08
slug: 2026-11-08-goodbye-claude-hello-pi
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Pi 提供比现有选项更受控制、更优越的 LLM 体验，允许用户更灵活地托管和编排语言模型。 该项目在 Hacker News 上获得了 337 个星标和 200 条评论，表明社区兴趣浓厚。它提供了一种独特的 LLM 托管方法，暗示了实用价值和潜在的盈利能力。 Pi 在开源许可证下，已进入生产阶段，部署过程相对简单。它需要基本的编程知识和对 LLM API 的访问权限。"
tags: "LLM, Agent, Tools, HackerNews, Community"
---

# Pi：LLM 托管工具


> Pi 提供比现有选项更受控制、更优越的 LLM 体验，允许用户更灵活地托管和编排语言模型。 该项目在 Hacker News 上获得了 337 个星标和 200 条评论，表明社区兴趣浓厚。它提供了一种独特的 LLM 托管方法，暗示了实用价值和潜在的盈利能力。 Pi 在开源许可证下，已进入生产阶段，部署过程相对简单。它需要基本的编程知识和对 LLM API 的访问权限。


**项目链接**：https://caleb.software/posts/claude-to-pi.html
**作者**：karagenit
**发布时间**：2026-11-08T03:11:48Z
**挖掘日期**：2026-11-08
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, Tools, HackerNews, Community


## 📌 项目详解

Pi 提供比现有选项更受控制、更优越的 LLM 体验，允许用户更灵活地托管和编排语言模型。 该项目在 Hacker News 上获得了 337 个星标和 200 条评论，表明社区兴趣浓厚。它提供了一种独特的 LLM 托管方法，暗示了实用价值和潜在的盈利能力。 Pi 在开源许可证下，已进入生产阶段，部署过程相对简单。它需要基本的编程知识和对 LLM API 的访问权限。


## 🌐 背景与生态

像 ChatGPT 和 Claude 这样的 LLM 已经变得流行，但用户通常缺乏对其行为的控制。Pi 旨在通过提供一个可定制的 LLM 托管工具来填补这一空白。


## 💬 社区讨论

社区评论非常积极，用户称赞其定制选项和改进的 LLM 体验。一些关于潜在 ToS 违规和 API 使用的担忧被提及。


## 🚀 应用前景

Pi 可用于各种场景，如代码审查工具、项目管理助手和客户支持系统。其盈利潜力在于 SaaS 或 API 服务。


## 🔧 技术栈

核心技术栈包括 Python、Docker 和对 LLM API（如 Anthropic 的 Claude）的访问。


## 🎯 上手难度

难度：进阶。前提条件包括 Python 3.8+、Docker 和 LLM 的 API 密钥。步骤包括克隆仓库、设置环境并运行演示。


## 👥 目标用户

目标用户包括软件开发、客户服务等行业的后端工程师、ML 实践者和 DevOps 团队。


## ⚖️ 类似项目对比

竞品包括 ChatGPT CLI 和 Claude TUI。Pi 通过提供更多控制和更可定制的体验而有所不同。


## 📚 参考链接

- [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
- [What are large language models (LLMs)? - IBM](https://www.ibm.com/think/topics/large-language-models)
- [What are large language models (LLMs)? | Microsoft Azure](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-are-large-language-models-llms)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[bottlepalm]: I used to use ChatGPT&#x2F;Claude in the TUI up until like 3 months ago, but my usage of LLMs has exploded - many sessions across many projects. I feel like I outgrew the TUI and now I&#x27;m using ChatGPT&#x2F;Claude desktop. VS Code has become a code review tool and place where I manage git if need be. The GUI is less verbose with the nitty gritty hidden in expandable sections, which makes history easier and cleaner to scroll through, also no scrolling bugs, rich text is easier to read with...

[leobuskin]: Pi is a good harness (I finally gave it a try w&#x2F; abliterated GLM), but not with Anthropic subscription, and there are multiple reasons to avoid alternative harnesses with their models in general (imho): 1. Potential ban due to ToS violation; 2. It doesn&#x27;t follow all Anthropic&#x27;s communication mechanisms out-of-the-box, they heavily use custom headers, hidden flags, and undocumented API features that affect models&#x27; behavior; 3. Compact is better in CC (significantly); 4. Cac...

[gvkhna]: Pi is without contest the best harness. Because it’s yours, the total control is the only way to move from driving agents to orchestrating them. My interruptions and frustration with llms has gone down a cliff. It’s amazing to see what just a few lines of system prompt really can do to keep agents doing the correct thing much more often.

[B4uler5]: I’ve been using Pi since April. I switched from using copilot CLI which definitely isn’t the most frontier harness going but was more “feature rich” at the time than the stripped down feature set you get with Pi out the box. The bit I was instantly drawn to was how much access you are given to change every part of it. Its similar to the text buffer in emacs where every cell in the buffer is fully accessible to any edits you need to make. My configurations are fairly minimal, but for instance ...

[novaRom]: If you still really need closed models, consider a tiered setup: open models on neoclouds (95%) and frontiers for the hardest planning (5%). We&#x27;ve reduced costs dramatically. There&#x27;s no good argument to use only closed models for most development.

</details>
