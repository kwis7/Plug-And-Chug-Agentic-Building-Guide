# Direct API Harness Pattern

Classification: custom harness implementation
Repository verification: `reference_pattern`

A model API does not read local harness files by itself. The application must implement context assembly, tool execution, permissions, persistence, budgets, verification, and writeback.

## Required loop

1. Resolve the active agent and task.
2. Load the compact common contract plus the named task and relevant references.
3. Enforce token/file budgets before sending context.
4. Expose only task-authorised tools and resources.
5. Validate tool arguments and preserve receipts.
6. Write drafts and artifacts into scoped directories.
7. Run verification and the closeout gate outside the model.
8. Persist reviewed task, status, memory pointers, and outputs.

```python
from pathlib import Path

root = Path("/path/to/system")
common = (root / "AGENTS.md").read_text(encoding="utf-8")
task = (root / "tasks/T-001/task.yaml").read_text(encoding="utf-8")
system_context = common + "\n\n# Active task\n" + task
```

That snippet only assembles text. A real harness still needs tool schemas, permission checks, injection boundaries, result validation, retry policy, context truncation, state transactions, and deterministic completion checks.
