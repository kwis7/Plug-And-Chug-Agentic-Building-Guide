# Start with your own AI assistant / 用现有 AI 助手开始

Open a new conversation in your usual AI app and select the local folder where you want your personal system to live. If you do not know how, let the assistant guide you. Copy the whole prompt below; it includes the repository URL. You do not need to install this Skill first.

在平常使用的 AI 应用中开一个新对话，选定想保存个人系统的本地文件夹。不知道怎么选，可以让助手带你操作。复制下面整段提示词即可，仓库链接已经包含在内，不需要先安装这个 Skill。

## English

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

## 中文

```text
我不懂编程。请按照这个仓库的教程，带我搭建自己的本地 Agent 系统：
https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide

先读新手指南，再了解我想让 AI 帮什么忙、正在用哪个 AI 软件、
用什么电脑。每次只问两三个问题。
推荐适合我的最简单配置，用通俗语言解释；你能实际完成的技术步骤，
请你来做。创建文件前，先让我看看准备使用的新文件夹和里面的内容，
等我确认。使用新目录，保留我已有的文件。
带我完成一个小任务、检查结果，再试试新开一个会话后能否继续。
最后给我一份简短说明：文件在哪里、下次打开什么、该怎么对你说。
如果你无法读取仓库或操作本地文件，请告诉我下一步需要做什么，
不要直接说已经搭建完成。
```

The assistant needs to check its actual repository and local-file access. In a chat-only tool, start with a needs discussion and file plan; local creation and recovery remain untested until you use suitable tools or save and reopen the files yourself. Pasting a prompt does not guarantee installation or runtime integration.

助手需要检查实际的仓库和本地文件访问能力。只有聊天功能时，先讨论需求、规划文件；使用合适工具或自己保存并重新打开文件之前，本地创建与续做都还没有验证。粘贴提示词不代表安装或接入已经成功。

For a walkthrough, read [Start here](https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide/blob/main/docs/start-here.md) or [中文入门](https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide/blob/main/docs/start-here.zh-CN.md). The optional [fictional workshop example](https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide/blob/main/examples/first-project/README.md) / [虚构工作坊练习](https://github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide/blob/main/examples/first-project/README.zh-CN.md) offers supplied sources before you use your own material.

The assistant can consult the [full facilitation protocol](facilitation-protocol.md) for a longer design conversation. You do not need to paste all of it. If this Skill is installed and discoverable, its [entrypoint](../../SKILL.md) provides the technical workflow.

更长的设计对话可以由助手参考[完整引导协议](facilitation-protocol.md)（英文），你不需要粘贴整份内容。如果这个 Skill 已经安装且能被工具发现，可以按其[入口文件](../../SKILL.md)使用技术流程。
