# 5 game-changing ways to acquire new customers with AI (YouTube long-form)

Status: research done, script not written. Pillar 2 (How to do it). Stage: Acquire.
Idea Bank card: "10–30 life-changing ways to acquire clients with Claude + GHL".
Systems and skills come from my Acquisition Systems Skill Map (6 Nov). This file says what each skill actually does when it runs, from reading every SKILL.md on 6 Nov 2026.

## Open before recording
- **Demo company:** the one from the landing-page video plan. That plan is in a Cursor canvas I can't open: [name + one line on what it sells].
- **Timing:** the Idea Bank card says wait for André M2 (9 Nov) and teach from the brain framework names, not the client catalogue. Don't show the catalogue PDF on screen.
- **Paid accounts:** system 2 needs Higgsfield credits (or a HeyGen plan); systems 1 and 4 work better with a ScrapeCreators key. Decide tonight.

## How the recording works
1. Record each system as its own Loom (easier to redo one). Download the MP4s.
2. Flub a line? Pause, then say it again from the start of the sentence. attentionmachine keeps the best take and drops the rest.
3. Hand the files to attentionmachine for the clean-up and captions, then do your own pass: cut anything that doesn't move the build forward.
4. Graphics, explainers and QA: see "Production tools" in `engines/youtube/README.md`.

Every segment has the same shape: **Claude explains the brief → install the skills → run → show the output → where it stops.**

---

## 1. AI ad creative at volume (image ads)

**What the viewer sees:** competitor ads go in, 50 grounded ad concepts come out, ready to pick from.

**The skills, in the order they run**
1. `ad-library-teardown` (ScrapeCreators). Finds the competitor in the Meta, Google or LinkedIn ad library, pulls their **active** ads (and video transcripts), groups them by pain point, offer, proof and objection, then writes a swipe file of hooks, headlines and CTAs plus "recommended tests for us". Output: one markdown teardown.
2. `ad-creative` (marketingskills), **Mode 3: scaled static batches**. This is the core. It won't start without a grounded inputs folder:
   ```
   inputs/winning-ads/   10–20 screenshots of the best ads
   inputs/reviews/       50–100 customer reviews
   inputs/comments/      ad comments (objections and praise)
   brand/                voice, hex codes, logo
   ```
   If `winning-ads/` or `reviews/` is empty it stops and asks. That's a good on-screen moment: "AI ads fail on bad inputs, not bad writing." It then cycles through its static template library (Us vs Them, Stat Callout, Review Card, Before/After, Founder Message, FAQ Card…), and every concept cites the review or ad it came from. Output: `outputs/YYYY-MM-DD/INDEX.md` + one file per concept (headline, body, visual brief, image prompt, source).
3. **Creative review page**: `ad-creative` also fills an HTML template that shows each concept as an Instagram/Facebook feed mockup. Great B-roll, and it's how a client picks winners.
4. `image` (marketingskills). Turns the image prompts into images if you have a key for Gemini (Nano Banana), Flux or Ideogram. Without a key you stop at prompts; the Canva route from your own build also works.

**Needs:** ScrapeCreators API key (paid per request) for step 1, or screenshot competitor ads by hand from the Meta Ad Library. An image-model key for step 4.
**Prep tonight:** fill `inputs/` for the demo company (made-up reviews labelled as made up).
**Where it stops:** it writes and plans; a person uploads and presses launch. Mortgage, finance and health ads have rules a skill doesn't know.

---

## 2. AI video ads, customer-made (UGC) style

**What the viewer sees:** a product photo and a script go in, a phone-style "customer" video comes out.

**The skills**
1. `ugc-video-auto` (AKCodez/higgsfield-claude-skills). Drives the Higgsfield website through **Playwright MCP**: generates a character image (Soul model), sends it to the video page, adds a UGC prompt, generates a Seedance video. It **asks before every generation** and shows the credit cost on the button.
2. `higgsfield-generate` (higgsfield-ai/skills). The official CLI version. Its **Marketing Studio** mode is the one to show: give it a product URL ("click-to-ad"), it imports the product, picks a preset avatar, and makes the ad video. There's also a "virality predictor" score.
3. `heygen-video` (heygen-com/skills). Presenter-style video from a script with an avatar and voice. Needs a HeyGen API key or the HeyGen MCP on a paid plan.

