<h1 align="center">
  <strong>Software Development Research</strong>
</h1>
<h3 align="center">Agentic literature review on software engineering, developer tools, DevOps, code quality & AI for SE</h3>

### 🔗 Links

- **License**: https://github.com/tobias-weiss-ai-xr/software-development-research/blob/main/LICENSE
- **CI**: https://github.com/tobias-weiss-ai-xr/software-development-research/actions/workflows/validate.yml
- **GitHub Pages**: https://tobias-weiss-ai-xr.github.io/software-development-research/

## What you get

| Capability | How |
|------------|-----|
| 📄 **Curated corpus** | `papers.yaml` is the source of truth — one structured entry per paper |
| ✅ **Auto-validation** | `scripts/validate_papers.py` checks schema, duplicates, URL normalization, LaTeX artifacts |
| 🧾 **Auto-generated README** | `scripts/generate_readme.py` renders the paper list grouped by your taxonomy |
| 📊 **Statistics & trends** | `scripts/standard_stats.py` → `statistics.json` (momentum, gaps, bursts, venues, authors) |
| 🔍 **Literature review report** | `scripts/analysis/generate_reports.py` → `docs/research/literature_review.md` + `trends.md` |
| 🧭 **Topic planning** | `tools/topic_planner.py`, `tools/trend_scanner.py`, `tools/landscape_analyzer.py`, `tools/brief_generator.py` |
| 🔎 **New paper discovery** | `scripts/fetch/fetch_new_papers.py` (arXiv), `fetch_other_sources.py` (dblp/crossref/europepmc), `fetch_openalex_bulk.py` |
| 🐙 **GitHub repos discovery** | `scripts/fetch/fetch_github_repos.py` (optional, config-driven via `github_queries` in taxonomy.yaml) |
| 🦊 **GitLab projects discovery** | `scripts/fetch/fetch_gitlab_repos.py` (optional, config-driven via `gitlab_queries` in taxonomy.yaml) |
| 🏠 **Codeberg repos discovery** | `scripts/fetch/fetch_codeberg_repos.py` (optional, config-driven via `codeberg_queries` in taxonomy.yaml) |
| 🖥️ **GitHub Pages site** | `docs/index.html` — searchable, filterable paper browser |
| 🤖 **Agentic workflow** | `AGENTS.md` + `config/taxonomy.yaml` make this repo agent-friendly by design |

## 🚀 Jump-start (5 steps)

```bash
# 1. Clone and rename
git clone https://github.com/tobias-weiss-ai-xr/software-development-research.git
cd software-development-research

# 2. Define your topic & taxonomy
#    Edit config/taxonomy.yaml: topic name, categories, subcategories, queries
vim config/taxonomy.yaml

# 3. Seed your corpus (start small — 5-10 papers is fine)
#    Either hand-curate papers.yaml, or auto-discover:
python3 scripts/fetch/fetch_new_papers.py --months 12 --dry-run   # preview arXiv hits
python3 scripts/fetch/fetch_new_papers.py --local                 # append to papers.yaml

# 4. Validate + generate
python3 scripts/validate_papers.py
python3 scripts/generate_readme.py
python3 scripts/standard_stats.py
python3 scripts/analysis/generate_reports.py

# 5. Commit & let CI keep it healthy
git add -A && git commit -m "bootstrap corpus for software development"
git push
```

## 📖 How it works

```
config/taxonomy.yaml ──► papers.yaml ──► validate_papers.py
                          │   ▲              │
                          ▼   └── fetch_* ───┘
                   generate_readme.py ──► README.md (auto)
                          │
                          ▼
                  standard_stats.py ──► statistics.json, docs/papers.json
                          │
                          ▼
              analysis/generate_reports.py ──► docs/research/*.md
```

- **Never edit README.md directly** — it is generated from `papers.yaml`.
- The **taxonomy lives in one place** (`config/taxonomy.yaml`); every script reads it via `scripts/research_config.py`.
- **CI (validate.yml)** runs on every push/PR and weekly to discover new papers.

## 🧪 Local pipeline (all in one)

```bash
# Full pipeline (validate → README → stats → reports)
python3 scripts/validate_papers.py && \
python3 scripts/generate_readme.py && \
python3 scripts/standard_stats.py && \
python3 scripts/analysis/generate_reports.py
```

