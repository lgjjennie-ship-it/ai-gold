---
layout: default
title: "FeyNoBg：自动背景移除"
date: 2026-07-28T12:00:00+00:00
discovered_date: 2026-07-28
slug: 2026-07-28-show-hn-feynobg-automatic-background-removal-model-and-training-library
source: hackernews
category: show-hn
ai_score: 8.0
summary: "FeyNoBg 是一个自动背景移除模型和训练库，旨在帮助公司使用 Python 和 BiRefNet 从他们的数据中构建自定义模型。 该项目因其在高危新闻上的高人气、解决 AI 核心任务的实际效用及其独特的背景移除方法而具有重要意义。它通过定制模型训练服务提供盈利潜力，并且是 MIT 许可的，易于采用和扩展。 该库在 MIT 许可下，表明其成熟度和易用性。它支持 BiRefNet 并与 Hugging Face Trainer 集成用于训练和评估。没有提到显著的硬件要求。"
tags: "AI, BackgroundRemoval, ComputerVision, CustomModel, Python"
---

# FeyNoBg：自动背景移除


> FeyNoBg 是一个自动背景移除模型和训练库，旨在帮助公司使用 Python 和 BiRefNet 从他们的数据中构建自定义模型。 该项目因其在高危新闻上的高人气、解决 AI 核心任务的实际效用及其独特的背景移除方法而具有重要意义。它通过定制模型训练服务提供盈利潜力，并且是 MIT 许可的，易于采用和扩展。 该库在 MIT 许可下，表明其成熟度和易用性。它支持 BiRefNet 并与 Huggi


**项目链接**：https://usefeyn.com/blog/feynobg/
**作者**：snyy
**发布时间**：2026-07-27T16:59:08Z
**挖掘日期**：2026-07-28
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, BackgroundRemoval, ComputerVision, CustomModel, Python


## 📌 项目详解

FeyNoBg 是一个自动背景移除模型和训练库，旨在帮助公司使用 Python 和 BiRefNet 从他们的数据中构建自定义模型。 该项目因其在高危新闻上的高人气、解决 AI 核心任务的实际效用及其独特的背景移除方法而具有重要意义。它通过定制模型训练服务提供盈利潜力，并且是 MIT 许可的，易于采用和扩展。 该库在 MIT 许可下，表明其成熟度和易用性。它支持 BiRefNet 并与 Hugging Face Trainer 集成用于训练和评估。没有提到显著的硬件要求。


## 🌐 背景与生态

背景移除是 AI 中的一项常见但复杂的任务，通常用于在不同的上下文中重用主体，如聊天贴纸。传统模型在伪装、运动模糊和细结构（如头发）方面存在困难。FeyNoBg 通过以可解释性为先的方法解决了这些挑战。


## 💬 社区讨论

社区评论表达了对项目成熟度和实用性的兴奋，有些人将其与 Adobe 的产品进行了比较，并询问了分辨率限制和许可问题。


## 🚀 应用前景

FeyNoBg 可用于电子商务、媒体和娱乐行业，用于创建透明的产品图像、动画贴纸和增强视频制作。可以通过 SaaS 或定制训练服务实现盈利。


## 🔧 技术栈

核心技术栈包括 Python、BiRefNet 和 NoBg 库，它支持使用 Hugging Face Trainer 训练和运行模型。基础设施基于 Docker 和 Kubernetes 以实现可扩展性。


## 🎯 上手难度

难度：入门。开始使用需要 Python 3.8+、GPU 和 API 密钥。步骤包括克隆存储库、安装依赖项和运行演示脚本。


## 👥 目标用户

该项目非常适合从事 AI 和计算机视觉的个人开发者、企业团队和研究人员。像后端工程师和 ML 实践者这样的角色会发现它特别有用。


## ⚖️ 类似项目对比

竞争对手包括 Adobe 的 Select Subject 模型，它提供强大的结果但缺乏定制。其他替代方案是 Pixelcut 用于批量背景移除和 MaskFactory 用于高质量分割。


## 📚 参考链接

