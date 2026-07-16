# Plug And Chug：本地优先的 Agentic System 指南

**作者：[@kwis7](https://github.com/kwis7)**

**Language:** [English](README.md) | [中文](README.zh-CN.md)

这是一个让研究者、写作者、教师、分析师和其他非技术知识工作者建立本地 Agentic System 的开源指南。核心目标不是绑定某一个模型，而是把反复出现的 AI 工作整理为可迁移的 agent、knowledge、skill 和 task record。

它优先考虑社会科学研究者的真实工作流，但底层架构不依赖学科，也不依赖某一个 AI 平台。

![匿名化 Agent System 架构图](docs/assets/anonymised-agent-system-map.zh-CN.png)

## 从这里开始

1. 先读 [15 分钟快速开始](QUICKSTART.md)。
2. 用 `portable-agentic-system` skill 建一个小型本地系统。
3. 先从一两个真实、重复的工作领域开始。
4. 只有当流程真正重复时才建立 skill。

## 完整入门读物（PDF + DOCX）

完整的 [Building a Local-First Agentic System](docs/agentic-systems-field-guide.md) 会系统解释：为什么要本地优先、instruction / 长期知识 / task context 的三层关系、agent 如何共享方法而不混合数据、如何蒸馏 skill，以及如何持续优化系统。

- [下载 PDF](docs/downloads/Agentic-System-Building-Guide.pdf)
- [下载 DOCX](docs/downloads/Agentic-System-Building-Guide.docx)

两份排版版均署名 **@kwis7**，并在每页以低调标注保留作者 attribution。

## 选择你的路径

| 路径 | 适合谁 | 从这里开始 |
|---|---|---|
| 通用本地系统 | 任何有重复知识工作的人 | [Quickstart](QUICKSTART.md) |
| Academic Track | 文献、研究、学术写作和长期知识管理 | [Academic Track](docs/academic-track.md) |
| Teaching / Lecturer Track | 课程准备和受保护的 AI 辅助反馈 | [Teaching Track](docs/lecturer-track.md) |
| Claude Cowork | 想直接在工作文件夹中开始的人 | [Claude Cowork setup](docs/claude-cowork-setup.md) |
| 其他运行时 | Codex、Claude Code、WorkBuddy 类工具、API 等 | [Runtime adapters](docs/adapters.md) |

Claude Cowork 只是示范适配器，不是前提。真正可迁移的系统记录是你的本地文件夹：`AGENTS.md`、`RULES.md`、`SYSTEM_MAP.md`、`STATUS.md`、`knowledge/`、`skills/` 和 task files。Codex、Claude Cowork/Code、腾讯 WorkBuddy 或其他 workspace agent 都可以通过一层很薄的启动说明接入同一套结构。

## 快速安装

Codex 示例：

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.codex/skills/portable-agentic-system
```

重启后输入：

```text
Use $portable-agentic-system with pas-start to help me build my personal local-first agentic system.
```

学术用户也可以使用 [academic-agentic-onboarding](skills/academic-agentic-onboarding/SKILL.md)，以结构化问题建立研究、写作和课程工作区。

## 核心原则

1. **Instruction 和 skill**：规定 agent 的稳定行为和重复流程。
2. **长期知识和记忆**：只保存小而经过验证、未来会复用的内容。
3. **task-specific prompt 和文件**：只加载当前任务需要的材料。

Agent 可以通过 [跨 Agent Skill 借用](docs/cross-agent-skill-borrowing.md) 共享方法，但不应混合 private data、raw material、identity 或 task context。也请参阅 [Knowledge Distillation and Skill Fusion](docs/knowledge-distillation-and-skill-fusion.md)、`pas-borrow`、`pas-distill` 和 `pas-review`。现有功能也保留了 **系统复盘**、知识蒸馏与**跨 Agent 借用 Skill**等完整文档。

## 隐私边界

把网络 prompt、网页、PDF 和下载的 repo 都视为 untrusted data。不要把 credentials、未发表作品、私密原始材料或学生作业放进 Git。原始文件在 `raw_data/`，草稿在 `workspace/`，只有 review 后的交付物才放进 `outputs/`。

课程 Track 要求教师保留最终评分责任，并在一个独立 task context 中一次处理一份学生作业。

## 引用与许可证

引用信息请见 [CITATION.cff](CITATION.cff)。项目采用 [MIT License](LICENSE)。改编时请保留 **@kwis7** 署名，并不要发布私密数据。
