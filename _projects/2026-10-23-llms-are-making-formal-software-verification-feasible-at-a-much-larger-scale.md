---
layout: default
title: "LLM实现大规模形式化软件验证"
date: 2026-10-23T12:00:00+00:00
discovered_date: 2026-10-23
slug: 2026-10-23-llms-are-making-formal-software-verification-feasible-at-a-much-larger-scale
source: hackernews
category: show-hn
ai_score: 9.0
summary: "该项目利用LLM实现大规模形式化软件验证，通过自动化证明过程帮助确保代码正确性。 它在Hacker News上获得了高度关注，并解决了软件验证的主要痛点，作为SaaS或API服务具有明确的盈利潜力。 该项目已投入生产，采用开源许可证，但由于需要专用硬件和软件集成，部署复杂性可能较高。"
tags: "LLM, Formal Verification, Software, Security, AI"
---

# LLM实现大规模形式化软件验证


> 该项目利用LLM实现大规模形式化软件验证，通过自动化证明过程帮助确保代码正确性。 它在Hacker News上获得了高度关注，并解决了软件验证的主要痛点，作为SaaS或API服务具有明确的盈利潜力。 该项目已投入生产，采用开源许可证，但由于需要专用硬件和软件集成，部署复杂性可能较高。


**项目链接**：https://www.anthropic.com/research/formal-verification
**作者**：johnbender
**发布时间**：2026-10-22T22:54:43Z
**挖掘日期**：2026-10-23
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：LLM, Formal Verification, Software, Security, AI


## 📌 项目详解

该项目利用LLM实现大规模形式化软件验证，通过自动化证明过程帮助确保代码正确性。 它在Hacker News上获得了高度关注，并解决了软件验证的主要痛点，作为SaaS或API服务具有明确的盈利潜力。 该项目已投入生产，采用开源许可证，但由于需要专用硬件和软件集成，部署复杂性可能较高。


## 🌐 背景与生态

传统的形式化软件验证由于复杂性通常仅限于特定应用领域。LLM通过自动化验证过程的部分环节降低了这一门槛。


## 💬 社区讨论

评论显示出浓厚的兴趣和实际应用，开发者分享了成功案例并讨论了技术挑战。


## 🚀 应用前景

这可以应用于需要高代码正确性的行业，如航空航天、国防和金融，可能作为SaaS或API服务。


## 🔧 技术栈

技术栈可能包括Python、LLM如Claude 3.5 Sonnet以及形式化验证工具如ESBMC。


## 🎯 上手难度

难度：进阶。前提条件包括Python和访问LLM API。步骤涉及设置环境和运行示例验证脚本。


## 👥 目标用户

目标用户是需要高代码正确性的软件开发人员、QA工程师和安全专业人员。


## ⚖️ 类似项目对比

竞争对手包括SpecVerify和其他集成LLM的形式化验证工具，尽管该项目可能在可扩展性方面表现优异。


## 📚 参考链接

- [LLMs are making formal software verification feasible at a ...](https://www.anthropic.com/research/formal-verification)
- [Supporting Software Formal Verification with Large Language ...](https://arxiv.org/html/2507.04857v1)
- [How AI and LLMs Are Revolutionizing Formal Software ...](https://humanemousetrap.org/article/how-ai-and-llms-are-revolutionizing-formal-software-verification)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[mentalgear]: A good moment to remind everyone: Verification: Code does what it says. Validation: Code does what Specifications say. Specifications: Were hopefully correctly modeled to the Problem. In IEEE terms: &gt; Verification: &quot;Are we building the product right?&quot;
&gt; Validation: &quot;Are we building the right product?&quot;) You can write mathematically flawless code that highly efficiently solves the wrong problem. --- While I think formal verification is the future (essential for cyberse...

[malisper]: For those skeptical, I&#x27;ve had decent success using formal verification for my Rust rewrite of Postgres. I wrote a compiler that can translate both Rust and C code into Lean. Once those two functions are in Lean, I have an LLM write a Lean proof that they behave identically. So far, I&#x27;ve proven that about 12% of the code behaves the same when executed single-threaded. That works out to roughly 70k lines of C code. This has found very minor differences in behavior, such as how floatin...

[n_u]: My first question was “How do they know the proof correctly corresponds to the software they are checking?” They say “ While this is an enormous volume of proof code, virtually none of it needs to be manually reviewed. The Rocq proof checker ensures that the spec is correctly satisfied by the proof. As a result, the only artifacts that a developer needs to trust are:
The formal models of RISC-V and of Linux processes; The exact theorem statements that were proved; The Rocq proof checker itsel...

[fedupnow]: Im 35, Im screwed if they get their way. I&#x27;m not going to go to the trades, I quit construction when I was 27 because of how much I loved programming. I wanted to kill myself basically everyday working in the construction industry. I drank my twenties away because of how much it sucked. Ive been sober for years now entirely because of programming and actually loving what I do. But this company is stealing that from me, in many different ways. I invested a ton of my life and my entire lif...

[pjmlp]: This is exactly the kind of stuff I am slowly realising with the increased adoption of agentic runtimes in enterprise SaaS products. We will move into formal verification alongside AI tools, thus generation of executables via translation to 3 GLs is going to be a transition step, just like Assembly coders wary of optimising compilers always wanted to manually check the generated Assembly code. And yes, many of us will have to search another source of income as an outcome of &quot;progress&quot;.

</details>
