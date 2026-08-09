# 即插即用指南：搭一套真正属于你的 Agentic System

[English](README.md) | [中文](README.zh-CN.md)

一份经过匿名化、local-first 的指南和实用工具，帮助你搭建真正符合自己工作方式的 AI Agent 系统。

## 愿景

这个项目帮助人们建立一套住在普通本地文件夹里的个人 AI Agent 系统。它应该让主人看得懂，也应该能在不同模型和工具之间迁移。目标不是把 AI 弄得更复杂，而是给反复出现的工作一个稳定的家：规则清楚、上下文有层次、方法可以复用、任务状态看得见，完成也有证据。

系统应该越用越顺手，而不是把每段聊天都塞进永久 memory。模型、API 和界面都可以换，但你的工作不必每次从零开始。

## 适合谁

- 研究者、学生、写作者、分析师、开发者和其他知识工作者；
- 想先把 AI 工作整理清楚、但不打算先补一门软件工程课的非技术用户；
- 在生活或工作多个领域使用 AI，经常在不同会话之间丢失上下文的人；
- 希望拥有可复用流程、明确隐私边界，也不想被单一模型或界面锁住的人。

你不需要计算机科学学位。只要你确实想让 AI 帮忙，也愿意给这份帮助一个清楚的落脚点，就可以开始。

## 适合你，如果

- 你会在几个固定领域反复找 AI 帮忙；
- 每次打开新聊天都要重新解释相同背景；
- 你希望把有用的 prompt 和习惯变成可复用 skill；
- 你需要把私密原始资料、草稿和已审核成品分开放；
- 你希望不同 Agent 可以互相借方法，但不要混用私密数据；
- 你想清楚看到任务是 active、blocked、verified 还是 completed；
- 你希望切换模型或 runtime 时，不必重建整个工作空间。

如果只是问一个临时问题，普通聊天通常已经够用。这个 package 更适合会反复出现、不断增长、有风险边界，或者需要在聊天结束后继续的工作。

## 它解决的问题

AI 用久以后，工作很容易散开：一个聊天里有不错的草稿，另一个聊天里有资料链接，第三个聊天里藏着上周做出的决定。文件越积越多，临时名字过几天就认不出来。模型本身可能很强，但模型周围的工作现场越来越难恢复。

真正麻烦的往往不是模型不够聪明，而是连续性：模型现在能看见什么，哪个文件才是权威来源，什么还没完成，哪些内容能分享，以及下一次会话如何接着做，而不是依赖用户或模型自己记得“顺手更新”。

本地 Agent Harness 给这些工作一个落脚点。聊天可以结束，主动运行的模型可以替换，但规则、任务状态、知识、流程、证据和已审核输出仍然留在你自己的工作空间里。

## 为什么不直接和最强模型聊天？

更强的模型可以给出更好的答案，但它不会自动保存项目规则、来源链、任务状态、隐私边界和验证习惯。这些东西才决定一项长期工作能不能可靠地继续。

对开发者来说，长期价值不只是一次修好 bug，还包括项目指令、常用命令、测试和未解决边角问题。对写作者来说，是语气、素材、修改历史和获批格式。对老师来说，是课程背景和学生上次卡住的地方。对研究者来说，是从来源、笔记到方法、判断和草稿的整条链路。

普通聊天很适合临时问题。Harness 服务的是会回来、会积累、需要继续的工作。

## 这里所说的 Harness 是什么

模型是正在工作的那个模块，但模型不等于整个 Agent 系统。**Harness 是围绕执行配置好的全部架构**：runtime 入口、identity、rules、权限、Agent 所有权、skills、tools、connectors、任务、生成式状态、memory、knowledge、原始材料、workspace、artifacts、logs、outputs、hooks、gates、budgets、locks、worktrees、validators 和 adapters。

更换模型就像更换员工。公司的使命、规章、档案、部门手册、工单、工具、办公桌和质检流程仍然保留。单 Agent 中，模型就是员工；只有多 Agent 矩阵里负责协调的中控模型才叫经理。

![完整 Harness 边界中显眼的主动运行、可替换模型](docs/assets/harness-concept-map.zh-CN.png)

这个区别很重要：模型提供主动推理，Harness 提供连续性、结构、访问、流程和控制。一个装满 Markdown 的文件夹不会自动变成有强制力的系统，所以在需要确定性行为的地方，这套工具也提供 scripts、manifests、hooks、validators 和明确的 evidence labels。

## 信息应该放在哪里

- `MEMORY.md`：精简的交接班和恢复索引。
- `knowledge/`：长期档案馆、参考资料库和机构知识。
- `task.yaml` 与 `workspace/`：当前任务状态和实际执行桌面。
- `raw_data/`：具名原始材料，默认禁止递归全读。
- `outputs/`：经过审核的交付物，但不自动代表可以发送或发布。
- `STATUS.md`：由 task manifests 生成，当前状态不依赖模型记得更新第二份真相。
- `skills/`：存放可复用流程；每次都应该生效的行为应放进入口文件或规则。
- receipts、gates、budgets 和 locks：在单靠文字不够时，明确验证证据和并发资源所有权。

Memory 和 Knowledge 都可以长期保存，但工作不同。Memory 回答“下一次会话恢复时必须知道什么”；Knowledge 回答“哪些稳定材料值得系统反复使用”。当前执行状态属于任务桌面，不属于任何一个档案库。

## 为什么要个性化

