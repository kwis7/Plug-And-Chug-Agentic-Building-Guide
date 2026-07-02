# Xiaomi MiMo Adapter

Use this when the model backend is Xiaomi MiMo, either through the official MiMo platform/API or through a local/self-hosted runtime for XiaomiMiMo open models.

## Official docs checked

- MiMo product site: https://mimo.xiaomi.com/mimo-v2-pro
- MiMo docs: https://mimo.mi.com/docs/usage-guide/passing-back-reasoning_content
- XiaomiMiMo GitHub organization: https://github.com/XiaomiMiMo
- XiaomiMiMo model repository: https://github.com/XiaomiMiMo/MiMo

## Naming note

The adapter name is **Xiaomi MiMo**. Do not label this as a generic Xiaomi adapter; the model family and developer platform are MiMo.

## Runtime shape

MiMo has both platform/API materials and open model releases. For hosted API use, follow the current MiMo platform docs for the official endpoint. For local or self-hosted use, expose the model through an OpenAI-compatible server such as vLLM or another runtime your environment supports.

```bash
export MIMO_API_KEY="..."
export MIMO_BASE_URL="https://YOUR_OFFICIAL_OR_LOCAL_MIMO_ENDPOINT/v1"
export MIMO_MODEL="MiMo"
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
    api_key=os.environ.get("MIMO_API_KEY", "local-dev-key"),
    base_url=os.environ["MIMO_BASE_URL"],
)

response = client.chat.completions.create(
    model=os.environ.get("MIMO_MODEL", "MiMo"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nReturn a concise task routing and writeback proposal."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Keep MiMo provider state separate from the local harness state. Durable updates still go to reviewed local files: `task.yaml`, `STATUS.md`, compact `MEMORY.md`, `knowledge/`, `skills/`, or `outputs/`.
