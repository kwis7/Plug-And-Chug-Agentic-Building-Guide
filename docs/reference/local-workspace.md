# Keep a local workspace around the assistant you already use

[中文](local-workspace.zh-CN.md) · [Start here](../start-here.md) · [Long-term example](../../examples/long-term-workspace/README.md)

An existing general-purpose assistant can already reason, read permitted files, run tools, and help finish work. Start by making your own materials easier to find and continue. You do not need to build a custom runtime to keep a useful local system.

Keep the working files under your control: a short instruction file, a current-task pointer, named inputs, a checked result, and a handoff. Add a knowledge index or a confirmed preference when you have something worth retaining. Native hooks, multiple models, and concurrent workers are optional later steps.

## Start with one task and three small files

Choose a new workspace folder, one recurring job, and a few non-sensitive inputs. Show the destination before creating it and preserve existing work. A practical first instruction is:

> Use this new folder for my source-comparison work. I will supply the fields or redacted notes you need. Save a local draft, check it against those named inputs, and leave the next step in workspace/current.md. Explain any file-access limitation before claiming that you saved something.

Create only what the first task needs:

```text
My Local Workspace/
├── AGENTS.md                    Short entrypoint for the selected runtime
├── workspace/current.md        Task pointer and next allowed step
└── tasks/T-venue.md             Goal, named inputs, result, checks, handoff
```

`AGENTS.md` is the example entrypoint. Use your runtime's supported instruction location; Claude Code's adapter describes its `CLAUDE.md` bridge. Most other filenames here are workspace conventions. Verify loading in a fresh session before claiming that the runtime uses them.

For routine work already within the agreed scope, let the assistant read the named permitted input and save the local draft. You need a new decision when the task adds a data source, changes the destination or access boundary, exports material, or proposes deletion. You do not need a separate approval conversation for every sentence or file read.

## Add places when there is something to put in them

This is a teaching workspace, not a mandatory generated scaffold. Grow the three-file start as needed:

```text
My Local Workspace/
├── AGENTS.md
├── workspace/current.md
├── tasks/T-venue.md
├── knowledge/
│   ├── index.md                 Reusable methods and dated references
│   └── source-comparison.md
├── preferences/
│   ├── index.md                 Approved preference IDs and versions
│   └── venue-source-comparison-opening.v1.json
├── raw_data/redacted/
│   ├── index.json               Only permitted derivative source IDs
│   └── S-venue-summary.v1.json
├── artifacts/                  Calculations, intermediate files, receipts
└── outputs/                    Results reopened and checked by their owner

User-controlled original archive
    Separate access boundary; original locations are not indexed here
```

Do not create empty departments to make the tree look complete. The original archive belongs to the user and is outside the agent's allowed inputs. A different folder alone does not create that boundary: configure the selected runtime's access or sandbox and, where needed, filesystem permissions. If those controls are unavailable, do not provide that archive to the runtime. Supply an allowed derivative instead.

| Place | Keep | Load when |
|---|---|---|
| Entrypoint | Job, source boundary, where current work is found | Runtime loads it as supported |
| `workspace/current.md` | Current task ID/path, result path, gap, next step | Starting or resuming this work |
| Task card | Objective, named sources, scope, preference/exception, checks and handoff | Working on that task |
| Knowledge and index | A reusable procedure or dated, attributed reference | Relevant to the current question |
| Preferences and index | Explicitly approved behavior, scope and version | Its task scope matches |
| Redacted inputs and index | Minimum authorised derivative and provenance | Task names that source ID |
| Artifacts | Reproducible calculations and actual evidence | A check or recovery needs them |
| Outputs | Reviewed local results | Named review or reuse |

A small `current.md` can say:

```text
Current task: tasks/T-venue.md
Result: outputs/venue-comparison.md
Preference: venue-source-comparison-opening, version 1, source-comparison tasks only
Unknown: Maple's step-free entry and all date-specific booking details
Next: draft one unsent question at workspace/maple-question.md
Read next: task card, reviewed result, and the three named synthetic notes
```

Keep the full reasoning and sources out of this pointer. The [long-term example](../../examples/long-term-workspace/README.md) provides copyable task, result, and handoff contents.

## Let personal originals stay under your control

