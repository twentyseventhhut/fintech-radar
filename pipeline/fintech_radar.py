#!/usr/bin/env python3
"""
fintech_radar.py — multi-source fintech news collector (full-text edition).

For every configured source it enumerates *all* posts in a time window
(using sitemaps / archive APIs / the WordPress REST API rather than capped
RSS feeds), fetches the full body of each post, extracts the plain text plus
the primary-source links embedded inside it, tags the post's section, and
writes a CSV (plus JSON + a Markdown digest).

Source mechanisms (chosen for completeness over RSS feed caps):
  - sitemap  : beehiiv & Ghost sites -> sitemap.xml -> fetch each post page
  - substack : /api/v1/archive (list) + /api/v1/posts/{slug} (full body_html)
  - wp_api   : WordPress REST API /wp-json/wp/v2/posts (content.rendered)
  - gnews    : Google News RSS proxy (headlines only; site is bot-blocked)

Pure standard library + `curl`.

Usage:
    python3 fintech_radar.py fetch  --since 30          # all sources, last 30 days
    python3 fintech_radar.py fetch  --since 2026-05-01 --only twif ctd
    python3 fintech_radar.py csv    --since 30          # rebuild CSV from the DB
    python3 fintech_radar.py digest --since 30
    python3 fintech_radar.py sources
"""

from __future__ import annotations  # Python 3.9: lazy annotations (X | None, tuple[...])

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from urllib.parse import urlparse, urlunparse
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
DIGEST_DIR = os.path.join(ROOT, "digests")
STATE_DIR = os.path.join(ROOT, "state")
DB_PATH = os.path.join(DATA_DIR, "items.jsonl")
CONFIG_PATH = os.path.join(ROOT, "sources.json")

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

UTC = dt.timezone.utc
CONTENT_CAP = 60000      # max chars of body text stored per item
SOURCE_TEXT_CAP = 14000  # max chars of fetched primary-source text
POLITE = 0.35            # delay between post fetches (seconds)
JINA_DELAY = 3.2         # delay after each r.jina.ai call (keyless ~20 rpm)
JINA_PREFIX = "https://r.jina.ai/"
SOURCE_CACHE = os.path.join(STATE_DIR, "source_cache.jsonl")


def now_utc() -> dt.datetime:
    return dt.datetime.now(UTC)


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------
# Networking
# --------------------------------------------------------------------------

def fetch(url: str, timeout: int = 45) -> tuple[int, str]:
    """Fetch a URL via curl. Returns (http_status, body). status 0 == failure."""
    try:
        proc = subprocess.run(
            ["curl", "-sSL", "--compressed", "-m", str(timeout), "--retry", "2",
             "--retry-delay", "2", "-A", UA,
             "-H", "Accept: text/html,application/xhtml+xml,application/json,application/xml;q=0.9,*/*;q=0.8",
             "-H", "Accept-Language: en-US,en;q=0.9",
             "-w", "\n%{http_code}", url],
            capture_output=True, text=True, errors="replace", timeout=timeout + 15,
        )
    except subprocess.TimeoutExpired:
        log(f"    ! timeout: {url}")
        return 0, ""
    body, _, code = proc.stdout.rpartition("\n")
    try:
        status = int(code.strip())
    except ValueError:
        status = 0
    return status, body


def fetch_json(url: str, timeout: int = 45):
    st, body = fetch(url, timeout)
    if st != 200:
        return st, None
    try:
        return st, json.loads(body)
    except json.JSONDecodeError:
        return st, None


# --------------------------------------------------------------------------
# Dates
# --------------------------------------------------------------------------

def parse_date(s: str) -> dt.datetime | None:
    if not s:
        return None
    s = s.strip()
    try:
        d = parsedate_to_datetime(s)
        if d is not None:
            return d.astimezone(UTC) if d.tzinfo else d.replace(tzinfo=UTC)
    except (TypeError, ValueError, IndexError):
        pass
    iso = s.replace("Z", "+00:00")
    for candidate in (iso, iso[:19], iso[:10]):
        try:
            d = dt.datetime.fromisoformat(candidate)
            return d.astimezone(UTC) if d.tzinfo else d.replace(tzinfo=UTC)
        except ValueError:
            continue
    return None


# --------------------------------------------------------------------------
# HTML extraction: plain text + links within a container
# --------------------------------------------------------------------------

VOID = {"br", "img", "input", "meta", "hr", "source", "area", "base", "col",
        "embed", "link", "param", "track", "wbr"}


BLOCK_BOUNDARY = {"p", "li", "h1", "h2", "h3", "h4", "h5", "blockquote"}


