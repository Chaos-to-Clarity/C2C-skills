---
name: cortex-update
description: Keeps the user's Cortex current. Scans recent meeting notes, email, and calendar, then updates people, initiatives, decisions, and context in place. Built to run weekly on a schedule.
---

# Cortex Update

Scan every connected source from the look-back window and keep the Cortex current. Safe to repeat: the Ingest Log guarantees each source is processed once across runs. For a single document, use add-to-cortex instead.

Read `references/cortex-store.md` first, then load the Cortex Config (section 3). If there's no config, say so and stop; in a scheduled run, there's no one to run setup, so just report it.

## Settings from the config

- `update.lookback_days` (default 7)
- `update.approval`: `autonomous` applies edits and reports. `required` shows the edit list and waits for approval.
- Scheduled runs must use `autonomous`. A run waiting for an approval nobody gives never finishes. If this is a scheduled run and the config says `required`, build the edit list, write nothing, and report that approval is needed.

## Step 1. Read the rules and the map

Read the Cortex Schema page and the Overview. Note any collections the user added; route to them too.

## Step 2. Pull new sources

Pull in parallel for the look-back window:

| Source | What to pull |
| --- | --- |
| Meeting notes | Every meeting in the window |
| Email | Threads with strategic signal: new relationships, decisions, initiative changes. Skip routine operations, newsletters, receipts, and automated mail |
| Calendar | Events that signal a new relationship or commitment |

Then check the Ingest Log and drop every source whose title or ID is already there. Work only the new ones. If a source is unavailable, note it in one line and continue.

## Step 3. Extract durable signal

For each new source, keep only what stays true for weeks or months.

| What changed | Goes to |
| --- | --- |
| A person they now deal with, or whose role or context shifted | People |
| An initiative that started, shifted, stalled, or finished | Initiatives |
| A decision made, or a question that opened or closed | Decisions |
| A durable fact about the business or their role | Standing Context |

Write in the user's words. Condense.

## Step 4. Build the edit list

Find each existing record by identity first.

**People** (match on Name)
- New: create with Status Active, Last Updated today, Source = the meeting or email title.
- Context changed: update in place, refresh Last Updated and Source.
- Relationship paused or ended: set Status to Dormant or Archived, update Context. Never delete.

**Initiatives** (match on Name)
- New: create with Status Active, plus Next Action and Blocker if known.
- Shifted: update Blocker, Next Action, or Status in place.
- Finished or dropped: set Status to Done or Dropped. Never delete.

**Decisions** (match on Title)
- New: create with Status Decided or Open, Date today.
- Reversed or replaced: set the old record to Reversed or Superseded, create the new one, set Supersedes to the old title.

**Standing Context**: surgical edits to specific facts. Never rewrite the page.

**New category**: if content clearly calls for a collection that doesn't exist, add it to the report as a proposal and don't create it, even in autonomous mode.

## Step 5. Approval gate

- `required`: show every create, update, and supersede. Write nothing until the user approves.
- `autonomous`: go to Step 6.

## Step 6. Apply

Re-read each record immediately before changing it. Then write. Notion: update only the changed fields. Markdown: rewrite the record and its `_index.md` row together.

If the week shifted the big picture, refresh the Synthesis paragraph at the top of the Overview.

## Step 7. Log every source processed

One Ingest Log row per source worked: Source = meeting title, email subject, or event name; Type = Meeting Notes, Email, or Document; Date Ingested today; What Changed = one line. Skipped sources get no row.

## Step 8. Report

A short table or a tight paragraph:

- Sources scanned, and sources skipped as already ingested
- Records created, updated in place, superseded
- Flags: thin data, ambiguous items, new-collection proposals waiting for a yes
- Sources that were unavailable
