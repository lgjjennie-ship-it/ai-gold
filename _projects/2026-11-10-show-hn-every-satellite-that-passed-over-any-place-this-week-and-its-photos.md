---
layout: default
title: "实时卫星追踪与地球影像"
date: 2026-11-10T12:00:00+00:00
discovered_date: 2026-11-10
slug: 2026-11-10-show-hn-every-satellite-that-passed-over-any-place-this-week-and-its-photos
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该网络应用追踪过去一周内飞越指定位置的每一颗卫星，并显示其真实的Sentinel-2、Landsat或NASA影像。它使用SGP4目录追踪超过17,000个物体，并使用GPU加速在浏览器中渲染轨道。 该项目因其高参与度（374个星标，66条评论）和提供真实卫星影像的独特效用而受到关注。它解决了访问特定卫星数据的痛点，并利用了当前地理空间技术的趋势，具有教育和商业应用潜力。 该项目采用MIT许可证，已投入生产，部署复杂度适中。它需要浏览器支持GPU加速，并整合了Sentinel-2、Landsat和NASA的数据。未提及超出标准网页浏览器能力之外的硬件要求。"
tags: "Satellite, Geospatial, Image, Data, Web"
---

# 实时卫星追踪与地球影像


> 该网络应用追踪过去一周内飞越指定位置的每一颗卫星，并显示其真实的Sentinel-2、Landsat或NASA影像。它使用SGP4目录追踪超过17,000个物体，并使用GPU加速在浏览器中渲染轨道。 该项目因其高参与度（374个星标，66条评论）和提供真实卫星影像的独特效用而受到关注。它解决了访问特定卫星数据的痛点，并利用了当前地理空间技术的趋势，具有教育和商业应用潜力。 该项目采用MIT许可证，


**项目链接**：https://www.watched.earth/
**作者**：a585gupt
**发布时间**：2026-11-09T17:51:31Z
**挖掘日期**：2026-11-10
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Satellite, Geospatial, Image, Data, Web


## 📌 项目详解

该网络应用追踪过去一周内飞越指定位置的每一颗卫星，并显示其真实的Sentinel-2、Landsat或NASA影像。它使用SGP4目录追踪超过17,000个物体，并使用GPU加速在浏览器中渲染轨道。 该项目因其高参与度（374个星标，66条评论）和提供真实卫星影像的独特效用而受到关注。它解决了访问特定卫星数据的痛点，并利用了当前地理空间技术的趋势，具有教育和商业应用潜力。 该项目采用MIT许可证，已投入生产，部署复杂度适中。它需要浏览器支持GPU加速，并整合了Sentinel-2、Landsat和NASA的数据。未提及超出标准网页浏览器能力之外的硬件要求。


## 🌐 背景与生态

该项目运行于地理空间生态系统，利用卫星数据进行地球观测。虽然存在替代方案，但该应用通过结合实时追踪和高分辨率影像脱颖而出。轨道力学和开源卫星目录数据的近期进步使此类项目成为可能。


## 💬 社区讨论

社区评论强调该项目在数据整合、风格和内容方面的美感。用户赞赏卫星轨道和地面轨迹的详细可视化，同时也有人建议改进UI/UX。


## 🚀 应用前景

该应用可解决农业、灾害管理和环境监测等现实问题。潜在产品包括面向企业的订阅式SaaS或开发者API访问。盈利模式可能涉及分层定价或卫星数据市场。


## 🔧 技术栈

核心技术栈包括JavaScript（通过WebGL实现GPU加速）、Python用于后端处理，并与Sentinel-2、Landsat和NASA API集成。使用SGP4模型进行轨道追踪。


## 🎯 上手难度

难度：入门。开始使用前，请确保使用支持GPU的现代网页浏览器。除此之外无需特定软件。流程包括访问网站、输入位置，并观察卫星数据和影像。


## 👥 目标用户

目标用户包括卫星爱好者、研究人员、教育工作者以及地理空间领域的 enterprise 团队。角色范围从后端工程师到ML从业者。


## ⚖️ 类似项目对比

竞品包括'OpenStreetMap'（通用地图）和'NOAA的GOES'（气象卫星数据）。该项目通过专注于实时卫星追踪和高分辨率影像而有所区别。


## 📚 参考链接

- [SGP4](https://en.wikipedia.org/wiki/SGP4)
- [Sentinel-2](https://en.wikipedia.org/wiki/Sentinel-2)
- [Kepler's equation](https://en.wikipedia.org/wiki/Kepler's_equation)

<details><summary>📄 查看原文内容</summary>


hey HN, i built this because I&#x27;m a satellite nerd who was bored this past weekend.<p>type in any place and it finds every satellite that passed over it in the last 7 days (SGP4 on the CelesTrak catalog, tracking 17k+ objects and runs in your browser in about half a second), then pulls the real Sentinel-2 &#x2F; Landsat &#x2F; NASA images from those passes.<p>fun fact: all ~17k objects in orbit are drawn on the GPU, solving Kepler&#x27;s equation every frame. also cool is that Sentinel-2 timestamps are often 5-10 min off from when the sat actually crosses your spot, so some cool math was involved in making it accurate on the site.<p>it only shows real images taken from those exact satellites, and it never store your location.<p>code: <a href="https:&#x2F;&#x2F;github.com&#x2F;dev-Armaan&#x2F;satellites" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;dev-Armaan&#x2F;satellites</a><p>would love feedback, contributions, or whatever else you guys can offer!


--- Top Comments ---

[adonovan]: Beautifully done, at so many levels: the pincushion view of just how much stuff is up there; the rendering of the orbit of each satellite; the ground track of its aperture; the time series of its passes. So many data sources seamlessly integrated. Even if Claude wrote every line of code, knowing what to ask for is quite a feat. Amazing.

[HoldOnAMinute]: I don&#x27;t say this lightly:  This may be the best combination of style and substance I have ever seen.

[lanewinfield]: Nice site. Likely very few people will care this much, but with a couple of very easy changes you would make this feel a LOT less vibe coded. The giveaways: * Instrument Sans (your logo) * Highlighted period in your logo * Highlighted italicized text in your header text (also in Instrument Sans) * Short punchy AI-written sentences. Just merge that into one sentence! (&quot;Enter any place on Earth to see every satellite that passed over it in the last week and the pictures they took there.&qu...

[sixtyj]: I have seen a lot of sites with satellites’ overviews… I work in geospatial. This site is really good one as you can see exact image taken by a satellite. Well done.

[nonameiguess]: The first half of my second career (third maybe) in software was spent in satellite ground processing. My first true culminating project, so to speak, was when the portion of the US Maritime Domain Awareness meant for use by the Navy went to initial operational capability. I checked out your site briefly. It&#x27;s mildly amusing to note differences between that and a real system in use by military units. It&#x27;d be nice to be able to use a selector of some sort rather than typing in a loca...

</details>
