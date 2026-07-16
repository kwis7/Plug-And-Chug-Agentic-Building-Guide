---
name: academic-agentic-onboarding
description: Use when a scholar, researcher, lecturer, or other academic knowledge worker wants to start or adapt a local-first agentic system, establish an Academic Track, personalise an academic writing workflow, create a course workspace, or move the same system between Claude Cowork, Codex, WorkBuddy, and similar runtimes.
---

# Academic Agentic Onboarding

Guide the user from a small, safe local system to a tailored academic workflow. This skill is primarily for social-science scholars but is not discipline-specific.

## Load order

1. Read `references/intake-and-boundaries.md`.
2. Read the relevant public guide: `docs/academic-track.md`, `docs/lecturer-track.md`, or `docs/claude-cowork-setup.md`.
3. Read existing workspace instructions only after the user selects a folder.
4. Load named source material only when necessary for the current task.

## Start with a bounded intake

Ask one section at a time. Do not ask for sensitive source files in the intake.

1. Which recurring work should be supported first: research/writing, teaching, administration, or another domain?
2. What is the smallest recurring output that would make the system worthwhile?
3. Which material is private, regulated, unpublished, or prohibited from cloud upload?
4. Which runtime will be used now, and might the user switch later?
5. What should become durable knowledge, and what must remain task-local?

Summarise the answers and propose the smallest structure. Show the proposed tree and wait for confirmation before creating or overwriting files.

## Choose the correct building block

| Need | Use |
|---|---|
| New recurring professional domain or strong privacy boundary | focused agent |
| Repeated procedure inside one agent | skill |
| Bounded project needing focused context | project folder or subagent |
| Stable reference or settled decision | knowledge file |
| Immediate request | task prompt and task manifest |

Do not create an agent because a task has a fashionable name. Do not create a skill for a one-off request.

## Runtime portability

Keep `AGENTS.md` as the general operating contract. Add `CLAUDE.md` for Claude-family tools when useful. For Codex, use `AGENTS.md` and install or link skills locally. For WorkBuddy or another workspace agent, supply a copy-paste startup prompt that names the root files it may read.

Never treat a runtime's chat history or cloud memory as the system of record. The portable record is the local folder.

## Academic writing personalisation

When the user wants a personal writing-revision agent:

1. Ask them to choose authorised samples and retain originals privately.
2. Extract a provisional style guide with observable patterns, not vague labels.
3. Ask the user to approve or correct it.
4. Use a four-pass workflow: diagnose, revision plan, revise, self-audit.
5. Update the style guide only with repeated, user-approved preferences.

## Teaching and grading boundary

If the user requests a course workspace, use the public course template. Separate student-facing materials, instructor notes, readings, assessment references, and `secured_data`.

If the request concerns grading, process one submission at a time with only its authorised references. Produce a provisional, criterion-linked rationale and feedback for instructor review. Do not make final grade decisions, upload submissions, or mix submissions into shared memory.

## Output habit

End each onboarding or configuration step with:

1. what was created or proposed;
2. where it lives;
3. which instructions or knowledge will load next time;
4. what remains private or unverified;
5. the smallest next action.
