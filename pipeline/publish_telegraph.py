#!/usr/bin/env python3
"""publish_telegraph.py — publish the daily digest to telegra.ph + a Telegram channel.

Reads digest/DATE.md (flat v5 markdown with two market sections; falls back to the legacy
Posts/DATE.md), converts it to a telegra.ph page, then posts a short caption to the channel
via the bot. The caption = a 1–2 line summary of the day's KEY THESES (either a `<!-- summary: ... -->`
marker, or the top item headlines) + a hyperlink "Дайджест новостей дд/мм/гг" pointing at the
telegra.ph page (Instant View). `## ` section headers render as h3, `# ` as the page title.
The digest is ONE telegra.ph page (filled up to the cap; overflow tail dropped — never split into parts).
Deterministic, stdlib-only.

Env:
  TELEGRAM_BOT_TOKEN  (required) bot token; the bot must be a channel ADMIN ("Post Messages").
  TELEGRAM_CHANNEL    (required) @username or numeric -100... id.
  TELEGRAPH_TOKEN     (optional) persistent telegra.ph access token (consistent author +
                      lets the SAME page be re-edited). If unset, a throwaway account is
                      created per run (page still public, just a new URL each time).
  TELEGRAPH_AUTHOR    (optional) author_name (default "Fintech Radar").

Usage: python3 pipeline/publish_telegraph.py --date 2026-06-21 [--force]
  Normal: skip if pipeline/state/published/DATE.json exists.
  --force: re-publish, OVERWRITING the existing page (editPage) and channel message
           (editMessageText) when the marker has them; falls back to create/send.
  No-op (exit 0) if creds are missing.
"""
import os, re, json, argparse, urllib.request, urllib.parse, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_TG = "https://api.telegram.org"
API_TPH = "https://api.telegra.ph"

LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
INLINE_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)|\*\*(.+?)\*\*')
COMMENT_RE = re.compile(r'^<!--\s*(.*?)\s*-->\s*$')
SUMMARY_RE = re.compile(r'^<!--\s*summary:\s*(.*?)\s*-->\s*$', re.I)


