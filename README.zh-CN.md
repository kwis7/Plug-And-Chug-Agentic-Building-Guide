# 即插即用指南：搭一套真正属于你的 Agentic Empire

[English](README.md) | [中文](README.zh-CN.md) · [从这里开始](docs/start-here.zh-CN.md) · [完整手册](docs/handbook/index.md) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)

已经有 Codex、Claude Code、WorkBuddy 这些好用的应用，为什么还需要自己的本地 Agent 系统？

这些应用已经能帮我们查资料、写代码、修改文章，也有各自的项目和记忆功能。可是一项工作往往要做上几天、几周，甚至几年。助手要继续帮得上忙，就得知道你现在做到哪里、哪些材料可以使用、哪些判断已经确认，以及你为什么这样做。工作越深入，这些背景就越具体，单靠每次重新交代会越来越费力。

比如，你正在写一篇论文。这次对话里，AI 帮你比较了几篇文献，你纠正了它对一个概念的理解，又决定暂时放弃某个论证。下周继续时，只有一份改好的稿子还不够：放弃那个论证的理由是什么？哪条结论有原文支持，哪条还需要验证？如果这些只留在长长的聊天记录里，重新接手的人或助手仍要翻找、猜测。若把文献出处、关键判断、当前稿件和下一步放在同一个项目文件夹里，再告诉助手从哪里读起，就有了一份双方都能查看的工作底稿。

这里说的“自建文件系统”，可以从这样一个普通文件夹开始。你和助手一起约定：资料说明放在哪里，哪个稿件是当前版本，进度记在哪个文件，好用的方法怎样留下。下次开始工作，助手先读取相关内容；完成后，把新的结果和交接写回去。文件因此既保存成果，也参与下一次工作。一条要求过时了，你可以直接改；助手理解错了，也能回头检查它读了什么，找到需要纠正的地方。

同一类工作做过几次，你也会更清楚自己希望助手怎样配合：比较文献时先看什么，结论还不确定时怎么写，哪些修改要由你亲自决定。你确认要保留的要求和做法，可以写成以后还能用的说明。再遇到类似任务，把相关说明交给助手，就不必重讲一遍；回头看这些说明，也能判断哪些要求有用，哪些已经不适合。整理这些内容的过程，也是在想清楚自己怎样工作，以及哪些部分愿意交给 AI。

把这些内容保存在自己掌握的文件里，还有一个实际好处：你能查看、修改、备份，也能在更换应用时带走。现有应用的项目和记忆功能仍然可以使用；本地文件提供一份你能独立管理、按需交给不同助手的底稿。换工具后仍需设置读取方式并检查效果。这里的“本地”指文件的保存与管理，不要求模型也在本机运行；使用云端模型时，实际提供给它的内容仍可能发送到服务端，个人原件应由你掌握，只提供当前任务获准使用的必要内容。

如果你只是偶尔问一个问题，现有应用通常已经够用。当你开始长期研究、反复写作，或同时推进几个项目，一套简单的文件安排才更值得建立。可以先留下这次工作需要的内容，试着在新会话里继续；确实省下了重复解释和查找的力气，再逐步补充。

本指南最初是为计算社会科学学者而设计的，也适合学生、写作者和日常使用 AI 的人。研究者可能想接续文献笔记和当前思路，写作者则要保留语气要求、反馈与版本。书里会解释怎样组织这些内容，带你用现有助手试一次，再根据结果调整；不需要先补一门编程课。

哪些安排值得做，要看它有没有帮到你。如果为了使用 AI，反而每天忙着维护一堆说不清用途的文件，就该重新考虑。把有用的方法和知识保存在自己能看懂、能修改的地方，也是为了以后还有选择。

<a id="一张图理解模型怎样接上你的工作"></a>
## 模型、Agent 和工作环境各做什么

这张图用公司的分工帮助理解。你决定工作目标并掌握材料，模型负责当前的理解和推理，Agent 把这些能力用于一项职责。Harness 则是支撑执行的环境，包含指令、文件、工具、访问安排与检查。现有应用已经提供的能力，可以继续使用。

