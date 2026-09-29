---
layout: default
title: "Pac-Bench：AI Pac-Man 游戏基准测试"
date: 2026-09-29T12:00:00+00:00
discovered_date: 2026-09-29
slug: 2026-09-29-show-hn-pac-bench-how-well-can-models-one-shot-a-pac-man-game
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Pac-Bench 测试 AI 模型从单个 HTML 页面提示中创建 Pac-Man 游戏的能力，检验其一次性学习的能力。 该项目展示了 AI 模型在从简单提示中创建复杂游戏方面的实用价值，在 Hacker News 上获得中等关注度，表明社区兴趣。 该项目采用 MIT 许可证，处于 alpha 阶段，需要网页开发技能，无需特定硬件，但游戏准确性有所不同。"
tags: "AI, Game, Prompt, Benchmark, Web"
---

# Pac-Bench：AI Pac-Man 游戏基准测试


> Pac-Bench 测试 AI 模型从单个 HTML 页面提示中创建 Pac-Man 游戏的能力，检验其一次性学习的能力。 该项目展示了 AI 模型在从简单提示中创建复杂游戏方面的实用价值，在 Hacker News 上获得中等关注度，表明社区兴趣。 该项目采用 MIT 许可证，处于 alpha 阶段，需要网页开发技能，无需特定硬件，但游戏准确性有所不同。


**项目链接**：https://jonclegg.github.io/pacman-bakeoff/
**作者**：thefourthchime
**发布时间**：2026-09-28T22:43:12Z
**挖掘日期**：2026-09-29
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：AI, Game, Prompt, Benchmark, Web


## 📌 项目详解

Pac-Bench 测试 AI 模型从单个 HTML 页面提示中创建 Pac-Man 游戏的能力，检验其一次性学习的能力。 该项目展示了 AI 模型在从简单提示中创建复杂游戏方面的实用价值，在 Hacker News 上获得中等关注度，表明社区兴趣。 该项目采用 MIT 许可证，处于 alpha 阶段，需要网页开发技能，无需特定硬件，但游戏准确性有所不同。


## 🌐 背景与生态

Pac-Bench 位于 AI 应用领域，测试一次性学习。替代方案包括游戏克隆挑战，但 Pac-Bench 专注于基于 Web 的 AI 创造力。


## 💬 社区讨论

社区评论强调了游戏克隆的乐趣和学习过程，AI 在复制原始细节方面的局限性，以及对提示改进的建议。


## 🚀 应用前景

Pac-Bench 可启发教育工具、AI 创造力基准测试和游戏开发辅助工具。盈利模式可能来自教育或游戏领域的 SaaS 或 API 服务。


## 🔧 技术栈

技术栈包括 HTML、JavaScript 和 GPT-3 等 AI 模型，未提及特定框架，专注于基于 Web 的游戏创建。


## 🎯 上手难度

难度：入门。前提：基本网页技能，Python。步骤：克隆仓库，运行示例，调整提示。无需 GPU。


## 👥 目标用户

目标用户包括对 AI 创造力和一次性学习感兴趣的 AI 研究人员、游戏开发者和教育工作者。


## ⚖️ 类似项目对比

竞品包括游戏 AI 基准测试和 GitHub Copilot 等 AI 代码生成工具。Pac-Bench 在专注于一次性 Web 游戏创建方面有所不同。


## 📚 参考链接

- [PAC-BENCH: Evaluating Multi-Agent Collaboration under Privacy Constraints - ACL Anthology](https://aclanthology.org/2026.findings-acl.1552/)

<details><summary>📄 查看原文内容</summary>


Benchmarks how well Harness+models can create a Pac-Man game from a single prompt:<p>“Create a Pac-Man game in a single HTML page”<p>Each model gets one shot — no follow-up prompts or fixes.


--- Top Comments ---

[yambam]: This reminds me of a couple decades ago when some friends and I set ourselves a challenge to, individually, each create as much of a Pac-Man clone as possible in 10 hours. None of us had any experience in games programming or graphics coding. It was great fun and we all learned a lot. No-one ended up with a complete clone but I loved how we all ended up focusing on different things, like pixel-perfect graphics versus accuracy in gameplay, and how we all brought our existing skills to the chal...

[drcxd]: Interesting, recently I am working on my own clone of Pac-Man. LLM implementations lose lots of details. They are not 1:1 replication of the original game. For example, the behavior of the ghost is not the same as the original. If I have not implemented the game myself, I can not tell the differences. What LLM produced look like the original game, but they are not.

[strataspace]: I tried this with DOOM. Fable 5 did a pretty shit job. Astra made pretty crazy animated sprites and was pretty good considering. The fact that these are at all playable and 100x my programming skill level is pretty depressing from a certain pov. The ThreeJS dude posted ab how demotivated he was to continue his work, and while I was never a dev that did much with webgl, I commiserate.

[jmathai]: This prompt is a good way to test how well models fill in missing context because it&#x27;s so nondescript. They&#x27;re definitely improving. Remember when people considered you a genius for prompting with &quot;You are a skilled writer....&quot;.

[_matthew_]: I don&#x27;t think it makes sense to have the prompt be that short. This is basically a bench.ark of how models interpret an overly vague prompt. It should at least be &quot;Create a pacman clone in a single html page. Make it faithful to the original&quot; if that&#x27;s what we&#x27;re scoring it on.

</details>
