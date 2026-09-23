# Workshop exercise — reference handoff

This is a completed-checkpoint example, not a log from your tool. In your own `workspace/handoff.md`, record only files and checks that actually exist. Paths below are relative to `examples/first-project/`.

## State to preserve

- Task: compare three fictional venues for 16 people after 18:00 with step-free entry.
- Checkpoint: the comparison has been reviewed against the three supplied source notes. The reviewed learner result belongs at `outputs/comparison.md`; the draft belongs at `workspace/comparison.md`.
- Conclusion: shortlist Cedar Hall on the recorded requirements; Willow Room's hours do not fit; Maple Studio's step-free entry is unknown.
- Open information: Maple's entry access. Event date, duration, price, booking terms, and date-specific availability were not supplied. No venue is confirmed bookable.
- Exercise scope: synthetic data only; no external research, communication, or booking.

## Evidence and limits

The reference answer compares capacity, hours, and step-free entry with each source, and links every venue row to its note. This is an authored checkpoint. It is not evidence that a particular runtime read the files, saved a result, or resumed work. Fresh-session recovery in your setup: **not tested until observed**. No hooks or external actions are tested by this example.

## Next step

Read the permitted inputs below. Check that the reviewed result exists and matches this checkpoint; if it does not, report the gap and return to the review step. Draft **one unsent question** asking whether Maple Studio provides step-free entry during its recorded evening hours. Save it at `workspace/maple-question.md`.

Then update `workspace/handoff.md` with the files actually read, the new local output, and the outcome observed. Keep the access question unresolved: drafting a question is not obtaining an answer. Do not contact anyone.

## Allowed reads for this step

- `workspace/handoff.md`
- `task-brief.md`
- `outputs/comparison.md`
- `sources/cedar.md`
- `sources/willow.md`
- `sources/maple.md`

Do not load `expected/`, unrelated folders, or other sources to fill a gap. If a named input is missing, identify it and limit the conclusion accordingly.

## Allowed writes for this step

- `workspace/maple-question.md`: the unsent clarification.
- `workspace/handoff.md`: actual progress and remaining information gap.

Preserve all source notes and the reviewed comparison. No browsing, sending, booking, personal data, credentials, or settings changes are required or allowed by this exercise.
