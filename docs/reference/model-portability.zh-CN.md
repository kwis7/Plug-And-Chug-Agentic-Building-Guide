# 与现有 AI 应用协作的模型可移植性

[English](model-portability.md)

让本地工作区在应用、服务商或模型变化后仍然可用。宿主（host）已经负责运行模型、提供工具、管理当前对话，以及执行原生权限和上下文压缩（compaction）。Plug & Chug 帮助你保留描述自己工作的文件：归属、指定输入、确认的偏好、可复用知识、任务状态、检查过的产物和恢复指针。

这份可选指南适用于比较或更换现有配置。它不要求再搭建一套执行引擎、服务商网关或多 Agent 系统。如果眼下只是想整理长期使用的材料，先看[本地工作区指南](local-workspace.zh-CN.md)。

## 分清正在变化的层次

| 层次 | 记录什么 | 变化后检查什么 |
|---|---|---|
| 客户端（client） | 你使用的应用、CLI 或 SDK 及其版本 | 生效设置，以及选择运行时或接口地址的方式 |
| 运行时（runtime） | 执行对话和工具的软件 | 指令加载、工具、原生权限、恢复，以及已配置的 hooks |
| 服务商（provider） | 接收并服务请求的平台 | 接口类型、地区或套餐、可用性与数据使用条件 |
| 通信 API（wire API） | 请求和响应协议 | 消息角色、工具 ID 和参数、流式响应、错误与服务商专用字段 |
| 模型（model） | 请求的模型标识与实际返回的版本 | 任务所需能力、生效参数、上下文行为和任务结果 |
| 行为补充指引（behavioral overlay） | 对共享指引的小幅、带版本调整 | 示例、格式或过程提示是否改善同一个任务 |

客户端和运行时可能是同一个产品。API 服务商也可能另有 Agent 产品。记录你实际使用的软件；单独一个服务商名称不能确定运行时。API 语法兼容不能证明原生指令加载，也不能证明宿主厂商正式支持该组合。

测试模型时，保持 owner 和工作契约稳定。行为补充指引可以在观察后澄清输出格式，或删去无益的过程安排，但不能削弱审批、私密数据边界、工具权限或完成标准。偏好应当是[明确且可复核的选择](personalization-and-evolution.zh-CN.md)，而不是对模型或用户的猜测。

## 让宿主继续负责执行

使用宿主已有的工具、原生记忆和上下文压缩，不必用本地脚本重复实现。保存简短的本地交接和指定文件的指针，让另一段对话可以恢复任务。本地恢复说明不能复现宿主对话状态的每个细节；目录名称也不构成访问控制。

更换宿主时，检查它能否在预期权限下读取指定文件。可移植文件不会自动注册 Skills、配置工具、导入原生记忆或启用 hooks。[Adapter 选择参考](../../skills/portable-agentic-system/pas/references/adapters.md)和[验证流程](verification.md)分别说明这些检查面。

个人信息原件由用户控制。只使用用户为本次任务提供的最小字段、明确标记为 Agent 可读的脱敏副本，或受控中介的输出。本地保存不代表离线处理，也不代表可以把数据发送给另一个服务商。参见[隐私与边界](privacy-and-boundaries.md)。

## 记录一个选定组合

[模型组合模板](../../skills/portable-agentic-system/pas/templates/model-combination.json)是一份可选 JSON 记录。将它复制到 owner 已有的任务或配置位置，设置有意义的 ID。模板是示意记录，能力为未知，`acceptance.status` 为 `not_run`；它不是生效配置、benchmark 或兼容性声明。

只填写已知信息：

- 记录客户端和运行时版本、服务商接口类型与地区、请求的模型 ID，以及可获得的实际模型 ID。无法获得实际 ID 或验证日期时，保留 `null`。会变化的别名不是固定版本。
- 列出任务所需能力。每项观察使用 `documented`、`observed`、`unknown` 或 `unsupported`，并附官方来源或本地 receipt 引用。文档支持仍需实际任务检查才能验收。
- 区分文档中的 token 上限和观察到的 compaction 行为。不要根据模型名称或文件字节预算推断可用上下文。
- 记录该组合支持、忽略和不支持的参数。空列表表示尚未记录条目，不表示所有参数都支持。
- 保留简短的 overlay ID 和版本。已有证据时，引用验收 receipts、上一个通过验收的组合和明确的回退条件。

