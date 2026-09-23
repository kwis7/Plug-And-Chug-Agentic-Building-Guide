# Task Contracts, Generated Status, Gates, Budgets, and Locks

## Task contract

A task contract is a work order, not a diary. Use it when work crosses sessions, touches several files, has a formal deliverable, needs independent verification, or carries meaningful risk. Keep one-off questions lightweight.

Required v2 fields:

```yaml
schema_version: 2
id: T-001
owner: research-agent
owner_root: research-agent-Agent
status: active
objective: Produce a source-backed comparison.
scope:
  included:
    - named sources
  excluded:
    - external publication
inputs:
  - raw_data/source-index.json
authority:
  allowed_reads:
    - raw_data/source-index.json
  allowed_writes:
    - workspace/
    - artifacts/
    - outputs/
  allowed_tools:
    - local parser
  prohibited_actions:
    - send
    - publish
    - use credentials
outputs:
  - outputs/comparison.md
completion_criteria:
  - claims have sources
  - counter-evidence is preserved
failure_conditions:
  - required source unavailable
verification:
  commands:
    - python3 scripts/check_report.py outputs/comparison.md
  receipts:
    - artifacts/verification/report-check.json
verification_state: pending
execution:
  writer: null
  parallel_write: false
  worktree: null
  resources: []
handoff:
  summary: null
  next_action: collect sources
```

The generated scaffold stores JSON syntax inside `task.yaml`. JSON is valid YAML and allows the stdlib-only validator to parse nested structures without installing a dependency. The validator also supports a conservative human-written YAML subset.

## Generated status

`STATUS.md` is a materialised view of task contracts. Agents update task manifests and run `generate_status.py`; they do not maintain a second hand-written copy of state. A check mode fails when the snapshot is stale. This turns forgotten status updates from a behavioural hope into a deterministic test.

## Verification receipts

A verification command string is only an intention. A receipt records what actually happened. A useful receipt contains task ID, command or check, timestamp and timezone, runtime/tool version, exit code, checked inputs, observed outputs, hashes when appropriate, and pass/fail details. Store large evidence outside the manifest and link it.

Distinguish file existence, static validation, local execution, runtime loading, external deployment, message delivery, and transaction completion. Evidence at one level never proves another.

## Completion gate

Successful terminal completion requires:

1. valid task schema;
2. terminal status;
3. all declared outputs inside the owner root and present;
4. non-empty completion criteria;
5. `verification_state: passed`;
6. verification receipts present and readable;
7. generated status current;
8. no remaining locks owned by that task;
9. instruction, memory, task, and large-file budgets pass;
10. handoff summary present.

`failed` and `cancelled` are honest terminal outcomes. They require current state and a useful handoff, but they must not fabricate successful outputs, `verification_state: passed`, or success receipts.

Use the same `closeout_gate.py` beneath runtime-specific hooks, then translate its result into the host protocol. The generated wrapper returns `decision: block` for Codex/Claude `Stop` and `decision: deny` for Gemini `AfterAgent`. Markdown reminders and a bare validator exit code remain advisory. A gate is only verified after the actual runtime blocks an intentionally invalid terminal task and accepts a valid one.

## Memory and context budgets

Budgets prevent invisible degradation. The portable defaults intentionally leave room beneath runtime ceilings:

| File | Default |
|---|---:|
| Root `AGENTS.md` | target 16 KiB; hard 24 KiB |
| `CLAUDE.md` or `GEMINI.md` delta | 4 KiB |
| Root `MEMORY.md` | 12 KiB or 120 lines |
| Domain memory | 8 KiB or 100 lines |
| `task.yaml` | 32 KiB |
| Large file in raw/artifact/log/output containers | 256 KiB before mandatory manifest indexing |

When memory overflows, move task facts to the task, stable background to knowledge, history to archive, evidence to receipts, and repeated procedures to skills. Keep pointers and durable significance in memory. Do not silently truncate the only authority.

## Data lifecycle

`raw_data/` holds immutable or append-only originals. `workspace/` holds active drafts. `artifacts/` holds generated intermediates. `logs/` holds rotated traces. `outputs/` holds reviewed deliverables. `archive/` holds closed versions. Every file at or above the threshold in raw/artifact/log/output containers needs a manifest entry with relative path, exact `size_bytes`, context policy, and short retrieval summary.

## Resource locks

Task manifests record intended writer, worktree, and resources. Atomic lock files record live ownership and are ignored by Git. A lock includes resource, task, session, writer, mode, worktree, created time, heartbeat, and expiration.

Rules:

- one authoritative path has one writer;
- parallel read-only work is allowed;
- separate Git worktrees isolate concurrent code edits;
- a branch is checked out in only one worktree;
- resources must be declared in the active task before acquisition;
- writer, session, task, and worktree must match the task contract;
- locks have TTLs, heartbeat renewal, and stale recovery;
- handoff releases or transfers ownership;
- terminal closeout fails while locks remain.

Locks are coordination, not security. Filesystem permissions, runtime sandboxes, tool policies, and user approval still define the actual authority boundary.

## Failure handling

Use `blocked` when the task cannot progress without a named dependency or decision. Use `failed` for an honest terminal failure with its reason and handoff; successful verification receipts are not required for a failed outcome. Use `partial` in the handoff or output when some requested work is incomplete. Never mark a task complete to make a dashboard look clean.
