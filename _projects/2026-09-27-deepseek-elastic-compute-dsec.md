---
layout: default
title: "可扩展AI代理计算基础设施"
date: 2026-09-27T12:00:00+00:00
discovered_date: 2026-09-27
slug: 2026-09-27-deepseek-elastic-compute-dsec
source: hackernews
category: show-hn
ai_score: 8.0
summary: "DeepSeek弹性计算（DSec）提供可扩展的基础设施，用于运行AI代理和任务，使用沙盒环境、容器、微虚拟机和全虚拟机后端，通过统一的SDK。 DSec因其在高星数（240星）和评论数（81条）的Hacker News上的高参与度而具有重要意义，表明了强烈的兴趣。它解决了AI操作中对弹性计算的需求，提供了SaaS或API monetization的潜力。 该项目采用宽松许可证，似乎处于生产成熟度，涉及复杂的部署，包括基于Epyc的服务器节点等硬件要求。"
tags: "AI, Infrastructure, Scalability, Compute, Elastic"
---

# 可扩展AI代理计算基础设施


> DeepSeek弹性计算（DSec）提供可扩展的基础设施，用于运行AI代理和任务，使用沙盒环境、容器、微虚拟机和全虚拟机后端，通过统一的SDK。 DSec因其在高星数（240星）和评论数（81条）的Hacker News上的高参与度而具有重要意义，表明了强烈的兴趣。它解决了AI操作中对弹性计算的需求，提供了SaaS或API monetization的潜力。 该项目采用宽松许可证，似乎处于生产成熟度


**项目链接**：https://arxiv.org/abs/2609.22978
**作者**：shenli3514
**发布时间**：2026-09-26T18:22:41Z
**挖掘日期**：2026-09-27
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Infrastructure, Scalability, Compute, Elastic


## 📌 项目详解

DeepSeek弹性计算（DSec）提供可扩展的基础设施，用于运行AI代理和任务，使用沙盒环境、容器、微虚拟机和全虚拟机后端，通过统一的SDK。 DSec因其在高星数（240星）和评论数（81条）的Hacker News上的高参与度而具有重要意义，表明了强烈的兴趣。它解决了AI操作中对弹性计算的需求，提供了SaaS或API monetization的潜力。 该项目采用宽松许可证，似乎处于生产成熟度，涉及复杂的部署，包括基于Epyc的服务器节点等硬件要求。


## 🌐 背景与生态

DSec属于AI基础设施生态系统，解决了扩展AI操作挑战。它与Google的Ax项目相似，但提供了统一的SDK用于各种沙盒后端。


## 💬 社区讨论

社区评论对规模（380,000个并发沙盒）表示兴奋，并讨论资源分配挑战，将其与Google的Ax进行比较。


## 🚀 应用前景

DSec可应用于需要可扩展AI代理训练的场景，如自主系统和大规模数据处理。潜在的monetization路径包括SaaS、API或金融和医疗行业的本地解决方案。


## 🔧 技术栈

技术栈包括Python、Docker、Kubernetes和各种沙盒后端，如容器、微虚拟机和全虚拟机，以及FnCall等框架的依赖。


## 🎯 上手难度

难度：进阶。前提条件包括Python 3.8+、GPU和API密钥。步骤包括设置Docker、配置Kubernetes，并使用SDK部署沙盒环境。


## 👥 目标用户

目标用户包括金融、医疗和技术行业的后端工程师、ML从业者和发展团队。


## ⚖️ 类似项目对比

竞品包括专注于弹性执行的Google Ax项目，以及提供AI任务无服务器计算的AWS Lambda。


## 📚 参考链接

- [[2609.22978] DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978)
- [DeepSeek details DSec sandbox infrastructure for agent training · TechNode](https://technode.com/2026/09/23/deepseek-dsec-agent-training-sandbox-infrastructure/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[flowerlad]: It seems every DeepSeek paper&#x2F;patent has a huge number of authors, and this one is no exception. They couldn&#x27;t even fit everyone on the page, there are 31 others not shown. This could be an asset protection strategy (i.e., human assets). Imagine if there were only 3 authors. Those authors may get hired away by competitors. If you list every employee on every paper then competitors don&#x27;t know who to lure away.

[vblanco]: 380.000 concurrent sandboxes on 160 Epyc based server nodes. Crazy stuff

[piterrro]: 12 sandboxes per code is insane, I wonder how many of these sandboxes are idle at a time. Depending on the tasks assigned the resource requirements are different. Compare an agent doing pdf conversion and one responding to a simple question. One is cpu bound the other is mostly network wait. This is an interesting problem from infra perspective since you cannot predict the workload. On a bigger scale you may get away with forecasts. Im waiting for tech that elastically allocates cpu&#x2F;mem ...

[erulabs]: Appears to be similar to what Google is building with ax  https:&#x2F;&#x2F;github.com&#x2F;google&#x2F;ax

[throwaway7783]: Is this like agent substrate?

</details>
