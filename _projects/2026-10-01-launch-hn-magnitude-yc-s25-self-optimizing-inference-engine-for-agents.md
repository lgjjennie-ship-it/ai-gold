---
layout: default
title: "用于代理的自优化推理引擎"
date: 2026-10-01T12:00:00+00:00
discovered_date: 2026-10-01
slug: 2026-10-01-launch-hn-magnitude-yc-s25-self-optimizing-inference-engine-for-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Magnitude 是一个推理引擎，旨在通过设备上的编译和调优来优化自身，以在各种硬件平台上实现快速性能。 Magnitude 因其高性能和硬件兼容性而受到关注，解决了高效运行本地代理的痛点。 Magnitude 在 Apache 2.0 许可下，已达到生产就绪的成熟度，并提供动态内存分配，适合同时运行多个代理会话。"
tags: "Inference, AI, Optimization, Hardware, Performance"
---

# 用于代理的自优化推理引擎


> Magnitude 是一个推理引擎，旨在通过设备上的编译和调优来优化自身，以在各种硬件平台上实现快速性能。 Magnitude 因其高性能和硬件兼容性而受到关注，解决了高效运行本地代理的痛点。 Magnitude 在 Apache 2.0 许可下，已达到生产就绪的成熟度，并提供动态内存分配，适合同时运行多个代理会话。


**项目链接**：https://github.com/magnitudedev/magnitude
**作者**：anerli
**发布时间**：2026-09-30T17:37:40Z
**挖掘日期**：2026-10-01
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Inference, AI, Optimization, Hardware, Performance


## 📌 项目详解

Magnitude 是一个推理引擎，旨在通过设备上的编译和调优来优化自身，以在各种硬件平台上实现快速性能。 Magnitude 因其高性能和硬件兼容性而受到关注，解决了高效运行本地代理的痛点。 Magnitude 在 Apache 2.0 许可下，已达到生产就绪的成熟度，并提供动态内存分配，适合同时运行多个代理会话。


## 🌐 背景与生态

传统的推理引擎在性能和兼容性之间进行权衡。Magnitude 通过优化两者来填补这一空白，使其对本地硬件相关。


## 💬 社区讨论

社区评论指出基准测试结果不一，一些用户报告解码时间更快，但预填充时间比其他引擎慢。


## 🚀 应用前景

Magnitude 可用于需要高效本地模型推理的场景，例如 AI 开发工具、个人助手和边缘计算应用。


## 🔧 技术栈

Magnitude 使用 Rust 构建，包括自定义 GPU 内核运行时和自动调谐器，利用了 FlashAttention 和 SGLang 基数注意等技术。


## 🎯 上手难度

难度：进阶。前提条件包括 Python 3.8+、GPU（可选）和基本的 Rust 知识。步骤包括克隆仓库、安装依赖项并运行测试。


## 👥 目标用户

目标用户包括 AI 开发者、研究人员以及希望部署基于本地代理的应用的企业。


## ⚖️ 类似项目对比

竞品包括 llama.cpp、Ollama 和 SGLang，Magnitude 的不同之处在于其专注于自优化和针对特定硬件的调优。


## 📚 参考链接

