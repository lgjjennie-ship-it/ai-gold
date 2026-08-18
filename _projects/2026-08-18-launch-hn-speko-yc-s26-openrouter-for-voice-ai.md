---
layout: default
title: "Speko：语音AI的开放路由器"
date: 2026-08-18T12:00:00+00:00
discovered_date: 2026-08-18
slug: 2026-08-18-launch-hn-speko-yc-s26-openrouter-for-voice-ai
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Speko通过API为语音AI应用优化语音识别、大型语言模型和语音合成模型的组合，根据用户约束选择最佳模型堆栈。 Speko通过提供清晰高效的解决方案，解决了集成多个AI模型的痛点，并在Hacker News上获得高关注度，表明市场需求强烈，并通过API或SaaS具有明确的盈利潜力。 Speko采用MIT许可证，目前处于生产成熟阶段，部署复杂度适中。除了标准计算资源外，没有特定的硬件要求，但需要互联网连接。"
tags: "Voice AI, LLM, Text-to-Speech, Speech-to-Text, AI Integration"
---

# Speko：语音AI的开放路由器


> Speko通过API为语音AI应用优化语音识别、大型语言模型和语音合成模型的组合，根据用户约束选择最佳模型堆栈。 Speko通过提供清晰高效的解决方案，解决了集成多个AI模型的痛点，并在Hacker News上获得高关注度，表明市场需求强烈，并通过API或SaaS具有明确的盈利潜力。 Speko采用MIT许可证，目前处于生产成熟阶段，部署复杂度适中。除了标准计算资源外，没有特定的硬件要求，但需要互


**项目链接**：https://speko.ai/
**作者**：abdik
**发布时间**：2026-08-17T15:36:18Z
**挖掘日期**：2026-08-18
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：Voice AI, LLM, Text-to-Speech, Speech-to-Text, AI Integration


## 📌 项目详解

Speko通过API为语音AI应用优化语音识别、大型语言模型和语音合成模型的组合，根据用户约束选择最佳模型堆栈。 Speko通过提供清晰高效的解决方案，解决了集成多个AI模型的痛点，并在Hacker News上获得高关注度，表明市场需求强烈，并通过API或SaaS具有明确的盈利潜力。 Speko采用MIT许可证，目前处于生产成熟阶段，部署复杂度适中。除了标准计算资源外，没有特定的硬件要求，但需要互联网连接。


## 🌐 背景与生态

语音AI正在快速发展，语音识别、大型语言模型和语音合成模型变得越来越复杂。Speko通过简化选择和集成这些模型的过程，填补了市场上的空白，而之前这曾是一项耗时且复杂的任务。


## 💬 社区讨论

社区评论对Speko简化语音AI开发的能力及其改善现有语音代理的潜力表示强烈兴趣。一些用户对其基准测试方法和集成能力感到好奇。


## 🚀 应用前景

Speko可应用于客服、医疗和教育等行业，以增强基于语音的交互。其API和SaaS模式通过订阅计划或按使用付费提供可扩展的盈利机会。


## 🔧 技术栈

Speko使用的技术栈包括Python、RESTful API，并与主要的语音识别、大型语言模型和语音合成提供商集成。它利用Docker进行容器化，并使用Kubernetes进行编排。


## 🎯 上手难度

使用Speko的难度评级为进阶。前提条件包括Python 3.7+、Docker以及来自语音识别和语音合成提供商的API密钥。基本步骤包括设置环境、配置API并运行测试请求。


## 👥 目标用户

Speko的目标用户是从事语音AI的个人开发者、企业团队和研究人员。它特别适用于电信和医疗等行业中的后端工程师、机器学习实践者和DevOps团队。


## ⚖️ 类似项目对比

竞争对手包括IBM Watson Assistant、Google Cloud Speech-to-Text和Amazon Transcribe。Speko通过提供更简化和自动化的模型选择和集成方法而有所不同。


## 📚 参考链接

