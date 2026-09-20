---
layout: default
title: "互联网审查测量工具"
date: 2026-09-20T12:00:00+00:00
discovered_date: 2026-09-20
slug: 2026-09-20-measure-internet-censorship
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该工具通过检查IP可达性来测量互联网审查，使用ICMP ping等技术来确定目的地是否可访问。 它在Hacker News上获得了中等关注度，并能够提供有关网络级审查的见解，这是互联网自由的一个关键但往往被忽视的方面，因此它很重要。 该工具在宽松的许可证下是开源的，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，标准计算机即可。"
tags: "Censorship, Internet, Network, Privacy, Tools"
---

# 互联网审查测量工具


> 该工具通过检查IP可达性来测量互联网审查，使用ICMP ping等技术来确定目的地是否可访问。 它在Hacker News上获得了中等关注度，并能够提供有关网络级审查的见解，这是互联网自由的一个关键但往往被忽视的方面，因此它很重要。 该工具在宽松的许可证下是开源的，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，标准计算机即可。


**项目链接**：https://ooni.org/install
**作者**：Bluestein
**发布时间**：2026-09-19T20:00:59Z
**挖掘日期**：2026-09-20
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Censorship, Internet, Network, Privacy, Tools


## 📌 项目详解

该工具通过检查IP可达性来测量互联网审查，使用ICMP ping等技术来确定目的地是否可访问。 它在Hacker News上获得了中等关注度，并能够提供有关网络级审查的见解，这是互联网自由的一个关键但往往被忽视的方面，因此它很重要。 该工具在宽松的许可证下是开源的，目前处于alpha阶段，部署复杂度适中，没有特定的硬件要求，标准计算机即可。


## 🌐 背景与生态

互联网审查测量工具对于理解网络限制至关重要，特别是在互联网自由受限的地区。该项目专注于IP可达性，与平台级审查测量相比，这是一个利基领域。


## 💬 社区讨论

社区评论指出了域名选择中的偏差问题，以及该工具无法测量平台级审查的局限性，尽管其他人认为它有效地实现了其预期目的。


## 🚀 应用前景

该工具可用于研究人员、人权组织和网络管理员监测审查模式。潜在应用包括学术研究和互联网自由倡导。


## 🔧 技术栈

技术栈包括Python、用于网络诊断的ICMP，以及用于数据可视化的网络界面，未提及特定框架依赖。


## 🎯 上手难度

入门评级为进阶；前提条件包括Python 3.6+、基本的网络知识，以及安装OONI探测应用程序。


## 👥 目标用户

主要目标用户是研究人员、网络工程师和隐私倡导者，他们需要工具来评估网络可访问性和审查。


## ⚖️ 类似项目对比

竞品包括Censored Planet和IODA，它们提供更广泛的审查测量，但缺乏OONI的IP可达性关注。


## 📚 参考链接

- [Measuring Internet Censorship: Challenges, Trends, and Impact | ISOC Pulse](https://pulse.internetsociety.org/en/blog/2026/05/measuring-internet-censorship-challenges-trends-and-impact/)
- [Measuring Censorship - Pluggable Transports](https://www.pluggabletransports.info/measuring/)
- [IP Reachability Detection](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_Gaia_Advanced_Routing_AdminGuide/Topics-GARG/IP-Reachability-Detection.htm)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[mitxela]: There&#x27;s a pretty bad bias problem here because the probe app scans domains that are frequently blocked in dictatorships, but doesn&#x27;t scan domains that are frequently blocked in &quot;democracies&quot;, like Anna&#x27;s Archive. Then it ends up looking like the dictatorship countries have all the censorship.

[howunfortunate]: Hmm. I&#x27;d wager the vast majority of internet censorship is  within platform , like that done by Reddit mods. The most egregious example I&#x27;ve seen in my lifetime was when old Twitter decided to censor a NYPost article, down to blocking sharing in  DMs . It seems that type of example is entirely missed here. Is there any attempt to capture that signal?

[walrus01]: For everyone in this thread saying &quot;but the platforms!&quot;, I don&#x27;t disagree with you. Extensive censorship exists. But I don&#x27;t believe that&#x27;s the intended purpose of this tool and the metrics it collects. It doesn&#x27;t measure censorship at what we would call layers 4-7 in the OSI model. It&#x27;s concerned with IP reachability and layer 3. It collects valid data for that purpose.

[sandeepkd]: I really wonder if anyone installs it on their machine. May be I am one off but I am Hearing about this for first time, don&#x27;t recognize any of their partners.

[Panzerschrek]: Pretty strong censorship. That&#x27;s why I can&#x27;t even open this link in my country.

</details>
