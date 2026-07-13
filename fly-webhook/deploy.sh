#!/usr/bin/env bash
# Deploy the Telegram webhook Machine. Prereqs: `fly auth login`; export GH_DISPATCH_PAT (Actions:RW PAT),
# RESEARCH_BOT_TOKEN, and (optional) RESEARCH_ALLOWED_CHATS. Idempotent.
set -euo pipefail
cd "$(dirname "$0")"
APP=fintech-tg-webhook
: "${GH_DISPATCH_PAT:?export GH_DISPATCH_PAT=<Actions:read+write PAT>}"
: "${RESEARCH_BOT_TOKEN:?export RESEARCH_BOT_TOKEN=<bot token>}"
SECRET="${WEBHOOK_SECRET:-$(openssl rand -hex 16)}"

fly apps create "$APP" 2>/dev/null || echo "app $APP exists"
printf 'GH_DISPATCH_PAT=%s\nRESEARCH_BOT_TOKEN=%s\nWEBHOOK_SECRET=%s\nRESEARCH_ALLOWED_CHATS=%s\n' \
  "$GH_DISPATCH_PAT" "$RESEARCH_BOT_TOKEN" "$SECRET" "${RESEARCH_ALLOWED_CHATS:-}" \
  | fly secrets import -a "$APP"                        # via stdin, never echoed
fly deploy -a "$APP" --ha=false
echo "→ fly logs -a $APP   (expect: setWebhook … → True)"
