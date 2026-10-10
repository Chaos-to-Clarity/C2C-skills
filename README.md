# Chaos to Clarity Skills

Claude skills for founders and operators, from Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io). Each one turns a recurring piece of work into a single message to Claude.

## What's here

| Plugin | What it does |
| --- | --- |
| [**Cortex**](https://github.com/chaostoclarity/Cortex) | The context layer your AI reads first. A Map, catalogs, and records for your people, initiatives, decisions, and strategy, in Notion, Obsidian, or Google Drive. Lives in its own repo, listed here so one marketplace installs everything. |
| [**Founder OS**](plugins/founder-os) | Your weekly operating cycle. Plan Monday, brief each morning, reflect Friday. Runs on your Cortex. |
| [**Handwritten Notes**](plugins/handwritten-notes) | Photograph a page of notes. Checkbox items become tasks with time booked on your calendar. Everything else is filed as notes. |

Start with Cortex, then add Founder OS. Handwritten Notes works on its own.

## Install: the whole set (recommended)

Installs every skill in a plugin at once and keeps them updated. Needs a paid Claude plan.

**In the Claude app**

1. Open **Customize**, then **Plugins**.
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. Enter `chaostoclarity/Claude-skills`.
4. Add the plugins you want: Cortex, Founder OS, Handwritten Notes.

**In Claude Code**

```
claude plugin marketplace add chaostoclarity/Claude-skills
claude plugin install cortex@chaostoclarity
claude plugin install founder-os@chaostoclarity
```

## Install: one skill at a time

1. Click a **Download** link below. A ZIP file downloads. Don't unzip it.
2. In Claude, open **Customize**, then **Skills**.
3. Click **Create skill**, then **Upload a skill**, and choose the ZIP.
4. Turn the skill on, start a new chat, and use it.

Cortex skills download from the [Cortex repo](https://github.com/chaostoclarity/Cortex#install).

| Skill | Plugin | When you use it | Download |
| --- | --- | --- | --- |
| founder-os-setup | Founder OS | Once, to build the weekly system | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/founder-os-setup.zip) |
| weekly-planning | Founder OS | Monday | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/weekly-planning.zip) |
| daily-briefing | Founder OS | Each work day, on a schedule | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/daily-briefing.zip) |
| weekly-retro | Founder OS | Friday | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/weekly-retro.zip) |
| handwritten-notes | Handwritten Notes | Whenever you photograph your notes | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/handwritten-notes.zip) |

Skills you upload are private to your account. Your data stays in your own tools.

## Updating

Plugins added from the marketplace in the Claude app pick up new versions on their own. In Claude Code, turn on auto-update for the marketplace under `/plugin`, then Marketplaces, or run `claude plugin update`. For single skills, download links always serve the newest version: delete the old skill in Claude's Skills settings and upload the new ZIP. Your settings carry over, because they live in your own tools, not in the skill file.

## Questions

Reach Eric at [chaostoclarity.io](https://chaostoclarity.io).

## License

Free to use and adapt inside your own business. Not for resale, redistribution, or sharing.

These skills are licensed under the [PolyForm Internal Use License 1.0.0](LICENSE.md). In plain terms:

- **You can** install them, run them for your own company's internal operations, and change them to fit how you work.
- **You can't** share or distribute them, sublicense them, sell them, or package them into a product or service for others.

For other uses, such as rolling them out to clients or teaching them, contact Eric at [chaostoclarity.io](https://chaostoclarity.io).

## For maintainers

**Layout.** `.claude-plugin/marketplace.json` lists the plugins. Each plugin lives in `plugins/<plugin>/` with `.claude-plugin/plugin.json` and one folder per skill in `skills/`.

**Adding a skill**

1. Add `plugins/<plugin>/skills/<name>/SKILL.md`. The folder name must match the skill's `name` (lowercase, hyphens), and names must be unique across plugins.
2. Keep the `description` under 200 characters, and keep personal details (IDs, emails, workspace links) out of the file.
3. For a new plugin, add its `plugin.json` and an entry in `marketplace.json`. Don't set `version`: leaving it out lets installs track each commit.
4. Add a row to the download table above.
5. Commit and push to `main`. The release workflow checks everything, builds the ZIPs, and publishes a release. Links update automatically.

**Shared files.** Founder OS skills carry two references: `cortex-spec.md`, fetched from the [Cortex repo](https://github.com/chaostoclarity/Cortex/blob/main/spec/cortex-spec.md), and `founder-os.md`, mastered in `shared/`. Run `python scripts/sync_shared.py` to fetch and copy both. The release workflow also runs it daily and commits any change, so Founder OS picks up Cortex spec updates on its own.

**Cortex** is listed in `marketplace.json` with a `git-subdir` source pointing at `chaostoclarity/Cortex`. Its code lives only there.

**Test locally**

```
python scripts/sync_shared.py
python scripts/build_zips.py
claude plugin validate .
```
