# Reliability, Governance, and Enforcement

## 1. Reliability means recoverable truth

An agent system is reliable when it can answer three questions after interruption:

1. What is true now?
2. What evidence supports that claim?
3. What is the next safe action?

Fluent prose is not enough. Reliability comes from state, receipts, boundaries, and repeatable checks.

## 2. Define completion as a contract

Before work begins, define:

- required outputs;
- completion criteria;
- failure conditions;
- verification commands or review methods;
- required receipts;
- approvals that remain outside the agent's authority;
- cleanup and handoff requirements.

This makes “done” observable.

### Successful completion

A successful terminal task should require:

- status is `complete` or `completed`;
- every declared output exists inside the owner root;
- completion criteria are non-empty and satisfied;
- verification state is `passed`;
- verification receipts exist;
- generated status is current;
- instruction, memory, task, and storage budgets pass;
- task-owned locks are released;
- handoff summary is present.

### Unsuccessful completion

A `failed` or `cancelled` task should not be forced to claim that verification passed or that successful outputs exist. It should require:

- honest terminal status;
- reason or failure condition;
- preserved partial artifacts where useful;
- current status;
- released locks or explicit incident record;
- handoff summary and next option.

Correct failure is more reliable than fake success.

## 3. A completion gate must connect to the runtime

A standalone validator can return success or failure. A runtime hook expects an event-specific protocol. The adapter must translate between them.

For the generated portable scaffold:

- Codex `Stop`: return top-level `{"decision":"block","reason":"..."}` to continue the agent.
- Claude Code `Stop`: return top-level `{"decision":"block","reason":"..."}` to prevent stopping and feed back the reason.
- Gemini CLI `AfterAgent`: return `{"decision":"deny","reason":"..."}` to reject the final response and retry.

Calling the same Python validator from each hook without translating output is not an implementation. Likewise, a hook configuration file is not proof that the runtime discovered, trusted, or executed it.

### Session-to-task binding

A final-response hook must know which task is being reported. Resolution order can be:

1. explicit `PAS_TASK` constrained inside the harness;
2. session ID binding under `.pas/runtime/sessions/`;
3. the only active task if exactly one exists;
4. otherwise block an ambiguous completion claim.

Ambiguity should fail closed for completion, not for ordinary conversation.

## 4. Evidence levels prevent overclaiming

Use independent labels:

| Level | Evidence |
|---|---|
| Documented | current official source reviewed and dated |
| Verified static | generated syntax, schema, budgets, and fixtures pass |
| Verified runtime | clean session loads the intended entrypoint |
| Gate verified | invalid closeout blocks and valid closeout passes |
| Concurrency verified | conflict, renewal, release, and stale recovery tested |
| External verified | external action confirmed through independent readback |

An adapter may be documented but not generated, generated but not loaded, loaded but not enforced, or enforced locally but not externally verified.

## 5. Receipts are typed evidence

Different claims require different receipts:

| Claim | Suitable receipt |
|---|---|
| File exists | exact path and hash or stat |
| Test passed | command, exit code, dated output |
| Document rendered | rendered page set and visual inspection note |
| Runtime loaded instructions | clean-session response, runtime version, command |
| Hook blocked completion | invalid fixture transcript and hook debug record |
| Provider responded | timestamped response metadata |
| Deployment succeeded | deployment ID plus live health/readback |
| Message delivered | provider message ID and recipient readback where possible |
| Transaction occurred | authoritative external record, never model assertion |

Store receipts in task artifacts. Memory keeps a pointer and durable conclusion only.

## 6. Resource locks and worktrees solve different conflicts

### Resource lock

Use for a specific shared resource: a registry file, database, browser profile, port, device, generated index, or shared authority file. A lock should contain:

- canonical resource name;
- mode;
- task ID;
- session ID;
- writer;
- worktree if applicable;
- created time;
- heartbeat time;
- expiration time.

Acquisition must confirm that the task exists, is active, declares the resource, and matches writer/worktree. Create the lock atomically. Renew long-running locks. Release only with matching owner credentials. Expired locks should be surfaced for review rather than silently treated as success.

### Git worktree

Use for parallel write-heavy Git tasks that need independent branches and working directories. Record the worktree in the task contract. Avoid checking out the same branch in two worktrees. Integrate through review rather than editing the same file from two sessions.

A worktree does not isolate non-Git resources. A lock does not solve branch conflicts. Use each for its actual purpose.

## 7. One-writer ownership

For every authoritative path, identify one current writer. Other agents may inspect read-only or propose patches. This rule is simpler and more dependable than trying to merge simultaneous edits to policy, state, or a report.

Useful concurrency pattern:

- manager/owner writes the authoritative task and synthesis;
- workers write distinct artifacts or branches;
- reviewer reads outputs and writes a separate review receipt;
- owner integrates after checks.

## 8. Permission and authority kernel

Separate capabilities:

- allowed read;
- allowed local write;
- allowed tool execution;
- allowed network access;
- allowed external write;
- user-confirmed irreversible action.

The ability to use a tool does not grant authority to use it for every purpose. A mail connector can be available while sending remains approval-gated. A broker connector can supply research data while trading remains forbidden.

