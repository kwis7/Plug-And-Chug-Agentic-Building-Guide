# 2. Give the work a place to continue

Imagine reopening the venue comparison a week later. The recommendation says Cedar Hall is suitable, but you also need to know what "suitable" meant: enough space for 16 people, hours after 18:00 and recorded step-free entry. You need to see the notes behind that judgment and remember that availability and booking terms were never checked. The answer alone cannot preserve all of this.

A workspace keeps the result together with the evidence and state needed to interpret it. For this exercise, a small folder is sufficient. Separate the supplied notes from your draft, checked result and handoff. Leave the bundled `expected/` directory as a teaching reference. You can establish these roles without adding a database, a new Agent or the full standard scaffold.

## Give each file a clear job

The notes under `sources/` record the supplied evidence. Work on the comparison at `workspace/comparison.md`, then place the reviewed version at `outputs/comparison.md`. Keeping both makes the review visible, but it also introduces a responsibility: the old draft must not become a competing source of current conclusions. When new evidence changes the decision, review the revision, update the result and record its status in `workspace/handoff.md`.

The handoff answers a different question from the comparison. It tells the next session where the work stands and which step is permitted next. In our example, no venue has been contacted and Maple's accessibility remains unknown. A reader should be able to recover those facts without searching through the entire conversation.

Larger projects need the same distinctions, even if their files have different names:

| Kind of information | Question it answers | Example |
|---|---|---|
| Source material | What evidence was supplied? | Cedar Hall's recorded hours |
| Task state | What is happening now? | Comparison reviewed; no venue contacted |
| Memory | What short pointer helps us resume? | Location of the active task and key decision |
| Knowledge | What stable understanding is reusable? | How missing evidence affects a comparison |
| Skill | What procedure should we repeat? | Compare each candidate against every requirement |

These records become useful to a model when the runtime supplies them as **context** for the current session. A saved handoff may be available on disk yet absent from the model's input. For that reason, instructions about resuming should identify what to read, and the resumed answer should identify the files and facts it used. Asking the agent to read a source establishes an instruction; observing the read and checking its use establish more.

## Preserve sources and uncertainty

Maple's missing accessibility information belongs in the result as an unknown. Editing the source note to make the comparison complete would destroy the distinction between supplied evidence and your interpretation. If a new statement arrives later, preserve its source and date, then revise the affected judgment. The record will show why the answer changed without needing every sentence of the intervening chat.

Apply the same care to real research. A summary helps you understand a source, but a reviewer still needs to know which source supports the conclusion. Keep the attribution and the limits of the claim. Retain and expose only material you are authorised to use. Personal originals remain under your control, outside the Agent's read scope; provide the minimum authorised fields, an explicitly agent-readable redacted derivative or a controlled mediator output when such material is needed.

## Let structure follow need

The standard scaffold offers named places for a larger project: `raw_data/` for public, synthetic or explicitly authorised nonprivate source inputs; `workspace/` for drafts; `artifacts/` for generated intermediates; `logs/` for execution traces; `outputs/` for reviewed results; and `archive/` for closed material. The [filesystem contract](../../../skills/portable-agentic-system/pas/references/filesystem-contract.md) defines their full responsibilities.

These names make the intended use easier to understand. Access still depends on the tools and permissions: a file named "private" remains readable to a tool with access to the whole directory. Sensitive work needs actual access restrictions and a deliberate decision about what enters the model. Public examples should use synthetic or authorised material, never disguised personal records.

Before creating another folder, try finding the current answer, its sources and the next action. If that takes less than a minute, the present structure may be enough. If it takes longer, identify the ambiguity: perhaps two drafts look current, or the handoff names a file that has moved. Repair that problem first. Add structure when it makes a specific part of the work easier to continue.
