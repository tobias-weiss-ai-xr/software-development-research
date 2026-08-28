# Software Development Research — task runner (Unix-minimal)
.PHONY: test validate check pipeline triage enrich all

# Test layer: hermetic contract tests (no network, ~4s)
test:
	python3 -m pytest

# Contract: validate papers.yaml against the corpus contract
validate:
	python3 scripts/validate_papers.py

# Contract: confirm README.md matches papers.yaml
check:
	python3 scripts/generate_readme.py --check

# Read-only corpus quality triage (writes docs/research/corpus_triage.md)
triage:
	python3 tools/triage_corpus.py

# Full pipeline (validate -> README -> stats -> reports)
pipeline:
	python3 scripts/validate_papers.py && \
	python3 scripts/generate_readme.py && \
	python3 scripts/standard_stats.py && \
	python3 scripts/analysis/generate_reports.py

# Backfill missing abstracts from OpenAlex (curate, don't delete)
enrich:
	python3 scripts/fetch/fetch_abstracts.py

all: test validate check
