#!/usr/bin/env python3
"""
AI-visibility statistics with honest error bars. Python 3.8+, standard library only.

Input: a CSV with one row per AI answer (one prompt sent once to one engine).
  required : prompt, engine
  one of   : answer (full answer text)  OR  mentioned (1/0, true/false)
  optional : date (YYYY-MM-DD or ISO), run (run number, informational), cited_urls (URLs separated by space, ; or |)
  Rows with neither answer nor mentioned (failed runs) are dropped and counted.
  Competitor metrics and share of voice need the answer column.

Template: assets/runs-template.csv

Usage:
  python3 visibility_stats.py runs.csv --brand "Acme" --aliases "Acme AI,acme.io" \
      --competitors "Foo|Foo Inc,Bar,Baz" --domain acme.io
  # before/after impact of a change (e.g. an article published on 2026-09-15):
  python3 visibility_stats.py runs.csv --brand Acme --split-date 2026-09-15 --prompts-file targeted.txt
  python3 visibility_stats.py runs.csv --brand Acme --json

Metrics (definitions are printed in the report so readers can't misread them):
  mention rate    = answers mentioning the brand / answers           (with Wilson 95% CI)
  share of voice  = brand mentions / mentions of all tracked brands  (brand + competitors)
  citation share  = answers citing a URL on --domain / answers with at least one cited URL
"""
import argparse
import csv
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from urllib.parse import urlparse

Z = 1.96


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s)


def matcher(names):
    pats = [re.escape(norm(n).strip()) for n in names if n and n.strip()]
    if not pats:
        return None
    return re.compile(r"(?<![a-z0-9])(" + "|".join(sorted(pats, key=len, reverse=True)) + r")(?![a-z0-9])")


def wilson(k, n):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def two_prop_p(k1, n1, k2, n2):
    if not n1 or not n2:
        return None
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    z = abs(k2 / n2 - k1 / n1) / se
    return math.erfc(z / math.sqrt(2))


def pct(x):
    return f"{100 * x:.0f}%"


def ci_str(k, n):
    p, lo, hi = wilson(k, n)
    return f"{pct(p)} [{pct(lo)}–{pct(hi)}]" if n else "—"


def domain_of(u):
    try:
        d = urlparse(u if "://" in u else "https://" + u).netloc.lower()
        return d[4:] if d.startswith("www.") else d
    except Exception:
        return ""


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        sys.exit("Empty CSV.")
    cols = {c.strip().lower() for c in rows[0].keys()}
    if not {"prompt", "engine"} <= cols or not ({"answer", "mentioned"} & cols):
        sys.exit("CSV needs columns: prompt, engine, and answer or mentioned. See assets/runs-template.csv")
    rows = [{k.strip().lower(): (v or "").strip() for k, v in r.items() if k} for r in rows]
    kept = [r for r in rows if r.get("answer") or r.get("mentioned")]
    if len(kept) < len(rows):
        print(f"Note: dropped {len(rows) - len(kept)} rows with no answer and no mentioned value (failed runs).", file=sys.stderr)
    return kept


def analyse(rows, brand_re, comps, domain):
    out = []
    for r in rows:
        ans = r.get("answer", "")
        if ans:
            text = norm(ans)
            m = bool(brand_re.search(text)) if brand_re else False
        else:
            m = r.get("mentioned", "").lower() in ("1", "true", "yes", "y", "t")
            text = ""
        comp_hits = [name for name, rx in comps if text and rx.search(text)]
        urls = [u for u in re.split(r"[\s;|,]+", r.get("cited_urls", "")) if u.startswith("http") or "." in u]
        doms = [domain_of(u) for u in urls if domain_of(u)]
        out.append({"prompt": r["prompt"], "engine": r["engine"].lower(), "date": r.get("date", "")[:10],
                    "m": m, "comps": comp_hits, "domains": doms, "has_text": bool(ans),
                    "own_cited": bool(domain and any(d == domain or d.endswith("." + domain) for d in doms))})
    return out


