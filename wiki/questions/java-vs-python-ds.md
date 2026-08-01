---
title: "Java 静态类型如何影响数据结构设计？"
date: 2026-08-02
tags: [Java, C, type-systems, design]
status: open
---

# Java vs C：类型系统对数据结构设计的影响

> 原题含 Python 对比，因学习者无 Python 基础，于 2026-08-02 重写为 Java vs C 对比。

Java 的静态类型和 C 的类型系统在设计数据结构时各有什么优劣？

## 思考方向
- Java 的泛型 (Generics) 提供编译时类型安全，但类型擦除 (type erasure) 带来什么局限？C 的 `void*` 又付出了什么代价？
- Java 的 Interface 体系强制明确契约；C 用 struct + 函数指针模拟接口，靠什么保证契约？
- 实现一个通用数据结构（如 HashMap）时，Java 和 C 的策略有何不同？
- Java 引用（安全的指针）如何让链表/树实现比 C 的裸指针更安全？

## 已有知识
- Java 泛型 (已知，原理待深入)
- C 指针与 struct (已知)
- C 内存管理 malloc/free (待学，CS61C 覆盖)

## 相关
- [[inheritance-polymorphism]]
- [[hashing]]
- [[java-equals-vs-doubleequals]]
