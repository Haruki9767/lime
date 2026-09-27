#!/usr/bin/env python3
"""Run focused SEO smoke checks against a saved rendered HTML document."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path


class SEOParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.h1_count = 0
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key.lower(): value or "" for key, value in attrs}
        if tag.lower() == "title":
            self.in_title = True
        elif tag.lower() == "h1":
            self.h1_count += 1
        elif tag.lower() == "meta":
            self.meta.append(data)
        elif tag.lower() in {"a", "link"}:
            self.links.append(data)
        elif tag.lower() == "img":
            self.images.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def meta_value(parser: SEOParser, key: str, value: str) -> str:
    for item in parser.meta:
        if item.get(key) == value:
            return item.get("content", "").strip()
    return ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html", type=Path, help="saved rendered HTML file")
    args = ap.parse_args()
    if not args.html.is_file():
        print(f"ERROR: file not found: {args.html}", file=sys.stderr)
        return 2

    parser = SEOParser()
    parser.feed(args.html.read_text(encoding="utf-8", errors="replace"))
    title = "".join(parser.title_parts).strip()
    canonical = any(
        item.get("rel", "").lower() == "canonical" and item.get("href", "").strip()
        for item in parser.links
    )
    checks = [
        (bool(title), f"title present ({len(title)} characters)"),
        (bool(meta_value(parser, "name", "description")), "meta description present"),
        (canonical, "canonical link present"),
        (bool(meta_value(parser, "property", "og:title")), "og:title present"),
        (bool(meta_value(parser, "property", "og:description")), "og:description present"),
        (parser.h1_count == 1, f"exactly one h1 (found {parser.h1_count})"),
        (all("alt" in image for image in parser.images), f"all images have alt attributes (found {len(parser.images)})"),
    ]
    failures = 0
    for passed, message in checks:
        print(f"{'PASS' if passed else 'FAIL'}: {message}")
        failures += not passed
    return int(failures > 0)


if __name__ == "__main__":
    raise SystemExit(main())
