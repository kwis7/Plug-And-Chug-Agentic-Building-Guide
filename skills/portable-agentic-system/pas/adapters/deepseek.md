# DeepSeek Adapter

Use this when the model backend is DeepSeek and the durable agentic system remains in local Markdown files.

## Official docs checked

- DeepSeek API Docs: https://api-docs.deepseek.com/
- API keys: https://platform.deepseek.com/api_keys

## Runtime shape

DeepSeek exposes an OpenAI-compatible chat-completions API. The adapter can therefore use the same file-loading contract as `direct-api.md` and swap only the client configuration.

```bash
export DEEPSEEK_API_KEY="..."
export DEEPSEEK_BASE_URL="https://api.deepseek.com"
export DEEPSEEK_MODEL="deepseek-chat"
```

Use `deepseek-reasoner` only when the task benefits from explicit reasoning behaviour and current DeepSeek docs/account access support it.

## Harness context

```bash
export PAS_ROOT="$HOME/Desktop/My Agentic Control Center"
export PAS_LOAD_ORDER="IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md"
export PAS_TASK_MANIFEST="$PAS_ROOT/tasks/T-000-bootstrap/task.yaml"
```

Load root files first, then the active `task.yaml`, then only the relevant agent `knowledge/` or `skills/` files.

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
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
)

response = client.chat.completions.create(
    model=os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"),
    messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": task_context + "\n\nSummarise the current task and propose the next safe action."},
    ],
)
print(response.choices[0].message.content)
```

## Writeback

Ask DeepSeek for reviewed patch-style updates to `task.yaml`, `STATUS.md`, and compact `MEMORY.md` notes. Keep API keys in environment variables or `.env`; do not paste them into prompts, Markdown, or Git.

## Sandbox check without an API key

```bash
python3 - <<'PY'
import os
from pathlib import Path
root = Path(os.environ.get("PAS_ROOT", "/tmp/pas-smoke-system"))
for name in "IDENTITY.md RULES.md SYSTEM_MAP.md STATUS.md MEMORY.md".split():
    assert (root / name).exists(), name
print("DeepSeek adapter context files are readable")
PY
```
