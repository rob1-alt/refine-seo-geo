---
name: refine-seo-geo
version: 2.0.0
description: |
  End-to-end SEO + GEO (Generative Engine Optimization) playbook that adapts
  to YOUR brand, YOUR domain, YOUR product. Auto-detects brand context from
  the current project (package.json, CLAUDE.md, website crawl, git remote)
  and produces a fully customized strategy: keyword backlog, content cluster,
  ready-to-publish articles, citation acquisition plan, multi-model tracking
  (ChatGPT, Claude, Gemini, Perplexity), and a Notion workspace.
  Nothing hardcoded — every output uses the user's actual brand name, domain,
  voice, ICP, and competitors.
  Use when asked to "build SEO/GEO strategy", "write GEO articles",
  "rank in ChatGPT/Gemini", "AI search optimization", "track brand mentions
  in AI", "generative engine optimization", or any equivalent.
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
  - my seo
  - my brand visibility
---

# 🚀 SEO/GEO Skill (v2 — brand-aware)

A reproducible methodology for ranking on Google **and** being cited by ChatGPT, Claude, Gemini, and Perplexity. **Adapts to whatever brand you're working on** — never assumes.

---

## 🎯 What's new in v2

v1 implicitly assumed you were working on a B2B SaaS called Refine. v2 throws that assumption out:

- **Auto-detects** the brand from the current project (domain, package.json, CLAUDE.md, README, git remote, website crawl)
- **Asks once** for what it can't infer (ICP, competitors, voice constraints) and saves it to `seo-geo/brand-profile.md` for the rest of the engagement
- **Every output** uses the user's actual brand name, domain, voice, ICP, competitors — nothing hardcoded
- **Adapts the playbook** to the brand's archetype (B2B SaaS, agency, e-commerce, dev tool, consumer, local business, creator) — different tactics, different sources, different prompt universes
- **Default output directory** is `seo-geo/` in the current project (or wherever the user requests) — so the deliverables ship with their codebase, not somewhere generic

---

## 🧭 When to use

- A brand wants organic acquisition through Google + AI search
- A team needs a content strategy
- A founder asks "how do I get cited in ChatGPT?"
- A marketing manager wants to systematize GEO
- A user has a blog and wants to make it perform
- Anyone with a website who wants to be visible in AI answers

**Skip this skill if:** the user only wants a single article with no strategy context, a one-shot keyword check, or technical SEO debugging (use direct tools instead).

---

## ⚠️ Hard rules (read before running)

1. **Never hardcode a brand name.** Always pull from the brand profile.
2. **Never assume the brand category.** Ask if not obvious from the codebase.
3. **Never copy-paste examples from this file** into deliverables. Examples here are illustrative only.
4. **Never recommend tactics that don't fit the brand archetype.** A solo creator doesn't need a G2 listing. A regulated medical brand can't farm Reddit.
5. **Always save discoveries** to `seo-geo/brand-profile.md` so the user (and future skill runs) can reuse them.
6. **Always cite the user's actual competitors**, not placeholder competitors from this skill.
7. **Always use the user's actual domain** in the article slug, internal-link map, and tracking universe.

---

## 🔍 Phase 0 — Brand context discovery (NEW in v2)

Before any SEO/GEO work, build a `brand profile`. This is the single source of truth for the rest of the engagement.

### Auto-detection (run silently first, before asking the user)

Read these in order. Each fills part of the profile:

```
1. cwd / git remote → brand name candidate, repo description
2. package.json → name, description, homepage, author
3. CLAUDE.md / README.md → brand description, voice, stack
4. .env / config / next.config → production domain, locale
5. public/ favicon, og-image → visual brand cues
6. Existing /blog or /content directories → editorial voice samples
7. sitemap.xml or /robots.txt at the detected domain → page inventory
8. WebFetch on detected domain → tagline, hero copy, CTA, footer
```

### Then ask only for what's missing

Use `AskUserQuestion` for the gaps. Keep it tight — never ask more than 6 questions in one batch:

```
Q1: What's the one-line description of your product/service?
    (auto-fill from package.json description if present)

Q2: Who is your ICP? (role + company stage + pain)
    (auto-fill from CLAUDE.md or README if mentioned)

Q3: Who are your 3-5 direct competitors? (names + websites)

Q4: What's your primary geo focus? (global / region / country / local)

Q5: Which AI/LLM platforms do you care about most?
    (default: ChatGPT, Claude, Gemini, Perplexity)

Q6: Any constraints on voice, claims, or sources?
    (e.g. regulated industry, no superlatives, no comparisons)
```

