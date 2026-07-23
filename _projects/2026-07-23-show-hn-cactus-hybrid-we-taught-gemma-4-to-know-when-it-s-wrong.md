---
layout: default
title: "Cactus Hybrid：教会模型自我认知"
date: 2026-07-23T12:00:00+00:00
discovered_date: 2026-07-23
slug: 2026-07-23-show-hn-cactus-hybrid-we-taught-gemma-4-to-know-when-it-s-wrong
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Cactus Hybrid 对 Gemma 4 E2B 进行后训练，使其能够评估自身准确性，并为响应提供 0 到 1 之间的置信度分数。开发者可以根据这些分数路由查询，优化性能和成本。 该项目因其强大的影响力（106 星，14 条评论）和独特的设备上模型准确性方法而具有重要意义。它解决了不可靠的自我评估方法的痛点，并与混合 AI 解决方案的趋势相符，提供了明确的盈利潜力。 该项目根据 MIT 协议许可，Gemma 模型的使用受其条款约束。它已达到生产成熟度，部署复杂性取决于底层基础设施。探测层几乎不增加额外开销。"
tags: "AI, Model, Accuracy, Confidence, Hybrid"
---

# Cactus Hybrid：教会模型自我认知


> Cactus Hybrid 对 Gemma 4 E2B 进行后训练，使其能够评估自身准确性，并为响应提供 0 到 1 之间的置信度分数。开发者可以根据这些分数路由查询，优化性能和成本。 该项目因其强大的影响力（106 星，14 条评论）和独特的设备上模型准确性方法而具有重要意义。它解决了不可靠的自我评估方法的痛点，并与混合 AI 解决方案的趋势相符，提供了明确的盈利潜力。 该项目根据 MIT 协议


**项目链接**：https://github.com/cactus-compute/cactus-hybrid
**作者**：HenryNdubuaku
**发布时间**：2026-07-22T17:56:29Z
**挖掘日期**：2026-07-23
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Model, Accuracy, Confidence, Hybrid


## 📌 项目详解

Cactus Hybrid 对 Gemma 4 E2B 进行后训练，使其能够评估自身准确性，并为响应提供 0 到 1 之间的置信度分数。开发者可以根据这些分数路由查询，优化性能和成本。 该项目因其强大的影响力（106 星，14 条评论）和独特的设备上模型准确性方法而具有重要意义。它解决了不可靠的自我评估方法的痛点，并与混合 AI 解决方案的趋势相符，提供了明确的盈利潜力。 该项目根据 MIT 协议许可，Gemma 模型的使用受其条款约束。它已达到生产成熟度，部署复杂性取决于底层基础设施。探测层几乎不增加额外开销。


## 🌐 背景与生态

像 Gemma 4 这样的设备上模型速度快且私密，但准确性不足。混合 AI 解决方案结合设备上和云模型以平衡性能和成本。Cactus Hybrid 利用隐藏状态信号来提高模型的自意识。


## 💬 社区讨论

社区评论强调了创新的方法，并要求进一步澄清置信度评分机制。一些人表示怀疑，认为模型无法真正评估自身的准确性。


## 🚀 应用前景

这项技术可应用于对设备上准确性要求较高的场景，如移动 AI 应用、隐私敏感行业和实时决策系统。潜在产品包括 AI 驱动的聊天机器人和虚拟助手。


## 🔧 技术栈

核心技术栈包括 Gemma 4 E2B、一个带有 LayerNorm、低秩投影、注意力池化和一个小 MLP 头的 68k 参数探测层。基础设施依赖于 Transformer、MLX、Llama.cpp 和 Cactus。


## 🎯 上手难度

难度：进阶。前提条件包括 Python 3.8+、GPU 和对 Gemma 模型的访问权限。步骤包括克隆存储库、安装依赖项并运行提供的脚本。


## 👥 目标用户

目标用户包括医疗保健、金融和技术等行业中的后端工程师、ML 实践者和 DevOps 团队。


## ⚖️ 类似项目对比

竞争对手包括专注于模型可解释性的 Goodfire 的 RLFR，以及像 olafura 的 gemma-4-mic-transcribe 这样的项目，它们集成了类似的准确性评估技术。


## 📚 参考链接

