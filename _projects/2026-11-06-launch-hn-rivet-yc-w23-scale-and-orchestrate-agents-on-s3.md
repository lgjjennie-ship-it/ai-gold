---
layout: default
title: "Rivet：可扩展的代理编排器"
date: 2026-11-06T12:00:00+00:00
discovered_date: 2026-11-06
slug: 2026-11-06-launch-hn-rivet-yc-w23-scale-and-orchestrate-agents-on-s3
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Rivet是一个开源编排器，使用轻量级代理并通过S3存储扩展和管理代理工作负载，提供高密度和快速处理。 Rivet因其高人气（102个参与评分，53条评论）、对代理编排中演员模型的创新使用以及通过SaaS或API的明确盈利潜力而受到关注。 Rivet是开源的，处于Beta阶段，支持自托管并与S3集成，提供低延迟和成本效益的存储解决方案。"
tags: "Agent, Orchestration, S3, Actor, Scalability, Cloud"
---

# Rivet：可扩展的代理编排器


> Rivet是一个开源编排器，使用轻量级代理并通过S3存储扩展和管理代理工作负载，提供高密度和快速处理。 Rivet因其高人气（102个参与评分，53条评论）、对代理编排中演员模型的创新使用以及通过SaaS或API的明确盈利潜力而受到关注。 Rivet是开源的，处于Beta阶段，支持自托管并与S3集成，提供低延迟和成本效益的存储解决方案。


**项目链接**：https://github.com/rivet-dev/rivet
**作者**：NathanFlurry
**发布时间**：2026-11-05T17:17:42Z
**挖掘日期**：2026-11-06
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：Agent, Orchestration, S3, Actor, Scalability, Cloud


## 📌 项目详解

Rivet是一个开源编排器，使用轻量级代理并通过S3存储扩展和管理代理工作负载，提供高密度和快速处理。 Rivet因其高人气（102个参与评分，53条评论）、对代理编排中演员模型的创新使用以及通过SaaS或API的明确盈利潜力而受到关注。 Rivet是开源的，处于Beta阶段，支持自托管并与S3集成，提供低延迟和成本效益的存储解决方案。


## 🌐 背景与生态

Rivet的开发是为了解决管理代理工作负载的可扩展性和效率挑战，为传统的基于沙盒的方法提供了一种替代方案。


## 💬 社区讨论

社区评论强调了Rivet的效率、可扩展性，并将其与Cloudflare Durable Objects进行比较，有些人探索了它在多人游戏中的潜力。


## 🚀 应用前景

Rivet可应用于多人游戏、实时系统和复杂代理工作负载，通过SaaS或API服务具有盈利潜力。


## 🔧 技术栈

Rivet使用Rust、演员、带有SSD缓存的SQLite以及S3进行存储，提供高性能和可扩展的基础设施。


## 🎯 上手难度

入门评级为进阶，需要Python、GPU和API密钥，步骤包括在S3上部署工作实例。


## 👥 目标用户

目标用户包括游戏和实时系统行业的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Cloudflare Durable Objects和AWS Lambda，Rivet提供更高的灵活性和开源优势。


## 📚 参考链接

