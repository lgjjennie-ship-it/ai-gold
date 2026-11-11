---
layout: default
title: "面向编码代理的现代网页指导"
date: 2026-11-11T12:00:00+00:00
discovered_date: 2026-11-11
slug: 2026-11-11-show-hn-get-your-coding-agent-off-2019-javascript-onto-modern-web-primitives
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目为现代网页开发提供精选最佳实践，利用浏览器原生特性增强编码代理，涉及CSS.highlights、<dialog>和showModal()以及field-sizing。 该项目凭借380个星标和121条评论展现出强大吸引力，通过利用现代网页原语解决了编码代理默认采用旧模式的问题，并具备通过SaaS或API模式实现商业化的清晰路径。 项目采用开源许可，已达到生产成熟度，部署复杂度低，无需特定硬件要求，但需与浏览器原生特性集成。"
tags: "Web Development, Coding Agents, Browser Primitives, Chrome, Firefox"
---

# 面向编码代理的现代网页指导


> 该项目为现代网页开发提供精选最佳实践，利用浏览器原生特性增强编码代理，涉及CSS.highlights、<dialog>和showModal()以及field-sizing。 该项目凭借380个星标和121条评论展现出强大吸引力，通过利用现代网页原语解决了编码代理默认采用旧模式的问题，并具备通过SaaS或API模式实现商业化的清晰路径。 项目采用开源许可，已达到生产成熟度，部署复杂度低，无需特定硬


**项目链接**：https://github.com/GoogleChrome/modern-web-guidance
**作者**：paulirish
**发布时间**：2026-11-10T18:01:15Z
**挖掘日期**：2026-11-11
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Web Development, Coding Agents, Browser Primitives, Chrome, Firefox


## 📌 项目详解

该项目为现代网页开发提供精选最佳实践，利用浏览器原生特性增强编码代理，涉及CSS.highlights、<dialog>和showModal()以及field-sizing。 该项目凭借380个星标和121条评论展现出强大吸引力，通过利用现代网页原语解决了编码代理默认采用旧模式的问题，并具备通过SaaS或API模式实现商业化的清晰路径。 项目采用开源许可，已达到生产成熟度，部署复杂度低，无需特定硬件要求，但需与浏览器原生特性集成。


## 🌐 背景与生态

该项目位于网页开发和AI代理的生态系统中，填补了LLM训练数据中遗留代码模式的空白。它基于CSS.highlights和<dialog>等现代浏览器API构建。


## 💬 社区讨论

社区评论强调了浏览器特性支持差异，建议通过GitHub Pages发布markdown索引，对Chrome的主导地位表示担忧，并讨论了实施挑战。


## 🚀 应用前景

该项目通过引导代理使用现代浏览器特性，能够解决网页开发中的实际问题，适用于前端开发工具、调试和代码生成等领域，可通过SaaS或API模式实现商业化。


## 🔧 技术栈

核心技术栈包括JavaScript、CSS.highlights和<dialog>等现代浏览器API，以及支持CLI工具的基础设施，注重纯JS包。


## 🎯 上手难度

难度：进阶。前提条件包括Node.js和npm。步骤涉及安装CLI和搜索指南。项目针对CPU效率进行了优化。


## 👥 目标用户

目标用户为科技公司中的前端开发者、ML从业者及DevOps团队，特别是那些从事编码代理或网页开发工具开发的人员。


## ⚖️ 类似项目对比

竞品包括如'Web Dev Tools'和'Browser Extensions for AI Agents'等项目，它们在浏览器原生解决方案与第三方库的侧重上有所不同。


## 📚 参考链接

