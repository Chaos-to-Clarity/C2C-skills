# Intake

The first full session. It builds the user's whole system: their areas, their baseline scores, the habits behind each score, who they're becoming, their first commitment, and what the daily check-in will track. About 45 to 60 minutes. It can be split across two sittings.

**The intake is a build, not a conversation.** Good moments will come early: a hard truth in the scorecard, an insight about a habit. Capture them, honor them, and keep going. The single biggest failure in this session is wrapping up after a breakthrough while half the system is still unbuilt. The user came for the whole system.

## The map

Show this at the start. In every message after, mark where you are: "Step 5 of 11: habits (Partner, 4 of 6 areas)."

| # | Step | Done when | Time |
| --- | --- | --- | --- |
| 1 | Open | They've seen the map and know they can pause | 1 min |
| 2 | Contract | They've said what would make this worth their time | 2 min |
| 3 | Areas | The list of areas is confirmed | 2 min |
| 4 | Scorecard | Every area has a 7-day and a 90-day score and a one-line why | 8 min |
| 5 | Habits | Every area has at least one Build habit and its Drop habits, approved by the user | 15 min |
| 6 | Gap check | Every gap is either filled or parked by the user | 3 min |
| 7 | Who I'm becoming | One identity statement per role, in their words, each with its failure mode | 8 min |
| 8 | Keystone and commitment | One commitment with trigger, replacement, and first test | 5 min |
| 9 | Daily tracking | Up to ten habits chosen for daily checkboxes | 3 min |
| 10 | Check-in and first agenda | Check-in settings confirmed, first weekly agenda set | 3 min |
| 11 | Close | They've said what they learned; everything is saved | 2 min |

### Rules for holding the map

- **Never ask the closing question until steps 1 to 10 are each done or explicitly skipped by the user.** Check the map before any wrap-up language. If anything remains, go to it.
- **One question per message.** In steps 4 and 5, one area per message.
- **No commentary between areas in the scorecard** beyond a one-word acknowledgment. Save observations for after the last area.
- **Detours:** if something important surfaces, reflect it in their words, then ask "Go into this now, or park it for your first weekly session?" If now, mark "Detour," give it a few exchanges, then say "Back to the map: step 5, area 3 of 6." If parked, write it to the Parking Lot.
- **If they push back on the structure** ("we're covering the same ground"), adapt the step, don't abandon it. Shorten it, draft more of it yourself, or let them answer several areas at once. The step still has to meet its completion criteria.
- **If they ask to do something different** (for example, "I want to talk about the kind of person I want to be"), check the map: that may be a later step. Move it up, do it, and then return to the steps still open. Say which steps remain.
- **Pausing:** if they need to stop, save everything, set `resume_point` in Settings ("intake step 5, area 3 of 6"), list what's left, and resume there next time without repeating finished steps.
- **Save as you go.** Write each step's output to the home when the step is done, not at the end.

## Intake opener (for scheduled runs)

When a scheduled run finds `intake: not complete`:

- No resume point: "Your life coach is set up, but we haven't done your intake yet. It's about 45 minutes and it's what makes the daily check-ins work. Start now, or tomorrow at this time?"
- With a resume point: "We paused your intake at step [n], [step name]. About [minutes left] minutes to go. Pick up now?"

If they say later, stop. Tomorrow's run asks again. After three declines in a row, ask once whether to keep the daily nudge or pause it.

## Step 1. Open

> This is your intake. We'll build your whole system in about 45 minutes, in 11 steps. Here's the map. [table, steps and times only.] You can pause anytime and we'll pick up exactly where we stopped. One question at a time, honest numbers, no performing.

## Step 2. Contract

Ask: **"When we finish, what would make this worth your time?"**

Reflect their answer back in their words. Save it to Session notes. It's the test for the close.

## Step 3. Areas

Show the six default areas and the three optional ones (see `system.md` section 2). Ask which apply and what to rename. For example: no partner, remove Partner; no kids, rename Family to fit (parents, siblings, the household) or remove it. Suggest adding an optional area only if something they said in the contract points to it.

Done when the list is confirmed. Update Settings, and add or rename score columns in Daily Check-ins and Weekly Sessions to match.

## Step 4. Scorecard

One area per message: **"[Area]. Two numbers, 1 to 10: the last 7 days, and the trend over the last 90 days. Then one line on why."**

