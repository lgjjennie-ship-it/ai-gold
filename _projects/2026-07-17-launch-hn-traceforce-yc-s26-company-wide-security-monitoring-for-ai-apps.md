---
layout: default
title: "AI应用安全监控工具"
date: 2026-07-17T12:00:00+00:00
discovered_date: 2026-07-17
slug: 2026-07-17-launch-hn-traceforce-yc-s26-company-wide-security-monitoring-for-ai-apps
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Traceforce通过跟踪AI应用（如ChatGPT和Claude）的使用情况及其与数据源的连接（通过MCPs），监控AI应用，并提供开源渗透测试工具进行漏洞检测。 Traceforce通过在Hacker News上获得高关注度，提供新颖的监控和控制功能、开源渗透测试工具，以及清晰的企业级安全SaaS盈利模式，解决了关键的人工智能安全问题。 采用开源许可，处于Beta阶段，需要轻量级二进制文件和浏览器扩展安装，支持实时仪表板监控和本地内容检查。"
tags: "AI, Security, Monitoring, Tools, Enterprise"
---

# AI应用安全监控工具


> Traceforce通过跟踪AI应用（如ChatGPT和Claude）的使用情况及其与数据源的连接（通过MCPs），监控AI应用，并提供开源渗透测试工具进行漏洞检测。 Traceforce通过在Hacker News上获得高关注度，提供新颖的监控和控制功能、开源渗透测试工具，以及清晰的企业级安全SaaS盈利模式，解决了关键的人工智能安全问题。 采用开源许可，处于Beta阶段，需要轻量级二进制文件和


**项目链接**：https://news.ycombinator.com/item?id=48937020
**作者**：XiaHua
**发布时间**：2026-07-16T16:52:16Z
**挖掘日期**：2026-07-17
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Security, Monitoring, Tools, Enterprise


## 📌 项目详解

Traceforce通过跟踪AI应用（如ChatGPT和Claude）的使用情况及其与数据源的连接（通过MCPs），监控AI应用，并提供开源渗透测试工具进行漏洞检测。 Traceforce通过在Hacker News上获得高关注度，提供新颖的监控和控制功能、开源渗透测试工具，以及清晰的企业级安全SaaS盈利模式，解决了关键的人工智能安全问题。 采用开源许可，处于Beta阶段，需要轻量级二进制文件和浏览器扩展安装，支持实时仪表板监控和本地内容检查。


## 🌐 背景与生态

Traceforce填补了AI安全监控的空白，传统工具缺乏对AI应用层活动的可见性。AI功能的快速采用超出了可见性和控制解决方案的发展。


## 💬 社区讨论

开发者强调了跟踪AI工具与MCP交互的挑战，以及构建实时连接图的创新性，同时也有人询问关于竞争和信任中心的问题。


## 🚀 应用前景

适用于需要AI应用安全的企业，可解决数据泄露、API密钥暴露和合规性问题。在金融、医疗保健和技术行业具有潜力。


## 🔧 技术栈

二进制文件使用Go构建，扩展使用Node JS编写，与MCPs集成，并利用本地设备处理以保护隐私。


## 🎯 上手难度

入门难度。需要Python 3.8+，可选GPU，以及安装二进制文件和扩展。步骤包括配置和初始仪表板设置。


## 👥 目标用户

面向企业安全团队、后端工程师和金融、医疗保健等行业的机器学习从业者。


## ⚖️ 类似项目对比

竞争对手包括Runlayer（AI原生安全）和传统EDR/CASB工具。Traceforce通过AI特定的MCP监控实现差异化。


## 📚 参考链接

