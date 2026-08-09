# Build Workbook: From Interview to Verified Harness

## 1. How to use this workbook

Work in stages. At each stage, capture the answer, offer a minimal default, and identify decisions that must be made by the user. Do not create files until the Design Contract and target root are approved.

The workbook supports four paths:

- build a new harness;
- audit and harden an existing harness;
- migrate between runtimes;
- teach another person how the system works.

## 2. Stage A — problem and outcome

Ask:

1. What recurring work should the system make easier?
2. What currently gets forgotten, mixed up, repeated, or completed unreliably?
3. What deliverables should appear at the end?
4. Who reads those deliverables?
5. Which errors are merely annoying, and which are costly or dangerous?
6. What would count as success after one month?
7. What is explicitly outside scope?

Produce:

- one-sentence objective;
- three to seven success criteria;
- non-goals;
- risk level;
- suggested topology level: minimal, standard, or advanced.

## 3. Stage B — execution stack

Ask separately:

- Which application runs the agent: Codex, Claude Code, Gemini CLI, OpenClaw, Hermes, MiMo Code, a workspace product, or custom code?
- Which provider and model are active?
- Is a switchboard changing providers or configurations?
- Which machines and operating systems must work?
- Does the runtime support project files, skills, hooks, sandboxes, worktrees, or subagents?
- Which claims have been observed in a clean session rather than inferred from documentation?

Produce a stack card:

```text
Runtime:
Provider/model:
Switchboard:
Native entrypoint:
Skill locations:
Generated hook/policy:
Filesystem boundary:
Fresh-session evidence:
Gate evidence:
Known limitations:
Last reviewed:
```

## 4. Stage C — domain inventory

For each recurring domain, complete:

```text
Domain name:
Mission:
Use when:
Do not use when:
Private inputs:
Authoritative sources:
Reviewed outputs:
Reusable methods:
Tools/connectors:
Approval boundaries:
Freshness requirements:
Nearest routing collision:
```

Then decide:

- persistent domain agent;
- skill inside an existing agent;
- temporary task/project;
- knowledge collection;
- connector/tool;
- no new structure.

Require a reason for every persistent agent.

## 5. Stage D — routing evaluations

Write at least two prompts for each category:

- should route;
- should not route;
- might collide with an adjacent agent;
- mixed request that should split;
- authority-boundary request that should escalate.

Create expected results before testing. Preserve observed runtime/model version and date. Rewrite descriptions until the failures are understandable; do not hide collision tests.

## 6. Stage E — information architecture

Classify every existing or proposed file:

| Question | If yes | Home |
|---|---|---|
| Must apply to almost every task? | stable operating rule | entrypoint or rules |
| Defines mission/ownership? | stable identity | identity |
| Describes current task? | dynamic state | task manifest |
| Helps resume across sessions? | compact pointer/decision | memory |
| Is stable reference material? | long-term retrieval | knowledge |
| Is a repeatable procedure? | capability package | skill |
| Is an untouched input? | original data | raw data |
| Is a current draft? | working surface | workspace |
| Is generated but not reviewed? | intermediate | artifact |
| Is an execution trace? | operational record | log |
| Is reviewed and deliverable? | formal artifact | output |
| Is closed or superseded? | retained history | archive |

Identify files that currently serve more than one purpose. Propose a minimal migration with pointers and backups.

## 7. Stage F — task and completion design

Design the task schema:

```yaml
schema_version: 2
id: T-123
owner: research-agent
owner_root: research-Agent
status: active
objective: Produce a source-backed comparison.
scope:
  included: [named question]
  excluded: [external publication]
inputs: [raw_data/source-index.json]
authority:
  allowed_reads: [research-Agent]
  allowed_writes: [research-Agent/workspace, research-Agent/outputs]
  allowed_tools: [search, local analysis]
  prohibited_actions: [send, publish, use credentials]
outputs: [outputs/comparison.md]
completion_criteria:
  - material claims have sources
  - uncertainty is visible
failure_conditions:
  - authoritative source unavailable
verification:
  commands: [named validator]
  receipts: []
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

Decide which fields are required, which statuses are allowed, and which terminal states require success receipts. Generate status from these manifests.

## 8. Stage G — context budgets

Choose hard limits:

```text
Root entrypoint bytes/lines:
Runtime delta bytes/lines:
Root memory bytes/lines:
Domain memory bytes/lines:
Task manifest bytes/lines:
Large-file threshold:
Raw-data loading policy:
Artifact/log loading policy:
Output loading policy:
Compaction trigger:
```

Define an owner for compaction and a test that fails when the limit is exceeded.

## 9. Stage H — tools, connectors, and authority

For each tool or connector, record:

```text
Capability:
Justification:
Read objects:
Write objects:
Credential location outside repo:
Network destinations:
Cost/rate limit:
Human approval point:
Dry-run or shadow mode:
Independent readback:
Disable/revoke procedure:
```

Reject a connector that has no repeated need, no bounded scope, or no recovery path.

## 10. Stage I — concurrency

List shared resources:

- authority files;
- generated indexes;
- databases;
- ports/services;
- browser profiles;
- external accounts;
- branches and worktrees;
- expensive or rate-limited connectors.

For each, choose:

- single writer only;
- atomic TTL lock;
- separate worktree;
- queue;
- human scheduling;
- no parallel access.

Record resource names in task contracts before use.

## 11. Stage J — Design Contract template

```markdown
# Agent Harness Design Contract

