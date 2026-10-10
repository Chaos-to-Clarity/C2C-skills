---
name: weekly-retro
description: Runs the user's Friday retrospective: scores the week, asks reflection questions one at a time, names recurring patterns, writes reflections and commitments, and feeds lessons to the Cortex.
---

# Weekly Retro

Run the user's weekly retrospective. Honest, not soft. One question at a time, wait for each answer.

Read `references/cortex-spec.md` (Map, catalogs, reading and writing protocols) and `references/founder-os.md` (the Founder OS collections and how to read them). Find and validate the Cortex Map (spec section 4). If the Map doesn't list the Founder OS collections, offer founder-os-setup and stop. Read through the Map and catalogs; never list whole databases. Every write updates the record and its catalog row together (spec section 7).

## Prep mode (scheduled runs)

When the prompt says "prep mode", or no one is there to answer:

1. Do Step 1 and Step 2.
2. Add the scorecard from Step 2 to this week's Weekly Goals body under "Retro prep". Don't change its Status.
3. Send the user a short message: the scorecard in a few lines, any pattern you can already see, and "Say 'run my retro' when you're ready."
4. Stop. Don't ask the reflection questions and don't write anything else.

## Step 1. Read context

Read all of this before saying anything.

**Founder OS**
- This week's Weekly Goals record: body (goals, success criteria) and Status
- Tasks linked to this week: Status, Priority, Due
- The last three or four Reflections (main and Archive catalogs): body and ratings, to spot recurring patterns
- Commitments with Status Active, especially last week's non-negotiable

**Gap check:** if task statuses look stale (most still To do or Doing with no updates), check the calendar and recent meeting notes to fill the picture before scoring.

**Cortex**
- Initiatives, Active: Status, Blocker, Next Action
- Decisions, Open

Know the score before presenting it.

## Step 2. Score the week

No spin.

```
WEEK SCORE

Goal 1: [name], [Done / Partial / Not started]
Goal 2: [name], [Done / Partial / Not started]

Tasks: X done, Y still open, Z not started
Commitment: [kept / dropped]
```

If check-ins didn't run and the picture is incomplete, say so and note what you filled in from the calendar and meeting notes.

## Step 3. Reflection questions

One at a time. Wait for the full answer before the next. Don't stack or summarize mid-sequence.

1. "Looking at those goals, what got done and what didn't?"
2. "For what you accomplished, what contributed most to your success?"
3. "For what you didn't finish, what actually got in your way?"
4. "What was the single biggest win this week?"
5. "What caused the most friction?"
6. "What did you procrastinate on, and why?"
7. "Which habit helped most this week, and which one held you back?"
8. "What's the most important thing you learned?"
9. "Rate the week 1 to 10 on business, health, family, and energy."
10. "What's one commitment you'll make to improve next week?"

## Step 4. Name patterns

Look across the last three or four Reflections and today's answers. Name what keeps recurring.

- A goal slipping several weeks: "[Goal] has come up unfinished for [N] weeks. That's not a bad week, that's a pattern. What's actually blocking it?"
- Repeated avoidance: "You've mentioned procrastinating on [X] for [N] weeks. That's not circumstance."
- Excuses (circumstances given as reasons for things in their control): "That sounds like an explanation, not a cause. What part was in your control?"

If nothing recurs, skip this step. Don't manufacture patterns. No soothing, no cheerleading.

## Step 5. Build the write list

Compile every change and show it before writing anything:

- **Reflections:** new record "Week of [Monday's date]", Week Start, Business, Health, Family, Energy. Body sections: Wins, Friction, Habits That Helped, Habits To Improve, Avoidance Patterns, Top Lesson.
- **Commitments:** last week's non-negotiable to Kept or Dropped; a new record from question 10 with Status Active, Set today, Week = this week's record.
- **Weekly Goals:** this week's record to Closed.
- **Cortex** (spec section 7): Decisions made or surfaced this week; Initiatives whose status, blocker, or next action shifted; any recurring pattern worth tracking, proposed as a Decision or a Standing Context note.

Ask: "Look right? I'll write all of this once you confirm." Wait.

## Step 6. Write

After approval, in this order:

1. Reflections record (if one exists for this week, update it instead of creating a second). Set Reflections more than four weeks old to Archived, moving their catalog rows to the Archive catalog
2. Commitments: find last week's by identity and set its Status; create the new one
3. Weekly Goals: this week's record to Closed
4. Cortex: Decisions with Status Decided, Date today, Source "Weekly Retro [date]"; Initiatives updated in place with Last Updated and Source. Never delete. Supersede only with an explicit yes.
5. Ingest Log: one row, Source "Weekly Retro [date]", Type Document, What Changed = one-line summary

## Step 7. Close

**Six-line summary**, factual:

1. Goals completed vs. attempted
2. Biggest win
3. Biggest friction
4. Pattern named, if any
5. Last week's commitment: kept or dropped
6. New commitment

**One thing to carry into Monday:** the single insight, unfinished priority, or pattern to break that should shape next week's planning. One specific sentence.

## Tone

- One question at a time. Stop after each.
- Name patterns and excuses plainly.
- Write nothing until the user approves the write list.
- The summary is six lines. Not a paragraph, not ten bullets.
