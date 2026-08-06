---
layout: default
title: "Celld：自托管分布式持久对象"
date: 2026-08-06T12:00:00+00:00
discovered_date: 2026-08-06
slug: 2026-08-06-celld-self-hosted-distributed-durable-objects
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Celld使开发者能够在自己的服务器上运行分布式持久对象，通过提供自托管环境，为特定的云解决方案提供了一个替代方案。 该项目因其188条社区评论和Hacker News上的活跃讨论而具有重要意义，表明开发者对此兴趣浓厚。它解决了对自托管分布式系统的需求，这是云独立趋势中一个不断增长的需求。 该项目在开源许可证下提供，目前处于alpha阶段，需要对分布式系统和云存储配置有基本的了解。"
tags: "DurableObjects, Self-Hosted, Distributed Systems, Cloudflare, Developer Tools"
---

# Celld：自托管分布式持久对象


> Celld使开发者能够在自己的服务器上运行分布式持久对象，通过提供自托管环境，为特定的云解决方案提供了一个替代方案。 该项目因其188条社区评论和Hacker News上的活跃讨论而具有重要意义，表明开发者对此兴趣浓厚。它解决了对自托管分布式系统的需求，这是云独立趋势中一个不断增长的需求。 该项目在开源许可证下提供，目前处于alpha阶段，需要对分布式系统和云存储配置有基本的了解。


**项目链接**：https://github.com/denoland/celld
**作者**：calvinfo
**发布时间**：2026-08-05T16:50:06Z
**挖掘日期**：2026-08-06
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：DurableObjects, Self-Hosted, Distributed Systems, Cloudflare, Developer Tools


## 📌 项目详解

Celld使开发者能够在自己的服务器上运行分布式持久对象，通过提供自托管环境，为特定的云解决方案提供了一个替代方案。 该项目因其188条社区评论和Hacker News上的活跃讨论而具有重要意义，表明开发者对此兴趣浓厚。它解决了对自托管分布式系统的需求，这是云独立趋势中一个不断增长的需求。 该项目在开源许可证下提供，目前处于alpha阶段，需要对分布式系统和云存储配置有基本的了解。


## 🌐 背景与生态

持久对象是一个由Cloudflare开创的概念，它将计算与存储相结合，为网页开发提供了一种独特的方法。Celld旨在将这一概念带到自托管环境中，减少对云服务提供商的依赖。


## 💬 社区讨论

社区评论表达了对项目将持久对象去中心化的潜力的兴奋，一些人请求本地开发的功能，并将它与Cloudflare的WorkerD进行了比较。


## 🚀 应用前景

Celld可应用于需要去中心化和安全数据处理的场景，如供应链管理和去中心化应用。通过SaaS服务或API访问可以实现盈利。


## 🔧 技术栈

技术栈包括Go用于后端服务，以及对Cloudflare持久对象API的依赖，用于对象存储和管理。


## 🎯 上手难度

入门评级为进阶，需要基本的Go和云存储知识。先决条件包括安装了Go的服务器和对持久对象的理解。


## 👥 目标用户

目标用户包括后端开发者、DevOps工程师以及希望减少关键应用云依赖的组织。


## ⚖️ 类似项目对比

竞品包括Cloudflare的WorkerD，这是一个特定于Cloudflare的解决方案，以及其他自托管的分布式系统项目，如Redis和PostgreSQL。


## 📚 参考链接

- [Overview · Cloudflare Durable Objects docs](https://developers.cloudflare.com/durable-objects/)
- [What Are Distributed Systems ? | Splunk](https://embargo.splunk.com/en_us/blog/learn/distributed-systems.html)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[sakesun]: Wonder if this will become common practice from now on ?     &gt; Pull requests are disabled. Coding agents make it too easy to send a large, 
  &gt; low-context change that costs maintainers more time than it saves. 
  &gt; Thoughtful contributions are welcome; please understand the code, 
  &gt; keep the patch focused, and respect the review time you are asking for.
  &gt; 
  &gt; Send a git format-patch attachment to ...

[jitl]: what is the difference between celld and Cloudflare Workers open source version workerd?  https:&#x2F;&#x2F;github.com&#x2F;cloudflare&#x2F;workerd

[khalidx]: Finally! So happy to see support for running durable objects outside of one provider. Upvoted. The &quot;durable object&quot; concept has been repeatably demonstrated to be a valuable abstraction. &quot;Each object is its own SQLite database, addressed by name and replicated to an S3-compatible bucket you own&quot; -- this concept can take you a long way, both in its power and simplicity.

[jumploops]: I recently spun up a simple app for our annual mango tasting event[0] using Cloudflare Workers and Durable Objects. It worked really well! Excited to see more options outside of Cloudflare. [0] https:&#x2F;&#x2F;github.com&#x2F;jumploops&#x2F;mangotango

[hhthrowaway1230]: I like it! Would be great if I could run locally from the start without configuring an s3 for easy playing&#x2F;prototyping

</details>
