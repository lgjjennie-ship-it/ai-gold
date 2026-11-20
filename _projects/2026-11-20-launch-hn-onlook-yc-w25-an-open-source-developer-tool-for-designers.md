---
layout: default
title: "Onlook：基于代理的设计工具"
date: 2026-11-20T12:00:00+00:00
discovered_date: 2026-11-20
slug: 2026-11-20-launch-hn-onlook-yc-w25-an-open-source-developer-tool-for-designers
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Onlook 是一个开源工具，允许设计师使用他们现有的代理直接在代码库中创建设计，将设计集成到开发工作流程中。 Onlook 正在获得显著的关注，拥有超过 25,000 名支持者和 100 多名贡献者，通过将设计直接集成到代码库中，解决了设计师的一个真实痛点，并通过 SaaS 或 API 模型提供了明确的盈利潜力。 Onlook 遵循开源许可证，目前处于生产阶段，部署复杂度适中，除了标准的桌面环境外，没有特定的硬件要求。"
tags: "Design, Agent, Code, Tools, UI/UX"
---

# Onlook：基于代理的设计工具


> Onlook 是一个开源工具，允许设计师使用他们现有的代理直接在代码库中创建设计，将设计集成到开发工作流程中。 Onlook 正在获得显著的关注，拥有超过 25,000 名支持者和 100 多名贡献者，通过将设计直接集成到代码库中，解决了设计师的一个真实痛点，并通过 SaaS 或 API 模型提供了明确的盈利潜力。 Onlook 遵循开源许可证，目前处于生产阶段，部署复杂度适中，除了标准的桌面环境


**项目链接**：https://github.com/onlook-dev/onlook/
**作者**：D_R_Farrell
**发布时间**：2026-11-19T16:34:04Z
**挖掘日期**：2026-11-20
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：Design, Agent, Code, Tools, UI/UX


## 📌 项目详解

Onlook 是一个开源工具，允许设计师使用他们现有的代理直接在代码库中创建设计，将设计集成到开发工作流程中。 Onlook 正在获得显著的关注，拥有超过 25,000 名支持者和 100 多名贡献者，通过将设计直接集成到代码库中，解决了设计师的一个真实痛点，并通过 SaaS 或 API 模型提供了明确的盈利潜力。 Onlook 遵循开源许可证，目前处于生产阶段，部署复杂度适中，除了标准的桌面环境外，没有特定的硬件要求。


## 🌐 背景与生态

Onlook 坐落在日益发展的代理设计工具生态系统中，这些工具超越了基本的 AI 生成器，通过规划多步骤序列并在多个模型上执行它们。该项目解决了需要像设计师一样工作的设计工具的需求，将熟悉的画布界面与真实的代码库集成结合起来。


## 💬 社区讨论

社区评论表达了对该工具潜力的兴奋，但也提出了关于其可用性和与现有设计工具比较的问题。一些用户正在探索如何将 Onlook 集成到他们现有的工作流程中。


## 🚀 应用前景

Onlook 可应用于设计师越来越多地需要在代码中工作的行业，如 UI/UX 设计、网页开发和应用程序开发。它通过简化设计流程，为 SaaS 或 API 盈利提供了潜力。


## 🔧 技术栈

Onlook 使用 Python 进行后端开发，通过 API 与现有代码库集成，并利用基于浏览器的界面进行设计。它需要与 Claude 或 ChatGPT 等代理 AI 集成。


## 🎯 上手难度

使用 Onlook 的难度评级为进阶。前提条件包括 Python 环境、AI 代理的 API 密钥，以及对您打算在其中进行设计的代码库的熟悉。


## 👥 目标用户

Onlook 面向在基于代码的环境中工作的设计师、开发人员和研究人员。它特别适用于需要将设计直接集成到其开发工作流程中的人。


## ⚖️ 类似项目对比

竞争对手包括 Figma、Sketch 和 Adobe XD 等工具，这些工具更为成熟，但缺乏 Onlook 的代理设计功能。其他代理设计工具包括 Wireflow 和 IBM 的代理编码工具。


## 📚 参考链接

