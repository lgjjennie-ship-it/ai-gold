---
layout: default
title: "Bullet：一个更快的编码代理"
date: 2026-08-14T12:00:00+00:00
discovered_date: 2026-08-14
slug: 2026-08-14-launch-hn-bullet-yc-s26-a-faster-coding-agent
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Bullet是一个AI驱动的编码代理，旨在通过优化模型路由、目标代码搜索、上下文清理和高效轮次来提高编码效率和速度。 Bullet在Hacker News上获得了高分，并得到了积极的社区反馈，通过旨在成为更快的编码代理来解决开发人员的实际问题，表明其实用价值，并有可能作为SaaS或API进行商业化。 Bullet在MIT许可证下是开源的，目前处于生产成熟度，部署复杂度适中，没有特定的硬件要求，标准开发环境即可。"
tags: "AI, Coding, Agent, Productivity, SaaS"
---

# Bullet：一个更快的编码代理


> Bullet是一个AI驱动的编码代理，旨在通过优化模型路由、目标代码搜索、上下文清理和高效轮次来提高编码效率和速度。 Bullet在Hacker News上获得了高分，并得到了积极的社区反馈，通过旨在成为更快的编码代理来解决开发人员的实际问题，表明其实用价值，并有可能作为SaaS或API进行商业化。 Bullet在MIT许可证下是开源的，目前处于生产成熟度，部署复杂度适中，没有特定的硬件要求，标准


**项目链接**：https://www.codewithbullet.com/
**作者**：adi1
**发布时间**：2026-08-13T08:14:30Z
**挖掘日期**：2026-08-14
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Coding, Agent, Productivity, SaaS


## 📌 项目详解

Bullet是一个AI驱动的编码代理，旨在通过优化模型路由、目标代码搜索、上下文清理和高效轮次来提高编码效率和速度。 Bullet在Hacker News上获得了高分，并得到了积极的社区反馈，通过旨在成为更快的编码代理来解决开发人员的实际问题，表明其实用价值，并有可能作为SaaS或API进行商业化。 Bullet在MIT许可证下是开源的，目前处于生产成熟度，部署复杂度适中，没有特定的硬件要求，标准开发环境即可。


## 🌐 背景与生态

AI编码代理生态系统经历了显著增长，Claude Code和Codex较为突出。Bullet通过专注于减少往返次数和优化编码速度来区分自己。


## 💬 社区讨论

社区评论对Bullet的速度改进表示兴奋，并讨论了它与其他编码代理（如Codex）相比的潜力。


## 🚀 应用前景

Bullet可以应用于需要快速编码和调试的场景，如软件开发、数据工程和人工智能研究，通过SaaS或API模型具有商业化潜力。


## 🔧 技术栈

Bullet使用Python，并依赖于大型语言模型如Codex，基础设施包括Docker和高效的上下文管理。


## 🎯 上手难度

入门评级为进阶，需要标准Python环境和基本的AI编码代理熟悉度。步骤包括克隆仓库并运行设置脚本。


## 👥 目标用户

目标用户包括软件开发和数据科学行业的后端工程师、机器学习实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Claude Code和Codex，Bullet的区别在于其对速度和往返次数减少的关注。其他相关项目是Codex CLI和Cursor。


## 📚 参考链接

