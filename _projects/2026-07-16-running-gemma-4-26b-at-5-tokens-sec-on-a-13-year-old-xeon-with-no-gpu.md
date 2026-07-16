---
layout: default
title: "高效在旧硬件上运行Gemma 4 26B"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目展示了如何在13年老的Xeon上，不使用GPU的情况下，以每秒5个token的速度运行一个26B的AI模型，利用了高效的AI推理技术。 它因高社区参与度而重要，展示了在低成本硬件上高效运行大型AI模型，可能节省成本和能源。 该项目不需要GPU，并需要一台13年的老Xeon，表明部署复杂度低，硬件要求低。"
tags: "AI, Optimization, Inference, Efficiency, Hardware"
---

# 高效在旧硬件上运行Gemma 4 26B


> 该项目展示了如何在13年老的Xeon上，不使用GPU的情况下，以每秒5个token的速度运行一个26B的AI模型，利用了高效的AI推理技术。 它因高社区参与度而重要，展示了在低成本硬件上高效运行大型AI模型，可能节省成本和能源。 该项目不需要GPU，并需要一台13年的老Xeon，表明部署复杂度低，硬件要求低。


**项目链接**：https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/
**作者**：neomindryan
**发布时间**：2026-07-15T15:34:05Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Optimization, Inference, Efficiency, Hardware


## 📌 项目详解

该项目展示了如何在13年老的Xeon上，不使用GPU的情况下，以每秒5个token的速度运行一个26B的AI模型，利用了高效的AI推理技术。 它因高社区参与度而重要，展示了在低成本硬件上高效运行大型AI模型，可能节省成本和能源。 该项目不需要GPU，并需要一台13年的老Xeon，表明部署复杂度低，硬件要求低。


## 🌐 背景与生态

在旧硬件上高效运行大型AI模型正变得相关，因为模型越来越大，能源效率变得至关重要。


## 💬 社区讨论

社区评论表达了对本地运行大型模型的兴奋，并讨论了本地与云推理的成本和速度。


## 📚 参考链接

- [Mastering LLM Techniques: Inference Optimization | NVIDIA ... What is inference optimization? | Google Cloud Top 5 AI Model Optimization Techniques for Faster, Smarter ... LLM Inference Optimization — Quantization, Distillation ... Inference Optimization: Practical Techniques for Faster, Cost ... LLM Inference Optimization Complete Guide: KV Cache ... LLM Inference Optimization: Cut Cost & Latency at Every Layer ...](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
- [What is inference optimization? | Google Cloud](https://cloud.google.com/discover/inference-optimization)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dwa3592]: I have a prediction. By the mid of 2027, we will have &gt;200B MoE models running on basic consumer hardware. I am running Qwen3.6-35B-A3B locally on my 16GB mac with 7-9 tokens&#x2F;second. Link -  https:&#x2F;&#x2F;github.com&#x2F;deepanwadhwa&#x2F;samosa-chat  This is a GPT4 level model running locally with a decent speed on a 16gb ram macbook air.

[hagen8]: Some ppl don&#x27;t like to hear it. But I would assume that token costs when using an inference provider are cheaper than electricity of using locally. If we just take into account output token generation for simplicity. With 5tps u get 18k tokens an hour. That would costs around 0.005USD from an inference provider. I estimate that the server consumes probably around 500W during inference. In Germany where 1kwh cost around 0.3USD, 18k tokens inferred locally would therefore cost 0.15USD whic...

[Aurornis]: A dual Xeon of this era is probably pulling 300W or more when loaded. At national average electricity prices, that’s $1.35 per day. More during the summer if you have to cool the space. If you run it 24&#x2F;7 and ignore prompt processing time (not a good assumption at all) it would get around 400,000 tokens in a day. That’s about $0.30 per million output tokens. Coincidentally, that’s the same price for this model on OpenRouter right now, but OpenRouter token gen will be 8X faster. There are...

[hparadiz]: Here&#x27;s my report running several different models on a dual Xeon with 256 GB of DDR4 and no GPU.  https:&#x2F;&#x2F;gist.github.com&#x2F;hparadiz&#x2F;f3596d00a62d8ebb2dadcc46ee5...

[throwaway2027]: That&#x27;s quite slow I&#x27;m getting 8-12 t&#x2F;s on a 13 year old CPU. (Speed varies by context size and other settings who knows)  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=48354801

</details>
