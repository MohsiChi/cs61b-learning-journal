---
title: "Linked Lists: IntList → SLList"
date: 2026-08-08
tags: [CS61B, Data-Structures, Lists, Week2-3, Java]
status: learned
---

# Linked Lists — 从 IntList 到 SLList

> 2026-08-08 由 stub 填充（Lec 04: Lists II — SLLists，Textbook Ch 4）

## 核心问题回顾
- IntList 为什么不好用？三个不方便
- SLList 的设计如何逐一解决？
- Sentinel node（哨兵/占位节点）的作用
- 嵌套类 (nested class) 的意义：归属 + 封装

## 1. IntList 的三个不方便（问题驱动）

| 不方便 | 后果 |
|--------|------|
| 空列表 = null | 使用者每次使用都要判空，漏了就 NullPointerException |
| 头插必须手动 `L = new IntList(x, L)` | 忘了赋值就静默丢数据（不报错，更难排查） |
| 没有 size 信息 | 每次 size() 从头数一遍 O(N)；循环条件里用 size() → O(N²) |

关键认知：**负担被推给使用者**。判空、记住赋值模式、承受性能——全是使用者的事。

## 2. SLList：包装盒设计

```java
public class SLList {
    public static class IntNode {      // 改名后的节点类（原 IntList）
        public int item;               // 值
        public IntNode next;           // 指向下一个节点（自引用只在这里）
        public IntNode(int i, IntNode n) { item = i; next = n; }
    }
    private IntNode first;             // 指向第一个节点（是引用，不是 int！）
    private int size;                  // 长度，只有这一个地方存
    ...
}
```

设计要点：
- **列表 ≠ 节点**：包装盒（SLList）持有 size + first 引用；节点链（IntNode）是内部细节
- **private 封装**：使用者摸不到内部字段，只能通过方法操作 → 不会把结构改坏
- **嵌套类**：IntNode 只服务于 SLList（归属），外面世界不知道它存在（封装）
- 参考：IntList 里"列表 = 第一个节点"，长度信息无处安放 → 这是 SLList 存在的根本原因

## 3. 哨兵节点（Sentinel）—— 消除所有 null

问题：空列表怎么表示？`first = null` 会让每个方法都要判空（负担搬进实现里）。

解法：构造器里创建**占位节点**，`first` 永远指向它，永不指向 null：

```java
public SLList() {
    first = new IntNode(0, null);   // 占位节点：item 随便填，一生只创建一次
    size = 0;
}
```

空列表 = 占位节点孤零零（`占位.next == null`）。于是：

```java
public void addFirst(int x) {
    first.next = new IntNode(x, first.next);  // RHS 先造新节点（next = 旧 first.next），再接到占位节点后面
    size += 1;
}
public int getFirst() {
    return first.next.item;                   // 跳过占位节点
}
public int size() {
    return size;                              // O(1)，字段直读
}
```

- 没有 if、没有 null——结构上不可能为空
- 占位节点**永不更换**：addFirst 只动 first.next，绝不重新赋值 first
- size 字段由方法内部维护 → 不会过期（使用者无路绕过）

## 4. 其他收获
- **Overloading（重载）**：同名单参数列表不同（如双构造器）。与 Override（重写，继承）区分
- 方法名与字段名可以相同（`size()` 方法与 `size` 字段），字段/方法命名空间不同

## 对比总结

| | IntList | SLList |
|---|---|---|
| 空列表 | null（判空负担） | 占位节点（无 null） |
| 头插 | 手动赋值，会静默丢数据 | addFirst 方法内部完成 |
| size() | O(N) 递归 | O(1) 字段 |
| 结构可见性 | 全 public | private 封装 |
| 使用者心智 | 自己管理节点链 | 只面对一个列表对象（ADT 雏形） |

## 未覆盖（后续补）
- DLLists（Lec 05）、ArrayList 数组实现（Lec 05）
- 泛型 SLList\<E\>（Proj1A 前学）
- get(i) 仍 O(N) → 数组实现解决

## 资源
- Lec 04 (Spring 2024): Lists II — SLLists
- Textbook Ch 4: SLLists
- 相关：[[references-and-recursion]] [[arrays-and-arraylists]] [[java-classes-objects]]
