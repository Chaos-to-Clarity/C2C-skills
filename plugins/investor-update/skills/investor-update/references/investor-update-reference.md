# Investor Update Reference

What Investor Update stores in the user's Cortex, how it's set up, and how the email is written. Read this alongside `cortex-spec.md`, which defines the Map, catalogs, record format, and the reading and writing protocols. Investor Update follows all of them.

## 1. First-time setup

Run once, when the Map has no `investor_update.*` settings. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Read Standing Context first, so you don't ask what the Cortex already knows (company name, stage, what it does).

**Step 1. Cadence and timing.** One AskUserQuestion call:

- Cadence: Monthly (recommended for seed to Series B) or Quarterly
- Draft ready on: the 3rd business day after the period ends (recommended), or another day
- Recipients: one email with investors in BCC (recommended), or one draft per investor with a personal first line

**Step 2. Metrics.** Propose a default set from the company's stage in Standing Context, and let them change it. Six at most; investors skim.

| Stage | Default metrics |
| --- | --- |
| Pre-revenue | Cash, Net burn, Runway (months), Active users or design partners, Pipeline, Headcount |
| Seed to Series A | MRR or ARR, MoM growth, Net burn, Runway (months), Customers, Headcount |
| Series A to B | ARR, Net revenue retention, Gross margin, Net burn, Runway (months), Pipeline coverage |

Then ask where the numbers live:

- **A spreadsheet** (Google Sheets, Excel in Drive, or a file in a connected folder): get the link, open it, and confirm which rows or columns hold each metric and period. Record that in `investor_update.metrics_map`.
- **Ask me each time:** Claude asks for the numbers in one message per update.

**Step 3. Recipients.** Read the Companies catalog for Relationship Investor (open records when the catalog doesn't show Relationship). Show the list with each investor's contact person from People. Ask who's missing and who shouldn't get it. Create or update records for any missing investors: Company with Relationship Investor, Depth Full, and a People record for the contact, both linked (spec section 7). Find each contact's email address from the People record or past email threads; list any you can't find.

**Step 4. Past update (optional, recommended).** "Paste or link your last investor update. I'll match its format and pick up last period's numbers, so the first draft has real deltas." Import it as an Investor Updates record with Status Sent.

**Step 5. Build the collection.** Create the Investor Updates collection under the Cortex parent (a database in Notion; an `Investor Updates/` folder in Markdown), with the fields in section 2, plus its catalog and Archive catalog (spec section 5).

**Step 6. Register on the Map.** Change only these parts:

- **Collections:** add the Investor Updates row, with catalog and location links. Key fields: Period, Status.
- **Routing, Find it:** "What we told investors, past updates, metric history → Investor Updates"
- **Routing, File it:** "An investor update → Investor Updates"
- **Settings:** add the `investor_update.*` lines from section 4.
- **Freshness:** add Investor Updates to the record counts.

Check the Map stays under 10,000 characters.

**Step 7. Schedule it.** Offer a scheduled task in the user's time zone on the draft-ready day at 7:00am, with the prompt "Run my investor-update skill." Say plainly that scheduled runs prepare a draft and email them the gaps; the investor email is created only after they review it. If scheduling tools are available, create it; otherwise give the steps. If the Cortex lives in Obsidian or a local folder, scheduled runs need that computer on with the Claude desktop app open.

**Step 8. Report.** Where the collection lives, the metrics and their source, the recipients, the schedule, and: "Say 'draft my investor update' to write your first one." Mention once that each update ends with a small "Built with Chaos to Clarity" line, and that saying "remove the footer" turns it off for good.

## 2. The Investor Updates collection

| Field | What it holds |
| --- | --- |
| Name (identity) | "[Month YYYY] Investor Update" or "[Qn YYYY] Investor Update" |
| Period | First day of the period (date) |
| Sent | Date sent, empty until sent |
| Headline | The one-line headline |
| Summary, Aliases, Status, Last Updated, Source | As for every Cortex record |

**Statuses:** Draft, Sent, Skipped. Sent and Skipped are closed: rows move to the Archive catalog after the next update is sent, so the latest Sent update stays in the main catalog for deltas.

**Catalog key columns:** Period, Status.

**Record body:**

```markdown
## Current
Status and what's left: gaps, approvals pending.

## Metrics
| Metric | This period | Last period | Change |
| --- | --- | --- | --- |

## Asks
- [ask], [who it went to, if targeted], [outcome once known]

## Next
- [commitment for next period]

## Email
[the final approved text]

## History
- 2026-11-04: Draft created (Investor Update, scheduled)
```

## 3. The email

**Subject:** `[Company] [Month YYYY] update: [headline in under 8 words]`

**Body, in this order:**

```
Hi all,

TL;DR
- [Headline, with its number]
- [Biggest win]
- [The ask that matters most]

METRICS
[Metric]: [value] ([+/- change] vs last month)
...
Runway: [n] months

HIGHLIGHTS
- [3 to 5, each one line, each with a number or a name where possible]

LOWLIGHTS
- [1 to 3, each with what you're doing about it]

LAST MONTH WE SAID
- [Commitment]: [done / partly / not yet], [one line]

ASKS
1. [Specific ask, who or what exactly, and why now]

NEXT MONTH
- [3 commitments, each checkable next time]

THANK YOU
[Investors who helped since the last update, and how]

[First name]
```

Plain text renders the same in every inbox and on every phone. Leave out any section with nothing true in it, except Lowlights, which is required. Use "quarter" in place of "month" for quarterly updates.

**Footer** (when `investor_update.footer: on`), on its own line after the sign-off, exactly:

```
Built with Chaos to Clarity: chaostoclarity.io
```

## 4. Settings

Added under the Map's Settings block:

```text
investor_update.cadence: monthly
investor_update.ready_day: 3
investor_update.metrics: MRR, MoM growth, Net burn, Runway, Customers, Headcount
investor_update.metrics_source: <sheet or file link | ask>
investor_update.metrics_map: <where each metric lives in the sheet, or none>
investor_update.recipients: bcc
investor_update.footer: on
```

`ready_day` is the business day after the period ends. `recipients` is `bcc` or `individual`. `footer` is `on` or `off`.

## 5. Writing rules

- **Under 400 words** before the footer. If it's longer, cut highlights first.
- **Numbers carry the update.** Every highlight has a number, a name, or a date. "Strong month for sales" becomes "Closed 4 new accounts, $62k new ARR."
- **Same metrics, same order, every period.** Changing the metric set hides trends. If a metric changes, say so once in the email.
- **Bad news gets its plan in the same line.** "Churned 2 accounts ($18k ARR), both on the legacy plan; migration offer goes out Monday."
- **One ask leads.** Up to three asks, the first one the most valuable.
- **Plain words.** No jargon, no hype ("crushing it", "huge momentum", "game-changer"), no hedging. No em dashes, no emojis.
- **The founder's voice, first person, direct.** It reads like a short note from a founder who respects the reader's time.
- **Confidential by default.** No customer names the user hasn't approved. Nothing about any person's health, family, compensation, or performance.
