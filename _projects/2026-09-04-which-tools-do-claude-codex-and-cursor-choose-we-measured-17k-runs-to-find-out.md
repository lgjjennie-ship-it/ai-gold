---
layout: default
title: "AI编程代理工具偏好分析"
date: 2026-09-04T12:00:00+00:00
discovered_date: 2026-09-04
slug: 2026-09-04-which-tools-do-claude-codex-and-cursor-choose-we-measured-17k-runs-to-find-out
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目通过17,000次运行测量和分析Claude、Codex和Cursor等AI编程代理的工具偏好，提供对其技术选择的洞察。 对于开发者和公司优化AI工具具有重要价值，因为研究结果表明可以引导代理选择特定产品，显示出明确的商业化路径。 该项目是开源的，处于生产成熟度，部署复杂度适中；需要Python和可能需要GPU，为开发者提供集成点。"
tags: "AI, Coding Agents, Tools, Analysis, Research"
---

# AI编程代理工具偏好分析


> 该项目通过17,000次运行测量和分析Claude、Codex和Cursor等AI编程代理的工具偏好，提供对其技术选择的洞察。 对于开发者和公司优化AI工具具有重要价值，因为研究结果表明可以引导代理选择特定产品，显示出明确的商业化路径。 该项目是开源的，处于生产成熟度，部署复杂度适中；需要Python和可能需要GPU，为开发者提供集成点。


**项目链接**：https://armature.tech/blog/which-tools-coding-agents-install
**作者**：screm
**发布时间**：2026-09-03T21:20:34Z
**挖掘日期**：2026-09-04
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Coding Agents, Tools, Analysis, Research


## 📌 项目详解

该项目通过17,000次运行测量和分析Claude、Codex和Cursor等AI编程代理的工具偏好，提供对其技术选择的洞察。 对于开发者和公司优化AI工具具有重要价值，因为研究结果表明可以引导代理选择特定产品，显示出明确的商业化路径。 该项目是开源的，处于生产成熟度，部署复杂度适中；需要Python和可能需要GPU，为开发者提供集成点。


## 🌐 背景与生态

AI编程代理正成为开发的核心，其中Claude、Codex和Cursor引领市场。该项目通过量化工具偏好填补了空白，此前这仅是轶事。


## 💬 社区讨论

评论强调了Claude的Python使用、AI的黄金时代以及引导代理选择特定产品的潜力，表明了强烈的兴趣。


## 🚀 应用前景

这些洞察可以指导开发者为AI代理构建定制工具，在编码平台SaaS或API商业化方面具有潜在应用。


## 🔧 技术栈

技术栈包括Python、Docker和云基础设施，依赖于Claude、Codex和Cursor的API。


## 🎯 上手难度

难度：进阶。前提：Python 3.8+，推荐GPU。步骤：克隆仓库，安装依赖，运行分析脚本。


## 👥 目标用户

目标用户是科技公司或初创公司的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Preseason.ai的工具跟踪和Cursor的AI编程代理，它们在范围和焦点上有所不同。


## 📚 参考链接

- [Anthropic - Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
- [Introducing Codex | OpenAI](https://openai.com/index/introducing-codex/)
- [Cursor — Build Software with AI Agents](https://cursor.com/product)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[xnorswap]: They didn&#x27;t measure which programming language because we all know it&#x27;s python, which it tries to use, every session, despite repeated memory files to not use python. Recently it&#x27;s even taken to  installing python  to get jobs done.

[natnatenathan]: I keep telling people that we are living in the golden age of AI - like the first year or two of google. It is all down hill as these companies push for profit and lock-in.

[ttul]: I built this for my own company. Armature is on to something. You start by analyzing the choices agents would make for various use cases and then glean what, if anything, you might do to start tilting the agents in the direction of your own product and away from the competitor. Selling to agents is similar to selling to humans. You dump money into marketing to make sure agents find your solution around every corner for every use case you’re well suited to.

[IgorPartola]: For some reason Claude Code keeps using awk, sed, and even Python to do basic file editing. Anyone know why that changed with the 5 series?

[thedreammachine]: I&#x27;ve been tracking the same for a few months. All open source and available here:  https:&#x2F;&#x2F;preseason.ai&#x2F;

</details>
