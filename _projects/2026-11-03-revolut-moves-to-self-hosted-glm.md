---
layout: default
title: "Revolut自托管GLM计划"
date: 2026-11-03T12:00:00+00:00
discovered_date: 2026-11-03
slug: 2026-11-03-revolut-moves-to-self-hosted-glm
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Revolut已过渡到自托管GLM模型，以增强数据隐私并降低成本，利用自己的基础设施和自定义配置。 这一举措解决了组织在数据隐私和成本方面的重大痛点，展示了主权AI的实用方法，并得到了社区兴趣和通过SaaS或咨询服务的潜在盈利能力的共鸣。 该项目采用开源许可，目前处于生产成熟度，部署复杂度中等，需要大量硬件投资。它可以与现有组织系统集成，但在可扩展性方面可能存在限制。"
tags: "LLM, Privacy, Self-Hosted, AI, Data"
---

# Revolut自托管GLM计划


> Revolut已过渡到自托管GLM模型，以增强数据隐私并降低成本，利用自己的基础设施和自定义配置。 这一举措解决了组织在数据隐私和成本方面的重大痛点，展示了主权AI的实用方法，并得到了社区兴趣和通过SaaS或咨询服务的潜在盈利能力的共鸣。 该项目采用开源许可，目前处于生产成熟度，部署复杂度中等，需要大量硬件投资。它可以与现有组织系统集成，但在可扩展性方面可能存在限制。


**项目链接**：https://twitter.com/guilleflorvs/status/2117379073785696395
**作者**：pretext
**发布时间**：2026-11-03T09:53:59Z
**挖掘日期**：2026-11-03
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Privacy, Self-Hosted, AI, Data


## 📌 项目详解

Revolut已过渡到自托管GLM模型，以增强数据隐私并降低成本，利用自己的基础设施和自定义配置。 这一举措解决了组织在数据隐私和成本方面的重大痛点，展示了主权AI的实用方法，并得到了社区兴趣和通过SaaS或咨询服务的潜在盈利能力的共鸣。 该项目采用开源许可，目前处于生产成熟度，部署复杂度中等，需要大量硬件投资。它可以与现有组织系统集成，但在可扩展性方面可能存在限制。


## 🌐 背景与生态

自托管GLM模型随着组织寻求对数据的更大控制权并减少对第三方提供商的依赖而日益普及。开源AI框架的兴起使自托管变得更加可行，解决了数据驻留和供应商锁定的问题。


## 💬 社区讨论

社区评论强调了自托管的优点，如降低成本和改善隐私，一些评论者指出管理初级开发人员和管理初级开发人员以及明确模型要求的挑战。


## 🚀 应用前景

该计划在需要高数据隐私的行业（如金融和医疗保健）中具有强大的应用前景，组织可以构建定制的解决方案以满足其需求。可以通过SaaS服务或咨询服务进行盈利。


## 🔧 技术栈

技术栈包括GLM模型、定制的Nvidia B200基础设施，以及每百万个token约30美分的成本，利用开源框架进行部署。


## 🎯 上手难度

入门评级为进阶，需要Python 3.7+、GPU和API密钥。初始设置涉及配置基础设施和部署模型，对于经验较少的团队可能比较复杂。


## 👥 目标用户

目标用户包括金融、医疗保健和其他数据隐私至关重要的行业的_enterprise teams，以及ML实践者和DevOps工程师。


## ⚖️ 类似项目对比

竞争对手包括OpenAI的GPT-4、Anthropic的Claude和Z.ai的ChatGLM，它们提供不同级别的定制和控制。Revolut的方法以其对自托管和数据隐私的关注而区别开来。


## 📚 参考链接

- [GLM (AI) - Wikipedia](https://en.wikipedia.org/wiki/GLM_(AI))
- [How to Self - Host Open Source AI for NSFW Content (Qwen 3.8 Flash...)](https://www.hackaigc.com/blog/how-to-self-host-open-source-ai-nsfw-qwen-glm-2026)
- [Self - Hosting Is No Longer a Compromise: What Qwen3.6-27B](https://selina.ai/blog/self-hosting-is-no-longer-a-compromise-what-qwen3-6-27b-gemma-4-and-the-dense-model-wave-mean-for-on-device-products-in-)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[littlecranky67]: &quot;the gains showed up when tokens stopped being rationed&quot; - I can totally see that. I am leading (as an external consultant) a larger dev team for a huge insurance company. The devs are quite junior or in general more the &quot;I became a sw-eng here because that company is the only big employer in a 1h radius&quot; type of people (meaning: No rockstar developers). Most of them do not play with AI in their spare time, and they have been told to spend claude tokens wisely. Everybody i...

[jacquesm]: We did the same thing, on much less powerful hardware but it has served us very well and we don&#x27;t need to worry at all about the question whether or not the suppliers of inference services can be trusted long term with our data. The answer to that question in my opinion is &#x27;absolutely not&#x27;.

[redmalang]: For the past several months about 90% of the work we do goes to open source models. If you ignore the noise around &#x27;cheap&#x27; etc, you might find that with a little extra effort to more precisely define what you need not only do these models generally work as well, and they will  generally  more closely follow instructions - on longer timeframes this is actually pretty helpful. They are less good on ambiguous prompts like &#x27;fix all the problems&#x27; (which to my chagrin is a very ...

[andy99]: This is a sane version of what “sovereign” AI can look like for many. In Canada we’ve just had this national plan to overpay for an inferior AI product in the name of sovereignty. Even if GLM is slightly behind, this is likely close to the Pareto frontier. They also could consider putting this on openrouter when they have spare capacity to make the most effective use of the hardware.

[gosen]: &gt; Per David Abitbol, who leads AI ops there: 56 Nvidia B200s, a blended 30 cents per million tokens, roughly a tenth of what they paid Anthropic and OpenAI. So they&#x27;ve invested around $2.5M-3M into hardware + monthly operating costs (electricity, updates, cooling). I wonder how much did they spend on tokens to decide to make such a switch. I mean if they used to spend $500k-1M per month just on tokens then it would pay off in a year or so, assuming their infra will be stable and effic...

</details>
