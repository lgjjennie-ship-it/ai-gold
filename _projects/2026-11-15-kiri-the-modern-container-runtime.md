---
layout: default
title: "Kiri——快速容器运行时"
date: 2026-11-15T12:00:00+00:00
discovered_date: 2026-11-15
slug: 2026-11-15-kiri-the-modern-container-runtime
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Kiri 是一个用 Rust 编写的现代容器运行时，旨在通过在单个小型 Linux 虚拟机或直接在内核上运行容器来显著快于 Docker。它支持 Docker Engine API，确保与现有工具的兼容性。 Kiri 声称比 Docker 快 8 倍，解决了容器管理中的一个重要痛点，这是云原生和 DevOps 中的一个热门领域。它作为 SaaS 或 API 服务的潜力提供了明确的盈利路径，尽管其吸引力和社区参与度适中。 Kiri 遵循宽松的许可证，目前在所有主要平台（Mac、Windows、Linux）上都是 Beta 版。它旨在简化容器管理，但在与复杂编排工具的集成方面可能存在限制。"
tags: "Container, Runtime, Cloud-Native, Performance, DevOps"
---

# Kiri——快速容器运行时


> Kiri 是一个用 Rust 编写的现代容器运行时，旨在通过在单个小型 Linux 虚拟机或直接在内核上运行容器来显著快于 Docker。它支持 Docker Engine API，确保与现有工具的兼容性。 Kiri 声称比 Docker 快 8 倍，解决了容器管理中的一个重要痛点，这是云原生和 DevOps 中的一个热门领域。它作为 SaaS 或 API 服务的潜力提供了明确的盈利路径，尽管其吸


**项目链接**：https://runkiri.com/
**作者**：nikolay
**发布时间**：2026-11-15T04:40:41Z
**挖掘日期**：2026-11-15
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Container, Runtime, Cloud-Native, Performance, DevOps


## 📌 项目详解

Kiri 是一个用 Rust 编写的现代容器运行时，旨在通过在单个小型 Linux 虚拟机或直接在内核上运行容器来显著快于 Docker。它支持 Docker Engine API，确保与现有工具的兼容性。 Kiri 声称比 Docker 快 8 倍，解决了容器管理中的一个重要痛点，这是云原生和 DevOps 中的一个热门领域。它作为 SaaS 或 API 服务的潜力提供了明确的盈利路径，尽管其吸引力和社区参与度适中。 Kiri 遵循宽松的许可证，目前在所有主要平台（Mac、Windows、Linux）上都是 Beta 版。它旨在简化容器管理，但在与复杂编排工具的集成方面可能存在限制。


## 🌐 背景与生态

容器生态系统复杂，术语如 '容器引擎'、'容器运行时' 和 '容器管理器' 常常重叠。Kiri 旨在通过提供更快、更高效的运行时来填补这一空白，与 Docker 和 OrbStack 等成熟工具竞争。


## 💬 社区讨论

社区评论对容器管理中使用的术语感到困惑，并对 Kiri 的性能声明表示怀疑。一些用户要求对其架构进行解释，并询问它与替代方案的比较。


## 🚀 应用前景

Kiri 可用于云原生环境和 DevOps 工作流程，以提高容器部署和管理效率。其潜在应用包括用于容器编排的 SaaS 提供商和面向开发者的 API 服务。


## 🔧 技术栈

Kiri 是用 Rust 构建的，并在最小型 Linux 虚拟机或内核上运行容器。它支持 Docker Engine API，并设计得轻量级且快速。


## 🎯 上手难度

使用 Kiri 的难度评级为进阶。前提条件包括现代操作系统和已安装 Rust。基本步骤包括下载二进制文件并使用 Docker 命令运行它。


## 👥 目标用户

Kiri 主要面向 DevOps 工程师、云原生开发者和希望优化容器管理的企业。它特别适用于寻求容器工作流程性能改进的团队。


## ⚖️ 类似项目对比

竞争对手包括 Docker、OrbStack 和 Podman。Kiri 通过其性能和简单性方面的关注而脱颖而出，尽管 Docker 仍然是使用最广泛和最成熟的。


## 📚 参考链接

- [GitHub - libracoder/kiri: A small, fast container runtime for ...](https://github.com/libracoder/kiri/)
- [Kiri: a fast Docker Desktop alternative for Mac, Windows, Linux](https://runkiri.com/)
- [Kiri Docs](https://docs.runkiri.com/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[5G_activated]: I love cloud-native and containers just as much as the next person but the nomenclature for different things which do some but not all of the same things can be pretty confusing. We have the phrase “container engine” which could mean dockerd or Podman; “container runtime” to me usually refers to containerd or CRI-O but could also refer to runc and crun; and “container manager”, which could alternately refer to dockerd and Podman or to “orchestrators” like k8s Swarm and Nomad. “Desktop app” is...

[sercant]: &gt; One Apple-silicon Mac, one runtime at a time. Measured numbers replace these soon. :))))))

[gempir]: I would really like to understand  why  it claims it&#x27;s such much faster than OrbStack or Docker Desktop? What is the architecture or technology decision that makes that 8x claim possible?

[sureglymop]: I think the headline might be confusing because docker&#x2F;podman already have the concept of a runtime. E.g. you can pass `--runtime` to set it on the fly or set it in the config... For example, I don&#x27;t use crun but a more security hardened runtime instead.

[cholindo]: My question is wether &quot;8x faster than docker&quot; means that containers run faster or that the tooling around them runs faster

</details>
