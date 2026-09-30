---
layout: default
title: "实时太阳系可视化"
date: 2026-09-30T12:00:00+00:00
discovered_date: 2026-09-30
slug: 2026-09-30-show-hn-real-time-solar-system-with-526k-asteroids-and-all-tracked-satellites
source: hackernews
category: show-hn
ai_score: 8.0
summary: "该项目提供实时、交互式的太阳系可视化，包括52万小行星和所有已跟踪的卫星，使用WebGL2和Web Workers实现流畅渲染。 该项目因其高参与度（251个点，56条评论）和技术成就而脱颖而出，通过提供详细的实时可视化，解决了太空爱好者和教育者的实际问题。 该项目在开源许可下运行，已投入生产并表现出流畅的性能，需要WebGL2支持并每日从CelesTrak和JPL更新数据。"
tags: "Space, Visualization, WebGL, Education, Asteroids"
---

# 实时太阳系可视化


> 该项目提供实时、交互式的太阳系可视化，包括52万小行星和所有已跟踪的卫星，使用WebGL2和Web Workers实现流畅渲染。 该项目因其高参与度（251个点，56条评论）和技术成就而脱颖而出，通过提供详细的实时可视化，解决了太空爱好者和教育者的实际问题。 该项目在开源许可下运行，已投入生产并表现出流畅的性能，需要WebGL2支持并每日从CelesTrak和JPL更新数据。


**项目链接**：https://space.bl2.net/
**作者**：wanick
**发布时间**：2026-09-29T19:08:01Z
**挖掘日期**：2026-09-30
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Space, Visualization, WebGL, Education, Asteroids


## 📌 项目详解

该项目提供实时、交互式的太阳系可视化，包括52万小行星和所有已跟踪的卫星，使用WebGL2和Web Workers实现流畅渲染。 该项目因其高参与度（251个点，56条评论）和技术成就而脱颖而出，通过提供详细的实时可视化，解决了太空爱好者和教育者的实际问题。 该项目在开源许可下运行，已投入生产并表现出流畅的性能，需要WebGL2支持并每日从CelesTrak和JPL更新数据。


## 🌐 背景与生态

该项目利用WebGL2和Web Workers来处理可视化52万小行星和卫星的计算需求，这是一个结合了空间科学与先进网络图形的细分领域。


## 💬 社区讨论

社区评论强调了令人印象深刻的性能和教育价值，用户对详细的可视化表示兴奋，并请求更多功能。


## 🚀 应用前景

该项目在教育领域和太空探索方面具有强大的应用前景，可能为学校、博物馆和研究机构解决实际问题。


## 🔧 技术栈

核心技术栈包括用于渲染的WebGL2、用于轨道传播的Web Workers，以及来自CelesTrak和JPL的天体数据。


## 🎯 上手难度

难度：入门。要开始使用，请确保支持WebGL2的现代浏览器，并按照项目页面上的说明获取数据源。


## 👥 目标用户

目标用户包括对天文学和空间科学感兴趣的太空爱好者、教育者和学生。


## ⚖️ 类似项目对比

竞争对手包括LeoLabs（用于卫星可视化）和NASA的Eyes（用于更广泛的太阳系视图），尽管该项目在实时细节方面表现优异。


## 📚 参考链接

- [WebGL Explained : What is WebGL , How It Works & Use Cases](https://www.linkedin.com/pulse/webgl-explained-simple-words-beginner-friendly-uzfyc)
- [What Is WebGL ?](https://giscarta.com/blog/what-is-webgl)

<details><summary>📄 查看原文内容</summary>



--- Top Comments ---

[dunlin]: Always wanted to see the asteroid belt&#x27;s true density visualized; this really puts it into perspective. Impressive work keeping everything performant.

[wanick]: Author here. It&#x27;s a browser view of the Solar System at real scale, with its current state, plus the objects around Earth from the CelesTrak catalog. Data: CelesTrak TLEs (SGP4), asteroids and comets from JPL SBDB, spacecraft positions from JPL Horizons. Updated daily. Rendering is WebGL2, orbit propagation runs in web workers. The asteroid set (~30 MB) loads in the background. The time slider runs forwards and backwards; satellites appear and disappear by launch date.

[GnosiWorks]: 526k objects and it still feels smooth. are you culling by distance or doing something smarter on the gpu side?

[jurakovic]: No github repo? :(

[climech]: Just spent a little time following Europa Clipper, it will fly by Earth very soon! If you zoom out from Earth, it&#x27;s already pretty close. This will be its second gravity assist after Mars. Very cool site!

</details>
