# 1. Finish one small task

You are planning a workshop for 16 people after 18:00, and everyone must be able to enter without steps. Before contacting a venue, you want to know which options meet those requirements and which need more information. A short comparison is enough for this decision. A booking would require additional facts and separate permission.

The [first-project exercise](../../../examples/first-project/README.md) supplies three synthetic venue notes. These are fictional examples, not real businesses or verified live information. Use them to practise working from sources without browsing, sending messages, booking or making payments. None of those actions is authorised by the exercise.

If you have chosen your own task in the [beginner guide](../../start-here.md), follow the same method with its agreed inputs and result. The venue example shows the reasoning in a form you can inspect; it is optional practice.

## Know the result you want

A ranking alone would conceal a crucial difference: one venue fails a requirement, while another has an unanswered question. Ask for a comparison that shows the source facts before explaining the judgment. Applying the same requirements to each candidate makes the conclusion easier to inspect.

| Venue | Capacity | Recorded hours | Step-free entry | Judgment |
|---|---|---|---|---|
| Cedar Hall | 18 | 18:00-21:00 | Yes | Meets the recorded requirements |
| Willow Room | 24 | 09:00-17:00 | Yes | Fails the evening-hours requirement |
| Maple Studio | 20 | 18:00-22:00 | Unspecified | Cannot confirm accessibility |

Cedar Hall meets all three requirements on the supplied facts. Willow Room has enough space, but its recorded hours end before the workshop begins. Maple Studio has enough space and evening hours; the note gives no accessibility information, so its suitability remains uncertain. Missing evidence of step-free entry does not establish that an entrance has steps.

These notes also leave other questions open. They do not establish availability on a particular date, the workshop's duration, price or booking terms. The comparison can identify a suitable candidate for further investigation. It cannot supply the missing facts needed for a booking.

## Choose an available working route

Use an AI tool you already have and check what it can access. Direct file work requires permission to read the exercise files and write inside the working copy you choose. If your interface accepts only pasted text or uploads, supply the three notes and save the returned Markdown yourself. You can still examine the comparison, but filesystem loading and writeback remain manual and untested. Normal model or API usage costs may apply; the exercise needs no paid data service.

To preserve the bundled references, copy the exercise into a local practice folder and identify that copy as the place the agent may change. From the exercise root, give it this assignment:

```text
Read task-brief.md, sources/cedar.md, sources/willow.md,
and sources/maple.md. Do not read expected/ yet.
Compare the fictional venues for 16 people after 18:00,
with step-free entry required. Use only the supplied notes.
Write workspace/comparison.md with source links, judgments,
and unknowns. Identify missing inputs instead of guessing.
Do not browse, contact, or book. Agree on any overwrite first.
```

Start by producing your own draft, with the reference answers still closed. In a chat-only interface, save it yourself and record that local file loading was not tested. The files `expected/comparison.md` and `expected/handoff.md` show what a checked exercise might contain. Their presence in the repository says nothing about whether your attempt succeeded.

## Review before accepting

Open `workspace/comparison.md` and follow its source links to the three files under `sources/`. Check the capacities and time windows against the notes. Then examine how the requirements were applied: all three venues have enough capacity; Cedar and Maple have evening hours; Cedar alone also has a recorded step-free entrance. Once you have reviewed that reasoning, compare your result with `expected/comparison.md`.

If the draft recommends Maple without qualification, ask what establishes its accessibility. The note cannot answer that question. Correct the entry to "unknown," revise the recommendation and record the repair. This is a useful review habit: follow an important conclusion back to the specific fact it needs, rather than judging the answer by how convincing the prose sounds.

After any corrections, save the checked version at `outputs/comparison.md` while preserving the draft. The handoff at `workspace/handoff.md` should say what was checked, what remains unknown, which inputs and writes are permitted, and what to do next. Here the next step is to draft an unsent question about Maple's entrance. Drafting it does not obtain an answer or authorise sending it.

You now have a result and the information needed to continue. Recovery remains untested until you actually try it in another session. Likewise, a real booking decision would still require new information and separate authority. The next chapter explains how the files preserve these distinctions.
