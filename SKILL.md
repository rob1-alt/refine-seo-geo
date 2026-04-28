---
name: refine-seo-geo
version: 1.0.0
description: |
  End-to-end SEO + GEO (Generative Engine Optimization) playbook for any brand.
  Ships with a 9-phase methodology, long-tail keyword research, citable article
  structure, content cluster architecture, citation building strategy, and
  multi-model tracking (ChatGPT, Claude, Gemini, Perplexity).
  Produces: keyword backlog, editorial calendar, ready-to-publish articles,
  citation acquisition plan, weekly review template, and a complete Notion
  workspace package.
  Use when asked to "build SEO/GEO strategy", "write GEO articles",
  "rank in ChatGPT/Gemini", "AI search optimization", "generative engine
  optimization", "content strategy for AI search", "track brand mentions in AI",
  or any equivalent.
  Proactively suggest when a user has a marketing site or blog and mentions
  AI search, ChatGPT visibility, brand mentions, or organic acquisition.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - WebFetch
  - AskUserQuestion
  - TaskCreate
  - TaskUpdate
triggers:
  - seo geo
  - generative engine optimization
  - geo strategy
  - rank in chatgpt
  - rank in gemini
  - ai search optimization
  - brand mentions in ai
  - geo playbook
  - llm seo
  - geo articles
---

# 🚀 Refine SEO/GEO Skill

A reproducible methodology for ranking on Google **and** being cited by ChatGPT, Claude, Gemini, and Perplexity — adaptable to any brand in any vertical.

This skill packages every lesson from the Refine SEO/GEO playbook into a single executable workflow.

---

## 🎯 Mission of this skill

When invoked, this skill takes a brand from "we don't know what to write" to "we have a complete SEO/GEO program" — covering:

1. Brand & ICP discovery
2. Long-tail keyword research
3. Content cluster architecture
4. Article writing (SEO + GEO optimized)
5. Citation acquisition plan
6. Multi-model tracking setup
7. Weekly measurement workflow
8. Notion workspace generation
9. Continuous iteration loop

The output is **production-ready content + a measurable system**, not theory.

---

## 🧭 When to use this skill

- A brand wants organic acquisition through Google + AI search
- A team needs a content strategy (B2B SaaS, e-commerce, agency, consumer)
- A founder asks "how do I get cited in ChatGPT?"
- A marketing manager wants to systematize GEO
- A user has a blog and wants to make it perform

**Skip this skill if:** the user only wants a single article, a one-shot keyword check, or technical SEO debugging (use direct tools instead).

---

## 🔑 Core principles (always apply)

1. **One intent per article** — never two articles competing on the same long-tail.
2. **Long-tail > head terms** — 4-7 word queries convert better and are less competitive.
3. **Citability before rankability** — content must be *easy for an LLM to extract*: lists, clear headings, direct answers up top.
4. **Multi-model by default** — optimize for ChatGPT, Claude, Gemini, Perplexity simultaneously.
5. **Measurement first** — no article ships without being added to the prompt tracker.
6. **Source diversity** — own content + 3rd-party citations (directories, Reddit, YouTube, editorial).
7. **Cluster authority** — pillar + 4-6 satellites, never isolated articles.

---

## 📋 The 9-phase workflow

### Phase 1 — Brand & ICP Discovery

Before writing anything, gather:

```
- Brand name, website, one-liner
- Category & competitors (3-5 direct, 3-5 adjacent)
- ICP (Ideal Customer Profile) — role, company size, pain
- Buyer journey stages (Awareness / Consideration / Decision)
- Existing content inventory (URLs + topics)
- Current GSC data if available (top queries, impressions, position)
- Brand voice & tone constraints
- Geo/locale focus (global / FR / EU / US / etc.)
```

Use `AskUserQuestion` to fill gaps. Save findings to `seo-geo/01-brand-brief.md`.

---

### Phase 2 — Long-Tail Keyword Research

Sources to mine:

- **Google Search Console** — pages with high impressions but low clicks
- **Google Keyword Planner / SEMrush / Ahrefs** — long-tail variations
- **Conversations** — sales calls, support tickets, customer interviews
- **Reddit / Quora / Hacker News** — how real users phrase questions
- **Competitor visibility gaps** — prompts where competitors get cited and the brand doesn't
- **AlsoAsked / AnswerThePublic** — question-formatted variations

