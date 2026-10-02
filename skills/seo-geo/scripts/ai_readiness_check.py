#!/usr/bin/env python3
"""
AI-readiness check (agent-readiness audit) for a website. Python 3.8+, standard library only.

What it checks, without executing JavaScript (the way most AI crawlers see a page):
  1. robots.txt rules for each AI search / user / training bot
  2. HTTP access per user agent (403s, Cloudflare challenges) on the homepage and sample pages
  3. Raw-HTML content: visible words, title, meta description, H1/H2, meta robots
     (noindex / nosnippet / max-snippet), canonical, lang, JSON-LD types, dates
  4. JS-shell detection (content only rendered client-side = invisible to most AI crawlers)
  5. Sitemap: found, URL count, share of URLs with <lastmod>, most recent lastmod
  6. llms.txt presence (informational only: no measured effect on citations)

Usage:
  python3 ai_readiness_check.py https://example.com
  python3 ai_readiness_check.py example.com --pages 5 --out seo-geo/ai-readiness.md
  python3 ai_readiness_check.py example.com --json

Caveat: requests are sent from YOUR machine with a spoofed user agent. Firewalls that verify
bots by IP (Cloudflare, Akamai...) may treat spoofed requests differently from the real bot.
A block seen here is a strong signal to check; a pass is not a guarantee. Confirm in the CDN
dashboard (e.g. Cloudflare > AI Crawl Control) and in server logs.
"""
import argparse
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

TIMEOUT = 20
BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")

