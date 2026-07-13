#!/usr/bin/env bash
# Deploy the self-hosted runner Machine. Prereqs: `fly auth login` done, and GH_RUNNER_PAT exported
# (a repo Administration:read+write PAT). Idempotent — safe to re-run.
set -euo pipefail
cd "$(dirname "$0")"
APP=fintech-runner
REGION=$(grep -oE 'primary_region = "[a-z]+"' fly.toml | grep -oE '"[a-z]+"' | tr -d '"')
: "${GH_RUNNER_PAT:?export GH_RUNNER_PAT=<repo-admin PAT> first}"

fly apps create "$APP" 2>/dev/null || echo "app $APP exists"
fly volumes list -a "$APP" 2>/dev/null | grep -q runner_work \
  || fly volumes create runner_work --size 25 --region "$REGION" --yes -a "$APP"
printf 'GH_RUNNER_PAT=%s\n' "$GH_RUNNER_PAT" | fly secrets import -a "$APP"   # via stdin, never echoed
fly deploy -a "$APP"
echo "→ verify: gh api repos/YOUR_GH_OWNER/YOUR_REPO/actions/runners --jq '.runners[]|.name+\" \"+.status'"
