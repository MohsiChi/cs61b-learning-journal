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
- **C 结构体嵌套指针** → Java 对象引用受静态类型约束（`IntList rest` 只能是 IntList 或 null）

## 为什么需要 SLList？
裸 IntList 的弊端：
- `L.rest.rest.rest = ...` 容易出错
- 用户直接操作内部结构，不安全
- → 需要封装类 (SLList) 隐藏裸节点

## 结构图：IntList 的内存布局（SVG）

> 每个节点 = 两个格：左边 `first`（值），右边 `rest`（指向下一个节点的地址）。变量 `L` 只是指向第一个节点的门牌号。

<svg viewBox="0 0 580 130" xmlns="http://www.w3.org/2000/svg" font-family="Consolas, monospace, sans-serif">
<defs>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/>
</marker>
</defs>
<text x="290" y="18" font-size="14" text-anchor="middle" fill="#444">IntList 内存结构：3 → 10 → 15</text>
<rect x="30" y="40" width="140" height="70" fill="white" stroke="#333" stroke-width="2"/>
<line x1="100" y1="40" x2="100" y2="110" stroke="#333" stroke-width="2"/>
<text x="65" y="85" font-size="20" text-anchor="middle">3</text>
<text x="135" y="85" font-size="18" text-anchor="middle">→</text>
<rect x="220" y="40" width="140" height="70" fill="white" stroke="#333" stroke-width="2"/>
<line x1="290" y1="40" x2="290" y2="110" stroke="#333" stroke-width="2"/>
<text x="255" y="85" font-size="20" text-anchor="middle">10</text>
<text x="325" y="85" font-size="18" text-anchor="middle">→</text>
<rect x="410" y="40" width="140" height="70" fill="white" stroke="#333" stroke-width="2"/>
<line x1="480" y1="40" x2="480" y2="110" stroke="#333" stroke-width="2"/>
<text x="445" y="85" font-size="20" text-anchor="middle">15</text>
<text x="520" y="85" font-size="15" text-anchor="middle" fill="#888">null</text>
<line x1="170" y1="75" x2="216" y2="75" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
<line x1="360" y1="75" x2="406" y2="75" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
<text x="12" y="80" font-size="18" font-weight="bold">L</text>
<line x1="16" y1="75" x2="28" y2="75" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
</svg>

**看这张图回答**：`L` 能直接"走到"第 3 个节点吗？如果某个用户执行 `L.rest.rest = 另一个链表`，图会怎么变？——这就是 SLList 要封装的隐患。

## 资源
- Lec 03 (Spring 2024)
- Textbook Ch 3
