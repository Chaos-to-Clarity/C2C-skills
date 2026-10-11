# Customer Signal Reference

What Customer Signal stores in the user's Cortex, how it's set up, how themes work, and how the brief is written. Read this alongside `cortex-spec.md`, which defines the Map, catalogs, record format, and the reading and writing protocols. Customer Signal follows all of them.

## 1. First-time setup

Run once, when the Map has no `customer_signal.*` settings. Use AskUserQuestion for choices (up to 4 per call, recommended option first).

**Step 1. Check the inputs.** Confirm the meeting-notes source on the Map works: list the last week's meetings. Read the Companies catalog and count Customers and Prospects. If there are fewer than three, say the skill finds customer calls through those records, and offer to add the main accounts now (name and Relationship; they start as Stubs and fill in as calls come in).

**Step 2. Choices.** One AskUserQuestion call:

- Which conversations count: customer and prospect calls (recommended), or also partner calls
- Sources: meeting notes only (recommended), or meeting notes plus customer emails
- Where the weekly brief goes: email to me (recommended), or a document
- When it runs: Monday 7:00am (recommended), or Friday afternoon

Then show the default title keywords (demo, discovery, QBR, onboarding, renewal) and ask for any the team uses ("check-in", "pilot", "kickoff").

**Step 3. Build the collection.** Create the Customer Signals collection under the Cortex parent (a database in Notion; a `Customer Signals/` folder in Markdown), with the fields in section 2, plus its catalog and Archive catalog (spec section 5). In Notion, make Companies a two-way relation, so a Company record shows its themes.

**Step 4. Register on the Map.** Change only these parts:

- **Collections:** add the Customer Signals row, with catalog and location links. Key fields: Type, Strength, Last Seen.
- **Routing, Find it:** "What customers are asking for, complaining about, or praising; objections; churn risks; who asked for what → Customer Signals, then its Companies"
- **Routing, File it:** "Something a customer or prospect said about their needs, the product, pricing, or a competitor → Customer Signals (a theme), plus the Company's Open Thread for churn risk"
- **Settings:** add the `customer_signal.*` lines from section 6.
- **Freshness:** add Customer Signals to the record counts, and a "Customer signal" row under Last processed.

Check the Map stays under 10,000 characters.

**Step 5. Backfill (optional, recommended).** Offer to process the last 30 days of calls now, so the first brief has real counts. Run Steps 1 to 4 of the skill with a 30-day look-back. Skip the brief for the backfill; report the themes it found instead.

**Step 6. Schedule it.** Offer a weekly scheduled task at the chosen time, in the user's time zone, with the prompt "Run my customer-signal skill." If scheduling tools are available, create it; otherwise give the steps. If the Cortex lives in Obsidian or a local folder, scheduled runs need that computer on with the Claude desktop app open.

**Step 7. Report.** Where the collection lives, which calls it watches, when it runs, the backfill's top three themes, and: "Ask me 'what are customers saying about [topic]' any time."

## 2. The Customer Signals collection

Each record is one theme: an underlying customer need, with the evidence of every account that raised it.

| Field | What it holds |
| --- | --- |
| Name (identity) | The theme, in a customer's words: "SSO for enterprise rollout", "Setup takes too long" |
| Type | Pain, Request, Objection, Churn Risk, Praise, Competitor |
| Pillar | The Growth by Design pillar (section 4) |
| Companies | Relation to every Company that raised it |
| Initiatives | Relation to the Initiative addressing it, if any |
| Mentions | Separate conversations that raised it |
| Accounts | Number of distinct Companies linked |
| Strength | Weak (1 to 2 accounts), Emerging (3 to 4), Strong (5 or more). Blocking weight or money at stake moves it up one level |
| First Seen, Last Seen | Dates |
| Summary, Aliases, Status, Last Updated, Source | As for every Cortex record |

**Statuses:** Active, Addressed, Dismissed, Archived. Addressed, Dismissed, and Archived are closed and move to the Archive catalog. An Addressed theme that comes back in a new call reopens as Active, with a History line saying so.

**Catalog key columns:** Type, Strength, Last Seen.

