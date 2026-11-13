---
layout: default
title: "Edge0-145B：本地前沿AI"
date: 2026-11-13T12:00:00+00:00
discovered_date: 2026-11-13
slug: 2026-11-13-edge0-145b-frontier-ai-capabilities-on-your-own-computer
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Edge0-145B是一个AI模型，它允许在消费级计算机上以减少内存使用的方式运行前沿AI功能，利用矩阵共享和量化等技术。 该项目因其高参与度（271个星标，77条评论）和创新的大模型内存使用减少方法而具有重要意义，解决了主要痛点，并通过SaaS或API服务提供了明确的市场化潜力。 该模型在开放源代码许可下运行，处于生产成熟度，部署复杂性相对较低。它需要具有特定内存和计算能力的消费级硬件。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# Edge0-145B：本地前沿AI


> Edge0-145B是一个AI模型，它允许在消费级计算机上以减少内存使用的方式运行前沿AI功能，利用矩阵共享和量化等技术。 该项目因其高参与度（271个星标，77条评论）和创新的大模型内存使用减少方法而具有重要意义，解决了主要痛点，并通过SaaS或API服务提供了明确的市场化潜力。 该模型在开放源代码许可下运行，处于生产成熟度，部署复杂性相对较低。它需要具有特定内存和计算能力的消费级硬件。


**项目链接**：https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer
**作者**：sroussey
**发布时间**：2026-11-12T23:06:17Z
**挖掘日期**：2026-11-13
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

Edge0-145B是一个AI模型，它允许在消费级计算机上以减少内存使用的方式运行前沿AI功能，利用矩阵共享和量化等技术。 该项目因其高参与度（271个星标，77条评论）和创新的大模型内存使用减少方法而具有重要意义，解决了主要痛点，并通过SaaS或API服务提供了明确的市场化潜力。 该模型在开放源代码许可下运行，处于生产成熟度，部署复杂性相对较低。它需要具有特定内存和计算能力的消费级硬件。


## 🌐 背景与生态

Edge0-145B属于旨在将先进AI功能带到消费级硬件的设备上AI模型生态系统。替代方案包括Llama和Ollama等模型，但Edge0-145B因其内存效率而脱颖而出。量化和小型化技术的最新进步使该项目成为可能。


## 💬 社区讨论

社区评论表达了混合情绪，有些人对内存效率和工具使用示例印象深刻，而另一些人则对模型的能力和代理生成的输出质量持怀疑态度。


## 🚀 应用前景

Edge0-145B可应用于需要本地AI的场景，如个人助理、创意工具和教育软件。其潜在的市场化路径包括SaaS、API提供以及集成到企业解决方案中。


## 🔧 技术栈

技术栈包括Python、Transformers库以及Q3_K和NVFP4等量化技术。它利用Docker和K8s进行部署，并与LM Studio集成以方便访问。


## 🎯 上手难度

难度：进阶。前提条件包括至少具有29GB内存的MBP和Python 3.8+。步骤涉及克隆存储库、设置环境并运行提供的脚本。


## 👥 目标用户

目标用户包括软件开发、创意艺术和教育等行业中的后端工程师、ML从业者以及DevOps团队。


## ⚖️ 类似项目对比

竞品包括Llama和Ollama，它们同样专注于本地AI，但在内存效率和部署便利性方面有所不同。


## 📚 参考链接

- [Edge 0 - 145 B : Open-Source On-Device AI with 145 B Parameters - edge 0](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)
- [Edge 0 / Edge 0 - 145 B -NVFP4 · Hugging Face](https://huggingface.co/Edge0/Edge0-145B-NVFP4)
- [Google's TurboQuant: AI Memory Compression Revolution | AtomnyX](https://atomnyx.com/blog/google-turboquant-ai-memory-compression)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[origini]: Its not frontier even if it performs like a previous frontier model 12 month ago.

[_boffin_]: This just a quantized version of 3.8 next flash on strata that’s branded?

[mikeshi42]: &gt; Sharing matrices substantially reduces the weights that must be stored and moved while keeping the expert count unchanged. Each group of 64 experts shares two large matrices, while each expert retains a small set of parameters that captures its differences. 145B parameters with only peak 29GB memory usage - really impressive, truly something you can actually run on a decent spec MBP

[SwellJoe]: I&#x27;m really impressed with the Blender examples. It&#x27;s amazing how far &quot;tool use&quot; has come, when it now means using a tool as complicated as Blender to perform work that would take a human days to complete. I&#x27;m a little skeptical the actual models are workable, in the sense that a human could come in after and manually refine and apply better textures, etc. Historically, agent-made designs are messy as hell, and by the time you clean them up, you haven&#x27;t saved any ...

[mortalapeman]: Is this a derived from flash next? That&#x27;s the impression I get from reading over everything. Using Strata +  Qwen 3.8 Flash Next now and I am beyond impressed. It&#x27;s basically as capable as 5.6 Luna in my hands so far. If this is an upgrade I can&#x27;t wait to try it out.

</details>
