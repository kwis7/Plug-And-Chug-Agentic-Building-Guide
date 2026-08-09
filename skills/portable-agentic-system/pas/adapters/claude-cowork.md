# Claude Cowork Workspace Adapter

Classification: workspace agent
Repository verification: `manual_projection`
Native Claude Code entrypoint behaviour: not claimed

Claude Cowork projects can hold folders, standing instructions, links, project memory, skills, plugins, and subagents. Folder access and product approval modes are real capabilities, but they are not the same contract as Claude Code's `CLAUDE.md` import chain.

Official evidence:

- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- https://claude.com/docs/cowork/guide/projects
- https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Setup

1. Create a Cowork project for one recurring domain.
2. Attach only the owning agent folder or another deliberately scoped folder.
3. Put the compact portable operating contract in project/folder instructions.
4. Add the long-term reference files or links the project actually needs; do not mount every agent.
5. Install reviewed skills or plugins only after checking their connectors, subagents, code execution, network access, and data scope.
6. Keep task manifests and reviewed outputs in the mounted local folder when local writeback is enabled.

## Boundary

Cowork sessions may run remotely and reach local folders through the desktop app. Project memory is useful runtime memory but is not automatically the same as the local portable `MEMORY.md`. Record which store is authoritative and export durable decisions to local files when required.

## Manual verification

In a disposable project, verify folder scope, project instructions, skill invocation, deletion confirmation, one out-of-scope read, task writeback, and an invalid-versus-valid closeout workflow. Save screenshots or exportable receipts; do not describe a manual projection as a native local entrypoint adapter.
