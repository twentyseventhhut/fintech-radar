#!/usr/bin/env python3
"""Download SEC EDGAR filings (since 2024-01-01) for all companies in edgar_map.csv.

Captures the substantive IR documents:
  - Periodic/annual reports:  10-K, 10-Q, 20-F, 40-F, ARS, DEF 14A  (primary doc)
  - Earnings / events:        8-K, 6-K  -> primary doc + every EX-99.* exhibit
                              (earnings press releases, investor presentations,
                               letters to shareholders live here)
Skips XBRL/data/graphics noise (.xml, R*.htm, .jpg/.gif/.png) to save disk.

Resumable + checkpointed: a manifest row is flushed after every file; existing
non-empty files are skipped on re-run. Stops gracefully if free disk < MIN_FREE_GB.
"""
import json, csv, os, sys, time, urllib.request, urllib.error, shutil, re

BASE = os.environ.get("IR_DATASET", os.path.expanduser("~/Documents/IR-dataset"))
DATA = os.path.join(BASE, "data")
LOGS = os.path.join(BASE, "logs")
MANIFEST = os.path.join(BASE, "registry", "manifest_edgar.csv")
EDGAR_MAP = os.path.join(BASE, "registry", "edgar_map.csv")
UA = "IR research dataset (contact: you@example.com)"
CUTOFF = "2024-01-01"
MIN_FREE_GB = 0.7  # stop if less than this free

PERIODIC = {"10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A", "40-F", "40-F/A",
            "ARS", "DEF 14A", "DEFA14A", "6-K", "6-K/A", "8-K", "8-K/A"}
# forms whose EX-99.* exhibits we want (presentations / releases / letters)
EXHIBIT_FORMS = {"8-K", "8-K/A", "6-K", "6-K/A"}

HEADERS = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate"}
MANIFEST_COLS = ["company", "slug", "cik", "form", "filing_date", "accession",
                 "doc_type", "filename", "url", "local_path", "bytes", "status"]


def log(msg):
    line = time.strftime("%H:%M:%S ") + msg
    print(line, flush=True)
    with open(os.path.join(LOGS, "edgar.log"), "a") as f:
        f.write(line + "\n")


def free_gb():
    return shutil.disk_usage(BASE).free / 1e9


def fetch(url, retries=4, binary=True):
    import gzip
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return raw if binary else raw.decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def load_done():
    """Return (done_paths, done_accessions). Dedup by ACCESSION too — local_path is machine-specific
    (won't match in a fresh cloud work dir), so path-only dedup would re-download the whole corpus."""
    paths, accs = set(), set()
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as f:
            for row in csv.DictReader(f):
                if row.get("status") == "ok":
                    paths.add(row.get("local_path", ""))
                    if row.get("accession"):
                        accs.add(row["accession"])
    return paths, accs


def collect_filings(cik):
    """Return list of target filings (dicts) since CUTOFF across all submission shards."""
    out = []
    base = f"https://data.sec.gov/submissions/CIK{cik}.json"
    data = json.loads(fetch(base, binary=False))
    name = data.get("name", "")
    shards = [data["filings"]["recent"]]
    for extra in data["filings"].get("files", []):
        time.sleep(0.2)
        sh = json.loads(fetch(f"https://data.sec.gov/submissions/{extra['name']}", binary=False))
        shards.append(sh)
    for sh in shards:
        forms = sh["form"]; dates = sh["filingDate"]; accs = sh["accessionNumber"]
        prim = sh.get("primaryDocument", [""] * len(forms))
        for i in range(len(forms)):
            if dates[i] >= CUTOFF and forms[i] in PERIODIC:
                out.append({"form": forms[i], "date": dates[i],
                            "accession": accs[i], "primary": prim[i]})
    return name, out


import html as _html

