---
layout: default
title: "高效Gemma 4 26B在旧Xeon上的执行"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目展示了如何在没有GPU的13年旧Xeon上以5个token/秒的速度运行26B Gemma模型，使用了优化的软件技术。 该项目因其在高 trafic 上的显著表现和其创新方法而具有重要意义，即在过时的硬件上高效运行大型AI模型，为开发者提供了一种经济高效的解决方案。 该项目使用基于软件的优化，可能需要特定的配置，但它证明了在没有GPU的旧硬件上的可行性。"
tags: "LLM, Efficiency, Hardware, Inference, Cost"
---

# 高效Gemma 4 26B在旧Xeon上的执行


> 该项目展示了如何在没有GPU的13年旧Xeon上以5个token/秒的速度运行26B Gemma模型，使用了优化的软件技术。 该项目因其在高 trafic 上的显著表现和其创新方法而具有重要意义，即在过时的硬件上高效运行大型AI模型，为开发者提供了一种经济高效的解决方案。 该项目使用基于软件的优化，可能需要特定的配置，但它证明了在没有GPU的旧硬件上的可行性。


**项目链接**：https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/
**作者**：neomindryan
**发布时间**：2026-07-15T15:34:05Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Efficiency, Hardware, Inference, Cost


## 📌 项目详解

该项目展示了如何在没有GPU的13年旧Xeon上以5个token/秒的速度运行26B Gemma模型，使用了优化的软件技术。 该项目因其在高 trafic 上的显著表现和其创新方法而具有重要意义，即在过时的硬件上高效运行大型AI模型，为开发者提供了一种经济高效的解决方案。 该项目使用基于软件的优化，可能需要特定的配置，但它证明了在没有GPU的旧硬件上的可行性。


## 🌐 背景与生态

随着硬件老化，在旧硬件上运行大型AI模型是一个日益增长的挑战。该项目通过优化模型执行而不依赖GPU来解决这一问题。


## 💬 社区讨论

社区评论强调了未来在本地运行大型模型的可能性，并讨论了本地与云端推理的成本效益。


## 📚 参考链接

- [README.md · google/ gemma - 4 - 26 B -A 4 B at main](https://huggingface.co/google/gemma-4-26B-A4B/blob/main/README.md)
- [Gemma 4 — Google DeepMind](https://gemma4.com/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dwa3592]: I have a prediction. By the mid of 2027, we will have &gt;200B MoE models running on basic consumer hardware. I am running Qwen3.6-35B-A3B locally on my 16GB mac with 7-9 tokens&#x2F;second. Link -  https:&#x2F;&#x2F;github.com&#x2F;deepanwadhwa&#x2F;samosa-chat  This is a GPT4 level model running locally with a decent speed on a 16gb ram macbook air.

[hagen8]: Some ppl don&#x27;t like to hear it. But I would assume that token costs when using an inference provider are cheaper than electricity of using locally. If we just take into account output token generation for simplicity. With 5tps u get 18k tokens an hour. That would costs around 0.005USD from an inference provider. I estimate that the server consumes probably around 500W during inference. In Germany where 1kwh cost around 0.3USD, 18k tokens inferred locally would therefore cost 0.15USD whic...

[Aurornis]: A dual Xeon of this era is probably pulling 300W or more when loaded. At national average electricity prices, that’s $1.35 per day. More during the summer if you have to cool the space. If you run it 24&#x2F;7 and ignore prompt processing time (not a good assumption at all) it would get around 400,000 tokens in a day. That’s about $0.30 per million output tokens. Coincidentally, that’s the same price for this model on OpenRouter right now, but OpenRouter token gen will be 8X faster. There are...

[hparadiz]: Here&#x27;s my report running several different models on a dual Xeon with 256 GB of DDR4 and no GPU.  https:&#x2F;&#x2F;gist.github.com&#x2F;hparadiz&#x2F;f3596d00a62d8ebb2dadcc46ee5...

[throwaway2027]: That&#x27;s quite slow I&#x27;m getting 8-12 t&#x2F;s on a 13 year old CPU. (Speed varies by context size and other settings who knows)  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48354801

</details>