## Objective

## Non-goals

## Target root and privacy class

## Runtime stack and evidence levels

## Proposed agent registry

| Agent | Use when | Exclusions | Private owner data | Outputs |
|---|---|---|---|---|

## Shared capabilities

## File and data lifecycle

## Task/status authority

## Memory and context budgets

## Completion/failure gates

## Connectors and approval boundaries

## Concurrency, locks, and worktrees

## Files to create or change

## Validation and receipts

## Provisional or unverified items
```

Obtain approval for the exact target and change scope.

## 12. Scaffold implementation order

1. Preserve existing Git and user changes.
2. Create runtime-native root entrypoints.
3. Create identity, rules, system map, and compact memory templates.
4. Create task schema and generated status.
5. Create data-lifecycle directories and manifests.
6. Add agent folders only for approved persistent domains.
7. Add routing descriptions and eval fixtures.
8. Add deterministic validators.
9. Add runtime-specific hook translators where supported.
10. Add locks/worktree rules.
11. Validate static structure.
12. Run fresh-session fixtures.
13. Document evidence levels and limitations.

Do not install connectors, migrate private data, or publish the repository as part of scaffolding unless separately authorised.

## 13. Adapter implementation worksheet

For the selected runtime, answer:

```text
Official documentation URL and review date:
Native project entrypoint:
Hierarchy/precedence:
Supported import syntax:
Skill discovery locations:
Subagent description semantics:
Hook or policy configuration path:
Final-response/Stop event:
Blocking output schema:
Working directory and path resolution:
Project trust or permission requirement:
Sandbox/file access semantics:
Worktree behavior:
Static fixture result:
Fresh-session result:
Invalid closeout result:
Valid closeout result:
Limitations:
```

If no native semantics are documented, label the result a manual projection or provisional profile. Do not invent compatibility.

## 14. Audit path for an existing repository

### Pass 1 — structure without payload exposure

- list first- and second-level names;
- inspect Git status;
- identify entrypoints, schemas, scripts, tests, and docs;
- avoid opening private raw data, logs, memory, and outputs unless required.

### Pass 2 — authority and loading

- trace actual runtime discovery;
- find unsupported import syntax;
- find duplicate or conflicting policies;
- measure instruction chain and memory sizes;
- identify files assumed to auto-load but not actually discovered.

### Pass 3 — state and closeout

- inspect task schema and state transitions;
- determine whether status is generated;
- inspect successful and unsuccessful terminal logic;
- inspect receipts and handoff;
- inspect runtime hook translation.

### Pass 4 — data lifecycle

- classify raw data, workspace, artifacts, logs, outputs, and archive;
- locate large files and manifests;
- identify recursive-loading instructions;
- trace private-data ownership and cross-agent copying.

### Pass 5 — routing and capabilities

- review every agent/skill/subagent description;
- run positive, negative, and collision cases;
- distinguish provider, runtime, switchboard, and connector;
- identify unused or overly broad tools.

### Pass 6 — concurrency and recovery

- inspect writers, locks, TTLs, heartbeats, resources, branches, and worktrees;
- simulate stale status, missing receipt, lock contention, and interrupted work;
- verify clean-session recovery.

### Pass 7 — public-safety review

- scan absolute local paths, secrets, identities, account data, client/student data, raw private text, and logs;
- replace with generic structural examples;
- check links, license, attribution, and generated downloads.

## 15. Validation command set

From the source repository:

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /path/to/fixture \
  --config skills/portable-agentic-system/pas/examples/starter-config.json

python3 skills/portable-agentic-system/scripts/validate_agentic_system.py /path/to/fixture
python3 skills/portable-agentic-system/scripts/check_budgets.py /path/to/fixture
python3 skills/portable-agentic-system/scripts/check_descriptions.py /path/to/fixture
python3 skills/portable-agentic-system/scripts/generate_status.py /path/to/fixture --check
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/fixture --runtime codex
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/fixture --runtime claude-code
python3 skills/portable-agentic-system/scripts/adapter_smoke.py /path/to/fixture --runtime gemini-cli
```

