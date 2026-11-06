---
name: youtube-hooks
description: YouTube only. Writes hooks for one video angle, where a hook is a title + thumbnail text + the first 15 seconds I say on camera. Default 5 in the angle's lane (4 proven + 1 wildcard, one plain); "all lanes" gives 15 (Value, Emotion, Story). Tags each with its type, what it borrows and its weakest lever, no scores. Use at step 4 of youtube-card, or when I say "YouTube hooks for…", "titles for this video" or "thumbnail ideas".
---

# YouTube hooks
Reads: `database/writing/hooks.md` (types, the hook gate, my rules), `database/writing/virality.md` (lanes, levers), `database/writing/anti-ai.md`, `database/examples/hooks.md` (proven hooks), YouTube format notes in `engines/youtube/README.md`.
Optional research: `outlier-post-finder` (ScrapeCreators) on the creators the idea borrows from, for title shapes that overperformed. Borrow the shape, never the words.

1. **Angle:** confirm in one line: who it's for · what they get · target emotion · pillar. Fix it with me if fuzzy.
2. **Write the set.** Default 5 in the angle's lane: 4 PROVEN (each names its hook type or example) + 1 WILDCARD (names what it breaks from). At least one `plain`. "All lanes" = 15: 5 each in Value, Emotion, Story.
   Each hook has four parts:
   - **Title:** under ~60 characters where possible; says the promise.
   - **Thumbnail:** 2–4 words that add to the title, never repeat it.
   - **First 15 seconds:** what I say on camera, in the future tense until the build exists.
   - **Callout + promise:** named in a few words.
3. **Hook gate** (`database/writing/hooks.md`): callout + promise + the 5Cs + anti-AI (`python tools/slop_check.py` on the set, written to the scratchpad first; comma-before-a-name flags are false positives) + true (no results I don't have). Rewrite or drop every FAIL before showing anything.
4. **Show the set.** Each hook: title · thumbnail · first 15 s · callout ✓ promise ✓ · type · proven/wildcard (+ source) · weakest lever + the one move that would lift it. No scores, no winner picked for me.
5. **I pick** (or mix, or rewrite). Run my pick through the gate too. Offer up to 3 variations, each changing one lever.
6. Save the pick: on the card, in the Idea Bank row's Hook field, and at the top of `database/examples/hooks.md` (Platform: YouTube, Result: [after posting]).
Done when I've picked a hook and it's saved.