class ArticleExtractor(HTMLParser):
    """Collect visible text and <a href> links inside a target container.

    Produces three things:
      - full plain text of the container,
      - the flat list of all links,
      - `blocks`: per-paragraph/list-item segments as (text, links) — used to
        index the individual news items inside a roundup-style post.

    The container is selected by element id or by a class token. If neither is
    given, the whole document body is captured (use when the HTML *is* the body,
    e.g. WP content.rendered or Substack body_html).
    """
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "tr",
             "section", "article", "blockquote", "figure", "ul", "ol"}
    SKIP = {"script", "style", "noscript", "svg", "form", "button"}

    def __init__(self, want_id=None, want_class=None):
        super().__init__(convert_charrefs=True)
        self.want_id = want_id
        self.want_class = want_class
        self.parts: list[str] = []
        self.links: list[str] = []
        self.blocks: list[tuple] = []
        self._cur_text: list[str] = []
        self._cur_links: list[str] = []
        self.capture = want_id is None and want_class is None
        self.cap_depth = None
        self.depth = 0
        self.skip = 0

    def _matches(self, attrs) -> bool:
        d = dict(attrs)
        if self.want_id and d.get("id") == self.want_id:
            return True
        if self.want_class:
            return self.want_class in (d.get("class") or "").split()
        return False

    def _flush_block(self):
        t = re.sub(r"[ \t]+", " ", html.unescape("".join(self._cur_text))).strip()
        if t:
            self.blocks.append((t, list(self._cur_links)))
        self._cur_text = []
        self._cur_links = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
            return
        if tag not in VOID:
            self.depth += 1
        if not self.capture and (self.want_id or self.want_class) and self._matches(attrs):
            self.capture = True
            self.cap_depth = self.depth
        if self.capture and not self.skip:
            if tag in BLOCK_BOUNDARY:
                self._flush_block()
            if tag in self.BLOCK:
                self.parts.append("\n")
            if tag == "a":
                href = dict(attrs).get("href", "")
                if href:
                    self.links.append(href)
                    self._cur_links.append(href)

    def handle_startendtag(self, tag, attrs):
        if self.capture and not self.skip and tag == "br":
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
            return
        if tag not in VOID:
            self.depth -= 1
            if self.capture and self.cap_depth is not None and self.depth < self.cap_depth:
                self._flush_block()
                self.capture = False

    def handle_data(self, data):
        if self.capture and not self.skip and data.strip():
            self.parts.append(data)
            self._cur_text.append(data)

    def finalize(self):
        self._flush_block()

    def text(self) -> str:
        raw = html.unescape("".join(self.parts))
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n[ \t]+", "\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def extract_article(html_text, *, container_id=None, container_class=None):
    """Return (plain_text, raw_links, blocks) from an HTML fragment/page.

    blocks is a list of (segment_text, [hrefs]) — one entry per paragraph/list
    item, used downstream to index individual news items and their sources.
    """
    p = ArticleExtractor(want_id=container_id, want_class=container_class)
    try:
        p.feed(html_text)
        p.finalize()
    except Exception:
        txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_text)).strip()
        links = re.findall(r'href="(https?://[^"]+)"', html_text)
        return txt, links, []
    return p.text(), p.links, p.blocks


def blocks_to_news_items(blocks, own_host):
    """Each link-bearing block becomes an indexed news item with its sources."""
    out = []
    for text, raw_links in blocks:
        if len(text) <= 15 or BOILERPLATE.search(text):
            continue
        links = filter_source_links(raw_links, own_host)
        if links:
            out.append({"text": text[:800], "links": links})
    return out


# --------------------------------------------------------------------------
# Source-link filtering (keep primary sources, drop nav/social/images)
# --------------------------------------------------------------------------

SOCIAL_HOSTS = {
    "x.com", "twitter.com", "t.co", "linkedin.com", "lnkd.in", "facebook.com",
    "instagram.com", "bsky.app", "threads.net", "t.me", "telegram.me",
    "youtube.com", "youtu.be", "reddit.com", "mastodon.social", "wa.me",
    "whatsapp.com", "pinterest.com", "tiktok.com",
}
UTIL_SUBSTR = [
    "substackcdn.com", "media.beehiiv.com", "/subscribe", "/sponsor",
    "hsforms.com", "share.hsforms.com", "hubs.li", "/forms/", "forms.gle",
    "docs.google.com", "notion.site", "typeform.com", "calendly.com",
    "mailchi.mp", "/unsubscribe", "/privacy", "/terms", "/cdn-cgi/",
    "beehiiv.com/p/", "substack.com/app", "substack.com/sign",
    "substack.com/subscribe", "/account", "javascript:",
]

BOILERPLATE = re.compile(
    r"welcome to the new readers|cover image by|we.{0,3}re (looking|hiring)|"
    r"founding account|join the team|refer a friend|book a (demo|call)|"
    r"forwarded this email|read this email in your browser|"
    r"upgrade to paid|become a (paid|premium)|"
    r"brought to you by|sponsored by|in partnership with|our friends at|"
    r"want to sponsor|see what you can build|sponsor this newsletter|"
    r"today.{0,5}s (newsletter|edition) is|a word from our", re.I)
IMG_EXT = re.compile(r"\.(png|jpe?g|gif|webp|svg|ico|mp4|mp3|pdf|avif)(\?|#|$)", re.I)


def _host(u: str) -> str:
    try:
        h = urlparse(u).netloc.lower()
        return h[4:] if h.startswith("www.") else h
    except ValueError:
        return ""


def filter_source_links(links, own_host: str):
    """Keep external primary-source links; drop self/social/image/util links."""
    own = own_host.lower()
    if own.startswith("www."):
        own = own[4:]
    out, seen = [], set()
    for raw in links:
        u = html.unescape(raw or "").strip()
        if not u.lower().startswith("http"):
            continue
        host = _host(u)
        if not host:
            continue
        if host == own or host.endswith("." + own):
            continue
        if host in SOCIAL_HOSTS or any(host.endswith("." + s) for s in SOCIAL_HOSTS):
            continue
        if IMG_EXT.search(u):
            continue
        low = u.lower()
        if any(sub in low for sub in UTIL_SUBSTR):
            continue
        base = u.split("?")[0].split("#")[0]
        if base in seen:
            continue
        seen.add(base)
        out.append(base)
    return out


