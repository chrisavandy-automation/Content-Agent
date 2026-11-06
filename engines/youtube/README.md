# YouTube engine
Platform-specific only: titles, thumbnails, cards, formats and production tools. Pillars, voice, stories and hook rules come from `database/`.

## Where things live
| Need | Go to |
|---|---|
| The idea bank (the only one) | Notion Idea Bank, `collection://2aa9d92a-d274-47d9-9acd-a4838e6d4295`, filter Platform = YouTube |
| The card template | `engines/youtube/card-template.md` |
| Cards (one per video) | `engines/youtube/drafts/YYYY-MM-DD-slug.md` (the recording Saturday) |
| The demo company | `engines/youtube/demo-company.md` (Hollowmere Heat Pumps, made up) |
| Skills | `youtube-card` (idea → card, ready for Saturday) · `youtube-hooks` (title + thumbnail + first 15 s) |

## The week
Mon–Thu is for ideas and the card. Fri–Sun is for producing.
| Days | What happens | Skill | Idea Bank status |
|---|---|---|---|
| Mon–Thu | Get ideas down (Platform: YouTube). Pick Saturday's video (the video test: is there a real build or demo to show?). Write the card: brain dump → angle → hooks → beats with prompts → guardrails → prep list. Card written = Ready | `core-ideate`, `youtube-card` | Idea → Drafting → Ready |
| Thu 17:39 | Check: is Saturday's card Ready? Pings me only if not | scheduled task | |
| Fri | Prep: installs, dry-run every prompt, graphics | the card | Ready |
| Sat | Record, one Loom per beat | the card | Ready |
| Sun | Edit, thumbnail, description, Shorts, post | (a `youtube-publish` skill after 2–3 videos) | Posted |

## Format (Superpowers breakdown)
Build-first formats lead: screen shares, voiceover walkthroughs, written-to-video breakdowns. Grow into talking to camera; don't start there.
- Hooks = title + thumbnail text + first 15 seconds. Thumbnails: 1280×720, 2–4 words, big type.
- Production tools (starred repos, all run locally: Node, ffmpeg, Chrome) make the video, never the system being demoed: attentionmachine-skills (edit my talking + Shorts cuts) · Claude Video 2.0 on HyperFrames (intro, section cards, lower-thirds) · explainroo (narrated "how it works" explainers, chapters, subtitles) · Argo (scripted browser walkthroughs with voiceover) · video-director (QA every render) · Take One (optional cold open; slow and token-heavy).
- Research for titles: `outlier-post-finder` (ScrapeCreators) on the creators the idea borrows from.
