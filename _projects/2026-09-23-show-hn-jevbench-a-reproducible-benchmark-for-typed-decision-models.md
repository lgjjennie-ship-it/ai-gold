---
layout: default
title: "JevBench：类型化决策模型基准测试"
date: 2026-09-23T12:00:00+00:00
discovered_date: 2026-09-23
slug: 2026-09-23-show-hn-jevbench-a-reproducible-benchmark-for-typed-decision-models
source: hackernews
category: show-hn
ai_score: 8.0
summary: "JevBench 是一个基准测试工具，用于根据准确率、延迟和成本评估类型化决策模型与传统 LLM 的性能，并提供排行榜和加权评分指标。 该项目因其在高知名度的 Hacker News 上的高关注度而具有重要意义，提供了一种评估类型化决策模型的新方法，这些模型比 LLM 更快、更便宜，且具有通过 SaaS 或 API 提供明确的市场化路径。 JevBench 采用 MIT 许可证，处于生产成熟阶段，部署复杂度适中。它需要访问德国服务器进行延迟测试，并存在仅支持英语的限制。"
tags: "AI, Benchmark, Decision Models, LLM, Performance"
---

# JevBench：类型化决策模型基准测试


> JevBench 是一个基准测试工具，用于根据准确率、延迟和成本评估类型化决策模型与传统 LLM 的性能，并提供排行榜和加权评分指标。 该项目因其在高知名度的 Hacker News 上的高关注度而具有重要意义，提供了一种评估类型化决策模型的新方法，这些模型比 LLM 更快、更便宜，且具有通过 SaaS 或 API 提供明确的市场化路径。 JevBench 采用 MIT 许可证，处于生产成熟阶段，


**项目链接**：https://benchmarkheaven.com/jev-models
**作者**：florianstandhar
**发布时间**：2026-09-22T13:01:03Z
**挖掘日期**：2026-09-23
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Benchmark, Decision Models, LLM, Performance


## 📌 项目详解

JevBench 是一个基准测试工具，用于根据准确率、延迟和成本评估类型化决策模型与传统 LLM 的性能，并提供排行榜和加权评分指标。 该项目因其在高知名度的 Hacker News 上的高关注度而具有重要意义，提供了一种评估类型化决策模型的新方法，这些模型比 LLM 更快、更便宜，且具有通过 SaaS 或 API 提供明确的市场化路径。 JevBench 采用 MIT 许可证，处于生产成熟阶段，部署复杂度适中。它需要访问德国服务器进行延迟测试，并存在仅支持英语的限制。


## 🌐 背景与生态

类型化决策模型（如 Jev）返回有界的选择和概率，而不是文本，颠覆了传统 LLM。JevBench 为这些模型提供了可重复的基准测试，填补了 AI 生态系统中此类比较的空白。


## 💬 社区讨论

社区评论对 Jev 的性能和成本表示怀疑，而其他人则强调了该工具的潜力和设计缺陷。一些人讨论了技术细节和排行榜的差异。


## 🚀 应用前景

JevBench 可用于 AI 研究和开发，以比较类型化决策模型与 LLM。潜在应用包括企业决策系统、客户服务聊天机器人和金融分析工具。


## 🔧 技术栈

JevBench 使用 Python 并依赖 MIT 许可证。它集成了 TypeSafe AI 的 Jev 模型，并包括 Docker 进行部署。


## 🎯 上手难度

入门评级为进阶。前提条件包括 Python 3.8+、互联网访问和 GitHub 账户。克隆仓库并运行基准测试脚本。


## 👥 目标用户

目标用户包括 AI 研究人员、数据科学家和从事决策系统的企业团队。


## ⚖️ 类似项目对比

竞品包括 Hugging Face 的 JEV 决策模型和 SemIf。JevBench 的区别在于专注于类型化决策模型，而竞品是更广泛的 LLM 基准测试。


## 📚 参考链接