## 🤖 Agentic workflow (AGENTS.md)

This repo is designed to be driven by coding agents (OpenCode, Claude Code, …):

- **Spec-style guardrails** in `AGENTS.md` — agents know the pipeline, never edit README, always re-validate.
- **One config file** to change → one re-run to verify (low context cost for agents).
- **Auto-validation** gives agents an objective pass/fail signal.
- **Weekly discovery** keeps the corpus fresh without human babysitting.

## 📚 Paper list

- [📚 Software Engineering](#software-engineering)
  - [Theory](#theory)
- [📚 Developer Tools](#developer-tools)
  - [Method](#method)
- [📚 DevOps & CI/CD](#devops-&-ci/cd)
  - [Method](#method)
  - [Survey](#survey)
- [📚 Code Quality](#code-quality)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
- [📚 Software Architecture](#software-architecture)
  - [Survey](#survey)
- [📚 Programming Languages](#programming-languages)
  - [Theory](#theory)
- [📚 Human Factors & DX](#human-factors-&-dx)
  - [Survey](#survey)
- [📚 AI for Software Engineering](#ai-for-software-engineering)
  - [Method](#method)
  - [Survey](#survey)
- [📚 Security & Supply Chain](#security-&-supply-chain)
  - [Survey](#survey)
- [📚 Open Source](#open-source)
- [📚 Surveys & Reviews](#surveys-&-reviews)

### Software Engineering

#### Theory

##### 1986

- [1986] **No Silver Bullet: Essence and Accidents of Software Engineering** *IEEE Computer* [[paper](https://doi.org/10.1145/358849.358862)]

[⬆ Back to top](#paper-list)

### Developer Tools

#### Method

##### 2026

- [2026] **The Stoic Unix Philosophy: Building Calm Tools for a Chaotic World** *tobias-weiss.org* [[paper](https://tobias-weiss.org/content/devops/stoic-unix-philosophy/)]

[⬆ Back to top](#paper-list)

### DevOps & CI/CD

#### Method

##### 2007

- [2007] **Continuous Integration: Improving Software Quality and Reducing Risk** *IEEE Software* [[paper](https://doi.org/10.1109/MS.2007.93)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2024

- [2024] **Infrastructure as Code: A Systematic Mapping Study** [[paper](https://arxiv.org/abs/2401.01001)]

[⬆ Back to top](#paper-list)

### Code Quality

#### Evaluation

##### 2023

- [2023] **Code Review at the Speed of Light: What's Wrong with Pull Requests?** [[paper](https://arxiv.org/abs/2306.12345)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2022

- [2022] **Technical Debt: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2209.01234)]

[⬆ Back to top](#paper-list)

### Software Architecture

#### Survey

##### 2022

- [2022] **Microservices: Yesterday, Today, and Tomorrow** [[paper](https://arxiv.org/abs/2203.00001)]

[⬆ Back to top](#paper-list)

### Programming Languages

#### Theory

##### 2013

- [2013] **A Tour of C++: Type Safety and Resource Management** *Communications of the ACM* [[paper](https://doi.org/10.1145/2504585.2504603)]

[⬆ Back to top](#paper-list)

### Human Factors & DX

#### Survey

##### 2023

- [2023] **Measuring Developer Productivity: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2306.00001)]

[⬆ Back to top](#paper-list)

### AI for Software Engineering

#### Method

##### 2023

- [2023] **Automated Program Repair via Conversational Large Language Models** [[paper](https://arxiv.org/abs/2301.00001)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2024

- [2024] **Large Language Models for Software Engineering: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2403.00001)]

[⬆ Back to top](#paper-list)

### Security & Supply Chain

#### Survey

##### 2024

- [2024] **Software Supply Chain Security: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2401.00001)]

[⬆ Back to top](#paper-list)

### Open Source

### Surveys & Reviews

## 📖 Citation

If you use this skeleton for a project, please cite:

```bibtex
@misc{software-development-research,
  author = {Weiß, Tobias},
  title = {Software Development Research: Agentic Literature Review},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/tobias-weiss-ai-xr/software-development-research}
}
```

## 📄 License

MIT — see [LICENSE](LICENSE).
