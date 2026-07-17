---
layout: default
title: "AI应用安全监控工具"
date: 2026-07-17T12:00:00+00:00
discovered_date: 2026-07-17
slug: 2026-07-17-launch-hn-traceforce-yc-s26-company-wide-security-monitoring-for-ai-apps
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Traceforce追踪AI应用的使用情况及其与数据源的联系，提供全公司的安全监控。它使用轻量级二进制文件和浏览器扩展收集实时数据，并提供一个开源的动态MCP渗透测试工具。 Traceforce通过提供对AI应用及其连接的可见性和控制，解决了AI应用安全的一个关键需求。它在Hacker News上获得了很高的关注度，并有一个清晰的SaaS就绪模式，针对企业客户。 Traceforce是开源的，二进制文件使用Go语言编写，浏览器扩展使用Node JS编写，已在生产环境中部署超过1,000台设备。它需要很少的硬件资源，并与现有的安全工具集成。"
tags: "AI, Security, Monitoring, MCP, Tools"
---

# AI应用安全监控工具


> Traceforce追踪AI应用的使用情况及其与数据源的联系，提供全公司的安全监控。它使用轻量级二进制文件和浏览器扩展收集实时数据，并提供一个开源的动态MCP渗透测试工具。 Traceforce通过提供对AI应用及其连接的可见性和控制，解决了AI应用安全的一个关键需求。它在Hacker News上获得了很高的关注度，并有一个清晰的SaaS就绪模式，针对企业客户。 Traceforce是开源的，二进


**项目链接**：https://news.ycombinator.com/item?id=48937020
**作者**：XiaHua
**发布时间**：2026-07-16T16:52:16Z
**挖掘日期**：2026-07-17
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Security, Monitoring, MCP, Tools


## 📌 项目详解

Traceforce追踪AI应用的使用情况及其与数据源的联系，提供全公司的安全监控。它使用轻量级二进制文件和浏览器扩展收集实时数据，并提供一个开源的动态MCP渗透测试工具。 Traceforce通过提供对AI应用及其连接的可见性和控制，解决了AI应用安全的一个关键需求。它在Hacker News上获得了很高的关注度，并有一个清晰的SaaS就绪模式，针对企业客户。 Traceforce是开源的，二进制文件使用Go语言编写，浏览器扩展使用Node JS编写，已在生产环境中部署超过1,000台设备。它需要很少的硬件资源，并与现有的安全工具集成。


## 🌐 背景与生态

模型上下文协议（MCP）使AI代理能够安全地连接到数据源和工具。Traceforce通过提供对这些连接的实时监控，填补了市场上的空白，而传统的安全工具如EDR和CASB缺乏这种功能。


## 💬 社区讨论

社区评论强调了理解AI工具与MCP交互的重要性，以及需要更深入的应用行为跟踪。用户对实时连接图功能感到兴奋，并认为它有可能防止安全漏洞。


## 🚀 应用前景

Traceforce可用于金融、医疗保健和企业IT等行业，以监控AI应用的使用并防止数据泄露。其SaaS模式通过订阅费提供了一个明确的盈利路径。


## 🔧 技术栈

技术栈包括用于二进制文件的Go语言，用于浏览器扩展的Node JS，以及一个开源的动态MCP渗透测试工具。它利用模型上下文协议（MCP）进行安全的AI代理连接。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python环境以及安装Traceforce二进制文件和浏览器扩展。基本步骤包括配置和初始监控设置。


## 👥 目标用户

目标用户是企业安全团队、IT部门以及开发AI应用的开发者。角色包括后端工程师、机器学习实践者和DevOps专家。


## ⚖️ 类似项目对比

竞争对手包括Runlayer等AI原生安全解决方案提供商，以及CrowdStrike和Palo Alto Networks等传统的EDR/CASB提供商。Traceforce通过其专注于AI应用连接和MCP安全的特点来区分自己。


## 📚 参考链接

