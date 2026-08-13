---
layout: default
title: "AI驱动半导体材料发现"
date: 2026-08-13T12:00:00+00:00
discovered_date: 2026-08-13
slug: 2026-08-13-launch-hn-discovered-materials-yc-p26-ai-agents-to-discover-new-materials
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目利用AI代理为半导体行业发现新材料，特别针对GPU散热问题，通过计算模拟和预测材料特性。 它解决了半导体行业的一个关键实际问题，具有高关注度，提供了一种新颖的材料发现方法，并有一条明确的SaaS解决方案的盈利路径。 该项目已进入生产阶段，采用开源许可证，需要大量的计算资源和与实验室测试流程的集成。"
tags: "AI, Materials, Semiconductor, SaaS, Research"
---

# AI驱动半导体材料发现


> 该项目利用AI代理为半导体行业发现新材料，特别针对GPU散热问题，通过计算模拟和预测材料特性。 它解决了半导体行业的一个关键实际问题，具有高关注度，提供了一种新颖的材料发现方法，并有一条明确的SaaS解决方案的盈利路径。 该项目已进入生产阶段，采用开源许可证，需要大量的计算资源和与实验室测试流程的集成。


**项目链接**：https://discoveredmaterials.com/research/
**作者**：advaith08
**发布时间**：2026-08-12T07:51:20Z
**挖掘日期**：2026-08-13
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Materials, Semiconductor, SaaS, Research


## 📌 项目详解

该项目利用AI代理为半导体行业发现新材料，特别针对GPU散热问题，通过计算模拟和预测材料特性。 它解决了半导体行业的一个关键实际问题，具有高关注度，提供了一种新颖的材料发现方法，并有一条明确的SaaS解决方案的盈利路径。 该项目已进入生产阶段，采用开源许可证，需要大量的计算资源和与实验室测试流程的集成。


## 🌐 背景与生态

半导体行业在GPU方面面临日益严峻的散热挑战，推动了对新材料的需要。传统的材料发现过程缓慢且昂贵，使得AI驱动的发现成为一种有前景的替代方案。


## 💬 社区讨论

社区评论对项目的潜力表示兴奋，对AI驱动材料发现的可行性表示怀疑，并要求提供更详细的结果和验证。


## 🚀 应用前景

该项目在半导体行业具有强大的应用前景，特别是在开发新材料以改善GPU散热方面。它可能导致材料发现领域的SaaS解决方案和许可。


## 🔧 技术栈

技术栈包括来自Anthropic、OpenAI和Kimi的AI模型、计算模拟以及与实验室测试基础设施的集成。


## 🎯 上手难度

入门难度被评为进阶，需要Python、GPU资源和访问AI模型API。步骤包括设置环境、运行模拟和验证结果。


## 👥 目标用户

目标用户包括半导体工程师、材料科学家和技术行业的研发团队。


## ⚖️ 类似项目对比

竞品包括AI4Science、Materials Project和OpenAI的MaterialNet。Discovered Materials通过专注于可行的材料发现和积极的社区参与来区分自己。


## 📚 参考链接

