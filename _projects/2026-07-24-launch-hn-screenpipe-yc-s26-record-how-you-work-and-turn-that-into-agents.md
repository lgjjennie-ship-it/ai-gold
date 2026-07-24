---
layout: default
title: "Screenpipe：具有本地屏幕和音频记录的AI代理"
date: 2026-07-24T12:00:00+00:00
discovered_date: 2026-07-24
slug: 2026-07-24-launch-hn-screenpipe-yc-s26-record-how-you-work-and-turn-that-into-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Screenpipe在本地记录屏幕和音频，为AI代理创建可搜索的记忆，以帮助任务自动化和SOP创建。 Screenpipe在Hacker News上获得了71个点数和53条评论，显示出强烈的兴趣。它为AI代理提供了本地屏幕和音频记录的新颖方法，解决了自动化任务和创建SOP的实际问题。 Screenpipe处于开发阶段，采用开源许可证，目前处于alpha阶段，连续记录需要大量CPU资源。"
tags: "AI, Agent, Automation, SOP, Privacy"
---

# Screenpipe：具有本地屏幕和音频记录的AI代理


> Screenpipe在本地记录屏幕和音频，为AI代理创建可搜索的记忆，以帮助任务自动化和SOP创建。 Screenpipe在Hacker News上获得了71个点数和53条评论，显示出强烈的兴趣。它为AI代理提供了本地屏幕和音频记录的新颖方法，解决了自动化任务和创建SOP的实际问题。 Screenpipe处于开发阶段，采用开源许可证，目前处于alpha阶段，连续记录需要大量CPU资源。


**项目链接**：https://news.ycombinator.com/item?id=49024620
**作者**：louis030195
**发布时间**：2026-07-23T16:48:38Z
**挖掘日期**：2026-07-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agent, Automation, SOP, Privacy


## 📌 项目详解

Screenpipe在本地记录屏幕和音频，为AI代理创建可搜索的记忆，以帮助任务自动化和SOP创建。 Screenpipe在Hacker News上获得了71个点数和53条评论，显示出强烈的兴趣。它为AI代理提供了本地屏幕和音频记录的新颖方法，解决了自动化任务和创建SOP的实际问题。 Screenpipe处于开发阶段，采用开源许可证，目前处于alpha阶段，连续记录需要大量CPU资源。


## 🌐 背景与生态

该项目解决了AI代理需要了解用户计算机上活动需求的问题。它基于现有的RAG（检索增强生成）技术，旨在改进微调和工具调用的局限性。


## 💬 社区讨论

社区评论关注隐私问题、CPU使用率和过度授权代理访问记录数据的可能性。


## 🚀 应用前景

Screenpipe可用于各种行业，以自动化重复任务、创建SOP并增强AI代理功能。通过SaaS或API模型存在盈利潜力。


## 🔧 技术栈

Screenpipe使用Python、OCR和本地音频转录，如Parakeet/Whisper等模型。它集成了API，并需要Docker进行部署。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、GPU和API密钥。步骤涉及设置环境和运行CLI。


## 👥 目标用户

目标用户包括IT、医疗保健和金融等行业的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Daydream、GBrain和Embedbase。Screenpipe的区别在于专注于连续本地记录和API集成。


## 📚 参考链接

