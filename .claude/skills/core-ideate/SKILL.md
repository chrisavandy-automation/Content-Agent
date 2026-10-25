---
name: core-ideate
description: Sunday ideation (or any time): turns my Story Bank, my week and what I'm building into 10 tagged content ideas (7 proven, 2 adjacent, 1 wildcard), each matched to a proven example, and saves my picks to the Notion Idea Bank. Use when I say "ideate", "Sunday ideation", "what should I post?", "give me ideas", or "plan my week".
---

# Ideate
Reads, in this order (open only what's needed):
1. `database/foundation/pillars.md` (who, A → Z, pillars, guardrails)
2. `database/ideation/life-inspiration.md` (story types, prompts, momentum loop)
3. Notion Story Bank (`collection://a4aea437-a40f-4443-990a-7dbb6790e6f7`): query the last 7 days, plus Used = no rows of any story type not used in 2 weeks. Never use a Private row; Ask first rows are marked as such.
4. Notion Idea Bank (`collection://2aa9d92a-d274-47d9-9acd-a4838e6d4295`): what's already banked, drafting or recently posted (avoid repeats; note pillar balance).
5. `database/examples/index.md`: filter by story + lane + structure; open at most 3 example files.
6. `system/wildcard.md`.

Steps:
1. **Warm-up (2 minutes):** ask me 2-3 prompts from `life-inspiration.md` for story types missing lately, and "anything you're building that's in the momentum loop?". Use my answers as raw material (offer to log new moments with `core-story-bank`).
2. **10 ideas**, each one line: the angle (idea + reader promise) · pillar · story type · lane (Value / Emotion / Story) · target emotion · mix · borrows from (example id, or for the wildcard: which reference it breaks from).
   - 7 PROVEN (follow a matching example), 2 ADJACENT (a shape from another pillar, creator or platform), 1 WILDCARD (matches nothing in the index; still fits a pillar and the A → Z).
   - Spread the pillars; flag if one pillar has had nothing in 2 weeks. Pillars 1-3 pass the filter "can I teach this with Claude or GoHighLevel?".
   - Momentum: if something is in the loop, one idea is its next stage.
3. Run the guardrails from `pillars.md` section 7 on every idea; drop or flag any that break them.
4. I pick. Save picks to the Idea Bank (Status: Idea, all tags filled, Source story linked if it came from the Story Bank; mark that story Used once it's drafted, not now).
5. If I loved the wildcard, offer to add it to `database/examples/` as a reference.
Done when my picks are in the Idea Bank. No scores, no "best idea" ranking: give a one-line read on each and let me choose.
