#!/usr/bin/env python3
"""Find candidate AI-slop and code-hygiene signals without declaring verdicts.

Usage: python3 scan_slop_signals.py TARGET [--json]
The scanner is intentionally conservative. Every result requires human/source/rendered confirmation.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

EXTENSIONS = {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte"}
SKIP = {"node_modules", ".git", "dist", "build", ".next", "coverage", "vendor"}
PATTERNS = {
    "gradient": re.compile(r"gradient|bg-gradient|bg-clip-text|text-transparent", re.I),
    "glass": re.compile(r"backdrop-blur|backdrop-filter|glassmorph|rgba\([^)]*,\s*0?\.?\d+\)", re.I),
    "generic_copy": re.compile(r"\b(elevate|seamless|powerful|get started|unlock|revolutionize)\b", re.I),
    "default_font": re.compile(r"\b(inter|roboto|arial|helvetica|system-ui)\b", re.I),
    "repeated_radius_shadow": re.compile(r"rounded-(?:xl|2xl|3xl)|border-radius\s*:\s*[^;]+|shadow-(?:md|lg|xl)", re.I),
    "motion_default": re.compile(r"fade[-_ ]?in[-_ ]?up|slide[-_ ]?up|animate-(?:fade|bounce|pulse)", re.I),
    "debug_or_todo": re.compile(r"console\.(?:log|debug|warn)\s*\(|\bTODO\b|\bFIXME\b", re.I),
}


def files_under(root: Path):
    if root.is_file():
        yield root
        return
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in EXTENSIONS and not any(part in SKIP for part in path.parts):
            yield path


def scan(root: Path):
    findings = []
    counts = Counter()
    for path in sorted(files_under(root)):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for name, pattern in PATTERNS.items():
                if pattern.search(line):
                    counts[name] += 1
                    findings.append({"signal": name, "file": str(path), "line": line_no, "text": line.strip()[:240]})
    return {"target": str(root), "note": "Candidate signals only; confirm against the brief, source references, and rendered behavior.", "counts": dict(counts), "findings": findings}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    result = scan(args.target)
    if args.as_json:
        print(json.dumps(result, indent=2))
        return
    print(f"Target: {result['target']}")
    print("Candidate signals (not verdicts):")
    for signal, count in sorted(result["counts"].items()):
        print(f"  {signal}: {count}")
    for item in result["findings"]:
        print(f"{item['file']}:{item['line']} [{item['signal']}] {item['text']}")


if __name__ == "__main__":
    main()
