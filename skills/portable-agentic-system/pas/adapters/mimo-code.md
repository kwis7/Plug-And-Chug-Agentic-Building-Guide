# MiMo Code Runtime Adapter

Classification: native coding-agent runtime
Repository verification: `documented_only`
Fresh-session verification: not run

MiMo Code is separate from the MiMo API provider and Xiaomi MiMo Claw. Official setup recommends running `/init`, which analyses the project and generates a root `AGENTS.md` that MiMo Code uses for project context.

Official evidence:

- https://mimo.mi.com/docs/en-US/tokenplan/integration/mimo-code
- https://mimo.mi.com/docs/en-US/news/latest/mimocode

## Adapter rules

- Start in the generated harness root and retain the canonical `AGENTS.md` rather than allowing `/init` to overwrite it silently.
- If `/init` proposes a replacement, inspect and merge only runtime-specific deltas.
- Keep MiMo Code's native persistent memory and task mechanisms separate from the portable `MEMORY.md`, task contracts, and generated `STATUS.md`; define which is authoritative.
- Treat provider login and model selection as runtime/provider configuration, not harness identity.
- Use the common closeout command through a documented hook or wrapper; otherwise label the gate advisory.

## Smoke

Record `mimo --version`, `/init` behaviour on a disposable fixture, the resulting entrypoint diff, active task recall, memory projection, one invalid closeout, and one valid closeout. Until that evidence exists, do not mark runtime-verified.
