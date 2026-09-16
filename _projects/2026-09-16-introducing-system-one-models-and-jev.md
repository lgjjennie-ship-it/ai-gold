---
layout: default
title: "系统一模型和杰夫"
date: 2026-09-16T12:00:00+00:00
discovered_date: 2026-09-16
slug: 2026-09-16-introducing-system-one-models-and-jev
source: hackernews
category: show-hn
ai_score: 8.0
summary: "系统一模型和杰夫引入了一种使用LLM生成结构化输出的新方法，这些输出可以集成到软件中，用于分类和决策等任务。 该项目现在值得关注，因其在高星数和评论数（Hacker News上1340个点数和387条评论）的高牵引力，表明了强烈的社区兴趣。它结合了LLM和结构化输出，提供了一种新颖的方法，可以解决软件开发中的实际问题，特别是在分类和决策任务中。通过SaaS或API提供结构化输出服务，存在货币化潜力。 该项目采用开源许可证，似乎处于生产成熟度，部署复杂度适中。它需要与现有软件系统集成，并且可能对硬件有要求以实现最佳性能。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# 系统一模型和杰夫


> 系统一模型和杰夫引入了一种使用LLM生成结构化输出的新方法，这些输出可以集成到软件中，用于分类和决策等任务。 该项目现在值得关注，因其在高星数和评论数（Hacker News上1340个点数和387条评论）的高牵引力，表明了强烈的社区兴趣。它结合了LLM和结构化输出，提供了一种新颖的方法，可以解决软件开发中的实际问题，特别是在分类和决策任务中。通过SaaS或API提供结构化输出服务，存在货币化潜力


**项目链接**：https://typesafe.ai/blog/introducing-system-one-models-and-jev
**作者**：albelfio
**发布时间**：2026-09-15T19:25:03Z
**挖掘日期**：2026-09-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

系统一模型和杰夫引入了一种使用LLM生成结构化输出的新方法，这些输出可以集成到软件中，用于分类和决策等任务。 该项目现在值得关注，因其在高星数和评论数（Hacker News上1340个点数和387条评论）的高牵引力，表明了强烈的社区兴趣。它结合了LLM和结构化输出，提供了一种新颖的方法，可以解决软件开发中的实际问题，特别是在分类和决策任务中。通过SaaS或API提供结构化输出服务，存在货币化潜力。 该项目采用开源许可证，似乎处于生产成熟度，部署复杂度适中。它需要与现有软件系统集成，并且可能对硬件有要求以实现最佳性能。


## 🌐 背景与生态

系统一模型和杰夫位于AI驱动软件开发工具的生态系统中。替代方案包括传统的基于规则的系统和其他基于LLM的工具。最近LLM的进步使结构化输出生成更加可行和 relevant。


## 💬 社区讨论

社区评论非常热情，用户强调了基因alogical树匹配、分类和决策等用例。有些人对速度比较持怀疑态度，并建议更清晰的标题。


## 🚀 应用前景

该项目可以通过为分类和决策等任务生成结构化输出来解决软件开发中的实际问题。潜在应用包括SaaS服务、API提供以及集成到企业系统中以提高效率。


## 🔧 技术栈

核心技术栈包括LLM、结构化输出生成框架和集成工具。它可能依赖于Python等语言和Transformers等框架。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、GPU和API密钥。大致步骤到第一个工作结果包括设置环境、安装依赖项和运行示例脚本。


## 👥 目标用户

该项目面向在软件开发和AI领域工作的个人开发者、企业团队和研究人员。角色包括后端工程师、ML从业者以及DevOps专业人员。


## ⚖️ 类似项目对比

竞品或相关项目包括OpenAI的GPT-4、Hugging Face的Transformers和Google的BERT。这些在模型大小、速度和专用用例方面有所不同。


## 📚 参考链接

- [TypeSafe Jev Review: The AI Model That Doesn’t Generate... - Kingy AI](https://kingy.ai/blog/typesafe-jev-review-the-ai-model-that-doesnt-generate-text/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[vintermann]: &gt; Structured outputs slot into ordinary software as fuzzy decision rules: classify, route, score, extract, or branch where hand-written logic is too brittle. Oh, I have one of those use cases, matching people in genealogy trees. You can ask all sorts of questions: do the names match? Do they match within some edit distance? Do they match according to soundex&#x2F; metaphone rules (which are themselves a ginormous set of rules for letters and letter combinations which may or may not result ...

[jacobgold]: First, congrats to the team on launching something genuinely interesting and new. Seems like a more accurate title would be &quot;Jev: Trading general purpose generation for fast typed inference&quot; or something like that. This is interesting, but the speed comparison seems misleading? A generative model that can output code in a Turing-complete language can do anything a computer can do. Jev can only generate structured output, right? This is probably super useful for classification&#x2F;r...

[cfowles]: Wasn&#x27;t really till seeing this home assistant demo they have ( https:&#x2F;&#x2F;www.loom.com&#x2F;share&#x2F;18c4dbcf8db546dfb2d7f2ef018e78e4 ) that the value really clicked for me. Seems really cool.

[futurisold]: This, combined with contracts, could make a lot of things so much fun now! For those who don&#x27;t know (which is probably everyone but me), I ported the design-by-contract pattern in Python and combined it with LLMs. This was early 2025. I originally wrote about it here:  https:&#x2F;&#x2F;leoveanu.com&#x2F;2025-03-01-dbc&#x2F; 
. Contracts are a core feature of SymbolicAI ever since. The community seems to have loved it too ( https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44399234 ). ...

[maltalex]: This is a very promising idea - a model that takes arbitrary text input (which can be a complex json), plus a set of questions (yes&#x2F;no, multiple-choice, or score) and quickly (milliseconds) and cheaply ($0.042&#x2F;MTok) answers those questions. Unfortunately, none of this is explained in the announcement, but the documentation [0] is pretty good. [0]:  https:&#x2F;&#x2F;docs.typesafe.ai&#x2F;concepts&#x2F;how-to-build-with-system-o...

</details>
