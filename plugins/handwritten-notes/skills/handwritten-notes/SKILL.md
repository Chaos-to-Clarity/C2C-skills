---
name: "handwritten-notes"
description: "Use when the user sends a photo of handwritten notes: transcribe it, file checkbox tasks in their task database and book calendar time, and file notes. Runs a one-time setup if needed."
---

# Handwritten Notes to Tasks, Notes, and Calendar

The user photographs a sheet of handwritten notes. Transcribe it, turn checkbox items into scheduled tasks, file everything else as notes, and book calendar time. Then report back briefly.

This skill is portable. It never assumes a specific workspace. All workspace details live in a config page in the user's own knowledge store. If the config is missing or broken, run Setup first.

## Step 0. Load config or run Setup

1. Load tools with ToolSearch: the knowledge store (Notion first) and the calendar (Google Calendar, Outlook, or the device calendar tools).
2. Search the store for a page titled exactly "Handwritten Notes Config". Read the `text` block on it.
3. Validate: fetch each database it names. If all fetch and the calendar is reachable, skip to Step 1.
4. If the page is missing, run full Setup. If one item fails (a database was deleted or moved, a connector was removed), rerun only the matching Setup part, update the config, and continue.

If the user's photo arrives before setup is complete, keep the photo, finish Setup, then process it. Never lose the photo's contents: if setup is abandoned, still give the transcription in chat.

## Setup (first run only)

Keep it short. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Do the discovery silently before asking.

### A. Connectors

- **Knowledge store.** Notion is the default. If no Notion tools are present, search the connector registry (SearchMcpRegistry with ["notion", "notes", "tasks"]) and suggest it with SuggestConnectors. If the user prefers another connected app for tasks and notes (Todoist, Asana, Google Drive, and so on), use it and map the same fields as closely as it allows. If the user connects nothing, offer to keep going with calendar only and give notes back in chat.
- **Calendar.** Use whatever calendar tools are present (Google Calendar connector, Outlook connector, or the device calendar tools). If none, suggest a connector the same way. Without a calendar, tasks still get filed, unscheduled, and the report says so.
- After the user connects something, tell them it may take a new message for the tools to appear, then continue.

### B. Find or build the place to store things

1. **Look for an existing system.** Search the store for pages and databases with names like Cortex, Brain, Second Brain, Overview, Tasks, To-do, Notes, People, Projects, Initiatives, Clients. A strong match is a parent page holding a Tasks database plus People or Projects databases.
2. **If you find one, confirm it.** Ask: "I found [page name] with [Tasks, People, Projects]. Use it?" Options: use it (recommended), pick a different page, create a new setup.
3. **If you find nothing, ask where to store things.** Options:
   - Create a new page "Notes and Tasks" with Tasks and Notes databases (recommended)
   - Use an existing page or database I name
   - Use a different app
4. **Tasks database.**
   - Existing: fetch its schema and map these roles to its properties: title, due date, status (with its open and done values), priority (if any), context or project (if any). Only these are required: title and status. Then add the properties this skill needs that are missing, after telling the user in one line: Scheduled (date), Est. Minutes (number), Calendar Event (url).
   - New: create Tasks with Task (title), Due (date), Scheduled (date), Est. Minutes (number), Priority (High, Medium, Low), Status (To do, Doing, Done), Goal (text), Calendar Event (url).
5. **Notes database.** Use an existing notes database if the user has one and it has a title and a date field; add Captured (date) if missing. Otherwise create Notes under the chosen parent page with Name (title), Captured (date), Type (General, Person, Initiative, Meeting, Idea), Status (Active, Archived), Last Updated (date), Source (text), a two-way relation to Tasks (shows on Tasks as Source Note), and two-way relations to the People and Projects databases if they exist (each shows on those rows as Notes).
6. **Optional links.** Record the People database, the Projects or Initiatives database, a weekly planning database (with its week-start field), an ingest or activity log, and an overview or schema page if any exist. None are required.
7. If the parent has an overview or index page, add one line there describing the Notes database.

### C. Scheduling preferences

Ask in one AskUserQuestion call. Defaults in parentheses:
- Working hours (9:00am to 5:00pm). Mention that school runs, gym, and other fixed commitments must be on the calendar to be protected.
- Work days (Monday to Friday)
- Travel buffer around in-person meetings (30 minutes)
- Booking mode: book automatically and report (recommended), or propose times and wait for OK

