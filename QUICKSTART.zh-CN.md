# 快速开始

[English](QUICKSTART.md) | [中文](QUICKSTART.zh-CN.md) · [首页](README.zh-CN.md)

选一条路线即可。“跟着 AI 做学习案例”和“手动运行标准生成器”是两种入口，不需要依次完成。

| 路线 | 需要什么 | 得到什么 |
|---|---|---|
| [跟着 AI 完成第一个任务](docs/start-here.zh-CN.md) | 能读取所选本地文件的 AI 工具；保存结果还需要写入权限 | 一份资料比较和可以接着做的交接说明 |
| [手动生成标准结构](#manual-standard-scaffold) | Git、Python 3.10+、终端、可写的父目录 | 中控、两个示例领域 Agent、运行环境配置和本地检查工具 |

只有聊天功能的工具，可以在你粘贴虚构资料后讨论案例；没有文件能力时，不能证明本地文件读取或持久保存有效。AI 工具可能收取订阅或 API 费用。本地 Python 生成器不调用模型 API。

## 跟着 AI 完成第一个任务

打开[从这里开始](docs/start-here.zh-CN.md)，再按[第一个项目](examples/first-project/README.zh-CN.md)操作。这个学习工作空间不需要安装 Skill，也不是生成器提供的“最小模式”。练习以后，想整理自己的经常性工作，可以使用[简短起步提示词](skills/portable-agentic-system/pas/references/friend-starter-prompt.md#中文)。

<a id="manual-standard-scaffold"></a>
## 手动生成标准结构

下面是 Bash 或 Zsh 命令，不是 PowerShell 命令。请在可写目录中开始，并确认其中没有同名仓库文件夹或 `my-first-agent-workspace`。整个过程使用同一个终端。

### 1. 获取工具包，检查 Python

```bash
git clone https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide.git
cd Plug-And-Chug-Agentic-Building-Guide
python3 --version
```

请使用 Python 3.10 或更新版本。生成器和下列检查使用 Python 标准库，这条路线不需要安装额外包。运行前先检查仓库中的脚本。

### 2. 设定目标目录，预览结构

```bash
PAS_REPO="$(pwd)"
PAS_SCRIPTS="$PAS_REPO/skills/portable-agentic-system/scripts"
PAS_CONFIG="$PAS_REPO/skills/portable-agentic-system/pas/examples/starter-config.json"
PAS_TARGET="$PAS_REPO/../my-first-agent-workspace"
printf '%s\n' "$PAS_TARGET"
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG" --dry-run
```

`PAS_TARGET` 指向仓库旁边的新目录，不是当前仓库。需要换位置时，现在修改这个变量。如果目录已存在，请改用新的目标目录再继续。

预览会打印 JSON，包含根目录、两个 Agent 的路径和 `"mode": "dry-run"`。它不会创建文件，也不会检查所有可能的写入冲突。配置中的两个示例是 `research-assistant-Agent` 和 `life-admin-Agent`，供你检查和调整，并不意味着每个人都需要这两个 Agent。

### 3. 生成刚才预览的结构

```bash
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG"
```

预期结果：打印包含 `created_count` 和文件路径的 JSON 摘要。目标目录内出现 `AGENTS.md`、`SYSTEM_MAP.md`、`STATUS.md`、初始化任务、两个领域目录和 `.pas/bin/` 下的脚本。生成器还会写入 Codex、Claude Code、Gemini CLI 的 Hook 配置；用可能加载它们的工具打开目录之前，请先检查配置。

这是**标准结构（standard scaffold）**，目前没有最小模式或单一运行环境的开关。生成器默认拒绝覆盖已有文件，但中途失败可能留下已写入的文件。不要直接加 `--force` 处理原因不明的失败；先检查结果，必要时查阅[故障排查](docs/reference/troubleshooting.md)（英文）。

### 4. 检查生成结果

```bash
python3 "$PAS_SCRIPTS/validate_agentic_system.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_budgets.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_descriptions.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/generate_status.py" "$PAS_TARGET" --check
python3 "$PAS_SCRIPTS/harness_health_check.py" "$PAS_TARGET"
```

预期结果：JSON 验证报告中有 `"valid": true`，状态检查显示 `STATUS.md is current`，健康报告明确标为 **static**（静态）。除了错误，也要查看警告。静态检查通过，只说明结构和一致性符合检查条件；它不代表初始化任务已完成，也不能证明运行环境的实际行为。

### 5. 检查职责、接入工具，再试一个任务

阅读生成的 `SYSTEM_MAP.md`、`RULES.md` 和 `tasks/T-000-bootstrap/task.yaml`。引入真实资料之前，先把示例职责改成自己的工作。根据[兼容性参考](docs/reference/compatibility.md)（英文）选择工具；安装 Skill 是可选步骤，方式取决于运行环境。本快速开始不会安装个人范围的配置。

按[验证流程](docs/reference/verification.md)（英文）在新会话中确认指令加载情况，再检查适用的有效及无效任务收尾行为。记录工具版本、日期、命令和观察结果。仓库里的兼容性清单不能代替你本机的验证证据。

然后做一个边界清楚的任务，列出允许使用的资料，保存核对后的成果与交接说明，并从任务记录重新生成 `STATUS.md`。[手册](docs/handbook/index.md)解释整个过程；[任务参考](docs/reference/task-lifecycle.md)（英文）给出精确格式。
