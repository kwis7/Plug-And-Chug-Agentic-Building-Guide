# 7. Know what has actually been completed

“Done” can mean a file was created, a comparison was reviewed, a test passed, or an external action succeeded. Those claims need different evidence. A reliable workflow names the intended result before work begins and checks the evidence that corresponds to it.

For the venue exercise, completion means the comparison matches the supplied notes, the judgments follow the stated requirements, unknowns remain visible, and a usable handoff exists. It does not mean the workshop has a confirmed location. That distinction should survive both the final reply and the next session.

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

A **receipt** records what actually happened: the check, date, inputs, relevant tool version, result, and where its evidence lives. A planned command in a task file is not a receipt. For a small comparison, a short review note can be enough. Higher-consequence work may need test logs, hashes, screenshots, or a separate reviewer.

Automated checks are particularly good at explicit conditions such as a missing file or stale status page. They may not detect that a fluent conclusion misinterprets a source. In our example, checking that the word “accessibility” appears is weaker than checking whether Maple's accessibility was treated as unknown.

## Separate instructions from enforcement

An instruction can tell the agent to stop before booking. A restricted tool policy can prevent it from accessing a booking action. A validator can reject a task record with missing evidence. A runtime hook can act on that validator's result if the integration is actually loaded and behaves as expected.

These mechanisms complement one another, but they are not interchangeable. The repository's closeout gate checks structural conditions such as output presence, declared verification state, receipt paths, current status, budgets, and released locks. It does not independently determine whether every claim in a report is true. A dishonest or mistaken “passed” record still needs substantive review.

The runtime must also connect the gate correctly. A script returning an error in a terminal does not prove that the host blocks a final completion claim. That requires a fresh-session test with an intentionally incomplete task, followed by a valid one. Keep static and runtime evidence separate.

## Make partial completion useful

If Maple's source cannot be read, report which parts were checked and which remain unverified. If the task only requires an evidence-bounded comparison, “unknown accessibility” may be a correct final result. If it requires confirmed accessibility for every option, the same gap prevents completion. The task contract decides the difference.

When work cannot continue, preserve the usable files, explain the dependency, and name the next action. Use an honest failed or cancelled outcome when appropriate. Do not invent successful receipts to satisfy a gate or tidy a dashboard.

Good verification reduces ambiguity for the next person. It makes clear what they can rely on, what they should inspect, and which new evidence could change the result. The [reliability reference](../../../skills/portable-agentic-system/pas/references/textbook-reliability.md) expands the task, receipt, gate, and recovery mechanics.
