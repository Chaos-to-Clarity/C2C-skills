# Chaos to Clarity Skills

Claude skills for founders and operators, from Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io). Each one turns a recurring piece of work into a single message to Claude.

Want help putting this to work in your company? [Work with Eric.](#work-with-eric)

## What's here

| Plugin | What it does |
| --- | --- |
| [**Cortex**](https://github.com/chaostoclarity/Cortex) | The context layer your AI reads first. A Map, catalogs, and records for your people, initiatives, decisions, and strategy, in Notion, Obsidian, or Google Drive. Lives in its own repo, listed here so one marketplace installs everything. |
| [**Founder OS**](plugins/founder-os) | Your weekly operating cycle. Plan Monday, brief each morning, reflect Friday. Runs on your Cortex. |
| [**Recap**](plugins/recap) | Every meeting becomes done work: a branded recap email, your to-dos with time booked, follow-ups drafted, agreed meetings booked, and context saved. Runs twice a day. |
| [**Content Engine**](plugins/content-engine) | Last week's meetings become this week's content. One original framework, a newsletter issue, and a LinkedIn post in your voice, with every story kept confidential. Runs every Monday. |
| [**Chaos to Clarity AI Coach**](plugins/c2c-coach) | 30 leadership exercises for founders. Describe the problem in one sentence; Claude picks the tool and coaches you through it. |
| [**Above the Chaos**](plugins/above-the-chaos) | Nine Stoic leadership exercises from the book *Above the Chaos*. Claude coaches you through each one and gives you a summary to keep. Get the book at [abovethechaosbook.com](https://abovethechaosbook.com). |
| [**Handwritten Notes**](plugins/handwritten-notes) | Photograph a page of notes. Checkbox items become tasks with time booked on your calendar. Everything else is filed as notes. |
| [**Voice**](plugins/voice) | Share a few pieces of your writing and get your own voice skill. It drafts and rewrites anything so it sounds like you, and learns from every edit you make. |

Start with Cortex, then add Founder OS and Recap. The AI Coach, Above the Chaos, Handwritten Notes, and Voice work on their own. Recap and Content Engine work on their own too, and get smarter with a Cortex. Content Engine sounds most like you when you add Voice.

## Install: the whole set (recommended)

Installs every skill in a plugin at once and keeps them updated. Needs a paid Claude plan.

**In the Claude app**

1. Open **Customize**, then **Plugins**.
2. Click **Add**, then **Add marketplace**, then **Add from a repository**.
3. Enter `chaostoclarity/C2C-skills`.
4. Add the plugins you want: Cortex, Founder OS, Recap, Content Engine, Chaos to Clarity AI Coach, Above the Chaos, Handwritten Notes, Voice.

**In Claude Code**

```
claude plugin marketplace add chaostoclarity/C2C-skills
claude plugin install cortex@chaostoclarity
claude plugin install founder-os@chaostoclarity
claude plugin install recap@chaostoclarity
claude plugin install content-engine@chaostoclarity
claude plugin install c2c-coach@chaostoclarity
claude plugin install above-the-chaos@chaostoclarity
claude plugin install handwritten-notes@chaostoclarity
claude plugin install voice@chaostoclarity
```

## Install: one skill at a time

1. Click a **Download** link below. A ZIP file downloads. Don't unzip it.
2. In Claude, open **Customize**, then **Skills**.
3. Click **Create skill**, then **Upload a skill**, and choose the ZIP.
4. Turn the skill on, start a new chat, and use it.

Cortex skills download from the [Cortex repo](https://github.com/chaostoclarity/Cortex#install).

| Skill | Plugin | When you use it | Download |
| --- | --- | --- | --- |
| founder-os-setup | Founder OS | Once, to build the weekly system | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/founder-os-setup.zip) |
| weekly-planning | Founder OS | Monday | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/weekly-planning.zip) |
| daily-briefing | Founder OS | Each work day, on a schedule | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/daily-briefing.zip) |
| weekly-retro | Founder OS | Friday | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/weekly-retro.zip) |
| recap-setup | Recap | Once, to connect tools, set your branding, and schedule it | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/recap-setup.zip) |
| meeting-recap | Recap | Twice a day on a schedule, or "recap my last meeting" | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/meeting-recap.zip) |
| content-engine-setup | Content Engine | Once, to connect your notes, learn your voice, and schedule it | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/content-engine-setup.zip) |
| weekly-content-engine | Content Engine | Every Monday on a schedule, or "run my content engine" | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/weekly-content-engine.zip) |
| c2c-coach | Chaos to Clarity AI Coach | Whenever you're stuck on a leadership problem | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/c2c-coach.zip) |
| above-the-chaos | Above the Chaos | When you want to work on how you lead, not just what you do | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/above-the-chaos.zip) |
| handwritten-notes | Handwritten Notes | Whenever you photograph your notes | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/handwritten-notes.zip) |
| voice-setup | Voice | Once, to build your voice skill from samples of your writing | [ZIP](https://github.com/chaostoclarity/C2C-skills/releases/latest/download/voice-setup.zip) |

Skills you upload are private to your account. Your data stays in your own tools.

## Updating

Plugins added from the marketplace in the Claude app pick up new versions on their own. In Claude Code, turn on auto-update for the marketplace under `/plugin`, then Marketplaces, or run `claude plugin update`. For single skills, download links always serve the newest version: delete the old skill in Claude's Skills settings and upload the new ZIP. Your settings carry over, because they live in your own tools, not in the skill file.

## Questions

Reach Eric at [chaostoclarity.io](https://chaostoclarity.io).

## Work with Eric

I'm Eric Weiss, founder of Chaos to Clarity. I've spent ten years coaching more than 70 technical founders and CTOs at venture-backed companies, and every skill here came out of that work. There are a few ways I can help you go further.

**Executive coaching.** I coach founders and CTOs whose companies are growing faster than their leadership. Together we find the real bottleneck, name what you're tolerating, and build the habits and systems that let the company scale without routing everything through you.

**AI strategy.** I help leadership teams decide where AI belongs in the business, set the guardrails, and get their people using it well. I was an engineering leader and CTO before I became a coach, and I helped OpenAI operationalize its GPT models.

**AI products with a human edge.** I work with product teams to build AI into what they ship while keeping judgment, taste, and relationships in human hands.

**The Full-Stack AI Operating System.** This 12-week bootcamp is for founders and their executive teams. You'll build an AI strategy, an AI-native product roadmap, working systems with human checkpoints, and adoption guidelines for your team, and you'll leave with a library of AI skills and a 90-day plan. The program runs as six live workshops and six office hours in small cohorts. [See the program.](https://chaostoclarity.io/ai-os/)

**Let's talk.** [Book a call](https://calendly.com/emweiss/clarity), or email me at [eric@chaostoclarity.io](mailto:eric@chaostoclarity.io). Tell me what you're building and where you're stuck, and I'll reply personally.

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

**Shared files.** Founder OS, Recap, and Content Engine skills carry shared references: `cortex-spec.md`, fetched from the [Cortex repo](https://github.com/chaostoclarity/Cortex/blob/main/spec/cortex-spec.md), plus `founder-os.md`, `recap-config.md`, and `content-engine-config.md`, mastered in `shared/`. Run `python scripts/sync_shared.py` to fetch and copy them. The release workflow also runs it daily and commits any change, so these plugins pick up Cortex spec updates on their own.

**Cortex** is listed in `marketplace.json` with a `git-subdir` source pointing at `chaostoclarity/Cortex`. Its code lives only there.

**Test locally**

```
python scripts/sync_shared.py
python scripts/build_zips.py
claude plugin validate .
```
