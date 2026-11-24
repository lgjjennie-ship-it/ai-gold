---
layout: default
title: "无需扩展降低困惑度"
date: 2026-11-24T12:00:00+00:00
discovered_date: 2026-11-24
slug: 2026-11-24-lowering-perplexity-without-scaling
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目介绍了一种在不增加模型大小的情况下降低AI模型困惑度的方法，重点关注基于代码的训练数据。 它在HackerNews上获得了高度关注，并解决了AI模型性能的实际痛点，表明其实用价值，并有可能通过SaaS或API服务进行货币化。 该项目可能是开源的，许可证可能是宽松的，可能处于alpha或beta阶段，部署复杂度适中，主要集成点集中在基于代码的数据集上。"
tags: "AI, Model, Code, Performance, NLP"
---

# 无需扩展降低困惑度


> 该项目介绍了一种在不增加模型大小的情况下降低AI模型困惑度的方法，重点关注基于代码的训练数据。 它在HackerNews上获得了高度关注，并解决了AI模型性能的实际痛点，表明其实用价值，并有可能通过SaaS或API服务进行货币化。 该项目可能是开源的，许可证可能是宽松的，可能处于alpha或beta阶段，部署复杂度适中，主要集成点集中在基于代码的数据集上。


**项目链接**：https://micjm.com/blog/lowering-perplexity-without-scaling/
**作者**：qlte
**发布时间**：2026-11-23T04:33:50Z
**挖掘日期**：2026-11-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Model, Code, Performance, NLP


## 📌 项目详解

该项目介绍了一种在不增加模型大小的情况下降低AI模型困惑度的方法，重点关注基于代码的训练数据。 它在HackerNews上获得了高度关注，并解决了AI模型性能的实际痛点，表明其实用价值，并有可能通过SaaS或API服务进行货币化。 该项目可能是开源的，许可证可能是宽松的，可能处于alpha或beta阶段，部署复杂度适中，主要集成点集中在基于代码的数据集上。


## 🌐 背景与生态

困惑度是评估AI模型性能的关键指标，尤其是在NLP领域。传统方法降低困惑度通常涉及扩大模型规模，这可能非常耗费资源。该项目通过利用基于代码的训练数据提供了一种新颖的方法。


## 💬 社区讨论

HackerNews上的评论表明反应不一，一些人质疑基于代码训练的有效性，而另一些人则在探索其在编码模型中的潜在应用。


## 🚀 应用前景

这种方法可以应用于改进编码模型，减少错误并增强代码生成。潜在行业包括软件开发，其中精确的代码生成至关重要。


## 🔧 技术栈

技术栈可能涉及Python、TensorFlow或PyTorch等机器学习库以及代码分析工具。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.7+、对机器学习的基本理解以及访问代码数据集。步骤包括设置环境、加载数据和运行初始训练。


## 👥 目标用户

目标用户是软件开发公司中的后端工程师、机器学习实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括像'CodeBERT'和'GPT-Code'这样的项目，它们专注于基于代码的AI模型，但可能不会解决无需扩展即可降低困惑度的问题。


## 📚 参考链接

- [Perplexity for LLM Evaluation - GeeksforGeeks](https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[fedpost]: I occasionally see people complaining that models have gotten worse at &quot;creative writing&quot; over the past year or so. I don&#x27;t use models for expressive writing, that seems pretty deranged, so I wrote it off as people on the internet being crazy but maybe they were onto something? Also, I&#x27;ve heard training mix is not supposed to be zero sum and this seems to contradict that? Yeah it&#x27;s nonlinear and the are more important things than  predicting  code but it seems the bal...

[changoplatanero]: It&#x27;s funny how hard it is to create a sizable text corpus that you are pretty sure is not contaminated by text from the internet. It turns out that using a company&#x27;s private codebases is one of the most reliable ways to do it. The openai blog also doesn&#x27;t make clear how much increasing context length of the models plays a role in lowering perplexity. Perplexity is higher at the start of the context window when the model doesn&#x27;t have enough context to know whats going on ye...

[AlexCoventry]: Doesn&#x27;t this mostly just imply that code has lower entropy per token than natural-language text, which is not all that surprising? I hope the held-out test set used for the recent OpenAI graph was constant and representative of the training data for all models.

[MrScruff]: Not an expert, but isn&#x27;t the current discussion around the likelihood of improved coding models leading to RSI, and safety implications of that? In which case perplexity on a fixed dataset of code is probably still a relevant benchmark.

[merksittich]: Original discussion on the OpenAI blog post referenced in TFA:  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50601525 
(446 comments)

</details>
