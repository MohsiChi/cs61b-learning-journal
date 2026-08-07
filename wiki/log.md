# Activity Log

> Auto-maintained by AI.

| Date | Action | Details |
|------|--------|---------|
| 2026-07-06 | System initialized | Research wiki created in D:\BU\BU_Y2_S1\DATA Stru&Algo\research-wiki\ |
| 2026-07-06 | Materials scraped | Scraped CS61B course info from csdiy.wiki (course overview) and sp24.datastructur.es (full 15-week schedule, 40 lectures, 10 labs, 4 homeworks, 3 projects) |
| 2026-07-06 | Wiki seeded | Created all system files (system.md, CLAUDE.md, course_schedule.md, learner_profile.md, index.md, progress.md, revision_notes.md, log.md) with full CS61B Spring 2024 curriculum structure |
| 2026-07-06 | Resource links indexed | Documented all course resources: textbook (cs61b-2.gitbook.io, 39 chapters), YouTube playlists per lecture, Google Slides, Discussion PDFs, Lab specs, Gradescope (MB7ZPY), reference repos (PKUFlyingPig/CS61B, InsideEmpire/CS61B-PathwayToSuccess) |
| 2026-07-06 | Concepts scaffolded | Created 21 concept stubs covering all major CS61B topics from Java classes through P=NP |
| 2026-07-06 | Connections + Questions seeded | Created 4 connection pages and 4 open question pages to bootstrap the knowledge cycle |
| 2026-07-28 | Env setup complete | JDK 21, IntelliJ 2026.2, Git 2.54, Clash proxy configured, library-sp24 + skeleton-sp24 cloned |
| 2026-07-28 | Lab 1 completed | Arithmetic.java — fixed sum() bug, learned static vs instance, ran IntelliJ tests |
| 2026-07-28 | HW 0B completed | JavaExercises (4/4), ListExercises (4/4), MapExercises (3/3) — all tests pass |
| 2026-07-28 | Learner profile corrected | Updated: no Python background, Java generics/polymorphism weak, C pointers OK but no memory mgmt |
| 2026-07-28 | Concepts created | 4 new concept pages: [[java-static-methods]], [[java-collections-list-map]], [[java-equals-vs-doubleequals]], [[java-recursion]] |
| 2026-07-28 | Revision notes populated | 12 knowledge gaps identified, 8 resolved during session |
| 2026-07-28 | Index updated | Wiki index now reflects all new and existing content |
| 2026-07-30 | Lec 03 (Part 1) | References: 基本类型 vs 引用类型, new, null, 值拷贝 vs 地址拷贝 |
| 2026-07-31 | Lec 03 (Part 2) | IntList 自引用类型, 递归 size()/get(), 构建链表, 头插法 |
| 2026-07-31 | Concept filled | [[references-and-recursion]] stub → learned, 完整笔记 |
| 2026-07-31 | Session complete | Lec 03 完成, session note finalized |
| 2026-08-02 | 全库体检与维护 | ① git 校验：全部提交无损，Lec 03 状态正确（昨日故障未伤及 wiki）② 补建 16 个概念 stub 与 index.md 对齐 ③ 重写 [[java-vs-python-ds]]（去 Python，改 Java vs C）④ 清理 4 个概念页 Python 类比 ⑤ progress.md 补齐 Recently Learned / Needs Review ⑥ 修正 CLAUDE.md（4 projects、移除 CS61A 声明）⑦ 新增文件边界规则 + Python 禁用规则（CLAUDE.md + system.md）⑧ 与 sp24 官网核对 course_schedule 一致 |
| 2026-08-02 | 待办提醒 | raw/clips/csdiy-cs61b-guide.md 自 07-06 起未消化，按摄入协议需与用户讨论后编译 |
| 2026-08-02 | Skill 锤炼（参考 Obsidian Vault Notes 作者架构） | ① CLAUDE.md 新增非协商条款 #10 写前检查（git status/diff 后再写，禁整文件重建）② system.md 新增写前检查、任务路由表、读取范围默认值（≤3 概念页）③ 新增 tools/wiki_check.py 一致性校验（wikilink 解析、index 漂移、状态统计）④ 修复：index 4 个缺失 stub（2 connections + 2 questions，含 .md 后缀坑）⑤ 修复死链 java-arrays→arrays-and-arraylists ⑥ README 补 tools/ 与日志 ⑦ 校验通过：25 概念页（20 stub + 5 learned）零问题 |
| 2026-08-08 | Lec 04 (SLList) 教学会话 | ① IntList 三个不方便引导（判空/NPE、头插静默丢数据、size O(N) 循环爆炸）② SLList 包装盒设计（size 字段 + first 引用 + 嵌套 IntNode）③ 哨兵节点消除所有 null ④ addFirst/getFirst/size 实现 ⑤ 概念页 [[linked-lists]] stub → learned ⑥ 记录新缺口：C 结构体指针语法未学 ⑦ 解决：NPE、字段初始化顺序、Overload vs Override |
