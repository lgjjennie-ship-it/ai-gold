---
layout: default
title: "在Godot中集成C++"
date: 2026-09-29T12:00:00+00:00
discovered_date: 2026-09-29
slug: 2026-09-29-using-any-c-library-in-godot
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目提供了一份指南，用于通过GDExtension在Godot游戏引擎中集成任何C++库，使开发者能够在他们的Godot项目中利用C++功能。 它通过允许C++集成来解决Godot项目中性能和高级功能的需求，在Hacker News上获得了33个星和8条评论，显示出一定的吸引力。 该项目使用GDExtension，需要编写CMake脚本和Python，并已注意到Linux上版本脚本等限制。"
tags: "C++, Godot, GDExtension, GameDev, Integration"
---

# 在Godot中集成C++


> 该项目提供了一份指南，用于通过GDExtension在Godot游戏引擎中集成任何C++库，使开发者能够在他们的Godot项目中利用C++功能。 它通过允许C++集成来解决Godot项目中性能和高级功能的需求，在Hacker News上获得了33个星和8条评论，显示出一定的吸引力。 该项目使用GDExtension，需要编写CMake脚本和Python，并已注意到Linux上版本脚本等限制。


**项目链接**：https://blog.conan.io/cpp/conan/gamedev/godot/cmake/2026/09/29/Using-Any-Cpp-Library-In-Godot.html
**作者**：czoido
**发布时间**：2026-09-29T08:40:37Z
**挖掘日期**：2026-09-29
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：C++, Godot, GDExtension, GameDev, Integration


## 📌 项目详解

该项目提供了一份指南，用于通过GDExtension在Godot游戏引擎中集成任何C++库，使开发者能够在他们的Godot项目中利用C++功能。 它通过允许C++集成来解决Godot项目中性能和高级功能的需求，在Hacker News上获得了33个星和8条评论，显示出一定的吸引力。 该项目使用GDExtension，需要编写CMake脚本和Python，并已注意到Linux上版本脚本等限制。


## 🌐 背景与生态

GDExtension是Godot的原生扩展系统，允许高性能的C++代码与Godot项目无缝集成，改进了其前身GDNative。


## 💬 社区讨论

社区评论讨论了性能分析支持、Godot Rust绑定、集成过程的复杂性以及静态链接问题。


## 🚀 应用前景

这可以用于游戏开发以增强性能关键部分，可能为模拟和策略游戏等产业带来产品。


## 🔧 技术栈

技术栈涉及C++、GDExtension、CMake和Python，依赖于Godot引擎进行集成。


## 🎯 上手难度

难度：进阶。前提条件包括Python、C++编译器以及对CMake的熟悉。步骤包括设置C++库并将其配置为GDExtension。


## 👥 目标用户

目标用户是需要使用C++库扩展Godot功能的游戏开发者和工程师。


## ⚖️ 类似项目对比

竞品包括GDNative，GDExtension的前身，以及提供类似功能以用于Rust库的Godot Rust绑定。


## 📚 参考链接

- [What is GDExtension? - Godot Engine](https://docs.godotengine.org/en/latest/engine_details/engine_api/gdextension/what_is_gdextension.html)
- [Basic Concepts - Understanding GDExtension | GDExtension ...](https://vorlac.github.io/gdextension-docs/getting_started/basic-concepts/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[MeteorMarc]: So, what profiling support is available to find the critical parts of your GDscript or C# code. Before needlessly jumping into c++ hassle for performance reasons? Tfa addresses functional reasons, which is ok.

[valorzard]: If you know rust, the Godot rust bindings for GDExtension are also really good and let you use any Rust library in Godot (including tokio and async rust if you really want)
 https:&#x2F;&#x2F;godot-rust.github.io&#x2F;

[jokoon]: So it requires writing a CMake script, some python, and some weird C++ code. A bit tedious but that&#x27;s how it goes.

[hnacobsxph]: Static linking libstdc++ with -fvisibility=hidden saved me on Linux, though it bit me the day I needed exceptions to cross the boundary.

[fwsgonzo]: Just don&#x27;t forget the versioning script needed on at least Linux. It&#x27;s either that or build with the same older distro Godot uses, so you have a matching libstdc++ version. You can link with a newer stdlibc++ but you will need a linker versioning script that hides your impl from the dynamic linker so you don&#x27;t get random ghosts in your machine.

</details>
