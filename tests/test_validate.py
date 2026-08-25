"""Tests for the contract enforcer: scripts/validate_papers.py.

Covers the pure contract functions (clean_latex_artifacts, normalize_arxiv_url,
is_arxiv_url) and the validate_papers() gate on synthetic data. Hermetic, fast.
"""

from datetime import datetime

import validate_papers as vp


def _valid_paper(**over):
    p = {
        "title": "Test Paper",
        "date": "2026-01",
        "url": "https://arxiv.org/abs/2405.12345",
        "category": "software-engineering",
        "subcategory": "survey",
        "abstract": "Plain abstract without artifacts.",
    }
    p.update(over)
    return p


def _next_month() -> str:
    now = datetime.now()
    y, m = now.year, now.month
    if m == 12:
        y, m = y + 1, 1
    else:
        m += 1
    return f"{y:04d}-{m:02d}"


# --- pure helpers -------------------------------------------------------


def test_clean_latex_artifacts_strips_markup():
    text = r"Use \textit{italics}, \textbf{bold}, and $x^2$; also \(y\) here."
    cleaned = vp.clean_latex_artifacts(text)
    assert "textit" not in cleaned
    assert "textbf" not in cleaned
    assert "x^2" in cleaned
    assert "y" in cleaned
    assert "$" not in cleaned
    assert "\\\\" not in cleaned


def test_clean_latex_artifacts_empty_and_plain():
    assert vp.clean_latex_artifacts("") == ""
    assert vp.clean_latex_artifacts("Plain text.") == "Plain text."


def test_normalize_arxiv_url_forms():
    assert vp.normalize_arxiv_url("https://arxiv.org/pdf/2405.12345v2") == (
        "https://arxiv.org/abs/2405.12345"
    )
    assert vp.normalize_arxiv_url("https://doi.org/10.48550/arXiv.2405.12345") == (
        "https://arxiv.org/abs/2405.12345"
    )
    # Non-arXiv URLs pass through untouched
    assert vp.normalize_arxiv_url("https://doi.org/10.1000/xyz") == "https://doi.org/10.1000/xyz"


def test_is_arxiv_url():
    assert vp.is_arxiv_url("https://arxiv.org/abs/2405.12345")
    assert vp.is_arxiv_url("https://doi.org/10.48550/arXiv.2405.12345")
    assert not vp.is_arxiv_url("https://doi.org/10.1000/xyz")
    assert not vp.is_arxiv_url("https://dl.acm.org/doi/10.1145/1234567")


# --- validate_papers gate -------------------------------------------------


def test_valid_paper_passes(mini_cfg):
    data = {"papers": [_valid_paper()]}
    errors, warnings, fixed, _ = vp.validate_papers(data, mini_cfg)
    assert errors == []
    assert fixed == 0


def test_missing_required_fields_fail(mini_cfg):
    data = {"papers": [_valid_paper(title="", date="", url="", category="", subcategory="")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert len(errors) == 5
    joined = "\n".join(errors)
    for field in ("title", "date", "url", "category", "subcategory"):
        assert f"missing required field '{field}'" in joined


def test_invalid_category_and_subcategory_fail(mini_cfg):
    data = {"papers": [_valid_paper(category="nonsense", subcategory="bogus")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("invalid category 'nonsense'" in e for e in errors)
    assert any("invalid subcategory 'bogus'" in e for e in errors)


def test_bad_date_format_fails(mini_cfg):
    data = {"papers": [_valid_paper(date="26-01-2026")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("invalid date '26-01-2026'" in e for e in errors)


def test_future_date_fails(mini_cfg):
    future = _next_month()
    data = {"papers": [_valid_paper(date=future)]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("future date" in e for e in errors)


def test_non_https_url_fails(mini_cfg):
    data = {"papers": [_valid_paper(url="http://example.com/paper")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("URL must start with https://" in e for e in errors)


def test_arxiv_url_must_be_normalized(mini_cfg):
    data = {"papers": [_valid_paper(url="https://arxiv.org/pdf/2405.12345v2")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("not normalized" in e for e in errors)
    # --fix normalizes it in place
    errors, _, fixed, _ = vp.validate_papers(data, mini_cfg, fix=True)
    assert errors == []
    assert fixed == 1
    assert data["papers"][0]["url"] == "https://arxiv.org/abs/2405.12345"


def test_versioned_arxiv_url_rejected_and_fixed(mini_cfg):
    """arXiv URLs with a version suffix (…v1) violate the canonical form.

    Regression for a latent CI failure: ~90 corpus entries carried …v1/…v2
    suffixes that the contract rejects.
    """
    data = {"papers": [_valid_paper(url="https://arxiv.org/abs/2608.19674v1")]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("not normalized" in e for e in errors)
    errors, _, fixed, _ = vp.validate_papers(data, mini_cfg, fix=True)
    assert errors == []
    assert fixed == 1
    assert data["papers"][0]["url"] == "https://arxiv.org/abs/2608.19674"


def test_duplicate_entry_fails(mini_cfg):
    data = {"papers": [_valid_paper(), _valid_paper()]}
    errors, _, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("duplicate entry" in e for e in errors)


def test_latex_artifact_warns_and_fixes(mini_cfg):
    data = {"papers": [_valid_paper(title=r"Bleach: Teaching \$ git clone\$ Compilers")]}
    _, warnings, _, _ = vp.validate_papers(data, mini_cfg)
    assert any("LaTeX artifact" in w for w in warnings)
    errors, _, fixed, _ = vp.validate_papers(data, mini_cfg, fix=True)
    assert errors == []
    assert fixed == 1
    assert "$" not in data["papers"][0]["title"]


def test_vanity_domain_warns(mini_cfg):
    for domain in ("https://www.preprints.org/x", "https://www.researchsquare.com/x",
                   "https://doi.org/10.21203/rs.3.rs-123/v1",  # Research Square DOI prefix
                   "https://www.rgdoi.net/10.13140/RG.2.2.12345"):
        data = {"papers": [_valid_paper(url=domain)]}
        _, warnings, _, _ = vp.validate_papers(data, mini_cfg)
        assert any("non-peer-reviewed" in w for w in warnings), domain


def test_empty_corpus_fails(mini_cfg):
    errors, _, _, _ = vp.validate_papers({"papers": []}, mini_cfg)
    assert any("contains no papers" in e for e in errors)
