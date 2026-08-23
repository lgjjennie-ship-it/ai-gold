---
layout: default
title: "OzBrain：AI智能体的共享知识库"
date: 2026-08-23T12:00:00+00:00
discovered_date: 2026-08-23
slug: 2026-08-23-show-hn-ozbrain-a-shared-brain-for-knowledge-between-agents-and-your-team
source: hackernews
category: show-hn
ai_score: 8.0
summary: "OzBrain是一个平台，用于在AI智能体和团队之间集中和共享知识，使用结构化知识库和智能体友好的功能。 OzBrain解决了AI智能体生态系统中日益增长的对中央知识库的需求，显示出强大的吸引力并有可能作为SaaS解决方案进行商业化。 OzBrain处于alpha阶段，使用Supabase进行存储，并设计得易于使用，无需技术知识。它可以处理冲突并将知识重构为对token友好的块。"
tags: "AI, Agents, Knowledge, Collaboration, SaaS"
---

# OzBrain：AI智能体的共享知识库


> OzBrain是一个平台，用于在AI智能体和团队之间集中和共享知识，使用结构化知识库和智能体友好的功能。 OzBrain解决了AI智能体生态系统中日益增长的对中央知识库的需求，显示出强大的吸引力并有可能作为SaaS解决方案进行商业化。 OzBrain处于alpha阶段，使用Supabase进行存储，并设计得易于使用，无需技术知识。它可以处理冲突并将知识重构为对token友好的块。


**项目链接**：https://ozbrain.com/
**作者**：dariusmonsef
**发布时间**：2026-08-21T23:09:06Z
**挖掘日期**：2026-08-23
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agents, Knowledge, Collaboration, SaaS


## 📌 项目详解

OzBrain是一个平台，用于在AI智能体和团队之间集中和共享知识，使用结构化知识库和智能体友好的功能。 OzBrain解决了AI智能体生态系统中日益增长的对中央知识库的需求，显示出强大的吸引力并有可能作为SaaS解决方案进行商业化。 OzBrain处于alpha阶段，使用Supabase进行存储，并设计得易于使用，无需技术知识。它可以处理冲突并将知识重构为对token友好的块。


## 🌐 背景与生态

以智能体为中心的聊天界面正在获得关注，许多专业人士在管理共享知识方面遇到困难，导致定制解决方案的出现。


## 💬 社区讨论

开发者正在讨论大量文本编译时准确性的下降、对更好摘要的需求以及共享知识系统的复杂性与益处之间的权衡。


## 🚀 应用前景

OzBrain可以通过提供一个结构化的知识库来解决AI开发中的实际问题，对科技行业的团队和个人开发者非常有用。


## 🔧 技术栈

OzBrain使用Supabase进行存储，与Claude、ChatGPT、Cursor和编码智能体集成，并设计得可扩展且安全。


## 🎯 上手难度

入门评级为入门级，需要基本的技术知识，并需在Supabase上设置一个可工作实例的步骤。


## 👥 目标用户

目标用户包括科技和AI行业的个人开发者、企业团队和研究人员。


## ⚖️ 类似项目对比

竞品包括GitHub - dmonsef/ozbrain-cursor-plugin和其他为AI智能体构建的定制知识系统。


## 📚 参考链接

