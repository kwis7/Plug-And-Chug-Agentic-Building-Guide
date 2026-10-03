# 9. Reference: the standard toolkit

The earlier exercise needs only a few files to compare sources and resume the work. A larger project may need task contracts, generated status, budgets or locks, especially when it has several responsibilities to coordinate. The Portable Agentic System toolkit creates a standard scaffold with those features, domain folders and adapter configuration. Use that setup route when its features serve the work. Completing the exercise does not require it, and the small teaching workspace is not a special generator mode.

This chapter explains the commands and what their results establish. Run the examples from this repository's root with an installed `python3` compatible with the source. First inspect the scripts and their `--help`, your environment and the proposed target. For an initial trial, choose a new disposable directory so that the generated files stay separate from existing work. The examples describe operations you can perform; they are not a record of execution on your computer.

## Preview and create a scaffold

Begin with the [starter configuration](../../../skills/portable-agentic-system/pas/examples/starter-config.json). Its two owners illustrate how to describe responsibilities; they are not a recommendation to organise every project that way. For each Agent, the purpose, routing description, exclusions and examples should make it clear when work belongs there and when it belongs elsewhere. Copy the configuration to a working file before changing its sample domains.

Choose an unused target path. The first command previews where the scaffold and Agent folders would go:

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root /tmp/pas-learning-demo \
  --config skills/portable-agentic-system/pas/examples/starter-config.json \
  --dry-run
```

With `--dry-run`, the generator returns JSON containing the target root and Agent paths. It does not list every file it would write. Review the reported locations together with the templates and the generator's scaffold behavior. Once you have reviewed and authorised creation, run the same command without `--dry-run`.

By default, an existing target file causes the generator to refuse that write. Inspect a collision before deciding what to do; earlier writes may already have occurred. The `--force` option bypasses the refusal and permits overwriting, so it requires a deliberate decision about the existing work. It is not a routine way to make an error disappear.

The generated files include runtime configuration and operational scripts under `.pas/bin/`. Examine the hooks before trusting or enabling them in your chosen tool. At this stage you have created configuration files. Establishing that the runtime discovers and executes them requires a separate test.

## Run static checks

Once the files exist, run the static checks below against the generated root. If you selected another target, substitute it consistently in each command.

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

A failure identifies something to investigate before continuing. For example, changing a task record can leave `STATUS.md` out of date. The `--check` invocation compares the page with the task records without rewriting it. Run `generate_status.py` against the same root without `--check` to regenerate the page, then check again. This keeps the task record as the source of current state.

You can also inspect the selected adapter's configuration:

```bash
python3 skills/portable-agentic-system/scripts/adapter_smoke.py \
  /tmp/pas-learning-demo --runtime codex
```

The filename `adapter_smoke.py` can suggest a live test, but this probe inspects generated configuration. It reports `verification_level` as `static`. A passing result supports that inspection, without showing that an installed runtime loaded the instructions or enforced a hook. Choose the runtime you intend to use and follow its adapter's fresh-session procedure to obtain evidence for those behaviors.

## Understand task authority

A standard `tasks/<task-id>/task.yaml` makes the task's agreement explicit. It identifies the task and owner, objective and scope, permitted inputs and writes, available tools and prohibited actions. It also records outputs, completion conditions, verification and receipts, execution resources and the handoff. These fields let the local checks examine the recorded state rather than infer completion from a conversational claim.

The generator saves JSON syntax inside this YAML-named file. Its standard-library parser reads that syntax and also accepts a conservative YAML subset. The `.yaml` extension therefore does not mean every YAML feature is supported. Use the generated task as a format example, and consult the [governance reference](../../../docs/reference/task-lifecycle.md) before writing one manually. The short teaching handoff in chapter 3 serves recovery; it lacks the complete schema of a valid standard task manifest.

For an existing task in the generated system, run its bundled closeout gate from that system's root:

```bash
python3 .pas/bin/closeout_gate.py . tasks/T-123/task.yaml
```

Replace `T-123` with the actual task ID. To accept a successful terminal closeout, the gate requires declared outputs, the required verification state and receipt paths, current generated status, compliance with budgets, released task locks and a handoff. A failed or cancelled task should retain its honest unsuccessful outcome. Closing its record does not turn it into a success.

These checks can identify a missing output or receipt, but the existence of a file does not establish its quality. Review the deliverable and the evidence substantively. Likewise, calling the gate directly does not show that the host invokes it or blocks an attempted completion. That behavior needs its own runtime evidence.

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

For repository development, run the Python suite with `python3 -m unittest discover -s tests -v`. Report a passing result as evidence for the local behavior covered by those tests. Fresh-session compatibility, publication, delivery and external transactions are separate outcomes, each requiring evidence from the relevant operation.
