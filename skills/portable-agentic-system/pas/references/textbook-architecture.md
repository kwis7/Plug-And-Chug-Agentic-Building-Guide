# Architecture and Personalisation

## 1. Begin with ownership, not folder aesthetics

A multi-agent system is useful when it encodes real boundaries. It is harmful when it merely creates many personalities that compete for the same work.

For each recurring domain, define:

- the work it owns;
- the private context it owns;
- the outputs it owns;
- the methods it can share;
- the actions it may take;
- the evidence standard it follows;
- the adjacent agents it must not impersonate.

If two proposed agents share all six, they are probably one agent with two skills.

## 2. Four useful architectural units

### Domain agent

Use for recurring responsibility with stable ownership or data boundaries. Examples include an Investment Analysis Agent, Research Agent, Application Operations Agent, or Report and Design Agent. These names describe functions, not people.

### Skill

Use for a reusable procedure: literature search, financial statement parsing, citation audit, PDF rendering, claim verification, or weekly review. Skills can be shared only when their data assumptions and permissions are compatible.

### Task/project

Use for temporary outcomes: write one report, audit one repository, prepare one application package. A task receives an owner; it does not need a new identity.

### Connector/tool

Use for capabilities that cross the filesystem boundary: search, email, calendar, database, broker, cloud storage, deployment. A connector needs scope, approval, credentials, cost, rate, and data-handling policies.

## 3. A control center is a registry, not a super-agent

The control center should own:

- the agent registry and routing map;
- common governance and file contracts;
- runtime compatibility information;
- shared capability discovery;
- task/status aggregation;
- cross-agent coordination;
- system health and renewal.

It should not silently become the owner of every domain's facts or private data. Visibility of a folder does not create authority.

In a multi-agent topology, the central active model can act as manager by selecting an owner, decomposing dependencies, and integrating results. Its power should remain bounded by the same task, permission, and evidence contracts.

## 4. Description-first routing

An agent folder is inert until the system can select it correctly. The description is often the first and sometimes the only text a routing model sees. Therefore description quality precedes implementation.

A routing description is a compact decision rule:

```text
Use when [observable request conditions].
Own [inputs, decisions, outputs].
Require [freshness/evidence standard].
Do not use for [adjacent domain or prohibited action].
Escalate when [collision or authority boundary].
```

Bad:

> Helps with important research and analysis.

Better:

> Use when a request requires evidence collection, source comparison, literature synthesis, or uncertainty tracking. Own research notes and citations. Do not use for final report layout, external publication, or unsupported investment execution.

### Routing evaluation set

For each agent or skill maintain:

- obvious positive prompts;
- difficult positive prompts with indirect wording;
- obvious negative prompts;
- near-neighbor collision prompts;
- mixed prompts that require decomposition;
- out-of-scope prompts that require escalation.

Record expected route and observed route by runtime/model version. A description is configuration; evaluate it when it changes.

## 5. Separate model choice from agent identity

Agent identity should remain stable while the model slot changes. Record model selection as runtime configuration or task policy:

- model/provider;
- reasoning or latency profile;
- tool support;
- context limit;
- cost boundary;
- data residency;
- fallback rules;
- last verification date.

Do not duplicate the model name throughout identity, memory, and skills. That turns a replaceable dependency into a structural assumption.

Different tasks can select different employees. A fast model may classify requests; a stronger model may synthesise evidence; a specialised model may inspect images. The harness keeps ownership and verification constant.

## 6. Single-agent architecture

A strong single-agent system can include:

- one runtime-native entrypoint;
- one identity and rules set;
- several sharply described skills;
- task manifests for complex work;
- knowledge retrieval;
- a workspace and data lifecycle;
- deterministic closeout;
- one model slot that can be replaced.

This topology minimizes routing errors and duplicated context. It should be the default until domains truly conflict.

## 7. Multi-agent architecture

Introduce multiple agents when at least one is true:

- data must remain isolated;
- actions require different permissions;
- work has stable independent owners;
- evidence standards differ materially;
- contexts are too noisy together;
- parallel work has genuine latency value;
- independent review must be separated from execution.

A practical anonymous example can contain:

