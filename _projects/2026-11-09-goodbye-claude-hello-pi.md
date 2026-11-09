---
layout: default
title: "Pi：紧凑型LLM TUI harness"
date: 2026-11-09T12:00:00+00:00
discovered_date: 2026-11-09
slug: 2026-11-09-goodbye-claude-hello-pi
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Pi 是一个新的 LLM harness，它比传统界面提供更紧凑和高效的 TUI 体验，使用 Python 等语言和支持高效模型交互的框架。 Pi 在 Hacker News 上具有显著的影响力，为开发者提供了一种使用 LLMs 在 TUI 环境中的新方法，具有实用价值，并具有明确的扩展和盈利路径。 在 MIT 许可下，Pi 处于生产成熟阶段，部署复杂度适中，没有特定的硬件要求，易于集成到现有工作流程中。"
tags: "LLM, TUI, Agent, Code, Tools"
---

# Pi：紧凑型LLM TUI harness


> Pi 是一个新的 LLM harness，它比传统界面提供更紧凑和高效的 TUI 体验，使用 Python 等语言和支持高效模型交互的框架。 Pi 在 Hacker News 上具有显著的影响力，为开发者提供了一种使用 LLMs 在 TUI 环境中的新方法，具有实用价值，并具有明确的扩展和盈利路径。 在 MIT 许可下，Pi 处于生产成熟阶段，部署复杂度适中，没有特定的硬件要求，易于集成到现有工作


**项目链接**：https://caleb.software/posts/claude-to-pi.html
**作者**：karagenit
**发布时间**：2026-11-08T03:11:48Z
**挖掘日期**：2026-11-09
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, TUI, Agent, Code, Tools


## 📌 项目详解

Pi 是一个新的 LLM harness，它比传统界面提供更紧凑和高效的 TUI 体验，使用 Python 等语言和支持高效模型交互的框架。 Pi 在 Hacker News 上具有显著的影响力，为开发者提供了一种使用 LLMs 在 TUI 环境中的新方法，具有实用价值，并具有明确的扩展和盈利路径。 在 MIT 许可下，Pi 处于生产成熟阶段，部署复杂度适中，没有特定的硬件要求，易于集成到现有工作流程中。


## 🌐 背景与生态

TUI（基于文本的用户界面）体验在 LLM 方面越来越受欢迎，与传统的 GUI 相比，它提供了一种更高效的方式来与模型交互。Pi 填补了这一空白，为 LLM 提供了一个紧凑高效的 TUI。


## 💬 社区讨论

社区评论表明人们对 Pi 的内部工作原理和创建自定义 AI 代理的潜力非常感兴趣，开发者们表达了对当前 LLM harness 的兴奋和沮丧。


## 🚀 应用前景

Pi 可用于各种实际场景，例如代码审查工具、用于商业项目的 AI 代理，以及软件开发和客户服务等行业的基于 LLM 的自定义应用程序。


## 🔧 技术栈

核心技术栈包括 Python、Transformers 等关键框架，以及 Docker 等基础设施，使其易于部署和与现有系统集成。


## 🎯 上手难度

使用 Pi 的难度评级为进阶，需要 Python 3.7+、不需要 GPU，并需对 LLM 有基本了解。步骤包括克隆仓库、安装依赖项和运行演示。


## 👥 目标用户

目标用户包括对 LLMs 和 TUIs 感兴趣的个人开发者、企业团队和研究人员，特别是在软件开发、AI 和数据分析领域工作的人。


## ⚖️ 类似项目对比

竞品项目包括 OpenAI 的 ChatGPT WebUI 和 Hugging Face 的 Transformers，它们提供类似的 TUI 体验，但缺乏 Pi 的紧凑性和效率。


<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[bottlepalm]: I used to use ChatGPT&#x2F;Claude in the TUI up until like 3 months ago, but my usage of LLMs has exploded - many sessions across many projects. I feel like I outgrew the TUI and now I&#x27;m using ChatGPT&#x2F;Claude desktop. VS Code has become a code review tool and place where I manage git if need be. The GUI is less verbose with the nitty gritty hidden in expandable sections, which makes history easier and cleaner to scroll through, also no scrolling bugs, rich text is easier to read with...

[leobuskin]: Pi is a good harness (I finally gave it a try w&#x2F; abliterated GLM), but not with Anthropic subscription, and there are multiple reasons to avoid alternative harnesses with their models in general (imho): 1. Potential ban due to ToS violation; 2. It doesn&#x27;t follow all Anthropic&#x27;s communication mechanisms out-of-the-box, they heavily use custom headers, hidden flags, and undocumented API features that affect models&#x27; behavior; 3. Compact is better in CC (significantly); 4. Cac...

[real_faxenoff]: I became interested in how the harness works internally so I could try to implement my own small AI agent in a business project. And I realized that right now, most of the model’s efficiency lies precisely in the harness. And that there’s a whole complicated world inside it, one that will soon become more complex than the models themselves. All my experiments using third-party harnesses for code-writing agents showed that if a model is used in a non-native harness, it sometimes burns through ...

[gvkhna]: Pi is without contest the best harness. Because it’s yours, the total control is the only way to move from driving agents to orchestrating them. My interruptions and frustration with llms has gone down a cliff. It’s amazing to see what just a few lines of system prompt really can do to keep agents doing the correct thing much more often.

[siraben]: I&#x27;ve been daily driving Pi for over a month now and never looking back. The latest crop of frontier models have really complex bash calls, so I&#x27;ve written an extension that rewrites them into plain English while still making them easy to reveal in full, unlike some harnesses which seem to try to hide this from the user which is pretty irresponsible IMO.[0] [0]  https:&#x2F;&#x2F;github.com&#x2F;siraben&#x2F;pi-tool-summaries

</details>
