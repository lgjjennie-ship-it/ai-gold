---
layout: default
title: "LLM Networking with MikroTik"
date: 2026-07-15T22:23:27Z
slug: 2026-07-16-llm-networking-with-mikrotik
source: hackernews
category: show-hn
ai_score: 8.0
tags: "LLM, Networking, MikroTik, Automation, AI"
---

# LLM Networking with MikroTik

**链接**: https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html

**作者**: gregsadetsky

**发布时间**: 2026-07-15T22:23:27Z

**采集日期**: 2026-07-16


## AI 摘要

This project uses LLMs to automate and simplify MikroTik network configuration and management.

## AI 评价

High traction with 62 points on Hacker News and 24 comments, indicating strong community interest. The project addresses a real pain point in networking by leveraging LLMs for MikroTik configuration, showing practical utility and potential for monetization through SaaS or API services. The niche is specific but valuable, and the approach is novel in applying AI to network automation.


## 原文内容


--- Top Comments ---

[x2tyfi]: It’s interesting to observe and build LLM-driven solutions in Networking. The biggest challenges that most of us networking people have are around velocity (how fast we can build and scale networks) and how effectively we can operate them (avoid defects, fix them fast when something breaks). LLMs are great in both areas. AI helps with deployment challenges by speeding up tooling development and the creation of workflows on orchestration platforms. A manual process step today, say - reserving ...

[briHass]: I would expect LLMs to be especially excellent at configuring Mikrotik stuff, given MT publishes markdown reference docs for LLM ingestion, the full config without secrets can be dumped to one text file, and their cli commands are very stable between versions. I switched recently to OpenWrt from MT, which code agents are also good at. I&#x27;d wager most issues are going to be related to the user not specifying what they want clearly enough. The translation from network concepts to RouterOS c...

[alanwreath]: Yes! Recently connected two disparate systems (ubiquiti and mimrotik) using their exposed API’s and a Claude session so that systems I have on either environment could talk to each other. I am not a network engineer so it was liberating to get my gear working together.  That said it’s a work in progress and just today I noticed something weird that one of my computers can’t access Minecraft servers while the rest of my network can

[dools]: I’ve been using ChatGPT to configure my mikrotik gear for about a year it’s pretty awesome. And the end result is well documented reusable scripts rather than my usual set of random stack overflow copy pastes and shitty inscrutable notes

[arjie]: I only have the agent investigate directly. To actually configure the Mikrotik, I have the agent write a script that is aimed to be idempotent and then run the script. Investigation is fine, but the script acts as a memory of intent which I find useful. As agents get better, it can be a textual representation rather than a script, but for now that suffices.