- [highlight () CSS pseudo-element - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
- [HTMLDialogElement: showModal () method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal)
- [field-sizing CSS property - CSS | MDN - MDN Web Docs CSS field-sizing | Chrome for Developers field-sizing - CSS-Tricks CSS property: field-sizing - Can I use field-sizing - Interactivity - Tailwind CSS "field-sizing" | Can I use... Support tables for HTML5, CSS3, etc Field-sizing just works! | Polypane](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)

<details><summary>📄 查看原文内容</summary>


Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without &lt;span&gt;s everywhere, `&lt;dialog&gt;` and showModal() give you backdrops and ideal focus management, `field-sizing` to auto-grow textareas as the user types.. (Something yesterday&#x27;s ftrain post touched on [0])<p>Models know about some of these by name, but consistently won&#x27;t default to using the platform-native solution and instead prefer the incumbent &lt;div&gt;+JS based pattern.  We started an effort in Chrome to supplement coding agents with this key domain knowledge and we&#x27;re shipping our 1.0 today, in collaboration with Firefox, MDN, and Edge.<p>200+ guides (~1.7MB) of curated, hand-crafted implementation best-practices from web experts, updated as the web evolves.  (Open source, obv, so.. we&#x27;ll welcome your bikeshedding ;) Readable versions here: [1]<p>I&#x27;ve spent the last 9 months obsessing over how to ship this as an agent skill + (Agentic RAG) CLI without blowing up your context window. (Or cedeing activation mechanics to MCP dynamic tool search). The skill description is minmaxed for activating on relevant frontend tasks. The RAG work I&#x27;m pretty proud of… originally a 500mb native stack down to a ~7MB pure-JS package, ~10ms search on your CPU.<p>We just introduced a deterministic &#x27;legacy-scan&#x27; (trained on 30k github repos) to identify old &#x27;n dusted patterns that your agent can modernize. (92% avg precision on held-out repos.)<p>People make a lot of claims about what coding agents are good&#x2F;bad at. We wanted receipts, so we invested heavily in eval infra [2] to help us hill-climb, but also to identify when knowledge is common enough we can prune our guides. (Ofc, some of the things we thought AI didn&#x27;t know turned out to be wrong :)  We run codex&#x2F;claude&#x2F;agy against 200 tasks without the skill and then with.. In total ~1,700 playwright&#x2F;AST-based assertions. Agents go from 55% pass unguided to 92% guided.<p>Try it out:<p><pre><code>    DISABLE_TELEMETRY=1 npx modern-web-guidance@latest install
    DISABLE_TELEMETRY=1 npx modern-web-guidance@latest search &quot;animate dialog modal&quot;
    DISABLE_TELEMETRY=1 npx modern-web-guidance@latest legacy-scan .&#x2F;src
</code></pre>
If you spot something wrong or weird, give us a holler!<p>Longer write-up on the 1.0:  <a href="https:&#x2F;&#x2F;developer.chrome.com&#x2F;blog&#x2F;modern-web-guidance-v1" rel="nofollow">https:&#x2F;&#x2F;developer.chrome.com&#x2F;blog&#x2F;modern-web-guidance-v1</a><p>---<p>0: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50416456">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50416456</a><p>1: <a href="https:&#x2F;&#x2F;developer.chrome.com&#x2F;docs&#x2F;modern-web-guidance&#x2F;guides" rel="nofollow">https:&#x2F;&#x2F;developer.chrome.com&#x2F;docs&#x2F;modern-web-guidance&#x2F;guides</a><p>2: <a href="https:&#x2F;&#x2F;googlechrome.github.io&#x2F;modern-web-guidance-src&#x2F;" rel="nofollow">https:&#x2F;&#x2F;googlechrome.github.io&#x2F;modern-web-guidance-src&#x2F;</a>


--- Top Comments ---

[surround]: Here&#x27;s a list of browser features the skills will tell your agent to use that are stable in Chrome but not supported by Firefox and Safari:     CSS @function
  CSS calc-size()
  CSS interpolate-size
  CSS corner-shape
  CSS border-shape
  CSS flex-wrap: balance
  CSS text-fit
  CSS text-decoration-skip-spaces
  CSS scroll-axis-lock
  CSS scroll-target-group
  CSS :target-current
  CSS scroll-initial-target
  CSS container scroll-state queries
  scrollsnapchange event
  scrollsnapchanging...

[simonw]: Distribution suggestion: in addition to the npm packages you have right now, set up GitHub Pages to publish a markdown index document of the skills at  https:&#x2F;&#x2F;googlechrome.github.io&#x2F;modern-web-guidance-src&#x2F;skill...  (currently a 404) That index page should link to plain markdown versions of all of the documents, and should be designed for search with grep to find the right answers. That way I don&#x27;t have to install anything at all - provided my agent has the ability t...

[advisedwang]: Chrome already has too much power in the browser standards world. The last thing we need is everyone&#x27;s LLMs to follow Chrome team&#x27;s guidance on how to do web development. This road leads back to &quot;To view this site, please view in [DOMINANT BROWSER]&quot;

[zahlman]: &gt; Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without &lt;span&gt;s everywhere I tried to look this up and found  https:&#x2F;&#x2F;developer.mozilla.org&#x2F;en-US&#x2F;docs&#x2F;Web&#x2F;CSS&#x2F;Reference&#x2F;S...  but the example depends on JS. How are you meant to statically specify highlighted ranges without the &lt;span&gt; markup? If I&#x27;m syntax-highlighting code on a blog, it&#x27;s seems a...

[merelydev]: &gt; Coding agents often default to older patterns because LLM training data contains vast amounts of legacy code. This often leads them to generate bloated JavaScript for tasks that now have native, high-performance web platform solutions. Yes, now I can confirm I am not a crackpot when I said this:  https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=49854536  The main problem I see is that it will be extremely hard for new frameworks, languages to take off if everyone is using AI to code. ...

</details>
