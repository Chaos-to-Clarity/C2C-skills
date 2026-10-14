# One-on-Ones Reference

What One-on-Ones stores in the user's Cortex, how it's set up, the privacy rules, and the output formats. Read this alongside `cortex-spec.md`, which defines the Map, catalogs, record format, and the reading and writing protocols. One-on-Ones follows all of them.

## 1. First-time setup

Run once, when the Map has no `one_on_ones.*` settings. Use AskUserQuestion for choices (up to 4 per call, recommended option first).

**Step 1. Find the 1:1s.** Read the calendar (`sources.calendar`) for the next four weeks. List recurring events with exactly two attendees, the user and one other person. Resolve each person through the Glossary and People catalog. Show the list: "These look like your 1:1s. Which are direct reports?" Ask who's missing.

**Step 2. Each direct report.** For each person confirmed:

- Their People record: create it or promote it to Full (a direct report is a working relationship, spec section 2), with Role and Company set to the user's own company.
- Their Team record (section 2): Role, Cadence (from the calendar: weekly, biweekly, monthly), Calendar match (the event title, or "recurring with [name]"), Next 1:1, Health Green, and Started if the user knows it.
- One question per person, all in one message: "What's the one thing you want [name] to grow in this year?" That's their Growth Focus. "Skip" is fine; the team review will flag it later.

A roster change later runs this step for one person. Someone who left: set the Team record's Status Left and its People record's Status Dormant, and add History lines to both. Never delete.

**Step 3. Choices.** One AskUserQuestion call:

- Prep delivery: an email to me each morning with that day's 1:1s (recommended), or only when I ask
- Prep time: 7:00am on work days (recommended), or another time
- Share an agenda with the report: off (recommended), or a draft agenda to them before each 1:1
- Monthly team review: first Monday of the month (recommended), or off

**Step 4. Recap.** If a Recap Config exists, explain that Recap would otherwise email a recap of a 1:1, and offer to add each 1:1's Calendar match to `recap.skip_if_title_contains`, so One-on-Ones owns them entirely. Make the change only on a yes. Recommend yes.

**Step 5. Build the collection.** Create the Team collection under the Cortex parent (a database in Notion; a `Team/` folder in Markdown), with the fields in section 2, plus its catalog and Archive catalog (spec section 5). In Notion, make Person a two-way relation to People. Tell the user plainly: anyone with access to the Cortex can read the Team records, so keep the Cortex private or limit sharing on that database or folder.

**Step 6. Register on the Map.** Change only these parts:

- **Collections:** add the Team row, with catalog and location links. Key fields: Health, Next 1:1, Cadence.
- **Routing, Find it:** "Direct reports, 1:1 prep, what someone owes the owner or is owed, how the team is doing → Team, then the person's People record and Initiatives"
- **Routing, File it:** "Anything from a 1:1 with a direct report → Team (never People, Inbox, or Standing Context)"
- **Settings:** add the `one_on_ones.*` lines from section 6.
- **Freshness:** add Team to the record counts.
- **Glossary:** no new rows. Direct reports already have People entries.

Check the Map stays under 10,000 characters.

**Step 7. Schedule it.** Offer two scheduled tasks in the user's time zone: daily on work days at the prep time with the prompt "Run my one-on-ones skill.", and the monthly review with "Run my one-on-ones skill in team review mode." If scheduling tools are available, create them; otherwise give the steps. If the Cortex lives in Obsidian or a local folder, scheduled runs need that computer on with the Claude desktop app open.

**Step 8. Report.** Who's on the team and their cadences, where the Team records live, what's scheduled, and: "Say 'prep my 1:1 with [name]' any time."

## 2. The Team collection

One record per direct report.

| Field | What it holds |
| --- | --- |
| Name (identity) | The person's name, exactly as their People record |
| Person | Relation to their People record |
| Role | Their role |
| Cadence | Weekly, Biweekly, Monthly |
| Calendar match | How their 1:1 appears on the calendar |
| Started | Date they started in the role, if known |
| Growth Focus | The one thing they're growing in, in a few words |
| Health | Green, Yellow, Red |
| Last 1:1, Next 1:1 | Dates |
| Summary, Aliases, Status, Last Updated, Source | As for every Cortex record. Summary stays neutral: role and focus, never Health or performance |

**Statuses:** Active, Left. Left is closed and moves to the Archive catalog.

**Catalog key columns:** Health, Next 1:1, Cadence.

**Health**