- [Model Context Protocol - Wikipedia](https://en.wikipedia.org/wiki/Model_Context_Protocol)
- [MCP is the open standard helping AI agents take action. Here’s why it...](https://medium.com/@elisowski/mcp-explained-the-new-standard-connecting-ai-to-everything-79c5a1c98288)
- [How to Run an MCP Pentest : Complete Guide](https://www.uprootsecurity.com/blog/how-to-run-mcp-pentest-guide)

<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Xia and Varun, the founders of Traceforce (<a href="https:&#x2F;&#x2F;www.traceforce.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai&#x2F;</a>). Traceforce provides visibility and control over AI apps such as ChatGPT, Claude etc directly on all devices (laptops, sandboxes, virtual machines) by discovering not just which apps are being used but also how they are connected to other data sources via MCPs. We also have an open-source dynamic MCP pentesting tool <a href="https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray</a> to detect vulnerable MCPs.<p>The purpose of Traceforce is to:<p>- Give a company’s employees a standardized way to ensure that AI software running on their device is operating safely<p>- Give the company’s security team visibility of the activities of AI software on the company’s devices, and to detect and prevent unsafe actions and security breaches as early as possible.<p>How Traceforce works<p>1. Traceforce is installed on each device as a lightweight binary and browser extension.<p>2. Within 30 minutes, the device is uploading live data to the company profile, displaying all the AI agents&#x2F;apps running across all company devices on a dashboard.<p>3. Company security staff can monitor the activity of all the agents in real time, implement controls, and be alerted to any security risks as soon as they arise.<p>Here’s the video demo: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM</a><p>The inspiration for Traceforce came via Xia’s experience as Director of Engineering at a startup called Clumio (which was acquired by Commvault in Oct 2024). Being able to monitor how team members are using AI without slowing them down was a top priority at Clumio. After speaking with 50+ CISOs and CIOs, it became clear that this is a much-needed solution right now across industries. We keep hearing that new AI features are being adopted so quickly and so broadly that visibility and control just can&#x27;t keep up.<p>Traceforce is transparent about what we monitor and collect. By default, Traceforce collects only metadata and telemetry about the AI applications, MCPs, and tools running on a device. Security teams can enable options to inspect tool calls for the purpose of detecting, warning on, or blocking predefined high-risk or potentially destructive actions. All content inspection happens locally on the device. User prompts are never stored unless explicitly configured by the organization&#x27;s security administrators.<p>We work closely with end-users of the product, and once they understand what is being monitored&#x2F;shared, they actually have great comfort that they have a powerful layer of protection on their device to prevent security incidents. It enables them to just focus on their work without worrying about what leaks and breaches may be happening under the hood without their awareness.<p>The Traceforce binary is built using Go and the browser extension is written in Node JS. The hardest part is building a complete connectivity graph between AI applications, MCPs, and tools, then identifying the vulnerabilities and attack paths introduced by those connections. Traditional security tools fall short: EDRs see processes, CASBs see network traffic, but neither has visibility into the application-level activity happening inside AI apps. The way we got it to work was by understanding the configurations and logs of each and every app. It’s a labor intensive process because every app is different and AI features change frequently.<p>Traceforce is currently deployed across more than 1,000 devices at 10 organizations. On average, we discover over 15 AI applications per device with each application connected to 5-10 MCPs. We&#x27;ve helped customers identify exposed plaintext secrets in MCP configurations, prevent API keys from leaking through AI-generated code, and warn developers before executing potentially destructive commands such as “DROP TABLE”. Our &quot;warn and acknowledge&quot; approach has been especially well received, giving developers the freedom to work while helping them avoid costly mistakes.<p>We&#x27;re looking to work with security, IT, and AI platform teams at small to medium enterprises (200+ employees) that are rapidly adopting AI coding assistants, ChatGPT, Claude, and MCPs. If you&#x27;re struggling to understand what AI tools people use to boost their productivity or need a practical way to reduce AI-related security risk without slowing folks down, we&#x27;d love to talk.<p>You can get started with a free trial at <a href="https:&#x2F;&#x2F;www.traceforce.ai" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai</a> or reach out directly to schedule a demo and discuss your environment.


--- Top Comments ---

[brintha]: The tricky part here is not just spotting AI apps running on endpoints, but understanding how those AI tools interact with multiple cloud MCPs in real time - and what risks emerge from those connections. We built LynxTrac&#x27;s endpoint security to track deep app behavior and config changes, including registry and network activity, but connecting that to AI-driven MCP calls was a missing piece. Traceforce&#x27;s approach to building a live connectivity graph between AI apps and MCPs is exact...

[laul_pogan]: Hey Xia! Super excited for this- good talking to you a few weeks ago and best luck with the launch :)

[eddy-sekorti]: Congratulations, have you thought about setting up a professional trust center? you can try  https:&#x2F;&#x2F;sekorti.com

[gk1]: +1 You&#x27;re facing competition from both the incumbents who can ship these capabilites to their massive userbase, and emerging startups like Runlayer who are running away with the AI-native segment. What are you offering that people want yet neither of those classes of solutions offer?

[XiaHua]: We are also curious to ask what existing tools are folks using to gain visibility into what&#x27;s running out there?

</details>
