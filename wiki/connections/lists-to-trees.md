---
title: "Lists → Trees (泛化关系)"
date: 2026-07-06
type: connection
connects: [linked-lists, adts-and-bsts]
relationship: generalization
---

# Lists → Trees

链表和树的根本关系：**树是链表的泛化**。

## 关键洞察
- 单向链表每个节点有 1 个 next → 二叉树每个节点有 2 个 next (left, right)
- 链表的递归定义：List = Node + Rest-of-List
- 树的递归定义：Tree = Root + Left-Subtree + Right-Subtree
- 操作上的类比：链表遍历 → 树的 DFS/BFS

## 追问
如果树是链表的泛化，图又是树的泛化——这种"泛化链"在数据结构设计中反复出现。你能想到其他例子吗？
