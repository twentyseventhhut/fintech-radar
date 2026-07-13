#!/usr/bin/env python3
"""Download IR/press materials discovered by the research agents.

Reads every registry/ir_sources/<slug>.json (schema: {slug, company, materials:[{title,
date, doc_type, url, ...}]}) and downloads each material URL into
  data/<slug>/ir/<doc_type>/<safe-filename>

Tokenless, resumable, checkpointed (manifest_ir.csv flushed per file), disk-guarded.
Uses a browser-like User-Agent (many IR CDNs reject scripted UAs).
"""
import json, csv, os, sys, time, glob, hashlib, re, urllib.request, urllib.error, shutil, gzip

BASE = os.environ.get("IR_DATASET", os.path.expanduser("~/Documents/IR-dataset"))
DATA = os.path.join(BASE, "data")
LOGS = os.path.join(BASE, "logs")
SRC = os.path.join(BASE, "registry", "ir_sources")
MANIFEST = os.path.join(BASE, "registry", "manifest_ir.csv")
MIN_FREE_GB = 1.0
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip, deflate"}
COLS = ["company", "slug", "doc_type", "title", "date", "filename", "url",
        "local_path", "bytes", "content_type", "status"]
EXT_OK = (".pdf", ".pptx", ".ppt", ".xlsx", ".xls", ".doc", ".docx", ".zip", ".csv")


def log(m):
    line = time.strftime("%H:%M:%S ") + m
    print(line, flush=True)
    with open(os.path.join(LOGS, "ir_download.log"), "a") as f:
        f.write(line + "\n")


def free_gb():
    return shutil.disk_usage(BASE).free / 1e9


def sanitize(name):
    name = re.sub(r"[^\w.\-]+", "_", name).strip("_")
    return name[:150] or "file"


def fname_from(url, title, content_type):
    base = url.split("?")[0].split("#")[0].rstrip("/")
    fn = os.path.basename(base)
    ext = os.path.splitext(fn)[1].lower()
    if ext in EXT_OK:
        return sanitize(fn)
    # no usable extension on the URL -> derive from content-type, keep a hash to avoid collisions
    ct = (content_type or "").lower()
    ext = (".pdf" if "pdf" in ct else ".pptx" if "presentation" in ct
           else ".xlsx" if ("sheet" in ct or "excel" in ct)
           else ".html" if "html" in ct else ".bin")
    stem = os.path.splitext(sanitize(fn or title or "file"))[0][:120]
    h = hashlib.md5(url.encode()).hexdigest()[:6]
    return f"{stem}_{h}{ext}"


PERMANENT_HTTP = {400, 401, 403, 404, 405, 410, 451}


def fetch(url, retries=2):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=25) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    try: raw = gzip.decompress(raw)
                    except Exception: pass
                return raw, r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            if e.code in PERMANENT_HTTP:
                raise                      # dead link -> fail fast, no retry
            last = e; time.sleep(1.0 * (i + 1))
        except Exception as e:
            last = e; time.sleep(1.0 * (i + 1))
    raise last


def load_done():
    done = set()
    if os.path.exists(MANIFEST):
        for r in csv.DictReader(open(MANIFEST)):
            if r["status"] == "ok":
                done.add(r["url"])
    return done


def main():
    os.makedirs(DATA, exist_ok=True)
    os.makedirs(LOGS, exist_ok=True)      # fresh cloud work dir has no logs/ — log() opens LOGS/ir_download.log
    new = not os.path.exists(MANIFEST)
    mf = open(MANIFEST, "a", newline="")
    w = csv.DictWriter(mf, fieldnames=COLS)
    if new:
        w.writeheader(); mf.flush()
    done = load_done()

    only = set(sys.argv[1:])
    files = sorted(glob.glob(os.path.join(SRC, "*.json")))
    n_ok = 0
    for jf in files:
        try:
            rec = json.load(open(jf))
        except Exception as e:
            log(f"  !! bad json {jf}: {e}"); continue
        slug = rec.get("slug") or os.path.splitext(os.path.basename(jf))[0]
        if only and slug not in only:
            continue
        company = rec.get("company", slug)
        mats = rec.get("materials", []) or []
        log(f"{company} ({slug}): {len(mats)} materials")
        for m in mats:
            url = (m.get("url") or "").strip()
            if not url or not url.lower().startswith("http") or url in done:
                continue
            if free_gb() < MIN_FREE_GB:
                log(f"STOP: free disk {free_gb():.2f}GB < {MIN_FREE_GB}GB"); mf.flush(); return
            dtype = sanitize(m.get("doc_type", "other") or "other")
            row = {"company": company, "slug": slug, "doc_type": dtype,
                   "title": (m.get("title", "") or "")[:200], "date": m.get("date", ""),
                   "filename": "", "url": url, "local_path": "", "bytes": 0,
                   "content_type": "", "status": ""}
            try:
                blob, ct = fetch(url)
                fn = fname_from(url, m.get("title", ""), ct)
                outdir = os.path.join(DATA, slug, "ir", dtype)
                local = os.path.join(outdir, fn)
                if os.path.exists(local) and os.path.getsize(local) > 0:
                    row.update(filename=fn, local_path=local, content_type=ct,
                               bytes=os.path.getsize(local), status="ok")
                    done.add(url); w.writerow(row); mf.flush(); continue
                os.makedirs(outdir, exist_ok=True)
                with open(local, "wb") as out:
                    out.write(blob)
                row.update(filename=fn, local_path=local, bytes=len(blob),
                           content_type=ct, status="ok")
                done.add(url); n_ok += 1
            except Exception as e:
                row["status"] = f"err:{str(e)[:120]}"
            w.writerow(row); mf.flush()
            time.sleep(0.4)
        log(f"  free disk {free_gb():.2f}GB; files ok this run={n_ok}")
    mf.flush(); mf.close()
    log(f"FINISHED ir_download. ok this run={n_ok}; free={free_gb():.2f}GB")


if __name__ == "__main__":
    main()
