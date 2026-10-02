# Agent-readiness technical audit

Goal: make sure AI search engines and AI agents can **reach, read and trust** the site. This is what agencies sell as a "GEO audit"; with this checklist it takes about an hour. Output: `seo-geo/audit/technical.md` with a score, findings ranked by severity and copy-paste fixes.

## Step 1 — Run the script (if the environment has internet access)

```bash
python3 scripts/ai_readiness_check.py https://example.com --pages 8 --out seo-geo/audit/ai-readiness.md
```

It checks robots.txt per bot, HTTP access per user agent (403s, Cloudflare challenges), raw-HTML content (what non-JS crawlers see), meta robots/snippet controls, JSON-LD, dates, sitemap and lastmod. If it exits with "Cannot reach … from this environment", the sandbox has no open internet: do Step 2 manually with WebFetch (fetch `/robots.txt`, `/sitemap.xml`, the homepage and 3–5 key pages) and say so in the report.

Spoofed user agents ≠ real verified bots. Treat a block as "verify now", a pass as "probably fine". Confirm in the CDN dashboard and logs (Step 3).

## Step 2 — Checklist (severity in brackets)

### A. Access & crawl control
1. **[Critical] Search and user-fetch bots allowed** in robots.txt: `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`, `Googlebot`, `Bingbot`, `Applebot`, `MistralAI-User`, `DuckAssistBot`.
2. **[Critical] CDN/WAF not blocking them.** Cloudflare: *AI Crawl Control* → check Search / Agent / Training permissions (since 2026-09-15, new ad-monetised domains block Training + Agent by default and multi-purpose crawlers can be caught by Training blocks); *Security → Bots* "Block AI bots" / "AI Labyrinth"; custom WAF rules on user agents. Same idea for Vercel Firewall, Akamai, Fastly, Sucuri, Wordfence.
3. **[Decision] Training bots** (`GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `Meta-ExternalAgent`, `CCBot`): allowing helps models "know" the brand offline; blocking has no documented effect on live citations. Ask the owner, record the decision in the brand profile.
4. **[High] No accidental `noindex`, `nosnippet`, `max-snippet:0`** on pages that should be cited (meta tag or `X-Robots-Tag` header): `noindex` removes the page; `nosnippet` / `max-snippet:0` stop it being quoted in snippets, AI Overviews and AI Mode; `data-nosnippet` hides only the marked text (check it isn't wrapped around key content).
5. **[Medium] Geo/cookie walls & interstitials** don't hide the main content from a first HTTP GET.

Recommended robots.txt block (adapt the training section to the owner's decision):

```
# AI search & user-initiated fetches — keep allowed to appear in AI answers
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: MistralAI-User
User-agent: DuckAssistBot
Allow: /
Disallow: /app/
Disallow: /account/

# Model training — business decision (allow = models know you better offline)
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
User-agent: Applebot-Extended
Allow: /
Disallow: /app/
Disallow: /account/

User-agent: *
Allow: /
Disallow: /app/
Disallow: /account/

Sitemap: https://example.com/sitemap.xml
```
Note: a bot obeys only its most specific group, so repeat `Disallow` lines for private paths in each group.

### B. Readability without JavaScript
6. **[Critical] Main content present in the server HTML** (`curl -A "GPTBot" URL | grep "a sentence from the page"`). Client-side-only React/Vue/Framer embeds, tabs/accordions filled by JS, text in images or canvas = invisible to GPTBot, ClaudeBot, PerplexityBot. Fix: SSR/SSG/pre-render; for Webflow/Framer check that CMS text is in the HTML.
7. **[High] Pricing, product specs, comparison tables, FAQs in HTML text**, not in images, PDFs only, or JS widgets. AI answers about price/features are copied from here; wrong or missing = competitors' data wins.
8. **[Medium] Semantic HTML:** one H1, logical H2/H3, real `<table>`, `<ul>`, `<a>` with descriptive anchors.
9. **[Medium] Performance:** TTFB < 600 ms, pages not timing out (AI fetchers use short timeouts).

### C. Discovery & freshness
10. **[High] Sitemap** declared in robots.txt, only canonical 200 URLs, accurate `<lastmod>` (ISO 8601) changed only on real updates.
11. **[High] Bing Webmaster Tools** verified + sitemap submitted + **IndexNow** enabled (Bing feeds Copilot and influences ChatGPT). Plugins exist for WordPress, Shopify, Cloudflare (Crawler Hints), Next.js/Vercel via API.
12. **[High] Google Search Console** verified; key pages indexed (URL Inspection).
13. **[Medium] Visible "Updated on" date + `dateModified`** on articles, docs, pricing, comparisons.

### D. Entity clarity (hygiene, not a citation lever)
14. **[Medium] Organization JSON-LD** on the homepage: `name`, `url`, `logo`, `description`, `sameAs` (LinkedIn, Crunchbase, G2/Capterra, Wikidata, GitHub, YouTube…), `foundingDate`.
15. **[Low] Article / Product / SoftwareApplication / FAQPage JSON-LD** matching visible content (never invent ratings or reviews).
16. **[Medium] Consistent facts everywhere** — name, category wording, pricing, founders, HQ — across site, LinkedIn, G2, Crunchbase, Wikidata, app stores. Contradictions = AI hallucinations about you.
17. **[Low] About / Team / Press / Contact pages** that state who you are in one sentence ("X is a [category] for [ICP]").
18. **[Info] llms.txt:** optional, no measured effect. Never sell it as a lever.

### E. Logs (if accessible)
19. Server/CDN logs: hits from `ChatGPT-User`, `Claude-User`, `Perplexity-User` = pages being fetched live to answer users. Cross with pages cited in tracking: fetched-but-not-cited pages need content work; never-fetched pages need retrieval work (SEO, links, mentions).

## Step 3 — Report format (`seo-geo/audit/technical.md`)

```
# Agent-readiness audit — [BRAND] ([DOMAIN]) — [DATE]
Score: [N]/100  ·  Critical: [n]  ·  High: [n]  ·  Medium: [n]

## Fix first (this week)
1. [Finding] — [why it matters in one line] — [exact fix / snippet / where to click]
...
## Then
...
## Decisions for the owner
- Training bots: allow / block (recommendation + trade-off)
## What we did not check (and how to)
- Real-bot behaviour behind the CDN → Cloudflare AI Crawl Control > Metrics
```
Rules: every finding has a fix the reader can execute; no generic advice; mark spoofed-UA results as such.
