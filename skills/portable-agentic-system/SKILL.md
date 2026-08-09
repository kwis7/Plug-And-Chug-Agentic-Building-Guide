---
name: portable-agentic-system
description: Build, audit, migrate, explain, or harden a local-first AI agent harness whose active models are replaceable. Use when the request concerns agent folders, control centers, multi-agent routing, AGENTS.md/CLAUDE.md/GEMINI.md adapters, task manifests, generated status, completion gates, memory or context budgets, knowledge archives, skills, tools, raw data, outputs, locks, worktrees, provider switching, runtime compatibility, or questions such as “what is a harness?” and “how do I build my own agent system?”. Also trigger for pas-start, pas-audit, pas-add-agent, pas-adapt, pas-review, pas-create-skill, pas-distill, pas-borrow, and pas-explain. Do not use for a one-off prompt that needs no durable files, state, or workflow.
---

# Portable Agentic System

Design and maintain an inspectable operating system around one or more replaceable models. Build the smallest structure that can preserve ownership, recover work, limit context, enforce completion, and survive a change of model or runtime.

## Preserve the core mental model

- Treat the **model** as the active employee doing the reasoning. Put it in a visually and architecturally distinct, replaceable slot.
- Call a model the **manager** only when it centrally routes or coordinates a multi-agent matrix. In a single-agent system it is simply the employee.
- Treat the **harness** as every configured part around execution: runtime entrypoints, identity, rules, permissions, tools, connectors, skills, tasks, state, memory, knowledge, files, workspace, hooks, gates, budgets, locks, worktrees, validators, adapters, and ownership boundaries.
- Do not describe the harness as a vague second layer. Every configuration box and flow belongs to the harness.
- Treat **context** as the finite working surface assembled for the current turn, not as the whole filesystem.
- Treat **memory** as a compact recovery handover and index.
- Treat **knowledge** as the long-term archive or institutional library, loaded by retrieval only when relevant.
- Treat a **skill** as a reusable department playbook or capability package, not a permanent persona.
- Treat a **runtime** as the software that loads instructions, grants tools, runs hooks, and hosts the model.
- Treat a **provider** as an inference backend. A provider does not automatically read local entrypoints or persist state.

Read `pas/references/mental-model.md` when the user needs the concepts explained before construction.

## Use progressive disclosure deliberately

The runtime normally sees only this skill's `name` and `description` before activation. After activation it loads this file. Do not preload every reference, adapter, template, or script.

1. Identify the request mode.
2. Read only the references named for that mode.
3. Read one runtime adapter after the runtime is known.
4. Run scripts directly when their implementation does not need to enter context.
5. Open the standalone playbook only for a full teaching handoff or a deep audit.

This division keeps the trigger description precise, the operating instructions complete, and the large textbook out of routine context.

## Select one primary mode

| Mode | Trigger | Required references | Default result |
|---|---|---|---|
| `pas-explain` | Explain harness, model, memory, knowledge, skill, or context | `mental-model.md` | A clear explanation or system map |
| `pas-start` | Build a personal system from zero | `intake-questions.md`, `filesystem-contract.md`, `privacy-boundaries.md` | Design Contract, preview tree, then scaffold |
| `pas-audit` | Review an existing agent system or repository | `filesystem-contract.md`, `description-routing-evals.md`, `system-review-and-renewal.md` | Evidence-backed findings and minimal patch plan |
| `pas-adapt` | Add or repair runtime support | `adapters.md`, compatibility manifest, exactly one product adapter | Correct entrypoint/projection/gate plus evidence label |
| `pas-add-agent` | Add a durable owner or a bounded temporary worker | `intake-questions.md`, `description-routing-evals.md`, `filesystem-contract.md` | Agent-vs-skill-vs-task decision, routing contract, then files |
| `pas-create-skill` | Add or improve a skill or subagent | `description-routing-evals.md`, `skill-matrix.md` | Trigger contract, files, eval fixtures, validation |
| `pas-distill` | Convert notes, prompts, or repeated corrections into durable architecture | `skill-distillation-and-fusion.md`, `privacy-boundaries.md` | Classified rule, knowledge, skill, task, or archive material |
| `pas-borrow` | Reuse another agent's method without merging private context | `cross-agent-skill-borrowing.md`, `privacy-boundaries.md` | Scoped method borrowing and optional local distillation |
| `pas-review` | Compact memory, renew architecture, or archive noise | `system-review-and-renewal.md` | Renewal report and bounded state |
| full handoff | Teach another agent to build the whole system | `master-build-playbook.md`, `friend-starter-prompt.md` | Standalone guide and starter prompt |

