---
layout: default
title: "Ternary Bonsai 2.5 27B AI模型"
date: 2026-11-25T12:00:00+00:00
discovered_date: 2026-11-25
slug: 2026-11-25-ternary-bonsai-2-5-27b
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Ternary Bonsai 2.5 27B是一款高性能AI模型，具有大上下文窗口，在代理式编码任务中显示出潜力。 该项目因其在高中的高参与度（488个星标，150条评论）以及令人印象深刻的性能指标（包括大上下文窗口和快速标记处理速度）而值得关注，这些对于代理式编码任务非常有价值。 该模型采用开源许可证，似乎已进入生产成熟阶段，部署复杂度适中。它需要大量内存来支持其大上下文窗口。"
tags: "LLM, Agent, Code, Performance, Context"
---

# Ternary Bonsai 2.5 27B AI模型


> Ternary Bonsai 2.5 27B是一款高性能AI模型，具有大上下文窗口，在代理式编码任务中显示出潜力。 该项目因其在高中的高参与度（488个星标，150条评论）以及令人印象深刻的性能指标（包括大上下文窗口和快速标记处理速度）而值得关注，这些对于代理式编码任务非常有价值。 该模型采用开源许可证，似乎已进入生产成熟阶段，部署复杂度适中。它需要大量内存来支持其大上下文窗口。


**项目链接**：https://prismml.com/news/bonsai-2-5-27b
**作者**：b0m
**发布时间**：2026-11-24T20:08:03Z
**挖掘日期**：2026-11-25
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, Code, Performance, Context


## 📌 项目详解

Ternary Bonsai 2.5 27B是一款高性能AI模型，具有大上下文窗口，在代理式编码任务中显示出潜力。 该项目因其在高中的高参与度（488个星标，150条评论）以及令人印象深刻的性能指标（包括大上下文窗口和快速标记处理速度）而值得关注，这些对于代理式编码任务非常有价值。 该模型采用开源许可证，似乎已进入生产成熟阶段，部署复杂度适中。它需要大量内存来支持其大上下文窗口。


## 🌐 背景与生态

Ternary Bonsai 2.5 27B是PrismML Bonsai系列的组成部分，基于先前模型的成功。它旨在在一个紧凑的5.9 GB空间内改进代理式编码和多步骤任务执行。


## 💬 社区讨论

社区评论强调了该模型令人印象深刻的性能，特别是其快速标记处理速度和大上下文窗口，使其在代理式编码方面具有潜力。还有关于其与其他模型（如Qwen和Inkling）的比较的讨论。


## 🚀 应用前景

该模型在软件开发方面具有强大的应用前景，特别适用于需要多步骤推理和工具使用的任务。它可以用于IDE或作为编码辅助工具的后端。


## 🔧 技术栈

技术栈包括Python，模型使用基于Qwen3.8-27B的三元权重架构构建，并针对低内存使用进行了优化。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、GPU和对模型权重的访问。基本步骤包括设置环境和运行示例提示。


## 👥 目标用户

目标用户包括后端工程师、ML从业者以及从事编码相关任务的开发者。


## ⚖️ 类似项目对比

竞品包括Google的Gemma 27B和OpenAI的GPT-4。Ternary Bonsai 2.5 27B凭借其三元架构和对代理式编码的侧重而有所不同。


## 📚 参考链接

- [PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...](https://prismml.com/news/bonsai-2-5-27b)
- [Bonsai 2.5 27B - a prism-ml Collection - Hugging Face](https://huggingface.co/collections/prism-ml/bonsai-25-27b)
- [Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com](https://docs.prismml.com/models/bonsai-2-5-27b)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[ariwilson]: With this new Ternary Bonsai model (Q2 GGUF), I&#x27;m seeing about 22-25 tokens&#x2F;s on a Mac Mini M5 Pro 24G RAM&#x2F;512G SSD, sample Python generation prompt:     Prompt eval 2.05s
  Prompt speed 222.9 tok&#x2F;s
  Generation 83.49s
  Speed 22.3 tok&#x2F;s
  Tokens 1,860
  First token 2.12s
  
I can get up to 128k context in memory easily which makes it potentially useable for agentic coding. Pretty impressive for a small model. Will have to try a simple agentic task. Might be useful fo...

[nik_s]: Unless I&#x27;m totally mistaken, this scores equivalent to opus 4.6 (released feb 2026) on SWE-bench verified. I&#x27;d be curious to which extent this is Ternary Bonsai bechmaxxing, the underlying benchmark moving, or just us seeing frontier-like behavior on benchmarks in tiny models with a ~6 month lag: probably a bit of all three? I&#x27;ll be the first to say that SWE-bench verified is clearly not the most representative of benchmarks sadly, but progress in small models is really excitin...

[thepoet]: Some numbers for a self-created benchmark I have for running long horizon tasks with local models on my Mac (Opus 5.5 gets a 8 of 8 Passed). The tps remains the same, but the overall task completion time has improved.                    Passed   Steps            Time
  Bonsai2        5 of 8   358              107 min
  Bonsai2.5      5 of 8   296 (17% fewer)   76 min (29% less)

[tompagenet2]: Asking genuinely as I know I&#x27;m surely being daft here: the scores for this model in the table shown seem worse than Qwen. Am I reading it right and is the upside something else (memory use, speed etc)?

[syntaxing]: Just tried it through Unsloth studio. Similar speeds to inkling 2 mini Q4 on a MacBook (300 prefill, 30 generation). Actually “useful” compared to the older version 2. The agentic calls have been solid. This has been better than Q4 inkling 2 mini which was surprising.

</details>
