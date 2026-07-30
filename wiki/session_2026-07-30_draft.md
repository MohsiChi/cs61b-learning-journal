# Session Draft — 2026-07-30 (未完成)

> ⚠️ 临时缓存笔记。本次学习中断于 Lec 03 中途，下次会话从这里继续。
> 最终完整版将在学习完成后生成。

## 今天已覆盖的内容

### Lec 03: References, Recursion, and Lists — 第一部分

1. **Java 两种类型** ✅ 已理解
   - 基本类型 (8 种): 盒子存值本身。`int x = 5;` 拷贝值，互不影响。
   - 引用类型 (所有类/数组): 盒子存堆上对象的地址。`int[] arr2 = arr1;` 拷贝地址，指向同一个对象。
   - 类比: 引用类型 ≈ C 的安全指针 (无指针运算)

2. **`new` 的作用** ✅ 已理解
   - 在堆上分配内存，创建对象，返回地址
   - 变量 ≠ 对象，变量是门牌号，对象是房子

3. **`null`** ✅ 已理解
   - 地址为 0，不指向任何对象，≈ C 的 NULL

4. **值拷贝 vs 地址拷贝** ✅ 已理解
   - 基本类型 `b = a` → 独立两份
   - 引用类型 `b = a` → 共享同一对象

5. **IntList 链表节点类** 🔄 进行中
   - 自引用类型 (self-referential): `IntList rest` 字段的类型是 `IntList` 本身——但存的是地址（固定大小），不会无限嵌套
   - 动手编写了完整的 IntList 类：
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
   - CS61B 风格：底层数据结构类字段用 `public`，方便直接操作

## 中断位置

已讲完 IntList 节点类定义。**下一步待学**：
- 递归实现 `size()`, `get()` 方法
- 构建链表: `L.rest = new IntList(10, null);`
- 更复杂链表的构建方式
- SLList 封装 (将裸 IntList 包装为更安全的列表类)

## 核心理解

用户对引用类型的总结：
> "基本类型的变量每个之间都很独立，而引用类型则是都有一个地址指向 heap 里动态的'房间里的大象'，如果相互引用，就会有两个 arr 事实上在管理相同地址的同一个数组"
> "每个节点是一个'数据 + 下一个地址'的包裹"

## 本课学到的概念

| 概念 | 状态 | 说明 |
|------|------|------|
| Java 引用类型 vs 基本类型 | 🟢 已掌握 | 值拷贝 vs 地址拷贝 |
| `new` 与堆分配 | 🟢 已掌握 | 门牌号 vs 房子 |
| `null` | 🟢 已掌握 | 地址 0，≈ C NULL |
| 自引用类型 | 🟡 初步理解 | IntList rest 的类型就是 IntList |
| IntList 节点类 | 🟡 能写出 | 构造函数 + public 字段 |

## 待更新 (会话结束后)

会话正式结束后需要更新:
- `wiki/log.md`
- `wiki/progress.md`
- 新建概念页: `[[references-and-recursion]]` (自引用类型)

---

*📌 下次继续：Lec 03 — IntList 的递归方法 (size, get) 及链表构建*
