---
layout: default
title: "Almanac：AI公司知识代理"
date: 2026-09-01T12:00:00+00:00
discovered_date: 2026-09-01
slug: 2026-09-01-launch-hn-almanac-yc-s26-ai-that-knows-your-company
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Almanac 是一个AI代理，通过整合多个模型，将信息组织成个人和公司维基，以提供针对公司特定查询的上下文感知响应。 Almanac 解决了公司对上下文感知AI代理的需求痛点，具有高人气（53星，47条评论），并拥有清晰的SaaS盈利模式，其新颖的内存和上下文处理方法使其脱颖而出。 Almanac 处于开发阶段（alpha阶段），注重集成复杂性和硬件需求，提供个人和共享账户，支持一键连接到各种账户。"
tags: "LLM, Agent, RAG, Code, Tools"
---

# Almanac：AI公司知识代理


> Almanac 是一个AI代理，通过整合多个模型，将信息组织成个人和公司维基，以提供针对公司特定查询的上下文感知响应。 Almanac 解决了公司对上下文感知AI代理的需求痛点，具有高人气（53星，47条评论），并拥有清晰的SaaS盈利模式，其新颖的内存和上下文处理方法使其脱颖而出。 Almanac 处于开发阶段（alpha阶段），注重集成复杂性和硬件需求，提供个人和共享账户，支持一键连接到各种账


**项目链接**：https://usealmanac.com/
**作者**：kushagrchitkar
**发布时间**：2026-08-31T15:34:34Z
**挖掘日期**：2026-09-01
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, RAG, Code, Tools


## 📌 项目详解

Almanac 是一个AI代理，通过整合多个模型，将信息组织成个人和公司维基，以提供针对公司特定查询的上下文感知响应。 Almanac 解决了公司对上下文感知AI代理的需求痛点，具有高人气（53星，47条评论），并拥有清晰的SaaS盈利模式，其新颖的内存和上下文处理方法使其脱颖而出。 Almanac 处于开发阶段（alpha阶段），注重集成复杂性和硬件需求，提供个人和共享账户，支持一键连接到各种账户。


## 🌐 背景与生态

Almanac 属于AI代理生态系统，满足了企业对上下文感知代理的需求。竞争对手包括 Hermes Agent 和商业解决方案如 Claude 和 Codex，尽管 Almanac 的多模型集成和预编译维基提供了独特优势。


## 💬 社区讨论

社区评论强调了状态持久化、模型使用和上下文失效等挑战，显示出人们对 Almanac 创新方法的既兴奋又怀疑。


## 🚀 应用前景

Almanac 可以解决企业管理中的实际问题，如自动化任务和维护长期项目。其盈利模式包括SaaS服务、API访问和金融、医疗等行业的本地解决方案。


## 🔧 技术栈

Almanac 使用LLM、RAG和Hermes Agent，关键模型如GPT-4，基础设施包括Docker和K8s。它支持多模型集成和自定义API密钥。


## 🎯 上手难度

入门难度为进阶，需要Python 3.8+、GPU和API密钥。步骤包括注册、连接账户和组织维基。


## 👥 目标用户

目标用户是金融和科技行业的 enterprises teams、backend工程师和ML从业者，他们需要上下文感知的AI解决方案。


## ⚖️ 类似项目对比

竞争对手包括 Hermes Agent（开源）和商业解决方案如 Claude 和 Codex。Almanac 的多模型支持和预编译维基使其与众不同。


## 📚 参考链接

