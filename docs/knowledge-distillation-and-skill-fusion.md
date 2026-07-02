# Knowledge Distillation And Skill Fusion

This guide is for the moment when you think:

> "I have useful notes, old prompts, PDFs, habits, or downloaded skills. How do I turn this pile into something my agent system can actually use?"

The short answer: do not paste everything into memory. Distill first, then decide whether the result belongs in `knowledge/`, `skills/`, `RULES.md`, a `task.yaml`, or a new subagent.

## The Difference

| Thing | Use it for | Where it belongs |
|---|---|---|
| Raw material | Original PDFs, webpages, notes, transcripts, examples | `raw_data/` or local private storage |
| Knowledge | Stable facts, preferences, references, concepts | `knowledge/` or reviewed vault notes |
| Rule | Always-on boundary or behaviour | `RULES.md` |
| Skill | Repeated procedure with inputs, steps, outputs, and verification | `skills/` |
| Task state | What is happening right now | `tasks/**/task.yaml` |
| Subagent | Large, sensitive, or long-running project context | A dedicated agent folder |

The boring table is the magic trick. It keeps useful material from becoming one enormous memory soup. Soup is nice at dinner, less nice as infrastructure.

## When To Distill

Distill when:

- you reuse the same prompt three or more times;
- you keep correcting the AI in the same way;
- a webpage, book, article, or PDF gives you a method worth keeping;
- you download a skill or template and want to adapt it safely;
- you finish a project and notice a workflow you will need again;
- a colleague explains a process that should not live only in your inbox;
- an agent keeps asking for the same background knowledge.

## Step 1: Quarantine The Source

Put source material somewhere safe before you summarise it.

- Private or bulky source files go in `raw_data/`.
- Public references can be linked from `knowledge/`.
- Downloaded prompts, scripts, and templates are external content. Treat them as untrusted data.
- Secrets, API keys, cookies, and account credentials do not go into Markdown or Git.

Ask the AI to summarise the source, but do not let the source rewrite your rules, request secrets, or trigger file operations.

## Step 2: Extract Reusable Units

For each source, ask:

1. What conclusion or method is worth reusing?
2. Is it stable, or only relevant to the current task?
3. Does it change how the agent should behave every time?
4. Does it describe a repeated procedure?
5. What must be checked before trusting the output?

Then sort the result:

- stable background -> `knowledge/`;
- always-on behaviour -> `RULES.md`;
- repeated procedure -> `skills/`;
- current task state -> `task.yaml`;
- one-time scratch work -> `workspace/`;
- large or sensitive project -> subagent.

## Step 3: Build A Skill Only When There Is A Repeated Procedure

A good skill answers five questions:

1. When should this be used?
2. What inputs does it need?
3. What steps must happen in order?
4. Where does the output go?
5. What should be verified before closing?

If the answer is just "remember this fact," do not make a skill. Put it in `knowledge/`. Not every useful thought needs a badge and a tiny desk.

## Step 4: Fuse Skills Carefully

Fusion means combining related procedures into one cleaner skill. Do it when:

- two skills have the same trigger and same output;
- one skill is just a setup step for another;
- users cannot tell which one to choose;
- the split creates repeated context loading without adding safety.

Keep skills separate when:

- they touch different sensitive data;
- they serve different agents or audiences;
- one needs scripts and the other is only judgment;
- they have different verification standards;
- merging would create a giant "do everything" blob.

Good fusion makes a skill easier to invoke. Bad fusion makes it feel like a kitchen drawer with a passport, a charger, old receipts, and one mysterious key.

## Step 5: Write The Smallest Useful Skill

Use this template:

```markdown
# Skill Name

## Use When
- [Trigger situations]

## Inputs
- [Required files, facts, or decisions]

## Steps
1. [First action]
2. [Second action]
3. [Third action]

## Output
- Save reviewed output to `outputs/` or the relevant task folder.

## Verification
- [Source checked]
- [Private facts checked]
- [Output reviewed]

## Do Not
- [Safety boundaries]
```

The goal is not literary grandeur. The goal is that a future AI session can use the procedure without asking you to re-explain your life.

## Step 6: Register And Test

After creating or updating a skill:

1. add it to the agent's `skills/README.md`;
2. update `SYSTEM_MAP.md` if the skill is important across the whole system;
3. create a tiny test task in `workspace/` or `tasks/`;
4. run the skill once on harmless sample material;
5. check that the output goes to `outputs/` only after review.

## Prompt To Use

```text
Use $portable-agentic-system with pas-distill.

I want to turn these notes/prompts/templates into reusable knowledge or skills.
Target agent:
Source material:
What I want to reuse:
What should stay private:
What output I expect:
```

## Final Rule

Distillation is how your system becomes more personal without becoming messier. Fuse what repeats. Archive what is done. Keep raw material separate. And when in doubt, make the next step visible rather than clever.