If several modes apply, sequence them. For example: audit first, adapt second, migrate only after the target contract is approved.

## Establish authority before inspecting or writing

Perform this preflight:

1. Confirm the exact target root and whether it is new or existing.
2. Check runtime, operating system, Git state, and existing project instructions.
3. Treat existing changes as user-owned.
4. Define read and write scope.
5. Identify private-data classes and public-output constraints.
6. Separate local edits from external actions such as commit, push, deploy, send, publish, pay, trade, or delete.
7. Ask only for a missing decision that would materially change the result.

Do not read credentials, `.env` contents, tokens, cookies, keychains, account records, private messages, client/student records, raw health data, unpublished datasets, or large private corpora unless the user explicitly authorises the exact purpose and scope. Never copy those into examples, memory, logs, or public Git.

For public examples, use generic first- and second-level folder patterns only. Preserve architecture; remove identities, absolute personal paths, data values, task contents, and report contents.

Read `pas/references/privacy-boundaries.md` before scanning a private multi-agent system or producing public artifacts from it.

## Run discovery in stages

Do not send the entire questionnaire at once. Ask one short stage, summarise the answer, propose sensible defaults, and continue.

### Stage A — outcome

Determine:

- recurring work the system should handle;
- failure or friction in the current workflow;
- expected deliverables;
- success criteria after 30 days;
- whether the request is explanation, build, audit, migration, or hardening.

### Stage B — runtime stack

Name separately:

- the runtime or host actually executing the model;
- the provider and active model;
- any provider switchboard;
- local folders, connectors, MCP servers, plugins, or cloud workspaces;
- operating systems and machines that must work.

Never infer runtime behavior from the model name. “DeepSeek”, “Qwen”, or “GLM” may be providers inside Codex, Claude Code, a custom loop, or another runtime.

### Stage C — recurring domains

List recurring work domains. For each domain record:

- mission;
- primary inputs and outputs;
- data sensitivity;
- authoritative sources;
- tools and connectors;
- approval boundaries;
- overlap with other domains;
- positive and negative routing examples.

### Stage D — persistence

Decide what must persist across sessions:

- current task state;
- stable decisions;
- knowledge and source material;
- reusable procedures;
- reviewed deliverables;
- evidence receipts;
- unresolved questions.

Do not put all of these into memory.

### Stage E — risk and concurrency

Identify:

- external or irreversible actions;
- shared files and scarce resources;
- parallel writers;
- tasks that need separate worktrees;
- verification required before closeout;
- acceptable storage and context budgets.

Use the complete staged prompts in `pas/references/intake-questions.md` when more detail is needed.

## Produce a Design Contract before writing

Present a compact Design Contract containing:

1. objective and non-goals;
2. target root and privacy classification;
3. runtime, provider, switchboard, and adapter evidence level;
4. proposed agents and their ownership boundaries;
5. shared methods versus private context;
6. folder and file responsibilities;
7. task lifecycle and authoritative state;
8. memory, knowledge, and large-file budgets;
9. tools, connectors, permissions, and approval gates;
10. completion, failure, and handoff conditions;
11. concurrency model, resources, locks, and worktrees;
12. validation plan and named deliverables.

Show the proposed tree and the files to be created or changed. Obtain approval before writing an existing system unless the user already authorised that exact implementation.

## Choose the smallest sufficient topology

Use these tests:

