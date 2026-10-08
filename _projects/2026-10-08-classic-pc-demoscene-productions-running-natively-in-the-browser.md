---
layout: default
title: "浏览器中的经典PC演示场景模拟"
date: 2026-10-08T12:00:00+00:00
discovered_date: 2026-10-08
slug: 2026-10-08-classic-pc-demoscene-productions-running-natively-in-the-browser
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目使用x86模拟器在浏览器中本地运行经典PC演示场景制作，记录并翻译CPU执行为C代码。 它因高社区参与度和活跃讨论而重要，展示了新颖的技术方法，尽管没有明确的盈利模式，但在教育和娱乐方面具有潜力。 该项目采用开放许可，处于alpha阶段，由于模拟器的要求，部署可能具有中等复杂性。"
tags: "Web, Emulator, Demoscene, Education, Entertainment"
---

# 浏览器中的经典PC演示场景模拟


> 该项目使用x86模拟器在浏览器中本地运行经典PC演示场景制作，记录并翻译CPU执行为C代码。 它因高社区参与度和活跃讨论而重要，展示了新颖的技术方法，尽管没有明确的盈利模式，但在教育和娱乐方面具有潜力。 该项目采用开放许可，处于alpha阶段，由于模拟器的要求，部署可能具有中等复杂性。


**项目链接**：https://treylorswift.github.io/demoscene-recomp/web/
**作者**：adunk
**发布时间**：2026-10-08T06:29:25Z
**挖掘日期**：2026-10-08
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Web, Emulator, Demoscene, Education, Entertainment


## 📌 项目详解

该项目使用x86模拟器在浏览器中本地运行经典PC演示场景制作，记录并翻译CPU执行为C代码。 它因高社区参与度和活跃讨论而重要，展示了新颖的技术方法，尽管没有明确的盈利模式，但在教育和娱乐方面具有潜力。 该项目采用开放许可，处于alpha阶段，由于模拟器的要求，部署可能具有中等复杂性。


## 🌐 背景与生态

演示场景是一个专注于创建音频视觉计算机程序的亚文化，历史上受限于特定硬件。该项目将那种复古体验带到了现代网络平台。


## 💬 社区讨论

社区评论从对x86模拟方法的技术询问到对浏览器中演示场景价值的哲学辩论不等。


## 🚀 应用前景

这可能彻底改变复古计算教育，并提供独特的娱乐领域。潜在应用包括教育平台和利基游戏服务。


## 🔧 技术栈

技术栈包括x86模拟器、C代码生成以及用于渲染图形和音频的网络技术。


## 🎯 上手难度

难度：进阶。前提条件包括现代浏览器和对基本编程概念的理解。


## 👥 目标用户

目标用户是复古计算爱好者、教育工作者以及有兴趣在基于Web的模拟方面的开发者。


## ⚖️ 类似项目对比

竞品包括其他基于Web的模拟器如'86Box'以及已将经典游戏移植到浏览器中的项目。


## 📚 参考链接

- [X86 emulator](https://en.wikipedia.org/wiki/X86_emulator)
- [Demoscene](https://en.wikipedia.org/wiki/Demoscene)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[Retr0id]: &gt; The demo is run on an x86 emulator that records every block of code the CPU actually executes, over the whole demo. &gt; That recording is translated into C - the original instructions, one for one, with the exact cycle timing of the emulated machine. What&#x27;s the advantage of this approach vs cycle-accurate emulation? (I&#x27;d guess it can go faster, due to compiler optimization?) &gt; The result is checked against the emulator event for event: every interrupt, port access and frame...

[Martin_Silenus]: The days I gave up with demoscene. When PC killed Atari ST and Amiga scene (sorry to put you after amiguys, but life was always easier for you ;) ), all the magic of fixed hardware without tons of Mhz and RAM, when we were running after that cathode ray which wouldn&#x27;t wait, exploiting hardware bugs to break those damn borders above, below and sideways, spending hours turning my head upside-down to read unreadable scrolltexts, looking at psychedelic plasma effects with bazillions colors.....

[futurecat]: a couple of days ago I posted this:  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49982323  State of the Art was ported to the browser as well.

[Sharlin]: If there’s no human effort behind this, what’s the point? You could just as well watch any of the zillions of video recordings of these demos. There’s no inherent value in &quot;running natively in the browser&quot;. Never mind the vast irony in demoscene specifically being a celebration of human skill and creativity.

[gritzko]: So much fun. I recently ported some old strategy games. Claude does it almost on its own  http:&#x2F;&#x2F;replicated.live&#x2F;blog&#x2F;games

</details>
