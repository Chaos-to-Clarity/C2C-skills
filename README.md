# Chaos to Clarity Skills

Claude skills for founders and operators, from Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io). Each one turns a recurring piece of work into a single message to Claude.

## What's here

| Plugin | What it does |
| --- | --- |
| [**Cortex**](plugins/cortex) | The context layer your AI reads first. Your people, initiatives, decisions, and strategy in Notion, Obsidian, or Google Drive, kept current from your meetings and email. |
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

| Skill | Plugin | When you use it | Download |
| --- | --- | --- | --- |
| cortex-setup | Cortex | Once, to build your Cortex | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/cortex-setup.zip) |
| strategy-digest | Cortex | When a strategy doc changes | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/strategy-digest.zip) |
| add-to-cortex | Cortex | Any time you have a doc worth keeping | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/add-to-cortex.zip) |
| cortex-update | Cortex | Weekly, on a schedule | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/cortex-update.zip) |
| ask-cortex | Cortex | Any question about your work | [ZIP](https://github.com/chaostoclarity/Claude-skills/releases/latest/download/ask-cortex.zip) |
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

## For maintainers

**Layout.** `.claude-plugin/marketplace.json` lists the plugins. Each plugin lives in `plugins/<plugin>/` with `.claude-plugin/plugin.json` and one folder per skill in `skills/`.

**Adding a skill**

1. Add `plugins/<plugin>/skills/<name>/SKILL.md`. The folder name must match the skill's `name` (lowercase, hyphens), and names must be unique across plugins.
2. Keep the `description` under 200 characters, and keep personal details (IDs, emails, workspace links) out of the file.
3. For a new plugin, add its `plugin.json` and an entry in `marketplace.json`. Don't set `version`: leaving it out lets installs track each commit.
4. Add a row to the download table above.
5. Commit and push to `main`. The release workflow checks everything, builds the ZIPs, and publishes a release. Links update automatically.

**Shared files.** `shared/cortex-store.md` is the storage spec every Cortex and Founder OS skill follows. Edit the master copy, then run `python scripts/sync_shared.py` to copy it into each skill. The build fails if a copy is out of date.

**Test locally**

```
python scripts/sync_shared.py
python scripts/build_zips.py
claude plugin validate .
```