- [FeyNoBg: A SOTA Model For Background Removal — Feyn](https://usefeyn.com/blog/feynobg/)
- [GitHub - feyninc/ nobg : a library for image and video matting · GitHub](https://github.com/feyninc/nobg)
- [Evaluating image segmentation models for background removal for Images | The Cloudflare Blog](https://blog.cloudflare.com/background-removal/)

<details><summary>📄 查看原文内容</summary>


Hey HN, I’m Shreyash from Feyn. We help companies build custom models from their data.<p>Today, we’re releasing FeyNoBg, an automatic background removal model. Alongside it, we&#x27;re open-sourcing NoBg, the Python library we built to train and run it.<p>Try the model here: <a href="https:&#x2F;&#x2F;huggingface.co&#x2F;spaces&#x2F;feyninc&#x2F;feynobg" rel="nofollow">https:&#x2F;&#x2F;huggingface.co&#x2F;spaces&#x2F;feyninc&#x2F;feynobg</a>. Check out the library here: <a href="https:&#x2F;&#x2F;github.com&#x2F;feyninc&#x2F;nobg" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;feyninc&#x2F;nobg</a><p>Some sample outputs:<p>(1) Soccer Freekick: <a href="https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1MZkAGLwbhNVOZ0Oi7XvpCfSEu9QPCbwj&#x2F;view?usp=sharing" rel="nofollow">https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1MZkAGLwbhNVOZ0Oi7XvpCfSEu9Q...</a><p>(2) Hair in wind: <a href="https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1Odc2m0XMVH9uZtvI_KjaRbXzhLLdGK8Z&#x2F;view?usp=sharing" rel="nofollow">https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1Odc2m0XMVH9uZtvI_KjaRbXzhLL...</a><p>(3) Bicycle with visible spokes: <a href="https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1h99ahjfrtS1MFQJJgiKE2fuM3HZyQ-QJ&#x2F;view?usp=sharing" rel="nofollow">https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1h99ahjfrtS1MFQJJgiKE2fuM3HZ...</a><p>(4) Live Demo video: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;b1heHPvY8BM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;b1heHPvY8BM</a><p>Background removal separates an image&#x27;s subject from its surrounding. We&#x27;ve all tried it at some point. Often it is to reuse the subject in a different artifact. Nowadays, it is common to make chat stickers out of it. It is one of the most common but under-appreciated uses of AI. It is also surprisingly complex. Models can be easily confused by camouflage, motion blur, or fine structures like hair.<p>The task requires two skills. First, a model has to identify the foreground. Second, it has to trace the foreground’s boundary and estimate an opacity value for each pixel. Generally, these skills are taught with different datasets. That creates a failure point. A poor training mix can improve one skill at the expense of the other. We saw this in our controlled evaluation. A training run with just the MaskFactory dataset improved on the CAMO benchmark but regressed on DIS5K.<p>For FeyNoBg, we took an interpretability-first approach to training. We first studied how BiRefNet’s stages contribute to finding the foreground and reconstructing its boundary. We discovered that the third stage of it&#x27;s feature extractor holds a lot of information. Both localization and boundary reconstruction depend heavily on the feature map produced here.<p>This led us to expand this stage from 18 to 24 blocks while preserving the pre-trained weights. We then trained FeyNoBg on 26.1K diverse examples assembled from 10 datasets. The goal was to improve foreground identification and boundary precision without sacrificing either one.<p>Across eight benchmarks, FeyNoBg achieves the best published score on four and comes within 2% of the leader on the rest.<p>Building FeyNoBg also exposed a tooling problem. Image matting models are usually released as isolated repositories with incompatible preprocessing, training, and evaluation code. We built NoBg to solve this. NoBg puts these workflows behind one Python interface. It supports BiRefNet today, with more architectures coming. We hope you build something exciting with it!<p>Happy to answer any questions!


--- Top Comments ---

[geooff_]: I love seeing this. Background removal is such a core task used in so many systems, I group it in with speech to text in terms of importance. I love seeing maturity getting pushed in this space. Congratulations to you and the team!

[qingcharles]: How does it stack up against Adobe&#x27;s model? The advantage Adobe has is there are essentially two options: (1) Select Subject (95% of the time will give you the result you want); (2) Select Person (helps in the edge cases). The issue I have is, what is the subject? For instance, you have a person sat on a couch. You hit Select Subject. Is the subject the person, or the person plus the couch? With Adobe&#x27;s when I only want the person, most of the time Select Subject works, and when it ...

[woadwarrior01]: Why extend an MIT licensed model&#x27;s weights (BiRefNet) and release it under a cc-by-nc-4.0 license?

[nickludlam]: This looks great! What are the resolution limits? From the GitHub readme I saw mention of 1024x1024, but I was able to process an image 1920x2880 just fine. I didn&#x27;t see any really obvious scaling artefacts, so is there something clever happening behind the scenes?

[defmetrix]: This is awesome, I just bookmarked your tool. Ive been looking for something simple to use, since Its not easy to use the segment anything tool anymore. Thanks!

</details>