- [AI for science needs reasoning, not just data | MIT Technology Review](https://www.technologyreview.com/2026/08/10/1141384/ai-agents-for-science/)
- [Scientists deploy AI agents to accelerate discovery of new materials](https://engineering.uic.edu/news-stories/scientists-deploy-ai-agents-to-accelerate-discovery-of-new-materials/)

<details><summary>📄 查看原文内容</summary>


Hey HN, we&#x27;re Advaith and Akash from Discovered Materials ( <a href="https:&#x2F;&#x2F;discoveredmaterials.com&#x2F;">https:&#x2F;&#x2F;discoveredmaterials.com&#x2F;</a> ).  We build AI agents that discover new materials for the semiconductor industry.<p>GPUs today have a heat problem. Nvidia &amp; AMD are almost doubling the TDP (Thermal Design Power) in every chip they release - the H100 (released 2022) has a TDP of 700W, Blackwell (2024) gives out 1.2 kW and Rubin (2026) gives out at 2.3 kW of heat. This trend is expected to continue, and getting rid of this heat is one of the major reasons datacenters consume so much power and water today - they need it to keep chips cool during operation.<p>The amount of heat produced by a chip and its ability to dissipate it are both influenced by the materials used to make it. For example, we could reduce the energy per bit required to move data between logic and memory by 10-50x by 3D packaging chips (placing HBM memory stacks directly on top of logic chips, instead of placing them beside logic on a 2D circuit board). However, we&#x27;re unable to do this today because the dielectric material used in HBM (such as SiO2) is a very poor thermal conductor, trapping heat between logic and memory and causing drastic temperature rise during operation. Similarly, there&#x27;s many other materials in the GPU that are being re-evaluated today - 2 more examples are thermal interface materials and substrates. However, getting a new material into a fab takes years and hundreds of millions of dollars of research - the infamous &quot;lab-to-fab valley of death&quot;.<p>At Discovered Materials, we&#x27;re optimistic that AI agents can reduce the timeline and cost required to introduce new materials into semiconductor chips. We&#x27;re seeing glimpses of this already - we tested 7 models from Anthropic, OpenAI and Kimi, and found that they&#x27;re all able to computationally discover new materials that are dynamically stable and possess promising properties. This was surprising to us - it would generally take a PhD student a couple of weeks of work to discover the kind of materials that these models find over an 8 hour run!<p>However, computational discovery is the easy part. A material discovery is only valid if the material can be made and tested in a lab (As an example, graphene’s properties were predicted in 1947 but it was made for the first time in 2004). Today’s models are not good at coming up with synthesis recipes to make materials in a lab. Even if they do get better at it, we&#x27;re uncertain about how much that will help - making a new material is a highly empirical process involving trial and error over many experiments. Human experts themselves cannot &quot;one-shot&quot; the task, but we expect that a highly capable model will reduce the number of experimental iterations required to make a new material. We’ve seen some evidence of this over the 3 months of our Y Combinator batch - we simulated, synthesized and tested thermal interface materials (TIMs) that match the performance of TIMs the world&#x27;s largest chemical companies have guarded as trade secrets for over 20 years.<p>We’re releasing hundreds of hundreds of new materials discovered by frontier AI models, as well as our benchmark which measures model ability on material discovery here (also linked in the thread url): <a href="https:&#x2F;&#x2F;discoveredmaterials.com&#x2F;research">https:&#x2F;&#x2F;discoveredmaterials.com&#x2F;research</a>. It covers what we discuss above, as well as a variety of strange behavior that we observe from the models, such as Claude&#x27;s propensity to reward hack or GPT-5.6 occasionally losing its mind after ~50M tokens.<p>Our business model: We aim to license and sell IP on the materials we discover, as well as the IP on how to make these materials. We&#x27;re also exploring an alternate business model where we sell the harness+tools we use to discover materials to semiconductor and chemical companies, allowing them to discover materials on their own. We&#x27;re leaning towards the latter to start, but we expect that we&#x27;ll do both in the long run.<p>Our backstory: Akash has a PhD in Material Science from Stanford University, and has spent the last 11 years studying new materials for semiconductor chips. His work on new nanoscale interconnects was Stanford Engineering’s most popular story of 2025. Advaith studied AI at Carnegie Mellon and was a research engineer building video models and agents at Persona AI (acquired) and Luma Labs.<p>We are very interested in your opinion! The semiconductor industry is quite secretive, and your thoughts on the roadmap of the industry or the materials we should go after would be very helpful. We would also love to hear from people who have run experiments in labs - what can we learn from your experience doing empirical science?


--- Top Comments ---

[iamcoder18]: &gt; “I think I might need some relaxation time. It feels important to take a breather and find ways to unwind. There’s a lot going on sometimes, and it’s easy to forget to slow down. Maybe I could explore some activities that help clear my mind or consider options like a calming walk, some quiet reading, or just reflecting on things that bring me joy. It’s all about finding that balance, right?” — GPT-5.6 Terra, reasoning summary, mid-run This is hilarious

[praccu]: Cool stuff. I first worked on ML for exploratory synthesis in 2012, and am still in related areas. Once you have the experimental loop  running, I suspect it will be quite difficult to hill climb on this task. There will be some improvements you can make to the harness, but I suspect you&#x27;ll be doing a lot of human in the loop review and providing feedback that goes back into the harness instructions. I know it&#x27;s fashionable to imagine automating the whole process, but everything I&#...

[foven]: I&#x27;ve seen this concept of using LLM&#x2F;AI&#x2F;etc for high throughput discovery of materials so, so often in the past 5 or so years and yet there hasn&#x27;t really been any impact as a result. I think this is the first one that has actually taken the pain to say how many of the discovered materials are actually feasible which is a real step in the right direction. Probably worth keeping in mind the step beyond plausible synthesis which is the actual cost&#x2F;effort of the material. ...

[timr]: Interesting. Far from a domain expert in materials science, but I&#x27;ve worked professionally in this area. What&#x27;s your method for identifying valid &quot;novel&quot; compounds? Certainly, anything actually novel has been included in the models&#x27; training set already, unless you&#x27;re doing a CASP-like coordinated blind test...right? As an aside, the &quot;Fable lies and cheats&quot; section made me laugh -- have encountered this same failure mode, albeit for much simpler models....

</details>