- Create a **domain agent** when work recurs, owns distinct private context, needs stable rules, or produces a distinct class of outputs.
- Create a **skill** when the difference is a repeatable procedure that can be reused by one or more agents.
- Create a **task/project** when the work is temporary and does not justify persistent identity.
- Create a **knowledge collection** when the material is stable reference content requiring retrieval.
- Add a **connector/tool** when current external data or actions are required.
- Add a **subagent** when a bounded independent workstream benefits from separate context or tool restrictions.
- Add a **central manager model** only when multiple agents genuinely need routing, dependency management, or cross-workstream synthesis.

Prefer one agent with several skills over many overlapping agents. Split only where ownership, privacy, lifecycle, or permissions materially differ.

## Design descriptions before agent folders

Treat every agent, skill, and subagent description as executable routing infrastructure.

For each agent description include:

- what the agent owns;
- when to use it;
- representative inputs and outputs;
- exclusions and escalation boundaries;
- freshness or evidence requirements;
- collision rules with adjacent agents.

Require at least:

- two positive routing prompts;
- two negative routing prompts;
- collision prompts for overlapping domains;
- a human-readable exclusion list.

Reject promotional descriptions such as “helps with research”. Write behavioral descriptions such as “Use when a request requires evidence collection, source comparison, and uncertainty tracking; not for final visual packaging or external publication.”

Read `pas/references/description-routing-evals.md`. Run `check_descriptions.py` after generation.

## Apply the filesystem contract

Use one purpose per durable location:

| Location | Purpose | Default loading policy |
|---|---|---|
| `AGENTS.md` / runtime entrypoint | Compact always-on operating contract | automatically discovered by that runtime only |
| `IDENTITY.md` | Mission, audience, ownership, routing boundary | load during domain entry |
| `RULES.md` | Stable behavioral and safety rules | load for substantive work |
| `SYSTEM_MAP.md` | Stable registry and ownership topology | load for routing or architecture work |
| `task.yaml` | Authoritative task contract and lifecycle | load for that task |
| `STATUS.md` | Generated cross-task view | regenerate; never hand-edit |
| `MEMORY.md` | Bounded handover and recovery index | load only when continuity is needed |
| `knowledge/` | Stable long-term archive/library | retrieve named items only |
| `skills/` | Reusable procedures and capability packages | discover metadata, load full skill on trigger |
| `raw_data/` | Original inputs | never recursively auto-load |
| `workspace/` | Current desk, drafts, and active reasoning artifacts | load named current files |
| `artifacts/` | Generated intermediates, caches, calculations | summary-only by default |
| `logs/` | Execution traces | rotate and summarise; never full-context by default |
| `outputs/` | Reviewed deliverables | load named output only |
| `archive/` | Closed or superseded material | retrieval only |

Read `pas/references/filesystem-contract.md` for ownership and movement rules.

## Bound context and storage

Use hard limits, not prose reminders:

- root `AGENTS.md`: portable target at or below 24 KiB and 400 lines;
- runtime delta files: at or below 4 KiB and 100 lines;
- root `MEMORY.md`: at or below 12 KiB and 120 lines;
- domain `MEMORY.md`: target at or below 8 KiB and 100 lines;
- `task.yaml`: at or below 32 KiB and 800 lines;
- files at or above 256 KiB in `raw_data/`, `artifacts/`, `logs/`, or `outputs/`: require a local manifest entry with relative path, exact `size_bytes`, context policy, and short summary.

Use these default context policies:

- `raw_data`: `never-auto-load`;
- `artifacts`: `summary-only`;
- `logs`: `summary-only`;
- `outputs`: `named-only`.

When a memory file reaches 80% of budget, compact it. Move stable background into `knowledge/`, task-specific state into `task.yaml` or workspace, and closed detail into archive. Keep pointers, decisions, and recovery-critical facts in memory. Do not preserve transcripts.

## Use task contracts as the source of operational truth

Create a task manifest for cross-session, multi-file, high-risk, concurrent, or formally deliverable work. Require:

- unique task ID and owner root;
- objective, scope, inputs, and outputs;
- allowed reads, writes, tools, and prohibited actions;
- completion and failure conditions;
- verification commands and receipts;
- status and verification state;
- writer, `parallel_write`, worktree, and resources;
- handoff summary and next action.