# --------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------

def section_of(source, title, url, extra=None):
    sid = source["id"]
    slug = (url or "").lower()
    t = (title or "").lower()
    extra = extra or {}
    if sid == "twif":
        for key, name in [("latam", "LatAm"), ("africa", "Africa"),
                          ("china", "China"), ("uk-eu", "UK/EU"),
                          ("-uk-", "UK/EU"), ("asia", "Asia"), ("india", "India"),
                          ("public-ledger", "The Public Ledger"),
                          ("middle-east", "Middle East"), ("mena", "MENA")]:
            if key in slug:
                return name
        if "exclusive" in t or "deep" in slug:
            return "Deep Dive"
        return "Weekly"
    if sid == "brainfood":
        return "Essay"
    if source["type"] == "substack":
        if extra.get("section_name"):
            return extra["section_name"]
        for p in ("Podcast", "Analysis", "DeFi", "Deep Dive", "Fintech", "Weekly"):
            if t.startswith(p.lower()):
                return p
        return "Newsletter"
    if extra.get("tag"):
        return extra["tag"]
    return "News"


# --------------------------------------------------------------------------
# Item model
# --------------------------------------------------------------------------

def canonical_url(url: str) -> str:
    try:
        p = urlparse(url.strip())
        return urlunparse((p.scheme or "https", p.netloc.lower(),
                           p.path.rstrip("/") or "/", "", "", ""))
    except ValueError:
        return url.strip()


def clean_inline(s: str) -> str:
    if not s:
        return ""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def make_item(source, url, title, published, *, author="", section="",
              summary="", content="", source_links=None, audience="",
              has_fulltext=True, news_items=None):
    cu = canonical_url(url)
    pub = published.astimezone(UTC) if published else None
    text = (content or "").strip()
    return {
        "id": hashlib.sha1(cu.encode("utf-8")).hexdigest()[:16],
        "source": source["name"],
        "source_id": source["id"],
        "section": section,
        "title": clean_inline(title) or "(untitled)",
        "url": url.strip(),
        "author": clean_inline(author) or source.get("author", ""),
        "published": pub.isoformat() if pub else "",
        "published_date": pub.strftime("%Y-%m-%d") if pub else "",
        "audience": audience,
        "has_fulltext": has_fulltext,
        "word_count": len(text.split()),
        "summary": clean_inline(summary)[:600],
        "content": text[:CONTENT_CAP],
        "source_links": source_links or [],
        "news_items": news_items or [],
        "fetched_at": now_utc().isoformat(),
    }


# --------------------------------------------------------------------------
# Collectors
# --------------------------------------------------------------------------

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
GHOST_EXCLUDE = ("/tag/", "/author/", "/page/", "/about", "/privacy", "/contact",
                 "/subscribe", "/membership", "/terms", "/sitemap", "/rss")


def sitemap_post_urls(xml_text, source):
    """Return [(loc, lastmod)] for post URLs, beehiiv (/p/) or Ghost (top-level)."""
    out = []
    try:
        root = ET.fromstring(xml_text.encode("utf-8"))
    except ET.ParseError as e:
        log(f"    ! sitemap parse error: {e}")
        return out
    ghost = bool(source.get("container_class"))
    base_host = source.get("host", "")
    for u in root.findall(f"{SITEMAP_NS}url"):
        loc = (u.findtext(f"{SITEMAP_NS}loc") or "").strip()
        lastmod = (u.findtext(f"{SITEMAP_NS}lastmod") or "").strip()
        if not loc:
            continue
        if ghost:
            path = urlparse(loc).path
            segs = [s for s in path.split("/") if s]
            if len(segs) != 1 or any(x in loc for x in GHOST_EXCLUDE):
                continue
            if base_host and base_host not in loc:
                continue
            out.append((loc, lastmod))
        else:
            if source.get("post_match", "/p/") in loc:
                out.append((loc, lastmod))
    return out


def collect_sitemap(source, since, db, max_per_source, refresh):
    urls = []
    for sm in source.get("sitemaps", []):
        st, xml_text = fetch(sm)
        if st != 200:
            log(f"    ! sitemap HTTP {st}: {sm}")
            continue
        urls += sitemap_post_urls(xml_text, source)
    # window by lastmod, newest first
    recent = []
    for loc, lastmod in urls:
        d = parse_date(lastmod)
        if d and d >= since:
            recent.append((d, loc))
    recent.sort(reverse=True)
    recent = recent[:max_per_source]
    log(f"    {len(recent)} posts in window")

    items = []
    for i, (d, loc) in enumerate(recent, 1):
        cu = canonical_url(loc)
        if not refresh and cu in db and db[cu].get("content"):
            items.append(db[cu])
            continue
        st, page = fetch(loc)
        if st != 200 or not page:
            log(f"    ! [{i}/{len(recent)}] HTTP {st}: {loc}")
            continue
        it = build_from_page(source, loc, page, d)
        items.append(it)
        db[cu] = it  # checkpoint into DB so a crash mid-run loses nothing
        if i % 40 == 0:
            save_db(db)
            log(f"    ... {i}/{len(recent)} fetched (db checkpoint)")
        elif i % 10 == 0:
            log(f"    ... {i}/{len(recent)} fetched")
        time.sleep(POLITE)
    return items


