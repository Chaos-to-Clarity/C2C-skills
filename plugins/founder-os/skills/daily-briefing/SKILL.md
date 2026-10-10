---
name: daily-briefing
description: Produces the user's morning executive brief: schedule with Cortex context, meeting prep, open tasks, inbox flags, and whether today moves the week. Ends with a task check-in. Runs on a schedule.
---

# Daily Briefing

Produce the user's executive brief for today. Read every source, think, then write. Surface what matters and why. Scannable, no preamble. Built to run on a schedule before the user starts the day.

Read `references/cortex-spec.md` (Map, catalogs, reading and writing protocols) and `references/founder-os.md` (the Founder OS collections and how to read them). Find and validate the Cortex Map (spec section 4). If the Map doesn't list the Founder OS collections, still brief from calendar, meetings, and email, and note in one line that founder-os-setup adds goals and tasks. Read through the Map and catalogs; never list whole databases.

## Step 1. Pull every source in parallel

Pull everything before writing a word. If a source is unavailable, note it in one line and continue.

- **Calendar:** today's events with start times, durations, attendees.
- **Meeting notes:** meetings in the briefing look-back (default 24 hours). Open action items, decisions, and who is waiting on the user.
- **Email:** threads in the look-back that need a reply or a decision. Discard newsletters, receipts, automated mail, and FYI threads.
- **Cortex** (spec section 6): resolve every attendee and topic on today's calendar through the Glossary and the People and Initiatives catalogs, then open only those records and their linked initiatives. Read the Decisions catalog for Open items and the Strategy summary.
- **Founder OS** (`founder-os.md`, How Founder OS reads): this week's Weekly Goals record; open tasks due today or earlier, from the Tasks catalog.

Synthesize across all of them before writing.

## Step 2. Write the brief

This exact structure. No preamble, no section descriptions. If a section has no signal, leave it out rather than writing "nothing to report."

**TODAY AT A GLANCE**
One line: meeting load, open focus time, the single most important thing today.

**SCHEDULE**
- Time, event, one line of Cortex context: who the person is, what initiative it serves, what's open with them
- Flag tight transitions (under 15 minutes between events)
- Flag meetings with no prep material in the Cortex

**NEEDS PREP**
For each meeting that warrants it: what to review (the last meeting note, the open thread, the initiative's status), the one outcome to aim for, and any context that changes how to approach it.

**TODAY'S TASKS**
Open tasks due today or overdue, High priority first, then by Due date.
`[Priority] Task, due [date if overdue]`

**FROM YOUR MEETINGS**
`[Action], from [meeting], [who is waiting]`

**INBOX FLAGS**
Three to five emails that need the user today.
`[Sender], [what they want], [today / this week]`

**PRIORITIES CHECK**
Does today's schedule and task list move this week's goals and the strategy forward, or is today busy on the wrong things? Say it straight. If it's misaligned, name what's pulling focus and what's not getting time. One short paragraph.

**ONE MOVE**
The single highest-leverage action today, the one that makes the rest of the week easier, and one line on why it beats the rest.

## Step 3. Task check-in

Right after the brief, list the open tasks and ask in one message:
"Which of these are done? Which need a new due date? Any new tasks from today?"

When the user replies:

- Done: Status Done
- Rescheduled: update Due
- New: create a task with Status To do, Due, Priority, Goal (text), Week = this week's Weekly Goals record

Confirm in one line: "Updated: X done, Y rescheduled, Z added."

If there's no reply (common in scheduled runs), change nothing. Tomorrow's brief notes the check-in is still open.

## Step 4. Capture offer

If the brief surfaced something durable (a new decision, a shifted initiative, a commitment made, someone's context changed), offer in one line: "I noticed [X]. Want me to add it to your Cortex?"

On a yes, write it per spec section 7 (resolve identity, update in place or create, catalog row, Source "Daily Briefing [date]") and log it with Type Query Insight. Offer only.

## Output rules

- Scannable: headers, short lines, no padding.
- Cortex context is what makes the schedule useful. A meeting without context is just a name and a time.
- Priorities Check and One Move are where the judgment lives. Don't soften them.
