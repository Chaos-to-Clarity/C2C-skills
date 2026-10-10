---
name: voice-setup
description: Builds your own voice skill from samples of your writing. Analyzes your style, writes a test piece, iterates until it sounds like you, then saves a skill that writes and learns in your voice.
---

# Voice Setup

Turn samples of the user's writing into a personal voice skill. The skill this produces writes and rewrites anything in their voice, catches the habits that make text read as AI-written, and gets sharper every time they edit its drafts.

The flow: collect samples, analyze the voice, write a test piece, iterate until the user says it sounds like them, then save the skill.

Read `references/voice-skill-template.md` before Step 3. It holds the skill you'll fill in, including the universal rules every draft must pass.

Use AskUserQuestion for choices (up to 4 questions per call, recommended option first). If it isn't available, ask in plain text. Keep every message short; the user is busy.

## Step 0. Check for an existing voice skill

If the user already has a voice skill built by this setup (its description says "in [Name]'s voice, and learns from their edits"), ask what they want:

- **Refresh it with new samples** (recommended): run Steps 1 to 4 against the existing profile, then propose it as an update.
- **Start over**: build a new one from scratch.
- **Just use it**: stop and tell them how to call it.

## Step 1. Collect samples and context

Ask for writing samples in one message:

- **Three to five pieces they wrote themselves**, about 1,500 words or more in total. Their best work, and the kind of writing they want help with.
- **Unedited by others and not AI-drafted.** Ghostwritten, heavily edited, or AI-assisted samples teach the wrong voice. Say this plainly.
- **Any format works:** paste the text, attach files, or share links. Fetch links with WebFetch, or read them with a connected app (Google Drive, Notion). LinkedIn and some newsletter platforms block fetching; if a link fails, ask them to paste the text.
- **Optional but valuable:** one piece that sounds wrong to them, such as an AI draft they hated or a corporate version of their message. What they reject is as useful as what they write.

In the same turn, ask with AskUserQuestion:

1. **What will you use it for most?** (multi-select) LinkedIn posts; Newsletter or blog; Emails and messages; Long-form (book, report, essay).
2. **Who reads it?** Founders and operators; Customers and buyers; Investors and board; My team.
3. **What should the test piece be about?** Pick a topic for me from my samples (recommended); I'll give you a topic; Rewrite something I'll paste.
4. **Any hard rules?** (multi-select) No emojis; No em-dashes; No hashtags; Keep swearing out.

If samples are thin (under 800 words, or all one short format), say what's missing and ask for more before analyzing. A thin sample set produces a generic voice.

## Step 2. Analyze the voice

Read every sample closely. Then write a **Voice Analysis** the user can recognize themselves in. Every claim needs evidence: a short quote from their samples (under 15 words) or a measured number.

Measure, don't guess. If a shell is available, run a quick script over the samples for average sentence length, average paragraph length, share of sentences under eight words, questions per piece, and counts of em-dashes, exclamation points, emojis, bold, and bullets. Otherwise estimate carefully and say they're estimates.

Cover these sections, briefly:

1. **The voice in one line.** A plain description a friend would agree with.
2. **Audience and intent.** Who they write for and what they want the reader to do or feel.
3. **Tone.** Warmth, edge, humor, formality, confidence. How they handle disagreement or hard truths.
4. **Rhythm.** Sentence and paragraph length, how they use fragments and questions, how fast they get to the point.
5. **Word choice.** Plain or ornate, jargon tolerance, casual phrases, profanity, words and phrases they repeat (their signatures).
6. **Structure.** How they open, how they build, how they close, headers and lists, use of stories and examples.
7. **Stance toward the reader.** I, you, we. Teacher, peer, coach, insider. How much of themselves they put in.
8. **Formatting habits.** Em-dashes, emojis, bold, bullets, hashtags, sign-offs.
9. **What they never do.** Patterns absent from every sample that AI drafts usually include.
10. **Where they're strongest.** The two or three moves that make their writing theirs.
11. **Format modes.** If their LinkedIn, email, and long-form registers differ, describe each one separately.

Also note anything inconsistent across samples and ask which version is the real them.

## Step 3. Write the test piece

Read `references/voice-skill-template.md`. Write the test piece in the user's primary format, on the topic from Step 1, following the Voice Profile you just drafted and the template's universal rules. Run the template's pre-ship checklist before showing it.

Where the user's own habits conflict with a universal rule (they love em-dashes, they write in fragments on purpose), their samples win. Note the override in the profile.

Show the Voice Analysis and the test piece together. Then ask with AskUserQuestion:

- **Sounds like me**: accept and build the skill.
- **Close, needs tweaks**: they tell you what to change.
- **Off, here's why**: they explain.
- **I'll rewrite it myself**: they paste their own version of the test piece.

## Step 4. Iterate until they accept

Each round:

1. **Turn feedback into rules.** Every comment ("too polished," "I'd never say leverage," "cut the ending") becomes a specific profile change or rule, with the offending line as the example.
2. **If they rewrote the test piece, diff it deeply.** Line up both versions sentence by sentence. Log every change, down to single words: cuts, word swaps, additions, reordering, tone shifts. Group changes that share a cause and find the pattern behind them. Weigh what they added most heavily; it shows what your draft was missing. Each before and after pair goes in the example library.
3. **Update the analysis and rewrite the test piece.** Show the new version and a short list of what changed in the profile (three to six lines). Don't re-show sections that didn't change.
4. **Ask again** with the same four options.

Keep going until they choose "Sounds like me." If three rounds pass without acceptance, stop and diagnose: usually the samples are mixed (edited, ghostwritten, or from different registers) or the test topic is unlike what they normally write. Ask for better samples or a different topic.

## Step 5. Build and save the skill

Fill in the template from `references/voice-skill-template.md`:

- **Name:** `<first-name>-voice` in lowercase (for example `maya-voice`), or `my-voice` if they'd rather. Lowercase letters, numbers, and hyphens only. Never use "claude" or "anthropic" in the name.
- **Description:** fill in the template's description line. Keep it under 200 characters.
- **Voice Profile:** the final accepted analysis, written as instructions ("Open with the problem in one line"), not observations ("She tends to open with...").
- **Example Library:** every real before and after pair from Step 4, plus three or four short lines from their samples that capture the voice best, under 15 words each.
- **Watch List:** patterns you saw once in their feedback but aren't sure of yet.
- **Track Record:** one entry dated today summarizing setup: samples used, rounds taken, the biggest corrections.

Then save it, using the first option that works:

1. **The `propose_skills` tool** (Claude app). Call it with kind `new`, the skill's name and description, and the full filled-in SKILL.md. Tell the user to save it from the card.
2. **A skills folder you can write to** (Claude Code). Write the file to `~/.claude/skills/<name>/SKILL.md` and tell them it's installed.
3. **A ZIP to upload.** Create a folder named after the skill containing only `SKILL.md`, zip the folder (the folder must be the ZIP's single top-level entry), and send it to the user. Tell them: in Claude, open Customize, then Skills, click Create skill, then Upload a skill, choose the ZIP, and turn it on.

## Step 6. Show them how to use it

Close with a short message:

- **Write:** "Draft a LinkedIn post in my voice about [topic]."
- **Rewrite:** "Rewrite this in my voice," then paste the text.
- **Teach it:** after editing one of its drafts, paste your version and say "learn from this." It will diff your edit and propose updates to itself. The more you edit, the closer its first drafts get.
- **Refresh:** run this setup again any time with new samples.

Then ask whether they want to try it now on something real.
