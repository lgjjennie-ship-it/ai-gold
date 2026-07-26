---
layout: default
title: "在8美元微控制器上运行28.9M参数LLM"
date: 2026-07-26T12:00:00+00:00
discovered_date: 2026-07-26
slug: 2026-07-26-running-a-28-9m-parameter-llm-on-an-8-microcontroller
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目在8美元微控制器上运行一个28.9百万参数的大型语言模型（LLM），展示了在低成本硬件上进行AI的能力，采用了新颖的方法。 它因其高人气（144个星标和29条评论）而受到关注，解决了在微控制器上运行大型LLM的细分领域，并在边缘计算中具有独特的应用潜力。 该项目处于alpha阶段，使用针对ESP32-S3的自定义固件，并在模型大小和硬件性能方面存在限制。"
tags: "LLM, Microcontroller, Edge Computing, AI, Hardware"
---

# 在8美元微控制器上运行28.9M参数LLM


> 该项目在8美元微控制器上运行一个28.9百万参数的大型语言模型（LLM），展示了在低成本硬件上进行AI的能力，采用了新颖的方法。 它因其高人气（144个星标和29条评论）而受到关注，解决了在微控制器上运行大型LLM的细分领域，并在边缘计算中具有独特的应用潜力。 该项目处于alpha阶段，使用针对ESP32-S3的自定义固件，并在模型大小和硬件性能方面存在限制。


**项目链接**：https://github.com/slvDev/esp32-ai
**作者**：boveyking
**发布时间**：2026-07-25T18:59:50Z
**挖掘日期**：2026-07-26
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Microcontroller, Edge Computing, AI, Hardware


## 📌 项目详解

该项目在8美元微控制器上运行一个28.9百万参数的大型语言模型（LLM），展示了在低成本硬件上进行AI的能力，采用了新颖的方法。 它因其高人气（144个星标和29条评论）而受到关注，解决了在微控制器上运行大型LLM的细分领域，并在边缘计算中具有独特的应用潜力。 该项目处于alpha阶段，使用针对ESP32-S3的自定义固件，并在模型大小和硬件性能方面存在限制。


## 🌐 背景与生态

边缘计算正在发展，该项目通过在低成本硬件上展示AI来利用这一趋势。类似Milk-V的板卡提供了类似的功能，但价格不同。


## 💬 社区讨论

社区评论对项目的可行性表示兴奋，讨论了潜在的改进，并建议了相关的硬件，如Milk-V板卡。


## 🚀 应用前景

这可以用于智能家居设备、物联网应用和需要低延迟且无需网络访问的边缘AI场景。可以通过专门的硬件或软件解决方案来实现盈利。


## 🔧 技术栈

技术栈包括ESP32-S3微控制器、自定义固件和一个针对设备优化的28.9百万参数LLM模型。


## 🎯 上手难度

难度：入门。前提条件包括一个ESP32-S3、Python 3.7+以及基本的微控制器熟悉度。步骤包括设置固件和刷写微控制器。


## 👥 目标用户

这面向个人开发者、物联网爱好者以及希望在低成本硬件上运行LLM进行实验的边缘计算研究人员。


## ⚖️ 类似项目对比

竞品包括像'Milk-V'板卡和'GuppyLM'这样的项目，它们也专注于在微控制器上运行LLM，但在硬件规格和模型大小上有所不同。


## 📚 参考链接

- [Running a 28 . 9 M parameter LLM on an $8 microcontroller — Web Pulse](https://wpnews.pro/news/running-a-28-9m-parameter-llm-on-an-8-microcontroller)
- [TinyML: How AI Works on Microcontrollers & IoT Devices](https://pixelburn.tech/en/tinyml-how-artificial-intelligence-runs-on-microcontrollers)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[titzer]: It&#x27;s crazy what $5 can buy you in a microcontroller these days. Have a look at these Milk-V boards:  https:&#x2F;&#x2F;milkv.io  The duo has up to 256MB of memory, and a 1TOPS@INT8 TPU. They run Linux and are $5. I bought 5!

[kamranjon]: Pretty incredible performance for the footprint - really interested to see what could be done on slightly more powerful SBCs like some that have been mentioned in this thread.

[rao-v]: This is a really neat use of the per-layer embedding trick. It&#x27;s also worth noting that there viable TTS models that are ~20-30M param, so it might mean you can have a ESP32 with no network access read stuff out to you in near real time!

[NooneAtAll3]: While running LLM on tiny device is awesome, I&#x27;m more impressed by whatever training has produced the weights

[chrishynes]: Why can&#x27;t this scale to run much larger models on CPU backed by flash with good access patterns?

</details>
