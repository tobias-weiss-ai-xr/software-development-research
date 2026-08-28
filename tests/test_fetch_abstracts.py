"""Tests for scripts/fetch/fetch_abstracts.py — abstract backfill (enrichment).

Hermetic: no network. Verifies the OpenAlex inverted-index reconstruction and
the selection predicate that decides which papers need an abstract backfilled.
"""

import importlib.util
import sys
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "scripts" / "fetch" / "fetch_abstracts.py"
spec = importlib.util.spec_from_file_location("fetch_abstracts", TOOL)
fa = importlib.util.module_from_spec(spec)
sys.modules["fetch_abstracts"] = fa
spec.loader.exec_module(fa)


def test_reconstruct_abstract_roundtrip():
    inverted = {"the": [0, 4], "cat": [1], "sat": [2], "on": [3], "mat": [5]}
    text = fa.reconstruct_abstract(inverted)
    assert text == "the cat sat on the mat", text
    assert fa.reconstruct_abstract(None) == ""
    assert fa.reconstruct_abstract({}) == ""


def test_needs_abstract_true_for_doi_missing():
    p = {"title": "T", "url": "https://doi.org/10.1109/foo", "abstract": ""}
    assert fa.needs_abstract(p) is True


def test_needs_abstract_false_when_present():
    p = {"title": "T", "url": "https://doi.org/10.1109/foo", "abstract": "already here"}
    assert fa.needs_abstract(p) is False


def test_needs_abstract_false_for_arxiv():
    p = {"title": "T", "url": "https://arxiv.org/abs/2509.06216", "abstract": ""}
    assert fa.needs_abstract(p) is False


def test_needs_abstract_false_for_no_url():
    p = {"title": "T", "url": "", "abstract": ""}
    assert fa.needs_abstract(p) is False
