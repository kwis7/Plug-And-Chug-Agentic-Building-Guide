# 5. Separate work when responsibilities collide

One agent with a few well-chosen skills can handle a substantial amount of work. A new subject or a different writing format does not automatically require another agent. Splitting becomes useful when recurring work has a distinct mission, data boundary, source base, authority, or lifecycle.

Think about the failure you are trying to prevent. If source analysis keeps changing while a designer is preparing the final report, separate ownership may help. If the only problem is an inconsistent table format, a template or skill is probably enough.

## Choose the right unit

| Need | Usually start with |
|---|---|
| One temporary objective | A task or project |
| A procedure repeated across tasks | A skill |
| Stable reusable reference material | A knowledge collection |
| Recurring work with distinct ownership | A domain agent |
| One bounded independent contribution | A temporary subagent |
| Access to a service or executable action | A tool or connector |

A domain agent is a durable responsibility expressed through its instructions, working files, and access arrangements. It need not use a permanently assigned model. Choosing a different model changes the active reasoning component; it should not silently change who owns the sources or which actions are allowed.

For the venue exercise, one agent is sufficient. In a larger recurring event workflow, a research owner could maintain source comparisons while a communications owner prepares approved messages. Researching an option and contacting it have different authority requirements. Separating them can make that boundary easier to review, but it still needs tool permissions and explicit action rules.

## Define ownership before delegation

A useful delegation says what result is needed, which inputs may be read, where the worker may write, what is forbidden, and how the result will be checked. “Research this” leaves too much room for conflicting assumptions.

For example, a temporary reviewer could inspect the three fictional notes and report any unsupported claim in `workspace/comparison.md`. It needs read access to those files and a place for its review. It does not need to rewrite the sources, alter the task's scope, or contact venues. The lead retains responsibility for integrating the findings and checking the final answer before saving it to `outputs/comparison.md`.

Independent review is especially valuable when a plausible mistake could survive self-review. It costs additional time and context, so use it for a reason. A second agent repeating the same assumptions without checking the sources adds little confidence.

## Keep one writer per authority

Two agents can read the same source. Two agents editing the same current-state file can erase each other's work. Assign one writer to every authoritative path and let other contributors produce separate proposals or artifacts.

Git worktrees can isolate concurrent code changes in separate checkouts. Resource locks coordinate access to a shared file, device, port, or other resource. They solve different problems: a worktree does not isolate a shared account, and a lock is not a privacy control. Neither grants permission to publish or perform an external action.

A control center becomes useful when several durable owners need routing or coordinated work. Its job is to know where responsibilities belong, manage dependencies, and integrate results. That does not make it the owner of every domain's private facts. Share methods across agents; transfer data only within its authorised scope.

## Test the boundary in ordinary language

Write two requests that clearly belong to an agent, two that do not, and one that overlaps with a neighbour. Check whether the descriptions route them sensibly. The [routing guide](../../../skills/portable-agentic-system/pas/references/description-routing-evals.md) provides a fuller method.

If you cannot explain why a new agent needs its own responsibility, keep the work with its current owner. Add separation when it makes a real boundary clearer, and retain a single accountable lead for each result.
