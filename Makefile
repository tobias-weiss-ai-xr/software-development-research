# Software Development Research — task runner (Unix-minimal)
.PHONY: test validate check pipeline all

# Test layer: hermetic contract tests (no network, ~4s)
test:
	python3 -m pytest

# Contract: validate papers.yaml against the corpus contract
validate:
	python3 scripts/validate_papers.py

# Contract: confirm README.md matches papers.yaml
check:
	python3 scripts/generate_readme.py --check

# Full pipeline (validate -> README -> stats -> reports)
pipeline:
	python3 scripts/validate_papers.py && \
	python3 scripts/generate_readme.py && \
	python3 scripts/standard_stats.py && \
	python3 scripts/analysis/generate_reports.py

all: test validate check