def _req(url, data):
    """POST form-encoded; return parsed JSON even on HTTP 4xx (Telegram returns 400+body)."""
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body, headers={"User-Agent": "fintech-radar"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except Exception:
            return {"ok": False, "error": str(e)}


def inline_nodes(text):
    out, pos = [], 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            out.append(text[pos:m.start()])
        if m.group(1) is not None:
            out.append({"tag": "a", "attrs": {"href": m.group(2)}, "children": [m.group(1)]})
        else:
            out.append({"tag": "strong", "children": [m.group(3)]})
        pos = m.end()
    if pos < len(text):
        out.append(text[pos:])
    return out or [text]


def md_to_telegraph(md):
    """Return (title, content_nodes, summary). Summary comes from a <!-- summary: --> marker
    and is NOT rendered into the page body. Other comment lines are skipped."""
    title, nodes, summary = "Fintech дайджест", [], ""
    cur_ul = cur_li = nested_ul = None

    def flush():
        nonlocal cur_ul, cur_li, nested_ul
        if cur_ul is not None:
            nodes.append(cur_ul)
        cur_ul = cur_li = nested_ul = None

    for raw in md.splitlines():
        if not raw.strip():
            continue
        ms = SUMMARY_RE.match(raw.strip())
        if ms:
            summary = ms.group(1); continue
        if COMMENT_RE.match(raw.strip()):           # skip any other html comment
            continue
        if raw.startswith("## "):
            flush(); nodes.append({"tag": "h3", "children": inline_nodes(raw[3:].strip())}); continue
        if raw.startswith("# "):
            flush(); title = raw[2:].strip(); continue
        m_nested = re.match(r'^(?:\t+| {2,})\*\s+(.*)$', raw)
        if m_nested and cur_li is not None:
            if nested_ul is None:
                nested_ul = {"tag": "ul", "children": []}
                cur_li["children"].append(nested_ul)
            nested_ul["children"].append({"tag": "li", "children": inline_nodes(m_nested.group(1))})
            continue
        m_bul = re.match(r'^\*\s+(.*)$', raw)
        if m_bul:
            if cur_ul is None:
                cur_ul = {"tag": "ul", "children": []}
            cur_li = {"tag": "li", "children": inline_nodes(m_bul.group(1))}
            nested_ul = None
            cur_ul["children"].append(cur_li)
            continue
        flush()
        s = raw.strip()
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            nodes.append({"tag": "h4", "children": inline_nodes(s[2:-2])})
        else:
            nodes.append({"tag": "p", "children": inline_nodes(s)})
    flush()
    return title, nodes, summary


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ddmmyy(date):
    y, m, d = date.split("-")
    return f"{d}/{m}/{y[2:]}"


_LINK_RE = re.compile(r'\[([^\]]+)\]\([^)]*\)')   # [text](url) -> text

def _auto_summary(md, n=2, maxlen=230):
    """1-2 line caption = the day's TOP item headlines (key theses), links/bold stripped.
    Preferred source is the digest's `<!-- summary: ... -->` marker; this is the deterministic
    fallback. An item = a top-level bold headline line `**...**` (flat v5 digest)."""
    heads = []
    for ln in md.splitlines():
        s = ln.strip()
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            t = _LINK_RE.sub(r'\1', s[2:-2]).replace("**", "").strip()
            t = re.sub(r'\s+', ' ', t)
            if t:
                heads.append(t)
        if len(heads) >= n:
            break
    out = " · ".join(heads)
    return (out[:maxlen - 1].rstrip() + "…") if len(out) > maxlen else out


TPH_LIMIT = 58000   # bytes of JSON content per telegra.ph page (safely under the ~64KB cap)


def _block_nodes(nodes):
    """Group the flat node list into blocks so a headline (h3/h4) is never split
    from the bullet list / paragraph that follows it."""
    blocks, cur = [], []
    for n in nodes:
        tag = n.get("tag") if isinstance(n, dict) else None
        if tag in ("h3", "h4") and cur:
            blocks.append(cur); cur = [n]
        else:
            cur.append(n)
    if cur:
        blocks.append(cur)
    return blocks


def _chunk_nodes(nodes, limit=TPH_LIMIT):
    """Pack blocks into chunks whose serialized content stays under `limit` bytes,
    so a long digest spills across several telegra.ph pages instead of CONTENT_TOO_BIG."""
    chunks, cur = [], []
    for blk in _block_nodes(nodes):
        trial = cur + blk
        if cur and len(json.dumps(trial, ensure_ascii=False).encode()) > limit:
            chunks.append(cur); cur = list(blk)
        else:
            cur = trial
    if cur:
        chunks.append(cur)
    return chunks or [[]]


PAGE_MAX = 62000    # bytes of node JSON — fill a SINGLE telegra.ph page up to just under its ~64KB cap


def _fit_one_page(nodes, limit=PAGE_MAX):
    """Pack blocks into ONE page up to `limit` bytes (digest is ordered top-first, so overflow
    tail is dropped — never split into 'Часть N'). Returns (nodes_for_one_page, dropped_blocks)."""
    blocks = _block_nodes(nodes)
    kept = []
    for i, blk in enumerate(blocks):
        trial = kept + blk
        if kept and len(json.dumps(trial, ensure_ascii=False).encode()) > limit:
            return kept, len(blocks) - i
        kept = trial
    return kept, 0


def publish_page(md, title=None, author=None, token=None):
    """Create telegra.ph page(s) from arbitrary markdown -> list of URLs (chunked if >~64KB).
    Reusable by the researcher (full 1-pager → article). No Telegram send here."""
    author = author or os.environ.get("TELEGRAPH_AUTHOR", "Fintech Radar")
    t, nodes, _ = md_to_telegraph(md)
    title = (title or t or "Fintech research")[:256]
    tok = token or os.environ.get("TELEGRAPH_TOKEN")
    if not tok:
        acc = _req(f"{API_TPH}/createAccount", {"short_name": "FintechRadar", "author_name": author})
        if not acc.get("ok") or "result" not in acc:        # don't KeyError-crash on a failed createAccount
            raise RuntimeError(f"telegra.ph createAccount failed: {acc}")
        tok = acc["result"]["access_token"]
    chunks = _chunk_nodes(nodes); n = len(chunks); urls = []
    for i, ch in enumerate(chunks):
        ptitle = title if n == 1 else f"{title} ({i + 1}/{n})"
        r = _req(f"{API_TPH}/createPage", {"access_token": tok, "title": ptitle, "author_name": author,
                                           "content": json.dumps(ch, ensure_ascii=False), "return_content": "false"})
        if not r.get("ok"):                                  # RuntimeError (not SystemExit) so callers' except Exception catches it
            raise RuntimeError(f"telegra.ph createPage failed: {r}")
        urls.append(r["result"]["url"])
    return urls


def main():
    ap = argparse.ArgumentParser()
    import datetime
    ap.add_argument("--date", default=datetime.datetime.utcnow().strftime("%Y-%m-%d"))
    ap.add_argument("--force", action="store_true")
    ns = ap.parse_args()
    date = ns.date

    post_path = os.path.join(ROOT, "digest", f"{date}.md")
    if not os.path.exists(post_path):
        post_path = os.path.join(ROOT, "Posts", f"{date}.md")    # legacy fallback
    if not os.path.exists(post_path):
        print(f"publish: no digest/{date}.md (or Posts/{date}.md) — nothing to publish"); return
    bot = os.environ.get("TELEGRAM_BOT_TOKEN")
    channel = os.environ.get("TELEGRAM_CHANNEL")
    if not bot or not channel:
        print("publish: TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL not set — skipping"); return

    mark_dir = os.path.join(ROOT, "pipeline", "state", "published")
    mark = os.path.join(mark_dir, f"{date}.json")
    prev = json.load(open(mark)) if os.path.exists(mark) else None
    if prev and not ns.force:
        print(f"publish: {date} already published ({prev.get('telegraph_url')}) — skip (use --force to overwrite)"); return

    author = os.environ.get("TELEGRAPH_AUTHOR", "Fintech Radar")
    raw_md = open(post_path, encoding="utf-8").read()
    title, nodes, summary = md_to_telegraph(raw_md)
    if not summary:
        summary = _auto_summary(raw_md)
    # 1) telegra.ph page(s): chunk content to stay under telegra.ph's ~64KB page limit
    tok = os.environ.get("TELEGRAPH_TOKEN")
    if not tok:
        acc = _req(f"{API_TPH}/createAccount", {"short_name": "FintechRadar", "author_name": author})
        tok = acc["result"]["access_token"]

    prev_pages = (prev or {}).get("pages") or (
        [{"url": prev["telegraph_url"], "path": prev.get("telegraph_path")}]
        if prev and prev.get("telegraph_url") else [])
    # ONE telegra.ph page only — fill up to the page cap, drop any overflow tail (never split into parts)
    nodes_one, dropped = _fit_one_page(nodes)
    if dropped:
        print(f"  note: digest exceeded one page — dropped {dropped} trailing block(s) to keep a single part")
    content = json.dumps(nodes_one, ensure_ascii=False)
    page = None
    if ns.force and len(prev_pages) == 1 and prev_pages[0].get("path"):   # edit the existing single page in place
        path = prev_pages[0]["path"]
        r = _req(f"{API_TPH}/editPage", {"access_token": tok, "path": path, "title": title[:256],
                                         "author_name": author, "content": content, "return_content": "false"})
        if r.get("ok"):
            page = r["result"]; print(f"  telegra.ph: edited existing page /{path}")
        else:
            print(f"  telegra.ph editPage failed ({r.get('error')}), creating new page")
    if page is None:
        r = _req(f"{API_TPH}/createPage", {"access_token": tok, "title": title[:256],
                                           "author_name": author, "content": content, "return_content": "false"})
        if not r.get("ok"):
            raise SystemExit(f"telegra.ph createPage failed: {r}")
        page = r["result"]
    pages = [{"url": page["url"], "path": page.get("path", page["url"].rsplit("/", 1)[-1])}]

    # 2) channel caption: 1-2 line key theses + single digest link
    label = f'<a href="{pages[0]["url"]}">Дайджест новостей {ddmmyy(date)}</a>'
    caption = f"{esc(summary)}\n\n{label}" if summary else label

    msg_id = None
    if ns.force and prev and prev.get("message_id"):
        r = _req(f"{API_TG}/bot{bot}/editMessageText",
                 {"chat_id": channel, "message_id": prev["message_id"], "text": caption, "parse_mode": "HTML"})
        if r.get("ok"):
            msg_id = prev["message_id"]; print(f"  telegram: edited message {msg_id}")
        elif "not modified" in str(r.get("description", "")).lower():
            msg_id = prev["message_id"]; print("  telegram: message unchanged")
        else:
            print(f"  telegram editMessageText failed ({r.get('description')}), sending new message")
    if msg_id is None:
        r = _req(f"{API_TG}/bot{bot}/sendMessage", {"chat_id": channel, "text": caption, "parse_mode": "HTML"})
        if not r.get("ok"):
            raise SystemExit(f"Telegram sendMessage failed: {r}")
        msg_id = r["result"]["message_id"]

    os.makedirs(mark_dir, exist_ok=True)
    json.dump({"date": date, "pages": pages, "telegraph_url": pages[0]["url"],
               "telegraph_path": pages[0]["path"], "message_id": msg_id},
              open(mark, "w"), ensure_ascii=False, indent=2)
    print(f"publish: {date} -> {', '.join(p['url'] for p in pages)} ; channel msg {msg_id}")


if __name__ == "__main__":
    main()