- [I built an inference engine from scratch. Here is what I learnt](https://www.linkedin.com/pulse/i-built-inference-engine-from-scratch-here-what-learnt-ishan-jain-gqemc)
- [Inference Engine : A Simple Explanation | by Abhinav Pratap | Medium](https://pabhi18.medium.com/inference-engine-a-simple-explanation-80d319a492be)
- [What Is an Inference Engine and How Does It Function?](https://www.gmicloud.ai/ja/blog/what-is-an-inference-engine)

<details><summary>📄 查看原文内容</summary>


Hey HN, Anders and Tom here. We&#x27;re building Magnitude, an inference engine for agents that optimizes itself to run as fast as possible on your hardware. It works on Mac, Linux, and Windows on any hardware and is up to 2x faster than llama.cpp.<p>We&#x27;re both software engineers and previously built an open source browser agent to 4k+ GH stars and 100k+ downloads. We increasingly wanted to run it on local models, but found that no inference engine worked for our use case.<p>Inference engines today all make a performance tradeoff. They are either:<p>- Built for batched inference on datacenter hardware at the cost of single-session performance (vLLM, SGLang)
- Designed for broad compatibility instead of optimizing for specific hardware (llama.cpp, Ollama)
- Specialized for specific hardware or models but lacking engine completeness (oMLX, ds4)<p>Plus none of them are designed for running agents locally. Sessions are long, several often run at once, and you still want to use your computer for other things.<p>Magnitude is built for maximum performance on your hardware and running local agents:<p>- On-device compilation and tuning: Kernels are written with flexible parameters that are tuned on your actual device before the model runs. This gives you broad hardware compatibility with the same performance ceiling as hardware-specific kernels.<p>- Focus on best architectures: We write our tunable, highly efficient kernels for the most popular open-weights families. This allows us to achieve and surpass the performance of hardware or model specialized engines, without forcing ourselves to over-generalize at the cost of performance.<p>- Dynamic memory allocation: Magnitude reserves only enough memory up front to hold model weights. As your agent sessions grow, the memory heap dynamically increases, and frees itself when agents stop. Your hardware can still be used for other stuff while agents run.<p>- Hybrid paged attention: We borrow the best ideas from engines like SGLang to allow concurrent sessions to share prefix caches, but optimize placement for memory-adjacency so single-session performance doesn&#x27;t suffer.<p>Magnitude is fully open source (Apache 2.0). We built it in Rust, including a custom GPU kernel runtime and autotuner. We take inspiration from the best innovations in inference from academics (e.g. FlashAttention, FlashInfer, TurboQuant) as well as other engines (e.g. SGLang radix attention) to reach the performance ceiling.<p>Benchmarked against llama.cpp with Qwen 3.6 35B A3B (4 bit), 64k context, no speculative decoding:<p>Metal (Mac M4 Pro 48 GB)
- 92% faster decode (30 tok&#x2F;s → 57 tok&#x2F;s)
- 9% faster prefill (466 tok&#x2F;s → 507 tok&#x2F;s)
- 28% less per-agent memory usage<p>CUDA (DGX Spark)
- 19% faster decode (49 tok&#x2F;s → 58 tok&#x2F;s)
- 23% faster prefill (2,033 tok&#x2F;s → 2,507 tok&#x2F;s)
- 27% less per-agent memory usage<p>Magnitude ships as a desktop app that you can easily connect with whatever agents you already use (Pi, OpenCode, Hermes, Codex, and more). It automatically runs models on demand when these agents actually need them, and shuts them down after inactivity.
Here&#x27;s what it looks like: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=0qE8BWEZu7o" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=0qE8BWEZu7o</a><p>We&#x27;re excited to push Magnitude further to let you run bigger models on the same hardware while continuing to improve performance. Our plans include:<p>- Expert streaming: store experts on RAM or disk and load them just-in-time. This lets you run models bigger than what otherwise would fit on your GPU.<p>- Kernel compiler: our current kernels tune a few parameters to fit your hardware. We can take this further with a fully custom compiler that automatically chooses how to fuse kernels and which implementations to use, to make it fit to your hardware even better.<p>- Multi-device utilization: Make the best possible use of all hardware on a system (CPU, GPUs, RAM, disk) by detecting these and automatically solving for the best model layout.<p>We&#x27;d love for more people to try it out and give us feedback. Feel free to comment here, we&#x27;ll be around all day!


--- Top Comments ---

[mrtsepelev]: Congrats on launch! Tried it on the gemma-4-26b-qat-4bit model. Was indeed faster on token generation then on oMLX (82.8 tok&#x2F;s vs 76.5 tok&#x2F;s), but the prefill time was ~2.6x slower (709 tok&#x2F;s vs 1843 tok&#x2F;s). Don’t use any acceleration on the oMLX. Macbook M5 Pro, 48 gb

[lxe]: On my local inference box I have a perpetual codex thread open in my llama.cpp checkout that I periodically ask to take a look at currently pending llama.cpp PRs, do some research on latest MTP, Dflash and other prediction or attention optimizations, do research on the latest model quants and finetunes, take a look at localLlama Reddit threads and just do essentially a sweep of the frontier. Then it rebuilds latest llama.cpp, grabs the PRs it finds relevant to test against, and then it perfor...

[bythreads]: Ok so i took the time to benchmark this on the following on my m5 max 128gb: Qwen3-4B-Instruct-2507-4bit 
Qwen3.5-35B-A3B-4bit
Qwen3.5-9B-MLX-4bit
Qwen3-Reranker-0.6B-4bit
Qwen3-Coder-30B-A3B-Instruct-4bit
qwen2.5:0.5b and the results are what i kinda expected to begin with, this adds next to nothing? - also the repo was pivoted from a playwright sub assembly to this not long ago - so my conclusion - THIS MIGHT be worth some watching if you have a model where no-one!, has optimized it at all ...

[sebastienburel]: On a Mac the baseline I&#x27;d want is MLX, not llama.cpp. llama.cpp isn&#x27;t the fast path on Apple Silicon for most models people run locally, so a speedup over llama.cpp could still be slower than mlx_lm. Do you have that number? Second, more important for agents: decode speed is rarely what hurts. It&#x27;s resending the same system prompt plus tool schemas every turn. Does self-optimizing cover prefix cache reuse across requests, or is it kernel and layout tuning only? And is the endpo...

[kmike84]: This seems to be a good idea. However, beating llama.cpp on speed is a low bar :) I found it to be a good baseline, but at least on Mac there was always something way faster, and&#x2F;or with better memory requirements - like you said, ds4, omlx, mtplx, etc. It seems if you use local LLMs for real, there is very little reason not to use one of the more optimized engines. 3 main failure modes I observed in the engines: * Not using best available spec decoding * Using too much VRAM for KV cache...

</details>
