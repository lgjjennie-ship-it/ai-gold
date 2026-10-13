---
layout: default
title: "Agent37：低成本AI代理沙盒"
date: 2026-10-13T12:00:00+00:00
discovered_date: 2026-10-13
slug: 2026-10-13-launch-hn-agent37-yc-f26-low-cost-agent-sandboxes-for-running-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Agent37为开发者提供低成本AI代理沙盒，采用高效的CPU/内存管理、替代云服务提供商和资源共享技术。 Agent37凭借135个点赞和98条评论获得关注，解决了AI代理沙盒的高成本问题，并提供了清晰的低月费盈利模式。 Agent37采用开源许可模式，已投入生产，拥有成熟的基础设施，部署复杂度低，并与流行的AI模型有集成点。"
tags: "AI, Agent, Sandboxes, Cost-Effective, Development"
---

# Agent37：低成本AI代理沙盒


> Agent37为开发者提供低成本AI代理沙盒，采用高效的CPU/内存管理、替代云服务提供商和资源共享技术。 Agent37凭借135个点赞和98条评论获得关注，解决了AI代理沙盒的高成本问题，并提供了清晰的低月费盈利模式。 Agent37采用开源许可模式，已投入生产，拥有成熟的基础设施，部署复杂度低，并与流行的AI模型有集成点。


**项目链接**：https://news.ycombinator.com/item?id=50059096
**作者**：vishnukool
**发布时间**：2026-10-12T16:46:34Z
**挖掘日期**：2026-10-13
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agent, Sandboxes, Cost-Effective, Development


## 📌 项目详解

Agent37为开发者提供低成本AI代理沙盒，采用高效的CPU/内存管理、替代云服务提供商和资源共享技术。 Agent37凭借135个点赞和98条评论获得关注，解决了AI代理沙盒的高成本问题，并提供了清晰的低月费盈利模式。 Agent37采用开源许可模式，已投入生产，拥有成熟的基础设施，部署复杂度低，并与流行的AI模型有集成点。


## 🌐 背景与生态

Agent37处于AI沙盒市场，该市场存在Boat.dev等竞争对手。该项目因低成本AI开发工具的需求而具有相关性。


## 💬 社区讨论

社区评论表达兴奋和技术兴趣，并就内存管理和价格比较提出问题。


## 🚀 应用前景

Agent37可被各行业开发者用于低成本测试AI代理，具有SaaS盈利或集成到开发工具的潜力。


## 🔧 技术栈

Agent37使用gVisor进行高效资源共享，在Hetzner/OVH上托管，并支持Hermes/OpenClaw/Claude模型，侧重内存优化。


## 🎯 上手难度

入门难度。前提条件包括Python 3.8+和互联网访问。步骤涉及注册和部署沙盒。


## 👥 目标用户

目标用户为AI和软件开发中的个人开发者和企业团队，特别是那些使用消息代理的开发者。


## ⚖️ 类似项目对比

竞争对手包括Boat.dev和OpenClaw。Agent37以更低成本和gVisor集成区别，而Boat.dev提供更多存储。


## 📚 参考链接

