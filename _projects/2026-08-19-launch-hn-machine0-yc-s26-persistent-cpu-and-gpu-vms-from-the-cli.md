---
layout: default
title: "持久化虚拟机用于代理计算"
date: 2026-08-19T12:00:00+00:00
discovered_date: 2026-08-19
slug: 2026-08-19-launch-hn-machine0-yc-s26-persistent-cpu-and-gpu-vms-from-the-cli
source: hackernews
category: show-hn
ai_score: 8.0
summary: "machine0 提供从 CLI 创建的持久化 CPU 和 GPU 虚拟机，用于长期代理计算，按分钟计费。 machine0 在 HN 上获得 41 条评论和 68 分的高评分，解决了开发者对始终在线环境的需求问题，并提供清晰的盈利模式。 machine0 采用宽松的许可证，已进入生产阶段，具有高成熟度，提供简单的 CLI 部署和 GPU 集成。"
tags: "Agent, Compute, Cloud, CLI, VM"
---

# 持久化虚拟机用于代理计算


> machine0 提供从 CLI 创建的持久化 CPU 和 GPU 虚拟机，用于长期代理计算，按分钟计费。 machine0 在 HN 上获得 41 条评论和 68 分的高评分，解决了开发者对始终在线环境的需求问题，并提供清晰的盈利模式。 machine0 采用宽松的许可证，已进入生产阶段，具有高成熟度，提供简单的 CLI 部署和 GPU 集成。


**项目链接**：https://machine0.io/
**作者**：bwm
**发布时间**：2026-08-18T16:26:42Z
**挖掘日期**：2026-08-19
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Agent, Compute, Cloud, CLI, VM


## 📌 项目详解

machine0 提供从 CLI 创建的持久化 CPU 和 GPU 虚拟机，用于长期代理计算，按分钟计费。 machine0 在 HN 上获得 41 条评论和 68 分的高评分，解决了开发者对始终在线环境的需求问题，并提供清晰的盈利模式。 machine0 采用宽松的许可证，已进入生产阶段，具有高成熟度，提供简单的 CLI 部署和 GPU 集成。


## 🌐 背景与生态

代理工作负载正从临时转向始终在线，需要持久化虚拟机来处理长时间运行的任务。


## 💬 社区讨论

社区评论集中在快照/挂起/恢复功能、GPU 使用替代方案和虚拟机管理上。


## 🚀 应用前景

machine0 非常适合代理集群、模型优化和产品基础设施，在软件开发和 AI 研究等行业具有 SaaS 盈利潜力。


## 🔧 技术栈

核心技术栈包括 TypeScript、Postgres、Redis，以及具有真实 GPU 访问的完整 KVM 虚拟机。


## 🎯 上手难度

入门评级为进阶，需要 Python、GPU 和 API 密钥；步骤包括通过 CLI 创建虚拟机并进行管理。


## 👥 目标用户

目标用户包括软件开发和 AI 行业的后端工程师、ML 实践者和 DevOps 团队。


## ⚖️ 类似项目对比

竞品包括用于内存快照的 shellbox.dev 和 AWS/GCP 云计算，machine0 提供独特的 CLI 持久化功能。


## 📚 参考链接

