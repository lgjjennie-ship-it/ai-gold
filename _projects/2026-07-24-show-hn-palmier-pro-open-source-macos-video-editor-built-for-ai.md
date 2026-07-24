---
layout: default
title: "Palmier Pro：AI驱动的macOS视频编辑器"
date: 2026-07-24T12:00:00+00:00
discovered_date: 2026-07-24
slug: 2026-07-24-show-hn-palmier-pro-open-source-macos-video-editor-built-for-ai
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Palmier Pro是一个开源的macOS视频编辑器，集成了AI生成功能和本地MCP服务器支持，用于代理集成，实现AI与视频编辑的无缝工作流程。 Palmier Pro因其在高 trafic 上的 Hacker News 和活跃的社区讨论而受到关注，解决了手动AI视频编辑工作流程的痛点，并提供了通过信用或SaaS模式清晰的盈利潜力。 Palmier Pro在开源许可证下，目前处于beta阶段，部署复杂度中等，硬件要求包括支持本地AI模型的Mac。"
tags: "AI, Video, Editor, macOS, Open Source"
---

# Palmier Pro：AI驱动的macOS视频编辑器


> Palmier Pro是一个开源的macOS视频编辑器，集成了AI生成功能和本地MCP服务器支持，用于代理集成，实现AI与视频编辑的无缝工作流程。 Palmier Pro因其在高 trafic 上的 Hacker News 和活跃的社区讨论而受到关注，解决了手动AI视频编辑工作流程的痛点，并提供了通过信用或SaaS模式清晰的盈利潜力。 Palmier Pro在开源许可证下，目前处于beta阶段，部


**项目链接**：https://github.com/palmier-io/palmier-pro
**作者**：harrisontin
**发布时间**：2026-07-23T15:11:37Z
**挖掘日期**：2026-07-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Video, Editor, macOS, Open Source


## 📌 项目详解

Palmier Pro是一个开源的macOS视频编辑器，集成了AI生成功能和本地MCP服务器支持，用于代理集成，实现AI与视频编辑的无缝工作流程。 Palmier Pro因其在高 trafic 上的 Hacker News 和活跃的社区讨论而受到关注，解决了手动AI视频编辑工作流程的痛点，并提供了通过信用或SaaS模式清晰的盈利潜力。 Palmier Pro在开源许可证下，目前处于beta阶段，部署复杂度中等，硬件要求包括支持本地AI模型的Mac。


## 🌐 背景与生态

视频编辑生态系统随着AI集成而发展，但大多数解决方案缺乏AI生成和编辑之间的无缝集成。Palmier Pro通过提供原生macOS解决方案填补了这一空白。


## 💬 社区讨论

社区评论强调了人们对该工具潜力的兴奋，要求基于信用的定价，并提到了类似的开源项目。


## 🚀 应用前景

Palmier Pro可以为内容创作者自动化视频编辑中的繁琐工作，在媒体制作、营销和教育领域提供应用。盈利模式可能来自SaaS或API访问。


## 🔧 技术栈

用Swift构建的Palmier Pro使用本地AI模型如CoreML和SigLIP2，基础设施支持MCP服务器用于代理集成。


## 🎯 上手难度

难度：进阶。前提条件包括macOS 26的Mac和本地AI模型，以及基本的视频编辑熟悉度。步骤涉及克隆存储库并运行本地服务器。


## 👥 目标用户

目标用户包括媒体和营销行业的后端工程师、ML从业者以及内容创作者。


## ⚖️ 类似项目对比

竞品包括Donkey，一个基于网络的开放式视频编辑器，带有原生Swift伴侣应用程序，以及像OpenAI的Codex这样的用于代理编码的工具。


## 📚 参考链接

