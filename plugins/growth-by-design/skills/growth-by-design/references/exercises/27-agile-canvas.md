# 27. The Agile Canvas

| | |
| --- | --- |
| Pillar | Operating System |
| Read alongside | Chapter 13, "Agile Isn't Just for Engineers" |
| Workbook | page 34 |
| Time | 20 to 30 minutes (plus 15 for the optional sprint plan) |
| Lifts | Outcomes 4 |
| Feeds from | #15 The Outcome Canvas, #16 Feature Prioritization Matrix, #13 The Validation Canvas |
| Feeds into | #30 The Experiment Roster, #32 Weekly Metrics Scorecard, #33 The Retrospective Canvas |

## Why it matters

Part Four of the book is the operating system that keeps every pillar climbing, and this canvas is its basic unit: one build-test-learn cycle. Everyone knows agile as an engineering practice, but product and sales rarely work that way. Features get scoped in long waterfall cycles with no feedback loops. Sales promises release dates months out with no honest read on effort. Engineers never learn who the customer is or what they need.

The fix is to apply the same principles to the whole product process: rapid iteration, tight feedback loops, reflection and adaptation, transparency, and decisions made on data instead of opinion. Tighten each cycle and reflect at the end, so the next one runs better.

The workbook's rule for each cycle: fix the time, flex the scope. You always ship on time; you just won't know the exact features until you're in it. Founders usually do the opposite. They lock the feature list, let the date slide, and ship something big with no signal attached. The book's example is Tesla: most carmakers freeze a model for years and hold improvements for the next model year, while Tesla treats the car like software and pushes updates over the air to cars already in driveways. Ship, measure, improve, on a loop.

## Use it when

- Releases keep slipping because the scope is locked and the date isn't.
- The team ships features but can't say what each one was supposed to prove.
- Sales commits dates or features without engineering in the conversation.
- A dozen demands are competing (a big client, support tickets, a competitor launch, strained architecture) and there's no objective way to pick.

## Before you start

Ask what they're planning to build next and why. The best input is a top feature from #15 Outcome Canvas or a Quick Win or Big Bet from #16 Feature Prioritization Matrix, because those already carry a desired outcome and a metric. If they have neither, don't block: take the item they're about to build anyway and tag the success measure [Assumption] until it's tied to a customer outcome.

Ask which real customer will see this at the end of the cycle. If no one is lined up, getting one becomes part of the plan.

If a field can't be filled from real customer evidence, tag it [Assumption] and turn it into a learning goal.

## Run it

**Step 1 of 6: Capability**
> When this cycle ends, what will a customer be able to do that they couldn't do before?

Push for: a customer action, stated from their side. "Ship the new dashboard" is output. "A finance lead can see this month's spend by team without exporting" is a capability. Probe: "Who is the customer in that sentence, and what do they do differently?"

**Step 2 of 6: Success measure**
> What needle do you expect this to move, and by how much?

Push for: one metric and a target, tied to a customer outcome rather than activity. If they name clicks or usage, ask: "Could that number go up while the customer still fails?" Pull from #15 Outcome Canvas if it exists.

**Step 3 of 6: Smallest version**
> What's the roughest draft that would still give you a real signal?

Push for: something cut hard on scope and polish. The book's principle is least cost to validate: invest more only once you know it meets the need. Probe: "What could you cut and still learn the same thing?"

**Step 4 of 6: Timebox**
> How long is this cycle, fixed, no extensions?

Push for: a hard duration with a date. Make the trade explicit: "If it runs long, what gets cut, not what gets moved?" If they say "it depends on the features," that's the waterfall habit. Fix the time first.

**Step 5 of 6: Learning goals**
> What do you hope to learn from this, whether it works or not?

Push for: testable questions, written so a result could disappoint them. These feed #30 Experiment Roster as hypotheses.

**Step 6 of 6: The customer at the end**
> Which real customer sees this when the timebox ends, and how will you get their feedback?

Push for: a name or a defined group, and the method (a call, a usability session, analytics on a cohort). No customer, no closed loop.

**Optional Part 2: Sprint Planning Canvas (from the book)**

If they want to plan the sprint inside this cycle, run the book's Sprint Planning Canvas. Ask one question at a time:

> What's the one outcome this sprint must deliver, and what are the dates?

Then loop through each item: name, type (customer-driven, experiment, or quality / tech debt), source, owner, and done when. Tally the three types. The book's rule: every sprint holds at least one customer-driven item, one experiment, and one quality or performance improvement. If any type is missing, re-plan. Close with the sprint health check, a yes or no on each: Does every item map to a pillar on the Scorecard? Does at least one item have a testable hypothesis? Does the team agree this sprint goal is worth the two weeks?

## Push back when

- **The scope is fixed and the date floats.** "Fix the time, flex the scope. What comes out if you run short?"
- **The capability is a feature name.** "That's what you're building. What can the customer do afterward?"
- **The smallest version is the full version.** "Is this the roughest draft that still teaches you something, or the one you'd be proud to demo?"
- **No learning goals, or ones that can't fail.** "If every outcome confirms what you already believe, it isn't a learning goal."
- **The sprint has no experiment or no quality work.** "The book's rule is all three types every sprint. Which one are you skipping, and what will that cost you in a month?"

## Output

```
GROWTH BY DESIGN · Agile Canvas
[Company] · [Cycle name] · [Date]

Capability: [what the customer can do after this cycle]  [Evidence/Assumption]
Success measure: [metric] · target [ ]  [Evidence/Assumption]
Smallest version: [roughest draft that gives a real signal]  [Evidence/Assumption]
Timebox: [duration] · ends [date] · scope flexes to fit
Learning goals: [1] [2] [3]  [Evidence/Assumption]
Customer at the end: [who] · [how feedback is gathered]

Sprint Plan (from the book, optional)
Sprint goal: [one outcome] · Dates: [ ]
| Item | Type | Source | Owner | Done when |
Customer-driven: _ of _ · Experiments: _ of _ · Quality / tech debt: _ of _
Health check: maps to Scorecard pillar [Y/N] · testable hypothesis [Y/N] · worth the two weeks [Y/N]
```

**Coaching notes**: 3 to 5 sentences on what the canvas showed, for example whether the scope is really flexible, whether the success measure tracks a customer outcome, and whether a real customer closes the loop.

**Assumptions to test**: each [Assumption] field with the cheapest way to settle it inside this timebox.

**Your next move this week**: one action, usually "write the success measure and learning goals into the ticket, and book the customer who'll see it on the last day."

## Done well

- The capability is written from the customer's side.
- The timebox has a date and a stated rule for what gets cut.
- At least one learning goal could come back with an answer the founder doesn't want.
- A named customer sees the result before the next cycle is planned.

## Next

- Turn the learning goals into hypotheses in #30 Experiment Roster. When the cycle closes, review it in #33 Retrospective Canvas, and track the success measure in #32 Weekly Metrics Scorecard.
- **Book pointer:** Chapter 13 sets up the whole operating system, why the forces fighting for a team's attention need an objective process, and how agile principles apply to sales and product as well as engineering.
- **Coaching trigger:** the founder can't commit to a fixed timebox, or sprint after sprint ships with no experiment and no customer feedback at the end.
