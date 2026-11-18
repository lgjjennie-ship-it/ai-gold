---
layout: default
title: "AI驱动的CI系统，适用于高容量仓库"
date: 2026-11-18T12:00:00+00:00
discovered_date: 2026-11-18
slug: 2026-11-18-launch-hn-starsling-yc-p25-self-improving-ci-for-agent-volume-repos
source: hackernews
category: show-hn
ai_score: 9.0
summary: "StarSling利用带有AI代理的GitHub Actions运行器，持续改进高容量仓库的测试速度并降低CI成本。 StarSling针对高容量仓库的CI/CD痛点，提供了一种创新的AI代理方法来提高测试速度并降低成本，得到YC支持并拥有强烈的社区兴趣。 StarSling使用快速Zen 5机器上的临时沙盒和NVMe磁盘，提供无限并发和按秒计费，以及持久磁盘以实现速度提升。"
tags: "CI, Agent, AI, GitHub, DevOps"
---

# AI驱动的CI系统，适用于高容量仓库


> StarSling利用带有AI代理的GitHub Actions运行器，持续改进高容量仓库的测试速度并降低CI成本。 StarSling针对高容量仓库的CI/CD痛点，提供了一种创新的AI代理方法来提高测试速度并降低成本，得到YC支持并拥有强烈的社区兴趣。 StarSling使用快速Zen 5机器上的临时沙盒和NVMe磁盘，提供无限并发和按秒计费，以及持久磁盘以实现速度提升。


**项目链接**：https://news.ycombinator.com/item?id=50536468
**作者**：yonasb
**发布时间**：2026-11-17T19:01:43Z
**挖掘日期**：2026-11-18
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：CI, Agent, AI, GitHub, DevOps


## 📌 项目详解

StarSling利用带有AI代理的GitHub Actions运行器，持续改进高容量仓库的测试速度并降低CI成本。 StarSling针对高容量仓库的CI/CD痛点，提供了一种创新的AI代理方法来提高测试速度并降低成本，得到YC支持并拥有强烈的社区兴趣。 StarSling使用快速Zen 5机器上的临时沙盒和NVMe磁盘，提供无限并发和按秒计费，以及持久磁盘以实现速度提升。


## 🌐 背景与生态

StarSling填补了高容量仓库CI/CD的空白，利用AI代理优化工作流并降低成本，许多组织都面临这个问题。


## 💬 社区讨论

社区评论强调了衡量可部署合并的重要性、代理推理成本与CI节省的对比，以及优化后进行稳健测试的必要性。


## 🚀 应用前景

StarSling可解决高容量仓库中的实际问题，特别是在软件开发和DevOps领域，通过SaaS和API模式实现商业化。


## 🔧 技术栈

StarSling使用带有AI代理的GitHub Actions运行器，利用快速Zen 5机器、NVMe磁盘和CI harness进行优化。


## 🎯 上手难度

入门评级为进阶，需要Python 3.8+、GPU和API密钥，步骤包括设置工作环境。


## 👥 目标用户

目标用户包括软件开发和 enterprise 环境中的后端工程师、ML实践者和DevOps团队。


## ⚖️ 类似项目对比

竞品包括GitHub Actions自托管运行器、GitLab CI带有AI代理和Jenkins基于代理的CI，它们在成本、速度和专业化方面有所不同。


## 📚 参考链接

