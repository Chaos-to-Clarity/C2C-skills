# 16. Feature Prioritization Matrix

| | |
| --- | --- |
| Pillar | Outcomes (Product) |
| Read alongside | Chapter 7, "Nobody Wants Your Pile of Features" |
| Workbook | page 23 |
| Time | 30 to 45 minutes |
| Lifts | Outcomes 2, 4 |
| Feeds from | #15 The Outcome Canvas, #6 The Yellow Brick Road, #31 Customer Feedback Log, #12 Jobs-to-Be-Done Canvas |
| Feeds into | #27 The Agile Canvas, #30 The Experiment Roster, #13 The Validation Canvas |

## Why it matters

Nobody wants your pile of features. They want the result. Every feature on a roadmap competes for the same scarce engineering time, and most founders rank by gut, by the loudest customer, or by what's fun to build. The matrix forces each candidate onto two axes: how much it moves a customer outcome (impact) and what it costs to build (effort). Then the decision is mostly made for you.

The four quadrants: Quick Wins (high impact, low effort) get built now. Big Bets (high impact, high effort) get planned, then built. Fill-ins (low impact, low effort) get spare capacity only. Avoid (high effort, low payoff) gets dropped. The workbook's rule is stricter: ignore the low-impact ones entirely. That matches the Define the MVP exercise in Chapter 5, where anything you didn't score High on impact is out.

Impact here has one meaning: impact on a customer outcome from #15 The Outcome Canvas. Every feature should have a needle, a success metric defined while you're still deciding whether to build it, and that alone kills weak ideas before they cost a dime. Duolingo is the book's model: the streaks, the quizzes, the whole experience exist to drive one outcome, whether people keep learning day after day. A feature that doesn't move the outcome doesn't earn a slot.

The mistake: scoring impact as "customers asked for it" or "it would be cool." Requests are inputs. Impact is the change in what customers achieve. After a feature ships, the book asks you to come back and challenge your claims: did it make the impact you intended? If not, Eric's bet is that you didn't get enough customer feedback.

## Use it when

- The backlog is long and everything feels important.
- The team argues about what to build next.
- Big features keep shipping without moving retention or outcomes.
- Before planning a build cycle in #27 The Agile Canvas.

## Before you start

The matrix works only if outcomes are defined. Ask for the outcomes and North Star from #15 The Outcome Canvas. If they haven't done it, ask them to name the one result customers most want, write it down, and tag it [Assumption]. Offer #15 next.

Collect the candidate list: roadmap, backlog, customer requests from #31 Customer Feedback Log, and anything that fell off #6 The Yellow Brick Road. Agree on the cut line before scoring: what counts as high impact and high effort on the 1 to 5 scale (for example, 4 and up). Any impact score with no customer evidence behind it gets tagged [Assumption]. Don't block them.

## Run it

Loop steps 1 to 4 once per feature. Then do steps 5 and 6.

**Step 1 of 6: Feature**
> Name the next candidate feature.

Push for: one feature, described by what it does for the customer.

**Step 2 of 6: Impact (1 to 5)**
> Which customer outcome does this move, and by how much?

Push for: a named outcome from #15 and the evidence (feedback, usage data, test results). If it moves no outcome, it's a 1. If vague, ask: "What will customers achieve that they can't today?"

**Step 3 of 6: Effort (1 to 5)**
> What does it really cost to build, test, and support?

Push for: an honest estimate from whoever builds it. Ask whether there's a stripped-down version that still moves the outcome, and score that instead if so.

**Step 4 of 6: Quadrant and decision**
> Where does it land, and what's the call?

Push for: Quick Win, build now. Big Bet, plan then build, often with a #13 Validation Canvas card first. Fill-in, spare capacity only. Avoid, drop it. Low impact means it comes off the roadmap.

**Step 5 of 6: The build order**
> Looking at the whole grid, what are the first three things you build?

Push for: Quick Wins first, then the one Big Bet worth planning. If a low-impact feature made the list, ask why.

**Step 6 of 6: The needle check**
> For each feature you're building, what's the success metric, and when will you check it?

Push for: a metric and a review date per feature, tied back to #15.

## Push back when

- **Impact means "requested."** "How many asked isn't impact. What changes for them when it ships?"
- **Everything is high impact.** "If everything's a 5, the matrix can't help you. Which three move the outcome most?"
- **They keep the low-impact ones.** The workbook's rule: ignore the low-impact ones entirely. "Fill-ins are what you do when there's nothing better, and there's always something better."
- **A Big Bet goes straight to build.** "That's months of engineering on a belief. What's the cheapest test first?"
- **Effort is wishful.** "Ask whoever builds it. What would they say?"

## Output

```
GROWTH BY DESIGN · Feature Prioritization Matrix
[Company] · [Date]
Outcome scored against: [from #15]  [Evidence/Assumption]
Cut line: high = [4+]

| Feature | Impact (1-5) | Effort (1-5) | Quadrant | Decision |
| --- | --- | --- | --- | --- |
| [ ] | [ ] [E/A] | [ ] | [Quick Win / Big Bet / Fill-in / Avoid] | [build now / plan then build / spare capacity / drop] |

Build order: 1. [ ] 2. [ ] 3. [ ]
Needle per feature: [feature] · [success metric] · [review date]
Removed from roadmap (low impact): [ ]
```

**Coaching notes**: 3 to 5 sentences on what the grid revealed, for example how many features moved no outcome, whether the founder's favorite survived, and how much of the impact scoring is assumption.

**Assumptions to test**: each [Assumption] impact score with the cheapest way to test it, usually five customer conversations or a #13 card.

**Your next move this week**: one concrete action, usually "start the top Quick Win and delete the Avoid items from the backlog."

## Done well

- Every impact score names the customer outcome it moves.
- Low-impact features are off the roadmap entirely.
- Big Bets have a validation step before full build.
- Each feature being built has a needle and a review date.

## Next

- Run #27 The Agile Canvas to plan the first build cycle around the top item, and #30 The Experiment Roster to track whether each shipped feature moved its needle.
- **Book pointer:** Chapter 7 covers the North Star and input metrics that sit above feature-level needles, plus the difference between leading and lagging outcomes.
- **Coaching trigger:** most candidate features can't be tied to any customer outcome, or the founder keeps building Avoid items after the grid says drop them.
