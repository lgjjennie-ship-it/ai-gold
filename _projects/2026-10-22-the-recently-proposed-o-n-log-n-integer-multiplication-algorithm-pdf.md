---
layout: default
title: "高效整数乘法算法"
date: 2026-10-22T12:00:00+00:00
discovered_date: 2026-10-22
slug: 2026-10-22-the-recently-proposed-o-n-log-n-integer-multiplication-algorithm-pdf
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目提出了一种高效的整数乘法算法，具有亚二次复杂度，利用了先进的数学技术。 它因其高参与度而受到关注，并解决了一个重要的计算问题，在密码学和高性能计算中具有潜在应用。 该算法处于alpha阶段，需要高级数学知识，没有直接的部署复杂性，但需要专门的理解。"
tags: "Algorithm, Mathematics, Computational, Cryptography, Performance"
---

# 高效整数乘法算法


> 该项目提出了一种高效的整数乘法算法，具有亚二次复杂度，利用了先进的数学技术。 它因其高参与度而受到关注，并解决了一个重要的计算问题，在密码学和高性能计算中具有潜在应用。 该算法处于alpha阶段，需要高级数学知识，没有直接的部署复杂性，但需要专门的理解。


**项目链接**：https://web.maths.unsw.edu.au/~davidharvey/research/subnlogn.pdf
**作者**：craigcitro
**发布时间**：2026-10-22T02:30:52Z
**挖掘日期**：2026-10-22
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Algorithm, Mathematics, Computational, Cryptography, Performance


## 📌 项目详解

该项目提出了一种高效的整数乘法算法，具有亚二次复杂度，利用了先进的数学技术。 它因其高参与度而受到关注，并解决了一个重要的计算问题，在密码学和高性能计算中具有潜在应用。 该算法处于alpha阶段，需要高级数学知识，没有直接的部署复杂性，但需要专门的理解。


## 🌐 背景与生态

整数乘法算法已经发生了显著演变，当前的重点是亚二次复杂度以提高密码学和大规模计算中的效率。


## 💬 社区讨论

社区评论强调了正式证明的需求，并探讨了多项式乘法和素数域DFT相关改进。


## 🚀 应用前景

该算法可以增强密码学系统和高性能计算任务，特别是在需要大量整数操作的场景中。


## 🔧 技术栈

该算法主要是数学的，但使用Lean进行形式化验证，并且可能使用Python进行实现。


## 🎯 上手难度

难度：进阶。前提条件包括Python和数学背景。步骤包括理解论文，并可能实现该算法。


## 👥 目标用户

目标用户是数学家、研究人员以及从事密码学和高性能计算的开发人员。


## ⚖️ 类似项目对比

竞争对手包括Schönhage-Strassen算法和现代多项式乘法算法。该项目为大型整数提供更高效的方法。


## 📚 参考链接

- [Integer multiplication in time O ( n log n )](https://hal.science/hal-02070778/document)
- [Integer multiplication in time O ( n logn)](https://web.maths.unsw.edu.au/~davidharvey/talks/nlogn-unsw2019.pdf)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[jdb1729]: &gt; It would be good to have a formalised proof of the o(n log n) result, for example in Lean. As far as I can tell, one does not yet exist. The result is fully formalized in Lean by @platypii and myself (on Mathlib&#x27;s TM2 machine), with ongoing improvements to the exponent (currently at 1-2^-14.38):  https:&#x2F;&#x2F;github.com&#x2F;platypii&#x2F;integer-mult-bounds-lean  Contributions are welcome!

[Kapura]: &gt; I have not actually read the paper. In fact, there are three closely related papers [TC26a], [TC26b], [TC26c], and I have not read any of them. I tried, but soon gave up. The math(s) dump does not appear to be strong on exposition. Instead, I asked Fable to explain [TC26a] to me. Fable seems to understand the argument and thinks that it is correct. this does not feel like a healthy place to be

[kenferry]: &gt; There is one other aspect of the situation that I would like to emphasise. After two weeks of very
hard work, I have managed to understand only a small fraction of [TC26a]. When I ask Fable about
the paper, it seems to read and understand the whole thing in just a few minutes, even starting
from a fresh context. I know that some readers may be uncomfortable with my anthropomorphic
terminology, but I believe that “understand” is accurate, in the sense that the LLM seems to be able
to corr...

[jdb1729]: &gt;  The new result does not directly imply new complexity bounds for polynomial multiplication over a fixed finite field, say multiplication in F2[x]. The state of the art for this problem is an algorithm that multiplies polynomials of degree n in time O(n log n 4^log*(n)) [HvdH19]. @platypii and I obtained a Lean proof of the same improvement for DFT over prime-order finite fields (yielding polynomial multiplication via the convolution theorem):  https:&#x2F;&#x2F;github.com&#x2F;platypii&...

[flebron]: Note in this case the title says &quot;O(n log n)&quot;, but the important part is this is &quot;o(n log n)&quot;, not just &quot;O(n log n)&#x27;. The former is a strict subset of the latter. We already knew how to multiply two n-bit integers in O(n log n) time, via the FFT.

</details>
