#!/usr/bin/env python3
"""Checks the Markdown files of this repository. Standard library only.

1. Every relative link points at a file or directory that exists.
2. No text looks like a credential or a local home path, so private details
   do not slip into the public org pages.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FORBIDDEN = [
    (re.compile(r"/home/[a-z_][a-z0-9_-]*"), "local home path"),
    (re.compile(r"\b(?:ghp|gho|ghs|github_pat|sk-ant|xox[abp])[-_][A-Za-z0-9_-]{10,}"), "token-like string"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
]


def main() -> int:
    errors = []
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for n, line in enumerate(text.splitlines(), 1):
            for m in LINK.finditer(line):
                target = m.group(1)
                if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                file_part = target.split("#", 1)[0]
                if file_part and not (path.parent / file_part).exists():
                    errors.append(f"{rel}:{n}: broken relative link {target}")
            for rx, what in FORBIDDEN:
                if rx.search(line):
                    errors.append(f"{rel}:{n}: {what}")
    for e in errors:
        print(e)
    print(f"checked {len(files)} files, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
