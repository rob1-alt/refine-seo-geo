# Off-site playbook — earn the sources AI assistants trust

~84% of AI-cited links are earned media (Muck Rack 2026), and branded mentions/YouTube correlate with AI visibility far more than backlinks (Ahrefs). On-site content gets you retrieved; off-site mentions get you **recommended**.

All tactics below are transparent. Never: fake reviews, sockpuppets, undisclosed paid placements, vote manipulation, planted "inauthentic mentions" (explicitly spam under Google's 2026 policy and Reddit's rules).

## 1. Citation gap analysis (do this first)

From the visibility audit answers (or Refine `read_cited_page` / `list_cited_reddit_threads`):
1. List every URL cited on prompts where competitors appear and the brand doesn't.
2. Classify: third-party listicle · review site/directory · Reddit/forum thread · YouTube · LinkedIn article · press/news · Wikipedia/Wikidata · competitor-owned page · docs/GitHub · other.
3. For each: is the brand mentioned? misdescribed? absent? Who owns/edits it? Is it still updated (date)?
4. Score = (number of prompts × engines citing it) × (feasibility: 3 easy / 2 medium / 1 hard).
5. Save to `seo-geo/04-citation-tracker.csv`; work top-down. Re-run monthly.

## 2. Playbook by source type

### Third-party "best X" listicles & roundups (highest leverage for shortlist prompts)
- Target the exact lists the AI cites (often low-authority blogs updated recently).
- Pitch the author with what makes their list better: an honest one-paragraph description, pricing, a differentiator, a screenshot, a free account for testing. Offer to correct outdated info about competitors too.
- Track the list's update cadence; follow up when it's refreshed.
- Template:
  > Subject: Update for "[List title]" — [Brand] ([category])
  > Hi [Name], your [list] is one of the pages AI assistants quote when people ask for [category]. It's missing [Brand], a [category] for [ICP] used by [proof]. Here's a 60-word description, our pricing ([€/$]), and a free account if you want to test it. Happy to send anything else useful for your next update. — [Name, role]

### Review sites & directories (B2B: G2, Capterra, GetApp, TrustRadius, Software Advice, Gartner Peer Insights; local: Google Business Profile, Yelp, Tripadvisor; agencies: Clutch, Sortlist; consumer: Trustpilot, app stores)
- Claim and complete the profile (category, description using the category words, pricing, screenshots, integrations).
- Ask real customers for reviews after a success moment (in-app, CS emails). Never incentivise positive-only reviews; follow each platform's rules.
- Perplexity cites G2 heavily for B2B; review pages also feed comparison answers.

### Reddit (top cited domain overall; #1 for Gemini)
- Find threads already cited (tracker or `site:reddit.com [category]` searches). Answer the ones with real buyer questions.
- Use a **disclosed** account (founder/employee, flair or "I work at [Brand]"), or Reddit Pro for the brand page.
- Answer the question fully first; mention the brand only when relevant, alongside alternatives. Follow each subreddit's self-promotion rules; read them before posting.
- Start honest discussions (AMA, sharing data, asking for feedback) in relevant subreddits — not fake "what do you think of [Brand]?" posts.
- Template reply structure: direct answer → 2–3 criteria → options incl. competitors → "Disclosure: I work on [Brand]; it fits if [condition], otherwise [alternative]."

### LinkedIn (#2 cited domain; articles > posts)
- Long-form **LinkedIn articles** (not just posts) by named employees on the category's questions; 50–72% of LinkedIn citations are articles.
- Cadence beats virality: cited authors post 5+ times per 4 weeks; median cited post has 15–25 reactions.
- Repurpose each answer page into a LinkedIn article with a unique angle (data, opinion, example), linking back.

### YouTube (strongest correlate, #1 non-ranking AI Overview source)
- Short explainers and demos on the same questions as the answer pages; title = the question; full description + chapters + transcript.
- Get reviewed/mentioned by creators in the niche (send product, no script).

### Press & earned media
- Publish **original data** (a study from product data, a survey, a benchmark) — the most reliable way to earn citations from journalists and listicles. One solid study per quarter.
- Pitch trade media and newsletters in the niche; expert commentary (Qwoted, Featured, HARO-style platforms, local press for local brands).
- Press releases alone: ~1% of citations — distribute, but don't count on them.

### Wikipedia / Wikidata
- Wikipedia only if the brand meets notability with independent sources; never write your own article (conflict of interest). Wikidata entry with factual properties is fine and helps entity resolution.

### Partners, integrations, marketplaces, communities
- Integration/partner directories (Zapier, HubSpot, Shopify, Salesforce AppExchange…), GitHub/awesome-lists (dev tools), Product Hunt, Hacker News (genuine launches), Stack Overflow answers (dev), industry associations.

## 3. Archetype priorities

See `archetypes.md`. Regulated brands (health, finance, legal): authoritative editorial, professional bodies, .gov/.edu; avoid Reddit promotion; legal review for every claim.

## 4. Deliverable (`seo-geo/offsite-plan.md`)

```
# Off-site plan — [Brand] — [Month]
## Gap summary: top 10 sources cited for competitors, not for us
| Source | Type | Prompts × engines citing | Brand status | Action | Owner | Due |
## This month (5–8 actions max)
1. [Action] — [exact URL] — [draft message attached below]
## Drafts
[Pitch emails, Reddit replies, LinkedIn article outline — ready to send, personalised]
```
Measure: citation tracker status + mention rate on the prompts where those sources are cited (before/after).
