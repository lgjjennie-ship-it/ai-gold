---
layout: default
title: "Nori机器人：为开发者设计的低成本人形机器人"
date: 2026-09-02T12:00:00+00:00
discovered_date: 2026-09-02
slug: 2026-09-02-launch-hn-nori-robotics-yc-s26-a-low-cost-humanoid-robot-for-development
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Nori机器人开发了一款售价1,688美元的双臂人形机器人，专为机器人开发者和研究人员设计，具备19个自由度、两个7+1自由度手臂，以及用于板载处理的Raspberry Pi 5。 该项目因其低成本和强烈的社区兴趣而受到关注，解决了机器人研究中昂贵硬件的痛点，并通过直接面向消费者的销售提供了明确的盈利潜力。 Nori采用开源许可证，目前处于生产阶段（Beta版），部署复杂度适中。它需要Raspberry Pi 5和稳定的互联网连接才能实现全部功能。"
tags: "Robotics, Humanoid, Development, Research, AI"
---

# Nori机器人：为开发者设计的低成本人形机器人


> Nori机器人开发了一款售价1,688美元的双臂人形机器人，专为机器人开发者和研究人员设计，具备19个自由度、两个7+1自由度手臂，以及用于板载处理的Raspberry Pi 5。 该项目因其低成本和强烈的社区兴趣而受到关注，解决了机器人研究中昂贵硬件的痛点，并通过直接面向消费者的销售提供了明确的盈利潜力。 Nori采用开源许可证，目前处于生产阶段（Beta版），部署复杂度适中。它需要Raspbe


**项目链接**：https://www.norirobotics.com/
**作者**：AntonioLi
**发布时间**：2026-09-01T17:35:10Z
**挖掘日期**：2026-09-02
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Robotics, Humanoid, Development, Research, AI


## 📌 项目详解

Nori机器人开发了一款售价1,688美元的双臂人形机器人，专为机器人开发者和研究人员设计，具备19个自由度、两个7+1自由度手臂，以及用于板载处理的Raspberry Pi 5。 该项目因其低成本和强烈的社区兴趣而受到关注，解决了机器人研究中昂贵硬件的痛点，并通过直接面向消费者的销售提供了明确的盈利潜力。 Nori采用开源许可证，目前处于生产阶段（Beta版），部署复杂度适中。它需要Raspberry Pi 5和稳定的互联网连接才能实现全部功能。


## 🌐 背景与生态

人形机器人市场随着AI和机器人技术的进步而增长，使得昂贵机器人变得难以获得。Nori通过提供低成本替代方案填补了这一空白。


## 💬 社区讨论

社区评论指出RC式伺服电机导致手臂动作不流畅和缺乏精度的问题，同时其他人质疑其真实世界能力，并将其与更先进的人形机器人如Atlas进行比较。


## 🚀 应用前景

Nori可用于机器人研究、教育和小规模自动化任务。其潜在应用包括清洁、物体操作和控制环境中的人机交互。


## 🔧 技术栈

技术栈包括Python、Raspberry Pi 5、高比率伺服电机、差分轮式底座和双麦克风阵列。SDK支持远程操作和演示工具。


## 🎯 上手难度

入门评级为进阶。前提条件包括Python 3.8+、GPU和API密钥。步骤包括设置Raspberry Pi、安装SDK并运行基本远程操作脚本。


## 👥 目标用户

目标用户是个人开发者、机器人研究人员和小型企业团队，行业包括制造业和医疗保健。


## ⚖️ 类似项目对比

竞品包括Svaya Robotics的双臂人形机器人，专注于自然双手交互，以及波士顿动力的Atlas，以其先进的移动性而闻名。


## 📚 参考链接

