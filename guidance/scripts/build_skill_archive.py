#!/usr/bin/env python3
"""Build a deterministic ZIP containing complete skill packages."""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from check_skill_repo import discover_skill_packages


def build_archive(root: Path) -> Path:
    packages = discover_skill_packages(root)
    if not packages:
        raise ValueError(f"No skill packages with SKILL.md found under {root}")

    archive_path = root / "skillmd.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for package in packages:
            for path in sorted(package.rglob("*")):
                if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                    continue
                name = path.relative_to(root).as_posix()
                info = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    output = build_archive(args.root.resolve())
    print(f"Built complete skill archive: {output}")


if __name__ == "__main__":
    main()
