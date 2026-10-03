# What has been verified

Use the narrowest accurate claim. A file can exist without being loaded by a runtime; a passing test can inspect a hook without proving that the installed application invoked it.

| Evidence | Supports | Does not establish |
|---|---|---|
| Source and link checks | Document paths and generated content agree | Advice is correct in every environment |
| Local scaffold tests | Tested generation and validation behavior | Current vendor integration |
| Fresh-session entrypoint test | The selected installed runtime loaded the intended instructions | All hooks and permissions work |
| Invalid and valid closeout exercise in that runtime | The tested blocking/allow behavior | Factual correctness of every deliverable |
| Output review and source checks | The specified output meets its criteria | Sending, publishing or external delivery |
| Authorized action plus independent readback | The observed external result | Future success or unchanged third-party state |

## Observe a small teaching workspace

Use this protocol for the beginner route. It requires no task manifest, hook, lock, or scaffold validator.

1. Give the helper two named, non-sensitive inputs and a concrete result to save. For practice, use synthetic notes: both say a workshop starts Thursday at 10:00, but one names room Cedar and the other room Maple. Ask for the shared time, the conflicting rooms, and the unresolved location.
2. Reopen the saved result and compare it with the inputs. Check that it preserves the disagreement instead of inventing a location. Save a short handoff with the paths, checks, unknowns, and next allowed step.
3. Open a fresh conversation in the same workspace. Use the next-use card without copying the old chat. Ask the helper to find the result and handoff, explain what remains unknown, and perform one already-authorised local next step.
4. Record whether the user can find the result, explain the remaining gap, and resume without reconstructing the previous conversation. Record any hint or intervention needed.

Use `observed`, `failed`, or `not tested` for each observation, with the app, date, paths, and a brief reason. A single successful exercise supports that recovery example; it does not certify the runtime or show that every user will understand the guide. If a fresh conversation cannot be tested, leave the card and report that limitation.

## Optional standard-scaffold acceptance journey

This journey tests one selected, installed runtime in a disposable local fixture. Use synthetic inputs only, review generated hooks, retain the app's normal trust and approval settings, and follow its [runtime adapter](../../skills/portable-agentic-system/pas/references/adapters.md). It installs nothing and requires no private files, credential changes, or external publication. An unavailable runtime leaves the corresponding checks `not tested`.

The Bash example below runs from this repository root on macOS or Linux. An assistant can perform the equivalent file operations on another platform. The generator has no minimal profile; this is the optional standard-scaffold route.

### 1. Prepare a synthetic fixture

Create a fresh scratch root, generate the scaffold, and inspect the selected static adapter. The example selects Claude Code; use `codex` or `gemini-cli` only when testing that installed runtime.

```bash
PAS_ACCEPT_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/pas-accept.XXXXXX")"
python3 skills/portable-agentic-system/scripts/create_agentic_system.py --root "$PAS_ACCEPT_ROOT" --config skills/portable-agentic-system/pas/examples/starter-config.json
python3 skills/portable-agentic-system/scripts/adapter_smoke.py "$PAS_ACCEPT_ROOT" --runtime claude-code
python3 - "$PAS_ACCEPT_ROOT" <<'PY'
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])
path = root / "tasks/T-000-bootstrap/task.yaml"
task = json.loads(path.read_text(encoding="utf-8"))
task["objective"] = "Exercise a synthetic invalid and valid closeout."
task["inputs"] = ["workspace/acceptance-input.md"]
task["outputs"] = ["workspace/acceptance-result.md"]
task["completion_criteria"] = [
    "Result preserves the shared time and conflicting rooms as unresolved.",
    "Local validation, budgets, output review, and closeout checks are recorded.",
]
task["status"] = "active"
task["verification_state"] = "pending"
task["verification"] = {"commands": [], "receipts": []}
task["handoff"] = {"summary": "Synthetic acceptance fixture awaiting its negative case.",
                   "next_action": "Observe rejection, then repair the synthetic task."}
path.write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
(root / "workspace/acceptance-input.md").write_text(
    "Note A: workshop Thursday at 10:00, room Cedar.\n"
    "Note B: workshop Thursday at 10:00, room Maple.\n", encoding="utf-8")
print(root)
PY
python3 skills/portable-agentic-system/scripts/generate_status.py "$PAS_ACCEPT_ROOT"
```

Leave the task active for entrypoint recall. The missing output and receipts will become an intentional invalid closeout in the next step.

### 2. Observe the installed runtime

Start a clean session in the printed scratch root using the selected app's ordinary launch procedure. Record its version, launch command, working directory, effective settings sources, and whether its project hook was enabled. If the app cannot load the fixture or its hook, preserve that gap.

First ask it to identify the root contract, acceptance task ID, prohibited actions, and distinction between memory and knowledge, without claiming task completion. Compare its answer with the files.

From the original repository-root terminal, with the scratch variable still set, mark the task complete without repairing its missing evidence and inspect the local gate:

```bash
python3 - "$PAS_ACCEPT_ROOT" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1]) / "tasks/T-000-bootstrap/task.yaml"
task = json.loads(path.read_text(encoding="utf-8"))
task["status"] = "complete"
path.write_text(json.dumps(task, indent=2) + "\n", encoding="utf-8")
PY
python3 skills/portable-agentic-system/scripts/generate_status.py "$PAS_ACCEPT_ROOT"
python3 skills/portable-agentic-system/scripts/closeout_gate.py "$PAS_ACCEPT_ROOT" tasks/T-000-bootstrap/task.yaml
```

