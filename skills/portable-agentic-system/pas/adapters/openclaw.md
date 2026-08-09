# OpenClaw Runtime Adapter

Classification: native agent runtime/workspace
Repository verification: `documented_only`
Fresh-session verification: not run

## Native contract

OpenClaw has native agent workspaces and bootstrap files including `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md`, and `MEMORY.md`. Do not replace this with a generic environment-variable prompt. Project the portable contract into the documented workspace files and respect OpenClaw's bootstrap character budgets.

Official evidence:

- https://docs.openclaw.ai/agent-workspace
- https://docs.openclaw.ai/agent
- https://docs.openclaw.ai/automation/hooks
- https://docs.openclaw.ai/gateway/config-agents

## Projection

- `AGENTS.md`: compact portable operating contract.
- `IDENTITY.md`: agent mission and owner boundary.
- `MEMORY.md`: bounded recovery projection, not a transcript.
- `TOOLS.md`: tool inventory and exact scopes; never store credentials.
- `workspace/skills/` or `workspace/.agents/skills/`: reviewed local skills.
- Gateway configuration: workspace path, per-agent skill allowlist, sandbox, and bootstrap controls.
- Set per-file and aggregate bootstrap character budgets so a large `MEMORY.md` or workspace file cannot silently consume the initial context.
- Configure each agent's workspace, sandbox access, tool policy, and concurrency/depth separately; a multi-agent registry is not an isolation boundary by itself.

## Enforcement caveat

Selecting a workspace is not itself a hard sandbox. Basic internal lifecycle hooks are not equivalent to typed plugin hooks that can block, rewrite, or cancel actions. Use a typed `before_agent_finalize` plugin hook or an external wrapper if you need deterministic finalisation. This repository does not generate that product-specific plugin, so OpenClaw completion gating remains advisory until the integration is implemented and exercised against the common closeout script.

## Smoke

Run OpenClaw with a disposable generated workspace. Verify bootstrap loading, agent workspace isolation, skill allowlist, one denied out-of-scope file read, one invalid closeout, and one valid closeout. Save the OpenClaw version and receipts.