- [Orchestrating multi-agent AI architectures with Amazon S3 ...](https://aws.amazon.com/blogs/storage/orchestrating-multi-agent-ai-architectures-with-amazon-s3-files/)

<details><summary>📄 查看原文内容</summary>


Hey HN, this is Nathan and Nicholas from Rivet (<a href="https:&#x2F;&#x2F;rivet.dev">https:&#x2F;&#x2F;rivet.dev</a>) – a fast, high-density, and scalable orchestrator for agentic workloads using the actor model. Rather than running a heavyweight sandbox per agent, each agent gets a lightweight actor backed by S3.<p>Actors provide a long-lived process for long agent turns, in-memory state for context, a WebSocket server for multiplayer, durable SQLite storage backed by S3, and hibernation when idle.<p>It&#x27;s a similar model to Cloudflare Durable Objects, but it’s open source and self-hostable.<p>Here’s a video walkthrough: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=3Ev6I7DOV9c" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=3Ev6I7DOV9c</a><p>When we went through YC in 2023, we were building infrastructure for multiplayer games like Diep and Krunker. This involved heavily optimizing high-throughput matchmaking, real-time player messages, and blitz scaling. Through that process, we spent a lot of time on workloads where Postgres couldn&#x27;t keep up with our throughput. We started out by hacking together Lua scripts on top of Redis, but this became too cumbersome to maintain and upgrade. This led us to extend our game server orchestrator to support what we call Rivet Actors today: many lightweight workers with in-memory state and durable storage. By using actors, we were able to serve tens of millions of monthly active users.<p>As agents grew in popularity, it became clear that running agents in sandboxes is inefficient. Sandboxes are expensive, mostly idle, and slow to start. Developers started using actors because they are far more memory efficient (72 KB baseline for actors vs 512 MB for a minimal sandbox) and fast to start (4.9 ms p99 for actors vs 1.7 s p99 for sandboxes).<p>For example, Amp is using Rivet to orchestrate multiplayer agents. They originally tried to build on Cloudflare Durable Objects, but couldn’t launch because of the platform’s limitations and unresponsive support. They migrated to Rivet Actors in a weekend and deploy on-prem. Rivet’s flexible architecture lets them adapt it to their own use cases without being constrained by a framework or the memory, storage, and runtime limits of Cloudflare Durable Objects.<p>Under the hood, Rivet is backed by S3 while maintaining SSD speeds.<p>Why S3? Previously, Rivet ran on FoundationDB. However, we were surprised to find that companies are storing orders of magnitude more data on Rivet Actors than in Postgres, such as large session transcripts, agent artifacts, and full POSIX filesystems. As their data grew, they had to start paying for SSDs that sat mostly idle with old transcripts. This led us to double down on S3 as our primary storage medium without sacrificing performance. This choice means that data stored on Rivet is 10× cheaper than on EBS gp3 while maintaining SSD speeds.<p>It’s not as simple as writing data straight to S3. Lots of PUTs for tiny blobs of data are slow and expensive. Instead, we use an SSD tier to optimize speed and cost:<p>When you write data to an actor’s SQLite database, the write is acknowledged once SSDs in 2 of 3 availability zones have it. Then, the data is batched to S3 in the background. This means that S3 is never on the write path, which lowers latency and cost. When reading data or waking an actor, Rivet reads from SSDs if already cached and falls back to S3 if not. SSD caches can be tuned to meet your needs, giving you configurable tiered storage for your actors.<p>This architecture lets Rivet provide 1.07 ms durable writes (3 AZ, p99), 1.36 ms reads (p99), and 138 ms reads from object storage (p99).<p>We’ve spent a lot of time making sure that Rivet can run wherever you need it. Self-hosting requires deploying a single Rust binary with S3 as the only dependency, Rivet Cloud lets you deploy dedicated clusters on AWS or GCP in any region, and BYOC lets us deploy Rivet to your VPC without having to operate it yourself. Rivet also runs identically in local dev as in production, since Rivet is a lightweight binary that runs anywhere<p>Rivet Actors can be written in TypeScript or Rust. Out of the box, they support agents (Pi Durable), workflows, real-time, multiplayer, running AI-generated code, Durable Streams, and integrations with tools like Vercel’s Eve and Turso. See all of our available guides, or point your agent at them: <a href="https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;#guides">https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;#guides</a><p>Try it out now, by reading our quickstart guides (<a href="https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;">https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;</a>) or ask your agent: “Run npx skills add rivet-dev&#x2F;skills, then build a multiplayer chat agent and run it locally.”<p>We’d love to get feedback on your experience with Rivet! We’re deeply invested in making Rivet an easy-to-self-host, flexible, and efficient way to run agentic workloads.<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;rivet-dev&#x2F;rivet" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;rivet-dev&#x2F;rivet</a><p>Architecture: <a href="https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;architecture&#x2F;">https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;architecture&#x2F;</a><p>Benchmarks: <a href="https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;benchmarking&#x2F;">https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;benchmarking&#x2F;</a><p>Self-hosting: <a href="https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;deploy&#x2F;self-host&#x2F;">https:&#x2F;&#x2F;rivet.dev&#x2F;docs&#x2F;deploy&#x2F;self-host&#x2F;</a>


--- Top Comments ---

[jaekwon]: Not  using the actor model, and yet massively parallel:  https:&#x2F;&#x2F;gnosh.ai&#x2F;swarm.html  I wonder when one approach will be used over the other. Actually, I can imagine both approaches working together. Just filed two provisional patents on this stuff today; build on gno.land and let&#x27;s talk shop, I see symbiosis.

[kianN]: &gt; When you write data to an actor’s SQLite database, the write is acknowledged once SSDs in 2 of 3 availability zones have it. Then, the data is batched to S3 in the background. This means that S3 is never on the write path, which lowers latency and cost. When reading data or waking an actor, Rivet reads from SSDs if already cached and falls back to S3 if not. SSD caches can be tuned to meet your needs, giving you configurable tiered storage for your actors. As someone who is not incredibl...

[fastball]: Rivet is very cool. Switched a Cloudflare Durable Object piece of our infrastructure that lived in its own little fairy tale land to our own infra within the rest of our VPC. Was a very pleasant experience. Haven&#x27;t had the chance to try Rivet v3 yet but hoping to get to it soon.

[alexey_anshakov]: Moving state persistence to write-ahead SQLite tiered into S3 is a very clean answer to the latency-cost trap of raw object storage. The big operational win with decoupled actor state like this is avoiding zombie locks when an agent execution times out mid-turn. Curious how you handle split-brain fencing if an actor network partition occurs while a batched write is still draining to S3.

[sebastienburel]: How does hibernation decide an actor is idle? In my agent runtime actors run in XS. Messages are queued and only handled once the current handler returns, so a synchronous handler is never cut in half. But while a handler waits on an async call, an HTTP request say, other messages still get handled. So “no message being processed” isn’t the same as “nothing in flight”. Does Rivet hibernate an actor with an outstanding request, and if so, what happens when the response comes back?

</details>
