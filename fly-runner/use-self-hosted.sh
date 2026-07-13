#!/usr/bin/env bash
# Point every workflow at the Fly self-hosted runner. Run ONLY after the runner shows `online`.
set -euo pipefail
cd "$(dirname "$0")/.."
sed -i.bak 's/runs-on: ubuntu-latest/runs-on: [self-hosted, fly]/' .github/workflows/*.yml
rm -f .github/workflows/*.yml.bak
echo "switched to self-hosted:"; grep -rn "runs-on:" .github/workflows/*.yml
