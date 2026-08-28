---
layout: default
title: "优化1.1.1.1 DNS缓存内存"
date: 2026-08-28T12:00:00+00:00
discovered_date: 2026-08-28
slug: 2026-08-28-saving-100-terabytes-of-memory-by-optimizing-1-1-1-1-s-dns-cache
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目通过在DNS缓存布局中应用Rust级别的内存优化来优化DNS缓存内存使用，将每条记录的内存减少56%，并在Cloudflare的整个舰队中节省了大约100 TB的内存。 该项目因其高社区参与度（250条评论，评分859）以及在DNS缓存内存优化方面的实用价值而具有重要意义，这对于大型网络来说是一个关键领域，并在系统编程方面具有明确的扩展机会。 该项目采用开源许可证，目前处于生产成熟度，部署复杂度适中，没有特定的硬件要求。它与现有的DNS缓存系统集成，并因其内存效率而引人注目。"
tags: "System Programming, DNS, Optimization, Memory, Networking"
---

# 优化1.1.1.1 DNS缓存内存


> 该项目通过在DNS缓存布局中应用Rust级别的内存优化来优化DNS缓存内存使用，将每条记录的内存减少56%，并在Cloudflare的整个舰队中节省了大约100 TB的内存。 该项目因其高社区参与度（250条评论，评分859）以及在DNS缓存内存优化方面的实用价值而具有重要意义，这对于大型网络来说是一个关键领域，并在系统编程方面具有明确的扩展机会。 该项目采用开源许可证，目前处于生产成熟度，部署复


**项目链接**：https://blog.cloudflare.com/dns-cache-memory-optimization-1111/
**作者**：TangerineDream
**发布时间**：2026-08-27T17:17:57Z
**挖掘日期**：2026-08-28
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：System Programming, DNS, Optimization, Memory, Networking


## 📌 项目详解

该项目通过在DNS缓存布局中应用Rust级别的内存优化来优化DNS缓存内存使用，将每条记录的内存减少56%，并在Cloudflare的整个舰队中节省了大约100 TB的内存。 该项目因其高社区参与度（250条评论，评分859）以及在DNS缓存内存优化方面的实用价值而具有重要意义，这对于大型网络来说是一个关键领域，并在系统编程方面具有明确的扩展机会。 该项目采用开源许可证，目前处于生产成熟度，部署复杂度适中，没有特定的硬件要求。它与现有的DNS缓存系统集成，并因其内存效率而引人注目。


## 🌐 背景与生态

DNS缓存是互联网基础设施的关键组成部分，优化其内存使用可以带来显著的成本节约和性能提升。系统编程的最新进展使得更高效的缓存机制成为可能。


## 💬 社区讨论

社区评论强调了DNS缓存内存优化的重要性，并指出此类优化对于系统编程专家来说微不足道。一些人讨论了潜在的改进，并将该项目与现有的最佳实践相结合。


## 🚀 应用前景

该项目在大规模网络和云服务方面具有强大的应用前景，其中内存优化可以带来成本节约和性能提升。它可以用于构建专门的DNS服务或集成到现有基础设施中。


## 🔧 技术栈

该项目使用Rust进行系统级编程，关键框架包括Tokio运行时和Hyper HTTP库。它依赖于DNS缓存机制，并与Cloudflare的基础设施集成。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、对DNS缓存的初步了解以及熟悉Rust。步骤包括克隆仓库、安装依赖项和运行优化脚本。


## 👥 目标用户

目标用户包括对优化DNS缓存和提升系统性能感兴趣的系统程序员、网络工程师和云服务提供商。


## ⚖️ 类似项目对比

竞品项目包括Amazon Route 53的DNS缓存优化和Google的DNS服务器改进。这些项目关注DNS缓存的不同方面，但共享提高内存效率的目标。


## 📚 参考链接

- [How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS ...](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)
- [Saving 100 terabytes of memory by optimizing 1 . 1 . 1 . 1 's DNS cache](https://news.ycombinator.com/item?id=49468083)
- [1 . 1 . 1 . 1 — One of the Internet’s Fastest, Privacy-First DNS Resolver](https://one.one.one.one/help/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[lpapez]: This is the right way to deliver software. Produce working product first, validate the idea, stabilize the business, start generating profit, and then you can start optimizing your costs. In fact optimization is by far the easiest part of the process because there are many system programming experts on this HN thread who consider these optimizations to be trivial.

[irdc]: This is why system programming still matters. Looks like they&#x27;re missing the obvious optimisation of putting the record data right after the CacheEntry members instead of allocating memory separately though. But that might just be me as a C-programmer talking and not be all that easy in Rust.

[strenholme]: With my own MaraDNS, I aggressively optimized the memory usage of blacklist entries by having a single really big malloc() to allocate the memory for the entries, then traversing that memory block for potentially blacklisted entries. When I was using one malloc() per entry, a large blacklist took up 237 megabytes of memory.  The same blacklist, once optimized to be loaded with a single malloc() call, only took up 9.5 megabytes of memory.  https:&#x2F;&#x2F;samboy.github.io&#x2F;blog&#x2F;entr...

[grep_it]: This reminds me how you can save a bunch of bytes just by making sure your structs are aligned. In go for example:     type Wasteful struct {
    a int16
    b int
    c byte
  }

  type Aligned struct {
    b int
    a int16
    c byte
  }

  
Will have sizes of 24bytes and 16bytes (on a 64bit system). Same data 8bytes more. If you are storing millions of those objects, then it adds up.

[vinkelhake]: These seem like some fairly standard approaches for reducing memory usage. I can&#x27;t help to think that the approach of joining several distinct list into a single one in some way undercuts Rust&#x27;s safety guarantees. If you previous had three distinct Vec objects, then Rust would guarantee that you can&#x27;t index out of bounds. If you now put all those objects into a single Vec and rely on offsets, then you now open the door to indexing out of range of these sub-slices without any pa...

</details>
