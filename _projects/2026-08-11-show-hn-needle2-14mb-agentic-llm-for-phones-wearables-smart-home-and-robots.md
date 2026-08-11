---
layout: default
title: "Needle2：轻量级边缘设备智能体LLM"
date: 2026-08-11T12:00:00+00:00
discovered_date: 2026-08-11
slug: 2026-08-11-show-hn-needle2-14mb-agentic-llm-for-phones-wearables-smart-home-and-robots
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Needle2是一款14MB的智能体LLM，专为手机、可穿戴设备、智能家居和机器人设计，利用简单注意力网络实现高效性能。 凭借239个星标和活跃的社区参与，Needle2满足了边缘计算中对微型LLM日益增长的需求，为资源受限的设备提供了实用解决方案。 Needle2采用Apache 2.0许可证，处于alpha阶段，部署复杂度低，适合硬件资源有限的设备。"
tags: "LLM, Agent, Mobile, Wearable, Robotics"
---

# Needle2：轻量级边缘设备智能体LLM


> Needle2是一款14MB的智能体LLM，专为手机、可穿戴设备、智能家居和机器人设计，利用简单注意力网络实现高效性能。 凭借239个星标和活跃的社区参与，Needle2满足了边缘计算中对微型LLM日益增长的需求，为资源受限的设备提供了实用解决方案。 Needle2采用Apache 2.0许可证，处于alpha阶段，部署复杂度低，适合硬件资源有限的设备。


**项目链接**：https://cactuscompute.com/needle
**作者**：HenryNdubuaku
**发布时间**：2026-08-10T17:22:07Z
**挖掘日期**：2026-08-11
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：LLM, Agent, Mobile, Wearable, Robotics


## 📌 项目详解

Needle2是一款14MB的智能体LLM，专为手机、可穿戴设备、智能家居和机器人设计，利用简单注意力网络实现高效性能。 凭借239个星标和活跃的社区参与，Needle2满足了边缘计算中对微型LLM日益增长的需求，为资源受限的设备提供了实用解决方案。 Needle2采用Apache 2.0许可证，处于alpha阶段，部署复杂度低，适合硬件资源有限的设备。


## 🌐 背景与生态

物联网设备的兴起催生了对轻量级AI模型的需求，这些模型可以在不依赖云基础设施的情况下高效运行。传统的LLM对边缘设备来说资源消耗过大。


## 💬 社区讨论

社区反馈褒贬不一，一些人赞赏其效率和对机器人的潜力，而另一些人则批评网络演示的局限性和机器人功能。


## 🚀 应用前景

Needle2可用于智能家居自动化、机器人和移动应用，这些场景对实时处理和低功耗至关重要。盈利模式可能来自SaaS或API服务。


## 🔧 技术栈

Needle2使用Python构建，采用简单注意力网络，可在RAM有限的设备（如Raspberry Pi 5和Meta Quest 3S）上高效运行。


## 🎯 上手难度

难度：入门。开始使用，请安装Python 3.8+，下载模型，并运行提供的脚本。无需GPU。


## 👥 目标用户

目标用户包括开发物联网设备、机器人和边缘计算的开发人员，以及探索微型LLM应用的研究人员。


## ⚖️ 类似项目对比

竞品包括LFM2.5和Apple Foundation Model等LLM，它们更小但效率较低。边缘AI领域的类似产品有TensorFlow Lite和PyTorch Mobile。


## 📚 参考链接