def build_from_page(source, url, page, fallback_date):
    """Build an item from a fetched HTML post page (beehiiv or Ghost)."""
    title = _meta(page, "og:title") or _meta(page, "twitter:title")
    summary = _meta(page, "og:description") or _meta(page, "description")
    author = _meta(page, "author")
    # date
    date_s = (re.search(r'"datePublished":"([^"]+)"', page) or
              re.search(r'property="article:published_time" content="([^"]+)"', page))
    pub = parse_date(date_s.group(1)) if date_s else fallback_date
    # ghost tag (section)
    extra = {}
    mtag = re.search(r'class="gh-article[^"]*?\btag-([a-z0-9-]+)', page)
    if mtag:
        extra["tag"] = mtag.group(1).replace("-", " ").title()
    text, links, blocks = extract_article(
        page, container_id=source.get("container_id"),
        container_class=source.get("container_class"))
    low = text.lower()
    gated = (len(text) < 120 or "subscribers only" in low
             or "for paid subscribers" in low or "already have an account" in low)
    audience = "members-only" if gated else ""
    news_items = [] if gated else blocks_to_news_items(blocks, source.get("host", ""))
    if gated:
        text = clean_inline(summary)  # use the public teaser instead of paywall boilerplate
        links = []
    return make_item(
        source, url, html.unescape(title or url), pub,
        author=author, section=section_of(source, title, url, extra),
        summary=html.unescape(summary or ""), content=text,
        source_links=filter_source_links(links, source.get("host", "")),
        audience=audience, has_fulltext=not gated, news_items=news_items,
    )


def _meta(page, key):
    m = (re.search(rf'<meta property="{re.escape(key)}" content="([^"]*)"', page) or
         re.search(rf'<meta name="{re.escape(key)}" content="([^"]*)"', page))
    return m.group(1) if m else ""


def collect_substack(source, since, db, max_per_source, refresh):
    base = source["base"].rstrip("/")
    listed, offset = [], 0
    while offset < 1500:
        st, arr = fetch_json(f"{base}/api/v1/archive?sort=new&limit=50&offset={offset}")
        if st != 200 or not arr:
            break
        stop = False
        for it in arr:
            d = parse_date(it.get("post_date", ""))
            if d and d < since:
                stop = True
                continue
            listed.append(it)
        if stop:
            break
        offset += len(arr)  # advance by actual count — Substack's first page can be short
    listed = listed[:max_per_source]
    log(f"    {len(listed)} posts in window (archive API)")

    items = []
    for i, meta in enumerate(listed, 1):
        slug = meta.get("slug", "")
        url = meta.get("canonical_url") or f"{base}/p/{slug}"
        cu = canonical_url(url)
        if not refresh and cu in db and db[cu].get("content"):
            items.append(db[cu])
            continue
        st, post = fetch_json(f"{base}/api/v1/posts/{slug}")
        body = (post or {}).get("body_html") or ""
        text, links, blocks = extract_article(body)
        if not text:
            text = clean_inline(meta.get("truncated_body_text", ""))
        d = parse_date(meta.get("post_date", ""))
        audience = meta.get("audience", "")
        it = make_item(
            source, url, meta.get("title", ""), d,
            author=", ".join(b.get("name", "") for b in (post or {}).get("publishedBylines", []))
                   or source.get("author", ""),
            section=section_of(source, meta.get("title", ""), url,
                               {"section_name": meta.get("section_name")}),
            summary=meta.get("subtitle") or meta.get("description", ""),
            content=text,
            source_links=filter_source_links(links, source.get("host", "")),
            audience=audience,
            has_fulltext=(audience != "only_paid"),
            news_items=blocks_to_news_items(blocks, source.get("host", "")),
        )
        items.append(it)
        db[cu] = it  # checkpoint
        if i % 40 == 0:
            save_db(db)
            log(f"    ... {i}/{len(listed)} fetched (db checkpoint)")
        elif i % 10 == 0:
            log(f"    ... {i}/{len(listed)} fetched")
        time.sleep(POLITE)
    return items


def collect_wp_api(source, since, db, max_per_source, refresh):
    base = source["base"].rstrip("/")
    st, cats = fetch_json(f"{base}/wp-json/wp/v2/categories?slug={source['category_slug']}")
    if st != 200 or not cats:
        log(f"    ! WP categories HTTP {st}")
        return []
    cat_id = cats[0]["id"]
    after = since.strftime("%Y-%m-%dT%H:%M:%S")
    items, page = [], 1
    while page <= 10:
        url = (f"{base}/wp-json/wp/v2/posts?categories={cat_id}&per_page=100"
               f"&page={page}&after={after}&_fields=id,date_gmt,link,title,content,_links")
        st, arr = fetch_json(url)
        if st != 200 or not arr:
            break
        for p in arr:
            body = (p.get("content") or {}).get("rendered", "")
            text, links, blocks = extract_article(body)
            d = parse_date(p.get("date_gmt", "") + "Z")
            items.append(make_item(
                source, p.get("link", ""),
                (p.get("title") or {}).get("rendered", ""), d,
                section="News",
                content=text,
                source_links=filter_source_links(links, source.get("host", "")),
                news_items=blocks_to_news_items(blocks, source.get("host", "")),
            ))
        if len(arr) < 100:
            break
        page += 1
    log(f"    {len(items)} posts in window (WP REST API)")
    return items[:max_per_source]


