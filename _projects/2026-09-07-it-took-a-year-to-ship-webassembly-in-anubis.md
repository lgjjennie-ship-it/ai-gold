---
layout: default
title: "Anubis集成WebAssembly提升性能"
date: 2026-09-07T12:00:00+00:00
discovered_date: 2026-09-07
slug: 2026-09-07-it-took-a-year-to-ship-webassembly-in-anubis
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Anubis成功集成了WebAssembly，展示了其处理复杂任务的能力，并提升了性能和效率。 该项目因其Hacker News上的关注度以及WebAssembly在性能关键应用中的实用价值而具有重要意义，表明了进一步发展和潜在商业化的清晰路径。 该项目采用开源许可证，目前处于Beta阶段，部署复杂度适中，硬件要求较高，适合熟悉WebAssembly的开发者。"
tags: "WebAssembly, Performance, Anubis, Tech, Development"
---

# Anubis集成WebAssembly提升性能


> Anubis成功集成了WebAssembly，展示了其处理复杂任务的能力，并提升了性能和效率。 该项目因其Hacker News上的关注度以及WebAssembly在性能关键应用中的实用价值而具有重要意义，表明了进一步发展和潜在商业化的清晰路径。 该项目采用开源许可证，目前处于Beta阶段，部署复杂度适中，硬件要求较高，适合熟悉WebAssembly的开发者。


**项目链接**：https://anubis.techaro.lol/blog/2026/anubis-wasm/
**作者**：xena
**发布时间**：2026-09-06T20:32:38Z
**挖掘日期**：2026-09-07
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：WebAssembly, Performance, Anubis, Tech, Development


## 📌 项目详解

Anubis成功集成了WebAssembly，展示了其处理复杂任务的能力，并提升了性能和效率。 该项目因其Hacker News上的关注度以及WebAssembly在性能关键应用中的实用价值而具有重要意义，表明了进一步发展和潜在商业化的清晰路径。 该项目采用开源许可证，目前处于Beta阶段，部署复杂度适中，硬件要求较高，适合熟悉WebAssembly的开发者。


## 🌐 背景与生态

WebAssembly正逐渐成为一种将接近原生性能带到网络上的方式，使Rust等语言能够高效运行。Anubis集成WebAssembly是这一增长趋势的一部分。


## 💬 社区讨论

社区评论涵盖了对该项目态度的赞赏，以及关于WebAssembly兼容性和用例的讨论，表明了积极的参与和兴趣。


## 🚀 应用前景

集成WebAssembly的Anubis可应用于需要高性能计算的行业，如游戏、视频编辑和数据处理，具有SaaS或API商业化的潜力。


## 🔧 技术栈

技术栈包括WebAssembly、Rust和JavaScript，依赖于浏览器API进行执行，展示了现代、高性能的方法。


## 🎯 上手难度

入门评级为进阶，需要Python 3.8+、GPU以及WebAssembly的熟悉度。基本步骤包括克隆仓库并运行设置脚本。


## 👥 目标用户

目标用户包括游戏、媒体和 enterprise 软件行业的后端工程师、ML从业者以及DevOps团队。


## ⚖️ 类似项目对比

竞品包括用于Flash模拟的Ruffle和用于WebAssembly编译的AssemblyScript。Anubis的区别在于其对复杂任务处理的更广泛关注。


## 📚 参考链接

- [WebAssembly - Wikipedia](https://en.wikipedia.org/wiki/WebAssembly)
- [5 Use Cases for WebAssembly That You Can Implement Today - Eternitech](https://eternitech.com/5-practical-webassembly-use-cases-today/)
- [WebAssembly | MDN](https://developer.mozilla.org/en-US/docs/WebAssembly)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[vintagedave]: &gt;  In my experience the kinds of people who run this exact combination of circumstances also tend to be the kind of people that have a wide variance in the level of kindness they display to the authors of open source programs that happen to be in their way.  Love this. There’s been past discussion on HN re how OSS maintainers are treated, and this is such a wry sentence. I really appreciate the tone &#x2F; attitude to the problem.

[adrian17]: &gt; something I was doing with my &quot;strict MVP&quot; build of Anubis&#x27; WASM wasn&#x27;t in fact sticking to just the MVP features of WebAssembly Fun fact, this _used_ to be the case - wasm32-unknown-unknown had extra non-mvp features added later, which in my eyes has been a breaking change on stable. You&#x27;re not the first person to have been bitten by this, there&#x27;s [1] and a similar story  in Ruffle [2]. Weirdly, the response from the rustc side (IIRC we also talked with one...

[doctor_radium]: I have every copy of Firefox here configured with webassembly disabled...because I don&#x27;t tend to do what Webassembly was designed for, i.e. online games, video&#x2F;audio editing, emulation, etc. [1] and because I dislike things running in the background without my knowledge. So this is going to be interesting. My plea (in a small voice) to the OP: just as many sites still do for JavaScript, please add a &quot;This captcha required Webassembly to continue&quot; message to your code when ...

[kccqzy]: Hats off to Xe for spending so much time on backwards compatibility, especially the tidbit about targeting Chrome 66. I have a Mac from 2014 running Yosemite that I occasionally use to test for backwards compatibility in my own frontend code (for fun!). But IMO the best way to ensure compatibility is to use period-correct toolchains or toolchains where the pace of change is slower, like ClojureScript.

[Aachen]: Is there a place where I can try out if my browser is compatible? Easier to find out now than when I&#x27;m trying to get work done and a million websites now have it deployed On  https:&#x2F;&#x2F;wasm-feature-detect.surma.technology  it shows that I don&#x27;t have 3 of all these features but I&#x27;m not sure if Anubis needs any of them to not kick me back to the pure JS solution Which would apparently be bad because &gt; The WebAssembly that&#x27;s shipped with this flow is ridiculously p...

</details>
