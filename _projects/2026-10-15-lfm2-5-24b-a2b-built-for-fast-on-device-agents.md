---
layout: default
title: "专为快速本地代理优化的AI模型"
date: 2026-10-15T12:00:00+00:00
discovered_date: 2026-10-15
slug: 2026-10-15-lfm2-5-24b-a2b-built-for-fast-on-device-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "LFM2.5-24B-A2B是一个包含24B参数的推理模型，仅激活2B参数，专为快速、私密的本地代理性能而设计，在Apple M5 Max和NVIDIA B300 GPU上展现出卓越的速度。 该项目因其200条社区评论和Hacker News上的活跃讨论而具有重要意义，表明了强烈的兴趣和认可。它展示了卓越的本地性能，暗示了在快速AI代理领域的实用性和潜在应用。 该模型在非商业许可证下运行，已达到生产成熟度，并需要特定硬件如Apple M5 Max和NVIDIA B300 GPU以实现最佳性能。"
tags: "LLM, Agent, Performance, On-Device, AI"
---

# 专为快速本地代理优化的AI模型


> LFM2.5-24B-A2B是一个包含24B参数的推理模型，仅激活2B参数，专为快速、私密的本地代理性能而设计，在Apple M5 Max和NVIDIA B300 GPU上展现出卓越的速度。 该项目因其200条社区评论和Hacker News上的活跃讨论而具有重要意义，表明了强烈的兴趣和认可。它展示了卓越的本地性能，暗示了在快速AI代理领域的实用性和潜在应用。 该模型在非商业许可证下运行，已达到生


**项目链接**：https://www.liquid.ai/blog/lfm2-5-24b-a2b
**作者**：gmays
**发布时间**：2026-10-14T23:59:37Z
**挖掘日期**：2026-10-15
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, Performance, On-Device, AI


## 📌 项目详解

LFM2.5-24B-A2B是一个包含24B参数的推理模型，仅激活2B参数，专为快速、私密的本地代理性能而设计，在Apple M5 Max和NVIDIA B300 GPU上展现出卓越的速度。 该项目因其200条社区评论和Hacker News上的活跃讨论而具有重要意义，表明了强烈的兴趣和认可。它展示了卓越的本地性能，暗示了在快速AI代理领域的实用性和潜在应用。 该模型在非商业许可证下运行，已达到生产成熟度，并需要特定硬件如Apple M5 Max和NVIDIA B300 GPU以实现最佳性能。


## 🌐 背景与生态

本地AI代理正变得越来越重要，因为它们减少了对外部云连接的依赖，实现了更快、更私密的AI部署。LFM2.5-24B-A2B在这一领域代表了显著的进步，建立在之前的模型如LFM2.5-230M到LFM2.5-24B-A2B之上。


## 💬 社区讨论

社区评论强调了模型在各种GPU上的惊人速度，讨论了其非商业许可证，并将其与Qwen3.8和Ternary-Bonsai-27B等其他模型进行了比较。


## 🚀 应用前景

LFM2.5-24B-A2B可应用于需要快速本地AI处理场景，如个人助理、实时语言翻译以及医疗保健和金融等行业的自主系统。


## 🔧 技术栈

该模型使用的技术栈包括Python、PyTorch和SGLang 0.5.22，针对NVIDIA B300 GPU的GPU推理进行了优化。


## 🎯 上手难度

入门评级为进阶，需要Python 3.8+、NVIDIA GPU以及特定的模型量化步骤。


## 👥 目标用户

目标用户包括技术、医疗保健和金融等行业中的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Qwen3.8 MoE和Ternary-Bonsai-27B，它们在参数效率和本地性能上有所不同。


## 📚 参考链接

- [Run fast, private agents on-device with LFM2.5-24B-A2B](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b)
- [LiquidAI/LFM2.5-24B-A2B · Hugging Face](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B)
- [LFM2.5-24B-A2B: Built for Fast On-Device Agents | Blog](https://www.liquid.ai/blog/lfm2-5-24b-a2b)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[sebmellen]: &gt;  it runs up to 1.7× faster than comparable MoEs on-device, with 184 tokens&#x2F;s on an Apple M5 Max and up to 21K output tokens&#x2F;s on a single NVIDIA B300 GPU  Wow, those are seriously impressive numbers for how intelligent this model seems to be! One thing that this article doesn&#x27;t clarify, and that I guess I really should look into, is what exactly AutomationBench tests for as compared to other benchmarks. The standout performance on AutomationBench is interesting to see, but...

[ghotli]: Maybe someone knows what order of cost a release like this requires in real terms of hardware and energy spend? The cost over the diff from the moment of beginning training to the end. It&#x27;s iterative from a prior model so it starts there and becomes this release after spending occurs I presume. For example, is liquid spending millions in energy in this case and the cost is amortized over successive training runs over the initial datacenter spend? What if it&#x27;s just eating cloud costs...

[MatthiasPortzel]: Very cool. I’ve been on Gemma 4 12B because of my limited RAM. There’s already an Unsloth quantization of this model so I’m downloading that and will check its performance in the morning. Someone else in this thread recommended Ternary-Bonsai-27B, which I’ll also try. Just also wanted to note that this model has a questionably-enforceable non-commercial use clause in its license. I really wish they had consulted with an IP lawyer, it’s very confusing.

[2001zhaozhao]: This seems like a big deal, no? If Qwen had released a Qwen3.8 MoE of similar size, with a naive extrapolation its capabilities would roughly be similar to this model. So basically someone has caught up to Qwen (albeit Qwen from 1-2 months ago) in parameter efficiency.

[blinkingled]: I asked it to implement the simplest todo in ghostty codebase and it failed badly - kept going in circles fixing one compile error and introducing another. Qwen 3.8 was slower (40 tok&#x2F;s compared to 75) but did get it done.

</details>
