# Workshop comparison / 工作坊场地比较

**Synthetic exercise.** Every venue and venue fact is invented for learning. The notes are supplied fixtures, not real listings or current public facts. The task is local analysis only; no booking, sending, or live research.

**虚构练习。** 场地及其信息均为教学编写，不是真实地点、真实公告或最新公开事实。本任务只做本地分析，不预订、不发送、不搜索。

## Request / 任务

Compare Cedar Hall, Willow Room, and Maple Studio for a **16-person workshop after 18:00 requiring step-free entry**. Recommend a shortlist based only on the recorded facts. Explain exclusions and missing information. No event date, duration, price, or date-specific availability is supplied; do not invent them or claim a confirmed booking option.

为一场 **16 人、18:00 以后进行、需要无台阶入口**的工作坊比较 Cedar Hall、Willow Room 和 Maple Studio。只根据已记录事实提出候选建议，说明不适合之处和信息缺口。没有给出活动日期、持续时间、价格或指定日期的可用情况，不能编造，也不能声称已确认可以预订。

## Named inputs / 具名输入

- `task-brief.md`: requirements and scope / 需求与边界。
- `sources/cedar.md`: Cedar Hall fixture / Cedar Hall 虚构资料。
- `sources/willow.md`: Willow Room fixture / Willow Room 虚构资料。
- `sources/maple.md`: Maple Studio fixture / Maple Studio 虚构资料。

Use no other source for venue facts. `expected/` contains reference answers for later review, not additional evidence. The optional missing-source exercise narrows this input list by withholding `sources/maple.md`.

场地事实不使用其他来源。`expected/` 是之后对照的参考答案，不是额外证据。可选的资料缺失练习会进一步缩小输入范围，不提供 `sources/maple.md`。

## Files to create / 创建的文件

1. `workspace/comparison.md`: draft / 草稿。
2. `outputs/comparison.md`: result checked against every available source / 逐份资料核对后的结果。
3. `workspace/handoff.md`: completed work, actual checks, unknowns, next step, allowed inputs and writes / 已做工作、实际检查、未知项、下一步及读写范围。

Preserve the source fixtures and reference answers. Review existing destination files before changing them. During recovery, the next local output is `workspace/maple-question.md`, an **unsent** question about the unresolved entry-access information.

保留资料和参考答案。修改前查看已有目标文件。续做时下一个本地产物是 `workspace/maple-question.md`，只起草询问未确认入口情况的问题，**不发送**。

## Acceptance / 核对标准

- One row per venue, with capacity, hours, entry-access evidence, and a decision linked to its source.
- Distinguish recorded fact, your conclusion, and unknown information.
- Match the stated requirements; do not turn an unknown into a positive or negative fact.
- Explain that shortlist suitability does not establish availability, price, or booking.
- Verify the saved result and handoff by reopening them; do not claim runtime recovery until a fresh-session test is observed.

每个场地一行，列出容量、时间、入口依据和可追溯的判断；区分资料事实、分析结论和未知项。候选建议不代表可用档期、价格或预订已确认。重新打开结果与交接文件检查，实际观察新会话续做之前不声称测试通过。
