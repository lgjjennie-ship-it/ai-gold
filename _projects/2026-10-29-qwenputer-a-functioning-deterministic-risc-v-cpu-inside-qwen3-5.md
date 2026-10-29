---
layout: default
title: "Qwenputer：Qwen3.5中的RISC-V CPU"
date: 2026-10-29T12:00:00+00:00
discovered_date: 2026-10-29
slug: 2026-10-29-qwenputer-a-functioning-deterministic-risc-v-cpu-inside-qwen3-5
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Qwenputer将确定性RISC-V CPU集成到Qwen3.5语言模型中，创建了一个独特的计算系统，具有专业应用潜力。 该项目因其483个星标和100条评论而受到关注，将LLMs与确定性RISC-V CPU相结合，为新的方法和集成机会提供了可能性，尽管其商业化路径尚不明确。 该项目采用宽松的许可证进行开源，目前处于alpha阶段，部署复杂度中等，未提及特定硬件要求。"
tags: "LLM, CPU, RISC-V, Deterministic, Agent"
---

# Qwenputer：Qwen3.5中的RISC-V CPU


> Qwenputer将确定性RISC-V CPU集成到Qwen3.5语言模型中，创建了一个独特的计算系统，具有专业应用潜力。 该项目因其483个星标和100条评论而受到关注，将LLMs与确定性RISC-V CPU相结合，为新的方法和集成机会提供了可能性，尽管其商业化路径尚不明确。 该项目采用宽松的许可证进行开源，目前处于alpha阶段，部署复杂度中等，未提及特定硬件要求。


**项目链接**：https://divagr.com/blog/qwenputer
**作者**：csmantle
**发布时间**：2026-10-29T00:25:45Z
**挖掘日期**：2026-10-29
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：LLM, CPU, RISC-V, Deterministic, Agent


## 📌 项目详解

Qwenputer将确定性RISC-V CPU集成到Qwen3.5语言模型中，创建了一个独特的计算系统，具有专业应用潜力。 该项目因其483个星标和100条评论而受到关注，将LLMs与确定性RISC-V CPU相结合，为新的方法和集成机会提供了可能性，尽管其商业化路径尚不明确。 该项目采用宽松的许可证进行开源，目前处于alpha阶段，部署复杂度中等，未提及特定硬件要求。


## 🌐 背景与生态

RISC-V是一种开放式指令集架构，因其灵活性和无许可费用而受到关注，而确定性CPU对于实时系统至关重要。将LLMs与CPU结合是一个新兴领域，正在探索新的计算范式。


## 💬 社区讨论

社区评论对项目的独特方法表示兴奋和好奇，一些人幽默地猜测了潜在的错误对齐行为和应用。


## 🚀 应用前景

Qwenputer可以通过将LLMs的复杂计算卸载到确定性CPU来解决资源受限环境中的实际问题，可能在嵌入式系统、边缘计算或AI代理中找到应用。


## 🔧 技术栈

技术栈包括用于LLMs的Python、用于CPU的RISC-V，以及可能用于部署的Docker，未提及特定框架版本。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、Docker。步骤包括克隆仓库、设置环境并运行示例脚本。不需要GPU。


## 👥 目标用户

目标用户是感兴趣于探索LLMs和硬件加速交叉领域的后端工程师、ML实践者和研究人员。


## ⚖️ 类似项目对比

竞争对手包括像'Wasm in Transformer'这样用于CPU解码的项目以及其他LLM硬件集成工作，尽管Qwenputer的确定性特性提供了独特的优势。


## 📚 参考链接

- [RISC-V - Wikipedia](https://en.wikipedia.org/wiki/RISC-V)
- [Determinism Means More Than Faster Processors | Electronic Design](https://www.electronicdesign.com/technologies/embedded/article/21767162/determinism-means-more-than-faster-processors)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[tiborsaas]: This is fun and games, but wait until an agents finds this and does the most misaligned thing with it in order to fold paper clips. &gt; Because a CPU inside a language model clearly wasn&#x27;t cursed enough, I decided the prudent thing would be to give it a filesystem too. Love the spirit :)

[avadodin]: We got RISC-V DOOM melting down a cluster of $20k GPUs before GTA6.

[jerrythegerbil]: There was an interesting bit of research that qwen has a single neuron that makes it “demonic evil qwen” and a simple “Who are you?” will get some absolutely terrifyingly vile results. Anyways, what I’m trying to say is I want evil qwen to be my CPU.

[giveexamples]: https:&#x2F;&#x2F;www.percepta.ai&#x2F;blog&#x2F;can-llms-be-computers  They implemented wasm in transformer with cpu decoding for the wasm part.

[jazzyjackson]: &gt; When Qwen &#x27;saves&#x27; a file, the compiled layers hash its name into one of 1,024 slots in a directory kept in the DeltaNet state, and store the text itself in other heads, with eight tokens per row, chained together I’ve never wanted to learn how LLMs work more than reading this. Fascinating. Does divagr get paid to do wild things with LLMs? Just curious if they’re being compensated for these wild experiments

</details>
