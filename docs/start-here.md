# Build your own AI workspace

[English](start-here.md) | [中文](start-here.zh-CN.md) · [Home](../README.md)

Give this guide to the AI assistant you already use. It will help you understand the basics, choose a useful first setup, and create a local home for your recurring work. You choose the work and review the results; the assistant can handle file creation and other technical steps its tools allow.

An **agent** here is an AI assistant with a defined job, relevant materials, and working instructions. A personal system keeps those things, your results, and unfinished tasks in files you can return to. You can begin with one agent for one area of work, such as reading notes, writing projects, or study planning.

## 1. Open your usual AI app and choose a folder

Use an app such as Codex, Claude Code, or another assistant configured to work with selected local files. Open a new conversation and choose a folder where you want your system to live. A new, empty folder is easiest; if you are unsure how to select one, say so and let the assistant guide you for your app and operating system.

You do not need to run terminal commands for this route. Start with the prompt below; the assistant should check whether it can read the repository and the chosen folder before deciding how to build. A URL alone does not grant local file access.

If your app only offers chat, you can still discuss your needs and plan the files. Creating and reopening local files needs suitable tool access or your manual help. App subscriptions or model usage may have their own costs.

## 2. Copy this whole prompt

The repository link is already included. You do not need to install the Skill before starting.

<!-- STARTING_PROMPT:en -->
```text
I don't know how to program. Please use this repository to help me build
my own local agentic system:
https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide

Start with the beginner guide. Ask what I want help with, which AI app
I use, and what computer I have. Ask only two or three questions at a time.
Recommend the simplest useful setup for my work and explain it plainly.
Handle the technical steps you can actually perform. Before creating files,
show me the new folder and what you will put there, then wait for my agreement.
Use a new folder and preserve my existing files.
Help me complete one small task, check the result, and try continuing in
a new conversation. Finish with a short note explaining where my files are,
what to open next time, and what to ask you to do.
If you cannot read the repository or work with local files, explain the
one next step I need to take instead of claiming the setup is complete.
```
<!-- /STARTING_PROMPT -->

Keep this [short starting prompt](../skills/portable-agentic-system/pas/references/friend-starter-prompt.md#english) handy if you want to begin again later.

## 3. Let the assistant build around your work

The conversation should begin with your needs. For example: “Every week I read a few articles and want a comparison note, but I keep losing my sources and the next step.” You can answer in ordinary language. Ask it to explain any unfamiliar term before moving on.

### What the first conversation can look like

This short fictional exchange shows the sequence, not a record of an actual setup:

> **You:** I want to practise comparing the three fictional workshop venue notes, then continue another day without pasting the old chat.
>
> **Assistant:** Which AI app do you use, and what computer are you on? I will check whether I can read the guide and work with your selected local folder.
>
> **Assistant, after your answers:** I will propose a place for the source notes, a draft, a checked result, and a handoff. Before creating anything, I will show you the exact destination and wait for your agreement. If I cannot access the files, I will explain the next step you need to take.

The assistant should then show a small, concrete proposal: the exact new folder, the job the agent will do, where inputs and results belong, and how progress will survive the conversation. It should explain why each part helps. Review that proposal before it creates files. If an existing folder contains work, have it inspect the relevant files and preserve them.

Once you agree, let it perform the technical steps and show you the resulting files. The repository's generator creates a **standard scaffold**, a fuller starting structure. The assistant may use that when it fits, or propose a smaller learning workspace first. That smaller workspace is a separate teaching choice; the generator does not currently offer a minimal-profile option.

If a download, installation, or access change is genuinely needed, the assistant should explain the specific step and get the permission it needs. Pasting the prompt starts a guided process; it does not guarantee an unattended installation or working integration with every app.

## 4. Finish something useful and check it

Choose one low-risk task from your own work and a few non-sensitive inputs you are comfortable sharing. For example, turn three reading notes into a comparison with source links. Have the assistant save the result, reopen it, and check it against those inputs. Missing information should stay visible.

Next, have it leave a short handoff: what was done, which files were used, what is still unknown, and the next allowed step. Ask it for a card filled in with **your actual paths**, not placeholders:

| Keep this card | What the assistant should write |
|---|---|
| Open next time | Your app and the exact workspace folder |
| Say this | A short resume prompt naming the handoff file |
| Find my results | The saved, checked result's path |
| Find my progress | The handoff or current-task file's path |
| Next step | One concrete action and the inputs it needs |
| Checked so far | What was observed, and what remains untested |

### What a filled practice card can look like

This is an authored checkpoint for the [fictional workshop exercise](../examples/first-project/README.md), based on its [reference comparison](../examples/first-project/expected/comparison.md) and [reference handoff](../examples/first-project/expected/handoff.md). Paths below are relative to `examples/first-project/` in a local repository copy. The working result and handoff must be created during your attempt; this card is not a claim that those files already exist or a downloadable setup.

- **Open next time:** A local-file-capable AI app, with the local `examples/first-project/` folder selected
- **Say this:** “Read `workspace/handoff.md` and only its permitted inputs. Check the reviewed result, then draft the recorded unsent question.”
- **Find my results:** `outputs/comparison.md`, saved after checking the draft against all three notes
- **Find my progress:** `workspace/handoff.md`, naming the sources, result, information gap, and next allowed step
- **Next step:** Draft the question about Maple's step-free entry at `workspace/maple-question.md`; do not send it or fill the gap by guessing
- **Checked so far:** The teaching reference shows sourced comparisons and explicit unknowns. File saving and fresh-session recovery in your setup remain **not tested until observed**

For your own card, replace these relative examples with your actual app and folder paths. Record only files you can reopen and checks you observed.

## 5. Try a fresh session

Open a new conversation in the workspace shown on your card. Use its resume prompt without pasting the old chat. For example: “Read the handoff file named on my card, tell me what is complete and still unknown, and continue with the recorded next step using its named inputs.”

Check that the assistant finds the actual files and follows the recorded next step. Reopen anything it saves. If this works, record the app, date, and observed result in the handoff. If you have not tried it, label recovery **not tested**. This exercise checks the behavior you observed; it does not prove every integration or permission mechanism works.

<a id="practice-first"></a>
## Optional: practise before using your own material

The [fictional workshop example](../examples/first-project/README.md) supplies three venue notes, reference answers, and a restart exercise. Use it if you want safe practice or do not yet have a task in mind. It is optional; your personal system should grow from your own recurring work.

Continue with the [handbook](handbook/index.md) for the basics and worked explanations. The [quick start](../QUICKSTART.md) also offers a manual toolkit route for readers who prefer commands. The assistant can consult the [detailed facilitation protocol](../skills/portable-agentic-system/pas/references/facilitation-protocol.md); you do not need to read or paste that entire protocol yourself.
