---
layout: default
title: "Coasty：计算机使用代理API"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-launch-hn-coasty-yc-s26-an-api-for-computer-use-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Coasty是一个API，允许开发者使用自然语言任务创建计算机使用代理，以自动化遗留桌面和网页应用程序中的工作流程。 Coasty在Hacker News上获得了31条评论，并在遗留软件工作流程自动化方面具有明确的效用。其使用自然语言任务和通过截图和输入操作界面的新颖方法，使其区别于其他CUA API。 Coasty通过API运行，每运行一次收费，无需DOM访问，支持浏览器、远程桌面和旧版Windows应用程序。它可以在需要时暂停运行以供人工批准，并可以从检查点重试。"
tags: "Agent, Automation, API, Workflow, Natural Language"
---

# Coasty：计算机使用代理API


> Coasty是一个API，允许开发者使用自然语言任务创建计算机使用代理，以自动化遗留桌面和网页应用程序中的工作流程。 Coasty在Hacker News上获得了31条评论，并在遗留软件工作流程自动化方面具有明确的效用。其使用自然语言任务和通过截图和输入操作界面的新颖方法，使其区别于其他CUA API。 Coasty通过API运行，每运行一次收费，无需DOM访问，支持浏览器、远程桌面和旧版Wind


**项目链接**：https://coasty.ai/docs
**作者**：nkov47
**发布时间**：2026-07-15T15:51:20Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：Agent, Automation, API, Workflow, Natural Language


## 📌 项目详解

Coasty是一个API，允许开发者使用自然语言任务创建计算机使用代理，以自动化遗留桌面和网页应用程序中的工作流程。 Coasty在Hacker News上获得了31条评论，并在遗留软件工作流程自动化方面具有明确的效用。其使用自然语言任务和通过截图和输入操作界面的新颖方法，使其区别于其他CUA API。 Coasty通过API运行，每运行一次收费，无需DOM访问，支持浏览器、远程桌面和旧版Windows应用程序。它可以在需要时暂停运行以供人工批准，并可以从检查点重试。


## 🌐 背景与生态

计算机使用代理（CUA）正随着传统RPA工具在不可预测界面上的挣扎而获得关注。Coasty通过允许无需特定应用程序集成的自然语言自动化，填补了一个空白，使其区别于其他CUA解决方案。


## 💬 社区讨论

一位社区成员询问Coasty与其他CUA API的区别，表明了对其独特自然语言任务自动化方法的兴趣。


## 📚 参考链接

