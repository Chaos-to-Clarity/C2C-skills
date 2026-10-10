---
name: add-to-cortex
description: Digests one document (pasted, attached, or a named file or link) into the user's Cortex, routing people, initiatives, decisions, and context to the right place without duplicates.
---

# Add to Cortex

Digest one document into the user's Cortex. Use this for a single doc. For a folder of strategy documents, use strategy-digest. For a sweep of recent meetings and email, use cortex-update.

Read `references/cortex-store.md` first, then load the Cortex Config (section 3). If there's no config, offer to run cortex-setup and stop.

## Step 1. Read the rules and the map

Read the Cortex Schema page and the Overview, every time. Don't rely on memory of the rules; the user may have changed them or added collections.

## Step 2. Get the document

| Source | Action |
| --- | --- |
| Pasted text | Use it directly |
| Attached file (PDF, DOCX, image, slides) | Read it with file tools |
| A file name or link in their document source | Search for it; if several match, ask which one |
| A page in their Cortex backend or another app | Open it with that connector |

If the source is ambiguous, ask before reading.

## Step 3. Check the Ingest Log

If this exact source is already logged, tell the user when it was ingested and stop, unless they say re-ingest.

## Step 4. Extract what's durable

Keep only what stays true for weeks or months. Drop task noise, logistics, and one-off follow-ups.

| What it is | Goes to |
| --- | --- |
| A person they deal with: role, context, open thread | People |
| Something they're driving, with a next action | Initiatives |
| A call made, or an open question, with reasoning | Decisions |
| Positioning, ICP, GTM, brand, targets | Strategy page |
| Durable facts about the business or their role | Standing Context |
| Anything fitting a collection the user added (listed on the Overview) | That collection |

Write each item in the user's words. Condense.

## Step 5. Route and write

For each item, find the existing record by identity first (store reference, section 4).

- **New:** create it with Status Active (or Open for an undecided question), Last Updated today, Source = the document's name.
- **Updates an existing record:** change it in place, refresh Last Updated and Source.
- **Conflicts with an existing record** (role changed, decision reversed): don't overwrite silently.
  - People: update in place and note the old value in the report, or set Status to Dormant or Archived if they've moved on.
  - Initiatives: set Done or Dropped if it ended; never delete.
  - Decisions: set the old record to Reversed or Superseded, create the new one, and set Supersedes to the old title.
- **Strategy page:** add a dated section for this document; refresh the Strategy Summary only if positioning, ICP, GTM, targets, or brand changed. Never delete earlier sections.
- **Standing Context:** surgical edits only.
- **Fits nothing and looks like a new category** (Customers, Competitors, Portfolio): propose a new collection in one line with the reason, and wait for a yes before creating it.

Link relations where the document makes them obvious.

## Step 6. Log the ingest

One Ingest Log row: Source = document name, Type = Document, Meeting Notes, Email, or Strategy (whichever fits), Date Ingested today, What Changed = "X created, Y updated, Z superseded" with names.

## Step 7. Report

Tight: one short paragraph or a small table.

- Added (what and where)
- Updated in place
- Superseded, and why
- The log entry
- Anything thin, ambiguous, or skipped, with a question to sharpen it
