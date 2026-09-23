# Before the first task: how an agent works

You ask an AI assistant to compare three sources. It reads files, writes a table, checks a missing detail, and saves a note for next time. Which part did the work: the model, the Agent, the prompt, or a Skill?

Each contributed something different. Understanding those contributions helps you build a useful system without mistaking a folder for a capability or a good prompt for a guarantee. Here, an **agent** means a role carried out through a model, instructions, working state, available tools, and an execution loop. The exact implementation varies. An agent can operate in one session without local files, and it does not require other agents.

## Read the diagram as a working company

The diagram below presents the repository's complete design. It is a map of possible responsibilities, not a requirement to build every box before starting.

![The active model inside the user's configured harness.](../../assets/harness-concept-map.png)

At the top, **you are the owner**: you choose goals, control your materials, and authorise consequential actions. In the middle, the **model is the active employee**: it interprets the material supplied to it, reasons about the request, and proposes a response or tool call. The model is not the company, its records, or its permissions.

An **Agent is a working role**, such as a research assistant responsible for comparing sources. Its instructions describe the assignment and boundaries; its state records progress; its tools provide available operations. The same model can fill several roles in separate sessions with different context and permissions. Different models can also fill the same role over time. A name such as “Research Agent” does not create a separately trained model.

The surrounding **harness** is the configured environment that makes this work possible: rules, files, procedures, tools, state, and checks. In the diagram, these arrangements and the active model occupy one system boundary. Replacing the model can preserve the surrounding work, although a new runtime may need different adapters and verification.

The company analogy helps distinguish responsibilities. Skills resemble playbooks, tools resemble equipment, memory resembles a short handover, and knowledge resembles a reference library. A coordinating model is a manager only when several roles need routing or integration. It is still a model in a bounded role, not a necessary extra layer or a higher source of authority.

None of this implies consciousness, loyalty, permanent memory, or automatic access. The diagram's quality controls are effective only where the corresponding software is implemented and verified. A written policy and a mechanically blocked action are different things.

## Keep the core terms separate

| Term | Its job in the system |
|---|---|
| Model | Interprets supplied context and generates responses or proposed actions |
| Agent | Carries a role through instructions, state, tools, and an execution loop |
| Prompt | Communicates a request, instruction, or other material to the model |
| Skill | Packages a reusable procedure and supporting resources |
| Tool | Performs an operation, such as reading a file or running a calculation |
| Runtime | Hosts execution, supplies context, dispatches tools, and handles results |
| Harness | Configures the working environment around model execution |
| File | Stores information that can persist beyond a session |
| Context | The material actually available to the model for the current response |

These are design roles, not necessarily separate products. One application may provide execution, tools, storage, and an interface together.

A fixed workflow follows a predefined sequence. In an agentic loop, the model can choose subsequent steps in response to observations, within the system's limits. A practical system may combine both. This distinction follows [Anthropic's explanation of workflows and agents](https://www.anthropic.com/engineering/building-effective-agents); it does not certify any particular product's implementation.

## A prompt sets the task; a Skill carries a method

A task prompt might say: “Compare the supplied venues for 16 people after 18:00, with step-free entry required.” It tells the agent what you want now. Durable rules express instructions that should apply across a defined set of tasks, such as preserving original sources or keeping unsupported facts unknown. Both can influence the model when loaded, but they have different scope and expected lifetimes.

The model's input is not limited to your latest chat message. The runtime can assemble relevant instructions, loaded Skill contents, and tool observations into the current context as well.

At its core, a Skill in this repository is a reusable instruction document saved as `SKILL.md`. When loaded, its text becomes part of the model's current context. Think of it as **pinning a useful prompt or method** in a stable, discoverable place so you can reliably find and reuse it.

Pinning is an analogy for discovery, not permanent activation. In the [Agent Skills specification](https://agentskills.io/specification), the name and description support discovery first; the full instructions are loaded when needed. This does not mean the whole document appears in every turn or becomes a higher-priority system message. Actual discovery and loading depend on the host.

The document might teach requirement checks and source citation, with optional examples, references, or scripts alongside it. These materials supply a method, not new neural training or changed model weights. They do not grant tool permissions. An included script runs only through actual execution tools and their access rules; mentioning email does not connect an account or authorise sending.

The same model therefore has a clearer basis for comparison when it receives the task, source notes, and procedure than when it receives “pick a venue” alone. Better context helps shape its behavior, but the result still needs checking.

## Follow one execution loop

The first exercise uses synthetic notes, not real venue information. Its request is a comparison, not a booking. A typical tool-using loop looks like this:

1. **Observe the request.** The runtime supplies the task and relevant instructions. The model identifies the requirements and which source files it needs.
2. **Reason about the next step.** If it cannot yet see the notes, the model proposes a file-read operation rather than treating the filenames as evidence.
3. **Request a tool.** The proposed call names an available operation and its arguments. A sentence saying “I read the file” is not a tool execution.
4. **Execute through the runtime.** The host applies its configured access policy and dispatches the allowed operation. It may return file contents, deny access, or report an error.
5. **Use the result.** Returned material enters the subsequent working context. The model compares the notes and may request another operation if more permitted evidence is needed.
6. **Review and save.** It drafts `workspace/comparison.md`. After source review and corrections, the checked result belongs at `outputs/comparison.md`, with actual progress recorded in `workspace/handoff.md`.
7. **Stop or hand off.** It reports the achieved result and remaining limits. Missing information or authority can require a pause instead of another action.

Cedar Hall's supplied note supports the recorded requirements. Willow Room's hours do not fit. Maple Studio's step-free entry is unspecified. The loop should preserve that unknown; reasoning cannot manufacture an entrance statement that the source lacks. Writing an unsent question is a possible next task, but it does not obtain the answer.

Failures can occur at every stage: a wrong path, unavailable tool, denied permission, incomplete tool result, or mistaken interpretation. Even a successful file write does not prove the file is correct. Without file tools, a chat interface can return text for you to save, but it must not claim automatic writeback. Chapter 1 turns this outline into a concrete exercise.

## What Markdown files actually do

`.md` is a filename extension commonly used for **Markdown**, an editable plain-text format. A heading can begin with `#`; a list can use hyphens; links can point to other files. A person can read the underlying text without special software. Markdown is useful here because instructions, notes, and handoffs remain inspectable and easy to revise.

Some names have meaning only through a host's conventions. `AGENTS.md` or `SKILL.md` can serve as instruction or skill entrypoints when the selected environment discovers and loads them in the expected location. They are not universally executable files. Names such as `RULES.md` and `workspace/handoff.md` express project conventions; the workflow must arrange for the relevant content to be read.

These tiny excerpts illustrate different responsibilities. They are not additional required files for the first exercise or a complete installable Skill:

```text
task-brief.md
Compare the supplied venues for 16 people after 18:00.
Step-free entry is required.

RULES.md (illustrative project rule)
Keep missing source facts unknown; do not invent them.

skills/source-comparison/SKILL.md (illustrative procedure)
Check each requirement against each source and cite the evidence.

workspace/handoff.md (example state, only if actually true)
Draft saved at workspace/comparison.md; source review remains.
```

Three separate things now exist: **stored files**, **current context**, and **model weights**. Files retain text. Context contains the selected instructions, conversation, and tool results supplied for the current work. Weights are the model's learned parameters. Saving or loading these files does not by itself update those parameters. A future session resumes by retrieving relevant records, not because every saved fact has become part of the model.

## Personalise the work explicitly

A personal system should fit recurring work you actually do. You can specify language, detail level, evidence standards, review points, and preferred deliverables. These choices become useful when their scope is clear and you can revise them.

Suppose you correct a comparison: “For future source comparisons, lead with a short recommendation, then explain the evidence and unknowns.” That explicit preference can become a rule for comparison work. It need not apply to a poem, a debugging log, or every future conversation. Record what you requested, not an inferred personality profile.

Other lessons belong elsewhere. “Maple's access remains unknown” is current task state. The repeated sequence of extracting, comparing, citing, and reviewing can become a Skill. An explanation of why a missing field is not a negative answer can become a knowledge note. The distinction prevents one oversized memory file from collecting preferences, unfinished tasks, procedures, and reference material indiscriminately.

Personalisation changes the information and procedures available to the model. It is not automatic training, and repeated use does not prove a guessed preference. Sensitive traits should not be inferred from ordinary corrections. Retain only appropriate, authorised material, and review whether older preferences still apply.

## Why build this alongside existing AI software?

If you already use Codex, Claude Code, or WorkBuddy, the point is to organise your work within the software you choose. This guide does not assume those products lack memory, Skills, or workspace features. Reuse the runtime, tools, instruction loading, and storage features available in your chosen product. You do not need to write a new orchestration engine or custom application.

Your personal system is the deliberate combination of a stable role, your own authorised sources, scoped preferences, repeatable methods, and current state with evidence. Software supplies capabilities; you decide how they support your work. Some people will find the built-in arrangements sufficient as they are.

Here, **local** means keeping a durable workspace under your control. Files can be inspected, backed up, and, where appropriate, versioned to show what changed. Sources stay connected to conclusions. Another session can recover the next step, and another compatible tool can reuse the authorised materials.

Local files do not mean the model runs locally or that the workflow is offline. A hosted model or connector may receive content when used. Privacy depends on actual data flows, access permissions, service settings, and what you provide—not on the `.md` extension or folder name. Portability likewise requires checking how the next tool loads instructions and saves results; tools are not universally interchangeable.

This approach pays off when work repeats, spans sessions, or needs a traceable result. For a one-off explanation, normal chat may be enough. A durable system also costs effort: instructions can become stale, copies can diverge, and procedures need review. Start with one useful task and retain what makes its next occurrence easier. The [first-task chapter](01-first-task.md) shows that smallest working step.
