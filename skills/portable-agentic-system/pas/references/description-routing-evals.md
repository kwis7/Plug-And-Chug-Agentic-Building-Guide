# Description and Routing Evaluations

Descriptions are routing inputs, not promotional summaries. A good description states the job, concrete triggers, exclusions, required inputs, output class, and meaningful permission boundary.

## Description template

```yaml
description: Perform [job] for [specific recurring situations]. Use when [positive triggers and symptoms], including [examples]. Do not use for [near-neighbour exclusions]. Requires [key inputs] and produces [output class]. [Approval or data boundary when material].
```

## Evaluation card

For every skill or persistent subagent, create:

- three clearly positive prompts;
- three clearly negative prompts;
- three near-neighbour collision prompts;
- expected route and reason;
- observed route, runtime, version, and date;
- pass/fail and revision note.

## Example

Target: `investment-research`

Positive:

1. “Review this company's filing, catalysts, valuation, and risks.”
2. “Refresh the evidence behind my thesis and list invalidation conditions.”
3. “Build a source-backed research brief; do not trade.”

Negative:

1. “Place an order for 20 shares.”
2. “Rewrite this scholarship essay.”
3. “Summarise this biology paper for class.”

Collision:

1. “Analyse this broker statement and explain the tax forms.”
2. “Turn the investment report into a polished slide deck.”
3. “Monitor a public company but do not send alerts yet.”

The expected result may be investment research, tax/admin, design, or monitoring based on owner, output, and authority. Record why one route wins and whether a handoff is needed.

## Collision audit

Search all installed descriptions for repeated nouns and trigger phrases. Review pairs that share both an input and output class. Resolve collisions by tightening ownership, exclusions, or output responsibility rather than adding arbitrary priority numbers.

## Failure patterns

- “Helps with research” is too vague.
- A list of capabilities without situations does not explain when to invoke.
- Trigger rules hidden only in the body cannot help metadata-based discovery.
- Two agents that both “analyse data and create reports” need distinct owners or boundaries.
- A description that implies external sending or financial action without approval boundaries is unsafe.
