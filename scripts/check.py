#!/usr/bin/env python3
"""Check the portable document package without third-party dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/design"
REQUIRED = ["README.md", "SITEMAP.md", "LICENSE", "skills/design/SKILL.md", "skills/design/LICENSE"] + [
    f"skills/design/references/{name}.md" for name in
    ("principles", "web-ui", "html-documents", "document-story", "diagrams", "verification", "sources")
]
errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")
entry = SKILL / "SKILL.md"
if entry.exists():
    content = entry.read_text(encoding="utf-8")
    header = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not header or not re.search(r"^name: design$", header[1], re.M) or not re.search(r"^description: .+", header[1], re.M):
        errors.append("SKILL.md needs name: design and a nonempty description in frontmatter")
# Deliberately narrow heuristics: this is not a secret scanner.
private = re.compile(r"/home/[^\s/]+|/Users/[^\s/]+|(?:~|\$HOME)/|(?:[a-z0-9-]+\.)*honya\.dev|\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b", re.I)
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    content = path.read_text(encoding="utf-8")
    label = str(path.relative_to(ROOT))
    if private.search(content):
        errors.append(f"Possible private environment reference: {label}")
    for match in re.finditer(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", content):
        target = match[1].strip("<>")
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        resolved = (path.parent / unquote(parts.path)).resolve()
        boundary = SKILL if path.is_relative_to(SKILL) else ROOT
        if not resolved.is_relative_to(boundary):
            errors.append(f"Link escapes package: {label}: {target}")
        elif not resolved.exists():
            errors.append(f"Broken relative link: {label}: {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Package check passed: required files, frontmatter, relative links, and environment-reference heuristics.")
