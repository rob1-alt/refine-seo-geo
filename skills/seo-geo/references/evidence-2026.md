# Evidence base — what actually moves AI visibility (verified 2026-10-02)

Use this file to justify recommendations and to refuse myths. Quote numbers **with their source and caveat**. Bias key: **[P]** platform (Google, Microsoft, OpenAI, Anthropic, Cloudflare) · **[A]** academic · **[V]** vendor selling GEO/SEO tools (correlational, self-interested) · **[2nd]** secondary write-up, primary not verified.

If today's date is more than ~6 months after the verification date above, run a quick web search on the items marked ⏳ before quoting them: they move fast.

---

## 1. The big picture (say this first to any client)

1. **GEO is mostly SEO + off-site reputation.** Google's own guide (May 2026, updated July 2026): optimizing for generative AI search "is still SEO"; no special files, chunking or markup needed. [P] https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
2. **Retrieval rank is the gate.** ChatGPT pages at retrieval position 1 get cited 58.4% of the time vs 14.2% at position 10 (AirOps, 50k responses, Apr 2026) [V]. 88.5% of ChatGPT citations come from the general search index (Ahrefs, 1.4M prompts, Aug 2026) [V]. You can't be cited if you're not retrieved.
3. **Off-site beats on-site.** ~84% of AI-cited links are earned media (incl. Wikipedia, Reddit, press), paid ≈0% (Muck Rack, 1M+ links, May 2026) [V]. Across 75k brands, YouTube mentions (ρ≈0.74) and branded web mentions (0.66–0.71) correlate with AI visibility far more than backlinks (≈0.2) or page count (≈0.19) (Ahrefs, Dec 2025) [V, correlation].
4. **Answers are unstable — measure rates, not ranks.** <1% chance two ChatGPT/Google AI answers list the same brands; ~1/1000 for the same order (SparkToro × Gumshoe, 2,961 runs, Jan 2026). https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/
5. **AI traffic is small but qualified.** Google still sends ~190× ChatGPT's referral traffic (Ahrefs via SEJ, Aug 2026) [V]. Conversion evidence is mixed (−13% to +31% vs organic in e-commerce; one B2B case 15.9% vs 1.76%). Sell visibility + pipeline influence, not traffic.

## 2. Content traits that get cited

| Finding | Number | Source | Bias |
|---|---|---|---|
| Citations cluster at the top of the page | 44.2% from first third, 31.1% middle, 24.7% last third (1.2M answers) | Kevin Indig / Search Engine Land, Feb 2026 https://searchengineland.com/chatgpt-citations-content-study-469483 | independent |
| Cited passages are definitional and question-led | ~2× more "X is…" language; 78.4% of question-linked citations sit under a heading; dense in named entities | same | independent |
| Heading ↔ sub-query match | 41% citation rate at strong match vs 30.2% weak | AirOps "Fan-Out Effect", Apr 2026 https://www.airops.com/report/the-fan-out-effect-what-happens-between-a-query-and-a-citation | [V] |
| Statistics, quotations, citations help | up to ~40% relative lift; keyword stuffing doesn't | Aggarwal et al., GEO, KDD 2024 https://arxiv.org/abs/2311.09735 | [A] lab benchmark, 2023-24 engines |
| Depth | <800 words → 3.2 citations avg; >2,900 → 5.1 | SE Ranking, 216k pages, Nov 2025 https://www.searchenginejournal.com/new-data-top-factors-influencing-chatgpt-citations/561954/ | [V] corr. |
| Freshness | updated <3 months → 6.0 citations vs 3.6 | same | [V] corr. |
| AI cites fresher content than organic | 25.7% fresher on average | Ahrefs, 17M citations, Jul 2025 https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content | [V] |
| ChatGPT's most-cited pages | 76.4% of dated pages updated in last 6 months; Wikipedia 29.7%, homepages 23.8% of top-1000 | Ahrefs, Oct 2025 https://ahrefs.com/blog/chatgpts-most-cited-pages | [V] |
| Google on chunking | "No need to chunk or rewrite for AI"; systems understand multi-topic pages | Google AI optimization guide [P] | — |

