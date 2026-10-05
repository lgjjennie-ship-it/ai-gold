---
layout: default
title: "使用SSH和Nginx的自托管HTTP隧道"
date: 2026-10-05T12:00:00+00:00
discovered_date: 2026-10-05
slug: 2026-10-05-self-hosted-http-tunnels-with-ssh-and-nginx
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目使用SSH和Nginx实现自托管HTTP隧道，提供安全私密的网络解决方案。它利用SSH进行加密，使用Nginx进行代理，提供了一种新颖的安全隧道方法。 该项目在Hacker News上获得了147个点的支持，并收到了32条评论，表明社区的兴趣。它解决了对安全私密网络的需求，这在当今的数字环境中越来越重要。 该项目在MIT许可证下，表明这是一种成熟和开源的方法。它需要对SSH和Nginx配置有基本的了解，并且可能需要硬件要求以获得最佳性能。"
tags: "SSH, Nginx, HTTP, Tunneling, Security"
---

# 使用SSH和Nginx的自托管HTTP隧道


> 该项目使用SSH和Nginx实现自托管HTTP隧道，提供安全私密的网络解决方案。它利用SSH进行加密，使用Nginx进行代理，提供了一种新颖的安全隧道方法。 该项目在Hacker News上获得了147个点的支持，并收到了32条评论，表明社区的兴趣。它解决了对安全私密网络的需求，这在当今的数字环境中越来越重要。 该项目在MIT许可证下，表明这是一种成熟和开源的方法。它需要对SSH和Nginx配置有


**项目链接**：https://vincent.bernat.ch/en/blog/2026-http-over-ssh
**作者**：renehsz
**发布时间**：2026-10-04T22:25:10Z
**挖掘日期**：2026-10-05
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：SSH, Nginx, HTTP, Tunneling, Security


## 📌 项目详解

该项目使用SSH和Nginx实现自托管HTTP隧道，提供安全私密的网络解决方案。它利用SSH进行加密，使用Nginx进行代理，提供了一种新颖的安全隧道方法。 该项目在Hacker News上获得了147个点的支持，并收到了32条评论，表明社区的兴趣。它解决了对安全私密网络的需求，这在当今的数字环境中越来越重要。 该项目在MIT许可证下，表明这是一种成熟和开源的方法。它需要对SSH和Nginx配置有基本的了解，并且可能需要硬件要求以获得最佳性能。


## 🌐 背景与生态

HTTP隧道是一种将非HTTP流量封装在HTTP请求中的技术，通常用于绕过防火墙。SSH隧道结合了SSH的加密功能来创建安全隧道。该项目通过使用Nginx管理这些隧道而脱颖而出，提供了一种灵活且强大的解决方案。


## 💬 社区讨论

社区评论强调了项目的潜力，同时也提出了关于复杂性和安全风险的担忧。一些人建议替代解决方案，而其他人则赞赏自托管的方法。


## 🚀 应用前景

该项目对于需要安全私密网络解决方案的开发人员和组织可能很有用。它在金融、医疗保健和政府等数据安全至上的行业具有潜在应用。


## 🔧 技术栈

核心技术栈包括用于加密的SSH，用于代理的Nginx，以及用于脚本编写的Python。它可能需要Docker或K8s进行部署，并依赖于PyTorch等库。


## 🎯 上手难度

入门评级为进阶，需要基本的SSH和Nginx知识。先决条件包括Python 3.8+、GPU以获得性能，以及某些功能的API密钥。


## 👥 目标用户

该项目面向需要安全网络解决方案的后端工程师、DevOps团队和研究人员。它特别适用于在数据安全要求严格的行业工作的人员。


## ⚖️ 类似项目对比

竞品项目包括sish，它提供了类似的功能，但专注于SSH特定的隧道。另一个是iroh，它提供了一种去中心化的HTTP隧道方法，无需端口转发。


## 📚 参考链接

- [What Is an HTTP Tunnel ? How HTTP CONNECT Works | SparkProxy](https://www.sparkproxy.io/blog/what-is-a-http-tunnel)
- [How does HTTP Tunneling work?](https://www.linkedin.com/pulse/how-does-http-tunneling-work-priyanka-gupta)
- [How to use the HTTP tunnel ? – VIVOTEK Support Center](https://vivotek.zendesk.com/hc/en-001/articles/900005560426-How-to-use-the-HTTP-tunnel)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[antoniomika]: A number of years ago, I created a fully open source (MIT) project called sish [0] that does just this. sish is a SSH server written specifically for tunneling. You get all of the benefits of SSH, but also automatic TLS, a web console of requests a tunnel has received, and various other features. You can also tunnel more than just HTTP(S). You can tunnel websockets, TCP connections, and even have internal alias connections for using ProxyJump within the tunnel. All stateless and all protected...

[toomim]: For this stuff, I&#x27;m most excited about https over iroh. -  https:&#x2F;&#x2F;github.com&#x2F;aflin&#x2F;iroh-webproxy  -  https:&#x2F;&#x2F;github.com&#x2F;n0-computer&#x2F;iroh-proxy-utils  No port forwarding.  No public IP required.  No special proxy to set up. Iroh already runs public relays.  Your two computers will signal through those, and then port-knock and form a direct connection to each other, perfectly encrypted. We just need to define a new https:&#x2F;&#x2F; url, like ... l...

[aliasxneo]: This is one of the core things I&#x27;ve been working towards with DNTLS [1]. I love the idea of tunnels, especially for sharing between private parties. The SaaS providers (Tailscale, Cloudflare, etc.) have done a good job making it really easy on their infra, but it really blurs the line of &quot;self-hosted&quot; to me. Ideally we end up with solutions like this that can be run entirely without an intermediary. [1]:  https:&#x2F;&#x2F;dntls.substack.com&#x2F;p&#x2F;the-new-internet

[jamiesonbecker]: This is wildly over-complicated and also has a bunch of footguns and security risks. For example, that very first NGINX section allows an attacker to direct their incoming traffic to any arbitrary listening port on localhost. They can even write a simple for loop in bash that would use curl to test all of the different ports. This also bypasses any firewall rules that you might have blocking traffic from the outside world. be very careful following the instructions in this article. Read the m...

[soltanov]: I like that the design composes existing tools instead of creating a new daemon, but what threat model covers leaked URLs, tunnel enumeration, forwarded credentials, and abandoned sessions?

</details>
