# 09. Customer Interview Tracker

| | |
| --- | --- |
| Pillar | Persona (Market) |
| Read alongside | Chapter 3, "You Are Not Your Customer"; also Chapter 4 |
| Workbook | page 16 |
| Time | Log: 5 to 10 minutes per interview. Synthesize: 30 to 45 minutes |
| Lifts | Persona 3, 4, Problem 3, 4, Messaging 4 |
| Feeds from | #3 DSBA Interview Guide, #2 Don't Suck, Be Awesome |
| Feeds into | #4 From Suck to Awesome, #7 Persona Canvas, #11 Problem Canvas, #5 Animal Bite Framework, #20 Messaging Canvas |

## Why it matters

One interview is an anecdote. The tracker turns a run of conversations into evidence. Log each interview as you go. After 15 to 20 interviews, patterns emerge. Trust the patterns, not the outliers.

The number isn't arbitrary. Problem 4 on the scorecard asks whether you've interviewed 15 to 20 target customers about the problem in the last 90 days, and the PMF Milestones Checklist puts 15+ discovery interviews in 90 days as an early signal of fit. Chapter 4's insight is that there's no substitute or shortcut for thorough research and problem validation. The tracker is how the founder proves they've done it, and how they keep doing it.

The summary fields do the real work. Recurring themes are problems mentioned by three or more people. Outliers are anything mentioned only once, or only by an edge case; you discard those so a single loud voice doesn't steer the roadmap. Language to steal is the exact words that appear more than once. Those phrases become your copy in Chapter 9, because the closer your message is to the voice already in their head, the less convincing you have to do. The Surprise or signal column matters too. Chapter 4's rule: accept the truth. If the data don't fit your beliefs, your beliefs are wrong.

Keep the loop running. Chapter 15 notes you can now feed interviews to an LLM to auto-tag themes and surface patterns, with tools like Dovetail building this in. It also warns that the personas you built at the start stop representing your audience as you grow, so keep refreshing your research. The mistake founders make is interviewing in a burst, then never again, or keeping notes nobody can compare.

## Use it when

- The founder is starting discovery and needs a place to log conversations.
- They've done interviews but can't say what came up most often.
- Problem 3 or Problem 4 scored under 3, or they can't say how many interviews they've done in 90 days.
- They want to update personas, problems, or messaging and need the evidence trail.

## Before you start

Ask which mode they need.

- **Add** logs one or more new interviews as rows. Use it after every conversation, and to add to an existing tracker over time. If they have an existing tracker, ask them to paste it so new rows continue the numbering.
- **Synthesize** fills the three summary fields. It needs at least five rows. With fewer, say so and offer Add mode instead. With five to fourteen, synthesize but label every theme provisional; patterns firm up at 15 to 20.

If notes are thin, log what they have and tag anything reconstructed from memory [Assumption]. A row with no exact quote is a weak row; flag it. Never block them.

## Run it

### Mode A: Add (loop once per interview)

**Step 1 of 4: Who**
> Who did you talk to: name, role, company, and the date?

Push for: a real person in the target segment. If they're outside it, log them but note it; they may become an outlier.

**Step 2 of 4: Top problem mentioned**
> What was the top problem they mentioned, the one that hurt most?

Push for: one problem, as they described it. If they mentioned several, take the one they ranked highest in Stage 3 of #3 DSBA Interview Guide.

**Step 3 of 4: Exact quote**
> What's the exact line they said about it, word for word?

Push for: a verbatim quote with emotional heat if there was any. If they only have a paraphrase, ask: "What words did they actually use?" If none, tag the row [Assumption].

**Step 4 of 4: Surprise or signal**
> What surprised you, or what signal did you pick up that you didn't expect?

Push for: something that challenged the founder's belief, or a strong buying signal (a duct-taped workaround they built, money already spent on a fix, a willingness-to-pay hint from Stage 4). "Nothing surprised me" after several interviews is worth questioning: are they listening, or confirming?

Then ask if there's another interview to log. When done, report the running count and how many fall within the last 90 days.

### Mode B: Synthesize (needs 5+ rows)

**Step 1 of 3: Recurring themes**
> Looking across every row, which problems came up from three or more people?

Push for: themes with a count and the row numbers behind each. Group similar problems, but don't force them together. Probe: "Is that one theme or two?"

**Step 2 of 3: Outliers to discard**
> Which problems came up only once, or only from an edge case?

Push for: an honest list, especially if the founder's favorite problem is on it. Discarding means it doesn't drive decisions now; it can come back if more people raise it.

**Step 3 of 3: Language to steal**
> Which exact words or phrases showed up more than once?

Push for: verbatim phrases appearing in two or more quotes. Single-use phrases stay in the rows, not here.

## Push back when

- **One loud interview is steering everything.** "Trust the patterns, not the outliers. How many people said this?"
- **A theme has two mentions.** "Recurring means three or more. Right now it's a lead to chase in the next interview."
- **The quote column is paraphrase.** "Language to steal has to be their words. Without the exact quote, you can't use it in copy."
- **The favorite problem is an outlier.** "Accept the truth. If the data don't fit your beliefs, your beliefs are wrong."
- **The last interview was months ago.** "The scorecard asks about the last 90 days. When's the next one booked?"

## Output

```
GROWTH BY DESIGN · Customer Interview Tracker
[Company] · [Date] · Total interviews: [n] · In last 90 days: [n]

| # | Name / Role | Company | Date | Top problem mentioned | Exact quote | Surprise or signal |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [ ] | [ ] | [ ] | [ ] | "[ ]" | [ ]  [Evidence/Assumption] |

Recurring themes (problems mentioned by 3+ people): [theme · count · rows]  [Evidence/Assumption]
Outliers to discard (mentioned only once, or only by an edge case): [ ]
Language to steal (exact words that appear more than once): "[ ]"  [Evidence/Assumption]
```

In Add mode, output the new rows and the running count. In Synthesize mode, output the full table and the summary fields.

**Coaching notes**: 3 to 5 sentences: how close they are to 15 to 20 interviews in 90 days, which theme is strongest, whether any favored belief landed among the outliers, and how much usable language they've captured.

**Assumptions to test**: each provisional theme or [Assumption] row with the question to ask in the next interview.

**Your next move this week**: book enough interviews to reach the next five, targeting people who can confirm or kill the top provisional theme.

## Done well

- Every row has a verbatim quote, or is flagged as missing one.
- Every recurring theme names three or more rows.
- Outliers are discarded honestly, including inconvenient ones.
- The founder knows the 90-day count without looking it up.

## Next

- Once themes are recurring, distill them in #4 From Suck to Awesome and score them in #11 Problem Canvas. Update #7 Persona Canvas with what you learned. Carry Language to steal into #20 Messaging Canvas.
- **Book pointer:** Chapter 4 covers shadowing and the broad-to-specific interview sequence that makes each row worth logging, and Chapter 15 covers keeping feedback loops running as you grow.
- **Coaching trigger:** fewer than five interviews in 90 days with no plan to book more, or the founder keeps acting on outliers.