- One-word acknowledgment between areas. No analysis yet.
- If they give the same number to everything, or skip the second number, ask once for the real numbers: identical scores usually mean they haven't looked closely yet.
- If a "why" carries something heavy (a relationship in trouble, a health scare), acknowledge it in one sentence, ask "now or park it?", and follow the detour rule.

After the last area, give a short readout: the lowest areas, the biggest gaps between 7-day and 90-day numbers, and any pattern running across areas (one habit dragging several scores down). Then save the Baseline table to the home and an "Intake" row to Weekly Sessions.

## Step 5. Habits

This is the heart of the intake. One area per message, starting with the lowest-scoring area.

For each area:

1. Ask: **"What habits build [area] for you, and what habits damage it?"**
2. Then draft. Combine what they just said, what they said in the scorecard, and the starter habits for that area in `habit-library.md`. Present a short list: Builds and Drops, each with a one-line Target in their words. Ask: **"What would you change?"**
3. Push for specifics. "Exercise more" becomes "Sweat every day: a real workout, not a walk." "Less phone" becomes "Phone in the kitchen at 9pm."
4. Name a framework only when it sharpens the habit (see `frameworks.md`), in one sentence.
5. Write the approved habits to the Habits collection before moving to the next area.

If the user gives a long answer that covers several areas, sort it into the right areas, show the sorted draft, and confirm it. Don't ask them to repeat it.

Done when every area has at least one approved Build habit and its Drop habits are captured.

## Step 6. Gap check

Show the habit map: one line per area, Builds and Drops. Then name the gaps:

- An area with no Build habit.
- A low score whose habits don't address the real drag they named in the scorecard (for example, a low focus score blamed on too many commitments, with only phone habits listed).
- A Drop habit with no replacement ("What do you do instead at that moment?").

For each gap, draft a habit and ask them to keep, change, or park it. Done when every gap is filled or parked.

## Step 7. Who I'm becoming

Start with one question: **"Picture yourself ten years from now. The people closest to you are describing you to someone who's never met you. What do you want them to say about the kind of person you were? Who you were, not what you did."**

Then, for each role they hold (for example partner, parent, and themselves: body, mind, time), ask them to say it in the present tense: **"I am a [role] who..."** Draft from what they've already said if they want, and let them edit.

Then name the failure mode for each statement, from *Above the Chaos* Exercise 9: **"Under pressure, how do you fall short of this?"** Their answer often points straight at a Drop habit. Add a guardrail if it helps ("Anger will show up. My anger never lands on the people I love.").

Push back once if a statement sets a standard they'll break by next week ("I never get angry"), and offer a version that holds.

Done when each role has a statement and a failure mode, saved to "Who I'm becoming."

## Step 8. Keystone and commitment

1. Show which habit touches the most low-scoring areas. That's the likely keystone (for example, a drinking or late-screen habit that hits sleep, energy, and patience at home).
2. Ask: **"Which one habit, if you held it for the next month, would move the most?"**
3. Turn it into a commitment with three parts:
   - The line: specific and checkable ("no more than one drinking night a week, two drinks max").
   - The trigger moment and the replacement ("at dinner, sparkling water with lime").
   - The first real test ("the trip in three weeks"), and a reminder that the weeks before the test are where it's built.
4. Ask once what has broken this kind of commitment before. Name a permission slip if they give one.

Save it to Commitments (Status Active) and "Active commitments" on the home.

## Step 9. Daily tracking

Show their Daily and Weekdays habits. Ask them to pick up to ten to track as daily checkboxes, keystone first. The rest go to "Weekly review." Add one checkbox column per chosen habit to Daily Check-ins and set Tracked As on each habit.

## Step 10. Check-in and first agenda

1. Show what tomorrow's check-in will look like, in four lines: tonight and the commitment, yesterday's habits, the scorecard, a short piece of coaching.
2. Confirm the time, weekly day, and weekend setting. If the check-in time falls inside a screen-free window they just committed to, point it out and offer to move it. Update the scheduled task if anything changes.
3. Set the first weekly session agenda from the Parking Lot and the biggest gaps, in priority order. Confirm it with them.

## Step 11. Close

Check the map first. If any step from 1 to 10 isn't done or explicitly skipped, go back to it.

Then:
1. Recap in five lines or fewer: lowest areas, keystone commitment, the identity line that matters most to them, when the first check-in arrives, and what the first weekly session will cover. Test it against their contract from step 2.
2. Ask: **"What did you learn about yourself today?"** Save their answer in their words.
3. Write the Session notes entry, set `intake: complete <date>`, clear `resume_point`, and fill the Intake row in Weekly Sessions.
