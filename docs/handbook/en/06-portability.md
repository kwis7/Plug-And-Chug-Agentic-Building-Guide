# 6. Use the workspace with another tool

Portable work remains understandable outside the conversation that created it. The venue notes, comparison, handoff, and reusable method can all be read by a person or supplied to another model. That is the foundation of portability. Automatic loading, tool access, and enforcement require an additional layer of adaptation.

Changing a model and changing a runtime are different operations. The **model** performs the reasoning. The **provider** supplies inference through a service or backend. The **runtime** hosts the session, assembles context, exposes tools, and may manage permissions or hooks. A **switchboard** can route model or provider configuration without owning your task records or working files.

## Identify what actually needs to move

Start with the smallest useful package: the task's requirements, authorised sources, current result, handoff, and relevant procedure. Include the operating rules that affect the task. Do not upload an entire personal workspace simply because the destination accepts many files.

Then ask how the destination receives this material. A local tool may discover designated entrypoints. A hosted workspace may require project instructions and selected uploads. A custom API application must assemble context and implement persistence itself. A document saying “read my files” cannot create filesystem access in an interface that lacks it.

Also decide where changes return. If the new tool creates a revised comparison in chat, someone must save it to the authoritative workspace. Two copies with no reconciliation rule can diverge even when both models reason correctly. Manual writeback is a valid workflow when it is explicit.

## Read support as evidence, not a promise

The repository's [compatibility manifest](../../../skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) records product categories, generated configuration, limitations, and evidence status. Its recorded review date is 2026-08-09. In that record, Codex, Claude Code, and Gemini CLI are classified as `verified_static`, with fresh-session verification marked `not_run`. This is a statement about the repository's evidence, not a new certification of current vendor behavior.

Other entries distinguish documented integrations, manual projections, provisional support, providers, switchboards, and custom-harness patterns. An adapter file is useful guidance, but its existence is not proof that a product loaded it or enforced a rule. Read the [adapter selection guide](../../../skills/portable-agentic-system/pas/references/adapters.md), then the adapter for the tool you intend to use. Recheck the product's official instructions when installing or changing an integration.

## Test the destination with a small fixture

Use the synthetic venue exercise before migrating meaningful work. In a clean destination session, verify four separate behaviors:

1. It can identify the intended rules and named source files.
2. It reproduces the comparison without inventing Maple's accessibility.
3. It saves the result and handoff where the workflow expects them, or clearly leaves saving to you.
4. If a mechanical gate is claimed, an intentionally invalid completion is blocked and a valid completion passes.

Record the tool version, date, fixture, observed result, and remaining gaps. A model's statement that it “understands the rules” does not establish gate behavior. Conversely, a missing gate does not make a manual comparison impossible; it changes what you can claim and what you must review yourself.

Keep the original working copy until the new route has been checked. The aim is to carry forward your evidence and methods while adapting the parts that depend on a particular runtime. Portability becomes practical when both the durable files and the migration limits remain visible.
