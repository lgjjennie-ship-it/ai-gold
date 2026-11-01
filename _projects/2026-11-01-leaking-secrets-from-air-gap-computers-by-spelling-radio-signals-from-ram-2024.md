---
layout: default
title: "AI项目：通过无线电信号泄露安全隔离计算机的秘密"
date: 2026-11-01T12:00:00+00:00
discovered_date: 2026-11-01
slug: 2026-11-01-leaking-secrets-from-air-gap-computers-by-spelling-radio-signals-from-ram-2024
source: hackernews
category: show-hn
ai_score: 9.0
summary: "该项目探索如何通过从RAM中拼写无线电信号来泄露安全隔离计算机的秘密，采用了一种新颖的AI驱动方法。 它因高参与度、解决安全隔离计算机的主要安全问题以及尽管存在当前限制的潜在实际影响而具有重要意义。 该项目处于alpha阶段，需要恶意软件安装和特定的硬件设置，在实践部署方面存在显著限制。"
tags: "AI, Security, Radio, Computers, Innovation"
---

# AI项目：通过无线电信号泄露安全隔离计算机的秘密


> 该项目探索如何通过从RAM中拼写无线电信号来泄露安全隔离计算机的秘密，采用了一种新颖的AI驱动方法。 它因高参与度、解决安全隔离计算机的主要安全问题以及尽管存在当前限制的潜在实际影响而具有重要意义。 该项目处于alpha阶段，需要恶意软件安装和特定的硬件设置，在实践部署方面存在显著限制。


**项目链接**：https://arxiv.org/abs/2409.02292
**作者**：hapax_legomena
**发布时间**：2026-11-01T01:46:29Z
**挖掘日期**：2026-11-01
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Security, Radio, Computers, Innovation


## 📌 项目详解

该项目探索如何通过从RAM中拼写无线电信号来泄露安全隔离计算机的秘密，采用了一种新颖的AI驱动方法。 它因高参与度、解决安全隔离计算机的主要安全问题以及尽管存在当前限制的潜在实际影响而具有重要意义。 该项目处于alpha阶段，需要恶意软件安装和特定的硬件设置，在实践部署方面存在显著限制。


## 🌐 背景与生态

安全隔离计算机是为了防止网络威胁，但该项目表明，尽管存在隔离，AI仍可能启用新的攻击向量。


## 💬 社区讨论

评论表达了对AI不可控潜力的担忧，对电源线干扰的好奇，以及对实用性的怀疑。


## 🚀 应用前景

这可能会通过揭示隔离系统的秘密来影响网络安全，在情报或高安全行业可能有用。


## 🔧 技术栈

技术栈涉及用于信号生成的AI、射频技术以及用于初始访问的恶意软件。


## 🎯 上手难度

难度：进阶。前提条件包括Python、GPU和恶意软件设置。步骤涉及设置硬件和运行AI模型。


## 👥 目标用户

目标用户是安全研究人员、网络安全专业人员以及专注于高级威胁的开发人员。


## ⚖️ 类似项目对比

竞争对手包括传统的基于恶意软件的攻击和其他基于射频的方法，如RAMBO。


## 📚 参考链接

- [Air gap (networking) - Wikipedia](https://en.wikipedia.org/wiki/Air_gap_(networking))
- [Атака RAMBO: данные с изолированного компьютера уходят... | Дзен](https://dzen.ru/a/aubB8-AcSRbSDOVn)
- [Researchers turn RAM into radio antenna, beaming... | Cybernews](https://cybernews.com/security/researchers-turn-air-gapped-system-ram-into-radio-antenna/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[talon8635]: These and other methods are good reason to believe that AI can never be 100% contained, which gives me pause. The famous air gap case is stuxnet, but there are other technical and biological approaches. It’s a very weird reality we’ve found ourselves in if you stop, zoom out about, and really take in the gravity of the issues we are grappling with as a human race. Exciting, truly, and a bit nerve wracking.

[andai]: Does any information leak along the power line? I remember having some device back in the day that let me create a LAN through my apartment&#x27;s electric wiring. I&#x27;m wondering if anything ends up back there thru the PSU during normal use of a computer, or if the high frequency components get filtered out. (Though maybe secure computers do things differently with the power as well?)

[TGower]: Cool paper even if the attack isn&#x27;t practical, requiring getting the malware on the computer and a SDR antenna within 7 meters with clear line of sight of the affected computer for 100 bits per second (less after applying error correction). Hard to imagine a scenario where you can pull off both of those, but you couldn&#x27;t plug in a USB, grab the PC, or record the screen directly.

[WalterBright]: Devices like routers should have firmware in memory that has read-only access. The access should be turned on or off by a physical switch. This way, if malware gets installed on your router, doing a cold boot will eliminate it. You can have a timer to just cold boot it regularly. I&#x27;ve suggested this many times. The rationale for not doing it is so the firmware can be remotely updated. Well, that&#x27;s exactly how malware infects it.

[Grimeton]: There are tons of ways to make air gappped systems transmit data. They all include the installation of some malware and have become more expensive and less usable over time. Back in the day with crt screens you could just capture the frequencies transmitted when creating the picture and look at the copy straight away. No malware. No direct contact. And it worked over rather big distances.

</details>
