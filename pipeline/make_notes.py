#!/usr/bin/env python3
"""Generate Obsidian notes (one per news story) into the Fintech update vault.

Usage:
  python3 make_notes.py <YYYY-MM | all> [--limit N] [--ids s1,s2] [--dry]

Reads months/<YM>/{stories.json,titles.json,extra.json} + state/source_cache.jsonl.
Writes one .md per is_news story to  <VAULT>/News/<YM>/<title>.md
Tags: uses months/<YM>/tags.json {sid:[tag,...]} when present (AI tags);
      else falls back to a light heuristic tagger so the note is still usable.
Re-runnable: overwrites a note's generated regions but PRESERVES enrichment
sections (context/challenge/post) if a note already exists.
"""
import sys, json, glob, os, re, html, datetime as dt

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root = Obsidian vault
NEWS = os.path.join(VAULT, "News")
MAXSRC = 20000  # cap per-source text length (chars) for sanity
# domains whose "full text" is paywall stubs / junk (login walls, quote pages) -> link-only
SRC_BLOCK = {"stocktwits.com","finance.yahoo.com","reuters.com","bloomberg.com","ft.com",
             "wsj.com","simplywall.st","seekingalpha.com","marketscreener.com","barrons.com",
             "msn.com","investing.com","tradingview.com","markets.businessinsider.com"}

def host(u):
    m = re.match(r"https?://([^/]+)", u or "")
    h = (m.group(1) if m else "").lower()
    return h[4:] if h.startswith("www.") else h

def is_blocked(dom):
    return any(dom == b or dom.endswith("." + b) for b in SRC_BLOCK)

# ---------- light heuristic fallback tagger (AI tags override this) ----------
REGION_KW = {
    "region/us": ["united states","u.s.","american","new york","silicon valley","sec ","cfpb","occ"," fed ","federal reserve"],
    "region/uk": ["uk","united kingdom","london","britain","fca","pra "],
    "region/europe": ["europe","eu ","european","ecb","euro ","germany","france","spain","italy","netherlands","ireland","sepa"],
    "region/latam": ["latam","latin america","brazil","brasil","mexico","méxico","colombia","argentina","chile","peru"],
    "region/asia": ["asia","india","china","singapore","indonesia","japan","hong kong","philippines","vietnam","thailand","upi"],
    "region/africa": ["africa","nigeria","kenya","egypt","south africa","ghana"],
    "region/mea": ["middle east","uae","dubai","saudi","qatar","bahrain","israel"],
}
TYPE_KW = {
    "type/m-and-a": ["acqui","merger","merge","takeover","buyout","to buy "],
    "type/funding": ["raise","raised","raises","funding","series ","seed round","valuation","valued at","investment round"],
    "type/earnings": ["earnings","revenue","quarterly","full-year","reported a profit","net income","q1 ","q2 ","q3 ","q4 ","results"],
    "type/product": ["launch","unveil","rolls out","introduce","new feature","debut","released"],
    "type/partnership": ["partner","partnership","teams up","collaborat","integration with"],
    "type/regulation": ["regulat","license","licence","fined","fine ","lawsuit","compliance","sanction","approval"],
    "type/expansion": ["expand","enters","expansion","goes live in","new market","launches in"],
    "type/leadership": ["appoints","names ","hires","steps down","ceo","resign","new chief"],
}
INDUSTRY_KW = {
    "industry/stablecoins": ["stablecoin","usdc","usdt","pyusd","mgusd"],
    "industry/crypto": ["crypto","bitcoin","ethereum","blockchain","web3","digital asset","tokeniz"],
    "industry/payments": ["payment","checkout","acquir","card network","merchant","pos ","remittance","cross-border"],
    "industry/neobank": ["neobank","challenger bank","digital bank"],
    "industry/banking": ["bank ","banking","core banking","deposit","baas","banking-as-a-service"],
    "industry/lending": ["loan","lending","credit","bnpl","buy now"],
    "industry/wealth": ["wealth","investing","brokerage","trading app","robo-advis"],
    "industry/insurtech": ["insurance","insurtech","underwrit"],
    "industry/agentic-commerce": ["agentic","ai agent","autonomous checkout","agent commerce"],
    "industry/ai": ["artificial intelligence"," ai ","machine learning","llm","genai"],
}

def heuristic_tags(text):
    t = (" " + text.lower() + " ")
    tags = []
    for tag, kws in INDUSTRY_KW.items():
        if any(k in t for k in kws): tags.append(tag)
    for tag, kws in TYPE_KW.items():
        if any(k in t for k in kws): tags.append(tag); break
    reg = None
    for tag, kws in REGION_KW.items():
        if any(k in t for k in kws): reg = tag; break
    tags.append(reg or "region/global")
    # de-dup, keep order, cap 5
    out = []
    for x in tags:
        if x not in out: out.append(x)
    return out[:5] or ["type/other"]

