# 33. The Retrospective Canvas

| | |
| --- | --- |
| Pillar | Operating System |
| Read alongside | Chapter 17, "Were You Right, or Just Lucky?" |
| Workbook | page 40 |
| Time | 15 to 20 minutes per feature; 45 to 90 minutes for a full Grand Retrospective |
| Feeds from | #30 The Experiment Roster, #32 Weekly Metrics Scorecard, #28 The Idea-Source Audit |
| Feeds into | #29 The Idea Meritocracy Audit, #27 The Agile Canvas, #1 PMF Scorecard (quarterly re-score) |

## Why it matters

The book says every roadmap planning session should open with the Grand Retrospective: a review of the experiments you ran, the features you shipped, and the needles that moved. Because each feature's impact was predicted before it was built, you can compare what you expected against what happened. When results match, take the win. When they don't, it's a chance to examine how you make decisions.

If you're consistently wrong about the impact of your ideas, one of two things is true. Either you're terrible at strategic planning or, far more likely, you're deciding without a complete set of information. Lean on the highest-paid opinions, skip basic market research, or stay distant from customers, and the calls go bad. The book's bet: nine times out of ten, the answer is that you weighted internal opinion too heavily and gathered too little customer feedback. The retrospective drags that into the light and keeps steady pressure on the team to become more customer-centered.

Structure matters. Ask a fixed set of questions about every feature so you can trace the root cause of a surprise. The book's example is Toyota: when something broke on the line, workers asked "why" five times, drilling past the symptom to the root cause before fixing anything. Treat every missed result as a thread to pull. End each session with a short list of lessons and actions, make it public, and hold each other accountable. Analytics and AI can help by clustering missed predictions to reveal patterns one review would miss.

## Use it when

- It's the start of a roadmap planning session.
- A feature shipped and the number didn't move, or moved the wrong way.
- A feature beat expectations and nobody knows why.
- The team keeps making the same kind of miss.
- Quarterly, alongside the #1 PMF Scorecard re-score.

## Before you start

Ask which shipped features are up for review. One canvas per feature; offer to run several in a row and look for a common thread at the end. For each, the best input is its entry in #30 Experiment Roster, with the predicted impact and threshold written before launch.

If no prediction was recorded, don't skip the feature. Ask what the team expected at the time, tag Expected impact [Assumption], and note that the missing prediction is itself a lesson. If there's no actual data, tag Actual impact [Assumption] and make instrumenting it the next action.

## Run it

Loop steps 1 to 6 for each feature. Run step 7 once at the end.

**Step 1 of 7: Expected impact**
> What did you predict this feature would do, in its Experiment Roster or anywhere you wrote it down?

Push for: the original prediction, not a revised one. Probe: "Where was that written, and when?"

**Step 2 of 7: Actual impact**
> What did the data show?

Push for: the number against the prediction, plus what customers said. Name the gap plainly: matched, beat, or missed.

**Step 3 of 7: The six questions**
> Let's run the book's questions. Where did the idea originate? Have we seen this feature in other products? Did we validate it with customers before building? Did we design and run the experiment properly? Did we control for error well enough to trust the result? Did user feedback explain why it performed the way it did?

Ask them one at a time and capture a short answer to each. These answers point to the root cause.

**Step 4 of 7: Root cause**
> Why was there a gap? (Then ask "why" again on each answer, until you hit something you can change.)

Push for: five whys, Toyota style. Stop when the answer is a process or decision habit, not a one-off event. If it was a win, ask why too: luck and skill look the same until you check.

**Step 5 of 7: Lesson learned**
> What's the lesson, in one sentence someone else on the team could act on?

Push for: a lesson about how decisions get made, not about the feature alone.

**Step 6 of 7: Next action**
> What changes next cycle because of this, and who owns it?

Push for: a specific change with an owner and date. It goes on the public list.

**Step 7 of 7: Common thread (after several features)**
> Looking across these features, what's the common thread in the misses?

Lay out the six-question answers side by side. If most misses trace to HIPPO ideas or skipped validation, say so, and connect it to #28 Idea-Source Audit if they've run it.

## Push back when

- **The prediction gets rewritten after the fact.** "What did you write down before you shipped? If nothing, that's the first lesson."
- **The root cause is "the market."** "Keep asking why. What did you not know that a customer could have told you?"
- **Wins get skipped.** "Were you right, or just lucky? A win you can't explain won't repeat."
- **Lessons stay private.** "Make the list public and hold each other to it. A lesson nobody sees changes nothing."
- **The team is consistently wrong and calls it bad luck.** "Nine times out of ten, the answer is that internal opinion got weighted too heavily and customers too lightly. Does that fit here?"

## Output

One block per feature:

```
GROWTH BY DESIGN · Retrospective Canvas
[Company] · [Feature] · [Planning cycle / date]

Expected impact (from its Experiment Roster): [ ]  [Evidence/Assumption]
Actual impact (what the data showed): [ ]  [Evidence/Assumption]
Six questions: origin [ ] · seen before [ ] · validated first [y/n] · experiment run properly [y/n] · error controlled [y/n] · feedback explains it [y/n]
Root cause of any gap (why x5): [ ]  [Evidence/Assumption]
Lesson learned: [ ]
Next action (what changes next cycle): [ ] · owner [ ] · by [date]
```

After several features: **Common thread** and **Public lessons list** (lesson, action, owner).

**Coaching notes**: 3 to 5 sentences on the pattern, for example how often predictions matched, where the misses originated, and whether the root causes trace to skipped validation or untested opinion.

**Assumptions to test**: each [Assumption] field, with what to instrument or who to ask.

**Your next move this week**: one action, usually "post the lessons list where the team plans and assign each action an owner."

## Done well

- Expected impact was written before launch, or its absence is named as a lesson.
- The root cause is a decision habit the team can change.
- Wins get the same scrutiny as misses.
- The lessons list is public, with owners and dates.

## Next

- If misses trace to idea sources, run #29 Idea Meritocracy Audit. Carry next actions into #27 Agile Canvas. Re-score #1 PMF Scorecard as part of the quarterly Grand Retrospective.
- **Book pointer:** Chapter 17 explains how the retrospective becomes a discipline for mastering decision-making, and how analytics and AI can cluster missed predictions into patterns.
- **Coaching trigger:** most reviewed features had no recorded prediction, or the same root cause shows up in three or more misses.
