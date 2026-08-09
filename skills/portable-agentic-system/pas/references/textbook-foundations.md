# Foundations: From a Model to an Agentic System

## 1. The useful unit is not the model

A language model predicts and transforms text. It may reason well, write code, interpret images, or choose tools, but none of those abilities tells it which files belong to a project, what it may change, what happened yesterday, which output has been reviewed, or when a task is genuinely complete. Those properties come from the system around the model.

This distinction is easy to miss because the model is the visible, conversational part. When an answer is good, people credit the model. When an answer is inconsistent, they often switch models. Sometimes a different model helps. Often the real defect is structural: the wrong instructions loaded, the relevant evidence was never retrieved, two tasks shared mutable state, the agent had no verification receipt, or the runtime could not enforce the rule written in Markdown.

Use five separate terms:

| Term | Meaning | Typical failure if confused |
|---|---|---|
| Model | The active reasoning engine | Assuming intelligence creates persistence or authority |
| Provider | The API or service supplying inference | Assuming an API knows the local project layout |
| Runtime | The program hosting the model, tools, permissions, hooks, and instruction discovery | Copying another runtime's file syntax and expecting it to work |
| Agent | A model executing within a defined role, tool surface, and state boundary | Treating a persona paragraph as a complete system |
| Harness | All configured architecture that makes execution useful, bounded, recoverable, and testable | Drawing it as one optional wrapper instead of the configured whole |

The model should be drawn as a conspicuous replaceable module. It is active, but it is not the owner of durable truth. The harness outlives a model change.

## 2. A company is a better metaphor than a chatbot

Imagine a small company. The user is the board: they decide purpose, risk tolerance, priorities, and actions that require approval. An active model is an employee. The employee can be replaced without destroying the company.

The rest of the company maps naturally:

| Company concept | Agent-system concept |
|---|---|
| Charter and strategy | identity, mission, system map |
| Company rules | rules, permissions, approval boundaries |
| Department manual | skill |
| Work order | task contract |
| Shift handover | compact memory |
| Archive and library | knowledge collection |
| Desk | current context and workspace |
| Receiving room | raw data |
| Workshop scraps | artifacts and caches |
| Machine traces | logs |
| Reviewed shipment | output |
| Quality control | validators, receipts, completion gates |
| Room booking and branch office | resource lock and Git worktree |
| IT platform | runtime and connectors |
| Outside contractor | provider/model endpoint |

Do not call every active model a manager. In a single-agent system, the model is simply the employee doing the work. In a multi-agent system, a central model that routes work, manages dependencies, and synthesises results can reasonably be called the manager. Other active models remain employees with bounded assignments.

The metaphor has limits. A model has no stable private intention, does not automatically remember prior sessions, and can misunderstand policies presented only as text. The company analogy explains organization; deterministic controls provide reliability.

## 3. Harness is a set of configured relationships

The harness is not one folder and not an abstract “second layer”. It includes every configured element and the relations among them:

- which entrypoint a runtime discovers;
- which instruction wins when files conflict;
- how a request routes to an owner;
- which model is active and replaceable;
- which tools and connectors are visible;
- which data the owner may read or write;
- how a task records scope, status, outputs, and failure;
- which facts become compact memory;
- which references remain in long-term knowledge;
- which files may enter the context window;
- which validators produce receipts;
- which hook blocks a false completion claim;
- which locks or worktrees separate concurrent writers;
- which external actions require human approval.

A folder tree can show the nouns. A system map must also show the verbs: route, load, retrieve, execute, verify, hand off, approve, and archive.

## 4. Why personalisation matters

A generic assistant must remain vague because it does not know the user's repeated domains, privacy boundaries, evidence standards, output formats, or approval rules. Personalisation is not decorative biography. It is the process of encoding stable operational differences.

Useful personalisation answers questions such as:

- Which recurring work deserves a durable domain owner?
- Which tasks can share methods without sharing private context?
- Which sources count as authoritative in each domain?
- Which outputs must be reviewed, rendered, or independently reproduced?
- Which actions may be drafted but never sent automatically?
- Which facts are stable enough for memory, and which must be refreshed live?
- Which folders are safe to enumerate but unsafe to read recursively?
- Which runtime actually executes the work on each machine?

