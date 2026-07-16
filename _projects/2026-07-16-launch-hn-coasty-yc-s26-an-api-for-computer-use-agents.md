---
layout: default
title: "Coasty：计算机使用代理API"
date: 2026-07-16T12:00:00+00:00
discovered_date: 2026-07-16
slug: 2026-07-16-launch-hn-coasty-yc-s26-an-api-for-computer-use-agents
source: hackernews
category: show-hn
ai_score: 8.0
summary: "Coasty是一个API，允许开发者创建计算机使用代理，以自然语言任务自动化遗留桌面和网页应用程序的工作流程。 该项目因其在高 trafic 上的7条 Hacker News 评论以及对处理遗留软件的开发者的明显效用而值得关注。它提供了一种无需API自动化工作流程的新方法，并通过SaaS或API服务具有潜在的盈利能力。 该API已获授权用于生产，处于Beta阶段，并需要与现有系统集成。它支持多个环境，并可以处理具有人工批准选项的复杂工作流程。"
tags: "AI, Agent, Automation, Desktop, Web"
---

# Coasty：计算机使用代理API


> Coasty是一个API，允许开发者创建计算机使用代理，以自然语言任务自动化遗留桌面和网页应用程序的工作流程。 该项目因其在高 trafic 上的7条 Hacker News 评论以及对处理遗留软件的开发者的明显效用而值得关注。它提供了一种无需API自动化工作流程的新方法，并通过SaaS或API服务具有潜在的盈利能力。 该API已获授权用于生产，处于Beta阶段，并需要与现有系统集成。它支持多个环


**项目链接**：https://coasty.ai/docs
**作者**：nkov47
**发布时间**：2026-07-15T15:51:20Z
**挖掘日期**：2026-07-16
**AI 评分**：8.0/10
**来源**：hackernews
**标签**：AI, Agent, Automation, Desktop, Web


## 📌 项目详解

Coasty是一个API，允许开发者创建计算机使用代理，以自然语言任务自动化遗留桌面和网页应用程序的工作流程。 该项目因其在高 trafic 上的7条 Hacker News 评论以及对处理遗留软件的开发者的明显效用而值得关注。它提供了一种无需API自动化工作流程的新方法，并通过SaaS或API服务具有潜在的盈利能力。 该API已获授权用于生产，处于Beta阶段，并需要与现有系统集成。它支持多个环境，并可以处理具有人工批准选项的复杂工作流程。


## 🌐 背景与生态

Coasty解决了缺乏API的遗留应用程序自动化挑战。与传统的RPA不同，它使用自然语言处理和计算机视觉来与用户界面交互，使其更能适应应用程序行为的变化。


## 💬 社区讨论

社区评论表明对它与其他CUA API差异化的怀疑，需要更清晰的功能和使用场景区分。


## 📚 参考链接

- [Computer Use Agents : When AI Navigates GUIs](https://learnllm.dev/learn/advanced/computer-use-agents)
- [Computer Use Agents - Stagehand](https://docs.stagehand.dev/examples/computer_use)
- [UI Automation Agents - Arun Baby](https://www.arunbaby.com/ai-agents/0023-ui-automation-agents/)

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
