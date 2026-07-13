#!/usr/bin/env python3
"""mail_ingest.py — pull newsletter emails from IMAP (mailbox.org) into raw_news/<source>/.

Deterministic, stdlib-only (no Claude). Safe to run in GitHub Actions or locally.

Env:
  IMAP_HOST   (default imap.mailbox.org)
  IMAP_PORT   (default 993, SSL)
  IMAP_USER   full mailbox address
  IMAP_PASS   app-specific password (mailbox.org → Settings → app password)
  IMAP_FOLDER (default INBOX; comma-separated for several)
  RAW_DIR     (default <repo>/raw_news)

Each new message → raw_news/<source-slug>/<YYYY-MM-DD>_<uid>.eml  (+ .json sidecar with
from/subject/date/html/text/source). Incremental via raw_news/.ingest_state.json (seen
Message-IDs + per-folder UID high-water mark). Read-only on the mailbox (never deletes).

Source mapping: pipeline/sources_map.json = {"<email-or-domain>": "Friendly Name"}; unknown
senders get a slug from their domain (and are listed in raw_news/_unmapped_senders.json so you
can name them later).
"""
import imaplib, email, os, json, re, ssl, hashlib, sys
from email.utils import parseaddr, parsedate_to_datetime
from email.header import decode_header, make_header

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo root
RAW = os.environ.get("RAW_DIR", os.path.join(ROOT, "raw_news"))
SMAP = os.path.join(ROOT, "pipeline", "sources_map.json")
STATE = os.path.join(RAW, ".ingest_state.json")


def _dec(s):
    try:
        return str(make_header(decode_header(s or "")))
    except Exception:
        return s or ""


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "unknown"


def load_json(p, default):
    try:
        return json.load(open(p))
    except Exception:
        return default


def source_for(from_addr, smap):
    addr = (from_addr or "").lower()
    dom = addr.split("@")[-1] if "@" in addr else addr
    if addr in smap:
        return smap[addr]
    if dom in smap:
        return smap[dom]
    # try parent domain (news.thefintechblueprint.com -> thefintechblueprint.com)
    parts = dom.split(".")
    for i in range(len(parts) - 2):
        cand = ".".join(parts[i:])
        if cand in smap:
            return smap[cand]
    local = addr.split('@')[0] if '@' in addr else addr
    return None, local  # fallback: name BEFORE @ (local-part)


def get_bodies(msg):
    html, text = "", ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            disp = str(part.get("Content-Disposition") or "")
            if "attachment" in disp:
                continue
            try:
                payload = part.get_payload(decode=True)
                if payload is None:
                    continue
                charset = part.get_content_charset() or "utf-8"
                body = payload.decode(charset, errors="replace")
            except Exception:
                continue
            if ctype == "text/html" and not html:
                html = body
            elif ctype == "text/plain" and not text:
                text = body
    else:
        try:
            body = msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", errors="replace")
        except Exception:
            body = msg.get_payload() or ""
        if msg.get_content_type() == "text/html":
            html = body
        else:
            text = body
    return html, text


def main():
    user, pw = os.environ.get("IMAP_USER"), os.environ.get("IMAP_PASS")
    if not user or not pw:
        raise SystemExit("set IMAP_USER and IMAP_PASS env vars")
    host = os.environ.get("IMAP_HOST", "imap.mailbox.org")
    port = int(os.environ.get("IMAP_PORT", "993"))
    folders = [f.strip() for f in os.environ.get("IMAP_FOLDER", "INBOX").split(",") if f.strip()]
    os.makedirs(RAW, exist_ok=True)
    smap = load_json(SMAP, {})
    state = load_json(STATE, {"seen_msgids": [], "uidnext": {}})
    seen = set(state.get("seen_msgids", []))
    unmapped = {}

    M = imaplib.IMAP4_SSL(host, port, ssl_context=ssl.create_default_context())
    M.login(user, pw)
    saved = 0
    try:
        for folder in folders:
            typ, _ = M.select(f'"{folder}"', readonly=True)
            if typ != "OK":
                print(f"  ! cannot select {folder}"); continue
            typ, data = M.uid("search", None, "ALL")
            if typ != "OK":
                continue
            uids = data[0].split()
            for uid in uids:
                uid = uid.decode()
                typ, md = M.uid("fetch", uid, "(RFC822)")
                if typ != "OK" or not md or not md[0]:
                    continue
                raw = md[0][1]
                msg = email.message_from_bytes(raw)
                msgid = (msg.get("Message-ID") or f"{folder}:{uid}").strip()
                if msgid in seen:
                    continue
                from_name, from_addr = parseaddr(msg.get("From", ""))
                if from_addr.lower() == user.lower():       # skip own/welcome mail, not a newsletter
                    seen.add(msgid); continue
                src = source_for(from_addr, smap)
                if isinstance(src, tuple):
                    name, dom = src
                    source = dom            # friendly name unknown → use domain
                    unmapped[from_addr] = _dec(from_name) or dom
                else:
                    source = src
                slug = slugify(source)
                try:
                    d = parsedate_to_datetime(msg.get("Date"))
                    date = d.date().isoformat()
                except Exception:
                    date = "0000-00-00"
                html, text = get_bodies(msg)
                subj = _dec(msg.get("Subject"))
                outdir = os.path.join(RAW, slug)
                os.makedirs(outdir, exist_ok=True)
                base = f"{date}_{uid}"
                with open(os.path.join(outdir, base + ".eml"), "wb") as f:
                    f.write(raw)
                json.dump({"uid": uid, "message_id": msgid, "from": from_addr,
                           "from_name": _dec(from_name), "subject": subj, "date": date,
                           "source": source, "source_slug": slug, "html": html, "text": text},
                          open(os.path.join(outdir, base + ".json"), "w"), ensure_ascii=False)
                seen.add(msgid); saved += 1
    finally:
        try: M.logout()
        except Exception: pass

    state["seen_msgids"] = sorted(seen)
    json.dump(state, open(STATE, "w"))
    if unmapped:
        prev = load_json(os.path.join(RAW, "_unmapped_senders.json"), {})
        prev.update(unmapped)
        json.dump(prev, open(os.path.join(RAW, "_unmapped_senders.json"), "w"), ensure_ascii=False, indent=2)
    print(f"ingest: saved {saved} new emails into {RAW}/ ; {len(unmapped)} unmapped sender(s)")


if __name__ == "__main__":
    main()
