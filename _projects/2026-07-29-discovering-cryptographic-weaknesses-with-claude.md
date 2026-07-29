---
layout: default
title: "AI驱动的密码学漏洞发现"
date: 2026-07-29T12:00:00+00:00
discovered_date: 2026-07-29
slug: 2026-07-29-discovering-cryptographic-weaknesses-with-claude
source: hackernews
category: show-hn
ai_score: 9.0
summary: "该项目利用Claude这一AI模型，通过先进的提示技术并极少人工干预，自主识别AES等密码学系统的漏洞。 其重要性体现在高参与度（201个星标，139条评论）和大量投资（10万美元API成本），表明强大的吸引力和实用价值。新颖的方法提供了通过SaaS或API的明确盈利潜力。 该项目许可证条款需核实，似乎已投入生产，并因高API成本和专用硬件要求而具有显著的部署复杂性。"
tags: "AI, Security, Cryptographic, Research, Tools"
---

# AI驱动的密码学漏洞发现


> 该项目利用Claude这一AI模型，通过先进的提示技术并极少人工干预，自主识别AES等密码学系统的漏洞。 其重要性体现在高参与度（201个星标，139条评论）和大量投资（10万美元API成本），表明强大的吸引力和实用价值。新颖的方法提供了通过SaaS或API的明确盈利潜力。 该项目许可证条款需核实，似乎已投入生产，并因高API成本和专用硬件要求而具有显著的部署复杂性。


**项目链接**：https://www.anthropic.com/research/discovering-cryptographic-weaknesses
**作者**：gslin
**发布时间**：2026-07-28T17:22:16Z
**挖掘日期**：2026-07-29
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Security, Cryptographic, Research, Tools


## 📌 项目详解

该项目利用Claude这一AI模型，通过先进的提示技术并极少人工干预，自主识别AES等密码学系统的漏洞。 其重要性体现在高参与度（201个星标，139条评论）和大量投资（10万美元API成本），表明强大的吸引力和实用价值。新颖的方法提供了通过SaaS或API的明确盈利潜力。 该项目许可证条款需核实，似乎已投入生产，并因高API成本和专用硬件要求而具有显著的部署复杂性。


## 🌐 背景与生态

人工智能在密码学领域的应用正在增长，Claude Mythos是AI模型用于安全研究的显著例子。该项目基于AI可以发现人类专家可能遗漏的漏洞的观点。


## 💬 社区讨论

社区评论表达了对AI在密码学中潜力的兴奋，对成本和可扩展性的怀疑，以及对所使用方法的更多透明度的要求。


## 🚀 应用前景

这项技术可以通过主动识别和减轻密码学漏洞，应用于保护关键基础设施、金融系统和政府通信。


## 🔧 技术栈

技术栈包括Claude Mythos（AI模型）、Anthropic的API，以及可能用于最佳性能的专用硬件，Python可能用于脚本和集成。


## 🎯 上手难度

难度：进阶。前提条件包括访问Anthropic的API以及可能的高端硬件。步骤包括设置API、配置Claude Mythos并运行初始测试。


## 👥 目标用户

目标用户是安全研究员、密码学家以及有显著安全需求的大组织，他们能够负担与此技术相关的成本。


## ⚖️ 类似项目对比

竞品包括使用Claude进行漏洞扫描的Project Glasswing和传统的密码分析工具如OpenSSL。该项目通过AI驱动的自主发现与其不同。


## 📚 参考链接

- [Discovering cryptographic weaknesses with Claude \ Anthropic](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)
- [Claude AI Autonomously Discovers Cryptographic Weaknesses That Escaped Expert Review](https://cyberpress.org/claude-ai-autonomously-discovers-cryptographic-weaknesses/)
- [Claude found mathematical flaws in two cryptographic algorithms that years of expert review missed](https://thenextweb.com/news/anthropic-claude-mythos-cryptographic-attacks-hawk-aes)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[_dwt]: I find that some of my friends and acquaintances have gotten obsessed with prompting style, &quot;prompt engineering&quot;, which skills to use, which skills to build, &quot;context engineering&quot;, and a billion other variations on &quot;how to write smart things so the model does good&quot;. Friends, look at the prompts that Anthropic&#x27;s own people are putting into the machine: &gt; A few hours after the first message, we found that Claude was still searching for simple attacks and se...

[staticshock]: When high quality effort is applied to a tool, such as AES or the linux kernel, we intuit that it &quot;hardens&quot; the tool. That is, it makes the tool more correct, more resilient, less assailable, etc. Similarly, when effort is applied to an open problem, such as the Riemann hypothesis or P v NP, without progress, it &quot;hardens&quot; the problem: it makes the problem feel more daunting to whoever takes a stab at it next. Andrew Wiles, whose interview also hit the homepage today ( http...

[mmaunder]: “Each of the results cost roughly $100,000 in API cost to develop.” And “Over the course of a week, one Anthropic researcher worked together with Claude to develop the HAWK attack, and another researcher built a scaffold4 that allowed Claude to fully autonomously discover the AES attack.” Spending $100k in tokens in a week is an impressive feat even with massive parallelization. I suspect the TPS their internal folks have access to is far higher than their bulk public endpoints. There’s a tec...

[axus]: I can already picture the faces of national security directors everywhere. &quot;The attacks described in these two papers are the strongest attacks we have found to date. We are sharing them after a period of consultation with US government and industry leaders. But as we develop increasingly powerful cryptanalytic results, it would be prudent to consider how researchers should react if a language model were to discover vulnerabilities in cryptosystems where attacks do have an immediate real...

[a-dub]: &gt; The multi-agent workflow led to interesting dynamics. For example, the key idea in producing this attack was discovered by a pair of workers working together. Both started investigating the idea; the first worker prematurely rejected the idea as infeasible, but the second found a way to fully exploit it. The pair kept exchanging messages, and eventually both agreed they had found an effective attack. this is pretty interesting. the way it is written doesn&#x27;t make it sound like the co...

</details>
