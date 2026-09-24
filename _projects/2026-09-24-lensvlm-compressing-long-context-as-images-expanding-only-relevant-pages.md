---
layout: default
title: "LensVLM：基于图像的AI上下文压缩"
date: 2026-09-24T12:00:00+00:00
discovered_date: 2026-09-24
slug: 2026-09-24-lensvlm-compressing-long-context-as-images-expanding-only-relevant-pages
source: hackernews
category: show-hn
ai_score: 8.0
summary: "LensVLM将长上下文压缩成图像，并使用90亿参数的视觉语言模型仅聚焦于相关页面进行AI处理。 LensVLM在Hacker News上获得7条评论和75分，显示出社区兴趣。它提供了一种将长上下文压缩成图像的新方法，对LLM具有实用价值，并可能通过SaaS或API实现商业化。 LensVLM采用Apache 2.0许可证，处于Beta阶段，部署复杂度适中。它需要GPU进行处理，并与视觉语言模型集成。"
tags: "LLM, Image, Context, AI, Compression"
---

# LensVLM：基于图像的AI上下文压缩


> LensVLM将长上下文压缩成图像，并使用90亿参数的视觉语言模型仅聚焦于相关页面进行AI处理。 LensVLM在Hacker News上获得7条评论和75分，显示出社区兴趣。它提供了一种将长上下文压缩成图像的新方法，对LLM具有实用价值，并可能通过SaaS或API实现商业化。 LensVLM采用Apache 2.0许可证，处于Beta阶段，部署复杂度适中。它需要GPU进行处理，并与视觉语言模型集


**项目链接**：https://huggingface.co/apple/LensVLM-9B
**作者**：victormustar
**发布时间**：2026-09-23T18:36:29Z
**挖掘日期**：2026-09-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Image, Context, AI, Compression


## 📌 项目详解

LensVLM将长上下文压缩成图像，并使用90亿参数的视觉语言模型仅聚焦于相关页面进行AI处理。 LensVLM在Hacker News上获得7条评论和75分，显示出社区兴趣。它提供了一种将长上下文压缩成图像的新方法，对LLM具有实用价值，并可能通过SaaS或API实现商业化。 LensVLM采用Apache 2.0许可证，处于Beta阶段，部署复杂度适中。它需要GPU进行处理，并与视觉语言模型集成。


## 🌐 背景与生态

LensVLM解决了AI模型中处理长上下文的挑战，这是一个随着LLM处理更多数据而日益突出的痛点。近年来，视觉语言模型的进步使得上下文压缩更加高效。


## 💬 社区讨论

社区评论强调了其创新方法，并建议改进方向，如排列不变的KV缓存排序。有人将其与现有解决方案Snap compact进行比较。


## 🚀 应用前景

LensVLM可以通过减少上下文大小解决金融和医疗等数据密集型行业的实际问题。潜在产品包括用于AI驱动文档分析的SaaS平台。


## 🔧 技术栈

LensVLM使用Python、PyTorch和90亿参数的视觉语言模型。它依赖Docker进行部署，并与视觉语言模型集成。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、GPU和API密钥。步骤涉及克隆仓库、安装依赖项和运行示例脚本。


## 👥 目标用户

目标用户是金融和医疗等行业的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Oh My Pi的Snap compact和DeepSeek-OCR。LensVLM的区别在于其聚焦于基于图像的压缩和选择性扩展。


## 📚 参考链接

- [GitHub - apple-aiml-research/ml- lensvlm : Official code for LensVLM ...](https://github.com/apple-aiml-research/ml-lensvlm)
- [[2605.07019] LensVLM : Selective Context Expansion for Compressed...](https://arxiv.org/abs/2605.07019)
- [DeepSeek-OCR: How Optical Compression Redefines Long Context](https://intuitionlabs.ai/articles/deepseek-ocr-optical-compression)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[rao-v]: I really like this approach! I sort of think of the vision encoder here as an expensive high fidelity RAG encoder. The thing I’d love to do with a system like this is train it to be KV cache ordering independent (ie permutation invariant at the page level). Basically each page’s KV cache should be understandable by the model in any ordering - which would allow you to go one step further and treat the KV cache of the vision encoded page as the  chunk  for the model to reason over. Then all the...

[taylorfinley]: Oh My Pi has done this for a while now, they call it Snap compact.

[himata4113]: I always found it weird that we don&#x27;t have glacial type input for llms or any kind of active-working memory. There&#x27;s no reason why we shouldn&#x27;t be able to expose active relevant information that is only relevant for the next request: current agents running, time, etc. There&#x27;s also no reason why we shouldn&#x27;t have a cheaper lossy input which uses way less bytes per token - see deepseek flash 4.1.

[lathoa]: Interesting approach. thanks

</details>
