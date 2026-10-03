# 6. Use the workspace with another tool

Your saved venue notes, comparison and handoff give you material to work with in another tool. You can read them yourself and supply the authorised parts to a new model. What needs checking is how the new environment receives that material, uses its tools and saves the next result. File portability provides a starting point for those checks.

A move may involve several changes. The **model** does the reasoning, while the **provider** supplies inference through a service or backend. The **runtime** hosts the session, assembles context, exposes tools and may manage permissions or hooks. If you keep the same runtime and change a model setting, some of that arrangement may remain in place. Moving to another runtime can require different instruction entrypoints, tool configuration and recovery steps.

A **switchboard** can route model or provider configuration. Your task records and working files still need their own owner and location. Identifying which part you are changing helps you decide what can be carried forward and what must be adapted.

## Identify what actually needs to move

For the venue task, gather the requirements, authorised sources, current result, handoff and relevant procedure, along with the operating rules that apply. These are the materials the next session needs. A destination's ability to accept many files is no reason to upload a whole personal workspace. Personal originals remain under your control; provide only the minimum fields authorised for the task, an explicitly agent-readable redacted derivative or a controlled mediator output.

Check how the selected tool takes in those materials. A local tool may discover designated entrypoints. A hosted workspace may need project instructions and selected uploads. A custom API application would have to assemble context and implement saving itself. You can use the facilities of an existing app when they meet your needs. An instruction to read files still requires an interface with actual file access.

Agree on where revisions return. If a new comparison appears only in chat, the authoritative local file will still contain the old result until someone updates it. Manual writeback is a workable choice; tool-based saving is another when the environment supports it. In either case, identify the current working copy and who updates it. Otherwise both copies can continue to change independently. Also confirm the destination and permission before supplying material to another service: local storage alone does not establish offline processing.

## Read support as evidence, not a promise

The repository's [compatibility manifest](../../../skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) records product categories, generated configuration, limitations and evidence status. The recorded review date is 2026-08-09. Codex, Claude Code and Gemini CLI are classified there as `verified_static`, with fresh-session verification marked `not_run`. Those labels describe the evidence retained in the repository. They do not certify current vendor behavior.

The remaining entries distinguish documented integrations, manual projections, provisional support, providers, switchboards and custom-harness patterns. Read the entry for the kind of tool you are using, then consult the [adapter selection guide](../../../skills/portable-agentic-system/pas/references/adapters.md) and the selected adapter. An adapter describes the intended setup; observed loading and enforcement require separate evidence. Recheck the product's official instructions when installing or changing the integration.

## Test the destination with a small fixture

Keep meaningful work in its original location while you try the synthetic venue exercise in a clean destination session. Check four separate behaviors:

1. The session identifies the intended rules and named source files.
2. Its comparison follows the supplied notes and leaves Maple's accessibility unknown.
3. The result and handoff are saved where expected, or the workflow clearly assigns saving to you.
4. If the integration claims a mechanical gate, an intentionally invalid completion is blocked and a valid completion passes.

Record the tool version, date, fixture, observed result and remaining gaps. For the gate check, look for the integration's actual behavior. A model saying that it understands the rules cannot establish that the gate ran. If no gate is connected, you can still review a comparison manually, with that responsibility and limitation recorded.

Retain the original working copy until the new route has passed the checks it needs. If the destination cannot save a file or recover the task, you can return to the working setup and address the specific gap. The evidence and procedures already saved remain available while you adapt the parts that depend on the runtime.
