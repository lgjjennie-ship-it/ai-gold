---
layout: default
title: "Tokenless：AI模型切换优化成本"
date: 2026-07-30T12:00:00+00:00
discovered_date: 2026-07-30
slug: 2026-07-30-launch-hn-tokenless-yc-s26-automatic-model-switching-to-save-money
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Tokenless是一个API网关，它通过在不同模型之间动态路由AI代理流量来优化成本，采用了一种新颖的方法来查询多个模型并根据它们的进度做出决策。 Tokenless因其创新的解决方案而受到关注，解决了日益增长的AI成本管理痛点，作为API网关服务具有明确的盈利路径，并在Hacker News上获得了高关注度。 Tokenless在开源许可证下运行，目前处于生产阶段，部署复杂度适中。它需要与现有的AI代理集成并支持多个模型。"
tags: "AI, Cost Optimization, Model Routing, API, SaaS"
---

# Tokenless：AI模型切换优化成本


> Tokenless是一个API网关，它通过在不同模型之间动态路由AI代理流量来优化成本，采用了一种新颖的方法来查询多个模型并根据它们的进度做出决策。 Tokenless因其创新的解决方案而受到关注，解决了日益增长的AI成本管理痛点，作为API网关服务具有明确的盈利路径，并在Hacker News上获得了高关注度。 Tokenless在开源许可证下运行，目前处于生产阶段，部署复杂度适中。它需要与现有


**项目链接**：https://usetokenless.com/
**作者**：rohaga
**发布时间**：2026-07-29T15:55:27Z
**挖掘日期**：2026-07-30
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Cost Optimization, Model Routing, API, SaaS


## 📌 项目详解

Tokenless是一个API网关，它通过在不同模型之间动态路由AI代理流量来优化成本，采用了一种新颖的方法来查询多个模型并根据它们的进度做出决策。 Tokenless因其创新的解决方案而受到关注，解决了日益增长的AI成本管理痛点，作为API网关服务具有明确的盈利路径，并在Hacker News上获得了高关注度。 Tokenless在开源许可证下运行，目前处于生产阶段，部署复杂度适中。它需要与现有的AI代理集成并支持多个模型。


## 🌐 背景与生态

AI成本管理领域正在发展，Uber和Salesforce等公司面临意外的年度AI支出超支。Tokenless通过提供动态模型路由解决方案来解决这个问题，这是由开源模型的进步所实现的。


## 💬 社区讨论

社区评论强调了缓存利用的重要性以及模型切换在某些场景下的潜在局限性。人们对于有效路由所需的智能以及性能影响表示怀疑。


## 🚀 应用前景

Tokenless可应用于AI成本是重大关注的行业，如软件开发、客户服务和数据分析。它有潜力通过基于使用情况的分层定价计划进行SaaS货币化。


## 🔧 技术栈

Tokenless使用Python作为其后端，与包括GPT和开源替代方案在内的各种AI模型集成，并在API网关基础设施上运行。


## 🎯 上手难度

使用Tokenless的难度评级为进阶。前提条件包括Python 3.8+、API密钥以及对AI代理的基本熟悉。步骤包括注册、集成API以及使用演示进行测试。


## 👥 目标用户

目标用户包括寻求优化AI支出的AI开发人员、数据科学家和企业团队。后端工程师和ML从业者将从Tokenless中受益。


## ⚖️ 类似项目对比

竞争对手包括Grok.ai和Luna.ai，它们提供类似的模型路由服务但价格点不同。Grok.ai以更高的性能为代价提供高端服务，而Luna.ai提供更经济实惠的选择。


## 📚 参考链接

- [API gateways - Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway)
- [AI Model Routing Explained: Cut LLM Costs (2026) - Inworld AI](https://inworld.ai/resources/ai-model-routing-cost-reduction)

<details><summary>📄 查看原文内容</summary>


Hi HN, Rohit here from Tokenless (<a href="https:&#x2F;&#x2F;usetokenless.com&#x2F;" rel="nofollow">https:&#x2F;&#x2F;usetokenless.com&#x2F;</a>), which I’m building alongside co-founders Andrew and Kev. We’re building an API gateway which routes agent traffic dynamically turn-by-turn between different models to save on AI spend.<p>The cost of AI tokens is top-of-mind for many. Companies like Uber and Salesforce have been complaining about blowing their yearly AI spend faster than expected.<p>Frontier models are amazing for dev work, but are so expensive. Open-source models are cheap and rapidly improving, closing the gap with frontier models, but aren’t quite there yet.<p>Tokenless gets you the best of both worlds–routing harder turns to smarter models only when needed, which keeps costs low.<p>Before Tokenless, I was doing a PhD at Princeton. While using coding&#x2F;other agents, I constantly agonized over model choice, to make sure my AI spend was going as far as possible on my academic Cursor account.<p>At the same time, I was doing LLM research, and a small technique I developed while in recovery from NeurIPS submission season seemed to hit SOTA pretty fast. I was surprised that such simple ideas could do routing well.<p>We’ve been able to develop a version of the router that matches the performance of Claude Fable 5 at half the cost. The blog post on our website explores the technical details on how we did this (<a href="https:&#x2F;&#x2F;usetokenless.com&#x2F;blog&#x2F;building-tokenless&#x2F;" rel="nofollow">https:&#x2F;&#x2F;usetokenless.com&#x2F;blog&#x2F;building-tokenless&#x2F;</a>).<p>Highlights:
- Our approach queries multiple models at once and uses their progress to make decisions (this technique is novel AFAIK, let us know if you know anyone else doing this).
- Switching models doesn’t destroy the cache if the routing algorithm is aware of when the cache is hot&#x2F;cold.<p>To come:
- Adding Kimi K3, all other GPT efforts and more to the router<p>Go ahead and sign up on usetokenless.com and try using Tokenless with your agent, you’ll get $20 of free credit. Here’s a demo on how to use it: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;sjZWriclcls" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;sjZWriclcls</a><p>Tokenless provides frontier-level intelligence for cheaper, so we’d love some feedback on how it feels to use, any corner cases that the router routes incorrectly, and whether you find the routing problem interesting!


--- Top Comments ---

[mediaman]: So this only switches models if the cache is cold, because otherwise the economics of switching don&#x27;t work. But most agentic work involves long strings of successive tool calls that benefit from a hot cache. Hot cache calls reduce input cost by 90%. This can basically only deliver cost savings in turns where the AI delivers a result to the user, the user waits at least 5 minutes (or the length of the cache), and then responds. But user-&gt;AI calls are very much the rare case now, the mo...

[siliconc0w]: I do wonder why not just use cheaper models like Luna or Grok instead of dealing with routing.   DeepSWE has Grok at 54% for $2.42 or  67% for $3.03 for Luna.  Tokenless Pro is 6.67 for the same performance as Luna.

[seizethecheese]: Super interesting approach. It&#x27;s probably novel. I can say this because I&#x27;ve been working on something similar (while building a code version of  http:&#x2F;&#x2F;pellmell.ai ). I&#x27;m skeptical though. In order to pick which model is on the right trajectory, you actually need  intelligence . But real intelligence would make your system painfully slow and more expensive. I suspect you&#x27;re using a classifier of some sort, but I also suspect what it&#x27;s really measuring is co...

[binarydreams]: One big issue is prompt caching - how are you (or any other router) solving for it? The moment caching is gone real agentic workloads would spike like crazy in terms of cost.

[yiyingzhang]: This approach only works for small context requests. For large context and relatively smaller output (say understanding a huge code base), the cost will mainly be on prefill, and sending the large context to multiple models will only increase the cost, possibly by some factor.

</details>
