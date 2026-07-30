---
layout: default
title: "TurboFieldfare：Swift和Metal大型模型AI引擎"
date: 2026-07-30T12:00:00+00:00
discovered_date: 2026-07-30
slug: 2026-07-30-drumih-turbo-fieldfare
source: hackernews
category: show-hn
ai_score: 8.0
stars: 1339
repo: "drumih/turbo-fieldfare"
summary: "TurboFieldfare是一个基于Swift和Metal的开源引擎，它允许在任何M系列Mac上仅使用2 GB的RAM运行4位Gemma 4 26B AI模型，通过从SSD流式传输权重。 该项目因其在高危新闻上的高关注度（252条评论和活跃讨论）而具有重要意义，解决了在资源受限的设备（如M系列Mac）上运行大型AI模型的痛点。其流式传输模型权重的做法提供了通过SaaS或API服务明确的市场化潜力。 该项目采用宽松的许可证，目前处于alpha阶段，部署复杂度适中。它需要M系列Mac和SSD，并且在模型精度方面由于4位量化存在限制。"
tags: "LLM, Metal, Swift, On-Device AI, Inference Engine"
---

# TurboFieldfare：Swift和Metal大型模型AI引擎


> TurboFieldfare是一个基于Swift和Metal的开源引擎，它允许在任何M系列Mac上仅使用2 GB的RAM运行4位Gemma 4 26B AI模型，通过从SSD流式传输权重。 该项目因其在高危新闻上的高关注度（252条评论和活跃讨论）而具有重要意义，解决了在资源受限的设备（如M系列Mac）上运行大型AI模型的痛点。其流式传输模型权重的做法提供了通过SaaS或API服务明确的市场化潜力


**项目链接**：https://github.com/drumih/turbo-fieldfare
**作者**：gitpusher42
**发布时间**：2026-07-29T15:05:43Z
**挖掘日期**：2026-07-30
**AI 评分**：8.0/10
**Star 数**：1339
**来源**：hackernews
**标签**：LLM, Metal, Swift, On-Device AI, Inference Engine


## 📌 项目详解

TurboFieldfare是一个基于Swift和Metal的开源引擎，它允许在任何M系列Mac上仅使用2 GB的RAM运行4位Gemma 4 26B AI模型，通过从SSD流式传输权重。 该项目因其在高危新闻上的高关注度（252条评论和活跃讨论）而具有重要意义，解决了在资源受限的设备（如M系列Mac）上运行大型AI模型的痛点。其流式传输模型权重的做法提供了通过SaaS或API服务明确的市场化潜力。 该项目采用宽松的许可证，目前处于alpha阶段，部署复杂度适中。它需要M系列Mac和SSD，并且在模型精度方面由于4位量化存在限制。


## 🌐 背景与生态

该项目运行在本地AI生态系统内，由于内存限制，在本地运行大型模型具有挑战性。云服务或传统推理工具在延迟和成本方面存在替代方案。最近的量化技术和Metal API的进步使该项目成为可能。


## 💬 社区讨论

社区评论非常积极，用户赞扬了该项目的创新性和实用性。人们对将其与llama.cpp等替代方案进行比较以及探索其商业化潜力表示兴趣。


## 🚀 应用前景

该项目在需要本地AI推理的领域具有强大的应用前景，如个人生产力、内容创作和教育。潜在的市场化路径包括SaaS、API服务和企业许可。


## 🔧 技术栈

技术栈包括Swift编程语言、Metal API用于GPU加速，以及4位量化用于模型压缩。它利用SSD进行权重流式传输，并与苹果生态系统集成。


## 🎯 上手难度

难度：进阶。要开始使用，用户需要带有M系列芯片的Mac、SSD和Python 3.8+。过程包括下载权重（15GB）、安装依赖项并运行基于Swift的引擎。硬件要求至少8GB RAM。


## 👥 目标用户

目标用户包括对本地AI感兴趣的开发人员、研究人员和企业。后端工程师、ML从业者以及DevOps团队可以从这个项目中受益。


## ⚖️ 类似项目对比

竞品包括llama.cpp用于高效模型推理和Frontier AI用于本地大型语言模型。TurboFieldfare通过专注于Swift和Metal用于苹果硅，提供更好的苹果生态系统集成。


## 📚 参考链接

