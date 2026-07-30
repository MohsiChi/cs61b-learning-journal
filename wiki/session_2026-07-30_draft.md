# Session Note — Lec 03 完成 (2026-07-30 ~ 2026-07-31)

> ✅ 已完成。Lec 03: References, Recursion, and Lists 全部学完。

## 覆盖内容

### Part 1: Java 引用类型 (7月30日)

1. **Java 两种类型**
   - 基本类型 (8 种): 盒子存值本身。拷贝值，互不影响。
   - 引用类型 (所有类/数组): 盒子存堆上对象的地址。拷贝地址，指向同一对象。

2. **`new` 的作用**
   - 在堆上分配内存，创建对象，返回地址
   - 变量 ≠ 对象，变量是门牌号，对象是房子

3. **`null`** — 地址为 0，不指向任何对象，≈ C 的 NULL

4. **值拷贝 vs 地址拷贝**
   - 基本类型: 独立两份
   - 引用类型: 共享同一对象

### Part 2: IntList 链表实现 (7月31日)

5. **IntList 节点类** — 自引用类型
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
   - `IntList rest` 的类型就是 `IntList` 本身——存的是地址（固定 64 位），不会无限嵌套

6. **递归 `size()`**
   ```java
   public int size() {
       if (rest == null) return 1;
       return 1 + rest.size();
   }
   ```
   - base case: 最后一个节点（rest == null）返回 1
   - 递归 case: 1 + 子链表的 size

7. **递归 `get(int i)`**
   ```java
   public int get(int i) {
       return i > 0 ? rest.get(i - 1) : first;
   }
   ```
   - i == 0 时返回当前节点的 first
   - i > 0 时递归到子链表的 get(i-1)

8. **构建链表** — 从尾部往头建
   ```java
   IntList L = new IntList(5, null);
   L.rest = new IntList(10, null);
   L.rest.rest = new IntList(15, null);
   ```
   - 头插法: `IntList L2 = new IntList(3, L);` → 一行在头部加节点

## 核心顿悟

> "rest 就是 IntList 截取第一个节点后的剩余，谜底就在谜面" — 链表天然适合递归

> "每个节点是一个 '数据 + 下一个地址' 的包裹" — 引用类型串联数据的核心机制

## 学到的概念

| 概念 | 掌握程度 | 说明 |
|------|---------|------|
| Java 引用类型 vs 基本类型 | 🟢 掌握 | 值拷贝 vs 地址拷贝，门牌号 vs 房子 |
| `new` 与堆分配 | 🟢 掌握 | 变量是门牌号，对象是房子 |
| `null` | 🟢 掌握 | 地址 0，≈ C NULL |
| 自引用类型 | 🟢 掌握 | IntList rest 的类型是 IntList 自身 |
| IntList 节点类 | 🟢 掌握 | public 字段 + 构造函数 |
| 递归 size() | 🟢 掌握 | 1 + rest.size()，base case: rest==null→1 |
| 递归 get(i) | 🟢 掌握 | i>0 ? rest.get(i-1) : first |
| 构建链表 | 🟢 掌握 | 头插法一行加节点 |

## 下次继续

**Lec 04: SLList** — 将裸 IntList 封装为更安全的列表类
- public/private 分离
- 嵌套类 (nested class)
- addFirst, addLast, getFirst
