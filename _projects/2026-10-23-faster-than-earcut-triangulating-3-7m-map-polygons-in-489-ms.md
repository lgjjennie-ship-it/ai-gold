---
layout: default
title: "更快的地图多边形三角剖分库"
date: 2026-10-23T12:00:00+00:00
discovered_date: 2026-10-23
slug: 2026-10-23-faster-than-earcut-triangulating-3-7m-map-polygons-in-489-ms
source: hackernews
category: show-hn
ai_score: 9.0
summary: "该库能够在仅489毫秒内三角剖分3.7M个大型地图多边形，其性能优于现有方法。 它因高社区参与度（216票，40条评论）和显著的性能提升而受到关注，为制图和地理空间应用提供了实用价值。 采用MIT许可证，已达到生产就绪成熟度，专注于C++部署，对硬件要求不高但最适合大型数据集。"
tags: "Mapping, Triangulation, Performance, Geospatial, Libraries"
---

# 更快的地图多边形三角剖分库


> 该库能够在仅489毫秒内三角剖分3.7M个大型地图多边形，其性能优于现有方法。 它因高社区参与度（216票，40条评论）和显著的性能提升而受到关注，为制图和地理空间应用提供了实用价值。 采用MIT许可证，已达到生产就绪成熟度，专注于C++部署，对硬件要求不高但最适合大型数据集。


**项目链接**：https://globus.software/blog/2026/10/16/cutting-map-polygons/
**作者**：molind
**发布时间**：2026-10-22T09:31:18Z
**挖掘日期**：2026-10-23
**AI 评分**：9.0/10
**来源**：hackernews
**标签**：Mapping, Triangulation, Performance, Geospatial, Libraries


## 📌 项目详解

该库能够在仅489毫秒内三角剖分3.7M个大型地图多边形，其性能优于现有方法。 它因高社区参与度（216票，40条评论）和显著的性能提升而受到关注，为制图和地理空间应用提供了实用价值。 采用MIT许可证，已达到生产就绪成熟度，专注于C++部署，对硬件要求不高但最适合大型数据集。


## 🌐 背景与生态

三角剖分在制图中至关重要，Earcut是广泛使用的基准。该项目通过优化速度而非捆绑包大小进行创新，以满足日益增长的快速多边形处理需求。


## 💬 社区讨论

开发者对性能感到兴奋，将其与Earcut和Delaunay32进行比较，同时寻求优化技术和三角形质量方面的见解。


## 🚀 应用前景

非常适合GIS、制图服务和城市规划。可以通过API访问、企业许可证或用于复杂多边形任务的专用模块进行变现。


## 🔧 技术栈

使用C++构建，通过WASM进行优化，利用地理空间库和高效内存管理实现速度。


## 🎯 上手难度

入门难度。需要Python 3.8+、基本的C++知识以及现代CPU。通过pip安装并运行示例数据集以验证性能。


## 👥 目标用户

面向后端开发者、GIS工程师以及城市规划或地理空间分析领域的研究人员。


## ⚖️ 类似项目对比

Earcut（速度更快但捆绑包较小）、Delaunay32（约束三角剖分）和Turf.js（JavaScript库）。该项目在大型数据集的原始速度方面表现优异。


## 📚 参考链接

- [earcut - npm](https://www.npmjs.com/package/earcut?activeTab=dependents)
- [GitHub - mapbox/ earcut at pkgstats.com](https://github.com/mapbox/earcut?ref=pkgstats.com)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[amelius]: Should mention the mother of all triangulators:  https:&#x2F;&#x2F;www.cs.cmu.edu&#x2F;~quake&#x2F;triangle.html

[mourner]: Hey Evgen, Earcut author here — thanks for the writeup and a really cool library! I need to see if there are any tricks to borrow for Earcut&#x27;s JS version. :) One thing to note is that I deliberately had to reject some of the potential optimizations to keep the library small, so that bundle size doesn&#x27;t blow up — for most practical applications (e.g. Mapbox GL JS), it&#x27;s already fast enough (and 4.1k min&#x2F;gz). Curious how big the WASM build of Earstrip is. On the C++ side, Ma...

[morishuz]: awesome. the performance improvements looks impressive! i’m the author of Delaunay32, a constrained delaunay triangulator with polygon and hole support. it uses divide-and-conquer rather than incremental insertion, so im curious how it would compare with the delaunay baseline here.  https:&#x2F;&#x2F;github.com&#x2F;morishuz&#x2F;delaunay32  i havent benchmarked on your corpus yet, and our current polygon api requires simple rings with non-touching holes. thanks for publishing the datasets, t...

[stymaar]: I see that the result contains lots of very long, very thin triangles. Aren&#x27;t those generally the worse case scenario for the GPU rasterizer?

[mistercow]: I&#x27;ve wondered for a long time why ear clipping + optimizations has won on triangulation over stuff like Seidel&#x27;s trapezoidal method, which has O(nlog*n) time complexity and handles holes naturally. I know big-O isn&#x27;t everything, but that&#x27;s essentially linear versus quadratic, and it seems like we care about triangulating more and more complex polygons as time goes on. Is it just a triangle quality thing? Does Seidel lead to too many hard to deal with slivers?

</details>