Take the calendar ID and time zone from the calendar itself (the primary calendar). Ask only if there are several plausible calendars.

### D. Save the config

Create a page titled "Handwritten Notes Config" under the chosen parent page (or in the chosen app). Its body is one `text` code block in this format, with real values:

```text
config_version: 1
store: Notion
brain_page: <url>
overview_page: <url or none>
schema_page: <url or none>

tasks_db: <collection url>
tasks.title: <property>
tasks.due: <property or none>
tasks.scheduled: <property>
tasks.estimate: <property>
tasks.priority: <property (values) or none>
tasks.status: <property (open=<value>, done=<value>)>
tasks.context: <property or none>
tasks.week: <property or none>
tasks.source_note: <property or none>
tasks.calendar_link: <property>

notes_db: <collection url>
notes.title: <property>
notes.captured: <property>
notes.type: <property (values) or none>
notes.people: <property or none>
notes.projects: <property or none>
notes.tasks: <property or none>
notes.status: <property (value) or none>
notes.last_updated: <property or none>
notes.source: <property or none>

people_db: <collection url or none>
projects_db: <collection url or none>
weeks_db: <collection url (week-start field) or none>
ingest_log_db: <collection url (fields) or none>

calendar_provider: <Google Calendar | Outlook | Device>
calendar_id: <id>
time_zone: <IANA zone>
work_days: Mon-Fri
work_hours: 09:00-17:00
in_person_buffer_minutes: 30
default_block_minutes: 30
max_block_minutes: 90
min_lead_minutes: 30
booking_mode: auto
```

Tell the user in one line that setup is done and they can edit the config page to change any setting. Then process the photo.

## Rules for every write

- If `schema_page` is set, read it once and follow its rules.
- Identity first: before creating a task or note, look for an existing open row with the same title and update it instead of duplicating.
- Fill `last_updated` and `source` wherever those properties exist.
- Any property mapped to `none` is skipped silently.

## Step 1. Capture time

Set Captured (date and time, in `time_zone`) in this order:
1. Photo EXIF DateTimeOriginal, if the image file is readable in the workspace (Python/PIL or exiftool).
2. Otherwise the time the message was sent (use the current-time tool).
3. If the user wrote a date on the page, use that date and keep the time from 1 or 2.

Relative dates on the page ("Tuesday", "next week", "EOW") resolve against the Captured date, to the nearest future occurrence.

## Step 2. Transcribe

- Keep the user's structure (headings, bullets, indentation, arrows).
- Fix obvious spelling only. Do not rewrite their phrasing.
- Mark unreadable words `[illegible]` and best guesses `[word?]`.
- Skip crossed-out text.
- If `people_db` or `projects_db` is set, resolve near-matches in handwriting against their Active rows ("Sam R" to "Sam Rivera").

## Step 3. Classify each item

- **Task**: a square or checkbox next to it AND it reads as an action. Empty box means open. Checked or X'd box means done.
- **Note**: everything else.
- **Edge cases** (keep as notes, flag in the report, do not book):
  - An action with no box ("call Sam"): "possible task, not booked".
  - A box next to something that is not an action (a label, a name).
- **Task-related notes**: sub-bullets, arrows, or lines that clearly explain a task. These go in that task's page body, not in a separate note.

## Step 4. Tasks

**Duplicate check.** If `ingest_log_db` is set, look for an entry with the same Captured timestamp; otherwise look in `notes_db` and `tasks_db` for rows created from the same Captured timestamp. If found, stop and tell the user this photo was already processed.

For each task:

**Title.** A clean imperative phrase from the user's words with the date phrase removed. "create workshop slide deck by Tuesday" becomes "Create workshop slide deck".

**Existing task.** If an open task with the same or near-identical title exists, update it (due date, notes). Do not book a second block if it already has a Scheduled time.

**Due date.** A written date or day is the due date. The work block must finish before the due day starts ("by Tuesday" means book Monday or earlier). A written time ("by Tue 2pm") means the block must end before that time instead.

**Estimate.** Start from `default_block_minutes` (30). Judge by the work:
- 30: email, call, quick reply, send, review a short doc, book, pay, ask, intro
- 60: draft a post or newsletter, prep for a meeting, outline, research, a short proposal, set up a tool
- 90: slide deck, workshop design, long-form writing, a full proposal, a framework, anything multi-part
- Over `max_block_minutes`: split into blocks of that size named "(Part 1 of N)", all before the due date
- A written duration ("1 hr", "2h") wins.

