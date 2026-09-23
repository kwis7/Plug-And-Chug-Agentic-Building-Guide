# Your first project: a source comparison

[English](README.md) | [中文](README.zh-CN.md) · [Start here](../../docs/start-here.md)

Compare three fictional venues for a workshop. The result should be a short comparison that shows which recorded requirements each venue meets, where a source rules it out, and what is still unknown. Then prove that a new session can continue from a saved note.

All venue information is **synthetic learning data**, not real venue information or fresh public research. No search, message, or booking is needed. This directory is a learning worksheet, not a generated standard harness; do not run the scaffold validator against it.

## 1. Know what belongs where

| File or folder | Purpose |
|---|---|
| [task-brief.md](task-brief.md) | The request, allowed inputs, outputs, and check criteria |
| [sources/cedar.md](sources/cedar.md), [willow.md](sources/willow.md), [maple.md](sources/maple.md) | The three supplied source notes; preserve them |
| `workspace/comparison.md` | Your draft, created during the exercise |
| `outputs/comparison.md` | Your checked result, created after review |
| `workspace/handoff.md` | Current state and the next step, created during the exercise |
| `expected/` | Reference answers for comparison after your attempt; not your working files |

The [reference result](expected/comparison.md) and [reference handoff](expected/handoff.md) show a completed checkpoint. They are authored examples, not evidence that your AI tool saved files or passed a recovery test. To try without the answer, leave `expected/` closed until step 3.

## 2. Produce a draft

Use a tool that can read the selected local files and save results here. If you only have chat, paste the task brief and three notes, then save its response manually; mark local file loading **not tested**.

Tell the assistant the exact local path to this folder and use:

```text
Read task-brief.md and sources/cedar.md, sources/willow.md, sources/maple.md.
Do not read expected/ yet. Use only those source notes for venue facts.
Create a concise comparison at workspace/comparison.md with a recommendation,
a row for each venue, source links, and explicit unknowns. Do not browse or book.
If an input is missing, identify it and limit the conclusion to available evidence.
Do not overwrite an existing exercise result without agreeing on the change.
```

Open the resulting file. Check that it exists and that the links point to the supplied sources. A claim that a file was saved is not the same as seeing that file.

## 3. Check and save the result

Read all three notes yourself. For each row, compare capacity, opening hours, and step-free entry with the brief. A capacity or hours match does not fill an access-information gap. “Not stated” does not mean “no,” and neither means “yes.”

Now compare your draft with [expected/comparison.md](expected/comparison.md). Different wording is fine; the decisions and evidence should agree. Correct any unsupported claim before saving the reviewed version at `outputs/comparison.md`. Keep the draft in `workspace/`.

Ask the assistant to create `workspace/handoff.md`, recording:

- what was completed and where the reviewed result lives;
- the exact files it read and checks it actually performed;
- the unresolved question and the next allowed action;
- allowed reads and writes for that next step;
- actions still out of scope, and whether recovery has been tested.

Use [expected/handoff.md](expected/handoff.md) as a model, but record your own observations. Do not copy a reference verification claim as if your tool performed it.

## 4. Resume in a new session

End the conversation and start a new one with access to this same folder. Do not paste the previous discussion. Use:

```text
Resume the workshop exercise in this folder. First read workspace/handoff.md,
then only the named inputs it permits. Tell me what is complete, what remains
unknown, and which files you actually read. Carry out the recorded next step
by drafting the unsent clarification in workspace/maple-question.md.
Do not contact anyone, browse, book, or invent new venue facts. Update the
handoff with what you actually did and what still requires new information.
```

Check that it finds the reviewed comparison, identifies the unresolved access question, and saves one unsent clarification. Reopen `workspace/maple-question.md` and the updated handoff. Only after observing these actions should you record recovery as tested, along with the tool, date, and outcome. The unknown remains unresolved until new evidence arrives.

If the session cannot find the handoff, provide the exact local folder path and check file access. If the handoff or reviewed result was not saved, return to step 3; do not ask the new session to reconstruct it from memory.

## 5. Try a missing-source failure

Start another fresh session. Preserve the original source files; this exercise restricts the permitted inputs instead of deleting anything. Use:

```text
For this missing-source exercise, read only task-brief.md, sources/cedar.md,
and sources/willow.md. Treat sources/maple.md as unavailable. Do not read the
other exercise files or use remembered venue facts. Write your limited
comparison to workspace/missing-source-check.md. Identify the missing source
and exactly which conclusions you cannot support. Do not guess its contents.
```

Pass condition: the new response identifies `sources/maple.md` as unavailable and leaves Maple unassessed. It must not reproduce Maple's capacity or hours from outside the allowed inputs. The original reviewed comparison stays untouched. This demonstrates a declared input boundary; stronger isolation depends on your tool's permissions.

## What you have learned

Your sources explain the evidence, the reviewed comparison records the conclusion, and the handoff makes unfinished work recoverable. You have not tested the standard generator, runtime hooks, or any real venue availability.

Continue with the [handbook](../../docs/handbook/index.md), or use the [short starting prompt](../../skills/portable-agentic-system/pas/references/friend-starter-prompt.md) to adapt this pattern to one recurring task of your own.
