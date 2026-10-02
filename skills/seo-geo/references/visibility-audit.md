# AI-visibility audit (snapshot)

Goal: answer "Do AI assistants recommend us, who do they recommend instead, which sources do they rely on, and what do we do about it?" in one sitting. Output: `seo-geo/audit/visibility.md` (+ `runs.csv`).

This is the method Refine uses for its prospect reports. It works without any paid tool.

## 1. Build the question set (10–20 prompts for a snapshot)

Write prompts the way a buyer talks to an assistant, not like keywords.

| Type | Share | Example pattern |
|---|---|---|
| Category | 35% | "What are the best [category] for [ICP/use case] in [market]?" |
| Use case | 25% | "How do I [job-to-be-done] without [pain]?" |
| Comparison | 10% | "[Competitor] vs [Competitor]: which is better for [ICP]?" |
| Alternatives | 10% | "Alternatives to [Competitor] for [constraint]" |
| Full offer | 10% | "I need one partner/tool that does A, B and C for [ICP]. Who should I use?" |
| Branded | 5–10% | "What does [Brand] cost?" · "Is [Brand] good for [use case]?" |
| Local / Educational | as relevant | "[service] in [city]" · "What is [concept]?" |

Rules (each one comes from a real failure):
- **Use the category words buyers use**, checked against the homepage of the brand and of 2 competitors. A prompt outside the brand's real category produces a false 0% and destroys credibility.
- **Localise**: language + market ("in France", "for UK SMEs") when the brand is local; run with the matching country if the tool allows.
- **Competitors must be real**: same segment, same market, still active. Verify each in one search.
- Add the **full-offer prompt**: brands often appear when the buyer describes the whole offer but vanish on the category words alone — that gap is the most actionable insight (fix = say the category words plainly on the site + comparison pages).
- Mix funnel stages; avoid prompts that contain the brand name except in the branded set.

Save to `seo-geo/05-prompt-universe.csv` (template in `assets/`).

## 2. Collect real answers — never simulate

**Your own knowledge is not a measurement.** Never write "ChatGPT says…" from memory or invent results. Use one of these, in order of preference:

1. **Refine MCP connected** → `list_prompts` / `create_prompt`, then `get_visibility`, `get_test_results`, `list_competitors`, `list_cited_reddit_threads` (see `refine-mcp.md`).
2. **Another tracker the user already has** (Peec, Otterly, Profound, Semrush, Ahrefs Brand Radar…) → ask for a CSV export of answers or mention data.
3. **APIs the user has keys for**, with web search/grounding enabled (OpenAI web search tool, Perplexity Sonar, Gemini grounding with Google Search, Anthropic web search tool). API answers differ from consumer apps: say so in the method note.
4. **A browser tool is available** → open each assistant in a fresh/temporary chat, logged out or with memory off, paste each prompt, copy the full answer and the cited links into `runs.csv`.
5. **Nothing available** → hand the user the prompt sheet + `assets/runs-template.csv` and stop at the plan; run the analysis when they return the file.

**Runs:** start with **3 runs per prompt per engine** (pooled across prompts this gives a usable overall rate); quote a percentage for a single prompt only at **5+ answers**, otherwise show counts ("2 of 3"). Engines: ChatGPT, Perplexity, Gemini, Google AI Overviews/AI Mode by default; add Claude, Copilot, Mistral Le Chat (France/EU) when relevant to the market.

## 3. Analyse

```bash
python3 scripts/visibility_stats.py seo-geo/audit/runs.csv --brand "Brand" --aliases "Brand Inc,brand.com" \
  --competitors "Comp A|Comp A Inc,Comp B,Comp C" --domain brand.com --out seo-geo/audit/visibility-stats.md
```

Then read 10 answers yourself to: catch homonyms/missed aliases, note **how** the brand is described (accurate? outdated price? wrong category?), and list the **sources** cited next to competitors.

For each prompt where the brand is absent, find *why*: open the 2–3 most-cited pages (listicles, Reddit threads, review pages, competitor pages) and note whether the brand is missing, misdescribed or outranked.

## 4. Write the report (`seo-geo/audit/visibility.md`)

Fill `assets/visibility-report-template.md`: one page a CEO reads in 3 minutes — headline counts, results by question, who gets recommended instead and from which sources, 3–5 actions with the exact page/list/thread to act on, and a method note (date, runs, engines, locale, what wasn't tested). Put the full stats output (`visibility-stats.md`) in the same folder as the appendix.

Tone: factual, no fear-mongering, credit what already works (e.g. "when ChatGPT names you, it quotes your track record").

## 5. Standard action menu (pick what the evidence supports)

| Diagnosis | Action | Reference |
|---|---|---|
| Absent on category words, present on full-offer prompt | Say the category words plainly on home + service pages; add "[Brand] vs X" and "best [category] for [ICP]" comparison pages | `content-playbook.md` |
| Competitors cited via third-party listicles | Get included in those exact lists (outreach), not a self-ranking list | `offsite-playbook.md` |
| Reddit threads cited | Answer those threads transparently; seed honest discussions | `offsite-playbook.md` |
| Brand misdescribed / wrong price | Fix the source page + align facts across profiles | `technical-audit.md` §D |
| Cited on Perplexity, absent on ChatGPT | Check Bing indexing / IndexNow, OAI-SearchBot access | `technical-audit.md` |
| Absent everywhere, new brand | Foundations first: crawlable site, clear category page, 5–6 answer pages on real buyer questions, profiles on review sites | `content-playbook.md` |
