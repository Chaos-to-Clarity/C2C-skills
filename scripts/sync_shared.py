"""Keep shared reference files current in every skill that uses them.

Plugins install as self-contained copies and single-skill ZIPs must stand
alone, so each skill carries its own copies in references/.

- cortex-spec.md comes from the Cortex repository (its spec/ folder). It's
  fetched into shared/ so this repo always has a pinned copy.
- founder-os.md and recap-config.md are mastered here, in shared/.

Usage:
    python scripts/sync_shared.py            # fetch the Cortex spec, then copy
    python scripts/sync_shared.py --offline  # copy without fetching
    python scripts/sync_shared.py --check    # fail if any copy is out of date
"""

import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
CORTEX_SPEC_URL = "https://raw.githubusercontent.com/chaostoclarity/Cortex/main/spec/cortex-spec.md"

# shared file -> plugins whose every skill gets a copy
TARGETS = {
    "cortex-spec.md": ["founder-os", "recap"],
    "founder-os.md": ["founder-os", "recap"],
    "recap-config.md": ["recap"],
}


def fetch_cortex_spec() -> None:
    with urllib.request.urlopen(CORTEX_SPEC_URL, timeout=30) as response:
        text = response.read().decode("utf-8")
    dest = SHARED / "cortex-spec.md"
    if not dest.exists() or dest.read_text(encoding="utf-8") != text:
        dest.write_text(text, encoding="utf-8")
        print("Fetched the latest Cortex spec")


def targets():
    for filename, plugins in TARGETS.items():
        for plugin in plugins:
            for skill in sorted((ROOT / "plugins" / plugin / "skills").iterdir()):
                if skill.is_dir():
                    yield SHARED / filename, skill / "references" / filename


def main() -> int:
    check = "--check" in sys.argv
    if not check and "--offline" not in sys.argv:
        fetch_cortex_spec()

    stale = []
    for source, dest in targets():
        master = source.read_text(encoding="utf-8")
        if dest.exists() and dest.read_text(encoding="utf-8") == master:
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
