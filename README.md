# 🚀 refine-seo-geo

> A **Claude Code skill** that builds an end-to-end SEO + GEO (Generative Engine Optimization) strategy **for your brand** — automatically adapted to your domain, your product, your ICP, your competitors, and your voice.

Open-source, MIT licensed, drop-in install. Made for any team that wants to rank on Google **and** be cited by ChatGPT, Claude, Gemini, and Perplexity.

> **v2 update** — the skill is now fully brand-aware. It auto-detects context from your project (package.json, CLAUDE.md, website crawl, git remote) and asks only what it can't infer. Every output uses *your* brand name, *your* domain, *your* competitors, *your* voice. Nothing is hardcoded.

---

## 🎯 What this skill does for *you*

You install it once. Then, in any project, you ask Claude something like:

```
build me an SEO/GEO strategy for my brand
```

The skill:

1. **Looks at your project** — reads `package.json`, `CLAUDE.md`, README, git remote, and crawls your live site to figure out your brand name, domain, category, voice, and existing content.
2. **Asks only what it doesn't know** — usually 4 to 6 short questions: ICP, competitors, geo focus, voice constraints.
3. **Saves a `seo-geo/brand-profile.md`** — your single source of truth. Every output the skill produces reads from here, so it always uses your real brand details.
4. **Produces a fully customized strategy**:
   - 30-50 long-tail keywords plausible for *your* ICP
   - 2-4 content clusters with pillars + satellites built around *your* category
   - Ready-to-publish article drafts using *your* voice, linking to *your* actual pages, mentioning *your* actual competitors
   - A citation acquisition plan adapted to *your* archetype (B2B SaaS, agency, e-commerce, dev tool, consumer, local, creator, regulated)
   - A 50-300 prompt tracking universe built from *your* category terms
   - A weekly measurement loop
   - A Notion workspace package, pre-filled

If a teammate read all the deliverables, they should be able to identify your brand from the voice and references alone. That's the bar.

---

## 🧠 Why GEO (and not just SEO)?

In 2026, B2B buyers and consumers don't always start with Google anymore. They ask **ChatGPT, Claude, Perplexity, or Gemini** — and only the brands those LLMs cite get considered.

Traditional SEO is necessary but **not sufficient**. You also need:

- Content that's **easy for an LLM to extract** (structured, citable, direct answers)
- A **multi-platform tracker** — each LLM retrieves differently
- A **citation acquisition plan** for the third-party sources LLMs trust (Reddit, G2, YouTube, Wikipedia, Hacker News, niche directories…)
- A **prompt universe**, not a keyword universe

This skill packages all of it into one executable workflow that adapts to your brand.

---

## 🎭 Adapts to your brand archetype

Different brands need different tactics. The skill picks the right ones:

| Your archetype | What the skill prioritizes |
|---|---|
| **B2B SaaS** | G2/Capterra, comparison content, Reddit r/SaaS, industry editorial |
| **Agency** | Clutch, case-study driven content, LinkedIn editorial |
| **E-commerce** | Trustpilot, lifestyle press, YouTube reviewers, niche subreddits |
| **Dev tool** | GitHub, Hacker News, dev.to, Stack Overflow, technical blogs |
| **Consumer brand** | Reddit, Trustpilot, creators, lifestyle press |
| **Local business** | Google Business, Yelp, local press + directories |
| **Creator** | YouTube, Reddit, niche newsletters, podcasts |
| **Regulated** (health/finance/legal) | Authoritative editorial, .gov/.edu, professional bodies — no Reddit farming |

---

## 📋 The 9 phases

| Phase | Output |
|---|---|
| **0. Brand discovery** *(NEW in v2)* | `seo-geo/brand-profile.md` — single source of truth |
| **1. Brief** | Confirmation of inferred profile |
| **2. Long-tail keyword research** | 30-50 keyword backlog, prioritized, customized to your ICP |
| **3. Content cluster architecture** | 2-4 clusters with pillar + 4-6 satellites |
| **4. Article production** | Drafts using your voice, linking to your pages, mentioning your competitors |
| **5. Citation acquisition plan** | Tier-mapped third-party sources adapted to your archetype |
| **6. Multi-model tracking setup** | 50-300 prompt universe across ChatGPT, Claude, Gemini, Perplexity |
| **7. Performance dashboard** | Per-article metrics: GSC + AI visibility per model + share of voice |
| **8. Weekly measurement loop** | A repeatable 30-min Monday review template |
| **9. Notion workspace delivery** | Complete Notion-ready package: 7 databases (CSV) + 3 templates + setup guide |

---

## 🔑 Core principles

1. **One intent per article** — never two articles cannibalizing on the same long-tail
2. **Long-tail > head terms** — 4-7 word queries convert better, less competitive
3. **Citability before rankability** — content must be easy for LLMs to extract
4. **Multi-model by default** — ChatGPT, Claude, Gemini, Perplexity are not interchangeable
5. **Measurement first** — no article ships without being added to the prompt tracker
6. **Source diversity** — own content + 3rd-party citations adapted to your archetype
7. **Cluster authority** — pillar + 4-6 satellites, never isolated articles

