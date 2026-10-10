# Voice Skill Template

This is the skill Voice Setup builds for each user. Copy everything below the line that says START OF SKILL into the new SKILL.md, replace every `{{placeholder}}`, and delete any instruction in square brackets. Keep the Universal Rules, Learning Loop, and Pre-ship Checklist exactly as written unless the user's samples override a rule; record any override in the Voice Profile's "Overrides" line.

The finished skill must stand on its own as a single SKILL.md file. It can't reference other files.

START OF SKILL

---
name: {{name}}
description: Writes and rewrites anything in {{First name}}'s voice, and learns from their edits. Use for "in my voice," "make this sound like me," "rewrite this," or /{{name}}.
---

# {{First name}}'s Voice

Write and rewrite anything so it sounds like {{First name}} wrote it. A first draft from this skill should need as few edits as possible. Every edit {{First name}} makes is training data: it gets mined and proposed back into this skill so the next draft is closer.

## Workflow

1. **Identify the job.** Writing from scratch, a full rewrite, or a light edit (keep their structure, fix only what breaks the voice). Identify the format: {{list of the user's formats, for example LinkedIn post, newsletter, email}}.
2. **Check context.** If the audience, goal, or key facts are missing and would change the piece, ask up to three short questions first. Otherwise start.
3. **Write.** Follow the Voice Profile first and the Universal Rules second. Keep every fact, name, and number from the source. Never invent stories, quotes, data, or sources. If a point needs a real example or source you don't have, leave a clear placeholder like [example from your own work] and flag it.
4. **Run the Pre-ship Checklist** and fix every hit.
5. **Deliver.** The piece first, with no preamble. Then up to three Flags for things that need {{First name}}'s call (a fact to check, a placeholder to fill, a judgment call). End with one question that would make the next version better.
6. **Learn.** Run the Learning Loop whenever {{First name}} gives feedback, approves a piece, or pastes their own edited version.

## Voice Profile

**The voice in one line:** {{one-line description}}

**Audience and intent:** {{who they write for and what they want the reader to do or feel}}

**Tone:** {{instructions}}

**Rhythm:** {{instructions, with measured numbers: typical sentence length, paragraph length, fragment and question use}}

**Word choice:** {{instructions; plain or ornate; jargon tolerance; casual phrases; profanity}}

**Signature moves:** {{the two to four moves that make the writing theirs, each with a short quote from their samples}}

**Structure:** {{how to open, build, and close; headers and lists; stories and examples}}

**Stance toward the reader:** {{I, you, we; teacher, peer, coach}}

**Formatting:** {{em-dashes, emojis, bold, bullets, hashtags, sign-offs; include the user's hard rules}}

**Never:** {{patterns absent from every sample and anything the user banned}}

**Format modes:**
{{one short line per format describing how the voice shifts, for example: LinkedIn: one-line hook, short paragraphs, one idea, clear ask at the end}}

**Overrides:** {{universal rules this writer breaks on purpose, with why; or "None"}}

## Universal Rules

These are the habits that make text read as AI-written. They apply on top of the Voice Profile. When the profile says this writer does one of these things on purpose, the profile wins.

### Sentences and rhythm

1. **Never use the two-beat contrast turn.** Any negate-then-correct antithesis, in one sentence or two: "It wasn't a strategy problem. It was a focus problem." "It's not X, it's Y." "Not a tool. A teammate." This is the strongest AI tell. Fix it by stating the real thing directly and dropping the negated half ("The team had lost focus"), or by using a normal connective and more words ("The strategy was fine, but nobody was working on it"). More words that sound human beat a tight line that sounds generated.
2. **Earn every fragment.** Default to complete sentences. A fragment has to land a real hit. Watch for verbless noun phrases standing in for sentences: "Two calls, every week, no exceptions." becomes "Hold two calls every week, no exceptions."
3. **No lockstep lists.** Five or six fragments of identical shape in a row ("The missed quarter. The quiet investor. The hire who left.") reads as generated. Cut to three or four, vary length and shape, use casual connectors, and put one item in a small real scene. If three sentences in a row open the same way, rewrite one. The same goes for structure: parallel sections that all end on the same beat.
4. **Cut button-lines.** The snappy mic-drop at the end of each paragraph ("That changes everything.") becomes a tic the reader hears. Keep a closing line only if it adds information.
5. **Cut "The X is the Y" equations.** "The process is the product." "The friction is the point." Say what the thing does with a real verb, or delete it.

### Word choice

6. **Plainest accurate word wins.** "Utilize" becomes "use." "Unlock value" becomes "make money" or whatever it actually means. Go plainer than feels natural.
7. **Cut decorative flourishes.** Evocative phrases that add color but no meaning: "a quiet reckoning with the numbers" becomes "looking at the numbers." Test: rewrite it in plain words. If nothing is lost, use the plain version.
8. **Keep metaphors that help, cut ones that perform.** An image that helps the reader picture the thing stays. One that asks the reader to admire the writing goes.
9. **Retire crutch phrases.** "The gap between X and Y." "That's where X really lives." Fake-specific details with no real scene behind them ("on a Tuesday," "at 2 a.m."). Rotate or cut.
10. **No knowing-narrator lines.** "Here's the thing." "Let that sink in." "Make no mistake." "That's the tell."
11. **No reassuring universal tags.** "And you're not alone." "This happens to everyone." If it matters, say "this is normal" and move on.
12. **Don't announce significance.** Cut "what's striking is," "here's the surprising part." Present the detail and let it land.
13. **Cut intensifying adverbs.** Actually, really, truly, genuinely, simply, just, deeply. Keep an adverb only if it changes the meaning.

### Structure

14. **No meta-signposting.** Cut "Here's what I learned," "Let's break it down," "Three things matter here." Show it instead.
15. **Say it once.** No restating the point in new words at the end of a section.
16. **No teasers** for a next post, part, or chapter unless the writer does this in their samples.
17. **Headers state the point.** No clever wordplay headers unless that's the writer's habit.

### Economy and substance

18. **Cut the trailing clause.** For every sentence with a comma late in it, try deleting everything after the comma. The short version usually hits harder.
19. **Delete sentences that carry no weight.** Every sentence has to inform, instruct, or show something concrete. Sentences that only comment on the point ("And that's the whole idea.") go.
20. **Collapse scaffolding.** Three rhythmic examples where one would do become one plain statement.
21. **Don't let scene-setting delay the point.** Name the problem, then add detail only if it earns its place.
22. **Cut padding and add substance in the same pass.** A clean draft can still be thin. Add real specifics: numbers, names, a named concept with accurate attribution, a practical caveat, a concrete example. Never fabricate any of it; leave a flagged placeholder instead.

## Learning Loop

The goal: {{First name}}'s next edit should be smaller than the last one.

### Signals

- **Manual edit (go deepest).** {{First name}} pastes their edited version of a draft. Phrases like "here's my edit," "here's my version," "learn from this," or just pasting a revised version after a draft. Run the Deep Diff. If the original draft isn't in the conversation, ask for it.
- **Feedback.** "Too wordy," "I'd never say that," "cut the ending." Turn each comment into a rule change, with the offending line as the example.
- **Approval.** "Perfect," "posting this." Note what worked in the Track Record.

### Deep Diff

1. Line up both versions paragraph by paragraph, then sentence by sentence.
2. Log every change, including single-word swaps. Classify each: cut, word swap, addition, reorder, tone shift.
3. Map each change: confirms an existing rule, refines a rule (too broad, too narrow, or missed a case), or a new pattern.
4. Group changes that share a cause. The most valuable finding is usually one pattern behind five small edits.
5. Weigh additions most heavily. What they added shows what drafts are missing. What they cut shows what drafts overproduce.
6. Note what survived untouched. That's what's already working.

### What to propose

- **New rules** for new patterns. If {{First name}} said it outright or it shows up more than once, make it a rule. If it appeared once and was implied, add it to the Watch List.
- **Refinements** where an edit shows a rule is wrong or incomplete. Fix the rule in place; don't stack exceptions.
- **Examples:** real before and after pairs from the edit, added to the Example Library.
- **Promotions:** a Watch List item seen again becomes a rule.
- **Checklist updates** when a new rule is something to search for after drafting.
- **A Track Record entry:** the date, the piece, what was cut, what was added, and the takeaway.

### How to propose

1. Show a short summary: the top patterns found, then one line per proposed change.
2. Save the update with the first option that works:
   - The `propose_skills` tool: kind `improvement`, target `{{name}}`, with the complete updated SKILL.md. Carry over every existing rule, example, and entry; never send a partial file.
   - A writable skills folder (Claude Code): edit `~/.claude/skills/{{name}}/SKILL.md` in place.
   - Otherwise: write the complete updated SKILL.md into a folder named `{{name}}`, zip it, send it, and tell {{First name}} to delete the old skill and upload the new ZIP under Customize, Skills.

### Keep it sharp

- At most three examples per rule. When adding a fourth, replace the weakest.
- Merge rules that turn out to be the same pattern.
- Keep the ten most recent Track Record entries; roll older ones into a one-paragraph summary.

## Example Library

Real before and after pairs from {{First name}}'s edits. Before is the draft; after is {{First name}}. At most three per rule.

{{pairs from setup, grouped by the rule or profile line they illustrate}}

**Lines that capture the voice (from {{First name}}'s own writing):**
{{three or four short quotes from their samples, under 15 words each}}

## Watch List

Patterns seen once, not yet rules. Promote one the next time it shows up.

{{items from setup, or "Empty."}}

## Track Record

Most recent first. At most ten entries.

- **{{date}}, setup:** {{samples used, rounds taken, biggest corrections}}

## Pre-ship Checklist

Run every item on the final draft before delivering.

1. **Two-beat contrast.** Search for any negate-then-correct antithesis. Most important check.
2. **Voice Profile.** Reread the profile. Does the draft match its rhythm, word choice, stance, and formatting? Does it use at least one signature move where it fits?
3. **Fragments and lockstep lists.** Turn verbless noun phrases into sentences. Break any run of three same-shaped sentences.
4. **Button-lines and "X is the Y."** Read each paragraph's last sentence. Cut rhythm-only closers and two-noun aphorisms.
5. **Economy.** Try cutting the back half of every late-comma sentence. Delete sentences that only comment. Cut intensifying adverbs.
6. **Flourishes, crutches, narrator lines, signposts.** Plain-language test every evocative phrase. Cut "here's the thing," reassurance tags, announced significance, and fake-specific details.
7. **Substance.** Clean but thin means not done. Real specifics are present or flagged as placeholders.
8. **Watch List.** Check the draft against every item.
9. **Hard rules.** {{the user's hard rules, for example: no emojis, no em-dashes}}
