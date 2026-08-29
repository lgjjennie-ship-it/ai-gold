---
layout: default
title: "三星的PIM技术"
date: 2026-08-29T12:00:00+00:00
discovered_date: 2026-08-29
slug: 2026-08-29-samsung-s-processing-in-memory-pim
source: hackernews
category: show-hn
ai_score: 9.0
summary: "三星的PIM技术将计算直接集成到内存模块中，以提高能源效率和性能。 该项目因其高参与度和讨论而具有重要意义，通过减少数据移动解决了计算中的关键痛点，并通过先进的硬件解决方案提供了明确的盈利潜力。 该技术已投入生产，需要先进的硬件集成和专业知识进行部署，当前实施的可扩展性存在显著限制。"
tags: "PIM, Hardware, Performance, Energy Efficiency, Computing"
---

# 三星的PIM技术


> 三星的PIM技术将计算直接集成到内存模块中，以提高能源效率和性能。 该项目因其高参与度和讨论而具有重要意义，通过减少数据移动解决了计算中的关键痛点，并通过先进的硬件解决方案提供了明确的盈利潜力。 该技术已投入生产，需要先进的硬件集成和专业知识进行部署，当前实施的可扩展性存在显著限制。


**项目链接**：https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing
**作者**：ingve
**发布时间**：2026-08-29T06:06:51Z
**挖掘日期**：2026-08-29
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：PIM, Hardware, Performance, Energy Efficiency, Computing


## 📌 项目详解

三星的PIM技术将计算直接集成到内存模块中，以提高能源效率和性能。 该项目因其高参与度和讨论而具有重要意义，通过减少数据移动解决了计算中的关键痛点，并通过先进的硬件解决方案提供了明确的盈利潜力。 该技术已投入生产，需要先进的硬件集成和专业知识进行部署，当前实施的可扩展性存在显著限制。


## 🌐 背景与生态

处理内存（PIM）是半导体架构中的一个新兴领域，解决了内存和处理器之间数据移动的瓶颈。三星的实现是更高效计算趋势的一部分。


## 💬 社区讨论

社区评论从对潜在益处的兴奋到对实施挑战的怀疑不等，有些人探索理论应用，其他人则将其与过去的技术进行比较。


## 🚀 应用前景

PIM在高性能计算、人工智能和数据中心方面具有强大的应用前景，减少数据移动可以显著提高性能和能源效率。


## 🔧 技术栈

技术栈包括先进的内存技术如LPDDR5-PIM，并与现有CPU架构集成，需要专门的硬件和软件支持。


## 🎯 上手难度

入门评级为进阶，需要先进的硬件和软件知识、Python以及访问专门的开发套件。


## 👥 目标用户

目标用户包括硬件工程师、人工智能研究人员以及专注于高性能计算和节能解决方案的企业团队。


## ⚖️ 类似项目对比

竞品包括英特尔Optane DC持久内存和惠普内存驱动计算，它们也旨在减少数据移动，但在具体实施方法上有所不同。


## 📚 参考链接

- [Processing - in - Memory ( PIM ) Architectures: The Next Frontier in...](https://www.linkedin.com/pulse/processing-in-memory-pim-architectures-next-frontier-epbof)
- [Processing - in - Memory ( PIM ) How It Works, Benefits & Uses](https://hashinghardware.com/processing-in-memory-pim/)
- [Memory in AI/ML and Data Era](https://hc2023.hotchips.org/assets/program/conference/day1/PIM/23_HC35_PIM_PNM_Samsung_final.pdf)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[OptionX]: So instead of putting more cache on the cpu you just put the cpu on the cache.

[bhouston]: I wrote up a theoretical post here about LMM performance of a MacBook Pro with PIM memory:  https:&#x2F;&#x2F;ben3d.ca&#x2F;blog&#x2F;m5-max-samsung-lpddr5-pim-650-tokens-p...

[londons_explore]: Whilst processing in memory is clearly the future, I am unconvinced by this implementation. Matrix multiplication involves getting every entry of the input and output matrices to be at the same multiplier at the same time. (Ie. N^2). To do that, a lot of data movement needs to happen.   Movement  is the main  thing - the multiplication and addition is a sideshow as far as energy and silicon space is concerned.   You need a &#x27;around the chip&#x27; ring shift register to pass every element ...

[pragma_x]: What I find amusing about moving compute to a RAM bank is it _almost_ resembles where we were with ISA-based extended RAM back in the 1980&#x27;s.  Some cards featured a CPU that took over the whole system and&#x2F;or functioned like an upgrade.  Others were a &quot;computer on a card&quot; that provided other features.  I think this goes to show how cyclic tech can be.  So, something like Samsung&#x27;s invention here might have gained traction, as overcoming the slow PC ISA bus would have b...

[plywoodShadow]: What about energy consumption? Wouldn&#x27;t active cooling be needed for RAM as well as for CPU and GPU?

</details>
