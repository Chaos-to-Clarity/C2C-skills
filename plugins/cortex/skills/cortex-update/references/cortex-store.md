# Cortex Store Reference

How every Cortex and Founder OS skill finds, reads, and writes the user's data, whatever tool they keep it in. Read this before any read or write.

This file is shared. The master copy lives in `shared/cortex-store.md` in the repository and is copied into each skill's `references/` folder. Edit the master, then run `python scripts/sync_shared.py`.

## 1. What the Cortex is

The Cortex is the user's context layer: a small, structured store of what stays true about their work, which every AI skill reads before acting. Founder OS is the weekly operating cycle that runs on top of it.

**Pages** (one document each)

| Page | Purpose |
| --- | --- |
| Overview | Map of everything in the Cortex. A Synthesis paragraph at the top, then one line per collection and page. Skills read this first. |
| Cortex Schema | The rules in section 6, written into the user's store so they can see and extend them. |
| Standing Context | Durable facts about the business and the user's role. Short prose. |
| Strategy | A summary at the top (positioning, ICP and personas, GTM, targets, brand), then one dated section per strategy document digested. |
| Cortex Config | Settings every skill reads. See section 3. |

**Cortex collections** (one record each)

| Collection | Identity | Fields |
| --- | --- | --- |
| People | Name | Role, Context (the one thing worth remembering), Cadence, Open Thread, Status (Active, Dormant, Archived), Last Updated, Source, Initiatives (relation) |
| Initiatives | Name | Why It Matters, Status (Active, Paused, Done, Dropped), Blocker, Next Action, Start, Target, Owner / Involved (relation to People), Decisions (relation), Last Updated, Source |
| Decisions | Title | Reasoning, Status (Decided, Open, Reversed, Superseded), Date, Supersedes (title of the earlier decision), Affects (relation to Initiatives), Last Updated, Source |
| Ingest Log | Source | Type (Meeting Notes, Email, Document, Strategy, Query Insight), Date Ingested, What Changed |

**Founder OS collections**

| Collection | Identity | Fields |
| --- | --- | --- |
| Weekly Goals | Name ("Week of Mon D, YYYY") | Week Start (Monday), Status (Planning, Active, Closed). Body: focus, goals, success criteria, health note, prep notes |
| Tasks | Task | Status (To do, Doing, Done), Due, Priority (High, Medium, Low), Goal (text), Week (relation to Weekly Goals) |
| Reflections | Name ("Week of Mon D, YYYY") | Week Start, Business, Health, Family, Energy (numbers 1 to 10). Body: Wins, Friction, Habits That Helped, Habits To Improve, Avoidance Patterns, Top Lesson |
| Commitments | Commitment | Status (Active, Kept, Dropped), Set (date), Week (relation to Weekly Goals) |

Users may add collections (Customers, Pipeline, Portfolio, anything). Every added collection has a title identity plus Status, Last Updated, and Source, and is listed on the Overview. Skills that read the Overview pick it up with no other change. Users may also add fields to any collection; preserve fields you don't recognize.

## 2. Supported backends

| Backend | Where it lives | How the skill reaches it |
| --- | --- | --- |
| Notion | A parent page holding the pages as pages and the collections as databases | The Notion connector |
| Google Drive | A folder of Markdown files | The Google Drive connector |
| Obsidian | A folder inside the user's vault | A folder connected through the Claude desktop app, or an Obsidian connector if one is installed |
| Local folder | Any Markdown folder on the user's computer (Dropbox, iCloud, OneDrive sync folders included) | A folder connected through the Claude desktop app |

If the user names something else (Airtable, Coda, Confluence, a Dropbox or OneDrive connector), use it when a connector exists and map the same model onto it as closely as it allows: collections become tables or folders, pages become documents. Record the mapping in the config.

Obsidian and local folders live on the user's computer. Scheduled runs only reach them while that computer is on and the Claude desktop app is open. Say so during setup.

## 3. Finding the config

Every skill starts by loading the Cortex Config. Look in this order and stop at the first hit:

1. Notion: search for a page titled exactly "Cortex Config".
2. Google Drive: search for a file named "Cortex Config.md".
3. Connected folders on the user's computer: look for "Cortex Config.md".

If none is found, the Cortex isn't set up. Tell the user in one line and offer to run cortex-setup. Founder OS skills also need the `founder_os` section; if it's missing, offer founder-os-setup.

**Validate before trusting it.** Open the Overview location the config names. If it fails (moved, deleted, connector removed), tell the user which item broke and offer to rerun the matching part of setup. Never guess a replacement location silently.

### Config format

The config is one fenced `text` block on the Cortex Config page or file. One `key: value` per line. `none` means not used.

```text
config_version: 1
owner: <first name>
time_zone: <IANA zone, e.g. America/New_York>

backend: <notion | google-drive | obsidian | local-folder | other: name>
root: <Notion page URL, or folder path / Drive folder ID>

page.overview: <URL or path>
page.schema: <URL or path>
page.standing_context: <URL or path>
page.strategy: <URL or path>

collection.people: <Notion data source URL, or folder path>
collection.initiatives: <...>
collection.decisions: <...>
collection.ingest_log: <Notion data source URL, or file path>

field_map: <none, or collection.field=actual name; collection.field=actual name>

sources.meeting_notes: <granola | fireflies | otter | fathom | notion-meetings | folder: path | none>
sources.calendar: <google-calendar | outlook | device | none>
sources.calendar_id: <primary or id>
sources.email: <gmail | outlook | none>
sources.documents: <google-drive | dropbox | onedrive | box | none>
sources.strategy_folder: <folder name or path, or none>

update.lookback_days: 7
update.approval: <autonomous | required>

[founder_os]
collection.weekly_goals: <...>
collection.tasks: <...>
collection.reflections: <...>
collection.commitments: <...>
work_days: Mon-Fri
work_hours: 09:00-17:00
deep_work_block_minutes: 120
briefing_lookback_hours: 24
```

