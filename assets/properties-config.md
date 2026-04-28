# ⚙️ Notion Properties Config

> Reference for configuring Notion databases after CSV import.

---

## 🔑 Keywords Backlog

| Column | Type | Options |
|---|---|---|
| Keyword | Title | — |
| Search Volume | Number | Number |
| Difficulty | Number | 0-100 |
| Intent | Select | Informational, Commercial, Transactional, Navigational |
| Priority | Select | High, Medium, Low |
| Status | Status | Idea, To Write, In Progress, Drafting, Published, Refresh |
| Cluster | Relation | → Content Clusters |
| Target Persona | Multi-select | Custom per brand |
| Competitor Cited | Multi-select | Custom per brand |
| Notes | Text | — |
| Source | Select | GSC, Google Keyword Planner, SEMrush, Ahrefs, Reddit, Customer call |

**Recommended views**: To Write (priority), Ideas pool, Published, By Cluster, Quick wins (low difficulty + high volume).

---

## 📅 Editorial Calendar

| Column | Type | Options |
|---|---|---|
| Title | Title | — |
| Slug | Text | — |
| Target Keyword | Relation | → Keywords Backlog |
| Status | Status | Idea, To Write, Drafting, In Review, Published, Refresh |
| Author | Person | — |
| Publish Date | Date | — |
| Word Count | Number | — |
| Cluster | Relation | → Content Clusters |
| Pillar or Satellite | Select | Pillar, Satellite |
| Internal Links | Number | — |
| External Links | Number | — |
| Brand Mentions | Number | — |
| CTA | Text | — |
| Reviewer | Person | — |
| GSC Submitted | Checkbox | — |
| Tracker Updated | Checkbox | — |
| URL | URL | — |

**Recommended views**: Calendar, Kanban by Status, This Week, By Cluster, Backlog, Published Library.

**Templates**: Article Template, Weekly Review Template.

---

## 🔗 Citation Tracker

| Column | Type | Options |
|---|---|---|
| Source Domain | Title | — |
| Source Type | Select | Review Site, Directory, Community, Editorial, YouTube, Podcast, Encyclopedia, Launch |
| Tier | Select | Tier 1, Tier 2, Tier 3, Tier 4, Tier 5 |
| Status | Status | To Contact, In Progress, Active, Live, Long-term |
| Owner | Person | — |
| Outreach Date | Date | — |
| Placement Date | Date | — |
| Citation Frequency in LLMs | Select | Very High, High, Medium, Low |
| Cluster Relevance | Multi-select | Custom per brand |
| Notes | Text | — |
| Contact | Email | — |
| Cost | Select | Free, Paid |
| LLM Citing | Multi-select | ChatGPT, Claude, Gemini, Perplexity, All |

**Recommended views**: To Action, By Tier, Active, High Impact.

---

## 📊 Performance Dashboard

| Column | Type | Options |
|---|---|---|
| Article | Relation | → Editorial Calendar |
| Target Keyword | Text | — |
| Publish Date | Date | — |
| Google Position | Number | — |
| GSC Impressions | Number | — |
| GSC Clicks | Number | — |
| GSC CTR | Number | Percent |
| ChatGPT Visibility | Number | 0-100 |
| Claude Visibility | Number | 0-100 |
| Gemini Visibility | Number | 0-100 |
| Perplexity Visibility | Number | 0-100 |
| Overall AI Score | Formula | (ChatGPT + Claude + Gemini + Perplexity) / 4 |
| Share of Voice | Number | Percent |
| Sources Cited | Number | — |
| Conversions | Number | — |
| Last Measured | Date | — |
| Status | Select | Top performer, Decent, Watch, Optimize, Refresh |

**Recommended views**: Top Performers, To Optimize, Lowest CTR, By Cluster, Recent.

---

## 💬 Prompt Universe

| Column | Type | Options |
|---|---|---|
| Prompt | Title | — |
| Category | Select | Category, Comparison, Use Case, Educational, Branded |
| Buyer Stage | Select | Awareness, Consideration, Decision |
| Priority | Select | High, Medium, Low |
| Brand Cited | Select | Yes, Sometimes, No |
| Top Competitor Cited | Select | Custom per brand |
| Top Source Cited | Text | — |
| Tracked In | Multi-select | ChatGPT, Claude, Gemini, Perplexity, All |
| Last Run | Date | — |
| Notes | Text | — |

**Recommended views**: Where We Win, Where We Compete, Gaps, By Category, Competitor Watch.

---

## 🧱 Content Clusters

| Column | Type | Options |
|---|---|---|
| Cluster Name | Title | — |
| Pillar Article | Relation | → Editorial Calendar |
| Pillar Keyword | Text | — |
| Satellite Articles Count | Number | — |
| Total Articles | Rollup | Count of related articles |
| Status | Select | Active, Sub-cluster, Planning, Idea |
| Owner | Person | — |
| Target Persona | Multi-select | Custom per brand |
| Business Goal | Text | — |
| Notes | Text | — |

**Recommended views**: Active Clusters, In Planning, All Clusters.

---

## 🥊 Competitor Tracking

| Column | Type | Options |
|---|---|---|
| Competitor | Title | — |
| Website | URL | — |
| Pricing | Select | High enterprise, Mid-market, SMB, Tool |
| Position | Select | Direct, Adjacent |
| Content Output (per month) | Number | — |
| Top Cluster | Text | — |
| Their Visibility ChatGPT | Number | 0-100 |
| Their Visibility Gemini | Number | 0-100 |
| Their Visibility Perplexity | Number | 0-100 |
| Their Visibility Claude | Number | 0-100 |
| Strengths | Text | — |
| Weaknesses | Text | — |
| Last Reviewed | Date | — |
| Notes | Text | — |

**Recommended views**: Direct Competitors, Adjacent Watch, Visibility Leaderboard.

---

## 🔗 Required Relations

After importing all 7 databases, configure these relations:

| From | → To | Description |
|---|---|---|
| Keywords Backlog | Editorial Calendar | Article written for this keyword |
| Editorial Calendar | Keywords Backlog | Keyword targeted by content |
| Editorial Calendar | Content Clusters | Cluster ownership |
| Content Clusters | Editorial Calendar | All articles in cluster |
| Performance Dashboard | Editorial Calendar | Measured article |
| Citation Tracker | Editorial Calendar | Article benefiting from source (optional) |

---

## 🤖 Optional Notion Automations

(Notion Plus / Business required)

1. **Article → "Published"** → auto-create row in Performance Dashboard
2. **Status = "To Write"** → notify author on Slack
3. **Last Measured > 7 days** → add tag "To remeasure"
4. **New Keyword with Priority = High** → auto-create card in Editorial Calendar
