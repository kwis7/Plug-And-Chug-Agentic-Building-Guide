---
name: [skill-name]
description: "Perform [bounded job] for [owner/output class]. Use when [specific positive triggers]. Do not use for [nearest confusing workflows or authority boundaries]."
---

# [Skill Name]

## Use when

- [Positive trigger 1]
- [Positive trigger 2]

## Do not use when

- [Negative boundary 1; name the better route]
- [Negative boundary 2; name the better route]

## Inputs

- [Input 1]
- [Input 2]

## Output contract

- Owner: `[AGENT_OR_DOMAIN]`
- Output path: `[OUTPUT_PATH]`
- Required evidence or receipts: `[EVIDENCE]`
- Completion condition: `[VERIFIABLE_CONDITION]`

## Steps

1. Load only the named task, workspace, and source files needed for this run.
2. Run the workflow steps in order.
3. Write outputs to `[OUTPUT_PATH]`.
4. Verify the result before closing.

## Verification

- Positive prompt: `[should route here]`
- Negative prompt: `[should not route here]`
- Collision prompt: `[should route to a named neighbouring skill]`
- Artifact check: `[command or inspection]`
- Failure behaviour: return `partial` or `failed` with the missing dependency; do not report success.

## Output

End with:

- what changed;
- where the output lives;
- what was verified;
- what the next action is.
