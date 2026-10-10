# 06. The Yellow Brick Road

| | |
| --- | --- |
| Pillar | Core framework (Solution) |
| Read alongside | Chapter 5, "Sell It Before You Build It" |
| Workbook | page 13 |
| Time | 45 to 60 minutes |
| Lifts | Solution 1, 4, Outcomes 1 |
| Feeds from | #4 From Suck to Awesome, #11 Problem Canvas, #12 Jobs-to-Be-Done Canvas |
| Feeds into | #13 Validation Canvas, #14 Experience Canvas, #16 Feature Prioritization Matrix |

## Why it matters

Production-ready software is still the most expensive cost in the business and the hardest to change once it's built. Chapter 5's insight: test, test, test, and don't invest a ton of time and money in an untested idea. Prove it while it's still cheap to be wrong.

Most people confuse an MVP with a prototype. An MVP is fleshed out enough that someone will use it, and maybe pay for it. Anything less is a prototype. Plan to iterate through several prototypes, validating with beta users, until you have something that can go to market. The MVP's purpose is to gain traction and gather feedback. It may be missing features it would need to beat the competition. The point is to get something into users' hands that solves their problem as early as possible.

Deciding what goes in is the hard part. You have a grand vision, and cutting anything feels like failure. So focus on what's most valuable from the customer's point of view, the goals they're trying to accomplish, and build only the features that take them straight there. That's the Yellow Brick Road: the direct path from where the customer starts to the goal they came for. Every feature off that path waits for a later version. The book's diagram sorts the off-road features into nice-to-have, later, and someday (from the book). The more you build before launch, the longer you wait for traction and revenue. The book quotes Reid Hoffman: "If you are not embarrassed by the first version of your product, you've launched too late."

Figma is the book's example of iterating instead of betting on one release: they spent years in private beta, refining the product with designers before launching publicly. The mistake founders make is treating the grand vision as the first release, because cutting anything feels like failure.

## Use it when

- The MVP feature list keeps growing and launch keeps slipping.
- The founder can't say which single goal the first release delivers.
- The team argues about scope with no shared rule for what's in.
- They're about to commit engineering budget to a first build.

## Before you start

You need the customer's most important goal. Pull it from #4 From Suck to Awesome (the one problem to solve first) or #12 Jobs-to-Be-Done Canvas. If neither exists, ask the founder to state it and tag it [Assumption]. The road is only as good as the goal at the end of it, so that assumption becomes the first thing to confirm with customers.

Ask for their full wish list of features up front. Expect it to be long; that's the point.

## Run it

This runs the book's 8-step "Define the MVP" exercise, then sorts the result onto the road. Steps 3, 5, and 6 loop through features.

**Step 1 of 8: The essential goals**
> What are the absolutely essential goals your product helps users achieve? Keep it to the ones they came for.

Push for: one to three goals in customer terms, ideally in their words. If a goal is a feature ("use our dashboard"), ask: "What are they trying to get done?" Mark the most important one as THE GOAL.

**Step 2 of 8: Every feature**
> List every feature you'd like in your first release. Everything, no filtering yet.

Push for: the whole list, including the ones they're attached to. Cutting comes next.

**Step 3 of 8: Impact on a goal (loop)**
> For this feature, what's its impact on an essential goal: Low, Medium, or High?

Push for: a rating tied to a specific goal, and evidence where it exists. Probe: "Which customer would miss this if it weren't there?"

**Step 4 of 8: First cut**
> Anything not rated High is out. Which of these cuts hurts most, and why?

Push for: acceptance, not renegotiation. Anything that wasn't High goes OFF the road. Let them say why it hurts, then move on.

**Step 5 of 8: The two-part test (loop)**
> Could the system function without this feature, and could the user reach the goal without it?

Push for: two honest answers. If both are yes, it's out. If either is no, it stays. Probe: "Could they reach the goal with a manual workaround for now?"

**Step 6 of 8: Strip it down (loop)**
> What's the most stripped-down version of this feature that still lets the system function and the user reach the goal?

Push for: the smallest version, not the ideal one. Hard-coded data, a manual step behind the scenes, or a part marked "coming soon" are all fair. The book says it's fine to have parts of the MVP marked "coming soon."

**Step 7 of 8: Lay the road**
> Put the survivors in order from START to THE GOAL. Does each one move the customer one step closer?

Push for: a clean sequence of core features. Anything that doesn't advance the customer gets moved OFF, sorted into nice-to-have, later, or someday.

**Step 8 of 8: Describe it to users**
> Who will you describe this stripped-down product to this week, and what will tell you they'd use it?

Push for: named users and a clear signal. If it still makes sense to them and they'd use it, that's the MVP. If not, the road is missing a step or the goal is wrong.

## Push back when

- **The MVP is the grand vision.** "Every feature that isn't on the path to the goal waits for a later version. Which of these could wait?"
- **Medium keeps getting promoted to High.** "Anything you didn't score High is out. The more you build before launch, the longer you wait for traction."
- **They want it polished first.** "If you are not embarrassed by the first version, you've launched too late."
- **The goal is the founder's.** "Whose goal is this? Show me the customer who said it."
- **They call a prototype an MVP.** "Would someone use this for real, and maybe pay for it? If not, it's a prototype. That's fine; call it one."

## Output

```
GROWTH BY DESIGN · The Yellow Brick Road
[Company] · [Date]

THE GOAL: [the customer's most important goal]  [Evidence/Assumption]
Other essential goals: [ ]

START -> [Core feature, stripped] -> [Core feature, stripped] -> [Core feature, stripped] -> THE GOAL

ON THE ROAD (build now: takes the customer toward the goal) | OFF THE ROAD (defer: everything else, until the path works)
[feature: stripped-down version]     | [feature] · nice-to-have / later / someday (from the book)
[ ]  [Evidence/Assumption]           | [ ]

Feature ratings: [feature] · Impact [L/M/H] · System needs it [y/n] · User needs it [y/n]
User check: described to [names] · response [ ]  [Evidence/Assumption]
```

**Coaching notes**: 3 to 5 sentences: how much the list shrank, which cut was hardest and why, whether the goal is grounded in customers, and whether the result is a true MVP or still a prototype.

**Assumptions to test**: each [Assumption] with the cheapest test, usually describing the road to three users or a clickable prototype.

**Your next move this week**: describe the ON THE ROAD product to three target users and ask whether they'd use it.

## Done well

- Every ON feature has High impact on THE GOAL, and the system or the user can't do without it.
- Each ON feature is the stripped-down version.
- The OFF list is longer than the ON list.
- Real users have heard the description, or a date is set.

## Next

- Run #13 Validation Canvas on the riskiest assumption behind the road. Map the path to the Aha Moment in #14 Experience Canvas. Rank the OFF list later with #16 Feature Prioritization Matrix.
- **Book pointer:** Chapter 5 covers proving demand with a landing page and ads before you build, keeping prototypes deliberately ugly to get honest feedback, and the full Figma story.
- **Coaching trigger:** the founder can't cut the list below their original scope, or there's no single customer goal they can name.