- [Best Agentic Design Tools in 2026 | Wireflow](https://www.wireflow.ai/blog/best-agentic-design-tools-in-2026)
- [What Is Agentic AI? Definition, 6 Levels & Examples (2026)](https://agentic.ai/what-is-agentic-ai)
- [What is agentic coding? - IBM](https://www.ibm.com/think/topics/agentic-coding)

<details><summary>📄 查看原文内容</summary>


Hey HN, I&#x27;m Daniel, founder of Onlook (<a href="https:&#x2F;&#x2F;github.com&#x2F;onlook-dev&#x2F;onlook" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;onlook-dev&#x2F;onlook</a> and onlook.com).<p>Onlook is a desktop app that puts a canvas on top of your real codebase, letting you design directly in code with the agent you already use. Over 25,000 designers and developers have supported the project, 100+ have contributed, and it&#x27;s been the #1 trending repo in the world twice. We just rebuilt the entire product as an agentic design tool, and open-sourced it to the community.<p>Here’s a demo video: (<a href="https:&#x2F;&#x2F;youtu.be&#x2F;BogcYWf4siM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;BogcYWf4siM</a>)<p>If you&#x27;re an engineer, traditional engineering tools are largely built for convergence, whereas designers tend to explore and diverge on ideas. Onlook gives designers a familiar canvas while managing all of the dev processes that get between them and making mind-blowing designs in code. Designers can work on a multiple simultaneous worktrees that run on the real app locally, and every change lands as a PR you can review or throw away, so there aren’t mockups to rebuild.<p>We built Onlook because we believe there needs to be a developer tool that works the way designers do.<p>More and more, designers are expected to work in code. Designers think by seeing, drafting, arranging variations, using references, and remixing ideas. That’s why the canvas has been the signature feature of design tools because it genuinely is useful for how messy the creative process is. Most of the challenge of using engineering tools for design work is that the first half of starting a project often takes mental bandwidth in of itself (What branch am I on? What page was that last exploration on?) and the second half is constrained by configuring your coded design to present itself (prompting design tools on top of what you’ve built or making temporary navigation for that specific state).<p>Some of you may remember our earlier Show HNs (July 2024: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=40904862">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=40904862</a>, August 2024: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41390449">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41390449</a>, May 2025: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44127653">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44127653</a>). Since then, we built a web version (too early), then a Storybook-native build (a mistake). We noticed that our desktop product from July 2024 was still getting hundreds of downloads a month despite zero promotion, so we decided to rebuild it for the new era of designers working in code.<p>How it works…<p>Onlook shines at exploring tons of ideas at once. Ask it to lay out every flow in your product, show every state of a component, or riff on ten versions of one screen. Your designs all show up side by side on an infinite canvas, with each frame as a real webview running your actual app with real data. Not as a mockup, but the real deal.<p>When we built this editor, we had an epiphany that it could be a new kind of IDE for design. Design tools used to be limited to a proprietary setup or closed schema, but now you can push and pull the medium of code to get whatever result you want, so why not give agents an infinite canvas of browsers and see what they do? It turns out, the agents can figure out how to better present coded work by adjusting the urls of browser frames and arranging and resizing them on the canvas.<p>The concept is simple, but it requires a lot of product thinking. For example, because all of the frames on the canvas share a single browser session, and Chromium only allows six connections per host per session, ten frames of the same app end up fighting over limited connections. So, we had to plan around that, and there are still tons of things we need to do to make the canvas ultra performant.<p>Onlook is an Electron app where you can import a repo from GitHub or upload a local folder. Then, Onlook creates a git worktree, starts your dev server, and has the agent sort out missing dependencies or other requirements. You never open a terminal and everything the agent does is a normal git diff that can go to GitHub as a PR. We inject a small script into each frame that draws selection outlines and reads the page, so that way you can click an element, say &quot;make this a card layout,&quot; and the agent knows exactly what &quot;this&quot; is.<p>This time we didn&#x27;t build our own agent. Onlook runs Claude Code or Codex on your own subscription, and we turn whatever the agent emits into one typed event log and draw the UI from that in our own chat interface. On top of that we give the agent a bespoke set of design-specific tools, from arranging frames on the canvas, to making suggestions, to generating multiple iterations of a selection – which is especially useful because the agent decides how to get the app into a state that you need based on your prompt.<p>We also have our own Artifacts which are quick HTML sketches that live in the editor, but outside your repo. They’re almost like components in other design tools in that they can be carried and edited across every project but are detached from the project with no network access. As an example, you can ask the agent to turn your interface into an Artifact, and use it as a reference for another exploration, or download it as HTML and send it to a coworker as an interactive export of something you have in progress. I frequently go back to the artifacts I’ve made as visual snippets when I need new ideas or need to borrow something that’s already been built.<p>The desktop editor is free (you can download it from our website at onlook.com) and open source under Apache-2.0, and we&#x27;ll eventually offer a paid cloud product for teams.<p>We&#x27;d love to hear which repos work and which don&#x27;t, what you try to do on the canvas, and what&#x27;s missing. We’re so excited for this to be a new way for designers to work in code!<p>The Onlook team (Joel - thebrubaker and Kris - krisodd), and I will be here all day!


--- Top Comments ---

[Kuyawa]: First congrats, now the hard question... Why would I use any tool (not just onlook) besides my coding harness if all I do is ask and receive, I don&#x27;t design anymore, I don&#x27;t code, I don&#x27;t review. I am just an architect (used to be a programmer for 40 years) and all I do is brainstorming sessions with my agent and once we have all specs, features, scope and roadmap all I say is &quot;go&quot; and in ten minutes I have a beautiful and fully functioning app, it may need a few cosm...

[modestnature]: The &quot;ten versions of one screen&quot; part is where I&#x27;ve had the most trouble with agents. When I asked for variations of one section, they&#x27;d also quietly change the header, the copy, section heights and the CTA, so the comparison stopped being about the thing I asked for. What fixed it for me was a standing rule: start every variant from the production screen and keep everything the request doesn&#x27;t mention exactly as it is. Is there a way in Onlook to pin parts of a frame...

[chrisvalleybay]: How are you using a Claude Code subscription? Leveraging a Claude Code subscriptions API-key without going through the Claude Code harness can lead to a user being banned for violating terms. Are you doing anything like that, or are you directly interacting with the Claude Code harness? Edit: Aaand congrats on the launch! Also, please allow us to delete our accounts. Offering sign-up without account deletion is not nice.

[husseinhb]: That&#x27;s great tool but the issue the design of the AI even if it like that easy to change it fix it what ever they still creating the same template of designs i think they needs a lot of samples that are real from real designers to use them as a source. 
For example when i was creating my platform about 2 years ago designing it was the most complex part because the AI was making a lot of mistakes in layers and z-index and content appearance and much more. But now a days those issues becom...

[dalisraieb]: congrats on the launch. curious how you handle states that need login or specific data, like an admin page or an empty cart. do you seed each worktree with test data, or does the agent click through the app to get there?

</details>
