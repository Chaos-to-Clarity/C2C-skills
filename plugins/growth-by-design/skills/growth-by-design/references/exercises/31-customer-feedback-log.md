# 31. Customer Feedback Log

| | |
| --- | --- |
| Pillar | Operating System |
| Read alongside | Chapter 15, "Make the Customer the Loudest Voice in the Room" |
| Workbook | page 38 |
| Time | 20 to 40 minutes per monthly review (5 minutes per batch of new items) |
| Lifts | Solution 3, Experience 3, Outcomes 3, Persona 3 |
| Feeds from | #9 Customer Interview Tracker, #28 The Idea-Source Audit, #29 The Idea Meritocracy Audit |
| Feeds into | #16 Feature Prioritization Matrix, #27 The Agile Canvas, #7 The Persona Canvas, #33 The Retrospective Canvas |

## Why it matters

Making the customer the loudest voice in the room takes a steady supply of their actual words. The book names three ways to gather feedback, and you want all three. **Ask** them: interviews, surveys, and in-app prompts capture intentions and emotional state (tools like Typeform and Intercom make this easy). **Observe** them: usability tests and session recordings show actual behavior, which often differs from what they say (Hotjar, FullStory, Maze, UserTesting). **Analyze** them: event capture and analytics show patterns in aggregate (Amplitude, Mixpanel, PostHog, Looker).

Once the product is live, never stop. The most reliable channels are surveys, beta groups, customer interviews, analytics, support, and sales. Build listening into the rhythm of the business so it runs continuously instead of in bursts. The book also flags what's new: you can feed interviews, support tickets, and reviews to an LLM to auto-tag themes and surface patterns across thousands of pieces of feedback, work that used to take an analyst weeks. Tools like Dovetail build this in. A flood of raw feedback becomes a ranked list of what customers care about.

The trap as you grow: the personas built at the start stop representing your audience. Early adopters aren't mainstream customers, and assumptions that fit a hundred customers break at a hundred thousand. A running log is how you notice. Amazon's empty chair, the seat Jeff Bezos left for the customer, works only if someone fills it with what customers actually said this month.

## Use it when

- Feedback lives in five places (support inbox, call notes, reviews, Slack) and nobody sees the whole picture.
- The backlog is driven by whoever complained last or loudest.
- #28 Idea-Source Audit showed support, research, or analytics underweighted.
- The founder wants to check whether personas still match today's customers.
- It's the monthly review and the patterns need to drive the backlog.

## Before you start

Ask them to paste raw feedback: support tickets, app store or review-site reviews, interview notes, sales call notes, survey responses, NPS comments. Messy is fine. The skill does the tagging. If they have nothing collected, start the log with what they remember from the last two weeks, tag each item [Assumption] because it's recalled rather than recorded, and make setting up one capture channel the next move.

Pillar tags use the ten pillars: Problem, Solution, Experience, Differentiation, Outcomes, Persona, Messaging, Channel, Model, Timing. Quick guide: "it doesn't do X" is Solution; "confusing, slow, frustrating to use" is Experience; "I didn't get the result" is Outcomes; "too expensive, wrong plan" is Model; "I thought it was something else" is Messaging; "you're like competitor Y" is Differentiation; a bad-fit user is Persona.

## Run it

**Step 1 of 5: Paste the raw feedback**
> Paste in everything you've got from this period: tickets, reviews, call notes, survey comments. Where did each batch come from?

Push for: the source of each batch (support, interview, review, sales). Ask for dates if they're easy; otherwise use the batch date.

**Step 2 of 5: Tag it**

Split the paste into individual items. For each, write a row: date, source, verbatim quote or a one-line summary, pillar, and sentiment (positive, negative, or neutral). Keep verbatim quotes wherever the words are strong; they feed #20 Messaging Canvas. Show the tagged table, then ask:

> Here's how I tagged these. Anything I got wrong, or context I'm missing about who said what?

Push for: corrections from the founder, especially on pillar. If an item could be two pillars, pick the one closest to the root cause.

**Step 3 of 5: Action taken**
> For each item that needs a response, what action was taken, or what should be?

Push for: a real action (replied, fixed, logged to backlog, no action and why). Blank is acceptable for neutral items.

**Step 4 of 5: Summary fields**
> Looking at the pattern: what's the most common complaint, the most common praise, and which pillar shows up most in the negative feedback?

Draft all three from the tags first, then ask the founder to confirm. Show the counts by pillar so the answer is visible.

**Step 5 of 5: One backlog item**
> What's the one backlog item this log should influence?

Push for: a specific item to add, move up, or kill, tied to the top pattern. Ask whether the complaints come from the persona they're targeting or from a different group; if a different group, flag #7 Persona Canvas for a refresh.

On later runs, add new items to the existing log, then redo the four summary fields for the month.

## Push back when

- **Only praise gets logged.** "The complaints drive the backlog. Where are the support tickets?"
- **Everything is a summary.** "Keep their words. 'I freaking hate this' tells you more than 'mild friction.'"
- **One loud customer dominates the log.** "That's one voice. How many separate customers raised this?"
- **The review never happens.** "Review monthly or it's a diary. When's the next one on the calendar?"
- **The pattern contradicts the roadmap and the roadmap wins.** "The workbook's line: the patterns drive the backlog. What would it take for this one to?"

## Output

```
GROWTH BY DESIGN · Customer Feedback Log
[Company] · [Month]

| Date | Source (support / interview / review / sales) | Verbatim quote or summary | Pillar | Sentiment (positive / negative / neutral) | Action taken |
| ... |

Counts by pillar (negative): [Pillar _ · Pillar _ · ...]

Most common complaint this month: [ ]  [Evidence/Assumption]
Most common praise this month: [ ]  [Evidence/Assumption]
Pillar showing up most in negative feedback: [ ]  [Evidence/Assumption]
One backlog item this log should influence: [ ]
```

**Coaching notes**: 3 to 5 sentences on the pattern, for example which pillar is leaking, whether the complaints come from the target persona, and which source is missing from the mix (ask, observe, or analyze).

**Assumptions to test**: any recalled or single-source items, with the cheapest way to confirm the pattern (five follow-up calls, a session recording review, an analytics pull).

**Your next move this week**: one action, usually "move the backlog item into the next cycle and tell the customers who raised it."

## Done well

- Feedback comes from at least two of ask, observe, and analyze.
- Most rows keep the customer's own words.
- The four summary fields are backed by counts, not impressions.
- One backlog item actually changed because of the log.

## Next

- Bring the backlog item into #16 Feature Prioritization Matrix or straight into #27 Agile Canvas. If complaints come from outside the target persona, refresh #7 Persona Canvas.
- **Book pointer:** Chapter 15 explains the difference between the process in theory and in practice, and why early adopters stop representing the market as you scale.
- **Coaching trigger:** the same pillar leads negative feedback two months running with no backlog change, or the founder has no capture channel at all.