- [GPU cloud providers for self-hosted GitHub Actions runners](https://grokipedia.com/page/GPU_cloud_providers_for_self-hosted_GitHub_Actions_runners)
- [GitHub Actions Runners](https://docs.github.com/en/actions/concepts/runners)

<details><summary>📄 查看原文内容</summary>


We’re Yonas and Daniel and we’re building StarSling (<a href="https:&#x2F;&#x2F;starsling.dev">https:&#x2F;&#x2F;starsling.dev</a>), fast GitHub Actions runners with AI agents that ship PRs to continuously improve your tests and workflows.<p>Every CI job gets its own ephemeral sandbox on the fastest Zen 5 machines and NVMe Disk with unlimited concurrency so a burst of agent PRs all run at once. We’re different from other runners because ours come with agents that cut down your CI bill over time. PRs are generated through our CI harness, which runs an agent loop that’s tuned to improve your CI speed and reduce cost.<p>Mastra now merges over 1,800 PRs a month and we got their slowest workflow from 29m 56s on GitHub-hosted runners down to 5m 06s (5.87x) on StarSling. We realized the true value of having an agent loop running on top of fast runners when our agents found an 11-month-old performance bottleneck in better-auth. The fix made one of their test jobs 5.4x faster: <a href="https:&#x2F;&#x2F;github.com&#x2F;better-auth&#x2F;better-auth&#x2F;pull&#x2F;10762" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;better-auth&#x2F;better-auth&#x2F;pull&#x2F;10762</a>.<p>I previously founded StackShare, which grew to over 1.5M developers. Daniel helped build Netflix&#x27;s internal developer portal. Last year we started building AI agents for DevOps because shipping code to prod fell way behind agentic coding. We hit the CI bottleneck ourselves as we were building agents. Our own agents shipped so many PRs that at peak our job queues were backed up for hours and our CI bill got close to our inference bill.<p>We now support per-second billing, and just shipped StarSling Disks - persistent disks that give you a 4.9x speedup in dependencies ready over actions&#x2F;cache. You can see a quick demo of disks in action here : <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=2JrrpRm9Mww" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=2JrrpRm9Mww</a>.<p>Our CI harness runs a loop that has agents:
- Analyze your workflows, run logs, and machine telemetry
- Propose an optimization
- Test your unchanged workflow side by side the proposed change
- Deterministically judge that the difference is statistically significant
- Ship the winner to you as a PR with benchmarks evidence<p>We benchmarked open source repos on our runners and average 10x speedup in wall clock time with 70% less runner time:
- <a href="https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-gogs" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-gogs</a> (12.8x)
- <a href="https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-shellcheck" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-shellcheck</a> (5.5x)
- <a href="https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-chatwoot" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-chatwoot</a> (3.9x)
- <a href="https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-transfer.sh" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-transfer.sh</a> (11.7x)
- <a href="https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-mirotalksfu" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starsling-demo-org&#x2F;benchmark-mirotalksfu</a> (36.4x)<p>Yes, you can do these optimizations yourself with prompts so we’ve released skills for this: <a href="https:&#x2F;&#x2F;github.com&#x2F;starslingdev&#x2F;skills" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starslingdev&#x2F;skills</a>. The benefit of using our agents is that you don’t need to spend tokens and CI compute finding optimizations yourself.<p>We started building our runners on AWS at the beginning of the year and realized that was too expensive. But at that time there weren’t any cloud providers that could give us the same machines we were getting on AWS, billed per minute (microVMs). So we convinced a handful of sandbox providers to get Zen 5s and started benchmarking them publicly (<a href="https:&#x2F;&#x2F;github.com&#x2F;starslingdev&#x2F;hpc-sandbox-benchmarks" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;starslingdev&#x2F;hpc-sandbox-benchmarks</a>).<p>We’ve learned that fast infrastructure is table stakes for CI, but it’s not sufficient on its own. To get fast and cost effective CI you need a process that continues making improvements. We turned CI optimizations from OpenAI, Anthropic, Linear and others into playbooks for your agent: <a href="https:&#x2F;&#x2F;starsling.dev&#x2F;ci-playbooks">https:&#x2F;&#x2F;starsling.dev&#x2F;ci-playbooks</a>.<p>To try it, give your agent this URL: <a href="https:&#x2F;&#x2F;docs.starsling.dev&#x2F;start">https:&#x2F;&#x2F;docs.starsling.dev&#x2F;start</a>. You get 2,000 free minutes. Our agents start opening PRs once you&#x27;ve hit about 10,000 minutes.<p>Today we announced our CI Challenge: if StarSling can&#x27;t save you at least 10% on your next CI bill, we&#x27;ll literally give you $1,000. Eligibility and rules here: <a href="https:&#x2F;&#x2F;starsling.dev&#x2F;blog&#x2F;ci-challenge">https:&#x2F;&#x2F;starsling.dev&#x2F;blog&#x2F;ci-challenge</a>.<p>We’d love your feedback on the headless experience and what you’d like to see improved in your own CI setup!<p><a href="https:&#x2F;&#x2F;starsling.dev">https:&#x2F;&#x2F;starsling.dev</a>


--- Top Comments ---

[colek42]: We should probably be measuring deployable merges to main.  The math just doesn&#x27;t work for pipeline based CI as you add more agents. Three things matter. 1 -- How many non-conflicting changes can actually be made at one time (Fan Out) 2 -- How long a critical path takes 3 -- How many times you have to run that critical path.  Most orgs run it 2-3x, once before the PR in the agent loop, once in CI, and another in the MQ This is why most orgs cant get past about 12 PRs an hour.

[poxlr]: Curious how the inference cost of the agent loop compares to the CI minutes it saves. On a smaller repo I could see it eating most of the savings. Is there a repo size where it starts to clearly pay off?

[bekacru]: Bereket from Better Auth - we&#x27;ve been on StarSling for about a year now, it&#x27;s been such a hard a problem for us ot solve CI to the amount of PRs we get and continues need of optimization and faster runners, im so bullish!

[emscb]: So the agent compares the changed workflow with the existing one and judges whether the speedup is significant. But a change that re-shards or skips tests would always look like a win on speed alone, wouldn&#x27;t it? How do you check that such changes still catch the bugs the old workflow caught? I had the same worry when I trimmed our tests because CI was too slow.

[jstrasner]: So good! CI is still such a pain. Out of curiosity, do you use any open source harnesses under the hood or did you roll your own?

</details>
