"""Tests for scripts/research_config.py — the single config loader.

Verifies taxonomy loading, display helpers, fallbacks, and that the checked-in
config satisfies the corpus contract (no hardcoded values in scripts).
"""

from pathlib import Path

import research_config as rc

REPO = Path(__file__).resolve().parent.parent


def test_real_config_loads():
    cfg = rc.load_config()
    assert cfg["topic"]["name"] == "Software Development Research"
    cats = rc.get_categories(cfg)
    subs = rc.get_subcategories(cfg)
    assert len(cats) >= 10, "must have at least 10 categories"
    assert len(subs) >= 8, "must have at least 8 subcategories"
    assert len({c["id"] for c in cats}) == len(cats), "category ids must be unique"
    assert len({s["id"] for s in subs}) == len(subs), "subcategory ids must be unique"


def test_missing_config_falls_back():
    cfg = rc.load_config(Path("/nonexistent/taxonomy.yaml"))
    assert rc.get_topic(cfg)["name"] == "Research Corpus"
    assert rc.get_categories(cfg), "fallback taxonomy must define at least one category"


def test_display_helpers(mini_cfg):
    assert rc.category_display(mini_cfg, "code-quality") == "Code Quality"
    assert rc.subcategory_display(mini_cfg, "method") == "Method"
    # unknown ids fall back to the id itself
    assert rc.category_display(mini_cfg, "unknown") == "unknown"


def test_trend_keywords_fallback(mini_cfg):
    kws = rc.get_trend_keywords(mini_cfg)
    assert isinstance(kws, list) and kws


def test_openalex_mailto_env_override(mini_cfg, monkeypatch):
    monkeypatch.setenv("OPENALEX_MAILTO", "override@example.org")
    assert rc.get_openalex_mailto(mini_cfg) == "override@example.org"


def test_load_papers_real_corpus_is_populated():
    # Cheap contract-with-reality check: the corpus must stay populated.
    # Full YAML parsing happens in CI's validate_papers.py step; pytest stays
    # fast by scanning lines instead (YAML parse of the 9.6MB corpus ~60s).
    lines = (REPO / "papers.yaml").read_text(encoding="utf-8").splitlines()
    count = sum(1 for line in lines if line.strip().startswith("- title:"))
    assert count > 5000, "corpus must remain populated (contract with reality)"


def test_load_papers_custom_path(tmp_path, mini_cfg):
    f = tmp_path / "papers.yaml"
    f.write_text("papers: [{title: A, date: 2026-01, url: https://x.y, category: software-engineering, subcategory: survey}]\n")
    papers = rc.load_papers(f)
    assert len(papers) == 1
    assert papers[0]["title"] == "A"
