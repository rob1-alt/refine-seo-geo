# Changelog

## 3.0.0 — 2026-10-02

Full rewrite for the plugin marketplace.

- **Plugin format**: `.claude-plugin/plugin.json` + `marketplace.json`; skill moved to `skills/seo-geo/` (also uploadable to claude.ai as a zip).
- **Six modes** instead of one long playbook: quick audit, technical audit, citable content, off-site plan, measurement, full strategy. Each ends with a concrete file and the top 3–5 actions.
- **Evidence base** (`references/evidence-2026.md`): 2025–2026 data on what gets cited (answer-first, fan-out sub-questions, freshness, depth), off-site weight (earned media, YouTube, Reddit, LinkedIn articles, third-party listicles), technical facts (non-JS crawlers, bot roles, Cloudflare's Sept 2026 Search/Agent/Training split, Bing/IndexNow) and policy red lines (Google's 2026 spam policies on AI manipulation and scaled content).
- **Myths removed**: keyword density targets, FAQ schema as a GEO lever, llms.txt, "rank in ChatGPT", self-ranking listicles at scale.
- **New scripts**: `ai_readiness_check.py` (robots.txt per AI bot, access by user agent, raw-HTML/JS-shell detection, snippet controls, sitemap lastmod, JSON-LD) and `visibility_stats.py` (mention rate, share of voice, citation share with Wilson CIs, before/after significance).
- **Measurement**: explicit metric definitions, sample sizes, per-page impact reports, GA4 AI channel regex, GSC generative-AI reports, Bing AI Performance grounding queries, self-reported attribution.
- **Off-site playbook**: citation gap analysis, listicle outreach, review sites, disclosed Reddit, LinkedIn articles, YouTube, original data, with templates.
- **Visibility report template** based on the report format Refine sends to brands.
- **Optional Refine MCP integration** for live tracking data and publishing.
- New markets/engines: Mistral Le Chat, Copilot, Google AI Mode; France/EU specifics.
- Templates and CSV trackers rebuilt around prompts, mention rates and impact.

## 2.0.0 — 2026-04-28
Brand-aware refactor: auto-detected brand profile, archetypes, `seo-geo/` output directory.

## 1.0.0
Initial release.