- [Dual Arm Robots : The Technology Accelerating the Humanoid Era](https://en.bonsystems.com/newsletter/dual-arm-robot-actuator/)
- [Bimanual Humanoid Robot by Svaya Robotics - Humanoid .guide](https://humanoid.guide/product/bimanual/)

<details><summary>📄 查看原文内容</summary>


Hey HN, I’m Antonio from Nori Robotics (<a href="https:&#x2F;&#x2F;norirobotics.com">https:&#x2F;&#x2F;norirobotics.com</a>). We build a $1,688 bimanual mobile robot in San Francisco for robotics developers and researchers.<p>I started working on Nori while doing robotics research at Columbia. I was teaching robots through human demonstrations, but getting my hands on affordable hardware was difficult. Most labs have one or two expensive robots, which makes it hard to collect large datasets, run long experiments, or test across several robots.<p>So I built my own. After seven iterations the latest Nori has:<p>* 19 degrees of freedom<p>* Two 7+1 DOF arms with a 1.5 kg payload per arm<p>* A 55 kg telescoping lift<p>* A differential wheeled base<p>* Four 720p, 30 fps RGB cameras<p>* 2D lidar<p>* A dual microphone array with full-duplex voice communication<p>* A 432 Wh battery<p>* A Raspberry Pi 5 with 4 GB RAM (SLAM and safeties are run on board, heavier ACT and VLAs must be run from a computer via LAN or a server via WAN)<p>Getting this under $2,000 was the main engineering challenge. Nori has more than 100 moving and structural parts, so costs add up quickly across actuators, bearings, wiring, power delivery, and assembly. Some main choices we made to get the cost low was using high-ratio servos instead of QDD motors, and using a wheel base instead of legs.<p>We assemble each robot in San Francisco and have designed it to be easy to manufacture and repair (we offer 3D files to print repairs).<p>Our open SDK includes teleoperation and demonstration tools: <a href="https:&#x2F;&#x2F;github.com&#x2F;Nori-Robotics&#x2F;nori-sdk-py" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;Nori-Robotics&#x2F;nori-sdk-py</a><p>We also built a browser-based simulator so you can try it out: <a href="https:&#x2F;&#x2F;lab.norirobotics.com&#x2F;nori&#x2F;model">https:&#x2F;&#x2F;lab.norirobotics.com&#x2F;nori&#x2F;model</a><p>We’ve shipped our first robot and are building the next batch. Eventually, we want people without robotics experience to teach Nori tasks and share them with other owners.<p>Currently the hardware is already capable of basic cleaning tasks, opening drawers, restocking shelves and pouring beers. Here is a video of Nori doing things: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;VRfVXHfQvD8" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;VRfVXHfQvD8</a><p>We make money by selling the hardware for $1,688, with optional paid software on top. Parts of hardware are open source. More details are in our hardware paper: <a href="https:&#x2F;&#x2F;doi.org&#x2F;10.48550&#x2F;arXiv.2605.16537" rel="nofollow">https:&#x2F;&#x2F;doi.org&#x2F;10.48550&#x2F;arXiv.2605.16537</a><p>If you work in robotics, what would you build with a robot at this price? What would you change about the hardware?


--- Top Comments ---

[elictronic]: The biggest problem is they are using RC style servos.  This is why all the arm motions are jerky and lack precision. What this means:
No force feedback on positioning.  
Jerky motion due to actuator steps.  
Limited precision.  
Terrible slow motion control performance.  Fast movements will look better.
Inability to solve problems with software. Basically think of all the joints like those cheap thermal camera screens that are at 320 x 240 resolution.  For rough work or finding some sort of ...

[jonplackett]: Looks cool. Can you be up front about its real capabilities. Are these videos of it eg tidying up real or just staged &#x2F; cherry picked? If you let it loose in a messy room or stirring something in a kitchen, what are the genuine results you would expect in the wild? We’re all used to seeing things like Atlas back flipping but then can’t do anything in a real environment. Just curious how this fits in and what the success &#x2F; fail rate is.

[arjie]: Where are you guys in SF? Would love to come see it. Mostly interested in seeing the speed of action (what multiple is the video replay at, etc.) and looking at center-of-mass etc. issues. I have a pretty straightforward use-case in a home. The Dreame we have in the living room is pretty good at avoiding most obstacles, but I usually have an LLM-based agent review the image automatically and either send out the vacuum or suggest moving things that would foul it up. Works great. Obviously subs...

[theahura]: honored to welcome another nori* business, alongside - nori.ai (ai health coach) - heynori.com (ai family hub) - nori inc (soil based carbon sequestration) - noriagentic.com (that&#x27;s us, ai cloud infrastructure) and my personal favorite - nori.co (makers of &#x27;The Nori Cloud&#x27; a clothes steamer, as seen on Oprah&#x27;s Favorite Things)

[mrnotcrazy]: My question would be how riffable is it? I don&#x27;t have 10-20k to drop on a robot. I work for co-ops so while I make good money(90k~ pretty good!) its less than I could make else where but the trade off is I have more time to build random stuff. 2k is the price point for me where I might buy a big thing every so many years, teaching this to play board games, making new hands for it, teaching it to clean etc would be fun and at a price point that works for me. I would probably want a suctio...

</details>