# (token used in robots.txt, role, full UA string for fetch test or None)
BOTS = [
    ("OAI-SearchBot", "search", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot"),
    ("ChatGPT-User", "user", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot"),
    ("GPTBot", "training", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot"),
    ("Claude-SearchBot", "search", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-SearchBot/1.0; +https://www.anthropic.com"),
    ("Claude-User", "user", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com"),
    ("ClaudeBot", "training", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ClaudeBot/1.0; +claudebot@anthropic.com"),
    ("PerplexityBot", "search", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot"),
    ("Perplexity-User", "user", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"),
    ("Googlebot", "search (AI Overviews / AI Mode)", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    ("Google-Extended", "training/grounding token (Gemini)", None),
    ("Bingbot", "search (Bing, Copilot, feeds ChatGPT)", "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"),
    ("Applebot", "search (Siri / Spotlight)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)"),
    ("Applebot-Extended", "training token (Apple Intelligence)", None),
    ("DuckAssistBot", "user (DuckDuckGo AI answers)", None),
    ("MistralAI-User", "user (Le Chat)", "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots"),
    ("Meta-ExternalAgent", "training", None),
    ("CCBot", "training (Common Crawl)", None),
]
FETCH_TEST_BOTS = ["OAI-SearchBot", "ChatGPT-User", "Claude-User", "PerplexityBot", "Bingbot", "Googlebot"]


# --------------------------------------------------------------------------- http
def fetch(url, ua=BROWSER_UA, max_bytes=3_000_000):
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en,fr;q=0.8",
        "Accept-Encoding": "gzip",
    })
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            raw = r.read(max_bytes)
            if r.headers.get("Content-Encoding") == "gzip" or raw[:2] == b"\x1f\x8b":
                try:
                    raw = gzip.decompress(raw)
                except OSError:
                    pass
            return {"status": r.status, "url": r.geturl(), "headers": dict(r.headers),
                    "body": raw.decode(r.headers.get_content_charset() or "utf-8", "replace"),
                    "ms": int((time.time() - t0) * 1000), "error": None}
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read(200_000).decode("utf-8", "replace")
        except Exception:
            pass
        return {"status": e.code, "url": url, "headers": dict(e.headers or {}), "body": body,
                "ms": int((time.time() - t0) * 1000), "error": None}
    except Exception as e:  # DNS, TLS, timeout
        return {"status": None, "url": url, "headers": {}, "body": "", "ms": int((time.time() - t0) * 1000),
                "error": f"{type(e).__name__}: {e}"}


def is_challenge(resp):
    h = {k.lower(): v for k, v in resp["headers"].items()}
    body = resp["body"][:20000].lower()
    if h.get("cf-mitigated") == "challenge":
        return True
    markers = ["just a moment...", "cf-chl-", "challenge-platform", "attention required! | cloudflare",
               "verify you are human", "_incapsula_resource", "px-captcha", "ddos protection by"]
    return resp["status"] in (403, 429, 503) and any(m in body for m in markers) or "cf-chl-" in body


# --------------------------------------------------------------------------- robots
def parse_robots(text):
    """Return list of groups: {'agents': [...], 'rules': [(allow:bool, path)]}, plus sitemaps."""
    groups, sitemaps, cur, last_was_agent = [], [], None, False
    text = text.lstrip("\ufeff")
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        k, v = [x.strip() for x in line.split(":", 1)]
        k = k.lower()
        if k == "sitemap":
            sitemaps.append(v)
            continue
        if k == "user-agent":
            if cur is None or not last_was_agent:
                cur = {"agents": [], "rules": []}
                groups.append(cur)
            cur["agents"].append(v.lower())
            last_was_agent = True
        elif k in ("allow", "disallow") and cur is not None:
            if v or k == "allow":
                cur["rules"].append((k == "allow", v))
            last_was_agent = False
        # other directives (crawl-delay, host...) don't end a run of user-agent lines
    return groups, sitemaps


def _pattern_to_regex(p):
    anchored = p.endswith("$")
    p = p[:-1] if anchored else p
    rx = "".join(".*" if c == "*" else re.escape(c) for c in p)
    return re.compile("^" + rx + ("$" if anchored else ""))


def robots_allowed(groups, agent, path="/"):
    """Google-style: most specific UA group wins; longest matching rule wins; allow wins ties."""
    a = agent.lower()
    matched = [g for g in groups if any(x != "*" and x in a for x in g["agents"])]
    if matched:
        best_len = max(max(len(x) for x in g["agents"] if x != "*" and x in a) for g in matched)
        matched = [g for g in matched if any(len(x) == best_len and x in a for x in g["agents"])]
    else:
        matched = [g for g in groups if "*" in g["agents"]]
    if not matched:
        return True, "no group applies"
    rules = [r for g in matched for r in g["rules"]]
    best = None
    for allow, pat in rules:
        if pat == "":
            continue
        if _pattern_to_regex(pat).match(path):
            score = (len(pat), allow)
            if best is None or score > best[0]:
                best = (score, allow, pat)
    if best is None:
        return True, "no rule matches"
    return best[1], f"{'Allow' if best[1] else 'Disallow'}: {best[2]}"


# --------------------------------------------------------------------------- html
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.text = []
        self.title = ""
        self._in_title = False
        self.metas = []
        self.links = []
        self.h = {"h1": [], "h2": [], "h3": []}
        self._hcur = None
        self.jsonld = []
        self._in_jsonld = False
        self._jsonbuf = []
        self.scripts = 0
        self.lang = None
        self.a_hrefs = []
        self.tables = 0
        self.lists = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag in ("script", "style", "noscript", "template", "svg"):
            if tag == "script":
                self.scripts += 1
                if (a.get("type") or "").lower() == "application/ld+json":
                    self._in_jsonld = True
                    self._jsonbuf = []
            self.skip += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            self.metas.append(a)
        if tag == "link":
            self.links.append(a)
        if tag in self.h:
            self._hcur = [tag, []]
        if tag == "a" and a.get("href"):
            self.a_hrefs.append(a["href"])
        if tag == "table":
            self.tables += 1
        if tag in ("ul", "ol"):
            self.lists += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "template", "svg"):
            if tag == "script" and self._in_jsonld:
                self.jsonld.append("".join(self._jsonbuf))
                self._in_jsonld = False
            self.skip = max(0, self.skip - 1)
        if tag == "title":
            self._in_title = False
        if self._hcur and tag == self._hcur[0]:
            self.h[tag].append(" ".join("".join(self._hcur[1]).split()))
            self._hcur = None

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonbuf.append(data)
            return
        if self._in_title:
            self.title += data
        if self.skip:
            return
        self.text.append(data)
        if self._hcur:
            self._hcur[1].append(data)


def jsonld_types(blocks):
    types, dates = set(), {}

    def walk(o):
        if isinstance(o, dict):
            t = o.get("@type")
            if isinstance(t, list):
                types.update(map(str, t))
            elif t:
                types.add(str(t))
            for k in ("dateModified", "datePublished"):
                if k in o and k not in dates:
                    dates[k] = o[k]
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    bad = 0
    for b in blocks:
        try:
            walk(json.loads(b))
        except Exception:
            bad += 1
    return sorted(types), dates, bad


def analyse_html(html, x_robots=""):
    p = PageParser()
    try:
        p.feed(html)
    except Exception:
        pass
    text = " ".join(" ".join(p.text).split())
    words = len(text.split())
    meta = {}
    for m in p.metas:
        key = (m.get("name") or m.get("property") or "").lower()
        if key:
            meta[key] = m.get("content", "")
    robots_meta = " ".join(filter(None, [meta.get("robots", ""), meta.get("googlebot", ""), x_robots or ""])).lower()
    canonical = next((l.get("href") for l in p.links if "canonical" in (l.get("rel") or "").lower()), None)
    types, dates, bad_jsonld = jsonld_types(p.jsonld)
    if "article:modified_time" in meta:
        dates.setdefault("article:modified_time", meta["article:modified_time"])
    shell_markers = re.search(r'<div[^>]+id="(root|app|__next|__nuxt|svelte)"[^>]*>\s*</div>', html, re.I)
    js_shell = words < 120 and (p.scripts >= 3 or bool(shell_markers))
    return {
        "words": words, "title": " ".join(p.title.split()), "meta_description": meta.get("description", ""),
        "h1": p.h["h1"], "h2": p.h["h2"][:20], "h2_count": len(p.h["h2"]), "h3_count": len(p.h["h3"]),
        "question_h2": sum(1 for x in p.h["h2"] if x.strip().endswith("?")),
        "robots_meta": robots_meta, "canonical": canonical, "lang": p.lang,
        "jsonld_types": types, "jsonld_invalid_blocks": bad_jsonld, "dates": dates,
        "scripts": p.scripts, "js_shell": js_shell, "tables": p.tables, "lists": p.lists,
        "text_sample": text[:300],
    }


# --------------------------------------------------------------------------- sitemap
def read_sitemap(url, depth=0, budget=None):
    budget = budget if budget is not None else {"files": 0}
    out = {"urls": [], "lastmods": [], "error": None}
    if budget["files"] >= 6:
        return out
    budget["files"] += 1
    r = fetch(url, max_bytes=60_000_000)
    if r["status"] != 200 or not r["body"].strip():
        out["error"] = f"HTTP {r['status']} {r['error'] or ''}".strip()
        return out
    body = r["body"]
    try:
        root = ET.fromstring(body.encode("utf-8"))
    except ET.ParseError as e:
        out["error"] = f"XML parse error: {e}"
        return out
    ns = re.match(r"\{.*\}", root.tag)
    ns = ns.group(0) if ns else ""
    if root.tag.endswith("sitemapindex"):
        for sm in root.findall(f"{ns}sitemap")[:5]:
            loc = sm.findtext(f"{ns}loc")
            if loc and depth < 1:
                sub = read_sitemap(loc.strip(), depth + 1, budget)
                out["urls"] += sub["urls"]
                out["lastmods"] += sub["lastmods"]
    else:
        for u in root.findall(f"{ns}url"):
            loc = u.findtext(f"{ns}loc")
            if loc:
                out["urls"].append(loc.strip())
                lm = u.findtext(f"{ns}lastmod")
                out["lastmods"].append(lm.strip() if lm else None)
    return out


# --------------------------------------------------------------------------- main
def normalise(url):
    if not re.match(r"^https?://", url):
        url = "https://" + url
    p = urllib.parse.urlparse(url)
    return f"{p.scheme}://{p.netloc}", url


def host_key(u):
    h = urllib.parse.urlparse(u).netloc.lower()
    return h[4:] if h.startswith("www.") else h


def pick_sample(urls, base, n):
    """Prefer blog/article/compare/pricing pages, then anything else (same host, www-insensitive)."""
    pri = re.compile(r"/(blog|articles?|guides?|resources|learn|compare|vs|alternatives?|pricing|product|features?)/", re.I)
    same = [u for u in urls if host_key(u) == host_key(base)]
    first = [u for u in same if pri.search(u)]
    rest = [u for u in same if u not in first]
    seen, out = set(), []
    for u in first + rest:
        if u.rstrip("/") not in seen and urllib.parse.urlparse(u).path.strip("/") != "":
            seen.add(u.rstrip("/"))
            out.append(u)
        if len(out) >= n:
            break
    return out


def run(target, pages):
    base, start = normalise(target)
    report = {"base": base, "checked_at": time.strftime("%Y-%m-%d %H:%M"), "findings": []}

    def finding(level, area, msg, fix=""):
        report["findings"].append({"level": level, "area": area, "msg": msg, "fix": fix})

    # reachability first: a network error here means OUR environment can't reach the site
    probe = fetch(start)
    if probe["status"] is None:
        sys.exit(f"Cannot reach {start} from this environment ({probe['error']}).\n"
                 "This is a network/sandbox limit, not a site finding. Run the script on a machine with open "
                 "internet access, or fall back to the manual checklist in references/technical-audit.md.")
    if probe["url"] and probe["url"] != start:  # follow redirects (http->https, apex->www)
        base, _ = normalise(probe["url"])
        start = probe["url"]
        report["base"] = base

    # robots
    rb = fetch(base + "/robots.txt")
    groups, sitemaps = ([], [])
    report["robots_status"] = rb["status"]
    if rb["status"] == 200 and "<html" not in rb["body"][:500].lower():
        groups, sitemaps = parse_robots(rb["body"])
    elif rb["status"] is not None and rb["status"] >= 500:
        finding("FAIL", "robots.txt", f"robots.txt returns HTTP {rb['status']}: Google treats a 5xx robots.txt as 'disallow all' and other crawlers may back off.",
                "Make /robots.txt return 200 (plain text) or 404.")
    elif rb["status"] in (404, 410):
        finding("INFO", "robots.txt", "No robots.txt (404): everything is allowed. Add one to declare the sitemap and AI-bot rules explicitly.")
    else:
        finding("WARN", "robots.txt", f"robots.txt not served cleanly (HTTP {rb['status']}, or HTML instead of text).",
                "Serve a plain-text /robots.txt with explicit rules for AI bots and a Sitemap line.")
    rob = []
    for token, role, _ in BOTS:
        ok, why = robots_allowed(groups, token, "/")
        rob.append({"bot": token, "role": role, "allowed": ok, "rule": why})
        if not ok and ("search" in role or "user" in role):
            finding("FAIL", "robots.txt", f"{token} ({role}) is disallowed on '/' ({why}).",
                    f"Allow {token}: it governs live answers/citations, not training.")
    report["robots"] = rob
    blocked_training = [r["bot"] for r in rob if not r["allowed"] and "training" in r["role"]]
    if blocked_training:
        finding("INFO", "robots.txt", "Training bots blocked: " + ", ".join(blocked_training) +
                ". Business choice; no documented effect on live citations, may reduce what models know offline.")

    # homepage with browser UA
    home = fetch(start)
    report["home_status"] = home["status"]
    if home["status"] != 200:
        finding("FAIL", "access", f"Homepage returned HTTP {home['status']} {home['error'] or ''} to a browser UA.")
    home_a = analyse_html(home["body"], home["headers"].get("X-Robots-Tag", "")) if home["body"] else None
    report["home"] = home_a

    # per-UA access
    access = []
    for token, role, ua in BOTS:
        if token not in FETCH_TEST_BOTS or not ua:
            continue
        r = fetch(start, ua)
        ch = is_challenge(r)
        words = analyse_html(r["body"])["words"] if r["body"] else 0
        access.append({"bot": token, "status": r["status"], "challenge": ch, "words": words, "ms": r["ms"], "error": r["error"]})
        if r["status"] in (401, 403, 429, 503) or ch or r["status"] is None:
            finding("FAIL", "access", f"{token} got HTTP {r['status']}{' + bot challenge' if ch else ''} on the homepage (spoofed UA test).",
                    "Check CDN/WAF bot rules (Cloudflare AI Crawl Control: Search/Agent/Training permissions; managed rules; 'Block AI bots'). Allow search & user agents.")
        elif home_a and home_a["words"] > 200 and words < home_a["words"] * 0.5:
            finding("WARN", "access", f"{token} receives much less text ({words} words) than a browser ({home_a['words']}).",
                    "Possible bot-specific rendering or cloaking; serve the same content to bots and users.")
    report["access"] = access

    # sitemap
    sm_urls = sitemaps or [base + "/sitemap.xml"]
    sm = {"urls": [], "lastmods": [], "error": None}
    for u in sm_urls[:3]:
        s = read_sitemap(u)
        sm["urls"] += s["urls"]
        sm["lastmods"] += s["lastmods"]
        sm["error"] = sm["error"] or s["error"]
    with_lm = [x for x in sm["lastmods"] if x]
    report["sitemap"] = {"declared_in_robots": bool(sitemaps), "url_count": len(sm["urls"]),
                         "lastmod_share": round(len(with_lm) / len(sm["lastmods"]), 2) if sm["lastmods"] else 0,
                         "latest_lastmod": max(with_lm) if with_lm else None, "error": sm["error"] if not sm["urls"] else None}
    if not sm["urls"]:
        finding("FAIL", "sitemap", f"No sitemap URLs found ({sm['error']}).", "Publish /sitemap.xml and reference it in robots.txt.")
    else:
        if not sitemaps:
            finding("WARN", "sitemap", "Sitemap not declared in robots.txt.", "Add 'Sitemap: <url>' to robots.txt.")
        if report["sitemap"]["lastmod_share"] < 0.8:
            finding("WARN", "sitemap", f"Only {int(report['sitemap']['lastmod_share']*100)}% of sitemap URLs have <lastmod>.",
                    "Add accurate <lastmod> (ISO 8601) and change it only when content really changes; pair with IndexNow.")

    # pages
    sample = pick_sample(sm["urls"], base, pages)
    page_results = []
    for u in sample:
        r = fetch(u)
        a = analyse_html(r["body"], r["headers"].get("X-Robots-Tag", "")) if r["body"] else None
        page_results.append({"url": u, "status": r["status"], **(a or {})})
    report["pages"] = page_results
    if sm["urls"] and not sample:
        finding("WARN", "sitemap", "No sitemap URL on this host could be sampled (sitemap lists another host, or only the homepage).",
                "Make sitemap URLs use the canonical host (same scheme and www/non-www as the site).")
    # robots rules on the sampled paths (not only '/')
    blocked_root = {r["bot"] for r in rob if not r["allowed"]}
    for u in sample:
        path = urllib.parse.urlparse(u).path or "/"
        hits = {}
        for token, role, _ in BOTS:
            if ("search" in role or "user" in role) and token not in blocked_root:
                ok, why = robots_allowed(groups, token, path)
                if not ok:
                    hits.setdefault(why, []).append(token)
        for why, toks in hits.items():
            finding("FAIL", "robots.txt", f"{path} is disallowed for {', '.join(toks)} ({why}).",
                    "Allow AI search & user bots on content you want cited.")

    for pr in ([{"url": start, "status": home["status"], "is_home": True, **home_a}] if home_a else []) + page_results:
        u = pr["url"]
        if pr.get("status") != 200:
            finding("WARN", "page", f"{u} returned HTTP {pr.get('status')}.")
            continue
        rm = pr.get("robots_meta", "")
        if "noindex" in rm:
            if pr.get("is_home"):
                finding("FAIL", "indexing", f"{u}: homepage is noindex (meta robots or X-Robots-Tag).", "Remove noindex from the homepage.")
            else:
                finding("WARN", "indexing", f"{u}: noindex (meta robots or X-Robots-Tag) but listed in the sitemap.",
                        "If the page is private (app, account), remove it from the sitemap; if it should rank and be cited, remove noindex.")
            continue
        if pr.get("js_shell"):
            finding("FAIL", "rendering", f"{u}: only {pr['words']} words in raw HTML ({pr['scripts']} scripts) — content looks client-side rendered.",
                    "Server-render or pre-render (SSR/SSG) the main content: GPTBot, ClaudeBot, PerplexityBot do not execute JavaScript.")
        if "nosnippet" in rm or re.search(r"max-snippet:\s*0", rm):
            finding("FAIL", "snippets", f"{u}: nosnippet / max-snippet:0 prevents use in AI Overviews/AI Mode and snippets.")
        if not pr.get("title"):
            finding("WARN", "on-page", f"{u}: missing <title>.")
        if not pr.get("meta_description"):
            finding("WARN", "on-page", f"{u}: missing meta description.")
        if len(pr.get("h1") or []) != 1:
            finding("WARN", "on-page", f"{u}: {len(pr.get('h1') or [])} H1 tags (expected 1).")
        if pr.get("jsonld_invalid_blocks"):
            finding("WARN", "schema", f"{u}: {pr['jsonld_invalid_blocks']} JSON-LD block(s) do not parse.")
    org_types = {"Organization", "Corporation", "LocalBusiness", "WebSite", "OnlineStore", "OnlineBusiness",
                 "ProfessionalService", "Store", "NGO", "EducationalOrganization", "MedicalOrganization", "SoftwareApplication"}
    home_types = {t.rstrip("/").split("/")[-1] for t in (home_a or {}).get("jsonld_types", [])}
    if home_a and not (org_types & home_types):
        finding("WARN", "schema", "Homepage has no Organization/WebSite JSON-LD.",
                "Add Organization (name, url, logo, sameAs to LinkedIn/Crunchbase/G2/Wikidata...) for entity clarity. Hygiene, not a citation lever.")
    content_pages = [p for p in page_results if p.get("status") == 200 and p.get("words", 0) > 300]
    if content_pages and not any(p.get("dates") for p in content_pages):
        finding("WARN", "freshness", "No machine-readable dates (dateModified / article:modified_time) on sampled content pages.",
                "Expose datePublished/dateModified in JSON-LD and show a visible 'Updated on' date; refresh key pages at least quarterly.")

    llms = fetch(base + "/llms.txt")
    report["llms_txt"] = llms["status"] == 200 and "<html" not in llms["body"][:300].lower()

    # score: start 100; each distinct (level, area) costs FAIL -15 / WARN -5, so one
    # systemic issue repeated on many pages is not counted many times (floor 0)
    score = 100
    for lvl, area in {(f["level"], f["area"]) for f in report["findings"]}:
        score -= 15 if lvl == "FAIL" else 5 if lvl == "WARN" else 0
    report["score"] = max(0, score)
    return report


def to_markdown(r):
    L = [f"# AI-readiness check — {r['base']}", "", f"_Checked {r['checked_at']} · score {r['score']}/100 (−15 per failing area, −5 per warning area)_", ""]
    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    L += ["## Findings (most severe first)", ""]
    if not r["findings"]:
        L.append("No issues detected.")
    for f in sorted(r["findings"], key=lambda x: order[x["level"]]):
        L.append(f"- **{f['level']}** · {f['area']} — {f['msg']}" + (f"  \n  → {f['fix']}" if f["fix"] else ""))
    L += ["", "## robots.txt by bot", "", "| Bot | Role | Allowed on / | Rule |", "|---|---|---|---|"]
    for b in r["robots"]:
        L.append(f"| {b['bot']} | {b['role']} | {'yes' if b['allowed'] else '**no**'} | {b['rule']} |")
    L += ["", "## Access test (homepage, spoofed user agents)", "", "| Bot | HTTP | Challenge | Words served | ms |", "|---|---|---|---|---|"]
    for a in r["access"]:
        L.append(f"| {a['bot']} | {a['status'] or a['error']} | {'yes' if a['challenge'] else 'no'} | {a['words']} | {a['ms']} |")
    h = r.get("home") or {}
    L += ["", "## Homepage as a non-JS crawler sees it", "",
          f"- Words in raw HTML: {h.get('words')} · scripts: {h.get('scripts')} · JS-shell suspected: {h.get('js_shell')}",
          f"- Title: {h.get('title')!r}", f"- Meta description: {h.get('meta_description')!r}",
          f"- H1: {h.get('h1')}", f"- H2 ({h.get('h2_count')}): {h.get('h2')}",
          f"- lang: {h.get('lang')} · canonical: {h.get('canonical')} · meta robots: {h.get('robots_meta') or '—'}",
          f"- JSON-LD types: {', '.join(h.get('jsonld_types') or []) or 'none'}"]
    s = r["sitemap"]
    L += ["", "## Sitemap", "", f"- Declared in robots.txt: {s['declared_in_robots']} · URLs read: {s['url_count']} · with lastmod: {int(s['lastmod_share']*100)}% · latest lastmod: {s['latest_lastmod']}"]
    if r["pages"]:
        L += ["", "## Sampled pages", "", "| URL | HTTP | Words | H2 (questions) | Tables/Lists | JSON-LD | Dates |", "|---|---|---|---|---|---|---|"]
        for p in r["pages"]:
            L.append(f"| {p['url']} | {p['status']} | {p.get('words','')} | {p.get('h2_count','')} ({p.get('question_h2','')}) | {p.get('tables','')}/{p.get('lists','')} | {', '.join(p.get('jsonld_types') or []) or '—'} | {'yes' if p.get('dates') else 'no'} |")
    L += ["", f"llms.txt present: {r['llms_txt']} (informational — no measured effect on AI citations)", "",
          "> Spoofed-UA tests can differ from real verified bots. Confirm blocks in your CDN dashboard and server logs."]
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--pages", type=int, default=5, help="sample pages from the sitemap (default 5)")
    ap.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    ap.add_argument("--out", help="write the report to this file")
    a = ap.parse_args()
    rep = run(a.url, a.pages)
    out = json.dumps(rep, indent=2, ensure_ascii=False, default=str) if a.json else to_markdown(rep)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"Report written to {a.out} (score {rep['score']}/100)")
    else:
        print(out)