**Implication:** answer-first, one clear definition, question-shaped H2s that mirror sub-queries, specific entities and sourced numbers, real depth, real refreshes with a visible date. Don't fragment pages into micro-chunks.

## 3. Query fan-out

- Google AI Mode / AI Overviews issue "multiple related searches across subtopics" [P] https://developers.google.com/search/docs/appearance/ai-features
- Only **38%** of AI Overview citations rank top-10 for the original query, down from 76% (Jul 2025), attributed to wider fan-out; YouTube is #1 among non-ranking citations (Ahrefs, 4M citations, Mar 2026) [V] https://ahrefs.com/blog/ai-overview-citations-top-10
- ChatGPT: studies measure fan-out differently and disagree on levels — AirOps saw 2 sub-queries for 88.6% of searched prompts (Apr 2026) [V]; ⏳ Peec reports the share of prompts resolved with a single query falling from 94% to 43.5% after a 2026-08-06 model update [2nd]. Direction is consistent: more sub-queries, more sources per answer in 2026.
- **Guardrail [P]:** "separate content for every possible variation" = scaled content abuse. Cover sub-questions *inside* one strong page or a tight cluster.
- Free fan-out sources: Bing Webmaster Tools **grounding queries** (real), Qforia (iPullRank), "People also ask", your own sales/support questions.

## 4. Technical facts

