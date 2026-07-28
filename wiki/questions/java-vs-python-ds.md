---
title: "Java 静态类型如何影响数据结构设计？"
date: 2026-07-06
tags: [Java, Python, type-systems, design]
status: open
---

# Java vs Python：类型系统对数据结构设计的影响

Java 的静态类型和 Python 的动态类型在设计数据结构时各有什么优劣？

## 思考方向
- Java 的泛型 (Generics) 提供了编译时类型安全，但也带来了类型擦除 (type erasure) 的局限
- Python 的 duck typing 让代码更灵活，但在大型项目中可能导致运行时类型错误
- Java 的 Interface 体系强制明确契约，Python 的 Protocol 是隐式的
- 在实现一个通用数据结构时（如 HashMap），两种语言的策略有何不同？

## 已有知识
- Java 泛型 (已知)
- Python duck typing (已知 CS61A)
- C 的 void* 和手动类型管理

## 相关
- [[inheritance-polymorphism]]
- [[hashing]]
