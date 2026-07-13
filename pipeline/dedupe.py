#!/usr/bin/env python3
"""
dedupe.py — stage 3: clean + deduplicate per-mention news into unique stories,
then enrich (authoritative source for paywalled/blocked ones + clean titles).

Flow:
  1. prep      : DB window -> cleaned atomic mentions (/tmp/mentions.json + compact .txt)
  2. (LLM)     : cluster same-event duplicates -> /tmp/clusters.json
  3. assemble  : merge -> unique stories. Emits /tmp/stories.json (for enrichment) and
                 the CSV. Optional overrides folded in:
                   --titles        titles.json   {story_id: "clean headline"}
                   --extra-sources extra.json     {story_id: ["https://authoritative", ...]}
                 Extra-source TEXT is pulled from fintech_radar's source cache, so the URLs
                 must be fetched first (fintech_radar fetch_source_text / `expand`).

Each story gets a STABLE id = "s"+sha1(sorted member-mention ids), so titles/sources
keyed by id survive re-assembly. Mention ids are CONTENT-addressed (see mention_id),
which makes story_id globally unique across months. (Older monthly artifacts used
positional mention ids and so produced cross-month story_id collisions; re-build a
month with a fresh `prep` to migrate it. `(story_id, month)` is unique either way.)
"""
import argparse, csv, hashlib, json, os, re
from urllib.parse import urlparse
import fintech_radar as fr

ROOT = os.path.dirname(os.path.abspath(__file__))

NEWS_CHANNELS = {"This Week in Fintech", "Connecting the Dots in Fintech",
                 "Fintech Wrap Up"}  # roundup/news; the rest (Brainfood, Blueprint) are essays

SUMMARY = re.compile(
    r"in the news this week|today.?s agenda|here.?s what|the inbox is overflowing|"
    r"reads of the week|in case you missed|quick hits|chart of the week|"
    r"table of contents|what we.?re reading|elsewhere in|top stories", re.I)

JUNK_MARKERS = [
    "new to stocktwits", "add to watchlist", "log in to existing", "create account",
    "continue with apple", "enable javascript", "please enable js", "captcha",
    "verify you are human", "are you a robot", "subscribe to read", "subscribe to continue",
    "we use cookies", "accept all cookies", "page not found", "404 error",
    "access denied", "you have been blocked", "sign in to continue", "for full access",
]


def looks_like_junk(t: str) -> bool:
    low = t[:2500].lower()
    if sum(m in low for m in JUNK_MARKERS) >= 2:
        return True
    if len(re.findall(r"\$\d[\d,\.]*", t[:1500])) >= 8:
        return True
    lines = [ln.strip() for ln in t.split("\n") if ln.strip()]
    if len(lines) >= 12 and sum(1 for ln in lines if len(ln.split()) <= 3) / len(lines) > 0.6:
        return True
    return False


def canon(u: str) -> str:
    p = urlparse(u)
    return f"{p.scheme}://{p.netloc}{p.path}".rstrip("/")


def dom(u: str) -> str:
    h = urlparse(u).netloc.lower()
    return h[4:] if h.startswith("www.") else h


def clean_text_of(rec):
    st, txt = rec.get("status", "pending"), (rec.get("text") or "").strip()
    if st == "ok" and txt and not looks_like_junk(txt):
        return txt
    return None


def mention_id(ch_short, date, text):
    """Content-addressed mention id, stable across runs AND months.

    The single source of truth shared with daily_source.py (which imports this).
    Historical bug: cmd_prep used positional ids (`len(mentions)`) that reset to 0
    every month, so `story_id()` — a hash of the member-mention ids — produced the
    SAME id for unrelated stories sitting at the same index in different months
    (e.g. singleton index 27 -> story_id sbc33ea4e in 10 different months). Hashing
    content instead makes mention ids globally unique, so story_id is too.
    """
    return "m" + hashlib.sha1(f"{ch_short}|{date}|{text}".encode()).hexdigest()[:10]


def build_mentions(since, until=None):
    posts = fr.window_items(fr.load_db(), since, until)
    out = {}
    for p in posts:
        ch_short = p["source"].split("(")[0].strip()
        for ni in p.get("news_items", []):
            t = re.sub(r"\s+", " ", ni.get("text", "")).strip()
            links = ni.get("links", [])
            if len(t) < 45 or SUMMARY.search(t) or len(links) > 3:
                continue
            mid = mention_id(ch_short, p["published_date"], t)
            out[mid] = {"id": mid, "ch": p["source"], "ch_short": ch_short,
                        "date": p["published_date"], "text": t, "links": links}
    return list(out.values())


def cmd_prep(args):
    if getattr(args, "month", None):
        since, until = fr.month_bounds(args.month)
    else:
        since, until = fr.resolve_since(args.since), None
    mentions = build_mentions(since, until)
    json.dump(mentions, open(args.mentions, "w"), ensure_ascii=False)
    lines = [f"{m['id']}\t[{m['ch_short'][:16]}]\t{m['text'][:150]}" for m in mentions]
    open(args.compact, "w").write("\n".join(lines))
    print(f"{len(mentions)} atomic mentions -> {args.mentions}")


def mk_title(txt):
    t = re.sub(r'^[^A-Za-z0-9“"]+', "", txt).strip()
    t = re.sub(r"^\d+[\.\)]\s*", "", t)  # leading "2." / "3)"
    return re.split(r"(?<=[.!?])\s", t)[0][:120]


def story_id(ids):
    # ids are content-addressed mention ids -> this hash is content-derived, so the
    # 8-hex (32-bit) truncation only carries a negligible birthday risk; the patcher's
    # (story_id, month) key tolerates even that.
    return "s" + hashlib.sha1(",".join(map(str, sorted(ids))).encode()).hexdigest()[:8]


