---
name: founder-os-setup
description: Sets up the Founder Operating System on top of the user's Cortex: Weekly Goals, Tasks, Reflections, and Commitments, plus the daily, Monday, and Friday routines. Run once.
---

# Founder OS Setup

Build the weekly operating cycle that runs on the user's Cortex: plan Monday, brief each morning, reflect Friday. Run once. If it already exists, confirm it and stop.

Read `references/cortex-store.md` first. Use AskUserQuestion for choices (up to 4 per call, recommended option first).

## Step 1. Check the Cortex

Load the Cortex Config (store reference, section 3).

- **No config:** Founder OS reads the Cortex for priorities, people, and strategy. If the cortex-setup skill is installed, offer to run it first (recommended), then come back here. If it isn't, or the user wants Founder OS alone, build a minimal Cortex yourself from the store reference: ask where it should live and confirm access (section 2), ask which meeting notes, calendar, and email tools they use and test each one, create the pages and collections in section 1 empty, write the Schema rules (section 6), and save the Cortex Config (section 3). Tell them the Cortex can be filled later and Founder OS gets sharper as it does.
- **Config has a `[founder_os]` section that validates:** tell the user it's already set up, show where, and offer to change a setting or redo the routines (Step 5). Stop unless they pick one.
- **Existing planning databases** (Weekly Goals, Tasks, Reflections, Commitments, or close matches like "Weekly Planning", "To-dos", "Journal"): offer to adopt them. Map their fields with `field_map`, add only the missing fields, and never rename what they have.

## Step 2. Build the four collections

In the same backend as the Cortex, create a "Founder OS" page or folder under the Cortex parent, then the four collections with the fields in section 1:

1. **Weekly Goals**
2. **Tasks**, with Week as a relation to Weekly Goals
3. **Reflections**
4. **Commitments**, with Week as a relation to Weekly Goals

Notion: make Week two-way so Weekly Goals shows its Tasks and Commitments. Markdown: create each folder under `Founder OS/` with an `_index.md` holding the header row (section 5).

## Step 3. Working rhythm

Ask in one AskUserQuestion call, defaults in parentheses:

- Work days (Monday to Friday)
- Working hours (9:00am to 5:00pm). Mention that fixed commitments like school pickup must be on their calendar to be protected.
- Deep-work block length for planning (2 hours)
- When the daily briefing should arrive (6:45am on work days)

## Step 4. Save to the config

Add the `[founder_os]` section to the Cortex Config with the collection locations and rhythm settings. Add one line per collection to the Overview, under a "Founder OS" heading.

## Step 5. Schedule the routines

Offer all three, in the user's time zone:

| Routine | When | Prompt for the scheduled task |
| --- | --- | --- |
| Daily briefing | Each work day at the time from Step 3 | Run my daily-briefing skill. |
| Planning prep | Monday 7:00am | Run my weekly-planning skill in prep mode. |
| Retro prep | Friday 2:00pm | Run my weekly-retro skill in prep mode. |

Planning and retro are conversations, so the scheduled runs only prepare them: they read the week, write a prep note, and notify the user to finish when ready. A fully scheduled planning session would sit waiting for answers and never finish.

If scheduling tools are available in this session, create the tasks after the user picks which ones. Otherwise give the steps to add each scheduled task with the prompt above. If the Cortex lives in Obsidian or a local folder, scheduled runs need that computer on with the Claude desktop app open; say so.

## Step 6. Report

- Where Founder OS lives, with a link
- The four collections and how they connect
- Which routines are scheduled, and when
- Next step: "Run weekly-planning to plan your first week."
