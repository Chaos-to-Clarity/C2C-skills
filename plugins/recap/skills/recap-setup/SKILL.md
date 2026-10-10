---
name: recap-setup
description: Sets up Recap, which turns every meeting into a branded recap email, tasks with time booked, follow-up drafts, booked meetings, and saved context. Run once; it also schedules the routine.
---

# Recap Setup

Set up Recap for the user: their tools, their branding, how much it does on its own, and the twice-daily routine. Run once. If a Recap Config already exists, show the current settings and offer to change any of them.

Read `references/recap-config.md` first. It defines every setting and the config format. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Do discovery silently before asking.

## Step 1. Check for an existing setup

Look for a page or file titled "Recap Config" (Notion, then Google Drive, then connected folders). If it exists and its links validate, show the settings in a short list and ask what to change. Stop unless they pick something.

Also look for a Cortex Map (see `references/cortex-spec.md`, section 4) and Founder OS collections on it. If found, Recap will use them for memory and tasks; tell the user in one line.

## Step 2. Connect the tools

Detect what's connected and pre-select it. Ask only about gaps.

| Role | Options |
| --- | --- |
| Meeting notes | Granola, Fireflies, Otter, Fathom, Zoom or Google Meet notes, Notion meeting notes, a notes folder |
| Email | Gmail, Outlook |
| Calendar | Google Calendar, Outlook, device calendar |
| Memory | Cortex (if found), a Notion page, a Google Drive folder, or none |
| Tasks | Founder OS Tasks (if found), a Notion database, another task app with a connector, or calendar blocks only |

Test each with one small read. For anything missing, search the connector registry and suggest it. Meeting notes, email, and calendar are required; memory and tasks are optional.

## Step 3. Branding

Recap emails go out under the user's name and brand. Ask in one round, with defaults:

- Name and title to sign with
- Company or brand name, tagline, and website (or none)
- Brand colors: a primary and an accent (defaults: navy `#1A4567` and coral `#CD5247`). If they have a Cortex design system, a brand page, or a website, offer to pull the colors from it.
- Logo: an image URL, or a text wordmark (default: brand name in bold)
- Footer line (default: "[Brand] | [website] | Confidential")
- What to call the email (default "Meeting Recap"; for example "Session Recap" for coaching, "Call Recap" for sales)

Optional: ask them to paste one recent email they wrote. Save three or four voice notes from it (tone, length, sign-off) so recaps sound like them.

## Step 4. Behavior

One AskUserQuestion call:

- **What it does on its own** (defaults are the recommended "Mixed" mode):
  - Recap emails: send (default) or draft
  - Follow-up emails the user promised: draft (default) or send
  - Meetings agreed in the call (follow-ups, coffee, intros): book and send the invite (default) or propose times by email draft
  - Small proactive tasks it can do itself (research, an agenda, a doc outline): do them (default) or just suggest
- **Who gets the recap:** external attendees with the user CC'd (default), every attendee, or only the user
- **Which meetings:** every meeting with notes (default), only a chosen folder or tag, or only meetings with external attendees

## Step 5. Time and places

Reuse what exists before asking. If Founder OS or handwritten-notes settings exist, copy work days, hours, and buffers from them.

- Work days and hours (Monday to Friday, 9:00am to 5:00pm). Mention that fixed commitments like school pickup must be on the calendar to be protected.
- Travel buffer around in-person meetings (30 minutes)
- Where they usually meet people in person: their neighborhood or city, and up to five favorite spots for coffee, lunch, or drinks. These are used when a call ends with "let's grab coffee." Leave blank to have Recap suggest places near their area.

## Step 6. Tracking

Recap must never process a meeting twice. Choose where it records what it has handled:

- If a Cortex exists: its Ingest Log.
- Otherwise: create a "Recap Log" next to the config (a Notion database or a Markdown file) with columns Meeting, Date, Note Link, Outcome (Sent, Drafted, Skipped, Blocked), What Was Done.

## Step 7. Save the config

Write the Recap Config page or file in the format in `references/recap-config.md`. Put it under the Cortex parent if there is one; add one line to the Cortex Map's Collections or Settings so other skills can find it. Otherwise, put it where the user chooses.

## Step 8. Send a test

Pick the most recent finished meeting with notes. Run the meeting-recap skill on it in **draft-only mode**, whatever the settings say: build the recap and save it as a draft to the user only, list the tasks, follow-ups, and bookings it would make, and change nothing else. Ask: "Does this look right?" Adjust branding or voice from their answer.

## Step 9. Schedule the routine

Offer to run Recap twice each work day, after the user's typical meeting blocks. Default 12:15pm and 3:15pm in their time zone; ask if their meetings run later. If scheduling tools are available, create the scheduled task with the prompt "Run my meeting-recap skill." Otherwise give the steps. Tell them the routine needs permission to act on its own (automatic approval) or every run will stop to ask.

## Step 10. Report

- Where the config lives, with a link
- Tools connected
- What runs automatically, and when
- How to change anything: "Say 'change my Recap settings.'"
