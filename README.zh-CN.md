# Plug & Chug

## 理解 AI Agent，搭建自己的工作系统

已经有 Codex、Claude Code、WorkBuddy 这些好用的应用，为什么还需要自己的本地 Agent 系统？

[English](README.md) | [中文](README.zh-CN.md) · [从这里开始](docs/start-here.zh-CN.md) · [完整手册](docs/handbook/index.md) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)

**这是一个教你搭建个人 AI 工作系统的仓库，没有编程基础也可以开始。** 使用你已经在用的 AI 软件，让它先了解你的工作，再解释选择、协助创建本地文件夹，一步步教你使用。

我们希望做到一件事：聊天结束后，你的资料、偏好、有效方法和未完成的工作还能留下来。以后即使换了模型，也能接着做，不必每次从零开始。

<a id="start-with-your-ai"></a>
## 把这段话交给你的 AI，就可以开始

打开你平时使用的 AI 软件，复制下面整段内容。Codex、Claude Code 等工具可以操作本地文件，具体能做哪些步骤取决于你使用的软件与权限。这条路线从对话开始，不要求你先安装 Skill 或打开终端。

<!-- STARTING_PROMPT:zh-CN -->
```text
我不懂编程。请按照这个仓库的教程，带我搭建自己的本地 Agent 系统：
https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide

先读新手指南，再了解我想让 AI 帮什么忙、正在用哪个 AI 软件、
用什么电脑。每次只问两三个问题。
推荐适合我的最简单配置，用通俗语言解释；你能实际完成的技术步骤，
请你来做。创建文件前，先让我看看准备使用的新文件夹和里面的内容，
等我确认。使用新目录，保留我已有的文件。
带我完成一个小任务、检查结果，再试试新开一个会话后能否继续。
最后给我一份简短说明：文件在哪里、下次打开什么、该怎么对你说。
如果你无法读取仓库或操作本地文件，请告诉我下一步需要做什么，
不要直接说已经搭建完成。
```
<!-- /STARTING_PROMPT -->

这就是 **Plug & Chug 的起点：复制一段话，让 AI 带着你搭建**。你来决定用途和存放位置，AI 协助处理技术步骤；用到哪一部分，再学会那一部分。

[一步步的新手指南](docs/start-here.zh-CN.md) · [保存起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文) · [AI 会问哪些问题](skills/portable-agentic-system/pas/references/intake-questions.md) · [完整引导流程](skills/portable-agentic-system/pas/references/facilitation-protocol.md)

## 你会学到什么，最后得到什么

第一个有用的成果，可以只是一个服务于学习、写作或日常工作的文件夹：AI 的职责清楚，里面有一份检查过的成果，也有让下一次对话接着做的说明。你能看懂、能修改，不需要一开始就记住所有技术名词。

| 走到哪一步 | 你和 AI 一起做什么 | 可以顺手读的说明 |
|---|---|---|
| 认识基本概念 | 分清模型、Agent、提示词、Skill 和文件分别负责什么 | [借公司图理解基础原理](docs/handbook/zh-CN/00-foundations.md) |
| 找到自己的用途 | 选一件经常做的事，说清楚什么结果对你有用 | [引导搭建](docs/start-here.zh-CN.md) |
| 给工作一个位置 | 整理指令、资料、草稿和检查后的成果 | [工作空间与文件分工](docs/handbook/zh-CN/02-workspace.md) |
| 完成一件小事 | 让 AI 做一次，再对照来源检查 | [第一次任务](docs/handbook/zh-CN/01-first-task.md) |
| 下次接着做 | 新开一个会话，找回进展和下一步 | [跨会话继续工作](docs/handbook/zh-CN/03-resume.md) |
| 越用越适合自己 | 保留有效方法，需要时增加职责，定期检查哪些安排有用 | [Skill](docs/handbook/zh-CN/04-skills.md) · [Agent 分工](docs/handbook/zh-CN/05-agents.md) · [维护](docs/handbook/zh-CN/08-maintenance.md) |

[完整手册](docs/handbook/index.md)按这条路线展开，提供中英文。喜欢从头连着读，可以打开[中文在线合订版](docs/agentic-systems-field-guide.zh-CN.md)或[英文在线合订版](docs/agentic-systems-field-guide.md)，也可以下载本页顶部的 PDF。

