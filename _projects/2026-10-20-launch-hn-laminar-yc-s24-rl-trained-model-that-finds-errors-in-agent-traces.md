---
layout: default
title: "Laminar：基于RL训练的AI代理错误检测工具"
date: 2026-10-20T12:00:00+00:00
discovered_date: 2026-10-20
slug: 2026-10-20-launch-hn-laminar-yc-s24-rl-trained-model-that-finds-errors-in-agent-traces
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Laminar利用RL训练的模型检测AI代理追踪中的错误，提供高质量的检测且成本较低，无需采样。 Laminar凭借57星和23条评论获得关注，通过独特的RL方法解决AI可观察性中的关键问题，并具有SaaS变现潜力。 Laminar采用Apache 2.0开源许可，支持自托管，并使用微调的RL模型进行错误检测。它需要Python并集成代理追踪。"
tags: "LLM, Agent, Observability, Tools, AI"
---

# Laminar：基于RL训练的AI代理错误检测工具


> Laminar利用RL训练的模型检测AI代理追踪中的错误，提供高质量的检测且成本较低，无需采样。 Laminar凭借57星和23条评论获得关注，通过独特的RL方法解决AI可观察性中的关键问题，并具有SaaS变现潜力。 Laminar采用Apache 2.0开源许可，支持自托管，并使用微调的RL模型进行错误检测。它需要Python并集成代理追踪。


**项目链接**：https://news.ycombinator.com/item?id=50154029
**作者**：skull8888888
**发布时间**：2026-10-19T16:00:18Z
**挖掘日期**：2026-10-20
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：LLM, Agent, Observability, Tools, AI


## 📌 项目详解

Laminar利用RL训练的模型检测AI代理追踪中的错误，提供高质量的检测且成本较低，无需采样。 Laminar凭借57星和23条评论获得关注，通过独特的RL方法解决AI可观察性中的关键问题，并具有SaaS变现潜力。 Laminar采用Apache 2.0开源许可，支持自托管，并使用微调的RL模型进行错误检测。它需要Python并集成代理追踪。


## 🌐 背景与生态

代理可观察性是一个不断发展的领域，现有工具通常侧重于追踪收集而非分析。Laminar通过使用RL模型深入检查追踪来解决这个问题。


## 💬 社区讨论

社区评论强调了检测细微工具调用错误的需求，以及在实际场景中追踪分析的实用价值。


## 🚀 应用前景

Laminar可用于软件、法律和客户支持行业监控和提升AI代理性能，通过SaaS模式实现变现。


## 🔧 技术栈

Laminar使用Python、RL训练的模型（flow-1）以及Docker等基础设施。它集成代理追踪并以JSON格式返回结果。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、GPU和代理追踪访问权限。步骤涉及克隆仓库并运行设置脚本。


## 👥 目标用户

目标用户是软件开发、客户支持等行业中的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括Hugging Face的Agent Trace和自定义可观察性工具。Laminar通过RL方法和成本效益与其区分。


## 📚 参考链接

- [Reinforcement learning - Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning)
- [Agent tracing overview - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)

<details><summary>📄 查看原文内容</summary>


