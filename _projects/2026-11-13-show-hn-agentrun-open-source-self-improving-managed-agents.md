---
layout: default
title: "AgentRun：自我改进的AI代理"
date: 2026-11-13T12:00:00+00:00
discovered_date: 2026-11-13
slug: 2026-11-13-show-hn-agentrun-open-source-self-improving-managed-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "AgentRun是一个开源平台，用于管理和改进自主代理，具有基于网络的 workflows 和广泛的工具集成，支持多种AI模型和 harness。 AgentRun 拥有 109 个星标和 29 条评论，显示出强烈的社区兴趣。它提供了自我改进的代理和一系列集成，展示了其实用性和通过管理平台进行货币化的潜力。 AgentRun 采用开源许可，处于生产成熟阶段，部署复杂度适中。它需要 OpenRouter 密钥进行自托管，并支持多种 AI 模型和 harness。"
tags: "Agent, AI, Self-improving, Tools, Integrations"
---

# AgentRun：自我改进的AI代理


> AgentRun是一个开源平台，用于管理和改进自主代理，具有基于网络的 workflows 和广泛的工具集成，支持多种AI模型和 harness。 AgentRun 拥有 109 个星标和 29 条评论，显示出强烈的社区兴趣。它提供了自我改进的代理和一系列集成，展示了其实用性和通过管理平台进行货币化的潜力。 AgentRun 采用开源许可，处于生产成熟阶段，部署复杂度适中。它需要 OpenRout


**项目链接**：https://github.com/Parcha-ai/agentrun/blob/main/README.md
**作者**：miguelrios
**发布时间**：2026-11-12T18:15:48Z
**挖掘日期**：2026-11-13
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Agent, AI, Self-improving, Tools, Integrations


## 📌 项目详解

AgentRun是一个开源平台，用于管理和改进自主代理，具有基于网络的 workflows 和广泛的工具集成，支持多种AI模型和 harness。 AgentRun 拥有 109 个星标和 29 条评论，显示出强烈的社区兴趣。它提供了自我改进的代理和一系列集成，展示了其实用性和通过管理平台进行货币化的潜力。 AgentRun 采用开源许可，处于生产成熟阶段，部署复杂度适中。它需要 OpenRouter 密钥进行自托管，并支持多种 AI 模型和 harness。


## 🌐 背景与生态

AgentRun 属于 AI 代理管理生态系统，提供了一个全面的自我改进代理解决方案。替代方案包括 LangChain 和 AutoGPT 等平台。开源 AI 工具的兴起使此类平台更加相关。


## 💬 社区讨论

社区评论集中在 PR 处理、计算限制和与专有数据源的集成。人们对任务控制功能感兴趣，并有可能进行合作。


## 🚀 应用前景

AgentRun 可以解决企业自动化、客户服务和数据分析等现实问题。它可以用于构建 AI 代理管理的 SaaS 产品，特别是在金融和医疗行业。


## 🔧 技术栈

AgentRun 使用 Python 并与 Pi、Claude Agents 和 Codex 等AI模型集成。它支持 ACP 进行代理通信，并利用 Docker 和 K8s 进行部署。


## 🎯 上手难度

入门评级为进阶。前提条件包括 Python 3.8+、OpenRouter 密钥以及对 Docker 的基本熟悉。步骤涉及克隆仓库并遵循一键安装指南。


## 👥 目标用户

目标用户包括金融、医疗和技术等行业中的后端工程师、ML 实践者和 DevOps 团队。


## ⚖️ 类似项目对比

竞争对手包括 LangChain、AutoGPT 和微软的 Azure AI 代理。AgentRun 通过专注于自我改进的代理和广泛的工具集成而有所不同。


## 📚 参考链接

- [What Are Self-Improving Agents? - Arize AI](https://arize.com/glossary/self-improving-agents/)
- [Stanford CS329A | Self-Improving AI Agents](https://cs329a.stanford.edu/)
- [What Is ACP in AI ? The Agentic Commerce Protocol Explained | Zinc](https://www.zinc.com/blog/what-is-acp)

<details><summary>📄 查看原文内容</summary>


We (GREP.AI, YC F26) are open-sourcing AgentRun and turning it into a full managed agents platform. Read more about it in this post: <a href="https:&#x2F;&#x2F;agentrun.ai&#x2F;blog&#x2F;introducing-agentrun-run-smarter-agents-use-fewer-tokens" rel="nofollow">https:&#x2F;&#x2F;agentrun.ai&#x2F;blog&#x2F;introducing-agentrun-run-smarter-ag...</a>.<p>It includes what we originally built for our own agent harness:<p>- Self-improving agents 
- Web-grounded workflows 
- A range of sandboxes and computer environments 
- Thousands of tools and integrations 
- Detailed analytics on how your agents behave<p>You can bring your own agent. AgentRun works with Pi, Claude Agents, Codex, OpenCode, and any other harness that supports ACP.<p>You can self-host it (see 1-click install on Render) with an OpenRouter key, or try the hosted version at console.agentrun.ai.<p>We’d love feedback, especially on the architecture (see README), or anything we may be missing to make it useful to you.


--- Top Comments ---

[whirlwin]: Would like to hear from everyone: How are you dealing with PRs in 2026? It&#x27;s our biggest bottle neck. We are considering looking into attestations, e.g. through the SLSA spec:  https:&#x2F;&#x2F;slsa.dev&#x2F;  to ensure build provenance and verification before it is deployed.

[ghempton]: If your team is using subscriptions, it is a lot more cost effective (and higher quality) to simply use a local orchestrator to automatically deal with PR reviews. We built  https:&#x2F;&#x2F;github.com&#x2F;codealong&#x2F;codealong  in part to help with this.

[bmiedlar]: I&#x27;ve noticed on some of my own research and testing that even with caps some agents will work around the per-call time limit using background processes. Do your caps cover compute in the detached processes?

[mfrye0]: Very cool. I was waiting for something like this to pop up. Is it possible to be added as a data source? I see you&#x27;re mostly pointing the agent to easy &#x2F; publicly available sources like the UK. We have ~200 government registrar integrations now and 500M entities in the system. We essentially have better coverage than OpenCorporates at this stage.  https:&#x2F;&#x2F;savvyiq.ai

[Rinkesh2010rpp]: Cool project, I myself have a similar autonomous agent, in python 
At rinkesh2010rpp&#x2F;sudarshana. But I liked your mission control. Will for sure take some inspiration. Also, what I have is ability to find other agents on run time, running on Modal, and a safety layer that checks every actions taken by the agent. and happy to talk more. Thanks

</details>
