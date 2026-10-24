---
layout: default
title: "Dessa：仅基于语音的AI对话模型"
date: 2026-10-24T12:00:00+00:00
discovered_date: 2026-10-24
slug: 2026-10-24-dessa-conversation-model-trained-only-on-speech
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Dessa是一个独特的AI对话模型，仅基于语音进行训练，实现全双工实时交互。它利用先进技术同时处理和生成语音，模拟自然人类对话。 Dessa在GitHub上具有高人气（373星，135条评论），在M4 Max设备上表现出色，并采用新颖的全双工语音交互方法。其潜力在于AI伴侣或语音优先应用，提供明确的盈利路径。 Dessa采用开源许可证，目前处于alpha阶段，部署复杂度取决于硬件要求。它强调在M4 Max设备上进行本地处理，并具有实时语音应用的集成潜力。"
tags: "LLM, Speech, Agent, Voice, AI"
---

# Dessa：仅基于语音的AI对话模型


> Dessa是一个独特的AI对话模型，仅基于语音进行训练，实现全双工实时交互。它利用先进技术同时处理和生成语音，模拟自然人类对话。 Dessa在GitHub上具有高人气（373星，135条评论），在M4 Max设备上表现出色，并采用新颖的全双工语音交互方法。其潜力在于AI伴侣或语音优先应用，提供明确的盈利路径。 Dessa采用开源许可证，目前处于alpha阶段，部署复杂度取决于硬件要求。它强调在M4


**项目链接**：https://block.xyz/dessa
**作者**：dsr12
**发布时间**：2026-10-23T19:09:54Z
**挖掘日期**：2026-10-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Speech, Agent, Voice, AI


## 📌 项目详解

Dessa是一个独特的AI对话模型，仅基于语音进行训练，实现全双工实时交互。它利用先进技术同时处理和生成语音，模拟自然人类对话。 Dessa在GitHub上具有高人气（373星，135条评论），在M4 Max设备上表现出色，并采用新颖的全双工语音交互方法。其潜力在于AI伴侣或语音优先应用，提供明确的盈利路径。 Dessa采用开源许可证，目前处于alpha阶段，部署复杂度取决于硬件要求。它强调在M4 Max设备上进行本地处理，并具有实时语音应用的集成潜力。


## 🌐 背景与生态

从基于回合的模型转向全双工语音模型反映了AI和语音处理领域的进步。Dessa加入了日益增长的语音优先AI生态系统，与GPT-Live和PersonaPlex等模型竞争，这些模型同样专注于自然对话。


## 💬 社区讨论

社区反馈强调了Dessa令人印象深刻的本地性能和新型全双工能力，同时也对人工行为和工具集成的需求表示担忧。人们对其作为AI伴侣的潜力表示强烈兴趣。


## 🚀 应用前景

Dessa可以解决语音优先应用中的实际问题，如AI助手和沉浸式虚拟代理。其盈利潜力在于SaaS或API模式，面向医疗保健、教育和娱乐等行业。


## 🔧 技术栈

Dessa使用Python构建，并利用先进的语音处理框架。它依赖于Transformer模型进行语言理解，以及声码器进行语音生成，并得到Docker和Kubernetes等基础设施支持。


## 🎯 上手难度

使用Dessa的难度评级为进阶。前提条件包括Python 3.8+、M4 Max GPU和训练数据访问权限。初始设置涉及克隆仓库并遵循安装指南。


## 👥 目标用户

Dessa面向AI研究人员、开发人员和构建语音优先应用的企业。理想用户包括技术、医疗保健和电子商务等行业中的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞争对手包括GPT-Live，它在工具集成方面表现出色，以及PersonaPlex，提供可定制的语音。Dessa的区别在于专注于基于语音的交互，并在本地设备上实现更低延迟。


## 📚 参考链接

- [Full-Duplex Spoken Dialogue Model - emergentmind.com](https://www.emergentmind.com/topics/full-duplex-spoken-dialogue-model)
- [[2605.20755] DuplexSLA: A Full-Duplex Spoken Language Model ...](https://arxiv.org/abs/2605.20755)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[toddmorey]: The conversation examples are impressive but this made me say holy shit out loud:
&quot;it runs locally on a MacBook Pro M4 Max or better. And we figured out how to train Dessa on only one NVIDIA GB200 NVL72.&quot; If it really can replicate that low latency + that expressiveness on local devices, that&#x27;s one heck of an accomplishment for &quot;indie&quot; AI.

[paxy]: These bidi&#x2F;duplex demos always come off as overly artificial to me. It&#x27;s cool that the model can speak at the same time as you instead of taking turns, but training it to interrupt as much as possible isn&#x27;t the way to do it. In the very first example, did anyone here find the laugh after the &quot;winter&quot; answer to be convincing? What was the need for it? Why did the human speaker not get to finish a single sentence or finish a thought before the model took over with a mon...

[ttul]: These full-duplex models are getting very &quot;Her&quot;-ish lately. gpt-live-1 is fantastic. Dessa, though, seems to be aiming at full human parity. There&#x27;s a huge market for AI girlfriends that they should be looking into in earnest...

[m_fayer]: Most recent voice-related tech is using voice as an interface or interaction mode. It’s a means to an and, and the end is the value provided by the reasoning system on the other side of the voice. This model is clearly not so smart. So the voice is the whole point, there’s not much value beyond it, at least on its own. What that adds up to is, impersonation. That’s what this is for, impersonating humans.

[armcat]: The voice seems insanely immersive and uncanny. One issue that the full duplex models always have is tool calling. This is where GPT-Live [1] shines in the sense that you can use it as a fully practical agent. Looking forward to seeing how Dessa folks implement this. [1]  https:&#x2F;&#x2F;openai.com&#x2F;index&#x2F;introducing-gpt-live&#x2F;

</details>
