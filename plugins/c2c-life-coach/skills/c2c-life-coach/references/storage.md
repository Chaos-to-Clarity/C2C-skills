# Storage and Schema

Where the life coaching system lives and what it's made of. The same schema works in every backend.

## Choosing a place (setup)

Ask once, during setup. First ask whether they use a Cortex (and look for a Cortex Map silently, per `cortex-spec.md` section 4). Then:

| Option | What gets created | How Claude reaches it |
| --- | --- | --- |
| **Cortex** (offer first when one exists) | A "Life Coaching" page or folder under the Cortex parent, with its collections registered in the Cortex Map | Whatever backend the Cortex uses |
| **Notion** | Ask where: under a page they name, or a new private top-level page. Then the Life Coaching home page with four databases inside it | The Notion connector |
| **Google Drive** | A "Life Coaching" folder of Markdown files | The Google Drive connector |
| **A folder on their computer** (Obsidian, Dropbox, iCloud, OneDrive) | The same Markdown layout as Google Drive | A folder connected through the Claude desktop app |

Anything else with a connector (Airtable, Coda): map the same structure as closely as it allows and note the mapping in the home's Settings.

Recommend a private location. This holds sensitive personal data: their relationships, health, and habits.

**Check that it works before moving on.** Make one real call: find or create the parent. If the tool isn't available, say which connection is missing in one line and let them choose again. Never pretend a save worked.

**Scheduled runs and local folders.** Obsidian and local folders are reachable only while that computer is on with the Claude desktop app open. Say so in one line if they choose one; a cloud backend (Notion, Google Drive) is more reliable for daily check-ins.

**Chat only isn't an option** for this skill. The daily and weekly coaching depends on a log. If they don't want to store anything, offer to run a one-time intake in the chat and stop there.

## What gets created

```
Life Coaching (home page)
  Coaching Frameworks (page, copied from frameworks.md)
  Habits (collection)
  Daily Check-ins (collection, a log)
  Weekly Sessions (collection, a log)
  Commitments (collection; reuse an existing one if Founder OS or Cortex has it)
```

### The home page

Create it with these sections, in this order. The scheduled task reads it first on every run, so it must stay current and readable.

```markdown
# Life Coaching

[One line: what this is, and that the scheduled coach reads this page first.]

## Settings
```text
owner: <first name>
time_zone: <IANA zone>
backend: <cortex-notion | notion | google-drive | obsidian | local-folder | other>
daily_checkin_time: <HH:MM local>
weekly_session_day: <Sunday>
weekend_checkins: <full | light | off>
areas: <Sleep, Health and Energy, Time and Focus, Partner, Family, Nature and Play>
intake: <not complete | complete YYYY-MM-DD>
resume_point: <none, or "intake step 5, area 3 of 6">
scheduled_task: <name of the scheduled task>
installed: <YYYY-MM-DD>
```

## How the system works
[Copy section 1 and sections 3 to 7 of system.md, in plain short form.]

## Who I'm becoming
[Identity statements, one per role, in the user's words. Filled during intake.]

## Habit map by area
[One line per area: Builds: ... Drops: ... Mirrors the Habits collection.]

## Active commitments
[One or two. Each with the trigger, the replacement, and the test ahead.]

## Daily check-in
[The protocol from daily-checkin.md, adjusted to their settings.]

## Weekly session
[The 10-step map from weekly-session.md.]

## Coaching rules
[The rules from system.md section 9, plus any the user adds ("don't bring up X on weekdays").]

## Parking lot
[Topics the user parked, dated. The weekly session pulls from here.]

## Weekly session agenda
[Open items, in priority order.]

## Baseline
[The intake scorecard: area, 7-day, 90-day, one-line note.]

## Session notes
[One short dated entry per intake or weekly session.]
```

### Habits

| Property | Type |
| --- | --- |
| Habit | Title |
| Area | Multi-select: the user's areas |
| Type | Select: Build, Drop |
| Frequency | Select: Daily, Weekdays, Weekly |
| Target | Text: what doing it means, in their words |
| Tracked As | Text: the Daily Check-ins column, or "Weekly review" or "Rotating question" |
| Status | Select: Active, Paused, Retired |
| Set | Date |
| Notes | Text |

### Daily Check-ins (a log)

| Property | Type |
| --- | --- |
| Check-in | Title: "YYYY-MM-DD Weekday" |
| Date | Date |
| Score [Area] | Number, one per area (Score Sleep, Score Health, Score Focus, Score Partner, Score Family, Score Nature) |
| One checkbox per daily-tracked habit | Checkbox, named short (Exercise, Screens Off, Bed On Time, Kept My Cool) |
| Habits Logged | Checkbox: this date's habit report is complete |
| Commitment Held | Select: Yes, No, Not tested |
| Tonight's Plan | Text |
| Question of the Day | Text |
| Answer | Text |
| Coach Note | Text: pattern seen, framework used, advice given |
| Status | Select: Completed, Partial, Missed |

Create the six default score columns at setup so a scheduled run works before intake. Intake renames or adds score columns for the user's chosen areas and adds the habit checkboxes. The weekly habit review adds or retires habit columns; never delete a column with data in it, just stop using it.

### Weekly Sessions (a log)

| Property | Type |
| --- | --- |
| Session | Title: "YYYY-MM-DD Weekly" (or "Intake", "Monthly") |
| Date | Date |
| Type | Select: Intake, Weekly, Monthly |
| [Area] 7d and [Area] 90d | Number, two per area |
| Week Recap | Text: start versus end scores, what happened, which habits moved which scores |
| Habit Hit Rates | Text |
| Deep Topic | Text |
| Insight | Text, in the user's words |
| Commitment | Text |
| Check-in Changes | Text |
| Status | Select: Completed, Partial, Missed |

