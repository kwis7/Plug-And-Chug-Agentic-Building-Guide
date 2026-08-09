# Simple Starting Prompt

Give your agent both of the following:

1. the main repository link: <https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide>
2. the prompt below

Ask it to read the repository as a guide and help you build the system gradually. It should interview you, propose one stage at a time, wait for approval before material changes, and leave you with a system you understand rather than generating a large unexplained structure all at once.

```text
Use the Agent Harness Builder skill and guide me one stage at a time.

First explain the company metaphor: I am the board/owner, the active model is a replaceable employee, and only a central coordinating model in a multi-agent setup is the manager. Treat all configuration - rules, identity, skills, tools, tasks, status, memory, knowledge, files, adapters, gates, budgets, locks, and validation - as parts of the harness.

Interview me to identify 2-5 recurring work domains, data/privacy boundaries, the runtime(s) I actually use, desired outputs, and actions requiring approval.

Recommend the smallest useful agent structure. Distinguish memory from the long-term knowledge archive and current workspace. Then show me the proposed folder tree, task schema, completion gate, memory/file budgets, resource-lock policy, and runtime compatibility status before writing anything.

After I approve the design, generate the system, run static validation and available fresh-session smoke tests, label anything unverified or provisional, and give me exact file paths plus the next smallest step.

Do not install tools, use credentials, upload private data, publish, delete, commit, push, or take external actions without my explicit approval.
```