- [OpenClaw — Open-Source AI Assistant](https://openclaw.ai/)

<details><summary>📄 查看原文内容</summary>


Hey HN, I’m Vishnu from Agent37 (<a href="https:&#x2F;&#x2F;agent37.com">https:&#x2F;&#x2F;agent37.com</a>). We build sandboxes for running AI agents at under 10% of the cost of most sandbox providers. Our customers spend an average of $0.37&#x2F;month per sandbox.<p>You can view a video walkthrough of the product here: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;DK5ISR2tbNo" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;DK5ISR2tbNo</a><p>We started as one of those OpenClaw wrapper companies back in February (yup.. judge me). In time we added more and more harnesses.<p>One of the goals I had at the time was to offer a free plan to users, so as to gain more market share. But it was too cost prohibitive to do it right away. Especially since we were bootstrapped and servers were running on my savings.<p>Today we’re actually able to offer the free plan thanks to the optimizations we’ve made since. Over 90% of the new signups we have are just free plan users and they host their personal Hermes&#x2F;Openclaw&#x2F;Claude Code etc on our cloud. Our infrastructure cost for the free sandboxes averages around $0.05 to $0.10 per user per month.<p>Here are some techniques that have worked for lowering cost:<p>* When you look at agent harnesses, they have certain patterns in the way they consume CPU and RAM. They need CPU in bursts when they’re initializing or performing certain tasks, but beyond that, they’re often not peaking. They need more RAM for things like browser and computer-use tasks. Once the task is done, usage often comes back down. This is a key insight in lowering cost, so by efficiently managing the CPU&#x2F;RAM utilization we could lower the cost.<p>* Secondly, you have to skip the hyperscalers when renting the Hosts. I worked at Amazon before and they have 80-90% margins on VMs. So it was an obvious choice once I looked at the prices to go one layer down to vendors like Hetzner and OVH. This alone was probably one of the biggest cost levers in reducing the cost.<p>* Thirdly, you also want to pick a technology stack that lets you efficiently cache and share resources across the host. We use gVisor for better utilization and fast boot times. It lets us use available host memory across sandboxes without reserving a full VM’s memory for each one. There are tradeoffs: our gVisor sandboxes don’t support workloads like Docker-in-Docker or Android emulators.<p>* And finally the size and shape of the hosts you buy also makes a big difference. RAM is typically the bottleneck when it comes to cost and not the CPU. This is specifically true for agent harness workloads, so when buying servers, we optimize for packing more RAM into a given host.<p>We also host full VM sandboxes for workloads that need them, including running Docker at a slightly higher price, but they are still pretty low cost given the rest of the techniques.<p>Overall, my learning has been that just by focusing on a niche of sandbox usecases, and optimizing for it you can give a much better cost&#x2F;performance tradeoff.<p>I was previously a Senior Software Engineer at Amazon and an Engineering Manager at Quantcast. I built Amazon&#x27;s internal AI chatbot, Diya, and their internal coding harness, Ziya.<p>If you’re someone who’s looking to run agents on sandbox and are exploring a sandbox vendor, come check us out. We’re particularly looking for developers building messaging agents to try their workloads and challenge the limits and economics of our platform.<p>Thanks!<p><a href="https:&#x2F;&#x2F;agent37.com">https:&#x2F;&#x2F;agent37.com</a>


--- Top Comments ---

[mparis]: Congrats on the launch! Very exciting! You guys are operating in a very competitive space. This stuff is fun to build, so a lot of engineers will end up building it. Not to discourage you, but I suspect it will be difficult to capture much value selling this offering as its going to be race to the bottom against very well funded alternatives that can sell these features at a loss in order to get you to use their databases and other offerings that are higher margin and stickier. As you guys le...

[pathly]: This is really impressive work on the infrastructure side.
Skipping hyperscalers like AWS for Hetzner&#x2F;OVH is definitely a massive lever, but your choice of gVisor for memory overcommit is where this gets technically interesting. A few questions on the implementation:
• Memory &amp; Density: Since gVisor allows you to share memory without reserving a full VM&#x27;s allocation, how are you handling noisy neighbors if multiple sandboxes spike in RAM usage simultaneously? Are you using speci...

[alasano]: I&#x27;ve been looking at offloading local work from my MacBook Pro (M1 Pro &#x2F; 32 GB) specifically because I&#x27;ve been working with a lot of Android apps and emulation is killing me on top of everything else that I&#x27;m running. Got a bunch of Daytona credits which are close to useless given their restrictions until you hit tier 3. You seem like you&#x27;re actually slightly cheaper than  https:&#x2F;&#x2F;boat.dev&#x2F;  but with less storage? That&#x27;s the closest to your pricing...

[select1dev]: I run a daily job that clones and runs a freshly launched open-source project in a sandbox, so a few notes from the consumer side of this market. Your point about bursty CPU matches what I see: install and build spike for 20–60 seconds, then the process mostly idles while the harness reads output. RAM only matters the day a project pulls in a headless browser. The things that actually cost me time were not CPU or RAM, though. First, network policy. I run untrusted code with an egress allowlis...

[MikhailTal]: Sandboxes look a bit commoditized. You cannot 10x on basically what&#x27;s just a VM with a few agent-friendly features in 2026. Hence competing on purely price as a new startup is a bad idea imo. As you mentioned hyperscalers have insane margins, but if this turns out to be a real market, they will lower cost, even just eat the loss if they want and take you out of business. Without any hardware innovation, it&#x27;s tough for me to see this working. If you are going with a customization ang...

</details>
