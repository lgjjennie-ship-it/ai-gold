---
layout: default
title: "Mole：一个注重隐私的LLM研究代理"
date: 2026-08-15T12:00:00+00:00
discovered_date: 2026-08-15
slug: 2026-08-15-show-hn-mole-deep-research-agent-for-your-terminal
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Mole是一个开源的深度研究代理，帮助用户在预算内进行研究，同时确保数据隐私并提供验证来源。它支持大多数LLM并执行预算限制。 Mole值得关注，因为它在GitHub上获得了58个星标和活跃的社区讨论。它解决了LLM研究中预算超支和数据隐私的痛点。 Mole遵循MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要本地数据处理，并支持大多数LLM。"
tags: "LLM, Agent, Privacy, Research, Tools"
---

# Mole：一个注重隐私的LLM研究代理


> Mole是一个开源的深度研究代理，帮助用户在预算内进行研究，同时确保数据隐私并提供验证来源。它支持大多数LLM并执行预算限制。 Mole值得关注，因为它在GitHub上获得了58个星标和活跃的社区讨论。它解决了LLM研究中预算超支和数据隐私的痛点。 Mole遵循MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要本地数据处理，并支持大多数LLM。


**项目链接**：https://github.com/lajosdeme/mole
**作者**：lajosdeme
**发布时间**：2026-08-14T18:52:48Z
**挖掘日期**：2026-08-15
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, Privacy, Research, Tools


## 📌 项目详解

Mole是一个开源的深度研究代理，帮助用户在预算内进行研究，同时确保数据隐私并提供验证来源。它支持大多数LLM并执行预算限制。 Mole值得关注，因为它在GitHub上获得了58个星标和活跃的社区讨论。它解决了LLM研究中预算超支和数据隐私的痛点。 Mole遵循MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要本地数据处理，并支持大多数LLM。


## 🌐 背景与生态

Mole应对了LLM研究领域日益增长的隐私和预算控制需求，这一领域已迅速采用大型语言模型执行各种任务。


## 💬 社区讨论

社区评论关注代码复杂性和潜在的利益冲突，而其他人则赞赏其对预算和隐私的关注。


## 🚀 应用前景

Mole可用于学术研究、数据分析以及任何需要严格预算和隐私约束的LLM领域。潜在的盈利路径包括SaaS或API服务。


## 🔧 技术栈

Mole使用Python构建，并支持大多数LLM，包括本地模型和订阅服务。它使用Docker进行部署，并具有与常见数据格式的集成。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、本地LLM和基本的Docker知识。步骤涉及克隆仓库并运行设置脚本。


## 👥 目标用户

目标用户包括需要严格隐私和预算控制LLM的研究人员、数据科学家和开发人员。


## ⚖️ 类似项目对比

竞品包括LangChain（灵活的LLM工作流）和Poe（AI协作）。Mole的区别在于专注于预算和隐私。


## 📚 参考链接

- [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
- [Local vs Cloud Data Processing: Security, Privacy, and Private AI Workflows](https://mljar.com/blog/local-cloud-security-comparison/)

<details><summary>📄 查看原文内容</summary>


Doing research with agents is fun until they blow way past budget, jumble the sources, and don&#x27;t even give you the best possible answer, just sound confident.<p>And if you want to run some research task on local data - you have no idea where your data ends up after the prompt consumes it.<p>So I built this tool: a deep-research agent with an enforced budget, verified quotes, and a privacy boundary for local data.<p>1. Never spend more than you budgeted (measured overshoot is 0%).
2. Every claim carries a source
3. Data stays local (give a CSV, it&#x27;ll analyze it without the data ever leaving your machine)<p>Works with most LLMs, including coding agents, subscriptions, local models, etc.<p>It&#x27;s free and open source, would appreciate all feedback!


--- Top Comments ---

[recroad]: That is a LOT of code for a pretty basic feature.

[basedpolymer]: https:&#x2F;&#x2F;github.com&#x2F;tw93&#x2F;Mole  I see a certain conflict of interest.

[daybox]: &gt; Never spend more than you budgeted I assume that this is &quot;$ spent on search + $ spent on LLM&quot; &lt; budget, but how do you handle the LLM spending more than you would expect on a request? Or is this handled by max_tokens and some form of pricing table? (and if so, how does caching play a role?)

[hankbond]: &gt; Honest numbers I&#x27;m glad your numbers are honest!  For a moment I thought, hey, maybe this person&#x27;s numbers are lying to me... but it turned out they were not so thank you!

</details>
