---
layout: default
title: "新型伪造1024位RSA签名方法"
date: 2026-09-25T12:00:00+00:00
discovered_date: 2026-09-25
slug: 2026-09-25-forging-1024-bit-rsa-signatures-in-nearly-snfs-time-pdf
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目介绍了一种新型方法，以几乎与整数筛法（SNFS）相同的速度伪造1024位RSA签名，利用Joux-Naccache-Thomé算法而不对模数进行因式分解。 它因高关注度（63分，11条评论）及其对密码安全的影响而具有重要意义，突出了当前RSA实践中一个关键漏洞，尽管它需要RSA预言机，限制了直接盈利。 该项目处于alpha阶段，操作需要RSA预言机，部署复杂度中等，未提及特定硬件要求。"
tags: "Cryptography, RSA, Security, Cryptanalysis, Breakthrough"
---

# 新型伪造1024位RSA签名方法


> 该项目介绍了一种新型方法，以几乎与整数筛法（SNFS）相同的速度伪造1024位RSA签名，利用Joux-Naccache-Thomé算法而不对模数进行因式分解。 它因高关注度（63分，11条评论）及其对密码安全的影响而具有重要意义，突出了当前RSA实践中一个关键漏洞，尽管它需要RSA预言机，限制了直接盈利。 该项目处于alpha阶段，操作需要RSA预言机，部署复杂度中等，未提及特定硬件要求。


**项目链接**：https://eprint.iacr.org/2026/2131.pdf
**作者**：int0x29
**发布时间**：2026-09-24T14:26:32Z
**挖掘日期**：2026-09-25
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Cryptography, RSA, Security, Cryptanalysis, Breakthrough


## 📌 项目详解

该项目介绍了一种新型方法，以几乎与整数筛法（SNFS）相同的速度伪造1024位RSA签名，利用Joux-Naccache-Thomé算法而不对模数进行因式分解。 它因高关注度（63分，11条评论）及其对密码安全的影响而具有重要意义，突出了当前RSA实践中一个关键漏洞，尽管它需要RSA预言机，限制了直接盈利。 该项目处于alpha阶段，操作需要RSA预言机，部署复杂度中等，未提及特定硬件要求。


## 🌐 背景与生态

RSA仍然是密码学的基石，但1024位密钥越来越容易受到攻击。该项目基于Joux等人在2007年的工作，展示了密码分析理论突破的实际影响。


## 💬 社区讨论

开发者对理论和实践意义感到兴奋，指出其对RSA预言机的依赖以及未来算法改进的潜力。


## 🚀 应用前景

这可能影响依赖1024位RSA的行业，如金融和政府，通过强制密钥升级和推动对更安全密码解决方案的需求。


## 🔧 技术栈

技术栈涉及Joux-Naccache-Thomé算法，利用数学原理，没有特定的框架或硬件依赖。


## 🎯 上手难度

难度：进阶。前提条件包括理解RSA和访问RSA预言机。步骤包括设置预言机和运行伪造算法。


## 👥 目标用户

目标用户是安全研究人员、密码学家以及仍有系统使用1024位RSA的 enterprises。


## ⚖️ 类似项目对比

竞品包括传统的因式分解方法如SNFS和其他RSA伪造技术如Boneh-Franklin攻击。


## 📚 参考链接

- [Sieve theory - Wikipedia](https://en.wikipedia.org/wiki/Sieve_theory)
- [Forging 1024 - bit RSA signatures in nearly SNFS... | E-Ink News Daily](https://news.e-ink.me/en/archive/2026-09-25/article/forging-1024-bit-rsa-signatures-in-nearly-snfs-time)

<details><summary>📄 查看原文内容</summary>


<a href="https:&#x2F;&#x2F;arstechnica.com&#x2F;security&#x2F;2026&#x2F;09&#x2F;theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before&#x2F;" rel="nofollow">https:&#x2F;&#x2F;arstechnica.com&#x2F;security&#x2F;2026&#x2F;09&#x2F;theres-a-new-way-to...</a>


--- Top Comments ---

[tptacek]: The most important thing to know about this work, which is awesome, is that it relies on access to a raw RSA oracle, where you have a public key and an API that allows you to directly do RSA operations with the corresponding key. The idea is that you then lose access to the oracle, and thus to the private key, but you&#x27;ve gained enough information from your session with the oracle to make forgeries in the future. So it&#x27;s not a straightforward general-purpose RSA-1024 signature break;...

[yababa_y]: in the PDF metadata we find the proper and appropriate title of this work:       Nearly SNFS-Speed Signature Forgery Sans Factoring N (NSNFSSSFSFN)

[RossBencina]: I was expecting to see mention of Microsoft&#x2F;Apple executable code-signing in the examples. I know key lengths are well beyond 1024 now, but on the Microsoft side it was (is?) possible for USB tokens to be distributed in the mail. What I don&#x27;t know is whether the tokens could be used as oracles in this attack.

[nk_kolja]: I was unaware of snfs algorithms for generic moduli and&#x2F;or signatures. Very nice. 
The theoretical result is purely due to the 2007 Joux et al. paper. 
What’s new is the implementation and the 1024-bit rsa signature forgery. Also no ai, so we can expect some speedups soon. I really didn’t expect rsa to be targeted so much this year. Hope that these results will motivate people to pursue algorithmic improvements!

[benmmurphy]: nice poem at the end of the paper

</details>
