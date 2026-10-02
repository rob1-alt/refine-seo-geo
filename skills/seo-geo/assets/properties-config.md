# Notion / Airtable properties config

Import each CSV from `assets/` (pre-filled with the brand's data), then set these property types, views and relations. ~15 minutes.

## Prompt Universe (`prompt-universe-template.csv`)
| Column | Type | Options |
|---|---|---|
| Prompt | Title | |
| Type | Select | Category, Use case, Comparison, Alternatives, Full offer, Educational, Branded, Local |
| Language | Select | per brand |
| Market | Select | per brand |
| Buyer Stage | Select | Awareness, Consideration, Decision |
| Priority | Select | High, Medium, Low |
| Target Page | Relation | → Editorial Calendar |
| Runs · Brand Mentions | Number | |
| Mention Rate | Formula | `prop("Brand Mentions") / prop("Runs")` (format: percent). Only quote it when Runs ≥ 5 (add a view filter) |
| Top Competitor · Top Source Cited | Text | |
| Engines Tracked | Multi-select | ChatGPT, Perplexity, Gemini, Google AIO/AI Mode, Claude, Copilot, Mistral |
| Last Run | Date | |
Views: Gaps (Mention Rate < 20%, High priority) · Where we win · By type · By market.

## Keywords Backlog
Keyword or Query (Title) · Linked Prompt (Relation → Prompt Universe) · Search Volume, Difficulty (Number) · Intent (Select: Informational, Commercial, Transactional, Navigational) · Priority (Select) · Status (Status: Idea, Planned, Covered) · Cluster (Relation → Content Clusters) · Target Page (Relation → Editorial Calendar) · Target Persona, Competitors in AI Answers (Multi-select) · Source (Select: GSC, Bing grounding, Keyword tool, Sales/support, Reddit, PAA).

## Editorial Calendar
Title (Title) · Slug (Text) · Page Type (Select: Category, Comparison, Alternatives, Answer, Best-for, Pricing, Product, Case study, Data study) · Target Prompts (Relation → Prompt Universe) · Status (Status: Idea, Brief, Drafting, Review, Published, Refresh due) · Author (Person) · Publish Date, Refresh Due (Date) · Cluster (Relation) · Pillar or Satellite (Select) · Internal Links In (Number) · Facts Verified, Tracker Baseline Set, IndexNow Pinged (Checkbox) · Off-site Amplification (Text) · URL (URL).
Views: Calendar · Kanban by status · Refresh due (Refresh Due ≤ today) · By cluster.

## Performance Dashboard
Page (Relation → Editorial Calendar) · URL · Page Type · Target Prompts · Published or Refreshed (Date) · Mention Rate Before / After (Number, %) · p-value (Number) · URL Cited by AI (Checkbox) · Google Position, GSC Impressions, GSC Clicks, AI Overview Impressions, AI Referral Sessions, Conversions (Number) · Verdict (Select: Significant gain, No significant change, Decline, Too early) · Last Measured (Date).

## Citation Tracker
Source URL (Title) · Source Type (Select: Listicle, Review site, Directory, Reddit, LinkedIn, YouTube, Press, Wikipedia/Wikidata, Partner, Community, Competitor page) · Prompts Citing, Engines Citing (Number / Multi-select) · Brand Status (Select: Absent, Misdescribed, Present, Recommended) · Competitors Present (Multi-select) · Last Updated (Date) · Feasibility (Select: Easy, Medium, Hard) · Score (Number) · Action (Text) · Status (Status: To do, Contacted, In progress, Live, Declined) · Owner (Person) · Due Date (Date) · Contact (Email) · Cost (Select: Free, Paid).
Views: Top score to do · By type · Live.

## Competitor Tracking
Competitor (Title) · Website (URL) · Segment, Market, Position (Select: Direct, Adjacent) · Mention Rate, Share of Voice (Number, %) · Strongest Prompts, Sources Citing Them, Strengths, Weaknesses (Text) · Pricing (Text) · Content Output per Month (Number) · Last Reviewed (Date).

## Content Clusters
Cluster Name (Title) · Pillar Page (Relation → Editorial Calendar) · Pillar Prompt (Relation → Prompt Universe) · Satellite Pages (Relation, rollup count) · Status (Select: Active, Planning, Idea) · Owner (Person) · Target Persona (Multi-select) · Business Goal (Text) · Mention Rate (Rollup average from prompts).

## Relations to create
Prompt Universe ↔ Editorial Calendar (Target Page) · Keywords Backlog ↔ Prompt Universe · Editorial Calendar ↔ Content Clusters · Performance Dashboard → Editorial Calendar · Citation Tracker → Prompt Universe (optional).

## Optional automations
Page → Published: create a Performance Dashboard row with "Too early" · Refresh Due reached: notify owner · Citation Tracker status Live: remind to re-measure linked prompts in 14 days.