- [AI agent - Wikipedia](https://en.wikipedia.org/wiki/AI_agent)
- [What Are Agentic LLMs? Use Cases, Risks, and How They Work](https://labs.adaline.ai/p/what-are-agentic-llms-a-comprehensive)
- [LLM vs Agentic AI: Understand the Differences - ML Journey](https://mljourney.com/llm-vs-agentic-ai-understand-the-differences/)

<details><summary>📄 查看原文内容</summary>


Hey HN,<p>Henry from Cactus here!<p>We previously released Cactus Needle, a 14MB agentic LLM for tool call, device use, and structured extraction for phones, wearables, smart homes, small robots and microcontrollers. We got really great feedback here, and have now incorporated the suggestions to release Needle 2.<p>The whole model is a single 14MB binary that runs a full session in 28MB of RAM; 45m parameters at 2bit compression. Needle hits 500 tokens&#x2F;sec decode speed on a Raspberry Pi 5, sits between 400-1,500 tokens&#x2F;sec on VR devices like Meta Quest 3S and Apple Vision Pro, and ranges 300-700 on sub-$200 phones such as the Samsung A-Series.<p>On the tool call and mobile device use benchmarks, Needle 2 trades wins with closest small models like LFM2.5 230M and Apple Foundation Model, at 5x to 70x smaller, both at f16 vs Needle 2 at 2bit. Needle is based on Simple Attention Networks from our paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2607.18363" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2607.18363</a>).<p>Edge AI has lately meant Macs and PCs, but that is just 1.5 billion of over 21 billion connected IoT devices in the world today, and in emerging markets most phones ship under $200, no NPU, cheap GPUs. These include budget phones, Raspberry Pis, microcontrollers, wearables, small robots like Reachy Mini, and connected home devices.<p>A conventional transformer of Needle&#x27;s width and depth spends 164 MFLOPs per token, and even one squeezed down to Needle&#x27;s parameter count spends 87, Needle spends 70. Even on a high-end phone, an always-on assistant lives inside a power budget; every MFLOP is milliwatt-hours, and Needle spends 7x to 85x fewer of them per token than the smallest performant LLMs. More about the architecture in the link.<p>When we structure intelligence for consumer devices as functions with typed parameters, the only hard part is mapping a messy sentence onto them; which function, with which values. Our research found that when framed that way, the problem needs no world knowledge and no open-ended prose, which is why 45M parameters suffice.<p>Needle 2 expands to structured extraction where the schema can be passed in-place of tools and the model returns structured output. You can use Needle as a text-classification model with an enum field, as a summarization model by providing a schema that extracts key fields, everything but free-range decode.<p>Every product has its own tool vocabulary and fine-tuning needle helps it achieve frontier-level performance on custom tasks, so using the python package (<a href="https:&#x2F;&#x2F;github.com&#x2F;cactus-compute&#x2F;needle" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;cactus-compute&#x2F;needle</a>), Needle can be fine-tuned Needle on a Mac&#x2F;PC in minutes to a few hours, with automated data-generation pipeline, just pass a couple samples.<p>Nonetheless, every response carries a learned confidence score based our Cactus Hybrid technique. If above your threshold, act, below it, escalate to the cloud or bigger model. Combining Needle 2 with a private DeepSeek-v4-Flash deployment works particularly well for enterprise-level tasks at barely any cost, we can help with this setup.<p>We have put a lot of thoughts into Needle 2 but might still be missing quite a lot, please use the playground in the provided link to test Needle and share your thoughts, always appreciated!


--- Top Comments ---

[nater5000]: This is cool. I definitely think the &quot;micro&quot; sized LLM space is underappreciated, so it&#x27;s always good to see work like this. I foresee a paradigm in some contexts where you have a hierarchy of LLMs, with more competent models actively training smaller models to solve specific tasks very efficiently, and something like this could be the smallest layer in that stack. With that being said, the web demo is not particularly impressive. It really doesn&#x27;t like anything I throw at...

[Tiberium]: Funny result from the web demo. I&#x27;m well aware that it&#x27;s an extremely small and, well, stupid, model, but even so: Query: HN Result: {
  &quot;function_calls&quot;: [
    {
      &quot;name&quot;: &quot;lock_door&quot;,
      &quot;arguments&quot;: {
        &quot;door&quot;: &quot;front door&quot;
      }
    }
  ],
  &quot;reasoning&quot;: &quot;User wants to lock the door. No specific door mentioned, so use &#x27;front door&#x27; as default.&quot;,
  &quot;confidence&quot;: 0
} I...

[kooi]: Its pretty significant you&#x27;ve got this working locally in wasm. Very cool. Re: robotics: I&#x27;m unsure how this could be helpful. It fails a pretty simple navigation prompt. X0: (0.0, 0.0). Object bounding box: [1.0, 1.0, 2.0, 2.0]. navigate to (3.0,3.0) I changed it to &quot;call path planner to navigate: a_star(x0, xf, obs)&quot; Another fail. My intuition tells me micro llms will&#x2F;are important for robotics. I just can&#x27;t grok it. Can someone without control theory experienc...

[dbeardsl]: My first query: &gt; Make it a little warmer in here. The reply: &gt;      &quot;name&quot;: &quot;set_thermostat&quot;,
&gt;      &quot;arguments&quot;: {
&gt;        &quot;temperature&quot;: 65,
&gt;        &quot;mode&quot;: &quot;cool&quot;,
&gt; ...
&gt;   &quot;reasoning&quot;: &quot;&#x27;warmer&#x27; implies need for cooling; set_thermostat with temperature 65 (typical warmth) and mode &#x27;cool&#x27;.&quot;, Maybe I&#x27;m doing it wrong?

[arthuqa]: That&#x27;s really cool - I was already thinking of compressing `functiongemma-270m-it` down to 1-2 bits so it would work flawlessly in the browser.
Your `Fine-tuning` feature is even much more convenient.

</details>
