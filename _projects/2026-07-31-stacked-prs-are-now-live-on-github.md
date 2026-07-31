---
layout: default
title: "GitHub堆叠PR发布"
date: 2026-07-31T12:00:00+00:00
discovered_date: 2026-07-31
slug: 2026-07-31-stacked-prs-are-now-live-on-github
source: hackernews
category: show-hn
ai_score: 8.0
summary: "堆叠PR将多个pull请求在GitHub上组合成一个可管理的单元，简化了开发工作流程。 此功能解决了管理多个相关PR的痛点，显示出强烈的社区兴趣，有582个星和195条评论，表明了提高工作流程效率的潜力。 该功能处于公共预览状态，有积极的发展轨迹，尽管报告了一些合并问题。它需要GitHub帐户访问，没有特定的硬件要求。"
tags: "GitHub, PR, Development, Workflow, Collaboration"
---

# GitHub堆叠PR发布


> 堆叠PR将多个pull请求在GitHub上组合成一个可管理的单元，简化了开发工作流程。 此功能解决了管理多个相关PR的痛点，显示出强烈的社区兴趣，有582个星和195条评论，表明了提高工作流程效率的潜力。 该功能处于公共预览状态，有积极的发展轨迹，尽管报告了一些合并问题。它需要GitHub帐户访问，没有特定的硬件要求。


**项目链接**：https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
**作者**：tomzorz
**发布时间**：2026-07-30T16:26:16Z
**挖掘日期**：2026-07-31
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：GitHub, PR, Development, Workflow, Collaboration


## 📌 项目详解

堆叠PR将多个pull请求在GitHub上组合成一个可管理的单元，简化了开发工作流程。 此功能解决了管理多个相关PR的痛点，显示出强烈的社区兴趣，有582个星和195条评论，表明了提高工作流程效率的潜力。 该功能处于公共预览状态，有积极的发展轨迹，尽管报告了一些合并问题。它需要GitHub帐户访问，没有特定的硬件要求。


## 🌐 背景与生态

GitHub的pull请求是核心协作工具，堆叠PR通过允许批量处理增强了这一点，符合提高开发者工作流程的趋势。


## 💬 社区讨论

社区反馈既强调了兴奋也指出了问题，特别是合并堆叠和组件方法。团队正在积极寻求反馈。


## 🚀 应用前景

这可以显著提高软件开发中的团队协作，特别是对于大型项目。潜在的应用案例包括SaaS开发和开源项目。


## 🔧 技术栈

该功能是GitHub的原生功能，除了需要GitHub帐户外，不需要特定的技术堆栈。它与现有的GitHub工作流程集成。


## 🎯 上手难度

入门评级为入门级。用户需要一个GitHub帐户，可以直接从GitHub界面开始堆叠PR。


## 👥 目标用户

目标用户包括软件开发人员，特别是那些在团队中或从事大规模项目的人员。它对企业和开源环境都很有用。


## ⚖️ 类似项目对比

竞品包括传统的pull请求管理工具，如GitHub自己的PRs和第三方解决方案，例如GitLab的合并请求。


## 📚 参考链接

- [GitHub Stacked PRs | GitHub Stacked PRs](https://github.github.com/gh-stack/)
- [Using stacked pull requests in GitHub - LogRocket Blog](https://blog.logrocket.com/using-stacked-pull-requests-in-github/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[matharmin]: I&#x27;ve been using the preview for a bit, and I&#x27;m quite surprised to see them expanding the preview with so many unfixed issue. For example, merging an entire stack is completely broken in many cases:  https:&#x2F;&#x2F;github.com&#x2F;github&#x2F;gh-stack&#x2F;discussions&#x2F;212  You can merge one by one, but if you&#x27;re using squash and merge, you need a re-approval for each PR in the stack if you require reviews. This makes you lose out on arguably the biggest gain of stacked P...

[necovek]: I dislike them reinforcing the component approach to delivering work through their examples, like the top screenshot showing &quot;database schema changes&quot;, &quot;api changes&quot; and &quot;frontend implementation&quot; as separate branches in a stack. So really, one does consider full stack a single feature, but unless they are reviewed in one go — which defeats the purpose of stacked branches and pull requests — you can end up landing one and a later review in branches higher in the s...

[sameenkarim]: Hey from the GitHub Stacked PRs team! Excited to release this more broadly so anyone can start stacking:  https:&#x2F;&#x2F;gh.io&#x2F;stacks  Would love to hear any feedback, especially with the UI and CLI. We&#x27;ve got a lot more updates to the PR experience in store! Also happy to answer questions about the design decisions we made. There&#x27;s a bunch happening behind the scenes, and it&#x27;s one of the largest launches in GitHub history covering almost every service from Actions and ...

[Okkef]: What&#x27;s the benefit of this type of stacked PRs over a well-curated set of commits, and reviewing per commit? I think the bigger problem is that big AI PR&#x27;s need a different way of reviewing. For example, the order in which the diff&#x27;s are shown can make a big difference in how easy the commits are to read (e.g., function definition change first, then all call sites, then the tests). Or maybe we should go to a system where diffs &amp; comments are intertwined, a bit like how &quo...

[steveklabnik]: This is one of the biggest changes to hit GitHub in many years. I&#x27;m really glad to see something like this deployed to one of the largest forges in the world, hopefully it will expose a lot of developers to workflows that they didn&#x27;t even know about before. If you buy the idea that stacking produces better software, then this also has the opportunity to really help out quite a few people.

</details>
