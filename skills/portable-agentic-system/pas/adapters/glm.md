# Z.AI GLM Adapter

Use this when the model backend is GLM through Z.AI and the durable agentic state remains in local Markdown files.

## Official docs checked

- Z.AI quick start: https://docs.z.ai/guides/overview/quick-start
- GLM-4.5 guide: https://docs.z.ai/guides/llm/glm-4.5

## Naming note

The public adapter name is **Z.AI GLM**. Keep the docs, README, file name, environment variables, and routing tables aligned with GLM / Z.AI.

## Runtime shape

```bash
export ZAI_API_KEY="..."
export GLM_BASE_URL="https://api.z.ai/api/paas/v4"
export GLM_MODEL="glm-4.5"
```

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

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
    api_key=os.environ["ZAI_API_KEY"],
    base_url=os.environ.get("GLM_BASE_URL", "https://api.z.ai/api/paas/v4"),
)

response = client.chat.completions.create(
    model=os.environ.get("GLM_MODEL", "glm-4.5"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nSummarise task state and propose safe writeback blocks."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Ask GLM for explicit Markdown/YAML blocks. Keep `task.yaml` as the authority for task state, `STATUS.md` as the system snapshot, and `MEMORY.md` as compact recovery notes.
