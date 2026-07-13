#!/usr/bin/env python3
"""daily_source.py — incremental [1] sourcing for the daily pipeline.

Only NEW posts (by stable post id) are processed, so existing notes/ids are never
touched. Deterministic core; the single LLM step (cluster new mentions + drop those
already in the base + emit title/sources/tags) is run by the orchestrator via
`claude -p` between `prep` and `assemble`, writing newstories.json.

  seed                        baseline: mark every post in the DB as processed (run ONCE).
  prep   --date YYYY-MM-DD     build new mentions from unprocessed posts → state/daily/<date>/
                              {mentions.json, compact.txt, recent_stories.json, new_post_ids.json}
  assemble --date .. --newstories N.json
                              append the agent's NEW stories to month files, fetch found
                              sources, generate notes (--only-new), mark posts processed,
                              write state/daily/<date>/new_story_ids.json

newstories.json = [{"mention_ids":[...], "title":"...", "source_urls":[...], "tags":[...]}, ...]
Mention id = dedupe.mention_id (content-addressed) → dedupe.story_id is globally unique.
"""
import argparse, glob, json, os, re, subprocess, datetime as dt
import fintech_radar as fr
import dedupe as dd

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(ROOT, "state")
PROCESSED = os.path.join(STATE, "processed_posts.json")
DAILY = os.path.join(STATE, "daily")


def load_processed():
    if not os.path.exists(PROCESSED):
        raise SystemExit("processed_posts.json missing — run `daily_source.py seed` once first.")
    return set(json.load(open(PROCESSED)))


def save_processed(ids):
    json.dump(sorted(ids), open(PROCESSED, "w"))


def day_dir(date, make=False):
    d = os.path.join(DAILY, date)
    if make:
        os.makedirs(d, exist_ok=True)
    return d


def mentions_from_posts(posts):
    out = {}
    for p in posts:
        ch_short = p["source"].split("(")[0].strip()
        for ni in p.get("news_items", []):
            t = re.sub(r"\s+", " ", ni.get("text", "")).strip()
            links = ni.get("links", [])
            if len(t) < 45 or dd.SUMMARY.search(t) or len(links) > 3:
                continue
            mid = dd.mention_id(ch_short, p["published_date"], t)
            out[mid] = {"id": mid, "ch": p["source"], "ch_short": ch_short,
                        "date": p["published_date"], "text": t, "links": links}
    return list(out.values())


def recent_existing_stories(lookback_days):
    cutoff = (dt.date.today() - dt.timedelta(days=lookback_days)).isoformat()
    res = []
    for sf in glob.glob(os.path.join(ROOT, "months", "*", "stories.json")):
        ym = os.path.basename(os.path.dirname(sf))
        tf = os.path.join(ROOT, "months", ym, "titles.json")
        titles = json.load(open(tf)) if os.path.exists(tf) else {}
        for s in json.load(open(sf)):
            if s.get("date", "") >= cutoff:
                res.append({"id": s["id"], "date": s["date"],
                            "title": titles.get(s["id"]) or s.get("title_auto", "")})
    res.sort(key=lambda r: r["date"], reverse=True)
    return res


def cmd_seed(args):
    db = fr.load_db()
    ids = {p["id"] for p in db.values()}
    os.makedirs(STATE, exist_ok=True)
    save_processed(ids)
    print(f"seeded {len(ids)} posts as processed baseline -> {PROCESSED}")


