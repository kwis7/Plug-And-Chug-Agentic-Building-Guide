# Intake Questions

Ask only the next useful question. Do not ask this whole list at once.

## First Question

"What are the 2-5 recurring areas of life or work where you wish AI could remember context and keep things organised?"

Examples:

- academic research;
- job search;
- family paperwork;
- language learning;
- investment research;
- health admin;
- writing projects;
- course planning;
- household maintenance.

## Follow-Up Questions

Ask these one at a time when needed:

1. "Which of these areas contains sensitive raw documents?"
2. "Which area has repeated workflows you do every week or month?"
3. "Which area needs long-term notes or an Obsidian-style vault?"
4. "Which area is actually one project, not a permanent agent?"
5. "Where should the system folder live?"
6. "What language should the agent use by default?"

## Agent Matrix Template

| Agent | Purpose | Sensitive raw data? | First skill candidate | Vault? |
|---|---|---|---|---|
| Research Assistant | Papers, notes, citations, research ideas | Maybe | Literature review | Yes |
| Life Admin | Forms, reminders, household paperwork | Yes | Document intake | Yes |

## Safe Defaults

- Start with 2 agents, not 12.
- Create vaults by default.
- Create `raw_data/`, `workspace/`, `outputs/`, and `archive/` for every long-lived agent.
- Keep descriptions short; refine after the first real task.
