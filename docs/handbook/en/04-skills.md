# 4. Keep a method that worked

The venue comparison contains a procedure you could use again. For each candidate, extract the same fields, compare them with the requirements, and distinguish a failed requirement from missing information. A later comparison might concern suppliers or reading notes, but it could still benefit from those steps.

Once you have used a procedure enough to recognise what helps, save it where you can find it. A **Skill starts with a Markdown instruction document**, conventionally named `SKILL.md`. When the host loads that document, its text enters the model's context. The model uses its existing capabilities to follow the instructions; its trained weights remain unchanged.

Keeping a method in a discoverable place is sometimes described as pinning it for reuse. Discovery and loading still depend on the host. The name and description help with selection; the host can then load the full instructions and references as needed. Pinning does not mean that the full document is present in every turn or has higher instruction priority. Examples, templates and scripts may accompany the instructions, with scripts requiring actual tools and permission to run. Maintaining this package makes sense when repeated work or a recurring error gives you a reason to reuse it.

## Extract the method, leave the case behind

To extract the method, ask what would remain useful if all three venue notes were replaced. Cedar's place on the shortlist depends on this exercise's requirements and evidence. Checking each candidate against every required condition is useful in the next comparison too. A procedure that includes the old recommendation could steer a new task towards Cedar before the new evidence has been considered.

Here is a sketch of the procedure worth retaining:

```text
Name: Source-backed comparison
Use when: comparing supplied candidates against explicit needs.
Inputs: requirements and named source notes.
Method: extract facts with sources; check each requirement;
separate meets, fails, and unknown; explain the final judgment.
Output: concise comparison, unresolved questions, and handoff.
Limits: do not infer missing facts or perform external actions.
```

Use the sketch to decide what the method should do. The repository's [skill template](../../../skills/portable-agentic-system/pas/templates/skill/SKILL.md) shows how to package it. Check the selected runtime's requirements for installation and discovery; the sketch alone is not a format every tool can install.

## Write a useful trigger

The description is what helps a host choose a skill before reading its full procedure. If it says only “Helps with research”, it could apply to summarisation, writing or data collection. Give it a more specific job by naming the work, the expected inputs and outputs, and the cases it excludes.

Test that description with requests you might actually make. “Compare these three supplier notes against our requirements” should select the comparison method. “Write a thank-you note” should not. A request to “Compare these venues and book the best one” needs to be separated into comparison and booking: the skill provides a method for the first, while the second requires its own capability and authority. Selecting the skill cannot supply that authority.

Next, inspect the output produced with the method. The venue fixture should support Cedar, exclude Willow because of its hours, and leave Maple's accessibility unresolved. Try a variation with a missing source or contradictory fact as well. The variation is useful because a reusable procedure must respond to the evidence it receives. Reproducing one reference answer gives you little information about how it handles a different case.

## Put each lesson in the right place

Some lessons affect the procedure; others belong with the task or its owner. An instruction to begin future source comparisons with a recommendation is a scoped preference for the relevant operating rules. Maple's unresolved entrance belongs in the current task state. Stable background can go in knowledge, while the repeated comparison steps belong in the skill. Reading files or accessing a service remains the work of a tool.

With those purposes separated, a change is easier to make in the right place. The skill's description helps with discovery, its main text explains the method, and longer references can be retrieved when needed. There is no need to load every skill and reference into each conversation. Select the material relevant to the current work so the procedure stays understandable and the context remains manageable.

## Share procedure deliberately

A second agent or project can use the comparison procedure with its own authorised inputs. Share the method and a synthetic example, while keeping private candidate notes, internal decisions and the full chat history with their owner. This lets another project try the useful steps without importing the original project's private material.

Return to the skill after actual use. If it repeatedly omits a required field, you have a concrete problem to fix and a result to check after the edit. An unusual request may need only a task-specific instruction. The [distillation guide](../../../skills/portable-agentic-system/pas/references/skill-distillation-and-fusion.md) explains how to retain repeated experience and review procedures that overlap.
