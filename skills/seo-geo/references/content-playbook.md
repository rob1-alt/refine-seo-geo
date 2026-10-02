# Content playbook — pages AI assistants cite

Goal: produce or refresh pages that rank (retrieval) **and** get quoted (extraction). Fewer, better, maintained pages beat volume. Every page must add something an LLM can't already write: first-hand data, product facts, real comparisons, expert judgement, examples.

## 1. Pick the right page type

| Page type | When | What makes it citable |
|---|---|---|
| **Category / "what is X" page** | Brand absent on category prompts | One-sentence definition, who it's for, how it works, criteria to choose, where the brand fits — honest |
| **Comparison: "[Brand] vs [Competitor]"** | Competitor dominates shortlist answers | Real table (price, features, limits, ideal user), when to pick the competitor, dated |
| **Alternatives: "[Competitor] alternatives for [ICP]"** | Buyers leaving a known incumbent | 4–8 genuine options incl. the brand, selection criteria, honest trade-offs |
| **"Best [category] for [use case]"** | Shortlist prompts | Transparent criteria + methodology, disclosed affiliation, competitors fairly described. ⚠️ Self-ranking lists are often cited while competitors get recommended (43% of answers, Ahrefs 2026): prioritise *third-party* lists; publish your own only with real testing data |
| **Answer page (question = title)** | Problem / how-to prompts | Answer in first 2–3 sentences, then steps, examples, pitfalls |
| **Pricing page** | "How much does X cost" / fact prompts | Prices in HTML text, plan table, what's included, currency, updated date |
| **Product / feature / integration pages** | Product pages gained share in ChatGPT retrieval in 2026 | Specs, use cases, limits, integrations, screenshots with alt text |
| **Original data / study** | Earn press, listicle and Reddit mentions | Proprietary numbers, method, downloadable chart; pitch it (see off-site) |
| **Case study** | Trust + B2B proof | Named customer, before/after numbers, timeline, quote |
| **Glossary / docs / help center** | Dev tools, complex products | Precise definitions, code, versioned |

For B2B SaaS, comparison/alternative pages + review-site presence are usually the fastest wins. For e-commerce: product pages with full specs + third-party reviews. For local: Google Business Profile + local press.

## 2. Anatomy of a citable page

1. **Title / H1** = the question or the exact category phrase buyers use.
2. **Answer-first block (40–80 words)** right under the H1: direct answer, the definition ("X is…"), who it's for. 44% of ChatGPT citations come from the top third of the page.
3. **H2s mirror the sub-questions** an assistant will fan out into (what, how, cost, vs, best for, risks, alternatives). Phrase several as questions. Source them from People Also Ask, Bing grounding queries, sales/support questions.
4. **Each section stands alone**: starts with its own one-sentence answer, names the entity instead of "it", 2–5 short paragraphs or a list/table. (Don't over-fragment: Google says no chunking needed.)
5. **Specifics**: numbers with source and date, named tools/companies, prices, steps, timeframes. Quote named experts or customers.
6. **Tables** for comparisons, pricing, specs; **lists** for steps and criteria.
7. **Evidence & honesty**: cite primary sources; say when the brand is *not* the best fit. AI engines and humans both reward balanced content.
8. **Author + updated date** visible (byline with real expertise, `dateModified`). Hygiene: no proven direct effect, but required for trust.
9. **Internal links** to the pillar and to product/pricing pages, descriptive anchors; 1–3 external links to authoritative sources.
10. **One clear CTA** matching intent (trial, demo, calculator), not five.

Length: as long as the question needs. Comprehensive pages (2,000–3,000 words) get cited more on average, but padding hurts; a pricing page can be 400 words.

## 3. Writing rules

- Brand voice from the profile; read 2–3 existing pieces before writing.
- Mention the brand 2–4 times naturally, always with its category ("[Brand], a [category] for [ICP]") — this teaches the association.
- Use the **exact category words** buyers use (from the prompt set), plus synonyms once.
- Short sentences, active voice, plain words. Define acronyms once.
- No fabricated stats, quotes, customers, reviews or awards. Placeholder `[TO VERIFY: …]` when a fact is missing — never ship with placeholders.
- Competitors: factual, current, sourced (their pricing page, docs). Date the comparison.
- Locale: write natively for the market (French for France, not translated English; € prices; local examples).

## 4. Refresh protocol (often the best ROI)

Every quarter, and immediately when a tracked prompt drops:
1. List pages targeting tracked prompts; sort by (business value × visibility gap).
2. For each: update facts, prices, screenshots, year; add the missing sub-questions; add a comparison table or data point; tighten the answer-first block.
3. Change `dateModified` and sitemap `lastmod` **only** if the content materially changed; ping IndexNow.
4. Log the change date in the editorial calendar → measure before/after (see `measurement.md`).

## 5. Pre-publish checklist

**Retrieval (SEO)**
- [ ] Target query/prompt cluster defined; no other page targets the same intent (cannibalisation check)
- [ ] Title ≤ 60 chars with the main phrase near the start; meta description 140–160 chars answering the question
- [ ] Short descriptive slug; canonical set; indexable; in sitemap with lastmod
- [ ] Content in server HTML (not JS-only); images have alt text; fast load
- [ ] 3–5 internal links in, 3–5 out; at least one link from a strong existing page

**Extraction (GEO)**
- [ ] Answer-first block under H1 with a one-sentence definition
- [ ] H2s cover the fan-out sub-questions; several phrased as questions
- [ ] Every section opens with a direct answer and names the entity
- [ ] ≥ 1 table and ≥ 1 list where the content allows
- [ ] ≥ 3 specific, sourced facts (numbers, dates, named sources)
- [ ] Brand named 2–4 times with its category; competitors named factually
- [ ] Visible author + "Updated on" date; Article JSON-LD with dateModified matching visible date

**Trust & policy**
- [ ] Adds first-hand information (data, experience, product facts) not available in an LLM's generic answer
- [ ] No invented facts, reviews or quotes; affiliations disclosed
- [ ] Not one of many near-duplicate pages (scaled content abuse risk)

**Tracking**
- [ ] Target prompts added to the tracker *before* publishing (baseline)
- [ ] Publication date logged; GSC URL inspection requested; IndexNow pinged

## 6. Output format

- Match the brand's blog system if detected (MDX, Markdown + frontmatter, JSON/TS objects, WordPress/Webflow via API or MCP). Otherwise `seo-geo/articles/[slug].md` with frontmatter: `title, slug, description, date, updated, author, target_prompts, cluster`.
- Article skeleton: `assets/article-template.md`.
- Deliver a short note per article: target prompts, sub-questions covered, sources used, facts to verify, where to publish, which off-site action amplifies it.
