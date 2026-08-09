# Generic Workspace Agent Projection

Classification: manual fallback, not a product integration
Repository verification: `manual_projection`

Use this only when a product can work in an authorised folder but its native instruction, skill, memory, hook, and writeback semantics are not documented or verified.

## Startup contract

```text
This folder is a local agent harness. The current model is a replaceable worker.
Read AGENTS.md as advisory operating instructions, then read SYSTEM_MAP.md and
the named active task contract. Load only the relevant identity, rules,
knowledge, skill, and source files. Do not recursively read raw_data, logs,
archives, or unrelated agent folders. Draft in workspace, keep intermediates in
artifacts, and place only reviewed deliverables in outputs. Do not delete,
upload, send, submit, publish, use credentials, or make external changes
without explicit user approval. Return proposed task and status updates when
local writeback is unavailable.
```

## Verification

Check the product's official documentation and actual behaviour for folder access, cloud copying, retention, model selection, skills/plugins, connectors, memory, write permissions, sandboxing, deletion, and external actions. Until a product-specific adapter exists, keep its status manual or provisional.

Tencent WorkBuddy currently remains in this category: official public material establishes authorised-folder operations, model configuration, skills, multi-agent work, and a sandbox, but not a stable PAS-native entrypoint contract.
