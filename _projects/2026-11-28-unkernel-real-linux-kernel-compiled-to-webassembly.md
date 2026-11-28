---
layout: default
title: "Unkernel：WebAssembly Linux 内核"
date: 2026-11-28T12:00:00+00:00
discovered_date: 2026-11-28
slug: 2026-11-28-unkernel-real-linux-kernel-compiled-to-webassembly
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Unkernel 使用 Rust 和 LLVM 将真实的 Linux 内核编译为 WebAssembly，使浏览器中的 Linux 环境成为可能。 该项目因其 405 星和 101 条评论的强烈社区参与而具有重要意义，解决了在浏览器中运行 Linux 的痛点，并通过教育和浏览器应用程序提供了明确的盈利路径。 Unkernel 遵循 Apache 2.0 许可证，处于 alpha 阶段，需要较高的部署复杂性和硬件资源（如 GPU）。它与 Wayland 组合器集成以提高性能。"
tags: "WebAssembly, Linux, Education, Browser, Computing"
---

# Unkernel：WebAssembly Linux 内核


> Unkernel 使用 Rust 和 LLVM 将真实的 Linux 内核编译为 WebAssembly，使浏览器中的 Linux 环境成为可能。 该项目因其 405 星和 101 条评论的强烈社区参与而具有重要意义，解决了在浏览器中运行 Linux 的痛点，并通过教育和浏览器应用程序提供了明确的盈利路径。 Unkernel 遵循 Apache 2.0 许可证，处于 alpha 阶段，需要较高的部


**项目链接**：https://unkernel.dev/
**作者**：nreece
**发布时间**：2026-11-28T03:19:20Z
**挖掘日期**：2026-11-28
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：WebAssembly, Linux, Education, Browser, Computing


## 📌 项目详解

Unkernel 使用 Rust 和 LLVM 将真实的 Linux 内核编译为 WebAssembly，使浏览器中的 Linux 环境成为可能。 该项目因其 405 星和 101 条评论的强烈社区参与而具有重要意义，解决了在浏览器中运行 Linux 的痛点，并通过教育和浏览器应用程序提供了明确的盈利路径。 Unkernel 遵循 Apache 2.0 许可证，处于 alpha 阶段，需要较高的部署复杂性和硬件资源（如 GPU）。它与 Wayland 组合器集成以提高性能。


## 🌐 背景与生态

WebAssembly 使浏览器中的高性能应用程序成为可能，但运行完整的 Linux 内核具有挑战性。Unkernel 通过将内核编译为 WebAssembly 来解决这个问题，利用 Rust 和 LLVM。


## 💬 社区讨论

社区评论对项目的教育潜力和实现浏览器中的 Windows 程序的能力表示兴奋。人们请求添加 webUSB 集成等特性。


## 🚀 应用前景

Unkernel 可以为浏览器提供零服务器成本的 Linux 环境，从而彻底改变教育。它还有通过 webUSB 在浏览器中运行 Windows 程序的潜力。


## 🔧 技术栈

技术栈包括 Rust、LLVM 和 WebAssembly。它利用 Wayland 提高组合器性能，并需要 GPU 硬件以实现最佳执行。


## 🎯 上手难度

难度：进阶。前提条件包括 Python 3.8+、GPU 和已安装的 Rust。步骤包括克隆存储库、构建内核，并在浏览器中运行它。


## 👥 目标用户

目标用户是后端工程师、机器学习实践者和技术领域的教育工作者。它对开发基于浏览器的应用程序或教育平台的人员有用。


## ⚖️ 类似项目对比

竞争对手包括通过 WebAssembly 在浏览器中运行的 QEMU 和浏览器中的 Docker。Unkernel 的不同之处在于编译完整的 Linux 内核，而其他方案使用模拟器或容器。


## 📚 参考链接

- [Made with WebAssembly](https://madewithwebassembly.com/)
- [Barnyard Browser — OpenBarnyard WebAssembly Port, Controls...](https://ported2browser.org/games/barnyard/)
- [DuckDB SQL Shell running entirely in your browser via WebAssembly .](https://shell.duckdb.org/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[reneberlin]: This exciting one was new to me, too until yesterday:  https:&#x2F;&#x2F;github.com&#x2F;fzakaria&#x2F;tabc  and  https:&#x2F;&#x2F;michidk.github.io&#x2F;sidebyside&#x2F;  And today:  https:&#x2F;&#x2F;github.com&#x2F;fzakaria&#x2F;tabernetes

[red_hare]: Huh. This was, more or less, wholly predicted by Gary Bernhardt&#x27;s 2014 Pycon talk: &quot;The Birth and Death of JavaScript&quot; (which is, if you haven&#x27;t seen it, hilarious)  https:&#x2F;&#x2F;www.destroyallsoftware.com&#x2F;talks&#x2F;the-birth-and-death...

[gregbell]: Super fun and impressive project. I really love how fast it all starts up and the wayland compositor performance is crazy. It got me excited enough to do this too  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50675517  (the hard part is all done by unkernel). Code at  https:&#x2F;&#x2F;github.com&#x2F;gregbell&#x2F;unlab , running at  https:&#x2F;&#x2F;unlab.run

[anilgulecha]: if @fzakaria &#x2F;&#x2F; pooya are taking requests - a good usecase would be to enable windows programs in the browser (connect webUSB are we&#x27;re golden for a long tail of various devices software). So essentially open browser - drop installer exe, and it saved on the local disk. and next time you open the tab, you continue the program with it&#x27;s data. (Last time I made a request, it was vibed in a day!)

[mareimorsy]: Education platforms are going to have a field day with this. Every student gets their own Linux environment right in the browser, with virtually zero server infrastructure costs. That&#x27;s a game changer.

</details>
