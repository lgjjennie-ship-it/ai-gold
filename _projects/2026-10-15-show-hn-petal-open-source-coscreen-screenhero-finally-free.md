---
layout: default
title: "开源配对编程工具Petal"
date: 2026-10-15T12:00:00+00:00
discovered_date: 2026-10-15
slug: 2026-10-15-show-hn-petal-open-source-coscreen-screenhero-finally-free
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Petal是一个为远程协作设计的开源配对编程工具，其特点是将共享窗口作为真实的桌面窗口，具有可移动的光标和低延迟。 Petal因其强烈的Hacker News关注度而引人注目，并解决了远程工作时代配对编程工具有限的痛点，尽管目前尚未出现明确的盈利模式。 Petal在开源许可证下发布，目前处于alpha阶段，通过Docker部署，托管实例需要最小化配置。"
tags: "Code, Tools, Pair Programming, Remote Work, Collaboration"
---

# 开源配对编程工具Petal


> Petal是一个为远程协作设计的开源配对编程工具，其特点是将共享窗口作为真实的桌面窗口，具有可移动的光标和低延迟。 Petal因其强烈的Hacker News关注度而引人注目，并解决了远程工作时代配对编程工具有限的痛点，尽管目前尚未出现明确的盈利模式。 Petal在开源许可证下发布，目前处于alpha阶段，通过Docker部署，托管实例需要最小化配置。


**项目链接**：https://petal.live/
**作者**：thedracle
**发布时间**：2026-10-14T18:23:14Z
**挖掘日期**：2026-10-15
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Code, Tools, Pair Programming, Remote Work, Collaboration


## 📌 项目详解

Petal是一个为远程协作设计的开源配对编程工具，其特点是将共享窗口作为真实的桌面窗口，具有可移动的光标和低延迟。 Petal因其强烈的Hacker News关注度而引人注目，并解决了远程工作时代配对编程工具有限的痛点，尽管目前尚未出现明确的盈利模式。 Petal在开源许可证下发布，目前处于alpha阶段，通过Docker部署，托管实例需要最小化配置。


## 🌐 背景与生态

该项目源于CoScreen和Screenhero的关闭，两者都被大公司收购后不久被淘汰，突显了专用配对编程工具的空白。


## 💬 社区讨论

社区评论表达了兴奋和支持，创始人承认了以往工具被淘汰的痛苦，并对Petal的充满活力的社区表达了希望。


## 🚀 应用前景

Petal可用于软件开发、远程教育和客户支持场景，具有SaaS盈利或集成到更大开发工具的潜力。


## 🔧 技术栈

Petal使用LiveKit进行媒体传输，在macOS和Windows上运行，并利用开源模型如Fable和Astra进行快速开发。


## 🎯 上手难度

入门评级为入门级，需要Python和Docker，提供托管实例以实现零配置。


## 👥 目标用户

目标用户包括寻求高效配对编程解决方案的个人开发者、远程团队和教育机构。


## ⚖️ 类似项目对比

竞争对手包括Drovio（以其低延迟著称）和Pop（以其虚拟办公室功能为特色），尽管Petal的开源性质使其与众不同。


<details><summary>📄 查看原文内容</summary>


