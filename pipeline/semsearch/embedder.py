#!/usr/bin/env python3
"""embedder.py — dense embeddings via an OpenAI-compatible /embeddings endpoint.
Default: OpenRouter + Qwen3-Embedding-8B, MRL-truncated to EMBED_DIM. stdlib-only.

Config (env or pipeline/.env):
  OPENROUTER_API_KEY | EMBED_API_KEY   (required)
  EMBED_BASE_URL   (default https://openrouter.ai/api/v1)
  EMBED_MODEL      (default qwen/qwen3-embedding-8b)
  EMBED_DIM        (default 1024; sent as `dimensions` — Qwen MRL truncation)

Qwen3-Embedding is instruction-aware: queries get an "Instruct: …\\nQuery: …" prefix,
documents are embedded as-is. Use kind="query" for search, "passage" (default) for indexing.
Keep EMBED_DIM identical for indexing and querying (vectors must match).
"""
import os, json, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUERY_INSTRUCT = ("Instruct: Given a query, retrieve relevant fintech and tech news notes "
                  "that answer or relate to it\nQuery: ")


def _load_env():
    if os.environ.get("OPENROUTER_API_KEY") or os.environ.get("EMBED_API_KEY"):
        return
    p = os.path.join(ROOT, "pipeline", ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _cfg():
    _load_env()
    key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("EMBED_API_KEY")
    if not key:
        raise SystemExit("set OPENROUTER_API_KEY (env or pipeline/.env)")
    base = os.environ.get("EMBED_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    model = os.environ.get("EMBED_MODEL", "qwen/qwen3-embedding-8b")
    dim = int(os.environ.get("EMBED_DIM", "1024"))
    return key, base, model, dim


def embed(texts, kind="passage", batch=128, retries=5):
    """list[str] -> list[list[float]]. kind='query' prepends the Qwen retrieval instruction."""
    key, base, model, dim = _cfg()
    if kind == "query":
        texts = [QUERY_INSTRUCT + t for t in texts]
    out = []
    for i in range(0, len(texts), batch):
        part = [t if t.strip() else "." for t in texts[i:i + batch]]
        payload = {"model": model, "input": part}
        if dim:
            payload["dimensions"] = dim
        body = json.dumps(payload).encode()
        req = urllib.request.Request(base + "/embeddings", data=body, headers={
            "Authorization": f"Bearer {key}", "Content-Type": "application/json",
            "X-Title": "Fintech Radar"})
        for attempt in range(retries):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    d = json.load(r)
                rows = sorted(d["data"], key=lambda x: x["index"])
                out.extend([row["embedding"] for row in rows])
                break
            except urllib.error.HTTPError as e:
                msg = e.read()[:300]
                if e.code in (408, 429, 500, 502, 503, 524, 529) and attempt < retries - 1:
                    time.sleep(2 * (attempt + 1)); continue
                raise SystemExit(f"embed HTTP {e.code}: {msg}")
            except Exception:
                if attempt < retries - 1:
                    time.sleep(2 * (attempt + 1)); continue
                raise
        if i and (i // batch) % 5 == 0:
            print(f"  embedded {i + len(part)}/{len(texts)}", flush=True)
    return out


if __name__ == "__main__":
    import sys
    v = embed([sys.argv[1] if len(sys.argv) > 1 else "проверка соединения"], kind="query")
    print(f"OK — model returns dim={len(v[0])}")