**Priority and window when no date is written.**
- High (time-sensitive, someone waiting, money on the line, "ASAP", "!", underlined): book within 2 work days
- Medium (default): within 5 work days
- Low ("someday", "maybe", nice-to-have): within 10 work days
- A written due date within 3 work days also makes it High.

**Booking rules.**
1. Pull events from `calendar_id` from now through the due date (or the window end). Every timed event counts as busy, including earlier task blocks. Ignore declined events and events marked Free. All-day events block only if they are out-of-office, travel, or a full-day event.
2. Book only on `work_days` within `work_hours`, in `time_zone`. Never start sooner than `min_lead_minutes` from now.
3. In-person buffer: block `in_person_buffer_minutes` before and after any in-person event. An event is in-person when its location is a physical place (address, venue, restaurant, office, cafe) and not a video link (Zoom, Meet, Teams, Webex), phone number, or blank. Titles like "lunch", "coffee", "dinner", "drinks", "at [place]", "pickup", "drop off" also count.
4. Start on :00 or :30. Pick the earliest slot that fits. For 90-minute work, prefer a morning slot when one exists before the due date.
5. With several tasks from one photo, schedule by due date, then priority. Add each new block to the busy list before placing the next one, so blocks never overlap.
6. If nothing fits before the due date: book the best slot on the latest work day before it, even if shorter than the estimate (minimum 30 minutes), and flag it. If that fails, book the earliest slot on the due day before noon and flag it as late.
7. If `booking_mode` is `propose`, list the proposed slots and wait for OK before creating events.

**Create the calendar event.** Title = task title. Description = link to the task row, the estimate, the due date, and any task-related notes. Show as busy. Default reminders.

**Write the task row** using the property map: title, due (if written), scheduled (start and end of the block; for split tasks the first block, with all blocks listed in the page body), estimate, priority, status (open value; done value for a checked box, with no calendar block), context (the related project or person in a few words, if obvious), week (the weeks_db row whose week start matches the scheduled date's week, if set), source note (if a note row is created), calendar link. Page body: task-related notes under "Notes from page".

## Step 5. Notes

Create one note row for the freestanding notes on the page. If the page holds only tasks and their related notes, skip it. If the page clearly holds two unrelated topics, create one row per topic.

- **Context.** If `people_db` or `projects_db` is set, link the people and projects named or clearly implied. The relation makes the note show on those rows, so do not edit People or Projects rows directly.
- **Type** (if mapped). Person, Initiative (a project), Meeting, Idea (a framework, concept, or content idea), or General.
- **Title.** "[Topic], [Mon D YYYY]", for example "Pricing ideas, Oct 10 2026". With no clear topic: "Notes, Oct 10 2026 3:42pm".
- **Properties.** Captured (date and time), status Active, last updated today, source "Handwritten photo".
- **Body.** First line: "Captured [weekday, Mon D YYYY, h:mma]". Then the transcription under "Transcription". Then links to any tasks from the same page under "Tasks from this page".
- Link every task created from the same photo.

## Step 6. Log

If `ingest_log_db` is set, add an entry: source "Handwritten note, [Captured datetime]", type Document (or the closest option), date today, what changed = counts plus titles ("3 tasks booked, 1 note linked to Sam Rivera").

## Step 7. Report back

Short, phone-friendly, no preamble:

**Tasks**
- [Title], [est] min, [Day Mon D, h:mm to h:mm], due [Day] (or "no due date, [Priority]")

**Notes**
- [Title], linked to [people/projects] (or "General")

**Check these** (only if any)
- Illegible or guessed words, assumed dates, possible tasks not booked, blocks that are short or land on the due day

End with one line offering to move any block.

## Example

Photo line: "[ ] create workshop slide deck by Tuesday", with a sub-bullet "use Sam's outline", captured Saturday.
- Task: "Create workshop slide deck", due Tuesday, 90 minutes, High (due within 3 work days).
- Book the first open 90-minute work-hours slot on Monday, preferring the morning, respecting in-person buffers.
- "use Sam's outline" goes in the task body and the event description, not in a separate note.