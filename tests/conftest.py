"""Shared pytest fixtures / path setup for the *-research corpus test suite.

Ensures that ``scripts/`` and ``scripts/fetch`` are importable when running
tests from the repository root, mirroring how the pipeline scripts import
``research_config`` and each other.

Tests are hermetic: they exercise contract functions on synthetic data plus
the checked-in config. No network calls.
"""

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent

for _p in ("scripts", "scripts/fetch"):
    _path = str(REPO / _p)
    if _path not in sys.path:
        sys.path.insert(0, _path)


@pytest.fixture()
def mini_cfg() -> dict:
    """A small taxonomy config for synthetic-data tests."""
    return {
        "topic": {"name": "Test Corpus", "short": "test"},
        "taxonomy": {
            "categories": [
                {"id": "software-engineering", "display": "Software Engineering"},
                {"id": "code-quality", "display": "Code Quality"},
            ],
            "subcategories": [
                {"id": "method", "display": "Method"},
                {"id": "survey", "display": "Survey"},
            ],
        },
    }


@pytest.fixture()
def mini_papers() -> list[dict]:
    """Three valid papers spanning two categories and two years."""
    return [
        {
            "title": "On Software Craft",
            "date": "2026-01",
            "url": "https://arxiv.org/abs/2405.12345",
            "category": "software-engineering",
            "subcategory": "method",
            "authors": ["Ada Lovelace"],
            "venue": "arXiv",
            "abstract": "A study of software craft.",
        },
        {
            "title": "Code Review at Scale",
            "date": "2025-06",
            "url": "https://doi.org/10.1000/xyz123",
            "category": "code-quality",
            "subcategory": "survey",
            "authors": ["Grace Hopper"],
            "abstract": "Survey of code review practices.",
        },
        {
            "title": "Refactoring Patterns",
            "date": "2025-03",
            "url": "https://dl.acm.org/doi/10.1145/1234567",
            "category": "code-quality",
            "subcategory": "method",
            "authors": ["Alan Turing"],
        },
    ]
