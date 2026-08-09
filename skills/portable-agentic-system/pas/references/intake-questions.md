# Staged Harness Questionnaire

Ask one stage at a time. Summarise decisions and unresolved questions after each stage. Do not dump the whole questionnaire on a new user.

## A. Outcomes and recurring domains

1. What 2-5 areas of work repeatedly return across chats?
2. What result should each area reliably produce?
3. Who reviews or receives each output?
4. Which areas are permanent domains and which are temporary projects?
5. What should the system stop doing or never attempt?

## B. Agent boundaries

1. Which domain owns each source, fact, task, and deliverable?
2. Which domains must not share raw context?
3. Does a proposed agent have a distinct mission, privacy boundary, source base, authority, or output lifecycle?
4. Would one new skill inside an existing agent be enough?
5. Which agent is the control center, and what work must it route rather than perform?

## C. Runtime and model topology

1. Which software will run the model: Codex, Claude Code, Gemini CLI, Cowork, OpenClaw, Hermes, MiMo Code, another workspace product, or a custom API application?
2. Which parts are native, mechanically enforced, advisory, or manual?
3. Is one active model enough?
4. If multiple agents run, which model coordinates as manager and which are workers?
5. Which providers/models may be switched without changing the durable harness?

## D. Data and privacy

1. Which inputs contain credentials, personal records, private research, client/student information, account data, or regulated material?
2. What may remain local, be copied, uploaded, logged, retained, or published?
3. Which folders are read-only, case-isolated, or excluded from model access?
4. What are the largest files and longest logs?
5. What retention, archive, and deletion approvals apply?

## E. Task lifecycle

1. How is a task opened, assigned, blocked, handed off, completed, and archived?
2. What actions require explicit user approval?
3. What files or receipts prove completion?
4. What must be persisted before the agent can report success?
5. How should failures and partial results appear?

## F. Memory and knowledge

1. What does the next session need to resume in under two minutes?
2. Which information is stable institutional knowledge rather than handover state?
3. Which current facts belong only in task/workspace state?
4. What memory and context budgets should apply?
5. What is the consolidation and archival process when a limit is reached?

## G. Skills, tools, and descriptions

1. Which workflows repeat often enough to become skills?
2. What should trigger and exclude each skill?
3. What inputs, outputs, tools, and permissions does it require?
4. Which nearby skills or subagents could collide?
5. What harmless positive, negative, and collision prompts will test routing?

## H. Concurrency and resources

1. Will multiple sessions write at the same time?
2. Which files, devices, databases, browsers, APIs, or quotas require exclusive ownership?
3. When should separate Git worktrees be used?
4. What TTL and heartbeat should locks use?
5. Who may recover a stale lock or transfer ownership during handoff?

## I. Delivery and verification

1. Which files should the scaffold create?
2. Which static checks must pass?
3. Which installed runtimes can receive a fresh-session smoke test?
4. Which claims remain manual or provisional?
5. What final review is required before commit, push, publishing, sending, deployment, or another external action?

## Decision summary template

```markdown
# Harness Decision Summary

- Recurring domains:
- Domain owners:
- Active runtime(s):
- Replaceable provider/model choices:
- Single-agent or manager/worker topology:
- Sensitive data boundaries:
- Required tools/connectors:
- Task and completion gate:
- Memory/knowledge budgets:
- Lock/worktree policy:
- Required outputs:
- Static verification:
- Fresh-session verification:
- Provisional items:
- External actions not authorised:
```
