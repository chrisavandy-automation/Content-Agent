# YouTube engine
Platform-specific only: titles, thumbnails, scripts, video formats and YouTube skill references. Pillars, voice and stories come from `database/`.
Status: not built yet. An early YouTube agent (with a 15-idea bank) is staged in the Superpower-Newsletter repo, `youtube-agent/` folder; review it before building this.

Format rule (Superpowers breakdown): build-first formats lead, i.e. screen shares, voiceover walkthroughs, written-to-video breakdowns. Grow into talking to camera; don't start there.
- Production tools (starred repos, all run locally: Node, ffmpeg, Chrome) make the video, never the system being demoed: attentionmachine-skills (edit my talking + Shorts cuts) · Claude Video 2.0 on HyperFrames (intro, section cards, lower-thirds) · explainroo (narrated "how it works" explainers, chapters, subtitles) · Argo (scripted browser walkthroughs with voiceover) · video-director (QA every render) · Take One (optional cold open; slow and token-heavy).
- Hooks = title + thumbnail text + first 15 seconds: a `youtube-hooks` skill (to build; same lanes and database as `linkedin-hooks`). Drafts: `engines/youtube/drafts/`.
