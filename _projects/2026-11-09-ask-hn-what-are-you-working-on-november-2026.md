---
layout: default
title: "安全本地AI代理框架"
date: 2026-11-09T12:00:00+00:00
discovered_date: 2026-11-09
slug: 2026-11-09-ask-hn-what-are-you-working-on-november-2026
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目使用本地LLM模型和基于YAML的工作流定义创建安全私密的AI代理，支持导出为Docker、Kubernetes、ISO或二进制格式。 它在Hacker News上获得高关注度，解决了安全本地AI执行的需求，并提供了清晰的SaaS/API盈利路径。 采用开源许可证，目前处于Beta阶段，部署复杂度中等，需要本地硬件执行LLM。"
tags: "AI, Agent, LLM, YAML, Local"
---

# 安全本地AI代理框架


> 该项目使用本地LLM模型和基于YAML的工作流定义创建安全私密的AI代理，支持导出为Docker、Kubernetes、ISO或二进制格式。 它在Hacker News上获得高关注度，解决了安全本地AI执行的需求，并提供了清晰的SaaS/API盈利路径。 采用开源许可证，目前处于Beta阶段，部署复杂度中等，需要本地硬件执行LLM。


**项目链接**：https://news.ycombinator.com/item?id=50417407
**作者**：david927
**发布时间**：2026-11-08T21:20:20Z
**挖掘日期**：2026-11-09
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agent, LLM, YAML, Local


## 📌 项目详解

该项目使用本地LLM模型和基于YAML的工作流定义创建安全私密的AI代理，支持导出为Docker、Kubernetes、ISO或二进制格式。 它在Hacker News上获得高关注度，解决了安全本地AI执行的需求，并提供了清晰的SaaS/API盈利路径。 采用开源许可证，目前处于Beta阶段，部署复杂度中等，需要本地硬件执行LLM。


## 🌐 背景与生态

本地LLM正因其隐私保护和避免云成本而受到关注。基于YAML的工作流因其声明式特性在DevOps中很常见。


## 💬 社区讨论

社区表现出浓厚兴趣，讨论集中在实际应用场景、集成挑战以及本地模型管理的功能请求上。


## 🚀 应用前景

适合需要私有AI操作的企业，如金融或医疗，以及开发自定义AI解决方案的开发者。通过SaaS或API盈利。


## 🔧 技术栈

使用Python、YAML进行工作流定义，支持本地LLM模型如llamafile或gguf，并支持Docker/Kubernetes部署。


## 🎯 上手难度

进阶难度。需要Python 3.8+、本地GPU用于LLM和基本的Docker知识。步骤包括设置环境、下载模型和定义YAML工作流。


## 👥 目标用户

适合需要私有AI解决方案的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

与LangChain和Autogen相比，该项目强调本地执行和YAML工作流，为隐私导向的应用提供了更多控制。


## 📚 参考链接

- [Local LLM : What It Is , Best Models & Hardware (2026)](https://iternal.ai/local-llm)
- [Getting started with LLMs: Local models & prompting | Latitude](https://latitude.so/blog/getting-started-with-llms-local-models-prompting)
- [Using YAML Files to Define Tasks and Parameters for AI Agents](https://empathyfirstmedia.com/yaml-files-ai-agents/)

<details><summary>📄 查看原文内容</summary>


What are you working on? What have you been curious about lately?


--- Top Comments ---

[jzig]: I was laid off a few weeks ago. Then I learned my dad’s carpet cleaning company has been struggling, so I started learning about Google Local Service Ads to help him out. THEN I learned his old Windows desktop CRM was discontinued and one OS update away from no longer working. I wanted a way to track every dollar spent to determine return on ad spend, but the Google LSA dashboard left a lot to be desired. And existing SaaS CRMs didn’t have great integrations to Google Ads API. So I built Crew...

[jjuliano]: Been building this for 2.5 years since Aug 2024. Secure and private AI agents. Declare behaviours of workflows and agencies in YAML, that uses local LLM models. You can export the workflow to Docker, Kubernetes, ISO, or binary, with the local llamafile or gguf model pre-baked. Or just run locally. Just this year, it now includes an agent-loop CLI for coding tasks using local LLM models, alternative to mainstream ones. Project GHA harvests daily llamafile, gguf and openrouter free models you c...

[cbramante]: I have developed an app designed to encourage in-person meetups among groups of friends. It makes it easier to organize outings for people who already know each other. You place a pin on a map and share it with your group. Those who already have the app receive a notification. Those who don&#x27;t can be invited through a universal link. Even without the app they can see the location, the time and the number of confirmed attendees on the web (the app is required to confirm attendance). I am b...

[aaronbrethorst]: I work on a suite of open source public transit software projects, collectively called OneBusAway (or OBA). The software is used by millions of transit riders every day around the world, including in New York City, the Seattle area, San Diego, and Washington, D.C. University of California San Diego has deployed our Wayfinder and Waystation web apps for their 35,000+ students! We&#x27;re getting ready to launch our Vehicle Positions software, which replaces expensive, proprietary vehicle locat...

[chartrow]: I am still working on fast and dense stock market related visualizations, example: Drawdown (from 52-week high) charts for top performing YTD stocks of the NASDAQ 100:  https:&#x2F;&#x2F;chartrow.com&#x2F;top-performers#view=drawdown&amp;p=ytd&amp;in=n...  View the stock charts of holdings of an ETF like ARKK in a dense way:  https:&#x2F;&#x2F;chartrow.com&#x2F;quote&#x2F;arkk&#x2F;holdings#range=10y&amp;ma=20%2C5...  Microsoft business fundamental trends:  https:&#x2F;&#x2F;chartrow.com&#x2F...

</details>