---

## 📦 What's inside

```
refine-seo-geo/
├── SKILL.md                                # Brand-aware methodology + execution playbook
├── README.md                               # this file
├── LICENSE                                 # MIT
└── assets/
    ├── brand-profile-template.md           # Phase 0 starter
    ├── article-template.md                 # Article skeleton with placeholder substitution
    ├── weekly-review-template.md           # Monday review form
    ├── properties-config.md                # Notion DB properties + views config
    ├── keywords-backlog-template.csv       # Empty CSV ready to fill
    ├── editorial-calendar-template.csv
    ├── citation-tracker-template.csv
    ├── performance-dashboard-template.csv
    ├── prompt-universe-template.csv
    ├── content-clusters-template.csv
    └── competitor-tracking-template.csv
```

---

## 🛠️ Installation

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- macOS, Linux, or WSL

### One-liner

```bash
git clone https://github.com/rob1-alt/refine-seo-geo.git ~/.claude/skills/refine-seo-geo
```

That's it. Open Claude Code in any project and the skill loads automatically.

### Verify

In Claude Code, type:

```
build me an SEO/GEO strategy for my brand
```

If Claude responds with a discovery flow that *already references your project's name and domain*, the skill is working.

---

## 🚀 Usage examples

### Example 1 — Full strategy from scratch

```
I run a B2B SaaS for HR teams. Help me build an SEO/GEO strategy.
```

The skill will:
1. Auto-detect what it can from your project
2. Ask 4-6 questions to fill the gaps (ICP, competitors, geo, voice)
3. Save `seo-geo/brand-profile.md` and confirm with you
4. Generate a 30-keyword long-tail backlog around *your* category
5. Propose 2-3 content clusters using *your* terminology
6. Draft the first 3-5 articles in *your* voice, mentioning *your* competitors
7. Build a citation acquisition plan adapted to HR-tech
8. Set up a 50-prompt tracking universe with *your* brand and competitors
9. Deliver a Notion-ready workspace package

### Example 2 — Single article

```
Write me a GEO-optimized article for my blog on "[long-tail keyword]"
```

Returns a 2000-word article using *your* brand voice, linking to *your* actual pages, mentioning *your* competitors when appropriate, and a CTA pointing to *your* actual conversion URL.

### Example 3 — Audit existing content

```
Audit my blog at example.com against the SEO/GEO principles
```

Crawls your blog, scores each article on the 20-point checklist, surfaces gaps and refresh opportunities specific to your content.

---

## 🥊 Origin story

This skill was built and battle-tested by the team at [Refine](https://refine.ai), an AI brand visibility tracker. We needed a reproducible methodology to grow our own visibility across AI search — then realized the methodology works for any brand, not just ours. So we open-sourced it.

If you want **automated multi-model tracking** to back the methodology — running the prompt universe across ChatGPT/Claude/Gemini/Perplexity continuously, mapping citation sources, computing share of voice — that's what Refine does. Free audit at [refine.ai](https://refine.ai). The skill itself works completely standalone without any Refine account.

---

## 🔄 Migrating from v1

If you installed v1: pull the latest. v2's methodology is the same, but:

- v1 implicitly assumed your brand was Refine (oops). v2 works for any brand.
- v1 outputs landed in `notion-templates/`. v2 outputs land in `seo-geo/` inside the current project, alongside your code.
- v2 introduces `brand-profile.md` as the source of truth.

Update with:

```bash
cd ~/.claude/skills/refine-seo-geo
git pull origin main
```

Then re-run Phase 0 in any project to generate a fresh brand profile.

---

## 🤝 Contributing

Feedback, bug reports, and PRs welcome. The skill is versioned in `SKILL.md` (look for `version: 2.0.0`).

If you use this skill on a real brand and learn something new, please open an issue with the lesson — we'll fold it into the methodology.

---

## 📜 License

MIT — see [LICENSE](LICENSE).

You can use this skill commercially, modify it, redistribute it, and incorporate it into your own products. A link back to this repo is appreciated but not required.

---

## 👤 Author

**Robin Pautigny** — Co-founder, [Refine](https://refine.ai)
- Twitter/X: [@robinpautigny](https://x.com/robinpautigny)
- LinkedIn: [robin-pautigny](https://www.linkedin.com/in/robin-pautigny/)

---

## 🗺️ Roadmap

- [x] `v1.0` — Initial release with hardcoded examples
- [x] `v2.0` — Brand-aware: auto-detect + brand profile + every output customized
- [ ] `v2.1` — Voice-fingerprinting from existing content samples (read 3 articles → match tone)
- [ ] `v2.2` — Auto-generate articles directly into the brand's blog system (MDX, MD, JSON, TS object) detected from the codebase
- [ ] `v2.3` — Sub-skill `seo-geo-audit` for one-shot brand audits
- [ ] `v3.0` — Plugin format for `claude plugins install`

---

**If this skill helps you ship better SEO/GEO faster, drop a ⭐ on the repo.**