## 核心想法：模型可以更换，工作积累由你保留

借用公司的比喻：**你是所有者，模型是当前负责推理的员工，Agent 为这位员工安排具体职责**，配上指令、相关材料、工具和执行过程。**Harness** 则是完整的工作环境，包括文件、方法、访问安排、任务记录和检查机制。

![公司比喻：模型可以更换，工作安排和积累由你掌握](docs/assets/harness-concept-map.zh-CN.png)

[打开概念图 SVG 原图](docs/assets/harness-concept-map.zh-CN.svg)

**提示词（prompt）**告诉模型你想做什么。**Skill** 把可以反复使用的方法保存成 Markdown 文档，通常名为 `SKILL.md`；加载后，里面的文字成为模型上下文的一部分。你可以理解为把好用的操作手册“置顶”（pin），以后容易找到并复用。它不会训练新的模型权重，也不代表全文永久加载。**工具（tool）**负责执行读文件、保存等操作。文件存在于电脑上，只有内容被实际提供给模型时，才进入上下文。

现有 AI 软件提供能力；你的个人系统把这些能力组织成适合自己的工作方式：哪些资料重要，什么结果算好，什么方法可以重复用，下次怎样继续。本地文件让这些安排能查看、备份和恢复。模型仍可能通过云端服务运行，本地保存不等于离线，也不能单靠文件夹保证隐私。

## 可以从哪些事情开始？

| 你经常做的事 | 系统可以保留什么 | 值得重复使用的方法 |
|---|---|---|
| 学习 | 学习目标、练习结果、你能理解的解释 | 复盘错题，再安排下一次练习 |
| 研究 | 具名来源、笔记、待解决的问题和检查过的判断 | 比较证据，让缺失信息保持未知 |
| 写作 | 你选定的语气、素材、修改记录和认可的格式 | 从笔记写出草稿，再对照要求修改 |
| 求职 | 选中的职位、允许使用的申请材料和进度 | 对照职位与经历，准备申请草稿 |
| 日常事务 | 操作说明、清单和未完成事项 | 整理需要的材料，留下下一步 |

先让一个职责真正有用。另一类工作需要独立的资料、规则或负责人时，再考虑增加 Agent，不必为每个小任务都建一个部门。

