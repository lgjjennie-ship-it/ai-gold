---
layout: default
title: "Beam：通用型开源权重AI模型"
date: 2026-10-06T12:00:00+00:00
discovered_date: 2026-10-06
slug: 2026-10-06-beam-reflection-s-501b-open-weight-model
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Beam是由Reflection开发的开源权重AI模型，采用稀疏专家混合架构，拥有5010亿总参数和230亿活跃参数，旨在通用化并解决复杂谜题。 Beam获得467个星标和148条评论，显示出适度的社区兴趣。它解决了AI中开源权重模型的需求，并在“陆地或水域泛化实验”中展示了新颖的方法。 Beam采用开源权重模型许可，表明权重可下载和使用。该模型已投入生产，但部署复杂性可能因硬件要求而异。"
tags: "AI, Model, Open-Weight, Generalization, Puzzle"
---

# Beam：通用型开源权重AI模型


> Beam是由Reflection开发的开源权重AI模型，采用稀疏专家混合架构，拥有5010亿总参数和230亿活跃参数，旨在通用化并解决复杂谜题。 Beam获得467个星标和148条评论，显示出适度的社区兴趣。它解决了AI中开源权重模型的需求，并在“陆地或水域泛化实验”中展示了新颖的方法。 Beam采用开源权重模型许可，表明权重可下载和使用。该模型已投入生产，但部署复杂性可能因硬件要求而异。


**项目链接**：https://reflection.ai/blog/introducing-beam
**作者**：Philpax
**发布时间**：2026-10-05T19:16:35Z
**挖掘日期**：2026-10-06
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：AI, Model, Open-Weight, Generalization, Puzzle


## 📌 项目详解

Beam是由Reflection开发的开源权重AI模型，采用稀疏专家混合架构，拥有5010亿总参数和230亿活跃参数，旨在通用化并解决复杂谜题。 Beam获得467个星标和148条评论，显示出适度的社区兴趣。它解决了AI中开源权重模型的需求，并在“陆地或水域泛化实验”中展示了新颖的方法。 Beam采用开源权重模型许可，表明权重可下载和使用。该模型已投入生产，但部署复杂性可能因硬件要求而异。


## 🌐 背景与生态

开源权重模型正日益受到关注，因为它们允许用户访问和修改训练好的模型权重，从而促进创新。Reflection是一家专注于开发高级AI模型的公司，Beam是他们的最新开源产品。


## 💬 社区讨论

社区评论对模型的能力和泛化性能表示兴趣，一些人强调了模型背后组织的重要性，其他人则提到了发布的时间。


## 🚀 应用前景

Beam可应用于需要复杂推理和泛化的场景，如编码辅助、谜题解决和代理工作负载。其盈利潜力在于为开发者和企业提供的SaaS或API服务。


## 🔧 技术栈

Beam采用稀疏专家混合模型，拥有5010亿总参数和230亿活跃参数。它在2380万亿多样标记上进行预训练，并用于编码、推理和代理工作负载。


## 🎯 上手难度

使用Beam的难度评级为进阶。前提条件包括Python 3.8+、GPU和模型权重访问权限。初始步骤包括克隆仓库、安装依赖项并运行示例脚本。


## 👥 目标用户

Beam面向后端工程师、ML从业者以及从事编码、推理和代理AI任务的研究人员。它特别适用于希望利用开源权重模型进行创新的组织。


## ⚖️ 类似项目对比

竞品包括OpenAI的GPT-4，它提供类似的泛化能力但不是开源权重。其他替代方案是EleutherAI的GPT-Neo和GPT-J，它们是开源权重但可能在性能上有所不同。


## 📚 参考链接

- [Open - Weight AI Models Explained | In Simple Terms with... | LinkedIn](https://www.linkedin.com/posts/in-simple-terms-with-satish_what-is-an-open-weight-ai-model-open-weights-activity-7487542745708814336-8tqk)
- [Comparison of AI Models across Intelligence... | Artificial Analysis](https://artificialanalysis.ai/models)
- [What Is Open Wheight Ai | TikTok](https://www.tiktok.com/discover/what-is-open-wheight-ai)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[berkes]: What kind of company or organization is Reflection? I think it is ever more important to realize  who  is releasing models rather than what the models do and how they compare. Because models iterate at breakneck speed, looking at today&#x27;s benchmarks is only useful for someone  using  the models today. Whereas if one builds a product on top of it, or commits to one for a project or team, the company or organization behind it, is far more important. Will they exist in a few months? Do they ...

[Ariarule]: Always glad to see more open-weight models, but this caption on the 2nd demo image had me do a double-take: &quot;Land or Water Generalization Experiment: We recreated the viral X puzzle by asking Beam to create a fixed 180×90 grid for longitudes -179° to 179° and latitudes -89° to 89°, with 16,200 points. This puzzle is a few days old, so could not appear in the training data, thus testing the model’s generalization. Beam gets 95.5% coverage right, putting us between Opus 5 (92.5%) and Fable...

[springtimesun]: I feel like this is a marketing miss. If they had held their announcement until the model was released, I would have grabbed it and started running it through my benchmarks. It probably doesn’t get a place in the rotation based on their own description of its performance, but now the weights live on the server, I’m probably following them on HF and I will remember to check in every time I ls the models folder. With the announcement only, none of that happens and I’m likely to forget about thi...

[htrp]: &gt; Beam is a sparse Mixture-of-Experts model with 501 billion total parameters, 23 billion active, built for coding, reasoning, and agentic workloads. &gt; Beam’s capabilities come from major investments in both pretraining and reinforcement learning (RL). We pretrained the model on 23.8 trillion diverse, curated, high-quality tokens from the web and proprietary licensed datasets, matching or outperforming available similar-sized open base models. In parallel, we developed the algorithms, t...

[wren6991]: I thought it would be interesting to look at some key figures vs another contemporary model in the same weight class (DeepSeek V4.1 Flash)                                   DS V4.1F            Beam
    LM total params             552B                501B
    LM active params (prefill)  8B                  23B
    LM active params (decode)   16B                 23B
    N-gram&#x2F;PLE params           196B                0
    Pretrain tokens             45T                 28T
    Disk KV byt...

</details>
