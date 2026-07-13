#!/usr/bin/env python3
"""research_bot.py — Telegram research bot, polled FROM GitHub Actions (no external host).

Two phases so empty polls stay cheap (no index download / no claude):
  --poll     : Telegram getUpdates(offset from research/state.json); send cheap replies (/start,
               not-authorized -> chat id); queue authorized research queries to RUNNER_TEMP/pending.json;
               advance+persist offset ONLY if there were updates; emit has_work=true|false to GITHUB_OUTPUT.
  --process  : run `claude -p` (researcher skill: sem news+IR + web, MR/ER plugins, no xlsx/pptx) for each
               queued query and send the answer; write research/results + research/log.
No flag = poll then process (local use).

Env: RESEARCH_BOT_TOKEN (required), RESEARCH_ALLOWED_CHATS (csv chat ids), CLAUDE_CODE_OAUTH_TOKEN,
     ANTHROPIC_MODEL, OPENROUTER_API_KEY/EMBED_* (sem). Runs from the repo root.
"""
import argparse, glob, json, os, subprocess, sys, urllib.request, urllib.parse, urllib.error, datetime as dt

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RDIR = os.path.join(REPO, "research")
STATE = os.path.join(RDIR, "state.json")
RESULTS = os.path.join(RDIR, "results")
LOGS = os.path.join(RDIR, "log")
PEND = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "research_pending.json")
TOK = os.environ.get("RESEARCH_BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOK}"
ALLOW = {x.strip() for x in os.environ.get("RESEARCH_ALLOWED_CHATS", "").split(",") if x.strip()}
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8[1m]")
RUN_TIMEOUT = int(os.environ.get("RESEARCH_TIMEOUT", "3000"))


def tg(method, **params):
    data = urllib.parse.urlencode(params).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{API}/{method}", data=data), timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try: return json.load(e)
        except Exception: return {"ok": False}
    except Exception:
        return {"ok": False}


def send(chat, text):
    for i in range(0, len(text), 3900):
        tg("sendMessage", chat_id=chat, text=text[i:i + 3900], disable_web_page_preview="true")


def _emit(has_work):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        open(out, "a").write(f"has_work={'true' if has_work else 'false'}\n")


def poll():
    qo = os.environ.get("QUERY_OVERRIDE", "").strip()        # dispatch (webhook/manual): process this query directly
    if qo:
        chat = os.environ.get("CHAT_OVERRIDE", "").strip() or (sorted(ALLOW)[0] if ALLOW else "")
        json.dump([{"chat": chat, "q": qo, "deep": os.environ.get("DEEP_OVERRIDE", "").lower() == "true"}], open(PEND, "w"))
        print(f"manual query override (deep={os.environ.get('DEEP_OVERRIDE')}): {qo[:60]}", flush=True)
        _emit(True); return
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    offset = st.get("offset", 0)
    resp = tg("getUpdates", offset=offset, timeout=0, allowed_updates=json.dumps(["message"]))
    ups = resp.get("result", []) if resp.get("ok") else []
    print(f"getUpdates: {len(ups)} update(s) since offset {offset}", flush=True)
    max_id, pending = offset, []
    for u in ups:
        max_id = max(max_id, u["update_id"] + 1)
        msg = u.get("message") or {}
        if "text" not in msg or "chat" not in msg:
            continue
        chat, q = str(msg["chat"]["id"]), msg["text"].strip()
        if q.startswith("/start"):
            send(chat, "Send a company or market/theme → quick research note (news + IR + web).\n"
                       "Prefix with /deep for a full vendor-plugin research (market-researcher / earnings-reviewer).")
        elif not ALLOW:
            send(chat, f"Bot not configured. Your chat id: {chat} — set repo var RESEARCH_ALLOWED_CHATS to it.")
        elif chat not in ALLOW:
            send(chat, f"Not authorized. Your chat id: {chat} — ask the owner to allow-list it.")
        else:
            parts = q.split(None, 1)
            deep = parts[0].lower() in ("/deep", "/research")
            if deep:
                if len(parts) < 2:
                    send(chat, "Use: /deep <тема или компания>"); continue
                q = parts[1].strip()
            send(chat, f"Researching{' (deep — vendor plugins)' if deep else ' (quick)'} — news + IR + web…")
            tg("sendChatAction", chat_id=chat, action="typing")
            pending.append({"chat": chat, "q": q, "deep": deep})
    if max_id != offset:                                  # persist only on real progress (empty polls = no diff)
        json.dump({"offset": max_id}, open(STATE, "w"))
    json.dump(pending, open(PEND, "w"))
    print(f"queued {len(pending)} research quer(y/ies); offset -> {max_id}", flush=True)
    _emit(bool(pending))


def run_research(query, deep=False):
    """Returns (answer_markdown, skills_invoked). Uses stream-json so we capture BOTH the final note
    AND the actual tool calls (proof that the vendor market-researcher / earnings-reviewer plugins fire)."""
    if deep:
        # direct top-level orchestration (NOT wrapped in the researcher skill, to allow plugin-skill calls)
        prompt = (
            "You are a fintech researcher writing a FULL 1-pager (markdown, first line `# <Title>`). Steps:\n"
            "1) Gather context IN PARALLEL: Bash `./pipeline/semsearch/sem search \"<terms>\" --db pipeline/state/newsdb --k 8 --json`"
            " AND `./pipeline/semsearch/sem search \"<terms>\" --db pipeline/state/irdb [--company <slug>] --k 8 --json`"
            " (IR filings; cite each hit's drive_url) AND WebSearch for fresh/extra.\n"
            "2) THEN you MUST invoke the vendor plugin skills via the `Skill` tool, in order, feeding them the gathered"
            " context — THEME: `market-researcher:sector-overview` → `market-researcher:competitive-analysis` →"
            " `market-researcher:comps-analysis` (if a clear peer set) → `market-researcher:idea-generation`;"
            " COMPANY: `earnings-reviewer:earnings-analysis` → `earnings-reviewer:morning-note` +"
            " `market-researcher:competitive-analysis`. Mark unsourced figures [UNSOURCED]. NEVER pptx-author/xlsx-author,"
            " never write .xlsx/.pptx.\n"
            "3) Synthesize everything into ONE 1-pager (~600-1200 words), in the user's language. Output ONLY the markdown.\n\n"
            f"QUERY: {query}")
    else:
        prompt = ("Use the researcher skill (SIMPLE mode: news + IR DB + web only; do NOT invoke the "
                  "market-researcher / earnings-reviewer plugins). Output ONLY the FULL 1-pager research note in "
                  "markdown (first line `# <Title>`), per the skill.\n\n"
                  f"QUERY: {query}")
    cmd = ["claude", "-p", prompt, "--model", MODEL, "--dangerously-skip-permissions",
           "--output-format", "stream-json", "--verbose"]
    if deep:                                             # explicitly load the vendor plugins into the session
        base = os.path.expanduser("~/.claude/plugins/cache/claude-for-financial-services")
        for name in ("market-researcher", "earnings-reviewer"):
            hits = sorted(glob.glob(os.path.join(base, name, "*")))
            if hits:
                cmd += ["--plugin-dir", hits[-1]]
    try:
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, timeout=RUN_TIMEOUT)
    except subprocess.TimeoutExpired:
        return "Research timed out — try a narrower query.", []
    answer, texts, used, usage = "", [], [], {}
    for line in (r.stdout or "").splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except Exception:
            continue
        ty = ev.get("type")
        if ty == "result":
            answer = ev.get("result") or answer
            usage = ev.get("usage", usage)
        elif ty == "assistant":
            for b in ((ev.get("message") or {}).get("content") or []):
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "text":
                    texts.append(b.get("text", ""))
                elif b.get("type") == "tool_use":
                    nm, inp = b.get("name", ""), (b.get("input") or {})
                    if nm == "Skill":
                        lbl = str(inp.get("command") or inp.get("name") or inp.get("skill") or "")[:80]
                        used.append(lbl); print(f"  TOOL Skill: {lbl}", flush=True)
                    elif nm == "Task":
                        lbl = "Task:" + str(inp.get("subagent_type") or inp.get("description", ""))[:40]
                        used.append(lbl); print(f"  TOOL {lbl}", flush=True)
    if not answer:
        answer = "\n".join(t for t in texts if t).strip() or f"Research failed.\n{(r.stderr or '')[-400:]}"
    lines = answer.splitlines()                          # strip any preamble before the first '# Title'
    for idx, l in enumerate(lines):
        if l.startswith("# "):
            answer = "\n".join(lines[idx:]).strip(); break
    used = [u for u in used if u]
    print(f"  SKILLS/PLUGINS INVOKED: {used}", flush=True)
    seg_label = f"research{'-deep' if deep else ''}"     # segmented token breakdown (TOKENS/TRACE/TRACE-SEG)
    try:
        cap = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), f"{seg_label}.jsonl")
        with open(cap, "w", encoding="utf-8") as fh:
            fh.write(r.stdout or "")
        subprocess.run([sys.executable, os.path.join(REPO, "pipeline", "token_trace.py"), cap, seg_label])
    except Exception as e:
        print(f"  token_trace failed: {e}", flush=True)
    return answer, used


