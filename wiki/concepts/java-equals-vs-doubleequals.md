---
title: "Java == vs .equals()"
date: 2026-07-28
tags: [CS61B, Java, Pitfall, Week1]
status: L2-learned
source: [HW 0B: ListExercises.common()]
---

# Java == vs .equals()

## 一句话

| | `==` | `.equals()` |
|------|------|------------|
| 基本类型 (int, char, double...) | ✅ 比值 | ❌ 不能用 |
| 对象类型 (Integer, String, List...) | ⚠️ 比内存地址 | ✅ 比内容 |

## 例子

```java
// 基本类型：== 比值
int a = 5;
int b = 5;
System.out.println(a == b);  // true ✅

// 对象类型：== 比地址（坑！）
Integer x = 200;
Integer y = 200;
System.out.println(x == y);       // false！两个不同的对象
System.out.println(x.equals(y));  // true ✅

String s1 = new String("hello");
String s2 = new String("hello");
System.out.println(s1 == s2);       // false！不同地址
System.out.println(s1.equals(s2));  // true ✅
```

## Integer 的隐藏陷阱

Java 缓存了 -128 到 127 的 Integer 对象：

```java
Integer a = 100;
Integer b = 100;
System.out.println(a == b);  // true！（在缓存范围内，是同一个对象）

Integer c = 200;
Integer d = 200;
System.out.println(c == d);  // false！（超出缓存，不同对象）
```

**所以 == 对 Integer 有时候对有时候错——永远用 .equals() 就对了。**

## C 语言类比

```c
// C 里 == 永远比值
int a = 5, b = 5;
a == b;  // true

char *s1 = "hello";
char *s2 = "hello";
s1 == s2;  // 比指针地址，不一定相等（和 Java 的 == 一样）
strcmp(s1, s2) == 0;  // 比内容（和 Java 的 .equals() 一样）
```

## 规则

> 对象之间比内容 → 用 `.equals()`
> 基本类型比大小 → 用 `==`
> 不确定？用 `.equals()` 不会错

## 知识遗漏提醒

- [ ] `==` 和 `.equals()` 的底层原理是什么？（Object 类的 equals 默认就是用 ==）
- [ ] 为什么 String 的 equals 能比内容？（因为 String 重写了 equals 方法）
- [ ] 自己写的类需要重写 equals() 吗？怎么正确重写？

## 相关概念

- [[java-classes-objects]] — Object 类的 equals 方法
- [[inheritance-polymorphism]] — 方法重写 (@Override)，equals 是典型例子
