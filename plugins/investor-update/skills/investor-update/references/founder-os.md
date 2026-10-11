# Founder OS Reference

What Founder OS stores, and how it plugs into the user's Cortex. Read this alongside `cortex-spec.md`, which defines the Map, catalogs, record format, and the reading and writing protocols. Founder OS follows all of them.

The master copy lives in `shared/founder-os.md` in the C2C-skills repository and is copied into each Founder OS skill. Edit the master, then run `python scripts/sync_shared.py`.

## Collections

Founder OS adds four collections to the user's Cortex. Each also carries the fields every Cortex record has: Summary, Aliases, Status, Last Updated, Source.

| Collection | Identity | Fields | Statuses | Catalog key columns |
| --- | --- | --- | --- | --- |
| Weekly Goals | Name ("Week of Mon D, YYYY") | Week Start (Monday). Body: Focus, Goals with success criteria, Health note, Prep, Retro prep | Planning, Active, Closed | Week Start |
| Tasks | Task | Due, Priority (High, Medium, Low), Goal (text), Week (relation to Weekly Goals) | To do, Doing, Done | Due, Priority, Week |
| Reflections | Name ("Week of Mon D, YYYY") | Week Start, Business, Health, Family, Energy (1 to 10). Body: Wins, Friction, Habits That Helped, Habits To Improve, Avoidance Patterns, Top Lesson | Active, Archived | Week Start |
| Commitments | Commitment | Set (date), Week (relation to Weekly Goals) | Active, Kept, Dropped | Set |

Closed statuses (Closed, Done, Archived, Kept, Dropped) move a record's catalog row to the Archive catalog, so default reads stay small. A Reflection is set to Archived once it's more than four weeks old; weekly-retro reads the last few from the archive when it looks for patterns.

## Registering with the Cortex Map

founder-os-setup adds these to the Map.

**Collections table:** one row per collection above, with its catalog and location links.

**Routing**

Find it:
- This week's goals, focus, what's planned → Weekly Goals
- Open tasks, what's due, what's overdue → Tasks
- How past weeks went, patterns, lessons → Reflections
- Non-negotiables, promises to self → Commitments

File it:
- A to-do or action item for the owner → Tasks (not the Cortex's Initiatives, unless it's a multi-week effort)
- A weekly plan → Weekly Goals
- A weekly reflection → Reflections
- A commitment for the week → Commitments

**Settings** (added under the Map's Settings block):

```text
founder_os.work_days: Mon-Fri
founder_os.work_hours: 09:00-17:00
founder_os.deep_work_block_minutes: 120
founder_os.briefing_lookback_hours: 24
```

## How Founder OS reads

Always through the Map and catalogs, never by listing databases:

- **This week:** the Weekly Goals catalog, the row whose Week Start is this Monday, then open that record.
- **Open and overdue tasks:** the Tasks catalog filtered on Status (To do, Doing) and Due. Open a task record only when its body matters.
- **Last week's tasks:** Tasks catalog rows whose Week is last week's record, in both the main and Archive catalogs.
- **Patterns:** the last three or four Reflections, from the main and Archive catalogs.

Cortex context (people, initiatives, decisions, strategy) follows the Reading protocol in `cortex-spec.md` section 6.