The right harness therefore cannot be copied wholesale from another person. A public template should provide a grammar and safeguards, then guide the user through choices.

## 5. Three levels of system maturity

### Minimal

Use one agent, one compact runtime entrypoint, a small rules file, named skills, a current task file when needed, a workspace, and reviewed outputs. This is sufficient for one person with a small number of recurring workflows and low concurrency.

### Standard

Add domain agents with explicit descriptions, generated status, compact memory, long-term knowledge, file lifecycle rules, receipts, a deterministic closeout gate, and large-file manifests. This level suits sustained personal or small-team work.

### Advanced

Add a coordinating agent only where necessary, native runtime hook integrations, isolated connectors, per-agent sandboxes, evaluation suites, worktrees, resource locks, durable checkpoints, recovery drills, and external-action approval services. This level creates operational cost and should solve demonstrated problems.

Do not begin at the advanced level because it looks impressive. Start at the smallest level that can enforce the real boundary.

## 6. Context is computed, not discovered by magic

At each turn the runtime assembles a temporary input. It may contain platform instructions, project instructions, skill metadata, selected task state, retrieved knowledge, tool results, and recent conversation. The filesystem can be enormous while the context remains finite.

This leads to a central design law:

> Store broadly, index deliberately, retrieve narrowly, and verify before promotion.

The goal is not to make every fact permanently visible. The goal is to make the right fact retrievable with its authority, date, and provenance intact.

## 7. Instructions are not enforcement

An instruction such as “always update status” changes model behavior probabilistically. A generated status script changes a file deterministically. An instruction such as “do not read secrets” is valuable, but filesystem permissions and tool policies create a stronger boundary. An instruction such as “do not finish without tests” is advisory until a Stop or final-response hook translates a failed validator into the runtime's block or retry protocol.

Classify controls:

| Control | Example | Strength |
|---|---|---|
| Narrative | rule in Markdown | behavioral guidance |
| Structural | separate owner folders and named loading rules | reduces accidental mixing |
| Deterministic | schema validator, generated status, size check | repeatable local evidence |
| Runtime-enforced | tool deny policy, sandbox, blocking hook | prevents or interrupts behavior |
| Human-enforced | explicit approval for send, payment, publication | authority boundary |

Good systems combine them. They do not describe a narrative reminder as a security control.

## 8. Lessons from mature open-source systems

The purpose of studying successful repositories is to extract architecture patterns, not to copy their abstractions into every personal project.

- [OpenHands](https://github.com/All-Hands-AI/OpenHands) separates agent logic, controller/state, event stream, runtime, and sandbox. The general lesson is to keep the model separate from execution control and environment isolation.
- [LangGraph](https://github.com/langchain-ai/langgraph) foregrounds durable execution, checkpoints, and human-in-the-loop control. The general lesson is that long work should resume from explicit state rather than chat recollection.
- [Letta](https://github.com/letta-ai/letta) treats memory as an engineered subsystem rather than an unlimited transcript. The general lesson is to keep a small active working set and retrieve archival material on demand.
- Runtime-native skill systems in Codex, Claude Code, and Gemini CLI use metadata-first discovery and load full instructions only when selected. The general lesson is that descriptions and progressive disclosure are part of architecture.

These projects solve different problems at different scales. The portable pattern is the separation of model, controller, state, runtime, tools, storage, and verification.

## 9. A first diagnostic

Before adding anything, ask:

1. If the model changed tomorrow, which useful properties would remain?
2. If the chat disappeared, could another model recover the current task?
3. Can the system identify one owner for every private corpus and reviewed output?
4. Can it distinguish current state from historical memory?
5. Can it prove that a completion gate actually ran in the selected runtime?
6. Can a large log or raw-data directory enter context accidentally?
7. Can two writers edit the same authority file concurrently?
8. Does every agent description explain both when to route and when not to route?

Every “no” points to a harness requirement. Not every requirement needs a new agent.