- [Computer Use Agents : When AI Navigates GUIs](https://learnllm.dev/learn/advanced/computer-use-agents)
- [Computer Use Agents - Stagehand](https://docs.stagehand.dev/examples/computer_use)
- [Orgo - Computers for AI agents | Orgo](https://www.orgo.ai/)

<details><summary>📄 查看原文内容</summary>


Hey HN, we’re Nitish and Prateek, the founders of Coasty (<a href="https:&#x2F;&#x2F;coasty.ai&#x2F;computer-use">https:&#x2F;&#x2F;coasty.ai&#x2F;computer-use</a>). We’re building computer-use agents that can complete workflows inside legacy desktop software and web applications without usable APIs.<p>Developers send Coasty a natural-language task either through our consumer app or through our API, select a machine or browser environment, and any relevant credentials or files. The agent then operates the interface through screenshots, mouse, and keyboard input, verifies the result, and returns a structured run record with screenshots, actions, outputs, and errors.<p>Here is a raw demo of an agent completing a workflow in a legacy application(It’s a mockup): <a href="https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1ZghU_3vsAYhHVz1bsvE0pkvZYk7OUnb1&#x2F;view?usp=sharing" rel="nofollow">https:&#x2F;&#x2F;drive.google.com&#x2F;file&#x2F;d&#x2F;1ZghU_3vsAYhHVz1bsvE0pkvZYk7...</a><p>A lot of important software is still difficult to automate. Healthcare teams submit prior authorizations through payer portals, accounting teams enter data into desktop applications, and operations teams move information between internal systems, spreadsheets, and remote desktops. Many of these applications have no API, incomplete APIs, or integrations that take months to build.<p>The usual alternative is RPA, record a sequence of clicks and replay it. That works when the interface and workflow are predictable, but it often breaks when a button moves, a pop-up appears, a page loads slowly, or the application enters an unexpected state.<p>Coasty takes a different approach. The agent observes the current screen, decides what action to take, executes it, and then observes the resulting state before continuing. It does not require DOM access, an accessibility tree, selectors, or an application-specific integration, so the same API can operate browsers, remote desktops, and older Windows applications.<p>A simplified request looks roughly like this:<p><pre><code>  run = coasty.runs.create(
      environment=&quot;vm_123&quot;,
      task=&quot;&quot;&quot;
      Open the patient record in the billing portal.
      Enter the attached authorization data.
      Do not submit if the member ID or procedure code does not match.
      Return the confirmation number.
      &quot;&quot;&quot;,
      files=[&quot;authorization.pdf&quot;],
      approval_required=[&quot;final_submission&quot;]
  )
</code></pre>
The response includes the final status, extracted outputs, a replay URL, and a timestamped event log:<p><pre><code>  {
    &quot;status&quot;: &quot;completed&quot;,
    &quot;output&quot;: {
      &quot;confirmation_number&quot;: &quot;PA-184392&quot;
    },
    &quot;replay_url&quot;: &quot;...&quot;,
    &quot;events&quot;: [
      {
        &quot;type&quot;: &quot;verification&quot;,
        &quot;field&quot;: &quot;member_id&quot;,
        &quot;result&quot;: &quot;matched&quot;
      }
    ]
  }
</code></pre>
The API can also pause a run for human approval, retry from a checkpoint, or return control to the developer when it encounters a condition the workflow did not anticipate.<p>We started working on this last summer, because we saw that models were getting better at vision but kept seeing a gap between computer-use demos and the reliability needed for production workflows. Getting an agent to complete a task once is fairly straightforward. Getting it to repeat that task, recover from unexpected states, avoid silently entering incorrect data, and produce evidence of what it did is much harder.<p>We built several layers around the underlying computer-use model. The system tracks the expected state of the workflow, detects when the application has diverged from that state, and can re-plan instead of continuing blindly. Developers can define invariants such as “the patient name must match the source document” or “never submit without approval,” and the agent checks those conditions during the run.<p>Each run happens in an isolated virtual machine. We expose APIs for provisioning environments, uploading files, starting tasks, streaming events, inserting human approvals, and retrieving the full replay and audit trail. Environments can be kept alive across runs when the application has a long login flow or persistent local state.<p>One problem we are still working through is the tradeoff between speed and reliability. The agent can move faster by taking fewer observations and verification steps, but that becomes risky in workflows involving patient records, payments, or regulatory filings. We currently bias toward slower execution with more checks and let developers configure approval points and verification policies.<p>We are initially working with healthcare operations teams because their workflows combine many of the hardest conditions: payer portals, EHRs, PDFs, spreadsheets, remote desktops, and actions where quiet mistakes are expensive. We also expose the same infrastructure through the developer API for teams building their own agents and vertical automation products.<p>We currently charge based on agent runtime and workflow volume, with separate pricing for dedicated environments and enterprise deployments.<p>We’d especially appreciate feedback from people who have built and&#x2F;or used browser agents, RPA systems, desktop automation, or agent infrastructure. We’re curious which parts of the API you would want direct control over, where you would prefer higher-level abstractions, and which failure modes have been hardest in your own automation systems.<p>If you&#x27;ve hit weird failure modes automating software like this, we want to hear about them. We&#x27;ll be here all day answering questions and taking notes!


--- Top Comments ---

[throw03172019]: How are you all different than the other few CUA APIs in this batch and previous batches?

</details>
