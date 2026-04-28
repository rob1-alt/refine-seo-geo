# 📝 Article Template (brand-agnostic)

> **Before using this template**: read `seo-geo/brand-profile.md`. Substitute every `[BRACKETED]` placeholder with the actual brand value. Do NOT ship an article with placeholders still in it.

---

## Required substitutions

Replace these in every article:

| Placeholder | Source |
|---|---|
| `[BRAND_NAME]` | brand-profile.md → Identity → Brand name |
| `[DOMAIN]` | brand-profile.md → Identity → Domain |
| `[ONE_LINER]` | brand-profile.md → Identity → One-liner |
| `[ICP_ROLE]` | brand-profile.md → ICP → Role |
| `[ICP_PAIN]` | brand-profile.md → ICP → Pain |
| `[CATEGORY]` | brand-profile.md → Identity → Category |
| `[COMPETITOR_1..N]` | brand-profile.md → Competitors → Direct |
| `[CTA_URL]` | brand-profile.md → Conversion paths → Primary CTA URL |
| `[CTA_TITLE]` | derived: action verb + benefit, matched to the page's intent |
| `[VOICE_NOTE]` | brand-profile.md → Voice & Constraints → Tone |
| `[LOCALE]` | brand-profile.md → Geography → Locales |

---

## Brief

- **Brand**: [BRAND_NAME]
- **Target keyword (long-tail)**: [KEYWORD]
- **Search volume**: [N/month]
- **Difficulty**: [0-100]
- **Intent**: [Informational | Commercial | Transactional]
- **Buyer stage**: [Awareness | Consideration | Decision]
- **Cluster**: [CLUSTER_NAME]
- **Pillar or Satellite**: [Pillar | Satellite]
- **Target persona**: [ICP_ROLE]
- **Direct competitors ranking on it**: [COMPETITOR_1, COMPETITOR_2, ...]
- **Voice**: [VOICE_NOTE]

---

## Title H1
[KEYWORD]: [Clear benefit ≤ 70 chars, in the brand's voice]

## Excerpt (155-160 chars, in [LOCALE])
[Phrase 1 — context for [ICP_ROLE]]. [Phrase 2 — article promise, includes keyword + verb of action].

## Summary box
[4-6 lines: direct answer to the question. Mention the keyword once. Mention [BRAND_NAME] once, naturally, with a relative link to a relevant page on [DOMAIN].]

## Why this matters (callout)
[Strong stat or hook that justifies reading. Tie it to [ICP_PAIN] when possible.]

## H2 — What is [X]?
[2 paragraphs defining the concept. Direct answer first. Use [VOICE_NOTE] sentence rhythm.]

## H2 — Why [X] matters now (for [ICP_ROLE])
[2 paragraphs urgency, contextualized for the brand's ICP. 3-5 supporting bullet list.]

## H2 — How [X] works
[Mechanism. If relevant, sub-headings (H3) for each AI platform tracked in the profile (e.g. ChatGPT, Claude, Gemini, Perplexity). If only some apply to the category, only mention those.]

## H2 — The manual way
[Steps 1-5. Lists. Honest about the tedium so the automated way feels valuable.]

## H2 — The automated way (with [BRAND_NAME])
[How [BRAND_NAME] does this. 3-5 bullet list of features that map to the steps above. Honest tradeoffs. Internal link to a real page on [DOMAIN].]

## H2 — What to track
[5-7 KPIs as a bulleted list. Tailored to the brand's category — not generic SaaS metrics if the brand isn't SaaS.]

## H2 — Common mistakes to avoid
[5 mistakes as a bulleted list. Real mistakes the [ICP_ROLE] makes — informed by sales call patterns, support tickets, customer interviews.]

## Comparison (if commercial intent)
[Optional comparison table. Columns: features. Rows: [BRAND_NAME], [COMPETITOR_1], [COMPETITOR_2]. Honest. Use real product facts.]

## Bottom Line box
[3-4 lines actionable summary. Mentions keyword + [BRAND_NAME].]

## CTA
- Title: [CTA_TITLE]
- URL: [CTA_URL]

---

## Pre-publish checklist

### Brand consistency
- [ ] Every `[BRACKET]` placeholder substituted with a real value
- [ ] Brand name spelled correctly (case, accent, punctuation) every time
- [ ] Internal links resolve to real pages on [DOMAIN]
- [ ] CTA URL is the brand's actual conversion URL (not `/contact` by default)
- [ ] Voice matches a sample of the brand's existing content
- [ ] Locale is correct ([LOCALE])
- [ ] No mention of any brand the user did NOT list as a competitor

### SEO
- [ ] Keyword in title (start)
- [ ] Keyword in slug (short, no stop-words)
- [ ] Keyword in excerpt
- [ ] Keyword in H1 + 2+ H2s
- [ ] Keyword in first 100 words
- [ ] Density 0.8-1.5%
- [ ] 1500-2500 words (3000+ for pillar)
- [ ] 3-5 internal links to actual pages on [DOMAIN]
- [ ] 1-2 external links to authoritative sources
- [ ] Image alt-text descriptive
- [ ] Custom OG image

### GEO
- [ ] Definition in 1st H2
- [ ] 3+ structured bullet lists
- [ ] Comparison tables if relevant
- [ ] "What is X? X is…" direct answers
- [ ] Mentions only the AI platforms relevant to the brand's category
- [ ] Brand cited 2-4 times naturally
- [ ] Bottom line closing
- [ ] Q&A format for FAQ
- [ ] Zero marketing fluff
- [ ] FAQPage schema if H2s are questions

---

## Final sanity check

Read your article aloud and ask:

> "If I removed the brand name and competitor names, could a teammate still tell which brand this article belongs to from the voice, the examples, and the references alone?"

If yes — ship it. If no — go back and add brand-specific texture.
