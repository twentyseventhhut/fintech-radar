# Fintech Radar — self-hosted CI runner on Fly.io

Move the GitHub Actions **compute** off GitHub-hosted runners (which burn the private-repo minute
quota) onto one always-on Fly Machine. GitHub bills **0 minutes** for self-hosted runners. The repo,
secrets, Releases, cron and logs stay on GitHub — only where the jobs execute changes.

Only the LLM *inference* runs in Anthropic's cloud; the `claude -p` agent loop + tools + python all run
on this runner (that's the wall-clock time GitHub used to bill). Claude **Max** limits are unaffected.

## One-time setup (needs your Fly login + a GitHub PAT — I can't do these for you)

1. **Log in to Fly** (opens a browser) and make sure billing/a card is set:
   ```
   fly auth login
   ```
2. **Create a GitHub PAT** to let the Machine register itself:
   github.com → Settings → Developer settings → **Fine-grained token** → repo `YOUR_GH_OWNER/YOUR_REPO`
   → Repository permissions → **Administration: Read and write** → copy the token.
3. **Deploy** (from this `fly-runner/` dir):
   ```
   cd fly-runner
   fly apps create fintech-runner
   fly volumes create runner_work --size 25 --region fra --yes
   fly secrets set GH_RUNNER_PAT=<paste-the-PAT>       # stays only in Fly, not in git
   fly deploy
   ```
   `deploy.sh` runs the four commands above (export `GH_RUNNER_PAT=…` first).
4. **Confirm the runner is online:**
   ```
   gh api repos/YOUR_GH_OWNER/YOUR_REPO/actions/runners --jq '.runners[]|.name+" "+.status'
   ```
   You want `… online`.
5. **Switch the workflows to it** (do this ONLY after step 4 — otherwise jobs queue with no runner):
   ```
   bash fly-runner/use-self-hosted.sh && git add -A && git commit -m "ci: run on self-hosted Fly runner" && git push
   ```
   Revert anytime with `bash fly-runner/use-github-hosted.sh`.

## Operating it
- **Logs:** `fly logs -a fintech-runner`
- **Resize** (if IR indexing OOMs): edit `memory_mb` in `fly.toml` → `fly deploy`. Drop to `2048` to save cost.
- **Cost:** ~4 GB always-on ≈ $15–25/mo + 25 GB volume ≈ $4/mo. Cheaper than the GitHub overage at this usage.
- **One runner = jobs serialize.** A research poll can wait behind a running ingest-enrich (~25 min). If that
  matters, lower the research cron to `*/30`, or run a 2nd runner Machine (`fly scale count 2`, +RAM cost).
- **Redeploy** re-registers cleanly (SIGTERM de-registers the old runner).
