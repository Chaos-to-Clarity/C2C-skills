---
name: content-engine-setup
description: Sets up Content Engine, which turns last week's meetings into a framework, newsletter, and LinkedIn post in your voice. Connects notes, voice, and context, then schedules it weekly.
---

# Content Engine Setup

Set up Content Engine for the user: their meeting notes, their voice, their context, what it writes, where drafts go, and the weekly schedule. Run once. If a Content Engine Config already exists, show the current settings and offer to change any of them.

Read `references/content-engine-config.md` first. It defines every setting, the outputs, the writing rules, and the config format. If the user has a Cortex, also read `references/cortex-spec.md`.

Use AskUserQuestion for choices (up to 4 per call, recommended option first). If it isn't available, ask in plain text. Do discovery silently before asking. Keep every message short; the user is busy.

## Step 1. Check for an existing setup

Find the Content Engine Config (section 2 of the reference). If it exists and its links validate, show the settings in a short list and ask what to change. Stop unless they pick something.

Also look for:
- **A Cortex Map** (`references/cortex-spec.md`, section 4). If found, Content Engine reads Standing Context and Strategy for audience and positioning, and logs runs in the Ingest Log. Tell the user in one line.
- **A Recap Config.** If found, reuse its meeting-notes source, email, time zone, and owner details instead of asking again.
- **A voice skill** in the skills available to you: one whose description says it writes "in [Name]'s voice, and learns from their edits" (built by the Voice plugin), or any skill the user calls their voice skill.

## Step 2. Connect the tools

Detect what's connected and pre-select it. Ask only about gaps.

| Role | Options | Required |
| --- | --- | --- |
| Meeting notes | Granola, Fireflies, Otter, Fathom, Zoom or Google Meet notes, Notion meeting notes, a notes folder | Yes |
| Delivery | Gmail, Outlook, Notion, Google Drive | Yes |
| Context | Cortex (if found), a Notion page, a Google Drive folder, or none | No |

Test each with one small read: list last week's meetings, list one email or page. For anything missing, search the connector registry and suggest it. Granola is the most common; if it isn't connected, suggest it first.

## Step 3. Choose the meetings that feed it

Content comes from conversations, so the filter decides the quality. List the user's meetings from the last two weeks and show the titles grouped by pattern (recurring client sessions, customer calls, internal syncs, intros, interviews). Then ask in one AskUserQuestion call:

1. **Which conversations should feed your content?** (multi-select) Client or coaching sessions (recommended for coaches, consultants, advisors); Customer and user calls (recommended for founders); Team and leadership meetings; Partner and investor calls.
2. **Which should it always skip?** (multi-select) Sales and intro calls; Interviews; One-on-ones with my team; Personal meetings. Interviews and personal meetings are pre-selected.

From the titles you listed, propose `meetings.include_title_terms` and `meetings.exclude_title_terms` and confirm them in one line ("I'll treat titles with 'Session' or 'Kickoff' as client sessions and skip 'Intro' and 'Consult'. Right?").

## Step 4. Context

Pull before asking. From a Cortex, read Standing Context and the Strategy summary. Otherwise, fetch the user's website or LinkedIn About if they share a link. Draft these four lines and ask the user to confirm or edit:

- `owner.role`: what they do, one line
- `audience.who`: who reads their content
- `audience.problems`: what those readers struggle with most
- `positioning`: what they want to be known for

Then ask whether there are themes or lenses to favor (`themes.favor`) and topics to never touch (`themes.avoid`). Both can be none.

## Step 5. Voice

The drafts must sound like the user, or they won't ship them.

- **A voice skill exists:** set `voice.source: skill: <name>`. Ask it for a short summary of the profile (the one-line voice, tone, rhythm, hard rules) and save that in the config's Voice Profile block as a fallback, for runs where the skill can't be loaded.
- **No voice skill:** recommend the Voice plugin (it builds a full voice skill that learns from every edit). If they want to keep going now, build a compact profile here:
  1. Ask for three to five pieces they wrote themselves, about 1,500 words total, unedited and not AI-drafted, ideally newsletters and LinkedIn posts. Paste, attach, or link. If a link won't fetch, ask them to paste it.
  2. Measure what you can (sentence and paragraph length, fragments, questions, em dashes, emojis, bold, hashtags) and read for tone, stance, openings, closings, and signature phrases.
  3. Write a Voice Profile of eight to twelve lines, as instructions ("Open with the problem in one line"), each backed by a short quote under 15 words or a number from their samples. Include their hard rules.
  4. Set `voice.source: profile`.

Ask for any hard rules either way (`voice.hard_rules`): no emojis, no em dashes, no hashtags, no swearing.

## Step 6. Outputs

One AskUserQuestion call:

1. **What should it write each week?** (multi-select) Framework (recommended); Newsletter issue (recommended); LinkedIn post (recommended); X thread; Blog post; Short video script.
2. **How should the newsletter end?** A question that invites replies (recommended: replies build the relationship and the list's reputation); A link to my offer or booking page; No call to action. Skip if no newsletter.
3. **Where should drafts go?** One email to me (recommended); An email draft in my inbox; A Notion page; A Google Doc.
4. **When should it run?** Monday 7:45am (recommended: drafts are ready to edit and ship that day); Sunday evening; Friday afternoon.

If they chose a newsletter, ask in plain text for the newsletter's name, any recurring lens for every issue (for example a philosophy, a method, a value), and a P.S. to include word for word (for example a line about their offer). All three can be none. If they chose a CTA link, ask for it.

## Step 7. Tracking

Content Engine must never repeat a theme within 60 days (section 8 of the reference).

- If a Cortex exists: its Ingest Log.
- Otherwise: create a Content Log next to the config (a Notion database or a Markdown file) with the columns in section 8.

## Step 8. Save the config

Write the Content Engine Config in the format in section 1 of the reference, with the Voice Profile block if there is one. Put it under the Cortex parent if there is one and add one line to the Cortex Map's Settings so other skills can find it. Otherwise put it next to the Recap Config if one exists, or where the user chooses.

## Step 9. Test run

Run the weekly-content-engine skill now, in test mode: use the last full week (or the lookback rule if it was quiet), and show the drafts in chat instead of delivering them. Write the Content Log entry only if the user accepts.

Ask with AskUserQuestion:
- **Ship-ready**: keep the settings.
- **Voice is off**: they say what's wrong or paste their edited version. Turn each comment into a Voice Profile rule with the offending line as the example. If they use a voice skill, offer to run its learning loop on their edit instead.
- **Wrong theme or meetings**: adjust the meeting filter or themes.
- **Wrong outputs**: adjust the list.

Rewrite and show again after a change. Two rounds is usually enough; after three, check whether the meetings feeding it have enough substance.

## Step 10. Schedule it

Create the weekly scheduled task at the time from Step 6, in the user's time zone, with the prompt: "Run my weekly-content-engine skill. Work on your own without asking questions, and deliver the drafts per my Content Engine Config." Use the scheduling tools if available (search for them if they aren't loaded). Otherwise give the steps to create it in the Claude app.

Tell them the task needs permission to act on its own (automatic approval), plus the meeting-notes and delivery connectors enabled, or each run will stop to ask.

## Step 11. Report

- Where the config lives, with a link
- Tools connected, and the voice source
- What it writes, where it lands, and when
- How to change anything: "Say 'change my Content Engine settings.'"
- How to run it anytime: "Run my content engine for last week."