- [Model Context Protocol servers - GitHub](https://github.com/modelcontextprotocol/servers)
- [Codex in ChatGPT | AI Coding Agents for Software Engineering | OpenAI](https://openai.com/codex/)

<details><summary>📄 查看原文内容</summary>


Hi HN, we are Marcos and Harrison, cofounders of Palmier (<a href="https:&#x2F;&#x2F;palmier.io">https:&#x2F;&#x2F;palmier.io</a>). We are building Palmier Pro, an open source macOS video editor, with built-in AI generation and a local MCP server that connects to your agent. Here are a few demos:<p>- Making some AI transitions: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=hbM_-eR1GX4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=hbM_-eR1GX4</a><p>- Multicam editing with Codex: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=SjS2q2LT1q8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=SjS2q2LT1q8</a><p>- Cutting long form clips into shorts: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=PR66eN2ouuQ" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=PR66eN2ouuQ</a><p>We built Palmier Pro as an internal tool when we were making AI launch videos for other startups. The main problem it solved in the beginning was the back-and-forth between AI generation platform and video editor. The iteration loop was awkward: AI videos → download → import to editor → edit → realize we need to change the AI video → repeat. So we built a minimal video editor where we could let Claude generate AI videos inside the editor.<p>As we gave more and more tools to the agent, we wanted to push to see what else agents can do in the video editing space. So today, your Claude&#x2F;Codex can:<p>- Manage projects inside Palmier Pro<p>- Import media from a public URL or filesystem to the project, and organize them in folders<p>- Search media (by embedding footages using SigLIP2 running locally)<p>- Edit the timeline (tracks&#x2F;clips&#x2F;keyframes operations)<p>- Generate images, videos, sound effects, captions, music<p>- Export videos<p>There are two ways for LLMs to interact with the editor: by connecting to the local MCP server, or using the in-app chat. Both use the same tools and APIs exposed by the video editor.<p>We have seen people using MCP server to connect to their own workflow to automate massive-scale video editing (e.g. given this same podcast style, replicate it with other footages that I have). We have also seen people using the in-app chat where it lives closer to the editor UI, with lower latency for faster iteration.<p>We don&#x27;t believe that AI is going to replace human creativity (nor should it), but where it can really help is in automating the gruntwork in video editing. Most work in the editing workflow is more mechanical than creative. Our vision is to build a video editor where AI can enable more individuals to create.<p>Throughout our experiments, AI is not very good at creative editing, but given a pattern (transcription-based, beat-based), it can do a decent job at rough cut.<p>We built Palmier Pro in Swift as an MVP because we wanted better performance and minimal dependencies (no nodejs&#x2F;webview), with some native macOS APIs like SpeechAnalyzer and CoreML for us to run some models locally. We use SpeechAnalyzer for local transcriber, SigLip2 to embed video frames, beat_this for beat detection, Silero VAD for silence detection, all running locally. The tradeoff is that we don&#x27;t support Linux or Windows at the moment.<p>Palmier Pro is open source and free to try out (macOS 26 only at the moment, though - we&#x27;ll support more platforms over time, but for now are focusing on iterating the core product).<p>No login required except for the AI generation features, which route requests to our backend. We are offering free credits on sign up so you can try out the AI generation as well.<p>We&#x27;d love to hear your feedback!


--- Top Comments ---

[Marciplan]: This looks great! Have you thought about dropping the &#x27;subscription&#x27;-part and &#x27;just&#x27; selling credits instead? Here&#x27;s my thinking as a SaaS founder: when I launch a product, I don&#x27;t need a video every month. So a monthly pricing makes me do this little calculation every time: &quot;do I need a video this month? nah. Then I&#x27;ll wait. I lose the early-bird price, but I still net out cheaper.&quot; And since there&#x27;s no yearly option, there&#x27;s nothing pul...

[nsbk]: This is what I have been waiting for in order to process my massive action camera library, I will definitely give it a try! I will start with older standard GoPro videos, and hope that by the time I make it to the Insta360 videos the editor supports 360 video (unless it does already!)

[dthedavid]: Nice project. I’m building a similar project. It’s open source too.  https:&#x2F;&#x2F;github.com&#x2F;DonkeyUseCorp&#x2F;Donkey  It’s mostly a web app with a native swift companion app to access local resources like TTS, file storage and video rendering. I arrived at the same conclusion as you; every app should have AI chat. Just give it full access to the app like a real user. I found that users prefer talking to the AI when editing vs clicking around.

[misterchocolat]: I&#x27;ve been following Marcos&#x27;s youtube channel and it&#x27;s so great to see that they&#x27;ve  finally found their thing. Looks like an awesome product that people actually want. Well done.

</details>