`field_map` exists for users who adopted existing databases with different field names. Always translate through it when writing.

## 4. Operations

Every skill uses only these operations. The table says how each one works per backend.

| Operation | Notion | Markdown (Drive, Obsidian, local) |
| --- | --- | --- |
| Read page | Fetch the page | Read the `.md` file |
| Edit page | Targeted edit of the matching section; never replace the whole page unless asked | Read the file, change only the matching section, write the whole file back |
| List active | Query the data source filtered to Status = Active (or the stated filter) | Read the collection's `_index.md` and filter its rows |
| Find by identity | Query the data source for the title, case-insensitive, then near-matches | Look up the identity in `_index.md`, then open that record file |
| Create record | Create a page in the data source with all fields | Write `<Identity>.md` with frontmatter, then add its row to `_index.md` |
| Update record | Fetch the record fresh, then update only the changed fields | Read the record, change frontmatter fields, write it back, then update its `_index.md` row |
| Close record | Set Status to the closing value | Same as update |
| Append log | Create an Ingest Log row | Append a row to the table in `Ingest Log.md` |
| Check log | Query the Ingest Log for the Source | Search `Ingest Log.md` for the Source |

Re-read a record immediately before updating it. Another skill or the user may have changed it since you first read it.

## 5. Markdown layout

Used for Google Drive, Obsidian, and local folders.

```
Cortex/
  Cortex Config.md
  Overview.md
  Cortex Schema.md
  Standing Context.md
  Strategy.md
  Ingest Log.md
  People/
    _index.md
    Jane Rivera.md
  Initiatives/
    _index.md
  Decisions/
    _index.md
  Founder OS/
    Weekly Goals/
      _index.md
    Tasks/
      _index.md
    Reflections/
      _index.md
    Commitments/
      _index.md
```

**Record file.** File name is the identity, with characters that file systems reject (`/ \ : * ? " < > |`) replaced by `-`. Fields go in YAML frontmatter using the field names above, dates as `YYYY-MM-DD`. Relations are lists of wikilinks, which Obsidian renders as links:

```markdown
---
name: Jane Rivera
role: Head of Sales, Acme
context: Decides on renewals; prefers short written updates
cadence: Biweekly
open_thread: Waiting on Q3 pricing proposal
status: Active
initiatives: ["[[Q3 Pricing Reset]]"]
last_updated: 2026-01-15
source: Granola, Acme sync Jan 15
---

Optional longer notes.
```

**`_index.md`.** One table per collection, one row per record, kept in step with every create and update. It lets skills filter without opening every file. Columns:

| Collection | Index columns |
| --- | --- |
| People | Name, Status, Role, Last Updated |
| Initiatives | Name, Status, Next Action, Target, Last Updated |
| Decisions | Title, Status, Date |
| Weekly Goals | Name, Week Start, Status |
| Tasks | Task, Status, Due, Priority, Week |
| Reflections | Name, Week Start, Business, Health, Family, Energy |
| Commitments | Commitment, Status, Set, Week |

Link the identity cell to the file: `[[Jane Rivera]]`. If an index looks out of step with the folder, rebuild it from the record files and say so in the report.

**`Ingest Log.md`.** One table, newest row at the bottom: Source, Type, Date Ingested, What Changed.

**Google Drive specifics.** Create files as plain Markdown (`text/markdown`), never as Google Docs, so they stay readable by every tool. Updates rewrite the whole file, so read, change, write back in one step.

## 6. Cortex Schema rules

Setup writes these rules to the user's Cortex Schema page. If that page exists, read it; the user may have extended it, and their version wins. If it's missing, use these.

- **Identity first.** Each record has a stable identity, its title. Before writing, find the existing record by identity and update it in place. Never create a second record for the same person, initiative, or decision.
- **Supersede, don't delete.** When something changes or a decision reverses, set the old record's Status to the right closed value (Reversed, Superseded, Done, Dropped, Archived) and record the new state. Never delete history. Delete only a true accidental duplicate.
- **Stamp every write.** Set Last Updated to today and record the Source the entry came from.
- **Log every ingest.** Before ingesting a source, check the Ingest Log. If it's there, skip it. After ingesting, add a row: source, type, date, what changed. This makes ingestion safe to repeat.
- **Read the Overview first.** Open the Overview, then only the collections the task needs, filtered to Active. Never load the whole Cortex at once.
- **Durable only.** Keep what stays true for weeks or months. Day-to-day task noise belongs in Founder OS, not the Cortex.
- **Write in the user's words.** Condense. Drop marketing language and filler.
- **Extending the Cortex.** A new collection gets a title identity plus Status, Last Updated, and Source, and a line on the Overview. Propose a new collection to the user before creating it, even in autonomous runs.

## 7. Sources

Live sources are read through whatever connector the config names. If a source is `none` or its connector fails, note it in one line and continue with the rest. Never stop a whole run because one source is down.

| Source | Typical use |
| --- | --- |
| Meeting notes | Recent meetings, open actions, decisions, who is waiting on the user |
| Calendar | Today's and this week's events, free time, upcoming meetings with a person |
| Email | Threads that need a reply or decision, new relationships, strategic signal. Skip newsletters, receipts, and automated mail |
| Documents | Files the user names, and the strategy folder |
