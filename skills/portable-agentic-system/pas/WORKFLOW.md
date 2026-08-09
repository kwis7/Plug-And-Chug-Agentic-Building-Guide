# Harness Builder Workflow

Use `Route -> Discover -> Contract -> Design -> Build -> Verify -> Persist`.

## 1. Route

- Decide whether the request is explanation, new build, audit, migration, runtime adaptation, skill design, or system renewal.
- Identify the owning domain and whether the work belongs to a control center, domain agent, temporary task, or reusable skill.
- Reject unnecessary agent proliferation.

## 2. Discover

- For a new build, use the staged questionnaire.
- For an existing system, inspect actual entrypoints, rules, maps, task files, skills, scripts, outputs, tests, runtime versions, and Git state.
- Separate current official runtime facts from old notes and provider marketing.
- Identify sensitive data and external-action boundaries before loading sources.

## 3. Contract

Record objective, included/excluded scope, owner, inputs, allowed reads/writes/tools, prohibited actions, outputs, completion criteria, failure conditions, verification, resources, and handoff.

Use a task manifest for multi-step, multi-file, cross-session, high-risk, or formally delivered work. Skip it for a truly trivial explanation or edit.

## 4. Design

- Draw the harness boundary around all configured architecture.
- Single out the active replaceable model.
- Create new domain agents only for durable ownership boundaries.
- Separate runtime from provider and switchboard.
- Define memory, knowledge, workspace, raw data, artifacts, logs, outputs, and archive.
- Set budgets and consolidation rules.
- Define completion gate and verification receipts.
- Define one-writer, lock, and worktree rules.
- Draft skill/subagent descriptions and routing evaluations.

Present the proposed tree, adapter status, and authority boundaries before writing an existing user system.

## 5. Build

- Generate from canonical templates.
- Preserve existing files unless overwrite is explicitly approved.
- Use native runtime entrypoints and valid bridge syntax.
- Generate status from task manifests.
- Keep memory compact and long details in knowledge or archive files.
- Put runtime-specific deltas in runtime-specific files.

## 6. Verify

Run in increasing evidence order:

1. file/schema/path/privacy checks;
2. budget checks;
3. generated status check;
4. static adapter smoke;
5. fresh-session runtime smoke;
6. invalid and valid completion-gate smoke;
7. lock/worktree contention smoke;
8. output rendering or behaviour checks;
9. external delivery/readback only when authorised.

Label unrun levels explicitly.

## 7. Persist

- Update task state and regenerate `STATUS.md`.
- Store receipts outside the task body and link them.
- Add only durable recovery pointers to `MEMORY.md`.
- Distil stable background into `knowledge/`.
- Promote repeated procedures into skills after validation.
- Release or transfer locks and write a handoff.

## Mode notes

### `pas-start`

Explain the company metaphor, ask the staged questionnaire, design the smallest system, request location approval, scaffold, and verify.

### `pas-audit`

Read actual files, reproduce failures, compare claims with native runtime semantics, and report static versus runtime verification separately. Do not repair unless authorised.

### `pas-adapt`

Classify the product first. Read the compatibility manifest and one matching adapter. Generate a native bridge only where official semantics support it.

### `pas-create-skill`

Define repeated job, triggers, exclusions, inputs, outputs, tools, permission boundary, and positive/negative/collision evaluations. Keep `SKILL.md` concise and move long details to references.

### `pas-review`

Review tasks, generated status, receipts, memory size, knowledge candidates, skill reuse, logs, outputs, stale locks, runtime evidence, and archived material. Fix root causes in one authority rather than adding duplicate rules.

### `pas-explain`

Use the company metaphor. State explicitly that all configuration belongs to the harness and the model is the active replaceable employee. Call only the central coordinator a manager in a multi-agent system.
