---
name: daily-fintech
description: >
  Оркестратор ежедневного финтех-пайплайна Fintech Radar: [1] инкрементальный сбор
  новых новостей в базу заметок, [2] триаж top-K + контекст-обогащение [0]–[4] прямо
  в заметки, [3] дневной дайджест-пост. Идемпотентно/возобновляемо. Вызывать, когда
  просят «прогнать ежедневный финтех-пайплайн» за дату (по умолчанию сегодня).
---

# Daily Fintech Pipeline — orchestrator

Прогоняет 3 стадии за DATE (YYYY-MM-DD, по умолчанию сегодня). Каждый шаг ПРОПУСКАЕТ уже
сделанное (резюмируемость). Рабочая папка (CWD): `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline`.
Хранилище: `/Users/a.v.bakharev/Documents/fintech update/Fintech update` (заметки в `News/`,
посты в `Posts/`). Все артефакты дня — в `state/daily/DATE/`.

Запускай шаги по порядку; на каждом агентном шаге используй инструмент Task с
general-purpose агентом и промптом из раздела «Промпты агентов». Логируй краткий итог
каждого шага в `state/daily/DATE/run.log` (через `>>`).

## Подготовка (если launchd-обёртка не сделала)
Если нет `state/daily/DATE/mentions.json`:
```
git pull --rebase --autostash   # свежие письма приходят облачным ingest
python3 fintech_radar.py expand --since 4
python3 daily_source.py prep --date DATE --since 4 --lookback 14
```

## [1] Инкрементальный сбор
1. Если `state/daily/DATE/newstories.json` отсутствует И `mentions.json` непустой → запусти агента **«[1] brain»**.
2. `python3 daily_source.py assemble --date DATE --newstories state/daily/DATE/newstories.json`
   (пропусти assemble, если newstories.json пуст/отсутствует).

## [2] Триаж + контекст-обогащение (в заметки)
3. `python3 daily_pool.py --date DATE --days 7 --out state/daily/DATE/pool.json`
4. Если `state/daily/DATE/picks.json` отсутствует → запусти агента **«[2] ranker»** (top-6).
5. Для КАЖДОГО пика, чья заметка ещё не `enriched: true`, запусти агента **«[2] enrich»**
   — ПАРАЛЛЕЛЬНО (все пики разом, один Task-вызов с несколькими агентами). Каждый пишет
   context+challenge в заметку через `note_patch.py` и ставит `enriched: true`, `importance: N`.

## [3] Дневной дайджест (пост)
6. Если `Posts/DATE.md` отсутствует → запусти агента **«[3] digest»** → он пишет
   `Posts/DATE.md` и проставляет обратные ссылки + `status: published` в заметки.

## Финал
Допиши в `state/daily/DATE/run.log`:
`DATE done: <N> new stories, <K> enriched, digest=<yes|no>` и кратко отчитайся.

---

# Промпты агентов (подставь DATE)

## [1] brain  (cluster + dedup vs base + title + tags; БЕЗ веб-поиска)
> You are stage [1]: cluster new mentions, drop ones already in the archive, emit clean new stories. NO web search.
> Read `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/compact.txt` (NEW mentions, tab-separated:
> `id  post_date  [channel]  text`), `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/recent_stories.json`
> (already-archived [{id,date,title}]), and `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/tag_instructions.md`.
> 1) CLUSTER mentions of the SAME event (collect mention_ids); merge only true same-event dups.
> 2) DROP any cluster already represented in recent_stories.json.
> 3) For each SURVIVING new story emit {mention_ids, title (clean ≤12-word EN headline; essays→publication-prefixed),
>    tags (3–6 namespaced per tag_instructions: 1–2 company/ + 1–2 industry/ + 1 region/ + 1 type/),
>    date (the REAL date the event happened/was announced, YYYY-MM-DD — infer from the mention text or known facts;
>    if genuinely unknown, fall back to the post_date column. Do NOT just copy post_date when the text implies another day.)}.
> Write `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/newstories.json` (STRICT JSON array). Validate parses.
> Report one line: "N new stories, dropped D duplicates".

## [2] ranker  (subjective top-K; no formula)
> Read `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/pool.json` (recent un-enriched news [{story_id,date,title,tags}]).
> Select the TOP 6 by SUBJECTIVE judgment of SCALE × genuine INCREMENTAL added-value (no numeric formula;
> no near-duplicates; importance over diversity).
> Write `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/picks.json` STRICT JSON {"picks":[{story_id,title,reason}]}.
> Report: "picked N: <titles>".

## [2] enrich  (one per pick; INTO the note; internal vault search + external research)
> Stage [2] deep enrichment of ONE story, written INTO its note. Method: `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/skills/context-enrichment.md`
> ([0]–[4] + red-team gate vs PR). Russian. Skeptical; never invent.
> Target = the pick with title "<TITLE>" (month = DATE's YYYY-MM). Read its note:
> `grep -rl "<UNIQUE ASCII title substring>" "/Users/a.v.bakharev/Documents/fintech update/Fintech update/News/<YYYY-MM>/"` then read it.
> 1) INTERNAL: grep the vault for related prior notes by the main company/tags (e.g. `grep -rl "company/<x>" ".../News"`);
>    skim 2–4; cite as [[wikilinks]] (filename w/o .md).
> 2) EXTERNAL: WebSearch — dated timeline, prior art, adoption (live vs announced), exact numbers, competitors.
> 3) Write /tmp/ctx_<slug>.md ([0]–[4] with [[wikilinks]]+source URLs) and /tmp/chl_<slug>.md (10–15 second-order
>    red-team Qs each answered or "открыто" + final "Важность: N/5 — обоснование").
> 4) Inject (refine --match if it reports !=1):
>    `python3 /Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section context  --content-file /tmp/ctx_<slug>.md`
>    `python3 /Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section challenge --content-file /tmp/chl_<slug>.md --set enriched=true --set status=enriched --set importance=N`
> Report: "<slug> importance N/5".

## [3] digest  (the day's post)
> Stage [3]: build the daily fintech digest. FOLLOW `/Users/a.v.bakharev/.claude/skills/fintech-news-digest/SKILL.md`
> (Russian, "News & Trends", NO emoji, dense, numbers, decimal commas, foreign brands Latin / Russian Cyrillic,
> tail [источник](url) per item, items ordered by importance desc).
> Inputs = today's enriched picks: read `/Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/state/daily/DATE/picks.json`; for each,
> find + read its note (use its "## Контекст" [0]–[4] + "## Первоисточники" + frontmatter importance).
> Write `/Users/a.v.bakharev/Documents/fintech update/Fintech update/Posts/DATE.md`:
>   `# Fintech дайджест — DATE` / `_Статус: top-K обогащённых новостей дня._` / blank / тематический дайджест.
> Then back-link each included note: write /tmp/post_<n>.md = "Включено в дайджест [[Posts/DATE]] — DATE." and run
>   `python3 /Users/a.v.bakharev/Documents/fintech update/Fintech update/pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section post --content-file /tmp/post_<n>.md --set status=published`
> Report: "digest: K items -> Posts/DATE.md".
