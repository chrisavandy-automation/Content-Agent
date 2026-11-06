---
name: youtube-card
description: YouTube only. Takes one idea from the Notion Idea Bank to a card I can record from on Saturday: the video test, brain dump, angle, hooks (youtube-hooks), beats with the prompts to paste, guardrails, demo company and the Friday prep list, saved as a draft file and tracked in the Idea Bank. Use when I say "plan Saturday's video", "make the card", "YouTube card for…", "what am I recording this week?", or pick a YouTube idea from the Idea Bank.
---

# YouTube card
Reads: `database/foundation/pillars.md` first, then `engines/youtube/README.md` (the week, formats, production tools), `engines/youtube/card-template.md` (the card and its rules), `engines/youtube/demo-company.md` if the video needs a demo business.
Writes: `engines/youtube/drafts/YYYY-MM-DD-slug.md` (the recording Saturday), the Notion Idea Bank row (`collection://2aa9d92a-d274-47d9-9acd-a4838e6d4295`).

Rule for every step: nothing is shown to me until it passes the 5Cs (`database/writing/gate.md` section A) and is true. Fix first, then show.

1. **Pick (any day Mon–Thu).** Query the Idea Bank for Platform = YouTube, Status Idea or Ready. Show me up to 5 with one line each, or take the one I name. Run the **video test**: is there a real build or demo I can show on screen? If not, say so and suggest the build that would make it one, or another idea. Set Status: Drafting and Planned date: the coming Saturday.
2. **Brain dump.** Ask me to talk it through (voice is fine). Ask 2–3 questions only for what's missing: what I'll build on screen, what's real and what's demo, what the viewer leaves able to do. Flag any line that might be someone else's.
3. **Angle.** 1–3 angles, each tagged pillar · story type · lane · emotion · mix, with a one-line read each. I pick.
4. **Hooks.** Run `youtube-hooks` on the chosen angle. I pick.
5. **Beats.** Fill the "Record from here" section of the card template. Every build beat has: on screen · the explain prompt · install command · run prompt(s) to paste · what to show · where it stops and needs a person. Prompts must be ones I can dry-run. If the video needs a business, use the demo company or make a new one (check Companies House; say it's made up on screen).
6. **The rest of the card.** Guardrails (what's made up, what to blur, what not to show, no result numbers I don't have, when it can be posted), the description, install commands with costs, the Friday prep list.
7. **Check.** `python tools/slop_check.py` on the card (proper-noun comma flags are false positives). Fix every real flag.
8. **Hand over.** Save the card, put its path in the Idea Bank row's Notes, give me the hook I picked and the prep list. Set Status: **Ready** once I've picked the hook and the card is saved (the Thursday check looks for this). The dry run happens Friday, from the card's prep list.
9. **After posting** (when I tell you): Status: Posted, Post link; after 7 days ask for views, watch time and comments and log them in Result. Anything I'd change next time goes into `card-template.md` as a rule, shorter not longer, and one line in `MEMORY.md`.
Done when the card is saved and the Idea Bank row points to it.
