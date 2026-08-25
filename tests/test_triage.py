"""Tests for tools/triage_corpus.py — read-only corpus quality triage.

Verifies the flag heuristics on synthetic papers. The tool must be
non-destructive (never writes papers.yaml) and low-false-positive.
"""

import importlib.util
import sys
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "triage_corpus.py"
spec = importlib.util.spec_from_file_location("triage_corpus", TOOL)
triage = importlib.util.module_from_spec(spec)
sys.modules["triage_corpus"] = triage
spec.loader.exec_module(triage)


def _paper(**over):
    p = {
        "title": "Agentic Software Engineering",
        "date": "2026-01",
        "url": "https://arxiv.org/abs/2509.06216",
        "category": "software-engineering",
        "subcategory": "survey",
        "abstract": "A study of software engineering agents.",
    }
    p.update(over)
    return p


def test_clean_arxiv_paper_has_no_flags():
    assert triage.flags_for(_paper()) == []


def test_arxiv_no_abstract_is_still_clean():
    assert triage.flags_for(_paper(abstract="")) == []


def test_vanity_platform_flagged():
    fl = triage.flags_for(_paper(url="https://doi.org/10.21203/rs.3.rs-123/v1"))
    assert any(fid == "vanity-platform" for fid, _, _ in fl)


def test_foreign_domain_flagged():
    fl = triage.flags_for(_paper(title="Development of a decision support system "
                                      "for furrow and border irrigation",
                                 url="https://eprints.usq.edu.au/4083/2/x.pdf"))
    assert any(fid == "off-topic" for fid, _, _ in fl)


def test_doi_without_abstract_flagged_as_unvetted():
    fl = triage.flags_for(_paper(abstract="",
                                 url="https://doi.org/10.1000/xyz123"))
    assert any(fid == "no-abstract" for fid, _, _ in fl)


def test_junk_venue_flagged():
    fl = triage.flags_for(_paper(url="https://doi.org/10.55041/ijcope.v2i5.353",
                                 venue="International Journal of Creative and "
                                       "Open Research in Engineering and Management"))
    assert any(fid == "junk-venue" for fid, _, _ in fl)


def test_venue_list_handled():
    fl = triage.flags_for(_paper(venue=["Zenodo (CERN)"]))
    assert fl == []


def test_score_and_scan_sorting():
    papers = [
        _paper(),  # clean
        _paper(url="https://doi.org/10.21203/x"),  # vanity (score 4)
        _paper(abstract="", url="https://doi.org/10.1000/x"),  # no-abstract (2)
        _paper(title="Furrow irrigation system", abstract="",
               url="https://doi.org/10.5678/x"),  # off-topic + no-abstract (5)
    ]
    scored = triage.scan(papers)
    assert len(scored) == 3
    assert scored[0][0] == 5  # highest first
    assert scored[2][0] == 2
