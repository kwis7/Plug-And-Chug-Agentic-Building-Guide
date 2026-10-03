# Build an AI workspace you can return to

Suppose you are preparing a report over several weeks. An AI assistant helps you compare sources and revise a draft. By the second week, you have more than a collection of answers: you have selected evidence, rejected a few claims, settled on a format and left questions for later. To continue well, you need to recover those decisions along with the draft. Otherwise, you may repeat work or quietly lose the reasons behind it.

This guide grew out of Computational Social Science research, where the relationship between sources, methods and conclusions matters. The same problem appears in studying, writing, teaching and many other recurring tasks. A personal AI system gives that work a structure you can inspect and revise. You decide what to keep, what the assistant may use and which methods are worth repeating.

You can build it with the AI application you already use. The guided setup assumes no programming background. As you work through the book, the assistant can handle the technical steps its tools permit and explain the choices involved. The purpose is to make your work easier to continue without requiring you to organise your life around the software.

## Start with your own assistant

The [beginner guide](../../start-here.md) contains a starting prompt with the repository link. Give it to your usual assistant. It will ask about your work, app and computer, then propose a small setup. Review the proposed folder and its contents before agreeing to file creation. The proposal should account for the tools actually available: a chat-only assistant can explain a step for you to perform, while an assistant with appropriate file access may perform it directly.

Choose a task small enough to finish and check. At the end, you should have the result, a record of unfinished work and a short card telling you which files to open next time. Try that card in a new conversation and check that the assistant reads the named files, identifies the unfinished work and resumes at the agreed next step.

The chapters explain why each part is useful. When a term is unfamiliar, ask the assistant to explain it through your task. You can also use terminal commands directly; that optional route is collected in the final reference chapter and the [quick start](../../../QUICKSTART.md).

## Keep the work, change the model

The report example also explains why ownership matters. You should be able to inspect the sources and decisions, correct a procedure or try another model without surrendering the work you have already done. Keeping records in accessible formats makes those choices possible. Moving to another interface or provider still requires adaptation and checks; saving the files does not establish compatibility by itself.

The book uses **harness** for the configured environment around model execution: instructions, files, tools, task state and checks. Some of these are text that guides the model. Others are software that controls access or checks an action. Their effects differ, so we will be careful about what each one can establish.

The company diagram in the next chapter separates these responsibilities. You are the owner who sets the purpose and authorises consequential actions. The model does the reasoning within the working arrangements you have chosen. This analogy describes roles; it does not imply human awareness, loyalty or automatic access to the company's records.

## Learn through one example, then apply it to your work

Chapters 1-4 use three fictional venue notes to compare options, check a conclusion and leave the next step for another session. Because the inputs are supplied and contain no personal information, you can concentrate on the method. The exercise is optional. If you have already chosen a task during setup, apply the explanations to that task; there is no need to build a dedicated venue-comparison Agent.

Chapters 5-8 consider the decisions that follow: when to separate responsibilities, how to change tools, what to verify and how to maintain the system. The reference chapter then points to the standard toolkit. Read those sections when the corresponding question arises in your work.

The exercise needs only a few files. The guided route can create those teaching files directly; the standard generator creates a fuller scaffold with task manifests and local checks. Ask your assistant which arrangement suits the task and how it will be created.

## Read evidence at its stated level

Throughout the example, we will distinguish what a source says, what the assistant concludes and what has actually been tested. The data is synthetic. Commands and compatibility records describe the repository's implementation, with their stated limits; they do not certify the app on your computer. Reading an instruction, passing a static check, resuming in a fresh session and delivering something externally each require their own evidence.

Continue with [how an agent works](00-foundations.md) for the company diagram and the concepts behind it. As you read, consider which records your own task would need for someone to resume it accurately.