个性化可以很具体：你希望用什么语言解释，详细到什么程度，结论需要哪些证据，最终文件长什么样。你选择保留的反馈，可以帮助以后的工作；反复有效的流程成为 Skill，稳定背景进入知识，今天的进度留在任务中。[个性化说明](docs/handbook/zh-CN/00-foundations.md#通过明确反馈让系统适合自己)会把这些区别讲清楚。

<a id="toolkit-features"></a>
## 按你想做的事，找到功能入口

这些功能已经在工具包里。你可以直接告诉 AI 自己想做哪件事，让它使用对应材料，不用先记住脚本和模式名称。部分技术参考目前以英文为主，可以请 AI 结合你的问题解释。

| 我想…… | 工具包提供什么 | 直接入口 |
|---|---|---|
| 搭建自己的第一个系统 | 分阶段了解需求，提出适合你的设计 | [起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文) · [问卷](skills/portable-agentic-system/pas/references/intake-questions.md) |
| 创建标准文件夹结构 | 生成器、初始配置和模板 | [搭建步骤](QUICKSTART.zh-CN.md#manual-standard-scaffold) · [生成器](skills/portable-agentic-system/scripts/create_agentic_system.py) · [配置示例](skills/portable-agentic-system/pas/examples/starter-config.json) |
| 检查已有系统 | 检查结构、文件容量、路由和状态 | [健康检查脚本](skills/portable-agentic-system/scripts/harness_health_check.py) · [系统复查](docs/reference/system-review-and-renewal.md) |
| 增加一个 Agent 或 Skill | 判断是否需要独立职责，写清什么时候使用 | [职责与路由检查](skills/portable-agentic-system/pas/references/description-routing-evals.md) · [Skill 模板](skills/portable-agentic-system/pas/templates/skill/SKILL.md) |
| 把好用的方法留下来 | 从重复流程和纠正中提炼可复用内容 | [方法提炼与 Skill 整理](docs/reference/knowledge-distillation-and-skill-fusion.md) |
| 让不同 Agent 互相借方法 | 共享流程，同时区分各自的资料归属 | [跨 Agent 方法共享](docs/reference/cross-agent-skill-borrowing.md) |
| 看进度，检查是否完成 | 任务记录、自动生成的状态、验证记录和完成关卡 | [任务与完成检查](docs/reference/task-lifecycle.md) · [状态生成器](skills/portable-agentic-system/scripts/generate_status.py) |
| 控制上下文与并发工作 | 记忆和文件容量限制、资源锁、独立工作目录指引 | [容量检查](skills/portable-agentic-system/scripts/check_budgets.py) · [锁与并发机制](skills/portable-agentic-system/pas/references/textbook-reliability.md) |
| 更换 AI 软件或模型服务 | 不同运行环境的接入说明和各自的验证记录 | [适配指南](docs/reference/compatibility.md) · [如何选择适配方式](skills/portable-agentic-system/pas/references/adapters.md) |
| 用一段时间后整理改进 | 清理过期规则、冗余记忆和重叠方法 | [系统复查与更新](docs/reference/system-review-and-renewal.md) |

[可安装的 Skill](skills/portable-agentic-system/SKILL.md)把这些流程组织在一起，包含 `pas-start`、`pas-audit`、`pas-adapt`、`pas-add-agent`、`pas-create-skill`、`pas-distill`、`pas-borrow`、`pas-review` 等模式。这些是向支持该 Skill 的助手提出的请求，不是让你输入终端的命令。

## 一个更完整的个人系统，可以怎样组织？

第二张图展示匿名化的系统实例：协调者把任务交给不同职责的 Agent，共享方法和各自的工作资料分别保存。等你的需求增长时，可以参考其中的分工，再调整成自己的样子。

![协调者、不同职责的 Agent、共享方法和经过检查的执行流程](docs/assets/anonymised-agent-system-map.zh-CN.png)

[打开系统实例 SVG 原图](docs/assets/anonymised-agent-system-map.zh-CN.svg) · [架构参考](docs/reference/architecture.md)

| 位置 | 放什么 |
|---|---|
| `AGENTS.md`、`RULES.md` | 当前项目的工作说明和边界 |
| `MEMORY.md` | 简短的恢复说明，以及下次需要找到的内容 |
| `knowledge/` | 值得再次查阅的稳定参考资料 |
| `skills/` | 可复用流程，以及何时使用它们 |
| `tasks/`、`workspace/` | 当前任务状态与进行中的工作 |
| `raw_data/` | 具名来源材料，在任务允许的范围内读取 |
| `outputs/` | 检查过的成果；保存到这里不会自动发送或发布 |
| `STATUS.md` | 根据任务记录生成的进度总览 |

[文件系统约定](skills/portable-agentic-system/pas/references/filesystem-contract.md)解释完整结构，包括文件清单、中间产物、日志和归档；[文件分工说明](docs/reference/file-roles.md)更简短。

<details>
<summary>展开查看标准生成器的目录结构</summary>

```text
My Agent Workspace/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── IDENTITY.md / RULES.md / SYSTEM_MAP.md
├── MEMORY.md / STATUS.md
├── routing-evals.json / runtime-compatibility.json
├── .codex/ / .claude/ / .gemini/     运行环境配置
├── .pas/bin/                       本地检查和完成关卡
├── tasks/ / workspace/             当前工作
├── knowledge/ / skills/             可复用资料与方法
├── raw_data/ / artifacts/ / logs/   具名输入和工作记录
├── outputs/ / archive/             检查后的成果和归档
└── example-Agent/                  有独立文件和工作空间的职责
```

这是完整的标准结构。引导对话可以先采用更小的教学工作空间；它不是生成器里某个未写明的“最小模式”。

</details>

## 也可以先拿现成案例练手

[第一个项目](examples/first-project/README.zh-CN.md)提供三份虚构场地笔记。你可以比较资料、检查来源、保存结果，再新开一个会话，通过交接记录接着做。它适合在使用自己的资料之前练习，不是搭建个人系统的必经步骤。

[开始练习](docs/start-here.zh-CN.md#practice-first) · [参考比较](examples/first-project/expected/comparison.zh-CN.md) · [参考交接](examples/first-project/expected/handoff.zh-CN.md)

<a id="technical-setup"></a>
## 可选：自己安装 Skill，或运行工具包

上面的引导对话是主要的新手入口。这里给想直接操作的人，以及正在协助你的 AI 使用。下面是 Bash/Zsh 示例；执行前，把示例路径换成自己选择的位置。

### 安装 Skill

取得本仓库的本地副本后，在希望使用 Skill 的项目目录中操作。Codex 兼容的项目级位置示例：

```bash
mkdir -p .agents/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  .agents/skills/portable-agentic-system
```

个人级位置可改用 `"$HOME/.agents/skills"`。实际发现和加载方式，请看对应说明：[Codex](skills/portable-agentic-system/pas/adapters/codex.md)、[Claude Code](skills/portable-agentic-system/pas/adapters/claude-code.md)、[Gemini CLI](skills/portable-agentic-system/pas/adapters/gemini-cli.md)。其他产品见[适配指南](docs/reference/compatibility.md)。安装 Skill 和生成工作空间是两个不同步骤。

### 预览、生成，再检查

从本仓库根目录操作，使用 Python 3.10 或更新版本。先选一个新的目标目录，查看预览：

```bash
PAS_SCRIPTS="skills/portable-agentic-system/scripts"
PAS_CONFIG="skills/portable-agentic-system/pas/examples/starter-config.json"
PAS_TARGET="../my-first-agent-workspace"
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG" --dry-run
```

检查目标路径和初始配置后，生成刚才预览的结构，再运行检查：

```bash
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG"
python3 "$PAS_SCRIPTS/validate_agentic_system.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_budgets.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_descriptions.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/generate_status.py" "$PAS_TARGET" --check
python3 "$PAS_SCRIPTS/harness_health_check.py" "$PAS_TARGET"
```

生成器使用 Python 标准库，默认拒绝覆盖已有文件。中途失败可能留下部分结果，请先查看再重试。[快速开始](QUICKSTART.zh-CN.md)包括获取仓库、预期结果和后续步骤；[故障排查](docs/reference/troubleshooting.md)解释常见问题。

## 手册与资料入口

- **学习：**[分章手册](docs/handbook/index.md) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)。
- **给 AI 阅读：**[中文 Playbook](skills/portable-agentic-system/pas/references/master-build-playbook.zh-CN.md) · [英文 Playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md) · [详细建设工作手册](skills/portable-agentic-system/pas/references/textbook-build-workbook.md)。
- **设计自己的系统：**[起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文) · [分阶段问卷](skills/portable-agentic-system/pas/references/intake-questions.md) · [完整引导流程](skills/portable-agentic-system/pas/references/facilitation-protocol.md)。
- **日常使用：**[文件系统约定](skills/portable-agentic-system/pas/references/filesystem-contract.md) · [任务、完成关卡、容量与资源锁](docs/reference/task-lifecycle.md) · [隐私与边界](docs/reference/privacy-and-boundaries.md)。
- **接入与检查：**[适配指南](docs/reference/compatibility.md) · [精确兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) · [验证流程](docs/reference/verification.md) · [验证记录](docs/verification/reader-journey-verification-2026-09-22.md)。
- **继续探索或贡献：**[文档索引](docs/README.md) · [贡献和构建说明](CONTRIBUTING.md) · [变更记录](CHANGELOG.md)。

## 验证到了哪里

[兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json)记录的核验日期是 2026-08-09：Codex、Claude Code 和 Gemini CLI 的生成式接入标为 `verified_static`，新会话检查为 `not_run`；其他适配文件各有自己的证据等级。本地检查通过，不能证明你安装的软件已经加载规则或执行完成关卡。[验证流程](docs/reference/verification.md)说明了怎样检查自己的环境。

修改工具包时，可运行 `python3 -m unittest discover -s tests -v`；文档构建检查见 [CONTRIBUTING.md](CONTRIBUTING.md)。代码与正文采用 [MIT License](LICENSE)，随附字体采用 [SIL OFL 1.1](THIRD_PARTY_NOTICES.md)。教学案例使用虚构、可以公开的数据。
