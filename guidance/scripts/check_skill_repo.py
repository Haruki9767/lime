#!/usr/bin/env python3
"""Validate skill packages, the portable archive, and repository safety checks."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = ("ai-" + "slop-pattern-looker", "web-" + "quality-security-prd")
SECRET = re.compile(r"(?i)(api[_ -]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]")
EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".nuxt", ".output", "dist", "build"}


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


def discover_skill_packages(root: Path) -> list[Path]:
    return sorted(
        package
        for package in root.iterdir()
        if package.is_dir()
        and not package.name.startswith(".")
        and package.name != "lime"
        and (package / "SKILL.md").is_file()
    )


def validate_skill_packages(root: Path) -> list[Path]:
    skills = discover_skill_packages(root)
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
    return skills


def _package_files(packages: list[Path]) -> dict[str, bytes]:
    expected: dict[str, bytes] = {}
    for package in packages:
        for path in sorted(package.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            expected[path.relative_to(package.parent).as_posix()] = path.read_bytes()
    return expected


def validate_skill_archive(root: Path, packages: list[Path]) -> None:
    archive_path = root / "skillmd.zip"
    if not archive_path.is_file():
        fail(f"{archive_path}: portable skill archive is missing")
    expected = _package_files(packages)
    try:
        with ZipFile(archive_path) as archive:
            file_names = [info.filename for info in archive.infolist() if not info.is_dir()]
            if len(file_names) != len(set(file_names)):
                fail(f"{archive_path}: duplicate file paths in archive")
            archived_names = set(file_names)
            if archived_names != set(expected):
                missing = sorted(set(expected) - archived_names)
                extra = sorted(archived_names - set(expected))
                fail(f"{archive_path}: package contents differ (missing={missing}, extra={extra})")
            for name, content in expected.items():
                if archive.read(name) != content:
                    fail(f"{archive_path}: stale or modified package file {name}")
    except BadZipFile as error:
        fail(f"{archive_path}: invalid ZIP archive ({error})")


def validate_repository(root: Path = ROOT) -> int:
    skills = validate_skill_packages(root)
    validate_skill_archive(root, skills)

    tracked = subprocess.run(
        ["git", "grep", "-n", "-I", "-e", FORBIDDEN[0], "-e", FORBIDDEN[1]],
        cwd=root,
        text=True,
        capture_output=True,
    )
    if tracked.returncode == 0:
        fail("stale skill names found in tracked files:\n" + tracked.stdout)
    if tracked.returncode > 1:
        fail("git grep failed while checking stale skill names")

    for path in root.rglob("*.py"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    for path in root.rglob("*"):
        if (
            not path.is_file()
            or any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts)
            or path.suffix.lower() in {".jpg", ".mp4", ".png", ".gif"}
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        match = SECRET.search(text)
        if match:
            fail(f"possible secret assignment in {path}:{text[:match.start()].count(chr(10)) + 1}")

    return len(skills)


def main() -> None:
    count = validate_repository()
    print(f"Validated {count} skill packages, their complete portable archive, and all Python scripts")


if __name__ == "__main__":
    main()
