<div align="center">

# ⛏️ AI掘金

<p><strong>每日挖掘 GitHub 与 Hacker News 上有实践意义的 AI 项目，中文深度档案</strong></p>

[![Live Site](https://img.shields.io/badge/网站-AI掘金-263238?style=for-the-badge&logo=homepage&logoColor=white)](https://lgjjennie-ship-it.github.io/ai-gold/)
[![Daily Update](https://img.shields.io/github/actions/workflow/status/lgjjennie-ship-it/ai-gold/daily-summary.yml?branch=main&label=每日更新&style=for-the-badge&logo=date-fns&logoColor=white)](https://lgjjennie-ship-it.github.io/ai-gold/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lgjjennie-ship-it/ai-gold/pulls)
[![Stars](https://img.shields.io/github/stars/lgjjennie-ship-it/ai-gold?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lgjjennie-ship-it/ai-gold/stargazers)

[📖 在线站点](https://lgjjennie-ship-it.github.io/ai-gold/) · [📡 RSS 订阅](https://lgjjennie-ship-it.github.io/ai-gold/feed.xml) · [📋 项目档案库](https://lgjjennie-ship-it.github.io/ai-gold/#-项目档案库)

</div>

---

## 这是什么

**AI掘金** 是一个每日自动更新的 AI 项目深度档案站。它从 GitHub Trending 和 Hacker News 挖掘热门 AI 项目，为每个项目生成 8 段中文深度分析，帮你在 3 分钟内判断"这项目能不能用、怎么用、能赚什么钱"。

- **每日午间更新**（北京时间 12:00，GitHub Actions 自动运行）
- **每个项目 8 段深度档案**：项目详解 / 背景生态 / 社区讨论 / 应用前景 / 技术栈 / 上手难度 / 目标用户 / 类似项目对比
- **中文优先**：所有档案页中文化，告别只看 star 数猜项目的时代
- **分类清晰**：GitHub 热门项目 + Show HN 新项目，按来源分组

---

## 为什么用 AI掘金

| 痛点 | AI掘金 怎么解决 |
|---|---|
| GitHub Trending 只看 star 数，不知道项目实际能干嘛 | 每个项目有「应用前景」段落，直接告诉你能解决什么问题、怎么变现 |
| 看到热门项目不知道难不难上手 | 「上手难度」段落写清前提条件、部署步骤、硬件要求 |
| 想找类似项目对比 | 「类似项目对比」段落列出竞品和差异化 |
| 英文 README 看得慢 | 全中文档案，核心信息 3 分钟读完 |

---

## 档案页内容结构

每个项目档案页包含以下 8 段深度分析 + 2 段参考内容：

| 段落 | 说明 |
|---|---|
| 📌 项目详解 | 项目的核心功能和定位 |
| 🌐 背景与生态 | 技术背景、行业趋势 |
| 💬 社区讨论 | 社区反馈和讨论焦点 |
| 🚀 应用前景 | 能解决什么问题、怎么变现 |
| 🔧 技术栈 | 核心技术、依赖、架构 |
| 🎯 上手难度 | 前提条件、部署步骤、硬件要求 |
| 👥 目标用户 | 适合谁用 |
| ⚖️ 类似项目对比 | 竞品对比、差异化 |
| 📚 参考链接 | 相关资料 |
| 📄 原文内容 | 原始 README（折叠） |

---

## 数据源

- **GitHub Search API**：8 个查询覆盖 AI/LLM/Agent/RAG/Tools 等方向，取近期热门
- **Hacker News**：Show HN 板块，min_score=30 过滤高质量项目
- **AI 模型**：GLM-4-Flash-250414，2 轮 AI pass 生成深度分析

---

## 技术栈

- **Python 3.12** + [uv](https://github.com/astral-sh/uv) 包管理
- **Jekyll** + GitHub Pages 部署
- **GitHub Actions** 每日定时运行
- **ZhipuAI GLM-4-Flash** 生成中文深度分析

---

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/lgjjennie-ship-it/ai-gold.git
cd ai-gold

# 安装依赖
uv sync

# 配置（复制 GitHub Actions 用的配置）
cp data/config.github.json data/config.json

# 设置 API Key
export ZHIPU_API_KEY=your_key_here
export GITHUB_TOKEN=your_github_token

# 运行（挖掘最近 48 小时的项目）
uv run horizon --hours 48
```

运行后会在 `docs/_projects/` 生成项目档案，`docs/_posts/` 生成每日日报。

---

## 项目结构

```
ai-gold/
├── .github/workflows/daily-summary.yml  # 每日定时任务
├── docs/
│   ├── _projects/        # 项目档案（每个项目一个 .md）
│   ├── _posts/           # 每日日报
│   ├── _config.yml       # Jekyll 配置
│   ├── index.md          # 首页
│   └── assets/           # 静态资源
├── src/
│   ├── ai/               # AI 摘要和深度分析
│   ├── storage/          # 存储管理
│   ├── services/         # 邮件、Webhook 服务
│   └── orchestrator.py   # 主流程编排
├── data/
│   └── config.github.json  # 数据源配置
└── pyproject.toml
```

---

## 致谢

本项目基于 [Horizon](https://github.com/Thysrael/Horizon) 二次开发，感谢原作者 [@Thysrael](https://github.com/Thysrael) 的开源贡献。

AI掘金 在 Horizon 基础上做了以下差异化：
- 聚焦 **AI 项目**（Horizon 是泛 AI 新闻）
- 全中文深度档案（Horizon 是中英双语摘要）
- 8 段结构化分析（应用前景/上手难度/类似项目对比等）
- 按分类分组展示

---

<div align="center">

**如果 AI掘金 帮到了你，欢迎给个 ⭐ Star，让更多人看到**

[![Star History](https://api.star-history.com/svg?repos=lgjjennie-ship-it/ai-gold&type=Date)](https://star-history.com/#lgjjennie-ship-it/ai-gold&Date)

</div>
