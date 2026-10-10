# 15. The Outcome Canvas

| | |
| --- | --- |
| Pillar | Outcomes (Product) |
| Read alongside | Chapter 7, "Nobody Wants Your Pile of Features" |
| Workbook | page 22 |
| Time | 30 to 45 minutes |
| Lifts | Outcomes 1, 2, 3, 4, 5 |
| Feeds from | #12 Jobs-to-Be-Done Canvas, #6 The Yellow Brick Road, #4 From Suck to Awesome, #14 The Experience Canvas |
| Feeds into | #16 Feature Prioritization Matrix, #32 Weekly Metrics Scorecard, #30 The Experiment Roster, #27 The Agile Canvas |

## Why it matters

Customers don't want your pile of features. They want the result your features get them. Build a pile of features and you've just created work; get customers real results and you've built something worth paying for. The book's key insight: you can't solve a problem unless you know what success looks like, so start with the outcome and work backward.

Tony Ulwick's Outcome-Driven Innovation gives the form: a direction of improvement, a metric, and the thing being improved. "Minimize the time it takes to reconcile a month's expenses." "Reduce the likelihood of missing a deadline." "Increase the number of qualified leads from a campaign." Stated that way, an outcome is testable. Josh Seiden makes the same case in Outcomes Over Output: progress means a customer behavior changed. The trap is measuring the company by what you released. You can ship ten features a quarter and deliver nothing that matters. Duolingo is the book's example: it organized the whole product around one outcome, whether people keep learning day after day, and the streaks and quizzes exist to drive it.

Every feature needs a needle. Write how you'll know it worked before you build it: not "users can now export reports" but "teams cut their monthly reporting time in half." Underneath, name a North Star Metric (Amplitude coined the term), one number that rises only when customers win. The book's examples: Slack found teams that exchanged about 2,000 messages almost never left. Medium measures Total Time Reading instead of pageviews. Facebook's early growth team fixated on seven friends in ten days. Signups, downloads, and pageviews fail this test, because they rise when marketing works even if the product fails everyone. Under the North Star sit input metrics: the things the team can actually move.

Eric Ries separates vanity metrics from outcome metrics in The Lean Startup. A good outcome metric is actionable (ties to a decision), accessible (the team can see and understand it), and auditable (reflects real customer behavior). Total registered users fails all three; weekly active customers who completed the core job passes. Split measures into lagging (renewal, a customer hitting their goal) and leading (how fast a new customer reaches the Aha Moment). A customer health score built from leading signals shows who's about to churn while there's time to act.

## Use it when

- The roadmap is a feature list with no stated results.
- Features ship and nobody can say whether they worked.
- Outcomes scored under 3, or Outcomes 4 (every core feature has a success metric) scored 1 or 2.
- The dashboard is full of signups and pageviews but retention is unclear.

## Before you start

Ask for the job statement and success criteria from #12 Jobs-to-Be-Done Canvas and the core features from #6 The Yellow Brick Road. The canvas covers the top three features only. If they have more, ask which three matter most to the customer's goal.

Ask what analytics they have. Any outcome or metric they can't support with customer evidence or real data gets tagged [Assumption], and instrumenting it becomes the next task. Don't block them.

## Run it

Loop steps 1 to 3 once per feature (three times). Then do steps 4 and 5.

**Step 1 of 5: Feature**
> Name one of your top three features.

Push for: a real, shipped or planned feature on the path to the customer's goal.

**Step 2 of 5: Desired customer outcome**
> What result does this get the customer? Say it as direction, metric, and thing improved.

Push for: Ulwick's form ("reduce the time it takes to..."), in the customer's terms. If they describe the function ("they can export reports"), ask: "And then what changes for them?"

**Step 3 of 5: Success metric (with target)**
> What number proves the outcome happened, and what target are you aiming for?

Push for: a metric and a target. Run the three tests: actionable, accessible, auditable. Ask whether it's leading or lagging. If there's no target, ask: "What number would make you say this feature was worth building?"

**Step 4 of 5: North Star Metric (from the book)**
> What one number rises only when customers are genuinely winning?

Push for: delivered value. Test it: "Could this go up while customers fail?" If yes (signups, downloads, pageviews), keep looking.

**Step 5 of 5: Input metrics (from the book)**
> What can your team actually move this week that drives the North Star?

Push for: three to five levers the team controls, with at least one leading signal such as time to the Aha Moment. Ask: "Who owns each one?"

## Push back when

- **The outcome restates the feature.** "That's what it does. What does the customer get?"
- **No target.** "Without a number, you can't miss. Pick the target now, while you're still deciding if it's worth building."
- **Vanity metric.** "Total registered users goes up when marketing works. What shows customers getting the result?"
- **The North Star tracks activity.** "Pick the metric that can't climb unless customers are winning."
- **Progress is measured in releases.** "You can ship ten features a quarter and deliver nothing that matters. Which customer behavior changed?"
- **Post-launch, nobody checked.** "Did we really make the impact we intended? If not, what went wrong in how we decided?"

## Output

```
GROWTH BY DESIGN · Outcome Canvas
[Company] · [Date]

| Feature | Desired customer outcome | Success metric (with target) |
| --- | --- | --- |
| 1. [ ] | [direction + metric + thing improved] [E/A] | [metric] · [target] · [leading/lagging] [E/A] |
| 2. [ ] | [ ] [E/A] | [ ] [E/A] |
| 3. [ ] | [ ] [E/A] | [ ] [E/A] |

North Star Metric (from the book): [one number]  [Evidence/Assumption]
Input metrics (from the book): [3 to 5 levers, with owners]  [Evidence/Assumption]
Metric check: actionable [y/n] · accessible [y/n] · auditable [y/n]
```

**Coaching notes**: 3 to 5 sentences on what the canvas revealed, for example whether outcomes describe customer results or functions, whether any metric is vanity, and whether the North Star can rise while customers fail.

**Assumptions to test**: each [Assumption] field with the cheapest way to get real data, often instrumenting one event or asking five customers what changed.

**Your next move this week**: one concrete action, usually "instrument the success metric for Feature 1 and record a baseline."

## Done well

- Every outcome is written in Ulwick's form, in the customer's terms.
- Every metric has a target and passes actionable, accessible, auditable.
- The North Star can't climb unless customers win.
- At least one input metric is a leading signal the team can move this week.

## Next

- Run #16 Feature Prioritization Matrix, scoring impact against these outcomes. Put the North Star and inputs on #32 Weekly Metrics Scorecard.
- **Book pointer:** Chapter 7 explains how to build a customer health score from leading signals and how to close the loop by feeding outcome data back into the next round of discovery.
- **Coaching trigger:** none of the top three features has a measurable outcome, or the North Star is an activity metric the founder won't let go of.
