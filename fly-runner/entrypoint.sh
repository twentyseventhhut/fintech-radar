#!/usr/bin/env bash
# Registers this Fly Machine as a self-hosted runner for the repo at boot, then runs it.
# Needs a Fly secret GH_RUNNER_PAT = a GitHub token with repo Administration:read+write (to mint
# runner registration/removal tokens). On SIGTERM (fly deploy/restart) it de-registers cleanly.
set -euo pipefail
cd /home/runner/actions-runner

OWNER="${GH_OWNER:?set GH_OWNER}"; REPO="${GH_REPO:?set GH_REPO}"
: "${GH_RUNNER_PAT:?set the GH_RUNNER_PAT fly secret (repo-admin PAT to register the runner)}"
API="https://api.github.com/repos/${OWNER}/${REPO}"
URL="https://github.com/${OWNER}/${REPO}"
NAME="fly-${FLY_MACHINE_ID:-$(hostname)}"

# a persistent Fly volume mounts here root-owned — make it writable by the runner user
sudo chown -R runner:runner /home/runner/actions-runner/_work 2>/dev/null || true

_tok() {  # $1 = registration-token | remove-token
  curl -fsSL -X POST -H "Authorization: Bearer ${GH_RUNNER_PAT}" \
       -H "Accept: application/vnd.github+json" "${API}/actions/runners/$1" | jq -r .token
}

cleanup() {
  echo "de-registering runner ${NAME}…"
  ./config.sh remove --token "$(_tok remove-token)" || true
  exit 0
}
trap cleanup SIGINT SIGTERM

echo "registering runner ${NAME} → ${URL}"
./config.sh --url "$URL" --token "$(_tok registration-token)" --name "$NAME" \
  --labels self-hosted,fly,linux,x64 --work _work --unattended --replace

./run.sh & wait $!
