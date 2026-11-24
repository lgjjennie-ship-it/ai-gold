---
layout: default
title: "Stalwart：Exchange即插即用替代品"
date: 2026-11-24T12:00:00+00:00
discovered_date: 2026-11-24
slug: 2026-11-24-stalwart-is-now-a-drop-in-replacement-for-microsoft-exchange
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Stalwart是一个用Rust编写的开源邮件服务器，它作为Microsoft Exchange的即插即用替代品，提供JMAP、IMAP4、POP3、SMTP、CalDAV、CardDAV和WebDAV支持。 Stalwart在Hacker News上获得了564个评分和301条评论，高人气表明它解决了企业从Microsoft Exchange迁移的实际需求。它通过SaaS或高级功能许可提供了明确的盈利路径。 Stalwart在Apache License 2.0下许可，目前处于生产成熟度，部署复杂度适中。它需要标准服务器硬件，并与现代邮件协议集成。"
tags: "Email, Server, OSS, Microsoft, Migration"
---

# Stalwart：Exchange即插即用替代品


> Stalwart是一个用Rust编写的开源邮件服务器，它作为Microsoft Exchange的即插即用替代品，提供JMAP、IMAP4、POP3、SMTP、CalDAV、CardDAV和WebDAV支持。 Stalwart在Hacker News上获得了564个评分和301条评论，高人气表明它解决了企业从Microsoft Exchange迁移的实际需求。它通过SaaS或高级功能许可提供了明确


**项目链接**：https://stalw.art/blog/microsoft-exchange-replacement/
**作者**：shaunpud
**发布时间**：2026-11-23T22:32:29Z
**挖掘日期**：2026-11-24
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Email, Server, OSS, Microsoft, Migration


## 📌 项目详解

Stalwart是一个用Rust编写的开源邮件服务器，它作为Microsoft Exchange的即插即用替代品，提供JMAP、IMAP4、POP3、SMTP、CalDAV、CardDAV和WebDAV支持。 Stalwart在Hacker News上获得了564个评分和301条评论，高人气表明它解决了企业从Microsoft Exchange迁移的实际需求。它通过SaaS或高级功能许可提供了明确的盈利路径。 Stalwart在Apache License 2.0下许可，目前处于生产成熟度，部署复杂度适中。它需要标准服务器硬件，并与现代邮件协议集成。


## 🌐 背景与生态

Microsoft Exchange几十年来一直是主导的邮件服务器，但其主导地位正在减弱，因为更多企业寻求开源替代品。Stalwart通过提供一个安全、可扩展且易于操作的邮件服务器来填补这一空白。


## 💬 社区讨论

社区评论从对与Outlook的兼容性感到兴奋到对监管功能和迁移路径的担忧不等。有些人已经在使用它，而其他人则要求更多高级功能。


## 🚀 应用前景

Stalwart可以为从Exchange迁移的企业解决实际问题，特别是在对电子邮件保留有严格要求的行业。潜在产品包括SaaS电子邮件服务和企业协作工具。


## 🔧 技术栈

核心技术栈包括用于性能的Rust，用于协议的JMAP、IMAP4、POP3、SMTP、CalDAV、CardDAV和WebDAV，以及用于部署的Docker。


## 🎯 上手难度

难度：进阶。前提条件包括Linux服务器、Python 3.8+和Docker。大致步骤：安装Docker，拉取Stalwart镜像，并配置网络设置。


## 👥 目标用户

目标用户包括企业IT团队、系统管理员以及希望从Microsoft Exchange迁移的企业。


## ⚖️ 类似项目对比

类似项目包括Postfix、Exim和Microsoft Exchange Online。Stalwart通过提供更好的Outlook集成和更现代的功能集而有所不同。


## 📚 参考链接

- [Stalwart Mail & Collaboration Server](https://stalw.art/)
- [18 Best Open Source Microsoft Exchange Alternatives (2026)](https://opensourceprojects.cc/alternatives/microsoft-exchange)
- [Best Exchange Server Alternative in 2026: The Complete Guide](https://www.systoolsgroup.com/updates/exchange-server-alternatives/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[egorfine]: &gt; the new Outlook sends the IMAP server name, the user name and the password to Microsoft This is... incredible. To say the least.

[rmoriz]: The only issue is regulatory: As a freelancer or company in Germany, you have to archive mail in a way that can’t be deleted or altered and store it for access by the tax authorities for up to 10 years (“GoBD”). Stalwart does not have this feature in their regular plans (or the OSS variants)

[hobo123]: I don&#x27;t get it. They say that Outlook will no longer support Exchange on premise, only Cloud. So how will all their customers use Stalwart then, which is a drop-in replacement? Shouldn&#x27;t they first switch to another client (Outlook copy or Thunderbird)?

[andreashaerter]: The lock-in effect is inherent to the protocol and the clients. Furthermore, supporting MAPI and similar standards merely buys time and saves on licensing costs when your target is OSS. While I recognize the practical benefit for an administrator, in my view, anything that expands the protocol stack surrounding Microsoft email ultimately does a disservice to the remainder of the still-existing, open email ecosystem.

[markstos]: Stalwart is the mail server Mozilla’s Thundermail uses.

</details>
