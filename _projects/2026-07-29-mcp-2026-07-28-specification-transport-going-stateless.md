---
layout: default
title: "MCP无状态传输协议"
date: 2026-07-29T12:00:00+00:00
discovered_date: 2026-07-29
slug: 2026-07-29-mcp-2026-07-28-specification-transport-going-stateless
source: hackernews
category: show-hn
ai_score: 8.0
summary: "MCP 2026-07-28规范引入了一种无状态传输协议，以简化服务器端需求并增强无服务器兼容性，使用HTTP并减少对服务器状态持久化的需求。 该项目因其高参与度和其对无服务器架构主要痛点（通过消除服务器端状态管理）的解决方案而具有重要意义，通过SaaS或API提供了明确的盈利潜力。 该协议根据宽松的许可证授权，似乎处于生产成熟度，并且应该相对容易部署，无需复杂的硬件要求，但与现有系统集成可能需要开发工作。"
tags: "MCP, Serverless, HTTP, Protocol, Networking"
---

# MCP无状态传输协议


> MCP 2026-07-28规范引入了一种无状态传输协议，以简化服务器端需求并增强无服务器兼容性，使用HTTP并减少对服务器状态持久化的需求。 该项目因其高参与度和其对无服务器架构主要痛点（通过消除服务器端状态管理）的解决方案而具有重要意义，通过SaaS或API提供了明确的盈利潜力。 该协议根据宽松的许可证授权，似乎处于生产成熟度，并且应该相对容易部署，无需复杂的硬件要求，但与现有系统集成可能需要


**项目链接**：https://blog.modelcontextprotocol.io/posts/2026-07-28/
**作者**：Eldodi
**发布时间**：2026-07-28T18:35:11Z
**挖掘日期**：2026-07-29
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：MCP, Serverless, HTTP, Protocol, Networking


## 📌 项目详解

MCP 2026-07-28规范引入了一种无状态传输协议，以简化服务器端需求并增强无服务器兼容性，使用HTTP并减少对服务器状态持久化的需求。 该项目因其高参与度和其对无服务器架构主要痛点（通过消除服务器端状态管理）的解决方案而具有重要意义，通过SaaS或API提供了明确的盈利潜力。 该协议根据宽松的许可证授权，似乎处于生产成熟度，并且应该相对容易部署，无需复杂的硬件要求，但与现有系统集成可能需要开发工作。


## 🌐 背景与生态

无状态协议在Web架构中早已是标准，但像MCP这样的服务器端状态管理一直是一个挑战。向无服务器计算的转变突出了服务器协议中无状态设计的需要。


## 💬 社区讨论

社区反应总体上是积极的，开发者们对减少服务器状态负担和更容易部署无服务器感到欣慰。有些人质疑协议中长期使用的有状态语义。


## 🚀 应用前景

该协议可应用于无服务器计算环境，简化需要高可扩展性和低延迟的后端开发，特别是在金融科技和电子商务等行业。


## 🔧 技术栈

技术栈涉及HTTP作为核心协议，可能使用标准的网络库和框架。未提及特定的模型依赖，表明重点在于协议级别的更改。


## 🎯 上手难度

难度：入门。前提是了解HTTP基础知识并拥有服务器环境。步骤包括设置服务器并实现协议，对于有现有Web开发技能的人来说应该很简单。


## 👥 目标用户

目标用户包括后端开发人员、DevOps团队以及构建无服务器应用程序的组织，特别是在科技和电子商务部门。


## ⚖️ 类似项目对比

竞争对手包括HTTP/2和gRPC，它们提供高效的無狀態通信，尽管它们服务于不同的领域。HTTP/1.1对于基本的無狀態HTTP需求仍然相关。


## 📚 参考链接

- [Stateless protocol - Wikipedia](https://en.wikipedia.org/wiki/Stateless_protocol)
- [What Is a Stateless Protocol? – ITU Online IT Training](https://www.ituonline.com/tech-definitions/what-is-a-stateless-protocol/)
- [Stateless HTTP Container Isolation: Why MCP Servers on Serverless ...](https://pub.towardsai.net/stateless-http-container-isolation-why-mcp-servers-on-serverless-runtimes-must-disable-d4c6abe1ac5a)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[punkpeye]: Finally. I am running an MCP server gateway&#x2F;registry (some of you may know Glama). I cannot tell you what portion of our issues&#x2F;bugs were due to the need to persist server state. This change will allow us to offer a lot easier way for people to use Open-Source MCP servers.

[dend]: Hey folks - one of the Lead Maintainers for MCP. Happy that we got this release out the door today, this is an exciting change for those that wanted to roll out remove MCP servers into serverless hosts. There is, of course, more good stuff packed, so if you have questions or feedback - our team is here to help!

[btbuilder]: Excellent improvement. The server-side complexity required to handle sessions has been a large burden both on infrastructure and on educating teams on its characteristics.

[osinix]: This is the right practice. Why put the burden on the server? It is the job of client to remember, not the server. Server is there to serve requests, not do the remembering. That is how http worked from the beginning and that is why it has been successful.

[kamma4434]: Thank goodness johnny-comes-late saw the light! Who ever thought a the semantycs of a pipe was a good idea after 30 years of everything else becoming HTTP?

</details>
