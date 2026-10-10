---
name: cortex-setup
description: Builds the user's Cortex, the context layer their AI reads first, in Notion, Obsidian, or Google Drive, and fills it with their people, initiatives, and decisions. Run once.
---

# Cortex Setup

Build the user's Cortex: a small, structured store of what stays true about their work, which every other skill reads before acting. Then fill it with real context. Run once. If a Cortex already exists, build on it and never overwrite.

Read `references/cortex-store.md` first. It defines the model, the backends, the config format, and the rules.

Keep the user moving. Use AskUserQuestion for choices (up to 4 per call, recommended option first). Do discovery silently before asking.

## Step 1. Check for an existing Cortex

Look for a Cortex Config (store reference, section 3). If one exists and validates, tell the user their Cortex is already set up, show where it lives, and offer to: fill thin collections (Step 6), add a source, or change a setting. Stop there unless they pick one.

Also look for an older "Brain" setup: a page named like "Brain", "Second Brain", or "My Brain" holding People, Initiatives, and Decisions databases. If found, offer to adopt it as the Cortex: map its collections and fields into the config, keep its names, add any missing pages. Never move or rename the user's existing pages without asking.

## Step 2. Choose where the Cortex lives

Ask:

- **Notion** (recommended if they use Notion): databases with relations, easiest to browse and edit.
- **Obsidian**: Markdown files in their vault, linked with wikilinks.
- **Markdown in Google Drive**: plain files in a Drive folder, readable by any tool.
- **Something else**: a local folder, or another app with a connector.

Then confirm access:

- Check the matching connector or folder tool is available. If it isn't, search the connector registry and suggest it. For Obsidian or a local folder, the Claude desktop app must connect the folder; tell the user how, and that scheduled runs need that computer on.
- Ask where to put it: a parent page in Notion, or a folder. Default name: "Cortex".
- Do a test write: create the parent page or folder. If it fails, report the error plainly and stop until access works. Never build on a broken connection.

## Step 3. Connect sources

Ask which tools they use. Detect what's already connected and pre-select it.

- Meeting notes: Granola, Fireflies, Otter, Fathom, Notion meeting notes, a notes folder, or none
- Calendar: Google Calendar, Outlook, the device calendar, or none
- Email: Gmail, Outlook, or none
- Documents: Google Drive, Dropbox, OneDrive, Box, or none

For each one named, do a small test read (one recent meeting, today's events, one recent thread, one file). Report each as connected or not. For any that fail, name the connector to authorize, suggest it from the registry, and continue with the rest. Missing sources reduce what the Cortex learns; they don't block setup.

## Step 4. Build the structure

Create, under the parent, in this order (store reference, sections 1, 5, and 6):

1. **Cortex Schema** page: write the rules from section 6 word for word.
2. **Overview** page: an empty Synthesis section at the top, then one line per page and collection with its purpose, then a short "How to read the Cortex" note: Overview first, then only the collection you need, filtered to Active.
3. **People**, **Initiatives**, **Decisions** collections with the fields in section 1.
4. **Standing Context** page.
5. **Strategy** page, empty, with a note that strategy-digest fills it.
6. **Ingest Log** collection.

Relations:

- Notion: on Initiatives add a relation to People named "Owner / Involved" (two-way, shows on People as "Initiatives"). On Decisions add a relation to Initiatives named "Affects" (two-way, shows on Initiatives as "Decisions").
- Markdown: relations are wikilink lists in frontmatter. Create each collection folder with an empty `_index.md` holding just the header row.

## Step 5. Save the config

Write the Cortex Config page or file under the parent, in the format in section 3, with every location filled in. Ask one question to set `update.approval`:

- **Apply updates and report** (recommended, required for scheduled runs)
- **Show me edits first**

Add a line for Cortex Config on the Overview.

## Step 6. Fill it with real context

1. **Draft from sources.** If meeting notes or calendar are connected, scan the last 30 days. Draft People records from recurring names and a first pass at Initiatives from recurring themes. Show both lists before writing anything.
2. **Interview, one collection at a time:** People, then Initiatives, then Decisions, then Standing Context. Three to seven records each to start. Push for specifics:
   - Every person needs the one thing worth remembering.
   - Every initiative needs a Next Action.
   - Every decision needs its reasoning.
   - If an answer is vague, say so and ask them to sharpen it before saving.
3. **Write** each record with Status Active, Last Updated today, and a Source ("Setup interview" or the meeting it came from). Link relations where obvious.
4. **Synthesis.** Write a one-paragraph read on where things stand at the top of the Overview.
5. **Log** one Ingest Log row: Source "Cortex setup", Type Document, What Changed = counts per collection.

## Step 7. Offer the routine

Offer to schedule **cortex-update** weekly (suggest Sunday at 5pm in their time zone). If scheduling tools are available in this session, create a scheduled task whose prompt is: "Run my cortex-update skill." Otherwise give the user the steps to add a weekly scheduled task with that prompt. Note that scheduled runs need `update.approval: autonomous`.

## Step 8. Report

Short:

- Where the Cortex lives, with a link
- Records created per collection
- Sources connected and any that failed
- What's thin and worth filling next
- Next steps: strategy-digest to fill Strategy, add-to-cortex for any document, ask-cortex to query it, and founder-os-setup to add the weekly operating cycle
