---
name: linkedin-write
description: LinkedIn only. Takes one idea from brain dump to a gated draft: angle, hooks (linkedin-hooks), body, tighten, then the gate (linkedin-review), saved as a draft file and tracked in the Notion Idea Bank. Use when I say "let's write today's post", "write a post about…", "write this up", or pick an idea from the Idea Bank.
---

# Write
Reads: `database/writing/workflow.md` (the steps), `database/foundation/pillars.md`, `database/writing/structures.md`, `database/examples/index.md`, voice: LinkedIn-Agent `shared/voice-profile.md` (until a voice file exists in `database/foundation/`), platform notes in `engines/linkedin/README.md`.
Writes: `engines/linkedin/drafts/YYYY-MM-DD-short-slug.md` (planned posting date; one file per piece, overwritten as it improves), Notion Idea Bank row.

1. **Pick the idea:** from the Idea Bank (Status: Idea) or what I say. Set Status: Drafting.
2. **Brain dump:** ask me to talk it through (voice is fine). Ask 2-3 questions only for what's missing: the real moment, the number, what I actually did. Flag any line that might be someone else's: "yours or someone else's?"
3. **Angle:** 1-3 angles from the dump, each tagged pillar · story type · lane · emotion; give a one-line read on each. I pick.
4. **Hooks:** run `linkedin-hooks` on the chosen angle. I pick.
5. **Body:** the lane suggests the structure (`writing/virality.md` step 4); offer one alternative ("as a list instead?"). Use a skeleton: What/Why/How or But/Therefore. Borrow the shape of a matching example, never its words. Write WITH the 5Cs: one idea, my real details, my words.
6. **Tighten** to my voice. Save the draft file.
7. **Gate:** run `linkedin-review` on the file. Apply its fixes; bring me its questions.
8. **Hand over:** the draft + the gate card. I read it out loud and decide. Set Status: Ready only when I say so.
9. **After posting** (when I tell you): Status: Posted, Post link, mark the source story Used; ask for results after 48h and log them in the Idea Bank and `database/examples/hooks.md`. Strong performers go into `database/examples/index.md` as my own examples (pillar filled in).
