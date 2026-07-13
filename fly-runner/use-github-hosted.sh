#!/usr/bin/env bash
# Revert every workflow back to GitHub-hosted runners (undo use-self-hosted.sh).
set -euo pipefail
cd "$(dirname "$0")/.."
sed -i.bak 's/runs-on: \[self-hosted, fly\]/runs-on: ubuntu-latest/' .github/workflows/*.yml
rm -f .github/workflows/*.yml.bak
echo "switched to github-hosted:"; grep -rn "runs-on:" .github/workflows/*.yml
