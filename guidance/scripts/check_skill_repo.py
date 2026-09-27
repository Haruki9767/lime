#!/usr/bin/env python3
"""Validate this skills repository without relying on Manus-only paths."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = ("ai-" + "slop-pattern-looker", "web-" + "quality-security-prd")
SECRET = re.compile(r"(?i)(api[_ -]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]")


def fail(message: str) -> None:
    print(f"::error::{message}")
    raise SystemExit(1)


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        fail(f"{path}: unterminated YAML frontmatter")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def main() -> None:
    packages = sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("."))
    skills = [p for p in packages if (p / "SKILL.md").is_file()]
    if not skills:
        fail("No skill packages with SKILL.md were found")

    for package in skills:
        path = package / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text, path)
        if meta.get("name") != package.name:
            fail(f"{path}: frontmatter name {meta.get('name')!r} does not match directory {package.name!r}")
        if not meta.get("description"):
            fail(f"{path}: description is required")
        if len(text.splitlines()) > 500:
            fail(f"{path}: SKILL.md must stay under 500 lines")

    tracked = subprocess.run(
        ["git", "grep", "-n", "-I", "-e", FORBIDDEN[0], "-e", FORBIDDEN[1]],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if tracked.returncode == 0:
        fail("stale skill names found in tracked files:\n" + tracked.stdout)
    if tracked.returncode > 1:
        fail("git grep failed while checking stale skill names")

    for path in ROOT.rglob("*.py"):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix in {".jpg", ".mp4", ".png", ".gif"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        match = SECRET.search(text)
        if match:
            fail(f"possible secret assignment in {path}:{text[:match.start()].count(chr(10)) + 1}")

    print(f"Validated {len(skills)} skill packages and all Python scripts")


if __name__ == "__main__":
    main()