def process():
    os.makedirs(RESULTS, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
    sys.path.insert(0, os.path.join(REPO, "pipeline"))
    import publish_telegraph as ptg
    pending = json.load(open(PEND)) if os.path.exists(PEND) else []
    for p in pending:
        print(f"  research for chat {p['chat']}: {p['q'][:80]}", flush=True)
        md, used = run_research(p["q"], p.get("deep", False))
        title = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), p["q"][:80])
        try:                                            # publish the 1-pager as a telegra.ph article
            urls = ptg.publish_page(md, title=title)
            link = ("\n".join(f"Часть {i + 1}: {u}" for i, u in enumerate(urls))) if len(urls) > 1 else urls[0]
            send(p["chat"], f"{title}\n{link}")
        except Exception as e:                          # fallback: send the note inline
            print(f"  telegra.ph publish failed: {e}", flush=True)
            send(p["chat"], md)
        ts = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"); rid = f"{ts}_{p['chat']}"
        open(os.path.join(RESULTS, f"{rid}.md"), "w", encoding="utf-8").write(md if md.startswith("# ") else f"# {p['q']}\n\n{md}\n")
        with open(os.path.join(LOGS, ts[:8] + ".jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"ts": ts, "chat": p["chat"], "query": p["q"], "result": f"results/{rid}.md", "skills": used}, ensure_ascii=False) + "\n")
    print(f"processed {len(pending)} request(s)", flush=True)


def main():
    if not TOK:
        sys.exit("RESEARCH_BOT_TOKEN unset")
    ap = argparse.ArgumentParser()
    ap.add_argument("--poll", action="store_true"); ap.add_argument("--process", action="store_true")
    a = ap.parse_args()
    if a.poll:
        poll()
    elif a.process:
        process()
    else:
        poll(); process()


if __name__ == "__main__":
    main()
