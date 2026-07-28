---
title: "为什么需要这么多平衡树变体？"
date: 2026-07-06
tags: [trees, database, engineering]
status: open
---

# Balanced Trees: 为什么变体如此之多？

2-3 Tree, Red-Black Tree, AVL Tree, LLRB Tree, B-Tree, B+Tree... 为什么一个"平衡"的概念衍生出了这么多不同的实现？

## 思考方向
- AVL Tree 的严格平衡 vs RBT 的宽松平衡——什么时候严格更好？
- B-Tree 的设计动机：磁盘 I/O 最小化（数据库索引的核心）
- LLRB 把 2-3 Tree 映射到 BST——实现上的简化 vs 理解上的间接
- Java 的 TreeMap 用的是 RBT，为什么不是 AVL 或 B-Tree？

## 工程视角
每种平衡树都是为了解决特定场景下的工程约束而设计的。理解"为什么需要这一种"比记住旋转规则更重要。

## 相关
- [[b-trees]]
- [[red-black-trees]]
- [[adts-and-bsts]]