def cmd_prep(args):
    date = args.date
    d = day_dir(date, make=True)
    if getattr(args, "pubdate", None):
        # one-off single-day rebuild: take ALL posts published that day (dedup-vs-base handles overlaps)
        new_posts = [p for p in fr.load_db().values() if (p.get("published_date") or "") == args.pubdate]
    else:
        processed = load_processed()
        posts = fr.window_items(fr.load_db(), fr.resolve_since(str(args.since)), None)
        new_posts = [p for p in posts if p["id"] not in processed]
    mentions = mentions_from_posts(new_posts)
    json.dump(mentions, open(f"{d}/mentions.json", "w"), ensure_ascii=False)
    # compact: id \t post-date (fallback for event date) \t [channel] \t text
    open(f"{d}/compact.txt", "w").write(
        "\n".join(f"{m['id']}\t{m['date']}\t[{m['ch_short'][:16]}]\t{m['text'][:170]}" for m in mentions))
    json.dump([p["id"] for p in new_posts], open(f"{d}/new_post_ids.json", "w"))
    recent = recent_existing_stories(args.lookback)
    json.dump(recent, open(f"{d}/recent_stories.json", "w"), ensure_ascii=False)
    print(f"{date}: {len(new_posts)} new posts | {len(mentions)} new mentions | "
          f"{len(recent)} recent stories (<= {args.lookback}d) for dedup")
    print(f"artifacts -> {d}/")


def _merge_month_json(path, updates):
    cur = json.load(open(path)) if os.path.exists(path) else {}
    cur.update(updates)
    json.dump(cur, open(path, "w"), ensure_ascii=False)


_MON = "jan feb mar apr may jun jul aug sep oct nov dec".split()
_MIDX = {m: i + 1 for i, m in enumerate(_MON)}
_URLDATE = re.compile(r'/(20\d{2})[/-](\d{1,2})[/-](\d{1,2})(?:/|\b)')
_ISO = re.compile(r'\b(20\d{2})-(\d{2})-(\d{2})\b')
_MD = re.compile(r'\b(' + '|'.join(_MON) + r')[a-z]*\.?\s+(\d{1,2}),?\s+(20\d{2})\b', re.I)
_DM = re.compile(r'\b(\d{1,2})\s+(' + '|'.join(_MON) + r')[a-z]*\.?\s+(20\d{2})\b', re.I)


def _sane(d, post, lo=45, hi=2):
    try:
        x = dt.date.fromisoformat(d); p = dt.date.fromisoformat(post)
    except Exception:
        return None
    return d if (p - dt.timedelta(days=lo)) <= x <= (p + dt.timedelta(days=hi)) else None


def best_date(links, is_news, post_date, cache, brain_date=None):
    """Real source/event date, best-effort: URL date > news dateline (tight) > brain > post date."""
    for u in links:                                  # 1) date embedded in a primary-source URL
        m = _URLDATE.search(u)
        if m:
            try:
                d = dt.date(int(m[1]), int(m[2]), int(m[3])).isoformat()
                if _sane(d, post_date):
                    return d
            except Exception:
                pass
    if is_news:                                      # 2) dateline at the top of a fetched source (news only)
        for u in links:
            t = (cache.get(u) or {}).get("text", "")[:400]
            if not t:
                continue
            for rx, kind in ((_ISO, "iso"), (_MD, "md"), (_DM, "dm")):
                m = rx.search(t)
                if not m:
                    continue
                try:
                    if kind == "iso":
                        d = dt.date(int(m[1]), int(m[2]), int(m[3]))
                    elif kind == "md":
                        d = dt.date(int(m[3]), _MIDX[m[1][:3].lower()], int(m[2]))
                    else:
                        d = dt.date(int(m[3]), _MIDX[m[2][:3].lower()], int(m[1]))
                    s = _sane(d.isoformat(), post_date, lo=21)
                    if s:
                        return s
                except Exception:
                    pass
    if brain_date and re.match(r"^\d{4}-\d{2}-\d{2}$", str(brain_date)):  # 3) brain-inferred, bounded
        s = _sane(brain_date, post_date, lo=21)
        if s:
            return s
    return post_date                                 # 4) fallback: aggregator post date


