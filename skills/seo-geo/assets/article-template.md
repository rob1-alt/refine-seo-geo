# Article template (citable page)

> Read `seo-geo/brand-profile.md` first. Replace every `[PLACEHOLDER]`. Never publish with a placeholder or an unverified `[TO VERIFY]` left in.
> Adapt the structure to the page type (comparison, alternatives, answer page, category page) — see `references/content-playbook.md`. This is a skeleton, not a script.

---

## Brief (internal, not published)

- **Brand / domain**: [BRAND_NAME] / [DOMAIN]
- **Page type**: [Category | Comparison | Alternatives | Answer | Best-for | Pricing | Case study | Data study]
- **Target prompts** (as buyers ask assistants): [PROMPT_1], [PROMPT_2]
- **Search queries that retrieve sources** (GSC / keyword tool / Bing grounding): [QUERY_1], [QUERY_2]
- **Fan-out sub-questions to cover** (PAA, grounding queries, sales/support): [Q1] · [Q2] · [Q3] · [Q4] · [Q5]
- **What AI answers today**: [brands recommended, sources cited, how [BRAND_NAME] is described or missing]
- **Our unique input** (what an LLM can't write without us): [data, product facts, customer results, expert opinion]
- **ICP / stage**: [ICP_ROLE] · [Awareness | Consideration | Decision]
- **Cluster / pillar link**: [CLUSTER] → [PILLAR_URL]
- **CTA**: [CTA_TITLE] → [CTA_URL]
- **Locale & voice**: [LOCALE] · [VOICE_NOTE]

---

## Frontmatter

```yaml
title: "[Exact question or category phrase] — [benefit/specific]"   # ≤ 60 chars ideally
slug: "[short-descriptive-slug]"
description: "[140–160 chars that answer the question directly]"
date: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
author: "[Real name], [role / expertise]"
target_prompts: ["[PROMPT_1]", "[PROMPT_2]"]
cluster: "[CLUSTER]"
```

# [H1 = the question or category phrase buyers use]

**[Answer-first block, 40–80 words.]** [Direct answer in the first sentence.] [Definition: "[X] is …".] [Who it's for / when it applies.] [Where [BRAND_NAME], a [CATEGORY] for [ICP_ROLE], fits — one natural mention with a link to the most relevant page on [DOMAIN].]

*Updated [Month YYYY] · by [Author], [role]*

## [Sub-question 1 phrased as a question?]
[Open with a one-sentence answer that names the entity. Then 2–4 short paragraphs or a list. Specific numbers with source and date.]

## [Sub-question 2 — e.g. How does [X] work?]
[Steps as a numbered list. Concrete example.]

## [Sub-question 3 — e.g. How much does [X] cost?]
| Option | Price | Included | Best for |
|---|---|---|---|
| [BRAND_NAME] [plan] | [price, currency] | [...] | [...] |
| [COMPETITOR_1] [plan] | [price — source: their pricing page, date] | [...] | [...] |

## [Sub-question 4 — e.g. [BRAND_NAME] vs [COMPETITOR_1]: which should you choose?]
[Honest criteria. When to pick the competitor. When to pick [BRAND_NAME].]

## [Sub-question 5 — e.g. Common mistakes / what to avoid]
- [Mistake 1 — from real sales/support patterns]
- [...]

## [Optional: data, case study or expert quote section]
> "[Real quote]" — [Name, role, company]  ← only if real and approved

## Key takeaways
- [3–5 bullets restating the answer with specifics; mention [BRAND_NAME] once with its category]

## FAQ (only real questions not covered above)
**[Question?]** [2–3 sentence answer.]

[CTA_TITLE] → [CTA_URL]

Sources: [linked list of sources used]

---

## Publish note (deliver with the draft)
- Target prompts added to tracker (baseline date): [ ]
- Facts to verify before publishing: [list of TO VERIFY]
- Internal links to add *to* this page from: [existing pages]
- Off-site amplification: [LinkedIn article angle / Reddit thread to answer / list to pitch]
- Measurement: before/after mention rate on target prompts from [DATE] (see `references/measurement.md`)

## Pre-publish checklist
See `references/content-playbook.md` §5 (retrieval, extraction, trust & policy, tracking). Final test: remove the brand name — could a reader still tell whose page this is from the facts, examples and voice? If not, add first-hand substance.
