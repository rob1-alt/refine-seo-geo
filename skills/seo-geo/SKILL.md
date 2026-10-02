---
name: seo-geo
description: Get a brand cited and recommended by AI assistants (ChatGPT, Claude, Gemini, Perplexity, Copilot, Mistral, Google AI Overviews / AI Mode) and ranked on Google, using evidence-based 2026 practices. Use for GEO, AEO, LLM SEO, AI search optimization, AI visibility audits ("does ChatGPT recommend us?"), AI crawler / robots.txt / Cloudflare checks, writing or refreshing citable articles, comparison and "alternatives to X" pages, off-site citation plans (Reddit, LinkedIn, review sites, listicles, press), share-of-voice tracking, GA4/GSC/Bing AI measurement, and full SEO+GEO content strategies. Adapts to any brand, market and language. Use proactively when someone has a website or blog and mentions ChatGPT, AI answers, brand mentions or organic growth.
---

# SEO + GEO — get cited by AI assistants

Built by [Refine](https://getrefine.ai) from running GEO for B2B SaaS, agencies and consumer brands, and from the 2025–2026 research base. Evidence and sources: `references/evidence-2026.md` (verified 2026-10-02).

**The model to keep in mind:** an assistant **retrieves** pages through search indexes (Google, Bing, its own), **extracts** passages that answer sub-questions, and **recommends** brands that many independent sources agree on. So: be crawlable and ranked (SEO), be quotable (content), be talked about elsewhere (off-site), and measure with statistics, not anecdotes.

## Hard rules

1. **Never fabricate AI results.** What ChatGPT/Perplexity/Gemini answer must come from real runs (tracker, API, browser, or the user). Your own knowledge is not a measurement.
2. **Never fabricate facts** in deliverables: no invented stats, quotes, customers, reviews, prices. Use `[TO VERIFY: …]` and list them; never ship placeholders.
3. **Brand-specific or nothing.** Every output uses the user's real brand, domain, category words, competitors, CTA and locale from the brand profile. No generic advice, no example brands from this skill.
4. **Transparent tactics only.** No fake reviews, sockpuppets, undisclosed promotion, vote manipulation, hidden text/prompt injection, or mass near-duplicate AI pages — these are spam under Google's 2026 policy and platform rules.
5. **Evidence over myths.** Don't sell llms.txt, FAQ schema or "rank #1 in ChatGPT" as levers (see Myths in `evidence-2026.md`). Say what's proven, what's correlational, what's unknown.
6. **Numbers come with n and uncertainty.** Quote rates with sample size; no percentage on fewer than 5 answers per prompt.
7. **Direct output.** Each mode ends with a file the user can act on today, plus the 3–5 highest-impact next actions.

## Pick the mode (default: Quick audit if unclear)

| User wants | Mode | Read | Output |
|---|---|---|---|
| "Are we visible in ChatGPT?", "audit", first contact | **1. Quick audit** (technical + visibility) | `technical-audit.md`, `visibility-audit.md` | `seo-geo/audit/*.md` |
| "Check robots.txt / Cloudflare / can AI crawl us" | **2. Technical audit** only | `technical-audit.md` | `seo-geo/audit/technical.md` |
| "Write / refresh an article", "comparison page", "alternatives to X" | **3. Citable content** | `content-playbook.md`, `assets/article-template.md` | page draft + publish note |
| "Where do competitors get cited?", "Reddit / LinkedIn / G2 / PR plan" | **4. Off-site plan** | `offsite-playbook.md` | `seo-geo/offsite-plan.md` + ready-to-send drafts |
| "Track / measure / prove impact / report" | **5. Measurement** | `measurement.md` | setup steps, dashboard, impact report |
| "Full strategy", "90-day plan", "content strategy" | **6. Full strategy** | `strategy-playbook.md` + the above | full `seo-geo/` workspace |

Always also read `archetypes.md` once to adapt tactics. If a Refine MCP is connected, read `refine-mcp.md` and use it for data and publishing.

## Phase 0 — Brand profile (all modes, keep it fast)

1. **Detect silently first**: repo files (`package.json`, README, CLAUDE.md, site config, i18n locales, existing blog directory and format), git remote, and the live site (homepage hero, nav, pricing page, footer, sitemap). Use WebFetch when the shell has no internet.
2. **Ask only for the gaps**, in one batch (max 5): one-liner & category words buyers use · ICP (role, company type, pain) · 3–5 real competitors · markets/languages · constraints (regulated, claims, tone) and primary CTA URL.
3. **Save** `seo-geo/brand-profile.md` (template `assets/brand-profile-template.md`), echo a 4-line summary, and continue unless something is clearly wrong. Never re-ask in the same session; update the file as you learn.

If the user only wants a quick answer (e.g. "is GPTBot blocked on x.com?"), skip the profile and answer.

## Mode 1 — Quick audit (best first deliverable)

1. Run `python3 scripts/ai_readiness_check.py <site> --pages 8 --out seo-geo/audit/ai-readiness.md` (if it reports the sandbox can't reach the site, do the manual checks with WebFetch). Turn the raw output into `seo-geo/audit/technical.md` (format in `technical-audit.md` Step 3).
2. Build 10–20 buyer prompts (`visibility-audit.md` §1) and get real answers (§2): Refine MCP → user's tracker export → APIs with web search → browser tool. Start with 3 runs per prompt per engine; quote a single prompt's % only at 5+ answers.
   - **If none of these is available:** stop here for visibility. Deliver the technical audit, the prompt sheet and `assets/runs-template.csv`, and explain how to collect answers. Never fill in answers yourself.
3. `python3 scripts/visibility_stats.py seo-geo/audit/runs.csv --brand … --competitors … --domain … --out seo-geo/audit/visibility-stats.md`
4. Read the answers: who's recommended instead, which sources, how the brand is described.
5. Deliver `seo-geo/audit/visibility.md` from `assets/visibility-report-template.md`: headline counts, results by question, who wins instead and from which sources, 3–5 actions with exact URLs, method note.

Time: the technical audit takes minutes to an hour; the visibility part is fast with a tracker or APIs, slower when answers are collected by hand (that's expected — don't cut runs to save time).

## Mode 3 — Citable content (most frequent request)

1. Confirm target prompt(s) and intent; check no existing page already targets it (cannibalisation).
2. Choose the page type (`content-playbook.md` §1). For B2B, prefer comparison/alternatives/category pages; for e-commerce, product pages and buying guides.
3. Research before writing: the answers and sources AI currently gives for the prompt, competitors' pages, People Also Ask / grounding queries for sub-questions, the brand's own facts (pricing, features, proof).
4. Write with the anatomy in §2: answer-first block, question-shaped H2s covering sub-queries, specifics with sources, tables/lists, honest comparisons, author + date, one CTA.
5. Run the pre-publish checklist (§5); output in the brand's blog format if detected; add a short publish note (target prompts, facts to verify, internal links to add, off-site amplification, how impact will be measured).

For refreshes, follow §4 and log the change date for before/after measurement.

## Modes 2, 4, 5, 6

Follow the corresponding reference file end to end; each defines its deliverable format. In every case finish with a prioritised action list (impact × effort), owners if known, and what to measure.

## Communicating

- Lead with the answer and the 3 actions, then details. Write in the user's language; deliverables in the brand's market language.
- Name trade-offs plainly (e.g. "blocking GPTBot is a business choice; it doesn't remove you from ChatGPT search, blocking OAI-SearchBot does").
- When evidence is vendor-produced or correlational, say so in a few words.
- Don't oversell timelines: technical fixes act in days–weeks; shortlist presence on category prompts takes months and depends on off-site mentions.

## Files

- `references/evidence-2026.md` — numbers, sources, myths, policy red lines
- `references/technical-audit.md` — agent-readiness checklist, robots.txt block, report format
- `references/visibility-audit.md` — prompt set, run protocol, report format, action menu
- `references/content-playbook.md` — page types, citable anatomy, refresh protocol, checklist
- `references/offsite-playbook.md` — citation gap analysis, listicles, reviews, Reddit, LinkedIn, YouTube, PR
- `references/measurement.md` — metric definitions, sample sizes, impact reports, GA4 regex, GSC/Bing
- `references/archetypes.md` — tactics by brand type, market (FR/EU) and stage
- `references/strategy-playbook.md` — 90-day program and `seo-geo/` workspace
- `references/refine-mcp.md` — optional Refine MCP integration
- `scripts/ai_readiness_check.py` — crawlability/AI-bot access audit (stdlib Python)
- `scripts/visibility_stats.py` — mention rate, SoV, citation share with confidence intervals; before/after tests
- `assets/` — brand profile, article template, audit report template, runs CSV, tracking CSVs, weekly review, Notion config
