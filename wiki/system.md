# System Rules — CS61B Research Wiki

> This file defines how the AI-knowledge-wiki system operates.
> The AI reads this on every session start and follows these rules.

## Architecture

This system separates raw input (human-managed) from structured knowledge (AI-managed):

```
raw/   → 👤 Human adds materials here. ONLY here.
wiki/  → 🤖 AI maintains everything here. Human should NOT edit these files.
```

## The Knowledge Cycle

```
Materials are ingested → Concepts are extracted → Connections are discovered → Questions are raised
                                                                              ↓
                                                              Drive search for new materials
```

The AI proactively maintains this cycle. The human feeds raw materials and asks questions.

## Ingestion Protocol

1. Human adds files to `raw/`
2. Human asks AI to ingest
3. AI reads each file and discusses key takeaways with human
4. Human decides what enters the wiki
5. AI compiles the approved content into wiki/concepts/
6. AI checks for new connections → wiki/connections/
7. AI identifies open questions → wiki/questions/
8. AI updates index.md and log.md

The discussion step (step 3-4) is MANDATORY. AI must not skip it.

## Socratic Teaching Protocol

When teaching a concept, the AI:
1. First asks what the human already knows (Activation)
2. Guides through progressive questioning (Guided Discovery)
3. Has the human summarize in their own words (Consolidation)
4. Records gaps in revision_notes.md
5. Updates progress.md

The AI asks ONE question at a time and waits for the answer.
The AI does NOT explain unless the human is genuinely stuck after multiple attempts.

## File Maintenance Rules

- `index.md`: Auto-updated after every ingestion. Lists all files with brief descriptions.
- `log.md`: Auto-updated after every session. Records what was done, added, or changed.
- `progress.md`: Auto-updated after each learning session. Tracks concept mastery.
- `revision_notes.md`: Auto-updated when knowledge gaps are discovered.

## File Boundaries (2026-08-02 新增)

**AI 只允许写以下内容：**
- `research-wiki/wiki/` 下的 AI 管理文件（concepts/、connections/、questions/、index.md、log.md、progress.md、revision_notes.md、会话记录）
- `research-wiki/tools/`（skill 维护脚本，2026-08-02 新增）

**AI 绝对不允许写：**
- `learner_profile.md` — 用户所有，只读
- 代码目录（`skeleton-sp24/`、`library-sp24/`）— 学习作业时须先询问用户、经同意后操作
- `research-wiki/` 之外的任何文件 — 无论内容是什么

> 背景：2026-08-01 发生 AI 越界修改文件的故障，此规则防止复发。违反此规则 = 系统故障。

## 写前检查（2026-08-02 新增）

修改任何 wiki 文件之前：
1. 先运行 `git status` / `git diff <目标文件>`，确认目标文件是否有未提交修改
2. 有未提交修改时：以**工作区当前内容**为准做局部修改；禁止用 HEAD、索引或旧版本重建整文件
3. 写入后核对：目标段落、链接、frontmatter、block 仍然存在

> 背景：文件边界管"能不能写"，写前检查管"怎么写才不破坏"。2026-08-01 事故与 Obsidian Vault Notes 作者记录的事故同源——AI 用旧版本覆盖了用户未提交的新内容。

## 任务路由（2026-08-02 新增）

收到请求先分类，再套对应协议：

| 任务类型 | 走的协议 | 额外约束 |
|---------|---------|---------|
| 教学（讲解/提问/复盘） | Socratic Teaching Protocol | 一次一个问题；关键结构配 SVG 图 |
| 摄入（raw/ 新材料） | Ingestion Protocol | 讨论步骤强制，不可跳过 |
| 维护（index/log/progress/revision） | File Maintenance + 写前检查 | 动手前先 git 检查目标文件 |
| 代码（lab/hw/project） | Grading & Autograder Protocol | 必须先询问用户，获同意才动代码 |
| 技能本身（CLAUDE.md/system.md 修改） | 与用户讨论后修改 | 不经讨论不改 |

**读取范围默认值**：教学会话默认最多打开 3 个概念页；需要更多时先说明再扩展（对齐"最小上下文"原则，防止噪音稀释提问）。

## Reading Level Defaults

When processing materials without explicit instructions:
- New materials default to L1 (can locate it)
- Materials directly related to driving questions default to L2 (can use it)
- Only materials the human explicitly marks as core go to L3+

## Session Start Checklist

On every session start, the AI should:
1. Read this file (system.md)
2. Read learner_profile.md
3. Read course_schedule.md (to know where the user is in the course)
4. Read index.md (to know current wiki state)
5. Read log.md (to know recent activity)
6. Read progress.md (mastery tracking)
7. Read revision_notes.md (knowledge gaps)
8. Check for unprocessed files in raw/
9. Remind human of open questions in wiki/questions/
10. **Suggest the next concrete action** (a specific lecture/lab/hw to tackle)
