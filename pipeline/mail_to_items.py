#!/usr/bin/env python3
"""mail_to_items.py — convert raw_news/<source>/*.json emails into items.jsonl posts.

Deterministic, stdlib-only. Each email → one post in the same schema the dedup pipeline
expects (source, published_date, content, news_items=[{text,links}], source_links, url...).
Idempotent: skips emails whose post id is already in items.jsonl. Appends new ones.

Env: RAW_DIR (default <repo>/raw_news), ITEMS_PATH (default <repo>/data/items.jsonl).
"""
import os, re, json, glob, hashlib, datetime as dt
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.environ.get("RAW_DIR", os.path.join(ROOT, "raw_news"))
ITEMS = os.environ.get("ITEMS_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "items.jsonl"))

BLOCK = {"p", "div", "td", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6",
         "section", "article", "blockquote", "br", "hr", "ul", "ol", "table"}
DROP_LINK = re.compile(r"(unsubscribe|list-manage|/subscribe|view.{0,12}browser|/preferences|"
                       r"mailto:|/privacy|/terms|twitter\.com|//x\.com|linkedin\.com|facebook\.com|"
                       r"instagram\.com|//t\.me|youtube\.com|whatsapp|\.(png|jpe?g|gif|svg|webp)(\?|$))", re.I)
BOILER = re.compile(r"unsubscribe|view (this|in|in your) browser|update your preferences|"
                    r"you (are |')?receiv|was sent to|forwarded this (email|message)|advertise with|"
                    r"all rights reserved|privacy policy|manage your subscription|©", re.I)


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.cur, self.links, self.href, self.skip = [], [], [], None, 0

    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        if text or self.links:
            self.blocks.append((text, list(dict.fromkeys(self.links))))
        self.cur, self.links = [], []

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "head"):
            self.skip += 1
        if tag in BLOCK:
            self._flush()
        if tag == "a":
            self.href = dict(attrs).get("href")

    def handle_endtag(self, tag):
        if tag in ("style", "script", "head") and self.skip:
            self.skip -= 1
        if tag == "a" and self.href:
            if self.href.startswith("http") and not DROP_LINK.search(self.href):
                self.links.append(self.href.split("?utm")[0])
            self.href = None
        if tag in BLOCK:
            self._flush()

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)

    def close(self):
        super().close(); self._flush()


def extract(html, text):
    p = Blocks()
    try:
        p.feed(html or ""); p.close()
    except Exception:
        pass
    blocks = p.blocks
    if not blocks and text:  # plaintext fallback
        blocks = [(ln.strip(), re.findall(r"https?://\S+", ln)) for ln in text.split("\n") if ln.strip()]
    news_items, all_links, content_parts = [], [], []
    for txt, links in blocks:
        if BOILER.search(txt or ""):
            continue
        if txt:
            content_parts.append(txt)
        links = [l for l in links if l.startswith("http") and not DROP_LINK.search(l)]
        all_links += links
        if links and len(txt) >= 45 and len(links) <= 3:
            news_items.append({"text": txt, "links": links})
    return content_parts, news_items, list(dict.fromkeys(all_links))


def load_existing_ids():
    ids = set()
    if os.path.exists(ITEMS):
        for line in open(ITEMS):
            try:
                ids.add(json.loads(line)["id"])
            except Exception:
                pass
    return ids


def main():
    os.makedirs(os.path.dirname(ITEMS), exist_ok=True)
    have = load_existing_ids()
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    added = 0
    with open(ITEMS, "a", encoding="utf-8") as out:
        for jf in sorted(glob.glob(os.path.join(RAW, "*", "*.json"))):
            try:
                e = json.load(open(jf))
            except Exception:
                continue
            pid = "mail-" + hashlib.sha1(e.get("message_id", jf).encode()).hexdigest()[:12]
            if pid in have:
                continue
            content_parts, news_items, links = extract(e.get("html", ""), e.get("text", ""))
            content = "\n\n".join(content_parts)
            # Telegram posts: mentions are built from news_items, and extract() only emits a
            # news_item for a block that has a link (≥45 chars, ≤3 links). A TG post may carry no
            # external link, or be a multi-link digest → 0 news_items → it would be silently
            # dropped. Guarantee at least one mention from the post's own content.
            if str(e.get("message_id", "")).startswith("tg-") and not news_items and content.strip():
                news_items = [{"text": content[:1000], "links": links[:3]}]
            post = {
                "id": pid,
                "source": e.get("source", e.get("source_slug", "unknown")),
                "source_id": e.get("source_slug", "unknown"),
                "url": e.get("tg_url") or f"email://{e.get('source_slug','unknown')}/{e.get('uid','')}",
                "title": e.get("subject", ""),
                "author": e.get("from_name", ""),
                "section": "",
                "audience": "public",
                "published": e.get("date", ""),
                "published_date": e.get("date", ""),
                "fetched_at": now,
                "content": content,
                "news_items": news_items,
                "source_links": links,
                "num_source_links": len(links),
                "word_count": len(content.split()),
                "has_fulltext": bool(content),
                "summary": "",
            }
            out.write(json.dumps(post, ensure_ascii=False) + "\n")
            have.add(pid); added += 1
    print(f"mail_to_items: +{added} new posts → {ITEMS} (total ids now {len(have)})")


if __name__ == "__main__":
    main()
