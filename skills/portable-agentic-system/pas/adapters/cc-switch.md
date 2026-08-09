# CC Switch Switchboard Adapter

Classification: provider/CLI configuration manager and local routing switchboard
Repository verification: `switchboard_only`

Official evidence:

- https://ccswitch.io/en/
- https://github.com/farion1231/cc-switch

## What CC Switch owns

- Provider records, endpoints, model selections, and supported CLI configuration files.
- Optional local proxy/routing, failover, request logs, token counts, latency, and cost estimates.
- Skill distribution features offered by the installed version.

## What the portable harness owns

- Agent identity, ownership, rules, and authority.
- Task contracts, status, verification receipts, handoffs, and completion gates.
- Memory, knowledge, raw material, workspaces, artifacts, logs, and reviewed outputs.
- Resource locks and worktree claims.

Do not call CC Switch a second harness layer. It is one component inside or adjacent to the harness. Switching a model changes the active employee; it does not replace the company's rules, files, work orders, archives, or quality gates.

## Safe integration

1. Configure provider credentials only in CC Switch or an approved secret store.
2. Open the same harness root in the selected runtime.
3. Let that runtime load its native entrypoint.
4. Record optional model policy in the task without pretending the field changes CC Switch automatically.
5. Import usage data read-only and only with user consent. Never copy keys or raw request bodies into harness Markdown.

Verification must separately prove: CC Switch provider routing, target runtime entrypoint loading, and portable task/gate persistence.
