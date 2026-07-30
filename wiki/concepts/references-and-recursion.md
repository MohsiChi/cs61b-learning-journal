---
title: "References and Recursion in Java"
date: 2026-07-31
tags: [CS61B, Java, Recursion, Week2]
status: learned
---

# References and Recursion in Java

## Java 的两种类型

| 类型 | 存什么 | 拷贝行为 | 类比 |
|------|--------|---------|------|
| 基本类型 (8 种: int, double, char, boolean...) | 值本身 | 拷贝值，互不影响 | 盒子里直接放东西 |
| 引用类型 (所有类/数组) | 堆上对象的地址 (64 位) | 拷贝地址，共享同一对象 | 盒子里放门牌号，指向 heap 里的房子 |

### `new` 关键字
- 在堆 (heap) 上分配内存、创建对象、返回地址
- **变量 ≠ 对象**：变量是门牌号，对象是房子

### `null`
- 地址为 0，不指向任何对象
- 相当于 C 的 `NULL`

### 核心原则
- 基本类型赋值：值拷贝 → 完全独立
- 引用类型赋值：地址拷贝 → 共享同一对象，一方修改影响另一方

## 自引用类型 (Self-Referential Type)

链表节点类使用自引用：`IntList rest` 的类型就是 `IntList` 本身。

```java
public class IntList {
    public int first;
    public IntList rest;

    public IntList(int first, IntList rest) {
        this.first = first;
        this.rest = rest;
    }
}
```

**为什么不矛盾？** `rest` 存的是地址（固定 64 位），不是对象的完整副本。不会导致无限嵌套。

## 递归操作链表

链表天然适合递归：
> 一个链表 = 当前节点 (first) + 剩余链表 (rest)

### size() — 递归求长度
```java
public int size() {
    if (rest == null) return 1;   // base case: 我是最后一个节点
    return 1 + rest.size();        // recursive case: 我 + 后面
}
```

### get(int i) — 递归取第 i 个元素
```java
public int get(int i) {
    return i > 0 ? rest.get(i - 1) : first;
}
```

### 构建链表
```java
IntList L = new IntList(5, null);
L.rest = new IntList(10, null);
L.rest.rest = new IntList(15, null);
```

**头插法**: `IntList L2 = new IntList(3, L);` — 一行加节点到头部

## 与已知知识的关联
- **C 指针** → Java 引用是安全指针（无指针运算，不能加减地址）
- **Python 对象引用** (CS61A) → Java 引用受静态类型约束（`IntList rest` 只能是 IntList 或 null）

## 为什么需要 SLList？
裸 IntList 的弊端：
- `L.rest.rest.rest = ...` 容易出错
- 用户直接操作内部结构，不安全
- → 需要封装类 (SLList) 隐藏裸节点

## 资源
- Lec 03 (Spring 2024)
- Textbook Ch 3