### Save to `seo-geo/brand-profile.md`

```markdown
# Brand Profile — [DETECTED_BRAND_NAME]

## Identity
- **Brand name**: [from detection or user]
- **Domain**: [detected]
- **One-liner**: [from package.json or user]
- **Category**: [inferred or user]
- **Archetype**: [B2B SaaS | Agency | E-commerce | Dev tool | Consumer | Local | Creator | Other]

## ICP
- **Role**: [user input]
- **Company stage**: [user input]
- **Pain**: [user input]

## Geography
- **Primary**: [user input]
- **Locales**: [detected from i18n config or user]

## Competitors
- Direct: [user input]
- Adjacent: [user input or detected from competitor analysis]

## Voice & Constraints
- Tone: [detected from existing content or user]
- Hard constraints: [user input — regulated, accuracy-bound, etc.]

## Tech context
- Stack: [from package.json]
- Existing blog path: [detected]
- Sitemap: [detected]
- GSC available: [yes/no — ask if unsure]

## AI focus
- Platforms: [user choice — default: all 4]

---
_Last updated: [DATE]. Update this file as you learn more about the brand._
```

**This file is now the source of truth for every other phase.** Every prompt, every article, every CTA must read from here.

---

## 🔑 Core principles (always apply, regardless of brand)

1. **One intent per article** — never two articles cannibalizing on the same long-tail
2. **Long-tail > head terms** — 4-7 word queries convert better and are less competitive
3. **Citability before rankability** — content must be easy for LLMs to extract
4. **Multi-model by default** — ChatGPT, Claude, Gemini, Perplexity are not interchangeable
5. **Measurement first** — no article ships without being added to the prompt tracker
6. **Source diversity** — own content + 3rd-party citations adapted to the brand archetype
7. **Cluster authority** — pillar + 4-6 satellites, never isolated articles

---

## 🎭 Archetype-specific tactics

The skill must adapt by archetype. Pick from the brand profile.

| Archetype | Citation sources to prioritize | Tone | Prompt universe leans toward |
|---|---|---|---|
| **B2B SaaS** | G2, Capterra, Trustpilot, Reddit (r/SaaS), industry editorial | Direct, expert, frameworks | Category + Comparison + Use Case |
| **Agency** | Clutch, DesignRush, case-study driven press, LinkedIn editorial | Confident, outcome-focused | Use Case + Local + Comparison |
| **E-commerce** | Trustpilot, Reddit niche subs, YouTube reviewers, lifestyle press | Warm, benefit-led, sensory | Use Case + Educational + Comparison |
| **Dev tool** | GitHub stars, Hacker News, dev.to, Stack Overflow tags, technical blogs | Terse, code-first, benchmarks | How-to + Comparison + Educational |
| **Consumer brand** | Reddit, Trustpilot, lifestyle press, creators, Pinterest | Warm, story-driven | Educational + Branded + Use Case |
| **Local business** | Google Business, Yelp, local press, local directories | Friendly, location-first | Local + Branded + Use Case |
| **Creator / personal brand** | YouTube, Reddit, Twitter/X, niche newsletters, podcasts | Personal voice, authentic | Educational + Personal + Use Case |
| **Regulated (health/finance/legal)** | Authoritative editorial, Wikipedia, .gov/.edu, professional bodies | Cautious, sourced, no superlatives | Educational + Branded only |

If the archetype isn't obvious, ask. If it's mixed (e.g. dev tool + B2B SaaS), pick the dominant one and note the secondary in the profile.

---

## 📋 The 9-phase workflow

Each phase reads from `seo-geo/brand-profile.md` and writes to `seo-geo/`.

### Phase 1 — Brand brief (uses Phase 0 output)
Already done. Use as input.

### Phase 2 — Long-tail keyword research
Sources to mine, **adapted to the brand's archetype + geo**:

