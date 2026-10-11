---
name: investor-update
description: Drafts the monthly investor update from your Cortex: metrics with deltas, highlights, lowlights, what you promised last time, and specific asks. Saves a draft, never sends.
---

# Investor Update

Draft the founder's investor update from what their Cortex already knows: the metrics, what moved, what didn't, what they promised last time, and the asks that would actually help. The founder reviews and sends. Built to run monthly on a schedule, and on demand: "Draft my investor update", "Investor update for September".

Read `references/cortex-spec.md` (Map, catalogs, reading and writing protocols) and `references/investor-update-reference.md` (the collection, settings, email format, and writing rules). If the Map lists the Founder OS collections, also read `references/founder-os.md`.

Investor updates are high stakes. Every number comes from the user or their metrics source, never from an estimate. A draft is always a draft: never send an update, in any mode.

## Step 0. Cortex and setup

Find and validate the Cortex Map (spec section 4).

- **No Map:** Investor Update runs on a Cortex. Say so in one line and offer cortex-setup if it's installed. Stop.
- **Map has no `investor_update.*` settings or no Investor Updates collection:** run first-time setup (reference section 1), then continue to Step 1 if the user wants a draft now.
- **Set up:** continue.

## Step 1. Pick the period

Default to the last full period (`investor_update.cadence`): the month just ended, or the quarter just ended. The user can name another. Check the Investor Updates catalog for that period:

- **Sent:** say so, link it, and stop unless they want a revision.
- **Draft:** resume it. Show what's filled and what's missing.
- **None:** start a new one.

## Step 2. Gather, in parallel

Pull everything before writing a word. If a source is unavailable, note it in one line and continue.

1. **The last update.** The previous Investor Updates record: its metrics (for deltas), its asks (who helped?), and its "Next" commitments (did they happen?).
2. **Metrics.** For each metric in `investor_update.metrics`:
   - `investor_update.metrics_source` is a sheet or file: read this period's values from it. If a value is missing or the period isn't there yet, leave it as a gap.
   - `ask`: list every metric with last period's value beside it and ask for all of them in one message: "MRR (last month $84k)?" In a scheduled run, leave them as gaps.
   - Compute changes yourself: absolute and percent against last period. Runway in months is cash divided by average net burn of the last three periods, when both are known. Show your arithmetic in the review, not in the email.
3. **Cortex, through the Map and catalogs** (spec section 6):
   - Standing Context and the Strategy summary: what the company is chasing, so the headline ties to it.
   - Initiatives: Done or moved this period (Last Updated in the period, History lines dated in it), and any with a Blocker. Blockers are the best source of asks.
   - Decisions: Decided this period. Big calls (a pivot, a key hire, a pricing change) belong in the update.
   - Companies: new Customers this period, lost ones (closed or Archived), and Investors (the recipients).
   - **Customer Signals**, if the Map lists it: the strongest one or two themes and any churn risk on a named account.
   - **Team**, if the Map lists it: hires and departures this period, as counts and roles only. Nothing from 1:1 notes, ever.
   - **Founder OS Reflections**, if listed: the Wins and Top Lesson lines from this period's weeks. Never the Health, Family, or Energy fields.
4. **Format reference.** If a past update was imported at setup, match its section order and length.

## Step 3. Draft

Build the email in the format in reference section 3, with the writing rules in section 4.

- **Headline:** the single most important thing that happened, stated with its number.
- **Lowlights are required.** Investors trust founders who report bad news early. If the sources show none, ask the user for the one thing that went worse than planned. Never invent one, and never leave the section out.
- **Asks are specific.** A named intro ("an intro to a VP Eng who has scaled a team from 15 to 50"), a hire, a decision they want input on. Pull from Initiative blockers first. "Any intros welcome" is not an ask.
- **Last time we said:** each "Next" commitment from the last update, marked done, partly done, or not done, with one line why. Skip on the first update.
- **Thanks:** name investors who delivered on last period's asks. Ask the user who helped; never guess.
- **Customer names:** list every customer, prospect, or partner named in the draft and ask whether each can be named. Some are under NDA.
- **Voice:** if a voice skill built by the Voice plugin is installed (a skill whose description says it writes in the user's voice), load it and follow it. Otherwise use the plain founder voice in reference section 4.
- **Footer:** add it when `investor_update.footer` is `on` (the default), exactly as in reference section 3.

Write the draft to a file first and check it mechanically: no em dashes, no gap markers left, every number traceable to a source.

## Step 4. Review with the user

Show the full draft in the conversation, then in one message:

- **Gaps:** every missing number or fact, as a list.
- **Check:** each computed change with its arithmetic, and each customer name to approve.
- **Push:** one line of coaching where the draft is softer than the facts. For example: "Runway dropped from 19 to 14 months and it's in the table but not the TL;DR. Investors will see it. Say it first, with the plan."
- Ask: "Anything to change before I make it a draft email?"

Iterate until they approve. A request like "remove the footer" or "turn off the footer" changes the draft and sets `investor_update.footer: off` on the Map, so it stays off. Tell them it's off for good and they can turn it back on the same way.

**Scheduled runs:** no one is there to review. Save the record as Draft with its gaps listed at the top, and send the user one short email from `sources.email`: subject "Investor update for [period] is ready to review", the gaps, and "Say 'finish my investor update' to review it." Never create the investor email in a scheduled run.

## Step 5. Create the email draft

Once the user approves, create the draft in the email tool from `sources.email` (Gmail or Outlook):

- `investor_update.recipients: bcc` (default): one draft to the user, investors in BCC.
- `individual`: one draft per investor, same body, with a first line personalized from that investor's Company or People record (what they helped with, or the ask that fits them). Show the openers before creating them.

Recipients are People linked to Companies with Relationship Investor, Status Active. Use the address from the People record or the user's past email threads with them. If a recipient has no known address, list them and ask. Never add anyone who isn't an investor without the user's say.

Never send. Tell them where the draft is.

## Step 6. Save to the Cortex

Follow the Writing protocol (spec section 7):

- **The Investor Updates record** for the period (reference section 2): metrics, headline, asks, Next commitments, Status Draft, Last Updated today, Source "Investor Update [period]". Update its catalog row.
- **Asks on investor records:** when an ask targets a specific investor, update that Company record's Open Thread and add a History line, so the next update can thank them or follow up.
- **Decisions:** if writing the update surfaced a call the user made (a new target, a plan to extend runway), offer to log it as a Decision. Offer only.
- **Ingest Log:** one row, Source "Investor Update [period]", Type Document, What Changed = record created or updated, draft created.

**Marking it sent.** At the start of every run, and on "I sent it", check sent mail for the update's subject. When found, set Status Sent and Sent to that date, and update the catalog row.

## Step 7. Close

One line: where the draft is, what's left to fill, and the one ask most worth chasing this month.

## Output rules

- Numbers only from the user or their metrics source. A missing number stays a visible gap until the user fills it.
- Short beats complete. Investors read updates on their phones in under two minutes.
- Bad news early, with the plan next to it.
- Nothing from 1:1s, Reflections health fields, or private meetings goes in an update.
