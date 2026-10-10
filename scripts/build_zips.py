"""Package every skill folder in skills/ into an upload-ready ZIP in dist/.

Each ZIP has the skill folder as its single top-level entry, which is the
layout Claude's "Upload a skill" expects:

    handwritten-notes.zip
    └── handwritten-notes/
        ├── SKILL.md
        └── ...

The script also checks each skill before packaging and fails the build on
any problem, so a broken skill never reaches a release.

Usage:
    python scripts/build_zips.py
"""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED = ("anthropic", "claude")
DESCRIPTION_LIMIT = 200  # claude.ai upload limit
SKIP_NAMES = {".DS_Store", "Thumbs.db", "__pycache__"}


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_skill(folder: Path) -> list:
    problems = []
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return [f"{folder.name}: missing SKILL.md"]

    meta = read_frontmatter(skill_md)
    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        problems.append(f"{folder.name}: SKILL.md has no name in its frontmatter")
    elif name != folder.name:
        problems.append(f"{folder.name}: frontmatter name '{name}' must match the folder name")
    if name and not NAME_RE.match(name):
        problems.append(f"{folder.name}: name must be lowercase letters, numbers, and hyphens, 64 max")
    if any(word in name for word in RESERVED):
        problems.append(f"{folder.name}: name cannot contain 'anthropic' or 'claude'")
    if not description:
        problems.append(f"{folder.name}: SKILL.md has no description")
    elif len(description) > DESCRIPTION_LIMIT:
        problems.append(
            f"{folder.name}: description is {len(description)} characters, limit is {DESCRIPTION_LIMIT}"
        )
    return problems


def build(folder: Path) -> Path:
    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / f"{folder.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            if path.is_dir() or any(part in SKIP_NAMES for part in path.parts):
                continue
            zf.write(path, Path(folder.name) / path.relative_to(folder))
    return out


def main() -> int:
    folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not folders:
        print("No skills found in skills/")
        return 1

    problems = [msg for folder in folders for msg in check_skill(folder)]
    if problems:
        print("Fix these before releasing:")
        for msg in problems:
            print(f"  - {msg}")
        return 1

    for folder in folders:
        out = build(folder)
        print(f"Built {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
