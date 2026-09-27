from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "guidance" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_skill_archive import build_archive  # noqa: E402
from check_skill_repo import (  # noqa: E402
    discover_skill_packages,
    validate_skill_archive,
    validate_skill_packages,
)


class SkillRepositoryTests(unittest.TestCase):
    def make_package(self, root: Path, name: str = "sample-skill") -> Path:
        package = root / name
        (package / "references").mkdir(parents=True)
        (package / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: A sample skill.\n---\n\n# Sample\n",
            encoding="utf-8",
        )
        (package / "references" / "guide.md").write_text("Supporting guidance.\n", encoding="utf-8")
        return package

    def test_package_discovery_ignores_site_and_validates_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_package(root)
            (root / "lime").mkdir()
            (root / "lime" / "SKILL.md").write_text("not a skill package\n", encoding="utf-8")

            packages = validate_skill_packages(root)

            self.assertEqual(["sample-skill"], [package.name for package in packages])
            self.assertEqual(packages, discover_skill_packages(root))

    def test_archive_contains_complete_packages_and_is_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.make_package(root)

            archive_path = build_archive(root)
            packages = discover_skill_packages(root)
            validate_skill_archive(root, packages)
            first_bytes = archive_path.read_bytes()
            build_archive(root)

            self.assertEqual(first_bytes, archive_path.read_bytes())
            with ZipFile(archive_path) as archive:
                self.assertEqual(
                    {"sample-skill/SKILL.md", "sample-skill/references/guide.md"},
                    set(archive.namelist()),
                )
                self.assertEqual(
                    (package / "references" / "guide.md").read_bytes(),
                    archive.read("sample-skill/references/guide.md"),
                )

    def test_archive_validator_rejects_stale_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.make_package(root)
            build_archive(root)
            (package / "references" / "guide.md").write_text("Updated guidance.\n", encoding="utf-8")

            with self.assertRaises(SystemExit):
                validate_skill_archive(root, discover_skill_packages(root))

    def test_archive_validator_rejects_missing_supporting_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_package(root)
            build_archive(root)
            with ZipFile(root / "skillmd.zip", "w") as archive:
                archive.writestr("sample-skill/SKILL.md", "entrypoint only")

            with self.assertRaises(SystemExit):
                validate_skill_archive(root, discover_skill_packages(root))

    def test_package_validation_rejects_directory_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = self.make_package(root)
            (package / "SKILL.md").write_text(
                "---\nname: other-name\ndescription: A sample skill.\n---\n",
                encoding="utf-8",
            )

            with self.assertRaises(SystemExit):
                validate_skill_packages(root)


if __name__ == "__main__":
    unittest.main()
