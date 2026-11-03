---
layout: default
title: "AI驱动的QA代理进行错误检测"
date: 2026-11-03T12:00:00+00:00
discovered_date: 2026-11-03
slug: 2026-11-03-launch-hn-momentic-yc-w24-agents-that-catch-bugs-by-using-your-app
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Momentic利用AI代理自动测试Web、iOS、Android和桌面应用程序，通过探索和交互捕获错误，无需编写脚本。 Momentic解决了手动软件测试的痛点，具有高人气（146星，97条评论），并提供了一种新颖、可扩展的方法，具有明确的SaaS盈利模式。 Momentic遵循MIT许可，已投入生产，部署复杂度适中，需要云基础设施和API访问；支持主要平台，但目前不支持真实设备移动测试。"
tags: "AI, Testing, QA, Agents, DevTools"
---

# AI驱动的QA代理进行错误检测


> Momentic利用AI代理自动测试Web、iOS、Android和桌面应用程序，通过探索和交互捕获错误，无需编写脚本。 Momentic解决了手动软件测试的痛点，具有高人气（146星，97条评论），并提供了一种新颖、可扩展的方法，具有明确的SaaS盈利模式。 Momentic遵循MIT许可，已投入生产，部署复杂度适中，需要云基础设施和API访问；支持主要平台，但目前不支持真实设备移动测试。


**项目链接**：https://momentic.ai/
**作者**：wuweiweiwu
**发布时间**：2026-11-02T17:05:25Z
**挖掘日期**：2026-11-03
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Testing, QA, Agents, DevTools


## 📌 项目详解

Momentic利用AI代理自动测试Web、iOS、Android和桌面应用程序，通过探索和交互捕获错误，无需编写脚本。 Momentic解决了手动软件测试的痛点，具有高人气（146星，97条评论），并提供了一种新颖、可扩展的方法，具有明确的SaaS盈利模式。 Momentic遵循MIT许可，已投入生产，部署复杂度适中，需要云基础设施和API访问；支持主要平台，但目前不支持真实设备移动测试。


## 🌐 背景与生态

软件测试领域随着AI发展有所演变，但手动脚本仍然繁琐。Momentic利用LLM和基于代理的测试，受GPT-3浏览器等项目的启发，自动化了该过程。


## 💬 社区讨论

社区反馈提出了关于开源替代方案、部署成本和移动支持的问题，对定价和性能的看法不一。


## 🚀 应用前景

非常适合寻求自动化QA的企业和开发人员，尤其是在Web和移动应用测试领域。在软件质量保证方面具有SaaS服务潜力，可应用于金融、电子商务和医疗保健行业。


## 🔧 技术栈

使用Python构建，利用Codex和Claude等LLM，并与Playwright集成以实现浏览器自动化，以及云基础设施以实现可扩展性。


## 🎯 上手难度

进阶难度。需要Python 3.8+和GPU以加快处理速度，以及API密钥；设置涉及配置代理框架并运行初始测试。


## 👥 目标用户

面向后端工程师、QA团队和DevOps专业人士，特别是在Web和移动应用开发领域工作的人员。


## ⚖️ 类似项目对比

竞争对手包括用于手动测试的Playwright/Selenium，以及Devin和Claude Code等AI代理，尽管Momentic在召回率和代理协调方面表现优异。


## 📚 参考链接