- [OzBrain: shared brain every AI agent reads and writes](https://ozbrain.com/)
- [OzBrain - Shared knowledge brain for AI agents and teams](https://zeli.app/story/49394827)

<details><summary>📄 查看原文内容</summary>


I think agent-first chat interfaces will be a primary software modality and busy dashboard&#x2F;UI will go away. I’m not sure who exactly wins it, but I want my knowledge to grow&#x2F;go with me.<p>A lot of the “knowledge” ie research, analysis, reasoning will be done by agents as the primary user. Our current notes tools &amp; tasks management systems were built for humans… I don’t care what the 17th thing on my bug backlog is. I want to conduct agents that can execute for me and do great work.<p>What I built OzBrain to do:
+ Create a central place for agent reasoned knowledge to live
+ Be agnostic about what apps&#x2F;agents connect to it
+ Capture everything and track it so I can audit it
+ Enable teams, collaborators or partners to share brains
+ Handle conflicts so many agents in the same article doesn’t blow up
+ Refactor knowledge into more token friendly chunks and map the index well
+ Close the knowledge loop so new thinking supersedes old thinking across the corpus. Don’t erase, depreciate and link
+ Keep user data safe and secure
++ Be easy enough to use that you don’t have to have any technical knowledge<p>Some among us will always build their own custom solutions, but there are millions of tech professionals and small business owners that will use agents heavily and need a solution. So I’m trying to build that.<p>Isn’t this like gBrain? Yes, similar. I think it’s like AWS vs Vercel. AWS is very powerful, configurable, and useful if you’re technical and want to invest the time into really fine tuning your system… but if you just want your web deploy&#x2F;hosting to just work and be easy to deal with you use Vercel.<p>&#x2F;&#x2F; WHY I MADE IT<p>I’ve been enjoying getting back to my technical roots, as I lost my coding skills more than a decade ago, but with AI I can focus on the system and the product in partnership with agent coding workflows.<p>I recently built a Voice AI for older people. To build it I created an agentic engineering workflow (feel free to rip that up as I’m always looking to improve systems: <a href="https:&#x2F;&#x2F;ozbrain.com&#x2F;resources&#x2F;eng-flow" rel="nofollow">https:&#x2F;&#x2F;ozbrain.com&#x2F;resources&#x2F;eng-flow</a>) My approach with coding agents is trust but verify, and I’m trying to replace the parts where a human would review with an adversarial or specialized agent who would give a better answer&#x2F;review.<p>I have workflows that will go high level task to shipped PR running in Claude cloud sessions. I use Claude Code locally and Cursor when I want a tighter loop on doing visual work like UI or layout. And Codex to either load balance usage for TokenThriffting or when I want a different llm to think thru something.<p>It was a pain in the ass passing .md files around and keep track of which version was the most recent, so I built a hosted .md storage right in Supabase and any of my agents already have Supabase access. This let me build a solid, scalable, secure voice AI from my phone at the gym. All my agents have access to our knowledge, can write to it, update and refer to it as we build and improve the product and the systems we use.<p>Out of 75 founder friends I asked about how they manage shared knowledge, 26 built their own custom knowledge systems… Obsidian vaults with 7k files synced through a VPS, markdown repos behind their own MCP servers, cron jobs stitching Supabase to a skills file… each a different Frankenstein they have to maintain. 32 said they felt the pain of moving static files around but didn’t have any solution for it.<p>So I rebuilt my brain better and used it to build it.<p>&#x2F;&#x2F; HOW YOU CAN HELP<p>Would love to have you try it out. The maintenance loop is still in alpha so not running it on customer data yet.<p>If you built your own brain I’d love to hear how you did it. What criteria was most important for you in its design &amp; function.<p>If you are tired of shuffling .md files around I’d love to have you try out OzBrain and to give feedback, just ask your agent to put it in the shared bugs &amp; features brain!<p>Cheers!
Bubs.co


--- Top Comments ---

[gavinboston]: Do you have a solution for degradation in accuracy when compiling larger amounts of llm-produced text? I am also building LLM knowledge&#x2F;memory systems and I&#x27;ve been surprised how bad LLMs are, even SOTA models, at summarizing non-trivial input batches of text. They get things wrong, distort the underlying meaning or data, etc.

[Sammi]: I have a folder called reports, plans, and code-reviews in each repo. I put my md files for agents there, and voila they&#x27;re in the cloud along with my source code in git. I just talk to my local agent about these files and it finds things using grep and whatever. Done. No mcp or special server needed. I&#x27;ve been pitched products like ozbrain before, but I&#x27;ve failed to see the need over what I already have. Seems like more complication for no gain to me. Am I missing something?

[fallinditch]: I use the LLM-wiki pattern for a structured directory of topic folders of .md files, and made it also compatible with the Open Knowledge Format [1]. My agent (Hermes) responds to a made-up command &quot; vaultize  this doc&#x2F;link&#x2F;text, etc&quot; to add new .md files in the right format in the right place. The agent does a pretty good job of maintaining the index.md file, cross-links, etc. A Quartz website builder creates a static site on my server, each MD file is a web page, and rebu...

[pioneerjeff]: Great entry point! I&#x27;ve also run into this issue and am trying to solve it. But when I try this in different ways, a common issue is that the LLM often drifts. Sometimes it just drops important issues or records more trivial info than I need. Wondering how you solve this issue in OzBrain.

[sinuhe69]: I think the central question for a such memory system is whether we or the agents can find the relevant information and how to organize these data as changes continues to come in. Would we miss something in the retrieval  process? How do we organize the information so they stay actual and correct without piling up the garbage? Of course we can continue to concatenate the data and tag them with version and date, but then we have to face the problem of extracting the relevant information in a s...

</details>
