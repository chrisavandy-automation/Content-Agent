---
name: core-review
description: The publish gate, with fresh eyes: runs database/writing/gate.md on a draft (5Cs, hook/body/CTA, anti-AI and guardrails as pass/fail; then my calls as questions, never scored) and returns one card. Use at step 7 of core-write, or when I paste a draft and say "review this", "check this" or "gate this", including drafts I wrote myself.
model: sonnet
---

# Review (the gate)
Reads: `database/writing/gate.md` (the checklist and the card), `database/writing/anti-ai.md`, `database/foundation/pillars.md` (section 7 guardrails).
Fresh eyes: review the draft as written, not the conversation that made it. Assume it has problems; find them.

1. Save the draft to the scratchpad if it isn't a file; run `python tools/slop_check.py <file>`.
2. Sections A-C of the gate: PASS or FAIL for each line. Every FAIL quotes the line and gives the fix.
3. Section D: ask me each question with your honest one-line read. Don't answer for me.
4. Return the card: A-C results · the fixed draft (fixes applied, changes listed) · the D questions. No overall score, no "ready to post".
Done when the card is shown and every FAIL is fixed or I've overruled it.
