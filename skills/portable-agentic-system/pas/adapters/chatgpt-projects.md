# ChatGPT Projects and Custom GPT Projection

Classification: managed workspace/configured assistant
Repository verification: `manual_projection`

Official evidence:

- https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt
- https://help.openai.com/en/articles/8554407-key-guidelines-for-writing-instructions-for-custom-gpts

## ChatGPT Project projection

- Put the compact common contract in project instructions.
- Upload only reviewed identity, system-map, active-task, compact-memory, and relevant knowledge/skill files.
- Do not upload `raw_data/`, logs, archives, credentials, or unrelated agent context by default.
- Treat project memory as runtime convenience; keep the local task manifest and reviewed outputs as the portable source of truth.
- When local writeback is unavailable, ask for complete-file or patch-formatted proposals and review them before saving.

## Custom GPT projection

- Instructions: stable role, workflow, authority, and refusal/approval boundaries.
- Knowledge: reference files, not rules or a filesystem entrypoint.
- Capabilities/apps/actions: tools and external access with explicit scope.
- Conversation starters: discoverability, not enforcement.

No local `AGENTS.md` chain or deterministic filesystem completion hook is claimed for either surface. Verification is a manual checklist covering instruction recall, knowledge retrieval, tool scope, output format, and human writeback.
