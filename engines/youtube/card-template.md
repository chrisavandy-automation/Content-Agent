# YouTube card template
Read by: `youtube-card`. One card per video, saved as `engines/youtube/drafts/YYYY-MM-DD-slug.md` (the Saturday it's recorded). Worked examples: `drafts/2026-11-07-five-ways-to-acquire-customers-with-ai.md` (a listicle of builds) and `drafts/2026-10-25-hallmark-landing-page-into-ghl.md` (one build end to end).

Fill every section. A missing fact stays a [bracket]; never invent one.

```
# <Working title>

Recording: <Saturday date>. Idea Bank (Notion): "<Angle>".

**Working title:** …
**Angle:** who it's for, what's wrong now, what I'll build on screen. Emotion: …
**Pillar:** one only, with one line on why. Filter: can I teach it with Claude or GoHighLevel?
**Story type · ARR · Lane · Mix · Stage · Momentum:** …
**Format:** build-first screen share (default) · length · shape (cold open, setup, N segments, close).
**Demo company:** `engines/youtube/demo-company.md`, or a new one (check Companies House), or "none, my own build".

**Guardrails:** what's made up and how I say so · what to blur · what not to show · no result numbers I don't have · credits · when it can be posted.

### Hooks
From `youtube-hooks`: 5 options (4 proven + 1 wildcard, one `plain`), each = title · thumbnail (2–4 words) · first 15 seconds · callout · promise · borrows · weakest lever + one move. I pick.

### Before recording (Thu–Fri)
1. Folder and demo inputs.
2. Installs (commands at the bottom of the card) and accounts, with the cost of each.
3. Dry-run every prompt off camera. Paste what broke into "Dry-run notes".
4. Graphics from "Production tools" in `engines/youtube/README.md`.
Status goes to Ready only when the dry run is done.

### Record from here
One Loom per beat.
**Beat 1. Cold open (15 s).** On screen · say the hook's first 15 seconds.
**Beat 2. Setup (60–90 s).** What's made up · what a skill is (if skills appear) · why this matters to the viewer.
**Beats 3…N. One per build or system.** Same moves each time:
  title card → explain prompt (Claude explains the brief) → install → run prompt(s) to paste → show the output → say where it stops and needs a person.
**Last beat. Close (30 s).** One ask (which one next, a comment question). No pitch.

### Description (paste when it's up)
What's made up · repos and credits · chapters [from the edit].

### Dry-run notes
[what broke, the command that actually worked, what each run cost]
```

## Rules
- Every "say" line and hook passes the 5Cs (`database/writing/gate.md` section A) and `python tools/slop_check.py`.
- First-15-seconds lines are in the future tense until the build exists, so they're true when written.
- A beat must show something on screen. A beat that is only me talking gets cut or becomes a 15-second line.
