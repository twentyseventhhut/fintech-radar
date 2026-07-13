#!/usr/bin/env python3
"""Finalize a month's enrichment: merge agent parts -> titles.json + extra.json,
fetch the newly-found authoritative sources, re-assemble the deduped CSV, backup.

Usage: python3 enrich_finalize.py YYYY-MM
"""
import sys, json, glob, os, threading, subprocess
import concurrent.futures as cf
import fintech_radar as fr

ym = sys.argv[1]
d = f"months/{ym}"
titles, extra = {}, {}
for f in sorted(glob.glob(f"{d}/enrich_part_*.json")):
    try:
        data = json.load(open(f))
    except Exception as e:
        print("skip", f, e); continue
    for sid, v in data.items():
        if v.get("title"):
            titles[sid] = v["title"]
        urls = [u for u in (v.get("source_urls") or []) if isinstance(u, str) and u.startswith("http")]
        if urls:
            extra[sid] = urls
json.dump(titles, open(f"{d}/titles.json", "w"), ensure_ascii=False)
json.dump(extra, open(f"{d}/extra.json", "w"), ensure_ascii=False)

cache = fr.load_source_cache()
todo = list(dict.fromkeys(u for us in extra.values() for u in us
                          if u not in cache or cache[u].get("status") != "ok"))
print(f"{ym}: {len(titles)} titles, {len(extra)} stories sourced, {len(todo)} new URLs to fetch", flush=True)

lock = threading.Lock(); done = [0]; ok = [0]
def work(u):
    try:
        rec = fr.fetch_source_text(u)
    except Exception as e:
        rec = {"url": u, "domain": fr._host(u), "status": "error", "text": "",
               "word_count": 0, "method": "error"}
    with lock:
        fr.append_source_cache(rec); done[0] += 1
        if rec.get("status") == "ok":
            ok[0] += 1
if todo:
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for _ in cf.as_completed([ex.submit(work, u) for u in todo]):
            pass
print(f"{ym}: fetched {done[0]} (ok={ok[0]})", flush=True)

subprocess.run(["python3", "dedupe.py", "assemble",
                "--mentions", f"{d}/mentions.json", "--clusters", f"{d}/clusters.json",
                "--titles", f"{d}/titles.json", "--extra-sources", f"{d}/extra.json",
                "--stories-out", f"{d}/stories.json", "--out", f"{d}/deduped.csv"])
subprocess.run(["zsh", "backup.sh"])
print(f"{ym}: DONE", flush=True)
