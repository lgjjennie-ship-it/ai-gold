---
layout: default
title: "云flare的AI流量阻止选项"
date: 2026-07-26T12:00:00+00:00
discovered_date: 2026-07-26
slug: 2026-07-26-cloudflare-s-new-ai-traffic-options-for-customers
source: hackernews
category: show-hn
ai_score: 9.0
summary: "云flare推出新的AI流量选项，默认阻止新域名的训练和代理爬虫，同时允许搜索，旨在减少AI抓取并增强用户隐私。 该项目因在Hacker News上高社区参与度而具有重要意义，并通过提供对AI流量的增强控制来解决开发者和企业的一个关键痛点，具有通过SaaS或API模式清晰的盈利潜力。 这些选项对所有Cloudflare客户都可用，并在区域设置中配置，无需额外的硬件要求。"
tags: "AI, Traffic, Cloudflare, Scraping, Privacy"
---

# 云flare的AI流量阻止选项


> 云flare推出新的AI流量选项，默认阻止新域名的训练和代理爬虫，同时允许搜索，旨在减少AI抓取并增强用户隐私。 该项目因在Hacker News上高社区参与度而具有重要意义，并通过提供对AI流量的增强控制来解决开发者和企业的一个关键痛点，具有通过SaaS或API模式清晰的盈利潜力。 这些选项对所有Cloudflare客户都可用，并在区域设置中配置，无需额外的硬件要求。


**项目链接**：https://blog.cloudflare.com/content-independence-day-ai-options/
**作者**：alphabetatango
**发布时间**：2026-07-25T22:50:49Z
**挖掘日期**：2026-07-26
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：AI, Traffic, Cloudflare, Scraping, Privacy


## 📌 项目详解

云flare推出新的AI流量选项，默认阻止新域名的训练和代理爬虫，同时允许搜索，旨在减少AI抓取并增强用户隐私。 该项目因在Hacker News上高社区参与度而具有重要意义，并通过提供对AI流量的增强控制来解决开发者和企业的一个关键痛点，具有通过SaaS或API模式清晰的盈利潜力。 这些选项对所有Cloudflare客户都可用，并在区域设置中配置，无需额外的硬件要求。


## 🌐 背景与生态

云flare的AI流量选项是在AI抓取成为网站所有者主要关注问题时推出的，该公司正将自己定位为内容独立性的领导者。


## 💬 社区讨论

社区评论表达了混合情绪，有些人对新的选项感到兴奋，而其他人则对Cloudflare在对抗AI抓取的军备竞赛中的作用表示怀疑。


## 🚀 应用前景

这些选项可应用于各个行业以防止AI抓取，可能带来基于SaaS或API的盈利模式。


## 🔧 技术栈

技术栈涉及Cloudflare现有的基础设施和规则引擎，没有特别提到额外的技术。


## 🎯 上手难度

入门评级为入门级，除了拥有Cloudflare账户外，无需特定先决条件。


## 👥 目标用户

目标用户包括关注AI抓取和内容隐私的网站所有者、开发者和企业。


## ⚖️ 类似项目对比

竞品包括提供AI流量管理的其他CDN提供商，如Akamai和Amazon CloudFront。


## 📚 参考链接

- [Your site, your rules: new AI traffic options for all customers](https://blog.cloudflare.com/content-independence-day-ai-options/)
- [Search, Agent, Training: what Cloudflare 's AI bot taxonomy means for...](https://apogeewatcher.hashnode.dev/cloudflare-ai-bot-taxonomy-search-agent-training-monitoring)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[simonw]: The big news here is that Googlebot will be blocked from September 15th onwards by one the &quot;block training&quot; policies, because Google use the same crawler infrastructure for their search index AND for training Gemini: &gt; Another change that will apply on September 15 is that multi-purpose crawlers (specifically those that combine Search with Training) will be allowed&#x2F;blocked according to all of their behaviors, in line with our call for transparency for website owners. Since t...

[tekacs]: &gt; For all new domains onboarding to Cloudflare, the categories of Training and Agent will be blocked by default on the pages that display ads, while Search will remain allowed by default. It&#x27;s kind of exhausting seeing Cloudflare playing both sides of the arms race. I just can&#x27;t imagine bringing myself to use their technology to build agents and build AI products when they&#x27;re also doing things like this. &gt; This also lines up the incentive model we want to foster. Losing t...

[fc417fc802]: Please consider installing one of the many PoW schemes such as anubis rather than use these cloudflare &quot;features&quot;. I increasingly encounter outright blocks rather than any sort of captcha when visiting cloudflare &quot;protected&quot; sites. Each individual site isn&#x27;t particularly important to me but it&#x27;s depressing to watch the process unfold like this. You really are choosing to erode the core basis of the internet if you go this route.

[noduerme]: I wonder if this has anything to do with the cf bug that stripped all POST data from requests to a SPA I manage for 4-5 hours last week. That was a real good time, figuring out that it wasn&#x27;t trying to show challenges or anything. Default setting for any web app protection from cloudflare should always be &quot;off&quot; unless you&#x27;re under attack, and then who knows what settings will or won&#x27;t break your configuration.

[holografix]: What’s the end goal for Cloudflare and the web here? I don’t think ADOG (anthropic, deepmind, openai, google) is going to pay to crawl. What would force their hand? It’s more likely they’ll strike undisclosed agreements with major sources of discussion like reddit etc. That’s not to say getting new information as a way of context-providing is not going to happen but that’s not scraping.

</details>
