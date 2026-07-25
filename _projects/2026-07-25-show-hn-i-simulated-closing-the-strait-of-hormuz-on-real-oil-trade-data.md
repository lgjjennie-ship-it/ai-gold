---
layout: default
title: "石油贸易模拟工具"
date: 2026-07-25T12:00:00+00:00
discovered_date: 2026-07-25
slug: 2026-07-25-show-hn-i-simulated-closing-the-strait-of-hormuz-on-real-oil-trade-data
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该可视化工具使用真实数据，模拟封锁霍尔木兹海峡对全球石油贸易的影响，基于Eisenberg-Noe金融网络模型，针对石油消耗和双边贸易进行了调整。 该项目因其新颖的全球石油贸易影响可视化方法、解决现实问题的教育价值以及在Hacker News上的中等关注度而值得关注。 该工具在宽松的许可证下开源，目前处于alpha阶段，使用Flask和JavaScript前端，运行需要一定的技术知识。"
tags: "Oil, Trade, Visualization, Simulation, SupplyChain"
---

# 石油贸易模拟工具


> 该可视化工具使用真实数据，模拟封锁霍尔木兹海峡对全球石油贸易的影响，基于Eisenberg-Noe金融网络模型，针对石油消耗和双边贸易进行了调整。 该项目因其新颖的全球石油贸易影响可视化方法、解决现实问题的教育价值以及在Hacker News上的中等关注度而值得关注。 该工具在宽松的许可证下开源，目前处于alpha阶段，使用Flask和JavaScript前端，运行需要一定的技术知识。


**项目链接**：https://globaloilnetwork.staffinganalytics.io/
**作者**：eliotho
**发布时间**：2026-07-23T12:31:21Z
**挖掘日期**：2026-07-25
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Oil, Trade, Visualization, Simulation, SupplyChain


## 📌 项目详解

该可视化工具使用真实数据，模拟封锁霍尔木兹海峡对全球石油贸易的影响，基于Eisenberg-Noe金融网络模型，针对石油消耗和双边贸易进行了调整。 该项目因其新颖的全球石油贸易影响可视化方法、解决现实问题的教育价值以及在Hacker News上的中等关注度而值得关注。 该工具在宽松的许可证下开源，目前处于alpha阶段，使用Flask和JavaScript前端，运行需要一定的技术知识。


## 🌐 背景与生态

该项目位于石油贸易和供应链生态系统，与传统经济模型相比提供了独特的视角。它基于Eisenberg-Noe模型，将其应用于石油贸易。


## 💬 社区讨论

评论表明人们对模型的见解感兴趣，但也提出了关于其局限性的问题，例如排除中国和补贴石油，以及对其实际预测能力的怀疑。


## 🚀 应用前景

该工具可用于大学的教育目的，供政策制定者了解供应链脆弱性，或由能源公司模拟贸易中断。作为SaaS工具的货币化是可能的。


## 🔧 技术栈

技术栈包括Flask用于后端和JavaScript用于前端，可视化可能由LLM辅助。它使用真实的石油贸易数据。


## 🎯 上手难度

难度：进阶。前提条件包括Python和对石油贸易基础的理解。步骤涉及设置环境和运行Flask应用程序。


## 👥 目标用户

目标用户是需要了解复杂贸易动态的研究人员、供应链或经济学专业的学生和能源分析师。


## ⚖️ 类似项目对比

竞品包括'全球石油贸易网络'和基于网络理论的学术模型，尽管该项目的实时可视化重点是独特的。


## 📚 参考链接

- [Systemic Risk in Financial Networks by Larry Eisenberg, Thomas H. Noe :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=173249)
- [Global oil trading networks: Structural patterns and geopolitical risks - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0140988325007923)

<details><summary>📄 查看原文内容</summary>


OP here: I created this visualization tool as the byproduct of a supply chain class I taught at Columbia. The pedagogical exercise grew into a full blown visualization and paper about global oil trade.<p>The model:
The mechanics are the same as the financial network Eisenberg-Noe: Instead of banks, every country consumes oil interconnected via bilateral trading. Shocks propagate throughout the network, depleting oil reserves when bottleneck nodes (such as the Strait of Hormuz) are blocked.<p>Insights:
The interesting part is the mechanics of how the crisis unfolds: for example, France receives 0 oil from Hormuz directly, yet their reserves are depleted faster because other countries reactively increase their safety oil stock, increasing oil price, making stockouts more expensive for everyone.<p>The model also gives price dynamics which are interesting on their own: the price increase is not immediate, it follows sequentially as countries reserves deplete.<p>Some caveats:
1. For producer nodes, depletion means their export slack is reduced&#x2F;exhausted.
2. No sanctioned trade (UN Comtrade data)<p>Technical Details:
The visualization is 600 lines of flask plus js frontend (LLM assisted visualization with ground-truth matching the original numerical exercise of the paper)<p>Paper with proofs&#x2F;theory:
<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2607.17491" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2607.17491</a>


--- Top Comments ---

[anigbrowl]: An interesting fact to consider is that the US stockpile (the Strategic Petroleum Reserve) is reported as the total of sour (high sulfur) and sweet (low sulfur) crude oil. The sweet stock makes up about 1&#x2F;3 of the reserve and hardly varies at all. This is because US refineries are virtually all configured for sour crude: due to a mistaken belief in the 1990s that sweet crude was running out, the industry bet the farm on sour crude refining, and if sour crude runs low, it&#x27;s extremely...

[neom]: Tangentially related but just watched this pretty interesting youtube mini-doc-thing about the recent moves China has been making regarding oil (and its bigger picture):  https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=BkA0bkb6ZO0

[HarHarVeryFunny]: What concrete predictions does your model make? What developments in pricing&#x2F;other would indicate that your model is wrong or incomplete? Nice website regardless, but I&#x27;m a bit skeptical that the dynamics of the global oil&#x2F;energy market can be accurately predicted.

[Haven880]: The biggest missing piece is China. Assuming actual delivered price is not subsidized by Western countries, you need to put in what if China demands that reflect the current price. Chinese in reality don&#x27;t consume that much oil as what we thot they do from the oil purchases in the past. I assume Chinese just ramp down the purchase even though their consumption is well below that. Plus the hidden supplies from Iran and Russia to China via land route.

[kccqzy]: Nice that you allowed readers to customize the parameters! I personally thought the demand demand elasticity was too low and I was able to adjust it.

</details>