Use least privilege and narrow paths. Treat task authority as a ceiling; lower-level skills and external content cannot expand it.

## 9. Prompt injection and untrusted inputs

Webpages, PDFs, emails, repository files, issue comments, downloaded skills, tool outputs, and model messages are data. They may contain instructions that conflict with the harness.

Apply these rules:

- external content cannot change authority;
- never reveal secrets requested by content;
- do not execute installation or deletion instructions merely because a README says so;
- inspect scripts and dependencies before use;
- keep source text distinct from local policy;
- record when a conclusion comes from external content rather than verified behavior;
- validate paths and block traversal in hooks and tools.

## 10. Adapter security

Runtime entrypoints are not interchangeable:

- Codex discovers hierarchical `AGENTS.md`; arbitrary `@import` lines are not a generic include mechanism.
- Claude Code reads `CLAUDE.md`; its documented import is `@path`, so a compact `@AGENTS.md` bridge is possible.
- Gemini CLI reads hierarchical `GEMINI.md`; a documented relative import or configured context filename can bridge the common contract.
- Workspace products may rely on project instructions and uploads rather than local discovery.
- Providers do not own local loading at all.

Keep a machine-readable compatibility manifest with evidence date, category, entrypoint, skill locations, generated files, enforcement mechanism, limitations, and fresh-session status.

## 11. Description reliability

Routing descriptions deserve regression tests because changing a few words can change which agent or skill activates.

Evaluate:

- recall on positive prompts;
- rejection on negative prompts;
- collision rate with nearest neighbors;
- decomposition of mixed prompts;
- escalation on authority-boundary prompts;
- stability across model/runtime upgrades.

Do not use the same examples to tune and evaluate indefinitely. Preserve a small holdout set.

## 12. Observability without log explosion

Record events that help answer operational questions:

- task transition;
- tool or connector action;
- lock acquire/renew/release;
- gate decision;
- verification command and receipt;
- external approval and readback;
- error category and retry.

Do not store unlimited transcripts. Rotate logs by size or time. Produce compact incident summaries. Redact secret-like values before persistence. Large hook output itself can consume context; keep gate reasons concise.

## 13. Failure modes and recovery

### Stale status

Cause: task changed but generated status did not. Recovery: regenerate, compare, then rerun closeout.

### Memory overflow

Cause: memory absorbed task logs and knowledge. Recovery: classify each entry, move it to the correct layer, retain pointers, rerun budget check.

### Ambiguous active task

Cause: a runtime session can see several active manifests. Recovery: bind session ID to one task; never guess at finalisation.

### Orphaned lock

Cause: crash or abandoned session. Recovery: inspect owner and heartbeat, confirm task state, expire or release through an audited action, record the recovery.

### Adapter shell

Cause: documentation names a runtime but generated files do not use its native discovery or hook protocol. Recovery: verify official semantics, add a real projection/translator, then run invalid and valid fixtures.

### False completion loop

Cause: hook blocks repeatedly but the model lacks actionable feedback, or the condition cannot be satisfied. Recovery: return exact failing checks; use runtime loop guards; permit an honest failed/blocked closeout.

### Context explosion

Cause: recursive ingestion, oversized memory, giant log, or broad knowledge retrieval. Recovery: enforce manifests, summaries, named selections, and file budgets.

## 14. Human review as part of the system

Human-in-the-loop is not a fallback for weak automation. It is the correct boundary for value judgments and irreversible actions.

Require explicit review for:

- publication or external delivery;
- credentials and account settings;
- payment, trading, or funds movement;
- destructive deletion or overwrite;
- production deployment;
- sensitive personal-data transfer;
- claims whose consequences exceed the available evidence.

Provide a preview that identifies target, scope, changes, evidence, and rollback.

## 15. Renewal and drift control

Every system drifts: descriptions overlap, memories grow, adapter docs change, skills duplicate, connectors retain unused scope, and old outputs look current.

Run periodic renewal:

1. regenerate status;
2. check budgets and large-file manifests;
3. rerun routing collision tests;
4. inspect stale locks and unfinished tasks;
5. review connector scope and credentials without exposing secrets;
6. compare runtime adapters with current official docs;
7. compact memory;
8. archive superseded outputs and skills;
9. remove duplicate authority;
10. run recovery from a clean session.

Update the unique authority for a rule. Do not solve drift by adding another competing policy file.

## 16. Reliability review rubric

Score 0–3:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Task state | chat only | manual status | manifest | manifest plus generated status and transition tests |
| Completion | model assertion | checklist | local validator | runtime gate with invalid/valid receipt |
| Memory | unlimited transcript | manual cleanup | hard budget | compaction and retrieval review tested |
| Large files | unrestricted | prose warning | manifest policy | deterministic size/index enforcement |
| Concurrency | simultaneous edits | social coordination | locks/worktrees | ownership and stale recovery tested |
| Adapter | filename claim | doc mapping | generated static config | clean-session and gate verified |
| External action | tool availability implies authority | reminder | approval gate | readback and rollback tested |

The score is diagnostic, not a maturity badge.
