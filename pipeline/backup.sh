#!/bin/zsh
# Lean backup: only the irreplaceable raw data + small enrichment artifacts.
# Keeps 3 copies. Big deduped CSVs are NOT backed up (regenerable from clusters+cache).
cd "$(dirname "$0")" || exit 1
mkdir -p backups
ts=$(date +%Y%m%d-%H%M%S)
cp data/items.jsonl         "backups/items-$ts.jsonl"  2>/dev/null
cp state/source_cache.jsonl "backups/cache-$ts.jsonl"  2>/dev/null
tar -czf "backups/months-json-$ts.tgz" \
  months/*/titles.json months/*/extra.json months/*/deduped.csv 2>/dev/null
for pat in 'items-*.jsonl' 'cache-*.jsonl' 'months-json-*.tgz'; do
  ls -1t backups/$pat 2>/dev/null | tail -n +3 | xargs rm -f 2>/dev/null
done
echo "[backup $ts] items=$(wc -l < data/items.jsonl) cache=$(wc -l < state/source_cache.jsonl) backups=$(du -sh backups | cut -f1)"
