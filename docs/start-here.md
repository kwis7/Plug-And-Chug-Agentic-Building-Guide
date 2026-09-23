# Start with one task

[English](start-here.md) | [中文](start-here.zh-CN.md) · [Home](../README.md)

You will compare three fictional venue notes, check the result, and resume the work in a new session. By the end, the useful work will be in files you can inspect: a draft, a reviewed comparison, and a short handoff.

This is a learning example. It does not generate the standard harness, install a skill, change personal settings, or contact a venue.

## Before you begin

You need a local copy of this repository and an AI tool that can read the files you select. To let it save the exercise, the tool also needs permission to write inside `examples/first-project/workspace/` and `examples/first-project/outputs/`. Use an existing tool; there is no need to change model providers.

If you use Git, the clone and `cd` commands in [Quick start, step 1](../QUICKSTART.md#1-get-the-toolkit-and-check-python) obtain the repository. Stop there for this route: you do not need Python or the generator for the learning exercise. You can also download and unpack a repository copy yourself.

An ordinary chat without local file access can help prepare the comparison if you paste the three synthetic source notes and task brief. You must save the resulting files yourself. That tests the reasoning exercise, not local loading or automatic recovery. Tool subscriptions and API usage may have their own costs.

## Start the exercise

Open your local repository in the tool, or give it the repository's exact local path. Then paste:

```text
Help me complete the learning exercise in examples/first-project/README.md.
First read that tutorial, task-brief.md, and the three named files in sources/.
Do not read expected/ until I ask to compare the reference answers.
Use only those synthetic inputs; do not browse, contact anyone, or book anything.
Save my draft and handoff in workspace/ and my checked result in outputs/.
Preserve the source notes and reference answers. If any destination file already
exists, inspect it and agree on how to continue before overwriting it.
Show me which files you actually read and how you checked the comparison.
Then guide me through the new-session recovery exercise.
```

The [example tutorial](../examples/first-project/README.md) names the exact files, gives the check criteria, and includes the restart prompt. It also includes a missing-source exercise: a useful assistant should show the gap rather than invent the absent facts.

Success means that the saved comparison follows the supplied notes, unknowns remain visible, and a fresh session finds the next step from the handoff. Merely saying “saved” is not evidence; open the files and verify the content. If you do not run the fresh-session exercise, label recovery **not tested**.

## Bring the method to your own work

Choose one recurring task and a few non-sensitive inputs you are allowed to share with your tool. The [short starting prompt](../skills/portable-agentic-system/pas/references/friend-starter-prompt.md) helps an assistant ask about your desired result, current friction, and tool capabilities before proposing changes.

Use the [handbook](handbook/index.md) to understand each decision. When you want the existing standard structure, choose the [manual toolkit route](../QUICKSTART.md#manual-standard-scaffold). The generator is a separate, larger setup; the small example is not a minimal generator profile.
