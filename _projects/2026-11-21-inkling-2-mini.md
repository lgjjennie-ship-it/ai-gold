---
layout: default
title: "Inkling 2 Mini：开源AI与循环Transformer"
date: 2026-11-21T12:00:00+00:00
discovered_date: 2026-11-21
slug: 2026-11-21-inkling-2-mini
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Inkling 2 Mini是一款采用循环Transformer架构的开源AI模型，专为高性能和本地使用设计，其基准测试受到社区的高度关注。 该项目因其高参与度、活跃的开发状态和创新的架构而具有重要意义，它为本地AI应用提供了明确的价值，并具有通过SaaS或API服务实现商业化的潜力。 该模型采用开放许可证，目前处于alpha阶段，部署复杂度适中，对硬件有较高要求，尤其是在本地训练方面。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# Inkling 2 Mini：开源AI与循环Transformer


> Inkling 2 Mini是一款采用循环Transformer架构的开源AI模型，专为高性能和本地使用设计，其基准测试受到社区的高度关注。 该项目因其高参与度、活跃的开发状态和创新的架构而具有重要意义，它为本地AI应用提供了明确的价值，并具有通过SaaS或API服务实现商业化的潜力。 该模型采用开放许可证，目前处于alpha阶段，部署复杂度适中，对硬件有较高要求，尤其是在本地训练方面。


**项目链接**：https://thinkingmachines.ai/news/inkling-2-mini/
**作者**：jasondavies
**发布时间**：2026-11-20T20:12:19Z
**挖掘日期**：2026-11-21
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

Inkling 2 Mini是一款采用循环Transformer架构的开源AI模型，专为高性能和本地使用设计，其基准测试受到社区的高度关注。 该项目因其高参与度、活跃的开发状态和创新的架构而具有重要意义，它为本地AI应用提供了明确的价值，并具有通过SaaS或API服务实现商业化的潜力。 该模型采用开放许可证，目前处于alpha阶段，部署复杂度适中，对硬件有较高要求，尤其是在本地训练方面。


## 🌐 背景与生态

循环Transformer架构是一种创新方法，通过重复应用Transformer块来降低计算成本，与标准自注意力机制相比更为高效。Inkling 2 Mini旨在使高性能AI更易于本地使用。


## 💬 社区讨论

社区评论强调了该模型在实际场景中的潜力，其在基准测试中的表现，以及围绕其本地可用性的兴奋情绪。


## 🚀 应用前景

Inkling 2 Mini可解决本地AI应用中的实际问题，如编程辅助和数据分析，其在软件开发和金融等行业中具有通过SaaS或API实现商业化的潜力。


## 🔧 技术栈

技术栈包括Python、循环Transformer架构和本地训练能力，依赖于PyTorch和CUDA等库。


## 🎯 上手难度

入门难度为进阶，需要Python环境、GPU以及对AI框架的熟悉。基本设置涉及克隆仓库并遵循训练说明。


## 👥 目标用户

目标用户包括软件开发和AI研究等行业的后端工程师、ML实践者和研究人员。


## ⚖️ 类似项目对比

竞品包括GPT-4和Llama.cpp等模型，它们提供相似的性能但缺乏循环Transformer架构。Inkling 2 Mini因其本地可用性和开源权重而脱颖而出。


## 📚 参考链接

- [Transformer (deep learning) - Wikipedia](https://en.wikipedia.org/wiki/Transformer_(deep_learning))
- [Looped Transformer | Sebastian Raschka, PhD](https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/)
- [OpenAI Astra and Looped Transformers | Sebastian Raschka, PhD](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[montroser]: This is bonkers good if these benchmarks hold up in real-world scenarios.  To be at the level of Qwen3.8-27B with a looped transformer model is quite the flex.  They just left this note on reddit:  Hope that folks find this model more amenable to local usage - the sizing was largely informed by what folks on this subreddit ask for the most haha!   There are two particularly interesting aspects of this model for local users:   We do our training end-to-end in nvfp4, and although we haven&#x27;...

[hedgehog]: Seems pretty promising in a few quick coding tests. 27 tokens&#x2F;s decode on Ryzen 395 and llama.cpp Vulkan. Besides the obvious unmerged PRs (32694, 32657, 32429, 32704) you&#x27;ll want below tiny patch for about 30% speed boost. Also, if anyone from the team is reading, if you have access for researchers I&#x27;d be interested in doing some higher volume tests &amp; harness tuning than I have hardware for personally.       --- a&#x2F;src&#x2F;llama-graph.cpp
    +++ b&#x2F;src&#x2F;llama...

[lilytweed]: Whoa, not just a model that acknowledges and embraces using a looped architecture (GPT Astra 6+ and Sol 6.1+ are only [heavily] rumored to be looped), but it&#x27;s open weights, too? I&#x27;m willing to wager that most open models will go looped in the wake of this. Wonder what it means for safety and interpretability at this level of availability.

[dgacmu]: M1 Pro Macbook, 32GB: About 10t&#x2F;s using q4 xl while running browsers&#x2F;etc. and interacting using the local browser. test 1: write a python program to sort a csv by lastname and print out fields.
Result: Nailed it. Nice python program. Nice explanation of output, if a little chatty (it gave an example output, which I didn&#x27;t ask for). test 2: my standard &quot;identify the type and year of this coin&quot; test. Failed miserably, I gave up after 12,000 tokens of it babbling incessa...

[trilogic]: This looks great and is getting a lot of fun. Interesting cyberbench:  https:&#x2F;&#x2F;x.com&#x2F;ValsAI&#x2F;status&#x2F;2123874523938497007  Thinking machines just got up in Evaluation.

</details>
