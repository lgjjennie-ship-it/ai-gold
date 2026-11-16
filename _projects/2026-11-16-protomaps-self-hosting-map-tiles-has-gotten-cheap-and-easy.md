---
layout: default
title: "Protomaps：自托管地图瓦片"
date: 2026-11-16T12:00:00+00:00
discovered_date: 2026-11-16
slug: 2026-11-16-protomaps-self-hosting-map-tiles-has-gotten-cheap-and-easy
source: hackernews
category: show-hn
ai_score: 7.0
summary: "Protomaps使开发者能够轻松且经济地自托管地图瓦片，减少对公共基础设施的依赖。它使用PMTiles格式，并提供托管API进行定制。 该项目因其366个星标和活跃讨论而具有重要意义，解决了对经济高效的映射解决方案的需求。它通过SaaS或API模式提供了明确的盈利途径。 Protomaps在开源许可证下，处于生产就绪的alpha阶段，部署复杂度低，无需特定硬件要求，标准云存储即可。"
tags: "Map, GIS, Web, API, Self-Hosting"
---

# Protomaps：自托管地图瓦片


> Protomaps使开发者能够轻松且经济地自托管地图瓦片，减少对公共基础设施的依赖。它使用PMTiles格式，并提供托管API进行定制。 该项目因其366个星标和活跃讨论而具有重要意义，解决了对经济高效的映射解决方案的需求。它通过SaaS或API模式提供了明确的盈利途径。 Protomaps在开源许可证下，处于生产就绪的alpha阶段，部署复杂度低，无需特定硬件要求，标准云存储即可。


**项目链接**：https://bruceroettgers.eu/blog/protomaps/
**作者**：bcye
**发布时间**：2026-11-15T19:26:22Z
**挖掘日期**：2026-11-16
**AI 评分**：7.0/10
**来源**：hackernews
**标签**：Map, GIS, Web, API, Self-Hosting


## 📌 项目详解

Protomaps使开发者能够轻松且经济地自托管地图瓦片，减少对公共基础设施的依赖。它使用PMTiles格式，并提供托管API进行定制。 该项目因其366个星标和活跃讨论而具有重要意义，解决了对经济高效的映射解决方案的需求。它通过SaaS或API模式提供了明确的盈利途径。 Protomaps在开源许可证下，处于生产就绪的alpha阶段，部署复杂度低，无需特定硬件要求，标准云存储即可。


## 🌐 背景与生态

该项目源于开发者对地图数据控制的日益增长的需求，减少对昂贵公共地图服务的依赖。它基于PMTiles格式，该格式正作为开源替代方案获得关注。


## 💬 社区讨论

社区评论强调了该项目在反向地理编码和隐私方面的实用性，并提出了改进大瓦片处理和URL加载的建议。


## 🚀 应用前景

Protomaps可用于需要自定义地图样式的应用程序，如物流、房地产和户外导航。其SaaS或API模式可通过分层访问或企业解决方案进行 monetization。


## 🔧 技术栈

技术栈包括用于矢量地图数据的PMTiles，用于托管的云存储，以及用于定制的REST API。它支持多种编程语言，并与Maplibre集成。


## 🎯 上手难度

入门评级为入门级。前提条件包括云存储帐户和基本的REST API知识。第一个可工作结果可以通过托管一个PMTiles文件并将其与一个地图库集成来实现。


## 👥 目标用户

目标用户包括个人开发者、GIS专业人士和企业，他们需要经济高效的映射解决方案。后端工程师和机器学习从业者可以从其灵活性中受益。


## ⚖️ 类似项目对比

竞品包括OpenFreeMap，它提供免费的公共地图实例，以及Cartes.app，它由于成本问题从Maptiler转向。这些替代方案侧重于易用性和成本节约。


## 📚 参考链接

- [Free OpenStreetMap vector tiles & world maps – OpenMapTiles](https://openmaptiles.org/)
- [Protomaps - The open source map in a file](https://protomaps.com/)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[boramalper]: OpenFreeMap is a similar project:  https:&#x2F;&#x2F;openfreemap.org&#x2F;  &gt;  What is OpenFreeMap?  &gt; OpenFreeMap lets you display custom maps on your website and apps for free. &gt; Using our public instance is completely free: there are no limits on the number of map views or requests. There’s no registration, no user database, no API keys, and no cookies. We aim to cover the running costs of our public instance through donations. &gt;  What is the tech stack?  &gt; There is no tile ...

[dromtrund]: The svg tiles are decent for reverse geocoding too. I&#x27;ve had great success splitting gps routes into segments by pulling location data out of relevant tiles. A lot of the reverse geocoding APIs have pretty restrictive per-second limits and response times in the order of 1-2 seconds. Hosting this in an s3 bucket costs an order of magnitude less than any of the APIs I tried at my scale, with millisecond latency, no request limits and near-flat volume scaling.

[neomantra]: We&#x27;re doing something like this behind Cloudflare R2, same concept of owning the map infra (for privacy and access-control) and reducing load on public infrastructure. If you are into this stuff, you can view PMTiles from the CLI with &quot;gloss&quot;, or try to drag-and-drop on its web interface [1].   It seems large tiles (&gt;128M) and some raster formats are failing; plus it would be nice to load from URL there.  Will fix that... (AI warning).  ntmaps [2] is a Golang library that le...

[maelito]: For Cartes.app we used to pay Maptiler. While great, recommanded to start, without client revenue it was impossible to scale, we&#x27;ve hit 150 €&#x2F;month bills way too fast. Hence Protomaps. Hosting costs almost nothing. The main problem though is that once you host your tiles, why not put what you want inside ? Tune Tilemaker&#x27;s processing.lua to your envy. Spend hours designing maps and building a Typescrpt dynamic Maplibre style.

[motoroco]: yeah, basemaps are small enough to store and host cost effectively, but high res satellite imagery gets big and expensive fast as you go up in zoom level. I built my own satellite mosaic of North America for my app so I can offer users offline access to the tiles and had to stop at z17 because of projected storage requirements. high res global coverage can get you into the hundreds of TB range which is no longer in the &quot;stick it on r2 and serve it with a worker&quot; or &quot;download an...

</details>
