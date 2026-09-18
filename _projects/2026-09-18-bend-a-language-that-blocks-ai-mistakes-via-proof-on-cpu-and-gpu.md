---
layout: default
title: "Bend：用于CPU和GPU的AI证明语言"
date: 2026-09-18T12:00:00+00:00
discovered_date: 2026-09-18
slug: 2026-09-18-bend-a-language-that-blocks-ai-mistakes-via-proof-on-cpu-and-gpu
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Bend是一种编程语言，旨在通过证明防止AI错误，并针对CPU和GPU进行了优化，具有快速对象分配、高阶函数和无限制递归等功能。 Bend在4个月内获得了20K星，通过证明防止AI错误，解决了AI中的一个开发重要问题，这既新颖又实用，并通过SaaS或API服务具有明确的盈利路径。 Bend采用宽松许可证，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，但需要现代CPU或GPU以获得最佳性能。"
tags: "AI, Language, Proof, CPU, GPU"
---

# Bend：用于CPU和GPU的AI证明语言


> Bend是一种编程语言，旨在通过证明防止AI错误，并针对CPU和GPU进行了优化，具有快速对象分配、高阶函数和无限制递归等功能。 Bend在4个月内获得了20K星，通过证明防止AI错误，解决了AI中的一个开发重要问题，这既新颖又实用，并通过SaaS或API服务具有明确的盈利路径。 Bend采用宽松许可证，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，但需要现代CPU或GPU以获得最佳


**项目链接**：https://bend-lang.com/
**作者**：nicolas-siplis
**发布时间**：2026-09-17T20:36:13Z
**挖掘日期**：2026-09-18
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Language, Proof, CPU, GPU


## 📌 项目详解

Bend是一种编程语言，旨在通过证明防止AI错误，并针对CPU和GPU进行了优化，具有快速对象分配、高阶函数和无限制递归等功能。 Bend在4个月内获得了20K星，通过证明防止AI错误，解决了AI中的一个开发重要问题，这既新颖又实用，并通过SaaS或API服务具有明确的盈利路径。 Bend采用宽松许可证，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，但需要现代CPU或GPU以获得最佳性能。


## 🌐 背景与生态

Bend位于AI安全编程语言的细分领域，通过强制执行数学证明来防止AI错误，从而区别于传统语言。近年来AI和形式化验证的进步使这种方法成为可能。


## 💬 社区讨论

社区评论意见不一，一些人对其新颖的方法表示兴奋，而另一些人则对其实用性和可信度持怀疑态度。


## 🚀 应用前景

Bend可应用于对AI可靠性至关重要的场景，如自主系统、金融建模和科学研究，具有通过SaaS或API服务进行盈利的潜力。


## 🔧 技术栈

Bend结合了Rust和Haskell，依赖PyTorch进行GPU加速，并使用自定义编译器进行证明验证。


## 🎯 上手难度

使用Bend的难度评级为进阶，需要Python 3.8+、现代GPU以及函数式编程的熟悉程度。安装涉及下载最新版本并遵循设置指南。


## 👥 目标用户

目标用户包括后端工程师、ML实践者和自主车辆、金融和医疗保健等行业的研究员。


## ⚖️ 类似项目对比

竞品包括Gleam、V和Zig，这些也是高级编程语言，但缺乏Bend的AI证明功能。


## 📚 参考链接

- [A high-level, massively parallel programming language - GitHub](https://github.com/HigherOrderCO/bend)
- [Bend](https://bend-lang.org/)
- [Bend Language: AI-Proof Coding via LAWS.bend (2026 ...](https://www.explainx.ai/blog/bend-language-ai-proof-laws-2026)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[LightMachine]: Hi, I&#x27;m the author. HN staff: someone posted before me. Could we change the title to 
&quot;Bend - a language that blocks AI mistakes via proof and runs on GPUs&quot;? Everyone: feel free to ask any question, but I&#x27;d be highly appreciative if you could be a bit civilized and respectful this time. I&#x27;ve worked on this for 1 year, nearly 16h&#x2F;day, 7 days a week, and I&#x27;m giving it for free. You need not to use it. So, I&#x27;d be thankful if you could point occasional fail...

[mccoyb]: My read on this, after ingesting a good amount of content on the history, is: - this Bend is not really related to the old Bend (only in name) - this Bend doesn&#x27;t really have anything to do with interaction combinators - this Bend is a QTT, with a change to affinity which enforces a good performance property for GPUs - the &quot;higher order at comptime&quot; is neat, reminds me of Andras Kovacs&#x27; work on 2ltt and staging in dependently typed languages. - this Bend is likely to be go...

[plastic041]: This project&#x27;s repo has 20K stars with only 500 forks, with less than 300 issues(including closed). Something&#x27;s not right. Compared to other programming languages: - Gleam: 22K stars, 1K forks, 3K issues - V: 38K stars, 2.3K forks, 11K issues - Ruby: 23K stars, 5.6 forks, 19K issues - Zig: 43K stars, 3K forks, 14K issues It got 16K stars just in 4 months too.  https:&#x2F;&#x2F;www.star-history.com&#x2F;?repos=bendlang%2Fbend  Also how would anyone trust this? I&#x27;ve never seen a...

[meghanto]: Gotta say, having followed Taelin on this project since mid 2023, this was not the response I expected when this language first dropped. It&#x27;s interesting how cosmetics drive discussion, and how HN comments are weirdly divided in a very dismissive or skeptical camp and those acting incredulous and offended at the reaction of the former. What I expected instead was a lot more discussion about use cases, benchmarking, possibilities, limitations (that aren&#x27;t about git history) and the s...

[svachalek]: Cool idea. I tried using it to port a little meeting fixer cron job I vibe coded, it seemed a natural fit as its essentially trying to satisfy invariants in my calendar. It basically succeeded but Claude (Opus 5) did have some complaints: &#x27;Base ships one arithmetic law, U32.add_comm. There is no order theory. About 60 of PROOF.bend&#x27;s 163 lines are cmp_refl, and_false, and_comm, le_max_l, le_max_r, add_succ — facts you&#x27;d assume exist. You&#x27;d write them once per project and n...

</details>
