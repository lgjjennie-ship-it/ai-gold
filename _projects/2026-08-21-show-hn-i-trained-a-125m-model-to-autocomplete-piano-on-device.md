---
layout: default
title: "设备端钢琴自动补全AI模型"
date: 2026-08-21T12:00:00+00:00
discovered_date: 2026-08-21
slug: 2026-08-21-show-hn-i-trained-a-125m-model-to-autocomplete-piano-on-device
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目介绍了一个125M参数的Transformer模型，能够在设备端实时进行钢琴表演自动补全，类似于GitHub Copilot，但用于音乐，通过MIDI输入触发。 它在Hacker News上获得了高关注度（536个星标，111条评论），解决了钢琴表演自动补全的实际需求，并通过SaaS或应用商店收入提供了潜在的盈利模式。 该模型采用开放许可证，似乎处于alpha阶段，在iPhone 15上运行（约108个音符/秒），需要Core ML集成，但除设备外没有特定的硬件要求。"
tags: "AI, Music, Transformer, On-Device, Autocomplete"
---

# 设备端钢琴自动补全AI模型


> 该项目介绍了一个125M参数的Transformer模型，能够在设备端实时进行钢琴表演自动补全，类似于GitHub Copilot，但用于音乐，通过MIDI输入触发。 它在Hacker News上获得了高关注度（536个星标，111条评论），解决了钢琴表演自动补全的实际需求，并通过SaaS或应用商店收入提供了潜在的盈利模式。 该模型采用开放许可证，似乎处于alpha阶段，在iPhone 15上运行


**项目链接**：https://simedw.com/2026/08/20/midi-autocomplete/
**作者**：simedw
**发布时间**：2026-08-20T12:04:38Z
**挖掘日期**：2026-08-21
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Music, Transformer, On-Device, Autocomplete


## 📌 项目详解

该项目介绍了一个125M参数的Transformer模型，能够在设备端实时进行钢琴表演自动补全，类似于GitHub Copilot，但用于音乐，通过MIDI输入触发。 它在Hacker News上获得了高关注度（536个星标，111条评论），解决了钢琴表演自动补全的实际需求，并通过SaaS或应用商店收入提供了潜在的盈利模式。 该模型采用开放许可证，似乎处于alpha阶段，在iPhone 15上运行（约108个音符/秒），需要Core ML集成，但除设备外没有特定的硬件要求。


## 🌐 背景与生态

该项目利用了Transformer技术，该技术由GPT-4等模型普及，用于实时音乐生成，建立在边缘AI和生成模型趋势之上。


## 💬 社区讨论

评论强调了该项目与古典作曲训练的契合度，询问了数据量大小，将之与AI用户体验设计相比较，并指出了演示中模型的一个小错误。


## 🚀 应用前景

这可以应用于音乐教育、作曲辅助和娱乐应用，通过SaaS订阅或应用内购买进行盈利，目标用户为音乐家和休闲用户。


## 🔧 技术栈

技术栈包括一个125M参数的Transformer、Core ML用于设备端执行，以及MIDI用于输入，未提及特定框架版本。


## 🎯 上手难度

难度：入门。要求包括支持Core ML的兼容设备以及基本的Python知识。步骤包括下载应用，演奏音符以触发自动补全。


## 👥 目标用户

目标用户是音乐家、作曲家和音乐爱好者，他们可能从实时表演辅助和创意灵感中受益。


## ⚖️ 类似项目对比

竞品包括用于音乐生成的GPT-4和基于AI的作曲辅助工具如AIVA。该项目通过专注于设备端性能而有所不同。


## 📚 参考链接

- [Transformer (deep learning) - Wikipedia](https://en.wikipedia.org/wiki/Transformer_(deep_learning))
- [What are Transformers? - Transformers in Artificial Intelligence Explained - AWS](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/)
- [What is a Transformer Model? | IBM](https://www.ibm.com/think/topics/transformer-model)

<details><summary>📄 查看原文内容</summary>


I trained a 125M-parameter transformer to autocomplete piano performances in real time (~108 notes&#x2F;sec on an iPhone 15).<p>The idea is basically GitHub Copilot or Tabnine, except instead of prompting it with code, you prompt it by playing a few notes on a MIDI piano. The model then continues what you played, entirely on-device.<p>The app is free if anyone wants to try it. Happy to answer questions about the model, training, Core ML, or the many things that didn&#x27;t work.


--- Top Comments ---

[tom_vidal]: This sort of “autocomplete” is actually fundamental to how classical composers were trained. For anyone interested, I’d highly recommend reading Robert Gjerdingen’s article Gebrauchs-Formulas.  https:&#x2F;&#x2F;www.researchgate.net&#x2F;publication&#x2F;259731561_Gebrauchs...  You can also listen to the transcript of four Russian composers, including Rachmaninoff, playing this pattern recognition and generation game at a dinner party in the late 1800’s:  https:&#x2F;&#x2F;youtu.be&#x2F;PlFPO...

[jasonjmcghee]: I think this is a great project and very HN. Not sure why the comments are so focused on the deliverable- you learned way more and had a much more interesting experience. One think I didn&#x27;t see mentioned in the post- maybe I missed it- how large was the data? How many samples did you use to pretrain and post-train

[joshuamerrill]: Classical pianist and software product designer here. I see so much in common with this project and the numerous AI-based UX design tools out there. Whether it&#x27;s music or UI, now that the &quot;generation&quot; portion of the work costs zero, all that remains is taste. And so much of taste comes from exploring and killing off possibilities that turn out to be dead-ends. I love the idea that models like these will help us find the dead ends faster, or even produce a gem here and there. P....

[jancsika]: The end of the AI&#x27;s first sub-phrase in the video is wrong. You started by playing a simple I - vii - I as the first sub-phrase. Then the AI started its response with a dominant 7th-chord. In the vast majority of cases I can think of from the Classical era, the AI&#x27;s sub-phrase would end with a half-cadence. So, including what you played, the first two sub-phrases would look like this: I - vii - I V(7) - I - V But instead, the AI took the unusual step of having a full cadence for tha...

[goda90]: Reminds me of this project to generate every melody possible algorithmically in order to fight music copyright lawsuits. 
 https:&#x2F;&#x2F;allthemusic.info&#x2F;

</details>
