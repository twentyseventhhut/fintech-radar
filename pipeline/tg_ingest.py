#!/usr/bin/env python3
"""tg_ingest.py — pull new posts from PUBLIC Telegram channels into raw_news/<slug>/.

Scrapes the public web preview https://t.me/s/<username> (no API key, no login) and writes
each new post as raw_news/<slug>/<YYYY-MM-DD>_<msgid>.json in the SAME schema the email
ingest uses, so mail_to_items.py converts them into items.jsonl alongside the newsletters.
Deterministic, stdlib-only. Incremental via raw_news/.tg_state.json (per-channel high-water
message id). Each post = one news item (one block).

Channels: pipeline/tg_channels.json = {"channels": ["username1", "username2", ...]}
          (or {"channels": [{"username": "x", "slug": "y", "name": "Friendly"}]}).
Env: RAW_DIR (default <repo>/raw_news).
"""
import os, re, json, html, time, urllib.request, urllib.error
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.environ.get("RAW_DIR", os.path.join(ROOT, "raw_news"))
CHANNELS_CFG = os.path.join(ROOT, "pipeline", "tg_channels.json")
STATE = os.path.join(RAW, ".tg_state.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "unknown"


def load_json(p, default):
    try:
        return json.load(open(p))
    except Exception:
        return default


def fetch(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                        "Accept-Language": "ru,en;q=0.8"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError) as e:
            if i < retries - 1:
                time.sleep(2 * (i + 1)); continue
            print(f"  fetch failed: {url} — {e}")
            return None


class Channel(HTMLParser):
    """Parse a t.me/s/<user> page into [{id, date, text, html, links}] posts."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.posts, self.cur = [], None
        self.in_text = False
        self.depth = 0
        self._in_a = False

    def _flush(self):
        c = self.cur
        if c and c["id"] is not None:
            text = re.sub(r"[ \t]+\n", "\n", "".join(c["_t"])).strip()
            if text or c["links"]:
                c["text"] = text
                c["html"] = "<p>" + "".join(c["_h"]) + "</p>"
                c["links"] = list(dict.fromkeys(c["links"]))
                del c["_t"], c["_h"]
                self.posts.append(c)
        self.cur = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "div" and "data-post" in a:                 # message wrapper
            self._flush()
            mid = a["data-post"].rsplit("/", 1)[-1]
            self.cur = {"id": int(mid) if mid.isdigit() else None,
                        "date": "", "links": [], "_t": [], "_h": []}
            self.in_text = False
            return
        if self.cur is None:
            return
        if tag == "div" and "js-message_text" in cls:         # the post body
            self.in_text, self.depth = True, 0
            return
        if tag == "time" and a.get("datetime") and not self.cur["date"]:
            self.cur["date"] = a["datetime"][:10]
        if not self.in_text:
            return
        if tag == "div":
            self.depth += 1
        elif tag == "br":
            self.cur["_t"].append("\n"); self.cur["_h"].append("<br>")
        elif tag == "a":
            href = a.get("href", "")
            if href.startswith(("http://", "https://")):   # real external link, not a hashtag/relative
                self.cur["links"].append(href)
                self.cur["_h"].append('<a href="%s">' % html.escape(href, quote=True))
                self._in_a = True
            else:
                self._in_a = False

    def handle_endtag(self, tag):
        if not self.in_text or self.cur is None:
            return
        if tag == "a":
            if self._in_a:
                self.cur["_h"].append("</a>"); self._in_a = False
        elif tag == "div":
            if self.depth == 0:
                self.in_text = False
            else:
                self.depth -= 1

    def handle_data(self, data):
        if self.in_text and self.cur is not None:
            self.cur["_t"].append(data)
            self.cur["_h"].append(html.escape(data))

    def close(self):
        super().close(); self._flush()


def channel_title(page, username):
    m = re.search(r'<meta property="og:title" content="([^"]*)"', page or "")
    return html.unescape(m.group(1)).strip() if m else f"@{username}"


def normalize(entry):
    """Accept 'username' string or {username, slug?, name?} dict."""
    if isinstance(entry, str):
        u = entry.strip().lstrip("@")
        return {"username": u, "slug": slugify(u), "name": None}
    u = str(entry.get("username", "")).strip().lstrip("@")
    return {"username": u, "slug": entry.get("slug") or slugify(u), "name": entry.get("name")}


def main():
    cfg = load_json(CHANNELS_CFG, {})
    channels = [normalize(e) for e in cfg.get("channels", []) if e]
    if not channels:
        print("no channels in", CHANNELS_CFG); return
    state = load_json(STATE, {})
    total_new = 0

    for ch in channels:
        u, slug = ch["username"], ch["slug"]
        if not u:
            continue
        page = fetch(f"https://t.me/s/{u}")
        if page is None:
            continue
        p = Channel(); p.feed(page); p.close()
        title = ch["name"] or channel_title(page, u)
        last = int(state.get(u, 0))
        outdir = os.path.join(RAW, slug)
        os.makedirs(outdir, exist_ok=True)
        new, hi = 0, last
        for post in sorted(p.posts, key=lambda x: x["id"]):
            mid = post["id"]
            if mid <= last:
                continue
            date = post["date"] or ""
            rec = {
                "uid": mid,
                "message_id": f"tg-{slug}-{mid}",
                "from": f"@{u}",
                "from_name": title,
                "subject": (post["text"].splitlines()[0][:200] if post["text"] else title),
                "date": date,
                "source": title,
                "source_slug": slug,
                "tg_url": f"https://t.me/{u}/{mid}",
                "html": post["html"],
                "text": post["text"],
            }
            fname = f"{date or 'undated'}_{mid}.json"
            with open(os.path.join(outdir, fname), "w", encoding="utf-8") as fh:
                json.dump(rec, fh, ensure_ascii=False, indent=1)
            new += 1; hi = max(hi, mid)
        state[u] = hi
        total_new += new
        print(f"  {u} ({title}): {len(p.posts)} on page, {new} new (high-water {hi})")

    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=1)
    print(f"tg ingest: {total_new} new posts across {len(channels)} channels")


if __name__ == "__main__":
    main()
