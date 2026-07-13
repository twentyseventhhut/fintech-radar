#!/usr/bin/env python3
"""extract.py — plain-text extraction for IR documents (PDF / HTML / htm / txt).

Location-independent on purpose: callers pass an ABSOLUTE path resolved from a configurable
root (IR_DATASET / a Drive mount), so moving the raw corpus never touches this code or the index.
Extracted text is cached under pipeline/state/ir_cache/<md5>.txt so re-indexing never re-parses.

PDF -> PyMuPDF (fitz) if available, else pdfminer/pypdf if present, else "".
HTML/htm -> stdlib tag-stripper (drops script/style/nav noise).
"""
import os, re, hashlib, tempfile, urllib.request
from html.parser import HTMLParser

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(REPO, "pipeline", "state", "ir_cache")


class _HTMLText(HTMLParser):
    _DROP = {"script", "style", "head", "noscript", "svg", "nav", "footer", "form"}

    def __init__(self):
        super().__init__()
        self.parts, self._skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self._DROP:
            self._skip += 1
        elif tag in ("p", "br", "div", "tr", "li", "h1", "h2", "h3", "h4", "table"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self._DROP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip and data.strip():
            self.parts.append(data)

    def text(self):
        return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", "".join(self.parts))).strip()


def _from_html(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            html = raw.decode(enc); break
        except UnicodeDecodeError:
            html = raw.decode("utf-8", "ignore")
    p = _HTMLText()
    try:
        p.feed(html)
    except Exception:
        pass
    return p.text()


def _from_pdf(path):
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(path)
        return "\n".join(pg.get_text("text") for pg in doc).strip()
    except ImportError:
        pass
    try:
        from pdfminer.high_level import extract_text
        return (extract_text(path) or "").strip()
    except Exception:
        pass
    try:
        from pypdf import PdfReader
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(path).pages).strip()
    except Exception:
        return ""


def _download(url):
    """Best-effort fetch of a raw IR doc by its source url -> local temp path (or None)."""
    try:
        ext = os.path.splitext(url.split("?")[0])[1].lower() or ".htm"
        req = urllib.request.Request(url, headers={  # SEC requires a descriptive UA
            "User-Agent": "Fintech Radar research contact@example.com",
            "Accept-Encoding": "identity"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        fd, tmp = tempfile.mkstemp(suffix=ext)
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        return tmp
    except Exception:
        return None


def _parse(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return _from_pdf(path)
    if ext in (".htm", ".html"):
        return _from_html(path)
    if ext in (".txt", ".md"):
        return open(path, encoding="utf-8", errors="ignore").read()
    return ""


def extract(path, cache_key=None, use_cache=True, url=None):
    """Resolve a doc to plain text. Resolution order: cache -> local path -> source url (best-effort).
    cached by a STABLE cache_key so the cache survives the raw corpus moving to Google Drive, and the
    url fallback means a deep dive still works when neither the local copy nor a Drive mount is present.
    Returns '' if nothing resolves."""
    cp = None
    if use_cache:
        key = cache_key or hashlib.md5((path or url or "").encode()).hexdigest()
        cp = os.path.join(CACHE, key + ".txt")
        if os.path.exists(cp):                       # cache hit — no raw file required
            return open(cp, encoding="utf-8").read()
    tmp = None
    try:
        if path and os.path.exists(path):
            src = path
        elif url:
            src = tmp = _download(url)
        else:
            src = None
        txt = _parse(src) if src else ""
    except Exception:
        txt = ""
    finally:
        if tmp and os.path.exists(tmp):
            os.remove(tmp)
    txt = re.sub(r"\n{3,}", "\n\n", txt or "").strip()
    if use_cache and cp:
        os.makedirs(CACHE, exist_ok=True)
        open(cp, "w", encoding="utf-8").write(txt)
    return txt


if __name__ == "__main__":
    import sys
    t = extract(sys.argv[1], use_cache=False)
    print(f"[{len(t)} chars]\n{t[:1500]}")
