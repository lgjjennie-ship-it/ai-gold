---
layout: default
title: "基于Godot和Rust的终端复用器"
date: 2026-09-12T12:00:00+00:00
discovered_date: 2026-09-12
slug: 2026-09-12-show-hn-godot-and-rust-based-multiplexer-terminal-panes-and-more
source: hackernews
category: show-hn
ai_score: 8.0
summary: "gPTY是一个基于Godot和Rust构建的终端复用器，允许用户管理多个PTY，并以网格/平铺方式排列，具有集成AI代理编排的潜力。 该项目在Hacker News上获得了86分的参与度和44条评论，表明社区兴趣。它结合了Godot和Rust来创建一个独特的终端复用器，具有编排AI代理的潜力，展示了新颖性和实用价值。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要Rust和Godot，并具有集成AI代理的接口。"
tags: "Terminal, Godot, Rust, AI, Multiplexer"
---

# 基于Godot和Rust的终端复用器


> gPTY是一个基于Godot和Rust构建的终端复用器，允许用户管理多个PTY，并以网格/平铺方式排列，具有集成AI代理编排的潜力。 该项目在Hacker News上获得了86分的参与度和44条评论，表明社区兴趣。它结合了Godot和Rust来创建一个独特的终端复用器，具有编排AI代理的潜力，展示了新颖性和实用价值。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要Rust和


**项目链接**：https://github.com/godot-pty/gpty
**作者**：1nv1n
**发布时间**：2026-09-11T16:03:05Z
**挖掘日期**：2026-09-12
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Terminal, Godot, Rust, AI, Multiplexer


## 📌 项目详解

gPTY是一个基于Godot和Rust构建的终端复用器，允许用户管理多个PTY，并以网格/平铺方式排列，具有集成AI代理编排的潜力。 该项目在Hacker News上获得了86分的参与度和44条评论，表明社区兴趣。它结合了Godot和Rust来创建一个独特的终端复用器，具有编排AI代理的潜力，展示了新颖性和实用价值。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要Rust和Godot，并具有集成AI代理的接口。


## 🌐 背景与生态

Godot是一个开源的游戏引擎，不仅可以用于游戏，还可以用于终端管理。Rust以其性能和安全性而闻名。将这两种技术结合用于终端复用器是相对较新的尝试。


## 💬 社区讨论

社区评论积极，对Godot在终端管理中的应用表示兴奋，并请求更多功能。


## 🚀 应用前景

gPTY可用于开发者环境，管理多个终端和AI代理，可能通过SaaS或API模式实现商业化。


## 🔧 技术栈

技术栈包括用于UI的Godot，用于后端的Rust，以及潜在的Transformers等库的AI集成。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+，推荐GPU。步骤：克隆仓库，安装依赖，运行示例。


## 👥 目标用户

目标用户是需要高级终端管理和AI集成功能的开发者和研究人员。


## ⚖️ 类似项目对比

竞品包括tmux、Alacritty和TTY复用器。gPTY的独特之处在于基于Godot的UI和Rust后端。


## 📚 参考链接

- [Godot (game engine) - Wikipedia](https://en.wikipedia.org/wiki/Godot_(game_engine))
- [Rust (programming language) - Wikipedia](https://en.wikipedia.org/wiki/Rust_(programming_language))

<details><summary>📄 查看原文内容</summary>


I wanted to share my side-project: gPTY. Started off as an idea to combine Godot and Rust in a project (two stacks I wanted to use more to learn more). The base inspiration was tmux - simply allow spawning multiple PTYs and then let the user grid&#x2F;tile them how they see fit.<p>But since we have the Godot game engine at our disposal, we can do some more interesting things, like add an FPS counter, and then subsequently also let people set their preferred FPS (the idea being the potential lower power draw if someone&#x27;s running it on a laptop on battery power vs someone running it on a desktop with high&#x2F;native FPS). In its current state, with me using Oh-my-Pi a lot, it&#x27;s evolving into a terminal workspace that can be used for orchestrating autonomous AI agents by way of dogfooding (or you know, just run herdr inside of gPTY - it&#x27;s the better orchestrator and just good software - I found it after starting this project, and now I&#x27;m finding myself using it a lot).<p>Also, we&#x27;re not limited to just terminals. Since we have Godot, we have basically a 2D (and potentially a 3D) canvas to play with. We can already full-screen the app for &quot;zen&quot; mode, no taskbar, no distractions. TUI die-hards can have their media or other apps entirely in terminal panes.<p>There has been some ground-work on getting Markdowns displayed properly done and I want to work on some kind of Wiki framework for local knowledge-management next, then create more types of panes (think native audio&#x2F;video on a media pane, that sits alongside your terminal pane), and some simple 2D games (like snake) to prototype. More details are on the ROADMAP.<p>What&#x27;s not easy (and probably won&#x27;t happen) is a browser. Having done a couple of (small) projects using Electron already, the temptation to ditch Godot&#x2F;Rust (learning curve) did come up (and also the ecosystem, the ease with which I could pull components and use web technologies - development velocity would definitely be higher there). But on the flipside, given all of the available LLM and AI support that we are privileged to have today, I figured the velocity should be comparable depending on how much I leaned on those. And lean I did.<p>Godot&#x2F;Rust seemed the better call to me and my intent anyway - going with the &#x27;it&#x27;s not just the end but the journey that matters&#x27; philosophy. So yes, there has been heavy use of LLMs &amp; AI to generate a lot of the code. But I do review and steer actively, not relying solely on vibes, and there&#x27;s a few bits here &amp; there that have been human authored.<p>There are definitely a lot of polish and QoL items that need to land to make the end user experience better, but in the meantime, let me know your thoughts and&#x2F;or concerns!<p>Repository: <a href="https:&#x2F;&#x2F;github.com&#x2F;godot-pty&#x2F;gpty" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;godot-pty&#x2F;gpty</a><p>Docs&#x2F;Blog: <a href="https:&#x2F;&#x2F;godot-pty.github.io&#x2F;gpty&#x2F;" rel="nofollow">https:&#x2F;&#x2F;godot-pty.github.io&#x2F;gpty&#x2F;</a>


--- Top Comments ---

[rcr-anti]: If you squint, Godot has a cross platform hardware accelerated GUI. The editor is itself, in a sense, a Godot app and has builds for VR Headsets, Android, web apps, all the usual platforms. The extension api works pretty good too for Rust, and Rust itself has a fantastic cross platform and WASM story. It might be cursed, but it can get complicated stuff out the door and in anyone&#x27;s hands fast. edit: they also recently created libgodot, which flips the model. Your application owns and con...

[nitinreddy88]: A project without screenshots - I dont know how they expect us to understand unless we read everything

[da-x]: Terminals and web browsers are our main UI drivers right, so yeah, it makes sense to have a super app that provides them both in the best way. Embdding a terminal inside a web app is annoying because of Ctrl-W and other issues, and embedding a web broswer inside a terminal is even more weird. So we wind up having Wayland compositors do the work to combine them in one environment. I tried to do this with a simple wgpu + winit app, servo, and alactitty_terminal, and it kinda worked, but both te...

[icarito]: Love to see Godot used creatively beyond games! The terminal is for sure an area that can see innovation, why not!

[sebastianconcpt]: Can you add a &quot;why?&quot; &#x2F; &quot;why now?&quot; section?
Don&#x27;t be another project that is a bunch of how that is leaving out to explain why it exists or exemplify what classes of problems it unlocks solutions for (applicability).

</details>
