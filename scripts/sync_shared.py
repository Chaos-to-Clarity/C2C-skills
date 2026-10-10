"""Copy shared reference files into every skill that uses them.

Plugins are installed as self-contained copies, and single-skill ZIPs must
stand alone, so a skill can't point at a file outside its own folder. The
master copy of each shared file lives in shared/; this script copies it into
skills/<name>/references/ for every skill listed below.

Usage:
    python scripts/sync_shared.py          # copy
    python scripts/sync_shared.py --check  # fail if any copy is out of date
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"

# shared file -> plugins whose every skill gets a copy
TARGETS = {
    "cortex-store.md": ["cortex", "founder-os"],
}


def targets():
    for filename, plugins in TARGETS.items():
        source = SHARED / filename
        for plugin in plugins:
            for skill in sorted((ROOT / "plugins" / plugin / "skills").iterdir()):
                if skill.is_dir():
                    yield source, skill / "references" / filename


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for source, dest in targets():
        master = source.read_text(encoding="utf-8")
        current = dest.read_text(encoding="utf-8") if dest.exists() else None
        if current == master:
            continue
        if check:
            stale.append(dest.relative_to(ROOT))
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(master, encoding="utf-8")
            print(f"Updated {dest.relative_to(ROOT)}")
    if stale:
        print("Shared files out of date. Run: python scripts/sync_shared.py")
        for path in stale:
            print(f"  - {path}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