Hi HN!<p>I’m Jason Thomas, one of the founders of CoScreen.<p>As some of you may know, Datadog sunset the CoScreen service on July 31st.<p>Four of us from the original CoScreen team have spent the last couple months building a free and open source pair programming tool inspired by those that came before us: It’s called Petal (<a href="https:&#x2F;&#x2F;github.com&#x2F;kiruna-labs&#x2F;petal" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;kiruna-labs&#x2F;petal</a>)<p>Some history first, because when we started CoScreen we had hoped to break the sad and established pattern of this industry.<p>Screenhero was an exceptional tool that a lot of us loved for pairing. Multiple cursors, low latency, you could click your partner’s editor, and just start typing. It felt like magic while we had it. Then Slack bought it in 2015, and shut down the standalone app in December 2017.<p>When Till, Max, and I started CoScreen, we were aware of this history, and wanted to build an even more magical collaboration and screen sharing experience: the entire concept was “throw a window from your laptop up on someone else’s screen, and start collaborating with zero friction.”<p>Datadog acquired us in 2022, and thus began the great adventure of adapting our real-time technology into Datadog products, while also continue developing CoScreen as a standalone tool from the Datadog ecosystem. Datadog invested in the product for years and we’re thankful for that. But CoScreen itself proved, like so many other screen sharing tool acquisitions, to be too tangential from the customer base and core mission. We instead built other communication features in Datadog, the integrations with other video platforms, and also its wildly successful MCP server.
We weren&#x27;t the only ones. Around was bought by Miro and shut down in March 2025. Multi (formerly Remotion) was acqui-hired by OpenAI in 2024 and shut down about a month later. It&#x27;s nearly always the same story: a small team builds something hard that people love, a platform buys it for the team or the feature, and the standalone product doesn&#x27;t survive the integration.
So we decided firmly to do things differently this time. Petal is completely free and open source and we aren&#x27;t monetizing it. If we lose interest or get hit by a bus, you can self-host it or fork it, and nobody can sunset it on you. Honestly it&#x27;s a love letter to everyone in this community that supported us, believed in us, and to liberate collaborative screen sharing from this vicious cycle.<p>We hope through this we can help foster a large and vibrant community around innovating in this product sector.
What Petal does: shared windows show up as real windows on your desktop, movable and resizable, not tiles in a grid. Several people can share at once, everyone gets a labeled cursor, and you can click into any shared window to type and scroll. Rooms are persistent, so you click once to join &quot;eng-sync&quot; instead of passing links around.
It runs on macOS and Windows (Linux is next, this time for real and you can help us!), plus a web app. Media goes over LiveKit. You can use our hosted instance with zero config, or point the app at your own LiveKit server with one docker-compose if you want the traffic to stay on your network or even use an entirely different video backend if you want to.
The part that still feels strange to us: CoScreen took almost six years to build. The first version of Petal took under eight weeks, from scratch, with frontier models like Fable and Astra doing a lot of the work. Real-time video and window capture is some of the most unforgiving code we have ever written, so we didn&#x27;t expect that. We will do a proper writeup on what worked and what didn&#x27;t, and are happy to answer questions about it here.
Till, Darren, Max and I will be in the thread.


--- Top Comments ---

[jsherwani]: Screenhero co-founder&#x2F;CEO here — this is really great! It looks like we had similar feelings after leaving our acquiring companies with our products being sunset. Since leaving Slack, I&#x27;ve been building Pop with a new team. The first product we launched in 2020 is essentially Screenhero 2.0 (pop.com). Since then, we&#x27;ve been building an expanded product: a virtual office for remote teams, which is now almost ready for launch (there&#x27;s a waitlist at  https:&#x2F;&#x2F;new.pop...

[coscreen]: Till here, another co-founder of CoScreen. Like Jason wrote, our launches on HN and the feedback by many of you in 2019 were really important all the way back to the earliest days of our small and fancy tool. We did a lot of things since we&#x27;re proud of but a few plans remained unfulfilled, like support for Linux, until now. We&#x27;d love to work with you and see what you&#x27;ll build, now that Petal is out in the open for anyone to use, jam on, and make it your own.

[ripley12]: Very very happy to see this! I was lucky to work with Till+Jason on CoScreen (I came in late); they&#x27;re really exceptional people and CoScreen had a great collaboration UX that still hasn&#x27;t been matched by Zoom and friends. Really keen to see what they&#x27;ll be able to build this time around.

[lochnessduck]: Thank you for this, I am a big fan of pair programming, and even jetbrains is getting rid of their code-with-me service! It’s so Frustrating to see a useful feature&#x2F;tool get abandoned due to low usage. But those of us who use pair programming absolutely love it :) It’s a tool that helps further human connection, imo. And we could all use a little more of that atm.

[citizenfishy]: This is just what we need in our small startup. It solves problems we have when working remotely and joint debugging along with walking our customers through tricky issues. Can&#x27;t wait to give it a spin

</details>
