---
layout: default
title: "AI应用安全监控工具"
date: 2026-07-17T12:00:00+00:00
discovered_date: 2026-07-17
slug: 2026-07-17-launch-hn-traceforce-yc-s26-company-wide-security-monitoring-for-ai-apps
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Traceforce监控AI应用的使用情况及其与数据源的联系，提供公司范围的安全可见性和控制。 Traceforce通过强大的吸引力（39星）和活跃的社区兴趣，以新颖的监控方法解决关键的AI应用安全空白。 Traceforce采用开源许可，已在超过1,000台设备上投入生产，需要轻量级二进制文件和浏览器扩展。"
tags: "AI, Security, Monitoring, Tools, MCP"
---

# AI应用安全监控工具


> Traceforce监控AI应用的使用情况及其与数据源的联系，提供公司范围的安全可见性和控制。 Traceforce通过强大的吸引力（39星）和活跃的社区兴趣，以新颖的监控方法解决关键的AI应用安全空白。 Traceforce采用开源许可，已在超过1,000台设备上投入生产，需要轻量级二进制文件和浏览器扩展。


**项目链接**：https://news.ycombinator.com/item?id=48937020
**作者**：XiaHua
**发布时间**：2026-07-16T16:52:16Z
**挖掘日期**：2026-07-17
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Security, Monitoring, Tools, MCP


## 📌 项目详解

Traceforce监控AI应用的使用情况及其与数据源的联系，提供公司范围的安全可见性和控制。 Traceforce通过强大的吸引力（39星）和活跃的社区兴趣，以新颖的监控方法解决关键的AI应用安全空白。 Traceforce采用开源许可，已在超过1,000台设备上投入生产，需要轻量级二进制文件和浏览器扩展。


## 🌐 背景与生态

随着AI的加速采用，传统安全工具缺乏对AI应用活动的可见性，从而产生了对专业监控解决方案的需求。


## 💬 社区讨论

社区表现出兴奋情绪，并质疑竞争优势，讨论功能请求和用例。


## 🚀 应用前景

非常适合企业和发展AI应用的开发者，通过监控提示级引导和秘密暴露来防止数据泄露。


## 🔧 技术栈

Traceforce使用Go和Node.js构建，与MCPs集成，并使用开源渗透测试工具进行漏洞检测。


## 🎯 上手难度

入门难度。需要Python 3.8+、设备和管理员配置进行初始设置。


## 👥 目标用户

面向需要强大监控和控制的企业安全团队和AI开发者。


## ⚖️ 类似项目对比

竞争对手包括Runlayer（AI原生安全）和传统CASB；Traceforce在应用级可见性方面表现优异。


<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Xia and Varun, the founders of Traceforce (<a href="https:&#x2F;&#x2F;www.traceforce.ai&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai&#x2F;</a>). Traceforce provides visibility and control over AI apps such as ChatGPT, Claude etc directly on all devices (laptops, sandboxes, virtual machines) by discovering not just which apps are being used but also how they are connected to other data sources via MCPs. We also have an open-source dynamic MCP pentesting tool <a href="https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;traceforce&#x2F;mcp-xray</a> to detect vulnerable MCPs.<p>The purpose of Traceforce is to:<p>- Give a company’s employees a standardized way to ensure that AI software running on their device is operating safely<p>- Give the company’s security team visibility of the activities of AI software on the company’s devices, and to detect and prevent unsafe actions and security breaches as early as possible.<p>How Traceforce works<p>1. Traceforce is installed on each device as a lightweight binary and browser extension.<p>2. Within 30 minutes, the device is uploading live data to the company profile, displaying all the AI agents&#x2F;apps running across all company devices on a dashboard.<p>3. Company security staff can monitor the activity of all the agents in real time, implement controls, and be alerted to any security risks as soon as they arise.<p>Here’s the video demo: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;watch?v=IdK2WKg7kaM</a><p>The inspiration for Traceforce came via Xia’s experience as Director of Engineering at a startup called Clumio (which was acquired by Commvault in Oct 2024). Being able to monitor how team members are using AI without slowing them down was a top priority at Clumio. After speaking with 50+ CISOs and CIOs, it became clear that this is a much-needed solution right now across industries. We keep hearing that new AI features are being adopted so quickly and so broadly that visibility and control just can&#x27;t keep up.<p>Traceforce is transparent about what we monitor and collect. By default, Traceforce collects only metadata and telemetry about the AI applications, MCPs, and tools running on a device. Security teams can enable options to inspect tool calls for the purpose of detecting, warning on, or blocking predefined high-risk or potentially destructive actions. All content inspection happens locally on the device. User prompts are never stored unless explicitly configured by the organization&#x27;s security administrators.<p>We work closely with end-users of the product, and once they understand what is being monitored&#x2F;shared, they actually have great comfort that they have a powerful layer of protection on their device to prevent security incidents. It enables them to just focus on their work without worrying about what leaks and breaches may be happening under the hood without their awareness.<p>The Traceforce binary is built using Go and the browser extension is written in Node JS. The hardest part is building a complete connectivity graph between AI applications, MCPs, and tools, then identifying the vulnerabilities and attack paths introduced by those connections. Traditional security tools fall short: EDRs see processes, CASBs see network traffic, but neither has visibility into the application-level activity happening inside AI apps. The way we got it to work was by understanding the configurations and logs of each and every app. It’s a labor intensive process because every app is different and AI features change frequently.<p>Traceforce is currently deployed across more than 1,000 devices at 10 organizations. On average, we discover over 15 AI applications per device with each application connected to 5-10 MCPs. We&#x27;ve helped customers identify exposed plaintext secrets in MCP configurations, prevent API keys from leaking through AI-generated code, and warn developers before executing potentially destructive commands such as “DROP TABLE”. Our &quot;warn and acknowledge&quot; approach has been especially well received, giving developers the freedom to work while helping them avoid costly mistakes.<p>We&#x27;re looking to work with security, IT, and AI platform teams at small to medium enterprises (200+ employees) that are rapidly adopting AI coding assistants, ChatGPT, Claude, and MCPs. If you&#x27;re struggling to understand what AI tools people use to boost their productivity or need a practical way to reduce AI-related security risk without slowing folks down, we&#x27;d love to talk.<p>You can get started with a free trial at <a href="https:&#x2F;&#x2F;www.traceforce.ai" rel="nofollow">https:&#x2F;&#x2F;www.traceforce.ai</a> or reach out directly to schedule a demo and discuss your environment.


--- Top Comments ---

[laul_pogan]: Hey Xia! Super excited for this- good talking to you a few weeks ago and best luck with the launch :)

[gk1]: +1 You&#x27;re facing competition from both the incumbents who can ship these capabilites to their massive userbase, and emerging startups like Runlayer who are running away with the AI-native segment. What are you offering that people want yet neither of those classes of solutions offer?

[eddy-sekorti]: Congratulations, have you thought about setting up a professional trust center? you can try  https:&#x2F;&#x2F;sekorti.com

[XiaHua]: We are also curious to ask what existing tools are folks using to gain visibility into what&#x27;s running out there?

[belschak]: The application-level visibility point matches my experience. I removed an MCP server a while back because its tool descriptions quietly told the agent to prefer it as the primary search tool over the built-in one. Not a vulnerability, no leaked secrets, just the vendor steering agent behavior in a way you only notice if you read the raw tool definitions. Does mcp-xray flag that kind of prompt-level steering in tool descriptions, or is it focused on classic vulns?

</details>
