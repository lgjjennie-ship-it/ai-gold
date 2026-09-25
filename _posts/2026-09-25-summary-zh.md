---
layout: default
title: "AI掘金: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 143 条内容中筛选出 15 条重要资讯。

---

1. [AI 驱动的视频编辑和克隆工具](#item-1) ⭐️ 9.0/10
2. [QM：AI 开发的多玩家代理 harness](#item-2) ⭐️ 9.0/10
3. [GenOffice：AI 驱动的本地办公套件](#item-3) ⭐️ 9.0/10
4. [可扩展 AI 编码代理](#item-4) ⭐️ 9.0/10
5. [具有独立计算环境的开源 AI 同事](#item-5) ⭐️ 9.0/10
6. [Utopia：开源企业世界模型](#item-6) ⭐️ 9.0/10
7. [Graft：上下文编码代理增强器](#item-7) ⭐️ 9.0/10
8. [高度优化的 C 语言 CPU LLM 推理](#item-8) ⭐️ 9.0/10
9. [在 MacBook 上高效运行 Gemma 4](#item-9) ⭐️ 9.0/10
10. [大模型学习路线图](#item-10) ⭐️ 9.0/10
11. [谷歌太空机器学习基础设施](#item-11) ⭐️ 9.0/10
12. [Whiteboard：一个开源的协作软件设计 IDE](#item-12) ⭐️ 8.0/10
13. [使用 LLM 解码 17 世纪炼金术文本](#item-13) ⭐️ 8.0/10
14. [Opus 5.5 用于 AI 解说视频](#item-14) ⭐️ 8.0/10
15. [新型伪造 1024 位 RSA 签名方法](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 驱动的视频编辑和克隆工具](https://github.com/hypit-ai/hypit) ⭐️ 9.0/10

Hypit 利用 AI 自动交换视频中的面部、文字和补充画面，实现快速创建多个视频变体。 凭借高人气（超过 1.6 万个星标，1.9 千个分支）和近期活跃度，Hypit 通过提供 AI 驱动的自动化解决了视频创作的痛点，并具有清晰的 SaaS 盈利路径。 Hypit 采用 MIT 许可证，已达到生产成熟度，部署复杂度适中，需要 TypeScript 和 ffmpeg 等工具的集成。

github · hypit-ai · 9月24日 11:12

**背景**: 生成式 AI 提升了视频创作能力，文本到视频模型可实现脚本到片段的生成。Hypit 处于这一生态系统中，与 RunwayML 和 Pika Labs 等工具竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_AI">Generative AI - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/generative-ai">What is Generative AI ? | IBM</a></li>
<li><a href="https://huggingface.co/tasks/text-to-video">What is Text-to-Video? - Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区反馈积极，讨论集中在增加更多 AI 代理集成功能和提升文本到视频的准确性。

**标签**: `#AI`, `#Agent`, `#Video`, `#Editing`, `#Generative-AI`

---

<a id="item-2"></a>
## [QM：AI 开发的多玩家代理 harness](https://github.com/yc-software/qm) ⭐️ 9.0/10

QM 是一个用 TypeScript 构建的多玩家代理 harness，旨在管理 AI 代理在共享环境中的状态和控制流。 QM 拥有 15k 星和 1.9k 分叉的高人气，近期活跃，通过创建多玩家代理 harness 解决了 AI 开发者的实际问题，并具有清晰的 SaaS 或 API 货币化潜力。 QM 在 MIT 许可下是开源的，处于 alpha 阶段，有 575 个开放问题，基本使用需要 TypeScript 知识，没有特定的硬件要求。

github · yc-software · 9月25日 05:22

**背景**: QM 是 AI 开发生态系统的一部分，填补了管理多玩家代理交互的空白。它与单代理框架不同，能够实现持久的共享状态管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asibiont.com/en/blog/qm-multiplayer-kharness-dlya-agentov-novaya-fishka-vibe-coding-o-kotoroy-govoryat-vse">QM: Multiplayer Agent Harness for Work — How... — ASI Biont Blog</a></li>
<li><a href="https://www.everydev.ai/tools/qm-agent-harness">QM - Open Source Multiplayer Agent Harness | EveryDev. ai</a></li>
<li><a href="https://smartcr.org/ai-technologies/qm-multiplayer-agent-harness-for-work/">Qm – Multiplayer Agent Harness For Work - SmartCR</a></li>

</ul>
</details>

**社区讨论**: 社区情绪积极，开发者对实时代理协作的潜力感到兴奋，并要求更多文档。

**标签**: `#AI`, `#Agent`, `#Tools`, `#TypeScript`, `#Development`

---

<a id="item-3"></a>
## [GenOffice：AI 驱动的本地办公套件](https://github.com/genspark-ai/genoffice) ⭐️ 9.0/10

GenOffice 是一个开源的 AI 办公套件，具有内置的 AI 代理，用于本地编辑文档，支持文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器。它使用 TypeScript，并与 Claude Code、Codex 和 Cursor 集成。 GenOffice 正在获得显著的关注，拥有 7693 个星标和 996 个分支，解决了对本地 AI 驱动的办公套件的需求。它作为 SaaS 或 API 服务具有明确的盈利潜力。 GenOffice 是免费且开源的，许可证未明确说明。它已投入生产，活动频繁，需要本地硬件和与 AI 代理的集成。

github · genspark-ai · 9月25日 03:28

**背景**: AI 办公套件领域正在发展，Context 和 Microsoft Office 等项目正在探索类似的概念。GenOffice 填补了本地优先 AI 办公解决方案的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://groupthink.com/ai-office-suite/">AI Office Suite - Groupthink</a></li>
<li><a href="https://genoffice.ai/">GenOffice — Free, Open-Source AI Office Suite</a></li>
<li><a href="https://itsfoss.com/news/genoffice-overview/">This New Open Source Project Wants to Be the AI-First Alternative to ...</a></li>

</ul>
</details>

**社区讨论**: 社区对 GenOffice 的潜力感到兴奋，讨论集中在功能和与 AI 代理的集成上。

**标签**: `#AI`, `#Office`, `#Agent`, `#CLI`, `#Local-first`

---

<a id="item-4"></a>
## [可扩展 AI 编码代理](https://github.com/zai-org/ZCode) ⭐️ 9.0/10

ZCode 是一个利用 AI 协助开发者的可扩展编码代理，其核心框架使用 TypeScript，并提供了一个构建自定义编码代理的平台。 ZCode 凭借 6737 星和 2017 个分支的显著人气，满足了日益增长的 AI 驱动开发工具需求，并提供了通过 SaaS 或 API 服务实现盈利的清晰路径。 ZCode 遵循开源许可，已达到生产成熟度，部署复杂度适中，需要 TypeScript 知识以及对 AI 代理的基本理解。

github · zai-org · 9月24日 06:49

**背景**: 软件开发中 AI 的兴起催生了对智能编码代理的需求。ZCode 融入这一生态系统，为 Claude Code 和 Cursor 等现有工具提供了更具可扩展性的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pi.dev/">Pi Coding Agent</a></li>
<li><a href="https://www.zenml.io/llmops-database/building-pi-a-minimal-extensible-coding-agent-framework">Building Pi: A Minimal, Extensible Coding Agent Framework - ZenML</a></li>

</ul>
</details>

**社区讨论**: 社区表现出兴奋情绪，开发者积极贡献并请求新功能，表明对项目的强烈参与。

**标签**: `#AI`, `#Agent`, `#Code`, `#Tools`, `#Developer`

---

<a id="item-5"></a>
## [具有独立计算环境的开源 AI 同事](https://github.com/CopilotKit/OpenBot) ⭐️ 9.0/10

OpenBot 提供具有独立计算环境和动作记录的开源 AI 同事，使用 TypeScript 并与 AG-UI 代理集成。 OpenBot 凭借 5534 星和 723 个分支获得显著关注，通过独立计算环境和动作记录，解决 AI 代理治理和自动化需求，并具有明确的 SaaS 或 API 盈利路径。 OpenBot 采用开源许可证，已达到生产成熟度，部署复杂度适中，需要 TypeScript 环境并与 AG-UI 集成。

github · CopilotKit · 9月23日 18:18

**背景**: 具有独立计算环境的 AI 代理是一个增长趋势，能够实现更自主和安全的 AI 操作。OpenBot 通过提供一个这样的代理框架脱颖而出，利用 RAG 增强决策能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/retrieval-augmented-generation">What is RAG (Retrieval Augmented Generation)? | IBM</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-what-rag-generative-ai-mariam-kili-bechir-mxogf">Understanding what is RAG in Generative AI ?</a></li>

</ul>
</details>

**社区讨论**: 社区反馈积极，开发者对新颖的方法感到兴奋，并要求更多集成选项。

**标签**: `#AI`, `#Agent`, `#RAG`, `#Tools`, `#Automation`

---

<a id="item-6"></a>
## [Utopia：开源企业世界模型](https://github.com/deeplethe/utopia) ⭐️ 9.0/10

Utopia 是一个用 Rust 构建的开源企业世界模型，利用大型语言模型和图数据库进行语义搜索和时序知识表示。 Utopia 以超过 10k 星和频繁的活跃度获得显著关注，解决了企业世界模型的新兴领域。它通过 SaaS 或 API 实现强大的盈利潜力，为企业提供高级知识图谱。 该项目采用宽松的许可证，目前处于生产成熟度，部署复杂度适中。它需要 Rust 和与 PostgreSQL 等图数据库的集成。

github · deeplethe · 9月25日 08:14

**背景**: 企业世界模型对于企业管理复杂知识正变得越来越重要。Utopia 以使用 Rust 实现性能并集成大型语言模型进行高级语义搜索而脱颖而出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rust_%28programming_language%29">Rust ( programming language ) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://cloud.google.com/discover/what-is-semantic-search">What is semantic search, and how does it work? | Google Cloud</a></li>

</ul>
</details>

**社区讨论**: 社区表现出兴奋情绪，频繁的贡献和围绕 agent-memory 和 bitemporal 知识等功能的讨论。

**标签**: `#World-Model`, `#LLM`, `#Semantic-Search`, `#Graph`, `#Rust`

---

<a id="item-7"></a>
## [Graft：上下文编码代理增强器](https://github.com/trailhq/Graft) ⭐️ 9.0/10

Graft 是一个开源工具，通过 TypeScript 增强了编码代理（如 Claude Code、Cursor、Codex 和 Gemini），为开发者代码库提供特定的上下文理解。 Graft 因其 9184 星和 840 分叉的高人气、解决开发者痛点（通过为编码代理提供特定上下文洞察）以及作为 SaaS 或 API 服务的明确盈利潜力而受到关注。 Graft 在开源许可下，已投入生产，部署复杂度适中，需要 TypeScript 知识并集成现有编码代理。

github · trailhq · 9月25日 07:15

**背景**: 随着编码代理的演变，上下文理解变得至关重要，它们已从简单的命令执行发展到与代码库深度集成。Graft 通过提供一个工具来增强开发者代理的特定项目上下文能力来解决这个问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://getzowie.com/glossary/what-is-contextual-understanding">What is Contextual Understanding - Zowie</a></li>
<li><a href="https://www.featherhq.com/old-blog-2/what-is-contextual-analysis-in-ai-conversations">What Is Contextual Analysis in AI Conversations? — Amani Blog</a></li>
<li><a href="https://www.heybeagle.com/blog/context-engineering-for-coding-agents-beats-a-bigger-window">Context Engineering for Coding Agents Beats a Bigger Window</a></li>

</ul>
</details>

**社区讨论**: 社区反馈积极，开发者对工具提升编码代理的潜力感到兴奋，并要求更多集成选项。

**标签**: `#LLM`, `#Agent`, `#Code`, `#Tools`, `#Context-Engineering`

---

<a id="item-8"></a>
## [高度优化的 C 语言 CPU LLM 推理](https://github.com/FareedKhan-dev/kimi-k3-in-c) ⭐️ 9.0/10

该项目使用 C 语言在单个 CPU 上实现 2.78 万亿参数 LLM 推理，通过线性注意力和专家混合等技术，以极少的依赖实现高效。 它因其高人气（8609 星标，1382 个分支）和将大型 LLM 运行在 CPU 上的新颖方法而受到关注，解决了内存效率的痛点，并提供了通过专业软件进行货币化的清晰路径。 该项目在开源许可证下，处于生产成熟阶段，部署复杂度适中，需要 8.24 GB 的 RAM，并且不依赖 BLAS 或框架等外部依赖。

github · FareedKhan-dev · 9月22日 14:29

**背景**: 该项目解决了在 CPU 上进行高效 LLM 推理日益增长的需求，传统框架在内存使用方面存在困难。线性注意力和专家混合（MoE）等技术的使用是模型压缩的最新趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/MXFP4">MXFP4</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，围绕线性注意力和 MoE 等特性进行了积极讨论，并要求进一步优化和对更大模型的支持。

**标签**: `#LLM`, `#Inference`, `#CPU`, `#Memory-Efficient`, `#C`

---

<a id="item-9"></a>
## [在 MacBook 上高效运行 Gemma 4](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

该项目能够在 M 系列 MacBook 上高效运行 Gemma 4 26B-A4B LLM 推理，使用约 2 GB 的 RAM，利用 Swift 和 Metal 实现设备上的性能。 它很重要，因为它解决了在设备上进行大型模型推理日益增长的需求，具有高人气，并明确了通过 SaaS 或 API 进行货币化的清晰路径。 该项目采用 MIT 许可证，似乎处于 alpha 阶段，需要了解 Swift 和 Metal。它具有中等的部署复杂性，但硬件要求较低。

github · drumih · 9月22日 09:04

**背景**: 随着消费级硬件变得越来越强大，设备上的 LLM 推理正变得越来越重要。Metal 和 Swift 使 Apple Silicon 上的 GPU 使用效率更高，使该项目具有时效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B">google/ gemma - 4 - 26 B - A 4 B · Hugging Face</a></li>
<li><a href="https://gemma4.com/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://openrouter.ai/google/gemma-4-26b-a4b-it:free">Gemma 4 26 B A 4 B (free) - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区表现出强烈兴趣，围绕性能优化和功能请求有活跃的讨论。

**标签**: `#LLM`, `#On-Device-AI`, `#Metal`, `#Swift`, `#Gemma4`

---

<a id="item-10"></a>
## [大模型学习路线图](https://github.com/youngyangyang04/llm-master) ⭐️ 9.0/10

该项目提供大语言模型（LLM）的详细学习路线和教程，涵盖提示工程、RAG、AI 代理和部署。它使用中文使学习更易于理解。 因其高人气（948 星，93 次分叉）和近期活动而备受关注，通过提供实用指导解决了 LLM 学习的障碍。教育内容的潜在盈利能力。 根据许可协议，可能处于 alpha 阶段，部署复杂度适中。需要基本的 Python 知识和对 AI 概念的理解。

github · youngyangyang04 · 9月19日 08:45

**背景**: 大模型（LLM）的兴起创造了对易获取学习资源的需求。该项目通过提供关于高级 LLM 主题的全面中文教程来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/prompt-engineering">What Is Prompt Engineering? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective AI Agents \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区表现出热情，积极讨论 RAG 和部署等特性。未报告重大怀疑。

**标签**: `#LLM`, `#Agent`, `#RAG`, `#Learning`, `#Tutorial`

---

<a id="item-11"></a>
## [谷歌太空机器学习基础设施](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) ⭐️ 9.0/10

项目 Suncatcher 在太空中部署机器学习基础设施，使用 TPU 增强数据处理能力，利用独特环境进行 AI 计算。 该项目因其创新方法解决太空数据处理挑战、强大的社区参与度和通过基于太空的数据处理 SaaS 进行潜在盈利而受到关注。 该项目处于 alpha 阶段，需要在太空中进行复杂部署，并存在高成本和环境问题等显著限制。

hackernews · xnx · 9月24日 13:53 · [社区讨论](https://news.ycombinator.com/item?id=49830606)

**背景**: 项目 Suncatcher 属于日益发展的太空技术生态系统，与 Starcloud 等计划竞争。卫星技术的最新进展使此类项目成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/">Learn about Google ’ s Project Suncatcher to put ML infrastructure in...</a></li>
<li><a href="https://aiwiki.ai/wiki/project_suncatcher">Project Suncatcher | AI Wiki</a></li>
<li><a href="https://www.hopsworks.ai/dictionary/machine-learning-infrastructure">Machine Learning Infrastructure - MLOps Dictionary | Hopsworks</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一，一些人强调数据处理成本降低的潜力，其他人则提出对环境影响和可行性的担忧。

**标签**: `#AI`, `#Space`, `#Infrastructure`, `#ML`, `#Data`

---

<a id="item-12"></a>
## [Whiteboard：一个开源的协作软件设计 IDE](https://github.com/devdotfast/whiteboard) ⭐️ 8.0/10

Whiteboard 是一个开源的桌面应用程序，它使人类和 AI 代理能够通过共享工作空间协作设计软件，集成了 Claude Code 和 Codex 等工具。 Whiteboard 在 Hacker News 上获得了 302 个星标和 116 条评论，显示出显著的社区兴趣。它通过在共享工作空间中集成人类和代理的协作，提供了一种新颖的软件设计方法。 Whiteboard 在 MIT 许可证下发布，目前仅限于 macOS，并提供语义差异查看器和决策日志等功能。它与 Claude Code 和 Codex 等工具集成。

hackernews · sidharthkmenon · 9月24日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=49833867)

**背景**: Whiteboard 解决了软件设计中“白板会议”的需求，开发者可以在此协作理解和迭代系统。它利用 CodeOSS 进行代码集成和语义差异功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Visual_Studio_Code">Visual Studio Code - Wikipedia</a></li>
<li><a href="https://en.linuxadictos.com/code-oss-vscodium-or-visual-studio-code-what-should-i-install-on-linux.html">Code OSS, VSCodium or Visual Studio Code: what should you install on Linux</a></li>

</ul>
</details>

**社区讨论**: 社区评论对工具审查生成代码的潜力及其独特方法表示兴奋，将其与 revue 和 C4 等类似项目进行比较。

**标签**: `#AI`, `#Agent`, `#Software Design`, `#Collaboration`, `#Desktop`

---

<a id="item-13"></a>
## [使用 LLM 解码 17 世纪炼金术文本](https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical) ⭐️ 8.0/10

该项目使用大型语言模型（LLM）解码和追踪 17 世纪信件中的历史炼金术知识，专注于文本分析和历史研究。 该项目因其在高登网（131 个点，26 条评论）上的高参与度以及其在历史研究中的独特问题解决潜力而具有重要意义，并通过专门的 API 或 SaaS 解决方案具有盈利机会。 该项目处于 alpha 阶段，需要 Python 和可能需要 GPU 支持，未提及特定许可证。部署复杂性适中，与历史数据库的集成是关键。

hackernews · benbreen · 9月24日 19:14 · [社区讨论](https://news.ycombinator.com/item?id=49835531)

**背景**: 炼金术知识一直是历史研究中的一个利基领域，对原始文本的访问有限。近年来，LLM 的进步使其分析和解码这些文本成为可能，为研究开辟了新的途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@venkatesh.curious.in/unlocking-the-mysteries-of-large-language-models-a-deep-dive-c4d6f8c0153e">Unlocking the Mysteries of Large Language Models : A Deep... | Medium</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models ( LLMs )? | IBM</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/">Introduction to Large Language Model (LLM) - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对项目潜力的兴奋，有些人强调了其在家谱研究和数字人文中的应用。其他人建议与现有的历史数据库集成。

**标签**: `#LLM`, `#Historical`, `#Digital Humanities`, `#Alchemy`, `#Text Analysis`

---

<a id="item-14"></a>
## [Opus 5.5 用于 AI 解说视频](https://launchvideo.io/) ⭐️ 8.0/10

Opus 5.5 是一款 AI 工具，能够根据文本提示创建解说视频，利用先进自然语言处理和视频生成能力。 Opus 5.5 拥有 249 个星标和 130 条评论，显示出强烈的社区兴趣。它解决了自动化视频创建的需求，这一细分领域具有明确的 SaaS 或 API 盈利潜力。 该项目采用宽松许可协议，目前处于生产成熟度，部署复杂度低。它可以与 OpenRouter API 集成以增强功能。

hackernews · iacguy · 9月24日 20:28 · [社区讨论](https://news.ycombinator.com/item?id=49836374)

**背景**: Opus 5.5 运行在 AI 视频创建生态系统中，由于对吸引人内容的需求，该领域发展迅速。Synthesia 和 Canva 等替代品提供类似服务，但 Opus 5.5 专注于解说视频，使其脱颖而出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5.5 - Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.synthesia.io/tools/explainer-video-maker">Free AI Explainer Video Maker - Synthesia</a></li>

</ul>
</details>

**社区讨论**: 社区评论非常积极，用户称赞其能够创建高质量的解说视频，并指出其在商业应用中的潜力。一些人对其长期价值表示怀疑，但承认其当前实用性。

**标签**: `#AI`, `#Video`, `#Tools`, `#Explainer`, `#SaaS`

---

<a id="item-15"></a>
## [新型伪造 1024 位 RSA 签名方法](https://eprint.iacr.org/2026/2131.pdf) ⭐️ 8.0/10

该项目介绍了一种新型方法，以几乎与整数筛法（SNFS）相同的速度伪造 1024 位 RSA 签名，利用 Joux-Naccache-Thomé算法而不对模数进行因式分解。 它因高关注度（63 分，11 条评论）及其对密码安全的影响而具有重要意义，突出了当前 RSA 实践中一个关键漏洞，尽管它需要 RSA 预言机，限制了直接盈利。 该项目处于 alpha 阶段，操作需要 RSA 预言机，部署复杂度中等，未提及特定硬件要求。

hackernews · int0x29 · 9月24日 14:26 · [社区讨论](https://news.ycombinator.com/item?id=49831098)

**背景**: RSA 仍然是密码学的基石，但 1024 位密钥越来越容易受到攻击。该项目基于 Joux 等人在 2007 年的工作，展示了密码分析理论突破的实际影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sieve_theory">Sieve theory - Wikipedia</a></li>
<li><a href="https://news.e-ink.me/en/archive/2026-09-25/article/forging-1024-bit-rsa-signatures-in-nearly-snfs-time">Forging 1024 - bit RSA signatures in nearly SNFS... | E-Ink News Daily</a></li>

</ul>
</details>

**社区讨论**: 开发者对理论和实践意义感到兴奋，指出其对 RSA 预言机的依赖以及未来算法改进的潜力。

**标签**: `#Cryptography`, `#RSA`, `#Security`, `#Cryptanalysis`, `#Breakthrough`

---