---
layout: default
title: "Hurston-1：南方与非洲英语TTS模型"
date: 2026-10-26T12:00:00+00:00
discovered_date: 2026-10-26
slug: 2026-10-26-show-hn-hurston-1-open-source-tts-that-speak-southern-american-and-afro-english
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Hurston-1 是一个开源的TTS模型，旨在使用窄带方法生成南方美式英语和非洲英语口音的声音。 该项目因其在高危新闻上的高人气以及对独特领域的关注而具有重要意义，满足了在代表性不足的口音中生成AI声音的需求。 该模型在 Apache-2.0 下许可，目前处于alpha阶段，需要特定硬件以获得最佳性能。它不支持声音克隆。"
tags: "TTS, Voice, AI, Language, Accents"
---

# Hurston-1：南方与非洲英语TTS模型


> Hurston-1 是一个开源的TTS模型，旨在使用窄带方法生成南方美式英语和非洲英语口音的声音。 该项目因其在高危新闻上的高人气以及对独特领域的关注而具有重要意义，满足了在代表性不足的口音中生成AI声音的需求。 该模型在 Apache-2.0 下许可，目前处于alpha阶段，需要特定硬件以获得最佳性能。它不支持声音克隆。


**项目链接**：https://huggingface.co/destined/hurston-1
**作者**：Gcarter08
**发布时间**：2026-10-25T01:30:13Z
**挖掘日期**：2026-10-26
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：TTS, Voice, AI, Language, Accents


## 📌 项目详解

Hurston-1 是一个开源的TTS模型，旨在使用窄带方法生成南方美式英语和非洲英语口音的声音。 该项目因其在高危新闻上的高人气以及对独特领域的关注而具有重要意义，满足了在代表性不足的口音中生成AI声音的需求。 该模型在 Apache-2.0 下许可，目前处于alpha阶段，需要特定硬件以获得最佳性能。它不支持声音克隆。


## 🌐 背景与生态

该项目填补了AI生成语音在南方美式英语和非洲英语口音方面的空白，这是一个主流TTS模型以前服务不足的领域。


## 💬 社区讨论

社区评论对该模型的独特关注表示兴趣，并请求演示，同时讨论了用于口音的术语。


## 🚀 应用前景

该模型可用于配音、客户服务机器人和教育内容等应用，适用于有南方美式英语和非洲英语口音的地区。


## 🔧 技术栈

该模型使用 Maya1 构建，采用窄带TTS方法，可通过 Hugging Face 部署。它专注于电话质量的音频输出。


## 🎯 上手难度

入门评级为进阶，需要 Python 3.7+、GPU 和对 Hugging Face 模型的访问。基本设置涉及克隆存储库并按照说明进行。


## 👥 目标用户

目标用户包括媒体、娱乐和教育领域需要南方美式英语和非洲英语内容的开发者。


## ⚖️ 类似项目对比

竞争对手包括谷歌的文本转语音和微软的 Azure 语音，它们提供广泛的语言支持，但缺乏专门的地区口音。


## 📚 参考链接

- [Hurston-1: First Open TTS for Southern American and Afro ...](https://stackfutures.com/blog/hurston-1-tts-southern-american-afro-english-narrowband-phone-oct-2026/)

<details><summary>📄 查看原文内容</summary>


Hey HN, I’m open sourcing my Hurston-1 narrowband TTS model (Apache-2.0). It is very good with American English and does especially well with Southern American and Regional African English accents. Destined AI is based in Atlanta, and I built this because I’m amazed by what AI can do, and I wanted to help introduce and welcome more people to feel comfortable using and interacting with AI.<p>Since 2021, I’ve been collecting fully consented voice data from over 20,000 people, 1M audio recordings, and over 1,800 hrs of audio captured to date. For this model, I used a small part of the data, 136 hrs, to finetune Maya1 and expand it’s capabilities.<p>Hurston-1 is a narrowband TTS model that focuses the output on telephone use because that is still where most of these voices will be heard. I’ve used it to support customers such as Amazon and Salesforce and generated over half-mill revenue with it. Now I’m open sourcing it to help unlock opportunities for others as well.<p>Limitations: this model doesn’t maintain the exact same voice across prompts and doesn’t support voice cloning. For many use cases, this is fine but maybe not so - if you’re creating podcasts.<p>This is the first release - I’m already working on the next version with improvements.<p>I would appreciate, if anyone is interested in this space, download the model from huggingface, check it out and let me know any feedback. Also, open to connecting with others in this space as well.


--- Top Comments ---

[someperson]: Sounds like your project is for southern American English presumably including African-American Vernacular English (AAVE), and for regional accents in the African continent specifically for the English language. But tangentially related, for non-English languages of the African continent, the Gates Foundation are pledging some grants to improve AI access outside of English-speaking regions:  https:&#x2F;&#x2F;news.bpdata.com&#x2F;article&#x2F;gates-foundation-pledges-1-b...  Despite being foc...

[themanmaran]: Do you have a way to demo the voice without downloading and running the model? The Huggingface playback doesn&#x27;t work.

[SamBam]: Tangentially-related: When YouTube auto-dubs now, I noticed that Spanish language get dubbed in a Spanish-inflected accent, and French language similarly (I think). Is it likely that they are using a model like this? Or are they actually trying to voice clone the original and then translate to English? I&#x27;m not even sure if the few Spanish-accented English auto-dubs I&#x27;ve heard are the same voice or not. (Actually, that reminds me of growing up in Italy, where for a long time all Engl...

[fractorial]: Seeing Atlanna inspire an open weight model was not on my 2026 bingo card.

[pessimizer]: AAVE was an awful term, but &quot;Regional African English&quot; and &quot;Afro-English&quot; is even worse if you&#x27;re trying to talk about black Americans. Are you talking about the English of Africans in different parts of Africa? If so, are you including the voices of white and Mediterranean Africans? I&#x27;m confused. As a black American with roots (going back a couple centuries) in the Ark-La-Tex, I would think our dialects would be covered under &quot;Southern American,&quot; which...

</details>
