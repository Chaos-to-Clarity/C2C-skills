# Recap Reference

Settings, email template, and scheduling rules shared by recap-setup and meeting-recap.

The master copy lives in `shared/recap-config.md` in the Claude-skills repository. Edit it there, then run `python scripts/sync_shared.py`.

## 1. Config format

The Recap Config is one page or file titled "Recap Config", holding one fenced `text` block. One `key: value` per line; `none` means not used.

```text
config_version: 1
owner.name: <full name used to sign>
owner.title: <title, or none>
owner.email: <the user's address; always CC'd, never in "to">
owner.other_emails: <other addresses that are the user, comma-separated, or none>
time_zone: <IANA zone>

sources.meeting_notes: <granola | fireflies | otter | fathom | zoom | google-meet | notion-meetings | folder: path>
sources.email: <gmail | outlook>
sources.calendar: <google-calendar | outlook | device>
sources.calendar_id: <primary or id>
memory: <cortex | notion: page link | google-drive: folder | none>
tasks: <founder-os | notion: database link | app: name | calendar-only>
tracking: <cortex-ingest-log | recap-log: link or path>

brand.name: <company or brand>
brand.tagline: <or none>
brand.website: <or none>
brand.primary: <hex, default #1A4567>
brand.accent: <hex, default #CD5247>
brand.logo_url: <image URL, or none for a text wordmark>
brand.footer: <footer line>
recap.label: <default Meeting Recap>
voice.notes: <three or four short notes on how the user writes, or none>

recap.recipients: <external-cc-me | all-cc-me | me-only>
recap.meetings: <all-with-notes | folder: name | external-only>
recap.skip_if_title_contains: <[no recap], personal, ...>
recap.lookback_days: 3

autonomy.recap: <send | draft>
autonomy.follow_ups: <draft | send>
autonomy.meetings: <book | propose>
autonomy.proactive: <do | suggest>

work_days: Mon-Fri
work_hours: 09:00-17:00
in_person_buffer_minutes: 30
default_block_minutes: 30
max_block_minutes: 90
min_lead_minutes: 60
default_meeting_minutes: 30
in_person_meeting_minutes: 60

places.area: <neighborhood or city, or none>
places.preferred: <Name (type), Name (type), ... or none>
```

## 2. The recap email

Inline styles only (email clients strip `<style>` blocks). Fill every `{{placeholder}}`, escape `&`, `<`, and `>` in content, repeat the marked rows as needed, and remove all comments before sending.

**Dark mode rule:** dark text on light backgrounds everywhere. Never put white or light text on a colored background.

```html
<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="color-scheme" content="light dark"><meta name="supported-color-schemes" content="light dark"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#EEF2F5;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF2F5;"><tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="width:100%;max-width:640px;background:#FFFFFF;font-family:Helvetica,Arial,sans-serif;color:#2A3642;">
<tr><td style="padding:24px 32px 16px 32px;border-bottom:4px solid {{PRIMARY}};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
<td valign="middle">{{LOGO: <img src="LOGO_URL" alt="BRAND" height="36" style="display:block;border:0;"> or <div style="font-size:20px;font-weight:900;color:PRIMARY;letter-spacing:0.5px;">BRAND</div>}}</td>
<td valign="middle" align="right">
<div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#6B7C88;font-weight:bold;">{{RECAP_LABEL}}</div>
<div style="font-size:20px;font-weight:bold;color:{{PRIMARY}};margin:3px 0 2px 0;">{{MEETING_TITLE}}</div>
<div style="font-size:13px;color:#6B7C88;">{{Month D, YYYY}} &nbsp;|&nbsp; {{ATTENDEE_NAMES}}</div>
</td></tr></table></td></tr>
<tr><td style="padding:22px 32px 4px 32px;">
<p style="margin:0 0 14px 0;font-size:15px;line-height:22px;">Hi {{FIRST_NAMES}},</p>
<p style="margin:0 0 14px 0;font-size:15px;line-height:22px;">{{OPENING: one or two sentences in the user's voice, thanking them and naming the main outcome}}</p>
<p style="margin:16px 0 6px 0;font-size:19px;line-height:26px;font-weight:bold;color:#0F2A40;">{{HEADLINE_LEAD}} <span style="color:{{ACCENT}};">{{HEADLINE_TURN}}</span></p>
</td></tr>
<!-- SECTION: repeat for each section chosen for this meeting type -->
<tr><td style="padding:18px 32px 0 32px;">
<div style="font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:#0F2A40;border-bottom:2px solid {{PRIMARY}};padding-bottom:6px;"><span style="color:{{ACCENT}};">&#9632;</span>&nbsp; {{SECTION_TITLE}}</div>
<ul style="margin:10px 0 0 0;padding-left:20px;font-size:14px;line-height:21px;">
<li style="margin-bottom:6px;"><b style="color:#0F2A40;">{{LEAD}}</b> {{TEXT}}</li>
</ul></td></tr>
<!-- ACTIONS -->
<tr><td style="padding:18px 32px 0 32px;">
<div style="font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:#0F2A40;border-bottom:2px solid {{PRIMARY}};padding-bottom:6px;"><span style="color:{{ACCENT}};">&#9632;</span>&nbsp; Next Steps</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-size:14px;line-height:20px;margin-top:6px;">
<tr><td width="20" valign="top" style="padding:8px 0;border-bottom:1px solid #DDE4E9;">&#9744;</td><td width="80" valign="top" style="padding:8px 6px;border-bottom:1px solid #DDE4E9;font-size:11px;font-weight:bold;letter-spacing:1px;color:{{PRIMARY for them, ACCENT for the user}};">{{OWNER_FIRST_NAME_UPPERCASE}}</td><td valign="top" style="padding:8px 6px;border-bottom:1px solid #DDE4E9;">{{ACTION}}</td><td width="90" align="right" valign="top" style="padding:8px 0;border-bottom:1px solid #DDE4E9;color:#6B7C88;font-size:13px;">{{DUE}}</td></tr>
</table></td></tr>
<!-- OPTIONAL CALLOUT: next meeting booked, or a question to bring next time -->
<tr><td style="padding:20px 32px 0 32px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF2F5;border-left:4px solid {{PRIMARY}};"><tr><td style="padding:14px 18px;">
<div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:{{PRIMARY}};margin-bottom:6px;">{{CALLOUT_LABEL}}</div>
<div style="font-size:16px;line-height:23px;font-weight:bold;color:#0F2A40;">{{CALLOUT_TEXT}}</div>
</td></tr></table></td></tr>
<tr><td style="padding:22px 32px 26px 32px;">
<p style="margin:0 0 18px 0;font-size:15px;line-height:22px;">{{SIGNOFF_NAME}}</p>
<div style="border-top:1px solid #DDE4E9;padding-top:10px;font-size:12px;color:#6B7C88;">{{FOOTER, with the website as a link in PRIMARY}}</div>
</td></tr></table></td></tr></table></body></html>
```

