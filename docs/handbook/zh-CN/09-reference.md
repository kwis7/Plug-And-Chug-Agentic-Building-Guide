# 9. 参考：使用标准工具包

首次项目目录演示的是一种小型工作方法。Portable Agentic System 工具包提供更完整的标准项目骨架，包含领域目录、任务约定、自动状态页、容量检查、锁和适配配置。当这些功能有用时，可以选择这条搭建路线；完成前面的学习练习并不要求先生成它。

下面的命令从本仓库根目录运行，使用本地 Python 脚本，前提是已经安装与源码兼容的 `python3`。执行前检查脚本、`--help`、目标目录和自己的环境。第一次生成时使用一个新的临时目录。本章说明如何调用，并不表示这些命令已在你的电脑上运行。

## 先预览，再生成

阅读[初始配置](../../../skills/portable-agentic-system/pas/examples/starter-config.json)；需要修改示例领域时，先复制到自己的工作文件。随仓库提供的配置含有两个示例负责人，并不是适合所有人的推荐。每个 Agent 都需要使命、路由描述、排除范围，以及能够区分相邻工作的例子。

选择尚未使用的目标路径，先预览：

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /tmp/pas-learning-demo \
  --config skills/portable-agentic-system/pas/examples/starter-config.json \
  --dry-run
```

预览以 JSON 报告目标根目录与 Agent 路径，不会列出将写入的每个文件。创建前，结合这些路径检查模板和生成器实际生成结构的行为。需要实际创建这份已审阅的结构时，去掉同一命令中的 `--dry-run` 再运行。生成器默认拒绝与已有文件冲突；不要把 `--force` 当成常规报错修复，先查清冲突并保留已有工作。

生成的系统包含运行环境配置，以及 `.pas/bin/` 下的本地运行脚本。在目标工具中信任或启用 hooks 前，应先审阅它们。生成器运行成功，不证明运行环境已经发现或执行这些配置。

## 运行静态检查

生成以后，下列命令用于检查结构。如果选择了其他路径，把目标一致地替换掉。

```bash
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/check_budgets.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/check_descriptions.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/generate_status.py \
  /tmp/pas-learning-demo --check
python3 skills/portable-agentic-system/scripts/harness_health_check.py \
  /tmp/pas-learning-demo --json
```

每项失败都应先读清原因。如果任务记录已经变化而状态页过期，使用同一 root 运行不带 `--check` 的 `generate_status.py`，再重新检查。重新生成会写入 `STATUS.md`，检查模式只核对一致性。

还可以运行适配探测：

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py \
  /tmp/pas-learning-demo --runtime codex
```

执行的仍是**静态**探测，尽管文件名中有 smoke。它报告的 `verification_level` 是 `static`。根据实际目标选择 runtime，并按对应适配文档进行新会话测试。配置检查通过，不能据此升级为运行时验证通过。

## 理解任务记录的权威

标准 `tasks/<task-id>/task.yaml` 记录任务标识与归属、目标与范围、允许读取和写入的内容、工具与禁止动作、输出和完成条件、验证记录、执行资源，以及交接。生成器在 `.yaml` 文件内使用 JSON 语法，便于标准库解析器读取。解析器也支持保守的 YAML 子集，并不承诺支持完整 YAML 语法。

手工构建前，先以生成的任务为格式示例，并查看[治理参考](../../../docs/reference/task-lifecycle.md)。第 3 章的教学交接记录，并不是一份字段完整、可通过校验的任务清单。

对于已经写入生成系统的真实任务，可从该系统根目录调用随附的完成关卡：

```bash
python3 .pas/bin/closeout_gate.py . tasks/T-123/task.yaml
```

将 `T-123` 替换为已有任务。成功收尾需要声明的输出、验证状态与记录路径、最新的自动状态页、符合容量要求、已释放的任务锁，以及交接说明。失败或取消使用如实的非成功状态。关卡的结构检查不能替代内容复核，也不能证明宿主的阻止机制已经实际生效。

## 按需查阅深入说明

以下深层实现参考主要使用英文，精确标识符保持原文：

| 主题 | 维护中的参考 |
|---|---|
| 文件归属与加载 | [文件系统契约](../../../skills/portable-agentic-system/pas/references/filesystem-contract.md) |
| 私密资料与外部动作 | [隐私边界](../../../skills/portable-agentic-system/pas/references/privacy-boundaries.md) |
| 路由与描述 | [路由评估](../../../skills/portable-agentic-system/pas/references/description-routing-evals.md) |
| 运行环境分类 | [兼容性清单](../../../skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) |
| 适配选择与检查 | [适配指南](../../../skills/portable-agentic-system/pas/references/adapters.md) |
| 任务、关卡和并发 | [可靠性参考](../../../skills/portable-agentic-system/pas/references/textbook-reliability.md) |
| 完整设计访谈 | [搭建工作簿](../../../skills/portable-agentic-system/pas/references/textbook-build-workbook.md) |

仓库的 Python 测试命令是 `python3 -m unittest discover -s tests -v`。通过测试能支持被测试的本地行为，但不能证明新会话兼容性、发布、送达或任何外部交易。每一种结果，都应按实际取得的证据分别报告。
