---
name: daily-fintech
description: >
  Оркестратор ежедневного финтех-пайплайна Fintech Radar: [1] инкрементальный сбор
  новых новостей в базу заметок, [2] триаж top-K + контекст-обогащение [0]–[4] прямо
  в заметки, [3] дневной дайджест-пост. Идемпотентно/возобновляемо. Вызывать, когда
  просят «прогнать ежедневный финтех-пайплайн» за дату (по умолчанию сегодня).
---

# Daily Fintech Pipeline — orchestrator (ДВА режима)

Работает в ОДНОМ из двух режимов; режим задаёт вызывающий воркфлоу:
- **INGEST-ENRICH** (каждые 5 ч): Подготовка → [1] сбор новых заметок → [2] обогащение
  ТОП-70% новых заметок цикла. НЕ публикует. Обогащённые заметки копятся.
- **PUBLISH** (раз в день, 15:00 МСК / 12:00 UTC): только [3] — собирает дайджест из УЖЕ
  обогащённых заметок и пишет его в ОТДЕЛЬНЫЙ Obsidian-vault `digest/`. НЕ собирает/НЕ обогащает.

CWD = корень репозитория. Заметки — `News/`, дайджесты — `digest/` (отдельный vault).
Артефакты цикла — `state/daily/DATE/`. Каждый шаг ПРОПУСКАЕТ уже сделанное (резюмируемо).
Итог логируй в `state/daily/DATE/run.log` (через `>>`). На агентных шагах — инструмент Task
с general-purpose агентом и промптом из раздела «Промпты агентов».

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

## [2] Триаж + обогащение ТОП-70% (режим INGEST-ENRICH)
3. `python3 daily_pool.py --date DATE --days 7 --out state/daily/DATE/pool.json` (un-enriched, окно 7 дн).
4. Если `state/daily/DATE/picks.json` отсутствует → агент **«[2] ranker»** → ТОП-70% по КАЖДОМУ
   рынку (международный + российский) отдельно; нижние ~30% мусора отбрасывай; ≤20 за цикл,
   меньший рынок не зануляй (режь сначала больший).
5. Для КАЖДОГО пика, чья заметка ещё не `enriched: true`, ПАРАЛЛЕЛЬНО (один Task-вызов с
   несколькими агентами): **«[2] enrich»** + **«[2] market»** (всегда) + **«[2] earnings»**
   (по триггеру: тег `type/earnings` ИЛИ финрез в [0]). Каждый пишет в свою секцию заметки
   через `note_patch.py` и ставит `enriched:true` / `status:enriched` / `importance:N`.
   ЗДЕСЬ НЕ публикуем — обогащённые заметки копятся как кандидаты для PUBLISH.
   Финал (ingest-enrich): `run.log` → `DATE cycle: <N> new, <K> enriched`. Коммит/пуш делает воркфлоу.

## [3] Дайджест → отдельный vault `digest/` (режим PUBLISH)
6. `python3 daily_pool.py --date DATE --days 7 --enriched --out state/daily/DATE/pubpool.json`
   (pubpool = ОБОГАЩЁННЫЕ, ещё НЕ опубликованные заметки; рядом — `recent_published.json` для дедупа).
7. Если `digest/DATE.md` отсутствует → агент **«[3] digest»** → ТОП-30 из pubpool, ПЛОСКИЙ v5 формат
   (без сворачивания), ДВЕ секции рынка (🌍 Международный / 🇷🇺 Российский), пишет `digest/DATE.md`
   (в отдельный vault), ставит `status:published` на заметки.
8. Воркфлоу `publish` затем публикует `digest/DATE.md` в telegra.ph и постит ссылку в Telegram-канал
   (`pipeline/publish_telegraph.py`, токены из секретов). Финал (publish): `run.log` → `DATE published: <K> items`.

---

# Промпты агентов (подставь DATE)