Always send a plain-text version alongside the HTML: greeting, headline, each section as simple lines, next steps, sign-off.

## 3. Sections by meeting type

Pick the sections that fit. Two to four sections, plus Next Steps. Skip any section with nothing real in it.

| Meeting type | Sections |
| --- | --- |
| Client or customer session | What We Covered, Decisions, Open Questions |
| Coaching or advisory session | Wins, Challenges, Insights (optional callout: a question to bring next time) |
| Sales or discovery call | What We Heard, How We Can Help, Open Questions |
| Partner, investor, or intro call | What We Discussed, Where It Could Go |
| Internal team meeting (sent to the user only by default) | Decisions, Risks, Open Questions |
| Interview | No external recap. Notes and tasks only |

## 4. Writing rules

- Every line traces to something said in the meeting. Never invent numbers, names, dates, or commitments.
- Write for the recipient. Include only what was said openly with them. Never include the user's private asides, internal strategy, pricing logic, or opinions about the recipient.
- In the user's voice (`voice.notes`), second person to the recipient. Plain and specific. One idea per bullet, 25 words or fewer. Lead with specifics: numbers, names, dates, their own words.
- No filler openers ("Great call!"), no emojis, no buzzwords.
- Next Steps: every commitment, theirs first, the user's last. Each starts with a verb. Due is a short date ("Oct 14") resolved against the meeting date, or "Next meeting" or "Ongoing". Never "TBD".
- Subject: "[recap.label]: [meeting title or other party], [Month D]", using the meeting date.

## 5. Booking time for the user's own tasks

Same protocol as handwritten-notes.

- **Estimate:** 30 minutes by default. 30 for an email, call, quick reply, intro, or short review; 60 for drafting, meeting prep, research, or a short proposal; 90 for a deck, a full proposal, or multi-part work. Over `max_block_minutes`, split into blocks named "(Part 1 of N)". A duration someone stated wins.
- **Due date:** a stated date or day is the due date; the block must finish before the due day starts. No date: High priority (someone waiting, money on the line, "ASAP") within 2 work days, Medium (default) within 5, Low within 10.
- **Slots:** only on `work_days` within `work_hours`, never sooner than `min_lead_minutes` from now, starting on :00 or :30. Every timed event is busy, including earlier task blocks; ignore declined and Free events; all-day events block only if they are out-of-office, travel, or full-day.
- **In-person buffer:** block `in_person_buffer_minutes` before and after any event with a physical location or a title like lunch, coffee, dinner, drinks, pickup, or drop off.
- **Order:** earliest slot that fits; prefer mornings for 90-minute work. Several tasks: schedule by due date then priority, adding each block to the busy list before placing the next.
- **No fit before the due date:** take the best slot on the latest work day before it, even if shorter (minimum 30 minutes), and flag it. If that fails, the earliest slot on the due day before noon, flagged as late.
- **Event:** title = task, description = the commitment, the meeting it came from, a link to the note, and the due date. Busy, default reminders, no attendees.

## 6. Booking meetings with other people

For a meeting agreed in the call ("let's follow up next week", "let's grab coffee"):

- **When:** the timeframe they agreed. No timeframe: within the next 5 to 10 work days.
- **Length:** what they said, else `default_meeting_minutes`, or `in_person_meeting_minutes` for coffee, lunch, or drinks.
- **Slot:** the user's calendar only, within work hours, with the in-person buffer for in-person meetings. Prefer a time of day like the meeting just held, since it suited both of them.
- **Place, in person:** a `places.preferred` spot that fits the type (coffee, lunch, drinks). None set: search for a well-reviewed spot of that type near `places.area`. Never book a paid reservation or put down a card.
- **Video:** add a video link if the calendar supports it.
- **Invite (`autonomy.meetings: book`):** create the event with the other attendees invited. Title "[Other party] / [User first name]: [purpose]". Description: why you're meeting, from the call, and "If this time doesn't work, reply with one that does." The calendar sends the invite.
- **Propose (`autonomy.meetings: propose`):** draft an email to them with two or three open times and the place, and create nothing.
- **Check first:** search the next 21 days for an event with the same people and purpose. If one exists, skip.
