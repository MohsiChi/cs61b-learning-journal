# Wiki Index — CS61B

> Auto-maintained by AI. Last updated: 2026-08-08

## Raw Materials Inventory

### clips/
- **csdiy-cs61b-guide.md** — CS DIY wiki CS61B 中文指南。课程概览与资源索引。来源: csdiy.wiki

### courses/
- **sp24-course-website** — Spring 2024 课程官网 (sp24.datastructur.es)。包含完整 15 周课程日历、40 讲 Lecture 录像/幻灯片、13 次 Discussion 习题与解答、10 个 Lab 说明、4 个 Homework、3 个大型 Project。讲师: Justin Yokota, Peyrin Kao。
- **sp21-course-website** — Spring 2021 公开版本 (sp21.datastructur.es)。Gradescope 课程码 MB7ZPY，支持 auto-grader 自评。
- **fa23-course-website** — Fall 2023 版本 (fa23.datastructur.es)
- **sp23-course-website** — Spring 2023 版本 (sp23.datastructur.es)
- **sp18-course-website** — Spring 2018 版本 (sp18.datastructur.es)，Josh Hug 经典版本

### textbooks/
- **cs61b-gitbook** — CS61B 官方教材 (39 chapters, GitBook)。涵盖从 Java 基础到 P=NP 的全部课程内容。来源: cs61b-2.gitbook.io/cs61b-textbook

### videos/
- **youtube-playlists** — 每讲对应的 YouTube 播放列表。原版英文视频，B站有中文翻译搬运。
- **bilibili-mirror** — B站 CS61B 中文翻译视频

### reference-implementations/
- **PKUFlyingPig/CS61B** — GitHub 作业参考实现（可能为私有仓库）
- **InsideEmpire/CS61B-PathwayToSuccess** — GitHub 作业参考实现与学习路径

### tools/
- **Gradescope** — 课程码 MB7ZPY (SP2021)，可用于自评代码
- **IntelliJ** — 推荐 IDE，课程有保姆级配置教程

---

## Concepts

| 概念 | 状态 | 模块 |
|------|------|------|
| [[java-classes-objects]] | stub | Week 1: Java 基础 |
| [[java-static-methods]] | 🌱 learned | Week 1: static vs 实例方法 |
| [[java-equals-vs-doubleequals]] | 🌱 learned | Week 1: == vs .equals() 陷阱 |
| [[java-collections-list-map]] | 🌱 learned | Week 1: List & Map 快速参考 |
| [[java-recursion]] | 🌱 learned | Week 1-2: Java 递归 |
| [[references-and-recursion]] | 🌱 learned | Week 2: 引用与递归 — Lec 03 完成 |
| [[linked-lists]] | 🌱 learned | Week 2-3: 链表 — Lec 04 SLList 完成 |
| [[arrays-and-arraylists]] | stub | Week 2-3: 数组 |
| [[testing-and-tdd]] | stub | Week 3: 测试 |
| [[inheritance-polymorphism]] | stub | Week 3-5: 继承与多态 |
| [[asymptotics]] | stub | Week 5-6: 渐进分析 |
| [[disjoint-sets]] | stub | Week 5-6: 并查集 |
| [[adts-and-bsts]] | stub | Week 6: 抽象数据类型与二叉搜索树 |
| [[b-trees]] | stub | Week 7: B树 |
| [[red-black-trees]] | stub | Week 7: 红黑树 |
| [[hashing]] | stub | Week 7-8: 哈希 |
| [[heaps-and-pqs]] | stub | Week 8: 堆与优先队列 |
| [[graph-traversals]] | stub | Week 8-9: 图遍历 |
| [[shortest-paths]] | stub | Week 9: 最短路径 |
| [[minimum-spanning-trees]] | stub | Week 9: 最小生成树 |
| [[dags-and-toposort]] | stub | Week 10: DAG与拓扑排序 |
| [[tries]] | stub | Week 10: 前缀树 |
| [[sorting-algorithms]] | stub | Week 12-15: 排序算法 |
| [[compression]] | stub | Week 15: 压缩 |
| [[p-vs-np]] | stub | Week 15: 计算复杂度 |

---

## Connections

- [[lists-to-trees]] — 链表 → 树结构 (泛化)
- [[asymptotics-to-sorting]] — 渐进分析 → 排序比较 (应用)
- [[hashing-to-hashmaps]] — 哈希 → HashMap 实现 (实现)
- [[graphs-to-shortest-paths]] — 图遍历 → 最短路径 (算法递进)

---

## Open Questions

- [[java-vs-python-ds]] — Java 静态类型与 C 的类型系统如何影响数据结构设计？（2026-08-02 已按无 Python 基础重写）
- [[recursion-vs-iteration-java]] — 在 Java 中递归和迭代的实际性能差异？JVM 如何优化递归？
- [[balanced-trees-why]] — 为什么需要这么多平衡树变体（B-Tree, RBT, AVL, LLRB）？各自的工程适用场景是什么？
- [[hashing-collisions]] — 哈希碰撞的各种解决策略（Chaining, Open Addressing, Cuckoo Hashing）在 Java 标准库中如何选择？

---

## System Pages

- [[course_schedule]] — CS61B Spring 2024 15周课程路线图
- [[learner_profile]] — 学习偏好与背景
- [[progress]] — 学习进度追踪
- [[revision_notes]] — 知识漏洞与复习清单
- [[system]] — 系统运转规则