**Needs:** Higgsfield account with credits (both Higgsfield skills). HeyGen only if you want the presenter version, so skip it like you did for video prospecting.
**Recommendation:** show `higgsfield-generate` Marketing Studio only. One product, one ad, show the cost screen. Cheapest honest demo.
**Where it stops:** an AI "customer" isn't a real customer. Label it, and never pass it off as a testimonial.

---

## 3. Cold email on buying signals

**What the viewer sees:** a signal (a company hiring for the job you replace) turns into a scored lead and a first line written from that signal.

**The skills**
1. **Agent-Reach** (your star; not in the skill map). The free signal source: public LinkedIn job posts, Reddit and X posts asking for help, GitHub activity. `agent-reach linkedin` job search needs no login.
2. `prospecting` (marketingskills). Pick the branch (SaaS / B2B / local) → define the ICP → build the list → qualify each one → score and rank → output a lead sheet (chat table, or CSV over 25 rows). Defaults to free sources + browser if you have no Apollo or Clay. It refuses bulk LinkedIn or Google Maps scraping, which is worth saying on camera.
3. `playbook-hiring-surge` (coldoutboundskills). Writes the one clause that completes "Noticed …" from department hiring counts. **Built on Clay's free headcount action, so it needs a Clay account.** Without Clay, show its rules and let Claude write the line from the Agent-Reach job post instead.
4. `cold-email` (marketingskills). Writes the email and the follow-ups: peer tone, the personalisation must connect to the problem, one low-friction ask, a quality check before send.
5. `email-deliverability-audit` (coldoutboundskills). Checks SPF/DKIM/DMARC by DNS, then inbox health, bounces and spam placement **from Smartlead**. Only the DNS part works without a running Smartlead account.

**Needs:** nothing paid for the demo (Agent-Reach + Claude). Clay or Smartlead only for steps 3 and 5 in full.
**Where it stops:** new sending domains need 2–3 weeks to warm up. Show the list, the lines and the sequence; don't fake sends. Real numbers: `chris-vandy-brain/playbooks/signal-based-cold-outreach.md` (~$200–400/mo running).

---

## 4. Search pages at scale + AI answer visibility (AEO)

**What the viewer sees:** "is the business cited when people ask ChatGPT?" → a page plan → one page template → many pages.

**The skills**
1. `ai-seo` (marketingskills). The AEO audit, and the best on-screen moment of the video:
   - Step 1: test 10–20 buyer queries ("best [service] for [situation]", "[brand] vs [competitor]") in Google AI Overviews, ChatGPT and Perplexity, and log who gets cited.
   - Step 2: why competitors get cited (structure, stats, freshness, schema, Reddit/review presence).
   - Step 3: extractability check per page (clear first-paragraph answer, FAQ, comparison tables, author, updated date).
   - Step 4: AI bot access check in robots.txt (OAI-SearchBot, PerplexityBot, Claude-SearchBot…).
2. `programmatic-seo` (marketingskills). Picks one of 12 playbooks (location pages, comparisons, "[service] for [profession]"…), researches the keyword pattern, defines the data each page needs, designs the template, internal links and indexing. Its rule: unique value per page or don't build it.
3. `seo-programmatic` (claude-seo, your star). Checks the plan: thin-content gates, uniqueness, canonicals, sitemap, and Google's 2025–26 scaled-content-abuse rules. Gives a score out of 100 with critical / high / medium fixes.
4. `schema` (marketingskills). Writes the JSON-LD (FAQPage, Organization, Breadcrumb) and tells you to validate it.