# ---------- helpers ----------
def slugify(title, used):
    s = re.sub(r'[\\/:\*\?"<>\|\n\r\t]+', " ", title).strip()
    s = re.sub(r"\s+", " ", s).strip(" .")
    if len(s) > 118: s = s[:118].rstrip()
    if not s: s = "untitled"
    base = s; i = 2
    while s.lower() in used:
        s = f"{base} ({i})"; i += 1
    used.add(s.lower())
    return s

def yaml_str(s):
    return '"' + str(s).replace('\\','\\\\').replace('"','\\"') + '"'

def load_cache():
    cache = {}
    with open("state/source_cache.jsonl") as f:
        for line in f:
            try:
                r = json.loads(line); cache[r["url"]] = r
            except Exception: pass
    return cache

def build_note(s, title, urls, tags, cache, retrieved):
    sid = s["id"]; date = s.get("date",""); ym = (date or "")[:7]
    chans = s.get("channels") or []
    # split sources into with-text vs link-only
    with_text, link_only = [], []
    seen = set()
    for u in urls:
        if u in seen: continue
        seen.add(u)
        r = cache.get(u)
        dom = (r.get("domain") if r else "") or host(u)
        if r and r.get("status")=="ok" and (r.get("word_count") or 0) >= 50 and not is_blocked(dom):
            with_text.append((u, r))
        else:
            link_only.append(u)
    # frontmatter
    fm = ["---"]
    fm.append(f"title: {yaml_str(title)}")
    fm.append(f"date: {date}")
    fm.append(f"retrieved: {retrieved}")   # day the story was ingested into the pipeline (≠ event date)
    fm.append("tags:")
    for t in tags: fm.append(f"  - {t}")
    fm.append("sources:")
    for u,_ in with_text: fm.append(f"  - {u}")
    for u in link_only: fm.append(f"  - {u}")
    fm.append(f"status: {'tagged' if tags and not tags[0].startswith('type/other') else 'untagged'}")
    fm.append(f"n_mentions: {s.get('n_mentions',0)}")
    fm.append("channels:")
    for c in chans: fm.append(f"  - {yaml_str(c)}")
    fm.append(f"story_id: {sid}")
    fm.append(f"month: {ym}")
    fm.append("enriched: false")
    fm.append("---")
    # body
    b = []
    b.append(f"# {title}\n")
    b.append(f"> [!info] {date} · {s.get('n_mentions',0)} упоминаний · {len(with_text)} источника(ов) с текстом")
    b.append(f"> Каналы: {', '.join(chans) if chans else '—'}\n")
    b.append("## Агрегированный текст (из дайджестов)\n")
    b.append((s.get("agg_text") or "").strip() + "\n")
    b.append("## Первоисточники\n")
    if with_text:
        for u, r in with_text:
            dom = r.get("domain") or ""
            txt = (r.get("text") or "").strip()
            if len(txt) > MAXSRC: txt = txt[:MAXSRC].rstrip() + "\n\n[…текст обрезан…]"
            b.append(f"### {dom}")
            b.append(f"<{u}>")
            b.append(f"*{r.get('word_count','?')} слов · {r.get('method','?')}*\n")
            b.append(txt + "\n")
    else:
        b.append("_(нет загруженного полного текста первоисточника)_\n")
    if link_only:
        b.append("### Прочие ссылки (без извлечённого текста)\n")
        for u in link_only: b.append(f"- <{u}>")
        b.append("")
    # enrichment placeholders (indexed via HTML-comment markers)
    b.append("## Контекст\n\n<!-- enrichment:context -->\n_(пусто — заполняется при обогащении)_\n<!-- /enrichment:context -->\n")
    b.append("## Челлендж / ред-тим\n\n<!-- enrichment:challenge -->\n_(пусто)_\n<!-- /enrichment:challenge -->\n")
    b.append("## Связь с постом\n\n<!-- enrichment:post -->\n_(пусто)_\n<!-- /enrichment:post -->\n")
    b.append("## Market Research\n\n<!-- enrichment:market_research -->\n_(пусто)_\n<!-- /enrichment:market_research -->\n")
    b.append("## Earnings Review\n\n<!-- enrichment:earnings_review -->\n_(пусто)_\n<!-- /enrichment:earnings_review -->\n")
    return "\n".join(fm) + "\n\n" + "\n".join(b)

