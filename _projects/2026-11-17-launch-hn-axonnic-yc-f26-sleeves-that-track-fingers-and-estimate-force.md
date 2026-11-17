---
layout: default
title: "Axonnic肌电袖珍机器人训练"
date: 2026-11-17T12:00:00+00:00
discovered_date: 2026-11-17
slug: 2026-11-17-launch-hn-axonnic-yc-f26-sleeves-that-track-fingers-and-estimate-force
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Axonnic开发了一种前臂袖珍，通过读取肌肉活动来解码手指运动并估计指尖力量，有助于灵巧机器人训练。 该项目在Hacker News上获得高关注度，提供了一种使用肌电数据的新型机器人训练方法，解决了传统视频方法的局限性，并具有明确的盈利路径。 袖珍使用64个表面肌电通道，与手部跟踪同步，并估计指尖力量。它已获得生产许可，并在关节角度估计方面表现出高精度。"
tags: "EMG, Robotics, Wearable, Human-Machine Interaction, Data Collection"
---

# Axonnic肌电袖珍机器人训练


> Axonnic开发了一种前臂袖珍，通过读取肌肉活动来解码手指运动并估计指尖力量，有助于灵巧机器人训练。 该项目在Hacker News上获得高关注度，提供了一种使用肌电数据的新型机器人训练方法，解决了传统视频方法的局限性，并具有明确的盈利路径。 袖珍使用64个表面肌电通道，与手部跟踪同步，并估计指尖力量。它已获得生产许可，并在关节角度估计方面表现出高精度。


**项目链接**：https://news.ycombinator.com/item?id=50522776
**作者**：arshpatankar
**发布时间**：2026-11-16T20:29:48Z
**挖掘日期**：2026-11-17
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：EMG, Robotics, Wearable, Human-Machine Interaction, Data Collection


## 📌 项目详解

Axonnic开发了一种前臂袖珍，通过读取肌肉活动来解码手指运动并估计指尖力量，有助于灵巧机器人训练。 该项目在Hacker News上获得高关注度，提供了一种使用肌电数据的新型机器人训练方法，解决了传统视频方法的局限性，并具有明确的盈利路径。 袖珍使用64个表面肌电通道，与手部跟踪同步，并估计指尖力量。它已获得生产许可，并在关节角度估计方面表现出高精度。


## 🌐 背景与生态

肌电技术在机器人学中的应用日益增多，因为它能够捕捉肌肉活动，这比单独的视频更具信息量。Axonnic的方法通过专注于灵巧机器人训练，填补了传统方法难以解决的空白。


## 💬 社区讨论

社区评论对在双人舞和机器人领域的潜在应用表示兴奋，同时也提出了对疲劳变化和硬件可靠性的担忧。


## 🚀 应用前景

该技术可应用于机器人、自动化和医疗保健行业，用于训练灵巧机器人、假肢和康复。盈利模式可能通过SaaS、API服务或直接硬件销售实现。


## 🔧 技术栈

技术栈包括表面肌电传感器、用于解码手指运动的机器学习模型，以及与手部跟踪的同步。基础设施涉及定制PCB设计以减少干扰。


## 🎯 上手难度

难度：进阶。前提条件包括Python和访问肌电数据。步骤包括设置袖珍、校准传感器和运行解码软件。


## 👥 目标用户

目标用户是机器人工程师、研究人员和自动化行业的公司。角色包括后端工程师、机器学习实践者和DevOps专家。


## ⚖️ 类似项目对比

竞品包括Meta的肌电可穿戴技术和其他使用基于视频的手部跟踪的项目。Axonnic的优势在于其专注于肌电以获取肌肉活动洞察。


## 📚 参考链接

