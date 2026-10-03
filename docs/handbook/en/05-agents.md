# 5. Separate work when responsibilities collide

You may eventually have several kinds of recurring work: analysing sources, preparing a report and drafting messages about the result. One agent with suitable skills can handle much of this. Before adding another, look for a problem that separate responsibility would solve.

Suppose the analysis is still changing while a designer prepares the final report. You need an agreement about who settles the claims, which version goes to the designer and who approves a revision. Separate owners may help manage that handoff. An inconsistent table format is a smaller problem that a template or skill can usually address. A different subject or format alone gives you little reason to introduce another agent; distinct sources, data boundaries, authority or work cycles provide stronger reasons.

## Choose the right unit

| Need | Usually start with |
|---|---|
| One temporary objective | A task or project |
| A procedure repeated across tasks | A skill |
| Stable reusable reference material | A knowledge collection |
| Recurring work with distinct ownership | A domain agent |
| One bounded independent contribution | A temporary subagent |
| Access to a service or executable action | A tool or connector |

A domain agent maintains a continuing area of work through instructions, working files and access arrangements. The model carrying out that role can change. Ownership of the sources and authority to act should remain governed by the working agreement, rather than changing with the model selection.

The venue exercise needs only one agent. A recurring event workflow might later assign source comparisons to a research owner and approved messages to a communications owner. Those roles need different authority: comparing the notes gives a basis for a shortlist, while contacting a venue requires permission to send a particular message. Giving the roles separate names makes the arrangement easier to explain, but access restrictions still depend on tool permissions and explicit action rules.

## Define ownership before delegation

Give a delegated task enough detail to be checked when it returns: the result you need, the inputs the worker may read, where it may write, the actions it must avoid and the review criteria. “Research this” leaves each of those decisions open to interpretation.

For the venue exercise, you could ask a temporary reviewer to inspect the three fictional notes and report unsupported claims in `workspace/comparison.md`. It needs access to those files and a place to save its review. Rewriting the source notes, changing the scope or contacting venues would be outside that job. The lead then integrates the findings, checks the final answer and saves it to `outputs/comparison.md`.

The review earns its additional time and context when it can catch a plausible mistake. A statement that Maple meets the entrance requirement might look reasonable in a fluent report; a reviewer checking the note should notice that the information is missing. A second agent that simply rereads the conclusion and shares its assumptions would provide much less assurance. Give the reviewer evidence and a question it can investigate independently.

## Keep one writer per authority

Shared reading is often useful. Shared editing needs an arrangement to prevent one contributor from overwriting another. If the lead and reviewer both revise the current comparison, it can become unclear which changes were accepted and which version was checked. Assign one writer to each authoritative file, with other contributors saving separate proposals or artifacts for that writer to integrate.

For concurrent code work, Git worktrees put changes in separate checkouts. Resource locks coordinate use of a shared file, device, port or other resource. Changes in separate checkouts may still use the same account, and a lock provides no privacy boundary. Neither grants permission to publish or perform external actions. Delegating a role likewise needs actual access controls if the worker is meant to be unable to read particular material.

When several continuing owners depend on one another's work, a control center can route tasks, manage those dependencies and integrate results. It needs to know where the work belongs. That coordinating responsibility gives it no additional ownership of private domain facts. Methods can be shared between agents; any transfer of data must stay within its authorised scope.

## Test the boundary in ordinary language

Try the proposed descriptions on ordinary requests. Write two that clearly belong to an agent, two that do not and one that overlaps with a neighbour. Check who receives each request and who would integrate an overlapping task. The [routing guide](../../../skills/portable-agentic-system/pas/references/description-routing-evals.md) provides a fuller method.

If the new role has no distinct responsibility you can explain through those requests, keep the work with its current owner for now. You can split it when a specific source, authority or handoff problem arises. However many contributors take part, keep one accountable lead for the final result.
