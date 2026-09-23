# 2. Give the work a place to continue

A finished comparison preserves an answer. A useful workspace also preserves how to understand that answer: the inputs, the requirements, the checks, and any unfinished work. Without those, the next conversation can easily repeat the research or inherit a conclusion whose limits have been forgotten.

Our example needs only a small folder. The supplied source notes stay separate from the working result and handoff. The bundled `expected/` directory remains a teaching reference. Nothing about this layout requires a new agent, a database, or the full scaffold.

## Give each file a clear job

The source notes establish what was supplied. `workspace/comparison.md` is the draft; after review, `outputs/comparison.md` becomes the checked answer. `workspace/handoff.md` records current state and the next permitted step. These files have different jobs: the draft is not a second authority for the reviewed result. If a decision changes, review the change, update the result, and record its status in the handoff.

As work grows, these distinctions become useful:

| Kind of information | Question it answers | Example |
|---|---|---|
| Source material | What evidence was supplied? | Cedar Hall's recorded hours |
| Task state | What is happening now? | Comparison reviewed; no venue contacted |
| Memory | What short pointer helps us resume? | Location of the active task and key decision |
| Knowledge | What stable understanding is reusable? | How missing evidence affects a comparison |
| Skill | What procedure should we repeat? | Compare each candidate against every requirement |

**Context** is different: it is the material actually supplied to the model in the current session. A file can exist on disk without entering context. An instruction to read a source is also different from evidence that it was read. Ask the agent to identify the files and facts supporting its answer when loading matters.

## Preserve sources and uncertainty

Do not rewrite Maple's source note to make the comparison easier. Leave “accessibility unspecified” in the input and explain its consequence in the result. If new evidence arrives later, preserve its source and date, then revise the affected judgment. This keeps changes traceable without retaining every sentence of the conversation.

The same principle applies to real work. A summary is an interpretation of a source, not a replacement for provenance. Separate the source's claim from your conclusion, and retain enough attribution for a reviewer to inspect the bridge between them. Store only material you are authorised to retain and make available to the tool.

## Let structure follow need

The standard scaffold gives larger projects named places: `raw_data/` for original inputs, `workspace/` for drafts, `artifacts/` for generated intermediates, `logs/` for execution traces, `outputs/` for reviewed results, and `archive/` for closed material. Their full responsibilities are defined in the [filesystem contract](../../../skills/portable-agentic-system/pas/references/filesystem-contract.md).

Those names express intent. They do not enforce permissions. A tool that can read the whole directory may still reach a file called private. Sensitive work therefore needs actual access restrictions and a deliberate choice about which material enters the model. A useful public example should contain synthetic or authorised material, not a disguised copy of someone's private records.

Before adding folders, try one practical test: can you identify the current answer, its sources, and the next action within a minute? If yes, your present structure may be enough. If not, fix the ambiguity that caused the delay. Structure earns its place by reducing the cost of continuing.