- [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
- [What is RAG? - Retrieval-Augmented Generation AI Explained - AWS](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Hermes Agent — Open-Source AI Agent with Memory, Skills, and Cron](https://hermes-agent.ai/)

<details><summary>📄 查看原文内容</summary>


Hi HN, I&#x27;m Kushagra, one of three founders of Almanac, a Hermes with a brain that knows everything about your company.<p>We started our journey with setting up Hermes for our company, thinking it must be easy. We wanted an agent that would know every context about our company, so we could ask questions and get context-appropriate responses to.<p>This started a very annoying and difficult journey. Setting up Hermes, getting it to talk right, building OAuth apps for every connector myself, then feeding it context myself, and ultimately struggling with Hermes&#x27;s default memory. At the same time, we saw our YC batchmates struggling with the same problem, and we saw an opportunity.<p>So we built Almanac. This is how it works. You sign up, you get a Hermes agent straight out of the box. You have a one-click connect to any account (Gmail, Calendar, Granola, PostHog, etc). You have personal accounts (only accessible by you) and also shared accounts (accessible by everyone in the company). The consequence being I can never see my cofounders&#x27; accounts.<p>The “brain” of this agent is wikis. We pull in information from your connected sources, and start organizing this information in two wikis. A personal one, for you, which understands who you are, what your preferences are, the people in your life, and the things going on in your life. The second wiki is a company wiki, which includes what the company is, what you’re working on, what the roadmap is, and what the blockers of the company are. Your agent ultimately has access to these two wikis and the original accounts, which invoke the feeling of “it just knows you.”<p>Here’s a demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ajXP5PHuK18" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=ajXP5PHuK18</a><p>We&#x27;re three cofounders, Rohan, Kushagra, and Divit, and we&#x27;ve been friends for 11 years, since studying for the IIT-JEE. We all did Electrical Engineering (Rohan at IIT Delhi, me at IIT Kharagpur, Divit at BITS Pilani, Hyderabad), and Rohan and I later went to Harvard, where this pre-compilation layer became our capstone thesis. We have built multiple products around the idea of a pre-compiled knowledge layer.<p>Our main differentiating point is the way we approach memory and context in general. Most AI assistant tools treat memory as an afterthought. We have worked on wikis for AI for more than a year now, building products for Harvard and NASA. The one thing we have learnt is that one needs to spend a lot more compute upfront, in the pre-compilation of this knowledge base, to get it right.<p>Having this pre-compiled knowledge base enables a lot of interesting ideas. First is a proactive agent. Since I have compiled what’s going on in both my company and my current life, Almanac can start completing tasks on its own. Concretely, we run a background worker which takes a look at tasks that could be completed, pings the main agent, who then pings me, suggesting which tasks it could automate. As a result, I wake up to proactive notifications which look like “I already prepared a draft of your fundraising pitch deck, want to take a look?”<p>Second, long-horizon tasks. In our wikis, we maintain a section on ongoing projects, so Almanac can pick a task back up days later without losing the thread. Most agents are session-bound: they run once, finish, and forget. But a lot of real work isn&#x27;t one shot; it plays out over hours and days with people in the loop. The clearest example is anything that involves waiting on a human, like scheduling a meeting, following up on a sales thread, or chasing a document. Almanac can send an email on your behalf, and because it&#x27;s always on and remembers the project, it notices the reply four hours later and drafts the right follow-up in context.<p>Since launching, we&#x27;ve seen a lot of use cases for Almanac. One person runs her dog-rescue operation through it: finding available fosters, tracking pickups, and sending reminders for consent forms. Another researches Polymarket strategies with Almanac, where its memory holds what past strategies were, proposes new ones, and compares them against what went right or wrong last time. Another builds marketing campaigns on it without having to re-explain the business and the whole campaign every single time.<p>Regarding privacy and security, Almanac only accesses accounts you explicitly connect. Your OAuth credentials are held by our connection provider, not in Almanac’s database. We only store the wiki and the source behind its citations. So an email used as a citation may be retained as Markdown.<p>We’re live: <a href="https:&#x2F;&#x2F;usealmanac.com">https:&#x2F;&#x2F;usealmanac.com</a>. We have a 7-day trial on all of our plans. Happy to hear if people have done similar setups, and what new features they’d like in Almanac. If you’re a company that wants to get an agent that actually gets tasks done, I would love to talk: <a href="https:&#x2F;&#x2F;cal.com&#x2F;team&#x2F;almanac&#x2F;demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;team&#x2F;almanac&#x2F;demo</a>.


--- Top Comments ---

[sebastienburel]: The hard part for an always-on company agent is what survives a restart. My runtime snapshots the whole JS heap to bytes and restores it in a fresh process, so conversation and working state come back with no serialization code — but timers don&#x27;t survive, so an agent re-arms them from declarative state after restore. How do you handle that? Is a long-lived agent&#x27;s state checkpointed, or rebuilt by replaying context on each wake?

[jedberg]: There is a lot of competition in this space, both commercial companies and open source.  It seems like the biggest advantage for using one of these and not Claude or Codex is that you can use multiple models.  Otherwise, those two have all the same features, or probably will in the next week. Are you able to use multiple models?  Or I guess the first question is, what model(s) are you using?  At this point, many enterprises care so that should be front and center, especially if you&#x27;re us...

[i18ner]: Congrats on the launch, the approach of spending compute upfront is a compelling shift from what the current standard is. I am curious as to how you handle state invalidation and unseen side-channels during those long-running tasks, because if the agent pauses a task for X days, say waiting for an email reply, but the projects params changed offline or in a channel that the agent has no eyes on, how does the system realize that the pre-compiled context has now gone stale? Does that also mean ...

[paidx]: The interesting tradeoff here is not just better retrieval, but whether the pre-compiled wiki makes behavior more predictable over long-running tasks. It would be useful to see comparisons against a plain markdown repo plus Claude&#x2F;Codex: task completion, citation accuracy, stale-context failures, and the cost of keeping the wiki updated. Multi-model support and bring-your-own-key options also seem important for enterprises that don&#x27;t want their company&#x27;s context tied to a singl...

[Grombobulous]: Looks identical to Claude Desktop connectors. My Claude desktop app already talks to Jira, Slack, Outlook, GitHub, etc.

</details>
