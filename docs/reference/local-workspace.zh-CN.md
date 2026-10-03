# 围绕现有助手，管理自己的本地工作资料

[English](local-workspace.md) · [从这里开始](../start-here.zh-CN.md) · [长期案例](../../examples/long-term-workspace/README.zh-CN.md)

现有通用助手已经能推理、读取允许的文件、调用工具，并帮助你完成工作。先把自己的资料安排成容易查找、下次能继续的工作空间。为了保留有用的本地系统，不必先造一个自定义 runtime。

由你掌握工作文件：简短入口、当前任务指针、具名输入、核对后的成果和交接。确实有值得保留的内容时，再加知识索引或已确认偏好。原生 Hook、多模型和并行 worker 都可以以后按需加入。

## 从一项任务、三个小文件开始

选一个新工作目录、一项经常性工作和少量非敏感输入。创建前看清准确位置，保留已有文件。可以这样开始：

> 用这个新目录处理我的来源比较工作。我会提供需要的字段或脱敏笔记。保存本地草稿，按具名输入核对，在 workspace/current.md 留下下一步。如果无法访问文件，先说明限制，不要直接声称已保存。

先创建这项任务真正需要的文件：

```text
My Local Workspace/
├── AGENTS.md                    当前 runtime 的简短入口
├── workspace/current.md        任务指针和下一步允许动作
└── tasks/T-venue.md             目标、具名输入、成果、检查与交接
```

这里用 `AGENTS.md` 示范。实际入口位置取决于 runtime；Claude Code adapter 说明了 `CLAUDE.md` bridge。其余多数文件名是工作空间约定。只有在新会话中实际检查过加载，才声称 runtime 使用了这些指令。

已在约定范围内的日常工作，可以直接让助手读取具名许可输入、保存本地草稿。新增数据源、改变目标目录或访问边界、导出资料、提出删除时，才需要新的决定。无需每写一句话或读一次文件，都另开许可对话。

## 有内容需要保存时，再增加位置

这是学习工作区，不是必须生成的标准 scaffold。可以逐步扩展：

```text
My Local Workspace/
├── AGENTS.md
├── workspace/current.md
├── tasks/T-venue.md
├── knowledge/
│   ├── index.md                 可复用方法、注明日期的参考
│   └── source-comparison.md
├── preferences/
│   ├── index.md                 已确认偏好的 ID 与版本
│   └── venue-source-comparison-opening.v1.json
├── raw_data/redacted/
│   ├── index.json               仅列许可衍生输入的 source ID
│   └── S-venue-summary.v1.json
├── artifacts/                  计算、中间文件、验证记录
└── outputs/                    owner 重新打开并核对后的成果

用户控制的原件档案库
    单独的访问边界；原件位置不进入这里的索引
```

不要为了把目录画全，就创建空部门。原件档案库归用户掌握，不属于 Agent 的许可输入。不同文件夹本身不会产生访问边界：应配置当前 runtime 的访问限制或 sandbox，必要时配合 filesystem permissions。如果没有这些控制，就不要把原件库提供给 runtime，改为提供许可衍生输入。

| 位置 | 保存什么 | 何时加载 |
|---|---|---|
| 入口 | 职责、来源边界、当前工作的位置 | 按 runtime 支持的方式加载 |
| `workspace/current.md` | 当前任务 ID/路径、成果位置、缺口、下一步 | 开始或恢复该工作时 |
| Task card | 目标、具名来源、范围、偏好/例外、检查与交接 | 处理该任务时 |
| 知识与索引 | 可复用方法，或有日期和出处的参考 | 与当前问题相关时 |
| 偏好与索引 | 明确确认的行为、范围与版本 | 匹配适用任务时 |
| 脱敏输入与索引 | 最小许可衍生资料及来源记录 | 任务指明该 source ID 时 |
| Artifacts | 可复现计算、实际检查依据 | 核对或恢复需要时 |
| Outputs | 已审阅的本地成果 | 指定审阅或复用时 |

一份小的 `current.md` 可以这样写：

```text
当前任务：tasks/T-venue.md
成果：outputs/venue-comparison.md
偏好：venue-source-comparison-opening，版本 1，仅适用于 source-comparison
未知：Maple 无台阶入口，以及全部指定日期的预订信息
下一步：在 workspace/maple-question.md 起草一条未发送的问题
下次读取：任务卡、核对后的成果、三份具名虚构笔记
```

完整推理和来源不要塞进指针。[长期案例](../../examples/long-term-workspace/README.zh-CN.md)提供可复制的任务、成果与交接内容。

## 个人原件继续由你掌握