- [MCPS | PRS for Music](https://www.prsformusic.com/what-we-do/mcps)

<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Xia and Varun, the founders of Traceforce (<a href="https:&#x2F;&#x2F;www.traceforce.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai&#x2F;</a>). Traceforce provides visibility and control over AI apps such as ChatGPT, Claude etc directly on all devices (laptops, sandboxes, virtual machines) by discovering not just which apps are being used but also how they are connected to other data sources via MCPs. We also have an open-source dynamic MCP pentesting tool <a href="https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray</a> to detect vulnerable MCPs.<p>The purpose of Traceforce is to:<p>- Give a company’s employees a standardized way to ensure that AI software running on their device is operating safely<p>- Give the company’s security team visibility of the activities of AI software on the company’s devices, and to detect and prevent unsafe actions and security breaches as early as possible.<p>How Traceforce works<p>1. Traceforce is installed on each device as a lightweight binary and browser extension.<p>2. Within 30 minutes, the device is uploading live data to the company profile, displaying all the AI agents&#x2F;apps running across all company devices on a dashboard.<p>3. Company security staff can monitor the activity of all the agents in real time, implement controls, and be alerted to any security risks as soon as they arise.<p>Here’s the video demo: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM</a><p>The inspiration for Traceforce came via Xia’s experience as Director of Engineering at a startup called Clumio (which was acquired by Commvault in Oct 2024). Being able to monitor how team members are using AI without slowing them down was a top priority at Clumio. After speaking with 50+ CISOs and CIOs, it became clear that this is a much-needed solution right now across industries. We keep hearing that new AI features are being adopted so quickly and so broadly that visibility and control just can&#x27;t keep up.<p>Traceforce is transparent about what we monitor and collect. By default, Traceforce collects only metadata and telemetry about the AI applications, MCPs, and tools running on a device. Security teams can enable options to inspect tool calls for the purpose of detecting, warning on, or blocking predefined high-risk or potentially destructive actions. All content inspection happens locally on the device. User prompts are never stored unless explicitly configured by the organization&#x27;s security administrators.<p>We work closely with end-users of the product, and once they understand what is being monitored&#x2F;shared, they actually have great comfort that they have a powerful layer of protection on their device to prevent security incidents. It enables them to just focus on their work without worrying about what leaks and breaches may be happening under the hood without their awareness.<p>The Traceforce binary is built using Go and the browser extension is written in Node JS. The hardest part is building a complete connectivity graph between AI applications, MCPs, and tools, then identifying the vulnerabilities and attack paths introduced by those connections. Traditional security tools fall short: EDRs see processes, CASBs see network traffic, but neither has visibility into the application-level activity happening inside AI apps. The way we got it to work was by understanding the configurations and logs of each and every app. It’s a labor intensive process because every app is different and AI features change frequently.<p>Traceforce is currently deployed across more than 1,000 devices at 10 organizations. On average, we discover over 15 AI applications per device with each application connected to 5-10 MCPs. We&#x27;ve helped customers identify exposed plaintext secrets in MCP configurations, prevent API keys from leaking through AI-generated code, and warn developers before executing potentially destructive commands such as “DROP TABLE”. Our &quot;warn and acknowledge&quot; approach has been especially well received, giving developers the freedom to work while helping them avoid costly mistakes.<p>We&#x27;re looking to work with security, IT, and AI platform teams at small to medium enterprises (200+ employees) that are rapidly adopting AI coding assistants, ChatGPT, Claude, and MCPs. If you&#x27;re struggling to understand what AI tools people use to boost their productivity or need a practical way to reduce AI-related security risk without slowing folks down, we&#x27;d love to talk.<p>You can get started with a free trial at <a href="https:&#x2F;&#x2F;www.traceforce.ai" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai</a> or reach out directly to schedule a demo and discuss your environment.


--- Top Comments ---

[brintha]: The tricky part here is not just spotting AI apps running on endpoints, but understanding how those AI tools interact with multiple cloud MCPs in real time - and what risks emerge from those connections. We built LynxTrac&#x27;s endpoint security to track deep app behavior and config changes, including registry and network activity, but connecting that to AI-driven MCP calls was a missing piece. Traceforce&#x27;s approach to building a live connectivity graph between AI apps and MCPs is exact...

[eddy-sekorti]: Congratulations, have you thought about setting up a professional trust center? you can try  https:&#x2F;&#x2F;sekorti.com

[laul_pogan]: Hey Xia! Super excited for this- good talking to you a few weeks ago and best luck with the launch :)

[gk1]: +1 You&#x27;re facing competition from both the incumbents who can ship these capabilites to their massive userbase, and emerging startups like Runlayer who are running away with the AI-native segment. What are you offering that people want yet neither of those classes of solutions offer?

[XiaHua]: We are also curious to ask what existing tools are folks using to gain visibility into what&#x27;s running out there?

</details>
