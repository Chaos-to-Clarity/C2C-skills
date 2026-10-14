# Setup

Build the system, schedule it, then offer the intake. Run once. If a home already exists, show its Settings in a short list and ask what to change; stop unless they pick something.

Use AskUserQuestion for choices when it's available (up to four questions per call, recommended option first). Otherwise number the options. Do discovery silently before asking: look for a Cortex Map, an existing Life Coaching home, an existing Commitments collection, and the user's time zone.

Setup map (show it at the start, mark progress as you go):

1. Welcome
2. Where it lives
3. Schedule
4. Build the schema
5. Create the scheduled task
6. Offer the intake

## Step 1. Welcome

Three or four lines: what this is (a life coach that checks in daily, runs a weekly session, and tracks which habits move which scores), what setup will do (about five minutes), and that the intake comes right after. Mention the book once: the coaching's base layer comes from *Above the Chaos* by Eric Weiss (abovethechaosbook.com).

## Step 2. Where it lives

Ask: **"Do you use a Cortex?"** If a Cortex Map turned up in discovery, say so and recommend it. Then follow `storage.md`:

- **Yes:** install into the Cortex ("Installing into a Cortex"). If the Cortex is shared with a team, ask whether they'd rather keep this private.
- **No:** ask where it should go (Notion, Google Drive, a folder on their computer, or another tool with a connector) and where inside it. Recommend a private location.

Check the location works with one real call before moving on.

## Step 3. Schedule

One AskUserQuestion call:

- **Daily check-in time.** Recommend late afternoon or early evening, before the evening routine, so the check-in can shape tonight (default 5:00pm). Advise against a time inside a screen-free window they want to protect (family time, bedtime).
- **Weekly session day.** Default Sunday. The weekly session replaces that day's daily check-in and takes about 30 minutes.
- **Weekends.** Full check-in (default), a light one-question version, or off.
- **Time zone.** Confirm the detected zone.

## Step 4. Build the schema

Create everything in `storage.md`, "What gets created":

1. The Life Coaching home page with every section, Settings filled in, `intake: not complete`.
2. Coaching Frameworks: a page or file with the full contents of `frameworks.md`.
3. Habits, Daily Check-ins (with the six default score columns), Weekly Sessions, and Commitments (reuse an existing one if found).
4. If installing into a Cortex: register the collections on the Map and log it.

Confirm each piece exists by reading it back once. Fix anything that failed before moving on.

## Step 5. Create the scheduled task

Do this right away, before the intake, so the system is live even if they stop here.

1. Check for an existing scheduled task with a similar name. If one exists, update it instead of creating a duplicate.
2. Create one recurring scheduled task that runs every day at the chosen time in their zone. The same task runs the daily check-in and, on the weekly day, the weekly session. Use the prompt in `scheduled-prompt.md`, filled in with the home's link or path. If weekends are off, schedule weekdays plus the weekly day only.
3. Turn on push notifications if the tool allows it, so the check-in reaches their phone.
4. Tell them in one line which approval setting the task got. If runs will stop to ask permission, say they can switch the task to automatic approval in its settings, or every check-in will stall waiting for them.
5. Record the task's name in the home's Settings.

If no scheduling tool is available, give them the prompt from `scheduled-prompt.md` and the plain steps to schedule it themselves, and say the coach only works if it reaches out on its own.

If they chose a local folder or Obsidian, remind them the scheduled runs need that computer on with the Claude desktop app open.

## Step 6. Offer the intake

Say what's built and when the first check-in arrives, in two lines. Then offer the intake:

> The system is live. The last piece is your intake: about 45 minutes, where we score each area, map the habits that build and damage it, and set your first commitment. It's what makes the check-ins useful. Start now? You can pause anytime and pick up where you left off.

- **Yes:** run `intake.md`.
- **Not now:** confirm `intake: not complete` in Settings. The first scheduled run will open with the intake instead of a check-in.

## Changing the schedule later

"Change my check-in time," "move my weekly session to Saturday," "turn off weekends": update the scheduled task (don't delete and recreate it), update Settings on the home, and confirm in one line.
