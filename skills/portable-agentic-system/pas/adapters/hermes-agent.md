# Hermes Agent Runtime Adapter

Classification: native agent runtime
Repository verification: `documented_only`
Fresh-session verification: not run

## Native contract

Hermes reads a top-level `AGENTS.md` at the working directory and can discover nested instruction files as work enters those directories. It has native skills and deliberately bounded memory files.

Official evidence:

- https://hermes-agent.nousresearch.com/docs/guides/tips
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/

## Projection

- Keep the portable root `AGENTS.md` within the stricter repository budget.
- Install reviewed skills under `$HOME/.hermes/skills/` or expose `$HOME/.agents/skills/` when desired.
- Generate a Hermes-specific compact memory projection within the documented character limits. Do not copy the full 12 KiB portable memory into it.
- Treat external skill directories as writable whenever filesystem permissions allow it; “external” does not mean protected.

## Gate and smoke

Use a wrapper or supported completion mechanism to call `closeout_gate.py`. In a disposable fixture, verify top-level and nested instruction discovery, bounded memory failure, protected skill write behaviour, invalid closeout blocking, and valid closeout acceptance before changing the compatibility label.