- [machine0: Cloud computers for AI agents | Y Combinator](https://www.ycombinator.com/companies/machine0)
- [machine0](https://app.machine0.io/)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)

<details><summary>📄 查看原文内容</summary>


Hi HN! I’m Barnaby, founder of machine0 (<a href="https:&#x2F;&#x2F;machine0.io">https:&#x2F;&#x2F;machine0.io</a>). I’m building a CLI for long horizon agent compute: `machine0 new mybox` gives your agent a persistent cloud VM, billed by the minute, from $0.013&#x2F;hr up to 60 vCPU &#x2F; 240 GB RAM and GPUs (H100s, H200s etc), with 99.99% VM level uptime. Agents self drive via CLI or MCP.<p>Demo: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=gyllkZ0M04E" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=gyllkZ0M04E</a><p>Agent workloads are moving from ephemeral to always-on. A coding agent working on a complex feature runs 6-8 hours. Agent orchestrated training &amp; RL runs take days. OpenClaw &amp; Hermes run 24&#x2F;7. As you run more in parallel:<p>- Resources: a few agents on a large codebase saturate RAM and CPU. Model training and RL needs GPUs you don&#x27;t have.<p>- Security: `--yolo` on your personal machine is one prompt injection away from exfiltrated credentials.<p>- Availability: close your laptop and the agent dies mid-task.<p>- Isolation: there&#x27;s no clean line between you and the minimum your agent actually needs.<p>machine0 gives every agent its own computer. It&#x27;s a CLI simple enough that both humans and agents use it without reading docs:
`machine0 new mybox` creates an SSH-ready VM with a static IP and HTTPS endpoint. Always on (with 99.99% VM level uptime) until you switch it off.<p>- Billed by the minute. 1 vCPU &#x2F; 1 GB at $0.013&#x2F;hr up to 60 vCPU &#x2F; 240 GB, plus GPUs from RTX 4000 Ada to 8×H200.<p>- Suspend, snapshot and resume. Making it easy to pause your work, and come back to it later. Or to make a golden master image to stamp out clones for a fleet.<p>- Block storage. Persistent volumes (from 10 GB to 16 TB) that you can manage with intuitive grammar: `--yolo` and attach to your VMs.<p>- Profiles. Bundles of credentials, MCP connections, prompts, and env vars, injected at VM creation. So each agent gets exactly the capabilities you choose, and nothing else.<p>- Agents self-serve. Hand the CLI or MCP server to Claude, Codex, or OpenCode and it manages its own fleet: spin up a box for a build, snapshot it, tear it down.<p>- Reproducible Builds. Using NixOS flakes or Ansible playbooks with Ubuntu.<p>How do people use it today?<p>- Agent fleets. People run a pilot agent that scopes work and delegates it to sub-agents, each on its own VM: shape a project with the pilot, and the workers implement it and open PRs. One customer runs hundreds of machines at once, spun up and torn down from the CLI.<p>- Model optimization &amp; RL environments. ML teams use machine0 for agent-orchestrated RL environments and model optimization work. One customer runs RL environments on 60 vCPU machines that stay up for days at a time; another keeps a suspended H100 around and points an agent at it overnight to grind on inference-speed optimizations.<p>- Product infrastructure. One customer builds their product on top of machine0 rather than using it themselves: every user session gets a fresh XL machine from a versioned image of their own agent runtime. They&#x27;ve shipped hundreds of versions of that image and launched thousands of machines, most alive for two minutes.<p>What’s under the hood?<p>Every machine is a full KVM virtual machine, not a container or sandbox. You get the real GPU exposed to the guest with its actual driver, kernel-level access (load any module or driver you want), and no syscall-interception layer between you and the hardware. The stack itself is deliberately dull: TypeScript, Postgres, Redis. We weigh heavily towards security, reliability and performance making machine0 ideal for sustained compute intensive workloads. 
About me<p>I&#x27;ve been building cloud infrastructure for about 15 years. I dropped out of a PhD at Imperial College London on cloud resource allocation, later spent six years as co-founder and CTO of Upflow (YC W20), owning DevOps, infra and security personally the whole way to 7-figures in ARR because it was too high-stakes to delegate. machine0 started as a tool for me, I’m my own first user :)
Asks<p>Would love you to try it out and give us your feedback (see below). Or if you’re a company looking for compute for software factories, model training or RL environments, feel free to reach out at barnaby@machine0.io<p><pre><code>  # install machine0 
  $ curl -LsSf https:&#x2F;&#x2F;machine0.io&#x2F;install.sh | sh

  # create a machine and ssh in
  $ machine0 new myvm
  $ machine0 ssh myvm</code></pre>


--- Top Comments ---

[zodiac]: Does snapshot&#x2F;suspend&#x2F;resume keep processes&#x2F;RAM alive - or do you need to re-start processes&#x2F;reload stuff into RAM? How does that work under the hood (CRIU?) and how fast is it?

[messh]: If you don&#x27;t need GPU, check out  https:&#x2F;&#x2F;shellbox.dev  - it snapshots memory, processes. And you pay only for actual running time per minute

[atechboy]: &gt; People run a pilot agent that scopes work and delegates it to sub-agents, each on its own VM: shape a project with the pilot, and the workers implement it and open PRs. One customer runs hundreds of machines at once, spun up and torn down from the CLI. Are people spawning VMs for every tool call? If so, would love to understand why so, and why containers are not a good fit?

[averylostnomad]: When you say suspendible, do you mean that I could make a VM, configure it by installing packages and libraries, then pause it? And resume it later with the full disk ready to go? No billing during the inbetween time? That’d be huge, but seems wild. How can you economically keep the storage between active sessions?

[prodtorok]: Basic question: What are you doing here that my agent couldn&#x27;t do with: AWS, GCP, Hetzner, DigitialOcean? Quick read is this is some simple api abstraction? or you&#x27;re even brokering that compute? Which i would want, why?

</details>
