---
title: "Java 递归 (Recursion)"
date: 2026-07-28
tags: [CS61B, Java, Recursion, Week1-2]
status: L2-learned
source: [HW 0B: JavaExercises.hailstone()]
---

# Java 递归

## 什么是递归

函数调用自己来解决问题。冰雹序列是最直观的例子：

```
n = 20
20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

规则：
  偶数 → n/2
  奇数 → 3n+1
  到 1 → 停止
```

## 两种写法

### 迭代（while 循环）

```java
List<Integer> list = new ArrayList<>();
int x = n;
while (x != 1) {
    list.add(x);
    x = (x % 2 == 0) ? x / 2 : 3 * x + 1;
}
list.add(1);
return list;
```

### 递归（方法调用自己）

```java
private static List<Integer> hailstoneHelper(int x, List<Integer> list) {
    list.add(x);                              // 1. 记录当前数字
    if (x == 1) { return list; }              // 2. 终止条件
    else if (x % 2 == 0) {
        return hailstoneHelper(x / 2, list);  // 3. 偶数 → 递归
    } else {
        return hailstoneHelper(3*x + 1, list); // 3. 奇数 → 递归
    }
}
```

## 递归的必要条件

1. **终止条件（base case）**：`if (x == 1) return list;` —— 没有这个会无限递归
2. **每次递归离终止更近一步**：x 在不断变小/接近 1
3. **return 递归调用**：把结果一层层传回去

## Accumulator Pattern（累加器模式）

```java
hailstone(20)
  → hailstoneHelper(20, [])
    → list.add(20)         // list = [20]
    → hailstoneHelper(10, [20])
      → list.add(10)       // list = [20, 10]
      → hailstoneHelper(5, [20, 10])
        ...
        → hailstoneHelper(1, [20,10,5,16,8,4,2])
          → list.add(1)    // list = [20,10,5,16,8,4,2,1]
          → return list    // x==1，终止！
```

`list` 作为参数一路传递，每一层往里加一个数。这就是 accumulator pattern。

## 常见陷阱

| 陷阱 | 例子 | 后果 |
|------|------|------|
| 用 `=` 代替 `==` | `if (x = 1)` | 永远为 true，死循环 |
| 忘记 return | `hailstoneHelper(x/2, list)` 不加 return | 返回值丢失 |
| 递归里写 while | 递归和循环混用 | 逻辑混乱，递归调用栈浪费 |
| 没有终止条件 | 忘了 `if (x == 1)` | StackOverflowError |

## 知识遗漏提醒

- [ ] 递归和迭代各有什么优缺点？（递归简洁但耗栈空间，迭代高效但有时不好写）
- [ ] 什么是 StackOverflowError？递归深度能有多大？
- [ ] 尾递归优化是什么？Java 支持吗？（不支持）
- [ ] 什么时候该用递归？什么时候不该？（树遍历天然适合递归，简单循环没必要递归）

## 相关概念

- [[references-and-recursion]] — CS61B Week 2 用递归操作链表
- [[asymptotics]] — 递归算法的时间复杂度分析
