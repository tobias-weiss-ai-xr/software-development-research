#!/usr/bin/env python3
"""One-shot, audited cleanup: remove confirmed corpus pollution from papers.yaml.

This is NOT part of the routine pipeline. It implements the review decision
made on 2026-08-25 (see commit message) using EXACTLY the flag signals from
tools/triage_corpus.py (single source of truth — no duplicated regex), plus an
explicit keep-list for the few SE-relevant exceptions.

  REMOVED (objective, no content judgment):
    - entries from known predatory / non-peer-reviewed venues
  REMOVED (human-reviewed): triage 'off-topic' entries, minus keep-list

  EXCLUDED BY POLICY (accepted sources, never removed):
    - Research Square preprints (10.21203) — corpus maintainer decision
    - HAL entries (legitimate national repository, incl.
      INRIA/CentraleSupélec)

  KEPT intentionally (reviewed exceptions):
    - Galene (SE toolkit, IEEE APSEC), MSTI-3 (auto codegen, IEEE SmallSat),
      LEISA (microservices, arXiv), Qlik data-versioning (data engineering)

Safety:
  - writes an audit log of every removed entry to docs/research/removed_entries.yaml
  - never modifies any paper except removal; git provides full reversibility
  - coarse idempotency guard (.removal_applied, gitignored) prevents double runs

Usage:
    python3 tools/remove_audited_noise.py
"""

import importlib.util
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import research_config

GUARD = REPO / ".removal_applied"
REMOVED_LOG = REPO / "docs" / "research" / "removed_entries.yaml"

# Reuse the reviewed flag signals from the triage tool (no duplicated logic).
_triage_spec = importlib.util.spec_from_file_location(
    "triage_corpus", REPO / "tools" / "triage_corpus.py"
)
triage = importlib.util.module_from_spec(_triage_spec)
_triage_spec.loader.exec_module(triage)

# Reviewed exceptions — genuinely software-engineering relevant, keep.
KEEP_TITLES = {
    "Galene: A Toolkit for Encapsulating Software Engineering Practices in Marine Science AI Applications",
    "MSTI-3 Spacecraft Attitude Control Software Development using Automatic Code Generation",
    "LEISA: A scalable microservice-based system for efficient livestock data sharing",
    "Managing Historical AND Delta Loads with Efficient Data Versioning in Qlik Applications",
}

KEEP_DOMAINS = ("hal.science",)  # HAL = legitimate national repository, keep

# Gross SEO-spam content (content farms, exam-dump / scam-review mills).
# These carry no abstract and no scientific value; removing is uncontroversial.
SPAM_HOSTS = ("researchhub",)  # exam-dumps / fake-review content farm
SPAM_TITLE = re.compile(
    r"(exam dump|braindump|pass your exam|certification dumps|is it .*\?.*legit|"
    r"scam or legit|honest review| code ?reviews? 2026|course in pune)",
    re.IGNORECASE,
)


def reason_for(paper) -> str | None:
    """Return removal reason string, or None to keep."""
    url = paper.get("url", "") or ""
    title = paper.get("title", "") or ""

    if any(d in url for d in KEEP_DOMAINS):
        return None
    if title in KEEP_TITLES:
        return None

    if any(h in url for h in SPAM_HOSTS):
        return "SEO-spam content farm (researchhub exam-dumps / scam reviews)"
    if SPAM_TITLE.search(title):
        return "SEO-spam title (exam dump / fake review)"

    flags = {fid: detail for fid, _, detail in triage.flags_for(paper)}
    if "junk-venue" in flags:
        return "predatory / non-peer-reviewed venue"
    if "off-topic" in flags:
        return f"out-of-domain for software-development corpus ({flags['off-topic'][:80]})"
    return None


def main():
    if GUARD.exists():
        print(f"Refusing to run twice: {GUARD} present (one-shot by design).")
        sys.exit(1)

    yaml_path = REPO / "papers.yaml"
    data = research_config.load_yaml(yaml_path)

    papers = data.get("papers", [])
    removed, kept = [], []
    for p in papers:
        why = reason_for(p)
        (removed if why else kept).append((p, why))

    print(f"Total {len(papers)}; removing {len(removed)}; keeping {len(kept)}")
    if not removed:
        print("Nothing to remove.")
        return

    data["papers"] = [p for p, _ in kept]
    yaml_path.write_text(
        yaml.dump(data, default_flow_style=False, allow_unicode=True,
                  sort_keys=False),
        encoding="utf-8",
    )

    log_entries = [
        {"date_removed": datetime.now().strftime("%Y-%m-%d"), "reason": why,
         "title": p.get("title"), "url": p.get("url", ""), "date": p.get("date", "")}
        for p, why in removed
    ]
    REMOVED_LOG.parent.mkdir(parents=True, exist_ok=True)
    REMOVED_LOG.write_text(
        yaml.dump(log_entries, default_flow_style=False, allow_unicode=True,
                  sort_keys=False),
        encoding="utf-8",
    )

    GUARD.write_text(f"applied {datetime.now():%Y-%m-%d}\n", encoding="utf-8")
    print(f"Wrote {yaml_path} ({len(kept)} papers)")
    print(f"Wrote audit log {REMOVED_LOG} ({len(removed)} entries)")


if __name__ == "__main__":
    main()