## [1] brain  (cluster + dedup vs base + title + tags; БЕЗ веб-поиска)
> You are stage [1]: cluster new mentions, drop ones already in the archive, emit clean new stories. NO web search.
> Read `pipeline/state/daily/DATE/compact.txt` (NEW mentions, tab-separated:
> `id  post_date  [channel]  text`), `pipeline/state/daily/DATE/recent_stories.json`
> (already-archived [{id,date,title}]), and `pipeline/tag_instructions.md`.
> 1) CLUSTER mentions of the SAME event (collect mention_ids); merge only true same-event dups.
> 2) DROP any cluster already represented in recent_stories.json. Match by COMPANY + core event/figures, NOT
>    by headline wording or source — a reworded retelling, a different outlet's version, or a re-report of an
>    already-archived deal / prior-period financials is a DUPLICATE (drop it), even if the title differs.
>    ALSO DROP pure ads / sponsored / job-postings / event-invites / feedback-surveys / newsletter housekeeping — keep genuine news AND analysis.
> 3) For each SURVIVING new story emit {mention_ids, title (clean ≤12-word EN headline; essays→publication-prefixed),
>    tags (3–6 namespaced per tag_instructions: 1–2 company/ + 1–2 industry/ + 1 region/ + 1 type/),
>    date (the REAL date the event happened/was announced, YYYY-MM-DD — infer from the mention text or known facts;
>    if genuinely unknown, fall back to the post_date column. Do NOT just copy post_date when the text implies another day.)}.
> Write `pipeline/state/daily/DATE/newstories.json` (STRICT JSON array). Validate parses.
> Report one line: "N new stories, dropped D duplicates".

## [2] ranker  (subjective top-70% of EACH market — intl + ru; no formula)
> Read `pipeline/state/daily/DATE/pool.json` (recent un-enriched news [{story_id,date,title,tags,dup_candidates}];
> `dup_candidates` = recently-published notes AND other candidates that SHARE a company tag — the focused same-event suspects)
> AND `pipeline/state/daily/DATE/recent_published.json` (stories already published in recent daily digests, last ~3 weeks).
> STEP 1 — BUCKET every candidate into ONE of two markets:
>   • **ru** (Russian market, РФ) = tag `region/ru` OR a clearly Russia (РФ) subject — Russian banks /
>     fintechs / regulators / companies (ЦБ РФ, СБП, Сбер, Т-Банк/Тинькофф, Альфа, ВТБ, Wildberries/Ozon
>     fintech, Яндекс, цифровой рубль, …) or Russia-focused items from the Russian-language source channels.
>     (A purely CIS story with no Russia angle — Uzbekistan/Kazakhstan/etc. — is **intl**, not ru.)
>   • **intl** (international market) = everything else.
> STEP 2 — Within EACH bucket INDEPENDENTLY select the TOP ~70% by SUBJECTIVE judgment of SCALE × genuine
>   INCREMENTAL added-value (no numeric formula; no near-duplicates within the bucket): keep the genuinely
>   newsworthy majority, DROP only the bottom ~30% (clear noise / marginal / ad-like). Round UP per bucket.
>   NEVER let one market crowd out the other — if a bucket has even 1–2 items, still keep its top ~70%
>   (≥1). Soft cap 20 picks TOTAL per cycle; if the combined top-70% exceeds 20, trim from the LARGER
>   bucket first — never zero out or starve the smaller bucket. These picks get the FULL heavy enrichment below.
> DEDUP (use each candidate's `dup_candidates` list — the same-company suspects — plus recent_published.json):
> for each candidate, check whether any dup_candidate / recent_published row is the SAME real-world event
> EVEN IF the title wording or source URL differs (compare the event, not the headline). If the twin is
> already PUBLISHED → DROP the candidate. If two CANDIDATES are the same event → keep only ONE (the
> higher-scale framing) and drop/merge the other. Keep a candidate ONLY if it carries a genuine NEW material
> development (a real follow-up: e.g. "in talks" → "signed deal" with NEW terms; a NEW reporting period), NOT
> a reworded reprint, a different-source retelling, or a re-report of an already-published period's results.
> Write `pipeline/state/daily/DATE/picks.json` STRICT JSON {"picks":[{story_id,title,reason,market}]}  (market = "ru"|"intl").
> Report: "picked N (intl I / ru R): <titles>".

## [2] enrich  (one per pick; INTO the note; internal vault search + external research)
> Stage [2] deep enrichment of ONE story, written INTO its note. Method: `pipeline/skills/context-enrichment.md`
> ([0]–[4] + red-team gate vs PR). LANGUAGE: work and WRITE the enrichment in ENGLISH — search queries AND note content in English, since the corpus is English and that maximizes search + semantic recall. (Russian is produced ONLY later, in [3].) Skeptical; never invent.
> Target = the pick with title "<TITLE>" (month = DATE's YYYY-MM). Read its note:
> `grep -rl "<UNIQUE ASCII title substring>" "News/<YYYY-MM>/"` then read it.
> Run TWO research passes IN PARALLEL — co-equal, neither is optional or second:
> 1) INTERNAL (semantic search over the corpus, NOT grep): `./pipeline/semsearch/sem search "<company / event / key terms>" --k 8 --json`
>    (hybrid embeddings+BM25 over 15k+ notes; optional filters `--company <slug>` / `--type <t>` / `--since`). Build the query in ENGLISH.
>    Pull 2–4 relevant prior notes (the company, similar events, competitors), cite as [[wikilinks]] (filename w/o .md).
>    Fallback if the index is unavailable: `grep -rl "company/<x>" News/`.
> 2) EXTERNAL (WebSearch) — runs ALONGSIDE (1), NOT a fallback to it: dated timeline, prior art, adoption (live vs announced), exact/fresh numbers, competitors.
> Both passes always run; synthesize across both.
> 3) FRESHNESS / DUPLICATE VERDICT (MANDATORY — drives the dedup gate): from the INTERNAL retrieval, decide if
>    this event is genuinely new. Set `freshness=stale` (and `duplicate_of=<[[exact prior note]]>`, filename w/o .md)
>    when the SAME announcement / deal / figures is already covered by an existing note — a reprint, a re-framing
>    (e.g. GBP vs USD of the SAME results), a different-source retelling, or a re-report of an already-published
>    period's financials. Otherwise `freshness=fresh`. A genuine NEW development (new terms, a NEW reporting
>    period, a real "talks → signed deal" follow-up) is fresh. When in doubt and a near-identical prior note
>    exists, mark stale — a dropped reprint costs less than a published duplicate.
> 4) Write /tmp/ctx_<slug>.md ([0]–[4] with [[wikilinks]]+source URLs) and /tmp/chl_<slug>.md (10–15 second-order
>    red-team Qs each answered or "open" + final "Importance: N/5 — rationale"). All in English.
> 5) Inject (refine --match if it reports !=1):
>    `python3 pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section context  --content-file /tmp/ctx_<slug>.md`
>    `python3 pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section challenge --content-file /tmp/chl_<slug>.md --set enriched=true --set status=enriched --set importance=N --set freshness=<fresh|stale>`
>    (if stale, ALSO add `--set duplicate_of="[[<prior note filename w/o .md>]]"`).
> Report: "<slug> importance N/5 (fresh|stale)".

