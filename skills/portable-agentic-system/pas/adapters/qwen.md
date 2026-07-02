# Qwen Adapter

Use this when the model backend is Alibaba Cloud Model Studio / DashScope Qwen and the control center remains in local Markdown.

## Official docs checked

- Qwen API reference: https://help.aliyun.com/zh/model-studio/qwen-api-reference/
- OpenAI compatibility for DashScope: https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope
- API key setup: https://help.aliyun.com/zh/model-studio/get-api-key

## Runtime shape

Qwen can be called through Alibaba Cloud Model Studio. DashScope also provides an OpenAI-compatible mode. The exact endpoint depends on region and workspace; the common public compatible endpoint is:

```bash
export DASHSCOPE_API_KEY="..."
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
export QWEN_MODEL="qwen-plus"
```

For international or workspace endpoints, use the current URL from the official compatibility page instead of copying a stale blog snippet.

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

Load root context, then active task state, then the relevant agent knowledge or skill files.

## Minimal Python call

```python
import os
from pathlib import Path
from openai import OpenAI

root = Path(os.environ["PAS_ROOT"])
system_context = "\n\n".join(
    (root / name).read_text(encoding="utf-8")
    for name in os.environ["PAS_LOAD_ORDER"].split()
)
task_context = Path(os.environ["PAS_TASK_MANIFEST"]).read_text(encoding="utf-8")

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url=os.environ.get("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
)

response = client.chat.completions.create(
    model=os.environ.get("QWEN_MODEL", "qwen-plus"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nRoute this task and propose the smallest safe next step."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Have Qwen return proposed Markdown/YAML deltas. Save only reviewed updates to local `task.yaml`, `STATUS.md`, `MEMORY.md`, or `outputs/`.
