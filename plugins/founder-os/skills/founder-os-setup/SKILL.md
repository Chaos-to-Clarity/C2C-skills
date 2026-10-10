---
name: founder-os-setup
description: Sets up the Founder Operating System on the user's Cortex: Weekly Goals, Tasks, Reflections, and Commitments, registered on the Cortex Map, plus the daily, Monday, and Friday routines. Run once.
---

# Founder OS Setup

Build the weekly operating cycle on the user's Cortex: plan Monday, brief each morning, reflect Friday. Run once. If it already exists, confirm it and stop.

Read `references/cortex-spec.md` (how the Cortex works: Map, catalogs, records, protocols) and `references/founder-os.md` (what Founder OS adds). Use AskUserQuestion for choices (up to 4 per call, recommended option first).

## Step 1. Check the Cortex

Find and validate the Cortex Map (spec section 4).

- **No Map:** Founder OS reads the Cortex for priorities, people, and strategy. If the cortex-setup skill is installed, offer to run it first (recommended), then come back here. If it isn't, or the user wants Founder OS alone: ask where it should live and confirm access (spec section 3), ask which meeting notes, calendar, and email tools they use and test each, create the core collections and catalogs empty (spec sections 2 and 5), and write the Map (spec section 4). Tell them the Cortex can be filled later, and Founder OS gets sharper as it does.
- **Map already lists the Founder OS collections and they validate:** say it's set up, show where, and offer to change a setting or redo the routines (Step 6). Stop unless they pick one.
- **Existing planning databases** (Weekly Goals, Tasks, Reflections, Commitments, or close matches like "Weekly Planning", "To-dos", "Journal"): offer to adopt them. Map their field names in the Map's Field map, add only the missing fields, and never rename what they have.

## Step 2. Build the collections

In the Cortex's backend, create a "Founder OS" page or folder under the Cortex parent, then the four collections in `founder-os.md`, each with Summary, Aliases, Status, Last Updated, and Source:

1. Weekly Goals
2. Tasks, with Week as a relation to Weekly Goals
3. Reflections
4. Commitments, with Week as a relation to Weekly Goals

Notion: make Week two-way so a Weekly Goals record shows its Tasks and Commitments. Markdown: one folder per collection under `Founder OS/`.

## Step 3. Build the catalogs

One catalog and one Archive catalog per collection (spec section 5), with the key columns in `founder-os.md`. Empty, or filled from any adopted records.

## Step 4. Working rhythm

Ask in one AskUserQuestion call, defaults in parentheses:

- Work days (Monday to Friday)
- Working hours (9:00am to 5:00pm). Mention that fixed commitments like school pickup must be on their calendar to be protected.
- Deep-work block length for planning (2 hours)
- When the daily briefing should arrive (6:45am on work days)

## Step 5. Register on the Map

Edit the Cortex Map, changing only these parts:

- **Collections:** add the four rows, with catalog and location links
- **Routing:** add the Founder OS find and file rules from `founder-os.md`
- **Settings:** add the `founder_os.*` lines with the rhythm from Step 4
- **Freshness:** add the four collections to the record counts

Check the Map stays under 10,000 characters.

## Step 6. Schedule the routines

Offer all three, in the user's time zone:

| Routine | When | Prompt for the scheduled task |
| --- | --- | --- |
| Daily briefing | Each work day at the time from Step 4 | Run my daily-briefing skill. |
| Planning prep | Monday 7:00am | Run my weekly-planning skill in prep mode. |
| Retro prep | Friday 2:00pm | Run my weekly-retro skill in prep mode. |

Planning and retro are conversations, so their scheduled runs only prepare them: they read the week, write a prep note, and ping the user to finish when ready. A fully scheduled planning session would wait for answers and never finish.

If scheduling tools are available in this session, create the tasks the user picks. Otherwise give the steps to add each scheduled task with its prompt. If the Cortex lives in Obsidian or a local folder, scheduled runs need that computer on with the Claude desktop app open; say so.

## Step 7. Report

- Where Founder OS lives, with a link
- The four collections and how they connect
- Which routines are scheduled, and when
- Next step: "Say 'plan my week' to plan your first week."
