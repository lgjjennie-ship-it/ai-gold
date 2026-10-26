---
layout: default
title: "老旧CNN在皮肤癌诊断中胜过新式LLM"
date: 2026-10-26T12:00:00+00:00
discovered_date: 2026-10-26
slug: 2026-10-26-a-10-year-old-cnn-outperforms-frontier-llms-for-skin-cancer-diagnosis
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目显示，一个10岁的老旧CNN在诊断皮肤癌方面胜过前沿LLM，使用在皮肤镜图像上微调的Inception v3模型。 它在Hacker News上获得551个星和237条评论的关注，通过新颖的CNN与LLM比较来解决关键医疗问题，可能带来专业医疗诊断的货币化。 项目在宽松的许可证下，处于生产成熟度，部署需要一个H100 GPU，并专注于皮肤癌诊断的集成点。"
tags: "AI, Healthcare, CNN, Skin Cancer, Medical Diagnostics"
---

# 老旧CNN在皮肤癌诊断中胜过新式LLM


> 该项目显示，一个10岁的老旧CNN在诊断皮肤癌方面胜过前沿LLM，使用在皮肤镜图像上微调的Inception v3模型。 它在Hacker News上获得551个星和237条评论的关注，通过新颖的CNN与LLM比较来解决关键医疗问题，可能带来专业医疗诊断的货币化。 项目在宽松的许可证下，处于生产成熟度，部署需要一个H100 GPU，并专注于皮肤癌诊断的集成点。


**项目链接**：https://lynchlab.net/llm-skin-cancer
**作者**：sungam
**发布时间**：2026-10-25T17:15:38Z
**挖掘日期**：2026-10-26
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Healthcare, CNN, Skin Cancer, Medical Diagnostics


## 📌 项目详解

该项目显示，一个10岁的老旧CNN在诊断皮肤癌方面胜过前沿LLM，使用在皮肤镜图像上微调的Inception v3模型。 它在Hacker News上获得551个星和237条评论的关注，通过新颖的CNN与LLM比较来解决关键医疗问题，可能带来专业医疗诊断的货币化。 项目在宽松的许可证下，处于生产成熟度，部署需要一个H100 GPU，并专注于皮肤癌诊断的集成点。


## 🌐 背景与生态

卷积神经网络（CNN）长期以来一直是图像分类的标准，而大型语言模型（LLMs）正作为多用途工具出现。该项目探索了在医学图像分析中，一个专门的CNN可能胜过通用LLM的领域。


## 💬 社区讨论

评论从质疑LLM在医学诊断中的适用性到对CNN性能的惊讶不等，讨论了基准测试和实际应用。


## 🚀 应用前景

这可能彻底改变诊所和皮肤科诊所的皮肤癌筛查，提供一种经济高效、高精度的解决方案。潜在行业包括医疗保健、远程医疗和个人健康监测。


## 🔧 技术栈

技术栈包括Python、在ImageNet上预训练的Inception v3、TensorFlow/PyTorch，以及用于训练和推理的H100 GPU。


## 🎯 上手难度

难度：进阶。需要Python 3.7+、带CUDA的GPU、ISIC存档访问，以及在皮肤镜图像上微调Inception v3。


## 👥 目标用户

目标用户是医疗专业人员、皮肤科医生和寻求准确、可扩展皮肤癌诊断工具的医疗科技公司。


## ⚖️ 类似项目对比

竞争对手包括使用先进CNN进行病变检测的专门医疗图像AI工具，如DermAI和AI-Powered Dermoscopy，但缺乏直接的LLM比较。


## 📚 参考链接

- [Convolutional neural network - Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [Frontier Large Language Models - emergentmind.com](https://www.emergentmind.com/topics/frontier-large-language-models-llms)
- [Best LLMs in 2026: Top Large Language Models Ranked](https://aiintelreport.com/frontier-models/best-llms-2026)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[snitty]: This is an example of why I&#x27;m a little stumped about why people are excited about Jev-style decision models. For any application at scale it&#x27;d be way more accurate to have a dedicated classifier using the right architecture (neural net, bayesian, etc.) LLMs drive the cost of making those models down to near zero. Just use the LLM to make a thing that&#x27;s actually good at what you need it to do.

[vintermann]: This is not surprising, since the model is just given one piece of information and it&#x27;s the piece of information the CNN has been trained to make its whole decision on. I&#x27;m not a dermatologist, but I imagine they don&#x27;t make their decisions on one image alone (and the decision probably isn&#x27;t &quot;is this cancer&quot; but &quot;should we take a biopsy&quot;). The LLM can take into account additional information such as the patient&#x27;s age, occupational exposure and medic...

[tasuki]: &gt; I compared to a 10-year old CNN and to my surprise found that this was superior. I&#x27;m surprised he&#x27;s surprised. &gt; A small, old, specialised network using an outdated architecture recognises skin lesions far better than two frontier LLMs. Yes of course. A 30m params Katago network with one playout is superhuman in playing go, while frontier LLMs have over 10,000 times more parameters and aren&#x27;t any good at playing go. They&#x27;re good at other things (such as helping you...

[Legend2440]: &gt; I used Inception v3 pretrained on everyday photographs and then fine-tuned all layers on 68,011 dermoscopic and clinical images from the ISIC Archive on a single H100 GPU. &gt;These 200 test lesions, and every other photograph of the same lesion or patient, were removed from its data (including the validation set) before training, so it had never seen them, and they were not used to choose the model or set its threshold. This is just benchmaxxing. A benchmaxxed model will always beat an ...

[MitPitt]: And a calculator outperforms LLMs at multiplication and division...

</details>
