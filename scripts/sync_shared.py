"""Keep shared reference files current in every skill that uses them.

Plugins install as self-contained copies and single-skill ZIPs must stand
alone, so each skill carries its own copies in references/.

- cortex-spec.md comes from the Cortex repository (its spec/ folder). It's
  fetched into shared/ so this repo always has a pinned copy.
- founder-os.md, recap-config.md, and content-engine-config.md are mastered
  here, in shared/.
- The Chaos to Clarity Coach tools are mastered in shared/coach/ and copied
  into the router (c2c-coach) and the six theme plugins. See the Coach
  section below.

Usage:
    python scripts/sync_shared.py            # fetch the Cortex spec, then copy
    python scripts/sync_shared.py --offline  # copy without fetching
    python scripts/sync_shared.py --check    # fail if any copy is out of date
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
CORTEX_SPEC_URL = "https://raw.githubusercontent.com/chaostoclarity/Cortex/main/spec/cortex-spec.md"

# shared file -> plugins whose every skill gets a copy
TARGETS = {
    "cortex-spec.md": ["founder-os", "recap", "content-engine",
                       "investor-update", "customer-signal", "one-on-ones",
                       "c2c-life-coach"],
    "founder-os.md": ["founder-os", "recap", "investor-update", "one-on-ones"],
    "recap-config.md": ["recap"],
    "content-engine-config.md": ["content-engine"],
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


# ---------------------------------------------------------------------------
# Chaos to Clarity Coach
#
# Every coaching tool is mastered once in shared/coach/:
#   coach.json        registry: tool names, themes, and which plugin holds what
#   tools/<slug>.md   the full exercise
#   index/<slug>.md   problems, when to deploy, and what founders say
#   coach-method.md   how every coach skill runs a tool and closes
#
# The router (c2c-coach) carries all of them. Each theme plugin carries its
# own tools. This builds every coach skill's references/ folder and the
# generated index table inside its SKILL.md.
# ---------------------------------------------------------------------------

COACH = SHARED / "coach"
INDEX_START = "<!-- coach-index:start -->"
INDEX_END = "<!-- coach-index:end -->"
GENERATED = "<!-- Generated from shared/coach by scripts/sync_shared.py. Edit there, not here. -->"


def coach_registry() -> dict:
    return json.loads((COACH / "coach.json").read_text(encoding="utf-8"))


def coach_plugins(reg: dict) -> dict:
    """plugin -> ordered list of themes it carries (router carries all)."""
    plugins = {reg["router"]: reg["themes"]}
    for theme in reg["themes"]:
        plugins[theme["plugin"]] = [theme]
    return plugins


def theme_of(reg: dict, slug: str) -> dict:
    return next(t for t in reg["themes"] if slug in t["tools"])


def render_links(text: str, reg: dict, carried: set) -> str:
    def link(match):
        slug = match.group(1)
        name = reg["tools"][slug]["name"]
        if slug in carried:
            return f"**{name}**"
        return f"**{name}** ({theme_of(reg, slug)['title']} plugin)"
    return re.sub(r"\[\[([a-z0-9-]+)\]\]", link, text)


def compose_tool_index(reg: dict, themes: list, router: bool) -> str:
    carried = {slug for t in themes for slug in t["tools"]}
    title = "All Chaos to Clarity Coach tools" if router else themes[0]["title"]
    out = [GENERATED, "", f"# Tool Index: {title}", "",
           "Match the founder's own words against these entries. If their phrasing is close "
           "to a row in a tool's table, that tool is the primary; the Also consider column "
           "gives the alternative. Each tool's full exercise is in the file named under it.", ""]
    for theme in themes:
        out += [f"## {theme['title']}", "", f"{theme['summary']}.", ""]
        for slug in theme["tools"]:
            fragment = (COACH / "index" / f"{slug}.md").read_text(encoding="utf-8").strip()
            out += [f"### {reg['tools'][slug]['name']}", f"File: `tools/{slug}.md`", "",
                    render_links(fragment, reg, carried), ""]
    if not router:
        out += ["## In other Chaos to Clarity Coach plugins", "",
                "This skill doesn't carry these. When one fits better, name it and its plugin, "
                "and hand off if that skill is available. The all-in-one Chaos to Clarity AI "
                "Coach carries every tool.", "",
                "| Tool | Use it when | Plugin |", "| --- | --- | --- |"]
        for theme in reg["themes"]:
            if theme in themes:
                continue
            for slug in theme["tools"]:
                tool = reg["tools"][slug]
                out.append(f"| {tool['name']} | {tool['use_when']} | {theme['title']} (`{theme['plugin']}`) |")
        out.append("")
    return "\n".join(out)


def compose_skill_table(reg: dict, themes: list, router: bool) -> str:
    rows = [INDEX_START, GENERATED, "", "| Tool | Use it when | File |", "| --- | --- | --- |"]
    for theme in themes:
        if router:
            rows.append(f"| **{theme['title']}** (also its own plugin, `{theme['plugin']}`) | | |")
        for slug in theme["tools"]:
            tool = reg["tools"][slug]
            rows.append(f"| {tool['name']} | {tool['use_when']} | `{slug}.md` |")
    rows.append(INDEX_END)
    return "\n".join(rows)


def coach_outputs():
    """Yield (path, expected text) for every generated coach file."""
    reg = coach_registry()
    for plugin, themes in coach_plugins(reg).items():
        router = plugin == reg["router"]
        skills_dir = ROOT / "plugins" / plugin / "skills"
        if not skills_dir.exists():
            raise SystemExit(f"Coach plugin missing: plugins/{plugin}")
        for skill in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            refs = skill / "references"
            wanted = {f"{slug}.md" for t in themes for slug in t["tools"]}
            for name in sorted(wanted):
                yield refs / "tools" / name, (COACH / "tools" / name).read_text(encoding="utf-8")
            yield refs / "coach-method.md", (COACH / "coach-method.md").read_text(encoding="utf-8")
            yield refs / "tool-index.md", compose_tool_index(reg, themes, router)
            skill_md = skill / "SKILL.md"
            text = skill_md.read_text(encoding="utf-8")
            if INDEX_START not in text or INDEX_END not in text:
                raise SystemExit(f"{skill_md.relative_to(ROOT)} needs {INDEX_START} and {INDEX_END} markers")
            head, rest = text.split(INDEX_START, 1)
            tail = rest.split(INDEX_END, 1)[1]
            yield skill_md, head + compose_skill_table(reg, themes, router) + tail


def stale_tool_files():
    reg = coach_registry()
    for plugin, themes in coach_plugins(reg).items():
        wanted = {f"{slug}.md" for t in themes for slug in t["tools"]}
        for tools_dir in (ROOT / "plugins" / plugin / "skills").glob("*/references/tools"):
            for f in sorted(tools_dir.glob("*.md")):
                if f.name not in wanted:
                    yield f


def main() -> int:
    check = "--check" in sys.argv
    if not check and "--offline" not in sys.argv:
        fetch_cortex_spec()

    stale = []
    pairs = [(dest, source.read_text(encoding="utf-8")) for source, dest in targets()]
    pairs += list(coach_outputs())
    for dest, master in pairs:
        if dest.exists() and dest.read_text(encoding="utf-8") == master:
            continue
        if check:
            stale.append(dest.relative_to(ROOT))
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(master, encoding="utf-8")
            print(f"Updated {dest.relative_to(ROOT)}")
    for extra in stale_tool_files():
        if check:
            stale.append(f"{extra.relative_to(ROOT)} (not in shared/coach/coach.json for this plugin)")
        else:
            extra.unlink()
            print(f"Removed {extra.relative_to(ROOT)}")
    if stale:
        print("Shared files out of date. Run: python scripts/sync_shared.py")
        for path in stale:
            print(f"  - {path}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
