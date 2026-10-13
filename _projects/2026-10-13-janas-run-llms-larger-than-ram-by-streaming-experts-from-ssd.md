---
layout: default
title: "Janas：SSD流式传输大型LLM"
date: 2026-10-13T12:00:00+00:00
discovered_date: 2026-10-13
slug: 2026-10-13-janas-run-llms-larger-than-ram-by-streaming-experts-from-ssd
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Janas允许通过从SSD流式传输来在本地运行大型LLM，克服内存限制。它采用独特的流式方法，使LLM无需大量RAM即可访问。 Janas值得关注，因其获得了160个星标和Hacker News上的活跃讨论。它解决了开发者在本地运行大型LLM时的显著痛点，提供了一种新颖的解决方案，具有更广泛的应用潜力。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要SSD和基本的编程知识，除标准计算资源外没有特定的硬件要求。"
tags: "LLM, Streaming, Local, AI, Tools"
---

# Janas：SSD流式传输大型LLM


> Janas允许通过从SSD流式传输来在本地运行大型LLM，克服内存限制。它采用独特的流式方法，使LLM无需大量RAM即可访问。 Janas值得关注，因其获得了160个星标和Hacker News上的活跃讨论。它解决了开发者在本地运行大型LLM时的显著痛点，提供了一种新颖的解决方案，具有更广泛的应用潜力。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要SSD和基本的编程知识，


**项目链接**：https://github.com/prabanta-dev/janas
**作者**：khalidkhair
**发布时间**：2026-10-12T22:05:43Z
**挖掘日期**：2026-10-13
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Streaming, Local, AI, Tools


## 📌 项目详解

Janas允许通过从SSD流式传输来在本地运行大型LLM，克服内存限制。它采用独特的流式方法，使LLM无需大量RAM即可访问。 Janas值得关注，因其获得了160个星标和Hacker News上的活跃讨论。它解决了开发者在本地运行大型LLM时的显著痛点，提供了一种新颖的解决方案，具有更广泛的应用潜力。 该项目采用MIT许可证，目前处于alpha阶段，部署复杂度适中。它需要SSD和基本的编程知识，除标准计算资源外没有特定的硬件要求。


## 🌐 背景与生态

大型语言模型（LLMs）越来越受欢迎，但通常需要大量内存，限制了它们的本地部署。Janas通过从SSD流式传输LLMs来解决这一问题，这是AI工具生态系统中的一个 growing trend。像 llama.cpp 这样的替代方案已经启发了类似的流式解决方案。


## 💬 社区讨论

社区评论表达了对项目潜力和实用性的兴奋，有些人指出它与Strata等现有解决方案的相似性。其他人则强调了避免GPU内存问题的实际好处。


## 🚀 应用前景

Janas可用于需要本地LLM部署的场景，例如开发环境或中小企业。其潜在盈利路径包括为AI驱动工具提供的SaaS或API服务。


## 🔧 技术栈

技术栈包括用于性能的C++，以及CUDA等库的依赖项用于GPU加速。它利用SSD流式传输进行模型加载，并且不依赖除标准系统工具外的特定框架。


## 🎯 上手难度

难度：进阶。前提条件包括Python环境和SSD。步骤包括克隆仓库、从源代码构建，并运行一个基本测试脚本。


## 👥 目标用户

目标用户包括技术、医疗保健等行业中的后端工程师、ML实践者和DevOps团队。对于那些在内存限制下工作于AI驱动应用的人来说，它特别有用。


## ⚖️ 类似项目对比

竞品包括 llama.cpp 和 Strata。Janas通过专注于SSD流式传输而有所不同，这比基于GPU的解决方案更具可访问性。Strata 提供类似的功能，但方法不同。


## 📚 参考链接

- [Self-Hosting LLMs on the 512GB M5 Ultra Mac Studio... | Pinggy Blog](https://pinggy.io/blog/self_hosting_llms_on_512gb_m5_ultra_mac_studio/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dofm]: Amazing to me that something as wild as this is now basically a trope. I don&#x27;t mean this negatively; open weights AI and open source tooling is about the only thing that gives me hope. The fact that there are dozens of these things hints at the beginning of the dull normalisation of openly available, non-monopoly AI tools, which is what is needed if we are all to survive.

[jdb9001]: Every few weeks, someone stumbles on what llama.cpp has had for years again, and reimplements it. I&#x27;m not sure why.

[suprjami]: Qwen 3? (Jumanji) What year is it? What a waste of time. Strata already does this with Qwen3.8-Flash-Next:  https:&#x2F;&#x2F;github.com&#x2F;Niko1221&#x2F;Strata

[sieve]: &gt; Using a GPU has, once, caused a driver reset that took the desktop with it. Only once? This has happened to me so many times with LLM-assisted development. I was writing an OCR engine and pathological shapes would cause OOM that would take the display out. On other occasions, the LLM would try to load 24GB of bf16 weights onto a 16GB GPU without understanding the consequences. Have to encode this in logic: keep some space reserved for the display, and check before allocation. But some er...

[3eb7988a1663]: If anyone needs to see what 62 tokens&#x2F;second looks like:  https:&#x2F;&#x2F;token.qusai.pro&#x2F;?speed=62  Which seems sufficient for mortals who are not running gas town, but want a local model.

</details>