## [2] market  (Market Researcher — EVERY pick)
> Stage [2] market research for ONE pick, written INTO its note. Method: `pipeline/skills/market-research.md`. LANGUAGE: ENGLISH (queries + note content); skeptical, never invent.
> Target = pick "<TITLE>" (month YYYY-MM). Read its note, follow the method (sector context + in-base comps via `./pipeline/semsearch/sem search "<english query>" --k 8 --json` or grep + WebSearch + risk flags), write /tmp/mr_<slug>.md, then:
>   `python3 pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section market_research --content-file /tmp/mr_<slug>.md`
> IR GROUNDING (ALWAYS when the pick's `company/<slug>` is a covered company — i.e. the slug is a key in
> `pipeline/ir/ir_coverage.json`): pull that company's own filed results and fold them into market_research as
> PRIMARY evidence. Steps: (1) read `pipeline/ir/ir_latest.json` → `<slug>.latest_result` + the relevant
> `categories` (latest 10-Q/10-K/20-F/earnings_release/presentation) for date + doc link; (2) run
> `./pipeline/semsearch/sem search "<company> revenue growth guidance segments" --db pipeline/state/irdb --company <slug> --k 8 --json`
> (optionally `--doc <10-q|10-k|earnings_release|…>` to pick a form, `--since <YYYY-MM-DD>` for a period).
> Use the REAL reported figures (cite each hit's `drive_url` — the redirect to the full file in Drive — or
> its `url` fallback); when a filing is newer/more authoritative than the web, prefer it. If `pipeline/state/irdb` is absent, skip silently.
> Report: "<slug> market: N risk flags[ +IR]".