- [Gemma 4](https://en.wikipedia.org/wiki/Gemma_4)
- [Gemma 4 — Google DeepMind](https://deepmind.google/models/gemma/gemma-4/)

<details><summary>📄 查看原文内容</summary>


Hey HN, Henry &amp; Roman here from Cactus.<p>A small, on-device model is fast and private, but sometimes wrong, but frontier models are getting expensive pretty fast. So, we post-trained Gemma 4 E2B post-trained to know when it&#x27;s wrong. Every response comes with a confidence score between 0 and 1. Developers can accept the on-device when it&#x27;s high, hand off to a bigger cloud model when it&#x27;s low. By routing only 15-35% of queries to Gemini 3.1 Flash-Lite, Gemma-4-E2B matches Gemini 3.1 Flash-Lite on most benchmarks.<p>- ChartQA: 15-20%<p>- LibriSpeech: 25-30%<p>- MMBench, GigaSpeech, MMAU: 30-35%<p>- MMLU-Pro: 45-55%<p>We were always frustrated by the routing signals hybrid apps rely on: asking the model to rate itself in text (unreliable, and you&#x27;re parsing prose), or token entropy heuristics (barely better than a coin flip in our tests). So we did mechanistic studies on small models, Gemma 4 particularly, and found the hidden state for different layers carry meaningful self-awareness signal for various situations.<p>SO we extended the model with a 68k params probe layer (LayerNorm, low-rank projection, attention pooling, small MLP head) reads one intermediate layer during decoding and predicts p(wrong); confidence = 1 - p(wrong), returned as structured data, never parsed out of the answer text.<p>Across 12 hold-out benchmarks spanning text, vision and audio, the probe averages 0.814 AUROC vs 0.549 for token entropy. The result that convinced us this is real: the probe was trained on zero audio data, yet scores 0.79-0.88 AUROC on four audio benchmarks where entropy is near-random or worse (0.32-0.52). It&#x27;s reading a modality-independent correctness signal from the hidden state, not memorizing patterns from its training data.<p>We published all weights on HuggingFace and provide copy-pase codes to run it on Transformers, MLX, Llama.cpp or Cactus. With Ollama, vLLM, SGLang etc in the works. For llama.cpp we ship a patch series you compile in once (upstreaming is planned). The code is MIT licensed; Gemma model use remains subject to the Gemma terms.<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;cactus-compute&#x2F;cactus-hybrid" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;cactus-compute&#x2F;cactus-hybrid</a><p>Weights: <a href="https:&#x2F;&#x2F;huggingface.co&#x2F;collections&#x2F;Cactus-Compute&#x2F;cactus-hybrid-6a60da4551074db058e8bb64" rel="nofollow">https:&#x2F;&#x2F;huggingface.co&#x2F;collections&#x2F;Cactus-Compute&#x2F;cactus-hyb...</a><p>Some caveats:<p>- The probe scores single-sequence decoding only, up to the first 1024 generated tokens.<p>- Handoff works best when routing per task in a multi-step process, not per step.<p>- Hierarchical routing is still in the works: try on-device, then DeepSeek v4 Flash, before Fable&#x2F;GPT5.5&#x2F;Gemini&#x2F;Muse&#x2F;Grok.<p>- The technique is boutique for each model, we will share each weights as they roll out.<p>These issues are currently being tackled at Cactus and updated weights will be shipped directly into the HuggingFace collection and GitHub repository straight up. Please let us know your thoughts, it helps us find ways to improve the design progressively.<p>Thanks a million!


--- Top Comments ---

[BugsJustFindMe]: &gt;  &quot;post-trained to know when it&#x27;s wrong&quot;  Is it also post-trained to know when it&#x27;s wrong about when it&#x27;s wrong? &gt;  &quot;Every response comes with a confidence score between 0 and 1&quot;  How confident is it in its confidence? Please, I&#x27;m sure that what you&#x27;re doing is very neat and useful, but use other language to describe it. I beg you. You can&#x27;t know when you&#x27;re wrong. You can only know when you&#x27;re unsure or inconsistent. You can ...

[mncharity]: &gt;  the hidden state for different layers carry meaningful self-awareness signal for various situations. Is it plausible to wonder if some developer judgement feels, like maybe &quot;the code I just wrote is clean&#x2F;crufty&quot;, or &quot;things came together smoothly&#x2F;janky&quot;, might have extractable signals in some models? If so, might one create a shopping list of desired signals to check for in a model, as with activation steering concepts, where one checks whether and how har...

[astrobiased]: Is this in any way similar to Goodfire&#x27;s work?  https:&#x2F;&#x2F;www.goodfire.ai&#x2F;research&#x2F;rlfr#

[olafura]: Was actually pulling on a similar thread as I saw announcement so I integrated it just for fun. Have been only running this on my Framework Desktop but should be runnable elsewhere
 https:&#x2F;&#x2F;github.com&#x2F;olafura&#x2F;gemma-4-mic-transcribe

[cacio-e-pepe]: &gt; So we did mechanistic studies on small models, Gemma 4 particularly, and found the hidden state for different layers carry meaningful self-awareness signal for various situations. Neat! Just to make sure I understand - you trained your probe layer to take this hidden state and predict p(wrong)? Curious to learn more. Any more info on your approach (esp the mechanistic study)?

</details>