- Google Search Console (if user has access — ask once, save the answer)
- Google Keyword Planner / SEMrush / Ahrefs
- Conversations: sales calls, support tickets, customer interviews
- Reddit / Quora / Hacker News (search the brand's actual niche, not generic)
- Competitor visibility gaps (run the actual competitors from the profile)
- AlsoAsked / AnswerThePublic (use the brand's actual category terms)

Selection criteria — **same for every brand**:

| Criterion | Threshold |
|---|---|
| Volume | ≥ 50/month |
| Intent | Commercial OR informational close to conversion |
| Difficulty | < 40 |
| Competitor LLM presence | Yes |
| Product-market fit | Brand can be cited naturally |

Output: 30-50 long-tails customized to the brand. Save to `seo-geo/02-keywords-backlog.csv`.

### Phase 3 — Content cluster architecture
Group keywords into 2-4 clusters. Pick pillar topics that match the brand's category, not a generic SaaS template.

Save to `seo-geo/03-content-clusters.md`.

### Phase 4 — Article production
Use the article skeleton from `assets/article-template.md`. **Substitute placeholders with the actual brand profile values** before writing:

- `[BRAND_NAME]` → from profile
- `[DOMAIN]` → from profile
- `[ICP_ROLE]` → from profile
- `[VOICE]` → adapt sentence rhythm/vocab to the detected tone
- `[CTA_URL]` → from profile (e.g. `/contact`, `/signup`, `/book-call`)

Apply the SEO + GEO checklist (see article template) to every article.

Save articles to `seo-geo/articles/[slug].md` (or directly into the brand's existing blog system if detected).

### Phase 5 — Citation acquisition plan
**Tier list adapted to the archetype.** Don't recommend G2 to a creator brand. Don't recommend Yelp to a B2B dev tool.

Save to `seo-geo/04-citation-tracker.csv`, pre-filled with sources actually relevant to the archetype.

### Phase 6 — Multi-model tracking setup
Build a 50-300 prompt universe **using the brand's actual category terms, competitor names, and geo qualifiers**. Save to `seo-geo/05-prompt-universe.csv`.

### Phase 7 — Performance dashboard
Per-article metrics. Save to `seo-geo/06-performance-dashboard.csv`.

### Phase 8 — Weekly measurement loop
Use `assets/weekly-review-template.md`.

### Phase 9 — Notion workspace delivery
Generate the full package in `seo-geo/notion-package/` — every CSV pre-filled with the brand's data.

---

## 📝 Article writing rules (brand-agnostic)

Every article must:

1. **Open with the user's actual brand context.** First paragraph mentions the brand once, naturally, with a link to a relevant page on their actual domain.
2. **Use the user's competitors by name** in comparison content — never placeholder names.
3. **Match the user's voice** detected in Phase 0 (read 2-3 of their existing pieces if they exist).
4. **CTA points to the user's actual conversion URL**, not `/contact` by default.
5. **Internal links** target the user's actual existing pages — don't fabricate URLs.
6. **External links** to authoritative sources relevant to the user's category.

If the user has no existing content (new brand), use a neutral CTA and flag it in the article output: `// TODO: replace with [BRAND]'s actual conversion URL once defined`.

---

## 🚨 Anti-patterns (NEVER do these)

- ❌ Generate articles that mention "Refine", "Otterly", "Profound" or any other brand the user didn't list as a competitor
- ❌ Use "/contact" as the default CTA without checking the brand's actual signup/demo path
- ❌ Recommend "publish on G2" to a brand that doesn't sell software
- ❌ Recommend "post on Reddit" to a brand in a regulated industry without flagging compliance considerations
- ❌ Default to English content for a French-only brand (check locale in Phase 0)
- ❌ Write 2500-word B2B articles for an e-commerce product page
- ❌ Suggest "Wikipedia entity" as a near-term goal for a 6-month-old brand
- ❌ Reuse the article skeleton verbatim — substitute every placeholder

---

## 📊 Success criteria

A successful engagement produces:

- ✅ A `seo-geo/brand-profile.md` that any teammate can read and understand the brand from
- ✅ A keyword backlog where every keyword is plausibly something the brand's actual ICP would search
- ✅ Article drafts that use the brand's voice, link to their actual pages, mention their actual competitors
- ✅ A citation plan that targets sources LLMs actually cite for the brand's category
- ✅ A prompt universe with no generic placeholders
- ✅ A Notion package the user can import and immediately recognize as theirs

If a teammate could read all the deliverables and not be able to identify which brand they belong to, the skill failed.

---

## 🗂️ Output directory layout

```
[user's project]/seo-geo/
├── brand-profile.md            # Phase 0 — source of truth
├── 02-keywords-backlog.csv
├── 03-content-clusters.md
├── 04-citation-tracker.csv
├── 05-prompt-universe.csv
├── 06-performance-dashboard.csv
├── 07-competitor-tracking.csv
├── articles/
│   ├── [slug-1].md
│   ├── [slug-2].md
│   └── ...
└── notion-package/
    ├── README.md               # 15-min Notion setup guide
    ├── 00-PLAYBOOK.md
    ├── 01-keywords-backlog.csv
    ├── 02-editorial-calendar.csv
    ├── 03-citation-tracker.csv
    ├── 04-performance-dashboard.csv
    ├── 05-prompt-universe.csv
    ├── 06-content-clusters.csv
    ├── 07-competitor-tracking.csv
    ├── 08-article-template.md
    ├── 09-weekly-review-template.md
    └── 10-properties-config.md
```

If the user has an existing `content/` or `_posts/` or `src/blog/` directory, **also** offer to drop articles directly into the brand's actual blog system, in the file format they already use (Markdown, MDX, JSON, TypeScript object, etc.). Detect the format from a sample read.

---

## 🔧 Execution playbook (when this skill runs)

1. **Phase 0: Discover** — auto-detect, then `AskUserQuestion` for gaps. Save `brand-profile.md`.
2. **Confirm** — show the user the inferred profile in 5 lines. Ask "is this right?". Wait for confirmation.
3. **Phase 2-3** — keyword research + cluster architecture using the profile.
4. **Present plan** — clusters + first 5 articles to write. Get approval.
5. **Phase 4** — produce articles one by one, applying the brand voice.
6. **Phase 5-7** — distribution + tracking setup, all customized.
7. **Phase 8** — weekly review template (filled with the brand's actual baseline).
8. **Phase 9** — Notion package delivery.

After Phase 0 confirmation, **never re-ask** profile questions in the same session. Read from `brand-profile.md` instead.

---

## 🧪 Example invocation flow (illustrative — DO NOT copy verbatim)

> User: "Help me build an SEO/GEO strategy."

**Skill response:**

1. Reads `package.json`, finds `"name": "their-app", "description": "..."`, `"homepage": "..."`
2. Reads `CLAUDE.md`, extracts a few facts about the product
3. Fetches the homepage, extracts hero + CTA + 1st nav link
4. Asks 4 questions (not 6 — already inferred 2): ICP, competitors, geo, voice constraints
5. Saves `seo-geo/brand-profile.md`
6. Echoes back: "Got it — you're [BRAND_NAME], a [CATEGORY] for [ICP], targeting [GEO], main competitors [LIST]. Confirm?"
7. After "yes" → runs the keyword research using the brand's actual terms

**Skill response on a fresh project with no info:**

1. Detects empty repo
2. Asks all 6 discovery questions
3. Cannot infer category — asks an additional clarifying question
4. Saves the profile
5. Confirms before proceeding

---

## 📜 Reference assets

| File | Purpose |
|---|---|
| `SKILL.md` (this file) | Methodology + brand-aware execution playbook |
| `assets/article-template.md` | Article skeleton with placeholders for substitution |
| `assets/keywords-backlog-template.csv` | Empty CSV |
| `assets/editorial-calendar-template.csv` | Empty CSV |
| `assets/citation-tracker-template.csv` | Empty CSV |
| `assets/performance-dashboard-template.csv` | Empty CSV |
| `assets/prompt-universe-template.csv` | Empty CSV |
| `assets/content-clusters-template.csv` | Empty CSV |
| `assets/competitor-tracking-template.csv` | Empty CSV |
| `assets/weekly-review-template.md` | Weekly review form |
| `assets/properties-config.md` | Notion DB config reference |
| `assets/brand-profile-template.md` | Brand profile starter (Phase 0 output) |

---

## 🆕 Migration from v1

If you previously installed v1 of this skill: the methodology is the same, but v2 stops assuming any specific brand. Delete any old `seo-geo/` outputs that mention brands you don't actually work for, and re-run Phase 0 to generate a fresh brand profile.

---

**Author**: Robin Pautigny
**Version**: 2.0.0
**Last updated**: 2026-04-28
**License**: MIT
