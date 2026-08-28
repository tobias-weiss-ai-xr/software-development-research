# Changelog

## [Unreleased]
- **Abstract enrichment (curate, don't delete):** new
  `scripts/fetch/fetch_abstracts.py` backfills missing abstracts for real
  papers from OpenAlex (`abstract_inverted_index`); recovers what OpenAlex
  has without deleting anything. First run reclaimed **75** abstracts
  (closed-access Springer/Nature/IEEE lack them in OA, so recovery is
  partial by design).
- **Precision curation:** triage now flags `low-confidence-source` (no
  abstract + explicitly untrusted source: ResearchGate self-uploads, `irjmets`
  /`ijsrem`/`isi` predatory venues, `10.32388`). Audited one-shot removal
  dropped **16** such entries; `docs/research/removed_entries.yaml` now logs
  **103** total removals (52 off-topic + 22 SEO-spam + 16 untrusted + 12
  predatory + 1 spam-title). `make enrich` added.
- **Contract aligned to policy:** validator no longer warns on Research
  Square (`10.21203`) or HAL (accepted sources); still warns on
  techrxiv/preprints.org/zenodo-doi/rgdoi. `research_config.load_yaml()`
  restored (a skeleton-sync had dropped it, silently breaking 8 callers)
  and covered by a regression test.
- **Spec:** added "Curation & Quality Gates" requirement (accepted sources,
  read-only triage, audited/reversible removal, abstract enrichment).
- **CI:** `validate.yml` adds a daily `sync-on-drift` job that regenerates
  README/stats/bib and opens a fix-PR on derived-artifact drift.
- **Tests:** +18 (65 total) — load_yaml regression, fetch_abstracts, R.S./HAL
  acceptance, low-confidence-source.
  Square preprints (10.21203) that the previous audited cleanup had removed
  (5934 papers overall: 6021 − 87 other removals + 28 restored). The triage
  tool no longer flags Research Square or HAL as vanity-platform; the contract
  keeps an advisory (non-blocking) warning for both.
- **Curation pass (audited):** removed 87 confirmed-pollution entries
  (6021 → 5934, taxonomy saturation unchanged at 97.5%): SEO-spam content
- **Performance:** all corpus loads now use the PyYAML C loader via new
  `research_config.load_yaml()` (CSafeLoader with SafeLoader fallback).
  `validate_papers.py` 41s → 5.5s, `standard_stats.py` ~60s → ~5s, and every
  tool (topic_planner / trend_scanner / landscape_analyzer / brief_generator /
  concept-graph / export_bibtex) got the same 10x+ parse speedup. Routed
  through the existing single-source-of-truth loader in 14 scripts + 6 tools.
  Also regenerated stale `paper/references.bib` (21,200 lines of accumulated
  drift — the BibTeX exporter had not been run since the last ingestion).
- **Corpus triage tool:** new read-only `tools/triage_corpus.py` flags
  vanity-platform preprints (32), no-abstract unvetted bulk-ingest entries
  (781), out-of-domain topics (56), and suspicious venues (12) —
  860/6021 (14.3%) flagged overall — into `docs/research/corpus_triage.md`.
  Deleting nothing; human reviews the report. `make triage`.
- **Spec–contract–test pyramid:** added the missing test layer and the spec
  layer. `openspec/specs/papers-corpus/` now documents the corpus contract
  (data model, validation gates, pipeline, agent guardrails) in Gherkin
  scenarios; `tests/` adds a hermetic, network-free pytest suite (37 tests,
  ~4s) covering `validate_papers`, `research_config`, `generate_readme`,
  `standard_stats` helpers, `saturate_papers` dedup, and `export_bibtex`.
  CI (`validate.yml`) now runs `pytest` and `generate_readme.py --check`.
  Re-ran the pipeline to repair stale generated artifacts (README was
  2,469 lines out of date vs. `papers.yaml`).
- **Contract hardening:** `validate_papers.py` now flags non-peer-reviewed
  Research Square DOIs (`doi.org/10.21203/...`) via the vanity-domain check
  (37 corpus entries were previously invisible to the quality gate).
- **Bug fix:** All arXiv API calls now use `https://` instead of `http://`
  (`fetch_new_papers.py`, `fetch_metadata.py`, `saturate_papers.py`).  Many
  networks block plain HTTP; HTTPS is required for arXiv's API.
- **Bug fix:** `fetch_new_papers.py` — fixed `NameError` (`QUERIES` → `queries`) that
  crashed multi-query arXiv discovery runs.
- **Bug fix:** `fetch_openalex_bulk.py` — `reconstruct_abstract()` and
  `sanitize_date()` no longer return the literal string `"papers"` on empty/bad
  input; they return `""` as intended.
- **Config-driven trend keywords:** `standard_stats.py`, `trend_scanner.py`, and
  `landscape_analyzer.py` now read `trend_keywords` from `config/taxonomy.yaml`
  (via `research_config.get_trend_keywords()`), falling back to the built-in list.
  Each repo can now define topic-specific burst keywords.
- **Config-driven subcategory classification:** `fetch_new_papers.py` now exports
  `classify_subcategory(title, abstract, cfg)` that reads `subcategory_keywords`
  from `taxonomy.yaml` first, then falls back to heuristics. `fetch_other_sources.py`
  picks this up automatically via its existing import.
- **Config-driven display names:** `topic_planner.py`, `trend_scanner.py`,
  `landscape_analyzer.py`, `brief_generator.py`, and `standard_stats.py` now use
  `research_config.category_display()` / `subcategory_display()` for proper
  display names instead of raw title-casing of kebab IDs.
- **Config-driven OpenAlex mailto:** `fetch_openalex_bulk.py` reads
  `topic.openalex_mailto` from `taxonomy.yaml` (with env `OPENALEX_MAILTO` override)
  instead of a hardcoded address.
- **`research_config.py`** added `get_trend_keywords()`, `get_subcategory_keywords()`,
  and `get_openalex_mailto()` helpers.

## [0.1.0] — 2026-08-06
- Initial skeleton: config-driven taxonomy, validation, README generation, statistics, reports, discovery, GitHub Pages, CI, AGENTS.md.
