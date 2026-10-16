---
layout: default
title: "RPKI保护主要互联网路由"
date: 2026-10-16T12:00:00+00:00
discovered_date: 2026-10-16
slug: 2026-10-16-rpki-now-protects-70-of-internet-routes
source: hackernews
category: show-hn
ai_score: 7.0
summary: "RPKI（资源公共密钥基础设施）通过验证路由原点，使用加密方法保护了70%的互联网路由，防止未经授权的路由宣布。 该项目因其高采用率和积极的社区参与而具有重要意义，解决了互联网路由中的一个关键安全问题，并提供了通过SaaS或API服务进行货币化的潜在机会。 RPKI遵循宽松的许可证，目前处于生产使用中，部署复杂度适中，没有特定的硬件要求。它与现有的BGP基础设施集成以进行路由验证。"
tags: "Internet Security, RPKI, Network Routing, Cybersecurity, Technology"
---

# RPKI保护主要互联网路由


> RPKI（资源公共密钥基础设施）通过验证路由原点，使用加密方法保护了70%的互联网路由，防止未经授权的路由宣布。 该项目因其高采用率和积极的社区参与而具有重要意义，解决了互联网路由中的一个关键安全问题，并提供了通过SaaS或API服务进行货币化的潜在机会。 RPKI遵循宽松的许可证，目前处于生产使用中，部署复杂度适中，没有特定的硬件要求。它与现有的BGP基础设施集成以进行路由验证。


**项目链接**：https://ipinfo.io/blog/rpki-protects-70-internet-routes
**作者**：emot
**发布时间**：2026-10-16T00:52:35Z
**挖掘日期**：2026-10-16
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Internet Security, RPKI, Network Routing, Cybersecurity, Technology


## 📌 项目详解

RPKI（资源公共密钥基础设施）通过验证路由原点，使用加密方法保护了70%的互联网路由，防止未经授权的路由宣布。 该项目因其高采用率和积极的社区参与而具有重要意义，解决了互联网路由中的一个关键安全问题，并提供了通过SaaS或API服务进行货币化的潜在机会。 RPKI遵循宽松的许可证，目前处于生产使用中，部署复杂度适中，没有特定的硬件要求。它与现有的BGP基础设施集成以进行路由验证。


## 🌐 背景与生态

RPKI是互联网安全框架的一部分，旨在通过确保IP地址前缀由授权实体宣布来防止路由攻击。随着BGP劫持和其他路由漏洞的解决方案，该技术获得了关注。


## 💬 社区讨论

社区评论强调了对注册机构法律压力的担忧以及政府干预的可能性，同时强调了采用ASPA进行路由验证的重要性以及各国采用率的差异。


## 🚀 应用前景

RPKI在增强企业和服务提供商的网络安全方面具有强大的应用前景。它可以用于构建路由验证的SaaS服务，为网络运营商提供API服务，并提高关键基础设施部门的安全性。


## 🔧 技术栈

技术栈包括BGPsec等加密协议，与DNS和IP路由协议的集成，以及依赖于RPKI服务器和BGP路由器等基础设施。


## 🎯 上手难度

使用RPKI的入门难度被评为进阶。前提条件包括了解BGP和DNS，访问RPKI服务器，以及熟悉加密工具。步骤包括配置您的网络以使用RPKI进行路由验证。


## 👥 目标用户

目标用户包括网络工程师、网络安全专业人员以及希望增强其路由安全的企业。后台工程师和DevOps团队可以从实施RPKI中受益。


## ⚖️ 类似项目对比

竞争项目包括用于增强BGP安全的BGPsec和基于RPKI的路由原点授权（ROA）路由验证解决方案。这些替代方案侧重于路由安全的不同方面，但服务于类似的目的。


## 📚 参考链接

- [What Is RPKI and Why It Matters for... - InterLIR networks marketplace](https://interlir.com/2026/05/28/rpki-route-origin-authorization-internet-routing-security/)
- [Resource Public Key Infrastructure ( RPKI ) — RIPE Network...](https://www.ripe.net/manage-ips-and-asns/resource-management/rpki/)
- [What Is RPKI ? How RPKI and ROA Secure BGP - LARUS](https://larus.net/blog/what-is-rpki/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[cowlevel]: My concern about RPKI is legal pressure on the registries. By centralising all of Russia&#x27;s allowed routes on a database server in the Netherlands  and automatically enforcing it , it&#x27;s trivial for the Dutch government to cut off Russia&#x27;s internet access by tampering with that database.

[1473-bytes]: A couple years ago our org made a big push to have our routes and our downstream customer routes RPKI valid. It&#x27;s good to see the high adoption rate. It looks like ASPA is now available for ASN path validation. Probably should look at adopting ASPA at some point here.

[0xbadcafebee]: &gt; Much of the jump came from one country: China went from 3.7% of its IPv4 addresses in valid routes to 83.0%, almost 60% of the global gain counted by addresses. Interesting. China may have predicted cyber attacks in the near future. Or perhaps are readying for retaliation. It&#x27;s possible their military or intelligence branches didn&#x27;t anticipate this getting published. (Unless somebody knows if this year just happened to be when they decided to implement cyber reforms?) Hey, IPIn...

[est]: so is there a public service that can verify some IP block belongs to which country&#x2F;cert? whois is so deprecated.

[innovayse]: Does the data show how RPKI adoption varies across countries in the Caucasus and former Soviet Union? I’d be curious to see how Armenia and its neighboring countries compare.

</details>
