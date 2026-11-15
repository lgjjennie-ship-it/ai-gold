---
layout: default
title: "JAX中的DeepSeek V3，适用于AMD GPU"
date: 2026-11-15T12:00:00+00:00
discovered_date: 2026-11-15
slug: 2026-11-15-show-hn-deepseek-v3-in-200-lines-of-pure-jax
source: hackernews
category: show-hn
ai_score: 8.0
summary: "DeepSeek V3是一个在JAX中的深度学习模型的轻量级实现，专为在包括AMD GPU在内的各种硬件上进行本地训练而设计。 该项目因其240个星标和23条评论的高参与度而具有重要意义，表明了强烈的社区兴趣。它在无需CUDA的情况下为AMD硬件提供了本地训练的新方法，展示了实用价值并通过专门的SaaS或API服务具有明确的盈利潜力。 该项目根据允许性许可证授权，适合生产使用。它处于alpha阶段，部署复杂性取决于硬件和ROCm设置。"
tags: "LLM, JAX, DeepLearning, AMD, ROCm"
---

# JAX中的DeepSeek V3，适用于AMD GPU


> DeepSeek V3是一个在JAX中的深度学习模型的轻量级实现，专为在包括AMD GPU在内的各种硬件上进行本地训练而设计。 该项目因其240个星标和23条评论的高参与度而具有重要意义，表明了强烈的社区兴趣。它在无需CUDA的情况下为AMD硬件提供了本地训练的新方法，展示了实用价值并通过专门的SaaS或API服务具有明确的盈利潜力。 该项目根据允许性许可证授权，适合生产使用。它处于alpha阶段


**项目链接**：https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax
**作者**：VaibhaavTiwari
**发布时间**：2026-11-14T15:04:15Z
**挖掘日期**：2026-11-15
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, JAX, DeepLearning, AMD, ROCm


## 📌 项目详解

DeepSeek V3是一个在JAX中的深度学习模型的轻量级实现，专为在包括AMD GPU在内的各种硬件上进行本地训练而设计。 该项目因其240个星标和23条评论的高参与度而具有重要意义，表明了强烈的社区兴趣。它在无需CUDA的情况下为AMD硬件提供了本地训练的新方法，展示了实用价值并通过专门的SaaS或API服务具有明确的盈利潜力。 该项目根据允许性许可证授权，适合生产使用。它处于alpha阶段，部署复杂性取决于硬件和ROCm设置。


## 🌐 背景与生态

JAX是一个用于高性能数值计算和机器学习的Python库，特别适用于GPU加速。ROCm是AMD的GPU编程软件堆栈，支持非NVIDIA GPU在机器学习任务中的使用。


## 💬 社区讨论

社区评论表达了对项目能够在无需CUDA的AMD GPU上运行的兴奋，用户分享了他们的经验和询问了关于CPU兼容性和进一步开发的问题。


## 🚀 应用前景

该项目在需要本地训练AMD硬件的场景中具有强大的应用前景，例如研究机构和独立开发者。潜在产品包括针对AMD用户的专用机器学习工具和服务。


## 🔧 技术栈

技术栈包括JAX用于面向数组的数值计算，ROCm用于AMD硬件的GPU支持，以及Python用于整体实现。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.7+、已安装ROCm的AMD GPU以及对JAX的基本熟悉。步骤包括克隆存储库、安装依赖项并运行提供的脚本。


## 👥 目标用户

目标用户包括机器学习研究人员、使用AMD GPU的开发人员以及寻求无需CUDA依赖的本地训练解决方案的企业。


## ⚖️ 类似项目对比

竞品包括更广泛使用的TensorFlow和PyTorch，它们缺乏对AMD GPU的原生支持。像'ROCm-TensorFlow'和'PyTorch-ROCm'这样的项目提供了部分解决方案，但并未涵盖纯JAX实现的利基。


## 📚 参考链接

- [JAX (software) - Wikipedia](https://en.wikipedia.org/wiki/JAX_(software))
- [ROCm - Wikipedia](https://en.wikipedia.org/wiki/ROCm)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[joebarbere]: Thanks for this! I&#x27;ve been trying to get local training working on Fedora with ROCm for a while now, and this is the first project that ran end-to-end on my RX 7600 XT 16GB. The whole reason for me buying the card was to play around with deep learning and models, so it&#x27;s awesome to have a stepping off point now! No CUDA meant ROCm surprisingly just worked with JAX. Gotchas for anyone with a 7600 XT: it needed two env vars, HSA_OVERRIDE_GFX_VERSION=11.0.0 because JAX&#x27;s plugin re...

[madduci]: Does this work on CPU only hardware (Intel Core Ultra 7)?

[armcat]: I love this, there is nothing like recreating a model from first principles, plus makes me want to revisit Jax again (I&#x27;ll do it after I spend enough time with Zig). Thanks for this!

[mattfrommars]: Post like these always drives a motivation to understand how inference or what OP did. For folks who are more familiar in this space, is there a good road map how to build and understand the intuition behind this? I’m comfortable in Java and Python and do vanilla SWE work.

[d_tr]: I am just starting Raschka&#x27;s book to write an llm from scratch in C++ with zero dependencies with avx-512 on a 9950x, and then I&#x27;d like to go through the literature for more advanced stuff. I don&#x27;t know what Jax is exactly but while I am aware that the algorithm implementation is not something terribly complicated, 200 lines still sounds impressive. If anyone wants to share any tips, they&#x27;re welcome.

</details>
