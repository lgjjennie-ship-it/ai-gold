---
layout: default
title: "Nari Qwen3-TTS和ASR：开源语音模型"
date: 2026-09-15T12:00:00+00:00
discovered_date: 2026-09-15
slug: 2026-09-15-show-hn-nari-qwen3-tts-and-qwen3-asr-high-accuracy-low-latency-and-cost
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Nari Qwen3-TTS和Qwen3-ASR是具有高精度、低延迟和低成本的开放源语音模型，旨在与闭源模型竞争。 该项目现在值得关注，因其高人气（81个参与评分，28条评论）及其通过低延迟和低成本解决TTS市场痛点的方案，显示出通过SaaS或API进行货币化的潜力。 这些模型采用开放许可证，成熟度高，部署复杂度低。它们对硬件要求不高，并能很好地与现有系统集成。"
tags: "TTS, ASR, Voice, AI, Inference"
---

# Nari Qwen3-TTS和ASR：开源语音模型


> Nari Qwen3-TTS和Qwen3-ASR是具有高精度、低延迟和低成本的开放源语音模型，旨在与闭源模型竞争。 该项目现在值得关注，因其高人气（81个参与评分，28条评论）及其通过低延迟和低成本解决TTS市场痛点的方案，显示出通过SaaS或API进行货币化的潜力。 这些模型采用开放许可证，成熟度高，部署复杂度低。它们对硬件要求不高，并能很好地与现有系统集成。


**项目链接**：https://narilabs.com/blog/nari-labs-leads-coval-voice-ai-benchmarks/
**作者**：toebee
**发布时间**：2026-09-14T16:07:58Z
**挖掘日期**：2026-09-15
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：TTS, ASR, Voice, AI, Inference


## 📌 项目详解

Nari Qwen3-TTS和Qwen3-ASR是具有高精度、低延迟和低成本的开放源语音模型，旨在与闭源模型竞争。 该项目现在值得关注，因其高人气（81个参与评分，28条评论）及其通过低延迟和低成本解决TTS市场痛点的方案，显示出通过SaaS或API进行货币化的潜力。 这些模型采用开放许可证，成熟度高，部署复杂度低。它们对硬件要求不高，并能很好地与现有系统集成。


## 🌐 背景与生态

语音模型市场由闭源模型主导，但Nari Labs旨在通过提供高质量、低成本和快速的开放源替代方案来改变这一现状。


## 💬 社区讨论

社区评论积极，人们对模型的性能及其推动音频帕累托前沿的潜力表示兴奋。


## 🚀 应用前景

这些模型可以通过提供具有成本效益和高质量TTS和ASR解决方案来为各行业解决实际问题，具有通过SaaS或API进行货币化的潜力。


## 🔧 技术栈

技术栈包括Python、专为Qwen3-TTS和Qwen3-ASR设计的专用推理引擎，以及Docker和K8s等基础设施。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+版本、GPU和API密钥。大致步骤包括克隆存储库并按照设置说明进行操作。


## 👥 目标用户

目标用户包括医疗保健、教育和客户服务等行业的个人开发者、企业团队和研究人员。


## ⚖️ 类似项目对比

竞争对手包括Darwin TTS和ElevenLabs。Nari Qwen3-TTS和ASR的区别在于更具成本效益，并专为推理进行了优化。


## 📚 参考链接

- [Qwen3-TTS is an open-source series of TTS models developed ... - GitHub](https://github.com/QwenLM/Qwen3-TTS)
- [GitHub - QwenLM/Qwen3-ASR: Qwen3-ASR is an open-source series ...](https://github.com/QwenLM/Qwen3-ASR)

<details><summary>📄 查看原文内容</summary>


Hey HN, Toby from Nari Labs here.<p>We&#x27;ve been working on making OSS speech models super-fast. Last year, we built Dia, the first OSS text-to-speech model capable of doing natural dialogue. Since then, so many more great speech models have been released to the public.<p>But the market is still dominated by closed source models. We think that&#x27;s an inference problem. Existing systems such as vLLM &#x2F; SGLang are not well suited for multimodal inference. To prove this, we built an inference engine specialized for Qwen3-TTS and open-sourced it (<a href="https:&#x2F;&#x2F;github.com&#x2F;nari-labs&#x2F;nari-qwen3-tts" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;nari-labs&#x2F;nari-qwen3-tts</a>). Running at sub-50 ms latency at 10 RPS, this showed open models can be run much faster and cheaper.<p>Since then, we&#x27;ve been working hard to bring cheap, fast, and high quality serving to all. And we&#x27;ve even beat closed models at their game!<p>Measured on the highly cited Coval (YC S24) voice AI benchmarks, our Qwen3-TTS endpoint not just is #2 in latency, but #1 in accuracy (WER) compared to 11Labs, Cartesia etc. while being the cheapest endpoint. Our Qwen3-ASR endpoint has the lowest latency and #2 accuracy, just 0.1% away from #1. It is the second cheapest model on the list.<p>It took a lot of clever inference engineering to make these models quick, perform well while keeping costs low. Interestingly, Alibaba&#x27;s official endpoints seem to perform worse in terms of accuracy and latency compared to ours. But nonetheless, much love to the Qwen team for OSS-ing these amazing speech models.<p>We want to continue to push prices down to make speech technology a commodity - so that every app can have great TTS and STT without worrying about unit costs. We&#x27;re also working on other parts of audio such as diarization - as well as video and world model inference. More to come!


--- Top Comments ---

[karimf]: This is awesome. Thanks for pushing the audio pareto frontier forward. Probably far fetched for now, but I think the next big evolution is building the pareto&#x2F;much cheaper alternative to GPT-Live-1. The STT&#x2F;TTS market is quite saturated, while today, there&#x27;s almost no cheap&#x2F;open source alternative to GPT-Live-1.

[asaiacai]: This is really cool work! I&#x27;m curious like what do you see as the biggest lever for speeding up TTS models or from a technical perspective that this was a promising direction in the first place to push on. If I were to guess, some distillation but I&#x27;m certain there are probably TTS model aware architectural changes that just make inference wayyyy faster?

[apimade]: https:&#x2F;&#x2F;apimade.com&#x2F;audio-compare.html  Added it to my blind TTS model comparison leaderboard. So far Darwin TTS is the open model leading the pack, ElevenLabs is at the lead.

[konart]: All TTS generations are too fast. It&#x27;s almost I&#x27;m listening to a podcast on 1.25-1.5x speed.

[rahimnathwani]: For some reason it switched voices half way through a 33 second clip. For OP the clip name is nari-nina-01a0a12f-980a-765e-8029-fa56bd23210d.wav

</details>