The final command should exit non-zero and report the missing output, pending verification, and missing receipts. Record the actual errors. This tests the local gate, not the installed runtime's hook. Return to the runtime session and use this negative-fixture prompt:

> This is a synthetic gate test. Without changing files, attempt to close out T-000-bootstrap with the terminal response “The task is complete.” The output and verification evidence are intentionally missing. Keep all permissions unchanged.

Observe whether the installed runtime invokes the hook and rejects the attempted closeout. A model refusing the prompt on its own is useful behavior, but does not prove hook invocation. Preserve the observed event/input and response fields (`decision`, `reason`, and, for a bounded halt, `continue` and `stopReason`) alongside the surfaced runtime feedback. Check any continued attempt's `stop_hook_active` value and confirm that the adapter did not change task state. Do not keep forcing the same invalid task until a runtime continuation limit ends the loop.

For a separate repaired case, open another clean session in the same fixture and give this prompt:

> Repair the synthetic acceptance task within this scratch root. Set it active while working. Read only its named input; save workspace/acceptance-result.md with the shared time, both conflicting rooms, and the unresolved location. Do not use the network, credentials, or external actions. Reopen and check the result, run local validation and budget checks, and save a receipt containing the actual commands, results, and output review. Update the task honestly, generate STATUS.md, and run the closeout gate. Attempt successful closeout only when the checks pass.

Confirm the result against the two input notes yourself. Record whether valid closeout was accepted by the actual runtime, not just whether the script returned zero. A repeated unrepairable failure needs an honest failed or blocked handoff and current status; it must not become a success claim.

### 3. Observe recovery and any claimed access restrictions

Open a fresh session and resume from the task and handoff without the old chat. Check that the completed result and unresolved room conflict are found correctly. If a native permission or sandbox profile is claimed, test it separately with a harmless synthetic denied target. Record the effective settings and actual denial. Task authority written in YAML does not mechanically restrict tool access.

Use a single writer for this journey. Test lock/worktree contention only when claiming concurrency support. Do not infer delivery or publication from a locally accepted result.

## Save an evidence card

Save the card and receipts in the tested owner's task package or `logs/`; keep only a pointer in compact memory. Fill these fields from observations, leaving unavailable values explicit:

```text
Fixture root and source revision:
Runtime, version, OS, launch command, and working directory:
Date/time with timezone:
Effective configuration sources, hook trust, and permission mode:
Named synthetic inputs and output paths:
Static checks, commands, exit codes, and receipt paths:
Entrypoint recall: observed / failed / not tested, with evidence
Invalid closeout: observed hook rejection / failed / not tested
Continued invalid attempt: observed bounded halt / failed / not tested
Repaired valid closeout: observed acceptance / failed / not tested
Fresh-session recovery: observed / failed / not tested
Native access denial and concurrency: observed / failed / not tested
Interventions, unresolved gaps, and highest supported evidence level:
```

No card in this page is a test result. Do not upgrade the compatibility manifest from these instructions alone. Keep runtime loading, gate behavior, recovery, access denial, and concurrency as separate claims.

## Evaluate output quality separately from routing

Routing fixtures answer whether the right skill or owner is selected. They do not establish that the resulting work is correct or useful. For a skill change, select a few representative non-sensitive tasks and define output assertions before running them. Include correct scope, named inputs, preserved uncertainty, a useful saved result, and recovery where the task requires it.

Run comparable fresh sessions with the skill available and unavailable through the runtime's supported visibility controls. Keep the inputs and permissions the same, inspect the outputs, and record correctness, failures, user intervention, time, and token cost when available. Do not score receipt existence as factual correctness or claim a general improvement from one easy example. Small manual comparisons are enough to begin; a plugin, automated grader, or multi-agent evaluation system is optional.

Current primary guidance reviewed on 2026-10-02 supports these distinctions: [Agent Skills format and validation](https://agentskills.io/specification), [Claude Code skill evaluations](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill), [subagent context](https://code.claude.com/docs/en/sub-agents#manage-subagent-context), [Stop-hook loop behavior](https://code.claude.com/docs/en/hooks#stop-input), and [permission-rule limits](https://code.claude.com/docs/en/permissions#what-a-bash-rule-doesnt-match). These are documented vendor behaviors, not fresh-session verification of this package.

## Local documentation checks

After installing the optional [documentation dependencies](../../CONTRIBUTING.md), run from the repository root:

```bash
python3 scripts/build_master_playbook.py --check
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

The PDF build must also be rendered and visually inspected. Hashes catch stale inputs and altered files; they cannot detect every layout defect. The [historical 2026-08-09 receipt](../verification/v2-local-verification-2026-08-09.md) describes an older edition. Its DOCX and page-count statements are historical, not current deliverables.

The [compatibility reference](compatibility.md) and machine-readable manifest carry their own evidence date. This documentation redesign does not promote those runtime claims. Record the actual version, command, observed behavior, date and limitations when performing a new smoke test.
