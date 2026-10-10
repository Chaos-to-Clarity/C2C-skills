# Handwritten Notes

Snap a photo of your notebook page and send it to Claude. You get back a clean transcription, tasks in your to-do list with real time blocked on your calendar, and notes filed where you'll find them.

**[Download handwritten-notes.zip](https://github.com/chaostoclarity/claude-skills/releases/latest/download/handwritten-notes.zip)**

## What it does

- **Transcribes** the page, keeping your structure. Words it can't read are marked, not guessed silently.
- **Turns checkbox items into tasks.** A box next to an action becomes a task. A checked box is logged as done.
- **Estimates the time.** 30 minutes by default, 60 for drafting or prep, 90 for decks and bigger builds. Larger work is split into 90-minute blocks.
- **Books the time before the due date.** Write "by Tuesday" and the block lands Monday or earlier. No date means it schedules by urgency.
- **Respects your calendar.** Working hours only, never on top of existing events, with a travel buffer around in-person meetings.
- **Files the notes.** Notes about a person or project are linked to them. General notes get their own page stamped with the date and time.
- **Reports back** in a short summary and flags anything it wasn't sure about.

## What you need

- **Claude** with skills turned on.
- **Notion** connected to Claude (recommended). Other connected task or notes apps can work.
- **A calendar** connected to Claude: Google Calendar, Outlook, or your device calendar. Without one, tasks are filed but not scheduled.

## First run

The first time you send a photo, the skill runs a short setup:

1. Checks your connectors and offers to connect anything missing.
2. Looks for an existing system in Notion (a Tasks database, People, Projects) and asks before using it. If there isn't one, it offers to build a simple Tasks and Notes setup for you.
3. Asks four quick questions: working hours, work days, travel buffer, and whether to book automatically or propose times first.
4. Saves your answers to a page called **Handwritten Notes Config** in your Notion. Edit that page anytime to change how it works.

After that, just send photos.

## Tips for good results

- Draw a clear square for anything you want scheduled.
- Write the due date next to the task: "by Fri", "10/14", "EOW".
- Add a duration if you know it: "1 hr", "2h".
- Fixed commitments (school pickup, gym, travel) must be on your calendar to be protected.
- Shoot the page flat, in good light.

## Example

Your page says:

> ☐ create workshop slide deck by Tuesday
> &nbsp;&nbsp;&nbsp;– use Sam's outline

Claude creates the task "Create workshop slide deck", due Tuesday, estimated at 90 minutes, and books a morning block on Monday. "Use Sam's outline" goes in the task and the calendar event.