def collect_gnews(source, since):
    days = max(1, (now_utc() - since).days + 1)
    url = source["url"].replace("{days}", str(days))
    st, xml_text = fetch(url)
    if st != 200:
        log(f"    ! gnews HTTP {st}")
        return []
    try:
        root = ET.fromstring(xml_text.encode("utf-8"))
    except ET.ParseError:
        return []
    items = []
    for e in root.findall(".//item"):
        title = e.findtext("title") or ""
        pub = parse_date(e.findtext("pubDate") or "")
        if pub and pub < since:
            continue
        clean_title = re.sub(r"\s+-\s+[^-]+$", "", title).strip() or title
        items.append(make_item(
            source, e.findtext("link") or "", clean_title, pub,
            section="News",
            author=e.findtext("source") or source.get("author", ""),
            summary=clean_inline(e.findtext("description") or ""),
            content="",  # site is bot-blocked; full text unavailable
            has_fulltext=False,
            audience="headline-only",
        ))
    log(f"    {len(items)} headlines (Google News; full text blocked by Incapsula)")
    return items


COLLECTORS = {
    "sitemap": collect_sitemap,
    "substack": collect_substack,
    "wp_api": collect_wp_api,
}


# --------------------------------------------------------------------------
# Database
# --------------------------------------------------------------------------

