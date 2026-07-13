#!/usr/bin/env python3
"""token_trace.py — decompose a `claude -p --output-format stream-json --verbose` capture:
WHERE the tokens go — totals, per turn, per tool, and (SEGMENTED) per sub-agent and per active Skill.

Usage: token_trace.py <stream-json.jsonl> [label]

Prints:
  TOKENS[label]      — grand totals (input/output/cache_read/cache_creation, cost).
  TRACE[label]       — turns, base context, tool-call counts, bytes injected per tool, skills.
  TRACE-SEG[label by=subagent] — per sub-agent TYPE (main + each Task subagent_type, aggregated,
                       with instance count): the clean decomposition for ingest's ~60 enrich agents.
  TRACE-SEG[label by=skill]    — per active Skill span (turns from a Skill call to the next), aggregated
                       by skill command: the clean decomposition for research-deep's plugin skills
                       (market-researcher:* vs earnings-reviewer:* vs "core" = no active skill).

Segmentation keys (confirmed from the stream): every `assistant` event carries `parent_tool_use_id`
(None = main agent, else the id of the Task tool_use that spawned that sub-agent) and its own per-turn
`message.usage`. A `Skill` tool_use switches the "active skill" for the SUBSEQUENT turns of that context.
Never fails the step (exit 0)."""
import json, sys
from collections import defaultdict

path = sys.argv[1]
label = sys.argv[2] if len(sys.argv) > 2 else "claude"


def load(p):
    for line in open(p, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if line.startswith("{"):
            try:
                yield json.loads(line)
            except Exception:
                continue


def U(u):  # normalize a usage dict -> (in, out, cache_read, cache_creation)
    u = u or {}
    return (u.get("input_tokens", 0) or 0, u.get("output_tokens", 0) or 0,
            u.get("cache_read_input_tokens", 0) or 0, u.get("cache_creation_input_tokens", 0) or 0)


turns = 0
final = {}
first_turn_ctx = None
tool_calls = defaultdict(int)
tool_result_bytes = defaultdict(int)
skills = defaultdict(int)
pending_tool = {}

task_type = {}                                         # Task tool_use_id -> subagent_type label
seg_sub = defaultdict(lambda: [0, 0, 0, 0, 0, set()])  # type -> [in,out,cr,cc,turns, {parent_ids}]
seg_skill = defaultdict(lambda: [0, 0, 0, 0, 0])       # skill -> [in,out,cr,cc,turns]
active_skill = {}                                      # parent_tool_use_id -> current skill label

for ev in load(path):
    ty = ev.get("type")
    if ty == "assistant":
        msg = ev.get("message") or {}
        u = msg.get("usage") or {}
        parent = ev.get("parent_tool_use_id")           # None = main agent
        if u:
            turns += 1
            i, o, cr, cc = U(u)
            if first_turn_ctx is None and parent is None:
                first_turn_ctx = i + cc
            # --- segment by sub-agent TYPE ---
            stype = "main" if parent is None else task_type.get(parent, "subagent(?)")
            s = seg_sub[stype]
            s[0] += i; s[1] += o; s[2] += cr; s[3] += cc; s[4] += 1
            if parent is not None:
                s[5].add(parent)
            # --- segment by ACTIVE skill (of this context) ---
            cur = active_skill.get(parent, "core")
            k = seg_skill[cur]
            k[0] += i; k[1] += o; k[2] += cr; k[3] += cc; k[4] += 1
        for b in (msg.get("content") or []):
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use":
                nm = b.get("name", "?")
                inp = b.get("input") or {}
                if nm == "Task":
                    if b.get("id"):
                        task_type[b["id"]] = str(inp.get("subagent_type") or inp.get("description", "task"))[:40]
                    nm2 = "Task:" + str(inp.get("subagent_type") or "")[:30]
                elif nm == "Skill":
                    cmd = str(inp.get("command") or inp.get("name") or inp.get("skill") or "?")[:60]
                    skills[cmd] += 1
                    active_skill[ev.get("parent_tool_use_id")] = cmd   # subsequent turns of THIS context -> this skill
                    nm2 = "Skill:" + cmd.split("(")[0].strip()
                else:
                    nm2 = nm
                tool_calls[nm2] += 1
                if b.get("id"):
                    pending_tool[b["id"]] = nm2
    elif ty == "user":
        msg = ev.get("message") or {}
        for b in (msg.get("content") or []):
            if isinstance(b, dict) and b.get("type") == "tool_result":
                nm = pending_tool.pop(b.get("tool_use_id"), "?")
                c = b.get("content")
                n = len(c) if isinstance(c, str) else len(json.dumps(c, ensure_ascii=False)) if c else 0
                tool_result_bytes[nm] += n
    elif ty == "result":
        i, o, cr, cc = U(ev.get("usage"))
        final = {"input": i, "output": o, "cache_read": cr, "cache_creation": cc,
                 "turns": ev.get("num_turns"), "cost": ev.get("total_cost_usd")}

if not final and turns:                                # no result event (cancelled) — sum segments
    tot = [0, 0, 0, 0]
    for v in seg_sub.values():
        for j in range(4):
            tot[j] += v[j]
    final = {"input": tot[0], "output": tot[1], "cache_read": tot[2], "cache_creation": tot[3],
             "turns": turns, "cost": None}
if not final:
    print(f"TOKENS[{label}] usage unavailable (no stream events)"); sys.exit(0)

inp, out, cr, cc = final["input"], final["output"], final["cache_read"], final["cache_creation"]
GT = inp + cc + cr + out
print(f"TOKENS[{label}] input={inp} output={out} cache_read={cr} cache_creation={cc} "
      f"billed_input={inp + cc} grand_total={GT} turns={final.get('turns')} cost_usd={final.get('cost')}")
print(f"TRACE[{label}] assistant_turns={turns} base_context≈{first_turn_ctx or '?'}t (re-read each turn → cache_read)")
if turns:
    print(f"TRACE[{label}] avg_cache_read/turn={cr // max(turns,1)}t avg_cache_creation/turn={cc // max(turns,1)}t")
print(f"TRACE[{label}] tool_calls: " + ", ".join(f"{n}×{c}" for n, c in sorted(tool_calls.items(), key=lambda x: -x[1])[:8]))
tb = sorted(tool_result_bytes.items(), key=lambda x: -x[1])[:8]
print(f"TRACE[{label}] context injected by tool_results (≈chars): " + ", ".join(f"{n}={b // 1000}k" for n, b in tb if b))
if skills:
    print(f"TRACE[{label}] skills invoked: " + ", ".join(f"{s}×{c}" for s, c in sorted(skills.items(), key=lambda x: -x[1])))


def _seg_line(kind, name, v, count=None):
    i, o, r, c = v[0], v[1], v[2], v[3]; t = i + c + r + o
    tag = f" ×{count}" if count else ""
    print(f"TRACE-SEG[{label} by={kind}] {name}{tag}  in={i} out={o} cache_read={r} cache_creation={c} "
          f"total={t // 1000}k share={100*t//max(GT,1)}% billed={(i+c)//1000}k turns={v[4]}")


# --- per sub-agent type (share of grand_total), biggest first ---
for name, v in sorted(seg_sub.items(), key=lambda kv: -(kv[1][0] + kv[1][1] + kv[1][2] + kv[1][3])):
    _seg_line("subagent", name, v, count=len(v[5]) if v[5] else None)
# --- per active skill span, biggest first ---
for name, v in sorted(seg_skill.items(), key=lambda kv: -(kv[1][0] + kv[1][1] + kv[1][2] + kv[1][3])):
    _seg_line("skill", name, v)