- Agent 地图可以贴合你真正反复做的事情，而不是照抄别人的模板。
- Rules 可以反映你的隐私需求、风险偏好、语言习惯和审批边界。
- Skills 可以保存你确实会重复执行的流程。
- Outputs 可以对齐你真正会提交、发布、学习或归档的格式。
- Stable references 进入 knowledge，大型原件留在自动上下文之外，memory 才能保持精简。
- Verification 可以根据任务后果调整，不把每个生成答案都直接当成完成。

个性化不是装饰。它让系统减少重复 prompt，同时不强迫你的生活去适应某个工具的默认工作流。

## 匿名化系统实例

下面这张图展示一种可能的多 Agent 拓扑。它来自真实系统的结构抽象，但姓名、私人项目、路径、凭据和敏感领域都已经换成中性示例。中控中心把任务路由给不同功能 owner；方法可以共享，私有上下文仍留在自己的 owner 目录；任务经过明确的执行和验证流程。

![中控中心、四个功能 owner Agent、共享方法、私有上下文边界和验证执行流](docs/assets/anonymised-agent-system-map.zh-CN.png)

第一张图解释一个主动模型周围包含什么；第二张图说明这些 Harness 组件如何组成更大的系统。它是供你修改的例子，不是要求照抄的组织架构。

## 从小系统开始

两三个职责清楚的 Agent，通常比十个模糊 Agent 更有用。

| 示例 Agent | 负责什么 | 适合先做的 Skill |
|---|---|---|
| Research Assistant | 论文、笔记、引用和分析 | 来源核验 |
| Job Search Agent | 职位、简历和申请追踪 | 职位录入 |
| Life Admin Agent | 表格、家庭事务和跟进 | 文件 checklist |
| Learning Agent | 课程、练习和复盘记录 | 模考复盘 |

长期反复出现、需要独立 owner 和上下文的工作，适合建 **Agent**；现有 Agent 内反复执行的流程，适合建 **Skill**；稳定可复用材料进入 **Knowledge**；一次性工作留在当前 task workspace。

## 安装 Skill

Codex 项目级安装：

```bash
mkdir -p .agents/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  .agents/skills/portable-agentic-system
```

Codex 个人级安装：

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  "$HOME/.agents/skills/portable-agentic-system"
```

Claude Code 使用 `.claude/skills/`；Gemini CLI 使用 `.gemini/skills/` 或 `.agents/skills/`。安装前请先阅读相应 adapter，因为不同 runtime 的发现、加载和强制机制并不相同。

## 生成起步系统

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "/path/to/My Agent Harness" \
  --config skills/portable-agentic-system/pas/examples/starter-config.json

python3 skills/portable-agentic-system/scripts/validate_agentic_system.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/check_budgets.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/generate_status.py "/path/to/My Agent Harness" --check
python3 skills/portable-agentic-system/scripts/harness_health_check.py "/path/to/My Agent Harness"
```

generator 默认拒绝覆盖已有文件。只有在检查精确目标后才应使用 `--force`。

## 在不同 AI 工具之间使用

同一套本地结构可以服务不同模型和产品，但“可迁移”不等于假装每个产品用同一种方式加载指令。Codex、Claude Code、Gemini CLI、hosted workspace、provider API、模型 switchboard 和自建应用，在发现入口、权限、hooks 和持久化方面都不一样。

所以，这个仓库保持共同的 Harness 思路，同时分别记录每个 runtime 的真实入口和证据等级。接入具体工具时先看 [adapter 指南](docs/adapters.md)；需要精确判断支持范围时再看 [兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json)。“写了一份 adapter 文档”不等于“已经通过 runtime 实测”。

## 这套工具可以帮你做什么

- 通过分阶段问卷了解用户，再围绕真实重复工作设计一个小型 Agent 地图；
- 生成 control center 和 domain Agent 文件夹，默认不覆盖现有系统；
- 分清 identity、rules、memory、knowledge、当前工作、原始材料和 outputs；
- 把重复流程写成 progressive disclosure 的 Skills；
- 用清楚的 description 路由任务，并测试正向、负向和碰撞场景；
- 从 task contracts 生成状态，在 closeout 前要求验证证据；
- 管理 memory 和大文件的上下文预算；
- 用 resource claims、locks 和 worktree 指南协调并发工作；
- 检查结构、隐私边界、引用、manifests 和完成 receipts；
- 在真实使用后复盘系统，把反复纠正蒸馏成稳定改进。

## 主要文件

- [Quick Start](QUICKSTART.md)
- [可单独投喂的完整建设 Playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md)
- [给朋友的简单 Prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md)
- [分阶段问卷](skills/portable-agentic-system/pas/references/intake-questions.md)
- [Filesystem Contract](skills/portable-agentic-system/pas/references/filesystem-contract.md)
- [Task、Gate、Budget 和 Lock](docs/governance.md)
- [Runtime/Provider Adapters](docs/adapters.md)
- [长篇指南](docs/agentic-systems-field-guide.md)
- [Harness 概念图](docs/assets/harness-concept-map.zh-CN.svg)
- [匿名化系统实例图](docs/assets/anonymised-agent-system-map.zh-CN.svg)
- [DOCX 下载](docs/downloads/Agentic-System-Building-Guide.docx)
- [PDF 下载](docs/downloads/Agentic-System-Building-Guide.pdf)

## 验证声明

```bash
python3 -m unittest discover -s tests -v
python3 /path/to/skill-creator/scripts/quick_validate.py skills/portable-agentic-system
git diff --check
```

health score 明确只是 static evidence。它不能证明 runtime 已加载入口、hook 阻止了假完成、provider 已响应、文件已送达或系统已部署。

公共版本只使用匿名化的一级、二级目录模式，不包含个人路径、凭据、账户资料、客户/学生信息、原始私有数据、日志或具体报告内容。
