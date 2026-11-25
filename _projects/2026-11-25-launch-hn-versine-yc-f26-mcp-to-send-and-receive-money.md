---
layout: default
title: "Versine：AI驱动的金融交易"
date: 2026-11-25T12:00:00+00:00
discovered_date: 2026-11-25
slug: 2026-11-25-launch-hn-versine-yc-f26-mcp-to-send-and-receive-money
source: hackernews
category: show-hn
ai_score: 9.0
summary: "Versine是一个MCP，允许用户通过AI驱动的对话或短信发送和请求金钱，并与钱包和稳定币集成。 Versine解决了AI代理在金融交易中的真实痛点，通过集成稳定币和一次性密码批准，采用了一种新颖的方法，并且通过SaaS或API模型具有明确的盈利潜力。 在开放协议下许可，Versine已投入生产，部署复杂度适中，需要自托管稳定币钱包和与AI平台的集成。"
tags: "AI, Financial, MCP, Stablecoins, Payments"
---

# Versine：AI驱动的金融交易


> Versine是一个MCP，允许用户通过AI驱动的对话或短信发送和请求金钱，并与钱包和稳定币集成。 Versine解决了AI代理在金融交易中的真实痛点，通过集成稳定币和一次性密码批准，采用了一种新颖的方法，并且通过SaaS或API模型具有明确的盈利潜力。 在开放协议下许可，Versine已投入生产，部署复杂度适中，需要自托管稳定币钱包和与AI平台的集成。


**项目链接**：https://news.ycombinator.com/item?id=50634426
**作者**：harshithl1777
**发布时间**：2026-11-24T20:44:15Z
**挖掘日期**：2026-11-25
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Financial, MCP, Stablecoins, Payments


## 📌 项目详解

Versine是一个MCP，允许用户通过AI驱动的对话或短信发送和请求金钱，并与钱包和稳定币集成。 Versine解决了AI代理在金融交易中的真实痛点，通过集成稳定币和一次性密码批准，采用了一种新颖的方法，并且通过SaaS或API模型具有明确的盈利潜力。 在开放协议下许可，Versine已投入生产，部署复杂度适中，需要自托管稳定币钱包和与AI平台的集成。


## 🌐 背景与生态

MCP（模型上下文协议）已成为金融系统中AI集成的标准，实现了实时数据处理。Versine通过允许AI代理安全地管理金融交易来利用这一点。


## 💬 社区讨论

社区评论对一次性密码批准和声明转发功能表示兴奋，并建议在USDC上赚取收益并将市场扩展到英国。


## 🚀 应用前景

Versine可以解决实际世界的团体财务管理问题，例如分摊账单或结算债务，在金融科技和电子商务等行业中具有SaaS或API盈利潜力。


## 🔧 技术栈

Versine使用Python，与ChatGPT和Claude等AI平台集成，并利用Base上的稳定币（USDC）进行交易。


## 🎯 上手难度

入门评级为进阶，需要Python 3.8+版本、GPU和API密钥进行初始设置。


## 👥 目标用户

目标用户包括金融科技领域的个人开发者、企业团队和研究人员，角色如后端工程师和机器学习从业者。


## ⚖️ 类似项目对比

竞品包括PayPal传统支付和其他基于MCP的解决方案，如OpenBudget个人财务管理。


## 📚 参考链接

- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
- [What is MCP in banking and why is it replacing traditional RPA?](https://rootstack.com/en/blog/what-mcp-banking-and-why-it-replacing-traditional-rpa)
- [What Is MCP for Personal Finance? A Plain-English Guide](https://www.openbudget.sh/blog/what-is-mcp-model-context-protocol-and-what-does-it-mean-for-your-personal-finances)

<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Harshith, Param, and Vishnu and we&#x27;re building Versine (<a href="https:&#x2F;&#x2F;versine.com">https:&#x2F;&#x2F;versine.com</a>). Versine lets you send and request money just by talking or texting with your AI (think Venmo with an MCP). We’re software engineers who have worked on distributed systems at Stripe, Databricks, and Amazon.<p>Versine is an MCP that sits in front of a wallet with a balance. With it, your agent can do things like:<p>- Send money to someone with your approval (via passkey in our app)<p>- Send and request money to&#x2F;from up to 100 people at once<p>- Send money to people without a Versine account (they cash out to their bank in 2 mins)<p>- Pay people without your explicit approval to trusted contacts (you can set this)<p>Here’s a demo: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;Q9X7zioEqi0" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;Q9X7zioEqi0</a><p>We started working on this because assistants are frustratingly hands-off when it comes to finance and money movement. You can have your assistant go through a receipt and map out all the amounts owed taking care of splitting the subtotal, taxes, tips, but at the end of it the assistant hands back work to you when you have to go out and make the Venmo transfer.<p>Our current solution is oriented towards power users: those who want to automate everything through their agent use us to split dinners, group trips, or settle poker ledgers. We see ourselves unlocking more value for the general consumer as<p>1. More people turn into power users of agents, and
2. We expand to a more complete banking solution: deposits, transfers, wires, everything you can (and more) do with your bank offered as an MCP.<p>Behind the scenes, each user has a self-custodial stablecoin wallet storing USDC on Base. With self-custodial wallets, users own their keys, meaning money can’t be sent without their approval.<p>Interestingly, we were almost forced into this solution because we had around 4 weeks to build this product (after a pivot), and traditional fiat with a partner bank would have caused far too many regulatory and compliance slowdowns.<p>Because of that, the only fast option that remained was using stablecoin wallets. It also ensures we aren&#x27;t a Money Services Business (MSB) since we don’t hold control or access to the user’s funds.<p>Each call to the wallet creates what we call one-time or recurring standing permissions. For a one-time payment, your agent makes an MCP call, and you receive a notification in our mobile app. Once you swipe up in the app and approve with a passkey (or your device’s biometric method), we create a one-time permission that instructs your wallet to send $X to your recipient’s address.<p>Trusted contacts let your agent send money to people that you’ve previously authorized without explicit passkey approval. Generally, these are people that you’d trust to send your money back even if your agent made a mistake.<p>We’re also able to support sending money to someone off Versine using claim forwarding, where the user authorizes us to forward a specific amount to a future address (which we create once we verify a recipient&#x27;s OTP).<p>Param worked on scaling vector search at Databricks and harness evals at Glean. Harshith worked on core Stripe Connect fee-processing infrastructure and built an AWS Fargate autoscaler at Amazon. Vishnu worked on intent-based agent testing infrastructure at Amazon. None of us were experienced in stablecoin or crypto infra before working on Versine but our distributed systems experience has helped us a lot.<p>We&#x27;d love for you guys to try it! It&#x27;s available on iOS and Android and as an MCP on ChatGPT and Claude. We also support a public MCP and REST API for other agents.<p>Please let us know how you find it and if it works as you&#x27;d hoped!<p><a href="https:&#x2F;&#x2F;versine.com">https:&#x2F;&#x2F;versine.com</a>


--- Top Comments ---

[olliem36]: Congrats on the launch! Limits and passkey approval are cool. Earning yield on USDC would be cool, Privy (now part of Stripe) can route balances into lending vaults such as Morpho, allowing you to retain part of the yield. Are you planning to launch in the UK? I’d love to try it! Disclosure: I work at Tuppence (tuppence.ai), which provides virtual cards and on ramping for AI agents. If cards are on your roadmap, I’d be happy to compare notes or make an intro to the Privy team if that’s useful!

[atakanelik]: Congratz on the launch I hope it&#x27;ll be good for you guys. I used to work on fraud and chargebacks at a payments company. The hard part was never sending the money, it was the dispute after. If an agent pays the wrong person, what does the reversal flow look like here?

[pr337h4m]: If you&#x27;re using stablecoins and self-custody, why is the product US-only? That&#x27;s a bit of a shame :(

[vlkvklv]: Congratulations, great launch! So, you are basically building on a Paypal model, but with agents and USDC inside. I find it cool that you can send the money to the bank, not only to the other wallet. That differentiates Versine from pure agentic wallets, which are plenty. And the communication layer to the people outside Versine seems solidly built.
One question: you perform stablecoin&lt;-&gt;fiat transfers and the service looks custodial (as I understood, it is not, but sometimes you have t...

</details>