| Flag | Means |
| --- | --- |
| Green | Delivering, engaged, commitments kept |
| Yellow | One of these, for two 1:1s running: commitments slipping, the same blocker unresolved, energy or engagement down in what they said, a growth focus stalled |
| Red | Yellow for a month, a commitment missed that hurt the business, or they said they're unhappy or thinking of leaving |

**Record body:**

```markdown
## Current
What they're working on, what they need from the owner, how things stand. Three lines.

## Open Commitments
**They owe**
- [ ] [Commitment] (due [date], from [date] 1:1)
**You owe**
- [ ] [Commitment] (due [date], from [date] 1:1)

## Themes
- [Theme]: [n] times, last [date]

## History
- 2026-10-09: Hiring plan for Q1 agreed; asked for budget clarity again; growth focus on delegation, first progress
```

Closed commitments move into the History line of the 1:1 that closed them and leave Open Commitments.

## 3. Privacy rules (always on, never a setting)

These override every other setting and every other skill.

- **Nothing from a 1:1 leaves the Team record and the user's own inbox.** Never in a recap email, a shared doc, an investor update, a content draft, a brief to anyone else, or a draft to the report beyond the agenda topics.
- **Never store health, family, relationships, finances, compensation, immigration status, legal matters, or anything said in confidence.** If a report shared something personal, write only "Personal matter raised; check in" in History, with no detail, and only if the user wants a reminder.
- **No performance verdicts in the Cortex.** Store what was said and done, with dates. Health is the only judgment field, and the user sets it.
- **No psychological labels or inferences.** Write "Missed two deadlines on the migration." Never write "disengaged" or "burned out" unless they said it.
- **People records stay neutral.** A role change goes there. Nothing else from a 1:1 does.
- **The Ingest Log carries no content.** "Team record updated" only.
- **Other skills don't read Team content.** Investor Update may count hires and departures from Team Status. Daily briefings may show that a 1:1 is today and link the prep. Nothing more.

## 4. Output formats

No preamble. Short lines. Leave out any section with nothing in it.

### Prep

```
1:1 WITH [NAME], [time]  [Health flag if Yellow or Red]

YOU OWE
- [Commitment], due [date] [OVERDUE if so]

THEY OWE
- [Commitment], due [date] [OVERDUE if so]

SINCE LAST TIME ([date])
- [What moved or got stuck on their initiatives, with dates]

THEMES
- [Theme], raised [n] times. [One line on what that suggests]

ASK THEM
1. [On their growth focus]
2. [On the biggest blocker]
3. [Open: what do they need from you]

YOUR ONE THING
[The one message, decision, or piece of feedback to deliver this time, and why now]

[Coach routing line, if a pattern fits: "Third week the hiring plan has slipped. The Toleration Audit fits. Want to run it before the 1:1?"]
```

### Team review

```
TEAM REVIEW, [Month YYYY]

| Person | Health | Last 1:1 | Missed | Open (they / you) | Top theme |

ACROSS THE TEAM
- [Shared themes, with who raised them]
- You owe [n] commitments, [n] overdue
- [Cadence misses]

WATCH
- [Name]: [the pattern, with evidence]

ONE MOVE
[The one conversation or fix that helps the team most this month]
```

## 5. Coach routing

When a Chaos to Clarity Coach skill that carries the tool is installed (the all-in-one `c2c-coach`, or the theme plugin named below), offer the tool by name. When none is, name the pattern and the move without the tool reference.

| Pattern | Tool | Theme plugin |
| --- | --- | --- |
| Standards slipping, the user accepting work below the bar | Toleration Audit | `c2c-coach-people` |
| A conversation the user keeps putting off, or Red health | Hard Conversation Protocol | `c2c-coach-people` |
| Work comes back wrong, or the same handoff fails twice | CLEAR Expectations Framework | `c2c-coach-people` |
| Their decisions keep escalating to the user | Authority Audit | `c2c-coach-people` |
| Two reports in conflict over ownership | Object-Oriented Management | `c2c-coach-scale` |
| Their whole function is underperforming | Functional Scaling Redesign | `c2c-coach-scale` |
| The user is the recurring blocker across several reports | Identity Ceiling Tool | `c2c-coach-focus` |

## 6. Settings

Added under the Map's Settings block:

```text
one_on_ones.prep_delivery: email-me
one_on_ones.prep_time: 07:00
one_on_ones.share_agenda: off
one_on_ones.team_review: monthly
```

`prep_delivery` is `email-me` or `chat`. `team_review` is `monthly` or `off`.
