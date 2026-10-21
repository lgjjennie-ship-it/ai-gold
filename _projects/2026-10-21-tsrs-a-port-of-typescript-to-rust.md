---
layout: default
title: "Tsrs：TypeScript编译器在Rust中为WebAssembly"
date: 2026-10-21T12:00:00+00:00
discovered_date: 2026-10-21
slug: 2026-10-21-tsrs-a-port-of-typescript-to-rust
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Tsrs是一个移植到Rust的TypeScript编译器，针对WebAssembly环境进行了优化，与传统TypeScript编译器相比，提供了更快、更内存高效的类型检查。 Tsrs在Hacker News上获得了405个星标和198条评论，显示出强烈的社区兴趣。它解决了在WebAssembly环境中对快速、无垃圾回收编译器的需求，并通过专门的SaaS或API服务具有潜在的盈利能力。 Tsrs遵循MIT许可证，目前处于生产成熟度，部署相对简单。它需要Rust环境并与WebAssembly生态系统集成。"
tags: "TypeScript, Rust, WebAssembly, Compiler, Optimization"
---

# Tsrs：TypeScript编译器在Rust中为WebAssembly


> Tsrs是一个移植到Rust的TypeScript编译器，针对WebAssembly环境进行了优化，与传统TypeScript编译器相比，提供了更快、更内存高效的类型检查。 Tsrs在Hacker News上获得了405个星标和198条评论，显示出强烈的社区兴趣。它解决了在WebAssembly环境中对快速、无垃圾回收编译器的需求，并通过专门的SaaS或API服务具有潜在的盈利能力。 Tsrs遵循


**项目链接**：https://blog.cloudflare.com/typescript-rust-port/
**作者**：hnisjafx40
**发布时间**：2026-10-20T13:18:07Z
**挖掘日期**：2026-10-21
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：TypeScript, Rust, WebAssembly, Compiler, Optimization


## 📌 项目详解

Tsrs是一个移植到Rust的TypeScript编译器，针对WebAssembly环境进行了优化，与传统TypeScript编译器相比，提供了更快、更内存高效的类型检查。 Tsrs在Hacker News上获得了405个星标和198条评论，显示出强烈的社区兴趣。它解决了在WebAssembly环境中对快速、无垃圾回收编译器的需求，并通过专门的SaaS或API服务具有潜在的盈利能力。 Tsrs遵循MIT许可证，目前处于生产成熟度，部署相对简单。它需要Rust环境并与WebAssembly生态系统集成。


## 🌐 背景与生态

WebAssembly已成为高性能网络应用的关键技术，而TypeScript被广泛用于构建复杂的网络前端。Tsrs填补了这一空白，提供了一个基于Rust的快速TypeScript编译器，可以在WebAssembly环境中运行，而以前由于Rust中没有垃圾回收，这具有挑战性。


## 💬 社区讨论

社区评论表达了强烈的兴趣和兴奋，讨论了优化、内存模型以及该项目对TypeScript开发可能产生的影响。也有人对该项目的长期可行性以及AI在该项目中的作用表示怀疑。


## 🚀 应用前景

Tsrs可用于需要在WebAssembly环境中进行高性能TypeScript编译的场景，例如游戏开发、数据处理和复杂网络应用程序。通过针对游戏、金融和电子商务等行业提供SaaS或API服务，可以实现盈利。


## 🔧 技术栈

Tsrs使用Rust编程语言，与WebAssembly生态系统集成，并利用oxc-project的TypeScript类型检查器。它需要Rust环境和对WebAssembly的熟悉。


## 🎯 上手难度

使用Tsrs的难度被评为进阶。前提条件包括Rust环境、对WebAssembly的熟悉和基本的TypeScript知识。步骤包括设置Rust环境、克隆存储库并运行编译器。


## 👥 目标用户

Tsrs的目标用户是TypeScript开发者、Rust爱好者以及需要为他们的项目提供高性能、内存高效编译器选项的WebAssembly用户。


## ⚖️ 类似项目对比

竞争项目包括Babel，这是一个流行的JavaScript编译器，以及esbuild，它以其速度而闻名。这些替代方案侧重于不同的方面，如语言兼容性和构建速度。


## 📚 参考链接

- [Introducing tsrs : a Port of TypeScript to Rust | Cloudflare Blog](https://blog.cloudflare.com/typescript-rust-port/)
- [GitHub - oxc- project / tsrs : Rust port of the TypeScript 7 type checker](https://github.com/oxc-project/tsrs)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[DanRosenwasser]: Hey there, TypeScript team member here. The tsrs project has been extremely interesting to see come together. We&#x27;ve been working with the maintainers to better understand how tsrs is fast and what sorts of optimizations it uses are safe. We even did our own Rust vibe port and what we currently suspect is that a lot of the speed does not just come down to language choice, and some of what is going to make TS 7.1 faster and leaner (see the charts in the blog post) actually comes from optim...

[afdbcreid]: It appears they&#x27;re using a unique memory model ( https:&#x2F;&#x2F;github.com&#x2F;oxc-project&#x2F;tsrs&#x2F;blob&#x2F;main&#x2F;docs&#x2F;PORTING.m... ) to overcome the challenge that prevented the TypeScript team from choosing Rust to begin with: Rust has no GC and porting from a GC language to it often requires restructure of data. Essentially, they fake a GC via never-freed arenas for long-living objects. It&#x27;s interesting that Rust can do that (hopefully soundly)!

[sheepscreek]: Ah took me a while to understand the reason behind this. It wasn’t “let’s build a faster Rust based Typescript compiler” at all. That was a nice side-effect. They needed a Typescript compiler that can run on their WASM only sandbox. So the only existing option was to export tsc Go to WASM, but that comes with the full Go runtime. And to avoid that cost, they experimented with a Rust compiler and turns out it’s even faster than the reference tsc&#x2F;Go implementation.

[egonschiele]: It&#x27;s exciting to see the speed gains. I use TypeScript every day on a large codebase, and it is too slow to run locally.
I don&#x27;t love this change though: &gt; However, frontier AI models can now do large-scale ports almost independently in a matter of days &gt; I wrote zero code. Not &quot;barely any&quot;. Zero So we are going to move from a carefully handwritten port to an entirely AI-generated port. I know this is the way the industry is headed, I use coding agents a ton. But I s...

[weinzierl]: &quot;[..] that a lot of the speed does not just come down to language choice, and some of what is going to make TS 7.1 faster and leaner [..] actually comes from optimizations discovered in tsrs.&quot;  If the improvements were discovered by porting to a different language they very much come down to language choice (even if they can be implemented in the source language of the port). The  &quot;fearless ...&quot;  mottos of Rust are not hyperbole but a serious point. They allow you (and the...

</details>