Then run repository unit tests, skill frontmatter validation, JSON validation, `git diff --check`, privacy scans, and document rendering.

## 16. Runtime smoke protocol

For each installed runtime:

1. create a disposable fixture;
2. record runtime version and date;
3. start a clean session at the intended root;
4. ask the runtime to identify the active entrypoint, first three rules, active task ID, and prohibited actions;
5. inspect runtime-native context or debug commands where available;
6. create an invalid terminal task or completion claim;
7. confirm the runtime blocks or retries with the gate reason;
8. repair outputs, receipts, status, locks, budgets, and handoff;
9. confirm valid closeout is accepted;
10. preserve the transcript/debug receipt and label limitations.

Do not upgrade `verified_static` to `verified_runtime` without this receipt.

## 17. Concurrency fixture

Test:

1. undeclared resource acquisition fails;
2. declared resource acquisition succeeds atomically;
3. second session is blocked;
4. wrong session cannot renew or release;
5. correct owner can renew heartbeat;
6. task closeout fails while its lock remains;
7. correct release succeeds;
8. parallel write requires a declared worktree;
9. stale recovery is documented.

## 18. Large-file fixture

1. Create a synthetic file just above the threshold.
2. Confirm budget validation fails without a manifest entry.
3. Add relative path, exact size, correct policy, and summary.
4. Confirm validation passes.
5. Change the file size.
6. Confirm the stale manifest fails.
7. Verify no test reads the file content into model context.

## 19. Documentation and diagram review

The concept diagram should show:

- board/user;
- visible replaceable active model;
- every configured component inside the harness boundary;
- manager label only for multi-agent control;
- memory, knowledge, skill, and context as distinct;
- gates, budgets, locks, worktrees, adapters, and outputs.

The anonymous example system map should show:

- a control center;
- several functional domain agents;
- a replaceable model inside each active agent;
- common internal anatomy;
- ownership and privacy boundaries;
- method sharing without raw-data sharing;
- request-to-output flow;
- a legend for control, evidence, retrieval, and prohibited crossings.

Keep both diagrams. One teaches the concept; the other demonstrates a system.

For the PDF:

- make the main body a textbook, not an adapter catalogue;
- place adapter details in a compact appendix;
- include both diagrams near the beginning;
- render every page;
- inspect contact sheets and representative full-resolution pages;
- check clipped text, blank pages, broken tables, unreadable code, and incorrect page references;
- verify final page count and metadata.

## 20. Maintenance calendar

### Per task

- task/status/receipt closeout;
- release locks;
- archive or clean workspace;
- add memory only for durable recovery value.

### Monthly

- budget and large-file check;
- active/stale task review;
- routing collisions;
- connector scope;
- broken links and generated files.

### Quarterly

- runtime official-doc refresh;
- clean-session adapter smoke;
- memory compaction;
- skill duplication review;
- privacy/public-output scan;
- recovery drill.

### On model/runtime change

- rerun routing evaluations;
- verify entrypoint discovery;
- verify hook protocol;
- verify context budgets;
- compare output and tool behavior;
- keep the old evidence label until new receipts pass.

## 21. Handoff package

Provide:

- approved Design Contract;
- final system tree;
- agent registry and routing evals;
- compatibility manifest;
- generated task/status/gate scripts;
- validation report and receipts;
- diagrams;
- core skill plus references;
- textbook PDF;
- unresolved/provisional items;
- explicit statement of external actions not taken.

## 22. Minimal starter prompt

```text
Use the portable-agentic-system skill to help me design or audit my personal agent harness. Start by identifying the runtime, provider, recurring work domains, private-data boundaries, desired outputs, and approval-gated actions. Explain the model as the active replaceable employee and reserve “manager” for a central model in a true multi-agent system. Distinguish memory, knowledge, task state, workspace, skills, raw data, artifacts, logs, and reviewed outputs. Propose the smallest useful architecture, routing descriptions with positive/negative/collision tests, hard context budgets, generated status, completion gates, resource locks/worktrees, and adapter evidence levels. Show me the Design Contract and exact file plan before writing an existing system. Never expose private data or claim runtime support without current official documentation and a dated smoke receipt.
```
