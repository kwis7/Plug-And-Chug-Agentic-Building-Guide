# Architecture

This page describes the fuller standard scaffold. Begin with the [guided setup](../start-here.md) for a small personal workspace; add the structures below when the work needs them. A coordinator, task manifests and mechanical gates are not prerequisites for the teaching route.

## Harness boundary

The harness is not one middle layer. It is the full configured environment around model execution:

```text
User/board goals and approvals
        |
        v
+-------------------------------------------------------------+
| HARNESS                                                     |
| entrypoints | identity/rules | registry/routing             |
| skills/tools/connectors | task/status/handoff               |
| memory/knowledge | raw/workspace/artifacts/logs/outputs     |
| hooks/gates/budgets/locks/worktrees/validators/adapters     |
|                                                             |
|                 [ ACTIVE MODEL / EMPLOYEE ]                 |
|                 replaceable A <-> B <-> C                   |
+-------------------------------------------------------------+
```

In a multi-agent topology, the central coordinating model may act as manager. Worker models remain replaceable employees with bounded tasks.

## Control plane and domain ownership

The control center owns registry, routing, shared governance, compatibility, and system health. Domain agents own specialised facts, tasks, source material, skills, and outputs. Visibility does not transfer ownership or authority.

## State authorities

| Question | Authority |
|---|---|
| What exists and who owns it? | `SYSTEM_MAP.md` |
| What is currently active? | task manifests projected into generated `STATUS.md` |
| What may one task do? | that task's `authority` block |
| What proves completion? | receipts plus closeout-gate result |
| What lets the next session resume? | compact `MEMORY.md` pointers |
| What is durable background? | `knowledge/` |
| Where does current work happen? | `workspace/` and active context |
| What is ready for review? | `outputs/` |

## Evidence levels

Static structure, runtime loading, gate behaviour, concurrency, rendering, delivery, and deployment are separate claims. Every adapter and output should state the highest level actually verified.

## Two complementary maps

- [Harness concept map](../assets/harness-concept-map.svg): singles out the active replaceable model and shows that every configured component belongs to the harness.
- [Anonymised example system map](../assets/anonymised-agent-system-map.svg): shows a control center, four functional owner agents, private context, shared methods, adapters, and request-to-output flow.

## Engineering patterns

The design borrows general lessons, not dependencies, from mature systems: separate model from controller/runtime, persist task checkpoints, isolate execution and tools, keep active memory bounded, retrieve archives on demand, and require human approval for consequential actions. See the textbook foundations for links to OpenHands, LangGraph, and Letta.
