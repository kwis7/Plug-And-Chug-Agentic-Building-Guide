# Quick start

[English](QUICKSTART.md) | [中文](QUICKSTART.zh-CN.md) · [Home](README.md)

Choose one route. The guided learning example and the standard generator are alternatives; neither is a prerequisite for the other.

| Route | You need | You get |
|---|---|---|
| [AI-guided first task](docs/start-here.md) | An AI tool that can read your selected local files; write access for saved work | A small source comparison and a handoff you can resume |
| [Manual standard scaffold](#manual-standard-scaffold) | Git, Python 3.10+, a terminal, and a writable parent directory | A control center, two example domain agents, runtime configurations, and local checks |

A chat-only tool can discuss the example if you paste its fictional inputs, but cannot demonstrate local file discovery or persistence without those capabilities. Your AI tool may have subscription or API costs. The local Python generator does not call a model API.

## AI-guided first task

Open [Start here](docs/start-here.md), then follow the [first-project tutorial](examples/first-project/README.md). No skill installation is needed. It is a small learning workspace, not a supported minimal generator profile. For your own recurring work afterward, use the [short starting prompt](skills/portable-agentic-system/pas/references/friend-starter-prompt.md).

<a id="manual-standard-scaffold"></a>
## Manual standard scaffold

The commands below use Bash or Zsh. Use a shell with those conventions; they are not PowerShell commands. Start in a writable directory where neither the clone folder nor `my-first-agent-workspace` already exists. Keep the same terminal open through the steps.

### 1. Get the toolkit and check Python

```bash
git clone https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide.git
cd Plug-And-Chug-Agentic-Building-Guide
python3 --version
```

Use Python 3.10 or later. The generator and the checks below use the Python standard library; no package installation is required for this route. Review the repository's scripts before running them.

### 2. Set one destination and preview it

```bash
PAS_REPO="$(pwd)"
PAS_SCRIPTS="$PAS_REPO/skills/portable-agentic-system/scripts"
PAS_CONFIG="$PAS_REPO/skills/portable-agentic-system/pas/examples/starter-config.json"
PAS_TARGET="$PAS_REPO/../my-first-agent-workspace"
printf '%s\n' "$PAS_TARGET"
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG" --dry-run
```

`PAS_TARGET` is a new sibling directory of the repository, not this checkout. Change that variable now if you want a different location. If it already exists, choose a new destination before continuing.

The preview prints JSON with the root, the two agent paths, and `"mode": "dry-run"`. It creates no files and does not check every possible write conflict. The supplied config creates `research-assistant-Agent` and `life-admin-Agent`; they are examples to review, not a recommendation that everyone needs both.

### 3. Generate the previewed structure

```bash
python3 "$PAS_SCRIPTS/create_agentic_system.py" \
  --root "$PAS_TARGET" --config "$PAS_CONFIG"
```

Expected: a JSON summary with `created_count` and file paths. The destination contains `AGENTS.md`, `SYSTEM_MAP.md`, `STATUS.md`, a bootstrap task, two domain folders, and copied scripts under `.pas/bin/`. It also contains Codex, Claude Code, and Gemini CLI hook configurations. Review those before opening the folder in a runtime that may load them.

This is the **standard scaffold**. There is currently no minimal-profile or single-runtime switch. The generator refuses an existing file by default, but a failed run can leave files already written. Do not add `--force` to resolve an unexplained failure; inspect the result and use [troubleshooting](docs/reference/troubleshooting.md).

### 4. Check what was created

```bash
python3 "$PAS_SCRIPTS/validate_agentic_system.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_budgets.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/check_descriptions.py" "$PAS_TARGET"
python3 "$PAS_SCRIPTS/generate_status.py" "$PAS_TARGET" --check
python3 "$PAS_SCRIPTS/harness_health_check.py" "$PAS_TARGET"
```

Expected: the JSON validation reports have `"valid": true`, the status check says `STATUS.md is current`, and the health report labels itself **static**. Read warnings as well as errors. A static pass verifies structure and consistency; it does not complete the bootstrap task or prove runtime behavior.

### 5. Review, connect, and try one task

Read the generated `SYSTEM_MAP.md`, `RULES.md`, and `tasks/T-000-bootstrap/task.yaml`. Adapt the example roles to actual work before introducing real materials. Follow the [compatibility reference](docs/reference/compatibility.md) to select your tool; skill installation is optional and runtime-specific. No personal-scope installation is part of this quickstart.

Use the [verification procedure](docs/reference/verification.md) for a fresh session: verify which instructions were loaded, then test the relevant valid and invalid closeout behavior. Record the tool version, date, commands, and observed results. The repository's compatibility manifest does not substitute for evidence from your setup.

Next, try one bounded task, name its allowed inputs, save a checked result and a recovery note, and regenerate `STATUS.md` from its task record. The [handbook](docs/handbook/index.md) explains that workflow; the [task reference](docs/reference/task-lifecycle.md) gives the exact contract.