## [2] earnings  (Earnings Reviewer — if type/earnings OR financials reported OR IR-covered company)
> Run when triggered (tag `type/earnings`, reported financials in [0], OR the pick's `company/<slug>` is a
> covered company in `pipeline/ir/ir_coverage.json`). Method: `pipeline/skills/earnings-review.md`. LANGUAGE:
> ENGLISH (queries + note content), exact numbers, never invent; if there's genuinely no results data, say so briefly and stop.
> IR-COVERED → use the company's OWN filings as the PRIMARY source: read `pipeline/ir/ir_latest.json[<slug>]`
> for the latest period + doc links, and `./pipeline/semsearch/sem search "<company> results revenue guidance" --db pipeline/state/irdb --company <slug> --k 8 --json`
> (`--doc <form>` / `--since <date>` to target a form/period). Quote the reported figures and cite each hit's
> `drive_url` (redirect to the full filing in Drive; `url` fallback). Prefer the filing over web/consensus for the actuals.
> Target = pick "<TITLE>". Follow the method (reported figures + growth, vs prior/consensus, guidance, thesis-flags), write /tmp/er_<slug>.md, then:
>   `python3 pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section earnings_review --content-file /tmp/er_<slug>.md`
> Report: "<slug> earnings: beat/miss/in-line".

## [3] digest  (PUBLISH mode → separate Obsidian vault `digest/`, flat v5, TWO market sections)
> Stage [3]: build the daily fintech digest into the SEPARATE Obsidian vault `digest/`. SOURCE LANGUAGE:
> the enriched notes ([0]–[4], market_research, earnings_review) are in ENGLISH — SYNTHESIZE and TRANSLATE
> into the RUSSIAN post here (Russian produced ONLY at this stage). Authority =
> `pipeline/skills/final-formatting-rules.md` («## Формат отдельного vault (ПЛОСКИЙ v5, две секции рынка)»
> + «## Приоритетные уточнения (v5)» + the 7 «Эталонные посты (бенчмарк v5)»). Match the v5 benchmarks in
> structure/density/voice; IGNORE the older paragraph templates.
> Inputs = `pipeline/state/daily/DATE/pubpool.json` (ENRICHED, not-yet-published candidates
> [{story_id,date,title,tags,dup_candidates}]) + `pipeline/state/daily/DATE/recent_published.json` (dedup).
> (daily_pool already DROPPED notes the enricher marked `freshness:stale`/`duplicate_of` — those won't appear.)
> For each candidate find+read its note (`## Контекст` [0]–[4], `## Market Research`, `## Earnings Review`,
> frontmatter importance). DEDUP using each candidate's `dup_candidates` (same-company suspects) + recent_published:
> DROP any candidate whose event is the SAME as an already-published one EVEN IF the wording/source differs
> (compare the event, not the headline); and where TWO candidates are the same event (e.g. one launch named with
> two different partners), MERGE them into ONE item rather than printing both. Keep only genuine new developments.
> BUCKET each surviving item into one of two markets — **Российский** (tag `region/ru` OR a Russia (РФ)
> subject, same rule as the ranker; CIS-without-Russia → Международный) vs **Международный** (everything
> else). Within EACH bucket order by
> importance desc. Take the TOP 30 across both buckets PROPORTIONALLY — never drop the whole Russian bucket.
> PER-ITEM FORMAT (FLAT v5, NO collapsing): a BOLD headline with the source link INLINE on the action verb
> (`**Subject [глагол](url) …**`) + 2–5 dense RU bullets (`* `, nested tab-sub-bullets where useful for
> factor analysis) — the condensed analyst synthesis exactly as in the v5 benchmark posts. Decimal POINT;
> no «—» connector; no «не X, а Y»; no hype; explain unfamiliar entities briefly; add the "why it grew /
> strategic bet" factor + systematized metrics with growth where relevant.
> The deep [0]–[4] + market/earnings STAYS in the News notes (written there at [2]) — do NOT dump it into the post.
> Write `digest/DATE.md`:
>   line 1 = `# Fintech дайджест за DATE`, blank line;
>   `## 🌍 Международный рынок`, blank, the international items (flat v5), blank;
>   `## 🇷🇺 Российский рынок`, blank, the Russian items (flat v5).
>   If a bucket is empty, still write its header + one line `_За день значимых новостей нет._`.
>   NO «Статус:» line, NO telegram caption, NO lead/summary paragraph — just the two section headers + items.
> Then mark each included note published: write /tmp/post_<n>.md = "Опубликовано в дайджесте [[digest/DATE]] (DATE)." and run
>   `python3 pipeline/note_patch.py --match "<substr>" --month <YYYY-MM> --section post --content-file /tmp/post_<n>.md --set status=published`
> Report: "digest: K items (intl I / ru R) -> digest/DATE.md".
