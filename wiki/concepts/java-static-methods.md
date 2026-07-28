---
title: "Java Static 方法与实例方法"
date: 2026-07-28
tags: [CS61B, Java, OOP, static, Week1]
status: L2-learned
source: [Lab 1, HW 0B]
---

# Java Static 方法与实例方法

## 核心概念

Java 的方法分两种：

| | static 方法 | 实例方法 |
|------|------------|---------|
| 属于谁 | 类本身 | 每个对象 |
| 怎么调用 | `ClassName.method()` | `obj.method()` |
| 有 `this` 吗 | ❌ 没有 | ✅ 有，指向当前对象 |
| C 语言类比 | 普通函数 | 操作 struct 的函数（传指针） |
| 访问实例变量 | ❌ 不行 | ✅ 可以 |

## 什么时候用 static？

不需要对象状态就能完成任务的方法 → static

```java
// ✅ static 合适：只需要参数，不依赖对象状态
public static int product(int a, int b) {
    return a * b;
}

// ✅ static 合适：工具方法
Math.max(3, 5);           // 不需要 new Math()
Integer.parseInt("123");  // 不需要 new Integer()
```

## 一个容易踩的坑

```java
public class Arithmetic {
    private int a;    // 实例变量
    private int b;    // 实例变量

    public static int product(int a, int b) {  // 参数 a, b
        return a * b;  // ← 乘的是参数，不是实例变量！
    }
}
```

**static 方法里没有 `this`**，所以 `a` 和 `b` 永远指向参数。那两个 `private int a; private int b` 是死代码——声明了但从未被使用。代码里看到没用到的字段就该删掉。

## 知识遗漏提醒

- [ ] 什么场景下必须用实例方法而不是 static？
- [ ] `static` 变量（类变量）和实例变量有什么区别？
- [ ] Java 为什么把所有方法都塞进类里，不像 C 允许独立函数？

## 相关概念

- [[java-classes-objects]] — 类与对象的基础
- [[inheritance-polymorphism]] — 继承时会遇到 static 方法的隐藏规则
