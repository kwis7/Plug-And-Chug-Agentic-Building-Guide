# 9. 参考：使用标准工具包

前几章用少量文件完成了一次比较和交接。若你的工作需要领域目录、规范的任务记录、自动状态页、容量检查、锁或适配配置，可以采用 Portable Agentic System 工具包提供的标准项目骨架。先根据需要选择搭建方式，完成练习并不要求生成完整骨架。前面的教学工作空间也不是生成器中的特殊模式。

本章供选择工具包路线时查阅。命令应从本仓库根目录运行，使用已经安装、与源码兼容的 `python3`。执行前，先看脚本和 `--help`，确认环境与目标目录。第一次尝试宜使用新的临时目录，便于将生成结果与已有工作分开。这里的示例说明调用方法，不代表命令已在你的电脑上执行。

## 先预览，再生成

生成前先阅读[初始配置](../../../skills/portable-agentic-system/pas/examples/starter-config.json)。其中的两个负责人用于演示职责配置，不表示每个人都应采用同样的分工。配置一个 Agent 时，要说明它的使命、何时将任务交给它、哪些工作不归它，以及如何区分相邻任务。需要修改示例领域，就先复制配置到自己的工作文件。

选好尚未使用的目标路径后，先运行预览：

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /tmp/pas-learning-demo \
  --config skills/portable-agentic-system/pas/examples/starter-config.json \
  --dry-run
```

`--dry-run` 返回 JSON，报告目标根目录和各 Agent 的路径。它提供的是路径预览，没有逐一列出准备写入的文件。创建前还需查看模板，了解生成器会建立什么结构。确认并同意创建后，去掉同一命令中的 `--dry-run` 再运行。

如果遇到已有目标文件，生成器默认拒绝覆盖。应先检查发生冲突的路径和当前文件，已有部分输出也需要检查。`--force` 会允许覆盖已有文件，所以使用前必须明确如何保留原有工作，并取得相应授权。报错本身不能成为覆盖文件的理由。

生成结果包含运行环境配置和 `.pas/bin/` 下的本地运行脚本。准备在目标工具中信任或启用 hooks 时，先审阅这些内容。此时能确认的是文件已经生成；宿主是否发现、加载并执行了配置，要到对应环境中另行验证。

## 运行静态检查

生成后，下面的命令检查项目骨架。若使用了其他目标目录，每条命令都应指向同一个新路径。

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

检查失败时，先从报告定位原因。例如，任务记录更新后，状态页可能还保留旧内容。带 `--check` 的 `generate_status.py` 只比较一致性，不会改写状态页。要更新它，使用同一 root 运行不带 `--check` 的命令，再检查一次。这样，`STATUS.md` 始终由任务记录生成。

针对准备使用的 runtime，还可以检查适配配置：

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py \
  /tmp/pas-learning-demo --runtime codex
```

查看结果时，注意它报告的 `verification_level` 是 `static`。脚本名虽然含有 smoke，检查对象仍是生成的配置，运行结果不包含宿主实际加载规则或执行 hook 的证据。下一步应按所选 runtime 的适配文档进行新会话测试，再分别报告静态检查和运行时观察。

## 理解任务记录的权威

当任务需要标准检查时，要把工作约定写入 `tasks/<task-id>/task.yaml`。其中应记录任务标识和归属、目标和范围、允许的输入与写入、工具及禁止动作，也要说明输出、完成条件、验证与记录路径、执行资源和交接。这些字段让检查脚本有明确的依据，不必从一句“已经完成”中推测任务状态。

文件扩展名是 `.yaml`，生成器写入的内容采用 JSON 语法。标准库解析器可以读取它，也支持保守的 YAML 子集，但不能将其视为支持完整 YAML 的解析器。手工编写时，先参照生成任务的格式，再查看[治理参考](../../../docs/reference/task-lifecycle.md)。第 3 章的简短交接用于恢复工作，尚不具备完整任务清单所需的字段。

任务已经在生成系统中建立后，可以从该系统根目录调用随附的完成关卡：

```bash
python3 .pas/bin/closeout_gate.py . tasks/T-123/task.yaml
```

将 `T-123` 换成实际存在的任务 ID。成功收尾要求声明的输出、符合要求的验证状态与记录路径、最新生成的状态页、容量检查通过、任务锁已释放，以及交接说明。若任务失败或取消，应保留如实的非成功状态。结束记录不等于取得成功结果。

关卡可以发现输出或验证记录缺失，但文件存在仍需要内容复核，验证记录也需要检查其证据是否支持结论。这里直接调用脚本，还没有证明宿主会自动调用它，或会阻止不符合条件的收尾。后者属于运行时行为，需要单独观察。

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

维护仓库代码时，可运行 `python3 -m unittest discover -s tests -v`。通过测试，支持的是这些测试覆盖到的本地行为。新会话兼容性、发布、送达和外部交易是另外的结果，需要各自操作产生的证据。报告时说明取得了哪一层证据，才能让读者判断还有什么尚未验证。
