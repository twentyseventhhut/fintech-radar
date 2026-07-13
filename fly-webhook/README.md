# Instant research bot — Telegram webhook on Fly

Kills the 10-min poll lag. Telegram POSTs each message to this always-on tiny Fly Machine, which ACKs the
user instantly ("Ресёрч — запускаю…") and fires a `workflow_dispatch` of **research.yml** (query, deep,
chat) → the self-hosted Fly runner starts within seconds. The `*/10` cron is removed (getUpdates and a
webhook are mutually exclusive); research runs only via this dispatch now.

## What it needs
- **GH_DISPATCH_PAT** — a GitHub PAT with **Actions: Read and write** on `YOUR_GH_OWNER/YOUR_REPO`
  (the runner's Administration-only PAT can't dispatch — 403). Best: mint ONE fresh fine-grained PAT with
  Administration RW + Actions RW + Contents Read, use it here AND update the runner secret, then revoke the
  old (compromised) runner PAT.
- **RESEARCH_BOT_TOKEN** — the research bot token (already known).
- **WEBHOOK_SECRET** — auto-generated at deploy (Telegram echoes it back; blocks spoofed POSTs).
- **RESEARCH_ALLOWED_CHATS** — copied from the repo var.

## Deploy
```
cd fly-webhook
export GH_DISPATCH_PAT=<Actions:RW PAT>
export RESEARCH_BOT_TOKEN=<bot token>
export RESEARCH_ALLOWED_CHATS=<csv chat ids>
bash deploy.sh
```
It creates the app, imports the secrets (stdin), deploys the Machine; on boot the Machine self-registers the
Telegram webhook to `https://fintech-tg-webhook.fly.dev/tg`. Verify:
```
fly logs -a fintech-tg-webhook            # look for: setWebhook … → True
curl -s "https://api.telegram.org/bot<token>/getWebhookInfo"   # url set, pending_update_count low
```
Send a message to the bot → you should get an instant ack, and the research reply a few minutes later.

Revert to polling: `fly-webhook/../fly-runner/…` — restore the `*/10` cron in research.yml and
`curl .../deleteWebhook`.
