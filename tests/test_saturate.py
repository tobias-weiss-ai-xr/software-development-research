"""Tests for scripts/fetch/saturate_papers.py — dedup + relevance helpers.

Only pure functions are tested (no network). These guard the discovery
pipeline against duplicate ingestion and off-topic drift.
"""

import saturate_papers as sp


def _write_papers(tmp_path, papers):
    f = tmp_path / "papers.yaml"
    f.write_text(f"papers:\n" + "".join(
        f"  - title: {p['title']!r}\n    url: {p['url']!r}\n    category: software-engineering\n    subcategory: method\n"
        for p in papers
    ))
    return f


def test_load_existing_papers_indexes_ids_and_titles(tmp_path):
    f = _write_papers(tmp_path, [
        {"title": "Agentic Software Engineering", "url": "https://arxiv.org/abs/2509.06216"},
        {"title": "Another Paper", "url": "https://doi.org/10.1000/xyz"},
    ])
    data, papers, by_id, titles_lower = sp.load_existing_papers(f)
    assert len(papers) == 2
    assert "2509.06216" in by_id
    assert "agentic software engineering" in titles_lower


def test_title_similarity():
    assert sp.title_similarity("Agentic Software Engineering", "Agentic Software Engineering") == 1.0
    assert sp.title_similarity("A Framework for X", "Completely Unrelated Title") < 0.75
    assert sp.title_similarity("Hello World!", "Hello, World!") > 0.9


def test_dedup_title_threshold():
    titles = ["Agentic Software Engineering", "Code Review at Scale"]
    assert sp.dedup_title("Agentic Software Engineering", titles) is True
    assert sp.dedup_title("A paper about databases", titles) is False
    assert sp.dedup_title("Agentic Software Engineering", titles, threshold=1.0) is True


def test_is_relevant_keywords():
    kws = ["software engineering", "code review"]
    assert sp.is_relevant("On Software Engineering Practices", "abstract", kws)
    assert sp.is_relevant("Title", "A study on code review in industry", kws)
    assert not sp.is_relevant("Furrow Irrigation DSS", "decision support for crops", kws)
    # no keywords -> accept all
    assert sp.is_relevant("Anything", "anything", None) is True
    assert sp.is_relevant("Anything", "anything", []) is True