def cmd_assemble(args):
    date = args.date
    d = day_dir(date)
    mentions = {m["id"]: m for m in json.load(open(f"{d}/mentions.json"))}
    newstories = json.load(open(args.newstories))
    cache = fr.load_source_cache()

    by_month, titles_by_month, extra_by_month, tags_by_month, new_ids = {}, {}, {}, {}, []
    for ns in newstories:
        ids = [i for i in ns.get("mention_ids", []) if i in mentions]
        if not ids:
            continue
        sid = dd.story_id(ids)
        ms = sorted((mentions[i] for i in ids), key=lambda m: m["ch_short"])
        chans = sorted(set(m["ch_short"] for m in ms))
        is_news = True  # newsletters are news; ads/junk dropped by content (cleaning + [1] brain)
        agg = "\n\n".join(f"[{m['ch_short']}] {m['text']}" for m in ms)
        seen = {}
        for m in ms:
            for l in m["links"]:
                seen.setdefault(dd.canon(l), l)
        links = list(seen.keys())
        post_date = min(m["date"] for m in ms)
        date0 = best_date(links, is_news, post_date, cache, ns.get("date") or ns.get("event_date"))
        ym = date0[:7]
        title = ns.get("title") or dd.mk_title(ms[0]["text"])
        srcs = [u for u in (ns.get("source_urls") or []) if isinstance(u, str) and u.startswith("http")]
        tags = ns.get("tags") or []
        story = {"id": sid, "date": date0, "title_auto": title, "is_news": is_news,
                 "n_mentions": len(ms), "channels": chans,
                 "n_clean_sources": sum(1 for u in links if (cache.get(u) or {}).get("status") == "ok"),
                 "needs_source": is_news and not srcs and not links,
                 "agg_text": agg[:1500], "candidate_links": links}
        by_month.setdefault(ym, []).append(story)
        titles_by_month.setdefault(ym, {})[sid] = title
        if srcs:
            extra_by_month.setdefault(ym, {})[sid] = srcs
        if tags:
            tags_by_month.setdefault(ym, {})[sid] = tags
        new_ids.append(sid)

    todo = sorted({u for mm in extra_by_month.values() for us in mm.values() for u in us
                   if (cache.get(u) or {}).get("status") != "ok"})
    for u in todo:
        try:
            fr.append_source_cache(fr.fetch_source_text(u))
        except Exception:
            pass

    for ym, stories in by_month.items():
        mdir = os.path.join(ROOT, "months", ym)
        os.makedirs(mdir, exist_ok=True)
        sf = os.path.join(mdir, "stories.json")
        cur = json.load(open(sf)) if os.path.exists(sf) else []
        have = {s["id"] for s in cur}
        cur.extend(s for s in stories if s["id"] not in have)
        json.dump(cur, open(sf, "w"), ensure_ascii=False, indent=1)
        if ym in titles_by_month: _merge_month_json(os.path.join(mdir, "titles.json"), titles_by_month[ym])
        if ym in extra_by_month:  _merge_month_json(os.path.join(mdir, "extra.json"),  extra_by_month[ym])
        if ym in tags_by_month:   _merge_month_json(os.path.join(mdir, "tags.json"),   tags_by_month[ym])
        subprocess.run(["python3", os.path.join(ROOT, "make_notes.py"), ym, "--only-new"], cwd=ROOT)

    processed = load_processed()
    processed.update(json.load(open(f"{d}/new_post_ids.json")))
    save_processed(processed)
    json.dump(new_ids, open(f"{d}/new_story_ids.json", "w"))
    print(f"{date}: {len(new_ids)} NEW stories across {len(by_month)} month(s); fetched {len(todo)} sources")
    print(f"new story ids -> {d}/new_story_ids.json")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    ps = sub.add_parser("seed"); ps.set_defaults(func=cmd_seed)
    pp = sub.add_parser("prep")
    pp.add_argument("--date", required=True)
    pp.add_argument("--since", default="4")
    pp.add_argument("--pubdate", help="one-off: build from ALL posts with this published_date (YYYY-MM-DD)")
    pp.add_argument("--lookback", type=int, default=90)   # wider archive so [1] sees reworded recent twins
    pp.set_defaults(func=cmd_prep)
    pa = sub.add_parser("assemble")
    pa.add_argument("--date", required=True)
    pa.add_argument("--newstories", required=True)
    pa.set_defaults(func=cmd_assemble)
    args = ap.parse_args()
    if not getattr(args, "cmd", None):
        ap.print_help(); raise SystemExit(1)
    args.func(args)


if __name__ == "__main__":
    main()
