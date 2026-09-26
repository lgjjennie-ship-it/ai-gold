---
layout: default
title: "Ollaya决策模型"
date: 2026-09-26T12:00:00+00:00
discovered_date: 2026-09-26
slug: 2026-09-26-ollaya-ollama-for-open-source-jev-style-decision-models
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Ollaya是一个开源项目，旨在使用与Ollama类似的技巧为AI应用复制Jev式决策模型。 该项目有442个星标和117条评论，显示出社区的兴趣。它为决策模型提供了一种新颖的方法，这可能对AI初创公司具有重要意义。 该项目在开源许可下，似乎处于alpha阶段，部署需要本地GPU基础设施。"
tags: "LLM, Decision Models, Open Source, AI, Tools"
---

# Ollaya决策模型


> Ollaya是一个开源项目，旨在使用与Ollama类似的技巧为AI应用复制Jev式决策模型。 该项目有442个星标和117条评论，显示出社区的兴趣。它为决策模型提供了一种新颖的方法，这可能对AI初创公司具有重要意义。 该项目在开源许可下，似乎处于alpha阶段，部署需要本地GPU基础设施。


**项目链接**：https://ollaya.dev/
**作者**：Ardakilic
**发布时间**：2026-09-25T18:33:50Z
**挖掘日期**：2026-09-26
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：LLM, Decision Models, Open Source, AI, Tools


## 📌 项目详解

Ollaya是一个开源项目，旨在使用与Ollama类似的技巧为AI应用复制Jev式决策模型。 该项目有442个星标和117条评论，显示出社区的兴趣。它为决策模型提供了一种新颖的方法，这可能对AI初创公司具有重要意义。 该项目在开源许可下，似乎处于alpha阶段，部署需要本地GPU基础设施。


## 🌐 背景与生态

Jev式决策模型是用于做出结构化决策的小型AI模型，例如选择合适的工具或对搜索结果进行排序。Ollama是一个用于运行本地大型语言模型（LLMs）的工具。


## 💬 社区讨论

社区评论对该项目的创新及其对AI初创公司的影响表示怀疑，一些用户质疑Jev式模型与传统重排序器的实用性。


## 🚀 应用前景

Ollaya可用于需要客户服务、支持或内容审核中结构化决策的AI初创公司和 enterprises。潜在的盈利路径包括SaaS或API服务。


## 🔧 技术栈

技术栈可能包括与Ollama类似的Python，并可能涉及用于模型训练和推理的机器学习库，如PyTorch或TensorFlow。


## 🎯 上手难度

难度：进阶。前提条件包括本地GPU、Python 3.8+以及熟悉命令行工具。安装涉及下载仓库并运行设置脚本。


## 👥 目标用户

目标用户包括AI开发者、数据科学家以及从事决策系统开发的企业团队。


## ⚖️ 类似项目对比

竞品包括System One Models和传统的BERT-Reranker等重排序工具。这些替代方案可能为决策任务提供更成熟的解决方案。


## 📚 参考链接

- [Ollama](https://en.wikipedia.org/wiki/Ollama)
- [Jev Models Explained [2026]: Routing, Reranking, JSON](https://www.kunalganglani.com/blog/jev-models-explained-routing)
- [What Is Jev ? TypeSafe AI’s System One Model for AI Decisions](https://imini.com/blogs/jev-ai-model)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[pradn]: I&#x27;m not sure what this means for AI startups if their innovations can be copied by OSS so quickly (what, like 2 weeks?). There&#x27;s &quot;consumer surplus&quot; for everyone, to borrow an economic concept. But we do ideally want some of the surplus to flow to the innovator, too. I know there were precursors, but that&#x27;s fine - it&#x27;s hard to have a totally novel idea in such a popular field. I don&#x27;t know what the end game is for TypeSafe - they&#x27;d need to demonstrate pe...

[fooker]: For everyone dismissing Jev&#x27;s innovation as being trivial, no it&#x27;s not. It is definitely not the MNIST classifier you had trained in 2019. The difference is that you only train it once and the modern LLM machinery sort of takes care of that with large contexts. It&#x27;s great that Jev proved this is a viable product. I&#x27;d expect a great many research innovations coming from making this work better&#x2F;faster&#x2F;cheaper, and around interfacing modern agents with it.

[george_max]: Has anyone actually seen better or the same results with Laya compared to Jev? From my experience, Laya performs significantly worse. It&#x27;s less confident and often makes wrong decisions with more complex queries.

[alex7o]: Guys I have a real q, what is the difference between an instruct based re-ranker and laya&#x2F;jev I just don&#x27;t see it. Edit: One is that jev&#x2F;laya are tuned to have better probabilities, but a reranker can be fine tuned to do that as well. And jev&#x2F;laya use RLCD?

[solaire_oa]: I installed it, I tried the examples, it works.... But forgive my lack of imagination... what is this useful for? Like, their example is of classification for a support interface.... `refund_requested`. Pretty convenient bool given the example is about a refund- what if 99% of submissions don&#x27;t ask about a refund? Also, is that user not a `churn_risk`? What could possibly qualify as a churn risk if not a user asking for a refund?  https:&#x2F;&#x2F;ollaya.dev&#x2F;library&#x2F;laya  The ...

</details>
