---
layout: default
title: "指数时间假设的推翻"
date: 2026-10-27T12:00:00+00:00
discovered_date: 2026-10-27
slug: 2026-10-27-the-exponential-time-hypothesis-is-false-pdf
source: hackernews
category: show-hn
ai_score: 7.0
summary: "该项目提出了一篇数学论文，挑战了计算复杂性理论中的指数时间假设（ETH），表明许多先前被认为需要指数时间的问题可能存在更好的解决方案。 它现在很重要，因为项目获得了显著的社区关注（617个星标，222条评论），表明其与核心计算机科学问题的相关性。虽然它是理论性的，但它有可能在未来对算法设计和复杂性研究产生影响。 该项目是一篇理论性论文，没有直接的盈利模式，但获得了显著的社区关注。它可以在GitHub上作为PDF获取，并讨论了其对计算机科学的影响。"
tags: "Mathematics, Computer Science, Theoretical, Complexity, NP-Completeness"
---

# 指数时间假设的推翻


> 该项目提出了一篇数学论文，挑战了计算复杂性理论中的指数时间假设（ETH），表明许多先前被认为需要指数时间的问题可能存在更好的解决方案。 它现在很重要，因为项目获得了显著的社区关注（617个星标，222条评论），表明其与核心计算机科学问题的相关性。虽然它是理论性的，但它有可能在未来对算法设计和复杂性研究产生影响。 该项目是一篇理论性论文，没有直接的盈利模式，但获得了显著的社区关注。它可以在GitHu


**项目链接**：https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
**作者**：vok
**发布时间**：2026-10-26T21:59:15Z
**挖掘日期**：2026-10-27
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Mathematics, Computer Science, Theoretical, Complexity, NP-Completeness


## 📌 项目详解

该项目提出了一篇数学论文，挑战了计算复杂性理论中的指数时间假设（ETH），表明许多先前被认为需要指数时间的问题可能存在更好的解决方案。 它现在很重要，因为项目获得了显著的社区关注（617个星标，222条评论），表明其与核心计算机科学问题的相关性。虽然它是理论性的，但它有可能在未来对算法设计和复杂性研究产生影响。 该项目是一篇理论性论文，没有直接的盈利模式，但获得了显著的社区关注。它可以在GitHub上作为PDF获取，并讨论了其对计算机科学的影响。


## 🌐 背景与生态

指数时间假设（ETH）是计算复杂性理论中的一个基本猜想，断言3-SAT不能在次指数时间内解决。该项目的推翻可能对理解计算难度和算法设计产生深远影响。


## 💬 社区讨论

社区评论对结果表示兴奋，指出其对P vs NP的影响以及复杂性类别分离的罕见性。一些人讨论了潜在的应用和与其他方法的比较。


## 🚀 应用前景

这可能对算法设计和复杂性研究产生影响，特别是在密码学和优化等领域。潜在的应用包括为NP完全问题开发更高效的算法。


## 🔧 技术栈

该项目是纯数学和理论性的，没有提到特定的技术栈。它依赖于计算复杂性理论和数学证明。


## 🎯 上手难度

入门：该项目不适合初学者，因为它需要深入的计算复杂性理论知识。先决条件包括熟悉3-SAT和ETH。


## 👥 目标用户

目标用户包括计算机科学和数学领域的研究人员、学者和高级学生，他们对理论计算机科学感兴趣。


## ⚖️ 类似项目对比

竞品包括像“3-SAT的次指数算法”和“NP完全问题的改进下界”这样的项目。该项目在其方法和对ETH的更广泛影响方面有所不同。


## 📚 参考链接

- [Exponential time hypothesis](https://en.wikipedia.org/wiki/Exponential_time_hypothesis)
- [Exponential - Time Hypothesis Overview](https://www.emergentmind.com/topics/exponential-time-hypothesis)
- [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)

<details><summary>📄 查看原文内容</summary>


See also: <i>Announcing three new discoveries in mathematics, computer science, and physics</i> - <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50251344">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50251344</a>


--- Top Comments ---

[svat]: While this has no immediate bearing on P-vs-NP, it is interesting to note: - Early CS researchers like Donald Knuth entered CS in the days when regularly someone would come up with a surprising faster algorithm for some problem, and their intuitions were that most problems had faster algorithms than you&#x27;d expect. - Later generations of CS researchers, as all the easy algorithms were discovered, and post Karp&#x27;s definition of NP-completeness (and the Garey &amp; Johnson book, say), be...

[cochne]: This is an amazing and unexpected result.  To be clear though, it does not imply that NP is subexponential: &quot;Note that runtime bounds of the form 2^o(n) do not transfer under general polynomial-time reductions (2^n^o(1) would be needed for this), so our result does not imply that general NP problems
admit subexponential time algorithms.&quot; Edit: To explain more, it is guaranteed that you can  reduce  any NP problem to 3SAT in polynomial time with a polynomial factor in input size.  Yo...

[zodiac]: It appears that Anthropic has released a proof as well (same bounds), but with a different approach?  https:&#x2F;&#x2F;drive.google.com&#x2F;drive&#x2F;u&#x2F;0&#x2F;folders&#x2F;1uaWnPqWkXy1sjfsD...

[criemen]: Wow. Complexity class separations are really really rare. Can an expert in sat solving comment if there&#x27;s any immediate applications of the method from the paper? Or is SAT solving in general pretty far away from worst-case times, and this is a theoretical algorithm which would be hard to apply in practice.

[strommec]: It&#x27;s surprising that Exponential Time Hypothesis would be false. Quoting a paper from 2022[1]: &gt; We prove that the time complexity of self-attention is necessarily quadratic in the input length, unless the Strong Exponential Time Hypothesis (SETH) is false[...] If OpenAI&#x27;s proof is correct, does that mean self-attention can be implemented in sub-quadratic time? I.e. we could eventually have all the most advanced LLMs running on cheap hardware? To put it more playfully, is ETH bei...

</details>
