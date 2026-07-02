# Tencent Hunyuan Adapter

Use this when the model backend is Tencent Hunyuan and the portable harness state remains in local Markdown.

## Official docs checked

- Tencent Cloud Hunyuan product docs: https://cloud.tencent.com/document/product/1729
- Tencent Cloud Hunyuan API / compatibility docs: https://cloud.tencent.com/document/product/1729/111007

## Runtime shape

Tencent Hunyuan is usually accessed through Tencent Cloud credentials and official API/AI Gateway configuration. Because endpoint shape can depend on product mode, region, and gateway settings, keep the base URL configurable and copy it from the current Tencent Cloud console/docs for the target account.

```bash
export TENCENT_HUNYUAN_API_KEY="..."
export TENCENT_HUNYUAN_BASE_URL="https://YOUR_TENCENT_HUNYUAN_ENDPOINT/v1"
export TENCENT_HUNYUAN_MODEL="hunyuan-turbos-latest"
```

If your Tencent Cloud path uses request signing rather than an OpenAI-compatible key, wrap that official SDK call behind a small local adapter and keep the PAS file contract unchanged.

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

## Minimal OpenAI-compatible call

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
    api_key=os.environ["TENCENT_HUNYUAN_API_KEY"],
    base_url=os.environ["TENCENT_HUNYUAN_BASE_URL"],
)

response = client.chat.completions.create(
    model=os.environ.get("TENCENT_HUNYUAN_MODEL", "hunyuan-turbos-latest"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nPropose the next action and any reviewed file updates."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Do not rely on provider-side memory for durable state. Write reviewed task state back to local `task.yaml`, `STATUS.md`, and compact `MEMORY.md` notes.
