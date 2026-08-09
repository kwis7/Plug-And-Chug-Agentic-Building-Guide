# Context, State, Memory, Knowledge, and Files

## 1. The five different things people call memory

Agent discussions often use “memory” for incompatible mechanisms. Separate them:

1. **Conversation history**: recent messages supplied to the model.
2. **Working context**: the complete temporary input assembled for the current turn.
3. **Task state**: objective, scope, status, outputs, checks, resources, and next action.
4. **Recovery memory**: a compact cross-session handover and index.
5. **Knowledge archive**: durable source material, concepts, methods, and prior reviewed results.

Only the fourth should normally be called `MEMORY.md`. The fifth belongs in `knowledge/` or a retrieval store. Current task state belongs in a manifest. A transcript is neither a reliable task tracker nor a curated knowledge base.

## 2. Context as a compiled view

Think of context as a compiled program assembled from source files. The runtime selects an instruction chain, the agent selects a task and skill, retrieval selects knowledge snippets, and tools add observations. The result exists for one reasoning step and is discarded or compacted afterward.

This model explains why a file can exist without being known to the model, and why a directory can be dangerous even when every file is individually relevant. Loading all files replaces selection with noise.

An effective context assembly order is:

1. platform and runtime policy;
2. project entrypoint and nearest domain delta;
3. active task contract;
4. one triggered skill;
5. named knowledge or source fragments;
6. current workspace artifact;
7. concise tool observations;
8. verification result.

The order is conceptual rather than universal runtime behavior. Document the actual runtime semantics separately.

## 3. Stable, dynamic, historical, and external truth

Every durable file should primarily represent one temporal class:

| Class | Examples | Correct home |
|---|---|---|
| Stable policy | privacy rule, approval boundary | entrypoint or `RULES.md` |
| Stable identity | mission, audience, ownership | `IDENTITY.md` |
| Stable topology | domain registry, routing owner | `SYSTEM_MAP.md` |
| Dynamic task state | in progress, blocked, receipt pending | `task.yaml`, generated `STATUS.md` |
| Current working material | draft, scratch calculation | `workspace/` |
| Historical recovery | durable decision, last reviewed milestone | bounded `MEMORY.md` |
| Long-term reference | methods, source guides, background facts | `knowledge/` |
| External current fact | price, regulation, live status, provider behavior | fresh authoritative source plus dated receipt |

Problems appear when one file mixes these classes. An old report becomes “current”; a memory note becomes an approval; a hand-edited dashboard contradicts the task; a stable rule is buried in a log.

## 4. The task contract is the operational source of truth

A task contract should answer, without reading chat:

- What outcome is requested?
- Who owns it and where may it write?
- What is included and excluded?
- What inputs are authorised?
- Which tools and actions are allowed?
- Which actions are prohibited or require approval?
- What outputs must exist?
- What counts as success and failure?
- Which tests or reviews create receipts?
- Which writer, worktree, and resources are active?
- What is the current status?
- What should the next model do?

Use a manifest for work that is multi-file, cross-session, concurrent, high-risk, or formally deliverable. A one-line explanation does not need a bureaucratic task record.

### A state machine instead of adjectives

Prefer a small lifecycle with explicit transitions:

```text
proposed -> active -> waiting_review -> complete
                    -> blocked
                    -> failed
                    -> cancelled
```

`blocked` means an external dependency prevents meaningful progress. `failed` means the task reached a terminal unsuccessful outcome. `waiting_review` means work exists but approval or independent review is pending. `complete` means the completion gate passed, not merely that the model wrote a summary.

### Generated status

`STATUS.md` should be a deterministic projection of task manifests. It is a view, not an authority. A generator removes the requirement that every model remember to edit a dashboard in exactly the right way.

Staleness becomes testable: regenerate the expected view and compare it with the file. If they differ, the closeout gate blocks.

## 5. Memory is a handover, not a warehouse

A useful memory entry contains:

- a stable decision or user preference;
- why it matters;
- its date or review horizon;
- a pointer to the authoritative artifact;
- unresolved uncertainty;
- the smallest information required to resume.

A harmful memory entry contains:

- a copied transcript;
- routine tool output;
- a whole report;
- current task status already stored elsewhere;
- dynamic facts with no date;
- secrets or private raw data;
- speculative conclusions presented as settled.

### Memory budget and compaction

Set both byte and line limits. A recommended portable root ceiling is 12 KiB and 120 lines; domain memory can target 8 KiB and 100 lines. The exact number is less important than having a deterministic ceiling below the runtime's broader context limits.

At 80% capacity:

1. remove duplicated state;
2. move stable explanations to knowledge;
3. move closed task detail to archive;
4. replace evidence blocks with receipt paths;
5. merge repeated decisions;
6. mark stale facts with a review date or remove them;
7. keep the few pointers needed for recovery.