- [DeepSWE measures frontier coding agents on original, long-horizon...](https://deepswe.datacurve.ai/)

<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Wei-Wei and Jeff. We’re building Momentic, QA agents that autonomously plan, explore, and bug-bash controls and user flows in your web, iOS, Android, and (soon) desktop apps to catch bugs.<p>Here’s a demo: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;BFsM-Se1Fh8" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;BFsM-Se1Fh8</a><p>We’re both software engineers that spent our careers on dev tooling and infra across companies like Robinhood, Retool, WeWork, and Qualtrics. Testing was always a pain in the ass (esp Playwright and Selenium), so we built agents to do it for us.<p>Modern day software has a ton of bugs and the change failure rate is only growing faster as coding agent adoption scales. LLMs are really good at generating code, but reinforce their own assumptions, write a ton of useless tests, and are bad at visual understanding. On DeepSWE v1.1, Sonnet 5.5 hit 66.2% pass rate when banned from writing tests, versus 65.3% when allowed.<p>OSS end-to-end testing frameworks like Playwright, Selenium, or Maestro force you to hardcode implementation details like XPath, text, or aria-* attributes in your tests. Even with agents, these take a nontrivial amount of time and tokens to build and maintain.<p>In 2023, we saw Nat Friedman drive a browser with GPT-3 via natbot. We were inspired to use this technology to automate the most painful and tedious parts of software engineering: testing. We started with using LLMs to generate and maintain Playwright, but quickly realized that those primitives were fundamentally misaligned with the agentic SDLC. We think the future of QA is agents testing themselves, not writing scripts.<p>Mo is a custom agent harness for catching bugs that builds on the past 3 years of Momentic and millions of test traces from complex, real-world applications. Mo is built for recall: it finds the most real bugs, though Codex is a bit more precise at 86% vs 84%. The tradeoff is cost: Mo costs $2.67 per bug vs $0.80 for Codex, less than Claude Code and Devin.<p>- Self-organizing agent graph. Mo builds a directed acyclic graph (DAG) as it explores. Large product areas automatically fork into parallel sub-agents, each with their own browser or device for concurrent execution.<p>- Specialized agents for domain specific tasks. Planner agents reason over screenshots and video while dedicated locator agents inspect page structure to resolve plain-English interaction targets. Others include image analysis, video understanding, audio generation, and more.<p>- Parallel agents coordinate through cooperative resource leases. Agents can announce that they’re “using” or “modifying” overlapping resources or fixtures. Multiple “using” claims can coexist, but only a single “modifying” claim can be active on any particular one.<p>- Scaled infrastructure. Mo ships with a tunnel that lets users expose private sites and local apps to our hosted agents and infra. A single bug bash can spin up 100s of concurrent browsers and devices.<p>We benchmarked Mo against coding agents on 4 popular open-source apps: Gitea (58.8k stars), Metabase, Twenty (YC), and Saleor, with 1,396 human-labeled bugs. Each agent got the same brief, a fresh E2B sandbox, and no access to source code. Codex and Claude Code used hosted Browserbase browsers, while Devin used its built-in browser. For evaluators, we implemented LLM as a judge (GPT-6.1 Sol) with a human reviewer.<p>Results from a time-boxed 60-minute run:<p>- Mo: 269 bugs, 19.3% recall, 84% precision, $2.67 per bug<p>- Codex (GPT-6.1 Sol + Playwright MCP): 86 bugs, 6.2% recall, 86% precision, $0.80 per bug<p>- Claude Code (Opus 5.5 + Playwright MCP): 59 bugs, 4.2% recall, 80% precision, $4.09 per bug<p>- Devin: 27 bugs, 1.9% recall, 84% precision, $3.89 per bug<p>Mo finds more bugs the more time it has. From 30 to 60 minutes, it went from 177 to 269 bugs (+52%), while Codex gained only 16%.<p>Results: <a href="https:&#x2F;&#x2F;momentic.ai&#x2F;qa-bench">https:&#x2F;&#x2F;momentic.ai&#x2F;qa-bench</a><p>Write-up: <a href="https:&#x2F;&#x2F;momentic.ai&#x2F;blog&#x2F;qa-bench">https:&#x2F;&#x2F;momentic.ai&#x2F;blog&#x2F;qa-bench</a><p>Dataset: <a href="https:&#x2F;&#x2F;huggingface.co&#x2F;datasets&#x2F;momentic&#x2F;qa-bench" rel="nofollow">https:&#x2F;&#x2F;huggingface.co&#x2F;datasets&#x2F;momentic&#x2F;qa-bench</a><p>Harness: <a href="https:&#x2F;&#x2F;github.com&#x2F;momentic-ai&#x2F;qa-bench" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;momentic-ai&#x2F;qa-bench</a><p>We just shipped PR testing for Vercel and Cloudflare deploy previews and we’re giving every new signup $250 in Mo spend. Paid plans have higher infra capacity and included usage along with options to top up.<p>We’d love for you to try it out and give us feedback. Feel free to comment here, we’ll be around all day!


--- Top Comments ---

[JulianPaul]: Why is this better than running Opus 5.5 directly against my app with a custom Playwright-based harness for in my own subscription?

[beavisringdin]: Questions: - I would always pick an open source tool I can strap to my custom harness over using a service like this. Do you somehow expect that no such competitor will arrive that performs as well? - If you are YC 2024 what have you been doing for 2 years? - The real edge here would be supporting mobile development builds on real devices, is this on your roadmap and if so what&#x27;s your plan to support it? In that case I would pay for this if you handled the real device on your end.

[podoman]: &gt; Mo is a custom agent harness for catching bugs that builds on the past 3 years of Momentic and millions of test traces from complex, real-world applications. Mo is built for recall: it finds the most real bugs, though Codex is a bit more precise at 86% vs 84%. The tradeoff is cost: Mo costs $2.67 per bug vs $0.80 for Codex, less than Claude Code and Devin. is this good? so Mo costs more money per bug? I&#x27;m confused.

[vfosnar]: &gt; Momentic invited you to work together so apparently they automatically hand over your email to Slack to contact you upon login even tho I don&#x27;t remember this being mentioned anywhere at all. I went to check the Momentic settings and theres a Notifications section with Slack turned off... used my public email so idc but others may

[AgentMasterRace]: I used this service very briefly, but it&#x27;s too slow as it relies on the cloud and it&#x27;s way too expensive since most developers use a subscription service. Even just Claude with basic prompts is better, but even better with skills.. and then even better with maestro scripts.

</details>
