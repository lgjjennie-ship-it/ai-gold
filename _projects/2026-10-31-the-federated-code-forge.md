---
layout: default
title: "联邦代码熔炉"
date: 2026-10-31T12:00:00+00:00
discovered_date: 2026-10-31
slug: 2026-10-31-the-federated-code-forge
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Tangled 是一个自托管的代码搜索和发布管理平台，采用了一种新颖的方法来集中代码和发布流程，同时不牺牲去中心化。 该项目在 Hacker News 上获得了 289 个星标和 85 条评论，显示出强烈的社区兴趣。它解决了去中心化代码管理的需求，并提供了通过 SaaS 或 API 提供商的清晰盈利路径。 该平台在开源许可证下授权，目前处于 Beta 版本，部署复杂度适中。它需要服务器环境和一定的技术专长才能设置。"
tags: "Code, Tools, Self-Hosting, Development, Community"
---

# 联邦代码熔炉


> Tangled 是一个自托管的代码搜索和发布管理平台，采用了一种新颖的方法来集中代码和发布流程，同时不牺牲去中心化。 该项目在 Hacker News 上获得了 289 个星标和 85 条评论，显示出强烈的社区兴趣。它解决了去中心化代码管理的需求，并提供了通过 SaaS 或 API 提供商的清晰盈利路径。 该平台在开源许可证下授权，目前处于 Beta 版本，部署复杂度适中。它需要服务器环境和一定的


**项目链接**：https://tangled.org/blog/forge/
**作者**：zlliang
**发布时间**：2026-10-30T15:44:29Z
**挖掘日期**：2026-10-31
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Code, Tools, Self-Hosting, Development, Community


## 📌 项目详解

Tangled 是一个自托管的代码搜索和发布管理平台，采用了一种新颖的方法来集中代码和发布流程，同时不牺牲去中心化。 该项目在 Hacker News 上获得了 289 个星标和 85 条评论，显示出强烈的社区兴趣。它解决了去中心化代码管理的需求，并提供了通过 SaaS 或 API 提供商的清晰盈利路径。 该平台在开源许可证下授权，目前处于 Beta 版本，部署复杂度适中。它需要服务器环境和一定的技术专长才能设置。


## 🌐 背景与生态

代码熔炉传统上是集中式的，但对此的需求正在增长。Tangled 通过提供一个自托管的平台来填补这一空白，该平台在保持集中化优势的同时确保用户数据保持去中心化。


## 💬 社区讨论

社区评论非常热情，用户表示有兴趣从 Gitea 和 GitHub 等集中式平台迁移。创始人正在积极与社区互动并回应反馈。


## 🚀 应用前景

Tangled 可用于寻求去中心化代码管理的开发团队和组织。潜在应用包括软件开发、开源项目和希望减少对集中式平台依赖的企业。


## 🔧 技术栈

该平台使用现代网络技术构建，可能包括 Python、Docker 和 Kubernetes 进行部署。它可能与现有的代码仓库和 CI/CD 工具集成。


## 🎯 上手难度

入门评级为进阶。前提条件包括服务器环境、Python 3.8+ 和 Docker。基本步骤包括克隆仓库、设置环境和遵循安装指南。


## 👥 目标用户

目标用户包括需要自托管解决方案进行代码搜索和发布管理的后端工程师、DevOps 团队和研究人员。


## ⚖️ 类似项目对比

竞争对手包括 ForgeCode 和传统的代码熔炉，如 GitHub 和 GitLab。Tangled 通过其对去中心化和自托管能力的关注而区别于它们。


## 📚 参考链接

- [Forge (software) - Wikipedia](https://en.wikipedia.org/wiki/Forge_(software))
- [The federated code forge · The Tangled Blog](https://tangled.org/blog/forge/)
- [ForgeCode: your software factory](https://forgecode.dev/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[stryan]: Really looking forward to seeing Tangled develop! I&#x27;ve got a side project that&#x27;s main repo and CI is on my self-hosted Gitea but code and releases are mirrored to Github; I&#x27;m hoping to move it off Gitea and onto Tangled for code&#x2F;releases&#x2F;potentially CI and just keep Github for discoverability&#x2F;backups&#x2F;namespace &quot;squatting&quot;.
Just need git-bug to add a Tangled bridge so I can keep issues synced and (ideally) for there to be instructions for running th...

[icy]: Hi! Tangled co-founder here. We&#x27;re super stoked with this launch -- we&#x27;ve stabilized our AT Protocol lexicons, completely overhauled our architecture and UI, and made self-hosting the entire stack (or parts of it!) incredibly easy. We&#x27;ve also shipped support for organizations, and have private repos rolling out in the following couple weeks. Happy to answer any questions at all.

[bluerooibos]: I hope this takes off! Some feedback:- * I found the UI on the homepage&#x2F;timeline a bit busy - lots going on.  Notifications, Recents, Announcements don&#x27;t seem like they need to live on this page? * The Activity chart on a users profile page seems a bit wild to me.  I&#x27;d suggest simplifying it or just using what GitHub&#x2F;GitLab use with their square grid activity chart - it&#x27;s what users are most familiar with.   It&#x27;s kind of analagous to all the LLM&#x2F;Chat applica...

[ivanjermakov]: Finnish startup Tangled raises €3.8M to reinvent code collaboration  https:&#x2F;&#x2F;www.vestbee.com&#x2F;insights&#x2F;articles&#x2F;tangled-raises-3-8...

[eterm]: I tried to run:       git clone https:&#x2F;&#x2F;tangled.org&#x2F;tangled.org&#x2F;core 
  
And it failed?       Cloning into &#x27;core&#x27;...
    warning: redirecting to https:&#x2F;&#x2F;knot1.tangled.sh&#x2F;did:plc:j5hmlfdrwkvtxm7cjmu7j2is&#x2F;
    remote: Thanks for using knot1.tangled.sh!
    remote: Enumerating objects: 99191, done.
    remote: Total 99191, done.
    Receiving objects: 100% (99191&#x2F;99191), 122.19 MiB | 39.12 MiB&#x2F;s, done.
    Resolving deltas: 100% (49286&...

</details>