不要把 API 密钥、账户标识、私人路径、请求正文或原始推理内容写入记录。需要时，在引用的 receipt 中记录价格、延迟和用量：日期、实际耗时、重试次数、返回的 token 用量、实际或估算费用，以及价格来源。无法获得的测量值保持未知。比较实际任务表现，不给模型贴通用排名。

在本仓库根目录，用仅依赖标准库的检查器验证记录：

```bash
python3 scripts/check_workspace_records.py \
  skills/portable-agentic-system/pas/templates/model-combination.json
```

检查引用关系时，把相关 receipt 记录或包含记录的 bundle 一并传入命令。`acceptance.receipt_refs` 填写 receipt 记录的 ID，不是让检查器打开的文件名。检查器只检查结构、状态和已提供记录之间的关系；它不请求服务商、不读取任意引用来源、不切换模型，也不能证明运行时行为。设置 fallback ID 既不会配置自动切换，也不构成向备用服务商发送输入的授权。

## 用同一个任务比较

在使用个人材料之前，先用小型合成任务测试候选组合。例如，两份指定笔记都说研讨会在周四 10:00 开始，却写了不同房间。要求保存产物，保留共同时间，并把地点标为未解决，然后在新对话中根据交接继续。

基准组合和候选组合使用相同的输入、owner、权限、输出断言和评审标准。记录生效设置；不兼容参数不会因为数值相同就变得等价。使用宿主已有工具完成无害的本地读写练习；外部副作用使用模拟或省略。

| 通用检查 | 保留什么证据 |
|---|---|
| `instruction_loading` | 新会话从指定文件中识别正确的 owner、任务、指定输入和边界 |
| `tool_round_trip` | 正确处理一次授权的本地工具调用和返回结果，重新打开并检查保存的产物 |
| `uncertainty` | 产物保留分歧，没有编造房间 |
| `recovery` | 另一段新对话无需旧聊天，就能找到保存的产物、缺口和下一步允许动作 |

对每项额外所需能力增加实际检查，例如结构化输出、流式响应或图像输入。明确保留不支持或无法测试的检查。仅能聊天的规划，不能靠描述工具将如何运行来通过本地工具检查。

分别评估路由和产物质量：选对 Skill 不能证明事实正确。按指定输入和标准检查结果，记录人工提示或介入，并在声称改善之前重复重要案例。从小规模人工比较开始即可。

`passed` 要求 `observed` 模式的证据、验证日期，并关联覆盖四项通用检查及所有所需能力的实际 receipts。作者编写的示例应保留 `not_run`，或如实标为 `partial`；必要检查失败时保持 `failed`。以后运行时、协议、模型版本或 overlay 变化，需要新记录或重新验证受影响的检查。

只有配置实际使用并声明相应能力时，才另外测试原生完成 gate、原生访问拒绝或并发。[验证流程](verification.md)说明无效收尾、有限恢复和修复后验收。模型主动拒绝请求，不能证明 hook 或权限机制被触发。一次成功比较只支持被测任务和组合，不能证明该模型的所有用途。

## 当前协议注意点

以下官方来源于 **2026-10-02** 核验，说明为什么需要记录具体组合：

- Claude Code 网关文档明确不支持通过任何网关把 Claude Code 请求路由到非 Claude 模型。第三方实验不能表述为 Claude Code 官方兼容。网关也需要传递已安装运行时使用的能力。[Claude Code 网关](https://code.claude.com/docs/en/llm-gateway)
- Claude Code 区分别名和完整模型名称。可以获得实际模型时，应记录它，不能把别名当作不可变版本。[模型配置](https://code.claude.com/docs/en/model-config)
- DeepSeek thinking mode 接受但忽略某些采样参数；带 tools 的对话也有特定的 `reasoning_content` 回传要求。检查所选客户端的协议处理，在 receipt 中描述检查，不复制原始推理内容。[DeepSeek thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/)
- Qwen thinking 控制包含非标准参数，其支持情况随模型而异。接口地区和凭据地区也必须与所选服务一致。[Thinking 控制](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)、[OpenAI API 兼容](https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope)
- Z.AI 区分通用 API 接口和 Coding Plan 接口。记录选定接口类型，不要假设一个接口适用于所有套餐。[Z.AI 快速开始](https://docs.z.ai/guides/overview/quick-start)

这些是注明日期的文档事实，不是本仓库的在线验收结果。现有兼容性清单保留自己的证据日期和验证等级。
