---
layout: default
title: "HTTP2Shell：Brotli库漏洞利用"
date: 2026-10-25T12:00:00+00:00
discovered_date: 2026-10-25
slug: 2026-10-25-node2shell-evolves-to-http2shell-blast-radius-affects-many-http-libs-and-apps
source: hackernews
category: show-hn
ai_score: 8.0
summary: "HTTP2Shell 识别并利用 Brotli 压缩库中的漏洞，可能导致远程代码执行，主要关注 HTTP 环境。 该项目因其高参与度（307 分，152 条评论）和在 HN 上的讨论而具有重要意义，解决了广泛使用的库（Brotli）中的关键安全问题，并具有通过安全补丁或 SaaS 解决方案进行货币化的潜力。 该项目是开源的，采用宽松的许可证，针对使用 Brotli 的库，部署复杂度因目标应用程序而异。"
tags: "Vulnerability, Security, Brotli, RCE, HTTP"
---

# HTTP2Shell：Brotli库漏洞利用


> HTTP2Shell 识别并利用 Brotli 压缩库中的漏洞，可能导致远程代码执行，主要关注 HTTP 环境。 该项目因其高参与度（307 分，152 条评论）和在 HN 上的讨论而具有重要意义，解决了广泛使用的库（Brotli）中的关键安全问题，并具有通过安全补丁或 SaaS 解决方案进行货币化的潜力。 该项目是开源的，采用宽松的许可证，针对使用 Brotli 的库，部署复杂度因目标应用程序而


**项目链接**：https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497
**作者**：theanonymousone
**发布时间**：2026-10-24T08:06:39Z
**挖掘日期**：2026-10-25
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Vulnerability, Security, Brotli, RCE, HTTP


## 📌 项目详解

HTTP2Shell 识别并利用 Brotli 压缩库中的漏洞，可能导致远程代码执行，主要关注 HTTP 环境。 该项目因其高参与度（307 分，152 条评论）和在 HN 上的讨论而具有重要意义，解决了广泛使用的库（Brotli）中的关键安全问题，并具有通过安全补丁或 SaaS 解决方案进行货币化的潜力。 该项目是开源的，采用宽松的许可证，针对使用 Brotli 的库，部署复杂度因目标应用程序而异。


## 🌐 背景与生态

Brotli 由 Google 开发，被广泛用于网络应用程序的压缩。该漏洞最初在 Node.js 应用程序中识别，但随后已扩展到影响更广泛的 HTTP 环境。


## 💬 社区讨论

社区评论反应不一，有些人认为名称具有误导性，而其他人则赞赏漏洞披露，强调需要补丁。


## 🚀 应用前景

该工具可用于审计和 securing 使用 Brotli 压缩的应用程序，在企业安全或 API 监控中具有 SaaS 解决方案的可能性。


## 🔧 技术栈

技术栈包括用于脚本编写的 Python，以及依赖 Brotli 库和 HTTP 请求处理框架。


## 🎯 上手难度

难度：进阶。前提条件包括 Python 3.8+、Brotli 库安装和基本的 HTTP 理解。步骤包括克隆仓库并运行测试。


## 👥 目标用户

目标用户是安全研究员、DevOps 团队和专注于保护 Web 应用程序的企业开发者。


## ⚖️ 类似项目对比

竞品包括 Exploit Database 和专注于压缩库漏洞的商业漏洞扫描工具。


## 📚 参考链接

- [Node 2 Shell Brotli vuln (CVE-2026-111497) evolves to HTTP 2 Shell , as...](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)
- [GitHub - tom7voldemort/ http 2 shell : Simple experimental shell by...](https://github.com/tom7voldemort/http2shell)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[netsharc]: Well, whoever picked the name HTTP2Shell certainly didn&#x27;t use any intelligence, artificial or genuine. It&#x27;s so meaningless, broad and undescriptive of the actual issue. No it probably doesn&#x27;t affect an HTTP server with nothing else behind it, so why is HTTP being blasted? You might as well call it Exploit Pro Max...

[pimterry]: Much prefer the Broccoli2Shell name &amp; site (for the same vuln):  https:&#x2F;&#x2F;broccoli2shell.com&#x2F; . For starters, I&#x27;m pretty sure you can hit this without HTTP if you do any manual Brotli decoding, HTTP just happens to be the most common case that comes up.

[nayuki]: I see some irony here. For a period of time, Google chose not to include JPEG XL in Chrome because vulnerabilities in the library could compromise the software - a legitimate concern. Yet, Google is the author of the Brotli data compression format a decade before the JPEG XL drama, and was happy to use it in Chrome and encourage others to use the library, despite the fact that it also increases the attack surface.

[Rapzid]: &gt; reported it as unauthenticated remote code execution that works in both directions &gt; but it wasn&#x27;t recognized as a security issue at the time and no release shipped with the fix until now I&#x27;m always getting my dangerous RCE bugs mixed up with my harmless RCE bugs. I&#x27;m curious how this was reported and fixed back in Feb but nobody recognized the importance. A case of AI automation and nobody at the wheel?

[bawolff]: To me, the surprising part is how many of these implement brotli compression of request (not just response) bodies, given how obscure a feature that is. In any case all this sensationalism is starting to get annoying. Patch your stuff and move on. Edit: actually, between all the sensationalism, its hard to tell from the article how many of these actually support brotli compressed request bodies in common configs vs some other use of brotli (which is bad but nowhere near as critical)

</details>