def summarise(a, comp_names):
    n = len(a)
    k = sum(x["m"] for x in a)
    res = {"answers": n, "mentions": k, "mention_rate": wilson(k, n)}
    by_engine = defaultdict(list)
    by_prompt = defaultdict(list)
    for x in a:
        by_engine[x["engine"]].append(x)
        by_prompt[x["prompt"]].append(x)
    res["engines"] = {e: (len(v), sum(x["m"] for x in v)) for e, v in sorted(by_engine.items())}
    res["prompts"] = {}
    for p, v in by_prompt.items():
        cc = Counter(c for x in v for c in x["comps"])
        res["prompts"][p] = (len(v), sum(x["m"] for x in v), cc.most_common(1)[0] if cc else None)
    texted = [x for x in a if x["has_text"]]
    res["text_answers"] = len(texted)
    res["competitors"] = None
    res["share_of_voice"] = None
    if texted and comp_names:
        comp_counts = Counter(c for x in texted for c in x["comps"])
        res["competitors"] = {c: comp_counts.get(c, 0) for c in comp_names}
        kt = sum(x["m"] for x in texted)
        total = kt + sum(comp_counts.values())
        res["share_of_voice"] = (kt / total) if total else None
    with_cites = [x for x in a if x["domains"]]
    res["citation"] = None
    if with_cites:
        dom_counts = Counter(d for x in with_cites for d in set(x["domains"]))
        res["citation"] = {"answers_with_citations": len(with_cites),
                           "own_cited": sum(x["own_cited"] for x in with_cites),
                           "top_domains": dom_counts.most_common(15)}
    return res


