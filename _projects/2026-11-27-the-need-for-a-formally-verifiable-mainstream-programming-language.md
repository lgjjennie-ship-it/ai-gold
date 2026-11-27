---
layout: default
title: "形式化可验证主流语言提案"
date: 2026-11-27T12:00:00+00:00
discovered_date: 2026-11-27
slug: 2026-11-27-the-need-for-a-formally-verifiable-mainstream-programming-language
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该提案提出一种形式化可验证的主流编程语言，旨在提高软件可靠性和正确性，并专注于WebAssembly集成。 该项目因其Hacker News上的关注度以及解决软件开发中对更可靠代码的迫切需求（尤其是在AI生成代码日益普及的背景下）而具有重要意义。 该语言旨在实现主流采用，并专注于形式化验证。目前处于alpha阶段，在达到生产就绪之前仍需大量开发。"
tags: "Formal Verification, Programming Language, AI, Code Reliability, WebAssembly"
---

# 形式化可验证主流语言提案


> 该提案提出一种形式化可验证的主流编程语言，旨在提高软件可靠性和正确性，并专注于WebAssembly集成。 该项目因其Hacker News上的关注度以及解决软件开发中对更可靠代码的迫切需求（尤其是在AI生成代码日益普及的背景下）而具有重要意义。 该语言旨在实现主流采用，并专注于形式化验证。目前处于alpha阶段，在达到生产就绪之前仍需大量开发。


**项目链接**：https://blainehansen.me/post/mainstream-verifiable-language/
**作者**：todsacerdoti
**发布时间**：2026-11-27T05:22:06Z
**挖掘日期**：2026-11-27
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Formal Verification, Programming Language, AI, Code Reliability, WebAssembly


## 📌 项目详解

该提案提出一种形式化可验证的主流编程语言，旨在提高软件可靠性和正确性，并专注于WebAssembly集成。 该项目因其Hacker News上的关注度以及解决软件开发中对更可靠代码的迫切需求（尤其是在AI生成代码日益普及的背景下）而具有重要意义。 该语言旨在实现主流采用，并专注于形式化验证。目前处于alpha阶段，在达到生产就绪之前仍需大量开发。


## 🌐 背景与生态

形式化验证传统上用于特定领域，但随着AI生成代码的兴起，其可靠性问题日益突出，因此正获得更多关注。WebAssembly提供了一个理想的沙盒环境，适用于此类验证。


## 💬 社区讨论

评论从对形式化验证实用性的质疑到对其在AI生成代码中应用的热情，一些人将其与现有的验证工具进行了比较。


## 🚀 应用前景

该语言可用于需要高可靠性的行业，如航空航天、汽车和医疗保健，通过实现对关键系统和AI生成代码的验证。


## 🔧 技术栈

该语言围绕WebAssembly构建，可能使用Rust或类似语言以确保性能和安全性，并结合Dafny或SPARK等形式化验证工具。


## 🎯 上手难度

难度：进阶。前提是熟悉像Rust这样的编程语言以及形式化验证概念。安装涉及设置一个带有WebAssembly支持的开发环境。


## 👥 目标用户

目标用户包括在软件可靠性至关重要的行业中工作的后端工程师、机器学习实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Dafny、SPARK Ada和Verus，它们专注于形式化验证但缺乏主流采用。Zena与之相似，但针对WebAssembly以用于AI代码。


## 📚 参考链接

- [Formal verification - Wikipedia](https://en.wikipedia.org/wiki/Formal_verification)
- [WebAssembly](https://webassembly.org/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[hresvelgr]: &quot;Beware of bugs in the above code; I have only proved it correct, not tried it.&quot; — Donald Knuth Formal correctness does not guarantee desired function. People have written TLA+ specs for their software[1] and not have it materially improve the quality or reliability. You cannot just throw formal verification at a problem. I am very much of the opinion that crap code is an issue of organisation and aesthetics, and that  can  be automated. This is something that is enforced by framewo...

[Buttons840]: The author has another blog post about Flow Effects[0]. They propose an open-ended set of effects you could attach to functions, and then verify, at compile time, that certain functions either do or do not invoke certain effects. So if I had some functions like:       foo_1 (must NOT access the HDD)
    foo_2
    foo_3
    foo_4 (does access the HDD)
  
Only 2 of them are annotated with effects related to HDD access, but we can verify at compile time that foo_1 does NOT invoke foo_4, either d...

[spankalee]: Wow, I feel like Blaine is describe a language a lot like the one I&#x27;m working on now, Zena:  https:&#x2F;&#x2F;zena-lang.dev&#x2F;  I started Zena from wanting a TypeScript-like syntax that compiled to very efficient WebAssembly GC, and AssemblyScript had issues... The motivation for targeting Wasm was as a good sandboxing and orchestration unit for AI-generated code. So, out of both general PL curiosity and enthusiasm, and an attempt to make a language that&#x27;s good for AI generation...

[porcoda]: Dafny, SPARK Ada, Why3, Verus, Frama-C, TLA+, etc. are all sort of in this direction for different languages and styles of verification.  It is nice to see them getting attention now that LLMs make them digestible for a broader set of programmers.  I&#x27;m not sure one can start with a goal of creating a &quot;mainstream&quot; language that is verification-oriented.  Mainstreamness comes from adoption.  I&#x27;d look at those past languages (like the ones I listed), and ask &quot;why did the...

[thomasahle]: Rather than migrating all code to some new program language, I&#x27;ve been building ProgLib:  https:&#x2F;&#x2F;github.com&#x2F;thomasnormal&#x2F;proglib  which is like &quot;MathLib for Programming&quot;. It allows you to import code from any programming language (So far, Python, C++, Rust, and SystemVerilog are partially supported,) and prove stuff about it in Lean. You don&#x27;t need a &quot;verifiable programming language&quot;. All you need is formalized semantics for the programming l...

</details>
