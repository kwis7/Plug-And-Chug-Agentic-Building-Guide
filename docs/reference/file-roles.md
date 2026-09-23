# Where the work belongs

Begin with the files your task needs. The learning example uses three source notes, a comparison and a handoff. The standard scaffold adds explicit task state and operational checks for recurring or concurrent work.

| Question | Usual home | Keep out |
|---|---|---|
| What is this agent responsible for? | `IDENTITY.md` and its entrypoint | Detailed session history |
| What rules apply repeatedly? | `RULES.md` and runtime policy | Temporary task updates |
| What are we doing now? | A task record and `workspace/` | Claims that a plan has already been executed |
| What helps the next session resume? | A short handoff or `MEMORY.md` | Entire transcripts and bulky sources |
| What is useful background? | `knowledge/` | Undated live prices or unverified claims presented as stable facts |
| What procedure is worth reusing? | `skills/` | Raw private material |
| Where are the named source materials? | Explicitly scoped input files | Automatic recursive loading of private folders |
| What is ready to review? | `outputs/` | Assumed authorization to send or publish |

These are roles, not mandatory folders for every task. The [handbook workspace chapter](../handbook/en/02-workspace.md) explains the small example; the [filesystem contract](../../skills/portable-agentic-system/pas/references/filesystem-contract.md) specifies the standard scaffold. A file existing on disk does not prove that a runtime read it.

Markdown (`.md`) is the text format, not an agent or an access mechanism. Entrypoint and Skill discovery depend on the host; most other filenames here are project conventions. See [the foundations chapter](../handbook/en/00-foundations.md) for how files become context and how confirmed preferences shape recurring work.