![公司比喻：模型可以更换，工作安排和积累由你掌握](docs/assets/harness-concept-map.zh-CN.png)

[打开概念图 SVG 原图](docs/assets/harness-concept-map.zh-CN.svg)

可以把 AI 工作台想成一块面积有限的**记事板**。你给它的 prompt、上传后实际读取的文件内容，以及工具返回的结果，都像不断写到板上的新内容。模型这一轮能依据什么来工作，就取决于板上现在有什么；这就是当前的**上下文（context）**。聊天记录里保存着的内容，不一定全部还在这块板上。

板面越来越满，就需要腾出位置。常见的做法是先把重要内容整理成一份摘要，再用摘要接替较长的旧内容，继续接收新的信息。这就是你经常看到的 **compacting（上下文压缩）**。比喻里的“擦掉”，指从当前上下文中移出内容，聊天记录本身可能仍然保留。摘要能帮助工作继续，却可能漏掉细节；重要依据还需要有地方存放，之后才能重新核对。

如果你还要继续写这篇论文，就可以在板旁准备一本**任务记事本**：记下写到了哪一节，哪些判断已经确认，哪个引文尚未核对，下次从哪里继续。本指南把当前对话和为接续这项任务保存的记录称为 **Agent 的短期记忆**。压缩上下文或新开会话后，要让助手实际读取这些记录，相关进度才会回到板上。任务结束后，这些记录可以归档。

值得长期保留的东西，则放进你掌握的**文件柜**：文献及其出处、整理过的领域知识、你确认要长期采用的写作要求，还有反复有效的方法。这些构成**长期文档记忆**，可以检查、修改和备份，也能用于以后的任务。每次工作只取出有关的几份材料，读到板上；柜里存着多少，与助手这次实际看到了多少，是两个不同的问题。这里的短期、长期按用途和保留时间区分，各应用的叫法和实现可能不同。

其中，项目指令和规则文件像**固定（pin）在板边的提醒**，也像给工作者看的 SOP：这个项目要做什么、遵循哪些要求、怎样检查结果。这些约定长期保存在文件里；实际工作时，还要确认应用是否从约定的指令入口加载，并在新会话或上下文压缩后继续提供这些提醒。其他知识文档可以留在柜里按需查阅；一个文件仅仅叫 `.md`，并不会自动成为每次工作都生效的指令。

