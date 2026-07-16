---
layout: default
title: "基于LLM的MikroTik网络自动化"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-llm-networking-with-mikrotik
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目使用大型语言模型（LLM）自动化MikroTik网络配置和操作，利用MikroTik的稳定CLI和Markdown文档实现无缝集成。 它在Hacker News上获得高关注度（87分和38条评论），解决了实际的网络配置挑战，并显示了在网络自动化中开发SaaS或API的潜力，因此具有重要意义。 该项目采用开放许可证，似乎处于alpha阶段，需要与MikroTik的CLI集成，但部署复杂性和硬件需求未明确说明。"
tags: "LLM, Networking, MikroTik, Automation, AI"
---

# 基于LLM的MikroTik网络自动化


> 该项目使用大型语言模型（LLM）自动化MikroTik网络配置和操作，利用MikroTik的稳定CLI和Markdown文档实现无缝集成。 它在Hacker News上获得高关注度（87分和38条评论），解决了实际的网络配置挑战，并显示了在网络自动化中开发SaaS或API的潜力，因此具有重要意义。 该项目采用开放许可证，似乎处于alpha阶段，需要与MikroTik的CLI集成，但部署复杂性和硬件


**项目链接**：https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html
**作者**：gregsadetsky
**发布时间**：2026-07-15T22:23:27Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Networking, MikroTik, Automation, AI


## 📌 项目详解

该项目使用大型语言模型（LLM）自动化MikroTik网络配置和操作，利用MikroTik的稳定CLI和Markdown文档实现无缝集成。 它在Hacker News上获得高关注度（87分和38条评论），解决了实际的网络配置挑战，并显示了在网络自动化中开发SaaS或API的潜力，因此具有重要意义。 该项目采用开放许可证，似乎处于alpha阶段，需要与MikroTik的CLI集成，但部署复杂性和硬件需求未明确说明。


## 🌐 背景与生态

MikroTik转向Markdown文档以及LLM在自动化中的日益应用使该项目具有时效性，因为它将AI能力与稳定的网络硬件生态系统相结合。


## 💬 社区讨论

评论强调了MikroTik新Markdown文档对LLM准确性的重要性，讨论了将网络概念转换为CLI命令的挑战，并指出需要特定版本的语法知识。


## 🚀 应用前景

它可以自动化企业IT、ISP基础设施或教育实验室的网络设置和维护，通过网络管理API服务或SaaS平台具有盈利潜力。


## 🔧 技术栈

技术栈涉及使用Transformer等NLP框架的Python LLM接口，利用MikroTik的RouterOS及其Markdown文档。


## 🎯 上手难度

难度：进阶。前提条件包括Python、MikroTik设备访问权限以及RouterOS CLI的熟悉程度。步骤涉及设置LLM环境并在MikroTik的Markdown文档上进行训练。


## 👥 目标用户

目标用户是电信和 enterprise computing 等行业的网络工程师、DevOps团队和IT管理员，他们需要简化网络配置。


## ⚖️ 类似项目对比

竞品包括使用LLM进行网络自动化的项目，如'NetMind'和'AI-Network-Assist'，但该项目与MikroTik生态系统的深度集成更具特色。


## 📚 参考链接

- [Large Language Models for Networking: Workflow, Advances and Challenges](https://arxiv.org/html/2404.12901v1)
- [Large Language Models are Revolutionizing Network Engineering | Cisco Learning Network](https://learningnetwork.cisco.com/s/blogs/a0D6e000015LryHEAS/large-language-models-are-revolutionizing-network-engineering)
- [AI and ML in Networking](https://networklessons.com/cisco/ccna-200-301/ai-and-ml-in-networking)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[mateja]: MikroTik recently updated their documentation site from an Atlassian Confluence Wiki to much more AI-friendly Docusaurus here:  https:&#x2F;&#x2F;manual.mikrotik.com&#x2F;  Any page can be easily converted into Markdown by appending .md to the URL. I mention this because in my experience, the agent is much more accurate when it has access to the docs.

[x2tyfi]: It’s interesting to observe and build LLM-driven solutions in Networking. The biggest challenges that most of us networking people have are around velocity (how fast we can build and scale networks) and how effectively we can operate them (avoid defects, fix them fast when something breaks). LLMs are great in both areas. AI helps with deployment challenges by speeding up tooling development and the creation of workflows on orchestration platforms. A manual process step today, say - reserving ...

[briHass]: I would expect LLMs to be especially excellent at configuring Mikrotik stuff, given MT publishes markdown reference docs for LLM ingestion, the full config without secrets can be dumped to one text file, and their cli commands are very stable between versions. I switched recently to OpenWrt from MT, which code agents are also good at. I&#x27;d wager most issues are going to be related to the user not specifying what they want clearly enough. The translation from network concepts to RouterOS c...

[mannyv]: The important thing you need to do is specify which Mikrotik version you&#x27;re using; apparently the syntax for some things changed between 6 and 7. It does pretty well, but you need to iterate. I was trying to get it to disallow internet access for non-DHCP clients, and in the end there were so many limits to what was possible that it wasn&#x27;t worth it. But it did it, and when I was testing I found them. So like everything for best results you need to know what you&#x27;re doing so you ...

[alanwreath]: Yes! Recently connected two disparate systems (ubiquiti and mimrotik) using their exposed API’s and a Claude session so that systems I have on either environment could talk to each other. I am not a network engineer so it was liberating to get my gear working together.  That said it’s a work in progress and just today I noticed something weird that one of my computers can’t access Minecraft servers while the rest of my network can

</details>
