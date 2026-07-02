# Direct API Adapter

Use this when building a custom app or script around the same file contract.

## Official docs checked

This is the generic PAS adapter. Pair it with a provider adapter when using a specific model backend:

- DeepSeek: `pas/adapters/deepseek.md`
- Qwen / Alibaba Cloud Model Studio: `pas/adapters/qwen.md`
- MiniMax: `pas/adapters/minimax.md`
- Z.AI GLM: `pas/adapters/glm.md`
- Xiaomi MiMo: `pas/adapters/xiaomi-mimo.md`
- Tencent Hunyuan: `pas/adapters/tencent-hunyuan.md`

## System Message Assembly

```python
from pathlib import Path

root = Path("/path/to/My Agentic Control Center")
system_message = "\n\n".join(
    (root / name).read_text(encoding="utf-8")
    for name in ["IDENTITY.md", "RULES.md", "SYSTEM_MAP.md", "STATUS.md", "MEMORY.md"]
)
```

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

## Runtime Selection

For a task inside a domain agent, add the relevant `task.yaml` and domain agent files after the root files.

## Writeback

After a session, ask the model for:

1. a `task.yaml` update;
2. a `STATUS.md` update if system state changed;
3. a compact `MEMORY.md` update only for durable recovery notes;
4. any reviewed `outputs/`, skill, or knowledge file content.

Review before writing to disk.