ENRICH_SECTIONS = ["context", "challenge", "post", "market_research", "earnings_review"]
PLACEHOLDERS = {"", "_(пусто)_", "_(пусто — заполняется при обогащении)_"}

def _between(text, name):
    """Body between paired anchors <!-- enrichment:NAME --> ... <!-- /enrichment:NAME -->."""
    s, e = f"<!-- enrichment:{name} -->", f"<!-- /enrichment:{name} -->"
    if s not in text or e not in text:
        return None
    return text.split(s, 1)[1].split(e, 1)[0].strip("\n")

def _existing_sid(path):
    try:
        with open(path) as fh:
            for line in fh:
                if line.startswith("story_id:"):
                    return line.split(":", 1)[1].strip()
                if line.startswith("# "):
                    break
    except Exception:
        pass
    return None

def splice_enrichment(new_note, old_text):
    """Carry over any non-empty enrichment section from an existing note into the rebuilt one."""
    for name in ENRICH_SECTIONS:
        old_body = _between(old_text, name)
        if old_body is None or old_body.strip() in PLACEHOLDERS:
            continue
        new_body = _between(new_note, name)
        if new_body is None:
            continue
        s, e = f"<!-- enrichment:{name} -->", f"<!-- /enrichment:{name} -->"
        new_note = new_note.replace(f"{s}\n{new_body}\n{e}", f"{s}\n{old_body}\n{e}", 1)
    return new_note

def _carry_fm_line(new_note, old_text, key):
    """Preserve a frontmatter line (e.g. `retrieved`) from the existing note on full regen."""
    m = re.search(rf'^{re.escape(key)}: .*$', old_text, re.M)
    return re.sub(rf'^{re.escape(key)}: .*$', m.group(0), new_note, count=1, flags=re.M) if m else new_note

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    target = sys.argv[1]
    limit = None; only_ids = None; dry = "--dry" in sys.argv; only_new = "--only-new" in sys.argv
    if "--limit" in sys.argv: limit = int(sys.argv[sys.argv.index("--limit")+1])
    if "--ids" in sys.argv: only_ids = set(sys.argv[sys.argv.index("--ids")+1].split(","))
    months = sorted(glob.glob("months/*/stories.json")) if target=="all" else [f"months/{target}/stories.json"]
    cache = load_cache()
    total=0; wrote=0; notext=0; skipped=0
    for sf in months:
        ym = sf.split("/")[1]
        stories = json.load(open(sf))
        titles = json.load(open(f"months/{ym}/titles.json")) if os.path.exists(f"months/{ym}/titles.json") else {}
        extra  = json.load(open(f"months/{ym}/extra.json"))  if os.path.exists(f"months/{ym}/extra.json")  else {}
        tagmap = json.load(open(f"months/{ym}/tags.json"))   if os.path.exists(f"months/{ym}/tags.json")   else {}
        outdir = os.path.join(NEWS, ym); used=set()
        if not dry: os.makedirs(outdir, exist_ok=True)
        for s in stories:
            if not s.get("is_news"): continue
            sid = s["id"]
            if only_ids and sid not in only_ids: continue
            total += 1
            title = (titles.get(sid) or s.get("title_auto") or "untitled").strip()
            urls = list(dict.fromkeys((s.get("candidate_links") or []) + (extra.get(sid) or [])))
            tags = tagmap.get(sid) or heuristic_tags((title+" "+(s.get("agg_text") or "")))
            note = build_note(s, title, urls, tags, cache, dt.date.today().isoformat())
            fname = slugify(title, used) + ".md"
            path = os.path.join(outdir, fname)
            # a different story already owns this filename -> disambiguate with a short id
            if os.path.exists(path) and _existing_sid(path) not in (None, sid):
                fname = slugify(f"{title} ({sid[:6]})", used) + ".md"
                path = os.path.join(outdir, fname)
            if not any(cache.get(u,{}).get("status")=="ok" for u in urls): notext += 1
            if dry:
                if total <= 3: print("---- WOULD WRITE:", path, "\n", note[:1200], "\n...")
            else:
                if os.path.exists(path):
                    if only_new:
                        skipped += 1
                        continue
                    old_text = open(path).read()
                    note = splice_enrichment(note, old_text)               # keep [2]/[3] work
                    note = _carry_fm_line(note, old_text, "retrieved")     # keep original ingest day
                open(path, "w").write(note)
            wrote += 1
            if limit and wrote>=limit: break
        if limit and wrote>=limit: break
    print(f"news stories seen: {total} | notes written: {wrote} | skipped existing: {skipped} | without source text: {notext}")

if __name__ == "__main__":
    main()