**Skill 则像为某类任务准备的便利贴**。例如，比较文献时，你发现“先列出处，再区分原文结论与自己的推断，最后检查缺失信息”总是有用，就可以请助手把它整理成一个 Skill：写清什么时候用、怎么做、怎样检查结果，通常放在 `SKILL.md` 中，必要时附上示例、参考资料或脚本。下次遇到这类任务，支持 Skill 的应用就能按需取出这张便利贴，把方法放进当前上下文，指导这次工作。创建 Skill 是把方法写下来供以后使用，并不会训练模型权重，也不会自动增加工具权限；还要试一次，确认它能被找到并按预期使用。具体做法见[手册的 Skill 章节](docs/handbook/zh-CN/04-skills.md)，文件约定见 [Agent Skills 规范](https://agentskills.io/specification)。

板面还没写满，也可能已经很杂乱：旧稿、临时尝试和工具输出混在一起，模型可能漏掉要求或混淆判断。这类随上下文增多而出现的表现下降，常被称为 **[context rot（上下文衰减）](https://www.trychroma.com/research/context-rot)**，程度随模型和任务而异。项目提醒和临时取出的方法也会占用板面，先留这次任务用得上的内容。要是压缩之后总得重新交代背景，就可以回头检查：记事本有没有留下接续工作所需的线索，相关资料能不能再读回来。Anthropic 的[上下文工程说明](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)也讨论了这类安排。

保存这些内容时，先按用途选文件格式。笔记、规则和交接适合写成 `.md`（Markdown），它就是带有标题、列表和链接的纯文本，你可以直接读和改。JSON、YAML 适合按固定字段保存设置或记录，方便工具读取；脚本则用于实际执行计算、检查等步骤。论文 PDF、表格和图片仍可保留各自格式，另用笔记说明出处与用途。文件名和存放位置告诉人和工具去哪里找，能否生效还取决于是否被读取或执行。初学时先把说明写清楚，模板和脚本可以让助手按需要协助处理。

## 手册与实践

搭建时，不必把整本手册先读完。读一节，就和助手试着做相应的一小步；做到不明白的地方，再回书里找解释。比如，第一次比较做完了，你就要考虑草稿和确认过的结果怎么放；新开会话接不上进度，再看看交接怎样写、从哪里读起。

**[阅读中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf)** · **[Read the English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)** · [按章节阅读手册](docs/handbook/index.md)

| 你正在想什么 | 可以读哪一部分 |
|---|---|
| 模型、Agent、文件和工具怎样配合？ | [基础原理](docs/handbook/zh-CN/00-foundations.md) |
| 怎么先完成一件小事，并检查结果？ | [第一次任务](docs/handbook/zh-CN/01-first-task.md) |
| 资料、草稿与结果怎样放，才方便继续？ | [工作空间与文件分工](docs/handbook/zh-CN/02-workspace.md) |
| 新开一个会话，怎样找回下一步？ | [跨会话继续工作](docs/handbook/zh-CN/03-resume.md) |
| 有效方法、不同职责和旧安排怎样处理？ | [留下方法](docs/handbook/zh-CN/04-skills.md) · [Agent 分工](docs/handbook/zh-CN/05-agents.md) · [维护](docs/handbook/zh-CN/08-maintenance.md) |

喜欢连续阅读，可以打开[中文在线合订版](docs/agentic-systems-field-guide.zh-CN.md)或[英文在线合订版](docs/agentic-systems-field-guide.md)。PDF 收录核心手册和公司概念图。资料索引、偏好版本、模型验证记录等较细的做法，则放在后文链接的在线指南里。

想先试方法，可以[从虚构资料练习开始](docs/start-here.zh-CN.md#practice-first)。[三份场地笔记](examples/first-project/README.zh-CN.md)让你练习比较证据、处理未知信息和留下交接，不用提供个人资料。做完自己的草稿以后，再打开编写的[参考比较](examples/first-project/expected/comparison.zh-CN.md)和[参考交接](examples/first-project/expected/handoff.zh-CN.md)核对。

<a id="start-with-your-ai"></a>
## 把这段话交给你的 AI，就可以开始

选一件手头的小事，把下面这段话交给平时使用的 AI。先和它商量准备使用的新文件夹，确认后再创建；完成一份结果并核对，写下实际文件位置和下次怎么继续，最后开一个新会话试试。

助手也要先确认能不能读取仓库、有没有获准使用的本地文件工具。做不了的步骤，让它说明需要你怎样协助，不要把计划当成已经完成的搭建。

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

[一步步的新手指南](docs/start-here.zh-CN.md) · [保存起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文) · [AI 会问哪些问题](skills/portable-agentic-system/pas/references/intake-questions.md) · [完整引导流程](skills/portable-agentic-system/pas/references/facilitation-protocol.md)

想自己操作，也可以走[标准工具包的手动路线](QUICKSTART.zh-CN.md#manual-standard-scaffold)。引导搭建可以先采用较小的教学工作空间；标准生成器提供的完整结构，在后面的技术说明中。

## 用着用着，哪些安排值得留下？

资料一多，就容易记不清某项结论当时依据哪个版本。给资料记下出处，同时说明允许用于哪些任务；后来有了更新，也沿着这份记录补充。以后回看结论时，才有办法找到当时用过的依据。[本地资料工作空间](docs/reference/local-workspace.zh-CN.md)说明怎样用来源索引和任务记录，把这些线索留清楚。个人原件仍由你掌握，只向 AI 提供当前任务需要的最少字段或明确授权的脱敏衍生资料；详细做法见[隐私说明](docs/reference/privacy-and-boundaries.md)。

修改几次以后，你可能会发现有些要求希望一直沿用。比如，“以后的比较先给结论”说的是今后的比较任务；“这次短一点”则只交代了眼前这次回答。要把哪条要求留下、用于哪些工作，仍由你决定。[偏好记录与持续改进](docs/reference/personalization-and-evolution.zh-CN.md)说明这些要求怎样记录，以及以后怎样复查、修改或撤回。同一种修改反复出现，可以先列作待确认的要求，仍要经你授权才能保留。

有些内容又不是偏好：背景知识以后还会用，某套比较方法则值得重复执行。把背景留作知识，把方法写成需要时加载的 Skill，更新时就不容易混在一起。[个性化说明](docs/handbook/zh-CN/00-foundations.md#通过明确反馈让系统适合自己)用同一项任务解释这些区别。[虚构长期工作空间示例](examples/long-term-workspace/README.zh-CN.md)进一步展示怎样记录资料、偏好、一次性例外和下一步；它是记录方式的示范，实际加载和恢复仍需在你的环境里验证。

将来换工具时，这些底稿也有用。如果长期资料只能留在平台里，就像把书房安在别人商场里，入口和规则怎么变，难由你决定。保留自己的文件，至少能带走已有工作；新工具如何读取说明、调用工具、继续任务，再按[更换模型或应用](docs/reference/model-portability.zh-CN.md)中的做法核对，不假定同一份说明处处自动生效。

<a id="当工作变多再看职责怎样分开"></a>
## 什么时候分开职责

如果研究和写作使用不同资料、遵循不同要求，把它们分开可能更容易管理。若只是都要检查引用，借同一套方法就可以，不必每项小任务都建一个新角色。下面的匿名实例展示一种较完整的分工，读图时可以对照自己的需求，看哪些部分才用得上。

![协调者、不同职责的 Agent、共享方法和经过检查的执行流程](docs/assets/anonymised-agent-system-map.zh-CN.png)

[打开系统实例 SVG 原图](docs/assets/anonymised-agent-system-map.zh-CN.svg) · [架构参考](docs/reference/architecture.md)

图中的协调者负责把工作交给相应角色；各个角色有自己的资料和任务。研究 Agent 检查来源的方法，写作 Agent 也可以借用，但这不意味着它可以读取研究工作里的所有材料。`pas-borrow` 和 `pas-distill` 是支持该 Skill 的助手可使用的模式，分别用于借方法和提炼反复有用的部分。

<a id="toolkit-features"></a>
## 按你想做的事，找到功能入口

下面按用途列出了工具包入口。用到某项功能时，再请助手查看对应材料；部分技术参考是英文，也可以让它结合当前任务解释。

<details>
<summary>展开查看功能与对应入口</summary>

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

</details>

## 工作文件与目录，按需要再查

<details>
<summary>展开查看文件分工</summary>

| 位置 | 放什么 |
|---|---|
| `AGENTS.md`、`RULES.md` | 当前项目的工作说明和边界 |
| `MEMORY.md` | 简短的恢复说明，以及下次需要找到的内容 |
| `knowledge/` | 值得再次查阅的稳定参考资料 |
| `skills/` | 可复用流程，以及何时使用它们 |
| `tasks/`、`workspace/` | 当前任务状态与进行中的工作 |
| `raw_data/` | 公开或合成输入，以及当前任务批准、可供 Agent 读取的脱敏衍生资料；个人原件不在 Agent 读取范围内 |
| `outputs/` | 检查过的成果；保存到这里不会自动发送或发布 |
| `STATUS.md` | 根据任务记录生成的进度总览 |

[文件系统约定](skills/portable-agentic-system/pas/references/filesystem-contract.md)解释完整结构，包括文件清单、中间产物、日志和归档；[文件分工说明](docs/reference/file-roles.md)更简短。

查看文件时，先看它在当前任务里起什么作用。提示词交代请求，Skill 提供可复用的方法，读写文件则由工具完成。文件已经保存，并不能说明模型已经读到它；Skill 安装好了，也还要确认它有没有在实际任务中加载。

</details>

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

<a id="technical-setup"></a>
## 可选：自己安装 Skill，或运行工具包

希望助手带着做，可以从上面的引导对话开始，让它处理工具和权限允许的本地步骤。想自己运行命令时，再展开这里的安装与生成说明。

<details>
<summary>展开安装与生成步骤</summary>

下面是 Bash/Zsh 示例；执行前，把示例路径换成自己选择的位置。

### 安装 Skill

先取得仓库的本地副本，再进入希望使用 Skill 的项目目录。下面以 Codex 兼容的项目级位置为例：

```bash
mkdir -p .agents/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system \
  .agents/skills/portable-agentic-system
```

如果放在个人级位置，目标目录可改为 `"$HOME/.agents/skills"`。各工具怎样发现和加载，请看对应说明：[Codex](skills/portable-agentic-system/pas/adapters/codex.md)、[Claude Code](skills/portable-agentic-system/pas/adapters/claude-code.md)、[Gemini CLI](skills/portable-agentic-system/pas/adapters/gemini-cli.md)。其他产品见[适配指南](docs/reference/compatibility.md)。这一步安装的是 Skill；工作空间还要另行生成。

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

生成器使用 Python 标准库，默认不覆盖已有文件。如果中途失败，目标目录里可能已经留下部分结果，先查看这些内容，再决定怎样重试。[快速开始](QUICKSTART.zh-CN.md)包括获取仓库、预期结果和后续步骤；[故障排查](docs/reference/troubleshooting.md)解释常见问题。

</details>

## 手册与资料入口

- **学习：**[分章手册](docs/handbook/index.md) · [中文 PDF](docs/downloads/Agentic-System-Building-Guide.zh-CN.pdf) · [English PDF](docs/downloads/Agentic-System-Building-Guide.pdf)。
- **给 AI 阅读：**[中文 Playbook](skills/portable-agentic-system/pas/references/master-build-playbook.zh-CN.md) · [英文 Playbook](skills/portable-agentic-system/pas/references/master-build-playbook.md) · [详细建设工作手册](skills/portable-agentic-system/pas/references/textbook-build-workbook.md)。
- **设计自己的系统：**[起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文) · [分阶段问卷](skills/portable-agentic-system/pas/references/intake-questions.md) · [完整引导流程](skills/portable-agentic-system/pas/references/facilitation-protocol.md)。
- **日常使用：**[文件系统约定](skills/portable-agentic-system/pas/references/filesystem-contract.md) · [任务、完成关卡、容量与资源锁](docs/reference/task-lifecycle.md) · [隐私与边界](docs/reference/privacy-and-boundaries.md)。
- **接入与检查：**[适配指南](docs/reference/compatibility.md) · [精确兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) · [验证流程](docs/reference/verification.md) · [验证记录](docs/verification/reader-journey-verification-2026-09-22.md)。
- **继续探索或贡献：**[文档索引](docs/README.md) · [贡献和构建说明](CONTRIBUTING.md) · [变更记录](CHANGELOG.md)。

## 验证到了哪里

[兼容性清单](skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json)的核验日期是 2026-08-09。其中，由生成器提供的 Codex、Claude Code 和 Gemini CLI 接入标为 `verified_static`，新会话检查为 `not_run`；其他适配文件各自记录证据等级。也就是说，本地配置检查通过以后，还得观察所用软件有没有加载规则、执行完成关卡。[验证流程](docs/reference/verification.md)说明了怎样检查自己的环境。

修改工具包时，可运行 `python3 -m unittest discover -s tests -v`；文档构建检查见 [CONTRIBUTING.md](CONTRIBUTING.md)。代码与正文采用 [MIT License](LICENSE)，随附字体采用 [SIL OFL 1.1](THIRD_PARTY_NOTICES.md)。教学案例使用虚构、可以公开的数据。
