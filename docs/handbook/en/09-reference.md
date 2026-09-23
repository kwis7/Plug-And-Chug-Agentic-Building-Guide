# 9. Reference: the standard toolkit

The first-project folder teaches a small working method. The Portable Agentic System toolkit implements a broader standard scaffold with domain folders, task contracts, generated status, budgets, locks, and adapter configuration. It is an alternative setup route when those features are useful; completing the learning exercise does not require generating it.

The command examples below run from this repository's root. They use local Python scripts and assume `python3` is installed and compatible with the source. Inspect the scripts, their `--help`, the proposed target, and your environment before execution. Use a new disposable directory for a first scaffold. These instructions do not claim that the commands have run on your machine.

## Preview and create a scaffold

Read the [starter configuration](../../../skills/portable-agentic-system/pas/examples/starter-config.json) and copy it to a working file if you want to change its sample domains. The bundled file contains two illustrative owners; it is not a universal recommendation. Each configured agent needs a purpose, routing description, exclusions, and examples that distinguish it from adjacent work.

Choose an unused target path and run a preview:

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /tmp/pas-learning-demo \
  --config skills/portable-agentic-system/pas/examples/starter-config.json \
  --dry-run
```

The preview reports the target root and agent paths as JSON; it does not enumerate every file to be written. Review those paths, the templates, and the generator's scaffold behavior before creation. To create the reviewed scaffold, run the same command without `--dry-run`. The generator refuses existing-file collisions by default. Do not reach for `--force` as a routine error fix; inspect the collision and preserve existing work.

The generated system includes runtime configuration and local operational scripts under `.pas/bin/`. Review hooks before trusting or enabling them in your chosen tool. The generator does not itself prove that a runtime has discovered or executed the configuration.

## Run static checks

After generation, these commands inspect the scaffold. Replace the target consistently if you chose a different path.

```bash
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/check_budgets.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/check_descriptions.py \
  /tmp/pas-learning-demo
python3 skills/portable-agentic-system/scripts/generate_status.py \
  /tmp/pas-learning-demo --check
python3 skills/portable-agentic-system/scripts/harness_health_check.py \
  /tmp/pas-learning-demo --json
```

Read every failure before continuing. If task records changed and status is stale, run `generate_status.py` with the same root but without `--check`, then check again. That regeneration writes `STATUS.md`; check mode only verifies consistency.

The adapter probe is also available:

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py \
  /tmp/pas-learning-demo --runtime codex
```

This is a **static** probe despite its name. Its reported `verification_level` is `static`. Select a runtime matching your intended integration and follow its adapter for fresh-session tests. Do not upgrade the claim based on a passing configuration inspection.

## Understand task authority

A standard `tasks/<task-id>/task.yaml` records identity and ownership; objective and scope; allowed inputs, writes, tools, and prohibited actions; outputs and completion conditions; verification and receipts; execution resources; and handoff. The generator writes JSON syntax inside the YAML-named file, which its standard-library parser can read. The parser also accepts a conservative YAML subset; it is not a promise of full YAML support.

Use the generated task as a schema example and consult the [governance reference](../../../docs/reference/task-lifecycle.md) before constructing one manually. A teaching handoff from chapter 3 is not a complete valid task manifest.

For a real task already recorded in the generated system, invoke its bundled gate from that system's root:

```bash
python3 .pas/bin/closeout_gate.py . tasks/T-123/task.yaml
```

Replace `T-123` with an existing task. A successful terminal closeout requires the declared outputs, verification state and receipt paths, current generated status, budget compliance, released task locks, and handoff. Failed and cancelled tasks use honest unsuccessful outcomes. The gate's structural checks do not replace a substantive review of the deliverable or verification of the host's blocking behavior.

## Find deeper implementation detail

| Topic | Maintained reference |
|---|---|
| File authority and loading | [Filesystem contract](../../../skills/portable-agentic-system/pas/references/filesystem-contract.md) |
| Private material and external actions | [Privacy boundaries](../../../skills/portable-agentic-system/pas/references/privacy-boundaries.md) |
| Routing and descriptions | [Routing evaluations](../../../skills/portable-agentic-system/pas/references/description-routing-evals.md) |
| Runtime classification | [Compatibility manifest](../../../skills/portable-agentic-system/pas/compatibility/runtime-compatibility.json) |
| Adapter selection and testing | [Adapters](../../../skills/portable-agentic-system/pas/references/adapters.md) |
| Tasks, gates, and concurrent work | [Reliability reference](../../../skills/portable-agentic-system/pas/references/textbook-reliability.md) |
| Full design interview | [Build workbook](../../../skills/portable-agentic-system/pas/references/textbook-build-workbook.md) |

The repository's Python test suite runs with `python3 -m unittest discover -s tests -v`. Passing it supports the tested local behavior. It does not establish fresh-session compatibility, publication, delivery, or any external transaction. Report each of those only at the level of evidence actually obtained.