def md_report(brand, s, comp_names, domain, split=None):
    L = [f"# AI visibility — {brand}", ""]
    n, k = s["answers"], s["mentions"]
    L += [f"**Mention rate: {ci_str(k, n)}** — {k} of {n} answers mention {brand} (95% confidence interval in brackets).", ""]
    if comp_names and s["competitors"] is None:
        L.append("_Competitor metrics and share of voice need the `answer` column (full answer text)._")
        L.append("")
    if s["share_of_voice"] is not None:
        L.append(f"**Share of voice: {pct(s['share_of_voice'])}** of all mentions of tracked brands ({brand} + {len(comp_names)} competitors).")
        L.append("")
    if s["citation"]:
        c = s["citation"]
        if domain:
            L.append(f"**Citation share: {ci_str(c['own_cited'], c['answers_with_citations'])}** of answers with sources cite {domain}.")
            L.append("")
    L += ["## By engine", "", "| Engine | Answers | Mentions | Mention rate [95% CI] |", "|---|---|---|---|"]
    for e, (ne, ke) in s["engines"].items():
        L.append(f"| {e} | {ne} | {ke} | {ci_str(ke, ne)} |")
    if s["competitors"] is not None:
        nt = s["text_answers"]
        kt = k if nt == n else None
        L += ["", f"## Who gets recommended ({nt} answers with text)", "", "| Brand | Answers mentioning | Mention rate [95% CI] |", "|---|---|---|"]
        if kt is not None:
            L.append(f"| **{brand}** | {kt} | {ci_str(kt, nt)} |")
        for c, kc in sorted(s["competitors"].items(), key=lambda x: -x[1]):
            L.append(f"| {c} | {kc} | {ci_str(kc, nt)} |")
    L += ["", "## By prompt", "", "| Prompt | Answers | Mentions | Rate | Top competitor |", "|---|---|---|---|---|"]
    for p, (np_, kp, top) in sorted(s["prompts"].items(), key=lambda x: (x[1][1] / max(1, x[1][0]))):
        rate = f"{kp}/{np_}" if np_ < 5 else ci_str(kp, np_)
        L.append(f"| {p[:110]} | {np_} | {kp} | {rate} | {f'{top[0]} ({top[1]}/{np_})' if top else '—'} |")
    if s["citation"]:
        L += ["", "## Most cited domains (share of answers with sources)", "", "| Domain | Answers citing |", "|---|---|"]
        for d, c in s["citation"]["top_domains"]:
            L.append(f"| {d} | {c} ({pct(c / s['citation']['answers_with_citations'])}) |")
    if split:
        b, a_, p, _ = split
        L += ["", f"## Before / after {split[3]}", "",
              "| Period | Answers | Mentions | Mention rate [95% CI] |", "|---|---|---|---|",
              f"| Before | {b[0]} | {b[1]} | {ci_str(b[1], b[0])} |", f"| After | {a_[0]} | {a_[1]} | {ci_str(a_[1], a_[0])} |", ""]
        if p is None:
            L.append("Not enough data on one side to compare.")
        else:
            delta = (a_[1] / a_[0] - b[1] / b[0]) * 100
            verdict = "statistically significant (p < 0.05)" if p < 0.05 else "NOT significant — could be noise; keep measuring"
            L.append(f"Change: **{delta:+.0f} pts**, p = {p:.3f} → {verdict}. Correlation only: other things changed too.")
    L += ["", "## Read this before quoting numbers", "",
          f"- Answers vary run to run; this is a sample. With n = {n}, the margin of error is about ±{100 * (wilson(k, n)[2] - wilson(k, n)[1]) / 2:.0f} pts.",
          "- Rule of thumb: ~100 answers for ±10 pts, ~385 for ±5 pts. Pool related prompts instead of over-running one.",
          "- Prompts with fewer than 5 answers show raw counts, not percentages. Don't quote them as percentages.",
          "- Mention detection is name matching on answer text: check aliases and homonyms (spot-read 10 answers)."]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--brand", required=True)
    ap.add_argument("--aliases", default="", help="comma-separated extra names for the brand (product names, domain)")
    ap.add_argument("--competitors", default="", help="comma-separated; use | for aliases: 'Foo|Foo Inc,Bar'")
    ap.add_argument("--domain", default="", help="brand domain for citation share, e.g. acme.io")
    ap.add_argument("--split-date", default="", help="YYYY-MM-DD: compare answers before vs on/after this date")
    ap.add_argument("--prompts-file", default="", help="only analyse prompts listed in this file (one per line)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    rows = load(a.csv)
    if a.prompts_file:
        keep = {l.strip() for l in open(a.prompts_file, encoding="utf-8") if l.strip()}
        rows = [r for r in rows if r["prompt"] in keep]
        if not rows:
            sys.exit("No rows match --prompts-file (exact, case-sensitive match on the prompt text).")
    brand_re = matcher([a.brand] + [x for x in a.aliases.split(",") if x.strip()])
    comps = []
    for c in [x for x in a.competitors.split(",") if x.strip()]:
        names = [y.strip() for y in c.split("|") if y.strip()]
        comps.append((names[0], matcher(names)))
    comp_names = [c[0] for c in comps]
    domain = domain_of(a.domain) if a.domain else ""
    data = analyse(rows, brand_re, comps, domain)
    s = summarise(data, comp_names)

    split = None
    if a.split_date:
        before = [x for x in data if x["date"] and x["date"] < a.split_date]
        after = [x for x in data if x["date"] and x["date"] >= a.split_date]
        b = (len(before), sum(x["m"] for x in before))
        af = (len(after), sum(x["m"] for x in after))
        split = (b, af, two_prop_p(b[1], b[0], af[1], af[0]), a.split_date)
        s["split"] = {"date": a.split_date, "before": b, "after": af, "p_value": split[2]}

    out = json.dumps(s, indent=2, default=str) if a.json else md_report(a.brand, s, comp_names, domain, split)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out)
        print(f"Written to {a.out}")
    else:
        print(out)


if __name__ == "__main__":
    main()
