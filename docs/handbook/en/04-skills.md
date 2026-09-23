# 4. Keep a method that worked

After several comparisons, you may notice that the valuable part is the procedure. You identify the requirements, extract the same fields from each source, apply the requirements consistently, and expose missing evidence. That method can survive even when the venues, documents, or active model change.

A **Skill starts with a Markdown instruction document**, conventionally named `SKILL.md`. Its text becomes part of the model's context when the host loads it. You are keeping a useful prompt or method in a discoverable place—much like pinning a playbook for reuse. The model follows those instructions with the capabilities it already has; saving a Skill does not train new model weights.

That pin is a way to find the method again, not a promise to include its full text in every turn or give it higher instruction priority. The name and description help the host choose it; the full procedure and any supporting references are loaded as needed. A Skill can also include examples, templates, or scripts, but scripts still need actual tools and permission to run. It earns its maintenance cost when repetition or a recurring mistake makes the procedure worth preserving.

## Extract the method, leave the case behind

“Choose Cedar Hall” is a conclusion from one fictional exercise. “Check every candidate against every required condition” is a reusable method. Mixing the two can cause the next comparison to inherit an old answer.

For our example, a useful skill might be described as follows:

```text
Name: Source-backed comparison
Use when: comparing supplied candidates against explicit needs.
Inputs: requirements and named source notes.
Method: extract facts with sources; check each requirement;
separate meets, fails, and unknown; explain the final judgment.
Output: concise comparison, unresolved questions, and handoff.
Limits: do not infer missing facts or perform external actions.
```

This is a teaching sketch, not a universally installable skill format. The repository's [skill template](../../../skills/portable-agentic-system/pas/templates/skill/SKILL.md) shows its packaged form. Actual discovery depends on the selected runtime and installation location.

## Write a useful trigger

The description should help select the procedure before its full contents are loaded. “Helps with research” is too broad. It gives no reason to choose this skill over summarisation, writing, or data collection. A useful description names the work, expected inputs and outputs, and exclusions.

Try a small set of routing examples. “Compare these three supplier notes against our requirements” should activate the comparison method. “Write a thank-you note” should not. “Compare these venues and book the best one” contains two different actions: the skill can prepare the comparison, while booking needs separate capability and authority. A trigger must not quietly authorise the second action.

Then test the procedure itself. The venue fixture should produce Cedar as supported, Willow as unsuitable on hours, and Maple as unresolved on accessibility. Add a variation with a missing source or contradictory fact. These tests reveal whether the skill handles uncertainty, not merely whether it repeats the reference answer.

## Put each lesson in the right place

A preference that should always apply belongs in the relevant operating rules. Stable background belongs in knowledge. Today's unfinished comparison belongs in task state. A repeated sequence of work belongs in a skill. A tool belongs where real execution or external access is needed.

This separation keeps skills small enough to understand. The short description supports discovery; the main instructions explain the method; deeper references are loaded when the task needs them. Loading every skill and reference into every conversation defeats that design and consumes attention without improving the current answer.

## Share procedure deliberately

Another agent can borrow the comparison method without receiving private candidate notes, internal decisions, or a full chat history. Share the procedure and a synthetic example, then let the receiving project supply its own authorised inputs. This is how useful learning travels while data ownership stays clear.

Review a new skill after real use. Keep a correction when it addresses a detectable failure, and avoid turning every unusual request into a permanent rule. The deeper [distillation guide](../../../skills/portable-agentic-system/pas/references/skill-distillation-and-fusion.md) explains how to promote repeated experience without filling the system with overlapping procedures.
