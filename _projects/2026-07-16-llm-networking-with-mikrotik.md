---
layout: default
title: "LLM Networking with MikroTik"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-llm-networking-with-mikrotik
source: hackernews
category: show-hn
ai_score: 7.0
summary: "An AI project that uses LLMs to automate the configuration of Mikrotik networking devices."
tags: "LLM, Networking, Mikrotik, Automation, AI"
---

# LLM Networking with MikroTik

**链接**: https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html

**作者**: gregsadetsky

**发布时间**: 2026-07-15T22:23:27Z

**采集日期**: 2026-07-16


## AI 摘要

An AI project that uses LLMs to automate the configuration of Mikrotik networking devices.

## AI 评价

The project shows moderate traction with 27 comments and a score of 66 on Hacker News, indicating community interest. It addresses a real problem for network administrators by using LLMs to configure Mikrotik devices, which has a clear utility and potential monetization path through SaaS or API offerings. The novelty lies in applying LLMs to network configuration, though it requires user specificity.


## 原文内容


--- Top Comments ---

[mannyv]: The important thing you need to do is specify which Mikrotik version you&#x27;re using; apparently the syntax for some things changed between 6 and 7. It does pretty well, but you need to iterate. I was trying to get it to disallow internet access for non-DHCP clients, and in the end there were so many limits to what was possible that it wasn&#x27;t worth it. But it did it, and when I was testing I found them. So like everything for best results you need to know what you&#x27;re doing so you ...

[x2tyfi]: It’s interesting to observe and build LLM-driven solutions in Networking. The biggest challenges that most of us networking people have are around velocity (how fast we can build and scale networks) and how effectively we can operate them (avoid defects, fix them fast when something breaks). LLMs are great in both areas. AI helps with deployment challenges by speeding up tooling development and the creation of workflows on orchestration platforms. A manual process step today, say - reserving ...

[briHass]: I would expect LLMs to be especially excellent at configuring Mikrotik stuff, given MT publishes markdown reference docs for LLM ingestion, the full config without secrets can be dumped to one text file, and their cli commands are very stable between versions. I switched recently to OpenWrt from MT, which code agents are also good at. I&#x27;d wager most issues are going to be related to the user not specifying what they want clearly enough. The translation from network concepts to RouterOS c...

[alanwreath]: Yes! Recently connected two disparate systems (ubiquiti and mimrotik) using their exposed API’s and a Claude session so that systems I have on either environment could talk to each other. I am not a network engineer so it was liberating to get my gear working together.  That said it’s a work in progress and just today I noticed something weird that one of my computers can’t access Minecraft servers while the rest of my network can

[arjie]: I only have the agent investigate directly. To actually configure the Mikrotik, I have the agent write a script that is aimed to be idempotent and then run the script. Investigation is fine, but the script acts as a memory of intent which I find useful. As agents get better, it can be a textual representation rather than a script, but for now that suffices.