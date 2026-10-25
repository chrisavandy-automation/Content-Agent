# Database (router)
Everything the skills know. Plain text only. Each file below lists what it holds and its structure, so a skill can go straight to the right section.

## foundation/ (who I am and who I'm for: read first)
| File | Holds | Structure |
|---|---|---|
| `foundation/pillars.md` | The ICP: who I help, A → Z, association, pillars, PTL, ARR, stance, pre-publish checklist | Numbered sections 1-8. Pillars table: # · Pillar · Superpower · What goes in it · Proof · Guardrails |


## ideation/ (how to find ideas)
| File | Holds | Structure |
|---|---|---|
| `ideation/life-inspiration.md` | Story Bank habit, the 6 story types + prompts, the momentum loop, how the ideate skill uses them | Sections: Principle · Raw material · 6 story types (tag table) · Momentum loop · How the skill uses it |

## writing/ (how to write)
| File | Holds | Structure |
|---|---|---|
| `writing/hooks.md` | Hook anatomy, the 10 (+plain) hook types, best-practice checklist, my rules, the battle test (4 proven + 1 wildcard) | Tag table + checklists |
| `writing/virality.md` | The 3 viral formats as lanes (Value · Emotion · Story), the no-scores rule, the 15-hook flow | Lane table + flow steps |
| `writing/workflow.md` | Brain dump → shape → hooks → body → tighten → my read | 6 steps |
| `writing/gate.md` | THE pre-publish gate: 5Cs, hook/body/CTA, anti-AI + guardrails (pass/fail), then my calls (emotion, interesting, trust/authority) asked, never scored | Sections A-D + output card |
| `writing/anti-ai.md` | Pass/fail gate, do's, banned words, style rules (`tools/slop_check.py` automates part of it) | Sections |
| `writing/structures.md` | The 10 post structures: when and how | Tag table: tag · structure · best for · how to write |

## examples/ (proven posts and videos to borrow the shape of)
| File | Holds | Structure |
|---|---|---|
| `examples/README.md` | The tag vocabulary and how skills use examples | Column table + usage rules |
| `examples/hooks.md` | Hook swipe file (75 migrated + my winners) | Columns: date · hook · type · lane · creator · pillar · mix · result · notes |
| `examples/index.md` | One row per example (100 Jay Yang hooks so far), best results first | Columns: id · creator · platform · pillar · story · lane · hook · structure · result · notes |
| `examples/<creator>.md` | Posts per creator: `chris.md` (my 17 posted Publish30 posts, full text + results), `jay-yang.md` (100 hooks) | `## <id>` per post |

## Notion (what I write day to day)
| Where | Holds | Structure |
|---|---|---|
| Notion: Content Engine → **Story Bank** (`collection://a4aea437-a40f-4443-990a-7dbb6790e6f7`) | One row per story-worthy moment | Moment · Date · Story type · Pillar · Privacy · Story · Notes · Used · Post link |
| Notion: Content Engine → **Idea Bank** (`collection://2aa9d92a-d274-47d9-9acd-a4838e6d4295`) | Every idea from banked to posted | Angle · Status (Idea/Drafting/Ready/Posted/Parked) · Pillar · Story type · Lane · Emotion · Mix · Borrows from · Platform · Source story (→ Story Bank) · Planned date · Hook · Post link · Result · Notes |
Query both narrowly (e.g. Story Bank last 7 days, or Used = no + one story type; Idea Bank by Status). Never post a row marked Private; Ask first needs my OK.

Coming next (as I feed them in): voice, proof and numbers.

## sources/ (raw material I've fed in)
Kept as-is so we can always go back to the original. Distil what matters into a database file; skills read the database file, not the source.
| File | What |
|---|---|
| `sources/niche-and-pillars-lesson.md` | LinkedIn course lesson: brand = pairing, PTL, ARR, niche by transformation, checklist |
| `sources/inspiration-from-your-life-lesson.md` | Jay Yang lesson: Story Bank, 6 story types, momentum loop (distilled in `ideation/life-inspiration.md`) |
| `sources/art-of-the-hook-lesson.md` | Jay Yang lesson: hooks (distilled in `writing/hooks.md`) |
| `sources/post-structures-lesson.md` | Jay Yang lesson: 10 post structures (distilled in `writing/structures.md`) |
| `sources/ai-assist-and-viral-formats-lesson.md` | Jay Yang: using AI to assist, anti-AI checklist, 3 viral formats |
| `sources/viral-hook-science-deck.md` | Jay Yang deck notes: the 12 moves for value hooks (private course material) |
| `sources/5c-writing.md` | The 5Cs of writing + hooks, bodies, CTAs (employer references removed) |
| `sources/editing-checklist-lesson.md` | Jay Yang: editing checklist, 7 emotions, questions |
| `sources/arms-agentic-os-v2-guide.pdf` | RoboNuggets ARMS v2 guide: the 12 levels this system is built on (distilled in `system/architecture.md`) |
| Notion: "Your Superpowers: The Breakdown" (North Star + Superpowers) | Build / Architect + Measure / Teach, the one-liner, the camera point. Distilled into `foundation/pillars.md` (not copied here; read it in Notion) |

## Adding a file
1. Put it in the right folder (`foundation/` for identity; new folders for banks like hooks or stories).
2. Add a row here: file, what it holds, its structure.
3. If a skill should use it, add it to that skill's "Reads" line.