- **Most AI crawlers don't execute JavaScript** (GPTBot, ClaudeBot, PerplexityBot); Gemini via Googlebot does (Vercel/MERJ, Dec 2024) https://vercel.com/blog/the-rise-of-the-ai-crawler. Content must be in server HTML.
- **Bot roles** (search / user-fetch / training) — see `technical-audit.md`. Anthropic: blocking Claude-SearchBot or Claude-User "may reduce visibility" in Claude search [P]. OpenAI: robots.txt "may not apply" to ChatGPT-User user-initiated fetches (SEJ, Aug 2026). Google-Extended does **not** affect AI Overviews/AI Mode (they use Googlebot).
- ⏳ **Cloudflare (from 2026-09-15):** bots classed Search / Agent / Training; new domains block Training + Agent by default on ad-monetised pages; multi-purpose crawlers (Googlebot, Bingbot, Applebot) can be caught by Training blocks; "verified bot" = identity, not access (Help Net Security, Jul 2026 https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/). A site can become invisible to AI without anyone touching robots.txt.
- **Schema/JSON-LD is not a citation lever.** Controlled test: pages adding schema saw AI Overview citations −4.6%, ChatGPT +2.2% vs controls (Ahrefs, May 2026 https://ahrefs.com/blog/schema-ai-citations/) [V]; effect vanishes once rank is controlled (SSRN 6284518); 5 AI systems ignored JSON-LD at fetch time (searchVIU, Dec 2025). Google: "Structured data isn't required for generative AI search." Keep it for rich results and entity clarity.
- **llms.txt has no measured effect.** ~300k domains, no effect (SE Ranking, SEJ); 97% of llms.txt files never requested in a month, most reads from SEO tools (Ahrefs) [V]. Google: you don't need AI text files [P]. Optional hygiene only.
- **Bing matters for ChatGPT & Copilot.** 87% of SearchGPT citations matched Bing's top results vs 56% Google (Seer, small sample, Feb 2025). OpenAI also used Google results via SerpApi (The Information via SEL, Aug 2025). Be indexed and ranking in both.
- **Sitemaps:** Bing says `lastmod` is critical for AI-era crawling; ISO 8601; change only on real updates; `changefreq`/`priority` ignored; pair with IndexNow [P] https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/

## 5. Where engines get their sources

- **Top cited domains overall:** Reddit > YouTube > LinkedIn > Wikipedia > Forbes. ChatGPT leans Wikipedia/Reddit/Forbes; Perplexity leans Reddit/LinkedIn/G2 for B2B; Google surfaces lean Facebook/Yelp for local (Peec AI, 30M sources, Mar 2026) [V] https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138
- Gemini's #1 cited domain is Reddit (Muck Rack, May 2026) [V]. Journalism ≈25% of citations; press releases ~1% (up 5× but still marginal); >50% of cited articles <12 months old.
- **Reddit:** brands with >10M Reddit mentions get ~7.0 ChatGPT citations vs 1.8 (SE Ranking) [V corr.].
- **LinkedIn:** #2 cited domain in 11% of responses (ChatGPT Search 14.3%, AI Mode 13.5%); long-form *articles* are 50–66% of LinkedIn citations; cited authors post 5+ times/4 weeks; median cited post has only 15–25 reactions (Semrush, 325k prompts, Feb 2026) [V] https://www.semrush.com/blog/linkedin-ai-visibility-study/ · Pulse articles 72% of LinkedIn citations; Perplexity cites LinkedIn most (Otterly, 1.3M citations, Jun 2026) [V].
- **"Best X" listicles:** 43.8% of citations on "best" queries were blog listicles, ~35% on low-authority domains (Ahrefs/Allsopp) [V]. **Self-promotional lists backfire:** in 43% of answers the AI cited the brand's own list but recommended competitors (Ahrefs, 9,886 answers, Aug 2026) [V]. ⏳ [2nd] After the Aug 2026 ChatGPT update, listicles fell from 15.8% → 7.8% of retrieved pages while product pages rose to 16.4% (Peec). → Get into *third-party* lists; invest in rich product, pricing and comparison pages.
- **YouTube** is the strongest single correlate of AI visibility (ρ≈0.74) and #1 among AI Overview citations that don't rank organically (Ahrefs) [V].

## 6. Measurement facts

- Sample size for a mention rate at 95% confidence: ~97 answers for ±10 pts, ~385 for ±5 pts, ~9,600 for ±1 pt (Gumshoe, Feb 2026) [V — standard binomial math]. Pool across related prompts × engines × runs.
- Share-of-voice numbers for the same brand ranged 16.8%–31.4% depending on formula (Canonry) [V]. **Always print your definition.**
- **GA4:** native "AI Assistant" channel since 2026-05-13 (ChatGPT, Gemini, DeepSeek, Copilot, Grok) — misses Perplexity, Claude, Meta AI, Mistral; not retroactive. Use the custom regex in `measurement.md`.
- **GSC:** generative-AI performance reports (Jun 2026, worldwide by end Aug 2026) show **impressions only** for AI Overviews / AI Mode — no queries, no clicks [P] https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- **Bing Webmaster Tools AI Performance** (Feb 2026): citations, cited pages and **grounding queries** for Copilot/Bing AI — the only first-party source of real AI queries [P].
- Being cited in an AI Overview lifts organic CTR from 0.94% to 2.07% (Seer, 2026); position-1 CTR drops ~58% when an AI Overview is present (Ahrefs) [V].

## 7. Policy red lines (Google spam policies, updated Aug 2026) [P]

https://developers.google.com/search/docs/essentials/spam-policies
- Spam now explicitly includes "attempting to manipulate generative AI responses" (incl. **inauthentic mentions**, planted forum posts, hidden prompts).
- **Scaled content abuse:** generating many pages with AI "without adding value", one page per query variant, stitched/scraped content, site networks. The Aug 18–21, 2026 spam update enforced it; algorithmic demotions have no reconsideration path and take months to recover.
- Structured data must match visible content.
- Reddit bans vote manipulation and undisclosed promotion; use disclosed accounts and follow each subreddit's rules.

## 8. Myths to correct politely

| Myth | Reality |
|---|---|
| "Add llms.txt to get into ChatGPT" | No measured effect. Hygiene at best. |
| "FAQ schema makes AI quote you" | No controlled evidence; FAQ rich results are restricted by Google to gov/health sites since 2023. Write real Q&A *content*. |
| "Rank #1 in ChatGPT" | There is no stable rank. Track mention rate & share of voice with confidence intervals. |
| "Publish 100 AI articles to cover every prompt" | Scaled content abuse risk + 2026 spam update. Fewer, better, refreshed pages. |
| "GEO replaces SEO" | Retrieval comes from search indexes; SEO is the entry ticket. |
| "Our own 'Top 10 tools' list (with us #1) will do it" | AI often cites it and recommends competitors (43%). Earn third-party lists. |
| "Block all AI bots to protect content, still get cited" | Blocking search/user bots removes you from live answers. Block training bots only if that's a business decision. |
