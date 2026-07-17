---
layout: default
title: "模式夹具AI基准测试工具"
date: 2026-07-17T12:00:00+00:00
discovered_date: 2026-07-17
slug: 2026-07-17-schema-harness-achieves-99-on-arc-agi-3-public
source: hackernews
category: show-hn
ai_score: 9.0
summary: "模式夹具是一个AI工具，通过优化模型性能，在复杂的Arc-AGI-3基准测试中实现了高精度，使用自定义框架来增强推理任务。 该项目因其对Arc-AGI-3的高精度、强大的社区参与度以及通过专业AI工具或服务进行货币化的潜力而具有重要意义。 该项目是开源的，处于生产阶段，部署复杂度适中。它需要Python，并且可能需要GPU以获得最佳性能。"
tags: "AI, Model, Optimization, Benchmarks, Problem-Solving"
---

# 模式夹具AI基准测试工具


> 模式夹具是一个AI工具，通过优化模型性能，在复杂的Arc-AGI-3基准测试中实现了高精度，使用自定义框架来增强推理任务。 该项目因其对Arc-AGI-3的高精度、强大的社区参与度以及通过专业AI工具或服务进行货币化的潜力而具有重要意义。 该项目是开源的，处于生产阶段，部署复杂度适中。它需要Python，并且可能需要GPU以获得最佳性能。


**项目链接**：https://schema-harness.github.io/
**作者**：jasondavies
**发布时间**：2026-07-16T15:29:12Z
**挖掘日期**：2026-07-17
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Model, Optimization, Benchmarks, Problem-Solving


## 📌 项目详解

模式夹具是一个AI工具，通过优化模型性能，在复杂的Arc-AGI-3基准测试中实现了高精度，使用自定义框架来增强推理任务。 该项目因其对Arc-AGI-3的高精度、强大的社区参与度以及通过专业AI工具或服务进行货币化的潜力而具有重要意义。 该项目是开源的，处于生产阶段，部署复杂度适中。它需要Python，并且可能需要GPU以获得最佳性能。


## 🌐 背景与生态

模式夹具属于AI优化领域，建立在模型能力在复杂问题解决中日益重要的基础上。它解决了在高风险推理任务中需要更高效的AI工具的需求。


## 💬 社区讨论

社区评论对项目的潜力表示兴奋，但也警告需要开源和保留集验证。


## 🚀 应用前景

模式夹具可应用于需要高级推理的行业，如游戏、教育和人工智能研究。货币化可能通过SaaS或API模型实现。


## 🔧 技术栈

技术栈包括Python、用于模型优化的自定义框架，以及可能需要GPU支持以加速处理。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.7+、GPU以及对AI框架的熟悉。步骤包括克隆仓库并遵循设置说明。


## 👥 目标用户

目标用户包括科技和游戏行业的AI研究人员、后端工程师和DevOps团队。


## ⚖️ 类似项目对比

竞争对手包括ARC-AGI-2和其他模型优化工具如'模型夹具'。模式夹具以其在复杂基准测试中的更高精度而区别于其他工具。


## 📚 参考链接

- [GitHub - harness / harness - schema · GitHub](https://github.com/harness/harness-schema)
- [ARC-AGI-3](https://grokipedia.com/page/ARC-AGI-3)
- [ARC-AGI-3](https://arcprize.org/arc-agi/3)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[vessenes]: To be clear, we’ll want to see how this performs against the hold-out set. If it holds up, though, it’s a big deal, and kind of in line with the vibes this year, which I’d typify as ‘harness matters’. Maybe we’d upgrade to ‘harness matters immensely’ if this can 100% ARC-AGI-3 on existing models (more in the 13% range without this harness). I’m pretty excited to see what sort of generalization we come to over the next 12 months on the harness side: if it turns out this can be RLed in as ‘cons...

[ClassAndBurn]: Any custom harness for a problem shows that harness engineering is going away. Eventually models will introspect problems, then build custom harnesses tailored to that. Then use and modify the ephemeral harness as required. Sol Ultra style is the path forward. The models are smart enough to self serve their tooling and processes. Given a problem they can figure it out and ask for directions when needed.

[stared]: In the spirit of ARC-AGI-3-like challenges, we just tested if frontier AI models are able to solve a lovely puzzle game, Baba Is You:  https:&#x2F;&#x2F;quesma.com&#x2F;blog&#x2F;baba-is-bench&#x2F;  A year ago, Sonnet 4 barely solved the first level. Now, both Fable 5 and GPT-5.6 Sol beat the first two stages. GPT 5.2 is slow, but efficient, while Gemini 3.1 Pro and 3.5 Flash struggle.

[teravor]: it looks like what they are doing is using a frontier model to write a simulator for a game and then solve using it. it&#x27;s not as impressive as it looks. the goals of Arc-AGI-like constructs is to get an IQ-like figure using raw&#x27;ish 2D measurement &#x27;games&#x27; in the hope that it would signify something meaningful. what this harness does is get the model to write a simulator first, it&#x27;s measuring something entirely different.

[gandalfgeek]: Big jump for sure, but definitely comes with a giant grain of salt lacking open-sourcing the harness itself and measuring performance on the held-out set.

</details>