Generate `STATUS.md` from manifests. Never maintain status independently in both chat and a handwritten dashboard.

Use the lifecycle:

`proposed → active/in_progress → waiting_review or blocked → complete/failed/cancelled`

Successful completion requires declared outputs, satisfied criteria, `verification_state: passed`, receipts, current generated status, released task locks, budget compliance, and handoff. Failed or cancelled closeout requires an honest reason and handoff, not fake “passed” verification.

## Make completion gates mechanical

Do not rely on the user or model to remember status, memory, or handoff updates.

1. Update the task manifest.
2. Generate `STATUS.md`.
3. Run validation and budget checks.
4. Verify declared outputs and receipts.
5. Release task-owned locks.
6. Write the handoff summary.
7. Run `closeout_gate.py`.
8. Translate failure into the selected runtime's blocking protocol.

The generator provides protocol translators for Codex `Stop`, Claude Code `Stop`, and Gemini CLI `AfterAgent`. A raw validator exit code is not a runtime adapter. Treat other completion integrations as advisory until product-specific blocking behavior is implemented and exercised.

Do not require a memory edit on every task. Require memory only when a stable decision, durable preference, or recovery pointer is genuinely worth preserving.

## Coordinate concurrent work

Use a single writer for each authoritative path.

- Declare resources in `task.yaml` before acquiring locks.
- Acquire a lock with task ID, session ID, writer, worktree, mode, and TTL.
- Renew the heartbeat during long work.
- Release the lock before successful closeout.
- Reject undeclared resources, wrong writers, wrong sessions, or worktree mismatches.
- Use separate Git worktrees for parallel write-heavy branches.
- Use locks for shared non-Git resources, generated registries, databases, devices, ports, or authority files.
- Do not use a worktree as a substitute for privacy or external-action approval.

## Classify adapters honestly

Read `pas/compatibility/runtime-compatibility.json`, then exactly one relevant file in `pas/adapters/`.

Keep these categories separate:

- `native_runtime`: documented local entrypoint and runtime semantics;
- `workspace_agent`: instructions/uploads/projects require a manual projection;
- `provisional`: product exists but critical native semantics remain unproved;
- `switchboard`: provider/model/config routing only;
- `provider`: inference backend only;
- `custom_harness`: caller owns context assembly, tools, state, and gates.

Do not claim native support because an adapter Markdown file exists. Verify discovery, projection, enforcement, persistence, and evidence separately.

Use evidence labels:

1. `documented` — current official documentation reviewed and dated;
2. `verified_static` — files, schemas, budgets, and fixtures pass;
3. `verified_runtime` — a clean runtime loads the intended entrypoint;
4. `gate_verified` — invalid closeout blocks and valid closeout passes;
5. `concurrency_verified` — contention and stale recovery pass;
6. `external_verified` — deployment, message, provider response, or other external result is independently confirmed.

Never merge these labels into “works”.

## Build a new harness

Resolve the directory containing this `SKILL.md` as the skill root.

1. Copy `pas/examples/starter-config.json` to a user-owned working file.
2. Replace domains, descriptions, exclusions, and routing examples.
3. Dry-run the generator.
4. Show the target tree and file count.
5. Generate only after target approval.
6. Review generated hooks before trusting them.
7. Run all static validators.
8. Run clean-runtime fixtures for every support claim.

```bash
python3 scripts/create_agentic_system.py --root /path/to/system --config /path/to/config.json --dry-run
python3 scripts/create_agentic_system.py --root /path/to/system --config /path/to/config.json
```

The generator refuses to overwrite existing files unless `--force` is explicitly supplied. Do not use force without resolving exact collisions and preserving user work.

## Audit an existing harness

Inspect before recommending changes:

1. enumerate first- and second-level structure without opening private payloads;
2. identify actual runtime entrypoints and instruction precedence;
3. find fake imports, duplicated authorities, and oversized startup context;
4. map agents, descriptions, exclusions, and routing collisions;
5. trace task state, status generation, closeout, and receipts;
6. inspect memory budgets and knowledge retrieval boundaries;
7. inspect large-file manifests and loading policies;
8. inspect tools, connectors, permissions, and external-action gates;
9. inspect locks, writers, sessions, resources, and worktrees;
10. run validators and record exact evidence level.

