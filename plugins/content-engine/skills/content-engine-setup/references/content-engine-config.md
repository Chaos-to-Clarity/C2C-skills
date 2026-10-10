# Content Engine Reference

Settings, output formats, writing rules, and the self-edit pass shared by content-engine-setup and weekly-content-engine.

The master copy lives in `shared/content-engine-config.md` in the C2C-skills repository. Edit it there, then run `python scripts/sync_shared.py`.

## 1. Config format

The Content Engine Config is one page or file titled "Content Engine Config", holding one fenced `text` block. One `key: value` per line; `none` means not used. Multi-line values (the voice profile) go in a second fenced block titled "Voice Profile" on the same page or in the same file.

```text
config_version: 1
owner.name: <full name>
owner.email: <where drafts are delivered>
owner.role: <one line, for example "Fractional CFO for seed-stage startups">
time_zone: <IANA zone>

sources.meeting_notes: <granola | fireflies | otter | fathom | zoom | google-meet | notion-meetings | folder: path>
sources.email: <gmail | outlook | none>
memory: <cortex | notion: page link | google-drive: folder | none>
tracking: <cortex-ingest-log | content-log: link or path>

meetings.include: <client-sessions, customer-calls, team-meetings, partner-calls, ...>
meetings.include_title_terms: <terms that mark an included meeting, for example Coaching, Session, Kickoff>
meetings.exclude_title_terms: <terms that mark a skipped meeting, for example Consult, Intro, Interview, [no content]>
meetings.min_usable: 2
meetings.max_lookback_weeks: 3

audience.who: <who reads the content, one line>
audience.problems: <the problems they care about most, one line>
positioning: <what the user is known for, one line, or none>
themes.favor: <themes or lenses to lean toward, or none>
themes.avoid: <topics never to write about, or none>

outputs: <comma-separated, from section 3; default framework, newsletter, linkedin>
newsletter.name: <name of the newsletter, or none>
newsletter.lens: <a recurring lens for every issue, for example "leading with integrity, borrowing Stoic principles where they fit", or none>
newsletter.words: 600-900
newsletter.close: <reply-question | cta-link | none>
newsletter.ps: <a P.S. kept exactly as written, or none>
linkedin.words: 150-250
linkedin.hashtags: 2
cta.link: <booking or offer link used only where an output allows a CTA, or none>

voice.source: <skill: name | profile | none>
voice.hard_rules: <for example no emojis, no em dashes, no hashtags>

delivery.method: <email | email-draft | notion: page link | google-doc: folder>
schedule: <for example Monday 07:45>
```

## 2. Finding the config

Look in this order and stop at the first hit: a Cortex Map entry named Content Engine Config (see `references/cortex-spec.md`, section 4); a Notion page titled "Content Engine Config"; a Google Drive file with that title; a connected folder with `content-engine-config.md`.

## 3. Outputs

Write only the outputs listed in `outputs`. Every output carries the week's single theme and framework.

| Key | What it is | Shape |
| --- | --- | --- |
| framework | The week's named framework | Name (2 to 4 words), 3 to 5 parts, each with a one-line description and one diagnostic question the reader asks themselves |
| newsletter | One issue | 3 subject line options, then `newsletter.words` words with short paragraphs, hook subheadings, the framework, and one "do this Monday" action. Closes per `newsletter.close`, then `newsletter.ps` if set |
| linkedin | One post | `linkedin.words` words. First line under 12 words whose only job is to earn line two. Short lines, one idea, the framework compressed, ends on a pointed question. At most `linkedin.hashtags` hashtags |
| x-thread | One thread | 5 to 8 posts under 270 characters each. Post 1 is the hook; the last post asks a question |
| blog | One article | 1,000 to 1,500 words, an SEO-friendly title plus 2 alternates, a 150-character meta description, hook subheadings |
| video-script | One short video | 45 to 75 seconds spoken (about 120 to 180 words), a 3-second hook line, on-screen text cues in brackets, one call to action |

**Newsletter close options:**
- `reply-question`: a final question tied to this issue's content and a plain invitation to hit reply and answer it. This is the last line before the P.S. No other CTA in the body.
- `cta-link`: one sentence pointing to `cta.link`, tied to the issue's problem.
- `none`: end on the action.

## 4. Confidentiality (always on, never a setting)

Conversations are private. Every output must be safe to publish even if the people in the meetings read it.

- Never name a client, customer, colleague, their company, investors, deal sizes, headcounts, products, locations, or any detail that could identify them.
- Never mention anyone's health, family, finances, legal matters, or personal relationships, even disguised.
- Composite and generalize every story ("a Series B CTO I work with", "a founder I advised recently"). Change specifics enough that the person would not recognize themselves, including lines that echo their own words.
- Never quote a meeting participant, even anonymously.
- If a story cannot be told safely, leave it out.
- Internal team meetings: never reveal plans, numbers, or people issues the company hasn't made public.

## 5. Writing rules

Apply these on top of the user's voice. When the voice skill or Voice Profile says the user does one of these on purpose, the voice wins.

**Stance.** Write like an expert talking to one reader between meetings, not like a writer performing. Open on the reader's side: validate what they already sense, then name the missing piece. Coach, never lecture or moralize. Use first person mainly to show pattern recognition ("I see this in almost every team I work with"). The piece is about the reader, never about the author.