def load_db():
    db = {}
    if os.path.exists(DB_PATH):
        with open(DB_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    it = json.loads(line)
                except json.JSONDecodeError:
                    continue
                db[canonical_url(it["url"])] = it
    return db


def save_db(db):
    tmp = DB_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for it in sorted(db.values(), key=lambda x: x.get("published", ""), reverse=True):
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    os.replace(tmp, DB_PATH)


def window_items(db, since, until=None):
    items = []
    for it in db.values():
        if not it.get("published"):
            continue
        d = parse_date(it["published"])
        if d and d >= since and (until is None or d < until):
            items.append(it)
    items.sort(key=lambda x: x.get("published", ""), reverse=True)
    return items


def month_bounds(ym):
    """'2026-05' -> (2026-05-01, 2026-06-01) UTC."""
    y, m = map(int, ym.split("-"))
    start = dt.datetime(y, m, 1, tzinfo=UTC)
    end = dt.datetime(y + (m // 12), (m % 12) + 1, 1, tzinfo=UTC)
    return start, end


# --------------------------------------------------------------------------
# Outputs
# --------------------------------------------------------------------------

CSV_COLUMNS = ["date", "channel", "section", "title", "author", "url",
               "word_count", "has_fulltext", "audience", "content",
               "source_links", "num_source_links"]


def write_csv(items, path):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(CSV_COLUMNS)
        for it in items:
            links = it.get("source_links", [])
            w.writerow([
                it.get("published_date", ""),
                it.get("source", ""),
                it.get("section", ""),
                it.get("title", ""),
                it.get("author", ""),
                it.get("url", ""),
                it.get("word_count", 0),
                "yes" if it.get("has_fulltext", True) else "no",
                it.get("audience", ""),
                it.get("content", ""),
                "\n".join(links),
                len(links),
            ])
    return path


def write_digest(items, since, path):
    by_source = {}
    for it in items:
        by_source.setdefault(it["source"], []).append(it)
    today = now_utc().strftime("%Y-%m-%d")
    lines = [f"# Fintech Radar — дайджест",
             "",
             f"_Сгенерировано: {today} · окно с {since.strftime('%Y-%m-%d')} · "
             f"материалов: {len(items)}_", "",
             "| Источник | Постов | С полным текстом |", "| --- | ---: | ---: |"]
    for name in sorted(by_source, key=lambda n: -len(by_source[n])):
        grp = by_source[name]
        ft = sum(1 for x in grp if x.get("has_fulltext"))
        lines.append(f"| {name} | {len(grp)} | {ft} |")
    lines.append("")
    for name in sorted(by_source, key=lambda n: -len(by_source[n])):
        lines.append(f"## {name} ({len(by_source[name])})\n")
        for it in sorted(by_source[name], key=lambda x: x.get("published", ""), reverse=True):
            sec = f" · _{it['section']}_" if it.get("section") else ""
            nl = len(it.get("source_links", []))
            lines.append(f"- **[{it['title']}]({it['url']})** — {it.get('published_date','')}"
                         f"{sec} · {it.get('word_count',0)} слов · {nl} ссылок")
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


# --------------------------------------------------------------------------
# Primary-source text fetching (for the exploded, per-news-item CSV)
# --------------------------------------------------------------------------

def readability_lite(html_text: str) -> str:
    """Cheap readability: drop chrome, prefer <article>, join paragraph text."""
    h = re.sub(r"<(script|style|nav|header|footer|aside|form|figure|noscript)\b[^>]*>.*?</\1>",
               " ", html_text, flags=re.S | re.I)
    m = re.search(r"<article\b[^>]*>(.*?)</article>", h, flags=re.S | re.I)
    seg = m.group(1) if m else h
    paras = re.findall(r"<(p|h1|h2|h3|h4|li|blockquote)\b[^>]*>(.*?)</\1>",
                       seg, flags=re.S | re.I)
    text = "\n".join(re.sub(r"<[^>]+>", " ", body) for _, body in paras)
    return re.sub(r"[ \t]+", " ", html.unescape(text)).strip()


_jina_lock = threading.Lock()
_jina_last = [0.0]


def _jina_gate():
    """Serialize r.jina.ai calls across threads to stay under the keyless rate."""
    with _jina_lock:
        wait = JINA_DELAY - (time.monotonic() - _jina_last[0])
        if wait > 0:
            time.sleep(wait)
        _jina_last[0] = time.monotonic()


def fetch_jina(url: str) -> tuple[str, int]:
    st, body = fetch(JINA_PREFIX + url, 50)
    if st != 200 or not body:
        return "", st
    body = body.split("Markdown Content:", 1)[-1]
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)          # images
    body = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", body)       # links -> text
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body, st


def fetch_source_text(url: str) -> dict:
    """Direct readability first; fall back to r.jina.ai when thin/blocked."""
    domain = _host(url)
    st, page = fetch(url, 25)
    text = readability_lite(page) if (st == 200 and page) else ""
    method = "direct"
    if len(text.split()) < 150:  # too thin -> try the JS-rendering reader
        _jina_gate()
        jbody, _ = fetch_jina(url)
        if len(jbody.split()) > len(text.split()):
            text, method = jbody, "jina"
    text = text[:SOURCE_TEXT_CAP]
    wc = len(text.split())
    if wc >= 120 or len(text) >= 600:
        status = "ok"
    elif st in (401, 403, 429, 451, 0):
        status = "blocked"
    else:
        status = "thin"
    return {"url": url, "domain": domain, "status": status, "method": method,
            "word_count": wc, "text": text, "fetched_at": now_utc().isoformat()}


def load_source_cache() -> dict:
    cache = {}
    if os.path.exists(SOURCE_CACHE):
        with open(SOURCE_CACHE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                    cache[r["url"]] = r
                except (json.JSONDecodeError, KeyError):
                    continue
    return cache


def append_source_cache(rec: dict):
    with open(SOURCE_CACHE, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


ITEMS_CSV_COLUMNS = ["post_date", "channel", "section", "post_title", "post_url",
                     "item_index", "item_text", "source_url", "source_domain",
                     "source_status", "source_method", "source_word_count",
                     "source_text"]


def explode_rows(posts):
    """Flatten posts -> one row per (post, news-item index, source link)."""
    rows = []
    for post in posts:
        for idx, ni in enumerate(post.get("news_items", []), 1):
            for link in ni.get("links", []):
                rows.append((post, idx, ni.get("text", ""), link))
    return rows


def write_items_csv(rows, cache, path):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(ITEMS_CSV_COLUMNS)
        for post, idx, item_text, url in rows:
            rec = cache.get(url, {})
            w.writerow([
                post.get("published_date", ""), post.get("source", ""),
                post.get("section", ""), post.get("title", ""), post.get("url", ""),
                idx, item_text, url, rec.get("domain", _host(url)),
                rec.get("status", "pending"), rec.get("method", ""),
                rec.get("word_count", 0), rec.get("text", ""),
            ])
    return path


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def resolve_since(value: str) -> dt.datetime:
    value = (value or "30").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return dt.datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=UTC)
    return now_utc() - dt.timedelta(days=int(value))


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def cmd_fetch(args):
    cfg = load_config()
    since = resolve_since(args.since)
    log(f"Collecting since {since.strftime('%Y-%m-%d %H:%M UTC')}")
    db = load_db()
    collected = []
    for source in cfg["sources"]:
        if args.only and source["id"] not in args.only:
            continue
        log(f"→ {source['name']} [{source['type']}]")
        t = source["type"]
        if t == "gnews":
            got = collect_gnews(source, since)
        elif t in COLLECTORS:
            got = COLLECTORS[t](source, since, db, args.max_per_source, args.refresh)
        else:
            log(f"    ! unknown type {t}")
            got = []
        exc = [k.lower() for k in source.get("exclude_keywords", [])]
        if exc:
            before = len(got)
            got = [it for it in got
                   if not any(k in (it["title"] + " " + it["summary"]).lower() for k in exc)]
            if before != len(got):
                log(f"    keyword filter: {before} → {len(got)}")
        log(f"    collected {len(got)}")
        collected.extend(got)

    new = 0
    for it in collected:
        cu = canonical_url(it["url"])
        if cu not in db:
            new += 1
        db[cu] = it
    save_db(db)

    wi = window_items(db, since)
    stamp = now_utc().strftime("%Y-%m-%d")
    json_path = os.path.join(DATA_DIR, f"items-{stamp}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(wi, f, ensure_ascii=False, indent=2)
    csv_path = write_csv(wi, os.path.join(DATA_DIR, f"fintech-radar-{stamp}.csv"))
    digest_path = write_digest(wi, since, os.path.join(DIGEST_DIR, f"digest-{stamp}.md"))

    ft = sum(1 for x in wi if x.get("has_fulltext"))
    log("")
    log(f"✓ collected {len(collected)} ({new} new) · window has {len(wi)} items "
        f"({ft} with full text)")
    log(f"✓ CSV    → {csv_path}")
    log(f"✓ JSON   → {json_path}")
    log(f"✓ digest → {digest_path}")
    print(csv_path)


def cmd_csv(args):
    since = resolve_since(args.since)
    wi = window_items(load_db(), since)
    stamp = now_utc().strftime("%Y-%m-%d")
    path = write_csv(wi, os.path.join(DATA_DIR, f"fintech-radar-{stamp}.csv"))
    log(f"✓ CSV ({len(wi)} items) → {path}")
    print(path)


def cmd_digest(args):
    since = resolve_since(args.since)
    wi = window_items(load_db(), since)
    stamp = now_utc().strftime("%Y-%m-%d")
    path = write_digest(wi, since, os.path.join(DIGEST_DIR, f"digest-{stamp}.md"))
    log(f"✓ digest ({len(wi)} items) → {path}")
    print(path)


def cmd_expand(args):
    """Explode posts into per-news-item rows and fetch each primary source."""
    if getattr(args, "month", None):
        since, until = month_bounds(args.month)
    else:
        since, until = resolve_since(args.since), None
    posts = window_items(load_db(), since, until)
    if args.only:
        posts = [p for p in posts if p["source_id"] in args.only]
    rows = explode_rows(posts)
    cache = load_source_cache()
    uniq = list(dict.fromkeys(u for *_, u in rows))
    if args.refresh_sources:
        todo = list(uniq)
    else:
        todo = [u for u in uniq if u not in cache or cache[u].get("status") == "blocked"]
    if args.limit:
        todo = todo[:args.limit]
    log(f"{len(rows)} item-links across {len(posts)} posts · {len(uniq)} unique sources "
        f"· {len(uniq) - len(todo)} cached · {len(todo)} to fetch (workers={args.workers})")

    cache_lock = threading.Lock()
    done = [0]
    def work(u):
        rec = fetch_source_text(u)
        with cache_lock:
            cache[u] = rec
            append_source_cache(rec)
            done[0] += 1
            if done[0] % 20 == 0 or done[0] == len(todo):
                ok = sum(1 for r in cache.values() if r.get("status") == "ok")
                log(f"  {done[0]}/{len(todo)} fetched · ok so far: {ok}")
        return rec
    if todo:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for _ in as_completed([ex.submit(work, u) for u in todo]):
                pass

    stamp = now_utc().strftime("%Y-%m-%d")
    path = write_items_csv(rows, cache, os.path.join(DATA_DIR, f"fintech-radar-items-{stamp}.csv"))
    got = sum(1 for *_, u in rows if cache.get(u, {}).get("status") == "ok")
    log("")
    log(f"✓ {len(rows)} item rows · {got} with full source text "
        f"· {len(uniq)} unique sources")
    log(f"✓ items CSV → {path}")
    print(path)


def cmd_brief(args):
    """Readable Markdown brief: each post's news items + their source-text snippets."""
    since = resolve_since(args.since)
    posts = window_items(load_db(), since)
    if args.only:
        posts = [p for p in posts if p["source_id"] in args.only]
    cache = load_source_cache()
    total_items = sum(len(p.get("news_items", [])) for p in posts)
    by_source = {}
    for p in posts:
        by_source.setdefault(p["source"], []).append(p)
    today = now_utc().strftime("%Y-%m-%d")
    with_text = 0
    lines = ["# Fintech Radar — недельный обзор",
             f"_{since.strftime('%Y-%m-%d')} → {today} · {len(posts)} постов · "
             f"{total_items} новостей внутри них_", ""]
    for name in sorted(by_source, key=lambda n: -len(by_source[n])):
        lines.append(f"\n## {name}\n")
        for p in sorted(by_source[name], key=lambda x: x.get("published", ""), reverse=True):
            nis = p.get("news_items", [])
            if not nis:
                continue
            lines.append(f"### {p['published_date']} · {p.get('section','')} — "
                         f"[{p['title']}]({p['url']})\n")
            for ni in nis:
                blurb = re.sub(r"\s+", " ", ni.get("text", "")).strip()
                lines.append(f"- **{blurb[:260]}**")
                for link in ni.get("links", []):
                    rec = cache.get(link, {})
                    dom = rec.get("domain", _host(link))
                    status = rec.get("status", "pending")
                    txt = re.sub(r"\s+", " ", rec.get("text", "") or "").strip()
                    if status == "ok" and txt:
                        with_text += 1
                        lines.append(f"    - 🔗 [{dom}]({link}) — {txt[:args.snippet]}…")
                    else:
                        lines.append(f"    - 🔗 [{dom}]({link}) — _(первоисточник: {status})_")
            lines.append("")
    path = os.path.join(DIGEST_DIR, f"week-brief-{today}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log(f"✓ brief: {len(posts)} posts · {total_items} news items · "
        f"{with_text} with source text → {path}")
    print(path)


def cmd_context(args):
    """Internal corpus retrieval: every prior mention of given terms across ALL
    collected periods — the company, its competitors and analogous events. Feeds
    the context-enrichment / synthesis stage."""
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]
    db = load_db()
    cache = load_source_cache()
    allitems = sorted(db.values(), key=lambda x: x.get("published", ""))
    dates = [p["published_date"] for p in allitems if p.get("published_date")]
    span = f"{dates[0]}…{dates[-1]}" if dates else "—"
    out = ["# Внутренний контекст-пак (свой корпус, все периоды)",
           f"_термины: {', '.join(terms)} · корпус: {len(allitems)} постов · "
           f"период {span}_", ""]
    as_json = {"span": span, "corpus": len(allitems), "terms": {}}
    for term in terms:
        tl = term.lower()
        hits = []
        for p in allitems:
            nis = [ni for ni in p.get("news_items", []) if tl in ni.get("text", "").lower()]
            # also catch cached primary-source texts that mention the term
            src_hit = any(tl in (cache.get(l, {}).get("text", "") or "").lower()
                          for ni in p.get("news_items", []) for l in ni.get("links", []))
            if nis:
                for ni in nis:
                    hits.append((p, ni))
            elif tl in p.get("title", "").lower() or tl in p.get("content", "").lower() or src_hit:
                hits.append((p, None))
        seen, uniq = set(), []
        for p, ni in hits:
            k = (p["url"], (ni or {}).get("text", "")[:60])
            if k in seen:
                continue
            seen.add(k)
            uniq.append((p, ni))
        uniq.sort(key=lambda x: x[0].get("published", ""))
        out.append(f"\n## «{term}» — {len(uniq)} упоминаний в корпусе\n")
        rec = []
        for p, ni in uniq[-args.limit:]:
            blurb = re.sub(r"\s+", " ", (ni["text"] if ni else p.get("summary", "")))[:200]
            link = (ni["links"][0] if ni and ni.get("links") else p.get("url", ""))
            cached = "✓" if (link in cache and cache[link].get("status") == "ok") else " "
            out.append(f"- {p['published_date']} · {p['source']} · _{p.get('section','')}_ "
                       f"— {blurb} [{_host(link)}]({link}) {cached}")
            rec.append({"date": p["published_date"], "source": p["source"],
                        "section": p.get("section", ""), "blurb": blurb, "link": link,
                        "source_text_cached": cached == "✓"})
        as_json["terms"][term] = rec
    stamp = now_utc().strftime("%Y-%m-%d")
    md_path = os.path.join(DIGEST_DIR, f"context-{stamp}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    if args.json:
        with open(os.path.join(DATA_DIR, f"context-{stamp}.json"), "w", encoding="utf-8") as f:
            json.dump(as_json, f, ensure_ascii=False, indent=2)
    log(f"✓ context pack ({len(terms)} terms) → {md_path}")
    print(md_path)


def cmd_sources(args):
    for s in load_config()["sources"]:
        extra = f"  (LinkedIn: {s['linkedin']})" if s.get("linkedin") else ""
        loc = s.get("base") or (s.get("sitemaps") or [s.get("url", "")])[0]
        print(f"- {s['name']:46s} [{s['type']:8s}] {loc}{extra}")


def main():
    for d in (DATA_DIR, DIGEST_DIR, STATE_DIR):
        os.makedirs(d, exist_ok=True)
    ap = argparse.ArgumentParser(description="Fintech news multi-source collector")
    sub = ap.add_subparsers(dest="cmd")
    pf = sub.add_parser("fetch")
    pf.add_argument("--since", default="30")
    pf.add_argument("--only", nargs="*")
    pf.add_argument("--refresh", action="store_true")
    pf.add_argument("--max-per-source", type=int, default=200)
    pf.set_defaults(func=cmd_fetch)
    pc = sub.add_parser("csv")
    pc.add_argument("--since", default="30")
    pc.set_defaults(func=cmd_csv)
    pe = sub.add_parser("expand", help="explode posts into news items + fetch source text")
    pe.add_argument("--since", default="30")
    pe.add_argument("--month", help="YYYY-MM (overrides --since with that calendar month)")
    pe.add_argument("--only", nargs="*")
    pe.add_argument("--limit", type=int, default=0, help="cap sources fetched this run")
    pe.add_argument("--workers", type=int, default=12, help="parallel source fetchers")
    pe.add_argument("--refresh-sources", action="store_true")
    pe.set_defaults(func=cmd_expand)
    pd = sub.add_parser("digest")
    pd.add_argument("--since", default="30")
    pd.set_defaults(func=cmd_digest)
    pb = sub.add_parser("brief", help="readable Markdown brief with source-text snippets")
    pb.add_argument("--since", default="7")
    pb.add_argument("--only", nargs="*")
    pb.add_argument("--snippet", type=int, default=600)
    pb.set_defaults(func=cmd_brief)
    px = sub.add_parser("context", help="internal corpus retrieval for a set of terms")
    px.add_argument("--terms", required=True, help="comma-separated: company, competitors, event keywords")
    px.add_argument("--limit", type=int, default=40, help="max mentions per term")
    px.add_argument("--json", action="store_true")
    px.set_defaults(func=cmd_context)
    ps = sub.add_parser("sources")
    ps.set_defaults(func=cmd_sources)
    args = ap.parse_args()
    if not args.cmd:
        args = ap.parse_args(["fetch"])
    args.func(args)


if __name__ == "__main__":
    main()
