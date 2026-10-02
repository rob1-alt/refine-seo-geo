# Measurement — prove what works

Buyers' top two complaints about GEO are "how do I produce enough good content" and "how do I prove it worked". This file covers the second. Principle: **rates with error bars, explicit definitions, before/after per action.**

## 1. Metric definitions (print them in every report)

| Metric | Definition | Notes |
|---|---|---|
| **Mention rate** | answers mentioning the brand ÷ answers, over a prompt set × engines × runs | Primary KPI. Report with 95% CI (Wilson). |
| **Share of voice (SoV)** | brand mentions ÷ mentions of all tracked brands (brand + named competitors) | Depends on the competitor list — keep it fixed over time. |
| **Citation share** | answers citing a URL on the brand's domain ÷ answers with at least one cited URL | Separate from mentions: you can be mentioned without being cited and vice versa. |
| **Average position** | mean order of first mention when mentioned | Unstable (<1/1000 same order). Secondary at most. |
| **Accuracy** | % of brand descriptions with correct category/pricing/features | Spot-check 10 answers/month. |
| **AI referral sessions & conversions** | GA4 custom channel below | Small, under-counted (app clicks often arrive as Direct). |
| **AI impressions** | GSC generative-AI report (AI Overviews / AI Mode impressions, no queries/clicks) · Bing WMT AI Performance (citations + grounding queries) | First-party, free. |
| **Self-reported attribution** | "How did you hear about us?" field with "ChatGPT / AI assistant" option on signup/demo forms + CRM property | The most convincing B2B signal for leadership. |

## 2. Sample size & reliability

- ±10 pts needs ~100 answers; ±5 pts ~385. Get there by pooling: 20–50 related prompts × 3–4 engines × 3–5 runs.
- Never quote a percentage on fewer than 5 answers for a single prompt; show counts ("2 of 3").
- Keep prompts, engines, locale and competitor list stable; when you change the set, restart the baseline.
- `scripts/visibility_stats.py` prints CIs and flags small samples.

## 3. Per-content impact report (before/after)

For each published or refreshed page:
1. **Baseline**: target prompts tracked ≥ 7–14 days before publishing (or use the history if a tracker exists).
2. **After window**: 14–30 days after indexing (AI engines can pick up changes within days; Google AIO follows indexing).
3. Compare mention rate on target prompts before vs after:
   `python3 scripts/visibility_stats.py runs.csv --brand X --split-date YYYY-MM-DD --prompts-file targeted.txt`
4. Add: is the new URL cited? GSC clicks/impressions on the page; AI referral sessions to the page; conversions.
5. Control: compare with untargeted prompts over the same period (if they rose equally, it's not the page).
6. Verdict: "significant / not significant (could be noise)". Correlation, not proof — list other changes in the period.

Template line for the dashboard: `Page · published · target prompts · mention rate before → after (p) · cited? · GSC clicks · AI sessions · conversions · verdict`.

## 4. GA4 setup (AI referral traffic)

GA4 has a native "AI Assistant" channel (since 2026-05-13) but it misses Perplexity, Claude, Meta AI and Mistral and isn't retroactive. Create a custom channel group:

Admin → Data display → Channel groups → Create new → add channel **"AI assistants"** placed **above Referral**, condition *Session source* matches regex:

```
.*(chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|copilot\.cloud\.microsoft|edgeservices\.bing\.com|chat\.mistral\.ai|meta\.ai|chat\.deepseek\.com|grok\.com|you\.com|phind\.com|poe\.com|kagi\.com).*
```

Also: exploration report "Session source / Landing page / Key events" filtered on that channel. AI Overviews/AI Mode clicks can't be separated from Google organic in GA4. ChatGPT appends `utm_source=chatgpt.com` to many links.

## 5. Free first-party data to connect

- **Google Search Console** → Performance → generative AI report (impressions by page/country/device). Pair with classic query data to find prompts' search-side demand.
- **Bing Webmaster Tools** → AI Performance: citations, cited pages, **grounding queries** (real phrases AI used to retrieve your content) → feed them into the prompt set and H2s.
- **Server/CDN logs**: ChatGPT-User / Claude-User / Perplexity-User hits per page.
- **CRM**: self-reported attribution + deals whose first touch is an AI-referral session.

## 6. Weekly loop (30 minutes, Monday)

Use `assets/weekly-review-template.md`:
1. Mention rate & SoV (with CI) vs last week and vs 4 weeks ago — react only to moves outside the CI.
2. Prompts that moved; new competitors appearing (Refine `get_recent_changes`).
3. New sources cited; status of off-site actions.
4. Published/refreshed pages: impact report status.
5. Pick next week's 3–5 actions (one content, one refresh, 1–3 off-site).

## 7. Monthly report to leadership (1 page)

Mention rate & SoV trend (with CI) · top 3 wins with evidence · AI referral sessions & conversions · self-reported "AI assistant" leads · what we'll do next month. No vanity "rank #1 in ChatGPT" claims.
