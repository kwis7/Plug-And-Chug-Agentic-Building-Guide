# Gemini CLI Runtime Adapter

Classification: native coding-agent runtime
Repository verification: `verified_static`
Fresh-session verification: not run in this repository audit

## Native contract

Gemini CLI uses hierarchical `GEMINI.md` context files. Its documented import form is:

```text
@./AGENTS.md
```

An alternative is configuring `context.fileName` to discover `AGENTS.md`; do not use both if that would double-load the same contract. `/memory show` and `/memory reload` are useful loading checks.

Official evidence:

- https://geminicli.com/docs/cli/gemini-md/
- https://geminicli.com/docs/cli/skills/
- https://geminicli.com/docs/hooks/reference/
- https://geminicli.com/docs/reference/policy-engine/
- https://geminicli.com/docs/cli/git-worktrees/

## Skills, hooks, and policies

- Use `.gemini/skills/` or `.agents/skills/` at project scope.
- The generator writes `.gemini/settings.json` with an `AfterAgent` hook. `.pas/bin/runtime_hook_gate.py` translates a gate failure into `{"decision":"deny","reason":"..."}`, which rejects the final response and asks Gemini CLI to retry.
- A direct non-zero exit from the portable gate is not by itself a portable adapter; hook input and output protocols differ by runtime.
- Bind the session to a task when multiple task manifests are active.
- Use policies for tool allow/deny/ask decisions only where the installed version documents that tier as functional.
- Do not present a project policy file as enforced if the current official docs explicitly mark that tier non-functional.

## Verification

Run the static smoke, then start a clean Gemini CLI session, inspect `/memory show`, and ask for the active task ID and prohibited actions. Record version, command, date, and output. Test one rejected invalid final response and one accepted valid closeout before setting `verified_runtime`. Regenerate the hook configuration after moving the harness because its generated command contains the original absolute root.