Hi HN, we’re Robert and Din from Laminar (<a href="https:&#x2F;&#x2F;laminar.sh">https:&#x2F;&#x2F;laminar.sh</a>). We’ve been building open-source observability for AI agents since 2024. Recently, we released flow-1, a model trained with RL to find errors in agent traces. On our benchmark (<a href="https:&#x2F;&#x2F;laminar.sh&#x2F;blog&#x2F;flow-1">https:&#x2F;&#x2F;laminar.sh&#x2F;blog&#x2F;flow-1</a>), it matches GPT-6-sol in detection quality while being 23x cheaper. This makes it affordable to analyze every production agent trace, without sampling.<p>Here’s a one-minute walkthrough: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;KJa3h6ZJNLQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;KJa3h6ZJNLQ</a><p>We also put together a post with example traces and analyses from flow-1 and other models: <a href="https:&#x2F;&#x2F;laminar.sh&#x2F;blog&#x2F;flow-1-in-action">https:&#x2F;&#x2F;laminar.sh&#x2F;blog&#x2F;flow-1-in-action</a><p>Agent observability is crowded, so instead of a bullet list of how Laminar differs from X, we’ll explain how we’re solving agent observability from first principles.<p>Agents now run for many steps and fail implicitly. An agent can click the wrong button or cite the wrong document while every call completes successfully. These errors are the most useful ones to catch and understand. To find them, you need to understand what the agent was trying to do and inspect its LLM calls and tool results. Simply looking at the final agent output is not enough.<p>Collecting traces alone doesn’t solve this. A lot of agent observability platforms are still data collectors at their core. You can end up paying to store traces that nobody has time to read or extract value from.<p>Using another LLM to inspect traces is THE solution, but capable models are expensive at scale and cheaper ones often miss errors or flag unrelated things.<p>So we built our model to solve exactly this problem. We finetuned a small OSS model and then post trained it with RL on thousands of synthetic investigations of realistic agent workflows in software, legal, customer support, etc. We got a model that is both good at agent trace analysis and very cheap to run.<p>flow-1 runs inside a harness we call Signals. It acts as a coding agent, treating an agent trace like a repo, with each span (an LLM call, tool call, etc.) as a file. It starts from a compressed string representation of a full agent trace and a user prompt, then greps across spans and reads the relevant ones in full.<p>The beauty of Signals is that it can respond to a general prompt. You can ask it to identify user frustration, check whether your browser agent completed a checkout, and so on. It’s not limited to raw error detection. It returns findings as JSON in a schema users can freely define. We call these signal events.<p>Once you’re analyzing every trace, you also have too many individual events to read. That’s why we automatically group similar signal events into clusters. You can see recurring problems and how often they happen, then drill into individual events and the traces behind them.<p>You can use traces from a cluster to build an eval dataset for that type of failure. You can then use your favourite coding agent to hillclimb on those evals and check that the fix works across these cases before shipping it to prod.<p>Trace → analyze → catch errors and form clusters → fix → release. Making this loop easy is why we built Laminar.<p>We’ve put the same thought into the rest of Laminar. Our blog (<a href="https:&#x2F;&#x2F;laminar.sh&#x2F;blog">https:&#x2F;&#x2F;laminar.sh&#x2F;blog</a>) explains how looking closely at how agents actually work led us to build 20x trace compression, a custom SQL query engine and automatic task extraction.<p>Laminar is Apache 2.0 and self-hostable (<a href="https:&#x2F;&#x2F;github.com&#x2F;lmnr-ai&#x2F;lmnr" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;lmnr-ai&#x2F;lmnr</a>). We make money from the managed cloud.<p>We’d love to hear how you track your agents’ performance today. How much do you learn from user feedback versus your own monitoring? And when you fix something, how do you check that it hasn’t introduced a different failure?


--- Top Comments ---

[nucleus777]: Interesting. Most of the failures I&#x27;ve seen aren&#x27;t the agent doing something obviously daft, it&#x27;s a tool call that returns fine but the result shouldn&#x27;t be trusted. Stale cached data, or a web page or file with text in it that&#x27;s basically trying to give the agent instructions. Everything after that looks reasonable, it&#x27;s just built on a bad input. Can flow-1 flag that kind of thing? And how does it tell the difference between the tool giving back something wrong ...

[scottfalconer]: We ran into an interesting side effect of agent performance that we needed to explain in our results to our executive team. In our case we were rolling out an AI support agent that could help resolve customer problems. At the start we had calculated the total time and human cost per support ticket going back a few years. After a few months of running the AI agent, we found that both our time and cost per ticket had increased - but then digging in, the issue was that our overall cost and time ...

[sebastienburel]: To your question about how we track ours: one failure I had left no trace at all. A morning run on a resident agent just didn’t happen. The host timer runs on the uptime clock, the Mac slept through the slot, and nothing retries. As far as I can tell from the post, Signals reads traces that exist. Do you do anything for the run that should have happened and didn’t, like diffing against an expected schedule?

[dmos62]: How do you reuse traces as benchmarks (eval datasets)? Is it about being able to synthesise an agent session from the trace, and having another agent watch the first agent&#x27;s behavior? Having trouble wrapping my mind around all the little details. Edit: I initially asked also about general tips for observing agents, but later, noticing that there were no interactions with my comment yet, edited my comment to remove that question, because I felt that it was too broad and would detract from...

[paulariquelmee]: The point about paying to store traces nobody reads hit home. We had the same problem with customer interviews. We did 8 of them and the notes just sat in a doc until we tagged each problem by how many customers it affected. Curious how you decide which flagged errors matter most. Is it how often they show up across traces, or do you weight them by user impact?

</details>
