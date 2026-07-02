# 15-Minute Quickstart

This quickstart assumes you are not technical.

## Step 1: Choose A Place

Pick a stable local folder. Good examples:

```text
Desktop/My Agentic Control Center
Documents/My AI Agents
```

Avoid temporary download folders.

## Step 2: Install The Skill

For Codex:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/Plug-And-Chug-Agentic-Building-Guide/skills/portable-agentic-system ~/.codex/skills/portable-agentic-system
```

Then restart Codex.

## Step 3: Ask The Skill To Guide You

Use:

```text
Use $portable-agentic-system with pas-start.
```

The skill should ask what areas of life or work need recurring AI help.

## Step 4: Start With Two Agents

A safe starter system:

| Agent | Purpose |
|---|---|
| Research Assistant | Reading, notes, citations, writing |
| Life Admin | Forms, household tasks, reminders |

Add more after one real week of use.

## Step 5: Generate The Folder

If using the included script:

```bash
python3 skills/portable-agentic-system/scripts/create_agentic_system.py \
  --root "$HOME/Desktop/My Agentic Control Center" \
  --config skills/portable-agentic-system/pas/examples/starter-config.json
```

## Step 6: Validate

```bash
python3 skills/portable-agentic-system/scripts/validate_agentic_system.py \
  "$HOME/Desktop/My Agentic Control Center"

python3 skills/portable-agentic-system/scripts/harness_health_check.py \
  "$HOME/Desktop/My Agentic Control Center"
```

If the report says `"valid": true`, the structure is ready.

## Step 7: Use It

Open the new folder in your AI tool and ask:

```text
Read AGENTS.md, tell me which agents exist, and help me choose where my next task belongs.
```

## Step 8: Close The Loop

After each real task, ask the AI:

```text
Update the relevant task.yaml, refresh STATUS.md if needed, and add only compact recovery notes to MEMORY.md.
```

That writeback is what makes the system improve over time.

## Step 9: Distill What Repeats

When you notice that you keep reusing the same notes, prompts, templates, or corrections, ask:

```text
Use $portable-agentic-system with pas-distill to turn this material into reusable knowledge or a skill.
```

This is how the system becomes personal without turning into a drawer full of mystery prompts.
