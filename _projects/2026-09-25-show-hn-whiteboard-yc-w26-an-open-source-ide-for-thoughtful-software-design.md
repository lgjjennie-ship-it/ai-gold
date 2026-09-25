---
layout: default
title: "Whiteboard：一个开源的协作软件设计IDE"
date: 2026-09-25T12:00:00+00:00
discovered_date: 2026-09-25
slug: 2026-09-25-show-hn-whiteboard-yc-w26-an-open-source-ide-for-thoughtful-software-design
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Whiteboard是一个开源的桌面应用程序，它使人类和AI代理能够通过共享工作空间协作设计软件，集成了Claude Code和Codex等工具。 Whiteboard在Hacker News上获得了302个星标和116条评论，显示出显著的社区兴趣。它通过在共享工作空间中集成人类和代理的协作，提供了一种新颖的软件设计方法。 Whiteboard在MIT许可证下发布，目前仅限于macOS，并提供语义差异查看器和决策日志等功能。它与Claude Code和Codex等工具集成。"
tags: "AI, Agent, Software Design, Collaboration, Desktop"
---

# Whiteboard：一个开源的协作软件设计IDE


> Whiteboard是一个开源的桌面应用程序，它使人类和AI代理能够通过共享工作空间协作设计软件，集成了Claude Code和Codex等工具。 Whiteboard在Hacker News上获得了302个星标和116条评论，显示出显著的社区兴趣。它通过在共享工作空间中集成人类和代理的协作，提供了一种新颖的软件设计方法。 Whiteboard在MIT许可证下发布，目前仅限于macOS，并提供语义


**项目链接**：https://github.com/devdotfast/whiteboard
**作者**：sidharthkmenon
**发布时间**：2026-09-24T17:21:36Z
**挖掘日期**：2026-09-25
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agent, Software Design, Collaboration, Desktop


## 📌 项目详解

Whiteboard是一个开源的桌面应用程序，它使人类和AI代理能够通过共享工作空间协作设计软件，集成了Claude Code和Codex等工具。 Whiteboard在Hacker News上获得了302个星标和116条评论，显示出显著的社区兴趣。它通过在共享工作空间中集成人类和代理的协作，提供了一种新颖的软件设计方法。 Whiteboard在MIT许可证下发布，目前仅限于macOS，并提供语义差异查看器和决策日志等功能。它与Claude Code和Codex等工具集成。


## 🌐 背景与生态

Whiteboard解决了软件设计中“白板会议”的需求，开发者可以在此协作理解和迭代系统。它利用CodeOSS进行代码集成和语义差异功能。


## 💬 社区讨论

社区评论对工具审查生成代码的潜力及其独特方法表示兴奋，将其与revue和C4等类似项目进行比较。


## 🚀 应用前景

Whiteboard可用于协作软件设计至关重要的场景，例如在企业架构审查或编码代理原型中。盈利路径包括SaaS或SDK集成。


## 🔧 技术栈

Whiteboard使用Rust为其语义差异查看器，并集成了Claude Code和Codex等工具。它基于CodeOSS构建，并提供类似VSCode的键绑定和LSP支持。


## 🎯 上手难度

使用Whiteboard的难度评级为进阶。前提条件包括macOS系统和对VSCode等工具的熟悉。步骤包括克隆存储库并运行应用程序。


## 👥 目标用户

Whiteboard面向参与软件设计和架构的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括revue，它提供用于叙事代码审查的TUI，以及C4，它提供用于LLM生成架构图的文本表示。


## 📚 参考链接