Score architecture, entrypoints, routing, state, context, data lifecycle, enforcement, concurrency, security, and recoverability separately. Label unavailable evidence `partial`; do not fill gaps with model confidence.

## Run the built-in checks

```bash
python3 scripts/validate_agentic_system.py /path/to/system
python3 scripts/check_budgets.py /path/to/system
python3 scripts/check_descriptions.py /path/to/system
python3 scripts/generate_status.py /path/to/system --check
python3 scripts/harness_health_check.py /path/to/system --json
python3 scripts/adapter_smoke.py /path/to/system --runtime codex
python3 scripts/adapter_smoke.py /path/to/system --runtime claude-code
python3 scripts/adapter_smoke.py /path/to/system --runtime gemini-cli
```

For a terminal task:

```bash
python3 scripts/closeout_gate.py /path/to/system tasks/T-123/task.yaml
```

For a multi-task runtime session:

```bash
python3 scripts/bind_task.py /path/to/system tasks/T-123/task.yaml --session <runtime-session-id>
```

Read each script's `--help` before integrating it into automation.

## Validate changes at the right level

Use the smallest sufficient ladder:

- syntax and schema;
- deterministic unit and fixture tests;
- generated-system validation;
- static adapter inspection;
- clean-session entrypoint recall;
- invalid/valid completion-gate fixture;
- concurrent lock/worktree fixture;
- rendered document or diagram inspection;
- external readback when an external action was authorised.

Save receipts outside compact memory. Put only a pointer and the stable conclusion in memory.

## Reject common anti-patterns

- A model diagram with no visible replaceable model slot.
- A “harness layer” that excludes rules, files, adapters, or gates.
- Calling every model a manager.
- Treating knowledge and memory as synonyms.
- One giant `MEMORY.md` containing logs, tasks, sources, and history.
- Recursively loading `raw_data/`, `knowledge/`, `logs/`, or `archive/`.
- Maintaining `STATUS.md` by hand.
- Declaring completion without receipts or current generated status.
- Copying one hook command across runtimes without protocol translation.
- Claiming support from an adapter shell or configuration file alone.
- Creating agents before writing routing descriptions and collision tests.
- Parallel edits to the same authoritative path without worktree or lock discipline.
- Treating folder visibility as data authority.
- Treating a model switchboard as the durable harness.
- Putting secrets or private examples into public templates.

## Report completion precisely

Lead with the outcome. Include:

- what was built, audited, or explained;
- exact artifact paths;
- architecture and ownership decisions;
- checks run and receipts produced;
- evidence level per runtime adapter;
- unresolved, provisional, or unverified items;
- whether any external action occurred;
- the next smallest useful action.

Do not say “complete” if the applicable gate has not passed.

## Reference index

- `pas/references/mental-model.md` — core concepts and company metaphor.
- `pas/references/intake-questions.md` — staged design questionnaire.
- `pas/references/filesystem-contract.md` — file roles, ownership, and loading policy.
- `pas/references/privacy-boundaries.md` — public/private and authority boundaries.
- `pas/references/description-routing-evals.md` — agent/skill/subagent description design and tests.
- `pas/references/adapters.md` — adapter selection and verification ladder.
- `pas/compatibility/runtime-compatibility.json` — machine-readable product classification.
- `pas/references/skill-matrix.md` — reusable capability topology.
- `pas/references/cross-agent-skill-borrowing.md` — method borrowing without context leakage.
- `pas/references/skill-distillation-and-fusion.md` — convert repeated methods into skills.
- `pas/references/system-review-and-renewal.md` — compaction, archive, and renewal.
- `pas/references/troubleshooting.md` — failure diagnosis.
- `pas/references/facilitation-script.md` — guided workshop flow.
- `pas/references/master-build-playbook.md` — standalone long-form textbook/workbook.
- `pas/references/friend-starter-prompt.md` — short prompt that activates this workflow.
