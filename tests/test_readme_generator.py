"""Tests for scripts/generate_readme.py — the README/docs/papers.json generator.

Verifies rendering, JSON export, and the --check drift gate (exercise_contract:
README must always reflect papers.yaml).
"""

import json

import pytest

import generate_readme as gr

README_TEMPLATE = """# {name}

## 📚 Paper list

STALE LIST HERE

## 📖 Citation

If you use this work, cite...

## License

MIT
"""


def test_render_paper_list_groups_by_category_year(mini_cfg, mini_papers):
    text = gr.render_paper_list(mini_papers, mini_cfg)
    assert text.startswith("## 📚 Paper list")
    assert "### Code Quality" in text
    assert "### Software Engineering" in text
    assert "##### 2026" in text and "##### 2025" in text
    assert "[[paper](https://arxiv.org/abs/2405.12345)]" in text
    assert "**On Software Craft**" in text
    assert "⬆ Back to top" in text


def test_generate_readme_writes_between_markers(tmp_path, mini_cfg, mini_papers):
    readme = tmp_path / "README.md"
    readme.write_text(README_TEMPLATE.format(name="Test Corp"), encoding="utf-8")
    gr.generate_readme(mini_papers, readme, mini_cfg)
    text = readme.read_text(encoding="utf-8")
    assert "STALE LIST HERE" not in text
    assert "On Software Craft" in text
    # Marker sections preserved
    assert "## 📖 Citation" in text
    assert "## 📚 Paper list" in text


def test_generate_readme_check_sync_and_drift(tmp_path, mini_cfg, mini_papers):
    readme = tmp_path / "README.md"
    readme.write_text(README_TEMPLATE.format(name="Test Corp"), encoding="utf-8")
    gr.generate_readme(mini_papers, readme, mini_cfg)

    # In sync -> --check exits 0
    with pytest.raises(SystemExit) as e:
        gr.generate_readme(mini_papers, readme, mini_cfg, check_mode=True)
    assert e.value.code == 0

    # Paper list changed -> --check exits non-zero (drift detected)
    changed = mini_papers + [dict(mini_papers[0], title="Brand New Paper")]
    with pytest.raises(SystemExit) as e:
        gr.generate_readme(changed, readme, mini_cfg, check_mode=True)
    assert e.value.code != 0


def test_generate_json_roundtrip(tmp_path, mini_papers):
    out = tmp_path / "papers.json"
    gr.generate_json(mini_papers, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["papers"] == mini_papers
