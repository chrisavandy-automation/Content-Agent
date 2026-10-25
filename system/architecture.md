# Architecture
Built on the ARMS framework (Apps, Routines, Memory, Skills) from the RoboNuggets Agentic OS v2 guide. Every new file or skill should fit one of the layers below. If it doesn't, ask where it belongs before creating it.

## Memory (build first)
| Layer | What | File |
|---|---|---|
| L1 long-term | Plain-text maps, no vector database. Claude opens 2-3 files to answer anything. | `CLAUDE.md` (map) → `database/README.md` (router) → the file |
| L1 catalogue | One line per lesson, linked to its file | `MEMORY.md` |
| L2 short-term | Compact with a purpose: keep decisions, pillar changes, structures, templates | rule in `CLAUDE.md` |
| L3 self-evolving | A correction made twice means memory missed it: log it, fix the owning file | `MEMORY.md` + the file it belongs to |

Quick test: ask "where's X?". If Claude opens more than 3 files, the map needs another layer.

## Skills
| Type | What it does | Status |
|---|---|---|
| Database skill | Holds knowledge (examples + principles), not just steps. Reads `database/`. Pitches 70/20/10 with wildcards on by default. | Build first |
| Artifact skill | Makes posts, graphics, decks in HTML first from one brand book; exports at the end; saves to one inbox with an index | Next |
| Self-triggered skill | Runs from a dashboard button with `claude -p` | Waits for the dashboard |

Skill rules:
- Short `SKILL.md`; the examples and principles live in a database file the skill points to.
- Name skills by engine: `core-*` (shared), `linkedin-*`, `youtube-*`.
- Every content skill starts by reading `database/foundation/pillars.md`.
- When I like a wildcard, offer to add it to the references (that's how the database grows).
- Later (ARMS L2/L3): pin fixed-step skills to the smallest model; let feedback sharpen the skill (a principle, not another rule).

## Engines
`engines/<platform>/` holds only what's specific to that platform (formats, lengths, algorithm notes, its own skills' references). Anything true across platforms (pillars, voice, stories, proof) lives in `database/` so every engine shares it.

## Routines and Apps
Not yet. Routines get added as active or passive; apps once a job is routine enough to leave the chat.