**Arc.** Keep it consistent without letting it feel formulaic: (1) a one-line hook that names a painful, familiar problem; (2) a short, vivid scene showing how it shows up and why; (3) a clear, confident diagnosis; (4) the cost made undeniable, naming fear, ego, avoidance, or self-deception directly; (5) reassurance that a real fix exists; (6) the framework, framed around outcomes for the reader; (7) a clear action and close. The reader should feel seen, a little uncomfortable, and relieved that someone said it.

**Substance.** A clean draft that is thin is not done.
- Go one level deeper than the obvious point: name the mechanism underneath it, the thing an experienced practitioner knows.
- Include at least one real, accurately attributed named concept or source the reader could look up, with the book or framework in the same breath. Never name an authority without their work, and never misattribute. Paraphrase unless you are certain of the exact wording and source.
- Coin a memorable label for the pattern when it helps.
- Add a practical caveat where an experienced practitioner would (how people actually react, what goes wrong the first time).
- Never fabricate numbers, studies, quotes, or stories. If you lack a true specific, write the plain true statement.

**Sentences.**
- Plainest accurate word wins. No jargon, buzzwords, or guru speak. Banned: move the needle, next level, unlock, unleash, supercharge, game-changer, at the end of the day, hit the ground running, double down, level up, secret sauce, north star (as filler), leverage (when a plainer word works).
- Zero tolerance for the two-beat contrast in any form: "It's not X, it's Y", "He wasn't short on X. He was short on Y.", "You don't get there by X. You get there by Y.", "It feels like X. In practice it's Y." Drop the negated half and state the real thing, or collapse to one sentence with a subordinate clause.
- Default to complete sentences. A fragment is allowed only when it lands a real hit, never as a stack of noun phrases.
- No uniform parallel lists of fragments. If three or more sentences in a row open the same way, rewrite one.
- No "The X is the Y" equation lines as payoffs. Use a real verb.
- No button-lines: no paragraph closers that add rhythm without meaning.
- No knowing-narrator lines or announced significance ("Here's the thing", "Make no mistake", "That's the tell", "What's striking is"). No meta-signposting. No reassuring universal tags ("you're not alone").
- Retired crutches: "the gap between X and Y", "where X lives", "drift", "spine", "throughline", "quietly", fake-specific time markers ("on a Tuesday", "at 2 a.m."), dramatic nouns like "wreckage".
- Cut intensifying adverbs (actually, really, genuinely, simply, just).
- End each sentence where the idea lands. Delete any sentence that does not inform, instruct, or show something concrete.
- No em dashes, no emojis, no horizontal rules, unless the voice says otherwise.
- Bold at most one line per piece, the single most important payoff, and never explain it afterward.

**Headers and hooks.** Every subheading and the first sentence under it is a hook: a contrarian claim, a painful truth, a confession, a sharp imperative with a cost, or a question the reader can't answer yet. Plain words, no wordplay, and the section delivers on the promise.

## 6. Self-edit pass

Write each draft to a file first, so you can check mechanically with grep where possible. Fix every hit before delivering.

1. Two-beat contrast in every disguise (the most important check).
2. Fragments, fragment stacks, and three or more sentences with the same opening.
3. Paragraph closers that exist for rhythm only.
4. Sentences with a comma in the back third: try cutting everything after it. Delete sentences that only comment or restate.
5. Flourishes, crutch phrases, banned words, em dashes, "X is the Y" equations.
6. Knowing-narrator lines and meta-signposting.
7. Substance: a named, correctly attributed source; a concrete scene; a practical caveat; nothing fabricated. Any lens reference fits naturally; cut it if it feels bolted on.
8. Opens on the reader's side. Each output ends the way section 3 says.
9. Every subheading and the first line under it is a hook.
10. Confidentiality (section 4).
11. Word counts are in range.

## 7. Delivery

One delivery per run, to the user only. Never publish, post, or send content to anyone else.

Title or subject: "Content Engine: [framework name] (week of [Monday of the earliest week used])". Body, in this order:

1. **Theme:** one sentence, and why it was chosen.
2. **Framework.**
3. Each output in `outputs` order, ready to edit and ship.
4. **Sources:** meeting dates and first names only, for the user's eyes, so they can sanity-check confidentiality, plus one line flagging the riskiest detail.
5. **Alternative:** one other theme considered, in one line.
6. **Voice check:** one or two lines naming the judgment calls you were least sure of (a hook, a metaphor, a reference, a closer), so the user can give feedback.

| `delivery.method` | How |
| --- | --- |
| email | Send one email to `owner.email` with simple HTML headings and paragraphs plus a plain-text version |
| email-draft | Save the same email as a draft addressed to `owner.email` |
| notion | Create a child page under the configured page, titled as above |
| google-doc | Create a Google Doc in the configured folder, titled as above, and email `owner.email` the link if email is connected |

## 8. Content Log

The engine must never repeat a theme or framework within 60 days. Record each run:

- **Cortex:** one Ingest Log row. Source "Content Engine: [framework name]", Type Document, Date Ingested today, What Changed "Theme: [one line] | Framework: [name] | Outputs: [list] | Meetings: [dates]".
- **Otherwise:** a "Content Log" next to the config (a Notion database or a Markdown table) with columns Date, Theme, Framework, Outputs, Meetings Used, Delivered To.