Selection criteria (each keyword must pass):

| Criterion | Threshold |
|---|---|
| Search volume | ≥ 50/month |
| Intent | Commercial OR informational close to conversion |
| Difficulty | < 40 |
| Competitor LLM presence | Yes (signal the topic is cited) |
| Product-market fit | Brand can be cited naturally |

Output: a keyword backlog of **30-50 long-tails**, sorted by priority. Save to `seo-geo/02-keywords-backlog.csv`.

---

### Phase 3 — Content Cluster Architecture

Group keywords into 2-4 clusters. Each cluster = 1 pillar + 4-6 satellites.

**Cluster anatomy:**

```
PILLAR ARTICLE (3000+ words, head-term-ish)
├── Satellite 1 (long-tail, 1500-2500 words)
├── Satellite 2 (long-tail, 1500-2500 words)
├── Satellite 3 (long-tail, 1500-2500 words)
└── Satellite 4-6
```

**Internal linking rules:**
- Every satellite links to the pillar (anchor = pillar's main keyword)
- Pillar links to all satellites in a "Related reading" section
- Lateral links between satellites when contextually relevant
- Always natural, never forced

Save cluster map to `seo-geo/03-content-clusters.md`.

---

### Phase 4 — Article Production

Every article follows the same skeleton:

```
1. Title H1            → exact keyword + benefit (≤ 70 chars)
2. Excerpt (155-160c)  → keyword + number + action verb
3. Summary box         → direct answer to the question, 4-6 lines
4. Box "Why it matters"→ stat or strong hook
5. H2: Definition      → "What is X?"
6. H2: Why X matters now
7. H2: How X works
8. H2: Practical method (3-5 steps)
9. H2: Common mistakes
10. Bottom Line box    → actionable summary
11. CTA                → action + benefit
```

**Mandatory checklist before publishing** (apply to EVERY article):

#### SEO
- [ ] Keyword in title (ideally at start)
- [ ] Keyword in slug (short, no stop-words)
- [ ] Keyword in excerpt (meta description)
- [ ] Keyword in H1 + at least 2 H2s
- [ ] Keyword in first 100 words
- [ ] Natural density 0.8–1.5%
- [ ] 1500–2500 words minimum (3000+ for pillars)
- [ ] 3-5 internal links
- [ ] 1-2 external links to authoritative sources
- [ ] Image alt-text descriptive
- [ ] Custom Open Graph image

#### GEO (LLM)
- [ ] Concept defined in first H2
- [ ] At least 3 structured bullet lists
- [ ] Comparison tables when relevant
- [ ] Direct answers "What is X? X is…"
- [ ] Mentions ChatGPT, Claude, Gemini, Perplexity in body
- [ ] Brand cited 2-4 times in natural context
- [ ] "Bottom line" closing box
- [ ] Q&A format for FAQ
- [ ] No marketing fluff
- [ ] FAQPage schema (when H2s are questions)

Save article briefs to `seo-geo/articles/[slug].md`.

---

### Phase 5 — Citation Acquisition Plan

Owned content alone won't make LLMs cite a brand. Build third-party presence in 5 tiers:

| Tier | What | Examples |
|---|---|---|
| **Tier 1** | Review sites & directories | G2, Capterra, Trustpilot, Product Hunt, Crunchbase, AlternativeTo |
| **Tier 2** | Communities | Reddit (relevant subs), Indie Hackers, Hacker News, Quora |
| **Tier 3** | Editorial | Vertical media, guest posts, HARO/Featured |
| **Tier 4** | Video & Podcast | Niche YouTube channels, industry podcasts |
| **Tier 5** | Wikipedia | Build long-term notability signals |

For each tier:
- Map 5-15 specific targets relevant to the brand's category
- Identify which LLMs cite each domain (run sample prompts)
- Assign owner, outreach date, status
- Track citation frequency over time

Save to `seo-geo/04-citation-tracker.csv`.

---

### Phase 6 — Multi-Model Tracking Setup

Build a **prompt universe** of 50–300 prompts the brand cares about, organized in 4 buckets:

1. **Category** — "best [your category] for [your ICP]"
2. **Comparison** — "[you] vs [competitor]", "[competitor] alternatives"
3. **Use case** — natural-language descriptions of buyer problems
4. **Branded** — protect against hallucinations + misrepresentation

Run each prompt across **all 4 major LLMs** (ChatGPT, Claude, Gemini, Perplexity) on a schedule (weekly minimum). Track:

- Visibility rate (mentioned / not mentioned)
- Position in answer (first sentence vs buried)
- Sentiment & accuracy
- Sources cited by the LLM
- Competitor share of voice
- Trends week-over-week

Tools: Refine, Profound, Otterly, manual spreadsheet, or a custom tracker.

Save to `seo-geo/05-prompt-universe.csv`.

---

### Phase 7 — Performance Dashboard

For every published article, track in one place:

| Metric | Source |
|---|---|
| Google position | GSC |
| Impressions / Clicks / CTR | GSC |
| ChatGPT visibility (0-100) | Tracker |
| Claude visibility (0-100) | Tracker |
| Gemini visibility (0-100) | Tracker |
| Perplexity visibility (0-100) | Tracker |
| Overall AI score (avg) | Computed |
| Share of voice | Tracker |
| Sources cited | Tracker |
| Conversions to demo/signup | GA4 / CRM |

Status options: `Top performer`, `Decent`, `Watch`, `Optimize`, `Refresh`.

Save to `seo-geo/06-performance-dashboard.csv`.

---

### Phase 8 — Weekly Measurement Loop

Run every Monday morning:

1. Pull GSC data (impressions, clicks, position deltas)
2. Pull tracker data (per-model visibility per prompt)
3. Pull GA4 (organic blog traffic, conversions)
4. Update Performance Dashboard
5. Identify top 3 wins + top 3 problems
6. Diagnose articles that aren't performing:
   - Not indexed? → submit URL manually
   - Indexed but 0 impressions? → wrong keyword
   - Impressions but 0 clicks? → rewrite title + meta
   - Clicks but no LLM citation? → missing third-party citations
   - Cited but not in Gemini? → schema or Knowledge Graph issue
7. Plan next week's articles + outreach + refreshes

Use the **Weekly Review Template** at `seo-geo/templates/weekly-review.md`.

---

### Phase 9 — Notion Workspace Delivery

The deliverable is a complete Notion package the user can self-serve:

```
notion-templates/
├── README.md                    — 15-minute setup guide
├── 00-PLAYBOOK.md               — main playbook page
├── 01-keywords-backlog.csv      — DB
├── 02-editorial-calendar.csv    — DB
├── 03-citation-tracker.csv      — DB
├── 04-performance-dashboard.csv — DB
├── 05-prompt-universe.csv       — DB
├── 06-content-clusters.csv      — DB
├── 07-competitor-tracking.csv   — DB
├── 08-article-template.md       — template
├── 09-weekly-review-template.md — template
└── 10-properties-config.md      — Notion properties + views config
```

Each CSV is pre-filled with the brand's actual data when possible.

---

## 📝 Article skeleton (paste-ready)

When generating an article for any brand, use this exact structure (markdown or TS object):

```markdown
# [Exact long-tail keyword]: [Clear benefit ≤ 70 chars]

> [Excerpt: 155-160 chars, includes keyword + number + action verb]

## Summary
[4-6 lines: direct answer to the question, mentions keyword, names the brand]

> 💡 **Why this matters**
> [Strong stat or hook that justifies reading]

## What is [X]?
[2 paragraphs defining the concept clearly. Direct answer first.]

## Why [X] matters now
[2 paragraphs on urgency. Use a bulleted list of 3-5 supporting facts.]

## How [X] works
[Mechanism explained. Sub-headings if needed (H3). Natural mentions of ChatGPT, Claude, Gemini, Perplexity.]

## The manual way / The automated way
[Two approaches. Bulleted lists. Show how the brand's product fits.]

## What to track / measure
[Bulleted list of 5-7 KPIs.]

## Common mistakes to avoid
[Bulleted list of 5 mistakes.]

> 🎯 **Bottom line**
> [3-4 lines actionable summary. Mentions keyword + brand.]

**CTA:** [Action verb + benefit] → [URL]
```

---

## 🥊 Brand voice adaptation

Adapt the playbook to the brand's voice:

| Brand archetype | Tone adjustments |
|---|---|
| **B2B SaaS** | Direct, data-driven, expert. Stats + frameworks. |
| **Agency** | Confident, outcome-focused, case-studies. Show don't tell. |
| **E-commerce** | Friendly, benefit-led, lifestyle. Lists + sensory language. |
| **Developer tool** | Technical, terse, code-led. Snippets + benchmarks. |
| **Consumer brand** | Warm, story-driven, accessible. Anecdotes + reviews. |

Always preserve: clear structure, citable formatting, first-paragraph answers.

---

## 🔧 Execution playbook (when this skill runs)

When invoked, run this loop:

1. **Discover** — `AskUserQuestion` to gather brand brief (Phase 1)
2. **Research** — keyword backlog (Phase 2). Use `WebSearch` if needed.
3. **Architect** — propose cluster map (Phase 3). Get user approval.
4. **Produce** — generate articles one by one (Phase 4). Apply checklist.
5. **Distribute** — citation acquisition plan (Phase 5).
6. **Measure** — prompt universe + dashboard (Phases 6-7).
7. **Iterate** — weekly review template (Phase 8).
8. **Deliver** — Notion workspace package (Phase 9).

After Phases 1-3, **always** present the plan to the user before producing content.

---

## 🚨 Common pitfalls to avoid

When applying this skill to any brand:

- ❌ Tracking only branded prompts — easy to win, low value. Track unbranded category & comparison prompts.
- ❌ Treating Gemini like ChatGPT — they retrieve differently. ChatGPT favors training-data depth; Gemini favors live Google + Knowledge Graph.
- ❌ Single audit and done — AI answers shift constantly. Re-run weekly minimum.
- ❌ Ignoring AI Overviews — different surface from the Gemini app, must be tracked separately.
- ❌ One-off press hits — single mentions rarely move AI. Sustained coverage does.
- ❌ Buying low-quality directory listings — always verify in tracker first.
- ❌ Not engaging on Reddit — it's the highest-cited domain in many B2B categories.
- ❌ Treating citation acquisition as a quarter project — compounding only kicks in around month 6.
- ❌ Skipping the cluster — isolated articles never build topical authority.
- ❌ Marketing fluff — every sentence should carry information. LLMs strip filler ruthlessly.

---

## 📊 Success metrics for this skill

A successful engagement produces:

- **Phase 2-3 output**: 30+ keyword backlog + 2-4 cluster maps approved by user
- **Phase 4 output**: at least 5 articles drafted to checklist standard
- **Phase 5 output**: tier-mapped citation acquisition plan
- **Phase 6 output**: 50+ prompts in tracker
- **Phase 9 output**: complete Notion workspace ZIP/folder

Within 90 days of executing the plan, brand should see:
- Top 10 Google ranking on 50%+ of priority long-tails
- Citation in at least 2 of 4 major LLMs for high-priority prompts
- Measurable increase in brand-search and direct traffic
- A repeatable weekly workflow the team can run without this skill

---

## 🗂️ Reference files in this skill

| File | Purpose |
|---|---|
| `SKILL.md` (this file) | Methodology + execution playbook |
| `assets/article-template.md` | Drop-in article skeleton |
| `assets/keywords-backlog-template.csv` | Empty CSV ready to fill |
| `assets/editorial-calendar-template.csv` | Empty CSV |
| `assets/citation-tracker-template.csv` | Empty CSV |
| `assets/performance-dashboard-template.csv` | Empty CSV |
| `assets/prompt-universe-template.csv` | Empty CSV |
| `assets/content-clusters-template.csv` | Empty CSV |
| `assets/competitor-tracking-template.csv` | Empty CSV |
| `assets/weekly-review-template.md` | Weekly review form |
| `assets/properties-config.md` | Notion DB config reference |

---

## 🧪 Example: invoking this skill

> "I run a B2B SaaS for HR teams. Help me build an SEO/GEO strategy."

The skill will:

1. Ask 6-8 discovery questions (ICP, competitors, existing content, GSC data)
2. Generate a 30-keyword backlog with priorities
3. Propose 2-3 content clusters
4. Draft the first 3-5 articles applying the full checklist
5. Build a citation acquisition tier-list customized to HR-tech
6. Set up a 50-prompt tracking universe
7. Deliver a Notion-ready workspace package

---

**Author**: Robin Pautigny (Refine)
**Version**: 1.0.0
**Last updated**: 2026-04-28
