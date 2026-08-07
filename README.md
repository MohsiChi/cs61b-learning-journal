# CS61B Learning Journal

UC Berkeley CS61B: Data Structures and Algorithms (Spring 2024) — 个人学习笔记与反思。

> 仅包含个人obsidian用知识点笔记和反思，**不包含任何课程作业的解决方案代码**。
> 符合 CS61B 课程学术诚信政策。

## 课程信息

- **课程**: CS61B — Data Structures and Algorithms
- **学期**: Spring 2024
- **讲师**: Justin Yokota, Peyrin Kao
- **教材**: [CS61B GitBook](https://cs61b-2.gitbook.io/cs61b-textbook) (39 Chapters)
- **课程网站**: [sp24.datastructur.es](https://sp24.datastructur.es/)

## 仓库结构

```
wiki/
├── concepts/         # 知识点笔记（核心）
├── connections/      # 概念之间的关联
├── questions/        # 开放问题，驱动学习
├── course_schedule.md # 15 周课程路线图
├── progress.md       # 学习进度追踪
├── revision_notes.md  # 知识漏洞与复习清单
└── system.md         # 系统运转规则
tools/
└── wiki_check.py     # 一致性校验脚本（死链/索引漂移/状态统计，2026-08-02 新增）
```

## 学习日志

| 日期 | 内容 | 状态 |
|------|------|------|
| 2026-07-28 | Week 1: 环境搭建 + Lab 1 + HW 0B | ✅ 完成 |
| 2026-07-31 | Week 2: Lec 03 引用与递归完成 | ✅ 完成 |
| 2026-08-02 | 全库体检、16 概念 stub 补齐、SVG 教学法上线、写前检查规则、wiki_check 工具 | ✅ 完成 |

## 关于我

CST专业，Java/C 背景，通过 CS61B 系统学习数据结构与算法设计。

<svg viewBox="0 0 660 200" xmlns="http://www.w3.org/2000/svg">
    <text x="20" y="30" font-size="14" font-weight="bold" fill="#4a6fa5">第一次后（你的代码）:</text>
    <text x="20" y="60" font-size="13" fill="#333">L</text>
    <line x1="35" y1="56" x2="58" y2="56" stroke="#4a6fa5" stroke-width="2"/>
    <rect x="58" y="36" width="45" height="40" rx="6" fill="#fff8e1" stroke="#f9a825" stroke-width="2"/>
    <text x="80" y="60" text-anchor="middle" font-size="13" fill="#f9a825">0</text>
    <line x1="103" y1="56" x2="126" y2="56" stroke="#2e7d32" stroke-width="2"/>
    <rect x="126" y="36" width="45" height="40" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>
    <text x="148" y="60" text-anchor="middle" font-size="13" fill="#2e7d32">10</text>
    <line x1="171" y1="56" x2="194" y2="56" stroke="#999"/>
    <circle cx="200" cy="56" r="4" fill="none" stroke="#999"/>

    <text x="20" y="125" font-size="14" font-weight="bold" fill="#4a6fa5">第二次后（你的代码）:</text>
    <text x="20" y="155" font-size="13" fill="#333">L</text>
    <line x1="35" y1="151" x2="58" y2="151" stroke="#4a6fa5" stroke-width="2"/>
    <rect x="58" y="131" width="45" height="40" rx="6" fill="#fff8e1" stroke="#f9a825" stroke-width="2"/>
    <text x="80" y="155" text-anchor="middle" font-size="13" fill="#f9a825">0</text>
    <line x1="103" y1="151" x2="126" y2="151" stroke="#2e7d32" stroke-width="2"/>
    <rect x="126" y="131" width="45" height="40" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>
    <text x="148" y="155" text-anchor="middle" font-size="13" fill="#2e7d32">20</text>
    <line x1="171" y1="151" x2="194" y2="151" stroke="#999"/>
    <circle cx="200" cy="151" r="4" fill="none" stroke="#999"/>

    <rect x="320" y="131" width="45" height="40" rx="6" fill="#fdecea" stroke="#c0392b" stroke-width="2"/>
    <text x="342" y="155" text-anchor="middle" font-size="13" fill="#c0392b">10</text>
    <text x="342" y="120" text-anchor="middle" font-size="12" fill="#c0392b">孤儿：没人引用它了</text>
  </svg>