- [Visual Studio Code - Wikipedia](https://en.wikipedia.org/wiki/Visual_Studio_Code)
- [Code OSS, VSCodium or Visual Studio Code: what should you install on Linux](https://en.linuxadictos.com/code-oss-vscodium-or-visual-studio-code-what-should-i-install-on-linux.html)

<details><summary>📄 查看原文内容</summary>


Hello! We’re Sid, Alex, Ketan, and Milan. We’re building Whiteboard (<a href="https:&#x2F;&#x2F;whiteboard.dev.fast&#x2F;">https:&#x2F;&#x2F;whiteboard.dev.fast&#x2F;</a>), an open-source desktop app where humans and agents can architect software together in a common workspace. Here’s our repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;whiteboard" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;whiteboard</a>.<p>We were missing the feeling of a “whiteboard session” with another dev where you leave with a deep understanding of a system, so we built this app for ourselves. Whiteboard plugs into the tools you already use - e.g. Claude Code, Codex, etc. – and gives your agent an SDK to draw on an in-app canvas to describe its work. We began with an MVP based on HTML artifacts and started rethinking the app as we ran into limitations:<p>1. Built on top of CodeOSS: We found that in pure HTML tools it was hard to connect a spec or diagram to code. In Whiteboard, when you click on visualizations like a sequence diagram, an entity relationship diagram, or a quote from the agent’s trace, you can jump to the underlying code directly. When navigating code, you get keybindings and LSP support from VSCode out of the box. We’ve found this is especially valuable because tradeoffs are often only discovered after a first pass at implementation (re: slop)<p>2. Semantic diff viewer: we wrote a semantic, AST-aware diff viewer in Rust so you can only view the code changes which are relevant to you [1]. We’ve set up some sane defaults: large added functions are summarized as pseudocode, and things like unit tests and large documentation changes are collapsed &#x2F; hidden. This is all customizable with a WASM-based plugin system.<p>3. Decision Log: We found it difficult to reason about what set of decisions our agents made autonomously. So we built tools for agents to query and link their own traces to the Whiteboard, so you can understand how the requirements that you set were implemented, and understand what decisions your agent made autonomously.<p>Here’s a quick demo video explaining more: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ChPn3ftULWE" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ChPn3ftULWE</a><p>Folks at companies like Salesforce and Modal are using Whiteboard today as a review tool for architecture or spec-level changes – really any change where they want to be involved:<p>1. Reviewing your own coding agent’s work: because Whiteboard makes it easier to review large amounts of code, folks will typically have their AI agents create a prototype and a corresponding Whiteboard session so they can iterate on the design.<p>2. Reviewing other people’s changes: We’ve found that Whiteboard is particularly helpful when composed with tools like Greptile. For example, you can run an automated code reviewer on small changes and escalate to a Whiteboard session for the changes that require human judgement.<p>Why we built this: we’re four buddies from college who quit our jobs as tech leads right before agentic coding became industry standard. As we iterated towards an MVP for a previous idea, we struggled to maintain a comprehensible codebase while reaping all the velocity benefits of agentic coding. As more PRs were merged without our understanding, we felt a ‘cognitive debt’ begin to seep in, until it became difficult for us to even contribute to the system [2].<p>We’re releasing our desktop app under an MIT license. Please poke through and feel free to contribute! Eventually we’ll charge companies for a hosted web version that manages whiteboard session creation alongside features like trajectory storage and multiplayer reviews. Everything will always remain self-hostable.<p>Thanks for reading, and we hope you try it out! We would love to hear any feedback and to learn from your expertise.<p>Here’s are the project links again: <a href="https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;whiteboard" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;whiteboard</a>, and you can install (for MacOS + Linux) at <a href="https:&#x2F;&#x2F;install.dev.fast">https:&#x2F;&#x2F;install.dev.fast</a><p>[1] diffs library: <a href="https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;diffr" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;devdotfast&#x2F;diffr</a>
[2] Credit for the term ‘cognitive debt’ goes to  <a href="https:&#x2F;&#x2F;www.geoffreylitt.com&#x2F;2026&#x2F;07&#x2F;02&#x2F;understanding-is-the-new-bottleneck" rel="nofollow">https:&#x2F;&#x2F;www.geoffreylitt.com&#x2F;2026&#x2F;07&#x2F;02&#x2F;understanding-is-the...</a>


--- Top Comments ---

[mtford]: This is really cool! I&#x27;m pumped for anything that makes it easier to review generated code.  I, like many people these days, am searching for ways to stay close to the code whilst not being overwhelmed... and as a visual personal i like your idea to semantically link code to diagrams I&#x27;ve been working on a (semi-)similar thing, a TUI for narrative code reviews -  https:&#x2F;&#x2F;github.com&#x2F;mtford90&#x2F;revue  - the idea being to generate &quot;guided tours&quot; of a change ...

[solatic]: How do you compare to  https:&#x2F;&#x2F;likec4.dev&#x2F;  and  https:&#x2F;&#x2F;erode.dev&#x2F;  , which are currently fully open-source and community driven? C4 gives the text-based representation needed for LLMs to generate and maintain large architecture diagrams - why not build off that heritage?

[bbor]: Oh WOW, cool to see a technique that&#x27;ll be everywhere in 12 months (the fake pen drawing animations + streaming diagrams as they&#x27;re produced) first be announced. Do we still do &quot;First!&quot; comments, y&#x27;all? ~~ [EDIT: you need to put &quot;only for macOS&quot; in way more prominent places, all over -- that offends my soul greatly and may Linus frown upon you all] ~~  [EDIT2: I was mistaken!]  This all looks really solid. That said, two remarks: 1. The integration with OS L...

[_davide_]: The UX seems nice, but the scope is way too narrow.
I would be actually lazier for me to to just rebuild it inside my own harness (exactly as i want it) than start looking at yours.

[icar]: You cannot currently edit files in Whiteboard. If this is something that you find yourself wanting to do, please file an issue!
  
Do you still consider this an IDE? Curious

</details>