Compaction should preserve decisions, not wording.

## 6. Knowledge is the long-term archive

Knowledge can include domain glossaries, source maps, reviewed conceptual notes, method explanations, stable schemas, and lessons distilled from completed work. It is long-term, but not automatically true forever.

Each knowledge item benefits from metadata:

- title and scope;
- owner agent;
- source or provenance;
- creation and last-reviewed dates;
- stability class;
- sensitivity;
- retrieval keywords;
- superseded-by pointer;
- whether it may cross agent boundaries.

Load knowledge by name or retrieval query. Never use `knowledge/` as an implicit recursive include.

### Memory points; knowledge explains

Suppose a research workflow adopts a preferred source hierarchy. `MEMORY.md` might say: “Use the reviewed source hierarchy; see `knowledge/source-policy.md`, last reviewed 2026-08-09.” The knowledge file contains the explanation. The task manifest records whether that policy was applied in the current task. The receipt records the actual sources checked.

## 7. Skills store procedure

A skill answers “how do we repeatedly do this kind of work?” It should not absorb the agent's identity, the current task, or the entire knowledge archive.

Good skill structure:

```text
skill-name/
├── SKILL.md          # trigger, workflow, boundaries, reference router
├── references/       # details loaded only when relevant
├── scripts/          # deterministic or repetitive operations
├── templates/        # canonical reusable files
└── examples/         # small public-safe fixtures
```

Progressive disclosure works because the runtime can initially see only the skill name and description. It loads the body when the skill triggers, and referenced material only as needed. This makes the description part of the routing system.

## 8. A data lifecycle for files

Files should move through a lifecycle rather than accumulate in a general output folder:

```text
original input -> raw_data
                 |
                 v
active selection -> workspace
                 |
                 v
generated intermediate -> artifacts
                 |
                 v
verification receipt -> task/artifact index
                 |
                 v
reviewed deliverable -> outputs
                 |
                 v
closed/superseded -> archive
```

Logs run beside the flow, recording execution rather than carrying business truth.

### `raw_data/`

Store original or minimally transformed inputs. Prefer read-only use. Record source, date, license, sensitivity, and scope. Do not let an agent treat the directory name as permission to ingest everything.

### `workspace/`

Use it as the current desk: drafts, working notes, selected extracts, and task-local computations. Clean or archive it at closeout. A workspace file is not automatically reviewed.

### `artifacts/`

Store generated intermediate files such as parsed data, caches, test fixtures, render previews, and calculation tables. They may be reproducible and disposable. Record lineage when they support a conclusion.

### `logs/`

Store operational traces. Rotate them. Summarise errors. Keep secrets out. Load a named slice, not the entire history. A log proves that text was emitted, not necessarily that an external action succeeded.

### `outputs/`

Store reviewed deliverables. “In outputs” means approved as an artifact, not authorised for external delivery. Sending, publishing, submitting, deploying, or trading remains a separate action gate.

### `archive/`

Move closed or superseded material here rather than deleting by default. Archive should remain out of startup context and be retrievable by index.

## 9. Large-file manifests

A single oversized file can consume a context window or cause a runtime to truncate more important instructions. Use a local `manifest.json` in high-risk containers.

For every file at or above 256 KiB, record:

```json
{
  "path": "relative/path.ext",
  "size_bytes": 307200,
  "context_policy": "never-auto-load",
  "summary": "Original survey export; select columns with the documented loader."
}
```

The exact threshold can change, but the policy must be mechanical. Default policies:

- raw data: `never-auto-load`;
- artifacts and logs: `summary-only`;
- outputs: `named-only`.

The manifest is an index, not a place for private content. Avoid descriptions that leak identities or secrets.

## 10. Retrieval should preserve evidence boundaries

When retrieving a knowledge or raw-data fragment, carry:

- the owner;
- source path or URL;
- retrieval time;
- selection rule;
- freshness;
- confidence or verification state;
- whether the text is evidence, interpretation, hypothesis, or unknown.

This prevents a retrieved paragraph from losing the context that makes it trustworthy.

## 11. Checkpointing and recovery

Long work should be recoverable after context compaction, runtime failure, or model replacement. A checkpoint needs less prose than people expect:

- active task ID;
- last completed step;
- current artifact paths;
- verification receipts already obtained;
- locks and worktree;
- open questions;
- next safe action;
- failure or stopping condition.

The checkpoint belongs in task/workspace state. Memory should store a pointer only if the task will matter after the current work closes.

## 12. Storage review questions

For every directory, ask:

1. Who owns it?
2. What enters and leaves it?
3. What may load automatically?
4. What requires a named selection?
5. What size limit applies?
6. What makes a file reviewed?
7. What makes it stale?
8. When does it archive or delete?
9. Can another agent borrow the method without copying the data?
10. Can a fresh model recover the authoritative state without reading chat?
