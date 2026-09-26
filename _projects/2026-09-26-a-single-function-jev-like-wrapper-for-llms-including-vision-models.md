---
layout: default
title: "一个类似Jev的LLM和视觉模型包装器"
date: 2026-09-26T12:00:00+00:00
discovered_date: 2026-09-26
slug: 2026-09-26-a-single-function-jev-like-wrapper-for-llms-including-vision-models
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目提供了一个类似Jev的LLM和视觉模型包装器，通过缓存和JSON响应简化了它们的使用，使复杂的AI交互更加易于访问。 拥有58个星标和活跃的讨论，显示了社区对简化AI使用的兴趣。它解决了对更友好的AI工具的需求，可能提供SaaS或API的盈利路径。 该项目在开源许可证下，处于alpha阶段，表明可能存在错误和有限的功能。它需要一些技术设置，可能比替代方案慢。"
tags: "LLM, Agent, RAG, Image, Code"
---

# 一个类似Jev的LLM和视觉模型包装器


> 该项目提供了一个类似Jev的LLM和视觉模型包装器，通过缓存和JSON响应简化了它们的使用，使复杂的AI交互更加易于访问。 拥有58个星标和活跃的讨论，显示了社区对简化AI使用的兴趣。它解决了对更友好的AI工具的需求，可能提供SaaS或API的盈利路径。 该项目在开源许可证下，处于alpha阶段，表明可能存在错误和有限的功能。它需要一些技术设置，可能比替代方案慢。


**项目链接**：http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html
**作者**：allanrbo
**发布时间**：2026-09-26T04:20:58Z
**挖掘日期**：2026-09-26
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Image, Code


## 📌 项目详解

该项目提供了一个类似Jev的LLM和视觉模型包装器，通过缓存和JSON响应简化了它们的使用，使复杂的AI交互更加易于访问。 拥有58个星标和活跃的讨论，显示了社区对简化AI使用的兴趣。它解决了对更友好的AI工具的需求，可能提供SaaS或API的盈利路径。 该项目在开源许可证下，处于alpha阶段，表明可能存在错误和有限的功能。它需要一些技术设置，可能比替代方案慢。


## 🌐 背景与生态

该项目属于AI包装器和代理的生态系统，提供了一种简化LLM和视觉模型使用的新方法。AI的最新进展和对易于访问的AI工具日益增长的需求使该项目现在具有相关性。


## 💬 社区讨论

社区评论表达了不同的看法：一些人对其潜力感到兴奋，而另一些人则对性能和成本表示怀疑，暗示它可能比替代方案慢且更昂贵。


## 🚀 应用前景

它可以在需要简化AI交互的场景中发挥作用，例如客户服务机器人或数据分析工具。通过SaaS或API进行盈利，可针对医疗保健或零售等行业。


## 🔧 技术栈

技术栈可能包括Python、缓存机制，并可能使用Flask或FastAPI等框架进行API创建。它可能使用GPT-4等LLM和OpenCV等库来集成视觉模型。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、LLM的API密钥以及对JSON的基本理解。步骤包括克隆存储库、安装依赖项并运行示例脚本。


## 👥 目标用户

目标用户是需要将LLM和视觉模型集成到他们的应用程序中，但不需要在每个模型方面都具备深厚专业知识的开发人员和AI从业者。


## ⚖️ 类似项目对比

竞争对手包括Jevper，因其类型安全的方法，以及其他LLM包装器如LangChain。该项目通过专注于缓存和JSON响应来区分，但在性能方面可能落后。


## 📚 参考链接

- [Allan's Blog: A Jev-like wrapper for LLMs, including vision models](http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html)
- [GitHub - zhulinchng/jevper: Jev-shaped (TypeSafe System One) classification wrapper over OpenAI-like clients: probabilities and confidence instead of prose · GitHub](https://github.com/zhulinchng/jevper)
- [Jev Use Cases and Examples: 1,300+ Real Builds (2026) | AY Automate](https://www.ayautomate.com/jev-builds)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[TeMPOraL]: Now  this  is how[0] we get some of the most magical Star Trek technology that eludes us to this day, such as  automatic doors . Because if you notice, they work much,  much  better than real-life ones, because they seem to be doing something like this:     if(within 10 meters of door then) {
    if(Jev(
       [A] Intends to go through, expects doors to open
       [B] Approaches with no intent to pass
       [C] Passing by, loiters, or otherwise
       [D] Other
    ) == most definitely A) ...

[frabcus]: Presumably this is much less good than Jev, because the normal LLM models have been trained with RLHF and to be agents. Especially on a large model, I&#x27;d expect it to decide in an earlier layer. I&#x27;d hope whatever Jev&#x27;s Reinforcement Learning for Calibrated Decisions (RLCD) does is better at training the models to give accurate probabilities in the weights.

[prathje]: Nice! I would love to use it for images as well.
Then again is using Grammar-Based Decoding with a json response not the same? Is Jev just that with nice caching?
Because then I have been using that already…

[arcticbull]: Ah sweet it’s like Jev but several order of magnitude more expensive, and slower too.

[Havoc]: Likely works even better with fireworks ai since they have proper grammar support

</details>
