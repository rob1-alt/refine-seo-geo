# 🚀 refine-seo-geo

> An end-to-end **SEO + GEO (Generative Engine Optimization)** playbook for Claude Code, applicable to any brand.

A reproducible methodology to rank on Google **and** be cited by ChatGPT, Claude, Gemini, and Perplexity. Built and battle-tested by the team at [Refine](https://refine.ai).

---

## 🎯 What is this?

`refine-seo-geo` is a **Claude Code skill**. Once installed, when you ask Claude to:

- "build me an SEO/GEO strategy"
- "rank in ChatGPT and Gemini"
- "track my brand mentions in AI"
- "write GEO-optimized articles"
- "audit my visibility in AI search"

…Claude will load this skill and execute a complete 9-phase methodology — from brand discovery to ready-to-publish articles, citation acquisition plan, multi-model tracking setup, and a Notion-ready workspace package.

---

## 🧠 Why GEO (and not just SEO)?

In 2026, B2B buyers and consumers no longer go to Google first. They ask **ChatGPT, Claude, Perplexity, or Gemini** — and only the brands those LLMs cite get considered.

Traditional SEO tactics are necessary but **not sufficient** anymore. You also need:

- Content that's **easy for an LLM to extract** (structured, citable, direct answers)
- A **multi-platform tracker** (each LLM retrieves differently)
- A **citation acquisition plan** for third-party sources LLMs trust (Reddit, G2, YouTube, Wikipedia…)
- A **prompt universe** instead of a keyword universe

This skill packages all of it into a single executable workflow.

---

## 📋 What the skill does (the 9 phases)

| Phase | Output |
|---|---|
| **1. Brand & ICP discovery** | A complete brand brief: ICP, competitors, journey stages, current GSC data, voice constraints |
| **2. Long-tail keyword research** | A 30-50 keyword backlog, prioritized, with volume + difficulty + intent |
| **3. Content cluster architecture** | 2-4 clusters, each with 1 pillar + 4-6 satellites, internal-linking map |
| **4. Article production** | Ready-to-publish drafts following the SEO + GEO checklist (1500-2500 words each) |
| **5. Citation acquisition plan** | A tier-mapped list of third-party domains LLMs cite, with outreach roadmap |
| **6. Multi-model tracking setup** | A 50-300 prompt universe tracked across ChatGPT, Claude, Gemini, Perplexity |
| **7. Performance dashboard** | Per-article metrics: GSC + AI visibility per model + share of voice + conversions |
| **8. Weekly measurement loop** | A repeatable 30-min Monday review template |
| **9. Notion workspace delivery** | A complete Notion-ready package: 7 databases (CSV) + 3 templates (MD) + setup guide |

---

## 🔑 Core principles baked in

1. **One intent per article** — never two articles cannibalizing on the same long-tail
2. **Long-tail > head terms** — 4-7 word queries convert better and are less competitive
3. **Citability before rankability** — content must be easy for LLMs to extract
4. **Multi-model by default** — ChatGPT, Claude, Gemini, Perplexity are not interchangeable
5. **Measurement first** — no article ships without being added to the prompt tracker
6. **Source diversity** — own content + 3rd-party citations (Reddit, G2, YouTube, editorial)
7. **Cluster authority** — pillar + 4-6 satellites, never isolated articles

---

## 📦 What's inside

```
refine-seo-geo/
├── SKILL.md                            # 9-phase methodology + execution playbook (16 KB)
├── README.md                           # this file
├── LICENSE                             # MIT
└── assets/
    ├── article-template.md             # Drop-in article skeleton
    ├── weekly-review-template.md       # Weekly Monday review form
    ├── properties-config.md            # Notion DB properties + views config
    ├── keywords-backlog-template.csv   # Empty CSV ready to fill
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

That's it. Open Claude Code in any project and the skill is loaded automatically.

### Verify

In Claude Code, type:

```
/refine-seo-geo help me build a GEO strategy for my SaaS
```

If Claude responds with a discovery flow asking about your ICP, competitors, and current content, the skill is working.

---

## 🚀 Usage examples

### Example 1 — Full strategy from scratch

```
I run a B2B SaaS for HR teams. Help me build an SEO/GEO strategy.
```

The skill will:
1. Ask 6-8 discovery questions
2. Generate a 30-keyword long-tail backlog
3. Propose 2-3 content clusters
4. Draft the first 3-5 articles with the full checklist applied
5. Build a citation acquisition tier-list customized to HR-tech
6. Set up a 50-prompt tracking universe
7. Deliver a Notion-ready workspace package

### Example 2 — Single article

```
Write me a GEO-optimized article on the long-tail "how to track brand mentions in gemini"
```

Returns a 2000-word article following the SEO + GEO checklist (TOC, summary box, citable lists, comparison tables, brand mentions, bottom-line callout, CTA).

### Example 3 — Audit existing content

```
Audit my blog at example.com against the refine-seo-geo principles
```

Crawls your blog, scores each article on the 20-point checklist, surfaces gaps and refresh opportunities.

---

## 🥊 Why this skill exists

We built this at [Refine](https://refine.ai) to systematize how we grow our own brand visibility across AI search. Refine is a tool for tracking brand mentions across ChatGPT, Claude, Gemini, and Perplexity — so our team has been doing this work daily on real data.

We open-sourced the skill so any brand can apply the same playbook. If you want the **automated tracking** that backs the methodology — multi-model prompt monitoring, citation source mapping, share of voice — that's what Refine does. Start a free audit at [refine.ai](https://refine.ai).

---

## 🤝 Contributing

Feedback, bug reports, and PRs welcome. The skill is versioned in `SKILL.md` (look for `version: 1.0.0`).

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

- [ ] `v1.1` — Auto-generate the Notion workspace ZIP from a single command
- [ ] `v1.2` — Sub-skill `refine-geo-audit` for one-shot brand audits
- [ ] `v1.3` — Direct integration with the Refine API to pre-populate prompt sets
- [ ] `v2.0` — Plugin format for `claude plugins install`

---

**If this skill helps you ship better SEO/GEO faster, drop a ⭐ on the repo.**
