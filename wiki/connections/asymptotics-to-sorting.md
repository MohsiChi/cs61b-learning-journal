---
title: "Asymptotics → Sorting (应用关系)"
date: 2026-07-06
type: connection
connects: [asymptotics, sorting-algorithms]
relationship: application
---

# Asymptotics → Sorting

渐进分析最经典的应用场景就是排序算法的比较。

## 关键洞察
- 每个排序算法都有 Best / Average / Worst case 复杂度
- 基于比较的排序有理论上限：Ω(N log N)
- 为什么 Quicksort 在实际中比 Mergesort 快？（缓存局部性、常数因子）
- 为什么 Java 的 `Arrays.sort()` 对 primitive 用 Quicksort、对 Object 用 Timsort？

## 追问
如果基于比较的排序有下界，Radix Sort 如何"绕过"这个限制？它牺牲了什么？
