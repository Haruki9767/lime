#!/usr/bin/env python3
"""Dependency-free triage scanner for web SEO and security signals.

This is not a penetration tester. It reports reviewable evidence and returns a
non-zero status only at the configured severity threshold (high by default).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SECRET_PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "generic-secret-assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|token)\s*[:=]\s*(['\"])(?P<value>[^'\"]{12,})\1"
    ),
}
DANGEROUS_PATTERNS = {
    "eval": re.compile(r"\beval\s*\("),
    "innerHTML": re.compile(r"\.innerHTML\s*="),
    "shell-exec": re.compile(
        r"\b(?:child_process\.(?:exec|execSync|spawn)|os\.system|subprocess\.(?:run|Popen))\b"
    ),
    "debugger": re.compile(r"\bdebugger\s*;"),
}
TEXT_SUFFIXES = {
    ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue",
    ".svelte", ".py", ".rb", ".php", ".java", ".go", ".rs", ".json", ".yml",
    ".yaml", ".env", ".toml", ".md", ".txt", ".xml",
}
CODE_SUFFIXES = {
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".vue", ".svelte", ".py",
    ".rb", ".php", ".java", ".go", ".rs",
}
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", "coverage", ".venv", "venv", "vendor"}
PLACEHOLDER_WORDS = {
    "changeme", "change-me", "example", "placeholder", "your_", "your-",
    "replace-me", "redacted", "dummy", "sample", "xxxx", "<your", "<replace",
}
SEVERITY_ORDER = {"info": 0, "low": 1, "medium": 2, "high": 3}


def files_under(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"Dockerfile", "Makefile"}:
            yield path


def finding(kind: str, severity: str, path: str, line: int, message: str, confidence: str = "review"):
    return {
        "kind": kind,
        "severity": severity,
        "confidence": confidence,
        "path": path,
        "line": line,
        "message": message,
    }


def is_placeholder(value: str) -> bool:
    lowered = value.lower().strip()
    return (
        any(word in lowered for word in PLACEHOLDER_WORDS)
        or lowered.startswith(("${", "env(", "process.env", "os.getenv"))
        or lowered in {"none", "null", "undefined"}
    )


def html_has(text: str, tag: str, **attrs: str) -> bool:
    for match in re.finditer(rf"<{tag}\b[^>]*>", text, re.I):
        fragment = match.group(0)
        if all(re.search(rf"\b{re.escape(key)}\s*=\s*['\"]{re.escape(value)}['\"]", fragment, re.I) for key, value in attrs.items()):
            return True
    return False


def threshold_failed(findings: list[dict], threshold: str) -> bool:
    minimum = SEVERITY_ORDER[threshold]
    return any(SEVERITY_ORDER.get(item["severity"], 0) >= minimum for item in findings)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--origin", default="", help="Preferred HTTPS origin, if known")
    parser.add_argument("--json-out", default="", help="Optional JSON output path")
    parser.add_argument(
        "--fail-on", choices=tuple(SEVERITY_ORDER), default="high",
        help="Minimum finding severity that makes the command fail (default: high)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    scanner_path = Path(__file__).resolve()
    findings: list[dict] = []
    html_files: list[tuple[str, str]] = []
    robots: list[tuple[str, str]] = []
    sitemaps: list[tuple[str, str]] = []
    scanned_files = 0

    for path in files_under(root):
        if path.resolve() == scanner_path:
            continue
        scanned_files += 1
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = str(path.relative_to(root))
        if path.suffix.lower() in {".html", ".htm"} and path.name.lower() != "404.html":
            html_files.append((rel, text))
        if path.name.lower() == "robots.txt":
            robots.append((rel, text))
        if path.name.lower() == "sitemap.xml":
            sitemaps.append((rel, text))

        for name, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                value = match.groupdict().get("value", "")
                if name == "generic-secret-assignment" and is_placeholder(value):
                    continue
                line = text.count("\n", 0, match.start()) + 1
                findings.append(finding("secret-signal", "high", rel, line, f"Possible {name}; review and remove from tracked source.", "high"))

        if path.suffix.lower() in CODE_SUFFIXES:
            for name, pattern in DANGEROUS_PATTERNS.items():
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(finding("code-signal", "medium", rel, line, f"Review {name} usage for injection or unsafe execution."))

    if html_files:
        for rel, text in html_files:
            if not re.search(r"<title\b[^>]*>\s*[^<]{2,}\s*</title>", text, re.I):
                findings.append(finding("seo", "medium", rel, 1, "Missing or empty HTML title."))
            if not re.search(r'<meta\b[^>]*\bname=["\']description["\'][^>]*\bcontent=["\'][^"\']{20,}["\']', text, re.I) and not re.search(r'<meta\b[^>]*\bcontent=["\'][^"\']{20,}["\'][^>]*\bname=["\']description["\']', text, re.I):
                findings.append(finding("seo", "medium", rel, 1, "Missing or short meta description."))
            if args.origin and not re.search(r'<link\b[^>]*\brel=["\']canonical["\'][^>]*\bhref=["\']https://', text, re.I) and not re.search(r'<link\b[^>]*\bhref=["\']https://[^"\']+["\'][^>]*\brel=["\']canonical["\']', text, re.I):
                findings.append(finding("seo", "medium", rel, 1, "No HTTPS canonical link detected in static HTML; verify client-side metadata if SPA."))
            if not (html_has(text, "meta", property="og:title") or html_has(text, "meta", name="twitter:card")):
                findings.append(finding("seo", "low", rel, 1, "Open Graph/Twitter metadata not detected."))

    if args.origin and not sitemaps:
        findings.append(finding("seo", "medium", "", 0, "No sitemap.xml found in the repository."))
    if args.origin and not robots:
        findings.append(finding("seo", "low", "", 0, "No robots.txt found in the repository."))

    summary = {
        "total": len(findings),
        **{severity: sum(item["severity"] == severity for item in findings) for severity in SEVERITY_ORDER},
        "fail_on": args.fail_on,
    }
    result = {
        "root": str(root),
        "origin": args.origin,
        "files_scanned": scanned_files,
        "findings": findings,
        "summary": summary,
        "notes": [
            "This scanner is triage only; review each signal in source context.",
            "Static 404 documents are excluded from indexable-page metadata checks.",
            "Generated, vendor, dependency, and scanner source directories are excluded.",
        ],
    }
    rendered = json.dumps(result, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 1 if threshold_failed(findings, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main())