- [4-bit Quantization: A Comprehensive Guide for 2025](https://www.shadecoder.com/topics/4-bit-quantization-a-comprehensive-guide-for-2025)
- [Quantization in Plain English: 8‑bit, 4‑bit, and What You Lose](https://synthmetric.com/quantization-in-plain-english-8‑bit-4‑bit-and-what-you-lose/)

<details><summary>📄 查看原文内容</summary>


Hi HN,<p>I built a specialized inference engine for running 4-bit Gemma 4 26B-A4B-IT on any M-series Mac using about 2 GB of RAM. It is called TurboFieldfare and is written in Swift and Metal.<p>I have always adored on-device AI. It feels like magic that you can run a powerful NN on your Mac or iPhone. So I wanted to push the limits a bit and run a model whose weights don’t fit in memory.<p>The model’s 4-bit quantized weights occupy roughly 14 GB, which makes running it with conventional inference tools almost impossible on an 8 GB or even 16 GB Mac once the OS, applications, and KV cache are included.<p>The trick is to keep the shared part of the model and the KV cache in RAM, then stream only the routed experts needed for each token from SSD. An SSD is way slower than RAM, so the runtime uses a small expert cache and bounded parallel `pread`. While those reads are in flight, the GPU runs the shared part of the layer.<p>I ran more than 100 experiments. Most didn’t work. A few got me here. The experiments are described in the GitHub repo.<p>It currently generates 5–6 tok&#x2F;s on an 8 GB M2 MacBook Air and 31–35 tok&#x2F;s on an M5 MacBook Pro.<p>I also added an experimental OpenAI-compatible local server. It supports streaming and tool calls, and reuses one prompt prefix from the KV cache.<p>Try it! The Mac app is easy to install. On the first run, it will download 15 GB of weights from Hugging Face. The model is surprisingly capable.<p>I would love any kind of feedback!


--- Top Comments ---

[giancarlostoro]: Nice, I think this is the second time I see this here on HN, I always wondered why we need to shove the entire model into memory, I don&#x27;t care who King Charles is every single time. It always felt as though we already figured out how to break up large files and parse them efficiently with very little memory. Frontier AI feels like its full of people who are brilliant at making models, but when it comes to scale and practicality, they just leave it to whoever sets up infrastructure to wor...

[xenonite]: With my M1 MBA, I am still on macOS 15. To compile it, just remove the two lines with     opts.languageVersion = .version4_0
  
or surround them with     if #available(macOS 26.0, *) {
    opts.languageVersion = .version4_0
  }
  
You&#x27;ll miss out on a prefill speedup of 2.4x (as it yields 11.24x faster attention), according to the git comments, but it works. (On the 8-GPU-core MBA M1, I get 5-6 tok&#x2F;s.)

[tredre3]: I&#x27;m curious how your project compares to plain mmap! Because llama.cpp will already run 26B in 2GB of RAM if you really want to (mmap enabled, repacking disabled). It seems like the main difference is that your project synchronizes the SSD reads with inference activity, which you&#x27;ve presumably tuned to cause the least latency possible? Whereas the OS wouldn&#x27;t care about any of that.

[pwython]: Ran this on a 64 GB M4 Max MacBook. I figured having Gemma available with a small footprint would be a nice setup. No more unloading models when I need more RAM for work? Hell yea. Got 48 tok&#x2F;s decode at 1.9 GB RSS (2.4 GB peak), faster than the 24 GB M5 Pro mentioned in the benchmarks. The ~2.0 GB&#x2F;s SSD number quoted for M4 is the base chip. This M4 Max does ~7 GB&#x2F;s. Page cache seems to be why it beats the M5 Pro. With 64 GB the whole 12 GB packed_experts set stays resident, a...

[mmastrac]: I have a project that&#x27;s almost ready to run DiffusionGemma as well. The two project might potentially work well together. I&#x27;m getting ~20tok&#x2F;s on a 36GB M3 and there&#x27;s strong possibility we might be able to crib faster kernels from each other. Feel free to reach out. (currently at  https:&#x2F;&#x2F;github.com&#x2F;mmastrac&#x2F;diffgemma  but not in a releasable state yet)

--- From github ---
Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook

Language: Swift
Stars: 1339  Forks: 41  Open Issues: 8
Topics: apple-silicon, gemma, gemma4, gemma4-26b-a4b, gpgpu, llm, llm-inference, local-ai, macos, metal, on-device-ai, on-device-llm, swift
Owner: drumih
Created: 2026-07-17T15:57:54Z   Last Push: 2026-07-29T14:48:48Z

</details>
