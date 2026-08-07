# Learning Progress

> Auto-maintained by AI. Tracks concept mastery over time.

## Mastery Overview

| Concept | Level | Last Practiced | Notes |
|---------|-------|---------------|-------|
| Java static methods | L2 (can use) | 2026-07-28 | 理解 static vs 实例方法的区别 |
| Java arrays | L2 (can use) | 2026-07-28 | `new int[]{}`, `.length` |
| List\<E\> and ArrayList | L2 (can use) | 2026-07-28 | `.add()`, `.get()`, `.size()`, for-each |
| Map\<K,V\> and HashMap | L2 (can use) | 2026-07-28 | `.put()`, `.get()`, `.containsKey()`, `.keySet()` |
| Java recursion | L2 (can use) | 2026-07-28 | Hailstone 递归实现，理解 accumulator pattern |
| String methods | L2 (can use) | 2026-07-28 | `.charAt()`, `.length()`, `.equals()` |
| Java generics (basic) | L1 (seen it) | 2026-07-28 | `List<Integer>`, `Map<Character, Integer>` 语法，原理待深入 |
| Java for-each loop | L2 (can use) | 2026-07-28 | `for (Type x : collection)` 模式 |
| Java references vs primitives | L3 (can explain) | 2026-07-31 | 门牌号 vs 房子，值拷贝 vs 地址拷贝 |
| Self-referential types | L2 (can use) | 2026-07-31 | IntList rest 字段类型就是 IntList |
| Recursive linked list ops | L2 (can use) | 2026-07-31 | size(), get(i) 递归实现 |
| Linked list construction | L2 (can use) | 2026-07-31 | new IntList + 头插法 |
| SLList 包装盒设计 | L3 (can explain) | 2026-08-08 | size 字段 + first 引用；列表 ≠ 节点 |
| 哨兵节点（sentinel） | L2 (can use) | 2026-08-08 | 占位节点消除所有 null 判断；addFirst 只动 first.next |
| size 字段缓存 | L2 (can use) | 2026-08-08 | size() = O(1)，对比 IntList 递归 O(N) |
| Overloading（重载） | L2 (can use) | 2026-08-08 | 多构造器；与 Override 区分 |
| 嵌套类（nested class） | L2 (can use) | 2026-08-08 | IntNode 归属 + 封装 |

## Recently Learned

| 概念 | 日期 | 来源 |
|------|------|------|
| Java 引用 vs 基本类型（值拷贝 vs 地址拷贝） | 2026-07-30 | Lec 03 Part 1 |
| `new` 与堆分配、`null` | 2026-07-30 | Lec 03 Part 1 |
| 自引用类型（IntList rest） | 2026-07-31 | Lec 03 Part 2 |
| 递归 size() / get(i) | 2026-07-31 | Lec 03 Part 2 |
| 链表构建（头插法） | 2026-07-31 | Lec 03 Part 2 |
| null 上调用方法 → NullPointerException | 2026-08-08 | 会话引导（IntList 判空问题） |
| SLList 包装盒 + 哨兵节点 + size 字段 | 2026-08-08 | Lec 04 |
| Overloading vs Override | 2026-08-08 | Lec 04 |

## Needs Review

> 详细清单见 [[revision_notes]]。以下为高优先级待补项：

| 概念 | 优先级 | 计划时间 |
|------|--------|---------|
| Java 泛型原理（E/K/V 含义） | 🔴 高 | Week 3 继承学完后 |
| 多态（Polymorphism） | 🔴 高 | Week 3-5 |
| `==` vs `.equals()` 底层 | 🟡 中 | 学习 @Override 时 |
| 递归 vs 迭代选择 | 🟡 中 | Week 2-3 链表练习 |

---

## 课程模块进度

| 模块 | 周次 | 状态 | 完成日期 |
|------|------|------|---------|
| Module 1: Java + Lists | Week 1-3 | 🔄 进行中 | — |
| └ Week 1: Setup + Java Review | Week 1 | ✅ 已完成 | 2026-07-28 |
| └ Week 2: References + Lists | Week 2 | 🔄 进行中 (Lec 03 ✓ Lec 04 ✓) | — |
| Proj0: 2048 | Week 1-2 | ⬜ 未开始 | — |
| Proj1A: LinkedListDeque61B | Week 3-4 | ⬜ 未开始 | — |
| Proj1B: ArrayDeque61B | Week 4 | ⬜ 未开始 | — |
| Module 2: Inheritance + Asymptotics | Week 3-6 | ⬜ 未开始 | — |
| Proj1C: Deque61B Enhancements | Week 5 | ⬜ 未开始 | — |
| Module 3: Trees + Hashing | Week 6-8 | ⬜ 未开始 | — |
| Proj2A: NGrams | Week 6-7 | ⬜ 未开始 | — |
| Module 4: Graphs | Week 8-10 | ⬜ 未开始 | — |
| Proj2B/C: Wordnet | Week 9-10 | ⬜ 未开始 | — |
| Module 5: Sorting + Advanced | Week 12-15 | ⬜ 未开始 | — |
| Proj3: BYOW | Week 12-15 | ⬜ 未开始 | — |

### 图例
- ⬜ 未开始
- 🔄 进行中
- ✅ 已完成