- [What is Speech To Text? | IBM](https://www.ibm.com/think/topics/speech-to-text)
- [Choosing the Best LLM for Your AI Voice Agents | Retell AI](https://www.retellai.com/blog/choosing-the-best-llm-for-your-voice-ai-agents)
- [Speech LLMs Explained: The Technology Powering Voice AI Agents | Bluejay](https://getbluejay.ai/resources/speech-llms-explained)

<details><summary>📄 查看原文内容</summary>


Hi HN! I&#x27;m Bek, founder of Speko, a platform that finds an optimal combination of speech-to-text, LLM, and text-to-speech models, given your constraints, among all our public benchmarked options, and tells you why.<p>Demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=no2LY2gRh-c" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=no2LY2gRh-c</a><p>Typical production voice agent is an ensemble of three models: STT, an LLM, and TTS.<p>Each of those layers offers a dozen credible vendors, and each month there are new models on the market. Almost everyone evaluates once, picks a stack of their choice, and never rechecks because switching from a vendor to another involves yet another integration and arguments about the numbers.<p>The result is that you use voice agents running last quarter&#x27;s models while better and cheaper options are available.<p>Before founding Speko, I spent four years as cofounder and CTO building voice agents for enterprises across Asia in 10+ languages. Each time a new speech model would arrive, we repeated the same ritual: hire native-speaking raters, benchmark it against our existing stack, and update production if it improved. Speko turns this process into an API. A team running thousands of calls a day told us: &quot;we can literally go to this dashboard, switch the model, and it will do it for us.&quot;<p>How it works: you send a request with your optimization criteria (accuracy, latency, cost or balanced), language and region. The router filters to models which we measured for the given combination of constraints, benchmarks them, selects the winner, and returns a response with headers containing provider, model names, and the scores. The gateway prefetches signed session plans, so a new session dials the provider straight from memory; no control-plane round trip while a caller waits.<p>Failover happens only during connection setup stage: if the provider refuses the connection attempt, we start connecting to the runners-up.<p>Some of the customer stories: one founder came to us not knowing what to pick at all: he gave us his use case and now routes everything through the platform. A property management AI runs LiveKit in Python and had not updated STT or TTS since launch: they did not know their STT had high error rates on their calls, better options existed, and swapping always looked like an R&amp;D project. One team did not know which models to pick for Spanish. A medical team did not know which STT handles medical vocabulary best. In every case we helped find the right stack from the benchmarks, and now they route through us.<p>The measuring part is public: we pass the same inputs to every model in one region in different dated runs and we publish the boards, including those where our selections perform worse than alternatives. A launch demo answers which 30-second clip sounds better; production asks which model survives minute eight, so we test spontaneous speech, money and dates, ten-minute takes, and the rankings change. We trained an automatic scorer for TTS naturalness on our blind head-to-head listening votes; on providers it has never seen a vote for, it picks the same winner our raters do about as often as raters agree with each other.<p>We don&#x27;t train or sell models ourselves, that&#x27;s precisely how we keep our rankings impartial.<p>We also open sourced the gateway for teams who want to avoid an extra network hop on the audio path and don&#x27;t want to share keys with our cloud (<a href="https:&#x2F;&#x2F;github.com&#x2F;SpekoAI&#x2F;gateway" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;SpekoAI&#x2F;gateway</a>, MIT): one Go binary, which is running as a sidecar in your agent&#x27;s container, speaks one local protocol over Unix socket, pins provider hosts and attaches your keys. In BYOK mode it doesn&#x27;t communicate with us at all.<p>Notice that the anonymous, content-free telemetry is enabled by default, and one env var disables it.<p>Cost: the gateway and BYOK setup will be free forever, we charge for the hosted router and managed keys with consolidated billing. Since we started the batch in late June, external usage has grown about 25 percent per week on average, front-loaded toward the launch weeks.<p>I would love feedback from the community: how do you pick speech models now, and what makes you trust the third-party benchmark?<p><a href="https:&#x2F;&#x2F;speko.ai&#x2F;">https:&#x2F;&#x2F;speko.ai&#x2F;</a>


--- Top Comments ---

[alexcnwy]: why isn&#x27;t openrouter gonna be the openrouter for voice ?

[dgreensp]: This looks really interesting. I feel like there is a lot of room to build great voice-based agents that don&#x27;t exist right now. I have found that ChatGPT voice mode is unusable (e.g. hallucinates me saying things); Claude voice mode is usable, but very buggy around tool calling, and it often mishears things.  And it only supports Opus, not Fable (though it looks like you don&#x27;t support either of those).  But I use it anyway. Question, do any of your TTS options support increasing the...

[Taikhoom10]: Is voice the right form factor? If so then search aka google will win in practicality no?  https:&#x2F;&#x2F;s-1.vercel.app&#x2F;posts&#x2F;why-openrouter-can-be-the-next-...

[webo]: The benchmarks page seems interesting and something I can use to help make an informed decision. Can you talk about how you&#x27;re measuring some of these? I imagine it needs to involve some human input.  https:&#x2F;&#x2F;benchmarks.speko.ai&#x2F;turntaking

[spmartin823]: Does this include a turn taking API? It&#x27;d be great to have one API that could do &quot;Conversation in a box&quot;. One of the biggest annoyances is daisy chaining many models together for turn taking, dumb models for immediate responses, with smarter models returning and taking over after.

</details>
