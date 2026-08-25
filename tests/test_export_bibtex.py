"""Tests for scripts/export_bibtex.py — BibTeX sanitization."""

import export_bibtex as eb


def test_sanitize_bibtex_escapes_specials():
    assert eb.sanitize_bibtex("A & B 100%") == r"A \& B 100\%"
    assert eb.sanitize_bibtex("#hashtag") == r"\#hashtag"
    assert eb.sanitize_bibtex("under_score") == r"under\_score"
    assert eb.sanitize_bibtex("brace {x}") == r"brace \{x\}"


def test_sanitize_bibtex_plain_passthrough():
    assert eb.sanitize_bibtex("Agentic Software Engineering") == "Agentic Software Engineering"
    assert eb.sanitize_bibtex("") == ""
