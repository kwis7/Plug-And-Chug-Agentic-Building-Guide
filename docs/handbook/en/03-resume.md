# 3. Pick up where you left off

The reviewed comparison leaves a specific job unfinished: finding out whether Maple has a step-free entrance. Another session can prepare that question if it can find the result, understand the gap and see what you have authorised next. You can name the handoff file and ask it to continue from there.

Try this by closing the original conversation and starting a fresh one. The saved files should support the next step on their own. Pay particular attention to the status of the work: Cedar is a candidate supported by the supplied notes, Maple's entrance remains unknown, and no venue has been booked. A promise from the original model to remember these details gives you less evidence than watching a new session use the records correctly.

## Leave a handoff with a next action

Write the handoff while the outcome is still clear to you. Include the requirements, the files containing the result and its sources, the checks you performed, and the unresolved issue. Then specify the next permitted action. A later reader needs enough information to check the decision and continue; you can leave out the discarded wording and other drafting details. For example:

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

The file paths let the next session inspect the basis for the decision. The limits explain why drafting a question is appropriate while contacting or booking a venue is not authorised. Compare your note with [`expected/handoff.md`](../../../examples/first-project/expected/handoff.md), then make sure your own version describes checks you actually performed. The reference is a teaching example; copying it does not establish that those checks happened in your session.

## Run the restart exercise

Open a fresh session in the practice copy and ask it to begin with `workspace/handoff.md`. If your interface requires you to supply the files, provide the handoff and its named sources explicitly. Have the session inspect only the permitted files and explain the current result and unresolved issue before continuing. Its next job is to save one unsent question about Maple's step-free entrance at `workspace/maple-question.md` and update the handoff. The exercise allows no browsing, contact or booking.

Check the explanation against the reviewed comparison. Cedar should still be the supported candidate, Willow should still fail the hours requirement, and Maple's entrance should still be unknown. Reopen the question and the updated handoff to see whether the files were saved as intended. Record the tool, date and observed outcome before marking recovery as tested. Saving that draft leaves Maple's entrance status unresolved. Any missing input should be reported as a gap; remembered facts cannot replace evidence the task requires the session to read.

You can also rehearse a restart with incomplete inputs. In another fresh session, use the tutorial's missing-source prompt: permit only `task-brief.md`, `sources/cedar.md` and `sources/willow.md`, and declare Maple's note unavailable. Leave the original note in place, exclude the other exercise files and remembered facts, and save the limited comparison at `workspace/missing-source-check.md`. Maple should be unassessed in this result, while the original reviewed comparison remains untouched.

That exercise shows whether the session follows the declared input scope. To establish that it cannot access the excluded files, you would also need evidence from the tool's permissions. Keeping a source out of the prompt does not itself make the file inaccessible.

## Recover before repeating

After an interruption, inspect the draft, reviewed result and `workspace/handoff.md` before starting over. Suppose the draft exists but the reviewed result is missing. The next step is review, even if the draft looks finished. Finding the last successful step preserves useful work and prevents a partial result from being mistaken for a checked one.

Repeating a read or recreating a disposable draft is usually straightforward. External actions need more care. If a booking request times out, the response may have failed to reach you after the service accepted the booking. Check the external record before repeating the action; otherwise a retry could produce a duplicate booking, message or payment. Any new booking, message or payment also needs the appropriate authorisation. Our fictional exercise performs none of them, but its handoff gives you a place to learn how to record action status accurately.

For larger projects, the toolkit stores state in `tasks/<task-id>/task.yaml` and generates `STATUS.md` from it. The additional fields make scope, verification and lifecycle explicit. A small handoff can serve the first exercise: keep the current state in one place, preserve usable partial results, and identify the files and permitted action needed to continue.
