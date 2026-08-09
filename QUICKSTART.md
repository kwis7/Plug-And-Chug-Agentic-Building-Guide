# Quick Start

## 1. Let the Skill interview you

Install the skill in the location documented for your runtime, then use:

```text
Use $portable-agentic-system with pas-start. Explain the company metaphor, ask me the staged questionnaire one section at a time, recommend the smallest useful harness, and show me the tree, runtime status, privacy boundaries, task gate, budgets, and lock policy before writing files.
```

## 2. Edit the starter config

Copy `skills/portable-agentic-system/pas/examples/starter-config.json` to a private working location. Start with two or three recurring domains. Every agent config needs a behavioral `routing_description`, exclusions, at least two positive prompts, and at least two negative prompts. A new agent needs a durable mission, privacy boundary, source base, authority, or output lifecycle; otherwise add a task or skill instead.

## 3. Dry-run and generate

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "/path/to/My Agent Harness" \
  --config /path/to/my-config.json \
  --dry-run

python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "/path/to/My Agent Harness" \
  --config /path/to/my-config.json
```

## 4. Validate static structure

```bash
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/check_budgets.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/check_descriptions.py "/path/to/My Agent Harness"
python3 skills/portable-agentic-system/scripts/generate_status.py "/path/to/My Agent Harness" --check
python3 skills/portable-agentic-system/scripts/harness_health_check.py "/path/to/My Agent Harness"
```

## 5. Test the actual runtime

Read the matching file under `pas/adapters/`. Review and trust generated project hooks where the runtime requires it. Start a clean session in the generated fixture and ask it for the operating contract, active task, prohibited actions, and memory/knowledge distinction. Then exercise one invalid and one valid closeout. Save runtime version, command, date, output, and hook receipt. Static validation is not runtime or gate verification.

## 6. Complete one real task

Use a task contract, named inputs, a scoped workspace, reviewed outputs, verification receipts, and the closeout gate. Regenerate `STATUS.md`; do not edit it manually. The generated system contains its own scripts under `.pas/bin/`, so future operation does not depend on this source repository remaining at the same path. Review after real use before adding more agents or skills.
