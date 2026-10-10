# 28. The Idea-Source Audit

| | |
| --- | --- |
| Pillar | Operating System |
| Read alongside | Chapter 15, "Make the Customer the Loudest Voice in the Room" (the canvas is printed at the end of Chapter 14) |
| Workbook | page 35 |
| Time | 30 to 45 minutes |
| Feeds from | Nothing; a good first exercise for the Operating System. #1 PMF Scorecard helps. |
| Feeds into | #29 The Idea Meritocracy Audit, #31 Customer Feedback Log, #33 The Retrospective Canvas |

## Why it matters

Most companies have a product process, or think they do. Then the chaos of the business takes over and the process in practice looks nothing like the one in the charter. The book asks for an honest look in the mirror: forget the process docs, how do product decisions actually get made? Odds are the loudest voices, usually the founder or a big customer, carry far more weight than they should.

This audit is the mirror. List what you actually shipped, trace where each idea came from, and the biases show up on their own. A healthy mix pulls from customer support, sales calls, competitive analysis, surveys and user feedback, internal brainstorming, industry trends, growth experiments, and analytics. Then there's the Highest-Paid Person's Opinion, the HIPPO. The channels should be reasonably balanced, with extra weight on the user's voice through research, surveys, testing, and analytics. When the HIPPO roars, the job is to make the user's voice louder. If the founder is the HIPPO, the job is to learn to listen to the other voices in the room.

The book's example is Amazon. In the early days, Jeff Bezos left an empty chair in meetings to stand for the customer, the most important person in the room and the one not there to speak. It forced every decision to be argued from the customer's side of the table.

The mistake founders make is assuming their roadmap is customer-driven because they talk to customers. The tally usually says otherwise.

## Use it when

- The founder suspects the roadmap reflects their own taste or one big account.
- Features ship and land flat, and nobody can say why the idea was chosen.
- The team says "the CEO wanted it" more than "customers asked for it."
- Before #29 Idea Meritocracy Audit, to give that audit hard data.
- Before a roadmap planning session, as a reality check on the inputs.

## Before you start

Ask them to pull a list of the last 10 to 20 shipped features from release notes, the changelog, or the backlog tool. Twenty is better; fewer than ten won't show a pattern. If they can't remember where an idea came from, that is a finding. Tag the source "unknown" and note it: an untraceable roadmap is a process gap.

The canonical source tags are: support, sales, HIPPO, research, analytics, competitor, internal. Be strict about HIPPO. If the founder or an executive pushed it without customer evidence, it's HIPPO, even if a customer later liked it.

If a source can't be backed by evidence (a ticket, a call note, a data pull), tag it [Assumption].

## Run it

Loop steps 1 to 3 for each feature, then do the summary steps.

**Step 1 of 6: Feature**
> What's the next feature on your list?

Push for: a specific shipped thing, not a theme. Keep it to one line.

**Step 2 of 6: Source**
> Where did this idea actually come from: support, sales, HIPPO, research, analytics, competitor, or internal?

Push for: the true origin, not the justification added later. Probe: "Who first said it out loud, and did a customer say it before or after?" If two apply, pick the one that made it happen.

**Step 3 of 6: Impact, 1 to 5 (from the book)**
> How much did this move the business, on a scale of 1 to 5, and what's your evidence?

Push for: a number backed by a metric or customer response. If they have no measure, score it and tag it [Assumption]. This column matters later: high-impact ideas clustered in one source tell you which channel to trust more.

**Step 4 of 6: Tally**
> Let's count. How many came from each source, and what was the average impact for each?

Do the math for them and show the split as a short table. Name the largest source and the smallest. Point out any source with zero.

**Step 5 of 6: Read the mirror**
> Looking at this split, whose voice is loudest in your roadmap?

Push for: an honest answer. If HIPPO or internal leads, say so plainly. If user-voice sources (research, analytics, support) trail, ask: "What would have to change for the customer to be the loudest voice here?"

**Step 6 of 6: Top ten from each channel that matters**
> What are the top ideas you've heard from users directly, from your internal experts, and from industry trends, captured separately?

The book's rule: don't filter out any of the three channels that matter most, and capture at least the top ten ideas from each one independently. If they can't produce ten from users, that's the gap to close. Offer to start the lists now and finish them as homework.

## Push back when

- **Everything is tagged "research."** "Which interview or study? Name it, or it's internal."
- **HIPPO is under-counted.** "If you'd have built it without a single customer asking, that's HIPPO. Let's re-tag."
- **The founder is the HIPPO and defends it.** "Your instincts got you here. The audit just shows how often they went untested. When you're the HIPPO, your job is to listen to the other voices."
- **Impact scores are all 4s and 5s with no data.** "If you can't point to the needle, it's an assumption. Tag it and we'll check it in #33 Retrospective Canvas."
- **They want to skip the tally.** "The tally is the point. The biases only become obvious once the column is counted."

## Output

```
GROWTH BY DESIGN · Idea-Source Audit
[Company] · [Date] · [N] features reviewed

| Feature | Source | Impact 1 to 5 (from the book) | [Evidence/Assumption] |
| ... | ... | ... | ... |

Tally
Support _ · Sales _ · HIPPO _ · Research _ · Analytics _ · Competitor _ · Internal _ · Unknown _
Average impact by source: [ ]
Loudest voice: [source]  ·  Quietest voice: [source]

Top ten ideas, captured independently
Direct user feedback: [1 to 10]
Internal experts: [1 to 10]
Industry trends: [1 to 10]
```

**Coaching notes**: 3 to 5 sentences on what the split revealed, for example how much of the roadmap traces to the user's voice, whether HIPPO ideas underperformed, and which source produced the highest-impact work.

**Assumptions to test**: each [Assumption] impact score or source, with the data pull or customer check that would confirm it.

**Your next move this week**: one action, usually "put an empty chair, literal or written, into your next roadmap meeting: one customer quote or data point required before any idea moves forward."

## Done well

- At least ten shipped features, each with one source and an honest tag.
- HIPPO and internal are counted without softening.
- The founder can name the loudest voice in one sentence and sounds a little surprised.
- The three top-ten lists exist, or there's a dated plan to fill the user list.

## Next

- Run #29 Idea Meritocracy Audit to fix the process the tally exposed. Start #31 Customer Feedback Log if user-voice sources were thin.
- **Book pointer:** Chapter 15 also covers the three ways to gather feedback (ask, observe, analyze), the tools for each, and why personas built early stop representing the audience as you scale.
- **Coaching trigger:** HIPPO plus internal account for more than half the shipped features, or the founder can't trace the source of most of them.