- [What Are AI Agents ? | IBM](https://www.ibm.com/think/topics/ai-agents)
- [What are AI Agents ? - YouTube](https://www.youtube.com/watch?v=F8NKVhkZZWI)

<details><summary>📄 查看原文内容</summary>


Hi Hacker News, I&#x27;m Louis. I built Screenpipe (<a href="https:&#x2F;&#x2F;screenpipe.com">https:&#x2F;&#x2F;screenpipe.com</a>), an app that records your screen and audio locally (only!), and gives AI agents a searchable memory of what you&#x27;ve seen, said, and heard. This makes it easier to automate your repetitive tasks, turn them into SOPs (Standard Operating Procedure) and so on.<p>I made a HN-style demo video at <a href="https:&#x2F;&#x2F;www.tella.tv&#x2F;video&#x2F;build-your-ai-second-brain-with-screenpipe-e1j7" rel="nofollow">https:&#x2F;&#x2F;www.tella.tv&#x2F;video&#x2F;build-your-ai-second-brain-with-s...</a> and there’s a marketing video at <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=c1jV6E9pyug" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=c1jV6E9pyug</a>.<p>I’ve been obsessed with this for a long time. I’ve been maintaining a “second brain” since 2020, in which I would store journals, handwritten notes, music I listen to, projects I&#x27;m working on, conversations I have with people, personal CRM etc. I experimented a lot of RAG in the early days with ParlAI, hundreds of fine-tuned GPT2 models, and GPT3 (<a href="https:&#x2F;&#x2F;forum.obsidian.md&#x2F;t&#x2F;fine-tuning-openai-api-gpt3-on-your-second-brain-obsidian&#x2F;21849&#x2F;4" rel="nofollow">https:&#x2F;&#x2F;forum.obsidian.md&#x2F;t&#x2F;fine-tuning-openai-api-gpt3-on-y...</a>). Later I built Ava, the first Obsidian AI plugin, which grew to a few thousands of users quickly. It then became Embedbase, an API to make it easier to build AI apps powered by RAG.<p>What I learned from all this is how important it is for the models to have context about what you’re doing on your computer, in order to get them to do what you want.<p>In the early days there was fine tuning but it was too much pain, then there was tool calling so that AI can access software you use but still kinda not autonomous enough. needing micro management. Then MCP came, but it felt too static, and non technical users struggled to build and use MCP. Then we got skills. Most recently we’ve seen Karpathy’s LLM-maintained wiki, Garry&#x27;s GBrain, etc., where an agent incrementally maintains a persistent collection of Markdown pages. New sources update entity pages, strengthen or contradict existing claims, and improve a synthesis that compounds over time. I like this pattern, but it still begins with someone selecting and importing the sources. There is still no way AI can know what you and your company are doing every day, across apps, not just inside of apps.<p>Of course, not everyone wants this. But I do! I want AI to know what I&#x27;m doing and never lose memory ever again, and I want it to use the same software that humans do, without painful context switches.<p>I started building Screenpipe for myself in 2024 - a CLI to record your screen and plug this context into AI. An HN user posted it in 2024 (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41695840">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41695840</a>) and that discussion influenced the product. The most useful criticism concerned recording consent, local security, CPU usage, signal-to-noise, and whether agents could act on top of the data.<p>The naive implementation started from continuously recording video and running OCR over every frame. But that creates duplicate data, consumes substantial resources (it basically turns your computer into a space heater!), and discards structure the operating system already knows. Screenpipe now instead listens for events such as app switches, clicks, typing pauses, scrolling, and idle fallbacks. When something meaningful changes, it pairs a screenshot with the operating system’s accessibility tree at the same timestamp. OCR is used when structured accessibility data is unavailable. We also capture audio continuously, identify speakers and transcribe locally through Parakeet&#x2F;Whisper or using cloud models.<p>Everything is indexed in a local SQLite database, mp4 files, and sometimes md files. An AI friendly API on port 3030 is open for agents, with authentication and a MCP and skills.<p>Once Screenpipe has been up and running for a while, you can use it through our built-in chat, Claude, ChatGPT, Hermes, Openclaw, or any agent, to do things like:<p>- adding context to your current chat, e.g. &quot;gather all context about task X&quot;, then requiring less prompts to achieve your goal<p>- retrieve information, e.g. &quot;retrieve the tasks i was working on from 8 am to 4 pm, make a list of what got done and what&#x27;s left&quot;<p>- create and maintain a personal wiki &#x2F; second brain for your agents: &quot;every 1h organize everything i do in projects, people, tasks, meetings in my Obsidian vault as markdown files and folders&quot;<p>- create automations: whenever i visit someone&#x27;s profile on linkedin, update my crm<p>- find automation opportunities: look at everything my team has done this week and turn it into a list of automation opportunities<p>Screenpipe data is stored locally, though we also offer an enterprise plan to discover automation opportunities and for that the company decides where the data lives. We built our own AI PII model to redact sensitive information, it runs locally on Apple MLX or Windows DirectML, we also support cloud confidential inference for low end devices, although our local models are meant to use &lt;1% CPU and &lt;400 mb RAM. Users can set apps, windows, and urls to filter, in addition to browser incognito mode.<p>We also support recording schedules and other privacy features.<p>Most of our codebase is written in Rust, MLX, Onnx, we like cidre or direct C call for Apple APIs and windows-rs for Windows API. We also experimentally support Linux.<p>We have a desktop app (<a href="https:&#x2F;&#x2F;screenpipe.com&#x2F;how-to-install">https:&#x2F;&#x2F;screenpipe.com&#x2F;how-to-install</a>) and a CLI:<p><pre><code>  npx screenpipe record
</code></pre>
You can run that without creating an account. All the code is source-available at <a href="https:&#x2F;&#x2F;github.com&#x2F;screenpipe&#x2F;screenpipe" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;screenpipe&#x2F;screenpipe</a>. We took the dreaded step of making our own Screenpipe Commercial License. I know HN strongly prefers OSI open source (MIT&#x2F;Apache&#x2F;etc.) but couldn’t find a sustainable way to keep developing Screenpipe while companies were using it commercially for free. So now personal non-commercial, nonprofit, educational, and research use is free, but commercial use requires a license.<p>Versions released before the license change remain available under MIT. We have a free tier, and other plans, including Enterprise which helps companies find automation opportunities.<p>Would love to hear any feedback, things you&#x27;ve done with screenpipe, or features you&#x27;d want


--- Top Comments ---

[rahulladumor]: Once Screenpipe has months of screen and audio indexed locally, what stops a compromised or over-permissioned agent from querying the whole history through the port 3030 API instead of just the current task&#x27;s context? Continuous recording solves the memory problem, but it turns &quot;give the agent access to my second brain&quot; into a much bigger blast radius than giving it access to one document. Is there per-query scoping or a time-window restriction on what an agent can pull back, o...

[AlfeG]: Were not able to login - because You used github auth without browser interaction. Passkeys are in bitwarden in Chrome...

[AmazingTurtle]: Funny timing. I&#x27;ve been building something similar in my spare time called Daydream. There’s a lot of overlap: local screen&#x2F;audio capture, OCR and transcription, window and activity context, SQLite, and a searchable memory of what happened. The main difference is the product direction. Screenpipe seems focused on continuously giving agents context through APIs, MCP, and skills. Daydream is more narrowly built around answering &quot;what did I do today?&quot; through a timeline you c...

[subhajeet2107]: How are you planing to segregate between professional use and personal use, I dont want any agent or any llm to know all the time what i have been doing on my system, it would be privacy nightmare and most of the time the screencapture is not meaningful. People may use their work laptop or devices to checkout reddit or hackernews occasionally.

[kerv]: I tried this a couple months back. While I found it useful, I also found on my MacBook M1, the fact it was recording all the time, made my CPU melt at high temps all the time. I eventually had to shut it off and stop using because of that. Curious how it runs on more modern hardware? Is it pretty lightweight these days?

</details>
