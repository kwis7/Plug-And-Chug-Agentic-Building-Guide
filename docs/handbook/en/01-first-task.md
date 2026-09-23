# 1. Finish one small task

This chapter uses the optional fictional exercise to make the method visible. If you have already chosen your own task in the [beginner guide](../../start-here.md), use the same sequence—agree on the result, work from named inputs, check, save and leave a handoff—with that task.

Suppose you are planning a workshop for 16 people after 18:00. Everyone must be able to enter without steps. Before anyone contacts a venue, you want a short comparison that distinguishes a suitable candidate from an unsuitable or uncertain one.

The [first-project exercise](../../../examples/first-project/README.md) contains three synthetic source notes. They represent fictional venues, not real businesses or verified live information. The assignment is a source-comparison exercise; it grants no permission to book, send messages, or make payments.

## Know the result you want

A useful answer is more than a ranking. It should show the recorded facts, apply each requirement consistently, explain the resulting judgment, and preserve what remains unknown.

| Venue | Capacity | Recorded hours | Step-free entry | Judgment |
|---|---|---|---|---|
| Cedar Hall | 18 | 18:00–21:00 | Yes | Meets the recorded requirements |
| Willow Room | 24 | 09:00–17:00 | Yes | Fails the evening-hours requirement |
| Maple Studio | 20 | 18:00–22:00 | Unspecified | Cannot confirm accessibility |

Cedar Hall is the suitable candidate on the supplied facts. That is a bounded conclusion. It does not establish availability on a particular date, the duration of a workshop, price, or booking terms. Maple Studio's missing accessibility statement is an unknown; it is not evidence that the venue is inaccessible. Willow Room's larger capacity does not compensate for its hours.

## Choose an available working route

Use an AI tool you already have. For direct file work, it must be able to read the exercise files and write inside your chosen working copy. Check its actual permissions before starting. If your interface only accepts pasted text or uploads, provide the three notes explicitly and save the returned Markdown yourself. That route still teaches the method, although filesystem loading and writeback remain manual. Your existing model or API usage may carry its normal costs; the exercise itself needs no paid data service.

Copy the exercise into a local practice folder if you want to preserve the bundled reference files. Tell the agent exactly which copy it may change. From the exercise root, a suitable assignment is:

```text
Read task-brief.md, sources/cedar.md, sources/willow.md,
and sources/maple.md. Do not read expected/ yet.
Compare the fictional venues for 16 people after 18:00,
with step-free entry required. Use only the supplied notes.
Write workspace/comparison.md with source links, judgments,
and unknowns. Identify missing inputs instead of guessing.
Do not browse, contact, or book. Agree on any overwrite first.
```

The tutorial agent first creates the draft. In a chat-only interface, you perform that saving step and mark local file loading untested. The repository's `expected/comparison.md` and `expected/handoff.md` are reference answers, not proof that your own exercise has been completed. Leave them closed until you have attempted the draft.

## Review before accepting

Open your `workspace/comparison.md` and follow its links to the three files under `sources/`. Confirm the capacities and time windows yourself. Then inspect the reasoning: all three have enough capacity, only two have evening hours, and only Cedar has both evening hours and a recorded step-free entrance. You can now compare it with `expected/comparison.md`.

If the answer says Maple is suitable, ask which source establishes its accessibility. The correct repair is to mark that requirement unknown, revise the judgment, and record the correction. A polished paragraph cannot fill a missing source field.

After review and any corrections, ask the agent to save the checked version at `outputs/comparison.md`, preserving the draft. Then have it create `workspace/handoff.md` with the actual checks, remaining unknowns, permitted inputs and writes, and next step: an unsent clarification question about Maple's entrance. Record recovery as untested until you observe it. A real booking decision still requires new information and separate authority.
