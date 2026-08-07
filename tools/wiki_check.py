#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""research-wiki 一致性校验脚本（2026-08-02 创建，灵感：Obsidian Vault Notes 的 tests/ 层）

检查内容：
1. wiki/ 下所有 md 文件里的 [[wikilink]] 是否都能解析到实际文件
2. index.md 的 Concepts/Connections/Questions 条目是否都有对应文件（防索引漂移）
3. 概念页状态统计（stub vs learned）

用法：python tools/wiki_check.py [--fix-absent]
  --fix-absent  为 index.md 中缺失的 stub 条目自动创建空 stub 文件
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

def all_md_files():
    return {p.relative_to(WIKI).as_posix().removesuffix(".md"): p
            for p in WIKI.rglob("*.md") if ".git" not in p.parts}

def extract_links(text):
    # [[target]] 或 [[target|alias]]
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)

def main():
    fix = "--fix-absent" in sys.argv
    files = all_md_files()
    # Obsidian 式解析：[[name]] 按文件名匹配任意目录
    by_name = {}
    for rel in files:
        by_name.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)
    problems = 0

    # 1. wikilink 解析检查
    for rel, path in sorted(files.items()):
        text = path.read_text(encoding="utf-8")
        for link in extract_links(text):
            if link not in files and link not in by_name:
                print(f"BROKEN LINK  {rel}: [[{link}]] 无对应文件")
                problems += 1

    # 2. index.md 条目 vs 实际文件
    index_path = WIKI / "index.md"
    if index_path.exists():
        idx = index_path.read_text(encoding="utf-8")
        sections = {"Concepts": "concepts", "Connections": "connections", "Open Questions": "questions"}
        for section, folder in sections.items():
            m = re.search(rf"## {section}\n(.*?)(?=\n## |\Z)", idx, re.S)
            if not m:
                continue
            listed = set(re.findall(r"\[\[([^\]|]+)\]\]", m.group(1)))
            for name in sorted(listed):
                target = f"{folder}/{name}"
                if target not in files:
                    print(f"INDEX STALE  {section}: [[{name}]] 列在 index 但文件不存在")
                    problems += 1
                    if fix:
                        stub = WIKI / (target + ".md")
                        stub.parent.mkdir(parents=True, exist_ok=True)
                        stub.write_text(
                            f"---\ntitle: \"{name}\"\ndate: 2026-08-02\ntags: []\nstatus: stub\n---\n\n# {name}\n\n（stub，待填充）\n",
                            encoding="utf-8")
                        print(f"  -> 已创建 {target}")

    # 3. 状态统计（status 字段可能是 L2-learned 这类复合值，按子串归类）
    stats = {"stub": 0, "learned": 0, "other": 0}
    for rel, path in sorted(files.items()):
        if rel.startswith("concepts/"):
            text = path.read_text(encoding="utf-8")
            m = re.search(r"^status:\s*(.+)", text, re.M)
            v = m.group(1).strip().lower() if m else ""
            key = "learned" if "learned" in v else ("stub" if "stub" in v else "other")
            stats[key] += 1
    print(f"概念页统计: {stats}")

    if problems:
        print(f"\n发现 {problems} 个问题" + ("，已自动修复缺失 stub" if fix else "（可加 --fix-absent 自动创建缺失 stub）"))
        sys.exit(1)
    print("\n✅ 全部一致")

if __name__ == "__main__":
    main()
