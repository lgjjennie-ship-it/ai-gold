---
layout: default
title: "macOS AI照片和视频搜索"
date: 2026-10-05T12:00:00+00:00
discovered_date: 2026-10-05
slug: 2026-10-05-show-hn-ai-search-for-every-photo-and-every-frame-of-video-on-macos
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目为macOS提供AI照片和视频搜索工具，通过索引每一帧来实现精确搜索。它利用了像CLIP这样的先进AI模型进行图像识别，并利用macOS的Vision框架进行OCR。 该项目因其153个星标和69条评论在Hacker News上的强劲势头而具有重要意义，解决了在macOS上进行高效照片和视频搜索的实际需求。它抓住了媒体管理中AI日益增长的趋势，并通过SaaS或API提供具有明确的盈利潜力。 该项目采用开源许可证，目前处于Beta阶段，部署复杂度适中。它需要一台兼容的Mac硬件配置，可能需要GPU来提高性能。"
tags: "AI, Image, Video, Search, macOS"
---

# macOS AI照片和视频搜索


> 该项目为macOS提供AI照片和视频搜索工具，通过索引每一帧来实现精确搜索。它利用了像CLIP这样的先进AI模型进行图像识别，并利用macOS的Vision框架进行OCR。 该项目因其153个星标和69条评论在Hacker News上的强劲势头而具有重要意义，解决了在macOS上进行高效照片和视频搜索的实际需求。它抓住了媒体管理中AI日益增长的趋势，并通过SaaS或API提供具有明确的盈利潜力。 


**项目链接**：https://github.com/allenv0/SCM
**作者**：allenleee
**发布时间**：2026-10-04T09:24:52Z
**挖掘日期**：2026-10-05
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：AI, Image, Video, Search, macOS


## 📌 项目详解

该项目为macOS提供AI照片和视频搜索工具，通过索引每一帧来实现精确搜索。它利用了像CLIP这样的先进AI模型进行图像识别，并利用macOS的Vision框架进行OCR。 该项目因其153个星标和69条评论在Hacker News上的强劲势头而具有重要意义，解决了在macOS上进行高效照片和视频搜索的实际需求。它抓住了媒体管理中AI日益增长的趋势，并通过SaaS或API提供具有明确的盈利潜力。 该项目采用开源许可证，目前处于Beta阶段，部署复杂度适中。它需要一台兼容的Mac硬件配置，可能需要GPU来提高性能。


## 🌐 背景与生态

该项目位于macOS媒体管理工具生态系统中，提供了一种新颖的照片和视频搜索方法。替代方案包括原生macOS工具和第三方应用程序，但该项目通过索引每一帧脱颖而出。


## 💬 社区讨论

社区评论强调了使用Apple的Vision框架进行OCR，选择CLIP等AI模型，以及关于帧采样率和性能优化的讨论。


## 🚀 应用前景

该工具可以解决个人照片管理、专业媒体存档和内容创作工作流程中的实际问题。潜在产品包括用于企业照片搜索的SaaS平台或集成到其他应用程序的API。


## 🔧 技术栈

技术栈包括Python、用于图像识别的CLIP模型、用于OCR的Apple Vision框架以及用于媒体处理的macOS特定API。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、兼容GPU的Mac以及熟悉AI概念。步骤包括克隆存储库、安装依赖项并运行索引脚本。


## 👥 目标用户

目标用户包括需要macOS高级照片和视频搜索功能的个人开发者、媒体专业人士和企业。


## ⚖️ 类似项目对比

竞争项目包括Immich，它提供AI照片和视频搜索但侧重于跨平台方法，以及原生macOS工具如Spotlight。


<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[postalcoder]: Since this is for the mac you really should be using apple&#x27;s vision framework for OCR. It smokes tesseract in both speed and accuracy. Edit: I&#x27;m curious which LLM was used to generate the code. I fed the title of your post to claude&#x2F;deepseek&#x2F;qwen&#x2F;codex asking to recommend a stack for this project, expecting to frown thinking that they still recommend tesseract. However, I found that they all recommend apple&#x27;s vision framework. In fact the latest model to recommen...

[alt227]: Slightly offtopic, but made me wonder. Can you copyright things like this now that LLMs exist? I mean, up until now if a small startup has a great idea they will get bought out by big tech which will integrate (or kill) their tech. But now with LLMs can the likes of OpenAI just tell their model to make something that works similar to X (such as this project) and then get round copying laws and negate being behind the curve? EDIT: switched to the correct spelling of copyright.

[hn3ufz62f7]: Having built something similar with CLIP on an M1, frame sampling rate is the whole ballgame. One frame a second on 12k videos is days, keyframes only got me to an overnight run.

[lucideer]: possibly off-topic, but for anyone interested in this on a more cross-platform &#x2F; holistic basis, Immich does this (&amp; by &quot;this&quot; I mean an approximate AI search for photos &amp; videos - I can&#x27;t account for the &quot;every frame&quot;, nor for the comparative search quality)

[yt1998]: Why chose CLIP to do this. Have you tried small VLMs like Qwen-VL? I believe those models have video encoders can better perform at this scenario.

</details>