```text
Control Center/
├── Investment Analysis-Agent/
│   ├── knowledge/ skills/ tasks/ workspace/ raw_data/ artifacts/ outputs/
├── Research-Agent/
│   ├── knowledge/ skills/ tasks/ workspace/ raw_data/ artifacts/ outputs/
├── Application Operations-Agent/
│   ├── knowledge/ skills/ tasks/ workspace/ raw_data/ outputs/
└── Report and Design-Agent/
    ├── knowledge/ skills/ tasks/ workspace/ artifacts/ outputs/
```

These are public-safe functional examples. Real source material, identities, credentials, client records, account records, and task contents remain private.

## 8. The multi-agent execution loop

```text
User request
    |
    v
Control center classifies domain and authority
    |
    v
Owner agent receives task contract
    |
    +--> optional bounded subagents or method borrowing
    |
    v
Owner integrates evidence and runs verification
    |
    v
Completion gate and human approval where required
    |
    v
Reviewed output and durable handoff
```

The manager never delegates final responsibility. Subagent results are evidence or proposals until the owner reviews them.

## 9. Method sharing without context leakage

Cross-agent reuse should share:

- public skills;
- source-selection methods;
- schemas;
- test fixtures;
- rendering scripts;
- checklists;
- validation logic.

It should not automatically share:

- raw data;
- private memory;
- identity files;
- current task state;
- credentials;
- account, student, client, health, or application records;
- unpublished research corpora.

Record borrowed capability, source agent, version/date, local adaptation, and result in the receiving task package. The receiving agent remains authoritative.

## 10. Tools and connectors as capability cards

For each connector, create a capability card:

| Field | Question |
|---|---|
| Purpose | What repeated need justifies it? |
| Read scope | Which objects and fields may be read? |
| Write scope | Which external state may change? |
| Approval | Which call requires user confirmation? |
| Credentials | Where are secrets stored outside the repo? |
| Data boundary | What may leave the local machine? |
| Cost/rate | What budget or limit applies? |
| Evidence | How is success independently read back? |
| Failure | What happens on timeout, partial write, or duplicate call? |
| Disable | How is the connector revoked safely? |

Start read-only when practical. Introduce write scope after a shadow run. Separate “can call the connector” from “may take this action now”.

## 11. Subagents and temporary teams

Use a subagent for an independently verifiable, bounded workstream. Its delegation contract should name:

- objective;
- authority and prohibited actions;
- source and freshness rules;
- allowed files and tools;
- expected artifact or evidence;
- validation criteria;
- stop condition;
- whether it may delegate further.

Use the minimum number of workers. Parallel read-only exploration, source validation, or independent review is safer than multiple writers editing the same authority file.

Persistent named agents are justified only when the same role repeats or when the runtime must mechanically restrict tools, sandbox, permissions, or memory.

## 12. Architecture as explicit flows

A system map should show at least four flow types:

- **control flow**: request, route, task, approval;
- **evidence flow**: source, workspace, receipt, output;
- **retrieval flow**: memory pointer or knowledge query into current context;
- **coordination flow**: delegation, lock, worktree, handoff.

Use a boundary legend. A line that represents method borrowing should look different from a line that moves private data. Mark prohibited crossings explicitly.

## 13. Personalisation questionnaire for architecture

Ask:

1. What work repeats at least monthly?
2. Which work must never share raw context?
3. Which outputs have different audiences?
4. Which actions change external state?
5. Which tasks need current sources?
6. Which methods repeat across domains?
7. Which tasks fail because history is lost?
8. Which tasks fail because too much history is loaded?
9. Which agents could collide on the same prompt?
10. Which agent is the single owner when a prompt spans domains?

Turn the answers into ownership, skills, retrieval, and approval design—not additional folders by default.

## 14. Architecture review rubric

Score each dimension from 0 to 3:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Model separation | model treated as whole system | conceptual distinction only | visible replaceable slot | replacement tested |
| Ownership | no owner | folder names imply owner | explicit registry | boundaries tested with collisions |
| Routing | arbitrary | descriptions vague | positive/negative rules | evaluated across runtime/model versions |
| Privacy | broad visibility | prose warning | scoped paths/tools | isolation and denial fixture verified |
| Method reuse | copy everything | ad hoc copying | shared skills | provenance and compatibility recorded |
| Multi-agent need | decorative roles | partial rationale | boundary-based topology | topology reviewed and simplified regularly |

Low scores should produce a small repair plan, not a wholesale rewrite.
