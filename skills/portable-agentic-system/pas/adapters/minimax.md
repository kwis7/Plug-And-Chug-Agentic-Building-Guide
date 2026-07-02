# MiniMax Adapter

Use this when the model backend is MiniMax and the portable agentic state remains in local Markdown files.

## Official docs checked

- MiniMax platform docs: https://platform.minimax.io/docs/guides/models-intro
- MiniMax Chat Completions v2 docs: https://platform.minimaxi.com/document/ChatCompletion%20v2
- MiniMax OpenAI-compatible Chat Completions docs mention `/v1/chat/completions`.

## Runtime shape

MiniMax has multiple documentation domains and regional platform surfaces. Confirm the current base URL in the official console/docs for your account. The OpenAI-compatible path is documented around `POST /v1/chat/completions`; keep the base URL configurable:

```bash
export MINIMAX_API_KEY="..."
export MINIMAX_BASE_URL="https://api.minimax.io/v1"
export MINIMAX_MODEL="MiniMax-M1"
```

If your account docs show `api.minimaxi.com` or another regional host, set `MINIMAX_BASE_URL` to that official value.

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
    api_key=os.environ["MINIMAX_API_KEY"],
    base_url=os.environ["MINIMAX_BASE_URL"],
)

response = client.chat.completions.create(
    model=os.environ.get("MINIMAX_MODEL", "MiniMax-M1"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nReturn a reviewed task update proposal."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Request separate proposals for `outputs/`, `task.yaml`, and `STATUS.md`. Review locally before writing.
