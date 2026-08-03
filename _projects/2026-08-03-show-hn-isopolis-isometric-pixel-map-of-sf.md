---
layout: default
title: "旧金山等距像素地图"
date: 2026-08-03T12:00:00+00:00
discovered_date: 2026-08-03
slug: 2026-08-03-show-hn-isopolis-isometric-pixel-map-of-sf
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Isopolis 使用 3D 图块和 three.js 为旧金山创建一个等距像素地图，提供独特的、可滚动的城市探索体验。 该项目在 Hacker News 上拥有 178 个星标和 37 条评论，显示出社区的兴趣。它在等距像素艺术风格中提供了一种新颖的城市地图可视化方法，解决了城市探索的创意问题，并可能对游戏开发或教育领域有用。 该项目采用开源许可证，似乎已达到生产成熟度，并使用 three.js 进行渲染，这可能取决于硬件要求，部署复杂度适中。"
tags: "Map, Isometric, 3D, City, Web"
---

# 旧金山等距像素地图


> Isopolis 使用 3D 图块和 three.js 为旧金山创建一个等距像素地图，提供独特的、可滚动的城市探索体验。 该项目在 Hacker News 上拥有 178 个星标和 37 条评论，显示出社区的兴趣。它在等距像素艺术风格中提供了一种新颖的城市地图可视化方法，解决了城市探索的创意问题，并可能对游戏开发或教育领域有用。 该项目采用开源许可证，似乎已达到生产成熟度，并使用 three.js


**项目链接**：https://sf.isopolis.city/
**作者**：nuwandavek
**发布时间**：2026-08-03T00:46:38Z
**挖掘日期**：2026-08-03
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Map, Isometric, 3D, City, Web


## 📌 项目详解

Isopolis 使用 3D 图块和 three.js 为旧金山创建一个等距像素地图，提供独特的、可滚动的城市探索体验。 该项目在 Hacker News 上拥有 178 个星标和 37 条评论，显示出社区的兴趣。它在等距像素艺术风格中提供了一种新颖的城市地图可视化方法，解决了城市探索的创意问题，并可能对游戏开发或教育领域有用。 该项目采用开源许可证，似乎已达到生产成熟度，并使用 three.js 进行渲染，这可能取决于硬件要求，部署复杂度适中。


## 🌐 背景与生态

Isopolis 利用美国政府提供的免费 LIDAR 数据为旧金山创建一个详细的 3D 地图，填补了类似 Isometric.nyc 等项目中之前未探索的创意城市可视化领域。


## 💬 社区讨论

社区评论对项目的独特视觉风格及其扩展到教育或游戏工具的潜力表示兴奋，一些人指出了一些小错误并提出了改进建议。


## 🚀 应用前景

该项目可用于创建城市规划或历史可视化的教育工具，并在房地产或旅游等行业通过 SaaS 或 API 模型实现潜在的商业化。


## 🔧 技术栈

核心技术栈包括 three.js 用于 3D 渲染，Google 的 Photorealistic 3D Tiles 用于数据，以及 JavaScript 用于网页界面。


## 🎯 上手难度

难度：进阶。前提条件包括 JavaScript 知识和访问 3D 图块数据。步骤包括使用 three.js 设置项目并集成 3D 图块数据。


## 👥 目标用户

目标用户包括对创意数据可视化和城市探索感兴趣的 backend 工程师、ML 实践者和城市规划者。


## ⚖️ 类似项目对比

竞品包括 Isometric.nyc 和 Floor796，它们专注于等距城市地图，但缺乏 Isopolis 的 3D 图块集成和详细探索功能。


## 📚 参考链接

- [Tiles and tilemaps overview - Game development | MDN](https://developer.mozilla.org/en-US/docs/Games/Techniques/Tilemaps)
- [Three.js - Wikipedia](https://en.wikipedia.org/wiki/Three.js)
- [What (exactly) is three.js for? - Discussion - three.js forum](https://discourse.threejs.org/t/what-exactly-is-three-js-for/36588)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[lawrencechen]: Behind the scenes stuff:  https:&#x2F;&#x2F;sf.isopolis.city&#x2F;dev.html  &gt; The source is Google Photorealistic 3D Tiles. Isometric.nyc explored and rejected the use of 3d building data. It is pretty insane that US gov has free LIDAR data for every city in the US available to the public. I spent &lt;30mins exploring this and stuck to google 3d images. Claude Code whipped up a scraper to stream the 3D Tiles and render with three.js. This gives the best &quot;real&quot; texture base for th...

[EZ-Cheeze]: https:&#x2F;&#x2F;arstechnica.com&#x2F;science&#x2F;2018&#x2F;04&#x2F;these-oblique-satell...  &quot;Satellite images from highly oblique angles are pretty mindblowing&quot; If u like this u will like that

[murphyslab]: Incredible. It&#x27;s easy to just go on browsing and exploring. The massive, scrollable pixel art aspect reminds me a little of Floor796:  https:&#x2F;&#x2F;floor796.com&#x2F;

[cyanregiment]: A few AI anomalies, like several roads turning into rivers and lakes. There are also a few massive square ponds in the Tenderloin that I am pretty sure do not exist lol But I like the idea.

[jtfrench]: Those who know game dev know making good isometric maps can be deceptively difficult. You grabbed that bull by the horns and did so beautifully. Well done!

</details>
