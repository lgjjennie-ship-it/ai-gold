---
layout: default
title: "Scriptc：TypeScript到原生编译器"
date: 2026-07-27T12:00:00+00:00
discovered_date: 2026-07-27
slug: 2026-07-27-scriptc-by-vercel-typescript-to-native-compiler-no-javascript-engine-in-binary
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Scriptc将TypeScript编译为原生可执行文件，无需JavaScript引擎，专注于性能并减少二进制文件大小。 它通过消除JavaScript引擎来解决高性能应用的需求，因其创新方法和对AI的潜在应用而获得关注。 Scriptc采用MIT许可证，处于alpha阶段，需要C++工具链知识，面向性能关键型应用。"
tags: "TypeScript, Compiler, Native, Performance, AI"
---

# Scriptc：TypeScript到原生编译器


> Scriptc将TypeScript编译为原生可执行文件，无需JavaScript引擎，专注于性能并减少二进制文件大小。 它通过消除JavaScript引擎来解决高性能应用的需求，因其创新方法和对AI的潜在应用而获得关注。 Scriptc采用MIT许可证，处于alpha阶段，需要C++工具链知识，面向性能关键型应用。


**项目链接**：https://github.com/vercel-labs/scriptc
**作者**：maxloh
**发布时间**：2026-07-26T22:46:10Z
**挖掘日期**：2026-07-27
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：TypeScript, Compiler, Native, Performance, AI


## 📌 项目详解

Scriptc将TypeScript编译为原生可执行文件，无需JavaScript引擎，专注于性能并减少二进制文件大小。 它通过消除JavaScript引擎来解决高性能应用的需求，因其创新方法和对AI的潜在应用而获得关注。 Scriptc采用MIT许可证，处于alpha阶段，需要C++工具链知识，面向性能关键型应用。


## 🌐 背景与生态

随着TypeScript的普及，对无需JavaScript引擎的原生编译的需求日益增长，特别是在AI和高性能计算领域。


## 💬 社区讨论

社区评论意见不一，一些人怀疑Vercel的进展，其他人则在探索类似项目如Porforr和PerryTS。


## 🚀 应用前景

适用于需要低延迟和最小资源使用的AI模型和应用，如边缘计算和实时系统。


## 🔧 技术栈

使用TypeScript和C++构建，利用TypeScript编译器进行类型检查并生成C++源文件。


## 🎯 上手难度

进阶难度。需要C++工具链、Python 3.8+和对TypeScript的理解。


## 👥 目标用户

适合后端工程师、ML从业者以及游戏和金融等性能关键行业的开发者。


## ⚖️ 类似项目对比

竞品包括Porforr（相似目标）和AssemblyScript（npm生态兼容性）。


## 📚 参考链接

- [GitHub - vercel-labs/scriptc: TypeScript-to-Native Compiler · GitHub](https://github.com/vercel-labs/scriptc)
- [scriptc | TypeScript-to-Native Compiler](https://scriptc.dev/)
- [A Step Towards Compiling TypeScript to Native | by Casper Beyer | Commit Log | Medium](https://medium.com/commitlog/a-step-towards-compiling-typescript-caefa4944994)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[acmnrs]: Porforr&lt; https:&#x2F;&#x2F;porffor.dev &gt; has been working towards the same goal for a while. The creator, CanadaHonk&lt; https:&#x2F;&#x2F;honk.foo &gt;, is extremely talented and the project still only passes ~68% of Test262. I&#x27;m more than a little suspicious of how Vercel has made so much progress so fast, unless I&#x27;m misunderstanding the scope of this project.

[sheept]: One of the strengths of TypeScript besides its expressiveness is that it&#x27;s compatible with the massive npm ecosystem. Most packages only ship untyped JavaScript with type declarations defining the interface,[0] so realistically you&#x27;d still need a JavaScript engine if you use any packages. But if you&#x27;re starting from scratch and know you won&#x27;t be using any npm packages, you might as well use AssemblyScript.[2] [0]: Publishing packages in TypeScript is explicitly discouraged...

[chilipepperhott]: It&#x27;s difficult to ignore how the README is filled with Claudisms.

[satvikpendem]: A lot of people are trying this now with AI, a native TypeScript compiler, for example  https:&#x2F;&#x2F;github.com&#x2F;PerryTS&#x2F;pry . It&#x27;s a compelling value proposition, TypeScript is already well typed and barring a few cases it can be turned into machine code without a JS runtime.

[localhoster]: Funny to see vercel is loosing all credibility under the influence of AI.
Never liked their products anyway, so I believe it&#x27;s a net positive for the industry :)

</details>
