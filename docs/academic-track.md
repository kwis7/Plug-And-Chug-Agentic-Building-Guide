# Academic Track

**Primary audience:** social-science scholars; adaptable to all academic fields
**Author:** [@kwis7](https://github.com/kwis7)

This track turns the general local-first system into a research-and-writing workspace. It does not replace a reference manager, institutional storage, or research ethics procedures. It makes the AI-facing working layer easier to inspect and continue.

## Recommended starting structure

```text
Academic Control Center/
├── AGENTS.md
├── CLAUDE.md
├── RULES.md
├── SYSTEM_MAP.md
├── STATUS.md
├── knowledge/
│   ├── academic-standards.md
│   └── cross-agent-skill-map.md
└── Research-and-Writing-Agent/
    ├── knowledge/
    │   ├── source-quality-policy.md
    │   ├── author-style-guide.md
    │   ├── methods-and-concepts/
    │   └── project-briefs/
    ├── skills/
    ├── raw_data/                 # private originals; ignored by Git
    ├── workspace/                # temporary analysis and drafts
    ├── outputs/                  # reviewed deliverables
    └── archive/
```

Copy the public [academic control-centre template](../templates/academic-control-center/) and personalise the role files before importing any private material.

## A source hierarchy that prevents overclaiming

For each research task, identify the best available source class before asking for a synthesis:

1. primary sources, official datasets, registered materials, or original studies;
2. peer-reviewed research and systematic reviews;
3. reputable institutional reports;
4. credible explanatory sources;
5. unverified web content, used only as leads.

The agent should distinguish what a source says, what you infer from it, and what requires further verification. Never ask it to invent citations, page numbers, results, quotations, or causal claims.

## Build an author-style reference guide

1. Select several published or otherwise authorised writing samples that represent work you want to continue.
2. Keep originals in a private location. Do not commit them to a public repository.
3. Ask the agent to extract a *provisional* guide: argument architecture, paragraph openings, use of literature, hedging, transitions, sentence rhythm, preferred vocabulary, and common revision habits.
4. Review the guide yourself. Delete traits that are accidental or context-specific.
5. Save the approved version as `knowledge/author-style-guide.md`.
6. Use staged revision: diagnosis → plan → revision → self-audit against the guide.
7. Update the guide only after you repeatedly approve a pattern.

This is personalisation by explicit reference and feedback, not a claim that the underlying model has been fine-tuned on private work.

## A research task contract

Before a complex request, create a small `task.yaml` or task brief that answers:

- What is the research question or deliverable?
- Which files are authoritative?
- What source standard is required?
- What kind of claim is allowed: description, interpretation, causal inference, or speculation?
- What output format is required?
- What must be verified before the output leaves `workspace/`?

This lets a fresh session work carefully without loading an entire career's context window.

## Suggested skills to create first

| Repeated need | First skill |
|---|---|
| Literature triage | source inventory, relevance matrix, citation verification checklist |
| Conceptual writing | argument-map and counterargument review |
| Methods work | analysis plan reviewer that separates code, assumptions, and results |
| Manuscript revision | staged academic writing revision against your style guide |
| Research administration | meeting-to-action log with owner, deadline, and uncertainty fields |

Use `pas-create-skill` only after performing the workflow manually enough times to know its true inputs and failure modes.

## First-session prompt

```text
Read AGENTS.md, RULES.md, SYSTEM_MAP.md, STATUS.md, and the relevant agent's
IDENTITY.md and knowledge/README.md. Do not read raw_data unless I name a file.
Ask the Academic Track intake questions one section at a time. Propose the
smallest usable Research-and-Writing-Agent structure, show it to me, and wait
for confirmation before creating or overwriting files.
```

Continue with [Claude Cowork setup](claude-cowork-setup.md) or the main [field guide](agentic-systems-field-guide.md).