**Record body:**

```markdown
## Current
What customers want, in their language, in two or three lines. Who it matters most to, and what's at stake.

## History
- 2026-10-08: Acme, Jane Rivera (CRO), discovery: needs SSO before rolling out past 200 seats. Blocking, $48k deal
- 2026-09-30: Beta, onboarding call: IT won't approve without SAML. Important
```

**Theme rules**

- **One need per theme.** "SSO" and "Audit logs" are two themes even when the same buyer asks for both.
- **Name the need in the customer's terms.** "Can't see team usage" beats "Admin dashboard."
- **Merge on meaning.** "Onboarding is slow", "took us three weeks to get live", and "setup is painful" are one theme. Keep the variants as Aliases.
- **Split when the reason differs.** "Too expensive for a small team" (Model) and "Can't justify the price without ROI data" (Outcomes) are different themes.
- **Praise is a theme too.** What customers love, in their words, is the raw material for messaging.

## 3. Signal types

| Type | It's this when the customer | Example |
| --- | --- | --- |
| Pain | Describes a problem they live with, in or around the product | "We rebuild this report by hand every Friday" |
| Request | Asks for something the product doesn't do | "Can it push to Slack?" |
| Objection | Gives a reason not to buy, expand, or renew | "Legal won't sign off without SOC 2" |
| Churn Risk | Signals they might leave or shrink: a budget cut, a champion leaving, low use, a competitor trial, a frustrated tone at renewal | "We're reviewing all tools in Q1" |
| Praise | Says what's working and why | "My team stopped asking me for status" |
| Competitor | Names a competitor or alternative, and what they compare | "Linear does this out of the box" |

## 4. Growth by Design pillar map

Map each theme to the pillar it reveals. When two fit, choose the one the fix would live in.

| Pillar | Themes that point here |
| --- | --- |
| Problem | Pains that aren't urgent, or aren't the problem the product solves |
| Solution | Requests and gaps in what the product does |
| Experience | Setup, onboarding, usability, speed, reliability |
| Differentiation | Competitor comparisons, "why not just use X" |
| Outcomes | Unclear ROI, "can't prove it's working", results praise |
| Persona | The wrong buyer, the user isn't the buyer, champion problems |
| Messaging | Confusion about what the product does or who it's for |
| Channel | How they found you, or couldn't |
| Model | Pricing, packaging, seat or usage objections |
| Timing | "Not now", budget cycles, market shifts |

## 5. The brief

This structure. No preamble. Leave out any section with no signal rather than writing "nothing to report."

**HEADLINE**
One line: the one thing customers told you this week that matters most, with its count.

**CHURN RISKS**
`[Account], [what was said], [ARR or renewal date if known], [suggested move and owner]`
First, always, when there are any.

**RISING**
Themes that gained accounts this week, most new accounts first.
`[Theme] ([Type]): +[n] this week, [total] accounts. [Strongest quote or line]. [Money at stake if known]`

**NEW**
First-time themes worth watching. One line each.

**OBJECTIONS**
What's slowing or blocking deals, with how many deals and the dollar value when known.

**PRAISE**
What customers love, in their words. One line each. Note when a phrase would make good messaging.

**PMF READ**
Which pillar is generating the most pain this week and across the last month, in two sentences. If the growth-by-design skill is installed, name the one exercise to run on it (for example, "#20 Messaging Canvas: three prospects this week couldn't say what you do").

**ONE MOVE**
The single highest-return action this week, and one line on why it beats the rest. Close-the-loop notes count: "SSO shipped Tuesday. 9 accounts asked for it. Send the notes."

**Writing rules:** short lines, numbers first, customers' own words where they matter. Name accounts in the brief (it's internal). No em dashes, no emojis, no hype.

## 6. Settings

Added under the Map's Settings block:

```text
customer_signal.lookback_days: 7
customer_signal.sources: meetings
customer_signal.include_partners: off
customer_signal.title_keywords: demo, discovery, QBR, onboarding, renewal
customer_signal.deliver: email-me
```

`sources` is `meetings` or `meetings+email`. `deliver` is `email-me` or `doc`.
