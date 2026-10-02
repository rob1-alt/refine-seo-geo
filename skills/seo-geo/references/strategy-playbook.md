# Full strategy playbook (90 days)

Use when the user wants a complete SEO + GEO program, not a single deliverable. Everything reads from `seo-geo/brand-profile.md` and writes to `seo-geo/`.

## Week 0 — Diagnose (deliver in the first session)
1. Brand profile (SKILL.md Phase 0).
2. Agent-readiness audit → `audit/technical.md` (`technical-audit.md`).
3. AI-visibility snapshot on 10–20 prompts → `audit/visibility.md` (`visibility-audit.md`). Without a tracker or API keys, collecting answers takes longer: deliver the technical audit + prompt sheet first, the visibility numbers when answers are in.
4. One-page diagnosis: where the brand stands, top 3 gaps, top 5 actions.

## Weeks 1–2 — Plan
**Prompt universe** (`05-prompt-universe.csv`): 30–100 prompts to start (expand to 200+ only if a tracker runs them), tagged by type (Category, Use case, Comparison, Alternatives, Full offer, Educational, Branded, Local), funnel stage, priority, language/market. Use real buyer language: sales calls, support tickets, Reddit threads, People Also Ask, GSC queries, Bing grounding queries, competitor comparison pages.

**Keyword ↔ prompt map** (`02-keywords-backlog.csv`): for each priority prompt, the search queries that retrieve sources (GSC, keyword tool, Bing). Selection: real demand (any volume for B2B niche; ≥50/month otherwise), intent close to conversion, brand can be cited naturally, competitors present in AI answers. Volume is a weak signal for AI prompts; business value and gap matter more.

**Clusters** (`03-content-clusters.csv`): 2–4 clusters, each = 1 pillar (category/what-is page) + 4–6 satellites (comparisons, use cases, how-tos, pricing explainers). One intent per page; no cannibalisation.

**Off-site plan** (`offsite-plan.md`, `04-citation-tracker.csv`) from the citation gap analysis.

**Measurement setup**: tracker running (Refine or other), GA4 AI channel, GSC + Bing WMT, self-reported attribution field. Baseline locked.

## Weeks 3–10 — Execute (weekly rhythm)
- 1–2 new pages/week (comparison and category pages first for B2B), each with the pre-publish checklist.
- 1 refresh/week of an existing page targeting a tracked prompt.
- 3–5 off-site actions/week (list outreach, review requests, Reddit answers, LinkedIn article).
- 1 original data piece per quarter.
- Monday 30-min review (`assets/weekly-review-template.md`).

## Weeks 11–12 — Prove & iterate
- Impact report per page and per off-site action (`measurement.md` §3).
- Keep what moved mention rate significantly; drop what didn't; re-plan next 90 days.

## Realistic expectations to set upfront
- Technical fixes (unblocking bots, SSR) can show effects within days to weeks.
- New brands typically get first mentions on long-tail and full-offer prompts within weeks; category shortlists take months and depend on off-site mentions.
- Expect noise: week-to-week swings inside the CI mean nothing.

## Output directory

```
seo-geo/
├── brand-profile.md
├── audit/ (technical.md, ai-readiness.md, visibility.md, visibility-stats.md, runs.csv)
├── 01-editorial-calendar.csv
├── 02-keywords-backlog.csv
├── 03-content-clusters.csv
├── 04-citation-tracker.csv
├── 05-prompt-universe.csv
├── 06-performance-dashboard.csv
├── 07-competitor-tracking.csv
├── offsite-plan.md
├── articles/[slug].md
└── notion-package/ (optional)
```

If the project has a blog directory (`content/`, `posts/`, `src/content/blog`, etc.), also write articles there in the detected format.

## Optional: Notion / Sheets workspace

Copy the CSV templates from `assets/` pre-filled with the brand's data into `seo-geo/notion-package/`, plus `assets/properties-config.md` (property types, views, relations) and a README with the 15-minute import steps (Import → CSV for each database, then set property types and relations as in properties-config). If a Notion connector is available, offer to create the databases directly instead.
