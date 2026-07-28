---
title: "Java List 和 Map 快速参考"
date: 2026-07-28
tags: [CS61B, Java, Collections, List, Map, Week1]
status: L2-learned
source: [HW 0B: ListExercises, MapExercises]
---

# Java List 和 Map 快速参考

## 思维模型

```
数组 / List：数字索引 → 值         Map：任意 key → 值
┌───┬───┬───┬───┐          ┌───────┬───────┐
│ 0 │ 1 │ 2 │ 3 │          │"apple"│   5   │
├───┼───┼───┼───┤          ├───────┼───────┤
│ a │ b │ c │ d │          │"banana"│  3   │
└───┴───┴───┴───┘          └───────┴───────┘
  list.get(0) → "a"          map.get("apple") → 5
```

| 特性 | 数组 `int[]` | List\<E\> | Map\<K,V\> |
|------|-------------|-----------|------------|
| 大小 | 固定 | 动态增长 | 动态增长 |
| 索引/键类型 | `int` (0,1,2...) | `int` (0,1,2...) | 任意对象 |
| 查元素 | `arr[i]` | `list.get(i)` | `map.get(key)` |
| 设元素 | `arr[i] = v` | `list.set(i, v)` | `map.put(k, v)` |
| 长度 | `arr.length` | `list.size()` | `map.size()` |
| 遍历 | `for(i=0;...)` | for-each | `for (K k : map.keySet())` |

## List<E> 常用操作

```java
List<Integer> list = new ArrayList<>();
list.add(5);              // [5]
list.add(10);             // [5, 10]
list.get(0);              // 5
list.size();              // 2

// 遍历方式1：需要索引
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}

// 遍历方式2：不需要索引 → for-each 更干净
for (Integer x : list) {
    System.out.println(x);
}
```

## Map<K,V> 常用操作

```java
Map<Character, Integer> map = new HashMap<>();
map.put('a', 1);          // {'a': 1}
map.put('b', 2);          // {'a': 1, 'b': 2}
map.get('a');             // 1
map.get('z');             // null（key 不存在）
map.containsKey('a');     // true

// 遍历
for (char key : map.keySet()) {
    System.out.println(key + " → " + map.get(key));
}
```

## 设计思想

List、Map、数组都遵循同一个模式：**有顺序的容器，用索引/key 访问元素**。

| 容器 | 里面装什么 | 长度 | 取第 i 个 |
|------|----------|------|----------|
| String | `char`（基本类型） | `.length()` | `.charAt(i)` |
| List\<E\> | 任意对象 E | `.size()` | `.get(i)` |
| 数组 `T[]` | 任意类型 T | `.length` | `[i]` |

同一个抽象，不同的名字——Java 早期设计的瑕疵，但模式是统一的。

## 知识遗漏提醒

- [ ] `ArrayList` vs `LinkedList` 有什么区别？各适合什么场景？
- [ ] `HashMap` 内部是怎么实现 O(1) 查找的？（哈希表原理，Week 7-8 会学）
- [ ] `Map` 里如果放重复的 key 会怎样？（旧值被覆盖）
- [ ] `List.of()` 和 `new ArrayList<>()` 有什么区别？（不可变 vs 可变）

## 相关概念

- [[java-arrays]] — Java 数组
- [[hashing]] — HashMap 背后的哈希原理（Week 7-8）
- [[linked-lists]] — LinkedList 的实现（Week 2）