def cmd_assemble(args):
    mentions = {m["id"]: m for m in json.load(open(args.mentions))}
    groups = json.load(open(args.clusters)).get("groups", [])
    cache = fr.load_source_cache()
    titles = json.load(open(args.titles)) if args.titles and os.path.exists(args.titles) else {}
    extra = json.load(open(args.extra_sources)) if args.extra_sources and os.path.exists(args.extra_sources) else {}

    assigned, clusters = set(), []
    for g in groups:
        ids = [i for i in g.get("ids", []) if i in mentions]
        if len(ids) >= 2:
            clusters.append((g.get("title", "").strip(), ids)); assigned.update(ids)
    for mid in mentions:
        if mid not in assigned:
            clusters.append(("", [mid]))

    rows, stories = [], []
    for cl_title, ids in clusters:
        sid = story_id(ids)
        ms = sorted((mentions[i] for i in ids), key=lambda m: m["ch_short"])
        date = min(m["date"] for m in ms)
        chans = sorted(set(m["ch_short"] for m in ms))
        is_news = True  # channel-name gate removed; junk filtered by content
        agg = "\n\n".join(f"[{m['ch_short']}] {m['text']}" for m in ms)

        # original primary sources (in newsletter)
        seen = {}
        for m in ms:
            for l in m["links"]:
                seen.setdefault(canon(l), l)
        clean_blocks, dead_blocks, links, ok_n = [], [], [], 0
        for cu, l in seen.items():
            rec = cache.get(l) or cache.get(cu) or {}
            links.append(cu)
            txt = clean_text_of(rec)
            if txt:
                clean_blocks.append(f"[{dom(l)}] {cu}\n{txt[:6000]}"); ok_n += 1
            else:
                st = rec.get("status", "pending")
                reason = "навигация/мусор" if (st == "ok") else st
                dead_blocks.append(f"[{dom(l)}] {cu}\n(первоисточник недоступен: {reason})")

        # folded-in authoritative sources we found ourselves
        for u in extra.get(sid, []):
            cu = canon(u)
            if cu in seen:
                continue
            rec = cache.get(u) or cache.get(cu) or {}
            txt = clean_text_of(rec)
            links.append(cu)
            if txt:
                clean_blocks.append(f"[{dom(u)}] {cu}  ← найден авторитетный источник\n{txt[:6000]}")
                ok_n += 1
            else:
                st = rec.get("status", "pending")
                reason = "навигация/мусор" if st == "ok" else st
                dead_blocks.append(f"[{dom(u)}] {cu}  ← найден, но не извлёкся ({reason})")
        blocks = clean_blocks + dead_blocks  # usable sources first

        if titles.get(sid):
            title = titles[sid]
        elif cl_title:
            title = cl_title
        else:
            title = mk_title(ms[0]["text"])
            if not is_news:  # essay/analysis fragment -> prefix with the publication
                pub = ("Brainfood" if "Brainfood" in ms[0]["ch"] else
                       "Blueprint" if "Blueprint" in ms[0]["ch"] else ms[0]["ch_short"])
                title = f"{pub}: {title}"
        rows.append({"date": date, "title": title, "n_mentions": len(ms),
                     "channels": ", ".join(chans), "n_primary_sources": len(links),
                     "n_sources_with_text": ok_n, "aggregator_texts": agg,
                     "primary_links": "\n".join(links), "primary_sources": "\n\n".join(blocks)})
        stories.append({"id": sid, "date": date, "title_auto": title, "is_news": is_news,
                        "n_mentions": len(ms), "channels": chans, "n_clean_sources": ok_n,
                        "needs_source": is_news and ok_n == 0,
                        "agg_text": agg[:1500],
                        "candidate_links": links})

    rows.sort(key=lambda r: (r["date"], r["n_mentions"]), reverse=True)
    cols = ["date", "title", "n_mentions", "channels", "n_primary_sources",
            "n_sources_with_text", "aggregator_texts", "primary_links", "primary_sources"]
    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL); w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])
    json.dump(stories, open(args.stories_out, "w"), ensure_ascii=False, indent=1)

    merged = sum(1 for r in rows if r["n_mentions"] > 1)
    withtext = sum(1 for r in rows if r["n_sources_with_text"] > 0)
    needs = sum(1 for s in stories if s["needs_source"])
    print(f"{len(rows)} unique stories ({merged} merged) · {withtext} with clean source text · "
          f"{needs} NEWS stories still need an authoritative source")
    print(f"CSV -> {args.out}\nstories -> {args.stories_out}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    pp = sub.add_parser("prep")
    pp.add_argument("--since", default="7")
    pp.add_argument("--month", help="YYYY-MM (overrides --since with that calendar month)")
    pp.add_argument("--mentions", default="/tmp/mentions.json")
    pp.add_argument("--compact", default="/tmp/mentions_compact.txt")
    pp.set_defaults(func=cmd_prep)
    pa = sub.add_parser("assemble")
    pa.add_argument("--since", default="7")
    pa.add_argument("--mentions", default="/tmp/mentions.json")
    pa.add_argument("--clusters", default="/tmp/clusters.json")
    pa.add_argument("--titles", default="/tmp/titles.json")
    pa.add_argument("--extra-sources", default="/tmp/extra_sources.json")
    pa.add_argument("--stories-out", default="/tmp/stories.json")
    pa.add_argument("--out", default=os.path.join(ROOT, "data", "fintech-week-deduped.csv"))
    pa.set_defaults(func=cmd_assemble)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
