---
layout: default
title: "Spotify的Portal用于AI token优化"
date: 2026-09-05T12:00:00+00:00
discovered_date: 2026-09-05
slug: 2026-09-05-portal-by-spotify-cut-my-claude-code-token-usage-by-90
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Spotify的Portal通过将文件读取和样板代码生成委托给Gemini 2.5 Flash，将Claude Code的token使用量减少90%，并将Claude保留用于推理任务。 该项目因其高社区参与度、在降低token成本方面的实用价值以及通过SaaS或API进行货币化的潜力而具有重要意义。其创新的模型路由方法解决了日益增长的AI效率需求。 该项目采用开源许可证，似乎处于生产阶段，部署复杂度适中。它需要与AI模型API集成，并且可能因所使用的模型而异，存在硬件限制。"
tags: "AI, Token Optimization, Claude Code, Efficiency, SaaS"
---

# Spotify的Portal用于AI token优化


> Spotify的Portal通过将文件读取和样板代码生成委托给Gemini 2.5 Flash，将Claude Code的token使用量减少90%，并将Claude保留用于推理任务。 该项目因其高社区参与度、在降低token成本方面的实用价值以及通过SaaS或API进行货币化的潜力而具有重要意义。其创新的模型路由方法解决了日益增长的AI效率需求。 该项目采用开源许可证，似乎处于生产阶段，部署复杂


**项目链接**：https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90
**作者**：cebert
**发布时间**：2026-09-04T23:38:50Z
**挖掘日期**：2026-09-05
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Token Optimization, Claude Code, Efficiency, SaaS


## 📌 项目详解

Spotify的Portal通过将文件读取和样板代码生成委托给Gemini 2.5 Flash，将Claude Code的token使用量减少90%，并将Claude保留用于推理任务。 该项目因其高社区参与度、在降低token成本方面的实用价值以及通过SaaS或API进行货币化的潜力而具有重要意义。其创新的模型路由方法解决了日益增长的AI效率需求。 该项目采用开源许可证，似乎处于生产阶段，部署复杂度适中。它需要与AI模型API集成，并且可能因所使用的模型而异，存在硬件限制。


## 🌐 背景与生态

随着成本的上升，AI token优化成为一个关键领域。Spotify的Portal通过模型路由优化token使用量，这一细分领域由于前沿AI模型的高成本而获得了关注。


## 💬 社区讨论

社区评论表达了不同的观点：一些人兴奋于效率的提高，而另一些人则怀疑其在实际场景中的实用性和成本节约。


## 🚀 应用前景

这项技术可应用于软件开发、数据分析和内容生成行业。潜在产品包括用于AI编码辅助的SaaS平台和用于token优化的API服务。


## 🔧 技术栈

技术栈包括Python、Spotify的Portal API、Claude Code和Gemini 2.5 Flash。基础设施涉及API集成和模型管理。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、Claude Code和Gemini 2.5 Flash的API密钥。步骤包括设置环境、集成API和配置模型路由。


## 👥 目标用户

目标用户包括后端工程师、DevOps团队以及软件开发和数据分析行业的AI从业者。


## ⚖️ 类似项目对比

竞品包括用于token优化的'ssemble'和用于模型切换的OpenRouter。这些替代品侧重于token效率和模型选择的不同方面。


## 📚 参考链接

- [Portal by Spotify cut my Claude Code token usage by 90% ...](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
- [Spotify's Portal Cuts AI Coding Token Costs 90% With Model ...](https://news.lavx.hu/article/spotify-s-portal-cuts-ai-coding-token-costs-90-with-model-routing)
- [Portal by Spotify cut my Claude Code token usage by 90%](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[pmdr]: I wish websites would stop messing with the scrolling behavior.

[sognetic]: There are a bunch of approaches that do this kind of thing to reduce token usage (&quot;semble&quot; came to mind, technically different but functionally similar) but their performance is usually mixed because the models haven&#x27;t been RL tuned to use them as they have the default tool suite. Combine that with the incentive by Anthropic et al. to make you actually burn through as many tokens as possible and I don&#x27;t see these kind of things becoming mainstream yet. Maybe once we reach ...

[solenoid0937]: So this is just delegating certain work to dumber models? I certainly wouldn&#x27;t use Gemini 2.5 Flash (!!?) for code writing as suggested. I&#x27;ve never had an issue with Codex or Claude reading massive files, they&#x27;re really good at precise greps.

[jnwatson]: It cuts token usage because they are using a different service with a different token budget for the reader&#x2F;code writer tasks. You can also just delegate this to subagents with Claude Code (though you have a more limited choice of models unless you swap the cheaper models via OpenRouter). I&#x27;m OK using a dumb model as a smart grep, but the whole point of using the frontier models is using their intelligence for the hard stuff like coding.

[faangguyindia]: It doesn&#x27;t work well in practice. Try it yourself, use a big model like Opus or Sol to implement everything by first making a plan using plan mode. Then try distributing the task to a cheaper models like Luna Max or Gemini Flash 3.8. During planning, the big model already reads the relevant files in context, while giving a smaller model a slice of work itself requires the big model to reason about the task distribution, review, etc. So do you really save on tokens?

</details>