Do not ask the assistant to open or modify personal source originals. Use one of three inputs: the minimum fields you provide for this task, a derivative explicitly marked agent-readable and redacted, or output from a controlled mediator that exposes only those fields. If none is available, ask for the required fields and continue only with work that does not need them.

For example, a venue comparison needs capacity, opening hours, and entry-access information. It does not need identities, contact histories, account records, or your archive's full paths. A document-management task can start with safe source IDs, types, and dates without exposing the documents themselves.

If the standard scaffold uses `raw_data/`, that convention does not authorise reading personal originals. Use it only for allowed public/synthetic inputs or permitted derivatives. Keep sensitive originals in the user's separate archive. An index is a retrieval aid, not permission to inspect its underlying material.

For a retained derivative, record these minimum fields beside the data:

```json
{
  "source_id": "S-venue-summary",
  "version": 1,
  "derivative_ref": "raw_data/redacted/S-venue-summary.v1.json",
  "derived_at": "2026-10-02",
  "provenance": "Authored synthetic fields for one comparison",
  "agent_readable": true,
  "authorised_scope": ["T-venue: compare capacity, hours, and entry access"],
  "permitted_runtime_provider": "unknown; select an owner-approved destination before loading personal derivatives",
  "freshness_review_on": "2026-11-02",
  "retention_state": "retained-for-authorised-task",
  "retention": "Until task closure; user decides any later reuse or removal",
  "revocation_state": "not_revoked",
  "revocation": "Stop future loading when the user withdraws this scope",
  "verification_label": "illustrative; no runtime or current-source verification"
}
```

This metadata is an authored example, not evidence that a real user supplied or approved data. The review date is a proposed checkpoint, not a completed check or enabled schedule. In your workspace, date it accurately and record the actual scope and permitted destination. `unknown` is not permission to send a personal derivative to any runtime or provider. Index only the named derivatives you chose to use, not your whole archive. Use neutral source IDs; keep names, identifying summaries, sensitive original paths, credentials, and archive inventories out of shared indexes, Git, and model-facing logs.

The user decides ingestion, retention, export, and deletion. On revocation, stop future loading and mark the derivative unavailable for new tasks. Review affected drafts and outputs before reuse; let the user decide their retention or removal. Moving a file or changing an index does not by itself erase copies in native memory, an existing conversation, tool caches, or a hosted service. Review the actual retention and deletion controls separately; do not promise immediate forgetting or retrospective erasure from a changed index.

## Use instructions together with actual access controls

| Control | What it does | What it does not establish |
|---|---|---|
| Entrypoint or task instructions | Tell the assistant the allowed workflow | Filesystem denial |
| Runtime sandbox or filesystem ACL | Restrict access when correctly configured | Correct reasoning or safe export on every tool path |
| A separate worker role | Bound a delegated job and result | Isolation from inherited context or shared tools |
| A Git worktree | Separate repository edits | A private-data boundary |
| `.gitignore` | Keep matching files out of ordinary Git tracking | Prevent reads, uploads, or access to already tracked files |

Test a claimed denial with harmless synthetic material, not a private original. Check the effective runtime configuration and record which tool path was tested. If that cannot be verified, keep the original archive unavailable and label the restriction unknown.

Local files are compatible with hosted model calls. Local storage and an offline-looking workflow do not establish privacy if file text enters a hosted request or a networked tool. Review what the selected runtime and tools transmit. Do not automatically upload an archive, enable whole-disk indexing, or pass private context to a worker because it has a different name.

## Keep useful habits and changes traceable

Use the [preference guide](personalization-and-evolution.md) to retain an explicit future instruction with its scope, approval evidence, and version. A temporary request, such as “show exploratory alternatives first this time”, belongs on the task card as an exception. It does not rewrite the recurring preference.

Turn a repeatedly useful method into one small knowledge note or Skill. Preserve source IDs and dates when facts matter. Keep task outcomes and actual checks with the task, rather than turning the index into a transcript archive.

When you want to change the client, runtime, provider, model, or instruction overlay, use the [model portability guide](model-portability.md). Keep the old combination available, test a synthetic representative task, and record acceptance as `not_run` or partial until there is actual evidence. A record validator checks structure; it does not run a model or prove a better result.

Start advanced controls only when the work calls for them: a [runtime adapter](compatibility.md) for supported instruction loading, the standard scaffold for formal task gates, or locks/worktrees for verified concurrent writing. Your first durable result can be a checked local file and a handoff that another session actually finds.
