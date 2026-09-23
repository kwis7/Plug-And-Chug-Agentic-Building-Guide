# Plug & Chug

## 理解 AI Agent，搭建自己的工作系统

已经有 Codex、Claude Code、WorkBuddy 这些好用的应用，为什么还需要自己的本地 Agent 系统？

[English](README.md) | [中文](README.zh-CN.md)

和 AI 做过的好工作，应该能在下次接着用。这个项目帮你把反复进行的研究、写作、学习或项目工作，整理成一个由自己掌握的工作空间。

先从一件经常做的事开始：资料放在哪里，哪些决定已经做过，成果检查到了哪一步，下次从哪里继续，都留下清楚的记录。等工作确实需要，再加入可复用流程、更多 Agent 和自动检查。

工具包提供模板和 Python 脚本；手册解释每一部分什么时候有用，以及换一个 AI 工具之后还要检查什么。

## 选一条入口

| 我想…… | 从这里开始 |
|---|---|
| 跟着 AI 完成一个小任务 | [从一个任务开始](docs/start-here.zh-CN.md)：现成资料、核对结果、再开会话继续 |
| 理解这套方法 | [阅读手册](docs/handbook/index.md)：中英文在线版与 PDF |
| 直接生成标准工作空间 | [使用工具包](QUICKSTART.zh-CN.md#manual-standard-scaffold)：完整本地命令与检查步骤 |

这是三种入口，不是必须依次完成的流程。试做学习案例不需要安装 Skill，也不需要运行生成器。

## 一个任务，两次会话

[第一个项目](examples/first-project/README.zh-CN.md)为一场 16 人、18:00 以后进行、需要无台阶入口的工作坊，比较三个虚构场地。

| 输入资料 | 核对后的结论 |
|---|---|
| Cedar Hall：容纳 18 人，18:00–21:00，有无台阶入口 | 符合已记录的需求 |
| Willow Room：容纳 24 人，09:00–17:00，有无台阶入口 | 开放时间不符 |
| Maple Studio：容纳 20 人，18:00–22:00，入口情况未说明 | 需要补充信息，不能猜测是否有无台阶入口 |

第一次会话保存比较结果和来源。第二次会话读取简短交接说明，找到 Maple 尚未确认的问题，起草询问但不发送。你可以查看[参考比较](examples/first-project/expected/comparison.zh-CN.md)和[参考交接](examples/first-project/expected/handoff.zh-CN.md)，也可以先自己做，再对照答案。

所有场地资料都是学习用的虚构数据；练习不搜索真实场地，也不预订。

## 工具、员工，以及你自己的工作方式

借用公司的比喻：你是所有者，**model（模型）**是当前负责推理的员工。**Agent** 为这位员工安排职责、相关指令、工作状态和可用工具，由运行软件把它们组织起来。**prompt（提示词）**交代当前怎么做，**Skill** 保存可以反复使用的方法。Markdown（`.md`）只是方便阅读和修改的文件格式，文件本身不会思考。

![公司比喻：模型可以更换，工作安排和积累由你掌握](docs/assets/harness-concept-map.zh-CN.png)

Codex、Claude Code 和 WorkBuddy 已经提供了不少 Agent 能力。你自己的系统可以利用这些现成能力：决定成果以哪份为准、哪些偏好长期适用、哪些方法值得复用，以及新会话怎样继续工作。把这些安排建立起来，并不要求再开发一个软件。

本地工作空间让这些安排可以查看、备份和恢复；个性化让它们逐渐体现你确认过的工作标准与有用的领域知识。模型仍可能通过云端服务运行，把文件放在本地不等于离线或默认私密。[基础原理一章](docs/handbook/zh-CN/00-foundations.md)会结合这张公司图和一次实际执行过程，把各部分的关系讲清楚。

## 包含什么，验证到了哪里

- 双语入门、虚构练习和完整手册：[中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)。
- 可独立使用的 [portable-agentic-system Skill](skills/portable-agentic-system/SKILL.md)、模板和标准结构生成器。
- 本地检查脚本，用于结构、任务记录、容量限制、路由描述和状态一致性。

生成器会为 Codex、Claude Code 和 Gemini CLI 创建原生入口及 Hook 配置。仓库的[兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json)记录的核验日期是 2026-08-09：这三项标为 `verified_static`，新会话检查为 `not_run`。其他工具分别属于文档说明、手动映射、待核验或仅模型服务等类别。接入前请读[兼容性参考](docs/reference/compatibility.md)（英文）。

本地检查通过，不代表你安装的运行环境已经加载指令、执行了 Hook，或完成了外部操作。Markdown 指令也不构成强制安全边界。[验证参考](docs/reference/verification.md)（英文）说明应保留哪些证据。

## 参与和复用

改进文档、案例或工具包，请先看 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。精确行为和更多资料见[文档索引](docs/README.md)与[技术参考](docs/reference/file-roles.md)（英文）。

代码与正文采用 [MIT License](LICENSE)，随附字体采用 [SIL OFL 1.1](THIRD_PARTY_NOTICES.md)。复用实质内容时，请保留版权及许可声明。案例使用虚构且可公开的数据；引入真实工作前，请先明确自己的隐私边界。