**Needs:** nothing paid. A real-looking site for the demo company (the landing-page video's page works).
**Where it stops:** pages take weeks to index and rank. Show the audit, the plan and 3–5 built pages, not results.

---

## 5. Quiz or free-resource funnel

**What the viewer sees:** a scored quiz page that captures the lead first, gives a personal result, and routes by score.

**The skills**
1. `scorecard-marketing` (wondelai). The method, in four steps:
   - Landing page: a "score" hook ("Are you ready to [goal]?"), "takes under 3 minutes".
   - Questionnaire: **contact form first**, 8–15 questions for cold traffic, 2–7 categories, 1–5 points per answer, plus qualifying questions (budget, urgency, size).
   - Results page: overall score + category breakdown, Low/Medium/High tiers with different copy.
   - Follow-up: a different CTA per tier (low → free resource, medium → book a call, high → consultation).
2. `lead-magnets` (marketingskills). If you'd rather give away a resource than a quiz: matches the magnet to the buyer stage, the gating, the landing and thank-you pages.
3. `popups` (marketingskills). Exit-intent or scroll popup to push site traffic into the quiz.
4. `frontend-design` (anthropics/skills), or Hallmark from the landing-page video. Builds the page itself as one HTML file.

**Needs:** nothing paid. Your own `coaches-lead-magnet-builder` plugin also covers the resource route.
**Tie-in:** the landing-page video deploys this into GHL; mention it as "full build in another video".

---

## The YouTube long-form + Shorts system (the one I'm running on myself)

This is the system the skill map lists as #10. These skills plug straight into making this video:

| Skill | What it does | Use it on this video |
|---|---|---|
| `outlier-post-finder` (ScrapeCreators, your star) | Pulls a creator's videos, finds the ones far above their normal views, explains why, and builds a swipe file of hooks and formats. Needs the ScrapeCreators key. | Run it on Nick Saraev and the other creators from the Idea Bank card before writing the title and the first 15 seconds. |
| `content-strategy` (marketingskills) | Plans pillars and topic clusters, sorts content into "searchable" vs "shareable", maps keywords to buyer stage. | Decide whether this video is a searchable one (title it like a search) or a shareable one (title it like a claim), and what the next 3 videos are. |
| `remotion-captions` (remotion-dev) | Short Remotion helper: transcribe, display and animate captions. | Skip. attentionmachine already does captions. |
| `higgsfield-youtube-thumbnail` (higgsfield-ai) | Asks for the truthful promise, who appears (it uses your face photo), an optional 2–4 word headline and the ratio. Comes up with at least 5 concepts internally, renders the best (or up to 4 variants, capped at 16 generations), then lets you tweak. Never copies a reference thumbnail's identity. Uses Higgsfield credits. | Covers the thumbnail gap from the earlier list. Give it 2–3 photos of you and the headline. |

So the YouTube system is the same loop I'm building in `engines/youtube/`: outliers → angle → record → edit → thumbnail → Shorts. When that engine gets built, these become its skills.

---

## Install commands (from the skill map)
```bash
npx skills add coreyhaines31/marketingskills --skill ad-creative --skill image --skill cold-email --skill prospecting --skill ai-seo --skill programmatic-seo --skill schema --skill lead-magnets --skill popups --skill content-strategy -a claude-code
npx skills add ScrapeCreators/social-media-research-skills --skill ad-library-teardown --skill outlier-post-finder -a claude-code
npx skills add higgsfield-ai/skills --skill higgsfield-generate --skill higgsfield-youtube-thumbnail -a claude-code
npx skills add growthenginenowoslawski/coldoutboundskills --skill playbook-hiring-surge --skill email-deliverability-audit -a claude-code
npx skills add AgriciDaniel/claude-seo --skill seo-programmatic -a claude-code
npx skills add wondelai/skills --skill scorecard-marketing -a claude-code
npx skills add anthropics/skills --skill frontend-design -a claude-code
```
Agent-Reach: tell Claude Code "Install Agent Reach: https://raw.githubusercontent.com/Panniantong/Agent-Reach/main/docs/install.md".
If the CLI won't take several `--skill` flags in one command, run one command per skill (`--skill <name>` each time). Check each one installed with `npx skills list`, and read its SKILL.md once before recording.
