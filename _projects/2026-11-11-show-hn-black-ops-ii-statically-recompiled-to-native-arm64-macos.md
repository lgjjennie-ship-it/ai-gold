---
layout: default
title: "黑鹰坠落II重编译适配ARM64 macOS"
date: 2026-11-11T12:00:00+00:00
discovered_date: 2026-11-11
slug: 2026-11-11-show-hn-black-ops-ii-statically-recompiled-to-native-arm64-macos
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目利用Claude Opus 5.5将Steam版黑鹰坠落II静态重编译为原生ARM64 macOS可执行程序，在所有区域实现高达60fps的高性能，无需依赖任何模拟器。 它因高性能和原生兼容ARM64 macOS而受到关注，解决了热门游戏兼容性问题，并展示了新颖的重编译方法，具有通过SaaS或高级功能实现货币化的潜力。 该项目采用开源许可证，目前处于alpha阶段，部署复杂度中等，无需特定硬件要求，只需现代ARM64 Mac即可。支持战役、本地多人和本地僵尸模式。"
tags: "Game, Compatibility, Performance, macOS, Recompilation"
---

# 黑鹰坠落II重编译适配ARM64 macOS


> 该项目利用Claude Opus 5.5将Steam版黑鹰坠落II静态重编译为原生ARM64 macOS可执行程序，在所有区域实现高达60fps的高性能，无需依赖任何模拟器。 它因高性能和原生兼容ARM64 macOS而受到关注，解决了热门游戏兼容性问题，并展示了新颖的重编译方法，具有通过SaaS或高级功能实现货币化的潜力。 该项目采用开源许可证，目前处于alpha阶段，部署复杂度中等，无需特定硬


**项目链接**：https://github.com/adrbn/bo2-mac
**作者**：adrbn
**发布时间**：2026-11-11T04:56:47Z
**挖掘日期**：2026-11-11
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Game, Compatibility, Performance, macOS, Recompilation


## 📌 项目详解

该项目利用Claude Opus 5.5将Steam版黑鹰坠落II静态重编译为原生ARM64 macOS可执行程序，在所有区域实现高达60fps的高性能，无需依赖任何模拟器。 它因高性能和原生兼容ARM64 macOS而受到关注，解决了热门游戏兼容性问题，并展示了新颖的重编译方法，具有通过SaaS或高级功能实现货币化的潜力。 该项目采用开源许可证，目前处于alpha阶段，部署复杂度中等，无需特定硬件要求，只需现代ARM64 Mac即可。支持战役、本地多人和本地僵尸模式。


## 🌐 背景与生态

随着苹果转向ARM64架构，静态重编译日益重要，它使旧软件能够原生运行。该项目满足了在macOS上原生运行热门游戏日益增长的需求。


## 💬 社区讨论

社区评论对重编译过程表示好奇，并探讨了当前法律环境下反编译/逆向工程的挑战。


## 🚀 应用前景

该工具可扩展至其他游戏，提供包含分屏和局域网模式的增强功能SaaS服务。潜在行业包括游戏、教育和娱乐。


## 🔧 技术栈

技术栈包括用于重编译的Claude Opus 5.5，未提及具体框架或依赖项。基础设施可能是原生macOS。


## 🎯 上手难度

难度：进阶。前提条件包括现代ARM64 Mac、Steam账号和游戏。步骤包括下载工具并运行，未提及特定硬件要求。


## 👥 目标用户

目标用户是寻求高性能原生执行旧游戏的玩家和macOS爱好者，无需模拟器。


## ⚖️ 类似项目对比

竞品包括Wine和Rosetta，它们用于跨平台兼容性但使用模拟器。对于特定游戏的静态重编译，没有直接竞争对手。


## 📚 参考链接

- [GitHub - Zelda64Recomp/Zelda64Recomp: Static recompilation of...](https://github.com/Zelda64Recomp/Zelda64Recomp)
- [Gen1Recomp vs Emulation: What Is Different?](https://gen1recomp.com/gen1recomp-vs-emulation/)
- [Static Recompilation will probably be the only way to play... | ResetEra](https://www.resetera.com/threads/static-recompilation-will-probably-be-the-only-way-to-play-modern-closed-source-games-on-future-platforms-in-year-2050-on-our-pc-ps9-nintendo-mml-xbox.875400/)

<details><summary>📄 查看原文内容</summary>


I grew up with Black Ops 2 and wanted to see if I could make it work on my 2020 MacBook Pro. So I used Claude Opus 5.5 to create a tool that converts your copy of the game (from Steam) to a native ARM64 Mac app, with almost 60fps in all areas. The whole game is statically recompilated ahead-of-time (AOT) and does not use any emulator whatsoever, be it Wine, Crossover or Rosetta. The best thing is the performance, although some heat issues are still to fix. You get to play the whole Campaign, local Multiplayer (with bots) and local Zombies (all DLCs maps; you need to have them in your Steam library obviously) at about 60fps. Split-screen was not in the PC version, but I&#x27;ve been working on it lately; it&#x27;s coming soon! LAN mode is on the roadmap for later too :)


--- Top Comments ---

[cedws]: How does it actually recompile, does it use an existing tool? I can’t imagine the agent combs through every routine and hand translates the assembly.

[phaser]: what was your workflow for creating this? there&#x27;s now extra guardrails around decompiling &#x2F; reverse engineering, do you think this is still possible to do or were you just lucky enough to do it before the guardrails?

</details>