def parse_index_htm(text):
    """Parse the EDGAR filing -index.htm 'Document Format Files' table.
    Returns list of {name, type, desc}. The real document Type (EX-99.1, 10-K,
    GRAPHIC, EX-101.*) lives here -- index.json only has useless icon names."""
    docs = []
    for tr in re.finditer(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", tr.group(1), re.S | re.I)
        if len(cells) < 4:
            continue
        # Document cell (idx 2): prefer the <a href> basename. Inline-XBRL docs are
        # linked via the viewer as /ix?doc=/Archives/.../file.htm -> unwrap the doc param.
        href = re.search(r'href="([^"]+)"', cells[2], re.I)
        if href:
            raw = _html.unescape(href.group(1))
            if "doc=" in raw:
                import urllib.parse as _up
                doc = _up.parse_qs(_up.urlparse(raw).query).get("doc", [""])[0]
                name = os.path.basename(doc) if doc else ""
            else:
                name = os.path.basename(raw.split("?")[0].split("#")[0])
        else:
            txt = re.sub("<[^>]+>", "", _html.unescape(cells[2])).strip()
            name = txt.split()[0] if txt else ""
        doctype = re.sub("<[^>]+>", "", _html.unescape(cells[3])).strip()
        desc = re.sub("<[^>]+>", "", _html.unescape(cells[1])).strip()
        if name:
            docs.append({"name": name, "type": doctype, "desc": desc})
    return docs


def want_doc(form, doctype, name):
    """Decide from the REAL document type whether to keep it.
    Keep: the report itself + EX-99.* (press releases / investor presentations /
    shareholder letters) + standalone PDFs. Drop XBRL, graphics, certs, consents."""
    dt = (doctype or "").upper().strip()
    nm = (name or "").lower()
    if not name:
        return False
    # hard noise filters
    if dt in ("GRAPHIC", "XML", "ZIP", "JSON", "CALC", ""):
        if nm.endswith(".pdf"):
            return True            # glossy annual report PDFs sometimes lack a type
        return False
    if dt.startswith("EX-101") or dt.startswith("EX-100"):   # XBRL
        return False
    if nm.endswith((".xsd", ".jpg", ".jpeg", ".gif", ".png", ".css", ".js")):
        return False
    # keep the report document, the cover, and substantive exhibits
    if dt in PERIODIC or dt == "ARS":
        return True
    if dt.startswith("EX-99"):     # releases, presentations, letters
        return True
    return False


def main():
    os.makedirs(DATA, exist_ok=True)
    os.makedirs(LOGS, exist_ok=True)      # fresh cloud work dir has no logs/ — log() opens LOGS/edgar.log
    new_manifest = not os.path.exists(MANIFEST)
    mf = open(MANIFEST, "a", newline="")
    writer = csv.DictWriter(mf, fieldnames=MANIFEST_COLS)
    if new_manifest:
        writer.writeheader(); mf.flush()
    done, done_acc = load_done()

    companies = list(csv.DictReader(open(EDGAR_MAP)))
    # allow optional CLI filter: python edgar_download.py slug1 slug2 ...
    only = set(sys.argv[1:])
    if only:
        companies = [c for c in companies if c["slug"] in only]

    total_files = 0
    for ci, c in enumerate(companies, 1):
        if free_gb() < MIN_FREE_GB:
            log(f"STOP: free disk {free_gb():.2f}GB < {MIN_FREE_GB}GB"); break
        cik = c["cik"]; slug = c["slug"]; company = c["company"]
        log(f"[{ci}/{len(companies)}] {company} (CIK {cik})")
        try:
            secname, filings = collect_filings(cik)
        except Exception as e:
            log(f"  !! submissions fetch failed: {e}"); continue
        log(f"  {len(filings)} target filings since {CUTOFF}")
        time.sleep(0.3)
        for fl in filings:
            if fl["accession"] in done_acc:        # already collected (accession-level, path-independent)
                continue
            if free_gb() < MIN_FREE_GB:
                log(f"STOP mid-company: free disk {free_gb():.2f}GB"); mf.flush(); return
            acc_nodash = fl["accession"].replace("-", "")
            cik_int = int(cik)
            idx_url = (f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/"
                       f"{fl['accession']}-index.htm")
            try:
                items = parse_index_htm(fetch(idx_url, binary=False))
            except Exception as e:
                log(f"  !! index fail {fl['form']} {fl['date']}: {e}"); continue
            outdir = os.path.join(DATA, slug, "edgar", fl["form"].replace("/", "-"),
                                  f"{fl['date']}_{acc_nodash}")
            picked = [it for it in items if want_doc(fl["form"], it["type"], it["name"])]
            if not picked:  # fallback to primary doc
                if fl["primary"]:
                    picked = [{"name": fl["primary"], "type": fl["form"]}]
            for it in picked:
                fn = it["name"]
                local = os.path.join(outdir, fn)
                if local in done or (os.path.exists(local) and os.path.getsize(local) > 0):
                    continue
                url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/{fn}"
                row = {"company": company, "slug": slug, "cik": cik, "form": fl["form"],
                       "filing_date": fl["date"], "accession": fl["accession"],
                       "doc_type": it.get("type", ""), "filename": fn, "url": url,
                       "local_path": local, "bytes": 0, "status": ""}
                try:
                    blob = fetch(url)
                    os.makedirs(outdir, exist_ok=True)
                    with open(local, "wb") as out:
                        out.write(blob)
                    row["bytes"] = len(blob); row["status"] = "ok"
                    total_files += 1
                    done.add(local)
                except Exception as e:
                    row["status"] = f"err:{e}"
                writer.writerow(row); mf.flush()
                time.sleep(0.12)  # ~8 req/s, under SEC's 10/s limit
        log(f"  done {company}; files so far={total_files}; free={free_gb():.2f}GB")
    mf.flush(); mf.close()
    log(f"FINISHED. files downloaded this run={total_files}; free disk={free_gb():.2f}GB")


if __name__ == "__main__":
    main()
