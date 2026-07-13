#!/usr/bin/env python3
"""Telegram webhook receiver for the research bot — INSTANT response (no 10-min poll lag).

Telegram POSTs every message here the moment it arrives; we ACK Telegram immediately, send the user a
"Researching…" reply, and fire a GitHub workflow_dispatch of research.yml (inputs: query, deep, chat) so
the self-hosted Fly runner picks it up within seconds. getUpdates polling is dropped (mutually exclusive
with a webhook). Always-on tiny Fly Machine.

Env (Fly secrets/vars):
  RESEARCH_BOT_TOKEN   Telegram bot token (to ack + setWebhook)
  GH_DISPATCH_PAT      GitHub PAT with Actions:read+write on the repo (to dispatch research.yml)
  WEBHOOK_SECRET       shared secret; Telegram echoes it in X-Telegram-Bot-Api-Secret-Token
  RESEARCH_ALLOWED_CHATS  csv of allowed chat ids
  GH_OWNER, GH_REPO    default YOUR_GH_OWNER / YOUR_REPO
  FLY_APP_NAME         set by Fly → used to build the public webhook URL
"""
import json, os, urllib.request, urllib.parse, urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BOT = os.environ["RESEARCH_BOT_TOKEN"]
PAT = os.environ["GH_DISPATCH_PAT"]
OWNER = os.environ.get("GH_OWNER", "YOUR_GH_OWNER")
REPO = os.environ.get("GH_REPO", "YOUR_REPO")
ALLOW = {x.strip() for x in os.environ.get("RESEARCH_ALLOWED_CHATS", "").split(",") if x.strip()}
SECRET = os.environ.get("WEBHOOK_SECRET", "")
PORT = int(os.environ.get("PORT", "8080"))
TG = f"https://api.telegram.org/bot{BOT}"


def tg(method, **params):
    data = urllib.parse.urlencode(params).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{TG}/{method}", data=data), timeout=15) as r:
            return json.load(r)
    except Exception as e:
        print(f"tg {method} failed: {e}", flush=True); return {"ok": False}


def dispatch(query, deep, chat):
    body = json.dumps({"ref": "main", "inputs": {
        "query": query, "deep": "true" if deep else "false", "chat": chat}}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/research.yml/dispatches",
        data=body, method="POST", headers={"Authorization": f"Bearer {PAT}",
        "Accept": "application/vnd.github+json", "User-Agent": "fintech-webhook"})
    try:
        urllib.request.urlopen(req, timeout=15)
        print(f"dispatched research (deep={deep}) for chat {chat}: {query[:50]}", flush=True)
        return True
    except urllib.error.HTTPError as e:
        print(f"dispatch failed {e.code}: {e.read()[:200]}", flush=True); return False
    except Exception as e:
        print(f"dispatch failed: {e}", flush=True); return False


def handle(upd):
    msg = upd.get("message") or upd.get("edited_message") or {}
    if "text" not in msg or "chat" not in msg:
        return
    chat, q = str(msg["chat"]["id"]), msg["text"].strip()
    if q.startswith("/start"):
        tg("sendMessage", chat_id=chat, text="Пришли компанию/тему → ресёрч-заметка (новости + IR + веб). "
           "Префикс /deep — глубокий ресёрч с вендорскими плагинами."); return
    if not ALLOW:
        tg("sendMessage", chat_id=chat, text=f"Бот не настроен. Твой chat id: {chat}"); return
    if chat not in ALLOW:
        tg("sendMessage", chat_id=chat, text=f"Не авторизован. Твой chat id: {chat}"); return
    parts = q.split(None, 1)
    deep = parts[0].lower() in ("/deep", "/research")
    if deep:
        if len(parts) < 2:
            tg("sendMessage", chat_id=chat, text="Использование: /deep <тема или компания>"); return
        q = parts[1].strip()
    tg("sendChatAction", chat_id=chat, action="typing")
    tg("sendMessage", chat_id=chat, text=f"Ресёрч{' (deep — вендорские плагины)' if deep else ''} — запускаю, "
       "пришлю статью, как будет готово…")
    dispatch(q, deep, chat)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _send(self, code, body=b"ok"):
        self.send_response(code); self.send_header("Content-Length", str(len(body)))
        self.end_headers(); self.wfile.write(body)

    def do_GET(self):
        self._send(200)                                     # health check

    def do_POST(self):
        if SECRET and self.headers.get("X-Telegram-Bot-Api-Secret-Token") != SECRET:
            self._send(401, b"bad secret"); return
        n = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(n) if n else b"{}"
        self._send(200)                                     # ACK Telegram FAST, then process
        try:
            handle(json.loads(raw or b"{}"))
        except Exception as e:
            print(f"handle error: {e}", flush=True)


def main():
    app = os.environ.get("FLY_APP_NAME")
    if app:                                                 # register the webhook to our public URL
        r = tg("setWebhook", url=f"https://{app}.fly.dev/tg", secret_token=SECRET,
               allowed_updates=json.dumps(["message"]), drop_pending_updates="false")
        print(f"setWebhook https://{app}.fly.dev/tg → {r.get('ok')} {r.get('description','')}", flush=True)
    print(f"listening on :{PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()


if __name__ == "__main__":
    main()