不要让助手直接打开或修改个人信息源文件的原件。使用三类输入之一：你为本任务提供的最少字段，明确标为 agent-readable 的脱敏副本，或只输出必要字段的受控中介结果。没有合适输入时，先取得需要的字段；不依赖它们的工作仍可继续。

例如场地比较需要容量、开放时间、入口信息，不需要身份、联系记录、账户资料或档案库的完整路径。文档管理也可以从安全的 source ID、类型和日期开始，不必展示文档原文。

标准 scaffold 使用 `raw_data/`，不代表可以读取个人原件。该目录仅用于允许的公开/虚构输入或许可衍生资料。敏感原件保留在用户的独立档案库。索引用于查找，不会自动授予底层资料的读取权限。

需要保留的衍生资料，至少附上这些字段：

```json
{
  "source_id": "S-venue-summary",
  "version": 1,
  "derivative_ref": "raw_data/redacted/S-venue-summary.v1.json",
  "derived_at": "2026-10-02",
  "provenance": "Authored synthetic fields for one comparison",
  "agent_readable": true,
  "authorised_scope": ["T-venue: compare capacity, hours, and entry access"],
  "permitted_runtime_provider": "unknown; select an owner-approved destination before loading personal derivatives",
  "freshness_review_on": "2026-11-02",
  "retention_state": "retained-for-authorised-task",
  "retention": "Until task closure; user decides any later reuse or removal",
  "revocation_state": "not_revoked",
  "revocation": "Stop future loading when the user withdraws this scope",
  "verification_label": "illustrative; no runtime or current-source verification"
}
```

这是编写的示例，不是某个用户实际提供或批准数据的证据。review date 是建议检查点，不是已经完成的检查，也没有启用定时任务。自己的工作区应填写真实日期、实际范围与许可目的端。`unknown` 不代表可以把个人衍生资料交给任何 runtime 或 provider。只索引选定使用的具名衍生输入，不给整个个人档案建索引。用中性的 source ID；姓名、可识别摘要、敏感原件路径、凭据和档案库清单，不进入共享索引、Git 或给模型看的日志。

资料导入、保留、导出和删除由用户决定。撤回范围后，停止后续加载，标明该衍生输入不可用于新任务。复用相关草稿或成果前先复核，让用户决定保留或移除。移动文件或修改索引，不会自动清除 native memory、现有对话、工具缓存或服务商保留的副本。实际 retention 与 deletion controls 要单独核对；不能承诺立即遗忘，也不能把改了索引说成已抹去历史传输内容。

## 指令与实际访问控制一起使用

| 控制 | 能做什么 | 不能证明什么 |
|---|---|---|
| 入口或任务说明 | 告诉助手允许的流程 | 文件系统实际拒绝访问 |
| Runtime sandbox 或 filesystem ACL | 正确配置时限制访问 | 推理正确，或每条工具路径都能安全导出 |
| 单独的 worker 角色 | 约束分派任务和返回内容 | 与继承上下文、共享工具隔离 |
| Git worktree | 分开仓库修改 | 私密数据边界 |
| `.gitignore` | 排除普通 Git 跟踪中的匹配文件 | 阻止读取、上传，或保护已跟踪文件 |

声称访问拒绝有效时，用无害虚构资料做测试，不用私密原件。检查生效的 runtime 配置，记录测了哪条工具路径。无法验证时，保持原件库不可用，并把限制标为未知。

本地文件也可能进入 hosted model calls。若文字被放进云端请求或联网工具，本地保存和看似离线的流程都不能单独保证隐私。核对当前 runtime 和工具会传输什么。不要自动上传档案库、启用整盘索引，或因为 worker 名字不同，就把私密上下文交给它。

## 让有效方法与变化可追溯

按照[偏好指南](personalization-and-evolution.zh-CN.md)，保留明确的未来指令、适用范围、确认依据和版本。“这次先展示探索性的备选方案”属于任务卡上的一次性例外，不改写长期偏好。

反复有效的方法可以成为一个小知识条目或 Skill。事实重要时保留 source ID 与日期。任务成果和实际检查留在任务记录里，不把索引变成聊天档案。

要更换 client、runtime、provider、model 或 instruction overlay 时，使用[模型可移植性指南](model-portability.zh-CN.md)。保留原组合，用代表性虚构任务核对；没有实际证据之前，acceptance 留为 `not_run` 或 partial。记录校验器只检查结构，不调用模型，也不证明结果更好。

确实需要时再升级：使用[runtime adapter](compatibility.md)核对原生入口加载，用标准 scaffold 加正式任务关卡，或用锁/worktree 核对并行写入。第一份长期可用的成果，可以只是核对后的本地文件，以及下一会话真正找到的交接。