- [21 Best AI Coding Agents in 2026 — Agentic.ai](https://agentic.ai/best/coding-agents)
- [Best AI Coding Agents for 2026: 12 Tools Compared - Tembo](https://www.tembo.io/blog/top-coding-agent-tools)
- [Claude Code vs Codex: What I Learned After 100+ Hours With Both (2026) | Composio](https://composio.dev/content/claude-code-vs-openai-codex)

<details><summary>📄 查看原文内容</summary>


Hi HN! We’re Adi and Alex, founders of Bullet, a faster coding agent.<p>Bullet started in a senior year dorm. We were fresh out of working at AppLovin and Citadel, and naturally thought we were on a sure path to startup success. We were going to use our skills optimizing stock pricing calculation speeds and agent document context to take over the world. So, Bullet started as an AI hedge fund, a browser-use agent, synthetic financial data (oof), a mobile IDE, and a bunch of other things. We wanted to build something people wanted, but it seemed like everything we built was just terrible, useless, or both.<p>So, we decided to do something completely different, something completely out of the blue, something that no one had ever done before. Solve a problem we actually had.<p>Over the course of six pivots, we suffered. Throughout all of our adventures, one final boss kept getting in our way. Claude Code and his little brother Codex. We were spending hours waiting for coding agents like Claude Code and Codex, and got so frustrated to the point that I downloaded the Claude Code whip. We had spent months of time waiting for six codebases-worth of useless coding agent work.<p>Lightbulb moment. There’s nothing more noble than destroying the institutions! Let’s take on Claude Code and Codex, we can do it! Piece of cake!<p>And so, Bullet started off as a side project. We used the Claude Code to improve the Claude Code:<p>1. Model routing. Do you regret giving a task to Fable when it could have literally been done by Sonnet?<p>2. Targeted code + context search. We think embedding the whole repo is dumb. We also think sticking the whole context (or compressed context) in chat is dumb. So we do faster and better greps over both.<p>3. Aggressive context hygiene. Tool output is bounded, stale screenshots disappear, we don’t re-read files…the garbage never floods the model.<p>4. Efficient turns. Batch independent investigation, make one surgical edit, then perform one focused verification. Internal measurement showed 16% fewer round trips and 27% lower cost.<p>5. The Flash. We prayed to Barry Allen for speed.<p>And thank the Flash, he gave us speed! On SWE-bench Verified, Bullet resolved 479&#x2F;500 (95.8%) in one attempt, averaging 119s per task, 35–67% faster than mini-SWE-agent + Fable&#x2F;Sol depending on task. Full results and methodology here (<a href="https:&#x2F;&#x2F;www.codewithbullet.com&#x2F;blog&#x2F;benchmark-results.html" rel="nofollow">https:&#x2F;&#x2F;www.codewithbullet.com&#x2F;blog&#x2F;benchmark-results.html</a>)<p>Eventually we started using it every day and never went back.<p>Listed above were just some of the things about Claude Code that frustrated us the most, but we are constantly optimizing every day (look at that, maybe we did learn something from our jobs).<p>In our development, the biggest insight was that model speed matters less than reducing round trips. Independent searches, reads, and commands should happen in parallel, while dependent editing and verification stay sequential. One surprising obstacle was code search, small issues like regex-dialect mismatches caused silent misses and sent agents down completely wrong paths, so we built targeted search with fallbacks and bounded context. The most interesting use case so far has been long iterative work (like benchmarks, data pipelines, and evaluation loops), where each step depends on the last and running multiple agents can’t help as much.<p>Here’s the video demo (<a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=rWVmG5fRKgE" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=rWVmG5fRKgE</a>)<p>We hope that you guys try out Bullet if you are suffering with speed as much as we were, and we hope it brings you joy, rainbows, and faster responses. And if it’s terrible, let us know it’s terrible (we’re masochists btw)! We&#x27;ll be in the comments all day, you can also contact us at bullet@davidhf.com.<p>You can try it at <a href="https:&#x2F;&#x2F;codewithbullet.com" rel="nofollow">https:&#x2F;&#x2F;codewithbullet.com</a>.<p>P.S: we hid a code on the website, see if you can unlock the secret page at the footer, all built with Bullet


--- Top Comments ---

[andai]: 35% faster than swe-mini-agent, nice. You say this is due to somehow parallelizing operations? I&#x27;m using a custom harness based on swe-mini-agent (actually its little brother, their tutorial [0]) and found it way faster than codex (for small tasks) despite being &quot;just bash&quot; in a while loop. The main difference is that I do the opposite of what you said, i.e. I do dump the context in the prompt. You don&#x27;t need to grep for what&#x27;s right in front of you :) But my repos ar...

[seizethecheese]: This is a promising direction! Unfortunately, I think the benchmark result here is essentially meaningless. I recently discovered this same lesson the hard way. I was trying to get a multi-agent system I was building to improve upon GPQA  Diamond scores (system here:  http:&#x2F;&#x2F;pellmell.ai ). No matter how hard I tried, I could not get any lift. When Fable 5 dropped, it also did not improve upon Opus, and I realized my mistake. The benchmark was saturated! Now, looking at the result he...

[throw03172019]: &gt; Bullet started as an AI hedge fund, a browser-use agent, synthetic financial data (oof), a mobile IDE, and a bunch of other things. Is there another pivot coming? This would make me nervous.

[andai]: I expected Download to take me to a page with options, but it downloaded a 200MB .dmg file onto my Android phone.

[karanraina]: I use codex cli. It doens&#x27;t have a UI for linux. I use opencode for that but it doens&#x27;t work that well with the new 5.6 model suite from openai. Codex is both faster and better. 
I would have loved if there was a way to use a GUI that worked like codex. Gave this a try. I think this might be it. Please consider atleast adding MCP support if you can. That&#x27;ll help

</details>
