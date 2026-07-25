---
layout: default
title: "可扩展的 PostgreSQL LISTEN/NOTIFY"
date: 2026-07-25T12:00:00+00:00
discovered_date: 2026-07-25
slug: 2026-07-25-postgres-listen-notify-actually-scales
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目探索如何通过使用 Rust 和 GraphQL 订阅代理来高效扩展 PostgreSQL 的 LISTEN/NOTIFY 功能，以处理大量订阅。 它解决了数据库可扩展性中的实际问题，活跃的讨论表明其实用性和兴趣，暗示了扩展到更大系统的潜力。 该项目使用 Rust 和 GraphQL 订阅代理，内容中未明确提及许可证和成熟度级别。"
tags: "Database, PostgreSQL, Scalability, Networking, Performance"
---

# 可扩展的 PostgreSQL LISTEN/NOTIFY


> 该项目探索如何通过使用 Rust 和 GraphQL 订阅代理来高效扩展 PostgreSQL 的 LISTEN/NOTIFY 功能，以处理大量订阅。 它解决了数据库可扩展性中的实际问题，活跃的讨论表明其实用性和兴趣，暗示了扩展到更大系统的潜力。 该项目使用 Rust 和 GraphQL 订阅代理，内容中未明确提及许可证和成熟度级别。


**项目链接**：https://www.dbos.dev/blog/postgres-listen-notify-scalability
**作者**：KraftyOne
**发布时间**：2026-07-24T19:05:53Z
**挖掘日期**：2026-07-25
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Database, PostgreSQL, Scalability, Networking, Performance


## 📌 项目详解

该项目探索如何通过使用 Rust 和 GraphQL 订阅代理来高效扩展 PostgreSQL 的 LISTEN/NOTIFY 功能，以处理大量订阅。 它解决了数据库可扩展性中的实际问题，活跃的讨论表明其实用性和兴趣，暗示了扩展到更大系统的潜力。 该项目使用 Rust 和 GraphQL 订阅代理，内容中未明确提及许可证和成熟度级别。


## 🌐 背景与生态

PostgreSQL 的 LISTEN/NOTIFY 是一个用于实时通信的功能，但在可扩展性方面存在挑战。该项目旨在通过集成 Rust 和 GraphQL 来克服这些限制。


## 💬 社区讨论

开发者对使用 Rust 进行可扩展性的潜力感到兴奋，有些人分享了积极的经验，其他人则讨论了优化挑战。


## 🚀 应用前景

这可用于需要实时数据库更新的应用程序，例如金融系统或社交媒体平台，通过 SaaS 或 API 模型进行货币化。


## 🔧 技术栈

技术栈包括 PostgreSQL、Rust 和 GraphQL 订阅代理，基础设施可能使用 Docker 或 Kubernetes。


## 🎯 上手难度

难度：进阶。前提条件包括 Python、Rust 和 PostgreSQL 数据库。步骤涉及设置代理和配置订阅。


## 👥 目标用户

目标用户是需要可扩展实时数据解决方案的金融或电子商务行业后端工程师和数据库管理员。


## ⚖️ 类似项目对比

竞品包括像 Kafka 这样的实时数据流项目和像 Redis 这样的内存数据存储项目，它们提供不同的可扩展方法。


## 📚 参考链接

- [PostgreSQL: Documentation: 18: NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html)
- [PostgreSQL: Documentation: 18: LISTEN](https://www.postgresql.org/docs/current/sql-listen.html)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[jerf]: &quot;Scale&quot; isn&#x27;t a binary, it&#x27;s a continuum. &quot;Scales to 60K&#x2F;s&quot; can be 5 orders of magnitude more than one system needs and 5 orders of magnitude too small for another. Personally I&#x27;d knock the general &quot;premature optimization&quot; off the list of &quot;most common developer errors&quot; and put in its place &quot;using techs with the wrong scaling factors&quot;. If you use something too small and you exceed its needs, the failure is obvious, but the o...

[phamilton]: Just sharing a data point and experience. We had a lot of success with LISTEN&#x2F;NOTIFY when we paired it with a Rust graphql subscription broker. 10s of thousands of subscriptions, but only 3 or 4 LISTEN connections (one for each host). All changes would be pushed out to all hosts, who would each manage the actual user subscriptions and choose what to actually publish. This worked super well. In general, moving from hundreds of Ruby or Node hosts to just a few Rust hosts just allows so man...

[nzoschke]: I continue to love DBOS for how it just leverages Postgres (and now SQLite) properly. It&#x27;s effortless to drop into an existing CRUD stack. Once you start down the &quot;durable workflows&quot; path, you start seeing them everywhere. My latest experiments are treating individual emails as durable workflows, where you, the people you&#x27;re communicating with, agents and tools like GitHub or Attio all take turns in the flow.  https:&#x2F;&#x2F;housecat.com&#x2F;blog&#x2F;gmail-durable-wor...

[vhiremath4]: I once was the CTO of a company that serviced about 100k requests per day across all our services. We grew to millions and eventually 10&#x27;s of millions, but, somewhere along the way, an engineer on our team decided he wanted to build a queue off LISTEN&#x2F;NOTIFY semantics in order to take advantage of strong consistency with the rest of our data model, which seemed reasonable given LISTEN&#x2F;NOTIFY is not that hard to understand and we did need consistency guarantees for this workflow...

[dang]: Related, presumably:  Postgres LISTEN&#x2F;NOTIFY does not scale  -  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44490510  - July 2025 (321 comments)

</details>
