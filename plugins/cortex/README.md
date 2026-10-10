# Cortex

The context layer your AI reads first.

Every AI tool you use starts from zero: who your people are, what you're driving, what you already decided. Cortex fixes that. It's a small, structured store of what stays true about your work, and every Cortex and Founder OS skill reads it before acting. It gets more useful every week because it updates itself from your meetings and email.

## What's in it

| Part | Holds |
| --- | --- |
| People | Everyone you deal with regularly, with the one thing worth remembering and the open thread |
| Initiatives | What you're driving: why it matters, status, blocker, next action |
| Decisions | Calls made and questions still open, with the reasoning |
| Strategy | Positioning, ICP, GTM, targets, and brand, digested from your docs |
| Standing Context | Durable facts about your business and your role |
| Overview | The map. A live one-paragraph read on where things stand |
| Ingest Log | What's been processed, so nothing is ingested twice |

You can add your own collections (Customers, Pipeline, Portfolio). Register them on the Overview and every skill picks them up.

## Where it lives

You choose during setup:

- **Notion:** databases with relations
- **Obsidian:** Markdown files in your vault, linked with wikilinks
- **Markdown in Google Drive:** plain files, readable by any tool
- **Another tool**, if Claude has a connector for it

The structure and rules are the same everywhere, so you can switch later.

## The skills

| Skill | Run it | What it does |
| --- | --- | --- |
| `cortex-setup` | Once | Asks where to store it, connects your sources, builds the structure, and interviews you to fill it |
| `strategy-digest` | When a strategy doc changes | Condenses plans, decks, personas, and brand docs into the Strategy page |
| `add-to-cortex` | Any time | Digests one doc into the right places, without duplicates |
| `cortex-update` | Weekly, scheduled | Scans recent meetings, email, and calendar and updates everything in place |
| `ask-cortex` | Any time | Answers questions by connecting the Cortex with your live calendar, meetings, and email |

## Get started

1. Install the Cortex plugin (see the [main page](../../README.md)).
2. Say: **"Set up my Cortex."**
3. When it's done, say **"Digest my strategy docs"**, then ask it anything: **"Prep me for my call with Sam."**

## What it needs

- A storage tool: Notion, Obsidian, or Google Drive connected to Claude
- Optional but recommended: your meeting notes app, calendar, and email connected to Claude
- For weekly scheduled updates: a Claude plan with scheduled tasks