- [TMSi — an Artinis company — What Is Electromyography ( EMG )?](https://www.tmsi.artinis.com/blog/what-is-emg)
- [What Is EMG ( Electromyography ) and How Does It Work?](https://imotions.com/blog/learning/research-fundamentals/electromyography-101/)
- [Axonnic: Muscle-sensing sleeves for robot training | Product Hunt](https://www.producthunt.com/products/axonnic)

<details><summary>📄 查看原文内容</summary>


Hi HN! We’re Arsh and Max, founders of Axonnic (<a href="https:&#x2F;&#x2F;axonnic.com">https:&#x2F;&#x2F;axonnic.com</a>). We’ve developed a forearm sleeve that reads muscle activity to decode finger movements and estimate fingertip force, while leaving the hands bare. It’s used to record human movement and generate training data for dextrous robots.<p>Here’s a demo video: <a href="https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;xBrocTc9cfA" rel="nofollow">https:&#x2F;&#x2F;youtube.com&#x2F;shorts&#x2F;xBrocTc9cfA</a><p>We’ve found that electromyography (EMG) is a much better way to train robots than by video alone because video only captures movement, not muscle activity or the effort behind the movement. A useful signal can be present even when the hand barely moves; just maintaining a grip involves muscle activation. The subtle muscle movements that can barely be picked up in video are the most important details for activities like sewing and delicate assembly.<p>The sleeve has 64 channels of surface electromyography, or EMG. Electrodes on the skin detect electrical activity from muscles in the forearm. We distribute sensors across the forearm so as to not overfit to one muscle group. We synchronize EMG with hand tracking to train a model that predicts finger joint angles, then we run the decoder solely from EMG, adding in fingertip force estimates that have been calibrated from finger presses on force sensors.<p>When the user takes the sleeve off then puts it back on again, the electrode positions change, so we run tests over separate wearings. In one case, we ran a 215-second recording, four days after training, without any recalibration, and compared the results with Apple Vision Pro hand tracking. The result was just 6.9° error across 20 joint angles. We’ve published the measurements and evaluation details here: <a href="https:&#x2F;&#x2F;axonnic.com&#x2F;benchmarks">https:&#x2F;&#x2F;axonnic.com&#x2F;benchmarks</a>.<p>We faced many challenges doing recordings in factories, including wireless interference and unreliable off-the-shelf hardware. This led to some bad recordings and the need to repeat data collection. For that reason, we’re developing our own electronics that use a wired PCB design that will eliminate interference and timing inconsistencies.<p>Axonnic grew out of Max&#x27;s EMG research at Oxford. We looked at using the technology for computer control, then we thought a more promising use-case was in capturing the effort involved in skilled manual tasks. This technology could be described as a computer to human interface. Where computers gain insight and learn from human skills. Sewing particularly stood out because the material deforms and the operator is constantly adjusting grip and tension.<p>Maxim has an Oxford MBiol and conducted research on high-density surface EMG. He previously built internal tools at Skyscanner and worked at Voxblock across PCB development and supply chain. Arsh studied medicine at Oxford and has research experience applying machine learning to medical imaging, alongside software and robotics projects. Together we have built the sleeve, decoding software and data-collection system and tested them in industrial settings.<p>So far we have the tech being used to record sewing and other manual tasks at a European manufacturer, which signed an LOI for support with robotic implementation. We have also collected construction demonstrations involving electricians, plumbers and demolition work. These are pilot and data-collection examples. Separately, our public demos include controlling a Proception robotic hand from forearm EMG.<p>If you’ve done any of your own trials for training robots for manual tasks, we’d love to hear about what tasks you were trying to train for and how the trials went. We’re happy to discuss the hardware, calibration and models here in the comments. Thanks!<p><a href="https:&#x2F;&#x2F;axonnic.com">https:&#x2F;&#x2F;axonnic.com</a>


--- Top Comments ---

[millspore]: How does it handle fatigue shift, like if someone&#x27;s been gripping stuff for an hour the emg baseline must drift pretty hard

[nickthenerd]: Looks like a full sleeve version of what Meta is working on?  https:&#x2F;&#x2F;www.meta.com&#x2F;emerging-tech&#x2F;emg-wearable-technology&#x2F;

[knuckleheads]: I&#x27;ve wanted these for measuring how much force is applied via the hands during partner dancing for a long time. There&#x27;s a lot of subtly there that isn&#x27;t visible and I&#x27;ve long wondered how to measure and visualize that. Very neat! Hope I get to try one someday.

[lanewinfield]: This is great! And you&#x27;ve done the hard part super well. You know, the actual underpinning tech. But the &quot;easy&quot; part— I would immediately bounce off your page due to its clear vibe-designed and, most importanty, -worded nature. Eyebrows like &quot;Newer demos · newest first&quot;, italicized and contrastly colored words in sentences, and the two-to-three sentence phrased paragraphs (like &quot;Your best workers do the task wearing our EMG sleeve, on camera, with hand tracking. ...

[unpleasurable]: Are you planning to control human arms with this?

</details>
