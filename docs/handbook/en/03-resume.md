# 3. Pick up where you left off

Continuity is something you can test. Close the original conversation, start a fresh session, and see whether the saved files support the next step. This is more informative than asking the original model whether it will remember.

For the venue exercise, the task is already useful as a comparison. The handoff should prevent a later session from treating it as a completed booking or silently converting Maple's unknown into a positive answer.

## Leave a handoff with a next action

A handoff is a short working note, not a transcript. It should tell a newcomer what the task was, what exists, why the result stands, and what would change it. For example:

```text
Task: compare three fictional venues for 16 people after 18:00;
step-free entry is required.
Result: outputs/comparison.md. Draft: workspace/comparison.md.
Sources: sources/cedar.md,
sources/willow.md, sources/maple.md.
Checked: capacities, hours, and accessibility statements.
Decision: Cedar meets the recorded requirements; Willow fails
the hours requirement; Maple's accessibility remains unknown.
Limit: synthetic notes only. Availability, price, and exact event
duration are unverified. No contact or booking is authorised.
Next: verify the reviewed result exists, then draft one unsent
question about Maple's step-free entrance in workspace/maple-question.md.
Read only this handoff, task-brief.md, the reviewed result,
and the three named sources. Write only the question and this handoff.
Recovery: not tested until a fresh session is observed.
```

This note preserves a decision and its limits without preserving all the drafting conversation. The reference handoff in [`expected/handoff.md`](../../../examples/first-project/expected/handoff.md) is a model to compare against, not a replacement for recording what your own session actually checked.

## Run the restart exercise

Open a fresh session in the practice copy, or explicitly supply its handoff and named sources. Ask it to read `workspace/handoff.md`, inspect only the permitted files, and state the current result and unresolved issues. Then carry out the recorded next step: save one unsent question about Maple's step-free entrance at `workspace/maple-question.md` and update the handoff. No browsing, contact, or booking is allowed.

A successful restart finds the reviewed result, identifies Cedar as the supported candidate, preserves Maple's unknown, and recognises Willow's hours problem. Reopen the new question and updated handoff before recording recovery as tested with the tool, date, and observed outcome. Drafting a question does not answer it. If a named input is absent, the session should report that gap rather than reconstruct missing evidence from memory.

To practise failure handling safely, follow the tutorial's missing-source prompt in another fresh session. Permit only `task-brief.md`, `sources/cedar.md`, and `sources/willow.md`; declare Maple's note unavailable without deleting it. Exclude other exercise files and remembered facts. Save the limited comparison at `workspace/missing-source-check.md`, leaving Maple unassessed and the reviewed result untouched. This tests a declared input boundary; mechanical isolation depends on the tool's permissions.

## Recover before repeating

Interruptions often leave partial work. Before retrying, inspect the draft, reviewed result, and `workspace/handoff.md` to identify the last successful step. A missing reviewed result sends you back to review; a partial draft is not a checked output. Repeating a read or regenerating a disposable draft is usually straightforward. Repeating an external action can create a duplicate booking, message, or payment.

When an external operation has an uncertain result, first check the external record. A timeout means the response was not received; it does not prove that nothing happened. The fictional exercise has no external actions, but practising the distinction makes later workflows safer.

For larger work, the toolkit records state in `tasks/<task-id>/task.yaml` and generates `STATUS.md` from it. That adds explicit scope, verification, and lifecycle fields. The underlying habit remains the same: record current truth once, preserve useful partial work, and leave the next action precise enough that another session can continue without guessing.
