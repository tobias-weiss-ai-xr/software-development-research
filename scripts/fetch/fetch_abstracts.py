#!/usr/bin/env python3
"""Backfill missing abstracts for existing papers from OpenAlex.

Most corpus papers are ingested with abstracts, but a slice (bulk-ingested
from Crossref/other sources) lacks them. For those, query OpenAlex by DOI and
reconstruct the abstract from `abstract_inverted_index`. This *curates, does
not delete*: real papers from major publishers (Springer/Elsevier/IEEE/ACM/
Zenodo) regain their abstracts and stop tripping the `no-abstract` junk proxy.

Read-only w.r.t. existing abstracts — never overwrites a present abstract.
Networked (one OpenAlex lookup per missing-DOI paper), polite-pool + cached.

Usage:
    python3 scripts/fetch/fetch_abstracts.py            # backfill + write
    python3 scripts/fetch/fetch_abstracts.py --dry-run  # count only
    python3 scripts/fetch/fetch_abstracts.py --limit 50 # cap lookups (debug)
"""

import argparse
import re
import sys
import time
from pathlib import Path

import requests
import yaml

try:
    from yaml import CSafeLoader as _LOADER
except ImportError:
    _LOADER = yaml.SafeLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import research_config as rc

OPENALEX_API = "https://api.openalex.org/works"
CACHE_DIR = Path.home() / ".cache" / "research-runner" / "abstracts"
ARXIV = re.compile(r"arxiv\.org")
DBLP = re.compile(r"dblp\.org")
DOI = re.compile(r"https?://doi\.org/(10\.\d{4,9}/[^\s]+)")
SLEEP = 0.12  # polite-pool headroom


def reconstruct_abstract(inverted):
    """Reconstruct readable text from OpenAlex abstract_inverted_index."""
    if not inverted:
        return ""
    pos = {}
    for word, positions in inverted.items():
        for p in positions:
            pos[p] = word
    return " ".join(pos[i] for i in sorted(pos))


def needs_abstract(paper):
    """True if the entry lacks an abstract and has a resolvable DOI (not arXiv/DBLP)."""
    if (paper.get("abstract") or "").strip():
        return False
    url = paper.get("url", "") or ""
    if not url:
        return False
    if ARXIV.search(url) or DBLP.search(url):
        return False
    return bool(DOI.search(url))


def _cache_path(doi):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^0-9a-zA-Z]", "_", doi)
    return CACHE_DIR / f"{safe}.txt"


def _lookup(session, doi, mailto):
    cp = _cache_path(doi)
    if cp.exists():
        return cp.read_text(encoding="utf-8") or None
    for attempt in range(4):
        try:
            resp = session.get(f"{OPENALEX_API}/doi:{doi}", params={"mailto": mailto},
                                timeout=30)
            if resp.status_code == 429:
                wait = min(int(resp.headers.get("Retry-After", 5 * (attempt + 1))), 30)
                time.sleep(wait)
                continue
            if resp.status_code != 200:
                break
            data = resp.json()
            abstract = reconstruct_abstract(data.get("abstract_inverted_index"))
            cp.write_text(abstract, encoding="utf-8")
            return abstract
        except Exception as e:
            print(f"  WARN {doi}: {e}", flush=True)
            break
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="cap number of lookups")
    args = ap.parse_args()

    cfg = rc.require_valid_config()
    mailto = rc.get_openalex_mailto(cfg)
    papers_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    data = rc.load_yaml(papers_path)
    papers = data.get("papers", [])

    targets = [p for p in papers if needs_abstract(p)]
    print(f"{len(papers)} papers; {len(targets)} missing an abstract", flush=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "research-runner/1.0"})
    seen, recovered, capped = 0, 0, False
    for p in targets:
        m = DOI.search(p["url"])
        doi = m.group(1)
        abstract = _lookup(session, doi, mailto)
        seen += 1
        if abstract:
            recovered += 1
            p["abstract"] = abstract
        if seen % 50 == 0:
            print(f"  looked up {seen}/{len(targets)}; recovered {recovered}", flush=True)
        time.sleep(SLEEP)
        if args.limit and seen >= args.limit:
            capped = True
            break

    print(f"Recovered abstracts: {recovered}/{seen}"
          + (" (capped at --limit)" if capped else ""), flush=True)
    if args.dry_run:
        return

    if recovered:
        papers_path.write_text(
            yaml.dump(data, default_flow_style=False, allow_unicode=True,
                      sort_keys=False), encoding="utf-8")
        print(f"Wrote {papers_path} ({recovered} abstracts backfilled)", flush=True)
    else:
        print("Nothing to write.", flush=True)


if __name__ == "__main__":
    main()
