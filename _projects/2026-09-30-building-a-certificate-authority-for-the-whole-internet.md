---
layout: default
title: "云flare的互联网证书颁发机构"
date: 2026-09-30T12:00:00+00:00
discovered_date: 2026-09-30
slug: 2026-09-30-building-a-certificate-authority-for-the-whole-internet
source: hackernews
category: show-hn
ai_score: 8.0
summary: "云flare正在构建自己的证书颁发机构，为互联网提供安全可靠的证书，采用ACME和MTC标准。 该项目具有重要意义，因为云flare的高关注度、与其现有安全产品的一致性，以及通过SaaS和API服务实现盈利的潜力。 该项目已投入生产，采用宽松的许可证，但面临与现有生态系统集成和潜在信任碎片化的挑战。"
tags: "CA, Security, Web, Trust, Certificates"
---

# 云flare的互联网证书颁发机构


> 云flare正在构建自己的证书颁发机构，为互联网提供安全可靠的证书，采用ACME和MTC标准。 该项目具有重要意义，因为云flare的高关注度、与其现有安全产品的一致性，以及通过SaaS和API服务实现盈利的潜力。 该项目已投入生产，采用宽松的许可证，但面临与现有生态系统集成和潜在信任碎片化的挑战。


**项目链接**：https://blog.cloudflare.com/cloudflare-certificate-authority/
**作者**：ewpratten
**发布时间**：2026-09-29T13:44:00Z
**挖掘日期**：2026-09-30
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：CA, Security, Web, Trust, Certificates


## 📌 项目详解

云flare正在构建自己的证书颁发机构，为互联网提供安全可靠的证书，采用ACME和MTC标准。 该项目具有重要意义，因为云flare的高关注度、与其现有安全产品的一致性，以及通过SaaS和API服务实现盈利的潜力。 该项目已投入生产，采用宽松的许可证，但面临与现有生态系统集成和潜在信任碎片化的挑战。


## 🌐 背景与生态

证书颁发机构对于网络安全至关重要，云flare的行动符合PKI领域更集中控制和盈利的趋势。


## 💬 社区讨论

社区反应包括支持云flare在Let's Encrypt财务上的独立性，对信任碎片化的担忧，以及建议与顶级域名运营商合作。


## 🚀 应用前景

该证书颁发机构可以增强网站和服务的安全性，特别是在需要高信任度的行业，如金融和医疗保健，通过SaaS/API实现盈利。


## 🔧 技术栈

技术栈可能包括ACME用于发行，MTC用于传统支持，以及云flare现有的基础设施用于部署。


## 🎯 上手难度

入门难度为进阶；前提条件包括熟悉ACME和MTC，步骤涉及使用云flare的工具配置证书颁发机构。


## 👥 目标用户

目标用户是后端工程师、安全团队和企业，特别是在金融和电子商务领域需要可信证书的人。


## ⚖️ 类似项目对比

竞品包括Let's Encrypt、DigiCert和Sectigo，它们提供类似的证书颁发服务，但在定价、支持和集成选项上有所不同。


## 📚 参考链接

- [Certificate authority - Wikipedia](https://en.wikipedia.org/wiki/Certificate_authority)
- [What is a Certificate Authority? CA's Explained - DigiCert](https://www.digicert.com/blog/what-is-a-certificate-authority)
- [What Is a Certificate Authority ? Role, Work & PKI Trust Hierarchies](https://certera.com/blog/what-is-a-ca-certificate-authority-role-pki-trust-hierarchies/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[vg]: A very welcome move because for years Cloudflare has freeloaded certs from Let&#x27;s Encrypt without sponsoring Let&#x27;s Encrypt finacially. Though Cloudflare has contributed in otherwise to the ecosystem like by running CT logs etc. Now, it looks like WebPKI is going to fracture into two regarding PQ Crypto. With Google (GTS and Chrome), Cloudflare and Let&#x27;s Encrypt all preferring MTC and legacy CA&#x27;s like Digicert, Sectigo, Globalsign all heading towards non MTC. If Cloudflare w...

[chaz6]: The article contains conflicting statements: &gt; anyone already pointed at any existing free CA can move to us by changing a directory URL, with no new tooling and nothing to re-architect. &gt; We will only issue to clients that support ACME Renewal Information (ARI), standardized in RFC 9773. I do not think both can be true.

[MisterMunchkin]: It makes sense for them to issue their own certificates because it’s inline with the rest of their offerings, but it seems kind of strange you can just buy someone else’s root certificate and issue under their name. It kind of defeats the point of trusting the root. What if a bad actor starting buying up authorities? You could compromise a bunch of services without them even knowing.

[phillipseamore]: Would like to see them working more with TLD operators here, I&#x27;d like to see a CA partner with TLD ops to offer distributed and resilient issuance (especially with shorter cert lifetimes) with intermediate certificates locked to their TLDs, TLD operators are already a significant part of the chain of trust since it&#x27;s all based on DNS today.

[bossyTeacher]: The internet was meant to be a decentralized network. Why are humans so narrow minded short-termists?

</details>
