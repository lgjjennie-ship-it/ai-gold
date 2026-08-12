---
layout: default
title: "Nvidia Nemotron 3.5 Lightning 和 NeMo Switchyard"
date: 2026-08-12T12:00:00+00:00
discovered_date: 2026-08-12
slug: 2026-08-12-nvidia-nemotron-3-5-lightning-and-nemo-switchyard
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Nvidia Nemotron 3.5 Lightning 是一个可定制的 30B 混合专家模型，具有 3B 活跃参数，为长时间运行的代理提供快速高效的专用任务执行，而 NeMo Switchyard 智能地将 AI 任务路由到最合适的模型。 该项目因其在高登网上的高人气及其专注于通过实现高效、可自托管模型和智能路由来解决 AI 部署中的实际问题而具有重要意义，具有通过 SaaS 或 API 提供明确的市场化潜力。 该项目是开源的，Nemotron 3.5 Lightning 可在 Hugging Face 上找到，NeMo Switchyard 可在 GitHub 上找到。它适用于生产使用并提供可定制的模型，但部署复杂性可能会有所不同。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# Nvidia Nemotron 3.5 Lightning 和 NeMo Switchyard


> Nvidia Nemotron 3.5 Lightning 是一个可定制的 30B 混合专家模型，具有 3B 活跃参数，为长时间运行的代理提供快速高效的专用任务执行，而 NeMo Switchyard 智能地将 AI 任务路由到最合适的模型。 该项目因其在高登网上的高人气及其专注于通过实现高效、可自托管模型和智能路由来解决 AI 部署中的实际问题而具有重要意义，具有通过 SaaS 或 API 提供


**项目链接**：https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/
**作者**：droidjj
**发布时间**：2026-08-11T19:35:52Z
**挖掘日期**：2026-08-12
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

Nvidia Nemotron 3.5 Lightning 是一个可定制的 30B 混合专家模型，具有 3B 活跃参数，为长时间运行的代理提供快速高效的专用任务执行，而 NeMo Switchyard 智能地将 AI 任务路由到最合适的模型。 该项目因其在高登网上的高人气及其专注于通过实现高效、可自托管模型和智能路由来解决 AI 部署中的实际问题而具有重要意义，具有通过 SaaS 或 API 提供明确的市场化潜力。 该项目是开源的，Nemotron 3.5 Lightning 可在 Hugging Face 上找到，NeMo Switchyard 可在 GitHub 上找到。它适用于生产使用并提供可定制的模型，但部署复杂性可能会有所不同。


## 🌐 背景与生态

大型语言模型的兴起导致了对高效、较小的模型的需求不断增长，这些模型仍然可以执行复杂的任务。Nemotron 3.5 Lightning 和 NeMo Switchyard 通过专注于专用任务执行和智能路由来解决这个问题，利用了混合专家模型的优势。


## 💬 社区讨论

社区评论强调了混合专家模型在编码任务中的潜力以及高效 AI 部署的需求。人们感兴趣的是 NeMo Switchyard 如何处理提示缓存以及替代模型是否包含。


## 🚀 应用前景

这些工具非常适合需要高效 AI 任务执行的场景，例如编码辅助、自动内容生成和 AI 代理开发。可以通过 SaaS、API 或本地模型管理服务实现市场化。


## 🔧 技术栈

技术栈包括 Python、Rust 和 NVIDIA NeMo 框架。Nemotron 3.5 Lightning 是一个 30B 混合专家模型，具有 3B 活跃参数，而 NeMo Switchyard 是一个基于 Rust 的代理和库，用于 LLM 流量。


## 🎯 上手难度

入门评级为进阶。前提条件包括 Python 3.8+、GPU 以及通过 Hugging Face 或 GitHub 访问模型。基本步骤包括设置环境、下载模型并运行一个简单示例。


## 👥 目标用户

目标用户包括软件开发、内容创建和 AI 研究等行业的后端工程师、ML 实践者和 DevOps 团队。


## ⚖️ 类似项目对比

竞争对手包括 OpenAI 的 GPT-4 和 Google 的 PaLM，它们在模型大小和性能方面提供了类似的功能。NeMo Switchyard 可以被视为智能路由的专用替代方案。


## 📚 参考链接

- [NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution for Long-Running Agents | NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- [NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster, Smarter, More Efficient Agentic AI | NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)
- [Route AI Agents Across Models with NVIDIA NeMo Switchyard | NVIDIA Technical Blog](https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[kentonv]: Coincidentally I&#x27;ve been playing with small (~30B) self-hostable models for coding tasks today -- specifically plugging them into Cloudflare OS (which I work on) and asking each to build a collaborative whiteboard. I&#x27;m finding that the Mixture-of-Experts (MoE) models (Qwen 3.6-35B, and Nemotron 3.5 Lightning) are, well, terrible at this. They just couldn&#x27;t get the job done at all. Went way off the rails. They are really fast though! Whereas ~30B  dense  models (not MoE) are pre...

[jmward01]: One major consequence of the ramapocalypse, I think, is an even higher focus on small efficient models. I personally believe that the multi-trillion parameter models are fundamentally missing things and the push to smaller, more efficient will drive evolutionary structural changes that will lead to future gains

[thehamkercat]: &gt; NeMo Switchyard, an open source library for smart routing &gt; When deployed, NeMo Switchyard can intelligently direct each request to the most capable and suitable model for the job How do routers like this handle prompt caching when you send the second request? Sticky models per session? but then the second message of that session won&#x27;t be sent to a suitable model, and will only be sent to the same model as previous one.

[docheinestages]: They conveniently decided not to include the Qwen range of models in the Artificial Analysis graph, except the out-of-league Max variant. At least be brave and honest.

[average_bloke]: I would like to propose something: - problem: massive deluge of information because of AI - solution: human beings should adopt a minimalist style of communicating in writing. - e.g. this entire website page can be ten bullet points.

</details>
