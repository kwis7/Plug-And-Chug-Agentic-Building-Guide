# 7. Know what has actually been completed

The venue exercise ends with a reviewed comparison and a usable handoff. Each judgment should follow the supplied notes and the stated requirements, with unknowns still visible. Cedar can be shortlisted on that basis. Date-specific availability and booking remain unconfirmed, so the next session must still understand that no workshop location has been secured.

This illustrates why completion needs to be defined at the start. A saved draft, a reviewed answer and a successful external action are different results. If you know which result the task requires, you can choose the checks that would support it and report how far the work actually got.

## Match the check to the claim

| Claim | Evidence to look for |
|---|---|
| A result was saved | Open the exact file and inspect its contents |
| A comparison is supported | Trace material facts and judgments to the sources |
| A script passed | Record its command, exit status, and relevant output |
| A document is usable | Render it, inspect pages, and test navigation |
| A runtime loaded instructions | Observe a fresh session using the intended entrypoint |
| A completion gate works | Observe invalid and valid cases in that runtime |
| An external action succeeded | Check the service's authoritative result or readback |

A **receipt** keeps a record of a check you performed: the date, inputs, relevant tool version, result and location of the evidence. Listing a command in the task file records an intention. After running it, you can record the outcome. A short review note may be enough for the venue comparison; work with greater consequences may need logs, hashes, screenshots or a separate reviewer.

Consider what an automated file check would tell you here. It could establish that the comparison exists or that the status page is current. The document could still contain a fluent claim that Maple has step-free access. Detecting that mistake requires checking the judgment against the source. Searching for the word "accessibility" would find the mistaken sentence as readily as the correct one.

## Separate instructions from enforcement

The instruction to stop before booking gives the model a rule to follow. A restricted tool policy can also make the booking action unavailable. A validator has a different job: it can reject a task record when required evidence is missing. You can use these mechanisms together, provided you understand which part of the workflow each controls.

The repository's closeout gate checks structural conditions: output presence, declared verification state, receipt paths, current status, budgets and released locks. A task can satisfy those conditions while its report still misinterprets a source. Content review is needed to detect a mistaken or dishonest `passed` record; the gate does not independently determine whether every claim is true.

To use the gate during task completion, the runtime must be connected to it. A runtime hook can act on the validator's result when the integration is loaded and behaves as intended. Running the script in a terminal and seeing an error establishes that the script rejected that case. It leaves open whether the host would call it and block a final completion claim.

Test that connection in a fresh session with an intentionally incomplete task, followed by a valid one. Save the observed host behavior separately from the static checks. If the connection has not been tested, keep that part of the completion claim unverified.

## Make partial completion useful

If Maple's source cannot be read, state which sources were checked and leave Maple unassessed. If the note was read but omitted the entrance information, record accessibility as unknown. Both situations leave a gap, but they require different next inputs. The handoff should make that difference clear.

Whether the gap prevents completion depends on the task. A comparison limited to the supplied evidence can correctly leave accessibility unknown. A task requiring confirmed accessibility for every option cannot finish with the same gap. Use the original completion criteria to decide; changing them merely to obtain a pass would obscure what remains undone.

When work has to stop, preserve the useful files and describe the dependency and next action. An honest failed or cancelled outcome can retain checked material for later use. Inventing successful receipts would hide the reason the task stopped and give the next session an unreliable starting point.

In the handoff, distinguish results that can be reused from checks that still need to be performed. Explain what evidence would allow the work to continue. The [reliability reference](../../../skills/portable-agentic-system/pas/references/textbook-reliability.md) gives further detail on tasks, receipts, gates and recovery.
