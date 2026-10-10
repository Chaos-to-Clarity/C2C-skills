# Storage: where the founder's work lives

Every completed canvas and the founder's PMF Profile are saved where the founder chooses during onboarding. That's what lets them pick up next session, build on earlier canvases, and see their scores move quarter to quarter.

## Choosing a place (onboarding)

Ask once, during onboarding. Use AskUserQuestion when available; otherwise number the options.

> **Where should I keep your Growth by Design work?** Your PMF Profile and every canvas you finish go there, so we can pick up next time and track your scores each quarter.

| Option | What gets created | How Claude reaches it |
| --- | --- | --- |
| **Cortex** (offer only if they have one: a Cortex Map turned up in Step 0, or they mention it) | A "Growth by Design" collection in their Cortex, registered in the Cortex Map | Whatever backend their Cortex uses |
| **Notion** | Ask where to put it: under a page they name, or a new private top-level page. Then a "Growth by Design" page with a "PMF Profile" page and a "Growth by Design Exercises" database | The Notion connector |
| **Google Drive** | A "Growth by Design" folder with `PMF Profile.md` and an `Exercises/` folder | The Google Drive connector |
| **A folder on my computer** (including Obsidian, Dropbox, iCloud, OneDrive) | The same folder layout as Google Drive, as Markdown files | A folder connected through the Claude desktop app |
| **Just this chat** | Nothing saved. Canvases are delivered in the chat, with a downloadable file on request | None |

Anything else with a connector (Airtable, Coda, Confluence): map the same structure as closely as it allows.

**Check that it works before moving on.** Make one real call: find or create the parent page or folder. If the tool isn't available, say which connection is missing in one line ("I can't reach your Notion from here. Connect Notion in your Claude settings, or pick another option.") and let them choose again. Don't pretend a save worked. If a save fails later, say so plainly and give them the content in the chat.

**Cortex.** Read the Cortex Map first and follow its rules for adding a collection: create "Growth by Design" as an added collection, register it in the Map's Collections and Routing (for example "Growth by Design canvases, PMF scores, and PMF plans go to Growth by Design"), and keep its catalog current. Each completed canvas is a record; the PMF Profile is a page in the same collection. If the Map's rules and this file disagree, the Map wins.

**Notion database properties:** Name (title), Number, Pillar (select: the ten pillars, Core framework, Operating System, Diagnostic), Chapter, Date, Status (Current, Superseded), Summary (one line).

**Markdown layout:**

```
Growth by Design/
  PMF Profile.md
  Exercises/
    01 PMF Scorecard (2026-10-12).md
    07 Persona Canvas (2026-10-14).md
    09 Customer Interview Tracker.md      (living log, updated in place)
```

On Google Drive, create plain Markdown files (`text/markdown`), not Google Docs, unless the founder asks for Docs.

**After setup**, tell them where it lives in one line, then suggest: "Tip: add a line to your Claude instructions or project: 'My Growth by Design PMF Profile is at [link or path].' Then any chat finds it instantly."

## Finding the profile in a later session

Check in this order, using only the tools present. Stop at the first hit.

0. A PMF Profile pasted or attached in this conversation (how chat-only founders carry their work between chats).
1. A link or path in the user's instructions, project, or message.
2. Their Cortex Map, if they have one: the Growth by Design entry in Collections.
3. Notion: a page titled "PMF Profile" under a page titled "Growth by Design".
4. Google Drive: `PMF Profile.md` in a "Growth by Design" folder.
5. Connected folders: `Growth by Design/PMF Profile.md`.

Found: read it and greet them as a returning founder (see SKILL.md). Found more than one: ask which. Not found: treat them as new and run onboarding. Keep this quick; don't sweep their whole workspace.

## Stages

Use this one list everywhere (onboarding, the profile, diagnose):

1. Idea, no product yet
2. Building or just launched an MVP
3. Early customers, still finding fit
4. Paying customers, but growth is hard
5. Scaling

## Before storage exists

A new founder may run diagnose, a quick pillar check, or an exercise before onboarding. Keep the results in the conversation. At the close, offer setup in one line ("Want me to save this? Pick where your work should live."). Once they choose, create the PMF Profile and write everything held so far into it. If they decline, treat it as chat-only.

## The PMF Profile

One page per company. Create it at the end of onboarding and keep it current.

```
# PMF Profile

Company: [name]
What we're building: [one or two sentences]
Who it's for: [their words]
Stage: [one of the five stages below]
Has the book: [yes / not yet]
Model: [B2B / B2C / both]
Team size: [n]
Biggest worry at the start: [their words]
Storage: [backend and location]
Started: [date] · Last updated: [date]

## Current scores
| Pillar | Score | Band | Scored on | Scored by |
| --- | --- | --- | --- | --- |
(ten rows; partial scores from quick pillar checks are marked "quick check")
Overall PMF Score: [x.x]

## Priority pillars
1. [Pillar] · why it's low: [hypothesis] · first action: [ ] · owner: [ ] · by: [date]
2. ...
Objectives and key results: [ ]

## Score history
| Pillar | [YYYY Qn] | [YYYY Qn] | Trend |
| --- | --- | --- | --- |

## Exercise log
| Date | # | Exercise | Pillar | Key output (one line) | Link |
| --- | --- | --- | --- | --- | --- |

## Open next moves
- [date] [action] (from #N)

## Assumptions to test
- [assumption] (from #N) · status: [open / confirmed / killed]
```

## Saving an exercise

At the close of every exercise:

1. **Save the canvas** as its own page or file, titled `NN Exercise Name (YYYY-MM-DD)`, with the full output, the coaching notes, assumptions, and next move. The footer stays on.
2. **Repeat runs** get a new dated file. Mark the older one Superseded (Notion and Cortex) but never delete it; the history is the point.
3. **Living logs** are the exception: #9 Customer Interview Tracker, #22 Channel Testing Log, #31 Customer Feedback Log, and #32 Weekly Metrics Scorecard are one file each, titled without a date, updated in place by adding rows.
4. **Update the PMF Profile:** add an Exercise log row, add the next move to Open next moves, add new assumptions, update scores after a scorecard, re-score, or quick pillar check, and set Last updated.
5. **Confirm in one line** where it went. No narration of the steps.

**Just this chat:** at each close, offer the canvas and the updated PMF Profile as downloadable files. Tell them once per session: "Next time, paste or attach your PMF Profile and we'll pick up where you left off." Offer to set up real storage once per session, no more.

## Reading earlier work

Before running an exercise, check the Exercise log for canvases it feeds from (each module lists "Feeds from"). Open the most recent one and reuse what's there: "Your Persona Canvas from October 14 says your segment is [x]. Still right?" Don't make the founder repeat themselves.
