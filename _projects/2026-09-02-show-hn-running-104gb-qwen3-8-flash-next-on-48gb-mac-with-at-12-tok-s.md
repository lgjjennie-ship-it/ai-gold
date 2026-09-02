---
layout: default
title: "在低内存Mac上运行大型AI模型"
date: 2026-09-02T12:00:00+00:00
discovered_date: 2026-09-02
slug: 2026-09-02-show-hn-running-104gb-qwen3-8-flash-next-on-48gb-mac-with-at-12-tok-s
source: hackernews
category: show-hn
ai_score: 8.0
summary: "slotstream利用专家卸载和SSD流式传输技术，使低内存Mac能够运行大型Qwen3.8-Flash-Next模型，允许125B参数模型在16GB+系统上运行。 该项目通过在低内存设备上进行大型模型推理，解决了AI开发中的一个重要痛点，获得了201个星标和95条评论的高关注度，并具有通过SaaS或API进行商业化的潜力。 项目采用MIT许可证，处于alpha阶段，需要SSD和MLX，部署复杂度适中，除SSD外没有特定的硬件限制。"
tags: "LLM, Mac, Memory-Efficient, AI, Swift"
---

# 在低内存Mac上运行大型AI模型


> slotstream利用专家卸载和SSD流式传输技术，使低内存Mac能够运行大型Qwen3.8-Flash-Next模型，允许125B参数模型在16GB+系统上运行。 该项目通过在低内存设备上进行大型模型推理，解决了AI开发中的一个重要痛点，获得了201个星标和95条评论的高关注度，并具有通过SaaS或API进行商业化的潜力。 项目采用MIT许可证，处于alpha阶段，需要SSD和MLX，部署复杂


**项目链接**：https://github.com/carloslfu/slotstream
**作者**：carloslfu
**发布时间**：2026-09-01T16:42:46Z
**挖掘日期**：2026-09-02
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Mac, Memory-Efficient, AI, Swift


## 📌 项目详解

slotstream利用专家卸载和SSD流式传输技术，使低内存Mac能够运行大型Qwen3.8-Flash-Next模型，允许125B参数模型在16GB+系统上运行。 该项目通过在低内存设备上进行大型模型推理，解决了AI开发中的一个重要痛点，获得了201个星标和95条评论的高关注度，并具有通过SaaS或API进行商业化的潜力。 项目采用MIT许可证，处于alpha阶段，需要SSD和MLX，部署复杂度适中，除SSD外没有特定的硬件限制。


## 🌐 背景与生态

运行大型AI模型传统上需要高端硬件，但像slotstream这样的项目通过利用专家卸载等技术，使其在消费级Mac上成为可能。


## 💬 社区讨论

社区反馈强调了清理README的需求，并就性能和可扩展性提出了问题，一些用户分享了他们自己类似配置的经验。


## 🚀 应用前景

该工具可用于在预算硬件上进行大型语言模型的研发原型，在教育和小型企业中具有潜在应用。


## 🔧 技术栈

使用Swift和MLX构建，利用SSD流式传输和专家卸载，该技术栈针对Mac原生性能进行了优化，适用于Qwen3.8-Flash-Next模型。


## 🎯 上手难度

难度：进阶。前提条件包括带有SSD的Mac和Python 3.8+，安装步骤在README中概述。建议具备基本的AI和macOS知识。


## 👥 目标用户

目标用户包括需要在不牺牲性能的情况下在低预算硬件上运行大型模型的AI研究人员、开发者和教育工作者。


## ⚖️ 类似项目对比

竞品包括Deepanwadhwa的Samosa-chat和Hugging Face的推理工具，它们提供了类似的内存高效解决方案，但缺乏原生Mac优化。


## 📚 参考链接

- [Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [MoE Expert Offloading to CPU/NVMe](https://apxml.com/courses/mixture-of-experts-advanced-implementation/chapter-4-efficient-moe-inference/expert-offloading)

<details><summary>📄 查看原文内容</summary>


I built slotstream, a way to run Qwen3.8-Flash-Next 4-bit on a low-memory mac starting from 16GB, a 125B parameter model that would need 100GB+ memory&#x2F;RAM, thanks to expert-offloading&#x2F;ssd-streaming. Easy to install&#x2F;update, and mac-native using MLX and Swift.<p>It ships with auto-mode, which makes a good tradeoff between memory usage and speed. I&#x27;ll be implementing and porting the MTP module for speculative decoding next


--- Top Comments ---

[embedding-shape]: &gt; Hugging Face is the bottleneck, not your link. README could clearly make use of a cleanup, seems to be more like a session log dump now than a good introduction to the project for a new user. Maybe try something like &quot;Remove anything from the README.md that wouldn&#x27;t be helpful to someone who sees this project with zero context, for the first time. Rewrite all paragraphs and sections to be concise and remove all fluff, leave only important details new users must know before usin...

[mulemisterX]: I have a 48GB M5. I don&#x27;t need to run larger models. I want more context. I&#x27;ve managed to set the context window at 71,680 using Qwen3.8-27B-oQ4e-fp16-mtp. But I want more. Is anybody, with similar specs, able to set their context window higher?

[prometheus1992]: It&#x27;s hard to believe 16GB unified memory will give you 5 tok&#x2F;sec unless you are ignoring the thermal warnings. I am running Qwen3.6-35B-A3B on my 16GB M3 and get 7-8 tokens&#x2F;sec with all the optimizations while keeping the peak memory and thermal warnings at check.  https:&#x2F;&#x2F;github.com&#x2F;deepanwadhwa&#x2F;samosa-chat

[whartung]: I&#x27;m hoping to see progress in this space. Folks talking about how 32G is not enough for local use, but then there&#x27;s been work like this to empower it. My hope is that the new 32G M6 will be &quot;useful&quot; locally, possibly because of work like this.

[jmward01]: Not a mac&#x2F;UMA discussion point, but is it time to add additional, installable, DDR5 to GPUs? I can see this as a win&#x2F;loose. PCIe 5x16 is close to maxing out the bandwidth available from high end dual channel DDR5 now, but not quite. I&#x27;m not a hardware person but I suspect putting it on the card could lead to significant performance improvements over using system ram so allowing systems like this, where MOE weights are shed, to get even higher performance than just adding that D...

</details>