- [5 Decision-Making Models Explained (With Examples) - Simplilearn](https://www.simplilearn.com/decision-making-models-article)
- [Jev Playground, JevBench 75.3: The Claims, Checked (2026) | explainx.ai Blog | explainx.ai](https://www.explainx.ai/blog/jev-playground-jevbench-launch-2026)
- [Jev vs. LLMs - refix.ai](https://www.refix.ai/news/jev-vs-llms/)

<details><summary>📄 查看原文内容</summary>


Hi HN! I built JevBench because Jev kicks ass, and the world deserves to know how the serious open source and fake lookalike projects <i>really</i> perform in comparison.<p>Jev-class models return bounded choices and probabilities instead of text, and are disruptively faster and cheaper than LLMs, while being similarly intelligent on the text input they operate on.<p>JevBench allows looking at accuracy, latency and price all at once, in a weighted way - you can even configure the weighting.<p>A full run asks 534 English decisions. The v1.3 score combines chance-corrected Intelligence, Calibration, Speed and Cost.<p>Leaderboard right now:<p><pre><code>  #1 - Jev            74.4
  #2 - SemIf          73.1
  #3 - djev           73.0
  #4 - Winnow-12B Q8  71.2
  #5 reflex 4B        70.3.
</code></pre>
MIT harness, public items, frozen artifacts, scoring code and public per-task outcomes:<p><a href="https:&#x2F;&#x2F;github.com&#x2F;fstandhartinger&#x2F;jevbench" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;fstandhartinger&#x2F;jevbench</a><p>Two no-signup demos:<p><a href="https:&#x2F;&#x2F;who-is-right.app.mintapis.com" rel="nofollow">https:&#x2F;&#x2F;who-is-right.app.mintapis.com</a><p><a href="https:&#x2F;&#x2F;is-it-ai-slop.app.mintapis.com" rel="nofollow">https:&#x2F;&#x2F;is-it-ai-slop.app.mintapis.com</a><p>Limitations: English-only; latency from one German server; local&#x2F;demo latency gets a disclosed ×2 adjustment (+150 ms on my servers) which is an informed assumption; held-out prompts still reach evaluated services; ~1-point gaps can be noise.<p>Wdyt?


--- Top Comments ---

[hbrn]: $40m in funding, 2 years in stealth. Performs on-par with SemIf which was built in a couple days and apparently uses  raw  Qwen, with no fine-tuning. SemIf runs in your freaking browser. Oh and Jev is twice as expensive? Is it surprising that Jev consistently thinks it&#x27;s Qwen? I&#x27;m almost convinced that Jev is a scam. Take Qwen, fine tune it a little, tell investors it cost $10m, spend $1m on advertising, profit.

[dmix]: You can spot vibecoded websites by how they include the prompt or commit-style comments into the literal interface, instead of communicating it via visual context (or simply excluding it) &gt; Sort by any column; values the run could not produce always sort last. Hover a cost for how it was priced, a latency for the endpoint. Names link to each project. A designer would never write this, but an LLM just inserts it by making it small grey text next to the interface, just like it does with inan...

[ks2048]: I was trying to figure out what exactly the tests here are. I guess I found some of the questions (here:  https:&#x2F;&#x2F;github.com&#x2F;fstandhartinger&#x2F;jevbench&#x2F;blob&#x2F;main&#x2F;datase... ) e.g.,     &quot;instructions&quot;: &quot;Which intent does the user&#x27;s message express?&quot;,
  &quot;labels&quot;:[&quot;set_alarm&quot;, &quot;play_music&quot;, &quot;weather&quot;, &quot;send_message&quot;, &quot;turn_off_lights&quot;],
  &quot;state&quot;: &quot;Play some Taylor ...

[adityamishra241]: How do you handle task distribution and prevent the benchmark from favoring models that are tuned specifically to these 534 questions?

[sean_pedersen]: Good project but this one also exists  https:&#x2F;&#x2F;huggingface.co&#x2F;spaces&#x2F;multimodalart&#x2F;jev-decision-ind...  and the results do not seem to add up and also model sets are different... still needs time to mature likely

</details>
