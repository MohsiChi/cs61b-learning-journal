# Revision Notes

> Auto-maintained by AI. Knowledge gaps and review items discovered during Socratic sessions.

## Pending Review

### Java 基础

| 遗漏点 | 发现场景 | 优先级 |
|--------|---------|--------|
| Java 泛型（`List<E>`, `Map<K,V>` 的原理） | HW 0B 中用到了泛型语法但不理解 E/K/V 的含义 | 🔴 高 — Week 3 继承学完后必须补 |
| 多态（Polymorphism） | Learner profile 中自述不熟 | 🔴 高 — Week 3-5 核心 |
| `==` vs `.equals()` 底层原理 | common() 方法中踩坑，Object.equals() 默认行为 | 🟡 中 — 继承时学 @Override |
| `static` 变量（类变量）vs 实例变量 | Lab1 中理解了 static 方法，但 static 变量未涉及 | 🟡 中 |
| IntelliJ project/module/library 关系 | 每个模块需独立声明依赖，原理未完全理解 | 🟢 低 — 实践中会逐渐熟悉 |

### C 语言

| 遗漏点 | 发现场景 | 优先级 |
|--------|---------|--------|
| 内存管理（malloc/free） | 讨论 C 指针时自述不会内存管理 | 🟡 中 — CS61C 会覆盖 |
| 结构体指针访问（`p->field` / `(*p).field`） | 教学中发现：C 课程未学到结构体指针语法 | 🟡 中 — 需要时补，或 CS61C 覆盖 |

### 工具链

| 遗漏点 | 发现场景 | 优先级 |
|--------|---------|--------|
| Git 概念模型（clone/push/pull/remote） | 问"克隆=下载？""提交到哪里？" | 🟡 中 — Lab 4: Git 会系统讲 |
| GitHub 公开仓库 vs 私有仓库 | 创建学习记录仓库时需了解 | 🟢 低 |
| `=` vs `==` 经典陷阱 | hailstone 中 `if (x = 1)` | 🟢 低 — 已改正 |

### 递归

| 遗漏点 | 发现场景 | 优先级 |
|--------|---------|--------|
| 递归与迭代的选择判断 | hailstone 中 while 和递归混用 | 🟡 中 — Week 2 链表递归会大量练习 |
| 递归深度 / StackOverflowError | 讨论了递归 vs while 优缺点 | 🟢 低 |

---

## Resolved Items

| 遗漏点 | 解决日期 | 方式 |
|--------|---------|------|
| Java 数组创建语法（`new int[]{}` vs `{}`） | 2026-07-28 | HW 0B makeDice 练习 |
| `String.equals()` 比较字符串而非 `==` | 2026-07-28 | HW 0B takeOrder 练习 |
| `static` 方法 vs 实例方法的含义 | 2026-07-28 | Lab 1 Arithmetic + 讨论 |
| List/ArrayList 基本用法 | 2026-07-28 | HW 0B ListExercises |
| Map/HashMap 基本用法 | 2026-07-28 | HW 0B MapExercises |
| for-each 循环语法 | 2026-07-28 | HW 0B 替代传统 for 循环 |
| `char` 可以 `++`，是数字类型 | 2026-07-28 | letterToNum 练习 |
| Java 字符字面量 `'c'` vs 参数名 `c` | 2026-07-28 | countOccurrencesOfC 练习 |
| null 引用上调用方法 → NullPointerException | 2026-08-08 | SLList 哨兵设计前的引导讨论 |
| Java 字段初始化顺序（默认值 → 字段初始化 → 构造器 body） | 2026-08-08 | 错误方案 `size = 1 + rest.size()` 触发 NPE 时发现 |
| Overload（重载）vs Override（重写） | 2026-08-08 | 多构造器讨论；Override 待 Week 3 继承深入 |
