---
layout: default
title: "在旧硬件上高效部署Gemma 4"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目展示了如何在13年老的Xeon处理器上，不使用GPU的情况下，以每秒5个token的速度运行一个26B AI模型，展示了在旧硬件上高效部署AI的技术。 该项目因其高参与度（270分，175条评论）和在Hacker News上的讨论而具有重要意义，表明了人们对高效AI部署的浓厚兴趣。它解决了开发者在寻求成本效益AI部署时的实际问题，并通过SaaS或咨询服务具有潜在的盈利能力。 该项目使用token优化技术来高效运行26B模型。它适用于希望在旧硬件上部署大型AI模型的开发者，而无需进行重大修改。"
tags: "AI, Efficiency, LegacyHardware, Inference, TokenOptimization"
---

# 在旧硬件上高效部署Gemma 4


> 该项目展示了如何在13年老的Xeon处理器上，不使用GPU的情况下，以每秒5个token的速度运行一个26B AI模型，展示了在旧硬件上高效部署AI的技术。 该项目因其高参与度（270分，175条评论）和在Hacker News上的讨论而具有重要意义，表明了人们对高效AI部署的浓厚兴趣。它解决了开发者在寻求成本效益AI部署时的实际问题，并通过SaaS或咨询服务具有潜在的盈利能力。 该项目使用tok


**项目链接**：https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/
**作者**：neomindryan
**发布时间**：2026-07-15T15:34:05Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Efficiency, LegacyHardware, Inference, TokenOptimization


## 📌 项目详解

该项目展示了如何在13年老的Xeon处理器上，不使用GPU的情况下，以每秒5个token的速度运行一个26B AI模型，展示了在旧硬件上高效部署AI的技术。 该项目因其高参与度（270分，175条评论）和在Hacker News上的讨论而具有重要意义，表明了人们对高效AI部署的浓厚兴趣。它解决了开发者在寻求成本效益AI部署时的实际问题，并通过SaaS或咨询服务具有潜在的盈利能力。 该项目使用token优化技术来高效运行26B模型。它适用于希望在旧硬件上部署大型AI模型的开发者，而无需进行重大修改。


## 🌐 背景与生态

在旧硬件上运行大型AI模型一直是一个挑战，但token优化的进步使其成为可能。该项目基于这些进步提供了一个针对旧系统的实用解决方案。


## 💬 社区讨论

社区评论强调了在消费级硬件上运行大型模型的潜力，并讨论了本地与云端推理的成本影响。人们对效率的提升和在旧系统上运行强大模型的可能性感到兴奋。


## 🚀 应用前景

该项目在成本效益AI部署至关重要的行业（如医疗保健、教育和中小企业）中具有强大的应用前景。它可能导致开发能够普及高级AI能力的产品或服务。


## 🔧 技术栈

该项目利用了token优化技术，可能涉及像Python这样的编程语言，以及针对高效AI推理进行优化的框架和库。


## 🎯 上手难度

入门评级为进阶。前提条件包括13年老的Xeon处理器、Python以及熟悉token优化。基本步骤包括设置环境和运行示例推理脚本。


## 👥 目标用户

目标用户是希望在旧硬件上部署AI的开发者和企业。角色包括后端工程师、数据科学家和IT专业人员。


## ⚖️ 类似项目对比

竞品包括像'在MacBook Air上运行Qwen3.6-35B-A3B'和'Token优化用于AI推理'这样的项目。这些项目专注于高效运行大型模型，但在硬件要求和优化技术方面可能有所不同。


## 📚 参考链接

- [Gemma 4 model overview - Google AI for Developers](https://ai.google.dev/gemma/docs/core)
- [Gemma 4 — Google DeepMind](https://deepmind.google/models/gemma/gemma-4/)
- [Gemma 4 model card | Google AI for Developers](https://ai.google.dev/gemma/docs/core/model_card_4)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dwa3592]: I have a prediction. By the mid of 2027, we will have &gt;200B MoE models running on basic consumer hardware. I am running Qwen3.6-35B-A3B locally on my 16GB mac with 7-9 tokens&#x2F;second. Link -  https:&#x2F;&#x2F;github.com&#x2F;deepanwadhwa&#x2F;samosa-chat  This is a GPT4 level model running locally with a decent speed on a 16gb ram macbook air.

[hagen8]: Some ppl don&#x27;t like to hear it. But I would assume that token costs when using an inference provider are cheaper than electricity of using locally. If we just take into account output token generation for simplicity. With 5tps u get 18k tokens an hour. That would costs around 0.005USD from an inference provider. I estimate that the server consumes probably around 500W during inference. In Germany where 1kwh cost around 0.3USD, 18k tokens inferred locally would therefore cost 0.15USD whic...

[Aurornis]: A dual Xeon of this era is probably pulling 300W or more when loaded. At national average electricity prices, that’s $1.35 per day. More during the summer if you have to cool the space. If you run it 24&#x2F;7 and ignore prompt processing time (not a good assumption at all) it would get around 400,000 tokens in a day. That’s about $0.30 per million output tokens. Coincidentally, that’s the same price for this model on OpenRouter right now, but OpenRouter token gen will be 8X faster. There are...

[hparadiz]: Here&#x27;s my report running several different models on a dual Xeon with 256 GB of DDR4 and no GPU.  https:&#x2F;&#x2F;gist.github.com&#x2F;hparadiz&#x2F;f3596d00a62d8ebb2dadcc46ee5...

[throwaway2027]: That&#x27;s quite slow I&#x27;m getting 8-12 t&#x2F;s on a 13 year old CPU. (Speed varies by context size and other settings who knows)  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48354801

</details>
