# Refine — SEO + GEO plugin for Claude

> A Claude skill that gets your brand **cited and recommended by AI assistants** — ChatGPT, Claude, Gemini, Perplexity, Copilot, Mistral Le Chat, Google AI Overviews and AI Mode — and keeps you ranking on Google. Evidence-based, updated **October 2026**, works for any brand.

Open source (MIT). Installs as a Claude Code plugin or as a skill on claude.ai.

---

## What you get in one session

Ask Claude *"Is ChatGPT recommending us? Audit getacme.com"* and you get:

- **An agent-readiness score** for your site: AI bots blocked in robots.txt or by Cloudflare's 2026 defaults, content hidden behind JavaScript, missing sitemap dates, snippet blocks — each with the exact fix.
- **An AI-visibility report** from real answers (instant with a connected tracker or API keys; otherwise Claude gives you the prompt sheet first and builds the report from the answers you collect): how often you're mentioned (with a confidence interval, not a fake "rank"), who gets recommended instead, which sources the AI relies on, and the 3–5 actions that would change it.
- **Ready-to-use deliverables**: comparison and "alternatives to X" pages, answer-first articles, refreshed pages, listicle pitches, disclosed Reddit replies, LinkedIn article outlines, a measurement setup (GA4 regex, GSC and Bing AI reports) and before/after impact reports.

## Six modes

| Ask | Mode | Output |
|---|---|---|
| "Are we visible in AI answers?" | **Quick audit** | `seo-geo/audit/` — technical score + visibility report |
| "Can AI bots crawl us? Check our Cloudflare/robots" | **Technical audit** | prioritized fixes + robots.txt block |
| "Write a page on X", "Acme vs Foo", "alternatives to Foo" | **Citable content** | publish-ready page in your blog format + publish note |
| "Where do competitors get cited?" | **Off-site plan** | citation gap table + ready-to-send pitches and replies |
| "How do we measure / prove it worked?" | **Measurement** | KPI definitions, GA4/GSC/Bing setup, impact reports |
| "Build our SEO/GEO strategy" | **Full strategy** | 90-day plan + `seo-geo/` workspace (Notion/Sheets-ready) |

## Why this skill is different

- **Evidence over folklore.** Every recommendation is tied to 2025–2026 data (Google's AI-search guidance and spam policies, Bing AI Performance, Cloudflare's bot controls, studies from Ahrefs, SE Ranking, Semrush, Muck Rack, AirOps, SparkToro…) with the bias flagged. It tells you what *doesn't* work too: llms.txt, FAQ schema as a GEO lever, "rank #1 in ChatGPT", mass AI pages, self-ranking listicles.
- **Real measurement.** AI answers change on every run, so the skill never invents results and reports mention rates and share of voice with 95% confidence intervals and before/after significance tests (`scripts/visibility_stats.py`).
- **Brand-aware.** It reads your repo and site, asks at most five questions, saves `seo-geo/brand-profile.md`, and adapts to your archetype (B2B SaaS, agency, e-commerce, dev tool, consumer, local, creator, regulated) and market (incl. France/EU and Mistral Le Chat).
- **Off-site first-class.** About 84% of AI citations come from earned media (Muck Rack 2026, vendor data). The skill finds the exact listicles, Reddit threads, review pages and LinkedIn articles AI cites for your competitors, and drafts transparent outreach.
- **Safe.** No fake reviews, sockpuppets, hidden prompts or scaled thin content: these are spam under Google's 2026 policies and get sites demoted.

## Install

### Claude Code (plugin)

```
/plugin marketplace add rob1-alt/refine-seo-geo
/plugin install refine@refine
```

Then ask: `Audit our AI visibility for example.com` — or call it directly with `/refine:seo-geo`.

### claude.ai (skill upload)

1. Download `seo-geo.zip` (skill only) from the [latest release](https://github.com/rob1-alt/refine-seo-geo/releases), or zip the `skills/seo-geo/` folder yourself (the zip must contain the `seo-geo/` folder with `SKILL.md` inside).
2. In Claude's settings, open the **Skills** section, upload the zip and enable it. Code execution needs to be on for the scripts to run.

### Manual (Claude Code, without the plugin system)

```bash
git clone https://github.com/rob1-alt/refine-seo-geo.git
cp -r refine-seo-geo/skills/seo-geo ~/.claude/skills/seo-geo
```

## Requirements

- Nothing mandatory. Scripts use only the Python 3.8+ standard library.
- For live checks, the environment needs internet access (the scripts say so clearly when a sandbox blocks it, and the skill falls back to web fetches).
- To collect AI answers, any of: a connected [Refine](https://getrefine.ai) MCP, another tracker's export, API keys with web search, a browser tool, or pasting answers manually. The skill never simulates AI answers.

## What's inside

```
refine-seo-geo/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
└── skills/seo-geo/
    ├── SKILL.md                      # modes, hard rules, workflow
    ├── references/
    │   ├── evidence-2026.md          # numbers, sources, myths, policy red lines
    │   ├── technical-audit.md        # agent-readiness checklist + robots.txt
    │   ├── visibility-audit.md       # prompt set, run protocol, report format
    │   ├── content-playbook.md       # page types, citable anatomy, refresh, checklist
    │   ├── offsite-playbook.md       # listicles, reviews, Reddit, LinkedIn, YouTube, PR
    │   ├── measurement.md            # KPIs, sample sizes, impact reports, GA4/GSC/Bing
    │   ├── archetypes.md             # tactics by brand type, market and stage
    │   ├── strategy-playbook.md      # 90-day program + workspace
    │   └── refine-mcp.md             # optional Refine integration
    ├── scripts/
    │   ├── ai_readiness_check.py     # AI-bot access & crawlability audit
    │   └── visibility_stats.py       # mention rate, SoV, citations, CIs, before/after
    └── assets/                       # brand profile, article & report templates, CSV trackers, weekly review
```

## Example prompts

```
Audit our AI visibility. We're getacme.com, a payroll tool for French SMEs.
Check whether AI crawlers can read our site and fix our robots.txt.
Write "Acme vs PayFit" for HR managers at 20–200 person companies.
Which pages and Reddit threads does Perplexity cite for our competitors? Draft the outreach.
Set up GA4 to track ChatGPT/Perplexity/Claude traffic and build our monthly AI-visibility report.
Here are our tracker exports from before and after the new pricing page — did it work?
Build a 90-day SEO + GEO plan for our Shopify skincare brand.
```

## Works even better with Refine

The skill is fully standalone. If you use [Refine](https://getrefine.ai) (daily AI-visibility tracking on ChatGPT, Gemini and Perplexity, cited sources and Reddit threads, GSC/GA4, content generation and CMS publishing), connect its MCP server and the skill will pull your real data, prioritize opportunities and publish through it.

## Changelog

See [CHANGELOG.md](CHANGELOG.md). v3.0 (October 2026) is a full rewrite: plugin format, six modes, evidence base, two scripts, statistical measurement, off-site playbook.

## Contributing

Issues and PRs welcome — especially new studies (with sources), platform changes (bots, CDN defaults, GSC/Bing features) and lessons from real brands. Please include data and dates.

## Author

**Robin Pautigny** — Co-founder, [Refine](https://getrefine.ai) · [LinkedIn](https://www.linkedin.com/in/robin-pautigny/) · [X](https://x.com/robinpautigny)

## License

MIT — see [LICENSE](LICENSE).
