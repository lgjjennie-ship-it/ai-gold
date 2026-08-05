---
layout: default
title: "Maple-Preview：在iPhone上运行的 ternary 20B MoE模型"
date: 2026-08-05T12:00:00+00:00
discovered_date: 2026-08-05
slug: 2026-08-05-show-hn-maple-preview-ternary-20b-moe-running-at-120-tok-s-on-a-iphone
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Maple-Preview 展示了一个 ternary 20B 混合专家（MoE）模型，在 iPhone 上高效运行，速度达到每秒 120 个 token，利用了一种新颖的 ternary 格式进行低精度 AI。 该项目因其在高 trafic 上的 Hacker News 和积极的社区参与而具有重要意义，满足了高效、低精度 AI 模型的需求，这些模型可以在消费级硬件上运行。 该项目采用开源许可证，目前处于 alpha 阶段，部署复杂度适中，除了标准的 iPhone 外没有特定的硬件要求。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# Maple-Preview：在iPhone上运行的 ternary 20B MoE模型


> Maple-Preview 展示了一个 ternary 20B 混合专家（MoE）模型，在 iPhone 上高效运行，速度达到每秒 120 个 token，利用了一种新颖的 ternary 格式进行低精度 AI。 该项目因其在高 trafic 上的 Hacker News 和积极的社区参与而具有重要意义，满足了高效、低精度 AI 模型的需求，这些模型可以在消费级硬件上运行。 该项目采用开源许可证，


**项目链接**：https://deepgrove.ai/maple-preview
**作者**：edwardbzhang
**发布时间**：2026-08-04T19:44:55Z
**挖掘日期**：2026-08-05
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

Maple-Preview 展示了一个 ternary 20B 混合专家（MoE）模型，在 iPhone 上高效运行，速度达到每秒 120 个 token，利用了一种新颖的 ternary 格式进行低精度 AI。 该项目因其在高 trafic 上的 Hacker News 和积极的社区参与而具有重要意义，满足了高效、低精度 AI 模型的需求，这些模型可以在消费级硬件上运行。 该项目采用开源许可证，目前处于 alpha 阶段，部署复杂度适中，除了标准的 iPhone 外没有特定的硬件要求。


## 🌐 背景与生态

ternary 格式是 AI 模型设计中的一个新颖方法，通过减少计算需求，使模型在资源有限的设备上更高效地部署成为可能。该项目建立在本地 AI 模型在消费电子产品上运行的日益增长的趋势之上。


## 💬 社区讨论

社区评论强调了小型模型准确性的问题，与其他模型（如 Qwen 3.6）的比较，以及对新颖 ternary 训练方法的兴奋。


## 🚀 应用前景

该模型在需要快速、低功耗 AI 的场景中具有潜在应用，例如基于代理系统的实时工具调用、移动助手和教育工具。


## 🔧 技术栈

技术栈包括 ternary 神经网络架构、Python 脚本，并可能利用 Apple 的 Core ML 框架进行设备上的推理。


## 🎯 上手难度

入门难度为进阶，需要标准 iPhone、Python 3.8+，以及对 AI 概念的基本了解。安装涉及克隆仓库并遵循设置说明。


## 👥 目标用户

目标用户包括 AI 研究人员、从事移动 AI 开发的开发人员，以及寻求高效本地 AI 解决方案的企业。


## ⚖️ 类似项目对比

竞品包括 GPT-OSS-20B，因其参数数量和效率，以及 Locally AI，因其专注于在消费级设备上运行 AI 模型。


## 📚 参考链接

- [GPT-OSS-20B: Sparse MoE 20B Model - emergentmind.com](https://www.emergentmind.com/topics/gpt-oss-20b)
- [Show HN: Maple-Preview – ternary 20B MoE running at 120 tok/s ...](https://news.mcan.sh/item/49173984)
- [Locally AI - Run AI models locally on your iPhone, iPad, and Mac.](https://locallyai.app/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[walrus01]: I wish that &quot;small&quot; LLMs would stop being confidently very incorrect. Admittedly this is a bit of an intentionally esoteric test, but the confident way in which it presents a totally incorrect answer is a bit concerning. &quot;please write 250 words on the etymology and history of the word schlong&quot;  https:&#x2F;&#x2F;pastes.io&#x2F;uhshFgn4  The actual origin of the word is from middle high German and Yiddish-speaking Ashkenazi Jewish communities. For comparison qwen 3.6 35B A3...

[beautiful_apple]: A benchmark table comparing to Qwen 3.5 35B-A3B seems strange when Qwen 3.6 35B-A3B has been out for some time and is significantly better. I didn&#x27;t notice the version difference when first reading the article! So this is a heads up to people like me.

[kamranjon]: “Current approaches to low precision primarily focus on converting models trained in full precision to lower bitwidths. We view this as fundamentally the wrong approach…” Very excited to see how it performs, I’ve been a bit skeptical of the efficacy of converting existing models - really cool to see one trained from scratch in the ternary format.

[arjie]: For small models like this, it’s super important that it works well at tool calling etc. imho because it can’t memorize facts and isn’t big enough to tell when it doesn’t know. I could use it for high quality tool routing or a backup fast model for smaller task set. E.g. I use GPT-5.6 for voice channels at home. I’d prefer to be able to have this do basic tool calls and stuff because of the local speed. Will give it a crack as a quick model in my clawlike.

[momojo]: At this point I think Apple just needs to simply  not  do anything stupid and these small model makers are going to hand them models

</details>
