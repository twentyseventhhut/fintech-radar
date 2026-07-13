#!/usr/bin/env python3
"""Patch a News note's enrichment section — reliable writer for [2]/[3].

  note_patch.py (--note PATH | --story-id SID [--month YYYY-MM] | --match SUBSTR [--month YYYY-MM])
                --section context|challenge|post --content-file F
                [--set key=value ...] [--dry-run]

Locates exactly ONE note, replaces the body between the section's paired
<!-- enrichment:NAME --> ... <!-- /enrichment:NAME --> anchors with the file
content, and optionally sets frontmatter keys (e.g. enriched=true, status=enriched).

IMPORTANT: frontmatter `story_id` is NOT globally unique — the historical monthly
backfill reused per-month positional mention indices, so the same id appears in one
note per month (see dedupe.py). `(story_id, month)` IS unique. So `--story-id` alone
FAILS SAFE: if it matches >1 note it lists every candidate and refuses to patch.
Disambiguate with `--month YYYY-MM`, or target a single note with `--note`/`--match`.
"""
import argparse, fcntl, glob, os, re

NEWS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "News")
SECTIONS = ["context", "challenge", "post", "market_research", "earnings_review"]


def _month_of(path):
    return os.path.basename(os.path.dirname(path))


def _title_of(path):
    with open(path) as fh:
        head = fh.read(800)
    m = re.search(r'^title:\s*(.*)$', head, re.M)
    return m.group(1).strip().strip('"') if m else ""


def find_by_story_id(sid, month=None):
    """Every note whose frontmatter has `story_id: SID`, optionally scoped to a month."""
    pat = os.path.join(NEWS, month, "*.md") if month else os.path.join(NEWS, "*", "*.md")
    out = []
    for f in glob.glob(pat):
        with open(f) as fh:
            head = fh.read(4000)
        if re.search(rf'^story_id:\s*{re.escape(sid)}\s*$', head, re.M):
            out.append(f)
    return sorted(out)


def find_by_match(substr, month=None):
    pat = os.path.join(NEWS, month, "*.md") if month else os.path.join(NEWS, "*", "*.md")
    out = []
    for f in glob.glob(pat):
        if substr.lower() in _title_of(f).lower():
            out.append(f)
    return sorted(out)


def _ambiguous(kind, value, month, matches):
    scope = f" --month {month}" if month else ""
    lines = [f"--{kind} '{value}'{scope} matched {len(matches)} notes:"]
    for f in matches:
        lines.append(f"    [{_month_of(f)}] {_title_of(f)}")
        lines.append(f"        --note {os.path.relpath(f, NEWS)!r}")
    if matches:
        lines.append("disambiguate with --month YYYY-MM, or pass --note <path> / --match <title-substring>.")
    raise SystemExit("\n".join(lines))


def set_fm(text, key, val):
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    fm = parts[1]
    if re.search(rf'^{re.escape(key)}:.*$', fm, re.M):
        fm = re.sub(rf'^{re.escape(key)}:.*$', f'{key}: {val}', fm, count=1, flags=re.M)
    else:
        fm = fm.rstrip("\n") + f"\n{key}: {val}\n"
    return "---" + fm + "---" + parts[2]


def patch_section(text, name, content):
    """Replace the body between paired anchors <!-- enrichment:NAME --> ... <!-- /enrichment:NAME -->.
    Falls back to old single-anchor notes (replace up to next H2, then insert the closing anchor)."""
    s, e = f"<!-- enrichment:{name} -->", f"<!-- /enrichment:{name} -->"
    body = content.rstrip()
    if s in text and e in text:
        before = text.split(s, 1)[0]
        after = text.split(e, 1)[1]
        return f"{before}{s}\n{body}\n{e}{after}"
    if s in text:  # legacy single-anchor note
        before, after = text.split(s, 1)
        rest = after.split("\n## ", 1)
        tail = ("\n## " + rest[1]) if len(rest) > 1 else ""
        return f"{before}{s}\n{body}\n{e}\n{tail}"
    # neither anchor present → create the section (append at end), so reviewers land on older notes too
    heading = "## " + name.replace("_", " ").title()
    return f"{text.rstrip()}\n\n{heading}\n\n{s}\n{body}\n{e}\n"


def resolve(a):
    """Resolve the args to exactly one note path, or fail safe with candidates."""
    if a.note:
        f = a.note if os.path.isabs(a.note) else os.path.join(NEWS, a.note)
        if not os.path.exists(f):
            raise SystemExit(f"note not found: {f}")
        return f
    if a.match:
        matches = find_by_match(a.match, a.month)
        if len(matches) != 1:
            _ambiguous("match", a.match, a.month, matches)
        return matches[0]
    if a.story_id:
        matches = find_by_story_id(a.story_id, a.month)
        if len(matches) != 1:
            _ambiguous("story-id", a.story_id, a.month, matches)
        return matches[0]
    raise SystemExit("provide --note <path>, --story-id <id> [--month], or --match <title-substring> [--month]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", "--file", dest="note",
                    help="path to the note (absolute or relative to the vault News/ dir) — most precise")
    ap.add_argument("--story-id", help="locate by frontmatter story_id (fails safe + lists candidates if not unique)")
    ap.add_argument("--match", help="locate by a unique substring of the note title (ASCII-safe)")
    ap.add_argument("--month", help="YYYY-MM to scope --story-id / --match (disambiguator)")
    ap.add_argument("--section", required=True, choices=SECTIONS)
    ap.add_argument("--content-file")
    ap.add_argument("--set", action="append", default=[])
    ap.add_argument("--dry-run", action="store_true", help="resolve + report the target note, write nothing")
    a = ap.parse_args()

    f = resolve(a)
    if a.dry_run:
        fm = open(f).read().split("\n---", 1)[0]  # whole frontmatter (story_id sits below the sources list)
        m = re.search(r'^story_id:\s*(\S+)', fm, re.M)
        print(f"would patch [{a.section}] -> {os.path.relpath(f, NEWS)}  (story_id={m.group(1) if m else '?'})")
        return
    if not a.content_file:
        raise SystemExit("--content-file is required (unless --dry-run)")

    content = open(a.content_file).read()
    # Stage [2] runs enrich/market/earnings agents concurrently against the SAME
    # note (each patches a different section). Hold an exclusive lock across the
    # whole read-modify-write so concurrent patchers serialize instead of clobbering
    # each other's sections; distinct notes lock independently (parallelism preserved).
    with open(f, "r+") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            text = fh.read()
            text = patch_section(text, a.section, content)
            for kv in a.set:
                k, v = kv.split("=", 1)
                text = set_fm(text, k, v)
            fh.seek(0)
            fh.truncate()
            fh.write(text)
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)
    print(f"patched {a.section} -> {os.path.relpath(f, NEWS)}")


if __name__ == "__main__":
    main()
