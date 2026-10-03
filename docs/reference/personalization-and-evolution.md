# Keep useful preferences, review them, and change them safely

[English](personalization-and-evolution.md) | [中文](personalization-and-evolution.zh-CN.md) · [Home](../../README.md)

Use the capable AI app you already have. Its native harness provides instruction loading, tools, permissions, and execution. Your local workspace gives your authorised materials, useful methods, preferences, and unfinished work a place you can inspect and return to. This guide adds a small way to review retained preferences; it does not require another execution platform or a memory engine.

Begin with the [local workspace guide](local-workspace.md) if you are still choosing where your materials belong. Preferences are one part of that organisation. Personal originals stay under your control. Use only the minimum fields you supply for the current task, explicitly authorised agent-readable redacted derivatives, or controlled mediator output exposing those fields. Keeping files locally does not by itself prevent an app or hosted model from receiving their contents.

## Start with one clear request

You can say: “For future source comparisons, lead with a short recommendation, then explain the evidence and unknowns. Keep this preference for comparison work.”

The assistant should preserve what you asked for, its scope, and where it will be kept. It can use that explicit future-use instruction as retention authority within the stated scope. It should not repeatedly ask for the same agreement, infer a personality profile, or change unrelated instructions.

For a small workspace, a short note in the owner's existing scoped instructions or knowledge file can be enough. A formal JSON record is optional when you want versions, a review queue, or static checks. Neither choice needs a new Agent, a new database, or a rewrite of your app's native features.

## Decide what the feedback means

- **Only this task:** “Make this answer shorter.” Apply it here and keep any needed progress with the task. It is not a future preference.
- **An explicit future instruction:** “Use this opening for future source comparisons.” Retain it only with authority to keep it for that scope. If the intended scope is unclear, clarify that part before applying it elsewhere.
- **A repeated correction:** several similar requests can suggest a candidate. Repetition alone is not permission to retain it, proof of a stable preference, or a reason to apply it to every task.

Do not mine private transcripts or scan personal folders to discover preferences. Use the minimum feedback the user provides or an explicitly authorised, agent-readable summary. A local preference cannot expand reads, tools, account access, external actions, or permission boundaries. It must not override governing rules or weaken evidence requirements.

## A small lifecycle

**Capture → review conflicts → try when needed → activate for its scope → roll back or retire.**

1. **Capture a proposal.** Record the owner, requested behaviour, included task types, exclusions, date, and a minimal source reference. Keep candidates in the owner's existing workspace. Facts, unresolved questions, and one-off corrections remain with their task; reusable procedures belong in Skills.
2. **Review conflicts.** Compare the proposal with current instructions, active preferences, and authority boundaries. Mark the conflict review `pending`, `passed`, or `conflict`. Resolve a conflict before activation. A preference record is not a route for changing safety rules or permissions.
3. **Try it when needed.** If usefulness or scope is uncertain, mark it `trial`. Use a harmless example to check the requested format and a nearby task to check that the preference does not spread beyond its scope. A new-session check can separately show whether the intended version was actually loaded. Keep results as `not_run` until observed.
4. **Activate the authorised preference.** `active` means the owner has authorised retaining it for future matching work. It requires retention authority, a source other than `one_off`, and a passed conflict review. An explicit future-use instruction can authorise activation without an invented trial receipt. Activation records intended future use; it does not prove runtime loading or better output quality.
5. **Roll back deliberately.** Keep the earlier version before changing behaviour or scope. Record which older version is to be restored and why, then point the owner's relevant index or instruction to it. Retire the replaced version with a reason. Preserve both records so the change remains understandable.
6. **Retire what no longer fits.** A user can withdraw a preference, replace its scope, or stop using it. Mark it `retired`, record the reason, and remove it from the set selected for future tasks. Retain a small recovery pointer rather than deleting the only history. Review intervals should reflect actual use; this guide does not enable a scheduler.

Before a matching task, ask the assistant to read the named active preference, check its scope, and say which version it used. Excluded tasks should not receive it. An explicit current-task request can override an ordinary style default for that task, subject to the governing rules. It does not silently rewrite the long-term preference.

## Example: a better opening for comparisons

This is a fictional sequence, not an observed improvement:

- **Before:** a comparison starts with several background paragraphs and puts its recommendation at the end.
- **Feedback:** “For future source comparisons, give me two short opening sentences, then the sources and unknowns. Keep this for comparison work.”
- **Proposal:** owner `example-owner`, preference `source-comparison-opening`, version `1`; include `source-comparison`, exclude `creative-writing` and `debugging`.
- **Intended next result:** in the supplied fictional venue exercise, the opening identifies Cedar as a candidate on the recorded requirements and keeps Maple's step-free entry unknown. The source table follows. No new venue facts or booking claim are introduced.
- **Task exception:** “This time, explore possibilities before recommending.” That changes this task's presentation without retiring the retained preference.
- **Later revision:** if the user asks to change the future default, keep version `1`, propose version `2`, review its scope, and identify the older version available for rollback.

The [long-term workspace example](../../examples/long-term-workspace/README.md) connects preferences with task exceptions, source records, model profiles, and authored receipt examples. Its checks remain unobserved until someone performs them. A preferred format can fit the user's request without proving that the model itself improved.

<details>
<summary>Optional: use a versioned JSON record and static checker</summary>

The [preference record template](../../skills/portable-agentic-system/pas/templates/preference-record.json) is a fictional proposal. Its retention flag is `false`, conflict review is `pending`, evidence mode is `illustrative`, and receipt list is empty. Replace its owner, example behaviour, source reference, and date with authorised information before treating it as your own record.

The record keeps:

- **Identity:** `schema_version: 1`, `kind: preference`, stable `id` and `owner`, and a positive integer `version`.
- **State:** `proposed`, `trial`, `active`, or `retired`.
- **Scope:** named `include_task_types`, optional `exclude_task_types`, and the requested `behavior`.
- **Source and authority:** `source.kind`, a minimal `reference`, `recorded_at` as `YYYY-MM-DD`, `retention_authorized`, and `conflict_review`.
- **Version history:** `supersedes_version` and `rollback.restore_version` name an older positive version or remain `null`; a rollback has a reason. A retired record requires `retirement_reason`.
- **Evidence:** `illustrative` for an authored example or `observed` for actual observations. `evidence.receipt_refs` contains receipt record IDs, not file paths. Referenced receipt JSON files must be explicitly supplied together for version checks; the checker does not discover private evidence on its own.

Ask your assistant to run this from the repository root if you want to check the supplied template:

```bash
python3 scripts/check_workspace_records.py \
  skills/portable-agentic-system/pas/templates/preference-record.json
```

The command reads the named records and reports static problems. It does not mutate records, activate a preference, change settings, or run a model. Supply any relevant receipt files explicitly when checking their references. A static pass does not show that an app loaded the record, honoured its scope, or improved a result.

Keep actual loading evidence separate from retention authority. An observed receipt should identify the record and version, the app or runtime, the named inputs, and what was actually checked. Do not turn an illustrative receipt or a proposed check into observed evidence.

For a preference with `evidence.mode: observed`, the checker requires a non-empty list of explicitly supplied observed receipts matching the preference ID and version. An authorised `active` preference can remain `illustrative` with no receipt when no loading observation is claimed.

</details>

Use [review and renewal](system-review-and-renewal.md) to inspect recurring friction and [knowledge distillation](knowledge-distillation-and-skill-fusion.md) when a repeated procedure deserves a Skill. Use [model portability](model-portability.md) when changing tools or models; retaining a preference file and loading it in another app are separate steps.
