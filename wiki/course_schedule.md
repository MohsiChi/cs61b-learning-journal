---
title: "CS61B Spring 2024 课程路线图"
date: 2026-07-06
tags: [CS61B, course-schedule, learning-pathway, DSA]
---

# CS61B Spring 2024 课程路线图

> 基于 Spring 2024 课程官网 (sp24.datastructur.es) + GitBook Textbook (cs61b-2.gitbook.io)。
> 讲师: Justin Yokota, Peyrin Kao | 教材: CS61B GitBook (39 Chapters)

## 五大模块概览

```
Module 1: Java + Lists (Week 1-3)         →  Proj0: 2048
Module 2: Inheritance + Asymptotics (Week 3-6) →  Proj1: Deque61B
Module 3: Trees + Hashing (Week 6-8)      →  Proj2A: NGrams
Module 4: Graphs (Week 8-10)             →  Proj2B/C: Wordnet
Module 5: Sorting + Advanced (Week 12-15) →  Proj3: BYOW
```

---

## Week 1: Java Basics + Classes

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 01** | Intro, Course Overview | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRq5wRDN8wZFy7GrrJXUtr1q) / [Slides](https://docs.google.com/presentation/d/19NEzpJJ-a0lI-tdz9yC1kP-8Apt2oZm-918IsDiqgYQ) |
| **Lec 02** | Defining and Using Classes | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqziLs3JZ6LIH73ZsVtvsGy) / [Slides](https://docs.google.com/presentation/d/1zt0yh_gzmfjCdB1y7DzTdwNSfTtepnQAtORH7PqebQM) |
| **Lab 1** | Setup (IntelliJ, Java, Git) | [Lab Spec](https://sp24.datastructur.es/labs/lab01) |
| **HW 0A** | Java Syntax | [HW Spec](https://sp24.datastructur.es/homeworks/hw0/hw0a) |
| **HW 0B** | Data Structures Basics | [HW Spec](https://sp24.datastructur.es/homeworks/hw0/hw0b) |
| **Textbook** | Ch 1-2 | [Ch 1](https://cs61b-2.gitbook.io/cs61b-textbook/1.-introduction) / [Ch 2](https://cs61b-2.gitbook.io/cs61b-textbook/2.-defining-and-using-classes) |

**Your advantage**: Java 是你的主力语言。这周重点在配置环境和熟悉 CS61B 的代码风格规范。

---

## Week 2: Lists — References, Recursion, SLLists, DLLists, Arrays

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 03** | Lists I: References, Recursion, and Lists | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRpb4EQp0tOFJNZUXHnxTfXm) / [Slides](https://docs.google.com/presentation/d/1G5k4HcjJ7C2fT_9xQdvpfWjKC4xQa--5FnwXPGf0nwg) |
| **Lec 04** | Lists II: SLLists | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqyuN_xxm4o1Woa44dXW_N8) / [Slides](https://docs.google.com/presentation/d/1Uty7XFuhRuCg3SoaSaViXzJhPTZDoYUV878L2I_pe_k) |
| **Lec 05** | Lists III: DLLists and Arrays | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRpPjLuN6-QJUFeK_mBZPve4) / [Slides](https://docs.google.com/presentation/d/1jjivjdvD4mx6qb4bd4rUKB6FDZbYtveJ5NKeyVeA1lk) |
| **Discussion 01** | Introduction to Java | [Regular](https://sp24.datastructur.es/assets/discussions/regular01.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular01sol.pdf) |
| **Lab 2** | Debugging I | [Lab Spec](https://sp24.datastructur.es/labs/lab02) |
| **Textbook** | Ch 3-6 | SLLists, DLLists, Arrays |

**⚠️ 重点难点**: Java 引用语义 (reference semantics) — 与 C 指针和 Python 对象引用的精细对比。SLLists/DLLists 的封装设计（public/private/nested class）。

---

## Week 3: Testing + Inheritance I

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 06** | Testing | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqRR4OQx_I3YPkA87bO0whh) / [Slides](https://docs.google.com/presentation/d/1AxuxcFWc_9U-gmdBRPGcEqE-7Q0-48hEw5Iupbama74) |
| **Lec 07** | Lists IV: Arrays and Lists | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrv834ePjKGB7i1az039-Gw) / [Slides](https://docs.google.com/presentation/d/1RJuwap1NZDYFUS7eiPy_SZu7oWHJladwuhKQpQcTjt8) |
| **Lec 08** | Inheritance I: Interface and Implementation Inheritance | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqJVbwFNWwRrGyBwedwLnuW) / [Slides](https://docs.google.com/presentation/d/1LxnOVy_k13llkePdQIdBrZ5jEpgRmbrvMilD-ppRjlc) |
| **Discussion 02** | Scope, Static, Linked Lists, Arrays | [Regular](https://sp24.datastructur.es/assets/discussions/regular02.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular02sol.pdf) |
| **Lab 3** | Debugging II | [Lab Spec](https://sp24.datastructur.es/labs/lab03) |
| **HW 1** | Linked List Deque | Gradescope |
| **Textbook** | Ch 7-9 | Testing, ArrayList, Inheritance I |

**⚠️ 重点难点**: 测试驱动开发 (TDD) 理念——"TDD is dead" 辩论。Interface vs Implementation Inheritance 的设计选择。

---

## Week 4: Inheritance II-III-IV

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 09** | Inheritance II: Extends, Casting, Higher Order Functions | [Slides](https://docs.google.com/presentation/d/1jVqC44HVViVtajnF18KsZ6MdIfseTfOSerfvxH4pzP0) |
| **Lec 10** | Inheritance III: Subtype Polymorphism, Comparators, Comparable | [Slides](https://docs.google.com/presentation/d/1WpISEkGajVCwARZy6w-XDF5sofm1cITUhfAlPUnnnos) |
| **Lec 11** | Inheritance IV: Iterators, Object Methods | [Slides](https://docs.google.com/presentation/d/1bahvjVtbMcc2kuyzYQfQtD8EJyIiIkWnSALVSMuyQhI) |
| **Discussion 03** | Inheritance | [Regular](https://sp24.datastructur.es/assets/discussions/regular03.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular03sol.pdf) |
| **Textbook** | Ch 10-12 | Extends, Subtype Polymorphism, Exceptions, Iterators, Object Methods |

**⚠️ 重点难点**: `Comparable` vs `Comparator`——策略模式的经典案例。`Iterator` 和 `Iterable` 的区别，fail-fast 行为。

---

## Week 5: Asymptotics I + Disjoint Sets + Midterm 1

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 12** | Asymptotics I | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrajvLNrqCND6CQUbqaR0mU) / [Slides](https://docs.google.com/presentation/d/1CH4rsIIvu5pbmoWUNl9QdkPQYYkJc-ptX85CBhytlzM) |
| **Lec 13** | Ask Anything: Midterm 1 Review | [Recording](https://www.youtube.com/watch?v=2Q1g4A-P2V8) |
| **Lec 14** | Disjoint Sets | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRpMlYLU0hWYDMHNtcGi-Qmm) / [Slides](https://docs.google.com/presentation/d/18pzklQAvV94ODFpjeB60Rzj79wFHdkIB-ePWR_MeClk) |
| **Discussion 04** | Comparators, Iterators | [Regular](https://sp24.datastructur.es/assets/discussions/regular04.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular04sol.pdf) |
| **Lab 4** | Git | [Lab Spec](https://sp24.datastructur.es/labs/lab04) |
| **Midterm 1** | Covers Week 1-5 | |
| **Textbook** | Ch 13-14 | Asymptotics I, Disjoint Sets |

**⚠️ 重点难点**: 渐进分析的严格数学定义——Big O, Big Theta, Big Omega。并查集的 Weighted Quick Union + Path Compression 双重优化。

---

## Week 6: Asymptotics II + ADTs + BSTs

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 15** | Asymptotics II | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqwuAZ5q3P5xUxe2xNZL3an) / [Slides](https://docs.google.com/presentation/d/1zlmNjzu42WAEmyJFG2tYRZJIguExSFq5B__equ3-GaM) |
| **Lec 16** | ADTs, Sets, Maps, BSTs | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrks2Xi7wU8s82FcwPaINYs) / [Slides](https://docs.google.com/presentation/d/1tAXgjwVKsnH7AR-iCvkDM-rQFwrg4OnKVZzqPixZWI8) |
| **Discussion 05** | Asymptotics, Disjoint Sets | [Regular](https://sp24.datastructur.es/assets/discussions/regular05.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular05sol.pdf) |
| **Lab 5** | Disjoint Sets | [Lab Spec](https://sp24.datastructur.es/labs/lab05) |
| **HW 2** | Percolation | [HW Spec](https://sp24.datastructur.es/homeworks/hw2) |
| **Textbook** | Ch 15-16 | Asymptotics II, ADTs and BSTs |

**⚠️ 重点难点**: BST 的删除操作（Hibbard deletion）。ADT 与具体数据结构的区别——接口 vs 实现。

---

## Week 7: B-Trees + Red Black Trees + Hashing

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 17** | B-Trees (2-3, 2-3-4 Trees) | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRoMUlGWsTyt-WHK-SuyXK_E) / [Slides](https://docs.google.com/presentation/d/1uQYk0Hxhf0jhnp-aXxoIGNGM2w_yILMyukRctRPc9Uo) |
| **Lec 18** | Red Black Trees | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrYOYhFXExoXfP8uhHHCIri) / [Slides](https://docs.google.com/presentation/d/1WJze5Odoy4ZR1vqPM8X6duaZ5GGm_D7SaYrtOa5RnsA) |
| **Lec 19** | Hashing | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRr_rFqN57yjZtcw_P4UiJ7a) / [Slides](https://docs.google.com/presentation/d/12Su6RdBjVCGd5MrKE6Y5s-J4OyBgv--v-4LHjEwtJbU) |
| **Discussion 06** | ADTs, Asymptotics II, BSTs | [Regular](https://sp24.datastructur.es/assets/discussions/regular06.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular06sol.pdf) |
| **Lab 6** | BSTMap | [Lab Spec](https://sp24.datastructur.es/labs/lab06) |
| **Textbook** | Ch 17-19 | B-Trees, Red Black Trees, Hashing |

**⚠️ 重点难点**: RBT 的三个不变量（root is black, no adjacent reds, equal black depth）。为什么用 LLRB (Left-Leaning Red Black Tree) 简化实现。哈希的 `hashCode()` 与 `equals()` 契约。

---

## Week 8: Hashing II + Heaps + Graph Traversals

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 20** | Hashing II | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrSxUje7m5-Y41ELVPm50N_) / [Slides](https://docs.google.com/presentation/d/1EGP_BWIbha4xQ4A5PJLAVIQaK6G0RbWZfrVDd0GmS08) |
| **Lec 21** | Heaps and Priority Queues | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrFJrMMOkrShULQ3KeoqZB9) / [Slides](https://docs.google.com/presentation/d/1XVJfoSYH2ItiD1rz9yvyEf_HelejbfkYxQgukbgclSY) |
| **Lec 22** | Tree and Graph Traversals | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRoXCSo4Hx8TEZBsIpag6lMs) / [Slides](https://docs.google.com/presentation/d/1Gyke5ZMrgcMuBTa7qHAoklWZB3yf_yqQAymK2nV-Nqs) |
| **Discussion 07** | B-Trees, LLRBs, Hashing | [Regular](https://sp24.datastructur.es/assets/discussions/regular07.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular07sol.pdf) |
| **Lab 7** | LLRBs | [Lab Spec](https://sp24.datastructur.es/labs/lab07) |
| **Lab 8** | HashMaps | [Lab Spec](https://sp24.datastructur.es/labs/lab08) |
| **Textbook** | Ch 20-22 | Hashing II, Heaps, Tree Traversals and Graphs |

**⚠️ 重点难点**: 堆的数组实现（bubble up / bubble down）。BFS vs DFS vs Dijkstra 的适用场景对比。

---

## Week 9: Graphs — Traversals, Shortest Paths, MSTs

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 23** | Graph Traversals and Implementations | [Video](https://www.youtube.com/watch?v=YgPtwbWpLaM&list=PLnp31xXvnfRqyRDKtQeHvjxhonhNuaOAK) / [Slides](https://docs.google.com/presentation/d/1NKWnXSJ8pUn1E2Cw6zidxMRuXf_aINKCpW7XpEkyz6c) |
| **Lec 24** | Shortest Paths | [Video](https://www.youtube.com/watch?v=iMoFtG1md3w&list=PLnp31xXvnfRrbIn8mZ3pmpgygnfwp2zjW) / [Slides](https://docs.google.com/presentation/d/1mT-F0fxm-sVZj9EQS_E_QMv5SVfeCGptI9vsKpyp57Y) |
| **Lec 25** | Minimum Spanning Trees | [Video](https://www.youtube.com/watch?v=vnKK38JS9Ik&list=PLnp31xXvnfRr6RTCpKB1Xj3n9bZffJQ7L) / [Slides](https://docs.google.com/presentation/d/13pPWHDLRUX2TAUUUK5ucEQ6dF3vUjzkj_C_iXDGaTPU) |
| **Discussion 08** | Graphs, Heaps | [Regular](https://sp24.datastructur.es/assets/discussions/regular08.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular08sol.pdf) |
| **HW 3** | Graph Algorithms | Gradescope |
| **Textbook** | Ch 23-25 | Graph Traversals, Shortest Paths, MSTs |

**⚠️ 重点难点**: Dijkstra 的贪心原理——为什么不能处理负权边？A* vs Dijkstra。Prim vs Kruskal 的适用场景（稠密图 vs 稀疏图）。

---

## Week 10: DAGs + Tries + Software Engineering I

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 26** | Directed Acyclic Graphs | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRprqOwH0sojH3VLONWXtYM0) / [Slides](https://docs.google.com/presentation/d/1UHVEYtQhV7EQ74ETn5MvCsnRzsCzmp3MvXL84hXbw-g) |
| **Lec 27** | Software Engineering I | [Video](https://www.youtube.com/watch?v=JfATr-BBPY0) / [Slides](https://docs.google.com/presentation/d/15afX6n25MybwUmm58M2xn8KqjQbMYHTQcTJ7u3h_I2M) |
| **Lec 28** | Prefix Operations and Tries | [Video](https://www.youtube.com/watch?v=F8Q-SHW2hAM&list=PLnp31xXvnfRoMxe8IbO1qF3lXwudLHVDk) / [Slides](https://docs.google.com/presentation/d/1tcKJNY-ultPxwaHtYn-kd-DV7aXcuBQm6resYvpoCkw) |
| **Discussion 09** | Shortest Paths, MSTs | [Regular](https://sp24.datastructur.es/assets/discussions/regular09.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular09sol.pdf) |
| **Midterm 2** | Covers Week 6-10 | |
| **Textbook** | Ch 26-28 | Tries, Software Engineering I, Reductions and Decomposition |

**⚠️ 重点难点**: 拓扑排序 (Topological Sort)——DAG 的"线性化"。Trie 的空间换时间思想。Reduction 的核心思想——把新问题规约到已知问题。

---

## Week 11: Spring Break

春假，无课程。

---

## Week 12: Sorting I-III — Selection, Heapsort, Mergesort, Insertion, Quicksort

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 29** | Sorting I: Selection Sort, Heapsort | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrK9o_QZyGOCbQVFTsqOPtN) / [Slides](https://docs.google.com/presentation/d/1aleYBt-L8bwyaxw9tXPN3bMI5XxWxmpgfvvSEo9KxD0) |
| **Lec 30** | Sorting II: Mergesort and Insertion Sort | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqsfDWZNS86oYmHFY6UKA2t) / [Slides](https://docs.google.com/presentation/d/1MqmOxfh1c6gS4hk9hvuRR_hWXWTnCIXMqLGXwRX4Pvk) |
| **Lec 31** | Software Engineering II | [Recording](https://www.youtube.com/watch?v=8ZZmTVXDVZc) / [Slides](https://docs.google.com/presentation/d/1P1Uc8phy1GW1M4A8PA7mJJMWqb2QgOfewwwB1wMnFlU) |
| **Lec 32** | Sorting III: Quicksort | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRrHHQP93qqc_QBNBF_WEQLy) / [Slides](https://docs.google.com/presentation/d/11vRyW0ZPrsxUhRHCBgkygy01PlL1amB66n9FZQN03wo) |
| **Discussion 10** | Graphs II, Tries | [Regular](https://sp24.datastructur.es/assets/discussions/regular10.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular10sol.pdf) |
| **Lab 9** | Getting Started on Project 3 (Conway's Game of Life) | [Lab Spec](https://sp24.datastructur.es/labs/lab09) |
| **Textbook** | Ch 29-32 | Basic Sorts, Quicksort, Software Engineering II, More Quick Sort |

**⚠️ 重点难点**: 排序稳定性 (stable vs unstable)。Quicksort 的 pivot 选择策略与 Worst-case 退化。Mergesort 的空间复杂度分析。

---

## Week 13: Sorting IV + Software Engineering III + More Quicksort

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 33** | Sorting IV: Sorting and Algorithmic Bounds | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRqEadgCMXeo1gnlIxnETooG) / [Slides](https://docs.google.com/presentation/d/1sqpg9sM-0719KGcWzYmmrWlj0azaafgIAiM8U98jKi4) |
| **Lec 34** | Software Engineering III | [Recording](https://www.youtube.com/watch?v=8XY1TNODHw4) / [Slides](https://docs.google.com/presentation/d/1nE_oD8Mx6tRcO6zOnz7KbSxCtaZpaoDlcPhKzfNXrqI) |
| **Discussion 11** | Sorting | [Regular](https://sp24.datastructur.es/assets/discussions/regular11.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular11sol.pdf) |
| **Lab 10** | Tetris | [Lab Spec](https://sp24.datastructur.es/labs/lab10) |
| **Textbook** | Ch 33-34 | Software Engineering III, Sorting and Algorithmic Bounds |

**⚠️ 重点难点**: 基于比较的排序下界证明 (Ω(N log N))——决策树模型。

---

## Week 14-15: Radix Sorts + Compression + P=NP + Wrap-up

| 资源 | 内容 | 链接 |
|------|------|------|
| **Lec 35** | Sorting V: More Quicksort, Radix Sorts | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRr4cg5TeJZplLTlOVmMNE0d) / [Slides](https://docs.google.com/presentation/d/14jNEZC-YKUuxIr3Cxsvz1Kb6eX0jCjvjevb1zD8NRj4) |
| **Lec 36** | Sorting VI: Radix vs. Comparison Sorting | [Video](https://www.youtube.com/playlist?list=PLnp31xXvnfRoDV1sFRy3Hdx0N6BMZjI1n) / [Slides](https://docs.google.com/presentation/d/1wSTXwNB-D75VbHCtKqnr7QlOQtV-3wg6vTLNpNw7Qwk) |
| **Lec 37** | Software Engineering IV | [Recording](https://youtu.be/ePwXhqEP5j0) / [Slides](https://docs.google.com/presentation/d/13TE3w603C6zt1q5vWRL9WmbwxkG0VjFluIIHSbV0qNU) |
| **Lec 38** | Compression | [Video](https://www.youtube.com/playlist?list=PL8FaHk7qbOD6kGO6F1uWKggr-Ie9TCMUZ) / [Slides](https://docs.google.com/presentation/d/1k4tgpf7xaW-uhlHYlp3izZRYtBGMYPVRlHCmmpN6QXQ) |
| **Lec 39** | Complexity and P=NP? | [Video](https://www.youtube.com/playlist?list=PL8FaHk7qbOD5nfUOOXco_8Sx5Nkt-Wgq8) / [Slides](https://docs.google.com/presentation/d/1QFwbmMVE0Wlvg-gnWnemTxRX_t7h6IlhCQU69dcAkaA) |
| **Lec 40** | Summary, Fun | [Recording](https://www.youtube.com/watch?v=utxAtIWl8Xw) / [Slides](https://docs.google.com/presentation/d/1MmnYUoi-4Wyt6_3BcBdt_WkrL1XECZ9ypCyUmhW7e2U) |
| **Discussion 12** | More Sorting | [Regular](https://sp24.datastructur.es/assets/discussions/regular12.pdf) / [Solutions](https://sp24.datastructur.es/assets/discussions/regular12sol.pdf) |
| **HW 4** | Compression / Complexity | Gradescope |
| **Textbook** | Ch 35-39 | Radix Sorts, Sorting Conclusion, SE IV, Compression, P=NP |

**⚠️ 重点难点**: Radix Sort 的复杂度 = O(N * W)，突破比较排序下界！Huffman Coding——最优前缀编码。P vs NP——千禧年悬赏问题。

---

## Final Exam: May 7th (8-11AM)

Comprehensive, covers all 15 weeks.

---

## Projects 全景

| Project | Due | 内容 | 核心技能 |
|---------|-----|------|---------|
| **Proj0: 2048** | Week 2 | 实现 2048 游戏逻辑 | Java 基础、类设计、测试 |
| **Proj1A: LinkedListDeque61B** | Week 4 | 双向链表双端队列 | 引用操作、泛型、封装 |
| **Proj1B: ArrayDeque61B** | Week 4 | 循环数组双端队列 | 数组操作、取模、resizing |
| **Proj1C: Deque61B Enhancements** | Week 5 | MaxArrayDeque + 迭代器 | Iterator 实现、Comparator |
| **Proj2A: Ngordnet (NGrams)** | Week 7 | N-gram 文字分析 | 文件IO、数据结构选择 |
| **Proj2B/C: Ngordnet (Wordnet)** | Week 9-10 | 图遍历 + Wordnet | BFS/DFS, 图算法, Hyponyms |
| **Proj3: BYOW (Build Your Own World)** | Week 13-15 | 随机世界生成引擎 | 大规模工程、哈希种子、交互设计 |

---

## 历年考试资源

考试按学期分类在 sp24.datastructur.es/resources/exams/ :
- Spring 2024: Midterm 1 + Midterm 2 + Final
- 往期考试可用作额外练习

---

## AI 使用此文件的方式

1. 每次学习会话开始，读取此文件确定用户当前进度
2. 根据当前 Week 推荐对应资源（Lecture → Reading → Lab → HW）
3. 每完成一个模块，更新 `wiki/progress.md`
4. 学习路径：**看 Lecture 录像/幻灯片 → 读 Textbook 对应章节 → 做 Lab 巩固 → 做 HW/Project 检验 → 做 Discussion 加深**
