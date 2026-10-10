# 30. The Experiment Roster

| | |
| --- | --- |
| Pillar | Operating System |
| Read alongside | Chapter 16, "Every Feature Is an Experiment" |
| Workbook | page 37 |
| Time | 20 to 30 minutes per experiment |
| Lifts | Outcomes 3, 4 (and Messaging 5 or Model 4 when the experiment tests copy or price) |
| Feeds from | #27 The Agile Canvas, #15 The Outcome Canvas, #16 Feature Prioritization Matrix, #29 The Idea Meritocracy Audit |
| Feeds into | #33 The Retrospective Canvas, #32 Weekly Metrics Scorecard |

## Why it matters

Agile product development runs on a core loop of experimentation, analysis, and adaptation. A feature starts as an idea, and as you flesh it out you look for the simplest, fastest, cheapest way to validate it before sinking in real time or money. The book points out that growth hacking is really the scientific method applied to marketing and product. Its steps: develop a hypothesis, design an experiment to test it, set clear criteria for success or failure, run it with predefined cohorts and a control group, isolate it so you're testing one thing, measure the results, and confirm or deny the hypothesis.

The discipline is to do this for every release. Before you ship, write down a hypothesis, an experiment, and a measure of success. Keep releases as small as possible so you can isolate what caused what. Build the experiment into the release with cohorts, a control group, and a few A/B variations. After launch, measure the effect on business drivers over time: if you expect a feature to lift conversion, isolate customers who signed up around the same time, split them by cohort, and track the real effect over the following weeks. Then record the result on the roadmap itself, so the decision and its outcome live in one place.

The book's example is Dropbox. Paid ads weren't paying off, so they ran one clean experiment: more free storage for inviting a friend, and free storage for the friend too. Signups climbed dramatically and the loop funded itself.

The mistake founders make is calling a launch an experiment after the fact. Without a threshold written down first, any result looks like a win.

## Use it when

- Features ship with no prediction of what they'll do.
- Several changes go out in one big release and nobody can say which one moved the number.
- A disagreement about what to build needs to become "how do we test it?"
- A KPI is stuck and the team needs a list of bets to try.
- The roadmap records what shipped but not what happened.

## Before you start

Ask which KPI or outcome they want to move. The best source is the success measure from #27 Agile Canvas or a metric from #15 Outcome Canvas. If they don't have one, ask what number would tell them the product is working for customers, and tag it [Assumption].

Ask whether they can split users into cohorts today (feature flags, an analytics tool, even a manual list). If they can't, the cohort field will be rough. Don't block: a smaller, manual cohort with a clear baseline still beats no control.

The workbook says to brainstorm experiments to drive KPIs, then fold at least one into each release. Run the steps for one experiment at a time; offer to add more.

## Run it

**Step 1 of 6: Brainstorm**
> What are three to five changes you think could move this KPI?

Push for: a short list. Then ask which one is cheapest to test and most likely to matter. Run that one first.

**Step 2 of 6: Hypothesis**
> Finish this sentence: we believe [change] will cause [outcome].

Push for: one change and one outcome. If the sentence has "and" in the change, split it. Probe: "If that outcome didn't happen, would you believe the change failed?"

**Step 3 of 6: Metric and success threshold**
> What number confirms or denies it, and what value counts as a win?

Push for: a threshold set now, before any data exists. "It goes up" isn't a threshold. Ask for the baseline today and the specific target.

**Step 4 of 6: Cohort and control**
> Who's in the test, and who's the baseline you'll compare against?

Push for: a defined group and a comparable control, ideally from the same time window so seasonality doesn't fool them. Check isolation: "What else is shipping to this cohort at the same time?"

**Pause point.** Steps 5 and 6 need the experiment to have run. If they don't have it yet, stop here: save the canvas as a draft with the steps done so far, add the field work to Open next moves with a date, and tell them to say "continue" when they have results. Resume at the next step.

**Step 5 of 6: Result**
> What did the data show?

If the experiment hasn't run yet, leave this blank and set a date to come back. If it has, push for the number against the threshold, plus what customers said about it.

**Step 6 of 6: Decision**
> Ship, iterate, or kill?

Push for: the decision that the threshold implies. If they want to ship something that missed, ask what they learned that the threshold didn't capture. Record the result and decision on the roadmap document.

## Push back when

- **The threshold gets set after the result.** "Write the number down now. If you pick it later, you'll pick one you already hit."
- **The release bundles five changes.** "Keep releases small. If all five ship at once, which one gets the credit?"
- **There's no control.** "Compared to what? Without a baseline, you're measuring the season, not the feature."
- **Every experiment is a win.** "If nothing ever gets killed, the tests are too safe or the thresholds too low."
- **They skip recording the result.** "The roadmap should hold the decision and its outcome together. That's what the retrospective runs on."

## Output

```
GROWTH BY DESIGN · Experiment Roster
[Company] · [KPI] · [Date]

Experiment [N]: [name] · Release: [ ]
Hypothesis: we believe [change] will cause [outcome]  [Evidence/Assumption]
Metric and success threshold: [metric] · baseline [ ] · win at [ ]  [Evidence/Assumption]
Cohort and control: test [who] · control [who] · window [dates]  [Evidence/Assumption]
Result: [what the data showed, or "pending, check on [date]"]
Decision: [ship / iterate / kill]

Backlog of experiments: [other ideas from the brainstorm]
```

**Coaching notes**: 3 to 5 sentences on the quality of the test, for example whether the threshold was set in advance, whether the cohort is truly isolated, and what the result says about the original idea's source.

**Assumptions to test**: each [Assumption] field, with the cheapest way to firm it up (a baseline data pull, a flag to build the cohort).

**Your next move this week**: one action, usually "write the hypothesis and threshold into the next release ticket before it ships."

## Done well

- The hypothesis names one change and one outcome.
- The threshold and baseline were written before the test ran.
- The control is comparable and nothing else shipped to the cohort mid-test.
- The result and decision are recorded on the roadmap.

## Next

- When results come in, bring the prediction to #33 Retrospective Canvas. Track the metric weekly in #32 Weekly Metrics Scorecard.
- **Book pointer:** Chapter 16 includes the Growth Hacking Model diagram and a worked example of isolating a cohort to measure a feature's real effect on conversion over the following weeks.
- **Coaching trigger:** no release in the last quarter had a written hypothesis, or the team can't build any cohort or control at all.
