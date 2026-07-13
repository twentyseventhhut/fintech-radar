#!/bin/zsh
# MANUAL/FALLBACK local run of the full daily pipeline (the regular schedule now runs in
# GitHub Actions — see .github/workflows/daily.yml). Runs from the repo root so Claude Code
# finds the project skill at .claude/skills/daily-fintech. Uses your logged-in Claude.
export PATH="$HOME/.local/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export ANTHROPIC_MODEL="claude-opus-4-8[1m]"   # Opus 4.8, 1M-token context (applies to subagents too)
REPO="$HOME/Documents/fintech update/Fintech update"
cd "$REPO" || exit 1
[ -f pipeline/.env ] && set -a && source pipeline/.env && set +a   # TELEGRAM_*/TELEGRAPH_* for local publish
DATE=$(date +%F)
DD="pipeline/state/daily/$DATE"; mkdir -p "$DD"
LOG="$DD/run.log"

echo "[$(date)] === daily start $DATE ===" >> "$LOG"
git pull --rebase --autostash >> "$LOG" 2>&1
python3 pipeline/mail_to_items.py >> "$LOG" 2>&1                       # raw_news → items.jsonl (local)
python3 pipeline/fintech_radar.py expand --since 4 >> "$LOG" 2>&1     # fetch primary-source texts
python3 pipeline/daily_source.py prep --date "$DATE" --since 4 --lookback 14 >> "$LOG" 2>&1
echo "[$(date)] model: $ANTHROPIC_MODEL" >> "$LOG"
claude -p "Use the daily-fintech skill to run the daily fintech pipeline for date $DATE." \
  --model "$ANTHROPIC_MODEL" \
  --dangerously-skip-permissions >> "$LOG" 2>&1
rc=$?
python3 pipeline/publish_telegraph.py --date "$DATE" >> "$LOG" 2>&1   # telegra.ph + Telegram (skips if creds unset)
./pipeline/semsearch/sem index >> "$LOG" 2>&1                         # keep semantic index fresh (incremental; OPENROUTER_API_KEY from .env)
( git add -A \
  && git -c core.quotepath=false commit -q -m "daily $DATE: news notes + digest (local)" \
  && git pull --rebase --autostash -q && git push -q ) >> "$LOG" 2>&1 \
  && echo "[$(date)] committed+pushed" >> "$LOG" \
  || echo "[$(date)] git: nothing to commit or push failed" >> "$LOG"
echo "[$(date)] === daily done $DATE (claude exit $rc) ===" >> "$LOG"