### Commitments

If a Commitments collection already exists (Founder OS, or the user's Cortex), use it and don't create another. Otherwise create one: Commitment (title), Status (Active, Kept, Dropped), Set (date), Summary, Source, Last Updated.

### Notion DDL

For the Notion connector's create-database tool:

```sql
CREATE TABLE ("Habit" TITLE, "Area" MULTI_SELECT('Sleep':blue, 'Health and Energy':green, 'Time and Focus':purple, 'Partner':pink, 'Family':orange, 'Nature and Play':brown), "Type" SELECT('Build':green, 'Drop':red), "Frequency" SELECT('Daily':blue, 'Weekdays':purple, 'Weekly':yellow), "Target" RICH_TEXT, "Tracked As" RICH_TEXT, "Status" SELECT('Active':green, 'Paused':gray, 'Retired':default), "Set" DATE, "Notes" RICH_TEXT)

CREATE TABLE ("Check-in" TITLE, "Date" DATE, "Score Sleep" NUMBER, "Score Health" NUMBER, "Score Focus" NUMBER, "Score Partner" NUMBER, "Score Family" NUMBER, "Score Nature" NUMBER, "Habits Logged" CHECKBOX, "Commitment Held" SELECT('Yes':green, 'No':red, 'Not tested':gray), "Tonight's Plan" RICH_TEXT, "Question of the Day" RICH_TEXT, "Answer" RICH_TEXT, "Coach Note" RICH_TEXT, "Status" SELECT('Completed':green, 'Partial':yellow, 'Missed':red))

CREATE TABLE ("Session" TITLE, "Date" DATE, "Type" SELECT('Intake':purple, 'Weekly':blue, 'Monthly':green), "Sleep 7d" NUMBER, "Sleep 90d" NUMBER, "Health 7d" NUMBER, "Health 90d" NUMBER, "Focus 7d" NUMBER, "Focus 90d" NUMBER, "Partner 7d" NUMBER, "Partner 90d" NUMBER, "Family 7d" NUMBER, "Family 90d" NUMBER, "Nature 7d" NUMBER, "Nature 90d" NUMBER, "Week Recap" RICH_TEXT, "Habit Hit Rates" RICH_TEXT, "Deep Topic" RICH_TEXT, "Insight" RICH_TEXT, "Commitment" RICH_TEXT, "Check-in Changes" RICH_TEXT, "Status" SELECT('Completed':green, 'Partial':yellow, 'Missed':red))

CREATE TABLE ("Commitment" TITLE, "Status" SELECT('Active':green, 'Kept':blue, 'Dropped':gray), "Set" DATE, "Summary" RICH_TEXT, "Source" RICH_TEXT, "Last Updated" DATE)
```

Add habit columns later with `ADD COLUMN "<Name>" CHECKBOX`. Add area columns with `ADD COLUMN "Score <Area>" NUMBER` on Daily Check-ins and `"<Area> 7d" NUMBER; "<Area> 90d" NUMBER` on Weekly Sessions.

### Markdown layout (Google Drive, Obsidian, local folder)

```
Life Coaching/
  Life Coaching.md               (the home page)
  Coaching Frameworks.md
  Habits.md                      (one table, one row per habit)
  Commitments.md                 (one table)
  Daily Check-ins/
    2026-10-15 Thursday.md       (YAML frontmatter holds every property)
  Weekly Sessions/
    2026-10-18 Weekly.md
```

Daily Check-in file:

```markdown
---
date: 2026-10-15
status: Completed
score_sleep: 6
score_health: 5
score_focus: 7
score_partner: 6
score_family: 8
score_nature: 4
habits: {exercise: true, screens_off: false, bed_on_time: true, kept_my_cool: true}
habits_logged: true
commitment_held: Yes
---
Tonight's plan: ...
Question of the day: ...
Answer: ...
Coach note: ...
```

On Google Drive, create plain Markdown files (`text/markdown`), not Google Docs.

## Installing into a Cortex

Read the Cortex Map first and follow its rules (`cortex-spec.md`). The Map wins if it disagrees with this file.

1. Create the Life Coaching home under the Cortex parent, in the Cortex's backend.
2. Habits, Daily Check-ins, and Weekly Sessions are added collections. Habits gets Summary, Aliases, Status, Last Updated, and Source like any Cortex record, and a catalog. Daily Check-ins and Weekly Sessions are logs: no catalog, marked "log" on the Map.
3. If the Cortex already has a Commitments collection (Founder OS adds one), use it.
4. Register on the Map:
   - Collections: one row each for Habits, Daily Check-ins (log), Weekly Sessions (log), pointing to their locations.
   - Routing, Find it: "Life outside work: scores, habits, daily check-ins, weekly life sessions → Life Coaching (home), then Daily Check-ins, Habits, Weekly Sessions."
   - Routing, File it: "A life coaching check-in, habit, or weekly life session → Life Coaching and its collections."
5. Add an Ingest Log row: Source "Life Coach setup", Type Document, What Changed "Life Coaching collections added."
6. Keep the Map's budget. Don't add Glossary rows for habits.

Privacy: the Cortex may be shared with a team. If it is, ask before installing there, and offer a private location instead.

## Finding the home in a later session

Check in this order, using only the tools present. Stop at the first hit.

1. A link or path in the scheduled task prompt, the user's instructions, or their message.
2. The Cortex Map, if they have one: the Life Coaching entry.
3. Notion: a page titled "Life Coaching" that contains a "Daily Check-ins" database.
4. Google Drive: a "Life Coaching" folder with `Life Coaching.md`.
5. Connected folders: `Life Coaching/Life Coaching.md`.

Found more than one: ask which. Not found: offer Setup. Don't sweep the whole workspace.
