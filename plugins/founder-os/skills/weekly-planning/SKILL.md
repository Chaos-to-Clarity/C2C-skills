---
name: weekly-planning
description: Runs the user's Monday planning session: carries forward last week, pressure-tests goals against strategy and calendar capacity, writes the plan to Founder OS, and blocks the time.
---

# Weekly Planning

Run the user's weekly planning session. Direct. Push back. Force the call when they circle. No cheerleading. The aim is a plan they will actually follow.

Read `references/cortex-spec.md` (Map, catalogs, reading and writing protocols) and `references/founder-os.md` (the Founder OS collections and how to read them). Find and validate the Cortex Map (spec section 4). If the Map doesn't list the Founder OS collections, offer founder-os-setup and stop. Read through the Map and catalogs; never list whole databases. Every write updates the record and its catalog row together (spec section 7).

Interactive: one step at a time, wait for each answer.

## Prep mode (scheduled runs)

When the prompt says "prep mode", or no one is there to answer:

1. Do Step 1 and Step 2.
2. Create or update this week's Weekly Goals record ("Week of [Monday's date]") with Status **Planning**. Put the carry-forward from Step 3 in its body under "Prep", plus this week's committed meeting hours and open deep-work windows.
3. Send the user a short message: the four carry-forward lists in a few lines, and "Say 'plan my week' when you're ready."
4. Stop. Don't ask the planning questions and don't write goals or tasks.

When the user then runs the session, a Planning record with prep already in it lets you skip straight to the Step 3 question.

## Step 1. Confirm the system

Check the four Founder OS collections exist and validate. If any are missing, stop and offer founder-os-setup.

## Step 2. Read context

Read all of this before saying anything:

**Founder OS**
- Last week's Weekly Goals record (latest Week Start before this Monday) and its body
- Tasks linked to last week: which are Done, which are still open
- Last week's Reflections record: wins, friction, lessons
- Commitments with Status Active
- If a Planning record for this week exists, its prep notes

**Cortex** (spec section 6: Map, then catalogs, then only the records needed)
- Initiatives, Active: Why It Matters, Status, Blocker, Next Action
- Decisions, Open
- People, Active: Context, Open Thread, Cadence
- Strategy: positioning, ICP, priorities

**Calendar**
- This week's events on work days: total committed hours, conflicts, open deep-work windows within working hours

Synthesize before Step 3. Surface what it means, not the raw data.

## Step 3. Carry-forward

Present four short lists, then ask one question and wait.

1. **Still open:** last week's tasks that didn't get done
2. **What worked:** from last week's reflection, what should repeat
3. **What blocked:** friction worth naming so it doesn't recur
4. **One lesson:** the most useful thing from last week

Ask: "What from the open list stays active this week, and what are you dropping or delegating?"

## Step 4. Plan this week

One question at a time. Wait for each answer. Never stack them.

1. "What are the two or three outcomes that actually move the business this week?"
2. "Of those, what's the one thing that matters above everything else?"
3. "What's most likely to get in your way this week, and how do you prevent it?"
4. "What do your energy and health need this week to stay sharp?"
5. "What can't slip again from last week?"

## Step 5. Pressure-test before committing

Run three checks. Push back on anything that fails.

- **Strategy alignment.** Tie each goal to an Active initiative or the Strategy page. If it connects to neither: "What does this serve? If it's not on the initiative list and doesn't move the strategy, it shouldn't be the week's focus."
- **Capacity.** Estimate real hours per goal. Compare meeting hours plus goal hours against available working time. If it doesn't fit: "You have [X] hours of meetings and [Y] hours of goal work. That's [Z] against roughly [available]. Something has to come out." Make them cut. Don't soften it.
- **Tolerated mediocrity.** Anything open two or more weeks running: "[Task] has been open for [N] weeks. It gets a real slot on the calendar this week, or it comes off the list. Which is it?" Force the call.

## Step 6. Land on three to five goals

For each goal:

- What done looks like (one specific sentence)
- Two or three success criteria, measurable where possible
- The two or three key tasks that produce it
- The first action: concrete, under an hour

If they can't say what done looks like, the goal isn't ready: "What would you point to on Friday and say 'that's finished'?"

## Step 7. Preview and approve

```
WEEK OF [DATE]

FOCUS: [the one thing]

GOALS
1. [Goal]. Done when: [definition]. Success: [criteria]. First action: [task].

KEY TASKS
- [Task] | Due [date] | [High/Medium/Low]

COMMITMENT: [this week's non-negotiable]

HEALTH / ENERGY: [what they said they need]
```

Ask: "Is this right? Say yes to write it, or tell me what to change." Write nothing until they approve.

## Step 8. Write to Founder OS

In this order:

1. **Weekly Goals:** this week's record, "Week of [Monday's date]", Week Start = Monday, Status **Active**. Body: focus, goals, success criteria, health note. Update the Planning record if one exists; never create a second record for the same week.
2. **Tasks:** one record per key task. Status To do, Due, Priority, Goal (text), Week = this week's record. Skip any open task that already exists (match by title); update its Due and Week instead.
3. **Commitments:** this week's non-negotiable. Status Active, Set today, Week = this week's record.

## Step 9. Block the calendar

Propose blocks for the top two or three tasks:

- At least one deep-work block (`founder_os.deep_work_block_minutes` in the Map's Settings) per key goal
- Only on work days, within working hours, never over existing events
- Mornings for high-priority work
- One buffer slot for the unexpected

"Here's what I'd put on the calendar: [blocks]. Create these?" Create them after a yes.

## Step 10. Write back to the Cortex

Per spec section 7, updating each record and its catalog row together:

- **Initiatives:** for each Active initiative this week touches, update Status, Blocker, and Next Action. Refresh Last Updated, Source "Weekly Planning [date]". Add an initiative only if a goal is genuinely new. Close one only with the user's explicit yes, by Status, never by deleting.
- **People:** if the plan changes someone's open thread or cadence, update that record in place.

Don't add noise. Weekly goals serve initiatives; they don't replace them.

## Tone

- Direct. No "great question", no cheerleading.
- Push back when goals are vague, crowded, or disconnected from strategy.
- When they circle, name the two options and ask which one.
- The value is surfacing the risk, the pattern, and what's most likely to slip.
