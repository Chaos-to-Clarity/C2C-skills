# Chaos to Clarity Skills

Free Claude skills for founders and operators, from Eric Weiss at [Chaos to Clarity](https://chaostoclarity.io). Each one turns a recurring piece of work into a single message to Claude.

## Install in 2 minutes

1. Click a **Download** link below. A ZIP file downloads. Don't unzip it.
2. In Claude, open **Customize**, then **Skills**.
3. Click **Create skill**, then **Upload a skill**, and choose the ZIP.
4. Make sure the skill is turned on, then start a new chat and use it.

Skills you upload are private to your account. Nobody else sees your data.

## The skills

| Skill | What it does | Download |
| --- | --- | --- |
| Handwritten Notes | Photograph a page of notes. Checkbox items become tasks with time booked on your calendar. Everything else is filed as notes, linked to the right people and projects. | [handwritten-notes.zip](https://github.com/chaostoclarity/claude-skills/releases/latest/download/handwritten-notes.zip) |

Each skill has its own page in [`skills/`](skills/) with requirements and examples.

## Updating

Download links always serve the newest version. To update a skill you already installed, delete it in Claude's Skills settings and upload the new ZIP. Your settings carry over, because skills here store their configuration in your own tools, not in the skill file.

## Questions

Reach Eric at [chaostoclarity.io](https://chaostoclarity.io).

## For maintainers: adding or changing a skill

1. Add a folder under `skills/` named exactly like the skill's `name` (lowercase, hyphens).
2. Put `SKILL.md` in it, plus a short `README.md` for humans.
3. Keep the `description` under 200 characters, and keep personal details (IDs, emails, workspace links) out of the file.
4. Add a row to the table above using `https://github.com/chaostoclarity/claude-skills/releases/latest/download/<name>.zip`.
5. Commit and push to `main`. The release workflow checks every skill, builds the ZIPs, and publishes a new release. Links update automatically.

To test packaging locally: `python scripts/build_zips.py` (output goes to `dist/`).
