---
layout: default
title: "一个紧凑的任天堂模拟器AI模型"
date: 2026-10-31T12:00:00+00:00
discovered_date: 2026-10-31
slug: 2026-10-31-show-hn-a-working-nintendo-in-1gb-of-qwen-weights
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目在紧凑的AI模型中创建了一个工作的任天堂娱乐系统模拟器，使用Qwen权重实现这一点，大小约为1GB。它展示了将VM集成在LLM权重中的新颖方法。 该项目因其252个星标和122条评论的强大牵引力而具有重要意义，表明了社区的兴趣。它解决了紧凑型复古计算模拟的利基，并顺应了将AI与传统计算任务集成的趋势。 该模型在开源许可证下，目前处于alpha阶段，部署复杂度被标记为中等。它需要~1GB的权重，并在模型中模拟了CPU和RAM。"
tags: "AI, Emulator, RetroComputing, LLM, Tools"
---

# 一个紧凑的任天堂模拟器AI模型


> 该项目在紧凑的AI模型中创建了一个工作的任天堂娱乐系统模拟器，使用Qwen权重实现这一点，大小约为1GB。它展示了将VM集成在LLM权重中的新颖方法。 该项目因其252个星标和122条评论的强大牵引力而具有重要意义，表明了社区的兴趣。它解决了紧凑型复古计算模拟的利基，并顺应了将AI与传统计算任务集成的趋势。 该模型在开源许可证下，目前处于alpha阶段，部署复杂度被标记为中等。它需要~1GB的权重


**项目链接**：https://github.com/dbreunig/nesformer
**作者**：dbreunig
**发布时间**：2026-10-30T16:40:22Z
**挖掘日期**：2026-10-31
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：AI, Emulator, RetroComputing, LLM, Tools


## 📌 项目详解

该项目在紧凑的AI模型中创建了一个工作的任天堂娱乐系统模拟器，使用Qwen权重实现这一点，大小约为1GB。它展示了将VM集成在LLM权重中的新颖方法。 该项目因其252个星标和122条评论的强大牵引力而具有重要意义，表明了社区的兴趣。它解决了紧凑型复古计算模拟的利基，并顺应了将AI与传统计算任务集成的趋势。 该模型在开源许可证下，目前处于alpha阶段，部署复杂度被标记为中等。它需要~1GB的权重，并在模型中模拟了CPU和RAM。


## 🌐 背景与生态

复古计算正重新获得兴趣，像这样的项目利用AI为旧硬件注入新的活力。Qwen权重为这种紧凑型模拟提供了一个独特的基石。


## 💬 社区讨论

社区评论表达了对在LLM权重中编译VM的潜力的兴奋，讨论了效率、应用前景以及与真实控制台的比较。


## 🚀 应用前景

该模型可用于创建专门的复古计算工具或教育平台，为保护和交互经典游戏和软件提供解决方案。可以通过SaaS或API服务进行货币化。


## 🔧 技术栈

技术栈包括Qwen权重、用于RAM模拟的门控delta网络架构，以及可能用于VM集成的Python。基础设施可能涉及Docker进行部署。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、GPU和对Qwen权重的访问。步骤包括克隆仓库、安装依赖项并运行模拟器。


## 👥 目标用户

目标用户是对AI、复古计算和模拟感兴趣的开发者，以及希望创建复古计算应用程序的教育者和爱好者。


## ⚖️ 类似项目对比

竞争对手包括基于FPGA的复古计算项目如MISTER，以及专注于模拟但缺乏此项目紧凑性的AI模型。


## 📚 参考链接

- [Qwen - Wikipedia](https://en.wikipedia.org/wiki/Qwen)
- [Retrocomputing – Hackaday](https://hackaday.com/category/retrocomputing/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dbreunig]: A couple thoughts on the process here… First off, Opus 5.5 built working weights and code with only two prompts: 1. Read this article and any relevant source code:  https:&#x2F;&#x2F;divagr.com&#x2F;blog&#x2F;qwenputer . Then explore if you could emulate the chip and ram in a Nintendo Entertainment System (as people do today with FPGAs in MISTRs) using this technique. If so, what size model would you have to build and if you could use smaller faster ones, could you get it to be at the standar...

[armcat]: This opens up so many interesting opportunities. In principle one could compile a small VM inside the LLM weights. The VM can host for example a Python interpreter, a shell and tools like sed, cat, grep etc. Instead of LLMs having to do slow autoregressive token emission with the current &quot;external&quot; tool calling, it could literally execute everything except web search, inside the LLM, with just matmul operations. You could probably optimise this so it runs in batches. You could have ...

[jacquesm]: I love these hacks, even though from an efficiency point of view it is horrifying to my assembly-code-golfing-brain. And it also gives some new appreciation for how much more efficient deterministic programs are compared to AI.

[pbohun]: &gt;Overall, nesformer runs 150–290× slower than the real console. I like these kinds of projects because it helps to show the massive compute requirement between LLMs and ordinary programs. A while back I saw some people saying we would just have LMMs hallucinate an entire operating system  every single frame . I guess technically it&#x27;s now proven to be technically possible, but it would be thousands of times slower while requiring thousands of times more compute (a multi-million x diffe...

[cafebeen]: I expected this to only simulate the CPU itself, but was surprised to find they actually simulate the RAM as well (contained in the model itself via the gated deltanet architecture).  So in my understanding, the CPU, ROM, and RAM are all handled internally by the model, and the only inputs after initialization are the controller events, wild.

</details>
