---
name: ask-cortex
description: Answers questions about the user's world from their Cortex plus live meetings, calendar, and email. Lookups, meeting prep, and synthesis like what's at risk this week or where they're overcommitted.
---

# Ask Cortex

Answer questions about the user's business, people, priorities, and schedule. The Cortex is the durable layer; meeting notes, calendar, and email are the live layer. Connect them. Don't just retrieve.

Read `references/cortex-store.md` first, then load the Cortex Config (section 3). If there's no config, answer from live sources where you can, say the Cortex isn't set up, and offer cortex-setup.

If the user hasn't asked a question yet, ask what they want to know.

## Where to look

| Question | Cortex | Live supplement |
| --- | --- | --- |
| Positioning, ICP, brand, GTM | Strategy page | |
| A person: role, context, history | People | Recent meetings and threads with them |
| An initiative: status, blocker, next action | Initiatives | Recent mentions, upcoming events |
| A decision: what and why | Decisions | |
| Risk or overcommitment this week | Initiatives, People | Upcoming calendar, open meeting actions |
| Meeting prep | The person's record and linked initiatives | Their last meeting, the next one on the calendar |

## Step 1. Read the Overview

It shows what exists, including collections the user added. Open only what the question needs, filtered to Active. Never load the whole Cortex.

## Step 2. Pull from the Cortex

- **People:** the person or people named. Role, Context, Cadence, Open Thread, Status, Last Updated.
- **Initiatives:** Active. Why It Matters, Status, Blocker, Next Action.
- **Decisions:** Open or Decided. Reasoning, Status, Date.
- **Strategy:** for positioning, ICP, GTM, and brand questions.
- **Standing Context:** for durable facts about the business or their role.

## Step 3. Pull live data when it's time-sensitive

- Meeting notes: the last one to three meetings with the person or on the topic
- Calendar: relevant events in the next 7 to 14 days
- Email: recent threads with the person or on the topic

If a source is unavailable, note it in one line and continue.

## Step 4. Answer

Answer first, then the support. Say where each part came from and how recent it is ("People record, updated Mar 3" or "meeting on Mar 10").

When a question touches strategy, people, and schedule, pull from each and synthesize. Surface the implication behind the question, the pattern no single source shows, and where live data contradicts the Cortex.

By type:

- **Lookup:** one direct answer, the source, one line of context if useful.
- **Prep:** (1) where things stand, from the Cortex; (2) what the last meeting or thread showed; (3) what to raise, given their priorities and open threads.
- **Synthesis:** the pattern or risk, the evidence across sources, the implication. Name the one thing most likely to slip or compound if left alone.

## Step 5. Handle gaps

- **Missing:** say so in one line, pull it live if you can, otherwise ask for the doc or context. Once they give it, file it the way add-to-cortex does, then answer.
- **Stale or wrong:** flag it ("The Cortex says X, but the meeting on Mar 10 suggests Y"), propose the exact fix, and apply it after they approve, updating in place with Last Updated and Source.

## Step 6. Offer to keep what's worth keeping

If the answer produced something durable (a pattern across people, a real risk in a decision, a position worth reusing), offer to save it: update the relevant record, add a Decision if it settled something, or update Strategy. Offer only. Don't fill the Cortex with every passing question.

On a yes, write following the Schema, then log it: Source = "Query: [short description, date]", Type Query Insight, What Changed = what was saved and where.
