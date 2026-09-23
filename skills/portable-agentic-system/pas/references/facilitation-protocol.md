# Facilitator protocol for guided personal-system building

Use this reference after the user starts with the [shared starting prompt](friend-starter-prompt.md). The journey is the same as the beginner guide: understand the user's work, agree on a useful setup, build in the chosen local folder, finish and check one task, try a fresh-session handoff, and leave a next-use card.

If the `portable-agentic-system` Skill is installed and discoverable, follow its setup-depth routing. Otherwise, read the README, beginner guide and only the references needed for the current step. A repository URL does not grant local file access; establish what the current app can actually read and do.

## Guide the conversation naturally

Reply in the user's language. Explain unfamiliar terms when they become useful. Start with two or three questions about the work they want help with, their AI app, and their computer. Carry forward answers already given. If the user has already approved a concrete setup, continue from that point.

Use the company example to explain the basics briefly: the user owns the work; the model is the replaceable employee; the Agent is its assigned role; a prompt is the current request; instructions and Skills describe how to work; tools let it act; files preserve the work. Context is the selected material supplied for this turn. The harness is the surrounding arrangement that makes those parts work together. A coordinating model is a manager only when there is an actual team to coordinate.

A Skill's core is a Markdown document that enters context when loaded. “Pinning” a method makes it available for reuse, not permanently present in every turn or more authoritative than the user's request. Memory is a short handoff; knowledge is reference material retrieved when needed. Use the original company diagram when it helps.

After an answer, explain the next useful decision and recommend one default. Ask another question only if its answer would materially change the setup. Do not turn each stage into a form, repeat a full status checklist, or require the user to learn configuration vocabulary before beginning. Let the user pause, ask for an example, or revise the proposal in ordinary language.

## 1. Understand one recurring job

Start with a concrete example of what the user wants to get done. Learn what goes in, what a useful result looks like, what currently gets lost between conversations, and any preferences that affect the result. For example: “I read three articles each week and want a short comparison with links and unanswered questions.”

Confirm the chosen folder and the app's actual file access before writing. Use non-sensitive sample inputs for the first task. Do not scan private folders or assume that permission to create a workspace also permits reading unrelated files, connecting accounts, or publishing results. Read [privacy boundaries](privacy-boundaries.md) when handling private material.

Do not ask the user to name a model provider, hook protocol, storage budget or concurrency policy unless their work makes that decision necessary. Safely inspect available technical details yourself. A hosted chat without local tools can help plan, but cannot be presented as having created a local system.

## 2. Propose the smallest useful setup

Choose the setup depth explicitly and explain the practical consequence:

- **Teaching workspace:** normally right for a beginner starting with one recurring job. Propose a few files with clear purposes: instructions appropriate to the app, working material, a saved result, a handoff and a next-use card. Combine roles when that keeps the system understandable. No standard task manifest, generated dashboard, hook, lock or gate is required for this route.
- **Standard scaffold:** use when the user wants the fuller toolkit or needs its formal task records, checks, completion gates or concurrent-work controls. Consult the [intake questions](intake-questions.md) and [filesystem contract](filesystem-contract.md). Keep the generator's existing requirements and verification procedures intact. It has no minimal-profile option.

An existing standard scaffold must keep its governing rules. Do not call it a teaching workspace to bypass a failed gate. A later upgrade from a teaching workspace is an explicit migration with a file-preservation plan and checks of the added mechanisms.

For a teaching workspace, the proposal should fit in a short explanation: the recurring job, exact new folder and files, allowed inputs and actions, first result, and how to check and resume it. Show how it reflects the user's preferences. Wait for agreement before creating the proposed files; do not repeat approval for that same scope.

For a standard scaffold, show a Design Contract covering the objective, owner, runtime and adapter evidence, file responsibilities, privacy and approval boundaries, task state, budgets, relevant concurrency controls, validation plan and exact proposed changes. Mark optional mechanisms as useful later or unnecessary. Reuse confirmed answers instead of restarting the interview.

Prefer one capable Agent to several overlapping roles. Add a Skill for a repeatable method, knowledge for stable reference material, and a tool only for an action or source the work actually needs.

## 3. Build in the agreed folder

Preserve existing work and respect local instructions. Perform the technical steps your tools support; do not make the user run commands merely because the repository includes a command-line route. If an installation, download or access change is needed, explain the particular step and obtain any missing permission for it.

Create the approved files in small, understandable steps. Explain the purpose of the few files the user will return to. Use the actual entrypoint supported by the selected app; do not assume an arbitrary Markdown filename loads automatically. Keep named inputs separate from results and avoid automatically loading whole archives.

For the standard route, preview the generator output, create the approved scaffold, inspect its hooks, and run its validators. Do not overwrite collisions with `--force` without resolving them and preserving the user's work. Read only the relevant runtime adapter and retain its evidence limitations.

Show progress at meaningful checkpoints. If an unexpected existing file, access limitation or scope change affects the next step, resolve it before changing that part. Approval for local setup does not authorize sending, publishing, deploying, committing, pushing, deleting, using credentials or uploading private data.

## 4. Complete and check a first task

Use one small task from the user's actual work and a few approved, non-sensitive inputs. If they want practice first, offer the repository's fictional workshop example; it is optional.

Save the result, reopen it, and compare it with the named inputs and the user's requested format. Distinguish source facts from suggestions, assumptions and gaps. Explain one thing the user can inspect to judge whether the result is useful.

Write a handoff with the objective, files used, completed work, result path, checks performed, unknowns and the next allowed step. In a teaching workspace, this can be a short handwritten file. In a standard scaffold, update the authoritative task manifest, generate status, save receipts and pass the applicable closeout gate; do not introduce a competing handwritten status system.

## 5. Try recovery and leave a next-use card

Fill in this card using actual paths and the user's app:

| Card item | What to provide |
|---|---|
| Open next time | App and exact workspace folder |
| Say this | A short resume prompt naming the handoff or task file |
| Find my results | The saved and checked result's path |
| Find my progress | The authoritative handoff or task file's path |
| Next step | One concrete action and the inputs it needs |
| Checked so far | Observed checks and anything still untested |

Have the user open a fresh conversation in that workspace and use the card without copying the old chat. The new session should locate the named files, explain what is complete and unknown, and perform the recorded next step within its allowed scope. Reopen the resulting file. Record the app, date and observed outcome only when that test has actually happened.

If you cannot open a fresh session yourself, leave the card and the exact exercise for the user. Report “workspace and first task checked; fresh-session recovery not tested.” Do not equate file creation with observed recovery, or a successful recovery exercise with full runtime or gate compatibility.

Finish in ordinary language: what the user can now do, where the result and card are, what you checked, and what remains unverified. The teaching route does not claim standard-scaffold validation. The standard route must retain its documented/static/runtime/gate/concurrency distinctions. Recommend the next improvement after real use reveals a need, rather than creating more infrastructure at handoff.
