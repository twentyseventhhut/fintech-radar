#!/usr/bin/env python3
"""Print the token usage from a `claude -p --output-format json|stream-json` capture.

Usage: claude_usage.py <capture-file> [label]
Handles both --output-format json (one object) and stream-json (jsonl → take the result event).
Emits one grep-able line:  TOKENS[<label>] input=.. output=.. cache_read=.. cache_creation=.. ...
so a run's Claude cost is visible in the GitHub Actions log. Never fails the step (exit 0 always)."""
import json, sys

path = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else "claude"
try:
    raw = open(path, encoding="utf-8").read().strip()
except Exception as e:
    print(f"TOKENS[{label}] usage unavailable (no capture: {e})"); sys.exit(0)

res = None
try:                                   # --output-format json = a single object
    res = json.loads(raw)
except Exception:                      # stream-json = jsonl; the last result event carries the totals
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except Exception:
            continue
        if ev.get("type") == "result":
            res = ev

if not isinstance(res, dict) or "usage" not in res:
    print(f"TOKENS[{label}] usage unavailable (run cancelled/incomplete or no usage field)"); sys.exit(0)

u = res.get("usage", {}) or {}
inp = u.get("input_tokens", 0) or 0
out = u.get("output_tokens", 0) or 0
cr = u.get("cache_read_input_tokens", 0) or 0
cc = u.get("cache_creation_input_tokens", 0) or 0
print(f"TOKENS[{label}] input={inp} output={out} cache_read={cr} cache_creation={cc} "
      f"billed_input={inp + cc} grand_total={inp + cc + cr + out} "
      f"turns={res.get('num_turns')} cost_usd={res.get('total_cost_usd')}")
