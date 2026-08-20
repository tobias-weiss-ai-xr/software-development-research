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
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
- [📚 Developer Tools](#developer-tools)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 DevOps & CI/CD](#devops-&-ci/cd)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Code Quality](#code-quality)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Software Architecture](#software-architecture)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Programming Languages](#programming-languages)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Human Factors & DX](#human-factors-&-dx)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
- [📚 AI for Software Engineering](#ai-for-software-engineering)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Security & Supply Chain](#security-&-supply-chain)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
- [📚 Open Source](#open-source)
  - [Method](#method)
  - [Theory](#theory)
  - [Application](#application)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Systems](#systems)
  - [Development](#development)
- [📚 Surveys & Reviews](#surveys-&-reviews)

### Software Engineering

#### Method

##### 2026

- [2026] **Software Development Methodologies Evolutionary Trends from Waterfall to DevOps** *Journal of Global Research in Multidisciplinary Studies(JGRMS)* [[paper](https://doi.org/10.67805/jgrms.v2i8.150)]
- [2026] **Development of a decision support system for furrow and border irrigation** *University of Southern Queensland ePrints (University of Southern Queensland)* [[paper](https://eprints.usq.edu.au/4083/2/McClymont_2007_whole.pdf)]
- [2026] **Building Production Software and Professional Competence: A Collaborative Model for AI-Integrated Software Engineering Practice** [[paper](https://doi.org/10.1145/3803437.3805795)]
- [2026] **A Preliminary Search for Evidence on Government Software Engineering Practices: Results from Three Rapid Reviews** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2607.22485)]
- [2026] **Software development methodologies: analyzing usage based on project requirements, user involvement, development team, and project type** *International Journal of Systems Assurance Engineering and Management* [[paper](https://doi.org/10.1007/s13198-026-03384-9)]
- [2026] **AGILE VERSUS TRADITIONAL SOFTWARE DEVELOPMENT METHODOLOGIES: A CRITICAL REVIEW OF GOVERNANCE ALIGNMENT IN LARGE-SCALE ADOPTION.** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21273720)]
- [2026] **Software Engineering Practices** [[paper](https://doi.org/10.1201/9781003362111-5)]
- [2026] **A Meta-Synthesis of Ethics-Aware Software Engineering Practice: A Preliminary Framework** *Journal of Information Systems and Informatics* [[paper](https://doi.org/10.63158/journalisi.v8i3.1583)]
- [2026] **Comparative Analysis of Agile and Traditional Software Development Methodologies: A Systematic Review of Project Success, Flexibility, and Organizational Performance** *Direct Research Journal of Engineering and Information Technology* [[paper](https://doi.org/10.26765/drjeit79173911)]
- [2026] **Ontology-driven software engineering using LLMs for knowledge graphs in engineering biology** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.64898/2026.05.29.728869)]
- [2026] **Interface-Led Architecture (ILA): A Software Development Methodology for the AI Era, Validated by the AIKernel Execution Model** *Open MIND* [[paper](https://github.com/AIKernel-NET/AIKernel.NET)]
- [2026] **Sustainable Software Engineering Practices for Supply Chain Optimization: A Systematic Literature Review** [[paper](https://doi.org/10.23919/indiacom70271.2026.11526146)]
- [2026] **Organic Development: A Software Development Methodology for the AI Era** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19870288)]
- [2026] **LLM-Assisted Software Development in Aerospace Engineering Education: A Structured Workflow** [[paper](https://doi.org/10.1109/icaiset66439.2026.11541825)]
- [2026] **Evaluation of software development life cycle using multi-criteria decision-making approach** *Kuwait Journal of Science* [[paper](https://doi.org/10.1016/j.kjs.2026.100595)]
- [2026] **Code generation with large language models: a survey from neural program synthesis to autonomous software development** *Applied Intelligence* [[paper](https://doi.org/10.1007/s10489-026-07230-0)]
- [2026] **Replication package for the paper "Software Engineering Practices and Challenges in Virtual Reality Development: A Systematic Literature Review"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18886265)]
- [2026] **Novice Developers’ Perspectives on Adopting LLMs for Software Development: A Systematic Literature Review** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3800580)]
- [2026] **Microlearning in Software Engineering Education: A Systematic Review of Initiatives and Curriculum Modernization** *Education Sciences* [[paper](https://doi.org/10.3390/educsci16030487)]
- [2026] **C2|Q>: A Robust Framework for Bridging Classical and Quantum Software Development** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3803018)]
- [2026] **<scp>IMPACT</scp> Framework: Establishing Global Standards for Artificial Intelligence Implementation, Methodology, and Translation in Drug Discovery** *Wiley Interdisciplinary Reviews Computational Molecular Science* [[paper](https://doi.org/10.1002/wcms.70072)]
- [2026] **Impact of Software Engineering Practices and Technology Adoption on Business Sustainability** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18533240)]
- [2026] **A Critical Reflection on the State of Data Analysis in Empirical Software Engineering** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3799715)]
- [2026] **The development of analysis methodology of financial risks of projects in IT sphere** *Technology audit and production reserves* [[paper](https://doi.org/10.15587/2706-5448.2026.352430)]
- [2026] **Systematic Benchmarking of Climate Models: Methodologies, Applications, and New Directions** *Reviews of Geophysics* [[paper](https://doi.org/10.1029/2025rg000891)]
- [2026] **AI-First Software Development Lifecycle: An Agent-Driven Framework for Autonomous Planning, Coding, Testing, and Deployment** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19506964)]
- [2026] **Outsourcing in Global Software Development: Effects of Temporal Location and Methodologies** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2602.08084)]
- [2026] **A Research Roadmap for Augmenting Software Engineering Processes and Software Products with Generative AI** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2510.26275)]
- [2026] **Explainable Artificial Intelligence in Software Engineering: Current Trends, Gaps, and Future Directions** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3679576)]
- [2026] **Between Policy and Practice: GenAI Adoption in Agile Software Development Teams** *Lecture notes in business information processing* [[paper](https://doi.org/10.1007/978-3-032-22375-3_18)]
- [2026] **Adaptive Cyber Secure Software Engineering Practices for Big Data Platforms With Dynamic Access Control and Differential Privacy Mechanisms** *Big Data Analytics and Data Science* [[paper](https://doi.org/10.66472/bdas.v1i1.24)]
- [2026] **Modern Machine Learning Methods to Improve Software Engineering Methodologies: New Developments and Future Directions** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-981-96-8104-4_50)]
- [2026] **Supplemental Materials for Designing Tools to Enhance Software Engineering Best Practices in Research Software Engineering** *Virginia Tech Data Repository* [[paper](https://doi.org/10.7294/28426961.v1)]
- [2026] **Automation of software development for psychiatry, psychotherapy and medical psychology: methodology for creating technical specifications and code generation using artificial intelligence (vibe-coding)** *Сибирский вестник психиатрии и наркологии* [[paper](https://doi.org/10.26617/1810-3111-2025-4(129)-57-70)]
- [2026] **A Comparative Study of Traditional (RUP and MSF) Versus Agile (SCRUM and XP) Software Development Methodologies** *Studies in systems, decision and control* [[paper](https://doi.org/10.1007/978-3-031-85398-2_16)]
- [2026] **A Digital Twin Approach for Spacecraft On-Board Software Development and Testing** *Aerospace* [[paper](https://doi.org/10.3390/aerospace13010055)]
- [2026] **Development of HIL Based Methodology for Over-The-Air Updates Validation** *SAE technical papers on CD-ROM/SAE technical paper series* [[paper](https://doi.org/10.4271/2026-26-0480)]
- [2026] **Methods and Techniques of Agentic Software Engineering: A Systematic Literature Review** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3652325)]
- [2026] **METHODOLOGICAL ISSUES OF DEVELOPING COMPETENCIES IN SOFTWARE DEVELOPMENT** *ICSP «NEW SCIENCE» eBooks* [[paper](https://doi.org/10.46916/08062026-1-978-5-00276-114-2)]
- [2026] **Software Tools for Passive Acoustic Monitoring in Aquatic and Terrestrial Bio- and Ecoacoustics: A Living Systematic Review** *F1000Research* [[paper](https://doi.org/10.12688/f1000research.173495.1)]
- [2026] **An improvement for software families’ development with agile methodologies’ elements** *Open Publication Harvester of National Academy of Sciences of Ukraine* [[paper](https://harvester.nas.gov.ua/Record/pp_isofts_kiev_ua-article-910)]
- [2026] **The Open Handbook of Experience Sampling Methodology - Third edition** *OAPEN (The OAPEN Foundation)* [[paper](https://library.oapen.org/handle/20.500.12657/112436)]

##### 2025

- [2025] **Software Engineering Practices: In the era of AI / LLMs** *Journal of Computer Science and Technology Studies* [[paper](https://doi.org/10.32996/jcsts.2025.7.12.57)]
- [2025] **Recommended Software Engineering Practices for DistributedLedger Technology Solutions** *Journal of the Association for Information Systems* [[paper](https://aisel.aisnet.org/acis2025/116)]
- [2025] **A systematic literature review of software engineering research on Jupyter notebook** *Journal of Systems and Software* [[paper](https://arxiv.org/abs/2504.16180)]
- [2025] **Evolving Software Engineering Practices in the Era of AI-Driven Automation** [[paper](https://doi.org/10.1109/icca66035.2025.11430882)]
- [2025] **Supplementary Info Package - Empathy Guidelines for Improving Practitioner Well-being & Software Engineering Practices** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17862673)]
- [2025] **Benchmarking AI Models in Software Engineering: A Review, Search Tool, and Unified Approach for Elevating Benchmark Quality** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3644183)]
- [2025] **Bridging the skills gap through Agile methodologies in Vocational Software Development Education** *Array* [[paper](https://doi.org/10.1016/j.array.2025.100614)]
- [2025] **Multi-Agent Reinforcement Learning for Dynamic Software Development Methodology Selection: A Stakeholder-Aware Approach** [[paper](https://doi.org/10.1145/3787330.3787358)]
- [2025] **Method and Tool for Risk Management in Agile Software Development Methodologies Based on an Adaptive SEI Model** *ELARTU (Ternopil National Technical University)* [[paper](https://elartu.tntu.edu.ua/handle/lib/51139)]
- [2025] **Feature review of photovoltaic modeling software utilizing blind performance assessment** *Solar Energy* [[paper](https://doi.org/10.1016/j.solener.2025.114207)]
- [2025] **An Empirical Study of Self-Admitted Technical Debt in Machine Learning Software** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3785001)]
- [2025] **A Preference-Driven Methodology for Efficient Code Generation** *IEEE Transactions on Artificial Intelligence* [[paper](https://doi.org/10.1109/tai.2025.3639527)]
- [2025] **The Model of Software Effort Estimation in the Context of Methodology Agile and Software Development** *Journal of Internet Services and Information Security* [[paper](https://doi.org/10.58346/jisis.2026.i1.004)]
- [2025] **Software Supply Chain Resilience in 2025: A Comparative Analysis of Major Incidents Using OSINT Methodologies** *International Journal of Information Security and Cybercrime* [[paper](https://doi.org/10.19107/ijisc.2025.02.03)]
- [2025] **Software Development Students' Perception of Active Methodologies in Probability and Statistics** *Revista de Políticas Universitarias* [[paper](https://doi.org/10.35429/jup.2024.8.19.1.13)]
- [2025] **Generative AI for Requirements Engineering: A Systematic Literature Review** *Software Practice and Experience* [[paper](https://doi.org/10.1002/spe.70029)]
- [2025] **Software Engineering Practices for Remote Civil Engineering Project Management during COVID-19** [[paper](https://doi.org/10.33790/jiti1100113)]
- [2025] **Model-Assisted and Human-Guided: Perceptions and Practices of Software Professionals Using LLMs for Coding** [[paper](https://doi.org/10.1109/aiware69974.2025.00019)]
- [2025] **Evolution and Current Trends in Agile Software Development Methodologies: A Comprehensive Analysis of Industry Adoption and Practices** *IJARCCE* [[paper](https://doi.org/10.17148/ijarcce.2025.1411132)]
- [2025] **Software-in-the-Loop Simulation Implementation Methodology for Autonomous Vehicle System Development** *Transactions of Korean Society of Automotive Engineers* [[paper](https://doi.org/10.7467/ksae.2025.33.11.967)]
- [2025] **Automotive software product lines for ECU software configuration: A systematic literature review** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112716)]
- [2025] **Design Methodologies in The Software Development Process** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17546418)]
- [2025] **Applying Scrumban in Hybrid Software and Hardware Teams: An Experience Report** [[paper](https://doi.org/10.5753/sbqs.2025.15079)]
- [2025] **Utilization, Challenges, And Opportunities Of AI-Driven English Language Development Software of Language Teachers** *Research and Analysis Journal* [[paper](https://doi.org/10.18535/raj.v8i11.572)]
- [2025] **Impact of Agile Software Development Team Leaders� Mindset on Dynamic Capabilities for Achieving Organizational Agility** *Proceedings of the International Conference on Information Systems Development* [[paper](https://doi.org/10.62036/isd.2025.26)]
- [2025] **Quality assessment of software requirements using artificial intelligence methods: A systematic literature review** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107979)]
- [2025] **Privacy by design: Aligning GDPR and software engineering specifications with a requirements engineering approach** *Information and Software Technology* [[paper](https://arxiv.org/abs/2510.21591)]
- [2025] **Integration of Artificial Intelligence Into Software Engineering Practices: A Case Study of an Artifact Restoration Application** [[paper](https://doi.org/10.1109/inista68122.2025.11249671)]
- [2025] **Generative AI in Agile Software Development: A Comprehensive Survey** [[paper](https://doi.org/10.1109/icidca66325.2025.11280486)]
- [2025] **Software engineering in IoT: Insights from a survey of 361 experts** *Internet of Things* [[paper](https://doi.org/10.1016/j.iot.2025.101805)]
- [2025] **Secure Software Engineering for Industrial IoT: Integrating Threat Modeling into the Development Lifecycle** *ICCK Journal of Software Engineering* [[paper](https://doi.org/10.62762/jse.2025.729568)]
- [2025] **Evolution at the Core of Digital Twin Engineering** [[paper](https://doi.org/10.1109/models-c68889.2025.00119)]
- [2025] **Perspectives, Needs and Challenges for Sustainable Software Engineering Teams: A FinServ Case Study** [[paper](https://doi.org/10.1109/esem64174.2025.00022)]
- [2025] **Security Requirements Engineering: A Review and Analysis** *Computers* [[paper](https://doi.org/10.3390/computers14100429)]
- [2025] **Comparative Analysis of Software Development Methodologies** *Applied and Computational Engineering* [[paper](https://doi.org/10.54254/2755-2721/2026.tj27796)]
- [2025] **Management Roles in the Transition from Traditional to Agile Software Development Methodologies** *New University of Lisbon's Repository (New University of Lisbon)* [[paper](https://hdl.handle.net/10362/190260)]
- [2025] **Collaborative LLM agents for flexible software development of intelligent industrial robot control systems** *Complex & Intelligent Systems* [[paper](https://doi.org/10.1007/s40747-025-02051-z)]
- [2025] **Using artificial intelligence in software development processes: achievements and challenges** *Sustainable Engineering and Innovation ISSN 2712-0562* [[paper](https://doi.org/10.37868/sei.v7i2.id526)]
- [2025] **Management of IT Projects Using Transformer-Based Large Language Models for Software Development** [[paper](https://doi.org/10.1109/aict67988.2025.11268706)]
- [2025] **Software Development Projects as a Way for Multidisciplinary Soft and Future Skills Education** *Education Sciences* [[paper](https://doi.org/10.3390/educsci15101371)]
- [2025] **Rapid High Performance Liquid Chromatography methodologies for analytical characterization of biotherapeutic products** *Journal of Chromatography Open* [[paper](https://doi.org/10.1016/j.jcoa.2025.100272)]
- [2025] **AI and Machine Learning-Driven Software Development Frameworks for Healthcare Applications** [[paper](https://doi.org/10.1109/icscn67106.2025.11308160)]
- [2025] **Enhancing Security Practices across the Software Development Lifecycle: The Role of Artificial Intelligence** *Asian Journal of Research in Computer Science* [[paper](https://doi.org/10.9734/ajrcos/2025/v18i10767)]
- [2025] **A Comparative Study of Development Methodologies in Healthcare Software Systems: Agile, Classical Methodologies and DevOps** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-01967-7_11)]
- [2025] **A Novel Hybrid Deep Learning Framework with Metaheuristic Optimization for Accurate Software Effort Estimation** *SN Computer Science* [[paper](https://doi.org/10.1007/s42979-025-04459-3)]
- [2025] **Enhancing Quality Assurance Practices in Software Development: Application of Agile Methodology** *Asian Journal of Research in Computer Science* [[paper](https://doi.org/10.9734/ajrcos/2025/v18i10773)]
- [2025] **Learning through Practice: Teaching Empirical Software Engineering for Undergraduate Students** [[paper](https://doi.org/10.5753/sbes.2025.11268)]
- [2025] **A REVIEW OF SUSTAINABLE SOFTWARE ENGINEERING PRACTICES IN THE ERA OF ARTIFICIAL INTELLIGENCE** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19052589)]
- [2025] **Software Engineering Practice of Microservice Architecture in Full Stack Development: From Architecture Design to Performance Optimization** *Machine Learning Theory and Practice* [[paper](https://doi.org/10.38007/ml.2025.050107)]
- [2025] **Pedagogical Resources for Conducting STEM Engineering Projects in Chemistry Teacher Education: A Design-Based Research Approach** *Education Sciences* [[paper](https://doi.org/10.3390/educsci15091196)]
- [2025] **The impact of personality traits on scrum team effectiveness: Insights from Vietnamese software development companies** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107878)]
- [2025] **Requirements-Driven Automated Software Testing: A Systematic Review** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3767739)]
- [2025] **Software and pipelines for registration and analyses of rodent brain image data in reference atlas space** *Frontiers in Neuroinformatics* [[paper](https://doi.org/10.3389/fninf.2025.1629388)]
- [2025] **An automated software methodology for biomedical statistics, data pre-processing, and machine learning** *Computer Methods and Programs in Biomedicine* [[paper](https://doi.org/10.1016/j.cmpb.2025.109096)]
- [2025] **A Scrumban Integrated Approach to Improve Software Development Process and Product Delivery** *The American Journal of Interdisciplinary Innovations and Research* [[paper](https://doi.org/10.37547/tajiir/volume07issue09-07)]
- [2025] **Real-time privacy vulnerability detection techniques in software development: A Systematic Literature Review** *Computers & Security* [[paper](https://doi.org/10.1016/j.cose.2025.104659)]
- [2025] **METHODS FOR EVALUATING SOFTWARE ACCESSIBILITY** *Radio Electronics Computer Science Control* [[paper](https://arxiv.org/abs/2509.23469)]
- [2025] **STEM-based approaches to soft skills development: a synthesis of meta-analytic findings and empirical evidence** *Frontiers in Education* [[paper](https://doi.org/10.3389/feduc.2025.1663155)]
- [2025] **Dynamic Integration and Full-Process Automation of Agile R&D Toolchain for Software Factories** [[paper](https://doi.org/10.1109/iotaai66837.2025.11213096)]
- [2025] **A Systematic Literature Review on Explainability for ML/DL-based Software Engineering** *ACM Computing Surveys* [[paper](https://doi.org/10.1145/3763230)]
- [2025] **A methodology for Electrics/Electronics platform release management in the automotive domain** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112605)]
- [2025] **When machine learning models retire, decay, or become obsolete: A review on algorithms, software, and hardware** *Renewable and Sustainable Energy Reviews* [[paper](https://doi.org/10.1016/j.rser.2025.116231)]
- [2025] **MSTI-3 Spacecraft Attitude Control Software Development using Automatic Code Generation** *Digital Commons - USU (Utah State University)* [[paper](https://digitalcommons.usu.edu/smallsat/1994/all1994/15)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **USCHA: A SpecLoop Controlled Methodology for Software Development with LLM Agents** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21228013)]
- [2026] **Advancing research software engineering with AI: a research framework** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-026-00621-0)]
- [2026] **Coverage vs. Depth: The Methodological Warrant of Coverage-Architecture Scholarship — With a Disciplinary Catalog of the Crimson Hexagonal Archive at 705 Deposits** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20358078)]
- [2026] **Software Development Methodologies (2000–2026): A Scopus-Based Bibliometric Mapping of Scholarly Output and Thematic Evolution** *West Science Information System and Technology* [[paper](https://doi.org/10.58812/wsist.v4i01.2833)]
- [2026] **Orchestration and Context Serialization: A Systematic Methodology for LLM-Based Software Development** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19892525)]
- [2026] **Promptware Engineering: Software Engineering for Prompt-Enabled Systems** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3796535)]
- [2026] **A Grounded Theory of Debugging in Professional Software Engineering Practice** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2602.11435)]
- [2026] **Understanding Software Engineering Practices and Tools in Undergraduate Mechanical Engineering Students** [[paper](https://doi.org/10.1145/3770762.3772667)]
- [2026] **Multidimensional AI-Enabled Software Engineering Practices and Entrepreneurial Innovation Performance: A Conceptual Framework** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18533674)]
- [2026] **Multidimensional Cloud-Native Software Engineering Practices and Entrepreneurial Business Scalability: A Conceptual Perspective** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18534116)]
- [2026] **Multimodal Dataset on Agile Software Development Methodologies** *FDRepo UB Bamberg* [[paper](https://doi.org/10.48564/unibafd-3t91e-2pd14)]
- [2026] **Integrating formal methods and automated tools for DO-178C compliance in UAV software** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108068)]
- [2026] **Evaluating the requirements engineering process in model transformation development: a state of practice analysis** *Software & Systems Modeling* [[paper](https://doi.org/10.1007/s10270-025-01352-8)]
- [2026] **The Business Value and the Dark Sides of Agile Software Development Methodologies : Theoretical Foundations and Empirical Evidence** [[paper](https://doi.org/10.20378/irb-113764)]
- [2026] **On the Need to Rethink Trust in AI Assistants for Software Development: A Critical Review** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2026.3659804)]
- [2026] **A Systemic View of a Software Engineering Education Curriculum: Requirements and Guidelines in the Era of Generative AI** *Journal of Integrated Design and Process Science* [[paper](https://doi.org/10.1177/10920617251405471)]

##### 2025

- [2025] **From software architecture models to pipelines: a conceptual framework for model transformation in DevOps** *Frontiers in Computer Science* [[paper](https://doi.org/10.3389/fcomp.2025.1714197)]
- [2025] **FPGA technology in healthcare: A comprehensive review of hardware and software solutions for diagnostics, imaging, and patient care** *Array* [[paper](https://doi.org/10.1016/j.array.2025.100622)]
- [2025] **Factors influencing the adoption of secure software engineering practices in pre-adoption and post-adoption phases** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-27024-7)]
- [2025] **Leveraging model-based systems and software engineering for digital twin engineering: Methods and digital thread opportunities** *Journal of Industrial Information Integration* [[paper](https://doi.org/10.1016/j.jii.2025.101023)]
- [2025] **Towards AI-Augmented Software Engineering: A Theoretical Framework** *ICCK Journal of Software Engineering* [[paper](https://doi.org/10.62762/jse.2025.407864)]
- [2025] **Generative AI and the Future of Software Engineering in Saudi Arabia: Governance, Innovation, and Workforce Transformation** *International Journal of Theoretical & Applied Computational Intelligence* [[paper](https://doi.org/10.65278/ijtaci.2025.4)]
- [2025] **From Requirements to Code: Understanding Developer Practices in LLM-Assisted Software Engineering** [[paper](https://doi.org/10.1109/re63999.2025.00032)]
- [2025] **Editorial: Robotics software engineering** *Frontiers in Robotics and AI* [[paper](https://doi.org/10.3389/frobt.2025.1686496)]
- [2025] **Do’s and Don’t s of Partnering with Industry to Educate Software Engineering Students: Recommendations Based on a Teaching Experience** [[paper](https://doi.org/10.5753/sbes.2025.11193)]
- [2025] **Quantum-ready software engineering: principles, frameworks, and hybrid development pipelines** *International Journal of Information technology and Computer Engineering* [[paper](https://doi.org/10.55529/ijitc.52.1.7)]
- [2025] **Model for the Adoption of AI Tools in the Software Development Life Cycle: A Framework for Prompt Optimization in LLMs** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202509.1036.v1)]
- [2025] **Recent developments in atomistic modeling: machine learning models and datasets, methods, software releases, and scientific events** *AIDASCO Reviews* [[paper](https://doi.org/10.59783/aire.2025.79)]

##### 1986

- [1986] **No Silver Bullet: Essence and Accidents of Software Engineering** *IEEE Computer* [[paper](https://doi.org/10.1145/358849.358862)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Institutionalizing Research Software Engineering Practices Through an Academic Open Source Program Office** [[paper](https://doi.org/10.1145/3785462.3815879)]
- [2026] **LARGE LANGUAGE MODELS IN AI-AUGMENTED DEVSECOPS PIPELINES: EXPLORING SECURE SOFTWARE ENGINEERING PRACTICES AND ARCHITECTURAL CHALLENGES** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21771477)]
- [2026] **Software Engineering Practice Catalogue** [[paper](https://doi.org/10.1201/9781003362111-6)]
- [2026] **Software Engineering Practice Adoption** [[paper](https://doi.org/10.1201/9781003362111-7)]
- [2026] **Software Engineering Practices for Advanced Therapy Medicinal Products** [[paper](https://doi.org/10.1109/icsa-c68850.2026.00031)]
- [2026] **It's Alive! What a Live Object Environment Changes in Software Engineering Practice** [[paper](https://arxiv.org/abs/2603.02987)]
- [2026] **A Study of the Impact of Artificial Intelligence and Machine Learning on Software Engineering Practices in the Education Sector** *INTERNATIONAL JOURNAL OF MATHEMATICS AND COMPUTER RESEARCH* [[paper](https://doi.org/10.5281/zenodo.19148196)]
- [2026] **Examining Software Engineering Practices in the Pre-AI and Post-AI ERA** [[paper](https://doi.org/10.1109/icaiic68212.2026.11454249)]
- [2026] **Be a Partner, not a Bystander in Software Engineering Practice: Bridging the Gaps between Academia and Industry** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2604.16315)]
- [2026] **High performance computing software engineering practices** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-443-45574-2.00021-6)]
- [2026] **Exploring Technology Probe Applications in Software Engineering Practice** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6443058)]
- [2026] **Empathy Guidelines for Improving Practitioner Well-Being and Software Engineering Practices** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2026.3654969)]
- [2026] **Responsible Software Engineering Practices Toward AI Readiness and Trustworthy Systems** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-30836-8_42)]
- [2026] **Replication Package for the paper: Leadership in Software Engineering: Practices, Effects, and Perceived GenAI Influence** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21998674)]
- [2026] **Foundation Models in Software Engineering: A Taxonomy, Systematic Review, and In-Depth Analysis of Testing Support** *Information* [[paper](https://doi.org/10.3390/info17010073)]
- [2026] **An Empirical Study of Generative AI Adoption in Software Engineering** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6459920)]

##### 2025

- [2025] **Galene: A Toolkit for Encapsulating Software Engineering Practices in Marine Science AI Applications** [[paper](https://doi.org/10.1109/apsec66846.2025.00114)]
- [2025] **Supplementary materials for the paper "A Preliminary Search for Evidence on Government Software Engineering Practices: Results from Three Rapid Reviews"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18099187)]
- [2025] **Improving practical software engineering teaching with industrial mentoring of open source team projects** [[paper](https://doi.org/10.1145/3772338.3772350)]
- [2025] **SOFTWARE ENGINEERING: PRINCIPLES AND PRACTICES** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19906462)]
- [2025] **Best Practices for Machine Learning-Assisted Protein Engineering** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c01983)]
- [2025] **“It Works on My Research”: An Argument for Prioritized Software Testing in Research Software** *EPiC series in computing* [[paper](https://doi.org/10.29007/phr7)]
- [2025] **Report from MDE practice: An interview-based evaluation of model-driven engineering uses** *PLoS ONE* [[paper](https://doi.org/10.1371/journal.pone.0335461)]
- [2025] **Software Engineering: Emerging Trends and Practices in System Development** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-04581-2)]
- [2025] **Manifestations of Empathy in Software Engineering: How, Why, and When It Matters** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3612888)]
- [2025] **An Evidence-Based Study on the Relationship of Software Engineering Practices on Code Smells in Python ML Projects** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04207-1_8)]
- [2025] **Agentic Software Engineering: Foundational Pillars and a Research Roadmap** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2509.06216)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Reshaping the SDLC for Data- and AI-Centric Systems** [[paper](https://arxiv.org/abs/2608.17824)]
- [2026] **Algorithm-driven Development: A Proactive Approach to Improving Software Quality and Reducing Defects** [[paper](https://arxiv.org/abs/2608.01533)]
- [2026] **Exploring Dependence, Overreliance, and Addiction Related Behaviors Associated with Large Language Model Use Among Software Engineers** [[paper](https://arxiv.org/abs/2608.05561)]
- [2026] **Multiparty Session Types for GDPR Purpose Compliance** [[paper](https://arxiv.org/abs/2607.20190)]
- [2026] **GitHub Template Repositories: Served Domains, Maintenance, and Practitioner Guidelines** [[paper](https://arxiv.org/abs/2606.14616)]
- [2026] **AI-driven Software Development: A Pragmatic Path to Agentic Development Processes** [[paper](https://arxiv.org/abs/2606.15283)]
- [2026] **Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation** [[paper](https://arxiv.org/abs/2606.28998)]
- [2026] **Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents** [[paper](https://arxiv.org/abs/2606.05391)]
- [2026] **Architectural Constraints Alignment in AI-assisted, Platform-based Service Development** [[paper](https://arxiv.org/abs/2605.04973)]
- [2026] **A Research Agenda on Agents and Software Engineering: Outcomes from the Rio A2SE Seminar** [[paper](https://arxiv.org/abs/2605.11720)]
- [2026] **In-IDE Toolkit for Developers of AI-Based Features** [[paper](https://arxiv.org/abs/2605.14612)]
- [2026] **Operationalizing Ethics for AI Agents: How Developers Encode Values into Repository Context Files** [[paper](https://arxiv.org/abs/2605.05584)]
- [2026] **Prediction Model of Motivators and Demotivators of Integrating Large Language Models in Software Engineering Education: An Empirical Study** [[paper](https://arxiv.org/abs/2605.09393)]
- [2026] **Shift-Up: A Framework for Software Engineering Guardrails in AI-native Software Development -- Initial Findings** [[paper](https://arxiv.org/abs/2604.20436)]
- [2026] **AutonomyLens: A Self-Evolving Simulation-Based Testing Loop for Autonomous Systems** [[paper](https://arxiv.org/abs/2604.11672)]
- [2026] **Autark: A Serverless Toolkit for Prototyping Urban Visual Analytics Systems** [[paper](https://arxiv.org/abs/2604.20759)]
- [2026] **Don't Make Models Guess Security and Safety: Symbolic Guardrails for Domain-Specific AI Agents** [[paper](https://arxiv.org/abs/2604.15579)] [[code](https://github.com/hyn0027/agent-symbolic-guardrails)]
- [2026] **Fuzzing REST APIs in Industry: Necessary Features and Open Problems** [[paper](https://arxiv.org/abs/2604.01759)]
- [2026] **How Do Developers Interact with AI? An Exploratory Study on Modeling Developer Programming Behavior** [[paper](https://arxiv.org/abs/2604.16393)]
- [2026] **On the Economic Implications of Diversity in Software Engineering** [[paper](https://arxiv.org/abs/2603.22523)]
- [2026] **Large Language Models for Software Testing Education: an Experience Report** [[paper](https://arxiv.org/abs/2603.26329)]
- [2026] **Human-AI Synergy in Agentic Code Review** [[paper](https://arxiv.org/abs/2603.15911)]
- [2026] **A Course on the Introduction to Quantum Software Engineering: Experience Report** [[paper](https://arxiv.org/abs/2602.07589)]
- [2026] **SeRe: A Security-Related Code Review Dataset Aligned with Real-World Review Activities** [[paper](https://arxiv.org/abs/2601.01042)]
- [2026] **Revisiting Software Engineering Education in the Era of Large Language Models: A Curriculum Adaptation and Academic Integrity Framework** [[paper](https://arxiv.org/abs/2601.08857)]
- [2026] **From Human to Machine Refactoring: Assessing GPT-4's Impact on Python Class Quality and Readability** [[paper](https://arxiv.org/abs/2601.13139)]
- [2026] **Prompt Driven Development with Claude Code: Building a Complete TUI Framework for the Ring Programming Language** [[paper](https://arxiv.org/abs/2601.17584)]

##### 2025

- [2025] **"Can you feel the vibes?": An exploration of novice programmer engagement with vibe coding** [[paper](https://arxiv.org/abs/2512.02750)]
- [2025] **Explainable Verification of Hierarchical Workflows Mined from Event Logs with Shapley Values** [[paper](https://arxiv.org/abs/2512.09562)]
- [2025] **On the use of extended reality to support software development activities: A systematic literature review** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107999)]
- [2025] **Injecting Sustainability in Software Architecture: A Rapid Review** [[paper](https://arxiv.org/abs/2512.00106)]
- [2025] **Sustainability of Machine Learning-Enabled Systems: The Machine Learning Practitioner's Perspective** [[paper](https://arxiv.org/abs/2511.00901)]
- [2025] **Rethinking Services in the Quantum Age: The SOQ Paradigm** [[paper](https://arxiv.org/abs/2510.03890)]
- [2025] **Impact of LLMs on Team Collaboration in Software Development** [[paper](https://arxiv.org/abs/2510.08612)]
- [2025] **Ensuring Robustness in ML-enabled Software Systems: A User Survey** [[paper](https://arxiv.org/abs/2510.18292)]
- [2025] **A Brief History of the Waterfall Model: Past, Present, and Future** [[paper](https://arxiv.org/abs/2510.03894)]
- [2025] **Lifecycle-Aware code generation: Leveraging Software Engineering Phases in LLMs** [[paper](https://arxiv.org/abs/2510.24019)]
- [2025] **Generative AI and the Transformation of Software Development Practices** [[paper](https://arxiv.org/abs/2510.10819)]
- [2025] **Refactoring with LLMs: Bridging Human Expertise and Machine Understanding** [[paper](https://arxiv.org/abs/2510.03914)]
- [2025] **Leveraging Test Driven Development with Large Language Models for Reliable and Verifiable Spreadsheet Code Generation: A Research Framework** [[paper](https://arxiv.org/abs/2510.15585)]
- [2025] **Large Language Models for Fault Localization: An Empirical Study** [[paper](https://arxiv.org/abs/2510.20521)]
- [2025] **BDiff: Block-aware and Accurate Text-based Code Differencing** [[paper](https://arxiv.org/abs/2510.21094)]
- [2025] **Social debt in software development environments: A systematic literature review** *Science of Computer Programming* [[paper](https://doi.org/10.1016/j.scico.2025.103396)]
- [2025] **Reproducibility Practices of Software Engineering Controlled Experiments: Survey and Prospective Actions.** *ICEIS* [[paper](https://dblp.org/rec/conf/iceis/CordeiroO25a)]
- [2025] **Surveying Deliberation Practices and Methodological Needs in Robotics Software Engineering.** *TAROS* [[paper](https://dblp.org/rec/conf/taros/KlauckHLJ25)]
- [2025] **Best Practices and Evaluation Methods for Narrative Information Visualizations: A Systematic Review** *Proceedings of the 20th International Conference on Evaluation of Novel Approaches to Software Engineering* [[paper](https://doi.org/10.5220/0013202000003928)]

##### 2024

- [2024] **The Brazilian Practices for Handling Sustainability in Software Engineering: a Replicated Survey.** *SBQS* [[paper](https://dblp.org/rec/conf/sbqs/MeloVSP024)]
- [2024] **Challenges and Solutions in Software Testing Practices: A Systematic Review in Tanzanian Software Development Companies** [[paper](https://doi.org/10.2139/ssrn.4607901)]

##### 2023

- [2023] **Collaborative Model-Driven Software Engineering - A systematic survey of practices and needs in industry.** *J. Syst. Softw.* [[paper](https://dblp.org/rec/journals/jss/DavidAML23)]
- [2023] **People Management Problems and Practices in Software Development Projects: A Systematic Literature Review** *Proceedings of the 25th International Conference on Enterprise Information Systems* [[paper](https://doi.org/10.5220/0011985300003467)]

##### 2022

- [2022] **A Survey of Requirements Engineering and Software Testing Practices in Agile Teams.** *SAST* [[paper](https://dblp.org/rec/conf/sast/CoutinhoAM22)]
- [2022] **Agile requirements engineering practices: a survey in Brazilian software development companies.** *CoRR* [[paper](https://arxiv.org/abs/2202.12956)]
- [2022] **Hybrid Practices in Global Software Development: A Systematic Literature Review** *International Journal of Software Engineering &amp; Applications* [[paper](https://doi.org/10.5121/ijsea.2022.13101)]

##### 2021

- [2021] **A survey on the software engineering practices in brazilian software startups.** *CIbSE* [[paper](https://dblp.org/rec/conf/cibse/0001CM21)]
- [2021] **A Brief Survey of Current Software Engineering Practices in Continuous Integration and Automated Accessibility Testing.** *CoRR* [[paper](https://arxiv.org/abs/2103.00097)]
- [2021] **A Survey on Software Engineering Practices in Brazilian Startups.** *CoRR* [[paper](https://arxiv.org/abs/2108.00343)]

##### 2019

- [2019] **Communication and Documentation Practices in Agile Requirements Engineering: A Survey in Polish Software Industry.** *SIGSAND/PLAIS* [[paper](https://dblp.org/rec/conf/sigsand/JarzebowiczS19)]

##### 2018

- [2018] **What Software Engineering “Best Practices” are we Teaching Students - a Systematic Literature Review** *2018 IEEE Frontiers in Education Conference (FIE)* [[paper](https://doi.org/10.1109/fie.2018.8658576)]
- [2018] **A survey on modeling and model-driven engineering practices in the embedded software industry.** *J. Syst. Archit.* [[paper](https://dblp.org/rec/journals/jsa/AkdurGD18)]

##### 2017

- [2017] **Systematic literature review on the impacts of agile release engineering practices** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2017.01.009)]
- [2017] **Using the Case Survey Method to Explore Engineering Practices in Software Start-Ups.** *SoftStart@ICSE* [[paper](https://dblp.org/rec/conf/icse/Klotins17)]

##### 2016

- [2016] **Challenges and best practices in industry-academia collaborations in software engineering: A systematic literature review** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2016.07.006)]

##### 2015

- [2015] **Claims about the use of software engineering practices in science: A systematic literature review** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2015.07.011)]
- [2015] **A survey of software engineering practices in Turkey.** *J. Syst. Softw.* [[paper](https://dblp.org/rec/journals/jss/GarousiCBD15)]

##### 2014

- [2014] **A Survey of Software Engineering Practices in Turkey (extended version).** *CoRR* [[paper](https://arxiv.org/abs/1412.4648)]

##### 2012

- [2012] **Global software engineering and agile practices: a systematic review** *Journal of Software: Evolution and Process* [[paper](https://doi.org/10.1002/smr.561)]
- [2012] **A survey of software engineering best practices for the development of smart applications in Ambient Intelligence.** *J. Ambient Intell. Smart Environ.* [[paper](https://dblp.org/rec/journals/jaise/PreuveneersN12)]

##### 2011

- [2011] **Survey of Software Engineering Practices in Undergraduate Information System Projects.** *ICSECS* [[paper](https://dblp.org/rec/conf/icsecs/YusopKAR11)]

##### 2010

- [2010] **Agile Practices in Global Software Engineering - A Systematic Map** *2010 5th IEEE International Conference on Global Software Engineering* [[paper](https://doi.org/10.1109/icgse.2010.14)]

##### 2009

- [2009] **Requirements Engineering Problems and Practices in Software Companies: An Industrial Survey.** *FGIT-ASEA* [[paper](https://dblp.org/rec/conf/fgit/SolemonSG09)]

##### 2004

- [2004] **A Preliminary Survey on Software Testing Practices in Australia.** *Australian Software Engineering Conference* [[paper](https://dblp.org/rec/conf/aswec/NgMRGC04)]

##### 2000

- [2000] **A Survey of Software Development Practices in the New Zealand Software Industry .** *Australian Software Engineering Conference* [[paper](https://dblp.org/rec/conf/aswec/GrovesNRRU00)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **The Ethical Concerns Raised Using AI Tools on Software Development Systems** *Studies in systems, decision and control* [[paper](https://doi.org/10.1007/978-3-031-95310-1_149)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Generative Artificial Intelligence for Requirements Engineering in Software Development – Analysis of the State-of-the-Art** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-13187-4_12)]

##### 2025

- [2025] **Prompts as Software Engineering Artifacts: A Research Agenda and Preliminary Findings** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-12089-2_32)]
- [2025] **Determining the intrinsic structure of public software development history: an exploratory study** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10741-y)]
- [2025] **From Diverse Origins to a DEI Crisis: The Pushback Against Equity, Diversity, and Inclusion in Software Engineering** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04207-1_12)]
- [2025] **Reconsidering Requirements Engineering: Human–AI Collaboration in AI-Native Software Development** *Lecture notes in computer science* [[paper](https://arxiv.org/abs/2510.04380)]
- [2025] **Leveraging LLM-based data augmentation for automatic classification of recurring tasks in software development projects** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112641)]
- [2025] **Development of Agentic Workflows with LangGraph for Software Development Life Cycle Automation** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-031-98235-4_4)]

[⬆ Back to top](#paper-list)

### Developer Tools

#### Method

##### 2026

- [2026] **The Stoic Unix Philosophy: Building Calm Tools for a Chaotic World** *tobias-weiss.org* [[paper](https://tobias-weiss.org/content/devops/stoic-unix-philosophy/)]
- [2026] **Does ISO-Grounded NFR Specification Improve LLM Code Generation? A Comparison of Rich and Structured Interventions against a Natural-Language Baseline** [[paper](https://arxiv.org/abs/2608.13742)]
- [2026] **Statistical Analysis of Executability and Program Equivalence in Decompilation for IoT Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.06960)]
- [2026] **mktlib — reference implementation of the Möbius–Klein transform** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21532662)]
- [2026] **AssumptionMiner: Extracting, Tracing, and Revising Implicit Assumptions in LLM Code Generation** [[paper](https://arxiv.org/abs/2607.22898)]
- [2026] **Test Coverage Analysis of Agentic Pull Requests** [[paper](https://arxiv.org/abs/2607.18057)]
- [2026] **Beyond Price and Benchmark: A Cost–Methodology–Fit Framework for Selecting AI Developer Tools, with a Proposed Evaluation Protocol** [[paper](https://doi.org/10.64823/ijcsa.2601002)]
- [2026] **Radial-velocity Two-body (RV2B): A User-friendly and Optimized Command-line Interface for Fitting the Radial Velocity Equation** *Research Notes of the AAS* [[paper](https://doi.org/10.3847/2515-5172/ae8b96)]
- [2026] **DuoDose** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21455713)]
- [2026] **OptimSolution: A Cross-Platform Framework for Benchmarking, Sensitivity, and Complexity Analysis of Continuous Optimisation Methods** *Software* [[paper](https://doi.org/10.3390/software5030028)]
- [2026] **A generalized software framework for consolidation of radiotherapy planning and delivery data from diverse data sources** *Advances in Radiation Oncology* [[paper](https://arxiv.org/abs/2411.08876)]
- [2026] **Rule Based Approach for Conversational AI Chatbot using Log pattern Detection** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21559398)]
- [2026] **VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation** [[paper](https://arxiv.org/abs/2606.07992)]
- [2026] **Is Agent Code Less Maintainable Than Human Code?** [[paper](https://arxiv.org/abs/2606.21804)]
- [2026] **Privacy-Preserving Local LLM Inference for Developer Tooling — AI, LLM, Privacy, Sovereign AI, and Post-Cloud Architecture (Anticode)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20775678)]
- [2026] **opencltools: 'OpenCL' Tools for R Package Developers** [[paper](https://doi.org/10.32614/cran.package.opencltools)]
- [2026] **GPUMDkit: A User‐Friendly Toolkit for GPUMD and NEP** *Materials Genome Engineering Advances* [[paper](https://doi.org/10.1002/mgea.70074)]
- [2026] **Biom3d, a modular framework to host and develop 3D segmentation methods** *Medical Image Analysis* [[paper](https://doi.org/10.1016/j.media.2026.104184)]
- [2026] **What Software Engineering Looks Like to AI Agents? -- An Empirical Study of AI-Only Technical Discourse on MoltBook** [[paper](https://arxiv.org/abs/2605.08380)]
- [2026] **Enhancing Debugging and Maintainability of ASP.NET Core Backend APIs Using Structured Logging and Centralized Exception Handling** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20201105)]
- [2026] **Automated Log Analyzer Using Python for System Monitoring** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19995629)]
- [2026] **Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution** [[paper](https://arxiv.org/abs/2604.05955)]
- [2026] **The Most Important Developer Tools Every Programmer Should Know About** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32048580.v1)]
- [2026] **The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Review and Mapping Study** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2507.03156)]
- [2026] **Robust Methods for Developer Screening in Rapidly Evolving AI Contexts** [[paper](https://doi.org/10.1145/3772318.3790302)]
- [2026] **Design and Implementation of MCP-Web-Curl: A Model Context Protocol Server for Web and API Access in Agentic Coding Assistants** *JURNAL TEKNIK INFORMATIKA* [[paper](https://doi.org/10.15408/jti.v19i1.49625)]
- [2026] **Floating-point–consistent cross-verification methodology for reproducible and interoperable DDA solvers with fair benchmarking** *Computer Physics Communications* [[paper](https://arxiv.org/abs/2603.02871)]
- [2026] **Natural Language Processing-Based Command Line Application** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19759864)]
- [2026] **Performance Evaluation of Random Forest and Isolation Forest Algorithms for Detecting Anomalies in SIAKAD Server Log Data** *SinkrOn* [[paper](https://doi.org/10.33395/sinkron.v10i2.16030)]
- [2026] **Nginx-Narrator: LLM-Based Automated Nginx Log Analysis for UX Friction Detection in Web Applications** [[paper](https://doi.org/10.1109/icwr69602.2026.11513306)]
- [2026] **IndustriConnect: MCP Adapters and Mock-First Evaluation for AI-Assisted Industrial Operations** [[paper](https://arxiv.org/abs/2603.24703)]
- [2026] **SpecOps: A Fully Automated AI Agent Testing Framework in Real-World GUI Environments** [[paper](https://arxiv.org/abs/2603.10268)]
- [2026] **Developer Tool Comparison Matrix 2026: Feature Analysis of 18 Infrastructure and Development Tools** *Open MIND* [[paper](https://mohitkhare.me)]
- [2026] **GreenDIGIT Deliverable D5.2 Energy Measurement and Impact Assessment Framework and Methodology and Developer Tooling** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20289682)]
- [2026] **Towards a framework for cross-boundary collaborative open learning for cross-institutional academic development** *Research Output (Edinburgh Napier University)* [[paper](https://napier-surface.worktribe.com/1025583/1/Towards%20a%20framework%20for%20cross-boundary%20collaborative%20open%20learning%20for%20cross-institutional)]
- [2026] **Development and application of an environmental risk register for marine energy device and project developers** *Ocean & Coastal Management* [[paper](https://doi.org/10.1016/j.ocecoaman.2026.108170)]
- [2026] **MKado: a toolkit for McDonald-Kreitman tests of natural selection** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.64898/2026.03.02.709122)]
- [2026] **BlotTool: A reproducible command-line workflow for western blot densitometry** *Open MIND* [[paper](https://doi.org/10.5281/zenodo.18870068)]
- [2026] **Inference of process capability indices <i>C</i> <sub> <i>p</i> <i>y</i> </sub> and <i>C</i> <sub> <i>N</i> <i>p</i> <i>m</i> <i>k</i> </sub> using different methods of estimation for log-logistic distribution** *Communication in Statistics- Theory and Methods* [[paper](https://doi.org/10.1080/03610926.2026.2629495)]
- [2026] **Macro-to-TWh: A Log-Stabilized Benchmark of 21 Supervised Regressors for Country-Level Primary Energy Consumption Prediction** [[paper](https://doi.org/10.1109/satc69565.2026.11542520)]
- [2026] **A Hybrid Machine Learning Approach for Accurate Horizontal in-situ Stress Prediction in Complex Hydrocarbon Reservoirs Using Core and Well Log Data** *Rock Mechanics Bulletin* [[paper](https://doi.org/10.1016/j.rockmb.2026.100325)]
- [2026] **Beyond the Control Equations: An Artifact Study of Implementation Quality in Robot Control Software** [[paper](https://arxiv.org/abs/2602.04799)]
- [2026] **Unveiling the Role of ChatGPT in Software Development: Insights from Developer-ChatGPT Interactions on GitHub** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3798163)]
- [2026] **SOLWEIG-GPU: GPU-Accelerated Thermal Comfort Modeling Framework for Urban Digital Twins** *The Journal of Open Source Software* [[paper](https://doi.org/10.21105/joss.09535)]
- [2026] **CosCNN-DTQ: An integrated framework for efficient deployment of cosine convolutional neural networks** *Neurocomputing* [[paper](https://doi.org/10.1016/j.neucom.2026.133110)]
- [2026] **Doing More with Less: Accurate and Scalable Ligand Free Energy Calculations by Focusing on the Binding Site** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c02932)]
- [2026] **Situated Understanding of Errors in Older Adults’ Interactions with Voice Assistants: A Month-Long, In-Home Study** *ACM Transactions on Accessible Computing* [[paper](https://doi.org/10.1145/3796236)]
- [2026] **Simulation and real-world applications of exponential–log estimators under neutrosophic ranked set sampling** *Statistics* [[paper](https://doi.org/10.1080/02331888.2026.2631756)]
- [2026] **Predicting and optimizing viscosity of dental resin composites with Gaussian process regression and Bayesian optimization** *Dental Materials* [[paper](https://doi.org/10.1016/j.dental.2026.02.018)]
- [2026] **Estimating shear wave velocity of geologically complex reservoirs using a hybrid machine learning approach, integrating core measurements and geophysical logs** *Unconventional Resources* [[paper](https://doi.org/10.1016/j.uncres.2026.100356)]
- [2026] **From Logic to Toolchains: An Empirical Study of Bugs in the TypeScript Ecosystem** [[paper](https://arxiv.org/abs/2601.21186)]
- [2026] **SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents** [[paper](https://arxiv.org/abs/2601.16746)]
- [2026] **AI builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality** [[paper](https://arxiv.org/abs/2601.16839)]
- [2026] **Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub** [[paper](https://arxiv.org/abs/2601.00477)]
- [2026] **The ICD Platform: end-user and developer tools** *BMC Medical Informatics and Decision Making* [[paper](https://doi.org/10.1186/s12911-025-03317-9)]
- [2026] **The Invisible Adoption Tax: How Non-Technical Frictions Shape Developer Tool Adoption** [[paper](https://doi.org/10.31224/6280)]
- [2026] **Developer Productivity With and Without GitHub Copilot: A Longitudinal Mixed-Methods Case Study** *Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences* [[paper](https://arxiv.org/abs/2509.20353)]
- [2026] **Evaluation of tools used to assess adherence to PRISMA 2020 reveals inconsistent methods and poor tool implementability: part I of a systematic review** *Journal of Clinical Epidemiology* [[paper](https://doi.org/10.1016/j.jclinepi.2026.112133)]
- [2026] **Scripts, Software and Dataset for "Benchmarking LLM Commit Message Generation through a Developer-centric Pairwise Preference Framework"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18369469)]
- [2026] **phaser: a unified and extensible framework for fast electron ptychography** *npj Computational Materials* [[paper](https://doi.org/10.1038/s41524-026-01956-8)]
- [2026] **TI-Toolbox: An open-source software for temporal interference stimulation research** *Brain stimulation* [[paper](https://doi.org/10.1016/j.brs.2025.103016)]
- [2026] **RustSASA: A Rust Crate for Accelerated Solvent Accessible Surface Area Calculations** *The Journal of Open Source Software* [[paper](https://doi.org/10.21105/joss.09537)]
- [2026] **CHARMM-GUI Quick Bilayer: Simple and Intuitive One-Stop Membrane Bilayer Builder** *Journal of Molecular Biology* [[paper](https://doi.org/10.1016/j.jmb.2026.169672)]
- [2026] **AxioSAFE: an accessible, semi-automatic filtering tool for the curation of genotyping datasets** *Bioinformatics Advances* [[paper](https://doi.org/10.1093/bioadv/vbag062)]
- [2026] **RVAT: a unified framework to discover & interpret rare variant associations in large DNA sequencing datasets** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18182667)]
- [2026] **Teaching computers geology : Geological knowledge, best practices, uncertainty and justification in drill core logging with machine learning** *KTH Publication Database DiVA (KTH Royal Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:ltu:diva-116863)]

##### 2025

- [2025] **A Practical Solution to Systematically Monitor Inconsistencies in SBOM-based Vulnerability Scanners** [[paper](https://arxiv.org/abs/2512.17710)]
- [2025] **Inter-tool Analysis of a NIST Dataset for Assessing Baseline Nucleic Acid Sequence Screening** *Applied Biosafety* [[paper](https://doi.org/10.1177/15356760251401228)]
- [2025] **Tools and Algorithms for Nanopore Sequencing Data Analysis in Genomics, Metagenomics, and Epigenomics** *Mathematical Biology and Bioinformatics* [[paper](https://doi.org/10.17537/2025.20.588)]
- [2025] **TermiTeach: Natural Language Command Line Interface Tutoring Via Generative AI Simulations** [[paper](https://doi.org/10.1109/ised67359.2025.11405208)]
- [2025] **Chemprop v2: An Efficient, Modular Machine Learning Package for Chemical Property Prediction** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c02332)]
- [2025] **ALCHEMD: Bridging Accessibility and Accuracy in Automated Relative Binding Free Energy Workflows** *Journal of Chemical Theory and Computation* [[paper](https://doi.org/10.1021/acs.jctc.5c01857)]
- [2025] **A fast spectral sum-of-Gaussians method for electrostatic summation in quasi-2D systems** *Numerische Mathematik* [[paper](https://doi.org/10.1007/s00211-025-01518-y)]
- [2025] **Predictive maintenance and inventory optimization in medical device supply chains: a data-driven approach** *Network Modeling Analysis in Health Informatics and Bioinformatics* [[paper](https://doi.org/10.1007/s13721-025-00673-4)]
- [2025] **Software for Studying CASCADE Error Correction Protocols in Quantum Communications** [[paper](https://arxiv.org/abs/2511.23050)]
- [2025] **MermaidSeqBench: An Evaluation Benchmark for NL-to-Mermaid Sequence Diagram Generation** [[paper](https://arxiv.org/abs/2511.14967)]
- [2025] **Overview and Performance Evaluation of Supervisory Controller Synthesis with Eclipse ESCET v4.0** [[paper](https://arxiv.org/abs/2511.04370)]
- [2025] **Empirical Analysis of AI-Assisted Code Generation Tools Impact on Code Quality, Security and Developer Productivity** *International Journal For Multidisciplinary Research* [[paper](https://doi.org/10.36948/ijfmr.2025.v07i06.61350)]
- [2025] **Prakriti (constitutional typology) in Ayurveda: a critical review of Prakriti assessment tools and their scientific validity** *Frontiers in Medicine* [[paper](https://doi.org/10.3389/fmed.2025.1656249)]
- [2025] **Tool learning with language models: a comprehensive survey of methods, pipelines, and benchmarks** *Vicinagearth.* [[paper](https://doi.org/10.1007/s44336-025-00024-x)]
- [2025] **From Tools to Adoption** [[paper](https://doi.org/10.62329/kcep6732)]
- [2025] **A Model for Teaching Machine Learning, Deep Learning, and Research Computing to Domain Scientists on HPC Resources** [[paper](https://doi.org/10.1145/3731599.3767380)]
- [2025] **From Voice to Shell: A SLM-Based Assistant for IoT Maintenance Tasks on the Edge** *IEEE Internet of Things Journal* [[paper](https://doi.org/10.1109/jiot.2025.3632638)]
- [2025] **Fluke: Federated learning utility framework for experimentation and research** *Future Generation Computer Systems* [[paper](https://doi.org/10.1016/j.future.2025.108241)]
- [2025] **High-Throughput Mass Spectral Library Searching of Small Molecules in R with NIST MSPepSearch** *Journal of the American Society for Mass Spectrometry* [[paper](https://doi.org/10.1021/jasms.5c00322)]
- [2025] **XGBoost regression for robust acoustic impedance prediction in the absence of density and sonic logs** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-24727-9)]
- [2025] **Unlocking Value From Historical Documents: Automated Raster Log Digitization Using Visual Language Models And Computer Vision** [[paper](https://doi.org/10.2118/229257-ms)]
- [2025] **Observer Framework v5.2 (OF-11D-G) — 11D Governance Layer for Continuity, Repair, and Safe Export** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17726329)]
- [2025] **A High-Dimensional Parameter Identification Method for Pipelines Based on Static Strain and DNN Surrogate Models to Accelerate Langevin Bayesian Inference** *Buildings* [[paper](https://doi.org/10.3390/buildings15234254)]
- [2025] **Enhancing smoothed particle hydrodynamics for turbulent flow simulation: implementation of the dynamic Smagorinsky model** *Engineering Applications of Computational Fluid Mechanics* [[paper](https://doi.org/10.1080/19942060.2025.2591376)]
- [2025] **Can Deep Learning Models Predict Compositional Outputs Without Log-Ratio Transformations?** [[paper](https://doi.org/10.1109/ictai66417.2025.00028)]
- [2025] **Stock Market Prediction Using Sequential Log-Power Normalization and Ridge Regression** [[paper](https://doi.org/10.1109/incowoco68239.2025.11407222)]
- [2025] **A New Pulsed Neutron-Gamma Density Logging Method Based on Gamma-Ray Spectra and Machine Learning** *ACS Omega* [[paper](https://doi.org/10.1021/acsomega.5c06755)]
- [2025] **Bitcoin Price Forecasting using Seasonal Log-Differenced XGBoost with 2014–2025 Data** *SISTEMASI* [[paper](https://doi.org/10.32520/stmsi.v14i6.5547)]
- [2025] **AI, Health, and Health Care Today and Tomorrow** *JAMA* [[paper](https://doi.org/10.1001/jama.2025.18490)]
- [2025] **Interactive Developer Tools Powered by AI Agents: Usability and Architectural Patterns** *European Modern Studies Journal* [[paper](https://doi.org/10.59573/emsj.9(5).2025.103)]
- [2025] **Multi-agent AI Framework for Developer Assistance: A New Paradigm in Software Engineering Automation** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-03769-5_18)]
- [2025] **Cracking CodeWhisperer: Analyzing Developers’ Interactions and Patterns During Programming Tasks** [[paper](https://doi.org/10.1109/vl-hcc65237.2025.00051)]
- [2025] **On Developers’ Self-Declaration of AI-Generated Code: An Analysis of Practices** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3771937)]
- [2025] **Facilitating Trust in AI-assisted Software Tools** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3772370)]
- [2025] **Modern Graphical User Interface Application With PYQT5 For The Classic Caesar Encryption Algorithm** *Kuantum teknolojileri ve enformatik araştırmaları dergisi.* [[paper](https://doi.org/10.70447/ktve.2927)]
- [2025] **DeNoFo: a file format and toolkit for standardized, comparable <i>de novo</i> gene annotation** *Bioinformatics* [[paper](https://doi.org/10.1093/bioinformatics/btaf539)]
- [2025] **NOS-TLPlot: A Specialized Python Tool for Visualizing Newcastle–Ottawa Scale Risk-of-Bias Assessments in Systematic Reviews and Meta-Analysis.** [[paper](https://doi.org/10.31222/osf.io/r9yh2_v1)]
- [2025] **VSLAM-LAB: A Comprehensive Framework for Visual SLAM Methods and Datasets** [[paper](https://doi.org/10.1109/iros60139.2025.11247218)]
- [2025] **wristpy: Fast, User-Friendly Python Processing of Wrist-worn Accelerometer Data** *The Journal of Open Source Software* [[paper](https://doi.org/10.21105/joss.08637)]
- [2025] **Evaluating 12 automated, whole-genome sequencing analysis pipelines for Mycobacterium tuberculosis complex: a comparative study** *The Lancet Microbe* [[paper](https://doi.org/10.1016/j.lanmic.2025.101210)]
- [2025] **TaxaGO: a novel, phylogenetically informed gene ontology enrichment analysis tool** *Briefings in Bioinformatics* [[paper](https://doi.org/10.1093/bib/bbaf572)]
- [2025] **ROBOTIC PROCESS AUTOMATION IN SAP ERP: ENHANCING FINANCIAL TRANSACTION RECONCILIATION AND COMPLIANCE MONITORING** *Archives for Technical Sciences* [[paper](https://doi.org/10.70102/afts.2025.1833.279)]
- [2025] **Global Risk Index for AI-enabled Biological Tools (Public Report)** [[paper](https://doi.org/10.71172/wjyw-6dyc)]
- [2025] **The Rise of Agentic AI: A Review of Definitions, Frameworks, Architectures, Applications, Evaluation Metrics, and Challenges** *Future Internet* [[paper](https://doi.org/10.3390/fi17090404)]
- [2025] **Towards Trustworthy Sentiment Analysis in Software Engineering: Dataset Characteristics and Tool Selection** [[paper](https://doi.org/10.1109/rew66121.2025.00080)]
- [2025] **Governing Artificial Intelligence in Radiology: A Systematic Review of Ethical, Legal, and Regulatory Frameworks** *Diagnostics* [[paper](https://doi.org/10.3390/diagnostics15182300)]
- [2025] **Digital land-use decision support tools in Europe: a systematic review using the PRISMA method** *European Planning Studies* [[paper](https://doi.org/10.1080/09654313.2025.2524002)]
- [2025] **Future Perspectives for Physics-Based Urban Building Energy Modelling Tools** *Energies* [[paper](https://doi.org/10.3390/en18184888)]
- [2025] **Drafting the Landscape of Computational Musicology Tools: a Survey-Based Approach** [[paper](https://arxiv.org/abs/2507.15590)]
- [2025] **NCBI Orthologs: Public Resource and Scalable Method for Computing High-Precision Orthologs Across Eukaryotic Genomes** *Journal of Molecular Evolution* [[paper](https://doi.org/10.1007/s00239-025-10268-2)]
- [2025] **Efficient Self-Attention Based Joint Optimization for Lithology and Petrophysical Parameter Estimation in the Athabasca Oil Sands** [[paper](https://doi.org/10.31223/x57x65)]
- [2025] **A Practical Guide to Machine Learning in Petrophysics: Navigating the Chaos** [[paper](https://doi.org/10.2118/227016-ms)]
- [2025] **NADI – Network Analysis and Data Integration with a Domain Specific Language** *The Journal of Open Source Software* [[paper](https://doi.org/10.21105/joss.08655)]
- [2025] **Ensemblify: a user-friendly tool for generating ensembles of intrinsically disordered regions of AlphaFold and user-defined models** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.1101/2025.08.26.672300)]
- [2025] **INTELLIGENT ANOMALY DETECTION IN MEDICAL IOT DEVICES USING AN ANN WITH ENSEMBLE LEARNING** *International Journal of Data Science and IoT Management System* [[paper](https://doi.org/10.64751/ijdim.2025.v4.n3.pp119-126)]
- [2025] **Handling of missing values in whole-population electronic health records: a simulation study** *International Journal for Population Data Science* [[paper](https://doi.org/10.23889/ijpds.v10i4.3265)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **From Command to Conversation: Integrating Agentic AI Into Command-Line Interfaces** *Computer* [[paper](https://doi.org/10.1109/mc.2026.3673219)]
- [2026] **Balsa: A Fast C++ Random Forest Classifier with Command-line and Python Interface** *The Journal of Open Source Software* [[paper](https://doi.org/10.21105/joss.08778)]
- [2026] **例外処理でcatchとログはどこに置くべきか (archived 2026-08-01)** *Open MIND* [[paper](https://comcomponent.com/blog/2026/04/15/000-exception-catching-logging-error-handling/)]
- [2026] **Teachers as AI Developers** *Cambridge University Press eBooks* [[paper](https://doi.org/10.1017/9781009781107)]
- [2026] **أين يجب التقاط الاستثناءات وتسجيلها ومعالجة الأخطاء - دليل عملي للحدود والمسؤوليات في تسلسل الاستدعاء (archived 2026-07-27)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21621500)]
- [2026] **Où catch et la journalisation doivent-ils se situer dans la gestion des exceptions ? (archived 2026-07-27)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21618515)]
- [2026] **어디서 예외를 `catch`하고 로그를 내며 에러 처리해야 하는가 - 호출 계층의 경계와 책무를 실무용으로 정리 (archived 2026-07-27)** *Open MIND* [[paper](https://comcomponent.com/ko/blog/2026/04/15/000-exception-catching-logging-error-handling/)]
- [2026] **Где размещать catch и логирование при обработке исключений (archived 2026-07-27)** *Open MIND* [[paper](https://comcomponent.com/ru/blog/2026/04/15/000-exception-catching-logging-error-handling/)]
- [2026] **例外処理でcatchとログはどこに置くべきか (archived 2026-07-26)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21589784)]
- [2026] **The Dialectic of the Interface: From Command Line to Ceremony (EA-SEI-DIALUX-01 v1.0)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20618250)]
- [2026] **R Code for Regional Analysis: Spatiotemporal Logging and Pulse Simulation of Integrated GTFS-Static and Realtime Data 地域分析のためのRコード: GTFS静的・リアルタイム公共交通データの統合的可視化(都営バス、知多市「あいあいバス」、広島電鉄バスを例に)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20277603)]
- [2026] **Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.6c00528)]
- [2026] **Exploring proteins and protein–ligand complexes through residue interaction networks** *Nature Protocols* [[paper](https://doi.org/10.1038/s41596-026-01334-0)]
- [2026] **GHOST GOVERNANCE, CONFIRMED Reddit Legal Support Response to the Archival Reclamation Protocol, March 18, 2026** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19099760)]
- [2026] **Transactional or transformative? Offshore wind developer perspectives on community benefit mechanisms in the United States** *Energy Research & Social Science* [[paper](https://doi.org/10.1016/j.erss.2026.104625)]
- [2026] **Using development environment as code for enhancing developer experience: An action design research study** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112803)]
- [2026] **Topological Error-Correction: The Decidability of Physical Law and the Global Try-Catch Mechanism** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18610853)]
- [2026] **Joint Syntactic & Semantic Graph Alignment via Unbalanced Optimal Transport. Differentiable Low-Rank Gromov–Wasserstein Surrogates, and Log-Sinkhorn Stability; ALIGN100- 1/7** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19047544)]
- [2026] **Ethical Knowledge, Challenges, and Institutional Strategies Among Medical AI Developers and Researchers: Focus Group Study** *Journal of Medical Internet Research* [[paper](https://doi.org/10.2196/79613)]
- [2026] **Citizen Developers at Work: Roles, Activities, and Interfaces in Low-Code/No-Code Development** *Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences* [[paper](https://doi.org/10.24251/hicss.2026.672)]
- [2026] **Human Computer Interaction from Interfaces to Intelligent Systems** *Applied and Computational Engineering* [[paper](https://doi.org/10.54254/2755-2721/2026.as31460)]
- [2026] **Data Imputation for Business Process Event Logs** *SN Computer Science* [[paper](https://doi.org/10.1007/s42979-026-04724-z)]
- [2026] **Interactive creation, visualization, and exploration of process model collections** *Software & Systems Modeling* [[paper](https://doi.org/10.1007/s10270-025-01346-6)]
- [2026] **Capability-Boundary-Aware Memory Routing for Cost-Efficient Log Anomaly Detection** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.7294111)]
- [2026] **Enhancing Population Variance Estimation through Log-Type Models in Neutrosophic Statistics: Accepted January 2026** *Portuguese National Funding Agency for Science, Research and Technology (RCAAP Project by FCT)* [[paper](https://revstat.ine.pt/index.php/REVSTAT/article/view/1100)]
- [2026] **Hybrid Radial Basis and Log-Sigmoid Neural Network Using Rprop for Dengue–COVID-19 Co-infection Dynamics** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6910764)]
- [2026] **Blockchain-Enabled Network Intrusion Detection System for Secure and Transparent Threat Logging** *International Journal of Advanced Research in Science Communication and Technology* [[paper](https://doi.org/10.48175/ijarsct-30816)]
- [2026] **Beyond Accuracy: Reliability of Imbalance-Handling Strategies for Fine-Grained Emotion Classification** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.7212702)]
- [2026] **Informer-Based High-Order Geometrical Factor for Modeling Array Induction Logging in Layered Formations** *IEEE Transactions on Geoscience and Remote Sensing* [[paper](https://doi.org/10.1109/tgrs.2026.3674745)]
- [2026] **Semantic Identity Compression: Exact Zero-Error Laws, Rate-Distortion, and Neurosymbolic Necessity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19010331)]
- [2026] **Sevenforest/Digital-Cosmology: Digital Cosmology: The "Debugging Destiny" Protocol and the Exception Handling Architecture of the Universe** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18135758)]

##### 2025

- [2025] **Interpretability taxonomy: an approach for artificial intelligence developers technique selection** *Discover Data* [[paper](https://doi.org/10.1007/s44248-025-00096-6)]
- [2025] **Artificial intelligence (AI) for social innovation in health education: promoting health literacy through personalized ai-driven learning tools – a systematic review** *BMC Medical Education* [[paper](https://doi.org/10.1186/s12909-025-08462-3)]
- [2025] **Diffusion of innovation in controlled environment agriculture: A mixed-methods study of digital decision support tool adoption** *Journal of Innovation & Knowledge* [[paper](https://doi.org/10.1016/j.jik.2025.100882)]
- [2025] **PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2511.20555)]
- [2025] **{{\texttt {openIRM}}}: publicly accessible internal risk model of an artificial life insurer for analyzing and benchmarking actuarial methods in the solvency II setting** *European Actuarial Journal* [[paper](https://doi.org/10.1007/s13385-025-00435-6)]
- [2025] **BLOCKCHAIN-BASED CHAIN-OF-CUSTODY MODELS FOR TAMPER-PROOF EVIDENCE PRESERVATION IN DIGITAL FORENSICS INVESTIGATIONS** *International Research Journal of Modernization in Engineering Technology and Science* [[paper](https://doi.org/10.56726/irjmets80086)]
- [2025] **Project scope management using developers’ tools and practices** *Journal of Project Management* [[paper](https://doi.org/10.26425/3034-6916-2025-1-3-21-28)]
- [2025] **Rethinking agency in AI ethics: beyond the developer-centric paradigm** *AI & Society* [[paper](https://doi.org/10.1007/s00146-025-02671-6)]
- [2025] **Time Series Prediction of Backend Server Load via Deep Learning and Attention Mechanisms** [[paper](https://doi.org/10.1109/icbaie66852.2025.11326577)]
- [2025] **Pre-service biology teachers as developers of mobile augmented reality teaching materials: Enhancing, not replacing, science practices and connections with the natural environment** *Thinking Skills and Creativity* [[paper](https://doi.org/10.1016/j.tsc.2025.102019)]
- [2025] **The generative illusion: how ChatGPT-like AI tools could reinforce misinformation and mistrust in public health communication** *Frontiers in Public Health* [[paper](https://doi.org/10.3389/fpubh.2025.1683498)]
- [2025] **AI-Powered Phishing Detection In Email Forensics: A Machine Learning Approach For Cyber Threat** [[paper](https://doi.org/10.1109/icfsp67350.2025.11353877)]
- [2025] **Psychological safety and trust as drivers of teachers’ continued use of AI tools in classrooms** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-13789-4)]
- [2025] **Exploring the Factors That Promote a Balance Between Academic Integrity and the Effective Use of <scp>GenAI</scp> Tools in Higher Education: A Systematic Review** *Journal of Computer Assisted Learning* [[paper](https://doi.org/10.1111/jcal.70109)]
- [2025] **Description of chromatographic performance in reversed-phase liquid chromatography based on a generalised model. Part I: Column characterisation** *Journal of Chromatography A* [[paper](https://doi.org/10.1016/j.chroma.2025.466324)]
- [2025] **Nonlinear analysis and hybrid numerical simulation of a coupled Zeldovich model with Arrhenius kinetics** *Case Studies in Thermal Engineering* [[paper](https://doi.org/10.1016/j.csite.2025.106947)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Implementasi Penetration Testing untuk Mendeteksi Kerentanan XSS berbasis CLI (Command Line Interface)** *Jurnal Teknologi dan Sains Modern* [[paper](https://doi.org/10.69930/jtsm.v3i4.857)]
- [2026] **NetCoreApplicationTemplate** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20373042)]
- [2026] **Error Handling and Logging** [[paper](https://doi.org/10.1201/9781003665359-14)]
- [2026] **Adding a simple log to in-text citations to strengthen information literacy and argumentation while blocking casual misuse of generative AI** *Journal of Information Literacy* [[paper](https://doi.org/10.11645/20.1.847)]
- [2026] **"The AI tool can’t make it any worse." Investigating Developers’ Security Behavior with AI Assistants in a Password Storage Study** [[paper](https://doi.org/10.1145/3772318.3791693)]
- [2026] **Why MB-500 Exam Questions From Apply Developer Tools Feel Tricky In The Exam** [[paper](https://doi.org/10.55277/researchhub.vvmt9gzr.1)]
- [2026] **Developer Needs and Feasible Features for AI Assistants in IDEs** [[paper](https://arxiv.org/abs/2410.08676)]
- [2026] **Google it or ask ChatGPT? Impact of software developers' information search practices on organisational information security** *Behaviour and Information Technology* [[paper](https://doi.org/10.1080/0144929x.2026.2654495)]
- [2026] **The FSE Artifact 2026 : AccessRefinery** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19534299)]
- [2026] **<tt>XSNAP</tt> : An X-Ray Supernova Analysis Pipeline with Application to the Type II Supernova 2024ggi** *The Astrophysical Journal* [[paper](https://arxiv.org/abs/2511.10744)]
- [2026] **Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3796519)]
- [2026] **ChemView: A Browser-Based Molecular Visualization Tool** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18685910)]
- [2026] **ST-Analyzer: A Packaged Web and Command-Line Interface for Simulation Trajectory Analysis** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.64898/2026.02.06.704471)]
- [2026] **HipSTR-UI: A cross-platform graphical interface for accessible str genotyping from next-generation sequencing data** *Forensic Science International Genetics* [[paper](https://doi.org/10.1016/j.fsigen.2026.103456)]
- [2026] **FMUiL: An open-source package for in-the-loop simulations with functional mock-up units** *SoftwareX* [[paper](https://doi.org/10.1016/j.softx.2026.102560)]
- [2026] **Empirical analysis of generative AI tool adoption in software development** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108036)]
- [2026] **AI Tools in Software Development: Developer Perceptions and Usage Patterns** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.21305)]
- [2026] **Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces** *CISPA Helmholtz Center* [[paper](https://doi.org/10.60882/cispa.32056182.v1)]
- [2026] **PymolFold: A PyMOL Plugin for API-Driven Structure Prediction and Quality Assessment** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c02410)]
- [2026] **AI-based analysis of Android log files : Automation in handling error reports during Android application development** *KTH Publication Database DiVA (KTH Royal Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:kau:diva-108402)]

##### 2025

- [2025] **Human outbreak detection and best practice MPXV analysis and interpretation with squirrel** *Virus Evolution* [[paper](https://doi.org/10.1093/ve/veaf095)]
- [2025] **An empirical study on the use behavior towards AI painting tools based on TAM3 model** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-24405-w)]
- [2025] **Cleaning Maintenance Logs with LLM Agents for Improved Predictive Maintenance** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2511.05311)]
- [2025] **DESIGN AND DEVELOPMENT OF AN 8 CHANNEL DATA ACQUISITION AND LOGGING SYSTEM FOR HIGH PRECISION LABORATORY RESEARCH APPLICATIONS** *Journal Of Recent Trends of Electrical Engineering* [[paper](https://doi.org/10.65525/jrtee.v1i2.10)]
- [2025] **Empowering Developer & Operations Self-Service: Oracle APEX + ORDS as an Enterprise Platform for Productivity and Agility** *International Journal of Scientific Research in Science Engineering and Technology* [[paper](https://doi.org/10.32628/ijsrset1844429)]
- [2025] **The Command Line GUIde: Graphical Interfaces from Man Pages via AI** [[paper](https://arxiv.org/abs/2510.01453)]
- [2025] **How Can Clinicians Leverage Vibe Coding for Machine Learning and Deep Learning Research?** *Endocrinology and Metabolism* [[paper](https://doi.org/10.3803/enm.2025.2675)]
- [2025] **Optimizing Website Performance: A Comprehensive Google Lighthouse Study on Desktop and Mobile Modes** [[paper](https://doi.org/10.36227/techrxiv.175699271.14100083/v1)]
- [2025] **Safety Training and Incident Management in Ground Handling: Insights from A Case Study in Romania** *International Journal of Social Science and Human Research* [[paper](https://doi.org/10.47191/ijsshr/v8-i9-82)]
- [2025] **Designing and implementing scalable microservices with spring boot on AWS** *World Journal of Advanced Research and Reviews* [[paper](https://doi.org/10.30574/wjarr.2025.27.2.3008)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **xgt: a command-line interface for the Genome Taxonomy Database with cross-release taxonomic comparison** *GigaScience* [[paper](https://doi.org/10.1093/gigascience/giag086)]
- [2026] **rankkit: ranking evaluation with error bars and position-bias correction** *Open MIND* [[paper](https://github.com/mohammadi-hadi/rankkit/tree/v0.1.0)]
- [2026] **Egress Governance, Entropy-Based Sensitivity Detection, MCP Connection Visibility, and Per-Tool Behavioral Baseline Monitoring for Network-Layer AI Developer Tool Privacy Protection** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21172532)]
- [2026] **PyeLink and SyeLink: Open-source Python tools for low-level EyeLink experiment control and data parsing** [[paper](https://doi.org/10.1145/3797246.3805844)]
- [2026] **Code with Me or for Me? How Increasing AI Automation Transforms Developer Workflows** [[paper](https://doi.org/10.1145/3772318.3790850)]
- [2026] **Cenote-Taker 3 for fast and accurate virus discovery and annotation of the virome** *Peer Community Journal* [[paper](https://doi.org/10.24072/pcjournal.706)]
- [2026] **OBSCURA- A Dark Web Command Line Search Tool** *Scholarly Commons (Embry–Riddle Aeronautical University)* [[paper](https://commons.erau.edu/pr-discovery-day/2026/presentations/7)]
- [2026] **The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers** *Management Science* [[paper](https://doi.org/10.1287/mnsc.2025.00535)]
- [2026] **LLM Powered Command Line Interface Agent: A Comparative Analysis** [[paper](https://doi.org/10.1109/iciscois62701.2026.11447826)]
- [2026] **MUMSPI: A Model for Usability Measurement of Single-Platform Interface for Multi-Tasking in Big Data Tools** *Jordanian Journal of Informatics and Computing* [[paper](https://doi.org/10.63180/jjic.thestap.2026.1.1)]

##### 2025

- [2025] **Error Handling in Usability Model for Zero Trust Security in Internet of Things Systems** *INTERNATIONAL JOURNAL OF MATHEMATICS AND COMPUTER RESEARCH* [[paper](https://doi.org/10.5281/zenodo.18043031)]
- [2025] **Error Handing in Usability Model for Zero Trust Security in Internet of Things Systems** *INTERNATIONAL JOURNAL OF MATHEMATICS AND COMPUTER RESEARCH* [[paper](https://doi.org/10.5281/zenodo.18043032)]
- [2025] **The Blue Carbon Cost Tool – understanding market potential and investment requirements for high-quality coastal wetland projects** *Frontiers in Marine Science* [[paper](https://doi.org/10.3389/fmars.2025.1622255)]
- [2025] **SiSaNA: A Python-based command line interface for Single-Sample Network Analysis** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.1101/2025.11.06.680212)]
- [2025] **Protocol for creating a gene dictionary for organelle genomes using the Gene Dictionary Tool** *STAR Protocols* [[paper](https://doi.org/10.1016/j.xpro.2025.104187)]
- [2025] **Benchmarking gate-based quantum computers via certification of qubit von Neumann measurements** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-7095567/v1)]
- [2025] **A Systematic Literature Review on Intelligent Tools and the Developer Experience** [[paper](https://doi.org/10.1109/conisoft66928.2025.00046)]
- [2025] **Assessing scoring metrics for <scp>AlphaFold2</scp> and <scp>AlphaFold3</scp> protein complex predictions** *Protein Science* [[paper](https://doi.org/10.1002/pro.70327)]
- [2025] **A Collaborative Tool for Quantum Circuit Programming** [[paper](https://doi.org/10.1109/qce65121.2025.10311)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Eras of bioinformatics technologies from command-line interfaces to artificial intelligence (AI) chatbots** *Briefings in Bioinformatics* [[paper](https://doi.org/10.1093/bib/bbag256)]
- [2026] **Architecting Next-Generation Shells: AI-Driven Command Assistance and Proactive Safety Mechanisms in the Command-Line** *International Journal of Computer Applications* [[paper](https://doi.org/10.5120/ijca4f98e99c1f94)]
- [2026] **iPsychonaut/EGAP: v3.3.9 Logging and Bug Squashing** *Open MIND* [[paper](https://github.com/iPsychonaut/EGAP/tree/v3.3.9)]

##### 2025

- [2025] **A tutorial on developing metric tools for sample preparation: from green towards sustainable** *Analytica Chimica Acta* [[paper](https://doi.org/10.1016/j.aca.2025.345044)]
- [2025] **proGenomes4: providing 2 million accurately and consistently annotated high-quality prokaryotic genomes** *Nucleic Acids Research* [[paper](https://doi.org/10.1093/nar/gkaf1208)]
- [2025] **Inclusive education with AI: supporting special needs and tackling language barriers** *AI and Ethics* [[paper](https://doi.org/10.1007/s43681-025-00824-3)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **crowe-logic: an agent command-line interface** *Open MIND* [[paper](https://pypi.org/project/crowe-logic/)]
- [2026] **HBAT 2: A Python Package to Analyse Hydrogen Bonds and Other Non-covalent Interactions in Macromolecular Structures** *ChemRxiv* [[paper](https://doi.org/10.26434/chemrxiv.15000141/v1)]
- [2026] **<scp>GeneMiner2</scp> : Accurate and Automated Recovery of Genes From Genome Skimming Data** *Molecular Ecology Resources* [[paper](https://doi.org/10.1111/1755-0998.70111)]
- [2026] **Implementasi Sistem Logging Terpusat dan Error Handling Robust Menggunakan Spatie dan Sentry pada Aplikasi Laravel Berbasis Enterprise** *Invention Journal Research and Education Studies* [[paper](https://doi.org/10.51178/invention.v7i1.3280)]
- [2026] **Tools for Implementing Multi-Agent Systems Based on Protocols** [[paper](https://doi.org/10.1007/978-3-032-01082-7_8)]
- [2026] **Evolution of system software interfaces: from the command line to graphics** *Online library Sukhoi State Technical University of Gome (Sukhoi State Technical University of Gomel)* [[paper](https://elib.gstu.by/handle/220612/49431)]
- [2026] **Failure Classification for Microservice Systems Based on Variational Graph Auto-Encoders** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-95-5012-8_14)]
- [2026] **A 3D Simulation Platform for Fuel Handling and Storage Systems** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-95-7195-6_13)]
- [2026] **Derangadic: A Combinatorial Number System for Derangements with Amortised O(log n) Stateful Lexicographic Generation** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6853178)]

##### 2025

- [2025] **GNU Astronomy Utilities 0.24** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17726900)]
- [2025] **BLVDIFF: Supporting BLV Developers with Differential Debugging Tools** [[paper](https://doi.org/10.1145/3663547.3759716)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Rtinycc: Builds the 'TinyCC' Command-Line Interface and Library for 'C' Scripting in 'R'** [[paper](https://doi.org/10.32614/cran.package.rtinycc)]
- [2026] **Inspecting and Visualizing Language Extensions in Storm : A Developer Tool for Inspecting DSL Parsing** *DiVA (Linkoping University)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:liu:diva-226488)]
- [2026] **PyGMT: A Python interface for the Generic Mapping Tools** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18080259)]
- [2026] **BrkRaw: A modular toolkit for Bruker MRI raw-data handling** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18381735)]

##### 2025

- [2025] **AWS Master Class Chapter 08: Developer Tools and DevOps - Part 2** [[paper](https://doi.org/10.22541/au.173679846.60274144/v2)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **Characterizing Visual Accessibility Issues in AI Developer Tools: An Empirical Study** [[paper](https://arxiv.org/abs/2608.05116)]
- [2026] **Can LLMs Test Terminal User Interfaces?** [[paper](https://arxiv.org/abs/2608.03743)] [[code](https://github.com/tui-testing/tuicov)]
- [2026] **When AI Joins the Team! A Model of How AI Adoption Relates To Social Patterns in Software Engineering Teams** [[paper](https://arxiv.org/abs/2608.03462)]
- [2026] **Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline** [[paper](https://arxiv.org/abs/2608.16187)]
- [2026] **AgentR A Stateful and Recovery-Aware Software Architecture for LLM-based Auditable Workflows** [[paper](https://arxiv.org/abs/2608.15264)]
- [2026] **AI Sandbox: Technical Report** [[paper](https://arxiv.org/abs/2608.02679)]
- [2026] **Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection** [[paper](https://arxiv.org/abs/2608.17965)]
- [2026] **Trajectories That Segment Themselves: Agent-Declared Boundaries as a Training Unit** [[paper](https://arxiv.org/abs/2608.02302)]
- [2026] **TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference** [[paper](https://arxiv.org/abs/2608.01975)]
- [2026] **AI Image Generation Tools for Developers** *OSF Preprints (OSF Preprints)* [[paper](https://osf.io/dws49)]
- [2026] **Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports** [[paper](https://arxiv.org/abs/2607.15684)]
- [2026] **Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments** [[paper](https://arxiv.org/abs/2607.28591)]
- [2026] **Integrating Energy Efficiency into Software Development: Developer Perspectives and Requirements** [[paper](https://arxiv.org/abs/2607.22168)]
- [2026] **An Empirical Study of Model Context Protocol Applications** [[paper](https://arxiv.org/abs/2607.25635)]
- [2026] **ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs** *ICML 2026* [[paper](https://arxiv.org/abs/2607.14285)]
- [2026] **Toward Production-Ready Federated Learning in Healthcare: Privacy, Orchestration, and Governance in MLOps** [[paper](https://arxiv.org/abs/2607.10467)]
- [2026] **ThinkLog: Leveraging Reasoning for Log Statement Generation** [[paper](https://arxiv.org/abs/2607.11615)]
- [2026] **Exploring Block Anomaly Detection In HDFS Log Data Analysis** [[paper](https://arxiv.org/abs/2607.29383)]
- [2026] **Bifrost: Empowering Pretrained Language Model with Fallibility Representation for Log-Based Fault Diagnosis** [[paper](https://arxiv.org/abs/2607.23169)]
- [2026] **Can Large Language Models Generate Observability-Aware Code?** [[paper](https://arxiv.org/abs/2607.05785)]
- [2026] **LogNLQ: Natural-Language Log Querying with Parser-Induced and Semantically Grounded Schemas** [[paper](https://arxiv.org/abs/2607.03884)]
- [2026] **GPUAlert: A Zero-Instrumentation Process-Boundary Monitor for Diagnosing GPU Training-Job Failures** [[paper](https://arxiv.org/abs/2607.01409)]
- [2026] **Characterizing and Bridging the Diagnostic Gap in eBPF Verifier Rejections** [[paper](https://arxiv.org/abs/2607.02748)] [[code](https://github.com/eunomia-bpf/bpfix)]
- [2026] **Human-in-the-Loop Design Automation: A Comparative Study of Graphical and Command-Line Interfaces in CAD and EDA Workflows** [[paper](https://doi.org/10.1109/icosaas68663.2026.11648724)]
- [2026] **Where Should catch and Logging Go in Exception Handling? (archived 2026-07-27)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21614616)]
- [2026] **Semantic Identity Compression: Zero-Error Laws, Rate-Distortion, and Neurosymbolic Necessity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18123531)]
- [2026] **Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?** [[paper](https://arxiv.org/abs/2606.19388)]
- [2026] **Matching Matters: A Fair Quality-Efficiency Benchmark for Command-Line Agents** [[paper](https://arxiv.org/abs/2606.21140)]
- [2026] **Undefined Behavior in C and C++: An Experiment With Desktop Use Cases** [[paper](https://arxiv.org/abs/2606.12064)]
- [2026] **LogCopilot: Automating Log Aggregation Analysis through Large Language Models** [[paper](https://arxiv.org/abs/2606.17094)]
- [2026] **Cleaning Logs for Downstream Tasks (Registered Report)** [[paper](https://arxiv.org/abs/2606.27000)]
- [2026] **Before the Pull Request: Mining Multi-Agent Coordination** [[paper](https://arxiv.org/abs/2606.19616)]
- [2026] **crowe-logic-cli: a multi-provider AI command-line interface** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20724243)]
- [2026] **Correctness-Aware Repository Filtering Under Maximum Effective Context Window Constraints** [[paper](https://arxiv.org/abs/2605.14362)]
- [2026] **Accountable Agents in Software Engineering: An Analysis of Terms of Service and a Research Roadmap** [[paper](https://arxiv.org/abs/2605.04532)]
- [2026] **CIDR: A Large-Scale Industrial Source Code Dataset for Software Engineering Research** [[paper](https://arxiv.org/abs/2605.12153)]
- [2026] **An Empirical Study on Logging Evolution On Stack Overflow: Trends, Topics, and Challenges** [[paper](https://arxiv.org/abs/2606.00118)]
- [2026] **Leveraging Language Models for Log Statement Generation in Multilingual Scenarios: How Far Are We?** [[paper](https://arxiv.org/abs/2605.25374)]
- [2026] **How to Compare the Security of Code Written by Humans to LLM-generated Code** [[paper](https://arxiv.org/abs/2606.00186)]
- [2026] **CelerLog: Fast Log Parsing via Dynamic Routing** [[paper](https://arxiv.org/abs/2605.26005)]
- [2026] **Execution Envelopes: A Shared Admission Contract for Backend AI Execution Requests** [[paper](https://arxiv.org/abs/2605.08267)]
- [2026] **Detect, Localize, and Explain: Interactive Hierarchical Log Anomaly Analytics with LLM Augmentation** [[paper](https://arxiv.org/abs/2605.09222)] [[code](https://github.com/LeiMa0324/KRONE_Demo_official)] [[project](https://leima0324.github.io/KRONE_Demo_official)]
- [2026] **Integrating Log-Based Security Analytics in Agile Workflows: A Real-World Experience Report** [[paper](https://arxiv.org/abs/2605.00352)]
- [2026] **Using Logs to support Programming Education** [[paper](https://arxiv.org/abs/2605.10920)]
- [2026] **LogRouter: Adaptive Two-Level LLM Routing for Log Question Answering in Big Data Systems** [[paper](https://arxiv.org/abs/2605.18015)]
- [2026] **AppAgent-Claw: CLI Is All You Need for GUI Automation** [[paper](https://arxiv.org/abs/2606.05171)]
- [2026] **Tokalator: A Context Engineering Toolkit for Artificial Intelligence Coding Assistants** [[paper](https://arxiv.org/abs/2604.08290)]
- [2026] **TorchGWAS : GPU-accelerated GWAS for thousands of quantitative phenotypes** [[paper](https://arxiv.org/abs/2604.21095)] [[code](https://github.com/ZhiGroup/TorchGWAS)]
- [2026] **Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios** [[paper](https://arxiv.org/abs/2604.06742)]
- [2026] **From Helpful to Trustworthy: LLM Agents for Pair Programming** [[paper](https://arxiv.org/abs/2604.10300)]
- [2026] **Rethinking Software Engineering for Agentic AI Systems** [[paper](https://arxiv.org/abs/2604.10599)]
- [2026] **Recommending Usability Improvements with Multimodal Large Language Models** [[paper](https://arxiv.org/abs/2604.25420)]
- [2026] **Security Concerns in Generative AI Coding Assistants: Insights from Online Discussions on GitHub Copilot** [[paper](https://arxiv.org/abs/2604.08352)]
- [2026] **Is Vibe Coding the Future? An Empirical Assessment of LLM Generated Codes for Construction Safety** [[paper](https://arxiv.org/abs/2604.12311)]
- [2026] **Do AI Coding Agents Log Like Humans? An Empirical Study** [[paper](https://arxiv.org/abs/2604.09409)]
- [2026] **Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs** [[paper](https://arxiv.org/abs/2604.20211)]
- [2026] **Automated Logging Is Language-Sensitive: A Multilingual Benchmark and Empirical Study of LLMs** [[paper](https://arxiv.org/abs/2604.17529)]
- [2026] **Do Privacy Policies Match with the Logs? An Empirical Study of Privacy Disclosure in Android Application Logs** [[paper](https://arxiv.org/abs/2604.18552)]
- [2026] **A Comparative Study of Semantic Log Representations for Software Log-based Anomaly Detection** [[paper](https://arxiv.org/abs/2604.08028)]
- [2026] **Log-based vs Graph-based Approaches to Fault Diagnosis** [[paper](https://arxiv.org/abs/2604.14019)]
- [2026] **A Privacy-Preserving Approach to Conformance Checking** [[paper](https://arxiv.org/abs/2605.00283)]
- [2026] **Secure Conformance Checking using Token-based Replay and Homomorphic Encryption** [[paper](https://arxiv.org/abs/2604.25190)]
- [2026] **LLM-Enhanced Log Anomaly Detection: A Comprehensive Benchmark of Large Language Models for Automated System Diagnostics** [[paper](https://arxiv.org/abs/2604.12218)]
- [2026] **Assessing REST API Test Generation Strategies with Log Coverage** [[paper](https://arxiv.org/abs/2604.07073)]
- [2026] **Automata Learning versus Process Mining: The Case for User Journeys** [[paper](https://arxiv.org/abs/2604.03686)]
- [2026] **DeepParse: Hybrid Log Parsing with LLM-Synthesized Regex Masks** [[paper](https://arxiv.org/abs/2604.20553)]
- [2026] **AstraAI: LLMs, Retrieval, and AST-Guided Assistance for HPC Codebases** [[paper](https://arxiv.org/abs/2603.27423)]
- [2026] **GazePrinter: Visualizing Expert Gaze to Guide Novices in a New Codebase** [[paper](https://arxiv.org/abs/2603.19855)]
- [2026] **The Impact of AI-Assisted Development on Software Security: A Study of Gemini and Developer Experience** [[paper](https://arxiv.org/abs/2603.15298)]
- [2026] **An Object Web Seminar: A Retrospective on a Technical Dialogue Still Reverberating** [[paper](https://arxiv.org/abs/2603.26203)]
- [2026] **Are AI-assisted Development Tools Immune to Prompt Injection?** [[paper](https://arxiv.org/abs/2603.21642)]
- [2026] **SpaceTime Programming: Live and Omniscient Exploration of Code and Execution** [[paper](https://arxiv.org/abs/2603.18735)]
- [2026] **Empirical Characterization of Logging Smells in Machine Learning Code** [[paper](https://arxiv.org/abs/2603.23769)]
- [2026] **ReLog: Execution-Aware Logging with Runtime Feedback for LLM-Oriented Debugging** [[paper](https://arxiv.org/abs/2603.29122)]
- [2026] **IOTEL: A Tool for Generating IoT-enriched Object-Centric Event Logs** [[paper](https://arxiv.org/abs/2603.07906)]
- [2026] **LogFold: Compressing Logs with Structured Tokens and Hybrid Encoding** [[paper](https://arxiv.org/abs/2603.20618)]
- [2026] **SCOPE: Tree-based Self-Correcting Online Log Parsing via Syntactic-Semantic Collaboration** [[paper](https://arxiv.org/abs/2603.27247)]
- [2026] **The Market Dynamics for Third-Party AI Tools Trying to Compete With Electronic Health Record Developers** *JAMA* [[paper](https://doi.org/10.1001/jama.2026.2394)]
- [2026] **A Unified, Cross-Platform Framework for Automatic GUI and Plugin Generation in Structural Bioinformatics and Beyond** [[paper](https://arxiv.org/abs/2602.16047)]
- [2026] **LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces** [[paper](https://arxiv.org/abs/2602.14337)]
- [2026] **Software Testing at the Network Layer: Automated HTTP API Quality Assessment and Security Analysis of Production Web Applications** [[paper](https://arxiv.org/abs/2602.08242)]
- [2026] **Do Developers Read Type Information? An Eye-Tracking Study on TypeScript** [[paper](https://arxiv.org/abs/2602.04824)]
- [2026] **ArkEval: Benchmarking and Evaluating Automated CodeRepair for ArkTS** [[paper](https://arxiv.org/abs/2602.08866)]
- [2026] **V-SHiNE: A Virtual Smart Home Framework for Explainability Evaluation** [[paper](https://arxiv.org/abs/2602.11775)]
- [2026] **AgentTrace: A Structured Logging Framework for Agent System Observability** [[paper](https://arxiv.org/abs/2602.10133)]
- [2026] **Is Your Private Information Logged? An Empirical Study on Android App Logs** [[paper](https://arxiv.org/abs/2602.07893)]
- [2026] **A Case Study on Runtime Verification of a Continuous Deployment Process** [[paper](https://arxiv.org/abs/2602.20598)]
- [2026] **KRONE: Scalable LLM-Augmented Log Anomaly Detection via Hierarchical Abstraction** [[paper](https://arxiv.org/abs/2602.07303)] [[code](https://github.com/LeiMa0324/KRONE)] [[project](https://leima0324.github.io/KRONE_Demo_official/)]
- [2026] **On Sequence-to-Sequence Models for Automated Log Parsing** [[paper](https://arxiv.org/abs/2602.07698)]
- [2026] **Agentic Scientific Simulation: Execution-Grounded Model Construction and Reconstruction** [[paper](https://arxiv.org/abs/2603.00214)]
- [2026] **Achieving Productivity Gains with AI-based IDE features: A Journey at Google** [[paper](https://arxiv.org/abs/2601.19964)]
- [2026] **Enterprise Identity Integration for AI-Assisted Developer Services: Architecture, Implementation, and Case Study** [[paper](https://arxiv.org/abs/2601.02698)]
- [2026] **RITA: A Tool for Automated Requirements Classification and Specification from Online User Feedback** [[paper](https://arxiv.org/abs/2601.11362)]
- [2026] **Guidelines to Prompt Large Language Models for Code Generation: An Empirical Characterization** [[paper](https://arxiv.org/abs/2601.13118)]
- [2026] **Agentic Much? Adoption of Coding Agents on GitHub** [[paper](https://arxiv.org/abs/2601.18341)]
- [2026] **From LLMs to Agents in Programming: The Impact of Providing an LLM with a Compiler** [[paper](https://arxiv.org/abs/2601.12146)]
- [2026] **A Large Scale Empirical Analysis on the Adherence Gap between Standards and Tools in SBOM** [[paper](https://arxiv.org/abs/2601.05622)] [[code](https://github.com/dw763j/SAP)]
- [2026] **VarParser: Unleashing the Neglected Power of Variables for LLM-based Log Parsing** *WWW 2026* [[paper](https://arxiv.org/abs/2601.22676)]
- [2026] **DeLog: An Efficient Log Compression Framework with Pattern Signature Synthesis** [[paper](https://arxiv.org/abs/2601.15084)]
- [2026] **Small is Beautiful: A Practical and Efficient Log Parsing Framework** [[paper](https://arxiv.org/abs/2601.22590)]
- [2026] **Advanced Vulnerability Scanning for Open Source Software: Detection and Mitigation of Log4j Vulnerabilities** [[paper](https://arxiv.org/abs/2601.00235)]
- [2026] **MicLog: Towards Accurate and Efficient LLM-based Log Parsing via Progressive Meta In-Context Learning** [[paper](https://arxiv.org/abs/2601.07005)]
- [2026] **Exploring a Developer Tool for Code Comprehension through the Integration of Visual Aids and Large Language Models** *Seoul National University Open Repository (Seoul National University)* [[paper](https://hdl.handle.net/10371/233675)]
- [2026] **SMILE Prototyp zur Lagerverwaltung - Command Line Interface (CLI)** *Schule für Mathematik, Informatik, Logistik und Erfolg* [[paper](https://doi.org/10.1007/978-3-662-71857-5)]

##### 2025

- [2025] **Beyond the Prompt: An Empirical Study of Cursor Rules** [[paper](https://arxiv.org/abs/2512.18925)]
- [2025] **The Evolutionary Ecology of Software: Constraints, Innovation, and the AI Disruption** [[paper](https://arxiv.org/abs/2512.02953)]
- [2025] **Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking** [[paper](https://arxiv.org/abs/2512.21236)]
- [2025] **WhatsCode: Large-Scale GenAI Deployment for Developer Efficiency at WhatsApp** [[paper](https://arxiv.org/abs/2512.05314)]
- [2025] **FedLAD: A Modular and Adaptive Testbed for Federated Log Anomaly Detection** [[paper](https://arxiv.org/abs/2512.08277)] [[code](https://github.com/AA-cityu/FedLAD)]
- [2025] **QMon: Monitoring the Execution of Quantum Circuits with Mid-Circuit Measurement and Reset** [[paper](https://arxiv.org/abs/2512.13422)]
- [2025] **LLM-SrcLog: Towards Proactive and Unified Log Template Extraction via Large Language Models** [[paper](https://arxiv.org/abs/2512.04474)]
- [2025] **MINES: Explainable Anomaly Detection through Web API Invariant Inference** [[paper](https://arxiv.org/abs/2512.06906)]
- [2025] **XTrace: A Non-Invasive Dynamic Tracing Framework for Android Applications in Production** [[paper](https://arxiv.org/abs/2512.21555)]
- [2025] **A Story About Cohesion and Separation: Label-Free Metric for Log Parser Evaluation** [[paper](https://arxiv.org/abs/2512.21811)]
- [2025] **LogICL: Distilling LLM Reasoning to Bridge the Semantic Gap in Cross-Domain Log Anomaly Detection** [[paper](https://arxiv.org/abs/2512.09627)]
- [2025] **Borda/pyDeprecate: Adding developer tools** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17898559)]
- [2025] **Handling 403 errors in BuddyPress's new_activity_comment** [[paper](https://doi.org/10.59350/8t43b-pge97)]
- [2025] **The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents** [[paper](https://arxiv.org/abs/2511.03690)]
- [2025] **Agint: Agentic Graph Compilation for Software Engineering Agents** [[paper](https://arxiv.org/abs/2511.19635)]
- [2025] **Uncovering Code Insights: Leveraging GitHub Artifacts for Deeper Code Understanding** [[paper](https://arxiv.org/abs/2511.03549)]
- [2025] **AutoLogger: A Multi-Agent Framework for the End-to-End Automated Logging** [[paper](https://arxiv.org/abs/2511.18528)]
- [2025] **Scalable and Efficient Large-Scale Log Analysis with LLMs: An IT Software Support Case Study** [[paper](https://arxiv.org/abs/2511.14803)]
- [2025] **stable-pretraining-v1: Foundation Model Research Made Simple** [[paper](https://arxiv.org/abs/2511.19484)]
- [2025] **Generality Is Not Enough: Zero-Label Cross-System Log-Based Anomaly Detection via Knowledge-Level Collaboration** [[paper](https://arxiv.org/abs/2511.05882)]
- [2025] **FusionLog: Cross-System Log-based Anomaly Detection via Fusion of General and Proprietary Knowledge** [[paper](https://arxiv.org/abs/2511.05878)]
- [2025] **LogPurge: Log Data Purification for Anomaly Detection via Rule-Enhanced Filtering** [[paper](https://arxiv.org/abs/2511.14062)]
- [2025] **ZeroLog: Zero-Label Generalizable Cross-System Log-based Anomaly Detection** [[paper](https://arxiv.org/abs/2511.05862)]
- [2025] **REFLEX: Reference-Free Evaluation of Log Summarization via Large Language Model Judgment** [[paper](https://arxiv.org/abs/2511.07458)]
- [2025] **Architecting software monitors for control-flow anomaly detection through large language models and conformance checking** [[paper](https://arxiv.org/abs/2511.10876)]
- [2025] **AWS Master Class Chapter 07: Developer Tools and DevOps - Part 1** [[paper](https://doi.org/10.22541/au.173679845.56069145/v3)]
- [2025] **A decision-support tool for project developers** *TU/e Research Portal* [[paper](https://research.tue.nl/en/studentTheses/2d7fdb64-0365-49bc-8494-ffb6d3ee130e)]
- [2025] **OLIVAW: ACIMOV's GitHub robot assisting agile collaborative ontology development** [[paper](https://arxiv.org/abs/2510.17184)]
- [2025] **Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents** [[paper](https://arxiv.org/abs/2510.20211)]
- [2025] **Why Does the Engineering Manager Still Exist in Agile Software Development?** [[paper](https://arxiv.org/abs/2510.03920)]
- [2025] **Collaborative penetration testing suite for emerging generative AI algorithms** [[paper](https://arxiv.org/abs/2510.19303)]
- [2025] **AdProv: A Method for Provenance of Process Adaptations** [[paper](https://arxiv.org/abs/2510.05936)]
- [2025] **Optimized Log Parsing with Syntactic Modifications** [[paper](https://arxiv.org/abs/2510.26793)]
- [2025] **Accurate and Noise-Tolerant Extraction of Routine Logs in Robotic Process Automation (Extended Version)** [[paper](https://arxiv.org/abs/2510.08118)]
- [2025] **CodeAD: Synthesize Code of Rules for Log-based Anomaly Detection with LLMs** [[paper](https://arxiv.org/abs/2510.22986)]
- [2025] **A Process Mining-Based System For The Analysis and Prediction of Software Development Workflows** [[paper](https://arxiv.org/abs/2510.25935)]
- [2025] **SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?** [[paper](https://arxiv.org/abs/2509.16941)]
- [2025] **Towards Human-interpretable Explanation in Code Clone Detection using LLM-based Post Hoc Explainer** [[paper](https://arxiv.org/abs/2509.22978)]
- [2025] **Prompt Stability in Code LLMs: Measuring Sensitivity across Emotion- and Personality-Driven Variations** [[paper](https://arxiv.org/abs/2509.13680)]
- [2025] **A Survey on the Techniques and Tools for Automated Requirements Elicitation and Analysis of Mobile Apps** [[paper](https://arxiv.org/abs/2509.01068)]
- [2025] **Aspect-Oriented Programming in Secure Software Development: A Case Study of Security Aspects in Web Applications** [[paper](https://arxiv.org/abs/2509.07449)]
- [2025] **R-Log: Incentivizing Log Analysis Capability in LLMs via Reasoning-based Reinforcement Learning** [[paper](https://arxiv.org/abs/2509.25987)]
- [2025] **IoT Miner: Intelligent Extraction of Event Logs from Sensor Data for Process Mining** [[paper](https://arxiv.org/abs/2509.05769)]
- [2025] **LogPilot: Intent-aware and Scalable Alert Diagnosis for Large-scale Online Service Systems** [[paper](https://arxiv.org/abs/2509.25874)]
- [2025] **LogReasoner: Empowering LLMs with Expert-like Coarse-to-Fine Reasoning for Automated Log Analysis** [[paper](https://arxiv.org/abs/2509.20798)]
- [2025] **LogAction: Consistent Cross-system Anomaly Detection through Logs via Active Domain Adaptation** [[paper](https://arxiv.org/abs/2510.03288)]
- [2025] **What's Coming Next? Short-Term Simulation of Business Processes from Current State** [[paper](https://arxiv.org/abs/2509.07747)]
- [2025] **ConfLogger: Enhance Systems' Configuration Diagnosability through Configuration Logging** [[paper](https://arxiv.org/abs/2508.20977)]
- [2025] **Logging Requirement for Continuous Auditing of Responsible Machine Learning-based Applications** [[paper](https://arxiv.org/abs/2508.17851)]
- [2025] **Developer Insights into Designing AI-Based Computer Perception Tools** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2508.21733)]
- [2025] **Applying AI/ML to Kubernetes Logging and Monitoring in Enhancing Observability Through Intelligent Systems** *European Journal of Computer Science and Information Technology* [[paper](https://doi.org/10.37745/ejcsit.2013/vol13n49141152)]
- [2025] **Implementing Autonomous Monitoring in Oracle Cloud: A Deep Dive into OCI Observability and Logging Analytics** *European Journal of Computer Science and Information Technology* [[paper](https://doi.org/10.37745/ejcsit.2013/vol13n463444)]

##### 2024

- [2024] **Observability and Monitoring for Front-End: A Holistic Approach to Logging, Tracing, and Metrics with the Advent of AI** *INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* [[paper](https://doi.org/10.55041/ijsrem37217)]
- [2024] **A General Framework for Modernizing Logging and Monitoring** *A General Framework for Modernizing Logging and Monitoring* [[paper](https://doi.org/10.2172/2407257)]
- [2024] **Observability Challenges in Distributed Enterprise Transaction Systems: Beyond Traditional Logging** [[paper](https://doi.org/10.2139/ssrn.6489978)]
- [2024] **Observability in Microservices Architectures: Leveraging Logging, Metrics, and Distributed Tracing in Large-Scale Systems** [[paper](https://doi.org/10.2139/ssrn.5076624)]
- [2024] **Cloud-native Observability: The Many-faceted Benefits of Structured and Unified Logging - A Case Study** [[paper](https://doi.org/10.20944/preprints202208.0427.v1)]
- [2024] **CLOUD OBSERVABILITY IN FINANCE: MONITORING STRATEGIES FOR ENHANCED SECURITY** *CLOUD OBSERVABILITY IN FINANCE: MONITORING STRATEGIES FOR ENHANCED SECURITY* [[paper](https://doi.org/10.53555/nveo.v10i1.5761)]

##### 2023

- [2023] **Logging** *Practical OpenTelemetry* [[paper](https://doi.org/10.1007/978-1-4842-9075-0_8)]

[⬆ Back to top](#paper-list)

### DevOps & CI/CD

#### Method

##### 2026

- [2026] **Watchflow: Agentic DevOps Governance** *BIROn (Birkbeck, University of London)* [[paper](https://eprints.bbk.ac.uk/id/eprint/57759/1/Kargatzis%20D%2C%20final%20thesis%20for%20library.pdf)]
- [2026] **Cloud-Agnostic Infrastructure as Code: A Framework for Multi-Cloud Provisioning** *Open Repository of the University of Porto (University of Porto)* [[paper](https://hdl.handle.net/10216/175476)]
- [2026] **Deployability-Centric Infrastructure-as-Code Generation: Fail, Learn, Refine, and Succeed through LLM-Empowered DevOps Simulation** *Proceedings of the ACM on software engineering.* [[paper](https://arxiv.org/abs/2506.05623)]
- [2026] **PeopleCert PeopleCert DevOps-Foundation PDF** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20575516)]
- [2026] **PeopleCert PeopleCert DevOps-Leader PDF** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20920990)]
- [2026] **Implementing Infrastructure as Code Using Ansible on Debian Server Administration** *Journal of Artificial Intelligence and Engineering Applications (JAIEA)* [[paper](https://doi.org/10.59934/jaiea.v5i3.2576)]
- [2026] **Wearable Biosensors for Continuous Monitoring of Chronic Kidney Disease: Materials, Biofluids, and Digital Health Integration** *Biosensors* [[paper](https://doi.org/10.3390/bios16050287)]
- [2026] **Data Integrity Failures in Pharmaceutical Digital Twins and Continuous Manufacturing: An Alcoa + + Framework Integrating Human Factors and Simulation Vulnerabilities** *Journal of Pharmaceutical Innovation* [[paper](https://doi.org/10.1007/s12247-026-10778-6)]
- [2026] **An Analysis Of DevOps Practices In Cloud Environments** *International Journal of Scientific Research and Engineering Trends* [[paper](https://doi.org/10.5281/zenodo.20284247)]
- [2026] **Paper13_ARI-Based Post-Cloud Preservation and Reference Infrastructure** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20371894)]
- [2026] **Paper 1 - BIFACE-Based Sentence Coordinate Documents: Human-Readable Surfaces and AI+AGI-Referable Coordinates Across Documents, Code, Media, and Conversations** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20322707)]
- [2026] **Devops Automation Pipeline Deployment using Infrastructure as Code (Iac)** *International Journal of Creative and Open Research in Engineering and Management* [[paper](https://doi.org/10.55041/ijcope.v2i5.125)]
- [2026] **Advancing Infrastructure-as-Code Resilience through Generative AI Agents for Predictive Remediation and Autonomous Security Enforcement** *International Journal of Engineering and Advanced Technology* [[paper](https://doi.org/10.35940/ijeat.d4756.15040326)]
- [2026] **Metamorphic Testing for Infrastructure-as-Code Engines** *Proceedings of the ACM on Programming Languages* [[paper](https://doi.org/10.1145/3798226)]
- [2026] **Infrastructure as code for managing enterprise databricks lakehouse platforms** *Aaltodoc (Aalto University)* [[paper](https://aaltodoc.aalto.fi/handle/123456789/144531)]
- [2026] **ReTOSCA: Reverse Engineering Infrastructure-as-Code into TOSCA 2.0 Models** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19920687)]
- [2026] **Integrating Lean-Informed Continuous Improvement with Participatory Groundwater Governance: A PDCA Maturity Framework** *Water* [[paper](https://doi.org/10.3390/w18060666)]
- [2026] **A Comparative Analysis of Continuous Integration/Continuous Deployment Optimization Techniques** [[paper](https://doi.org/10.1201/9781003674818-19)]
- [2026] **Integrating Continuous Compliance into DevSecOps Pipelines: A Data Engineering Perspective** *Software* [[paper](https://doi.org/10.3390/software5010006)]
- [2026] **The comparison of circuit lifespan between integration and separation approach in extracorporeal membrane oxygenation patients requiring continuous renal replacement therapy support: a randomized controlled trial (E-CRRT Trial)** *Intensive Care Medicine* [[paper](https://doi.org/10.1007/s00134-026-08302-y)]
- [2026] **A framework integrating data-driven and computational fluid dynamics simulation for continuous blast furnace monitoring** *Engineering Applications of Artificial Intelligence* [[paper](https://doi.org/10.1016/j.engappai.2026.114092)]
- [2026] **Green‐lighting biofuels from microalgal lipids: A review of strategies to integrate stress into continuous cultures** *Biofuels Bioproducts and Biorefining* [[paper](https://doi.org/10.1002/bbb.70128)]
- [2026] **A coupled train-track-subgrade dynamic framework integrating the continuous surface cap model for ballastless track damage analysis** *Transportation Geotechnics* [[paper](https://doi.org/10.1016/j.trgeo.2026.101947)]
- [2026] **Design of an Intelligent Inspection System for Power Equipment Based on Multi-Technology Integration** *Electronics* [[paper](https://doi.org/10.3390/electronics15040827)]
- [2026] **Analysis of GitHub Advanced Security: Security Integration in GitHub and Azure DevOps** *Future Internet* [[paper](https://doi.org/10.3390/fi18020099)]
- [2026] **Zero-Trust DevOps for Electronic Health Records: Continuous Verification in Multi-Cloud Environments** *International Journal of Science and Engineering Applications* [[paper](https://doi.org/10.7753/ijsea1209.1049)]
- [2026] **From Agile DevOps to AIOps: Transforming Infrastructure Operations Through AI-Driven Automation** *International Journal of Research Publications in Engineering Technology and Management* [[paper](https://doi.org/10.15662/ijrpetm.2026.0901013)]
- [2026] **DevOps and CI/CD with Kubernetes** *Open MIND* [[paper](https://doi.org/10.26219/heal.aueb.9775)]
- [2026] **Artificial Intelligence for Infrastructure-as-Code—A Systematic Literature Review** *Electronics* [[paper](https://doi.org/10.3390/electronics15040755)]
- [2026] **Generative AI as an infrastructure copilot: automating Infrastructure-As-Code across the DevSecOps lifecycle** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-026-00600-5)]
- [2026] **AI-Assisted Detection of Malicious Changes in Infrastructure-as-Code for Secure DevOps** [[paper](https://doi.org/10.1109/icaic67076.2026.11395715)]
- [2026] **Continuous Integration for Distributed Applications** [[paper](https://doi.org/10.1109/icoecit68303.2026.11497251)]
- [2026] **Data-Driven Optimization of Continuous Stirred Tank Reactor Operation: Integration of Statistical Analysis, Stability Classification, and Machine Learning for Reversible Reaction Systems** *ChemRxiv* [[paper](https://doi.org/10.26434/chemrxiv.10001651/v1)]
- [2026] **Multi-modal AI in precision medicine: integrating genomics, imaging, and EHR data for clinical insights** *Frontiers in Artificial Intelligence* [[paper](https://doi.org/10.3389/frai.2025.1743921)]
- [2026] **A Concept of On-Demand Continuous Integration and Continuous Delivery Framework** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-13544-5_6)]
- [2026] **Evaluating DevOps Tools for Software Quality Engineering Using the VIKOR Method: A Multi-Criteria Decision-Making Approach** *Journal of Software Quality Engineering and DevOps* [[paper](https://doi.org/10.55124/jsqd.v1i1.101)]
- [2026] **Enhancing DevOps Continuous Monitoring Phase: Hybrid Intrusion Detection and Ensemble Learning System (HIDELS)** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3650793)]
- [2026] **Traceability in DevOps : Expectations, Challenges and Opportunities** *KTH Publication Database DiVA (KTH Royal Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:bth-29213)]
- [2026] **Autonomous Cloud Remediation And Self-Healing Infrastructure Through Infrastructure As Code And Artificial Intelligence Automation** *Journal of International Crisis and Risk Communication Research* [[paper](https://doi.org/10.63278/jicrcr.vi.3564)]
- [2026] **Infrastructure as Code and Custom Authentication** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-1321-4_15)]
- [2026] **The Testing Gaps in Infrastructure as Code Programs** *Open MIND* [[paper](https://doi.org/10.18420/se2026_60)]
- [2026] **Static analysis techniques and tools for infrastructure as code on the Kubernetes platform** *Athens University of Economics & Business* [[paper](https://doi.org/10.26219/heal.aueb.9698)]
- [2026] **AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3673923)]
- [2026] **Benefits of Using Infrastructure as Code to Manage On-Premises Data Centre** *Theseus (Ammattikorkeakoulujen)* [[paper](https://www.theseus.fi/handle/10024/924240)]
- [2026] **RootAsRole: Automated Least Privilege Discovery and Enforcement in Infrastructure-as-Code** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.31129630)]
- [2026] **Kognitiivisen kuorman vähentäminen DevOps-tiimeissä : infrastructure as code käyttöönottosuunnitelman laatiminen** *LUTPub (LUT University)* [[paper](https://lutpub.lut.fi/handle/10024/171541)]
- [2026] **Synergizing Infrastructure as Code and Container Orchestration: A Survey on Terraform and Kubernetes Automation** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18253655)]

##### 2025

- [2025] **Sustainable Devops: A Systematic Literature Review on Reducing Energy Footprint in Continuous Integration and Deployment (Ci/Cd) Pipelines** *International Journal of Computations Information and Manufacturing (IJCIM)* [[paper](https://doi.org/10.54489/ijcim.v5i2.565)]
- [2025] **Overcoming Challenges in Electrochemical Sensing: Toward Continuous Monitoring** *ACS Sensors* [[paper](https://doi.org/10.1021/acssensors.5c02717)]
- [2025] **Hype vs Reality in the Integration of Artificial Intelligence in Clinical Workflows** *JMIR Formative Research* [[paper](https://doi.org/10.2196/70921)]
- [2025] **Integrating additively manufactured continuous glass fibre inserts in compression moulding: A novel approach to mitigating fibre–matrix separation effect** *Composites Part A Applied Science and Manufacturing* [[paper](https://doi.org/10.1016/j.compositesa.2025.109497)]
- [2025] **Integrating Continuous Renal Replacement Therapy into <em>Ex-situ</em> Normothermic Liver Machine Perfusion** *Journal of Visualized Experiments* [[paper](https://doi.org/10.3791/69214)]
- [2025] **Implementation of Continuous Integration and Continuous Deployment for Automated System Deployment** *bit-Tech* [[paper](https://doi.org/10.32877/bt.v8i2.3295)]
- [2025] **Protection of DevOps Pipelines: Automation of Security within DevSecOps** *Automatic Control and Computer Sciences* [[paper](https://doi.org/10.3103/s0146411625701123)]
- [2025] **Production Development with Microservices Architecture and DevOps Practices** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202512.0134.v1)]
- [2025] **AI- AND ML-DRIVEN PREDICTIVE QUALITY ORCHESTRATION FOR U.S. HEALTHCARE AND HRM SYSTEMS: ENHANCING TEST INTELLIGENCE, DEFECT FORECASTING, AND COMPLIANCE OPTIMIZATION IN AGILE DEVOPS ENVIRONMENTS** *International Journal of Apllied Mathematics* [[paper](https://doi.org/10.12732/ijam.v38i12s.1485)]
- [2025] **The Impact of DevOps in IT Service Management** *Journal of Global Information Management* [[paper](https://doi.org/10.4018/jgim.392902)]
- [2025] **Large Language Models for Infrastructure as Code Vulnerability Remediation** *Journal of the Association for Information Systems* [[paper](https://aisel.aisnet.org/wisp2025/1)]
- [2025] **Infrastructure-as-code approach for on-premises automated Kubernetes deployment** *Athens University of Economics & Business* [[paper](https://doi.org/10.26219/heal.aueb.9697)]
- [2025] **A search-based file recommendation approach for infrastructure-as-code evolution** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112746)]
- [2025] **Infrastructure as Code (IaC) Maturity Model: A Framework for Secure and Scalable Automation** *Journal of Information Systems Engineering & Management* [[paper](https://doi.org/10.52783/jisem.v10i63s.13803)]
- [2025] **Infrastructure as Code and Observability Automation for Payment Systems in Cloud-Native Environments** *Frontiers in Artificial Intelligence Research* [[paper](https://doi.org/10.71465/fair526)]
- [2025] **Homogeneous catalysis in continuous flow integrating photocatalysis, electrocatalysis, and automation technologies** *Communications Chemistry* [[paper](https://doi.org/10.1038/s42004-025-01725-6)]
- [2025] **Micro‐Transfer Printed Continuous‐Wave and Mode‐Locked Laser Integration at 800 nm on a Silicon Nitride Platform** *Laser & Photonics Review* [[paper](https://doi.org/10.1002/lpor.202500956)]
- [2025] **Integrating Continuous Dual Glucose-Ketone Monitoring into Clinical Practice** *Diabetes Technology & Therapeutics* [[paper](https://doi.org/10.1177/15209156251392900)]
- [2025] **Multivendor Continuous Glucose Monitor Integration into the Electronic Health Record: Real-World Experience of an Academic Pediatric Endocrinology Clinic** *Diabetes Technology & Therapeutics* [[paper](https://doi.org/10.1177/15209156251395034)]
- [2025] **Integrating Sentiment Analysis into Agile Feedback Loops for Continuous Improvement** *Applied Sciences* [[paper](https://doi.org/10.3390/app152212329)]
- [2025] **Nutrigenomics meets multi-omics: integrating genetic, metabolic, and microbiome data for personalized nutrition strategies** *Genes & Nutrition* [[paper](https://doi.org/10.1186/s12263-025-00790-9)]
- [2025] **Dataset for "SpatialCOC: an integrative framework for spatial continuous mapping and cross-omics correction in spatial multi-omics data"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17655345)]
- [2025] **Advances in Point-of-Care Infectious Disease Diagnostics: Integration of Technologies, Validation, Artificial Intelligence, and Regulatory Oversight** *Diagnostics* [[paper](https://doi.org/10.3390/diagnostics15222845)]
- [2025] **Introduction to Continuous Integration – Streamlining Development with GitHub Actions** *INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* [[paper](https://doi.org/10.55041/ijsrem53760)]
- [2025] **Trends in Industry Support for Pricing-Driven DevOps in SaaS** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2025.3634801)]
- [2025] **Building an intelligent food assurance system based on DevOps: A review** *Future Foods* [[paper](https://doi.org/10.1016/j.fufo.2025.100847)]
- [2025] **A Scalable DevOps Framework Using Kubernetes-Orchestrated Microservices for Cloud-Native Infrastructure** [[paper](https://doi.org/10.1109/csitss67709.2025.11294211)]
- [2025] **Comparative Evaluation of Cloud-Native and VM-Based CI/CD Pipelines for Automated DevOps Deployments** *Asian Journal of Research in Computer Science* [[paper](https://doi.org/10.9734/ajrcos/2025/v18i11785)]
- [2025] **A Mobile DevOps Project Management Framework** *Tuwhera (Auckland University of Technology)* [[paper](https://hdl.handle.net/10292/20241)]
- [2025] **Securing Cloud-Native Applications via Infrastructure as Code and DevOps** [[paper](https://doi.org/10.1109/cloudcom67567.2025.11331450)]
- [2025] **Generative AI For Infrastructure As Code: Neural Approaches To Declarative Cloud Automation** *International Journal of Scientific Research and Engineering Trends* [[paper](https://doi.org/10.5281/zenodo.20351381)]
- [2025] **A concurrent optimization framework for composite structures: Integrating topology and continuous fiber path design under manufacturing and strength constraints** *Composite Structures* [[paper](https://doi.org/10.1016/j.compstruct.2025.119789)]
- [2025] **Population coding and self-organized ring attractors in recurrent neural networks for continuous variable integration** *Frontiers in Network Physiology* [[paper](https://doi.org/10.3389/fnetp.2025.1693772)]
- [2025] **Practicing Continuous Integration Continuous Delivery on AWS** *International Journal of Latest Technology in Engineering Management & Applied Science* [[paper](https://doi.org/10.51583/ijltemas.2025.1413sp006)]
- [2025] **When discrete characters are wanting: continuous character integration under the phylospecies concept informs the revision of the Australian land snail <i>Thersites</i> (Eupulmonata, Camaenidae)** *Zoological Journal of the Linnean Society* [[paper](https://doi.org/10.1093/zoolinnean/zlaf175)]
- [2025] **Advanced Fracture Diagnostics in Utah FORGE Enhanced Geothermal Systems(EGS): Integrating Continuous Wavelet Transform(CWT), Microseismic, and Fiber-Optic Data for Enhanced Stimulation Insights** *SPE Annual Technical Conference and Exhibition* [[paper](https://doi.org/10.2118/228063-ms)]
- [2025] **An AI-Augmented Framework for Continuous Quality in CI/CD Pipelines** *Journal of Computer Science and Technology Studies* [[paper](https://doi.org/10.32996/jcsts.2025.7.10.47)]
- [2025] **Continuous Integration for Cloud-Based Swarm Farming Applications** *Qucosa (Saxon State and University Library Dresden)* [[paper](https://monarch.qucosa.de/id/qucosa%3A104356)]
- [2025] **From challenges to metrics: An LLM-driven DevOps recommendation system grounded in evidence-based mappings** *Array* [[paper](https://doi.org/10.1016/j.array.2025.100547)]
- [2025] **MDDOAI: A Model-Driven DevOps Approach to CI/CD Automation** [[paper](https://doi.org/10.1109/itms67030.2025.11236630)]
- [2025] **Application of Retrieval-Augmented Generation (RAG) Systems in Software Engineering Education: An Approach Based on Generative AI and DevOps** *International Journal of Combinatorial Optimization Problems and Informatics.* [[paper](https://doi.org/10.61467/2007.1558.2025.v16i4.1003)]
- [2025] **Integrating DevOps for Continuous AI Deployment** [[paper](https://doi.org/10.70593/978-93-7185-061-2_9)]
- [2025] **Secure DevOps with AI-Enhanced Monitoring** *International Journal of Computer Technology and Electronics Communication* [[paper](https://doi.org/10.15680/ijctece.2025.0805002)]
- [2025] **GeoSAM: Fine-Tuning SAM with Multi-Modal Prompts for Mobility Infrastructure Segmentation** *Frontiers in artificial intelligence and applications* [[paper](https://doi.org/10.3233/faia250844)]
- [2025] **Governed GitOps: Converging Infrastructure-as-Code, Policy-as-Code, and Progressive Delivery** *Journal of Computational Analysis and Applications* [[paper](https://doi.org/10.48047/jocaaa.2025.34.12.19)]
- [2025] **Enhancing Competitive Advantage in Logistics through Infrastructure as Code and Cloud Technologies** *Communications of International Proceedings* [[paper](https://doi.org/10.5171/2025.4527025)]
- [2025] **Advancing real-time validation of automotive software systems via continuous integration and intelligent failure analysis** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-21416-5)]
- [2025] **A Continuous Integration Framework for Machine Learning-Based Mobile Behaviour Analysis** [[paper](https://doi.org/10.1109/i-pact65952.2025.11307944)]
- [2025] **FDSPC: Fast and Direct Smooth Motion Planning via Continuous Curvature Integration** *IEEE Robotics and Automation Letters* [[paper](https://doi.org/10.1109/lra.2025.3604729)]
- [2025] **Glucose360: An Open-Source Python Platform with Event-Based Integration for Continuous Glucose Monitoring Data Analysis** *Diabetes Technology & Therapeutics* [[paper](https://doi.org/10.1177/15209156251374711)]
- [2025] **Integration of CO2 clearance and continuous neurally adjusted ventilatory assist in an animal model of respiratory distress** *Respiratory Physiology & Neurobiology* [[paper](https://doi.org/10.1016/j.resp.2025.104499)]
- [2025] **Digital Twin Cognition: AI-Biomarker Integration in Biomimetic Neuropsychology** *Biomimetics* [[paper](https://doi.org/10.3390/biomimetics10100640)]
- [2025] **Introducing sociopolitical approaches to science education: an integrative review of the concept of subjectivity in science curricula and continuous professional development programmes** *Studies in Science Education* [[paper](https://doi.org/10.1080/03057267.2025.2563997)]
- [2025] **Next‐Generation Piezoelectric Materials in Wearable and Implantable Devices for Continuous Physiological Monitoring** *Advanced Science* [[paper](https://doi.org/10.1002/advs.202507853)]
- [2025] **Agile Stealth: Bioinspired Metamaterials with Continuous Dynamic Tuning** *Advanced Materials* [[paper](https://doi.org/10.1002/adma.202511070)]
- [2025] **Continuous pharmaceutical manufacturing and its contemporary regulatory insights** *Discover Applied Sciences* [[paper](https://doi.org/10.1007/s42452-025-07712-9)]
- [2025] **Recent Progress in Flexible Wearable Sensors for Real-Time Health Monitoring: Materials, Devices, and System Integration** *Micromachines* [[paper](https://doi.org/10.3390/mi16101124)]
- [2025] **Data-Driven Optimization of Discontinuous and Continuous Fiber Composite Processes Using Machine Learning: A Review** *Polymers* [[paper](https://doi.org/10.3390/polym17182557)]
- [2025] **Continuous Integration for Electronic Products–Enabled by Digital Twins** [[paper](https://doi.org/10.1109/idaacs68557.2025.11322082)]
- [2025] **Targeted Test Selection Approach in Continuous Integration** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2509.10279)]
- [2025] **Optimizing Performance in Agile and DevOps Teams** [[paper](https://doi.org/10.1109/ic2ie67206.2025.11283346)]
- [2025] **THE IMPACT OF DEVOPS METHODOLOGIES ON THE DEVELOPMENT OF IT STUDENTS' DIGITAL COMPETENCIES** *Information Technologies and Learning Tools* [[paper](https://doi.org/10.33407/itlt.v108i4.6057)]
- [2025] **AI IN DEVOPS: A FRAMEWORK FOR PREDICTIVE MAINTENANCE AND AUTOMATED ISSUE RESOLUTION** *International Journal of Apllied Mathematics* [[paper](https://doi.org/10.12732/ijam.v38i2s.83)]
- [2025] **An empirical study on performance comparisons of different types of DevOps team formations** *Frontiers in Computer Science* [[paper](https://doi.org/10.3389/fcomp.2025.1554299)]
- [2025] **Implementing Infrastructure as Code (IaC) with Terraform for Scalable Cloud Deployments** *Journal of Information Systems Engineering & Management* [[paper](https://doi.org/10.52783/jisem.v10i60s.13257)]
- [2025] **Provider-Agnostic Infrastructure As Code: A Modular Framework For Secure Multi-Tenant Cloud Automation** *Journal of International Crisis and Risk Communication Research* [[paper](https://doi.org/10.63278/jicrcr.vi.3257)]
- [2025] **Automated Disaster Recovery Infrastructure for HIPAA-Regulated Healthcare Systems: A Cloud-Native Implementation Using Infrastructure as Code** *International Journal of Computational and Experimental Science and Engineering* [[paper](https://doi.org/10.22399/ijcesen.3928)]
- [2025] **ESTABLISHING AN INFRASTRUCTURE AS CODE APPROACH FOR MULTI-REGIONAL INFRASTRUCTURE** *Universum Technical sciences* [[paper](https://doi.org/10.32743/unitech.2025.138.9.20839)]

##### 2007

- [2007] **Continuous Integration: Improving Software Quality and Reducing Risk** *IEEE Software* [[paper](https://doi.org/10.1109/MS.2007.93)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **Topology as a Bridge: The Unification of the Discrete and the Continuous** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20769319)]
- [2026] **LOW-CODE ENVIRONMENT FOR DESIGNING AND TESTING SECURITY POLICIES IN INFRASTRUCTURE-AS-CODE DELIVERY PIPELINES** [[paper](https://doi.org/10.58168/mist2026_1212-1218)]
- [2026] **DevOps orchestrator** *Cvut DSpace (Czech Technical University)* [[paper](https://hdl.handle.net/10467/181265)]
- [2026] **R Code for Regional Analysis: Interactive Scenario Modeling of Public Transport Infrastructure using Leaflet and GTFS Data 地域分析のためのRコード: LeafletとGTFSデータを用いた公共交通インフラのインタラクティブなシナリオ・モデリング** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20130390)]
- [2026] **Binding continuous response features of extended movements: Integration with discrete response but not stimulus features** *Psychological Research* [[paper](https://doi.org/10.1007/s00426-026-02295-5)]
- [2026] **Nonlinear thermal consolidation model for saturated clays integrating non-darcian flow and heat transfer under continuous drainage boundary** *International Journal of Heat and Mass Transfer* [[paper](https://doi.org/10.1016/j.ijheatmasstransfer.2026.128686)]
- [2026] **devops and cloud computing** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19830060)]
- [2026] **From Concrete to Code: A Survey of AI-Driven Transportation Infrastructure, Security, and Human Interaction** *Sensors* [[paper](https://doi.org/10.3390/s26072219)]
- [2026] **R Code for Regional Analysis: Interactive Mapping of Public Transport Infrastructure using Leaflet 地域分析のためのRコード:Leafletによる公共交通(バス)配置のインタラクティブ・マップ化** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19809487)]
- [2026] **Monolithic integration of continuous-variable cluster-state generation, manipulation and measurement** *Nature Photonics* [[paper](https://doi.org/10.1038/s41566-026-01868-5)]
- [2026] **Auditors in the digital risk era: A conceptual framework for integrating cybersecurity, continuous auditing, and professional judgment** *EDPACS* [[paper](https://doi.org/10.1080/07366981.2026.2640130)]
- [2026] **DevOps research across a decade: Patterns, trends, and insights with LDA** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108118)]
- [2026] **Multifunctional CNT/cellulose-BN/PVA Composites Integrating Dual-continuous Network Structure with Gradient Conductivity for Electromagnetic Interference Shielding and Joule Heating** *Chinese Journal of Polymer Science* [[paper](https://doi.org/10.1007/s10118-025-3520-6)]
- [2026] **IdempotencyGuard: Static Analysis for Infrastructure as Code Idempotence** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18487090)]
- [2026] **A foundation model for continuous glucose monitoring data** *Nature* [[paper](https://doi.org/10.1038/s41586-025-09925-9)]
- [2026] **Wearable microneedle sensors for continuous interstitial fluid monitoring** *Biosensors and Bioelectronics* [[paper](https://doi.org/10.1016/j.bios.2026.118385)]
- [2026] **DevOps** [[paper](https://doi.org/10.1007/978-3-662-72726-3_7)]
- [2026] **Carbon-Aware AI Control Plane for DevOps Automation: A Reference Architecture and Next-Generation Sustainability Framework** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3656467)]
- [2026] **Monitoring in DevOps** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-443-45032-7.00010-9)]
- [2026] **DevOps-Aktivitäten** *Essentials* [[paper](https://doi.org/10.1007/978-3-658-51692-5_3)]
- [2026] **DevOps – Kritik** *Essentials* [[paper](https://doi.org/10.1007/978-3-658-51692-5_6)]
- [2026] **Einleitung – warum DevOps?** *Essentials* [[paper](https://doi.org/10.1007/978-3-658-51692-5_1)]
- [2026] **Mastering DevOps** *Elsevier eBooks* [[paper](https://doi.org/10.1016/c2025-0-00512-4)]
- [2026] **Cloud computing for DevOps** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-443-45032-7.00005-5)]
- [2026] **Introduction to DevOps** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-443-45032-7.00001-8)]
- [2026] **devops-predictive-logs** *Hugging Face* [[paper](https://doi.org/10.57967/hf/7504)]
- [2026] **DevSecOps and DevOps for Linux** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-2077-9)]
- [2026] **DevOps osana ohjelmistotuotantoa** *Tampere University Institutional Repository (Tampere University)* [[paper](https://trepo.tuni.fi/handle/10024/238149)]
- [2026] **IMPACT OF ARTIFICIAL INTELLIGENCE ON DEVOPS ENGINEERING** [[paper](https://doi.org/10.34218/ijctm_05_01_001)]

##### 2025

- [2025] **Integrating dimensionless analysis and reaction-diffusion modeling in the continuous synthesis of alginate microgels for dye removal** *Journal of Molecular Liquids* [[paper](https://doi.org/10.1016/j.molliq.2025.129081)]
- [2025] **Intelligent interaction control for aerial manipulator: integrating visual servoing and continuous characteristic model** *Nonlinear Dynamics* [[paper](https://doi.org/10.1007/s11071-025-11865-y)]
- [2025] **Additive manufacturing of continuous carbon fiber-reinforced C/C composites with synergistic shrinkage suppression and multifunctional integration** *Composites Communications* [[paper](https://doi.org/10.1016/j.coco.2025.102688)]
- [2025] **opourazar/operation-devops: v0.2.0** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17873041)]
- [2025] **Operationalizing ESG-as-Code: Automating ESG Compliance and Regulatory Reporting Pipelines Using Containerized AI Workflows on Kubernetes–OpenStack Infrastructure.** *Algora* [[paper](https://doi.org/10.63084/algora.v2i2.60)]
- [2025] **Integrable and Continuous Solutions of the Nonlinear Delayed Abel Fractal Integral Equation of the Second Kind** *International Journal of Analysis and Applications* [[paper](https://doi.org/10.28924/2291-8639-23-2025-285)]
- [2025] **Barriers to translating continuous monitoring technologies for preventative medicine** *Nature Biomedical Engineering* [[paper](https://doi.org/10.1038/s41551-025-01520-7)]
- [2025] **Approaches to Fault Tolerance and Disaster Recovery in DevOps Processes** *Premier journal of science.* [[paper](https://doi.org/10.70389/pjs.100165)]
- [2025] **The sociotechnical politics of digital sovereignty: Frictional infrastructures and the alignment of privacy and geopolitics** *Big Data & Society* [[paper](https://doi.org/10.1177/20539517251400729)]
- [2025] **Integrating Continuous Glucose Monitoring Into Pharmacy Elective Curriculum: A Practical Learning Experience** *Journal of Pharmacy Technology* [[paper](https://doi.org/10.1177/87551225251379742)]
- [2025] **Enhancing BankCo’s Digital Transformation with Cloud Governance Aligned to Ambidextrous COBIT 2019 Traditional and Focus Area DevOps** [[paper](https://doi.org/10.1109/icoseit67010.2025.11291041)]
- [2025] **Climate change impacts on geotechnical infrastructure: role of unsaturated soil mechanics for adaptation** *Frontiers in Built Environment* [[paper](https://doi.org/10.3389/fbuil.2025.1666334)]
- [2025] **Ambidextrous Blockchain Governance Approach for Advancing SmartCo's Digital Transformation Using COBIT 2019 Traditional and DevOps** *Scientific Journal of Informatics* [[paper](https://doi.org/10.15294/sji.v12i3.26974)]
- [2025] **From IaC to IoC—Using Infrastructure as Code (IaC) to Generate Synthetic Datasets of Compromised (IoC) Linux Systems for Use in Digital Forensics** *Digital Threats Research and Practice* [[paper](https://doi.org/10.1145/3748268)]
- [2025] **ARPaCCino: An Agentic-RAG for Policy as Code Compliance** *Communications in computer and information science* [[paper](https://arxiv.org/abs/2507.10584)]
- [2025] **TESTING-BASED PREVENTION OF MISCONFIGURATION THREATS IN AWS INFRASTRUCTURE AS CODE** *Cybersecurity Education Science Technique* [[paper](https://doi.org/10.28925/2663-4023.2025.29.887)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Studying Developer Perceptions on the Potential of CI Recommendation Systems** [[paper](https://arxiv.org/abs/2608.02682)]
- [2026] **Stylometric Defenses Against Author Impersonation in Software Repositories** [[paper](https://arxiv.org/abs/2608.02695)]
- [2026] **Doc2CI: A Multi-Service Study of CI Configuration Generation Using Large Language Models** [[paper](https://arxiv.org/abs/2608.01451)]
- [2026] **Alteron: A Tool for Behavioral Regression Testing Across NLP Classifier Versions** [[paper](https://arxiv.org/abs/2607.29557)] [[code](https://github.com/shazzad5709/alteron)]
- [2026] **Not In My Git Yard: Catching Backdoors at Commit and Release Time** [[paper](https://arxiv.org/abs/2607.26719)]
- [2026] **Beyond Pixel Diffs: Benchmarking Image Change Captioning for Web UI Visual Regression Testing** [[paper](https://arxiv.org/abs/2607.01728)]
- [2026] **Claimed or Attested? A Commit-Signature Dataset and Identity Trust Tiers across the World of Code** [[paper](https://arxiv.org/abs/2607.06194)]
- [2026] **How Far Are We from Detecting Flaky Tests? On the Limits of Code-Based Detection** [[paper](https://arxiv.org/abs/2607.09345)]
- [2026] **Verifying the Rust Standard Library** [[paper](https://arxiv.org/abs/2606.17374)]
- [2026] **Exploring Statistical Change Point Detection Techniques for Performance Anomaly Detection at Mozilla** [[paper](https://arxiv.org/abs/2606.18377)]
- [2026] **Understanding the Rejection of Fixes Generated by Agentic Pull Requests -- Insights from the AIDev Dataset** [[paper](https://arxiv.org/abs/2606.13468)]
- [2026] **Similar Pattern Annotation via Retrieval Knowledge for LLM-Based Test Code Fault Localization** [[paper](https://arxiv.org/abs/2605.07957)]
- [2026] **QUTest: A Native Testing Framework for Quantum Programs** [[paper](https://arxiv.org/abs/2605.19736)] [[code](https://github.com/QBugs/qutest)]
- [2026] **RSE of a Quantum Transport Code and its Effects** [[paper](https://arxiv.org/abs/2605.21334)]
- [2026] **Bayesian Sequential Verification for Budget-Aware Quantum Program Testing** [[paper](https://arxiv.org/abs/2605.15601)]
- [2026] **Heimdallr: Characterizing and Detecting LLM-Induced Security Risks in GitHub CI Workflows** [[paper](https://arxiv.org/abs/2605.05969)]
- [2026] **From Assistance to Agency: Rethinking Autonomy and Control in CI/CD Pipelines** [[paper](https://arxiv.org/abs/2605.07062)]
- [2026] **An Architecture for Decentralised Deployment and Operation of Blockchain Applications** [[paper](https://arxiv.org/abs/2605.22239)]
- [2026] **Is this Build Failure Related to my Patch? An Empirical Study of Unrelated Build Failures in Continuous Integration** [[paper](https://arxiv.org/abs/2605.05564)]
- [2026] **Deployment, DevOps, and Automation** *Productivity Press eBooks* [[paper](https://doi.org/10.4324/9781003729068-10)]
- [2026] **richardaiagent/devops-aiops-platform-vol2: Enterprise DevOps AIOps Platform v2.0** *Open MIND* [[paper](https://github.com/richardaiagent/devops-aiops-platform-vol2/tree/v1.0)]
- [2026] **Web Servers and Cloud DevOps** *Auerbach Publications eBooks* [[paper](https://doi.org/10.1201/9781003727651-11)]
- [2026] **Journal of Software Quality Engineering and DevOps** *Journal of Software Quality Engineering and DevOps* [[paper](https://doi.org/10.55124/3071-5946)]
- [2026] **Beyond the YAML File: Understanding Real-World GitHub Actions Workflow Adoption** [[paper](https://arxiv.org/abs/2604.17662)]
- [2026] **A Vision for Context-Aware CI Adoption Decisions** [[paper](https://arxiv.org/abs/2604.09683)]
- [2026] **A Test Taxonomy and Continuous Integration Ecosystem for Dynamic Resource Management in HPC** [[paper](https://arxiv.org/abs/2604.26824)]
- [2026] **Commit-Aware Learning-Based Test Case Prioritization for Continuous Integration** [[paper](https://arxiv.org/abs/2604.25363)]
- [2026] **Cache-Related Smells in GitLab CI/CD: Comprehensive Catalog, Automated Detection, and Empirical Evidence** [[paper](https://arxiv.org/abs/2604.17890)]
- [2026] **Where did we fail? -- Reproducing build failures in embedded open source software** [[paper](https://arxiv.org/abs/2604.27075)]
- [2026] **Reliability of AI Bots Footprints in GitHub Actions CI/CD Workflows** [[paper](https://arxiv.org/abs/2604.18334)]
- [2026] **CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows** [[paper](https://arxiv.org/abs/2604.27148)]
- [2026] **How Developers Adopt, Use, and Evolve CI/CD Caching: An Empirical Study on GitHub Actions** [[paper](https://arxiv.org/abs/2604.13129)]
- [2026] **GitFarm: Git as a Service for Large-Scale Monorepos** [[paper](https://arxiv.org/abs/2604.11977)]
- [2026] **Adaptive and AI-Augmented Security Testing: A Systematic Survey of Program Analysis, Feedback-Driven Testing, and Hybrid Learning-Based Approaches** [[paper](https://arxiv.org/abs/2604.27000)]
- [2026] **Android Instrumentation Testing in Continuous Integration: Practices, Patterns, and Performance** [[paper](https://arxiv.org/abs/2604.03438)]
- [2026] **On the Reliability of Agentic AI in Continuous Integration Pipelines** [[paper](https://doi.org/10.1145/3793302.3793585)]
- [2026] **Prinzo: An Automated Printing Infrastructure Built on QR Code Technology and Real-Time Privacy** [[paper](https://doi.org/10.1109/dicct69099.2026.11536010)]
- [2026] **Data-Oriented Modeling for Spacecraft Design** [[paper](https://arxiv.org/abs/2603.24841)] [[code](https://github.com/VisVivaSpace/vverdad-prototype)]
- [2026] **SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration** [[paper](https://arxiv.org/abs/2603.03823)]
- [2026] **From Leaderboard to Deployment: Code Quality Challenges in AV Perception Repositories** [[paper](https://arxiv.org/abs/2603.02194)]
- [2026] **A Practical Framework for Flaky Failure Triage in Distributed Database Continuous Integration** [[paper](https://arxiv.org/abs/2603.23054)]
- [2026] **Praxium: Diagnosing Cloud Anomalies with AI-based Telemetry and Dependency Analysis** [[paper](https://arxiv.org/abs/2603.23890)]
- [2026] **Risk-Aware Batch Testing for Performance Regression Detection** [[paper](https://arxiv.org/abs/2604.00222)]
- [2026] **Smart wearable and implantable biosensors for continuous health monitoring: materials, biocompatibility, and AI integration** *npj Flexible Electronics* [[paper](https://doi.org/10.1038/s41528-026-00560-6)]
- [2026] **Continuous Integration and Deployment for Data Systems** [[paper](https://doi.org/10.70593/978-93-7185-364-4_8)]
- [2026] **DevOps Laboratory Manual** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18979517)]
- [2026] **AWS Interview Questions For Devops** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18955256)]
- [2026] **It's Not Just Timestamps: A Study on Docker Reproducibility** [[paper](https://arxiv.org/abs/2602.17678)]
- [2026] **Source Code Hotspots: A Diagnostic Method for Quality Issues** [[paper](https://arxiv.org/abs/2602.13170)]
- [2026] **Causal Inference for the Effect of Code Coverage on Bug Introduction** [[paper](https://arxiv.org/abs/2602.03585)]
- [2026] **Understanding and Detecting Flaky Builds in GitHub Actions** [[paper](https://arxiv.org/abs/2602.02307)]
- [2026] **Role of CI Adoption in Mobile App Success: An Empirical Study of Open-Source Android Projects** [[paper](https://arxiv.org/abs/2602.01957)]
- [2026] **Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection** [[paper](https://arxiv.org/abs/2602.05312)]
- [2026] **PhantomRun: Auto Repair of Compilation Errors in Embedded Open Source Software** [[paper](https://arxiv.org/abs/2602.20284)]
- [2026] **Cross-Project Flakiness: A Case Study of the OpenStack Ecosystem** [[paper](https://arxiv.org/abs/2602.09311)]
- [2026] **Terraform-Driven Infrastructure as Code in Financial Data Platforms** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19165738)]
- [2026] **Leveraging LLMs for Generating Infrastructure as Code: An Exploratory Empirical Study** [[paper](https://doi.org/10.1145/3796563.3796572)]
- [2026] **Predicting Intermittent Job Failure Categories for Diagnosis Using Few-Shot Fine-Tuned Language Models** [[paper](https://arxiv.org/abs/2601.22264)]
- [2026] **Reinforcement Learning for Dynamic Workflow Optimization in CI/CD Pipelines** [[paper](https://arxiv.org/abs/2601.11647)]
- [2026] **LogSieve: Task-Aware CI Log Reduction for Sustainable LLM-Based Analysis** [[paper](https://arxiv.org/abs/2601.20148)]
- [2026] **Human DevOps: A tool for measuring and enhancing human factors in DevOps adoption** *SoftwareX* [[paper](https://doi.org/10.1016/j.softx.2026.102515)]
- [2026] **DevOps and Infrastructure** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-2347-3_22)]
- [2026] **DevOps and DataOps for Snowflake** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-2628-3_20)]
- [2026] **Infrastructure As Code** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-2347-3_23)]

##### 2025

- [2025] **Fast and Realistic Automated Scenario Simulations and Reporting for an Autonomous Racing Stack** [[paper](https://arxiv.org/abs/2512.24402)]
- [2025] **Detecting Flakiness in Quantum Software: A Dynamic Testing Approach** [[paper](https://arxiv.org/abs/2512.18088)]
- [2025] **Integrating Continuous Cover, Manure Management, and Anaerobic Digestion Strategies on a Pennsylvania Dairy Farm: A Life Cycle Assessment** *Environmental Science & Technology* [[paper](https://doi.org/10.1021/acs.est.5c04797)]
- [2025] **Continuous Compliance Pipelines for HIPAA-Aligned Healthcare DevOps Systems** *International Journal of Science and Engineering Applications* [[paper](https://doi.org/10.7753/ijsea1012.1006)]
- [2025] **DRS-OSS: A Diff-Risk Scoring Tool for Continuous Integration Workflows** [[paper](https://arxiv.org/abs/2511.21964)]
- [2025] **Exploringand Unleashing the Power of Large Language Models in CI/CD Configuration Translation** [[paper](https://arxiv.org/abs/2511.01316)]
- [2025] **Ontology-Driven Model-to-Model Transformation of Workflow Specifications** [[paper](https://arxiv.org/abs/2511.13661)]
- [2025] **AI-Enabled Continuous Integration And Deployment Pipelines** *Open MIND* [[paper](https://www.ijset.in/ai-enabled-continuous-integration-and-deployment-pipelines/)]
- [2025] **Declarative Automation of DevOps Workflows through Infrastructure as Code** [[paper](https://doi.org/10.22541/au.176236358.85778824/v1)]
- [2025] **Large-Scale Empirical Analysis of Continuous Fuzzing: Insights from 1 Million Fuzzing Sessions** [[paper](https://arxiv.org/abs/2510.16433)]
- [2025] **Auto-repair without test cases: How LLMs fix compilation errors in large industrial embedded code** [[paper](https://arxiv.org/abs/2510.13575)]
- [2025] **Operationalizing AI: Empirical Evidence on MLOps Practices, User Satisfaction, and Organizational Context** [[paper](https://arxiv.org/abs/2510.09968)]
- [2025] **Towards an Optimized Benchmarking Platform for CI/CD Pipelines** [[paper](https://arxiv.org/abs/2510.18640)]
- [2025] **Past, Present, and Future of Bug Tracking in the Generative AI Era** [[paper](https://arxiv.org/abs/2510.08005)]
- [2025] **A General Solution for the Implementation of CI/CD in Embedded Linux Development** [[paper](https://arxiv.org/abs/2510.19240)]
- [2025] **AI-Driven DevOps Automation for Cloud-Native Application Modernization** [[paper](https://doi.org/10.1007/978-3-032-02853-2_9)]
- [2025] **A Study on DevOps and Continuous Delivery Models** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20280655)]
- [2025] **Vision: An Extensible Methodology for Formal Software Verification in Microservice Systems** [[paper](https://arxiv.org/abs/2509.02860)]
- [2025] **Multi-Threaded Software Model Checking via Parallel Trace Abstraction Refinement** [[paper](https://arxiv.org/abs/2509.13699)]
- [2025] **Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open & Industry Data** [[paper](https://arxiv.org/abs/2509.09313)]
- [2025] **ReDef: Do Code Language Models Truly Understand Code Changes for Just-in-Time Software Defect Prediction?** [[paper](https://arxiv.org/abs/2509.09192)]
- [2025] **On the Illusion of Success: An Empirical Study of Build Reruns and Silent Failures in Industrial CI** [[paper](https://arxiv.org/abs/2509.14347)]
- [2025] **REST API Testing in DevOps: A Study on an Evolving Healthcare IoT Application** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3765744)]
- [2025] **DevOps for Automatic Train Operation with the DEFACTO Pipeline** [[paper](https://doi.org/10.1109/iavvc61942.2025.11219450)]
- [2025] **DTInsight: A Tool for Explicit, Interactive, and Continuous Digital Twin Reporting** [[paper](https://arxiv.org/abs/2508.18431)]
- [2025] **Addressing Reproducibility Challenges in HPC with Continuous Integration** [[paper](https://arxiv.org/abs/2508.21289)]
- [2025] **The Integration of Agile Methodologies in DevOps Practices within the Information Technology Industry** [[paper](https://arxiv.org/abs/2508.21811)]
- [2025] **Artificial Intelligence-Driven DevOps: Automating, Optimizing, and Securing Modern Software Delivery** [[paper](https://doi.org/10.70593/978-93-7185-022-3)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Multicloud Security Assessment: A Benchmark Study of Infrastructure as Code Scanners** *ICCK Transactions on Information Security and Cryptography* [[paper](https://doi.org/10.62762/tisc.2026.777114)]
- [2026] **Continuous Integration Test and Evaluation Concept of Operations** *The ITEA Journal of Test and Evaluation* [[paper](https://doi.org/10.61278/itea.47.1.1001)]
- [2026] **Continuous inclined-screw torrefaction with off-gas heat integration: pilot-scale residence-time impacts on severity and fuel quality** *Case Studies in Chemical and Environmental Engineering* [[paper](https://doi.org/10.1016/j.cscee.2026.101339)]
- [2026] **Continuous Integration Optimization Experiment** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18683783)]
- [2026] **Provisioning Multi-Stage Cloud Infrastructure with Infrastructure as Code** *FH JOANNEUM ePUB* [[paper](https://resolver.obvsg.at/urn:nbn:at:at-fhj:1-59304)]

##### 2025

- [2025] **Employing Continuous Integration inspired workflows for benchmarking of scientific software — A use case on numerical cut element quadrature** *Advances in Engineering Software* [[paper](https://arxiv.org/abs/2503.17192)]
- [2025] **Integration of artificial intelligence and wearable technology in the management of diabetes and prediabetes** *npj Digital Medicine* [[paper](https://doi.org/10.1038/s41746-025-02036-9)]
- [2025] **Evaluation of Foundation Models for Infrastructure-as-Code Automation on Amazon Bedrock** [[paper](https://doi.org/10.1109/cars67163.2025.11337933)]
- [2025] **Industrial Views on DevOps Adoption Before and After Implementation: A Qualitative Comparison** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04403-7_18)]
- [2025] **Design, integration, and evaluation of a low-cost system for automatic apple picking and infield sorting** *Computers and Electronics in Agriculture* [[paper](https://doi.org/10.1016/j.compag.2025.110933)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **White paper: A perspective on civilian-to-defence research transfer to SDD** [[paper](https://arxiv.org/abs/2608.09349)]
- [2026] **Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions** [[paper](https://arxiv.org/abs/2607.02294)]
- [2026] **Documentation Technical Debt in Continuous Integration and Continuous Deployment: Replication Dataset** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21584519)]
- [2026] **DevOps and General Developers: Insights from Stack Overflow's 2023 Survey** [[paper](https://arxiv.org/abs/2606.19395)]
- [2026] **Overcoming Challenges in Agile and DevOps Integration: A Qualitative Study** [[paper](https://arxiv.org/abs/2606.01676)]
- [2026] **AutoPipelineAI: Context-Aware CI/CD Pipeline Generation from Natural Language** [[paper](https://arxiv.org/abs/2606.06662)]
- [2026] **BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization** [[paper](https://arxiv.org/abs/2606.27733)]
- [2026] **DEVhaitam/Infrastructure-as-Code-IaC-Quality-Assurance-QA-SLR-: v2.0** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20538519)]
- [2026] **Low-Code Paradox in DevOps: Security and Governance Insights from Practitioners** [[paper](https://arxiv.org/abs/2605.16971)]
- [2026] **Software Product Line Engineering: Adoption, Tooling and AI Era Challenges** [[paper](https://arxiv.org/abs/2605.21353)]
- [2026] **Operationalizing Software Engineering Theories for Practical Validation** [[paper](https://arxiv.org/abs/2605.03257)]
- [2026] **Measuring Delivery Consistency in Practice: A DORA Extension from a Multi-Platform Release Setting** [[paper](https://arxiv.org/abs/2606.00364)]
- [2026] **Fixed but Not Gone: A Longitudinal Study of Security Violations in Infrastructure-as-Code** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20172372)]
- [2026] **A Model-Driven Digital Twin for the Systematic Improvement of DevOps Pipelines** [[paper](https://arxiv.org/abs/2604.02077)]
- [2026] **Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode** [[paper](https://arxiv.org/abs/2604.04978)]
- [2026] **AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems** *ICLR 2026 Workshop on Agents in the Wild. Camera-ready version with revised layout and framework overview figure* [[paper](https://arxiv.org/abs/2603.14688)]
- [2026] **Packaging Jupyter notebooks as installable desktop apps using LabConstrictor** [[paper](https://arxiv.org/abs/2603.10704)]
- [2026] **Architectural Anti-Patterns in Student-Developed Microservice Architectures: An Exploratory Study** [[paper](https://arxiv.org/abs/2602.07147)]
- [2026] **HAIF: A Human-AI Integration Framework for Hybrid Team Operations** [[paper](https://arxiv.org/abs/2602.07641)]
- [2026] **DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle** [[paper](https://arxiv.org/abs/2601.20882)]
- [2026] **Auditable DevOps Automation via VSM and GQM** [[paper](https://arxiv.org/abs/2601.03574)]
- [2026] **From Everything-is-a-File to Files-Are-All-You-Need: How Unix Philosophy Informs the Design of Agentic AI Systems** [[paper](https://arxiv.org/abs/2601.11672)]
- [2026] **Cognitive Platform Engineering for Autonomous Cloud Operations** [[paper](https://arxiv.org/abs/2601.17542)]
- [2026] **When AI Agents Touch CI/CD Configurations: Frequency and Success** [[paper](https://arxiv.org/abs/2601.17413)]
- [2026] **Architecting AgentOps Needs CHANGE** [[paper](https://arxiv.org/abs/2601.06456)]
- [2026] **An Intelligent Multi-Class XGBoost-Based Model for Optimizing DevOps Continuous Integration and Continuous Deployment Failure Prediction.** *Inf.* [[paper](https://dblp.org/rec/journals/information/AlBaltahAAAA26)]
- [2026] **Continuous integration, delivery, and deployment** *Mastering DevOps* [[paper](https://doi.org/10.1016/b978-0-443-45032-7.00008-0)]
- [2026] **Toward continuous and non-invasive monitoring: a scoping review of <i>in vitro</i> blood glucose devices from electrochemistry to optics and micro-system integration** *Journal of Materials Chemistry B* [[paper](https://doi.org/10.1039/d5tb02338f)]
- [2026] **A systematic survey: Implementation of software life cycle using DevOps** *AIP conference proceedings* [[paper](https://doi.org/10.1063/5.0301356)]

##### 2025

- [2025] **Aligning Security Compliance and DevOps: A Longitudinal Study** [[paper](https://arxiv.org/abs/2512.14453)]
- [2025] **A Systematic Analysis of Higher Education on Software Engineering in the Netherlands** [[paper](https://arxiv.org/abs/2512.12650)]
- [2025] **An Architecture for Remote Container Builds and Artifact Delivery Using a Controller-Light Jenkins CI/CD Pipeline** [[paper](https://arxiv.org/abs/2511.05720)]
- [2025] **DataOps-driven CI/CD for analytics repositories** [[paper](https://arxiv.org/abs/2511.12277)]
- [2025] **Docker-based CI/CD for Rocq/OCaml projects** [[paper](https://arxiv.org/abs/2510.19089)]
- [2025] **RAG4Tickets: AI-Powered Ticket Resolution via Retrieval-Augmented Generation on JIRA and GitHub Data** [[paper](https://arxiv.org/abs/2510.08667)]
- [2025] **Multi-Agent Code-Orchestrated Generation for Reliable Infrastructure-as-Code** [[paper](https://arxiv.org/abs/2510.03902)]
- [2025] **Scalable CI/CD for Legacy Modernization: An Industrial Experience Addressing Internal Challenges Related to the 2025 Japan Cliff** [[paper](https://arxiv.org/abs/2510.17430)]
- [2025] **"Let it be Chaos in the Plumbing!" Usage and Efficacy of Chaos Engineering in DevOps Pipelines** [[paper](https://arxiv.org/abs/2509.14931)]
- [2025] **Enhancing DevOps Efficiency through AI-Driven Predictive Models for Continuous Integration and Deployment Pipelines** *International Journal of Research Publication and Reviews* [[paper](https://doi.org/10.55248/gengpi.6.0125.0229)]

##### 2024

- [2024] **Infrastructure as Code: A Systematic Mapping Study** [[paper](https://arxiv.org/abs/2401.01001)]
- [2024] **Securing Cloud-Based DevOps: Integration of Security into Continuous Delivery** [[paper](https://doi.org/10.31219/osf.io/bqdjh)]
- [2024] **Enhancing Continuous Integration and Delivery Pipelines Using Azure DevOps and GitHub Actions** [[paper](https://doi.org/10.2139/ssrn.5285094)]
- [2024] **Continuous Integration and Continuous Delivery  (CI/CD) Pipelines: Explore How Devops Practices Ensure Seamless Integration And Delivery of AI-Models** [[paper](https://doi.org/10.2139/ssrn.5229541)]

##### 2023

- [2023] **DevOps and continuous integration/continuous deployment (CI/CD) automation** *Advances in Engineering Innovation* [[paper](https://doi.org/10.54254/2977-3903/4/2023031)]
- [2023] **Multi-Project Multi-Environment Approach - An Enhancement to Existing DevOps and Continuous Integration and Continuous Deployment Tools.** *Comput.* [[paper](https://dblp.org/rec/journals/computers/ErdenebatBBK23)]

##### 2022

- [2022] **Effect of Using Continuous Integration (CI) and Continuous Delivery (CD) Deployment in DevOps to reduce the Gap between Developer and Operation.** *ACIT* [[paper](https://dblp.org/rec/conf/acit3/MowadFH22)]
- [2022] **Eat your own DevOps: a model driven approach to justify continuous integration pipelines.** *MoDELS* [[paper](https://dblp.org/rec/conf/models/Pulgar22)]
- [2022] **Robbery on DevOps: Understanding and Mitigating Illicit Cryptomining on Continuous Integration Service Platforms.** *SP* [[paper](https://dblp.org/rec/conf/sp/00480C0LXZ0Z22)]

##### 2021

- [2021] **Continuous Integration** *Continuous Delivery 2.0* [[paper](https://doi.org/10.1201/9781003221579-9)]
- [2021] **Branch Strategy Conducive to Integration** *Continuous Delivery 2.0* [[paper](https://doi.org/10.1201/9781003221579-8)]

##### 2020

- [2020] **Hands-on Azure Pipelines** [[paper](https://doi.org/10.1007/978-1-4842-5902-3)]

##### 2019

- [2019] **Agile, Continuous Integration, and DevOps.** *COMPSAC* [[paper](https://dblp.org/rec/conf/compsac/Chang19)]
- [2019] **DevOps Continuous Integration: Moving Germany&apos;s Federal Employment Agency Test System into Embedded In-Memory Technology.** *HICSS* [[paper](https://dblp.org/rec/conf/hicss/SultanowCJBM19)]

##### 2018

- [2018] **DevOps Improvements for Reduced Cycle Times with Integrated Test Optimizations for Continuous Integration.** *COMPSAC* [[paper](https://dblp.org/rec/conf/compsac/MarijanLS18)]
- [2018] **Effect of Continuous Integration on Build Health in Undergraduate Team Projects.** *DEVOPS* [[paper](https://dblp.org/rec/conf/laser/EmburyP18)]
- [2018] **Building lean continuous integration and delivery pipelines by applying DevOps principles: a case study at Varidesk.** *ESEC/SIGSOFT FSE* [[paper](https://dblp.org/rec/conf/sigsoft/DebroyMB18)]

##### 2016

- [2016] **Implementing Continuous Integration** *DevOps on the Microsoft Stack* [[paper](https://doi.org/10.1007/978-1-4842-1446-6_9)]

##### 2015

- [2015] **Including Performance Benchmarks into Continuous Integration to Enable DevOps.** *ACM SIGSOFT Softw. Eng. Notes* [[paper](https://dblp.org/rec/journals/sigsoft/WallerEH15)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **GitOps and Infrastructure as Code** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21938483)]
- [2026] **Artifact for Metamorphic Testing for Infrastructure-as-Code Engines** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18755966)]
- [2026] **Infrastructure as Compromise: Abusing Residual Trust in Infrastructure as Code Tools** [[paper](https://doi.org/10.1145/3800506.3803500)]
- [2026] **Evaluating Language Models on Infrastructure-as-Code Development** [[paper](https://doi.org/10.1109/cloudsummit68932.2026.00021)]
- [2026] **Towards Mitigating Infrastructure-as-Code Security Smells** *Open Repository and Bibliography (University of Luxembourg)* [[paper](https://orbilu.uni.lu/handle/10993/68436)]
- [2026] **Artifact for FSE'2026 paper "Unfulfilled Promises: LLM-Based Detection of OS Compatibility Issues in Infrastructure as Code"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19512669)]
- [2026] **Automated Incident Management using Infrastructure-as-Code - code, datasets, and analysis notebooks** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19047155)]
- [2026] **Using Infrastructure as Code to Provision Cloud Resources for Computational Laboratories** *Journal of Chemical Education* [[paper](https://doi.org/10.1021/acs.jchemed.6c00015)]
- [2026] **A new C1-continuous variational integration scheme for mechanical systems subjected to acceleration-dependent forces** *Journal of Computational and Applied Mathematics* [[paper](https://doi.org/10.1016/j.cam.2026.117509)]
- [2026] **Sustainability Smells in Infrastructure as Code** *PolyPublie (École Polytechnique de Montréal)* [[paper](https://publications.polymtl.ca/73177/37/2026_SeifeldinKosbar.pdf)]
- [2026] **Deployment for Cyber-Physical Systems: The Relations Between the Testing and Monitoring DevOps Phases** [[paper](https://doi.org/10.1007/978-981-95-1786-2_6)]
- [2026] **DevOps Case Studies: Anthropic** *Open MIND* [[paper](https://osf.io/det7g)]
- [2026] **Standardization for DevOps and Cyber-Physical Systems** [[paper](https://doi.org/10.1007/978-981-95-1786-2_8)]
- [2026] **Responsible DevOps for Cyber-Physical Systems** [[paper](https://doi.org/10.1007/978-981-95-1786-2_7)]
- [2026] **DevOps Testing for Cyber-Physical Systems** [[paper](https://doi.org/10.1007/978-981-95-1786-2_4)]
- [2026] **Infrastructure as Code with Terraform** [[paper](https://doi.org/10.1007/978-3-032-22035-6_5)]
- [2026] **Performance-related Configuration Patterns in Infrastructure as Code** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6806070)]
- [2026] **Automated Incident Management using Infrastructure-as-Code** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2026.3676644)]
- [2026] **Infrastructure as Code (IaC) Automation Using Terraform** *University of Alberta Library* [[paper](https://doi.org/10.7939/84337)]
- [2026] **Infrastructure as Code: A Rule Catalog for Incident Self-Healing** [[paper](https://doi.org/10.5220/0014798000004039)]
- [2026] **An Open-Source Reference Architecture for Infrastructure-as-Code Self-Healing** [[paper](https://doi.org/10.5220/0014798100004039)]
- [2026] **Automation of Incident response in containerized enviroments using "Infrastructure as Code"** *Brno University of Technology Digital Library (Brno University of Technology)* [[paper](https://hdl.handle.net/11012/259621)]

##### 2025

- [2025] **Code for global impacts of transportation infrastructure on forest degradation and loss** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17873268)]
- [2025] **Achieving Continuous Deployment with Infrastructure as Code and Container Orchestration** *Repository of the University of Ljubljana (University of Ljubljana)* [[paper](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=176634)]
- [2025] **Metagenomics-metabolomics integration reveals the impacts and action mechanisms of sulfamethoxazole in a continuous-flow aerobic granular sludge membrane bioreactor: System performance and microbial functional shifts** *Chemical Engineering Journal* [[paper](https://doi.org/10.1016/j.cej.2025.168034)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Security-First Evaluation of Text-to-Terraform: Benchmarking LLMs and SLMs for Secure IaC Generation** [[paper](https://arxiv.org/abs/2608.02672)]
- [2026] **Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair** [[paper](https://arxiv.org/abs/2608.13404)]
- [2026] **AI Agent Development for Autonomous DevOps** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21903610)]
- [2026] **TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair** [[paper](https://arxiv.org/abs/2607.11390)]
- [2026] **Taming the Drift: Context-aware Repair of Dockerfile Drift during Software Evolution** [[paper](https://arxiv.org/abs/2607.12541)] [[code](https://github.com/dw763j/Cadre)]
- [2026] **SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code** [[paper](https://arxiv.org/abs/2606.05249)]
- [2026] **Verifier-First Evaluation of Agentic LLMs for Infrastructure-as-Code Generation** [[paper](https://arxiv.org/abs/2607.20478)]
- [2026] **Ambig-IaC: Multi-level Disambiguation for Interactive Cloud Infrastructure-as-Code Synthesis** [[paper](https://arxiv.org/abs/2604.02382)]
- [2026] **Understanding Bugs in Template Engine-Based Applications: Symptoms, Root Causes, and Fix Patterns** [[paper](https://arxiv.org/abs/2604.27692)]
- [2026] **RIVA: Leveraging LLM Agents for Reliable Configuration Drift Detection** [[paper](https://arxiv.org/abs/2603.02345)]
- [2026] **Beyond Local Code Optimization: Multi-Agent Reasoning for Software System Optimization** [[paper](https://arxiv.org/abs/2603.14703)]
- [2026] **Replication package of: The Energy Impact of Batch Testing in Continuous Integration** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18507066)]
- [2026] **TerraFormer: Automated Infrastructure-as-Code with LLMs Fine-Tuned via Policy-Guided Verifier Feedback** [[paper](https://arxiv.org/abs/2601.08734)]
- [2026] **APEX-SWE** [[paper](https://arxiv.org/abs/2601.08806)]
- [2026] **Code and DevOps Assistants** *Apress eBooks* [[paper](https://doi.org/10.1007/979-8-8688-2758-7_34)]

##### 2025

- [2025] **IaC Generation with LLMs: An Error Taxonomy and A Study on Configuration Knowledge Injection** [[paper](https://arxiv.org/abs/2512.14792)]
- [2025] **Evaluación de la conveniencia de adoptar DevOps como estrategia para la entrega continua de productos de software en la Alianza Bioversity -CIAT sede las Américas, Colombia** *LA Referencia (Red Federada de Repositorios Institucionales de Publicaciones Científicas)* [[paper](https://revistas.javerianacali.edu.co/index.php/pensamientopsicologico/article/view/122)]
- [2025] **Accelerating Control Systems with GitOps: A Path to Automation and Reliability** [[paper](https://arxiv.org/abs/2511.05663)]
- [2025] **GenSIaC: Toward Security-Aware Infrastructure-as-Code Generation with Large Language Models** [[paper](https://arxiv.org/abs/2511.12385)]
- [2025] **"Wakeups": the most important DevOps metric** [[paper](https://doi.org/10.59350/18ew7-11v25)]
- [2025] **Security smells in infrastructure as code: a taxonomy update beyond the seven sins** [[paper](https://arxiv.org/abs/2509.18761)]
- [2025] **Principals' perceptions on integrating physically active learning through a continuous professional development programme** *Teaching and Teacher Education* [[paper](https://doi.org/10.1016/j.tate.2025.105193)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **Observing the Quantum Compiler through Automatic Experiment Tracking for Qiskit** [[paper](https://arxiv.org/abs/2608.05041)]
- [2026] **Integration-First Structural Coverage for Embedded Software:Trace-Based Evidence, Hybrid Runtime Analysis, and Cross-Variant Consolidation** [[paper](https://arxiv.org/abs/2608.13322)]
- [2026] **Characterizing the Quality Profile of AI-Generated C++ in Production** [[paper](https://arxiv.org/abs/2608.06640)]
- [2026] **JTA: Joint Testability Architecture for Scenario-Based Validation of Safety-Critical Software** [[paper](https://arxiv.org/abs/2608.05594)]
- [2026] **Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems** [[paper](https://arxiv.org/abs/2608.11166)]
- [2026] **Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools** [[paper](https://arxiv.org/abs/2608.07446)]
- [2026] **Software Engineering for and with GUI Agent** [[paper](https://arxiv.org/abs/2608.09278)]
- [2026] **Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model** [[paper](https://arxiv.org/abs/2608.13867)]
- [2026] **AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence** [[paper](https://arxiv.org/abs/2607.03516)]
- [2026] **Registry-Governed Agent Lifecycle:Completing EDDOps with Evaluation-DrivenRegistration, Promotion, and Retirement on AWS AgentCore** [[paper](https://arxiv.org/abs/2607.00345)]
- [2026] **FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure** [[paper](https://arxiv.org/abs/2607.17525)]
- [2026] **Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization** [[paper](https://arxiv.org/abs/2607.13184)]
- [2026] **TraceSynth: Generating Production-Quality Kernel Traces with Constraint-Guided Diffusion Models** [[paper](https://arxiv.org/abs/2607.12104)]
- [2026] **LLM-Driven CI-CD Workflow Intelligence for Cyber Systems Engineering** [[paper](https://arxiv.org/abs/2607.04579)]
- [2026] **Characterizing Structural Testability in JavaScript: An Empirical Study** [[paper](https://arxiv.org/abs/2607.24965)]
- [2026] **Malaika: Understanding Malware through Tri-Grounded Agentic Reasoning** [[paper](https://arxiv.org/abs/2607.09179)]
- [2026] **LLMoxie: Exploring Agentic AI for Scientific Software Development** [[paper](https://arxiv.org/abs/2607.02703)]
- [2026] **OrEdge: Efficient Multi-Modal Anomaly Detection in Distributed Software Systems via Orthogonal-Domain Learning** [[paper](https://arxiv.org/abs/2608.00309)] [[code](https://github.com/theamrzaki/MicroService_Twin_Original)]
- [2026] **CoACT: Action-Preserving Observation Compression for Coding Agents** [[paper](https://arxiv.org/abs/2607.02911)]
- [2026] **UModel: An Agent-Ready Observability Data Modeling Method at Scale** [[paper](https://arxiv.org/abs/2606.04799)]
- [2026] **AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework** [[paper](https://arxiv.org/abs/2606.18532)]
- [2026] **AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted and Data-Transformation Workflows** [[paper](https://arxiv.org/abs/2607.09682)]
- [2026] **SDVDiag: Multimodal Causal Discovery for Online Diagnosis in Software-defined Vehicles** [[paper](https://arxiv.org/abs/2606.15559)]
- [2026] **A Topology-Aware, Memory-Centric Architecture that Separates Root-Cause Derivation from Root-Cause Explanation** [[paper](https://arxiv.org/abs/2606.20758)]
- [2026] **MCP Server Architecture Patterns for LLM-Integrated Applications** [[paper](https://arxiv.org/abs/2606.30317)]
- [2026] **From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws** [[paper](https://arxiv.org/abs/2606.06324)]
- [2026] **STMutants: A Mutation Testing Dataset for Structured Text Programs in Industrial Automation** [[paper](https://arxiv.org/abs/2606.05499)]
- [2026] **When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime** [[paper](https://arxiv.org/abs/2606.14589)]
- [2026] **DevOps and GitOps Services Roadmap to Maturity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20726702)]
- [2026] **Enabling Performant and Flexible Model-Internal Observability for LLM Inference** [[paper](https://arxiv.org/abs/2605.11093)] [[code](https://github.com/ProjectDMX/DMI)]
- [2026] **AI-Driven Adaptive Adversaries and the Erosion of Cryptographic Trust in Public Key Systems** [[paper](https://arxiv.org/abs/2605.24542)]
- [2026] **KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition** [[paper](https://arxiv.org/abs/2605.25376)]
- [2026] **Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes** [[paper](https://arxiv.org/abs/2605.12078)]
- [2026] **Finding Missing Input Validation in TEEs via LLM-Assisted Symbolic Execution** [[paper](https://arxiv.org/abs/2605.22058)]
- [2026] **LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices** [[paper](https://arxiv.org/abs/2605.03505)] [[code](https://github.com/kottinov/lats-rca)]
- [2026] **AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents** [[paper](https://arxiv.org/abs/2605.13357)]
- [2026] **AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair** [[paper](https://arxiv.org/abs/2605.04624)]
- [2026] **The green dividend of data: How data assetization fuels corporate continuous innovation through financial derisking and AI integration** *International Review of Economics & Finance* [[paper](https://doi.org/10.1016/j.iref.2026.105347)]
- [2026] **Toward an Architectural Blueprint to Observe Sustainability in and by Software Systems** [[paper](https://arxiv.org/abs/2604.09278)]
- [2026] **AI Observability for Large Language Model Systems: A Multi-Layer Analysis of Monitoring Approaches from Confidence Calibration to Infrastructure Tracing** [[paper](https://arxiv.org/abs/2604.26152)]
- [2026] **Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses** [[paper](https://arxiv.org/abs/2604.25850)]
- [2026] **CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend** [[paper](https://arxiv.org/abs/2604.23455)]
- [2026] **The Grand Software Supply Chain of AI Systems** [[paper](https://arxiv.org/abs/2604.27781)]
- [2026] **Operationalizing Reconstructive Authority: Runtime Construction, Dependency Resolution, and Execution Gating in Autonomous Agent Systems** [[paper](https://arxiv.org/abs/2605.23935)]
- [2026] **Beyond Task Success: An Evidence-Synthesis Framework for Evaluating, Governing, and Orchestrating Agentic AI** [[paper](https://arxiv.org/abs/2604.19818)]
- [2026] **LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications** [[paper](https://arxiv.org/abs/2603.27355)]
- [2026] **PARCER as an Operational Contract to Reduce Variance, Cost, and Risk in LLM Systems** [[paper](https://arxiv.org/abs/2603.00856)]
- [2026] **Clawdrain: Exploiting Tool-Calling Chains for Stealthy Token Exhaustion in OpenClaw Agents** [[paper](https://arxiv.org/abs/2603.00902)]
- [2026] **From Natural Language to PromQL: A Catalog-Driven Framework with Dynamic Temporal Resolution for Cloud-Native Observability** [[paper](https://arxiv.org/abs/2604.13048)]
- [2026] **Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes** [[paper](https://arxiv.org/abs/2603.06847)]
- [2026] **Reasoning Provenance for Autonomous AI Agents: Structured Behavioral Analytics Beyond State Checkpoints and Execution Traces** [[paper](https://arxiv.org/abs/2603.21692)]
- [2026] **Bridging Protocol and Production: Design Patterns for Deploying AI Agents with Model Context Protocol** [[paper](https://arxiv.org/abs/2603.13417)]
- [2026] **MetaRCA: A Generalizable Root Cause Analysis Framework for Cloud-Native Systems Powered by Meta Causal Knowledge** [[paper](https://arxiv.org/abs/2603.02032)]
- [2026] **Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents** [[paper](https://arxiv.org/abs/2603.01548)]
- [2026] **REGAL: A Registry-Driven Architecture for Deterministic Grounding of Agentic AI in Enterprise Telemetry** [[paper](https://arxiv.org/abs/2603.03018)]
- [2026] **From Goals to Aspects, Revisited: An NFR Pattern Language for Agentic AI Systems** [[paper](https://arxiv.org/abs/2603.00472)]
- [2026] **Yaksha-Prashna: Understanding eBPF Bytecode Network Function Behavior** [[paper](https://arxiv.org/abs/2602.11232)]
- [2026] **From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems** [[paper](https://arxiv.org/abs/2602.23701)]
- [2026] **From Prompt-Response to Goal-Directed Systems: The Evolution of Agentic AI Software Architecture** [[paper](https://arxiv.org/abs/2602.10479)]
- [2026] **MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems** [[paper](https://arxiv.org/abs/2602.19843)]
- [2026] **Identifying Adversary Tactics and Techniques in Malware Binaries with an LLM Agent** [[paper](https://arxiv.org/abs/2602.06325)]
- [2026] **Agentic Observability: Automated Alert Triage for Adobe E-Commerce** *AAAI* [[paper](https://arxiv.org/abs/2602.02585)]
- [2026] **World of Workflows: A Benchmark for Bringing World Models to Enterprise Systems** [[paper](https://arxiv.org/abs/2601.22130)]
- [2026] **KELP: Robust Online Log Parsing Through Evolutionary Grouping Trees** [[paper](https://arxiv.org/abs/2601.00633)]
- [2026] **Intelligent and Secure Automation of CI/CD Pipelines for Cloud Infrastructures** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-9260975/v1)]
- [2026] **Economic Evaluation of Artificial Intelligence-Driven Software Testing in Modern IT Enterprises** *PPR* [[paper](https://doi.org/10.14293/pr2199.003340.v1)]
- [2026] **Transferable Migration Framework Derived from a Large-scale Tertiary Hospital EHR System.** *MED* [[paper](https://doi.org/10.4258/hir.2026.32.2.145)]
- [2026] **A Proposal of Secure and Automated Over-the-Air Firmware Update Mechanism for IoT Devices Using Continuous Integration and Continuous Delivery.** *MED* [[paper](https://doi.org/10.3390/s26051535)]
- [2026] **SecMLOps: A comprehensive framework for integrating security throughout the machine learning operations lifecycle.** *MED* [[paper](https://doi.org/10.1007/s10664-025-10795-y)]
- [2026] **Performance analysis of network automation techniques for dense IP networks.** *MED* [[paper](https://doi.org/10.1038/s41598-026-40975-9)]
- [2026] **Transforming routine health data use in LMICs through modular, AI-supported automation: insights from Zimbabwe.** *MED* [[paper](https://doi.org/10.1093/oodh/oqag003)]
- [2026] **Reinforcement Learning with AI for Autonomous Incident Response in DevSecOps: Using RL Agents to Detect, Classify, and Mitigate Security Threats in Cloud-Native DevOps Environments** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-14044-9_30)]
- [2026] **devops-incident-response** *Hugging Face* [[paper](https://doi.org/10.57967/hf/7497)]

##### 2025

- [2025] **Monitoring Monitorability** [[paper](https://arxiv.org/abs/2512.18311)]
- [2025] **Opus: A Quantitative Framework for Workflow Evaluation** [[paper](https://arxiv.org/abs/2511.04220)]
- [2025] **Quality-by-digital-design for the in-process integration of Raman spectroscopy as a PAT tool in continuous manufacturing of pharmaceutical liquids and semi-solids** *International Journal of Pharmaceutics* [[paper](https://doi.org/10.1016/j.ijpharm.2025.126349)]
- [2025] **Monitoring and Observability of Machine Learning Systems: Current Practices and Gaps** [[paper](https://arxiv.org/abs/2510.24142)]
- [2025] **Validating Alerts in Cloud-Native Observability** [[paper](https://arxiv.org/abs/2510.23970)]
- [2025] **Interoperability From OpenTelemetry to Kieker: Demonstrated as Export from the Astronomy Shop** [[paper](https://arxiv.org/abs/2510.11179)]
- [2025] **Task-Aware Reduction for Scalable LLM-Database Systems** [[paper](https://arxiv.org/abs/2510.11813)]
- [2025] **Crossing the scales: Single-neuron recruitment and continuous cortical propagation of slow wave events revealed by integrative opto-magnetic imaging** *NeuroImage* [[paper](https://doi.org/10.1016/j.neuroimage.2025.121513)]
- [2025] **Towards a user-centric HPC-QC environment** [[paper](https://arxiv.org/abs/2509.20525)]
- [2025] **A Grey Literature Review of AI-Native Applications** [[paper](https://arxiv.org/abs/2509.13144)]
- [2025] **CRACI: A Cloud-Native Reference Architecture for the Industrial Compute Continuum** [[paper](https://arxiv.org/abs/2509.07498)]
- [2025] **UniSage: A Unified and Post-Analysis-Aware Sampling for Microservices** [[paper](https://arxiv.org/abs/2509.26336)]
- [2025] **Explain and Monitor Deep Learning Models for Computer Vision using Obz AI** [[paper](https://arxiv.org/abs/2508.18188)]
- [2025] **A Review of Generative AI and DevOps Pipelines: CI/CD, Agentic Automation, MLOps Integration, and Large Language Models** *PPR* [[paper](https://doi.org/10.20944/preprints202506.1040.v1)]
- [2025] **IDEAL-Enhanced DevOps: A Structured Framework for Continuous Improvement in Software Engineering** *PPR* [[paper](https://doi.org/10.20944/preprints202503.1031.v1)]
- [2025] **Enterprise Architecture in the Digital Era: A Comprehensive Review of Academic Progress and Industry Implementation** *PPR* [[paper](https://doi.org/10.20944/preprints202510.0314.v1)]

[⬆ Back to top](#paper-list)

### Code Quality

#### Method

##### 2026

- [2026] **Accelerating Accurate Assignment Authoring Using Solution-Generated Autograders** [[paper](https://arxiv.org/abs/2608.06572)]
- [2026] **ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning** [[paper](https://arxiv.org/abs/2608.14352)]
- [2026] **Unethical Ways to Manage Technical Debt** *Queue* [[paper](https://doi.org/10.1145/3830399)]
- [2026] **TestMiner: Software Testing Analysis for GitHub Repositories** [[paper](https://arxiv.org/abs/2607.12223)] [[project](https://andrehora.github.io/testminer)]
- [2026] **(Over)Reliance on Test Agents in AI-Assisted Software Testing** [[paper](https://arxiv.org/abs/2607.17927)]
- [2026] **Faithful Autoformalization of Natural Language Assertions** [[paper](https://arxiv.org/abs/2607.13303)]
- [2026] **From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants** [[paper](https://arxiv.org/abs/2607.11387)]
- [2026] **Benchmarking Quantum Software Testing with Scalable Quantum Programs** [[paper](https://arxiv.org/abs/2607.02029)]
- [2026] **An Exploration of Agentic Information Fusion for Test Maintenance Prediction** [[paper](https://arxiv.org/abs/2607.04786)]
- [2026] **On the risk of coding before testing: An empirical study on LLM-based test generation workflow** [[paper](https://arxiv.org/abs/2607.05139)]
- [2026] **Complexity Theory of Randomised Testing** [[paper](https://arxiv.org/abs/2607.11811)]
- [2026] **AI-Driven Software Testing: A Review** *Big Data and Cognitive Computing* [[paper](https://doi.org/10.3390/bdcc10070233)]
- [2026] **Software Testing Techniques: A Review Paper** *International Journal of Scientific Engineering and Research* [[paper](https://doi.org/10.70729/se26721153224)]
- [2026] **From Custom Logic to APIs: Understanding and Recommending API Replacement Refactorings** [[paper](https://arxiv.org/abs/2606.06912)]
- [2026] **Humor in Software Testing Education** [[paper](https://arxiv.org/abs/2606.21682)]
- [2026] **Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing** [[paper](https://arxiv.org/abs/2606.08806)]
- [2026] **Learning Critical Testing Literacy Through Puzzles: an Experience Report** [[paper](https://arxiv.org/abs/2606.20129)]
- [2026] **Characterizing Tests in IoT Software: Practices, Challenges and Opportunities** [[paper](https://arxiv.org/abs/2606.12592)]
- [2026] **AI-Driven Test Case Generation from Natural Language Requirements: A Survey of Techniques and Research Gaps** [[paper](https://arxiv.org/abs/2606.06563)]
- [2026] **Metaheuristic optimization of ML for software testing defect prediction: a systematic review and critical analysis of methods, datasets, and research gaps** *Evolutionary Intelligence* [[paper](https://doi.org/10.1007/s12065-026-01225-z)]
- [2026] **Prescriptive and Contextual Technical Debt Management with LLM and SonarQube** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20551293)]
- [2026] **Exploring the Output of Software Testing Tools through a Visual Comparative Analysis** [[paper](https://arxiv.org/abs/2605.04189)]
- [2026] **Robust Mutation Analysis of Quantum Programs Under Noise** [[paper](https://arxiv.org/abs/2605.13279)]
- [2026] **PITMuS: A Tool for Automated Bug Dataset Generation via Source-Level Mutant Reconstruction** [[paper](https://arxiv.org/abs/2605.21930)]
- [2026] **ClozeMaster: Fuzzing Rust Compiler by Harnessing LLMs for Infilling Masked Real Programs** [[paper](https://arxiv.org/abs/2605.00413)]
- [2026] **LLM-Based Static Verification of Code Against Natural-Language Requirements: An Industrial Experience Report** [[paper](https://arxiv.org/abs/2605.17926)]
- [2026] **System Test Generation for Virtual Reality Applications using Scenario Models** [[paper](https://arxiv.org/abs/2605.07534)]
- [2026] **VISOR: A Vision-Language Model-based Test Oracle for Testing Robots** [[paper](https://arxiv.org/abs/2605.10408)]
- [2026] **Inverting the Shield: Systematically Generating Safety Tests from Policy Specifications** [[paper](https://arxiv.org/abs/2605.24883)] [[code](https://github.com/huac-lxy/POLARIS)]
- [2026] **FeedbackLLM: Metadata driven Multi-Agentic Language Agnostic Test Case Generator with Evolving prompt and Coverage Feedback** [[paper](https://arxiv.org/abs/2605.01264)]
- [2026] **NOETHER: A Constructive Framework for Metamorphic Pattern Discovery from Operator Algebras** [[paper](https://arxiv.org/abs/2605.17390)]
- [2026] **Randomized and Diverse Input State Generation for Quantum Program Testing** [[paper](https://arxiv.org/abs/2605.03957)]
- [2026] **Conceptualizing alternative training and education in computer science: a scoping review of coding bootcamps** *Computer Science Education* [[paper](https://doi.org/10.1080/08993408.2026.2646155)]
- [2026] **Supervised Machine Learning for Technical Debt in Python: Analysis and Prediction** *Machine Learning and Knowledge Extraction* [[paper](https://doi.org/10.3390/make8050118)]
- [2026] **Applications of Causality in Software Testing: A Rapid Review** [[paper](https://arxiv.org/abs/2606.15683)]
- [2026] **Software Testing Beyond Closed Worlds: Open-World Games as an Extreme Case** [[paper](https://arxiv.org/abs/2604.04047)]
- [2026] **QMutBench: A Dataset of Quantum Circuit Mutants** [[paper](https://arxiv.org/abs/2604.15870)]
- [2026] **Teaching testing seriously in academia** [[paper](https://arxiv.org/abs/2606.15677)]
- [2026] **Enhancing Large Language Models with Retrieval Augmented Generation for Software Testing and Inspection Automation** [[paper](https://arxiv.org/abs/2604.15270)]
- [2026] **SHIFT: Sigmoid-Based Heuristic Invertible Fitness-Landscape Transformation for Accelerating SBST** [[paper](https://arxiv.org/abs/2604.09171)]
- [2026] **LLMs taking shortcuts in test generation: A study with SAP HANA and LevelDB** [[paper](https://arxiv.org/abs/2604.14437)]
- [2026] **FLARE: Agentic Coverage-Guided Fuzzing for LLM-Based Multi-Agent Systems** [[paper](https://arxiv.org/abs/2604.05289)]
- [2026] **Ising-based Test Optimization and Benchmarking** [[paper](https://arxiv.org/abs/2604.10450)] [[code](https://github.com/WSE-Lab/IsingBench)]
- [2026] **Sustainability Analysis of Prompt Strategies for SLM-based Automated Test Generation** [[paper](https://arxiv.org/abs/2604.02761)]
- [2026] **MR-Coupler: Automated Metamorphic Test Generation via Functional Coupling Analysis** [[paper](https://arxiv.org/abs/2604.10126)]
- [2026] **ExplainFuzz: Explainable and Constraint-Conditioned Test Generation with Probabilistic Circuits** [[paper](https://arxiv.org/abs/2604.06559)]
- [2026] **TestDecision: Sequential Test Suite Generation via Greedy Optimization and Reinforcement Learning** [[paper](https://arxiv.org/abs/2604.01799)]
- [2026] **Artifact Repository for A Methodological Analysis of Empirical Studies in Quantum Software Testing** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18159892)]
- [2026] **Challenges in Testing Large Language Model Based Software: A Faceted Taxonomy** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3806396)]
- [2026] **An Agent-Based Approach to Automating Software Performance Testing (Work In Progress Paper)** [[paper](https://doi.org/10.1145/3777911.3801107)]
- [2026] **Replication package for 'The Effect of Complexity and Provenance on Code Review Decisions: Evidence from a Controlled Experiment'** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19685702)]
- [2026] **YOLOv8 to YOLO11 Performance Benchmark and Comprehensive Architectural Comparative Review** *Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)* [[paper](https://arxiv.org/abs/2501.13400)]
- [2026] **Self‐Admitted Technical Debt Detection Approaches: A Decade Systematic Review** *Journal of Software Evolution and Process* [[paper](https://arxiv.org/abs/2312.15020)]
- [2026] **Can Language Models Pass Software Testing Certification Exams? a case study** [[paper](https://arxiv.org/abs/2603.23142)]
- [2026] **Generative AI in Software Testing: Current Trends and Future Directions** [[paper](https://arxiv.org/abs/2603.02141)]
- [2026] **ISTQB Certifications Under the Lens: Their Contributions to the Software-Testing Profession; and AI-assisted Synthesis of Practitioners' Endorsements and Criticisms** [[paper](https://arxiv.org/abs/2603.14572)]
- [2026] **From Natural Language to Executable Properties for Property-based Testing of Mobile Apps** [[paper](https://arxiv.org/abs/2603.21263)]
- [2026] **Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing** [[paper](https://arxiv.org/abs/2603.08616)]
- [2026] **TestAgentX: Leveraging Large Language Models and Reinforcement Learning for Scalable and Adaptive Software Testing** [[paper](https://doi.org/10.1109/nqcomp68334.2026.11497649)]
- [2026] **A systematic review of methods for interpreting building code regulations in automated compliance systems** *Building Research & Information* [[paper](https://doi.org/10.1080/09613218.2026.2637965)]
- [2026] **Sentiment analysis for code-mixed low-resource languages: a systematic review of approaches, techniques, applications, challenges, and future directions** *Social Network Analysis and Mining* [[paper](https://doi.org/10.1007/s13278-026-01588-2)]
- [2026] **Non-coding RNA biomarkers in resistant hypertension: a scoping review** *Frontiers in Molecular Biosciences* [[paper](https://doi.org/10.3389/fmolb.2026.1786399)]
- [2026] **Human Rights Protections and Ethical Governance in Global Psychiatry: A Cross-National Review of Ethical Codes from Member Societies of the World Psychiatric Association** *Psychiatry International* [[paper](https://doi.org/10.3390/psychiatryint7020050)]
- [2026] **Vibe-coding as a Teaching Competency in the Use of Artificial Intelligence for Medical Education: A Scoping Review** *Revista Española de Educación Médica* [[paper](https://doi.org/10.6018/edumed.705121)]
- [2026] **Detection of Technical Debt in Java Source Code** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3801745)]
- [2026] **Technical Debt Analysis as an Approach to Identifying Curriculum Deficiencies in Software Engineering Education** [[paper](https://doi.org/10.1109/infoteh68759.2026.11477672)]
- [2026] **Management of Technical Debt in Startups: A Systematic Mapping** *Journal of Software Engineering Research and Development* [[paper](https://doi.org/10.5753/jserd.2026.5462)]
- [2026] **SACS: A Code Smell Dataset using Semi-automatic Generation Approach** [[paper](https://arxiv.org/abs/2602.15342)]
- [2026] **Before Autonomy Takes Control: Software Testing in Robotics** [[paper](https://arxiv.org/abs/2602.02293)]
- [2026] **What Do Contribution Guidelines Say About Software Testing?** [[paper](https://arxiv.org/abs/2602.02966)]
- [2026] **Search-Based Quantum Program Testing via Commuting Pauli String** [[paper](https://arxiv.org/abs/2602.11487)]
- [2026] **Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions** [[paper](https://arxiv.org/abs/2602.10522)]
- [2026] **ATTest: Agent-Driven Tensor Testing for Deep Learning Library Modules** [[paper](https://arxiv.org/abs/2602.13987)] [[code](https://github.com/iSEngLab/ATTest.git)]
- [2026] **DeCEAT: Decoding Carbon Emissions for AI-driven Software Testing** [[paper](https://arxiv.org/abs/2602.18012)]
- [2026] **Every Maintenance Has Its Exemplar: The Future of Software Maintenance through Migration** [[paper](https://arxiv.org/abs/2602.14046)]
- [2026] **Can We Classify Flaky Tests Using Only Test Code? An LLM-Based Empirical Study** [[paper](https://arxiv.org/abs/2602.05465)]
- [2026] **Test vs Mutant: Adversarial LLM Agents for Robust Unit Test Generation** [[paper](https://arxiv.org/abs/2602.08146)]
- [2026] **Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting** [[paper](https://arxiv.org/abs/2602.12256)]
- [2026] **Context-Aware Code Review Automation: A Retrieval-Augmented Approach** *Applied Sciences* [[paper](https://doi.org/10.3390/app16041875)]
- [2026] **Review on Modulation Formats and Channel Coding in Free Space Optical Communication: Selection Criteria, Trade-Offs, and Emerging Trends** *Journal of Lightwave Technology* [[paper](https://doi.org/10.1109/jlt.2026.3664749)]
- [2026] **Research progress on long non‑coding RNAs in lung cancer (Review)** *Molecular Medicine Reports* [[paper](https://doi.org/10.3892/mmr.2026.13827)]
- [2026] **Coupling methods between Monte Carlo and computational fluid dynamics codes for nuclear reactor analysis: A systematic literature review** *Progress in Nuclear Energy* [[paper](https://doi.org/10.1016/j.pnucene.2026.106325)]
- [2026] **Non-Coding RNA-Based Therapeutic Strategies in Triple-Negative Breast Cancer: A Systematic Review** *International Journal of Molecular Sciences* [[paper](https://doi.org/10.3390/ijms27041882)]
- [2026] **"Technical Debt survey"** *IEEE DataPort* [[paper](https://doi.org/10.21227/2h3e-4h76)]
- [2026] **The Rise of Agentic Testing: Multi-Agent Systems for Robust Software Quality Assurance** [[paper](https://arxiv.org/abs/2601.02454)]
- [2026] **Prompt-Based REST API Test Amplification in Industry: An Experience Report** [[paper](https://arxiv.org/abs/2601.17903)]
- [2026] **Usage, Effects and Requirements for AI Coding Assistants in the Enterprise: An Empirical Study** [[paper](https://arxiv.org/abs/2601.20112)]
- [2026] **A Methodological Analysis of Empirical Studies in Quantum Software Testing** [[paper](https://arxiv.org/abs/2601.08367)]
- [2026] **MLIR-Smith: A Novel Random Program Generator for Evaluating Compiler Pipelines** [[paper](https://arxiv.org/abs/2601.02218)]
- [2026] **SWE-Tester: Training Open-Source LLMs for Issue Reproduction in Real-World Repositories** [[paper](https://arxiv.org/abs/2601.13713)]
- [2026] **Hybrid Concolic Testing with Large Language Models for Guided Path Exploration** [[paper](https://arxiv.org/abs/2601.12274)]
- [2026] **Human-Agent versus Human Pull Requests: A Testing-Focused Characterization and Comparison** [[paper](https://arxiv.org/abs/2601.21194)]
- [2026] **TAM-Eval: Evaluating LLMs for Automated Unit Test Maintenance** [[paper](https://arxiv.org/abs/2601.18241)] [[code](https://github.com/trndcenter/TAM-Eval)]
- [2026] **When Generic Prompt Improvements Hurt: Evaluation-Driven Iteration for LLM Applications** [[paper](https://arxiv.org/abs/2601.22025)]
- [2026] **On the Flakiness of LLM-Generated Tests for Industrial and Open-Source Database Management Systems** [[paper](https://arxiv.org/abs/2601.08998)]
- [2026] **ChiSA: Static Analysis for Lightweight Chisel Verification.** *Proc. ACM Program. Lang.* [[paper](https://dblp.org/rec/journals/pacmpl/CuiCZTL26)]
- [2026] **Automated Software Test Case Generation Using Directional Partially Weighted Ensemble Large Language Models With Retrieval-Augmented Generation (RAG)** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3667925)]
- [2026] **Leveraging AI-driven multi-agents for next-generation software testing: a lattice-based cross-industry automation framework** *International Journal of Information Technology* [[paper](https://doi.org/10.1007/s41870-025-03091-x)]
- [2026] **Network Analysis of Qualitative Data (NAQD): An Analytic Framework and Software for Qualitative Data Science Visualization and Hypothesis Testing** *International Journal of Qualitative Methods* [[paper](https://doi.org/10.1177/16094069261439942)]
- [2026] **Using Transformer and GAN Models for Software and Security Testing** *Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences* [[paper](https://doi.org/10.24251/hicss.2026.831)]
- [2026] **Hard-to-Find Bugs in Public-Key Cryptographic Software: Classification and Test Methodologies** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-16342-4_19)]
- [2026] **Replication package for the paper "An Agent-Based Approach to Automating Software Performance Testing (Work In Progress Paper)"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18344041)]
- [2026] **MSTDP: a multi-scale temporal deep learning framework for just-in-time software defect prediction with cross-attention fusion** *Journal of King Saud University - Computer and Information Sciences* [[paper](https://doi.org/10.1007/s44443-025-00401-y)]
- [2026] **Software Testing Techniques and Strategies** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21604706)]
- [2026] **Software Testing in the Quantum World** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.13996)]
- [2026] **An In-Depth Survey of Software Testing Methodologies** *International Journal of Scientific Research in Computer Science Engineering and Information Technology* [[paper](https://doi.org/10.32628/cseit261210)]
- [2026] **A Survey on Modern Techniques in Software Testing** *International Journal for Research in Applied Science and Engineering Technology* [[paper](https://doi.org/10.22214/ijraset.2026.76900)]
- [2026] **[SOK] Large Language Models in Security Code Review and Testing** *Journal of Systems Research* [[paper](https://doi.org/10.5070/sr3.62177)]
- [2026] **Intelligent Code Review and Vulnerability Localization Based on Large-Scale Pre-Trained Language Models (LLM)** [[paper](https://doi.org/10.1109/iceaai68945.2026.11442374)]
- [2026] **Non-Coding RNA Profile in the Progression of Carotid Atherosclerosis: A Systematic Review** *International Journal of Molecular Sciences* [[paper](https://doi.org/10.3390/ijms27021002)]
- [2026] **Systematic literature review on software code smell detection approaches** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112784)]
- [2026] **Bridging Languages in Healthcare: A Comprehensive Review of Multilingual and Code-Switched Chatbot Interactions** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3664257)]
- [2026] **The missing code in osseointegration: A genome-wide review of RNA sequencing in implant integration** *Journal of Prosthodontic Research* [[paper](https://doi.org/10.2186/jpr.jpr_d_25_00279)]
- [2026] **Source code vulnerability detection based on deep learning: a review** *Cybersecurity* [[paper](https://doi.org/10.1186/s42400-025-00518-7)]
- [2026] **Response Paper: A Critical Review of Sprengholz's <i>Public Preferences Regarding Slow Codes in Critical Care</i>** *Bioethics* [[paper](https://doi.org/10.1111/bioe.70073)]
- [2026] **Beyond Neurotrophins: A Proposed Neurotrophic–Epigenetic Axis Mediated by Non-Coding RNA Networks for Hericium erinaceus Bioactives—A Hypothesis-Driven Review** *International Journal of Molecular Sciences* [[paper](https://doi.org/10.3390/ijms27031269)]
- [2026] **A Practical Guide for Establishing a Technical Debt Management Process** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18325238)]
- [2026] **Communicating Shadow IT: Surfacing the socio-technical debt** *KTH Publication Database DiVA (KTH Royal Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:bth-29937)]
- [2026] **The Art of Technical Debt: Strategic Approaches to Code Maintenance** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18490506)]
- [2026] **Evolution of Technical Debt in Large-Scale Software Systems** *DiVA (Blekinge Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:bth-29845)]

##### 2025

- [2025] **An Empirical Framework for Evaluating Semantic Preservation Using Hugging Face** [[paper](https://arxiv.org/abs/2512.07983)]
- [2025] **Industry Expectations and Skill Demands in Quantum Software Testing** [[paper](https://arxiv.org/abs/2512.14861)]
- [2025] **Search-based Software Testing Driven by Domain Knowledge: Reflections and New Perspectives** [[paper](https://arxiv.org/abs/2512.10079)]
- [2025] **Reinforcement Learning Integrated Agentic RAG for Software Test Cases Authoring** [[paper](https://arxiv.org/abs/2512.06060)]
- [2025] **Fuzzing the brain: Automated stress testing for the safety of ML-driven neurostimulation** [[paper](https://arxiv.org/abs/2512.05383)]
- [2025] **Multi-Agent LLM Committees for Autonomous Software Beta Testing** [[paper](https://arxiv.org/abs/2512.21352)]
- [2025] **How Low Can You Go? The Data-Light SE Challenge** [[paper](https://arxiv.org/abs/2512.13524)] [[code](https://github.com/KKGanguly/NEO)]
- [2025] **LLMCFG-TGen: Using LLM-Generated Control Flow Graphs to Automatically Create Test Cases from Use Cases** [[paper](https://arxiv.org/abs/2512.06401)]
- [2025] **Engineering Non-Linear Decay Dynamics: Pulse-Level Control and Software-Defined Qubit Rescue on Superconducting Processors** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18067974)]
- [2025] **A Fuzzy Fermatean TOPSIS Approach for Ranking Parameters in Software Testing** *International Journal of Reliability Quality and Safety Engineering* [[paper](https://doi.org/10.1142/s0218539325500597)]
- [2025] **Leveraging Retrieval-augmented LLMs for Automated Test Case Generation from Software Requirements Specification** *International journal of intelligent engineering and systems* [[paper](https://doi.org/10.22266/ijies2026.0131.04)]
- [2025] **Exploring Application of AIGC in Software Testing** [[paper](https://doi.org/10.1145/3795154.3795312)]
- [2025] **A Systematic Literature Review of the Use of GenAI Assistants for Code Comprehension: Implications for Computing Education Research and Practice** *ACM Transactions on Computing Education* [[paper](https://arxiv.org/abs/2510.17894)]
- [2025] **Quishing - A Review of QR Code Attacks and a Framework Design for Safe Scanning** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-981-95-0681-1_24)]
- [2025] **Common Patterns and Pedagogical Implications of Code-Switching and Code-Mixing in Multilingual Learners: A Systematic Literature Review** *Langkawi Journal of The Association for Arabic and English* [[paper](https://doi.org/10.31332/lkw.v11i2.11740)]
- [2025] **From Counsel to Code: Implications of AI Dependency for Authentic Human Bonds – A Systematic Review** *Premier Journal of Artificial Intelligence* [[paper](https://doi.org/10.70389/pjai.100020)]
- [2025] **Explainable Multilingual Sentiment Analysis for Sinhala, English and Code-Mixed Banking Reviews** [[paper](https://doi.org/10.1109/icac69156.2025.11361448)]
- [2025] **AI-Assisted Code Editors with Real-Time Collaboration: A Comprehensive Review** *INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* [[paper](https://doi.org/10.55041/ijsrem55648)]
- [2025] **The role of long non-coding RNAs in breast cancer drug resistance: a comprehensive review** *Journal of Translational Genetics and Genomics* [[paper](https://doi.org/10.20517/jtgg.2025.67)]
- [2025] **Managing technical debt across large-scale control systems** *JACOW* [[paper](https://doi.org/10.18429/jacow-icalepcs2025-tubr002)]
- [2025] **RefAgent: A Multi-agent LLM-based Framework for Automatic Software Refactoring** [[paper](https://arxiv.org/abs/2511.03153)]
- [2025] **A Code Smell Refactoring Approach using GNNs** [[paper](https://arxiv.org/abs/2511.12069)]
- [2025] **An Agent-Based Framework for the Automatic Validation of Mathematical Optimization Models** [[paper](https://arxiv.org/abs/2511.16383)]
- [2025] **Empirical Derivations from an Evolving Test Suite** [[paper](https://arxiv.org/abs/2511.00915)]
- [2025] **Technical knowledge and soft skills in software startups within the Colombian entrepreneurial ecosystem** [[paper](https://arxiv.org/abs/2511.21769)]
- [2025] **Autonomous QA Agent: A Retrieval-Augmented Framework for Reliable Selenium Script Generation** [[paper](https://arxiv.org/abs/2601.06034)]
- [2025] **LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework** [[paper](https://arxiv.org/abs/2511.20403)]
- [2025] **Towards Comprehensive Sampling of SMT Solutions** [[paper](https://arxiv.org/abs/2511.10326)]
- [2025] **Artificial Intelligence in Software Testing: A Systematic Review of a Decade of Evolution and Taxonomy** *Algorithms* [[paper](https://doi.org/10.3390/a18110717)]
- [2025] **A Metaheuristic and Neural Network-Based Framework for Automated Software Test Oracles Under Limited Test Data Conditions** *Journal of Electronic Testing* [[paper](https://doi.org/10.1007/s10836-025-06210-5)]
- [2025] **Topics, Trends, and Sentiments in Software Testing: An Analysis of Developers’ Engagement on Stack Overflow** *International Journal of Computer and Information Technology(2279-0764)* [[paper](https://doi.org/10.24203/dfjd8332)]
- [2025] **OSSAPTestingPlus: A Blockchain-Based Collaborative Framework for Enhancing Trust and Integrity in Distributed Agile Testing of Archaeological Photogrammetry Open-Source Software** *Information* [[paper](https://doi.org/10.3390/info16110992)]
- [2025] **Cost analysis of enhanced software reliability model with Weibull testing effort function using simulated annealing** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-25841-4)]
- [2025] **Design and Usability Testing of a Novel Internet-Delivered Cognitive Behavioral Therapy (iCBT) Software Platform for Children with Anxiety** *Children* [[paper](https://doi.org/10.3390/children12111535)]
- [2025] **stgem: A software library to develop falsification and test generation tools for cyber-physical systems using generative models** *Science of Computer Programming* [[paper](https://doi.org/10.1016/j.scico.2025.103412)]
- [2025] **Retrospective Review of the Criminal Code Review Board in Quebec for the Year 2023** *Forensic Sciences* [[paper](https://doi.org/10.3390/forensicsci5040059)]
- [2025] **Non-Coding RNAs (microRNAs, lncRNAs, circRNAs) in Adenomyosis: A Systematic Review of Mechanistic and Translational Evidence** *International Journal of Molecular Sciences* [[paper](https://doi.org/10.3390/ijms262110713)]
- [2025] **Grid code requirements for the integration of renewable energy sources in Indonesia—a review** *Renewable energy focus* [[paper](https://doi.org/10.1016/j.ref.2025.100782)]
- [2025] **Review of recent developments in grid codes: Focus on compliance testing and grid-forming inverter-based resources** *Renewable and Sustainable Energy Reviews* [[paper](https://doi.org/10.1016/j.rser.2025.116509)]
- [2025] **Stakeholder perspectives on the comprehensive review of the IMO STCW convention and code** *Australian Journal of Maritime & Ocean Affairs* [[paper](https://doi.org/10.1080/18366503.2025.2589597)]
- [2025] **Shear strengthening of two-way reinforced concrete slabs with openings: A review of strengthening techniques and code perspectives** *Results in Engineering* [[paper](https://doi.org/10.1016/j.rineng.2025.108059)]
- [2025] **Assessing the prognostic value of long non-coding RNAs in glioblastoma patients: findings from a systematic review and meta-analysis** *Cancer Cell International* [[paper](https://doi.org/10.1186/s12935-025-04051-y)]
- [2025] **A comparative review on recent research, recommendation, standard and code for large liquid storage tanks under seismic excitation** *Results in Engineering* [[paper](https://doi.org/10.1016/j.rineng.2025.108039)]
- [2025] **Large Language Model for Verilog Code Generation: Literature Review and the Road Ahead** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202511.0656.v2)]
- [2025] **Non‑coding RNAs in epithelial‑mesenchymal transition of renal cell carcinoma (Review)** *Molecular Medicine Reports* [[paper](https://doi.org/10.3892/mmr.2025.13761)]
- [2025] **Technical Debt in the Age of Artificial Intelligence and Methods of Its Forecasting** *International Journal of Science and Research (IJSR)* [[paper](https://doi.org/10.21275/sr251106165316)]
- [2025] **Software Testing with Large Language Models: An Interview Study with Practitioners** [[paper](https://arxiv.org/abs/2510.17164)]
- [2025] **Agentic RAG for Software Testing with Hybrid Vector-Graph and Multi-Agent Orchestration** [[paper](https://arxiv.org/abs/2510.10824)]
- [2025] **Harnessing the Power of Large Language Models for Software Testing Education: A Focus on ISTQB Syllabus** [[paper](https://arxiv.org/abs/2510.22318)]
- [2025] **Enhancing Software Testing Education: Understanding Where Students Struggle** [[paper](https://arxiv.org/abs/2510.00957)]
- [2025] **Beyond Pass/Fail: The Story of Learning-Based Testing** [[paper](https://arxiv.org/abs/2510.00450)]
- [2025] **LLMs are All You Need? Improving Fuzz Testing for MOJO with Large Language Models** [[paper](https://arxiv.org/abs/2510.10179)]
- [2025] **Fuzz Smarter, Not Harder: Towards Greener Fuzzing with GreenAFL** [[paper](https://arxiv.org/abs/2510.25665)]
- [2025] **GenIA-E2ETest: A Generative AI-Based Approach for End-to-End Test Automation** [[paper](https://arxiv.org/abs/2510.01024)]
- [2025] **Software Testing Education and Industry Needs - Report from the ENACTEST EU Project** [[paper](https://arxiv.org/abs/2510.14625)]
- [2025] **Reduction of Test Re-runs by Prioritizing Potential Order Dependent Flaky Tests** [[paper](https://arxiv.org/abs/2510.26171)]
- [2025] **Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework** [[paper](https://arxiv.org/abs/2510.05365)]
- [2025] **On Interaction Effects in Greybox Fuzzing** [[paper](https://arxiv.org/abs/2510.19984)]
- [2025] **How Students Use Generative AI for Software Testing: An Observational Study** [[paper](https://arxiv.org/abs/2510.10551)]
- [2025] **The Cost of Certainty: Shot Budgets in Quantum Program Testing** [[paper](https://arxiv.org/abs/2510.22418)]
- [2025] **Clarifying Semantics of In-Context Examples for Unit Test Generation** [[paper](https://arxiv.org/abs/2510.01994)]
- [2025] **A two-phase TOE framework integrating SEM and ANN for evaluating cloud computing adoption in software testing** *Technological Forecasting and Social Change* [[paper](https://doi.org/10.1016/j.techfore.2025.124371)]
- [2025] **The software testing community and IT stereotypes: a study with industry professionals** *Interacting with Computers* [[paper](https://doi.org/10.1093/iwc/iwaf047)]
- [2025] **Extending Test-driven development to Softwarized Networks and Intent Based Networking** [[paper](https://doi.org/10.23919/cnsm67658.2025.11297527)]
- [2025] **Human-in-the-Loop Intelligent Testing for Safety-Critical Software** [[paper](https://doi.org/10.1109/issrew67781.2025.00068)]
- [2025] **Initial Functionality Test of a Future Airport Surveillance Radar Using Software-Defined Radio** [[paper](https://doi.org/10.23919/isap63122.2025.11362223)]
- [2025] **Software Testing and Quality Assurance** [[paper](https://doi.org/10.63282/3050-9246/icrtcsit-119)]
- [2025] **Rapid Software Testing Methodology** [[paper](https://doi.org/10.1002/9781394319749.part2)]
- [2025] **Application of Artificial Intelligence in Software Testing** [[paper](https://doi.org/10.1109/sccc67219.2025.11420727)]
- [2025] **Breaking Task Isolation: Enhancing Code Review Automation with Mixture-of-Experts Large Language Models** [[paper](https://doi.org/10.1109/issre66568.2025.00033)]
- [2025] **Hydra-Reviewer: A Holistic Multi-Agent System for Automatic Code Review Comment Generation** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3621462)]
- [2025] **Impact of Stroke Code Activation on Functional Outcomes and the Role of Nursing in Neurorehabilitation: A Systematic Review** *Neurology International* [[paper](https://doi.org/10.3390/neurolint17110175)]
- [2025] **Advances in exosomal non‑coding RNAs in cervical cancer (Review)** *Molecular and Clinical Oncology* [[paper](https://doi.org/10.3892/mco.2025.2899)]
- [2025] **Causes and Consequences of Medical Coding Errors: A Systematic Review of the Literature** *Journal of Posthumanism* [[paper](https://doi.org/10.63332/joph.v4i3.3576)]
- [2025] **Accuracy of Diagnostic Codes and Algorithms Used to Identify Rheumatoid Arthritis and Juvenile Idiopathic Arthritis in Administrative Claims and Electronic Health Records: Systematic Review and Meta‐Analysis** *Arthritis Care & Research* [[paper](https://doi.org/10.1002/acr.25662)]
- [2025] **Technical Debt Is Killing Digital Transformation, But There Is a Way Out** *California Management Review* [[paper](https://doi.org/10.1177/00081256251370795)]
- [2025] **Automated Technical Debt Assessment In Legacy Banking Applications** *International Journal of Computational and Experimental Science and Engineering* [[paper](https://doi.org/10.22399/ijcesen.4065)]
- [2025] **DebtGuard: A Predictive Model For Managing Technical Debt In Agile Development** *Egyptian Informatics Journal* [[paper](https://doi.org/10.1016/j.eij.2025.100806)]
- [2025] **Unadmitted Technical Debt: Dataset and Detection Approaches** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3623644)]
- [2025] **Predicting software developer sentiment on self-admitted technical debt** *PeerJ Computer Science* [[paper](https://doi.org/10.7717/peerj-cs.3227)]
- [2025] **Large Language Models for Software Testing: A Research Roadmap** [[paper](https://arxiv.org/abs/2509.25043)]
- [2025] **AutoStub: Genetic Programming-Based Stub Creation for Symbolic Execution** [[paper](https://arxiv.org/abs/2509.08524)]
- [2025] **TPSQLi: Test Prioritization for SQL Injection Vulnerability Detection in Web Applications** [[paper](https://arxiv.org/abs/2509.10920)]
- [2025] **Leveraging SystemC-TLM-based Virtual Prototypes for Embedded Software Fuzzing** [[paper](https://arxiv.org/abs/2509.01318)]
- [2025] **TISSEA: A Framework for Testing IoT Systems Based on Technical Software Engineering Aspects** *IEEE Internet of Things Journal* [[paper](https://doi.org/10.1109/jiot.2025.3609240)]
- [2025] **Testing the Untestable? An Empirical Study on the Testing Process of LLM-Powered Software Systems** [[paper](https://doi.org/10.1109/scam67354.2025.00015)]
- [2025] **Automated Test Case Generation from Unstructured Software Requirements Using Advanced NLP Techniques** [[paper](https://doi.org/10.1109/icrito66076.2025.11241453)]
- [2025] **Research on Applying DOE in Software Testing** [[paper](https://doi.org/10.1145/3773365.3773604)]
- [2025] **Integrating RAG and LLM for Automated Code Review in Practice** [[paper](https://doi.org/10.1109/iscipt67144.2025.11265531)]
- [2025] **Building a Dataset for Combined Classification of Source Code Reviews** *Pattern Recognition and Image Analysis* [[paper](https://doi.org/10.1134/s1054661825700336)]
- [2025] **Automatic Code Generation Techniques: A Systematic Literature Review** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00551-3)]
- [2025] **Unveiling the Relationship Between Continuous Integration and Code Review: A Study with 10 Closed-source Projects** [[paper](https://doi.org/10.5753/sbes.2025.9965)]
- [2025] **Non-coding RNAs as diagnostic biomarkers for preeclampsia: a systematic review and meta-analysis** *BMC Pregnancy and Childbirth* [[paper](https://doi.org/10.1186/s12884-025-08116-8)]
- [2025] **Metamorphic Testing of Deep Code Models: A Systematic Literature Review** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3766552)]
- [2025] **Identification of idiopathic inflammatory myopathy research cohorts using international classification of disease (ICD) codes: A systematic review** *Seminars in Arthritis and Rheumatism* [[paper](https://doi.org/10.1016/j.semarthrit.2025.152830)]
- [2025] **A Comprehensive Review of Recent Progress in Quantum Error Correction: Codes, Decoders, and Fault-Tolerant Architectures** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202509.1037.v1)]
- [2025] **Accuracy of Suicidal Behaviors in Administrative Data as Measured by <i>International Classification of Diseases, Tenth Revision</i> –Based Codes, 2000-2024: A Rapid Review** *Public Health Reports* [[paper](https://doi.org/10.1177/00333549251350843)]
- [2025] **Interleaving Large Language Models for Compiler Testing** [[paper](https://arxiv.org/abs/2508.18955)]
- [2025] **Rethinking Testing for LLM Applications: Characteristics, Challenges, and a Lightweight Interaction Protocol** [[paper](https://arxiv.org/abs/2508.20737)]
- [2025] **Enhancing Software Quality Assurance: A Dual Approach to Automated and Human Testing for Web Applications** [[paper](https://doi.org/10.31224/5204)]
- [2025] **Assessing the Validity and Reliability of a Critical Thinking Test for Electrical Engineering Students Using Automation Studio Software** *TEM Journal* [[paper](https://doi.org/10.18421/tem143-60)]
- [2025] **A Review of Vulnerability Detection Algorithms in Software Code** *Indonesian Journal of Computer Science* [[paper](https://doi.org/10.33022/ijcs.v14i4.4972)]
- [2025] **Non-coding RNAs in chronic lymphocytic leukemia: A systematic review and meta-analysis to decode the diagnostic potential** *Molecular and Cellular Probes* [[paper](https://doi.org/10.1016/j.mcp.2025.102048)]

##### 2024

- [2024] **Enchanting Program Specification Synthesis by Large Language Models Using Static Analysis and Program Verification.** *CAV* [[paper](https://dblp.org/rec/conf/cav/WenCSXQHLCT24)]

##### 2018

- [2018] **Relational Program Reasoning Using Compiler IR - Combining Static Verification and Dynamic Analysis.** *J. Autom. Reason.* [[paper](https://dblp.org/rec/journals/jar/KieferKU18)]

##### 2017

- [2017] **Static analysis of functional programs with an application to the frame problem in deductive verification. (Analyse statique de programmes fonctionnels avec une application au problème du frame dans le domaine de la vérification déductive).** [[paper](https://dblp.org/rec/phd/hal/Andreescu17)]

##### 2016

- [2016] **Verification of Programmable Logic Controller Code using Model Checking and Static Analysis.** [[paper](https://dblp.org/rec/phd/dnb/Biallas16)]

##### 2015

- [2015] **Static Analysis and Verification of Aerospace Software by Abstract Interpretation.** *Found. Trends Program. Lang.* [[paper](https://dblp.org/rec/journals/ftpl/BertraneCCFMMR15)]

##### 2014

- [2014] **Reducing the verification cost of evolving product families using static analysis techniques.** *Sci. Comput. Program.* [[paper](https://dblp.org/rec/journals/scp/SabouriK14)]

##### 2012

- [2012] **Program slicing enhances a verification technique combining static and dynamic analysis.** *SAC* [[paper](https://dblp.org/rec/conf/sac/ChebaroKGJ12)]

##### 2010

- [2010] **Static Analysis, Abstract Interpretation and Verification in (Constraint Logic) Programming.** *25 Years GULP* [[paper](https://dblp.org/rec/conf/agp/DelzannoGR10)]

##### 2009

- [2009] **Static-Analysis Assisted Dynamic Verification of MPI Waitany Programs (Poster Abstract).** *PVM/MPI* [[paper](https://dblp.org/rec/conf/pvm/VakkalankaSVGKT09)]

##### 2008

- [2008] **A Security Domain Model for Static Analysis and Verification of Software Programs.** *SEKE* [[paper](https://dblp.org/rec/conf/seke/Shaffer08)]

##### 2007

- [2007] **Static Analysis of Dynamic Properties - Automatic Program Verification to Prove the Absence of Dynamic Runtime Errors.** *GI Jahrestagung* [[paper](https://dblp.org/rec/conf/gi/Wissing07)]

##### 2006

- [2006] **Software Verification: Infinite-State Model Checking and Static Program Analysis, 19.02. - 24.02.2006** *['Software Verification - Infinite-State Model Checking and Static Program Analysis', 'Dagstuhl Seminar Proceedings']* [[paper](https://dblp.org/rec/conf/dagstuhl/2006P6081)]
- [2006] **06081 Executive Summary -- Software Verification: Infinite-State Model Checking and Static Program Analysis.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/AbdullaBM06)]
- [2006] **06081 Abstracts Collection -- Software Verification: Infinite-State Model Checking and Static Program Analysis.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/AbdullaBM06a)]
- [2006] **Analysis of Dynamic Communicating Systems by Hierarchical Abstraction.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/BauerW06a)]
- [2006] **Lazy Shape Analysis.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/BeyerHT06)]
- [2006] **Reachability analysis of multithreaded software with asynchronous communication.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/BouajjaniESS06)]
- [2006] **Flat counter automata almost everywhere!.** *Software Verification - Infinite-State Model Checking and Static Program Analysis* [[paper](https://dblp.org/rec/conf/dagstuhl/LerouxS06)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **Technical Debt in the AI Era** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2026.3683173)]
- [2026] **Gamification in Software Testing** *OPUS (University of Passau)* [[paper](https://opus4.kobv.de/opus4-uni-passau/frontdoor/index/index/docId/2096)]
- [2026] **Ztrategic: Libraries and Tools For Software Language Specification, Transformation, and Testing - Artifact** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32162940)]
- [2026] **Unlocking the “Nuclear Energy Code” of the Ocean: A Review of Technologies for Uranium Recovery from Seawater** *Industrial & Engineering Chemistry Research* [[paper](https://doi.org/10.1021/acs.iecr.6c00056)]
- [2026] **An AI-Enhanced Technical Debt Management Framework for Aerospace and Defense Systems Engineering: Framework Design and Illustrative Application** *Systems* [[paper](https://doi.org/10.3390/systems14050591)]
- [2026] **Evolving Kubernetes: A Technical Debt Perspective** [[paper](https://doi.org/10.1145/3793302.3793335)]
- [2026] **“TODO: Fix the Mess Gemini Created”: Towards Understanding GenAI-Induced Self-Admitted Technical Debt** [[paper](https://doi.org/10.1145/3794915.3795777)]
- [2026] **Strategies Used by Software Leaders to Manage Technical Debt** *ScholarWorks (Walden University)* [[paper](https://scholarworks.waldenu.edu/dissertations/19886)]
- [2026] **Evaluating LLM-Based Test Generation Under Software Evolution** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2603.23443)]
- [2026] **Results of the 8th Intl. Competition on Software Testing (Test-Comp 2026)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18650772)]
- [2026] **Data preparation and quality for code-centric generative software engineering tasks: a systematic literature review** *Frontiers of Computer Science* [[paper](https://doi.org/10.1007/s11704-025-41376-3)]
- [2026] **A QUANTITATIVE ASSESSMENT OF THE IMPACT OF TECHNICAL DEBT ON THE SOFTWARE DEVELOPMENT LIFECYCLE** *Naukovyi visnyk Donetskoho natsionalnoho tekhnichnoho universytetu* [[paper](https://doi.org/10.31474/2415-7902-2026-1-16-27-37)]
- [2026] **Quantifying Architectural Technical Debt in Critical Digital Infrastructure: Development of the Architectural Technical Debt Index (ATDI)** *International Journal of Advances in Scientific Research and Engineering* [[paper](https://doi.org/10.31695/ijasre.2026.7.5)]
- [2026] **The Socio-Technical Debt Index: Quantifying the Friction of Engineering Dysfunction** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18158268)]
- [2026] **Reconceptualizing Technical Debt as an Organizational Security, Safety, and Sociotechnical Risk** *Safety and Security Advances* [[paper](https://doi.org/10.61093/ssa.2(1).37-52.2026)]

##### 2025

- [2025] **Advances in Managing Self-Admitted Technical Debt: A Review of NLP and Machine Learning Approaches** *Journal of Computational and Cognitive Engineering* [[paper](https://doi.org/10.47852/bonviewjcce52025975)]
- [2025] **Technical Debt in the Balance: The Role of Enterprise Architecture Management** *Journal of the Association for Information Systems* [[paper](https://aisel.aisnet.org/icis2025/isdesign/isdesign/3)]
- [2025] **Software Reliability Growth Model Combining Testing Effort Function and Burr-Type Fault Detection Rate** *Mathematics* [[paper](https://doi.org/10.3390/math13223633)]
- [2025] **Exact Inference for Quantum Circuits: A Testing Oracle for Quantum Software Stacks** [[paper](https://doi.org/10.1109/ase63991.2025.00203)]
- [2025] **KherveFitting: An Open Source Software for Fitting X‐Ray Photoelectron Spectroscopy Data** *Surface and Interface Analysis* [[paper](https://doi.org/10.1002/sia.70032)]
- [2025] **A dual perspective review on large language models and code verification** *Frontiers in Computer Science* [[paper](https://doi.org/10.3389/fcomp.2025.1655469)]
- [2025] **Faster Explicit-Trace Monitoring-Oriented Programming for Runtime Verification of Software Tests** *Proceedings of the ACM on Programming Languages* [[paper](https://doi.org/10.1145/3763183)]
- [2025] **Teachers’ Perspective on Software Testing Education** *ACM Transactions on Computing Education* [[paper](https://doi.org/10.1145/3772090)]
- [2025] **Beyond Static Analysis: Detecting SQL Injection via Context-Aware Code Review in Web Applications** [[paper](https://doi.org/10.1109/icocics68032.2025.11384074)]
- [2025] **Low-Code and No-Code Development in the Era of Artificial Intelligence: A Systematic Review** *Data & Metadata* [[paper](https://doi.org/10.56294/dm20251218)]
- [2025] **Fostering consumer sustainability trust by integrating blockchain-enabled reviews and QR code traceability systems in supply chain: a three-dimensional measurement scale development** *International Journal of Logistics Research and Applications* [[paper](https://doi.org/10.1080/13675567.2025.2574470)]
- [2025] **A Survey on LLM-based Code Generation for Low-Resource and Domain-Specific Programming Languages** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3770084)]
- [2025] **Software Fairness Testing in Practice** [[paper](https://doi.org/10.1109/icsme64153.2025.00012)]
- [2025] **Agile Software Architecture: Perceptions on Quality and Architectural Technical Debt Management** [[paper](https://doi.org/10.5753/sbcars.2025.11890)]
- [2025] **The Evolution of Technical Debt from DevOps to Generative AI: A multivocal literature review** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112599)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Replication package for ``Assessing Harmful Comments and Specificity in Code Review Feedback at Scale using Large Language Models''** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19382051)]
- [2026] **Reengineering of Simulation-based Digital Twin Toolchains for Automated Vehicles to Mitigate Technical Debt: A Case Study** [[paper](https://doi.org/10.1145/3786146.3788641)]
- [2026] **Software testing and their absence in research software** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18979055)]
- [2026] **Development and Field Testing of a UAS-Based Software-Defined Radar for Measuring Freshwater Bathymetry** *IEEE Transactions on Antennas and Propagation* [[paper](https://doi.org/10.1109/tap.2025.3642394)]
- [2026] **Enterprise Architecture as a Tool for Technical Debt Management in Public Universities: Contextual Challenges and Governance Opportunities** *The Electronic Journal of Information Systems in Developing Countries* [[paper](https://doi.org/10.1002/isd2.70051)]

##### 2025

- [2025] **Gene regulation by non-Coding RNAs in infertility: a mechanistic review** *Journal of Ovarian Research* [[paper](https://doi.org/10.1186/s13048-025-01862-5)]
- [2025] **WIP: Coding Neurodivergent - a Systematic Literature Review** [[paper](https://doi.org/10.1109/fie63693.2025.11328261)]
- [2025] **Technical Debt in Pull Requests: Insights from Apache Projects** *Journal of Software Engineering Research and Development* [[paper](https://doi.org/10.5753/jserd.2025.5722)]
- [2025] **Temporal Evolution of Architectural Complexity and Technical Debt in Microservices: An Exploratory Case Study** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-12089-2_18)]
- [2025] **Non-technical debt in games development research** *Proceedings of the International Conference on Information Systems Development* [[paper](https://doi.org/10.62036/isd.2025.9)]
- [2025] **bhuwanpaudel/Evolution-of-Technical-Debt-in-Monolithic-and-Hybrid-Microservice-Architecture: Exploring the Evolution of Technical Debt in Monolithic and Hybrid Microservice Architecture: An Industrial Case Study** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17618106)]
- [2025] **The Uneven Journey of AI in Software Testing: A Maturity Model for Industry Adoption** [[paper](https://doi.org/10.1109/cist65886.2025.11224099)]
- [2025] **Analysis of the Difficulties in Software Testing** *International Journal For Multidisciplinary Research* [[paper](https://doi.org/10.36948/ijfmr.2025.v07i05.58469)]
- [2025] **Conflicts of Interest in Infant and Young Child Feeding: A Review of Australian Health Professional Associations' Guidance to Members on the International Code of Marketing of Breast‐Milk Substitutes** *Maternal and Child Nutrition* [[paper](https://doi.org/10.1111/mcn.70137)]
- [2025] **A review of international grid codes for wind power integration** *Energy Conversion and Management X* [[paper](https://doi.org/10.1016/j.ecmx.2025.101278)]
- [2025] **Long Non-Coding RNAs in Psoriasis: A Comprehensive Review of Expression Profiles, Mechanistic Insights, Genetic Associations, and Their Clinical Implications** *Non-Coding RNA* [[paper](https://doi.org/10.3390/ncrna11050069)]
- [2025] **KinshipLR: software development and application for complex kinship testing in forensic genetics** *Forensic Science International* [[paper](https://doi.org/10.1016/j.forsciint.2025.112623)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **From AI Technical Debt to Agentic Technical Debt: A Systematic Mapping of Root Causes and Manifestations in Agentic AI Systems** [[paper](https://arxiv.org/abs/2608.01001)]
- [2026] **SmellCC: A Tool for Automated Code Smells Remediation** [[paper](https://arxiv.org/abs/2608.09477)]
- [2026] **Strategic Technical Debt: A Real Options Approach to Early-Stage Software Experimentation** [[paper](https://arxiv.org/abs/2608.16112)]
- [2026] **Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language** [[paper](https://arxiv.org/abs/2608.13029)]
- [2026] **Building AI-Intensive Software with AI: Early Results and a Cautionary Tale on Measuring Development Cost** [[paper](https://arxiv.org/abs/2608.13730)]
- [2026] **OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review** [[paper](https://arxiv.org/abs/2608.09290)] [[code](https://github.com/alibaba/open-code-review)]
- [2026] **AgentForge: An Immersive Role-Playing Platform for Learning Agentic Software Engineering** [[paper](https://arxiv.org/abs/2608.04148)]
- [2026] **COMMITGUARD: Differential Slice Fuzzing for Commit-Induced Bug Detection** [[paper](https://arxiv.org/abs/2608.17401)]
- [2026] **Comprehending Python Repetition Structures: An Eye-Tracking Study with Novice Developers** [[paper](https://arxiv.org/abs/2608.09875)]
- [2026] **On AI Safety and Security Technical Debt in Engineering AI-Enabled Systems** [[paper](https://arxiv.org/abs/2607.23365)]
- [2026] **Technical Debt Friction for Maintenance Prioritization: An Industrial Multi-Case Study** [[paper](https://arxiv.org/abs/2607.01850)]
- [2026] **Studying, Identifying, and Fixing Hidden Technical Debt in AI-Intensive Cyber-Physical Systems** [[paper](https://arxiv.org/abs/2608.02638)]
- [2026] **Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development** [[paper](https://arxiv.org/abs/2607.06101)]
- [2026] **Specification-Driven Development as the Foundation of AI-Native Enterprise Software Engineering** [[paper](https://arxiv.org/abs/2607.16680)]
- [2026] **Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects** [[paper](https://arxiv.org/abs/2607.12068)]
- [2026] **From Generic to Personalized: Exploring Persona-Aware Code Review Explanations** [[paper](https://arxiv.org/abs/2607.08990)]
- [2026] **Code Review is a Conversation: Toward Conversational AI Review Assistants** [[paper](https://arxiv.org/abs/2607.22095)]
- [2026] **From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality** [[paper](https://arxiv.org/abs/2607.13196)]
- [2026] **Is Agentic Code Review Helpful? Mining Developers' Feedback to CodeRabbit Reviews in the Wild** [[paper](https://arxiv.org/abs/2607.03316)]
- [2026] **Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review** [[paper](https://arxiv.org/abs/2607.24601)]
- [2026] **Archer: Towards Agentic Review for Compiler Optimizations** [[paper](https://arxiv.org/abs/2607.01808)]
- [2026] **Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment** [[paper](https://arxiv.org/abs/2607.16740)]
- [2026] **Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments** [[paper](https://arxiv.org/abs/2607.09524)]
- [2026] **"Go Home Copilot, You're Drunk": Understanding Developer Responses to Agent-Generated Code Review Comments** [[paper](https://arxiv.org/abs/2607.21997)]
- [2026] **3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse** [[paper](https://arxiv.org/abs/2607.07980)]
- [2026] **From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale** [[paper](https://arxiv.org/abs/2607.29516)]
- [2026] **SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review** [[paper](https://arxiv.org/abs/2607.06065)]
- [2026] **A Preliminary Study on Explaining Risk of Code Changes using LLM-Based Prediction Models** [[paper](https://arxiv.org/abs/2607.02782)]
- [2026] **Rethinking Training Data for Generating Code Review Comments** [[paper](https://arxiv.org/abs/2607.25851)]
- [2026] **Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis** [[paper](https://arxiv.org/abs/2607.05842)]
- [2026] **Personalized Assessments from Personal Artifacts** [[paper](https://arxiv.org/abs/2607.16494)]
- [2026] **TrustChain-Review: A Risk-Adaptive Blockchain and Game-Theoretic Framework for Trustworthy AI-Assisted Code Review** [[paper](https://arxiv.org/abs/2607.27310)]
- [2026] **Evaluation Bias and Epistemic Inequality in Global Software Development** [[paper](https://arxiv.org/abs/2607.12563)]
- [2026] **Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?** [[paper](https://arxiv.org/abs/2607.21656)]
- [2026] **Agents with Feelings? Personality and Emotion in Multi-Agent Software Teams** [[paper](https://arxiv.org/abs/2607.05659)]
- [2026] **Specifying the Delegated-Autonomy Boundary: Requirements Engineering for Agentic AI** [[paper](https://arxiv.org/abs/2607.17225)]
- [2026] **CommitLLM: A Fine-Tuned Pipeline for Git Commit Message Generation** [[paper](https://arxiv.org/abs/2607.17532)]
- [2026] **Faster Code, Deeper Debt? A Multivocal Literature Review on Technical Debt and Its Early Signs in LLM-Assisted Software Development** [[paper](https://arxiv.org/abs/2606.14796)]
- [2026] **A Preliminary Model for Managing Technical Debt in an Agile Environment** [[paper](https://arxiv.org/abs/2606.07859)]
- [2026] **Watts and Debts of Agentic Frameworks: An Empirical Study (Registered Report)** [[paper](https://arxiv.org/abs/2606.10702)]
- [2026] **Comparing ML-Specific and General Python Code Smells Across Project Characteristics** [[paper](https://arxiv.org/abs/2606.01882)]
- [2026] **Pomona: Continuous Code Quality Improvement via Small, Agentic Pull Requests at Bloomberg** [[paper](https://arxiv.org/abs/2606.06752)]
- [2026] **Qiskit Code Migration with LLMs** [[paper](https://arxiv.org/abs/2606.20173)]
- [2026] **Stakeholder Criteria in Technical Debt Decision-Making: A Practitioner-Informed Taxonomy** [[paper](https://arxiv.org/abs/2606.20935)]
- [2026] **Test Case Selection for Deep Neural Networks: A Replication Study on LLMs for Code** [[paper](https://arxiv.org/abs/2606.27601)]
- [2026] **Code Lifespan Survival Analysis (CLSA): Predicting the Survival of Source Code Lines Using AST-Aware Mining** [[paper](https://arxiv.org/abs/2606.04993)]
- [2026] **The End of Code Review: Coding Agents Supersede Human Inspection** [[paper](https://arxiv.org/abs/2606.13175)]
- [2026] **Same Scrutiny, More Time: Eye Tracking Insights into Reviewing LLM-Labelled Code** [[paper](https://arxiv.org/abs/2606.26505)]
- [2026] **Improving LLM-Based Go Code Review through Issue-List Generation and Context Augmentation** [[paper](https://arxiv.org/abs/2606.01859)]
- [2026] **CoRaCommit: A VS Code Extension for Commit Message Generation with Exemplar Retrieval** [[paper](https://arxiv.org/abs/2606.19814)]
- [2026] **TagDebt: A Bot to Support Technical Debt Management** [[paper](https://arxiv.org/abs/2605.29869)]
- [2026] **Beyond the Tip of the Iceberg: Understanding SATD in Dockerfiles through the Lens of Co-evolution** [[paper](https://arxiv.org/abs/2605.21238)]
- [2026] **The Dangers of Non-Self-Fixed Architecture Technical Debt and Its Impact on Time-to-Fix** [[paper](https://arxiv.org/abs/2605.16133)]
- [2026] **AI-Generated Smells: An Analysis of Code and Architecture in LLM and Agent-Driven Development** [[paper](https://arxiv.org/abs/2605.02741)]
- [2026] **Coding Agents Don't Know When to Act** [[paper](https://arxiv.org/abs/2605.07769)]
- [2026] **SkillOps: Managing LLM Agent Skill Libraries as Self-Maintaining Software Ecosystems** [[paper](https://arxiv.org/abs/2605.13716)]
- [2026] **From Code-Centric to Intent-Centric Software Engineering: A Reflexive Thematic Analysis of Generative AI, Agentic Systems, and Engineering Accountability** [[paper](https://arxiv.org/abs/2605.11027)]
- [2026] **DocSync: Agentic Documentation Maintenance via Critic-Guided Reflexion** [[paper](https://arxiv.org/abs/2605.02163)]
- [2026] **Rethinking Code Review in the Age of AI: A Vision for Agentic Code Review** [[paper](https://arxiv.org/abs/2605.17548)]
- [2026] **Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models** [[paper](https://arxiv.org/abs/2605.26100)]
- [2026] **These Aren't the Reviews You're Looking For How Humans Review AI-Generated Pull Requests** [[paper](https://arxiv.org/abs/2605.02273)]
- [2026] **From Rocq to Metal: A Pipeline for Formally Verified Microcontroller Firmware** [[paper](https://arxiv.org/abs/2606.02651)]
- [2026] **The Productivity-Reliability Paradox: Specification-Driven Governance for AI-Augmented Software Development** [[paper](https://arxiv.org/abs/2605.01160)]
- [2026] **Evaluating LLM-Generated Code: A Benchmark and Developer Study** [[paper](https://arxiv.org/abs/2605.09059)]
- [2026] **Requirements Debt in AI-Enabled Perception Systems Development: An Industrial RE4AI Perspective** [[paper](https://arxiv.org/abs/2604.27825)]
- [2026] **Beyond Isolated Tasks: A Framework for Evaluating Coding Agents on Sequential Software Evolution** [[paper](https://arxiv.org/abs/2604.03035)]
- [2026] **A Survey of Algorithm Debt in Machine and Deep Learning Systems: Definition, Smells, and Future Work** [[paper](https://arxiv.org/abs/2604.06363)]
- [2026] **Investigating CI/CD-based Technical Debt Management in Open-source Projects** [[paper](https://arxiv.org/abs/2604.10631)]
- [2026] **Portable and Secure CI/CD for COBOL: Lessons from an Industrial Migration** [[paper](https://arxiv.org/abs/2604.00936)]
- [2026] **Feature Toggle Dynamics in Large-Scale Systems: Prevalence, Growth, Lifespan, and Benchmarking** [[paper](https://arxiv.org/abs/2604.15872)]
- [2026] **Comprehension Debt in GenAI-Assisted Software Engineering Projects** [[paper](https://arxiv.org/abs/2604.13277)]
- [2026] **Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering** [[paper](https://arxiv.org/abs/2604.26275)]
- [2026] **Real-Time Toxicity Filtering for Open-Source Code Reviews** [[paper](https://arxiv.org/abs/2604.08886)]
- [2026] **Bigger Isn't Always Better: A Comparative Evaluation of LLMs for Automated Code Review** [[paper](https://arxiv.org/abs/2606.15689)]
- [2026] **Automated Classification of Human Code Review Comments with Large Language Models** [[paper](https://arxiv.org/abs/2604.23667)]
- [2026] **An Eye for Trust: An Exploration of Developers' Trust Perceptions Through Urgency and Reputation** [[paper](https://arxiv.org/abs/2604.08713)]
- [2026] **Humans Integrate, Agents Fix: How Agent-Authored Pull Requests Are Referenced in Practice** [[paper](https://arxiv.org/abs/2604.04059)]
- [2026] **SmartPatchLinker: An Open-Source Tool to Linked Changes Detection for Code Review** [[paper](https://arxiv.org/abs/2604.04045)] [[code](https://github.com/islem-kms/gerrit-chrome-extension)]
- [2026] **Characterizing the Usefulness of Code Review Comments in Scientific Software for Software Quality and Scientific Rigor** [[paper](https://arxiv.org/abs/2604.23832)]
- [2026] **ToxiShield: Promoting Inclusive Developer Communication through Real-Time Toxicity Filtering** [[paper](https://arxiv.org/abs/2604.14408)]
- [2026] **Recovering Fine-Grained Code Change Rationale from Multiple Software Artifacts** [[paper](https://arxiv.org/abs/2604.10345)]
- [2026] **From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests** [[paper](https://arxiv.org/abs/2604.03196)]
- [2026] **The Code Whisperer: LLM and Graph-Based AI for Smell and Vulnerability Resolution** [[paper](https://arxiv.org/abs/2604.13114)]
- [2026] **Workstream: A Local-First Developer Command Center for the AI-Augmented Engineering Workflow** [[paper](https://arxiv.org/abs/2604.17055)] [[code](https://github.com/happybhati/workstream)]
- [2026] **Scaling Coding Agents via Atomic Skills** [[paper](https://arxiv.org/abs/2604.05013)]
- [2026] **Prompt-Driven Code Summarization: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2604.15385)]
- [2026] **Dataset - A Study on Library induced Technical Debt** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32083569.v1)]
- [2026] **Dataset - A Study on Library Co-occurring Technical Debt** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32083569.v2)]
- [2026] **The Nature of Technical Debt in Research Software** [[paper](https://arxiv.org/abs/2603.20415)]
- [2026] **Reducing Labeling Effort in Architecture Technical Debt Detection through Active Learning and Explainable AI** [[paper](https://arxiv.org/abs/2603.02944)]
- [2026] **Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild** [[paper](https://arxiv.org/abs/2603.28592)]
- [2026] **SWE-Milestone: Evaluating AI Agents on Continuous Software Evolution** [[paper](https://arxiv.org/abs/2603.13428)]
- [2026] **The State of Generative AI in Software Development: Insights from Literature and a Developer Survey** [[paper](https://arxiv.org/abs/2603.16975)]
- [2026] **From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI** [[paper](https://arxiv.org/abs/2603.22106)]
- [2026] **Requirements Volatility in Software Architecture Design: An Exploratory Case Study** [[paper](https://arxiv.org/abs/2603.17648)]
- [2026] **Do AI Agents Really Improve Code Readability?** [[paper](https://arxiv.org/abs/2603.13723)]
- [2026] **Self-Admitted Technical Debt in Scientific Software: Prioritization, Sentiment, and Propagation Across Artifacts** [[paper](https://arxiv.org/abs/2603.15883)]
- [2026] **Investigating Technical Debt Types, Issues, and Solutions in Serverless Computing** [[paper](https://arxiv.org/abs/2603.22480)]
- [2026] **A Practical Guide for Establishing a Technical Debt Management Process (Preprint)** [[paper](https://arxiv.org/abs/2603.03085)]
- [2026] **Code Review Agent Benchmark** [[paper](https://arxiv.org/abs/2603.23448)]
- [2026] **CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents** [[paper](https://arxiv.org/abs/2603.11078)]
- [2026] **Gendered Prompting and LLM Code Review: How Gender Cues in the Prompt Shape Code Quality and Evaluation** [[paper](https://arxiv.org/abs/2603.24359)]
- [2026] **Test Code Review in the Era of GitHub Actions: A Replication Study** [[paper](https://arxiv.org/abs/2603.15935)]
- [2026] **SWE-PRBench: Benchmarking AI Code Review Quality Against Pull Request Feedback** [[paper](https://arxiv.org/abs/2603.26130)]
- [2026] **RippleGUItester: Change-Aware Exploratory Testing** [[paper](https://arxiv.org/abs/2603.03121)]
- [2026] **RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review** [[paper](https://arxiv.org/abs/2603.16107)]
- [2026] **Beyond the 'Diff': Addressing Agentic Entropy in Agentic Software Development** [[paper](https://arxiv.org/abs/2604.16323)]
- [2026] **Agentic Code Reasoning** [[paper](https://arxiv.org/abs/2603.01896)]
- [2026] **Impostor Phenomenon as Human Debt: A Challenge to the Future of Software Engineering** [[paper](https://arxiv.org/abs/2602.13767)]
- [2026] **Automated LLM-Based Accessibility Remediation: From Conventional Websites to Angular Single-Page Applications** [[paper](https://arxiv.org/abs/2602.17887)]
- [2026] **Socio-Technical Well-Being of Quantum Software Communities: An Overview on Community Smells** [[paper](https://arxiv.org/abs/2602.17320)]
- [2026] **ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files** [[paper](https://arxiv.org/abs/2603.00822)] [[code](https://github.com/reSHARMA/ContextCov)]
- [2026] **Reading Between the Code Lines: On the Use of Self-Admitted Technical Debt for Security Analysis** [[paper](https://arxiv.org/abs/2602.03470)]
- [2026] **A Survey of Code Review Benchmarks and Evaluation Practices in Pre-LLM and LLM Era** [[paper](https://arxiv.org/abs/2602.13377)]
- [2026] **Studying Quality Improvements Recommended via Manual and Automated Code Review** [[paper](https://arxiv.org/abs/2602.11925)]
- [2026] **Following Dragons: Code Review-Guided Fuzzing** [[paper](https://arxiv.org/abs/2602.10487)]
- [2026] **CL4SE: Benchmarking Context Learning on Software Engineering** [[paper](https://arxiv.org/abs/2602.23047)]
- [2026] **Forecasting Developer Environments with GenAI: A Research Perspective** [[paper](https://arxiv.org/abs/2602.07412)]
- [2026] **ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development** [[paper](https://arxiv.org/abs/2602.01655)] [[code](https://github.com/zsworld6/projdevbench)]
- [2026] **SV-Benchmarks: Benchmark Set for Software Verification and Testing (SV-COMP 2026, Test-Comp 2026)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18650775)]
- [2026] **Machine learning intervention on cyber-hate in code-switch texts: a systematic review with open challenges and solutions** *PeerJ Computer Science* [[paper](https://doi.org/10.7717/peerj-cs.3537)]
- [2026] **A Practical Guide to Establishing Technical Debt Management (TDM Guide for Practitioners)** [[paper](https://arxiv.org/abs/2601.11430)]
- [2026] **Self-Admitted Technical Debt in LLM Software: An Empirical Comparison with ML and Non-ML Software** [[paper](https://arxiv.org/abs/2601.06266)]
- [2026] **"TODO: Fix the Mess Gemini Created": Towards Understanding GenAI-Induced Self-Admitted Technical Debt** [[paper](https://arxiv.org/abs/2601.07786)]
- [2026] **Folklore in Software Engineering: A Definition and Conceptual Foundations** [[paper](https://arxiv.org/abs/2601.21814)]
- [2026] **An Exploratory Pilot Survey on Technical Quality Control Practices in Agile R&D Projects** [[paper](https://arxiv.org/abs/2601.06689)]
- [2026] **Technical Lag as Latent Technical Debt: A Rapid Review** [[paper](https://arxiv.org/abs/2601.11693)]
- [2026] **More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests** [[paper](https://arxiv.org/abs/2601.21276)]
- [2026] **The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming** [[paper](https://arxiv.org/abs/2601.02410)]
- [2026] **AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development** [[paper](https://arxiv.org/abs/2601.13597)] [[code](https://github.com/shyamagarwal13/agentic-coding-impact)]
- [2026] **Multi-Artifact Analysis of Self-Admitted Technical Debt in Scientific Software** [[paper](https://arxiv.org/abs/2601.10850)]
- [2026] **A Survey on Large Language Model Impact on Software Evolvability and Maintainability: the Good, the Bad, the Ugly, and the Remedy** [[paper](https://arxiv.org/abs/2601.20879)]
- [2026] **RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian** [[paper](https://arxiv.org/abs/2601.01129)]
- [2026] **HalluJudge: A Reference-Free Hallucination Detection for Context Misalignment in Code Review Automation** [[paper](https://arxiv.org/abs/2601.19072)]
- [2026] **AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection** [[paper](https://arxiv.org/abs/2601.19138)]
- [2026] **Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering** [[paper](https://arxiv.org/abs/2601.14470)]
- [2026] **Group versus Individual Review Requests: Tradeoffs in Speed and Quality at Mozilla Firefox** [[paper](https://arxiv.org/abs/2601.01514)]
- [2026] **LLM-Based Repair of C++ Implicit Data Loss Compiler Warnings: An Industrial Case Study** [[paper](https://arxiv.org/abs/2601.14936)]
- [2026] **TagDebt: a bot to support technical debt management.** *Empir. Softw. Eng.* [[paper](https://dblp.org/rec/journals/ese/BiazottoFAN26)]
- [2026] **Management of Technical Debt in Startups: A Systematic Mapping.** *J. Softw. Eng. Res. Dev.* [[paper](https://dblp.org/rec/journals/jserd/RandoLGB26)]
- [2026] **Establishing technical debt management - A five-step workshop approach and an action research study.** *J. Syst. Softw.* [[paper](https://dblp.org/rec/journals/jss/WieseSBMB26)]
- [2026] **An AI-Enhanced Technical Debt Management Framework for Aerospace and Defense Systems Engineering: Framework Design and Illustrative Application.** *Syst.* [[paper](https://dblp.org/rec/journals/systems/OuzzifB26)]
- [2026] **Investigating CI/CD-based Technical Debt Management in Open-source Projects.** *TechDebt@ICSE* [[paper](https://dblp.org/rec/conf/techdebt/BiazottoFAN26)]
- [2026] **Beyond the Code: The Value of Practicing and Evaluating Technical Debt Management.** *TechDebt@ICSE* [[paper](https://dblp.org/rec/conf/techdebt/OrucevicKM26)]
- [2026] **A Practical Guide for Establishing a Technical Debt Management Process.** *TechDebt@ICSE* [[paper](https://dblp.org/rec/conf/techdebt/WieseSB26)]
- [2026] **Autonomous AI and Agentic Testing Agents: A Multi-Agent Architecture for Self-Directed Software Quality Assurance** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-10220882/v1)]
- [2026] **Development and feasibility assessment of an in-house gravimetric control system for quality assurance of antineoplastic compounding.** *MED* [[paper](https://doi.org/10.1177/10781552261470007)]
- [2026] **AI Quality Ops Platform: A Unified, Containerised Ecosystem for Continuous AI Quality Assurance** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-10002757/v1)]
- [2026] **A python framework for single-image characterization of X-ray focal spot distribution and detector point spread function.** *MED* [[paper](https://doi.org/10.1002/mp.70513)]
- [2026] **Increasing demands on commissioning and quality assurance for cone-based multiple brain metastases robotic radiosurgery: evaluation in a custom phantom.** *MED* [[paper](https://doi.org/10.1007/s13246-026-01765-9)]
- [2026] **CrisisConnect** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-9634199/v1)]
- [2026] **Automated Analysis for MR Coil QA.** *MED* [[paper](https://doi.org/10.1002/acm2.70624)]
- [2026] **An explainable AI framework for enhanced software defect prediction using transformer-assisted boosting.** *MED* [[paper](https://doi.org/10.1038/s41598-026-44202-3)]
- [2026] **Quality assurance in rapid diagnostic tests for accurate diagnosis of malaria.** *MED* [[paper](https://doi.org/10.25259/ijmr_2477_2025)]
- [2026] **Psychological resilience, physical self-efficacy, and physical activity among college students: developing and testing a model based on social cognitive theory.** *MED* [[paper](https://doi.org/10.1038/s41598-026-58957-2)]
- [2026] **A two-dimensional software reliability growth model incorporating testing effort and coverage** *Safety and Reliability* [[paper](https://doi.org/10.1080/09617353.2025.2607197)]
- [2026] **Replication Package for "Evolving Kubernetes: A Technical Debt Perspective"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18351822)]

##### 2025

- [2025] **Quantitative Analysis of Technical Debt and Pattern Violation in Large Language Model Architectures** [[paper](https://arxiv.org/abs/2512.04273)]
- [2025] **Vibe Coding in Practice: Flow, Technical Debt, and Guidelines for Sustainable Use** [[paper](https://arxiv.org/abs/2512.11922)]
- [2025] **LAURA: Enhancing Code Review Generation with Context-Enriched Retrieval-Augmented LLM** [[paper](https://arxiv.org/abs/2512.01356)]
- [2025] **On Assessing the Relevance of Code Reviews Authored by Generative Models** [[paper](https://arxiv.org/abs/2512.15466)]
- [2025] **SGCR: A Specification-Grounded Framework for Trustworthy LLM Code Review** [[paper](https://arxiv.org/abs/2512.17540)]
- [2025] **Engagement in Code Review: Emotional, Behavioral, and Cognitive Dimensions in Peer vs. LLM Interactions** [[paper](https://arxiv.org/abs/2512.05309)]
- [2025] **Coding With AI: From a Reflection on Industrial Practices to Future Computer Science and Software Engineering Education** [[paper](https://arxiv.org/abs/2512.23982)]
- [2025] **A survey of generative AI adoption and perceived productivity among scientists who program** [[paper](https://arxiv.org/abs/2512.19644)]
- [2025] **What Happens When Technical Debt Vanishes?** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2025.3621709)]
- [2025] **An insight into the technical debt-fix trade off in software backporting** [[paper](https://arxiv.org/abs/2511.09000)]
- [2025] **SQuaD: The Software Quality Dataset** [[paper](https://arxiv.org/abs/2511.11265)]
- [2025] **Hidden in Plain Sight: Where Developers Confess Self-Admitted Technical Debt** [[paper](https://arxiv.org/abs/2511.01529)]
- [2025] **Establishing Traceability Links between Release Notes & Software Artifacts: Practitioners' Perspectives** [[paper](https://arxiv.org/abs/2511.18187)]
- [2025] **Exploring Scientific Debt: Harnessing AI for SATD Identification in Scientific Software** [[paper](https://arxiv.org/abs/2511.17368)]
- [2025] **Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics** [[paper](https://arxiv.org/abs/2511.10271)]
- [2025] **An Empirical Study of Java Code Improvements Based on Stack Overflow Answer Edits** [[paper](https://arxiv.org/abs/2511.05813)]
- [2025] **Peer Code Review in Research Software Development: The Research Software Engineer Perspective** [[paper](https://arxiv.org/abs/2511.10781)]
- [2025] **Benchmarking LLMs for Fine-Grained Code Review with Enriched Context in Practice** [[paper](https://arxiv.org/abs/2511.07017)] [[code](https://github.com/kinesiatricssxilm14/ContextCRBench)]
- [2025] **AILINKPREVIEWER: Enhancing Code Reviews with LLM-Powered Link Previews** [[paper](https://arxiv.org/abs/2511.09223)] [[code](https://github.com/c4rtune/AILinkPreviewer)]
- [2025] **When More Retrieval Hurts: Retrieval-Augmented Code Review Generation** [[paper](https://arxiv.org/abs/2511.05302)]
- [2025] **The Future of Development Environments with AI Foundation Models: NII Shonan Meeting 222 Report** [[paper](https://arxiv.org/abs/2511.16092)]
- [2025] **An Agentic-AI Solution for Intelligent Code Review** [[paper](https://doi.org/10.1109/slaai-icai68534.2025.11318443)]
- [2025] **LLMs as Code Review Agents: A Rapid Review and Experimental Evaluation with Human Expert Judges** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-09318-9_24)]
- [2025] **CppSATD: Large-Scale Technical Debt Dataset for C++ Projects** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17523466)]
- [2025] **Understanding Self-Admitted Technical Debt in Test Code: An Empirical Study** [[paper](https://arxiv.org/abs/2510.22249)]
- [2025] **Detecting and Characterizing Low and No Functionality Packages in the NPM Ecosystem** [[paper](https://arxiv.org/abs/2510.04495)]
- [2025] **Position: Vibe Coding Needs Vibe Reasoning: Improving Vibe Coding with Formal Verification** [[paper](https://arxiv.org/abs/2511.00202)]
- [2025] **Using Copilot Agent Mode to Automate Library Migration: A Quantitative Assessment** [[paper](https://arxiv.org/abs/2510.26699)]
- [2025] **Human to Document, AI to Code: Comparing GenAI for Notebook Competitions** [[paper](https://arxiv.org/abs/2510.18430)]
- [2025] **A First Look at the Self-Admitted Technical Debt in Test Code: Taxonomy and Detection** [[paper](https://arxiv.org/abs/2510.22409)]
- [2025] **A First Look at the Lifecycle of DL-Specific Self-Admitted Technical Debt** [[paper](https://arxiv.org/abs/2510.03802)]
- [2025] **SecureReviewer: Enhancing Large Language Models for Secure Code Review through Secure-aware Fine-tuning** [[paper](https://arxiv.org/abs/2510.26457)]
- [2025] **RevMine: An LLM-Assisted Tool for Code Review Mining and Analysis Across Git Platforms** [[paper](https://arxiv.org/abs/2510.04796)]
- [2025] **iCodeReviewer: Improving Secure Code Review with Mixture of Prompts** [[paper](https://arxiv.org/abs/2510.12186)]
- [2025] **What Types of Code Review Comments Do Developers Most Frequently Resolve?** [[paper](https://arxiv.org/abs/2510.05450)]
- [2025] **Automatic Building Code Review: A Case Study** [[paper](https://arxiv.org/abs/2510.02634)]
- [2025] **Enhancing Code Review through Fuzzing and Likely Invariants** [[paper](https://arxiv.org/abs/2510.15512)]
- [2025] **Grounded AI for Code Review: Resource-Efficient Large-Model Serving in Enterprise Pipelines** [[paper](https://arxiv.org/abs/2510.10290)]
- [2025] **The Fast and Spurious: Developer Productivity with GenAI** [[paper](https://arxiv.org/abs/2510.24265)]
- [2025] **Mapping the non-coding RNA landscape in ataxia telangiectasia: a scoping review of ATM dependent miRNA and lncRNA dysregulation** *Molecular Biology Reports* [[paper](https://doi.org/10.1007/s11033-025-11094-x)]
- [2025] **PromptDebt: A Comprehensive Study of Technical Debt Across LLM Projects** [[paper](https://arxiv.org/abs/2509.20497)]
- [2025] **Rethinking Technology Stack Selection with AI Coding Proficiency** [[paper](https://arxiv.org/abs/2509.11132)]
- [2025] **GitHub's Copilot Code Review: Can AI Spot Security Flaws Before You Commit?** [[paper](https://arxiv.org/abs/2509.13650)]
- [2025] **Fine-Tuning LLMs to Analyze Multiple Dimensions of Code Review: A Maximum Entropy Regulated Long Chain-of-Thought Approach** [[paper](https://arxiv.org/abs/2509.21170)]
- [2025] **ChatGPT for Code Refactoring: Analyzing Topics, Interaction, and Effective Prompts** [[paper](https://arxiv.org/abs/2509.08090)]
- [2025] **SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation** [[paper](https://arxiv.org/abs/2509.01494)]
- [2025] **Intuition to Evidence: Measuring AI's True Impact on Developer Productivity** [[paper](https://arxiv.org/abs/2509.19708)]
- [2025] **TestLoop: A Process Model Describing Human-in-the-Loop Software Test Suite Generation** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3765754)]
- [2025] **A Large-scale Benchmark for Technical Debt Assessment** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.7579716)]
- [2025] **Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions** [[paper](https://arxiv.org/abs/2508.18771)]
- [2025] **Previously on... Automating Code Review** [[paper](https://arxiv.org/abs/2508.18003)]
- [2025] **Characterizing the Global Polycrisis: A Systematic Review of Recent Literature** *Annual Review of Environment and Resources* [[paper](https://doi.org/10.1146/annurev-environ-111523-102238)]
- [2025] **From Technical Debt to Business Process Debt: A Framework for Proactive Debt Management in BPM.** *ICDSST* [[paper](https://dblp.org/rec/conf/ewgdss/NousiasTNV25)]
- [2025] **DebtQuest: Discover Technical Debt Management Issues with Survey Visualization.** *VISSOFT* [[paper](https://dblp.org/rec/conf/vissoft/IrgensOBGM25)]

##### 2024

- [2024] **Estimating Refactoring Efforts for Architecture Technical Debt** [[paper](https://doi.org/10.33915/etd.7711)]
- [2024] **Reducing Technical Debt Density: Refactoring vs. Writing Clean New Code** [[paper](https://doi.org/10.33612/diss.181245089)]

##### 2023

- [2023] **Code Review at the Speed of Light: What's Wrong with Pull Requests?** [[paper](https://arxiv.org/abs/2306.12345)]
- [2023] **Preventing technical debt with the TAP framework for Technical Debt Aware Management.** *Software Engineering* [[paper](https://dblp.org/rec/conf/se/WieseRRS23)]
- [2023] **Business-driven technical debt management using Continuous Debt Valuation Approach (CoDVA).** *Inf. Softw. Technol.* [[paper](https://dblp.org/rec/journals/infsof/StochelBWC23)]
- [2023] **Technical Debt Management in Industrial ML - State of Practice and Management Model Proposal.** *INDIN* [[paper](https://dblp.org/rec/conf/indin/WangSBK23)]

##### 2022

- [2022] **Refactoring debt** *Proceedings of the 19th International Conference on Mining Software Repositories* [[paper](https://doi.org/10.1145/3524842.3528527)]

##### 2021

- [2021] **Preventing Technical Debt by Technical Debt Aware Project Management.** *TechDebt@ICSE* [[paper](https://dblp.org/rec/conf/icse/WieseRS21)]
- [2021] **Technical Debt Guild: When experience and engagement improve Technical Debt Management.** *SBQS* [[paper](https://dblp.org/rec/conf/sbqs/DetofenoRA21)]

##### 2020

- [2020] **Refactoring of Code to Remove Technical Debt and Reduce Maintenance Effort** *2020 14th International Conference on Open Source Systems and Technologies (ICOSST)* [[paper](https://doi.org/10.1109/icosst51357.2020.9332917)]

##### 2019

- [2019] **Self-Admitted Technical Debt Removal and Refactoring Actions: Co-Occurrence or More?** *2019 IEEE International Conference on Software Maintenance and Evolution (ICSME)* [[paper](https://doi.org/10.1109/icsme.2019.00029)]
- [2019] **Lessons from the Exponential Growth of Refactoring Research in the Last Decade** *2019 IEEE/ACM International Conference on Technical Debt (TechDebt)* [[paper](https://doi.org/10.1109/techdebt.2019.00020)]
- [2019] **Integrating Technical Debt Management and Software Quality Management Processes: A Normative Framework and Field Tests.** *IEEE Trans. Software Eng.* [[paper](https://dblp.org/rec/journals/tse/RamasubbuK19)]

##### 2018

- [2018] **Integrating technical debt management and software quality management processes: a framework and field tests.** *ICSE* [[paper](https://dblp.org/rec/conf/icse/RamasubbuK18)]

##### 2016

- [2016] **An empirically developed method to aid decisions on architectural technical debt refactoring** *Proceedings of the 38th International Conference on Software Engineering Companion* [[paper](https://doi.org/10.1145/2889160.2889224)]

##### 2015

- [2015] **Tools for Repaying Technical Debt** *Refactoring for Software Design Smells* [[paper](https://doi.org/10.1016/b978-0-12-801397-7.15002-7)]
- [2015] **Technical Debt** *Refactoring for Software Design Smells* [[paper](https://doi.org/10.1016/b978-0-12-801397-7.00001-1)]
- [2015] **Repaying Technical Debt in Practice** *Refactoring for Software Design Smells* [[paper](https://doi.org/10.1016/b978-0-12-801397-7.00008-4)]

##### 2013

- [2013] **DebtFlag: technical debt management with a development environment integrated tool.** *MTD@ICSE* [[paper](https://dblp.org/rec/conf/icse/HolvitieL12)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **LLMs in Software Testing: A Practitioner Survey** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21019924)]
- [2026] **Extended Data for: Clinical Activation Codes in Improving Emergency Department Efficiency: A Systematic Review** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20408021)]
- [2026] **International Code of Nomenclature of Prokaryotes. Prokaryotic Code (2025 Revision)** *INTERNATIONAL JOURNAL OF SYSTEMATIC AND EVOLUTIONARY MICROBIOLOGY* [[paper](https://doi.org/10.1099/ijsem.0.006979)]
- [2026] **Seismic analysis of tanks and vessels: A comprehensive review of international codes and guidelines** *Structures* [[paper](https://doi.org/10.1016/j.istruc.2026.111276)]
- [2026] **A systematic review of urinary extracellular vesicle-derived non-coding RNAs in diabetic nephropathy: expression profiles, clinical correlations, and diagnostic performance** *Molecular Biology Reports* [[paper](https://doi.org/10.1007/s11033-026-11523-5)]
- [2026] **Online appendix: Demystifying Knowledge Hiding in Software Testing — Insights from Practitioners** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.30988318)]
- [2026] **A Review of Screenshot-to-Code Generation Systems** [[paper](https://doi.org/10.1109/iccces62661.2026.11436626)]

##### 2025

- [2025] **Challenges for Distance Relays in Grid Code-Compliant Inverter-Based Power Systems: A Review** *IEEE Open Journal of Power Electronics* [[paper](https://doi.org/10.1109/ojpel.2025.3640291)]
- [2025] **Technical Debt Tracker – Risk Management Template** [[paper](https://doi.org/10.1201/9781003646082-55)]
- [2025] **Using LLMs to enhance code quality: A systematic literature review** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107960)]
- [2025] **Enhancing sustainable food purchasing by blockchain-enabled reviews and QR code traceability systems in Vietnam: the moderating role of environmental concern** *Journal of Foodservice Business Research* [[paper](https://doi.org/10.1080/15378020.2025.2578600)]
- [2025] **Dampak dan Tantangan Pembelajaran Coding Bagi Siswa Sekolah Dasar: A Systematic Literature Review** *Jurnal Didaktika Pendidikan Dasar* [[paper](https://doi.org/10.26811/didaktika.v9i3.2033)]
- [2025] **Pathological, diagnostic, and therapeutic implications of non-coding RNAs in deep vein thrombosis: A comprehensive review** *Journal of Thrombosis and Thrombolysis* [[paper](https://doi.org/10.1007/s11239-025-03202-2)]
- [2025] **Diagnostic accuracy of non-coding RNA for detecting endometriosis: A systematic review and meta-analysis** *Clinica Chimica Acta* [[paper](https://doi.org/10.1016/j.cca.2025.120734)]
- [2025] **From hedonism to identity: what codes are present in game reviews?** *Current Psychology* [[paper](https://doi.org/10.1007/s12144-025-08489-1)]
- [2025] **Emerging roles and therapeutic potential of non-coding RNA in osteosarcoma: a review** *Medical Oncology* [[paper](https://doi.org/10.1007/s12032-025-03036-1)]
- [2025] **Non-coding RNAs’ pivotal importance in modulation of cancer sensitivity to Topotecan: a systematic review** *Medical Oncology* [[paper](https://doi.org/10.1007/s12032-025-03029-0)]
- [2025] **Fibrosis-associated non-coding RNAs in keloids: Dual roles in pathogenesis and therapy: A review** *International Journal of Biological Macromolecules* [[paper](https://doi.org/10.1016/j.ijbiomac.2025.147724)]

##### 2022

- [2022] **Technical Debt: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2209.01234)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **Enterprise AI Platforms: Why They Create Technical Debt** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21784212)]
- [2026] **Governing Technical Debt in Agentic AI Systems** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2605.29129)]
- [2026] **ERP Modernization Series – Part 2: Reducing Technical Debt During ECC to S/4HANA Transformation** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18471618)]
- [2026] **Dealing with Technical Debt** [[paper](https://doi.org/10.1201/9781003646525-7)]

##### 2025

- [2025] **Prompt Driven Test Generation: Leveraging Large Language Models and Knowledge Graphs for Quality Assurance in Data Intensive Software System** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-08649-5_17)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Modern Software Testing** [[paper](https://doi.org/10.1201/9781003544289-10)]
- [2026] **From Technical Debt to Cognitive and Intent Debt** *Queue* [[paper](https://doi.org/10.1145/3807966)]
- [2026] **Evaluating Tools for Automatic Software Testing (Report on Test-Comp 2026)** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-22774-4_23)]
- [2026] **Determinants of Accounting Software Acceptance among Undergraduate Students: Testing TAM/UTAUT in an Introductory Accounting Course Context** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6179941)]
- [2026] **Software Testing Report** *OSF Preprints (OSF Preprints)* [[paper](https://osf.io/2kasg)]
- [2026] **Quora Mobile Software Testing** *OSF Preprints (OSF Preprints)* [[paper](https://osf.io/52c6e)]
- [2026] **Practical Software Test Analysis** [[paper](https://doi.org/10.1007/978-3-032-27986-6)]
- [2026] **Towards Human-like Software Testing** *Open MIND* [[paper](https://doi.org/10.18420/se2026_65)]
- [2026] **Forecasting Technical Debt in Software Projects with Limited Historical Data** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-12478-4_23)]

##### 2025

- [2025] **Automated robustness testing for LLM-based natural language processing software** *Expert Systems with Applications* [[paper](https://doi.org/10.1016/j.eswa.2025.130642)]
- [2025] **Types of software testing** *ELARTU (Ternopil National Technical University)* [[paper](https://elartu.tntu.edu.ua/handle/lib/50999)]
- [2025] **On software testing reference ontologies** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112759)]
- [2025] **SOFTWARE TEST REQUIREMENTS MANAGEMENT** *Bulletin of the Angarsk State Technical University* [[paper](https://doi.org/10.36629/2686-777x-2025-1-19-120-123)]
- [2025] **The Potential of Large Language Models in Automating Software Testing: From Generation to Reporting** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-08649-5_13)]
- [2025] **Enhancing Software Security Through Automated Sdlc Integration and Model-Based Testing** [[paper](https://doi.org/10.1109/ssitcon66133.2025.11342172)]
- [2025] **Sociology and Software Testing** [[paper](https://doi.org/10.1002/9781394319749.ch17)]
- [2025] **Revisiting software reliability growth model under general setup** *International Journal of Systems Assurance Engineering and Management* [[paper](https://doi.org/10.1007/s13198-025-02988-x)]
- [2025] **Silver Box Testing for Scaling Software Development Fidelity: Enhancing Quality and Efficiency** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04403-7_23)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **An Approach for Embedding-Guided Function Reuse Detection in Embedded C Software** [[paper](https://arxiv.org/abs/2608.04137)]
- [2026] **LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles** [[paper](https://arxiv.org/abs/2608.13450)]
- [2026] **SNIPTEST: Fuzzing Multi-Level Code Slices for Validating Vulnerabilities** [[paper](https://arxiv.org/abs/2608.17396)]
- [2026] **CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing** [[paper](https://arxiv.org/abs/2608.10613)]
- [2026] **Comparing the Quality of Code Generated by Vibe Coding Tools** [[paper](https://arxiv.org/abs/2608.16302)]
- [2026] **Modelling Android applications through static analysis and systematic exploratory testing** [[paper](https://arxiv.org/abs/2608.00228)]
- [2026] **Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs** [[paper](https://arxiv.org/abs/2607.00555)]
- [2026] **AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs** [[paper](https://arxiv.org/abs/2607.01640)]
- [2026] **ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation** [[paper](https://arxiv.org/abs/2607.08691)]
- [2026] **TATG: Tracking-Aware Testing Objective for LLM-based Test Generation** [[paper](https://arxiv.org/abs/2607.03194)]
- [2026] **SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing** [[paper](https://arxiv.org/abs/2607.08949)]
- [2026] **Multi-Source and Cross-Scenario Strategy-Guided Code Optimization** [[paper](https://arxiv.org/abs/2607.20353)]
- [2026] **Using LLMs to Adjudicate Static-Analysis Alerts with Error Reduction Techniques** [[paper](https://arxiv.org/abs/2607.09979)]
- [2026] **Towards Automatically Inferring Constraints to Identify Implicit Assumptions in Data Analysis** [[paper](https://arxiv.org/abs/2607.03114)]
- [2026] **Hidden Amplifiers: Cross-Level Risk in Software Supply Chains** [[paper](https://arxiv.org/abs/2607.05894)]
- [2026] **Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code** [[paper](https://arxiv.org/abs/2607.21641)]
- [2026] **FlowLog: Re-thinking Datalog for Fast and Extensible Static Analysis** [[paper](https://arxiv.org/abs/2607.23971)]
- [2026] **Are LLMs Ready for Anti-Pattern Detection in Microservice Architectures?** [[paper](https://arxiv.org/abs/2606.26927)]
- [2026] **The Illusion of Safety: Multi-Tier Verification of AI vs. Human C++ Code** [[paper](https://arxiv.org/abs/2607.00107)]
- [2026] **Reinforcement Learning for Software Vulnerability Analysis: A Systematic Review with Emphasis on C/C++ Source Code and Static Analysis** [[paper](https://arxiv.org/abs/2606.28403)]
- [2026] **Are We Lost in the Woods? Detecting Silent Semantic Faults for Random Forest Classifiers with Data-informed Static Analysis** [[paper](https://arxiv.org/abs/2606.07709)]
- [2026] **Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning** [[paper](https://arxiv.org/abs/2606.25356)]
- [2026] **Data-aware Static Analysis: Improving Detection of Semantic Faults in Machine Learning Code Using Data Characteristics** [[paper](https://arxiv.org/abs/2606.09957)]
- [2026] **Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling** [[paper](https://arxiv.org/abs/2606.14261)]
- [2026] **FusionVul: A Multimodal Feature Fusion Framework for Source Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2606.08553)]
- [2026] **Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback** [[paper](https://arxiv.org/abs/2605.30478)]
- [2026] **Control Flow Graph Recovery for Dynamically Loaded Code via Symbolic Library Resolution** [[paper](https://arxiv.org/abs/2605.29620)]
- [2026] **Mitigating False Positives in Static Memory Safety Analysis of Rust Programs via Reinforcement Learning** [[paper](https://arxiv.org/abs/2605.04000)]
- [2026] **ConCovUp: Effective Agent-Based Test Driver Generation for Concurrency Testing** [[paper](https://arxiv.org/abs/2605.09573)]
- [2026] **CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement** [[paper](https://arxiv.org/abs/2605.04677)]
- [2026] **An Empirical Analysis of Static Analysis Methods for Detection and Mitigation of Code Library Hallucinations** [[paper](https://arxiv.org/abs/2604.07755)]
- [2026] **Guiding Symbolic Execution with Static Analysis and LLMs for Vulnerability Discovery** [[paper](https://arxiv.org/abs/2604.06506)]
- [2026] **Detecting Call Graph Unsoundness without Ground Truth** [[paper](https://arxiv.org/abs/2604.00885)]
- [2026] **Combining Static Code Analysis and Large Language Models Improves Correctness and Performance of Algorithm Recognition** [[paper](https://arxiv.org/abs/2604.03048)]
- [2026] **Mono2Sls: Automated Monolith-to-Serverless Migration via Multi-Stage Pipeline with Static Analysis** [[paper](https://arxiv.org/abs/2604.24550)]
- [2026] **Program Analysis Guided LLM Agent for Proof-of-Concept Generation** [[paper](https://arxiv.org/abs/2604.07624)]
- [2026] **Towards Better Static Code Analysis Reports: Sentence Transformer-based Filtering of Non-Actionable Alerts** [[paper](https://arxiv.org/abs/2604.18525)]
- [2026] **Malicious ML Model Detection by Learning Dynamic Behaviors** [[paper](https://arxiv.org/abs/2604.19438)]
- [2026] **AnomalyGen: Enhancing Log-Based Anomaly Detection with Code-Guided Data Augmentation** [[paper](https://arxiv.org/abs/2604.11107)]
- [2026] **Typify: A Lightweight Usage-driven Static Analyzer for Precise Python Type Inference** [[paper](https://arxiv.org/abs/2604.05067)]
- [2026] **VulWeaver: Weaving Broken Semantics for Grounded Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.10767)]
- [2026] **A Multi-Agent Framework for Automated Exploit Generation with Constraint-Guided Comprehension and Reflection** [[paper](https://arxiv.org/abs/2604.05130)]
- [2026] **From Heuristics to Transformers: A Comprehensive Survey of Type Inference from Stripped Binaries** [[paper](https://arxiv.org/abs/2606.23692)]
- [2026] **Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets** [[paper](https://arxiv.org/abs/2604.22291)]
- [2026] **Structural Quality Gaps in Practitioner AI Governance Prompts: An Empirical Study Using a Five-Principle Evaluation Framework** [[paper](https://arxiv.org/abs/2604.21090)]
- [2026] **Hallucination Inspector: A Fact-Checking Judge for API Migration** [[paper](https://arxiv.org/abs/2604.20202)]
- [2026] **Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval** [[paper](https://arxiv.org/abs/2603.22717)]
- [2026] **DAInfer+: Neurosymbolic Inference of API Specifications from Documentation via Embedding Models** [[paper](https://arxiv.org/abs/2603.28060)]
- [2026] **LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops** [[paper](https://arxiv.org/abs/2603.23613)]
- [2026] **Wherefore Art Thou? Provenance-Guided Automatic Online Debugging with Lumos** [[paper](https://arxiv.org/abs/2603.29013)]
- [2026] **Resolving Java Code Repository Issues with iSWE Agent** [[paper](https://arxiv.org/abs/2603.11356)]
- [2026] **Automatic Identification of Parallelizable Loops Using Transformer-Based Source Code Representations** [[paper](https://arxiv.org/abs/2603.30040)]
- [2026] **scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns** [[paper](https://arxiv.org/abs/2603.17893)]
- [2026] **Workflow-Level Design Principles for Trustworthy GenAI in Automotive System Engineering** [[paper](https://arxiv.org/abs/2602.19614)]
- [2026] **Distributed Architecture Reconstruction of Polyglot and Multi-Repository Microservice Projects** [[paper](https://arxiv.org/abs/2602.08166)]
- [2026] **Context-Sensitive Pointer Analysis for ArkTS** [[paper](https://arxiv.org/abs/2602.00457)]
- [2026] **iResolveX: Multi-Layered Indirect Call Resolution via Static Reasoning and Learning-Augmented Refinement** [[paper](https://arxiv.org/abs/2601.17888)]
- [2026] **Beyond Strict Rules: Assessing the Effectiveness of Large Language Models for Code Smell Detection** [[paper](https://arxiv.org/abs/2601.09873)]
- [2026] **AI Agent for Reverse-Engineering Legacy Finite-Difference Code and Translating to Devito** [[paper](https://arxiv.org/abs/2601.18381)]
- [2026] **Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming** [[paper](https://arxiv.org/abs/2601.02060)]
- [2026] **Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry** [[paper](https://arxiv.org/abs/2601.18844)]
- [2026] **Towards Analyzing N-language Polyglot Programs** [[paper](https://arxiv.org/abs/2602.00303)]
- [2026] **ArchAgent: Scalable Legacy Software Architecture Recovery with LLMs** [[paper](https://arxiv.org/abs/2601.13007)] [[code](https://github.com/panrusheng/arch-eval-benchmark)]
- [2026] **CVeDRL: An Efficient Code Verifier via Difficulty-aware Reinforcement Learning** [[paper](https://arxiv.org/abs/2601.22803)] [[code](https://github.com/LIGHTCHASER1/CVeDRL.git)]

##### 2025

- [2025] **Temporal HAL-API Dependencies as a Gateway to Formal Embedded Software Development** [[paper](https://arxiv.org/abs/2512.12788)]
- [2025] **BGPFuzz: Automated Configuration Fuzzing of the Border Gateway Protocol** [[paper](https://arxiv.org/abs/2512.05358)]
- [2025] **A Tale of 1001 LoC: Potential Runtime Error-Guided Specification Synthesis for Verifying Large-Scale Programs** [[paper](https://arxiv.org/abs/2512.24594)]
- [2025] **From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis** [[paper](https://arxiv.org/abs/2512.14070)]
- [2025] **QLCoder: A Query Synthesizer For Static Analysis of Security Vulnerabilities** [[paper](https://arxiv.org/abs/2511.08462)] [[code](https://github.com/neuralprogram/QLCoder)]
- [2025] **Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects** [[paper](https://arxiv.org/abs/2511.04427)]
- [2025] **SAINT: Service-level Integration Test Generation with Program Analysis and LLM-based Agents** [[paper](https://arxiv.org/abs/2511.13305)]
- [2025] **Actionable Warning Is Not Enough: Recommending Valid Actionable Warnings with Weak Supervision** [[paper](https://arxiv.org/abs/2511.12229)]
- [2025] **LLM-Driven Kernel Evolution: Automating Driver Updates in Linux** [[paper](https://arxiv.org/abs/2511.18924)]
- [2025] **LLM-Driven Adaptive Source-Sink Identification and False Positive Mitigation for Static Analysis** [[paper](https://arxiv.org/abs/2511.04023)]
- [2025] **ng-reactive-lint: Smarter Linting for Angular Apps** [[paper](https://arxiv.org/abs/2512.00250)]
- [2025] **Data Race Detection by Digest-Driven Abstract Interpretation (Extended Version)** [[paper](https://arxiv.org/abs/2511.11055)]
- [2025] **LLM-Powered Detection of Price Manipulation in DeFi** [[paper](https://arxiv.org/abs/2510.21272)]
- [2025] **Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks** [[paper](https://arxiv.org/abs/2510.23101)]
- [2025] **ZeroFalse: Improving Precision in Static Analysis with LLMs** [[paper](https://arxiv.org/abs/2510.02534)]
- [2025] **Checkstyle+: Reducing Technical Debt Through The Use of Linters with LLMs** [[paper](https://arxiv.org/abs/2510.23068)]
- [2025] **Automatically Generating Questions About Scratch Programs** [[paper](https://arxiv.org/abs/2510.11658)]
- [2025] **LSPRAG: LSP-Guided RAG for Language-Agnostic Real-Time Unit Test Generation** [[paper](https://arxiv.org/abs/2510.22210)]
- [2025] **CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings** [[paper](https://arxiv.org/abs/2509.11787)]
- [2025] **Try-Mopsa: Relational Static Analysis in Your Pocket** [[paper](https://arxiv.org/abs/2509.13128)]
- [2025] **Detection of security smells in IaC scripts through semantics-aware code and language processing** [[paper](https://arxiv.org/abs/2509.18790)]
- [2025] **ErrorPrism: Reconstructing Error Propagation Paths in Cloud Service Systems** [[paper](https://arxiv.org/abs/2509.26463)]
- [2025] **SecureFixAgent: A Hybrid LLM Agent for Automated Python Static Vulnerability Repair** *ICMLA 2025* [[paper](https://arxiv.org/abs/2509.16275)]
- [2025] **Towards Reliable Generation of Executable Workflows by Foundation Models** [[paper](https://arxiv.org/abs/2509.25117)]
- [2025] **Automated Insertion of Flushes and Fences for Persistency** [[paper](https://arxiv.org/abs/2509.19459)]
- [2025] **Security Evaluation of Android apps in budget African Mobile Devices** [[paper](https://arxiv.org/abs/2509.18800)]
- [2025] **Analysing Python Machine Learning Notebooks with Moose** [[paper](https://arxiv.org/abs/2509.11748)]
- [2025] **JSProtect: A Scalable Obfuscation Framework for Mini-Games in WeChat** [[paper](https://arxiv.org/abs/2509.24498)]
- [2025] **Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models** [[paper](https://arxiv.org/abs/2509.13023)]
- [2025] **Detecting Stealthy Data Poisoning Attacks in AI Code Generators** [[paper](https://arxiv.org/abs/2508.21636)]
- [2025] **Software Testing from Manual to AI-Driven Automation** *AI-Driven Software Testing* [[paper](https://doi.org/10.1007/979-8-8688-1829-5_2)]

##### 2024

- [2024] **Test Automation** *Introduction to Software Testing* [[paper](https://doi.org/10.1017/9781316771273.004)]
- [2024] **Suitable Software Automation Testing Tools for Microservices Architectures API Testing** [[paper](https://doi.org/10.2139/ssrn.5294994)]

##### 2023

- [2023] **The Importance of Software Testing** *Introduction to Software Testing* [[paper](https://doi.org/10.1007/978-1-4842-9514-4_1)]
- [2023] **Software Testing Types and Techniques** *Introduction to Software Testing* [[paper](https://doi.org/10.1007/978-1-4842-9514-4_2)]
- [2023] **Challenges and Solutions in Software Testing** *Introduction to Software Testing* [[paper](https://doi.org/10.1007/978-1-4842-9514-4_9)]

##### 2022

- [2022] **Automation Testing in Software Organization** *International Journal of Science and Research (IJSR)* [[paper](https://doi.org/10.21275/sr22629212828)]

##### 2017

- [2017] **Gamification of Software Testing** *2017 IEEE/ACM 12th International Workshop on Automation of Software Testing (AST)* [[paper](https://doi.org/10.1109/ast.2017.20)]
- [2017] **Testing** *Software Testing Automation Tips* [[paper](https://doi.org/10.1007/978-1-4842-3162-3_2)]
- [2017] **Software Testing Automation Tips** [[paper](https://doi.org/10.1007/978-1-4842-3162-3)]

[⬆ Back to top](#paper-list)

### Software Architecture

#### Method

##### 2026

- [2026] **Does It Render Everywhere? A Study of Cross-Environment Compatibility in MLLM-Generated Webpages** [[paper](https://arxiv.org/abs/2608.12518)]
- [2026] **Capturing and Exploiting Design Pattern Variability in Mobile Application Generation** [[paper](https://arxiv.org/abs/2607.15099)]
- [2026] **Benefits of Applying Software Design Patterns to Backend Rust Applications** [[paper](https://arxiv.org/abs/2607.02744)]
- [2026] **The Memory Wall of Green Software: Empirical Energy Evaluation of Memento Design Pattern** [[paper](https://arxiv.org/abs/2607.07944)]
- [2026] **Salesforce Messaging Architecture: Platform Events, Async Sends, and Multi-Tenancy at Scale** [[paper](https://arxiv.org/abs/2607.12943)]
- [2026] **A Control-Driven Framework for Secure SaaS Onboarding in Regulated Enterprises** [[paper](https://arxiv.org/abs/2607.16543)]
- [2026] **Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories** [[paper](https://arxiv.org/abs/2607.27250)]
- [2026] **Is Three the Magic Number? An Empirical Evaluation of LLM-Based Repair Loops** [[paper](https://arxiv.org/abs/2607.05197)]
- [2026] **A Large-Scale Dataset of MCP Implementations on GitHub** [[paper](https://arxiv.org/abs/2607.10123)]
- [2026] **Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges** [[paper](https://arxiv.org/abs/2607.26212)]
- [2026] **Skillware: A Software Ontology and Engineering Lifecycle for Persistent Behavioral Artifacts** [[paper](https://arxiv.org/abs/2607.18970)] [[code](https://github.com/MetaInFLow/skillware-patterns)]
- [2026] **Ontological Space Protocol: Modeling Software as a Conceptual Space with Epistemological Witnessing** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21206545)]
- [2026] **From Specification to Execution: AI Assisted Scientific Workflow Management** [[paper](https://arxiv.org/abs/2606.18425)]
- [2026] **From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes** [[paper](https://arxiv.org/abs/2606.23797)]
- [2026] **An LLM-Augmented Predictive Auto-Scaling Framework for Latency-Sensitive Microservice Backends** [[paper](https://doi.org/10.1109/icbase70763.2026.11619406)]
- [2026] **International Journal on Soft Computing** *International Journal on Soft Computing* [[paper](https://arxiv.org/abs/1209.1734)]
- [2026] **AMRF: A Software Architecture for Autonomous Mobile Robot Fleet Management in Warehouse Environments** [[paper](https://doi.org/10.1145/3816713.3819506)]
- [2026] **RackOps: Software Architecture and Automation Patterns for Large-Scale Server Rack Validation** *International Journal of Computer Applications* [[paper](https://doi.org/10.5120/ijcaf3f7a4838e82)]
- [2026] **Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton** [[paper](https://arxiv.org/abs/2605.26898)]
- [2026] **Deterministic vs. Probabilistic Summarisation: An Empirical Trade-off Study in Design Pattern Centric Java Code** [[paper](https://arxiv.org/abs/2605.21943)]
- [2026] **Using LLMs in Software Design: An Empirical Study of GitHub and A Practitioner Survey** [[paper](https://arxiv.org/abs/2605.01392)]
- [2026] **The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models** [[paper](https://arxiv.org/abs/2605.26128)]
- [2026] **Service Failure Detection in Distributed Microservice Platforms** *Saudi Journal of Engineering and Technology* [[paper](https://doi.org/10.36348/sjet.2026.v11i05.013)]
- [2026] **A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2605.20173)]
- [2026] **A Pilot Study on Detecting Software Design Patterns with Large Language Models: An Empirical Evaluation** [[paper](https://arxiv.org/abs/2604.17329)]
- [2026] **Quantum-HPC Software Stacks and the openQSE Reference Architecture: A Survey** [[paper](https://arxiv.org/abs/2604.20912)]
- [2026] **Collaborative Orchestration of Microservices and AI Services in Edges: A Dual-Time-Scale Reinforcement Learning Approach** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2026.3680248)]
- [2026] **Evolutionary Paths Toward Vehicle Zonal E/E Architecture: A Unified Architectural Framework** *SAE technical papers on CD-ROM/SAE technical paper series* [[paper](https://doi.org/10.4271/2026-01-0071)]
- [2026] **Impact of Micro Services Architecture Design Patterns on Software Maintenance Cost** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19522332)]
- [2026] **Dark Patterns in Software Engineering An Empirical Study of Behavioral Manipulation at the Architectural Level** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19665202)]
- [2026] **Evaluating Communication and Architectural Overheads in NTT Accelerators for ML-KEM** [[paper](https://doi.org/10.1109/ddecs69233.2026.11521008)]
- [2026] **LLM4Log: A Systematic Review of Large Language Model-based Log Analysis** [[paper](https://arxiv.org/abs/2604.16359)]
- [2026] **Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems** [[paper](https://arxiv.org/abs/2603.15690)]
- [2026] **Beyond the Code: A Multi-Modal Assessment Strategy for Fostering Professional Competencies via Introductory Programming Projects** [[paper](https://arxiv.org/abs/2603.18741)]
- [2026] **AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems** [[paper](https://arxiv.org/abs/2603.15727)]
- [2026] **MODIFy : A multi-modal anomaly diagnosis framework with diffusion-enhanced adaptive fusion in microservices** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112844)]
- [2026] **A Microservices-Based Solution with Hybrid Communication for Energy Management in Smart Grid Environments** *Sensors* [[paper](https://doi.org/10.3390/s26051714)]
- [2026] **Automated assessment of the relationship between microservice architectures and performance** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112857)]
- [2026] **Enhancing software-defined network security with deep learning: a comprehensive review** *International Journal of Information Security* [[paper](https://doi.org/10.1007/s10207-026-01232-2)]
- [2026] **Architecting AI-Augmented Enterprise Software Systems: A Systematic Framework for Scalable, Secure, and Event-Driven Cloud-Native Applications** *Journal of Computer Science and Technology Studies* [[paper](https://doi.org/10.32996/jcsts.2026.8.5.2)]
- [2026] **A Pythonic Functional Approach for Semantic Data Harmonisation in the ILIAD Project** [[paper](https://arxiv.org/abs/2604.13042)]
- [2026] **Carbon-Aware Governance Gates: An Architecture for Sustainable GenAI Development** [[paper](https://arxiv.org/abs/2602.19718)]
- [2026] **Towards Automated Page Object Generation for Web Testing using Large Language Models** [[paper](https://arxiv.org/abs/2602.19294)]
- [2026] **Bridging the Sim-to-Real Gap with multipanda ros2: A Real-Time ROS2 Framework for Multimanual Systems** [[paper](https://arxiv.org/abs/2602.02269)]
- [2026] **Adaptive Anomaly Detection in Microservice Systems via Meta-Learning** [[paper](https://doi.org/10.1145/3807246.3807348)]
- [2026] **Federated microservices architecture with blockchain for privacy-preserving and scalable healthcare analytics** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-026-39837-1)]
- [2026] **Mobility aware microservice placement in vehicular edge computing** *Journal of Cloud Computing Advances Systems and Applications* [[paper](https://doi.org/10.1186/s13677-026-00845-1)]
- [2026] **TraceHG: An Unsupervised Dual-View Framework for Microservice Anomaly Detection** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2026.3667576)]
- [2026] **Deep Reinforcement Learning-Based Microservices Placement Under Zero Trust Security Framework in Smart Grid** *Journal of Circuits Systems and Computers* [[paper](https://doi.org/10.1142/s0218126626501355)]
- [2026] **Knowledge management and the prescription paradox: lessons from patterns adoption** [[paper](https://doi.org/10.1201/9781003762614-141)]
- [2026] **Detection of vulnerabilities in software for unmanned aerial vehicles by using large language models** *Eastern-European Journal of Enterprise Technologies* [[paper](https://doi.org/10.15587/1729-4061.2026.352029)]
- [2026] **Design of An Improved Reinforced Transformer Architecture for Real-Time Policy Optimization in Intrusion Resilient Networks** *International Journal of Computer Networks And Applications* [[paper](https://doi.org/10.22247/ijcna/2026/09)]
- [2026] **SEER: Spectral Entropy Encoding of Roles for Context-Aware Attention-Based Design Pattern Detection** [[paper](https://arxiv.org/abs/2601.13334)]
- [2026] **Developer Perspectives on REST API Usability: A Study of REST API Guidelines** [[paper](https://arxiv.org/abs/2601.16705)]
- [2026] **Hybrid Orchestration of AI Services and Microservices in Cloud-Edge Collaboration** *IEEE Transactions on Mobile Computing* [[paper](https://doi.org/10.1109/tmc.2026.3654236)]
- [2026] **ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2504.18776)]
- [2026] **Survey on AI-Based Reliability and Anomaly Detection in Microservices** *International Journal of Computer Applications* [[paper](https://doi.org/10.5120/ijca2026926263)]
- [2026] **Protocol for Systematic Literature Review on Simulation Approaches for Microservice Architecture** *Brunel University London* [[paper](https://doi.org/10.17633/rd.brunel.31325641.v1)]
- [2026] **Evolution Patterns of Software-Architecture Smells** *Open MIND* [[paper](https://doi.org/10.18420/se2026_19)]
- [2026] **Evaluating the Consequences of Process Adjustment Patterns for Handling Software Architecture Uncertainties** *Lecture notes in business information processing* [[paper](https://doi.org/10.1007/978-3-032-22375-3_8)]
- [2026] **Cybersecurity and Resilience of Smart Grids: A Review of Threat Landscape, Incidents, and Emerging Solutions** *Applied Sciences* [[paper](https://doi.org/10.3390/app16020981)]
- [2026] **Benchmarking TabNet, NODE, and FT-Transformer for Software Defect Prediction: An Empirical Comparison and Explainability Analysis** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3656247)]
- [2026] **Edge-Optimized Vision Transformers: A Co-Designed Hardware-Software Framework for Efficient Attention Mechanism** *IEEE Transactions on Emerging Topics in Computing* [[paper](https://doi.org/10.1109/tetc.2026.3655830)]
- [2026] **Eco-Normalization as Diagnostic Architecture: A Cross-Case Analysis of Framework Requirements for Detecting Implementation Failure** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6598178)]
- [2026] **Design Pattern Prediction From Source Code Using LLM–Based Feature Engineering and SVM Classification** *IET Software* [[paper](https://doi.org/10.1049/sfw2/7163249)]
- [2026] **Edge computing System-on-Chip architecture for a Non-Intrusive Load Monitoring sensor in ambient intelligence applications** *Microprocessors and Microsystems* [[paper](https://doi.org/10.1016/j.micpro.2026.105250)]

##### 2025

- [2025] **Analysis of Design Patterns and Benchmark Practices in Apache Kafka Event-Streaming Systems** [[paper](https://arxiv.org/abs/2512.16146)]
- [2025] **Towards Benchmarking Design Pattern Detection Under Obfuscation: Reproducing and Evaluating Attention-Based Detection Method** [[paper](https://arxiv.org/abs/2512.07193)]
- [2025] **Hybrid-Code v2: Zero-Hallucination Clinical ICD-10 Coding via Neuro-Symbolic Verification and Automated Knowledge Base Expansion** [[paper](https://arxiv.org/abs/2512.23743)]
- [2025] **AI-Driven Anomaly Detection in Cloud-Native Microservices: The Night’s Watch Algorithm** *Applied Sciences* [[paper](https://doi.org/10.3390/app152312762)]
- [2025] **Hybrid Learning for Cold-Start-Aware Microservice Scheduling in Dynamic Edge Environments** *IEEE Transactions on Mobile Computing* [[paper](https://doi.org/10.1109/tmc.2025.3641936)]
- [2025] **Unsupervised Anomaly Detection in Cloud-Native Microservices via Cross-Service Temporal Contrastive Learning** [[paper](https://doi.org/10.1109/aibdf67964.2025.11440805)]
- [2025] **InfraLLM: A Generic Large Language Model Framework for Production-Grade Microservice Auto-Scaling in Cloud Infrastructure** *International Journal of Scientific Research and Modern Technology.* [[paper](https://doi.org/10.38124/ijsrmt.v4i11.1023)]
- [2025] **A Multi-Agent Coding Assistant for Cloud-Native Development: From Requirements to Deployable Microservices** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202512.1922.v1)]
- [2025] **Workload-Aware Machine Learning for Microservice Scaling in Kubernetes** *International Journal of Computational and Experimental Science and Engineering* [[paper](https://doi.org/10.22399/ijcesen.4546)]
- [2025] **The Role of Software Architectural Patterns in Blockchain Interoperability** [[paper](https://doi.org/10.1109/isaect68904.2025.11318717)]
- [2025] **RAG-Based AI Agents for Enterprise Software Development: Implementation Patterns and Production Deployment** *Frontiers in Artificial Intelligence Research* [[paper](https://doi.org/10.71465/fair456)]
- [2025] **Adaptive Software-Defined Perimeter Placement for Dynamic User Distributions in Zero-Trust Networks** *IEEE Transactions on Network Science and Engineering* [[paper](https://doi.org/10.1109/tnse.2025.3649680)]
- [2025] **An integrated graph neural network model for joint software defect prediction and code quality assessment** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-31209-5)]
- [2025] **Hybrid Cloud Strategy for Mission-Critical Financial Software Applications** *IJARCCE* [[paper](https://doi.org/10.17148/ijarcce.2025.1412136)]
- [2025] **Edge AI in Practice: A Survey and Deployment Framework for Neural Networks on Embedded Systems** *Electronics* [[paper](https://doi.org/10.3390/electronics14244877)]
- [2025] **Enabling AI in Healthcare: AWS Cloud Architecture for Scalable AI/ML Operations in Regulated Environments** *Universal library of engineering technology.* [[paper](https://doi.org/10.70315/uloap.ulete.2025.0204011)]
- [2025] **AI INTRUSION DETECTION SYSTEM USING GRAPH NEURAL NETWORKS FOR SOFTWARE DEFINED NETWORKS (SDN)** *International Journal of Apllied Mathematics* [[paper](https://doi.org/10.12732/ijam.v38i12s.1654)]
- [2025] **Designing LLM-based Multi-Agent Systems for Software Engineering Tasks: Quality Attributes, Design Patterns and Rationale** [[paper](https://arxiv.org/abs/2511.08475)]
- [2025] **Statistical Independence Aware Caching for LLM Workflows** [[paper](https://arxiv.org/abs/2511.22118)]
- [2025] **Adaptively diagnosing system faults in microservice architecture: An autonomous predictive model construction framework** *Future Generation Computer Systems* [[paper](https://doi.org/10.1016/j.future.2025.108256)]
- [2025] **Graph Neural AI with Temporal Dynamics for Comprehensive Anomaly Detection in Microservices** [[paper](https://doi.org/10.1109/wcniot67424.2025.11381337)]
- [2025] **Hierarchical Expert Multi-Agent Framework for Causal Root Cause Localization in Cloud-Native Microservices** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202511.0911.v1)]
- [2025] **Collaborative deployment of Large AI Models on the edge: A microservice approach to heterogeneous training and quantized inference** *Ad Hoc Networks* [[paper](https://doi.org/10.1016/j.adhoc.2025.104080)]
- [2025] **Agentic AI as the Next Evolution of Microservices** *International Journal of Science and Research (IJSR)* [[paper](https://doi.org/10.21275/sr251102171820)]
- [2025] **A microservices approach to scenario-based integration of smart mobility digital twins** [[paper](https://doi.org/10.1117/12.3093000)]
- [2025] **Real-Time Drilling Performance Monitoring Using AI-Enhanced Microservices and LLM Integration** [[paper](https://doi.org/10.2118/228955-ms)]
- [2025] **Experimenting Architectural Patterns in Federated Learning Systems** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112655)]
- [2025] **COSMOS: Performance Portable Graph Pattern Matching with Domain-Specific Software Distributed Shared Memory** [[paper](https://doi.org/10.1145/3712285.3759860)]
- [2025] **Anti-patterns Detection in Microservice-Based Software Architectures Using Graph Analysis** [[paper](https://doi.org/10.1109/icaea69058.2025.11301540)]
- [2025] **Scalable, High-Fidelity Monitoring of Application Communication Patterns in Vernier** [[paper](https://doi.org/10.1145/3731599.3767520)]
- [2025] **Enhancing Software Fault Prediction Using Swarm Intelligence and Deep Learning Approach: Optimizing Accuracy and Robustness** *SN Computer Science* [[paper](https://doi.org/10.1007/s42979-025-04426-y)]
- [2025] **Lingxi: Repository-Level Issue Resolution Framework Enhanced by Procedural Knowledge Guided Scaling** [[paper](https://arxiv.org/abs/2510.11838)]
- [2025] **Structural Generalization for Microservice Routing Using Graph Neural Networks** [[paper](https://doi.org/10.1109/aiac68175.2025.11332534)]
- [2025] **Multi-Objective Adaptive Rate Limiting in Microservices Using Deep Reinforcement Learning** [[paper](https://doi.org/10.1145/3778534.3778668)]
- [2025] **A Pattern-Based Framework for Automated Migration of Monolithic Applications to Microservices** *Big Data and Cognitive Computing* [[paper](https://doi.org/10.3390/bdcc9100253)]
- [2025] **A Systematic Literature Review on Fault Injection Testing of Microservice Systems** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2025.3621564)]
- [2025] **Multi-Dimensional Autoscaling in Microservices Using Reinforcement Learning** [[paper](https://doi.org/10.1109/mascots67699.2025.11283269)]
- [2025] **Consensus-based distributed orchestration framework for microservices in edge computing clusters** *Future Generation Computer Systems* [[paper](https://doi.org/10.1016/j.future.2025.108221)]
- [2025] **Between Promise and Pain: The Reality of Automating Failure Analysis in Microservices with LLMs** [[paper](https://doi.org/10.1145/3725783.3764388)]
- [2025] **Scalability in Microservices: A systematic literature review** *Journal of Computer Science and Technology* [[paper](https://doi.org/10.24215/16666038.25.e11)]
- [2025] **Zync: A microservice platform for IoT device management and complex event monitoring** *Computers & Electrical Engineering* [[paper](https://doi.org/10.1016/j.compeleceng.2025.110752)]
- [2025] **DRKC: Deep Reinforcement Learning Enhanced Microservice Scheduling on Kubernetes Clusters in Cloud-Edge Environment** *IEEE Transactions on Cloud Computing* [[paper](https://doi.org/10.1109/tcc.2025.3624031)]
- [2025] **IMPLEMENTASI ARSITEKTUR MICROSERVICE PADA APLIKASI BANK SAMPAH DIGITAL BERBASIS DONATJS** *CENDEKIA Jurnal Ilmu Pengetahuan* [[paper](https://doi.org/10.51878/cendekia.v5i4.7140)]
- [2025] **Quantifying Chaos Engineering Effectiveness In Event-Driven Microservices** *Journal of International Crisis and Risk Communication Research* [[paper](https://doi.org/10.63278/jicrcr.vi.3334)]
- [2025] **Training-Less Anomaly-Based Intrusion Detection In Containerized Microservices** [[paper](https://doi.org/10.3990/1.9789036569460)]
- [2025] **A novel adaptive transformer based quantum intrusion detection system for software defined networks** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-20356-4)]
- [2025] **Security Pattern Detection in Software Architectures** *QSpace (Queen's University Library)* [[paper](https://hdl.handle.net/1974/35365)]
- [2025] **AI-driven intrusion detection and mitigation framework for software-defined IoT networks** *Peer-to-Peer Networking and Applications* [[paper](https://doi.org/10.1007/s12083-025-02151-0)]
- [2025] **A Modular Architecture Framework for Flutter Using Clean Architecture and Design Patterns: A Software Quality Perspective** [[paper](https://doi.org/10.1109/icicos68590.2025.11330072)]
- [2025] **AI-Augmented Software Architecture: Autonomous Refactoring with Design Pattern Awareness** [[paper](https://doi.org/10.63282/3050-9246/icrtcsit-102)]
- [2025] **Electromagnetically Reconfigurable Fluid Antenna System for Wireless Communications: Design, Modeling, Algorithm, Fabrication, and Experiment** *IEEE Journal on Selected Areas in Communications* [[paper](https://doi.org/10.1109/jsac.2025.3625163)]
- [2025] **Invited Paper: APS: Open-Source Hardware-Software Co-Design Framework for Agile Processor Specialization** [[paper](https://doi.org/10.1109/iccad66269.2025.11240817)]
- [2025] **Are We SOLID Yet? An Empirical Study on Prompting LLMs to Detect Design Principle Violations** [[paper](https://arxiv.org/abs/2509.03093)]
- [2025] **A Policy-Driven Approach for Securing Microservices Workflow in Kubernetes Cluster** [[paper](https://doi.org/10.1109/clusterworkshops65972.2025.11164216)]
- [2025] **Concurrency-Aware Self-Duration and Hierarchical RCA for Deep Microservice Call Chains** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202509.2158.v1)]
- [2025] **Microservice Deployment in Space Computing Power Networks Via Robust Reinforcement Learning** *IEEE Transactions on Mobile Computing* [[paper](https://doi.org/10.1109/tmc.2025.3607488)]
- [2025] **A Comparative Study of Object-Oriented, Procedural, and Functional Programming Paradigms in Microservice Architecture** *VFAST Transactions on Software Engineering* [[paper](https://doi.org/10.21015/vtse.v13i3.2216)]
- [2025] **Cheminformatics Microservice V3: a web portal for chemical structure manipulation and analysis** *Journal of Cheminformatics* [[paper](https://doi.org/10.1186/s13321-025-01094-1)]
- [2025] **Energy–Latency-Aware Microservice Orchestration in Edge Computing via Node Ranking Matrix and Proportional Routing** *IEEE Internet of Things Journal* [[paper](https://doi.org/10.1109/jiot.2025.3615211)]
- [2025] **Toward Generating Microservice Architectures from Textual Requirements with Large Language Models** [[paper](https://doi.org/10.5753/sbcars.2025.14591)]
- [2025] **A Scalable Microservices Platform for Deploying Machine Learning Models in Drug Discovery and Beyond** *ChemRxiv* [[paper](https://doi.org/10.26434/chemrxiv-2025-thhkd)]
- [2025] **Visualizing and Exploring Data Access in Microservices Using Interactive Treemaps** [[paper](https://doi.org/10.1109/vissoft67405.2025.00012)]
- [2025] **Evaluating Strategies for Teaching Micro Frontends: Do Anti-patterns Help?** [[paper](https://doi.org/10.5753/sbes.2025.11029)]
- [2025] **Integrating AI Models into Production Software Systems: Architectural Patterns for Scalable Machine Learning Deployment** *Iconic Research and Engineering Journals* [[paper](https://doi.org/10.64388/irev9i3-1715615)]
- [2025] **WinVMJ Composer: Enabling Web-based Software Product Line Development** [[paper](https://doi.org/10.1145/3748269.3748489)]
- [2025] **Design Trade-offs in REST API Data Transfer Object Architecture: Centralized vs. Independent DTO Patterns in Enterprise Software Development** [[paper](https://doi.org/10.22541/au.175693403.35876810/v1)]
- [2025] **Genshin: A Generalized Framework with Software-Hardware Co-design and Pruned Fault Injection for Reliability Analysis** [[paper](https://doi.org/10.1109/itc58126.2025.00008)]
- [2025] **A Systematic Literature Review of Machine Learning Approaches for Migrating Monolithic Systems to Microservices** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3603897)]
- [2025] **Disruption-Aware Microservice Re-Orchestration for Cost-Efficient Multi-Cloud Deployments** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2025.3604373)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **A Pattern-Driven Software Architecture for Multi-Digital Twin Integration in Circular Systems** *Advances in transdisciplinary engineering* [[paper](https://doi.org/10.3233/atde260463)]
- [2026] **A federated observability architecture pattern for reliable agentic AI software systems across the AI software development lifecycle** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108260)]
- [2026] **Development of a Microservice Orchestrator for decentralised smart manufacturing systems** *Journal of Manufacturing Systems* [[paper](https://doi.org/10.1016/j.jmsy.2026.04.006)]
- [2026] **Automatic detection of software design patterns using a language model on transformer architecture** *Scientific and technical journal of information technologies mechanics and optics* [[paper](https://doi.org/10.17586/2226-1494-2026-26-2-324-330)]
- [2026] **Ontology-Aware Design Patterns for Clinical AI Systems: Translating Reification Theory into Software Architecture** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2604.01661)]
- [2026] **Graph-Based Contrastive Representation Learning for Predicting Performance Anomalies in Cloud and Microservice Platforms** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202602.0559.v1)]
- [2026] **MVCPVM: Model-View-Controller-Presenter-View Model - A Unified Architectural Pattern** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6376119)]
- [2026] **Four-Layer Architecture v2.0 — Integrated Runtime Safety and Structural Discovery Framework** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18443328)]
- [2026] **Automated Analysis and Augmented Reality Visualization of Software Module Architecture for Anti-Pattern Detection : dissertation to obtain the degree of Doctor of Philosophy** *Electronic Kyiv-Mohyla Academy Institutional Repository (National University of Kyiv-Mohyla Academy)* [[paper](https://ekmair.ukma.edu.ua/handle/123456789/40604)]

##### 2025

- [2025] **Data microservice composition optimization using deep reinforcement learning** *Future Generation Computer Systems* [[paper](https://doi.org/10.1016/j.future.2025.108290)]
- [2025] **Nookiin: Python software to build commensurable multilayer heterostructures** *Computer Physics Communications* [[paper](https://doi.org/10.1016/j.cpc.2025.110011)]
- [2025] **An Integrated Cybersecurity Framework for Software Development and Risk‐Aware Practices in the SDLC** *Journal of Software Evolution and Process* [[paper](https://doi.org/10.1002/smr.70075)]
- [2025] **Attention-Guided Graph Neural Networks with Adaptive Feature Selection for Explainable Software Defect Prediction** *Statistics Optimization & Information Computing* [[paper](https://doi.org/10.19139/soic-2310-5070-2906)]
- [2025] **Authentication Challenges and Solutions in Microservice Architectures** *Applied Sciences* [[paper](https://doi.org/10.3390/app152212088)]
- [2025] **Resilient microservices: an investigation into Istio effectiveness in Kubernetes** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05750-x)]
- [2025] **Polyglot Persistence in Microservices: Managing Data Diversity in Distributed Systems** [[paper](https://doi.org/10.1109/iotais67227.2025.11282136)]
- [2025] **A formal approach for security pattern enforcement in software architecture** *Computers & Security* [[paper](https://doi.org/10.1016/j.cose.2025.104749)]
- [2025] **VibeLayer Development: An Architectural Pattern for Long-Running Autonomous Software Development** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17734814)]
- [2025] **An Adaptive Dynamic Defense Strategy for Microservices Based on Deep Reinforcement Learning** *Electronics* [[paper](https://doi.org/10.3390/electronics14204096)]
- [2025] **Software Architecture Recovery Augmented With Semantics** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3620670)]
- [2025] **Autonomic Microservice Management via Agentic AI and MAPE-K Integration** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04403-7_11)]
- [2025] **AgriMicro—A Microservices-Based Platform for Optimization of Farm Decisions** *AgriEngineering* [[paper](https://doi.org/10.3390/agriengineering7090299)]
- [2025] **Performance prediction and resource adaptive adjustment for cloud-native microservices** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05437-3)]
- [2025] **Microsegmentation for containerized microservices in edge computing** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-443-34109-0.00011-5)]
- [2025] **Language Models as Architectural Gatekeepers: Automating Conformance Checking from Natural Language** [[paper](https://doi.org/10.5753/sbes.2025.11100)]
- [2025] **Agentic AI for Autonomous Micro-Frontend User Interfaces and Microservices Evolution in Cloud Platforms** *Journal of Computer Science and Technology Studies* [[paper](https://doi.org/10.32996/jcsts.2025.7.8.135)]
- [2025] **Enhancing REST API Handlers Organization for Node.js Microservices** *SN Computer Science* [[paper](https://doi.org/10.1007/s42979-025-04311-8)]
- [2025] **Transformer-based performance prediction and proactive resource allocation for cloud-native microservices** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05237-9)]
- [2025] **COMPARATIVE ANALYSIS OF THE EFFECTIVENESS OF ARCHITECTURAL STYLES REST, GRAPHQL, AND GRPC FOR SCALABLE MICROSERVICE SYSTEMS** *Herald of Khmelnytskyi National University Technical sciences* [[paper](https://doi.org/10.31891/2307-5732-2025-355-79)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Cloud-Native AI Workloads Using Microservice Architectures** *International Journal of Technical Research Studies (IJTRS)* [[paper](https://doi.org/10.63090/ijtrs/3139.1788.0008)]
- [2026] **An Empirical Evaluation of Large Language Models Applying Software Architectural Patterns** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202603.2486.v1)]
- [2026] **A Token-Governed Software Architectural Pattern for Public and Protected File Handling in Microservices-Based Refactoring of Legacy Systems: An Applied Case Study** *المجلة العلمية لكلية التربية النوعية جامعة دمياط* [[paper](https://doi.org/10.21608/sjeud.2026.471118.1076)]
- [2026] **Cloud Agents and the Third Era of AI-Driven Software Development: Architecture, Adoption Patterns, and Implications for the Software Engineering Discipline** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18856486)]
- [2026] **Understanding the issues, their causes and solutions in microservices systems: An empirical study** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112828)]
- [2026] **HGraphScale: Hierarchical Graph Learning for Autoscaling Microservice Applications in Container-Based Cloud Computing** *IEEE Transactions on Services Computing* [[paper](https://doi.org/10.1109/tsc.2026.3651267)]
- [2026] **PROPHET: Efficient and Intelligent Orchestrator for Microservices Scheduling and Scaling** *IEEE Transactions on Networking* [[paper](https://doi.org/10.1109/ton.2026.3658319)]
- [2026] **Architectural Design Patterns for Fault-Tolerant Distributed Software Systems** *International Journal of Advanced engineering Management and Science* [[paper](https://doi.org/10.22161/ijaems.123.1)]

##### 2025

- [2025] **An Empirical Study on Challenges of Event Management in Microservice Architectures** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3776581)]
- [2025] **Software Architecture Patterns for Real-Time Digital Twin–IoT in Smart Campus Management: A Comparative Study** [[paper](https://doi.org/10.1109/telecom66943.2025.11304092)]
- [2025] **MLOps with Microservices: A Case Study on the Maritime Domain** *Communications in computer and information science* [[paper](https://arxiv.org/abs/2506.06202)]
- [2025] **MIGRATING LEGACY HEALTHCARE SYSTEMS TO CLOUD-NATIVE MICROSERVICES WITH AI: BEST PRACTICES AND PITFALLS** *International Journal of Apllied Mathematics* [[paper](https://doi.org/10.12732/ijam.v38i2s.123)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Loop Engineering for Agentic Software Systems: LEAF Architecture, Pattern Taxonomy, Use Cases, Evaluation, Challenges, and Future Directions** [[paper](https://doi.org/10.13140/rg.2.2.13129.10081)]
- [2026] **Benefits of Being Bayesian: Motor Imagery EEG Classification (Thesis Software)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20415596)]
- [2026] **Benchmarking SQL and NoSQL Persistence in Microservices Under Variable Workloads** *Future Internet* [[paper](https://doi.org/10.3390/fi18010053)]
- [2026] **Design and Performance Evaluation of Event-Driven Microservices for Large-Scale Enterprise Data Processing** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6730598)]
- [2026] **Service-Level Energy Modeling and Experimentation for Cloud-Native Microservices** *Lecture notes in computer science* [[paper](https://arxiv.org/abs/2510.13447)]

##### 2025

- [2025] **Chaos experiments in microservice architectures: A systematic literature review** *Computer Standards & Interfaces* [[paper](https://doi.org/10.1016/j.csi.2025.104116)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Hidden or Formal Architects: Understanding Who Makes Architectural Decisions in Practice** [[paper](https://arxiv.org/abs/2607.11251)]
- [2026] **Schedulable Job-Level Dependencies for Cause-Effect Chains via Graph Neural Networks** [[paper](https://arxiv.org/abs/2607.02624)]
- [2026] **SAKE: Software Architectural Knowledge Evaluation Benchmark for Large Language Models** [[paper](https://arxiv.org/abs/2606.29520)]
- [2026] **Digital Sovereignty as a Quality Attribute for Software Architectures** [[paper](https://arxiv.org/abs/2606.31590)]
- [2026] **The ARDoCo Tool Landscape: REST API, TraceView, and TraceViz for Architecture Traceability** [[paper](https://arxiv.org/abs/2606.28064)]
- [2026] **CAPRA: Scaling Feedback on Software Architecture Deliverables with a Multi-Agent LLM System** [[paper](https://arxiv.org/abs/2606.18976)]
- [2026] **The EVerest Dataset for Secure Software Engineering** [[paper](https://arxiv.org/abs/2606.23197)]
- [2026] **How Software Engineering Students Use LLMs to Write Research Papers: An Experience Report** [[paper](https://arxiv.org/abs/2606.05114)]
- [2026] **Graphical-Probabilistic Modeling of Generative Flows in LLM-Native Software Systems** [[paper](https://arxiv.org/abs/2606.15943)]
- [2026] **Supporting the Adoption of Privacy-Enhancing Technologies through Requirements Engineering** [[paper](https://arxiv.org/abs/2606.17387)]
- [2026] **Evaluating Hardware Abstraction Layer Concepts for Software Defined Vehicles: Insights into Applicability and Effectiveness** [[paper](https://arxiv.org/abs/2607.00039)]
- [2026] **Beyond Models: Reflections on Engineering AI-enabled Systems in a Project-Based Course** [[paper](https://arxiv.org/abs/2606.16842)]
- [2026] **Engineering Reliable Autonomous Systems: Challenges and Solutions** [[paper](https://arxiv.org/abs/2606.23760)]
- [2026] **Mining Architectural Quality Under Agentic AI Adoption: A Causal Study of Java Repositories** [[paper](https://arxiv.org/abs/2606.13298)]
- [2026] **Quantum Software Architecture Framework (QSAF): A Component-Based Framework for Designing Hybrid Quantum-Classical Systems** [[paper](https://arxiv.org/abs/2605.01800)]
- [2026] **ProgramBench: Can Language Models Rebuild Programs From Scratch?** [[paper](https://arxiv.org/abs/2605.03546)]
- [2026] **LLM Consortium for Software Design Refinement: A Controlled Experiment on Multi-Agent Collaboration Topologies** [[paper](https://arxiv.org/abs/2606.01490)]
- [2026] **Governance-Aware Software Architecture for Multi-Stakeholder Platforms** [[paper](https://arxiv.org/abs/2605.31316)]
- [2026] **Towards LLM-Assisted Architecture Recovery for Real-World ROS~2 Systems: An Agent-Based Multi-Level Approach to Hierarchical Structural Architecture Reconstruction** [[paper](https://arxiv.org/abs/2605.20055)]
- [2026] **The Rise of the Software-Defined Vehicle: Architectures, Enabling Technologies, and Future Opportunities** [[paper](https://arxiv.org/abs/2605.30001)]
- [2026] **Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory** [[paper](https://arxiv.org/abs/2606.01385)]
- [2026] **Toward a Sustainable Software Architecture Community: Evaluating ICSA's Environmental Impact** [[paper](https://arxiv.org/abs/2604.04096)]
- [2026] **Benchmarking and Evaluating VLMs for Software Architecture Diagram Understanding** [[paper](https://arxiv.org/abs/2604.04009)]
- [2026] **CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models** [[paper](https://arxiv.org/abs/2604.05755)]
- [2026] **A Pattern Language for Resilient Visual Agents** [[paper](https://arxiv.org/abs/2604.28001)]
- [2026] **Supporting Belonging in Software Engineering Through Role Models Exposure** [[paper](https://arxiv.org/abs/2604.25099)]
- [2026] **Designing Adaptive Digital Nudging Systems with LLM-Driven Reasoning** [[paper](https://arxiv.org/abs/2604.11206)]
- [2026] **Fairness-First Design Thinking for Software Architecture** [[paper](https://arxiv.org/abs/2604.18055)]
- [2026] **Benchmarking Requirement-to-Architecture Generation with Hybrid Evaluation** [[paper](https://arxiv.org/abs/2604.06683)]
- [2026] **CIAO - Code In Architecture Out - Automated Software Architecture Documentation with Large Language Models** [[paper](https://arxiv.org/abs/2604.08293)]
- [2026] **One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption** [[paper](https://arxiv.org/abs/2604.27333)]
- [2026] **Can Large Language Models Assist the Comprehension of ROS2 Software Architectures?** [[paper](https://arxiv.org/abs/2604.21699)]
- [2026] **Towards Leveraging LLMs to Generate Abstract Penetration Test Cases from Software Architecture** [[paper](https://arxiv.org/abs/2603.23698)]
- [2026] **ArchBench: Benchmarking Generative-AI for Software Architecture Tasks** [[paper](https://arxiv.org/abs/2603.17833)]
- [2026] **A Human-Centred Architecture for Large Language Models-Cognitive Assistants in Manufacturing within Quality Management Systems** [[paper](https://arxiv.org/abs/2603.16325)]
- [2026] **Beyond Monolithic Models: Symbolic Seams for Composable Neuro-Symbolic Architectures** [[paper](https://arxiv.org/abs/2603.15087)]
- [2026] **Exploring the Reasoning Depth of Small Language Models in Software Architecture: A Multidimensional Evaluation Framework Towards Software Engineering 2.0** [[paper](https://arxiv.org/abs/2603.07091)]
- [2026] **LLM-based Automated Architecture View Generation: Where Are We Now?** [[paper](https://arxiv.org/abs/2603.21178)]
- [2026] **RAD-AI: Rethinking Architecture Documentation for AI-Augmented Ecosystems** [[paper](https://arxiv.org/abs/2603.28735)]
- [2026] **Towards Supporting Quality Architecture Evaluation with LLM Tools** [[paper](https://arxiv.org/abs/2603.28914)]
- [2026] **Software-heavy Asset Administration Shells: Classification and Use Cases** [[paper](https://arxiv.org/abs/2602.16499)]
- [2026] **AROLA: A Modular Layered Architecture for Scaled Autonomous Racing** [[paper](https://arxiv.org/abs/2602.02730)]
- [2026] **AgenticAKM : Enroute to Agentic Architecture Knowledge Management** [[paper](https://arxiv.org/abs/2602.04445)]
- [2026] **Evaluating Large Language Models for Detecting Architectural Decision Violations** [[paper](https://arxiv.org/abs/2602.07609)]
- [2026] **Sovereign-by-Design A Reference Architecture for AI and Blockchain Enabled Systems** [[paper](https://arxiv.org/abs/2602.05486)]
- [2026] **Compiling Large Multi-Modal Requirement Documents into Runnable Software Systems: From an Agentic Test-Driven Perspective** [[paper](https://arxiv.org/abs/2602.13723)]
- [2026] **GenAI for Systems: Recurring Challenges and Design Principles from Software to Silicon** [[paper](https://arxiv.org/abs/2602.15241)]
- [2026] **Systematic Literature Reviews on Microservice Architecture Mentioning the Role of Simulation** *Brunel University London* [[paper](https://doi.org/10.17633/rd.brunel.31325446.v2)]
- [2026] **Liquid Interfaces: A Dynamic Ontology for the Interoperability of Autonomous Systems** [[paper](https://arxiv.org/abs/2601.21993)]
- [2026] **From Scattered to Structured: A Vision for Automating Architectural Knowledge Management** [[paper](https://arxiv.org/abs/2601.19548)]

##### 2025

- [2025] **A Reference Architecture for Embedding Quantum Software Into Enterprise Systems** [[paper](https://arxiv.org/abs/2512.12009)]
- [2025] **Who's Who? LLM-assisted Software Traceability with Architecture Entity Recognition** [[paper](https://arxiv.org/abs/2511.02434)]
- [2025] **A Self-Improving Architecture for Dynamic Safety in Large Language Models** [[paper](https://arxiv.org/abs/2511.07645)]
- [2025] **Generating Software Architecture Description from Source Code using Reverse Engineering and Large Language Model** [[paper](https://arxiv.org/abs/2511.05165)]
- [2025] **Towards Realistic Project-Level Code Generation via Multi-Agent Collaboration and Semantic Architecture Modeling** [[paper](https://arxiv.org/abs/2511.03404)]
- [2025] **Collaborative LLM Agents for C4 Software Architecture Design Automation** [[paper](https://arxiv.org/abs/2510.22787)]
- [2025] **An AUTOSAR-Aligned Architectural Study of Vulnerabilities in Automotive SoC Software** [[paper](https://arxiv.org/abs/2510.07941)]
- [2025] **Efficient Integration of cross platform functions onto service-oriented architectures** [[paper](https://arxiv.org/abs/2510.27344)]
- [2025] **Tracing and Metrics Design Patterns for Monitoring Cloud-native Applications** [[paper](https://arxiv.org/abs/2510.02991)]
- [2025] **Full stack optimization of microservice architecture: systematic review and research opportunity** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05690-6)]
- [2025] **State-of-the-Art in Software Security Visualization: A Systematic Review** [[paper](https://arxiv.org/abs/2509.20385)]
- [2025] **SWE-QA: Can Language Models Answer Repository-level Code Questions?** [[paper](https://arxiv.org/abs/2509.14635)]

##### 2024

- [2024] **Microservices Architecture in Cloud Computing: A Comprehensive Analysis of Design Patterns, Scalability, and Performance** [[paper](https://doi.org/10.2139/ssrn.6579999)]

##### 2022

- [2022] **Microservices: Yesterday, Today, and Tomorrow** [[paper](https://arxiv.org/abs/2203.00001)]
- [2022] **Microservices Design Patterns** *Azure Kubernetes Services with Microservices* [[paper](https://doi.org/10.1007/978-1-4842-7809-3_3)]
- [2022] **Microservices: Architecting and Design Considerations** *Azure Kubernetes Services with Microservices* [[paper](https://doi.org/10.1007/978-1-4842-7809-3_2)]
- [2022] **Introduction to Microservices and AKS** *Azure Kubernetes Services with Microservices* [[paper](https://doi.org/10.1007/978-1-4842-7809-3_1)]
- [2022] **Structural Patterns and Chaining Processes** *Practical Event-Driven Microservices Architecture* [[paper](https://doi.org/10.1007/978-1-4842-7468-2_4)]

##### 2019

- [2019] **Patterns for Microservices-Centric Applications** *Essentials of Microservices Architecture* [[paper](https://doi.org/10.1201/9780429329920-8)]
- [2019] **Microservices Architecture** *Practical Microservices Architectural Patterns* [[paper](https://doi.org/10.1007/978-1-4842-4501-9_4)]
- [2019] **Distributed Computing Architecture Landscape** *Practical Microservices Architectural Patterns* [[paper](https://doi.org/10.1007/978-1-4842-4501-9_1)]
- [2019] **Axon for CQRS Architecture** *Practical Microservices Architectural Patterns* [[paper](https://doi.org/10.1007/978-1-4842-4501-9_12)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **An Empirical Comparison of Monolithic and Microservices Architectures for an E-Commerce Application** [[paper](https://arxiv.org/abs/2608.15668)]
- [2026] **Energy Efficiency in Microservice Architectures: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2608.04070)]
- [2026] **ORCA: Observability-Grounded Program Repair for Microservice Incidents** [[paper](https://arxiv.org/abs/2608.17018)]
- [2026] **GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices** [[paper](https://arxiv.org/abs/2608.08968)]
- [2026] **eIRWR: Enhanced Iterative Random Walk with Restart for Scalable Root Cause Analysis in Microservices** [[paper](https://arxiv.org/abs/2608.08073)]
- [2026] **Hybrid entropy–fuzzy weighted decision matrix (HEF-WDM) for the optimal software architecture pattern selection** *Applied Soft Computing* [[paper](https://doi.org/10.1016/j.asoc.2026.116220)]
- [2026] **Spanergy: Energy-aware Distributed Tracing for Microservices** [[paper](https://arxiv.org/abs/2607.24902)]
- [2026] **A Unified Feature Model for Microservice Identification and Refactoring** [[paper](https://arxiv.org/abs/2608.02644)]
- [2026] **Stochastic Connectivity as the Foundation of a Runtime Model for Microservice Availability Analysis** [[paper](https://arxiv.org/abs/2607.00740)]
- [2026] **SequenceFI: Non-intrusive Temporal Fault Injection for Microservice Systems** [[paper](https://arxiv.org/abs/2607.20050)]
- [2026] **Balancing Microservices and Monolithic Architectures** [[paper](https://arxiv.org/abs/2607.03898)]
- [2026] **KRCA: An Efficient Root Cause Analysis System in Hyper-scale Microservice Systems via Agentic AI** [[paper](https://arxiv.org/abs/2607.01788)]
- [2026] **Structural Validation of LLM-Generated Microservice Decompositions Using Source-Code Dependencies** [[paper](https://arxiv.org/abs/2607.28331)]
- [2026] **Fault Injection in OpenAPI Specifications for Evaluating Black-Box Testing Effectiveness** [[paper](https://arxiv.org/abs/2607.12101)]
- [2026] **Industrial Practice of LLM-Based Test Case Carving and Assertion Generation (Experience Paper)** [[paper](https://arxiv.org/abs/2607.24000)]
- [2026] **From Textual Requirements to Microservice Architectures - A Comprehensive Evaluation of LLM-Based Design Synthesis** [[paper](https://arxiv.org/abs/2607.28307)]
- [2026] **HTTP REST API Structure Learning** [[paper](https://arxiv.org/abs/2607.02442)]
- [2026] **OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis** [[paper](https://arxiv.org/abs/2607.11357)]
- [2026] **A literature review of recent advances in software design and architecture** [[paper](https://arxiv.org/abs/2607.26110)]
- [2026] **Analyzing the Evolution of Structural Communities within Microservice Architecture** [[paper](https://arxiv.org/abs/2606.04047)]
- [2026] **Organizational Cohesion in Microservice Architectures: A Multi-Project Empirical Study** [[paper](https://arxiv.org/abs/2606.16725)]
- [2026] **MicroAgent: Context-Augmented Multi-Agent Framework for Automatic Microservice Decomposition** [[paper](https://arxiv.org/abs/2606.29742)]
- [2026] **A Multi-Dataset Benchmark for Evaluating LLM Agents in Microservice Failure Diagnosis** [[paper](https://arxiv.org/abs/2606.29193)]
- [2026] **Anomaly Detection and Root Cause Analysis for Microservice Systems** [[paper](https://arxiv.org/abs/2606.09942)]
- [2026] **The Dependency Black Hole** [[paper](https://arxiv.org/abs/2606.25949)]
- [2026] **Microskill Architecture: A Modular Skill-Driven Framework for AI-Native Code Generation** [[paper](https://arxiv.org/abs/2606.05720)]
- [2026] **Hierarchical colored Petri nets for enforcing security patterns in software architecture** *Journal of Information Security and Applications* [[paper](https://doi.org/10.1016/j.jisa.2026.104530)]
- [2026] **From Sensors to On-Device Inference: An Embedded-to-Edge-AI Reference Architecture** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20784402)]
- [2026] **A Domain-Driven Design Simulator for Business Logic-Rich Microservice Systems** [[paper](https://arxiv.org/abs/2605.01159)]
- [2026] **Genetic Programming for Self-Adaptive Auto-Scaling of Microservices** [[paper](https://arxiv.org/abs/2605.01533)]
- [2026] **SmellDoc: Extending Elastic Stack for Microservice Bad Smell Detection and Visualization** [[paper](https://arxiv.org/abs/2605.24471)]
- [2026] **Can Graph-Based Microservice Performance Detection Be Used for Microservice Intrusion Detection?** [[paper](https://arxiv.org/abs/2605.24283)]
- [2026] **Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis** [[paper](https://arxiv.org/abs/2605.15569)]
- [2026] **Towards In-Depth Root Cause Localization for Microservices with Multi-Agent Recursion-of-Thought** [[paper](https://arxiv.org/abs/2605.14866)]
- [2026] **Making OpenAPI Documentation Agent-Ready: Detecting Documentation and REST Smells with a Multi-Agent LLM System** [[paper](https://arxiv.org/abs/2605.14312)]
- [2026] **LLM-Based Robustness Testing of Microservice Applications: An Empirical Study** [[paper](https://arxiv.org/abs/2605.14202)]
- [2026] **Software Architecture and Automation Patterns for Large-Scale Server Rack Validation** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-9581829/v1)]
- [2026] **E2E-REME: Towards End-to-End Microservices Auto-Remediation via Experience-Simulation Reinforcement Fine-Tuning** [[paper](https://arxiv.org/abs/2604.11094)]
- [2026] **Gamifying Architectural Governance to Reduce Organizational Coupling in Microservice Systems** [[paper](https://arxiv.org/abs/2604.22454)]
- [2026] **Key Developer Roles and Organizational Coupling in Microservices: A Longitudinal Analysis** [[paper](https://arxiv.org/abs/2604.25804)]
- [2026] **Which Types of Heterogeneity Matter for Root Cause Localization in Microservice Systems ?** [[paper](https://arxiv.org/abs/2604.26670)]
- [2026] **TORAI: Multi-source Root Cause Analysis for Blind Spots in Microservice Service Call Graph** [[paper](https://arxiv.org/abs/2604.13522)]
- [2026] **MIRAGE: Online LLM Simulation for Microservice Dependency Testing** [[paper](https://arxiv.org/abs/2604.04806)]
- [2026] **Log-based, Business-aware REST API Testing** [[paper](https://arxiv.org/abs/2604.08007)]
- [2026] **Rebooting Microreboot: Architectural Support for Safe, Parallel Recovery in Microservice Systems** [[paper](https://arxiv.org/abs/2604.09963)]
- [2026] **More Is Different: Toward a Theory of Emergence in AI-Native Software Ecosystems** [[paper](https://arxiv.org/abs/2604.19827)]
- [2026] **Gravity Well Codebase v0.4.1 — Compression, Wrapping, and Anchoring Microservice (EA-GW-01)** *Open MIND* [[paper](https://github.com/leesharks000/gravitywell)]
- [2026] **Can AI Agents Generate Microservices? How Far are We?** [[paper](https://arxiv.org/abs/2603.09004)]
- [2026] **Fuzzing Microservices in Face of Intrinsic Uncertainties** [[paper](https://arxiv.org/abs/2603.02551)]
- [2026] **Microservice Architecture Patterns for Scalable Machine Learning Systems** [[paper](https://arxiv.org/abs/2603.13672)]
- [2026] **An Empirical Study on How Architectural Topology Affects Microservice Performance and Energy Usage** [[paper](https://arxiv.org/abs/2604.00080)]
- [2026] **Q-GARS: Quantum-inspired Robust Microservice Chaining Scheduling** [[paper](https://arxiv.org/abs/2603.23127)]
- [2026] **Can an LLM Detect Instances of Microservice Infrastructure Patterns?** [[paper](https://arxiv.org/abs/2603.23073)]
- [2026] **Configurable Runtime Orchestration for Dynamic Data Retrieval in Distributed Systems** [[paper](https://arxiv.org/abs/2603.06980)]
- [2026] **Joint Temporal-Structural Representation Learning for Distributed Fault Discrimination in Microservice Architectures** [[paper](https://doi.org/10.1109/cisce69494.2026.11504875)]
- [2026] **Invariant-Driven Automated Testing** [[paper](https://arxiv.org/abs/2602.23922)]
- [2026] **Performance Antipatterns: Angel or Devil for Power Consumption?** [[paper](https://arxiv.org/abs/2602.12079)]
- [2026] **ModARO: A Modular Approach to Architecture Reconstruction of Distributed Microservice Codebases** [[paper](https://arxiv.org/abs/2602.08181)]
- [2026] **Cast: Automated Resilience Testing for Production Cloud Service Systems** [[paper](https://arxiv.org/abs/2602.00972)]
- [2026] **A Microservice-Based Platform for Sustainable and Intelligent SLO Fulfilment and Service Management** [[paper](https://arxiv.org/abs/2602.12875)]
- [2026] **PPTAMη: Energy Aware CI/CD Pipeline for Container Based Applications** [[paper](https://arxiv.org/abs/2602.12081)]
- [2026] **Automated Multi-Source Debugging and Natural Language Error Explanation for Dashboard Applications** [[paper](https://arxiv.org/abs/2602.15362)]
- [2026] **Structure-Aware Unified Modeling for Root Cause Localization in Microservice Systems Using Multi-Source Observability Data** [[paper](https://doi.org/10.1145/3813808.3813812)]
- [2026] **From Monolith to Microservices: A Comparative Evaluation of Decomposition Frameworks** [[paper](https://arxiv.org/abs/2601.23141)]
- [2026] **Hypothesize-Then-Verify: Speculative Root Cause Analysis for Microservices with Pathwise Parallelism** [[paper](https://arxiv.org/abs/2601.02736)]
- [2026] **FastFI: Enhancing API Call-Site Robustness in Microservice-Based Systems with Fault Injection** [[paper](https://arxiv.org/abs/2601.14800)]
- [2026] **RepoGenesis: Benchmarking End-to-End Microservice Generation from Readme to Repository** [[paper](https://arxiv.org/abs/2601.13943)] [[code](https://github.com/pzy2000/RepoGenesis)]
- [2026] **AnoMod: A Dataset for Anomaly Detection and Root Cause Analysis in Microservice Systems** [[paper](https://arxiv.org/abs/2601.22881)]
- [2026] **Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices** [[paper](https://arxiv.org/abs/2601.02732)]
- [2026] **LogicLens: Leveraging Semantic Code Graph to explore Multi Repository large systems** [[paper](https://arxiv.org/abs/2601.10773)]
- [2026] **AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems** [[paper](https://arxiv.org/abs/2601.09393)]
- [2026] **Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation** [[paper](https://arxiv.org/abs/2602.02584)]
- [2026] **A domain-specific language and architecture for detecting process activities from sensor streams in IoT** *Internet of Things* [[paper](https://arxiv.org/abs/2507.00686)]
- [2026] **Strategy Patterns to Handle Different Types of Software Architecture Uncertainties** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-19154-0_14)]
- [2026] **Design Patterns in Software Architecture: A Critical Analysis of Their Influence on Performance and Maintainability** [[paper](https://doi.org/10.18687/laccei2026.1.1.962)]
- [2026] **A Federated Observability Architecture Pattern for Reliable Agentic AI Software Systems Across the AI** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6098702)]
- [2026] **Large Language Models for Software Architecture Recovery from Source Code: Class Diagrams, Patterns, Styles, and Architecture-as-Code Views** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6381011)]
- [2026] **BEHAVIORAL SAFEGUARDS BY DESIGN: A COMPARATIVE ARCHITECTURAL ANALYSIS OF SOFTWARE DESIGN PATTERNS FOR MITIGATING PROBLEMATIC GAMBLING BEHAVIOR IN REAL-TIME SYSTEMS** [[paper](https://doi.org/10.13140/rg.2.2.12979.59680)]

##### 2025

- [2025] **MicroRacer: Detecting Concurrency Bugs for Cloud Service Systems** [[paper](https://arxiv.org/abs/2512.05716)]
- [2025] **PRAXIS: Integrating Program Analysis with Observability for Root-Cause Analysis** [[paper](https://arxiv.org/abs/2512.22113)]
- [2025] **Resilient Microservices: A Systematic Review of Recovery Patterns, Strategies, and Evaluation Frameworks** [[paper](https://arxiv.org/abs/2512.16959)]
- [2025] **Decoupling Adaptive Control in TeaStore** [[paper](https://arxiv.org/abs/2512.23495)]
- [2025] **Evaluating Asynchronous Semantics in Trace-Discovered Resilience Models: A Case Study on the OpenTelemetry Demo** [[paper](https://arxiv.org/abs/2512.12314)]
- [2025] **Reusability in MLOps: Leveraging Ports and Adapters to Build a Microservices Architecture for the Maritime Domain** [[paper](https://arxiv.org/abs/2512.08657)]
- [2025] **AdaptiFlow: An Extensible Framework for Event-Driven Autonomy in Cloud Microservices** [[paper](https://arxiv.org/abs/2512.23499)]
- [2025] **Adaptable TeaStore: A Choreographic Approach** [[paper](https://arxiv.org/abs/2512.23497)]
- [2025] **Legacy Modernization with AI -- Mainframe modernization** [[paper](https://arxiv.org/abs/2512.05375)]
- [2025] **Adaptable Teastore with Energy Consumption Awareness: A Case Study** [[paper](https://arxiv.org/abs/2512.23498)]
- [2025] **Natural Language Summarization Enables Multi-Repository Bug Localization by LLMs in Microservice Architectures** [[paper](https://arxiv.org/abs/2512.05908)]
- [2025] **Behavior-Driven Microservice Architecture** *Revista Abierta de Informática Aplicada* [[paper](https://doi.org/10.59471/raia2025227)]
- [2025] **FC-ADL: Efficient Microservice Anomaly Detection and Localisation Through Functional Connectivity** [[paper](https://arxiv.org/abs/2512.00844)]
- [2025] **MicroRemed: Benchmarking LLMs in Microservices Remediation** [[paper](https://arxiv.org/abs/2511.01166)] [[code](https://github.com/LLM4AIOps/MicroRemed)]
- [2025] **Microservices Are Dying, A New Method for Module Division Based on Universal Interfaces** [[paper](https://arxiv.org/abs/2511.04548)]
- [2025] **Root Cause Analysis for Microservice Systems via Cascaded Conditional Learning with Hypergraphs** [[paper](https://arxiv.org/abs/2511.17566)]
- [2025] **Offloading Data Center Tax** [[paper](https://arxiv.org/abs/2511.06558)]
- [2025] **Microservice architecture for securing distributed IoT** *Elsevier eBooks* [[paper](https://doi.org/10.1016/b978-0-44-333759-8.00019-8)]
- [2025] **Refactoring Towards Microservices: Preparing the Ground for Service Extraction** [[paper](https://arxiv.org/abs/2510.03050)]
- [2025] **DynaCausal: Dynamic Causality-Aware Root Cause Analysis for Distributed Microservices** [[paper](https://arxiv.org/abs/2510.22613)]
- [2025] **Key Considerations for Auto-Scaling: Lessons from Benchmark Microservices** [[paper](https://arxiv.org/abs/2510.02585)]
- [2025] **From Specification to Service: Accelerating API-First Development Using Multi-Agent Systems** [[paper](https://arxiv.org/abs/2510.19274)] [[code](https://github.com/sirbh/code-gen)]
- [2025] **SBOMproof: Beyond Alleged SBOM Compliance for Supply Chain Security of Container Images** [[paper](https://arxiv.org/abs/2510.05798)]
- [2025] **Trace Sampling 2.0: Code Knowledge Enhanced Span-level Sampling for Distributed Tracing** [[paper](https://arxiv.org/abs/2509.13852)]
- [2025] **Application Management in C-ITS: Orchestrating Demand-Driven Deployments and Reconfigurations** [[paper](https://arxiv.org/abs/2509.18793)] [[code](https://github.com/ika-rwth-aachen/application_manager)]
- [2025] **Componentization: Decomposing Monolithic LLM Responses into Manipulable Semantic Units** [[paper](https://arxiv.org/abs/2509.08203)]
- [2025] **Adaptive Root Cause Localization for Microservice Systems with Multi-Agent Recursion-of-Thought** [[paper](https://arxiv.org/abs/2508.20370)]
- [2025] **Software Patterns for the 21st Century: From Monolithic Designs to AI-Driven Architectures** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-7437898/v1)]
- [2025] **An efficient and resilient IoT architecture for smart grids via quantum key distribution and multi-homocryption encryption** *Quantum Information Processing* [[paper](https://doi.org/10.1007/s11128-025-04906-3)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **The financial implications of open innovation: Evidence from stock market reactions to public companies' open source software releases** *Research Policy* [[paper](https://doi.org/10.1016/j.respol.2026.105500)]

##### 2025

- [2025] **On the Impact of Message Brokers Implementations in the Choreography of Microservices** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-00137-5_1)]
- [2025] **Sparse-MoE: Syntax-Aware Multi-view Mixture of Experts for Long-Sequence Software Vulnerability Detection** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-95-3456-2_24)]
- [2025] **Rookie Mistakes: Measuring Software Quality in Student Projects to Guide Educational Enhancement** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04207-1_10)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **Fuzzing Microservice Resilience under Uncertainty with LLM-Guided Scenario Generation** [[paper](https://doi.org/10.1109/eei70303.2026.11640489)]
- [2026] **Evidence-Verified Root Cause Localization for Microservice Incidents under Tool and Telemetry Noise** [[paper](https://doi.org/10.1109/mlise70044.2026.11607508)]

##### 2025

- [2025] **WaveSurfer - Scheduling Irregular Pulsing Attacks on Microservice Autoscaling** [[paper](https://doi.org/10.1145/3744969.3748419)]

[⬆ Back to top](#paper-list)

### Programming Languages

#### Method

##### 2026

- [2026] **igraph 1.0 enables fast and robust network analysis across programming languages** *PLoS ONE* [[paper](https://arxiv.org/abs/2311.10260)]
- [2026] **Weighing and Reading the Dark Matter of a Language Model** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21274616)]
- [2026] **International Journal on Natural Language Computing** *International Journal on Natural Language Computing* [[paper](https://doi.org/10.5121/ijnlc)]
- [2026] **The Tail-Preserving Alternative: A Design Specification for Variance-Preserving Language Models, and the Political Economy of Why They Are Not Deployed (v1.0)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20587033)]
- [2026] **Healing Justice Practice Professional Development Program for Black K‐12 World Language Educators** *Foreign Language Annals* [[paper](https://doi.org/10.1111/flan.70059)]
- [2026] **International Journal of Programming Languages and Applications** *International Journal of Programming Languages and Applications* [[paper](https://arxiv.org/abs/1402.0087)]
- [2026] **irAE-GPT: leveraging large language models to identify immune-related adverse events in electronic health records and clinical trial datasets** *EBioMedicine* [[paper](https://doi.org/10.1016/j.ebiom.2026.106227)]
- [2026] **Consumption Types and Dynamic Regimes in Constrained Generative Systems: Refinement of the Irreversibility Axiom and SCC Classification of Asymptotic Behavior** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18839251)]
- [2026] **Prompt-Native Semantic Runtimes for Language Models: Inference-Time Semantic Governance, Provenance, Compression, and Document-Level Process Teaching** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19059674)]
- [2026] **A synthetic system for RNA-responsive pyroptosis based on type III-E CRISPR nuclease-protease** *Nature Communications* [[paper](https://doi.org/10.1038/s41467-026-69179-5)]
- [2026] **Overview of partial model query language** [[paper](https://doi.org/10.1201/9781003762614-75)]
- [2026] **The Programming Framework: A General Method for Process Analysis Using LLMs and Mermaid Visualization** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18463441)]
- [2026] **Programmed to please: the moral and epistemic harms of AI sycophancy** *AI and Ethics* [[paper](https://doi.org/10.1007/s43681-026-01007-4)]
- [2026] **Generation–grid–load–storage coordination for a park-level integrated energy microgrid under new-type power systems** *Energy Reports* [[paper](https://doi.org/10.1016/j.egyr.2025.108924)]
- [2026] **Automatic Programming via Large Language Models With Population Self-Evolution for Dynamic Fuzzy Job Shop Scheduling Problem** *IEEE Transactions on Fuzzy Systems* [[paper](https://doi.org/10.1109/tfuzz.2025.3650586)]
- [2026] **An Expressive Assertion Language for Quantum Programs** *Proceedings of the ACM on Programming Languages* [[paper](https://doi.org/10.1145/3776658)]
- [2026] **Videogame Programming & Education: Enhancing Programming Skills Through Unity Visual Scripting** *Computers* [[paper](https://doi.org/10.3390/computers15010068)]

##### 2025

- [2025] **Design and Experimental Validation of a Photocatalyst Recommender Based on a Large Language Model** *Angewandte Chemie International Edition* [[paper](https://doi.org/10.1002/anie.202514544)]
- [2025] **Escape rooms for learning programming: A systematic literature review** *Review of Education* [[paper](https://doi.org/10.1002/rev3.70123)]
- [2025] **Thematic insights into the impact of large language models on K-12 education in rural India from student volunteers’ perspectives** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-18047-1)]
- [2025] **How reliable are large language models in analyzing the quality of written lesson plans? A mixed-methods study from a teacher internship program** *Computers and Education Artificial Intelligence* [[paper](https://doi.org/10.1016/j.caeai.2025.100538)]
- [2025] **Modeling and dynamic analysis on spar-type floating offshore wind turbines system via structure-preserving iterative method** *Applied Mathematical Modelling* [[paper](https://doi.org/10.1016/j.apm.2025.116562)]
- [2025] **Language proficiency in translation and interpreting programs** *Translation and Interpreting Studies* [[paper](https://doi.org/10.1075/tis.24139.cil)]
- [2025] **Provide personalized programming learning for individuals based on large language models** *Alexandria Engineering Journal* [[paper](https://doi.org/10.1016/j.aej.2025.10.026)]
- [2025] **Intensional Differences Between Programming Languages: A Conceptual and Practical Analysis** *Philosophies* [[paper](https://doi.org/10.3390/philosophies10060129)]
- [2025] **AI literacy: A core practice in world language education** *Foreign Language Annals* [[paper](https://doi.org/10.1111/flan.70037)]
- [2025] **Neural Methods for Programming: A Comprehensive Survey and Future Directions** *Applied Sciences* [[paper](https://doi.org/10.3390/app152212150)]
- [2025] **Development of a health literacy-based hypertension self-management education program using sign language for Deaf individuals** *BMC Health Services Research* [[paper](https://doi.org/10.1186/s12913-025-13726-1)]
- [2025] **Type IV secretion systems: from structures to mechanisms** *The EMBO Journal* [[paper](https://doi.org/10.1038/s44318-025-00584-0)]
- [2025] **Cooling performance optimization of a novel L1−−-type structure for the forced air-cooled battery thermal management system** *International Journal of Heat and Fluid Flow* [[paper](https://doi.org/10.1016/j.ijheatfluidflow.2025.110085)]
- [2025] **Evaluation of a Series-Type Mount Structure for Electric Vehicle Suspension System** *Machines* [[paper](https://doi.org/10.3390/machines13100903)]
- [2025] **A Novel Vibration Control System for Active Mass Drivers Based on Dynamic Fractional-order Type-2 Fuzzy Model and Adaptive Fractional Derivative** *Journal of Vibration Engineering & Technologies* [[paper](https://doi.org/10.1007/s42417-025-02128-6)]
- [2025] **A systematic literature review and meta‐analysis of real‐world evidence on commercially available automated insulin delivery systems in people with type 1 diabetes** *Diabetes Obesity and Metabolism* [[paper](https://doi.org/10.1111/dom.70161)]
- [2025] **Strengthening the Aging Brain: Functional Connectivity Changes After a Language-Based Cognitive Program** *Brain Sciences* [[paper](https://doi.org/10.3390/brainsci15111139)]
- [2025] **Integrating Low-Code Data Flow programming and mruby for Efficient IoT Development** [[paper](https://doi.org/10.1109/dasc68382.2025.00031)]
- [2025] **Program execution summarization by novel design pattern specification, detection, and consolidation techniques** *Array* [[paper](https://doi.org/10.1016/j.array.2025.100555)]
- [2025] **Plang: Efficient prompt engineering language for blending natural language and control flow in large language models** *Expert Systems with Applications* [[paper](https://doi.org/10.1016/j.eswa.2025.130118)]
- [2025] **Policy Search through Genetic Programming and LLM-assisted Curriculum Learning** *ACM Transactions on Evolutionary Learning and Optimization* [[paper](https://doi.org/10.1145/3772718)]
- [2025] **Large language models as a catalyst for opportunity recognition capability** *International Journal of Entrepreneurial Behaviour & Research* [[paper](https://doi.org/10.1108/ijebr-08-2024-0815)]
- [2025] **Design and transient analysis of a novel type passive residual heat removal system** *Nuclear Engineering and Design* [[paper](https://doi.org/10.1016/j.nucengdes.2025.114446)]
- [2025] **Battery types and recent developments for energy storage in electric vehicles: technical criteria and battery management system** *Clean Energy* [[paper](https://doi.org/10.1093/ce/zkaf048)]
- [2025] **Mechanical and optical effects of post-curing time and device type in two 3D-printed resin systems** *BMC Oral Health* [[paper](https://doi.org/10.1186/s12903-025-06813-6)]
- [2025] **Robust PID-Type Iterative Learning Control for Nonlinear Square and Nonsquare Systems** *IEEE Transactions on Neural Networks and Learning Systems* [[paper](https://doi.org/10.1109/tnnls.2025.3601656)]
- [2025] **Glycaemic control and variability with different commercially available hybrid closed loop systems in people with type 1 diabetes: A systematic review and meta‐analysis of randomized controlled trials** *Diabetes Obesity and Metabolism* [[paper](https://doi.org/10.1111/dom.70150)]
- [2025] **Real-World Effectiveness of the MiniMed™ 780G Advanced Hybrid Closed-Loop System for People ≥65 Years with Type 1 or Type 2 Diabetes in the United States** *Diabetes Technology & Therapeutics* [[paper](https://doi.org/10.1177/15209156251376654)]
- [2025] **Development of in-situ permeability testing system for low-permeability sandstone-type uranium deposits** *ADVANCES IN GEO-ENERGY RESEARCH* [[paper](https://doi.org/10.46690/ager.2025.10.06)]
- [2025] **The Heart in Space: Effects of Microgravity on Different Cell Types and Their Functions in the Cardiovascular System** *Biomedicines* [[paper](https://doi.org/10.3390/biomedicines13102336)]
- [2025] **A Bayesian decision support system for automated insulin doses in adults with type 1 diabetes on multiple daily injections: a randomized controlled trial** *Nature Communications* [[paper](https://doi.org/10.1038/s41467-025-63671-0)]
- [2025] **Genomic profiling and experimental validation of type VI secretion system-associated proteins in Klebsiella** *PLoS Genetics* [[paper](https://doi.org/10.1371/journal.pgen.1011878)]
- [2025] **Dual-actuator-type active noise control in vibro-acoustic systems with openings** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-17810-8)]
- [2025] **In Search of Beautiful Molecules: A Perspective on Generative Modeling for Drug Design** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c01203)]
- [2025] **CoderAgent: Simulating Student Behavior for Personalized Programming Learning with Large Language Models** [[paper](https://doi.org/10.24963/ijcai.2025/34)]
- [2025] **Preparing teachers for the algorithmic educational landscape: A critical mapping of generative AI integration in language teacher education** *Technology in Language Teaching & Learning* [[paper](https://doi.org/10.29140/tltl.v7n2.102841)]
- [2025] **Sustainable and Inclusive Education Reform in Türkiye: A Cipp Evaluation of the Primary Turkish Language Curriculum** *Sustainability* [[paper](https://doi.org/10.3390/su17198659)]
- [2025] **THE ROLE OF TECHNOLOGICAL SYSTEMS IN MANAGING AND EVALUATING THE LANGUAGE TEACHING PROGRAM** *Wiralodra English Journal* [[paper](https://doi.org/10.31943/wej.v9i2.406)]
- [2025] **Agents are all you need: Pioneering the use of agentic artificial intelligence to embrace large language models into dairy science** *Journal of Dairy Science* [[paper](https://doi.org/10.3168/jds.2025-26775)]
- [2025] **Pre-service language teachers’ experiences and perceptions of integrating generative AI in practicum-based lesson study** *Humanities and Social Sciences Communications* [[paper](https://doi.org/10.1057/s41599-025-05715-w)]
- [2025] **Portrait Of Arabic Language Immersion Program In Indonesian Islamic Colleges** *Ijaz Arabi Journal of Arabic Learning* [[paper](https://doi.org/10.18860/ijazarabi.v8i3.33064)]
- [2025] **Housing Policy and the Housing System** [[paper](https://doi.org/10.4324/9781003670735)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **Sound Enforcement of Dynamic Release Information Flow Policy-Full Version** [[paper](https://arxiv.org/abs/2608.09506)]
- [2026] **Let it Flow: A Formally Verified Compilation Framework for Asynchronous Dataflow** [[paper](https://arxiv.org/abs/2608.05451)]
- [2026] **Categorical Models of Amortized Cost: An Adjoint Relationship between Cost and Potential** [[paper](https://arxiv.org/abs/2608.09635)]
- [2026] **GPU Offload in Rust: Portable, Safe, and Fast** [[paper](https://arxiv.org/abs/2608.13759)]
- [2026] **Refined^2 Environment Classifiers** [[paper](https://arxiv.org/abs/2608.07888)]
- [2026] **Mixed Choice Multiparty Session Types, Precisely** [[paper](https://arxiv.org/abs/2608.10704)]
- [2026] **Staying Productive Under the Palm Trees. On Graded Coeffect Typing in the Tropical Semiring** [[paper](https://arxiv.org/abs/2608.02596)]
- [2026] **P4-SpecTec: Integrating a Language Mechanization Framework into the Real-World P4 Specification** [[paper](https://arxiv.org/abs/2608.00639)]
- [2026] **Renaming or Tightness: Enforcing Disjunctive Information Flow Policies** [[paper](https://arxiv.org/abs/2608.09120)]
- [2026] **Logical Foundations of Two-Sided Type Theory** [[paper](https://arxiv.org/abs/2607.14325)]
- [2026] **Linearising Explicit Substitutions using Intersection Types** [[paper](https://arxiv.org/abs/2607.20179)]
- [2026] **Practical Range Refinement Types with Inference** [[paper](https://arxiv.org/abs/2607.00824)]
- [2026] **Imprecise Probabilistic Programming, Precisely: Credal Sets via Graded Monads, BDDs, and Semiring-Parametric Inference (Functional Pearl)** [[paper](https://arxiv.org/abs/2607.20801)]
- [2026] **Causality in Pure Quantum Computation with Quantum Control** [[paper](https://arxiv.org/abs/2607.15926)]
- [2026] **KernelScript: Cross-Boundary Typed DSL for eBPF Applications** [[paper](https://arxiv.org/abs/2607.23900)]
- [2026] **Kani: A Model Checker for Rust** [[paper](https://arxiv.org/abs/2607.01504)]
- [2026] **The Duality of Information Flow: Reconciling Robust Downgrading with Non-Interference** [[paper](https://arxiv.org/abs/2607.17445)]
- [2026] **Top-down = Bottom-up: Sound and Complete Characterisations of Liveness by Multiparty Global Protocols** [[paper](https://arxiv.org/abs/2607.21489)]
- [2026] **Type Safety via Hoare Logic with Separation and Pure Types** [[paper](https://arxiv.org/abs/2607.25262)]
- [2026] **Definitional Inversion, Without Normalisation** [[paper](https://arxiv.org/abs/2607.13662)]
- [2026] **Bidirectional Elaborators à la Carte** [[paper](https://arxiv.org/abs/2607.09564)]
- [2026] **GLP: A Grassroots, Multiagent, Concurrent, Logic Programming Language for AI** [[paper](https://arxiv.org/abs/2607.21189)]
- [2026] **Quantum Systems at The Brink: Helium–Type Systems** *Archive for Rational Mechanics and Analysis* [[paper](https://arxiv.org/abs/1908.04883)]
- [2026] **When Types Intersect and Effects Get Handled** [[paper](https://arxiv.org/abs/2606.09526)]
- [2026] **Formal Semantics and Type System for Vega Data Transformations** [[paper](https://arxiv.org/abs/2606.15013)]
- [2026] **CANONIC: Governance Is Compilation** [[paper](https://arxiv.org/abs/2607.05410)]
- [2026] **Effect Systems as Abstract Interpretations** [[paper](https://arxiv.org/abs/2606.19686)]
- [2026] **A Typestate Approach to Purpose-aware Programming** [[paper](https://arxiv.org/abs/2606.26386)]
- [2026] **Same Coeffect, Different Base: Connecting Two Dominant Approaches to Graded Types** [[paper](https://arxiv.org/abs/2606.28042)]
- [2026] **Dynamic Software Updates using CRDTs** [[paper](https://arxiv.org/abs/2606.10920)]
- [2026] **Kasteran* — Programming Language Design Principles — Compiler, Programming Languages, Type Theory, Sovereign AI, and Post-Cloud Architecture (Kasteran)** *OSF Preprints (OSF Preprints)* [[paper](https://osf.io/zt9m7)]
- [2026] **Categorical Message Passing Language (CaMPL) for programmers** [[paper](https://arxiv.org/abs/2605.09491)]
- [2026] **Automated Amortised Analysis of Skew Heaps and Leftist Heaps (Extended Version)** [[paper](https://arxiv.org/abs/2605.12091)]
- [2026] **Pacing Types for Asynchronous Stream Equations** [[paper](https://arxiv.org/abs/2605.26635)]
- [2026] **Towards Formal Verification of Hybrid Synchronous Programs with Refinement Types** [[paper](https://arxiv.org/abs/2605.04377)]
- [2026] **LFPL: Revisited and Mechanized** [[paper](https://arxiv.org/abs/2605.12893)]
- [2026] **First-Class Refinement Types for Scala** [[paper](https://arxiv.org/abs/2605.08369)]
- [2026] **Static Type Checking for Database Access Code** [[paper](https://arxiv.org/abs/2605.02569)]
- [2026] **Ordered Adjoint Logic** [[paper](https://arxiv.org/abs/2605.19112)]
- [2026] **Ownership Refinement Types for Pointer Arithmetic and Nested Arrays** [[paper](https://arxiv.org/abs/2604.22361)]
- [2026] **act: Technical report** [[paper](https://arxiv.org/abs/2604.02955)]
- [2026] **Linear Constraints** [[paper](https://arxiv.org/abs/2604.21467)]
- [2026] **Finite Functional Programming** [[paper](https://arxiv.org/abs/2604.26161)]
- [2026] **JTON: A Token-Efficient JSON Superset with Zen Grid Tabular Encoding for Large Language Models** [[paper](https://arxiv.org/abs/2604.05865)]
- [2026] **Proceedings 17th Workshop on Programming Language Approaches to Concurrency and Communication-cEntric Software** [[paper](https://arxiv.org/abs/2604.05737)]
- [2026] **NEURA: A Unified and Retargetable Compilation Framework for Coarse-Grained Reconfigurable Architectures** [[paper](https://arxiv.org/abs/2604.04236)] [[code](https://github.com/coredac/neura)]
- [2026] **Trustworthy Clinical Decision Support Using Meta-Predicates and Domain-Specific Languages** [[paper](https://arxiv.org/abs/2604.21263)]
- [2026] **Vectorial solutions for a class of Hartree-Fock type systems with the double coupled feature** *Advances in Differential Equations* [[paper](https://doi.org/10.57262/ade031-0708-513)]
- [2026] **VerusBelt: A Semantic Foundation for Verus's Proof-Oriented Extensions to the Rust Type System (Artifact)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19613067)]
- [2026] **Failing with Purpose: Dangling Coverage-Guided Negative Test Generation from a Mechanized P4 Type System** *Open MIND* [[paper](https://github.com/kaist-plrg/p4-spectec/tree/concrete)]
- [2026] **Software Artifact for &quot;CMakeSonar: A Static Approach to Detecting CMake Bugs with a Fine-Grained Type System&quot;** *Artifact Digital Object Group* [[paper](https://doi.org/10.1145/3747415)]
- [2026] **DSFB Structural Semiotics Engine for Robotics Health Monitoring: A Deterministic Augmentation Layer for Typed Residual Interpretation of Joint Degradation, Actuator Drift, and Kinematic Anomalies in Safety-Critical Robotic Systems** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19778382)]
- [2026] **Syntax-Directed Semantics in Programming Language Design** *Iconic Research and Engineering Journals* [[paper](https://doi.org/10.64388/irev9i10-1716556)]
- [2026] **Integrating AI-TPACK for Pre-Service Teachers: Applications and Challenges in English Language Program** *Journal of Nusantara Education* [[paper](https://doi.org/10.57176/jn.v5i2.207)]
- [2026] **Tracking Capabilities for Safer Agents** [[paper](https://arxiv.org/abs/2603.00991)]
- [2026] **Set-Theoretic Types for Erlang: Theory, Implementation, and Evaluation** [[paper](https://arxiv.org/abs/2603.22032)]
- [2026] **On Representability of Multiple-Valued Functions by Linear Lambda Terms Typed with Second-order Polymorphic Type System** [[paper](https://arxiv.org/abs/2603.25337)]
- [2026] **Towards verifying unsafe Rust programs against Rust's pointer-aliasing restrictions** [[paper](https://arxiv.org/abs/2603.28326)]
- [2026] **A Core Calculus for Type-safe Product Lines of C Programs** [[paper](https://arxiv.org/abs/2603.04013)]
- [2026] **Type-safe Monitoring of Parameterized Streams** [[paper](https://arxiv.org/abs/2603.11104)]
- [2026] **Dimensional Type Systems and Deterministic Memory Management: Design-Time Semantic Preservation in Native Compilation** [[paper](https://arxiv.org/abs/2603.16437)]
- [2026] **Decidable By Construction: Design-Time Verification for Trustworthy AI** [[paper](https://arxiv.org/abs/2603.25414)]
- [2026] **Popov stability and nonlinear control of El Borhamy–Rashad–Sobhy Duffing-type system** *International Journal of Dynamics and Control* [[paper](https://doi.org/10.1007/s40435-026-02018-z)]
- [2026] **Circular One/Two/Three-dimensional Consecutive k-Type Systems** *Methodology And Computing In Applied Probability* [[paper](https://doi.org/10.1007/s11009-026-10250-5)]
- [2026] **Well-posedness, absolute boundary stabilization and numerical results for a nonlinear Timoshenko-Ehrenfest type system** *Discrete and Continuous Dynamical Systems - S* [[paper](https://doi.org/10.3934/dcdss.2026100)]
- [2026] **Large Language Models for manufacturing** *Journal of Manufacturing Systems* [[paper](https://doi.org/10.1016/j.jmsy.2026.02.014)]
- [2026] **Impact of Coding as Another Language-KIBO kindergarten curriculum on preschool children’s computational thinking skills in programming and non-programming contexts** *Thinking Skills and Creativity* [[paper](https://doi.org/10.1016/j.tsc.2026.102193)]
- [2026] **Uniqueness is Separation** [[paper](https://arxiv.org/abs/2602.06386)]
- [2026] **Type-Based Enforcement of Non-Interference for Choreographic Programming** [[paper](https://arxiv.org/abs/2602.21630)]
- [2026] **Global Protocols under Rendezvous Synchrony: From Realizability to Type Checking** [[paper](https://arxiv.org/abs/2602.09197)]
- [2026] **A Flow Extension to Coroutine Types for Deadlock Detection in Go** [[paper](https://arxiv.org/abs/2602.19686)]
- [2026] **RustyDL: A Program Logic for Rust** [[paper](https://arxiv.org/abs/2602.22075)]
- [2026] **Programming Backpropagation with Reverse Handlers for Arrows** [[paper](https://arxiv.org/abs/2602.18090)]
- [2026] **Practical Refinement Session Type Inference (Extended Version)** [[paper](https://arxiv.org/abs/2602.06715)]
- [2026] **Handling Exceptions and Effects with Automatic Resource Analysis** [[paper](https://arxiv.org/abs/2603.02260)]
- [2026] **Contextual MetaML: Syntax and Full Abstraction** [[paper](https://arxiv.org/abs/2602.03033)]
- [2026] **Meta-Monomorphizing Specializations** [[paper](https://arxiv.org/abs/2602.12973)]
- [2026] **A Lorenz-Type System and Application in Switching Converter** *International Journal of Bifurcation and Chaos* [[paper](https://doi.org/10.1142/s021812742650080x)]
- [2026] **Existence and limiting profiles of normalized solutions to critical Choquard type systems** *Journal d Analyse Mathématique* [[paper](https://doi.org/10.1007/s11854-026-0435-2)]
- [2026] **Tunable 2D atomic localization via azimuthal quantum number in a four-level tripod-type system** *Journal of Applied Physics* [[paper](https://doi.org/10.1063/5.0302871)]
- [2026] **Parametric investigation of arm-length effects on novel hybrid wave energy converters: performance enhancement through integration of Wavestar units with two-raft-type system** *Energy Conversion and Management* [[paper](https://doi.org/10.1016/j.enconman.2026.121286)]
- [2026] **Document 237: THE TRAVERSAL GRAMMAR — Logotic Programming Extension Module v0.6 — Crimson Hexagon Archive** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18480959)]
- [2026] **Dependently-Typed AARA: A Non-Affine Approach for Resource Analysis of Higher-Order Programs** [[paper](https://arxiv.org/abs/2601.12943)]
- [2026] **Formalization and Implementation of Safe Destination Passing in Pure Functional Programming Settings** [[paper](https://arxiv.org/abs/2601.08529)]
- [2026] **Remarks on Algebraic Reconstruction of Types and Effects** [[paper](https://arxiv.org/abs/2601.15455)]
- [2026] **Handling Scope Checks (Extended Version)** [[paper](https://arxiv.org/abs/2601.18793)]
- [2026] **Contextual Metaprogramming for Session Types** [[paper](https://arxiv.org/abs/2601.15180)]
- [2026] **morloc: a workflow language for multi-lingual programming under a common type system.** *PeerJ Comput. Sci.* [[paper](https://dblp.org/rec/journals/peerj-cs/Arendsee26)]
- [2026] **Let Generalization, Polymorphic Recursion, and Variable Minimization in Boolean-Kinded Type Systems** *Proceedings of the ACM on Programming Languages* [[paper](https://doi.org/10.1145/3776644)]
- [2026] **Linear two-dimensional consecutive k-type systems in multi-state case** *Reliability Engineering & System Safety* [[paper](https://doi.org/10.1016/j.ress.2026.112215)]
- [2026] **When Lifetimes Liberate: A Type System for Arenas with Higher-Order Reachability Tracking (Artifact)** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18370268)]
- [2026] **Artifact for: Let Generalization, Polymorphic Recursion, and Variable Minimization in Boolean-Kinded Type Systems** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17346848)]
- [2026] **Opportunities and Challenges of 2D p‐Type Semiconductors: From Material Systems to Electronic and Optoelectronic Device Applications** *Advanced Functional Materials* [[paper](https://doi.org/10.1002/adfm.202531994)]
- [2026] **Finite-time stability for Caputo–Hadamard type fractional differential systems without and with proportional delays** *Chaos An Interdisciplinary Journal of Nonlinear Science* [[paper](https://doi.org/10.1063/5.0311074)]
- [2026] **Design and Implementation of a Compiler for a Reversible Object-Oriented Programming Language** *Publication Server of Goethe University Frankfurt am Main (Goethe University Frankfurt)* [[paper](https://doi.org/10.25716/thm-426)]
- [2026] **Programming language design ergonomics forCompetitive Programming** *Theseus (Ammattikorkeakoulujen)* [[paper](https://www.theseus.fi/handle/10024/913656)]
- [2026] **Aria Programming Language** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18240247)]
- [2026] **SARL: Agent-Oriented Programming Language —Retrospective and Prospective Analysis** [[paper](https://doi.org/10.1007/978-3-032-01082-7_2)]
- [2026] **The Jus Programming Language: Towards a Functional Language for Secure and Verifiable Smart Contracts on Tezos** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-3-032-01234-0_11)]
- [2026] **Limiting Inconsistencies in Legal Languages** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6805778)]

##### 2025

- [2025] **Belobog: Move Language Fuzzing Framework For Real-World Smart Contracts** [[paper](https://arxiv.org/abs/2512.02918)]
- [2025] **NVLang: Unified Static Typing for Actor-Based Concurrency on the BEAM** [[paper](https://arxiv.org/abs/2512.05224)]
- [2025] **Simple Modal Types for Functional Reactive Programming** [[paper](https://arxiv.org/abs/2512.09412)]
- [2025] **Existence and concentration of normalized solutions for logarithmic Schrödinger–Bopp–Podolsky type system** *Proceedings of the Royal Society of Edinburgh Section A Mathematics* [[paper](https://doi.org/10.1017/prm.2025.10117)]
- [2025] **Agronomic performance of cocoa production type systems in Colombia** *PLoS ONE* [[paper](https://doi.org/10.1371/journal.pone.0337624)]
- [2025] **Qualitative analysis of the nonlinear Ψ-Hilfer fractional neutral-type delayed integro-differential stochastic system: existence, uniqueness and controllability** *International Journal of Systems Science* [[paper](https://doi.org/10.1080/00207721.2025.2602081)]
- [2025] **Natural-Law-Type Conditions for Persistent Self-Modifying Systems with Predictive Semantics** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17896036)]
- [2025] **Exploring the potential and limitations of large language models for novice program fault localization** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112731)]
- [2025] **<scp>galápagos</scp> : Automated N-Version Programming with LLMs** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3785363)]
- [2025] **A Synthetic Reconstruction of Multiparty Session Types (with Appendix)** [[paper](https://arxiv.org/abs/2511.22692)]
- [2025] **A Word Sampler for Well-Typed Functions** [[paper](https://arxiv.org/abs/2512.01036)]
- [2025] **TypeDis: A Type System for Disentanglement** [[paper](https://arxiv.org/abs/2511.23358)]
- [2025] **Filling the Gaps of Polarity: Implementing Dependent Data and Codata Types with Implicit Arguments** [[paper](https://arxiv.org/abs/2511.15819)] [[project](https://polarity-lang.github.io/)]
- [2025] **On Circuit Description Languages, Indexed Monads, and Resource Analysis** [[paper](https://arxiv.org/abs/2511.22419)]
- [2025] **A programming language combining quantum and classical control** [[paper](https://arxiv.org/abs/2511.22537)]
- [2025] **Omnidirectional type inference for ML: principality any way** [[paper](https://arxiv.org/abs/2511.10343)]
- [2025] **All for One and One for All: Program Logics for Exploiting Internal Determinism in Parallel Programs** [[paper](https://arxiv.org/abs/2511.23283)]
- [2025] **Introducing Linear Implication Types to λ_{GT} for Computing With Incomplete Graphs** [[paper](https://arxiv.org/abs/2510.17429)]
- [2025] **A Complementary Approach to Incorrectness Typing** [[paper](https://arxiv.org/abs/2510.13725)]
- [2025] **Learning to Guarantee Type Correctness in Code Generation through Type-Guided Program Synthesis** [[paper](https://arxiv.org/abs/2510.10216)]
- [2025] **SafeFFI: Efficient Sanitization at the Boundary Between Safe and Unsafe Code in Rust and Mixed-Language Applications** [[paper](https://arxiv.org/abs/2510.20688)]
- [2025] **Imperative Quantum Programming with Ownership and Borrowing in Guppy** [[paper](https://arxiv.org/abs/2510.13082)]
- [2025] **Concept-Based Generic Programming in C++** [[paper](https://arxiv.org/abs/2510.08969)]
- [2025] **Internalizing Extensions in Lattices of Type Theories** [[paper](https://arxiv.org/abs/2510.26839)]
- [2025] **Typing Strictness (Extended Version)** [[paper](https://arxiv.org/abs/2510.16133)]
- [2025] **Exploiting the Potential of Linearity in Automatic Differentiation and Computational Cryptography** [[paper](https://arxiv.org/abs/2510.17220)]
- [2025] **JAX Autodiff from a Linear Logic Perspective (Extended Version)** [[paper](https://arxiv.org/abs/2510.16883)]
- [2025] **Free to Move: Reachability Types with Flow-Sensitive Effects for Safe Deallocation and Ownership Transfer** [[paper](https://arxiv.org/abs/2510.08939)]
- [2025] **Deciding not to Decide: Sound and Complete Effect Inference in the Presence of Higher-Rank Polymorphism** [[paper](https://arxiv.org/abs/2510.20532)]
- [2025] **GLP: A Grassroots, Multiagent, Concurrent, Logic Programming Language for AI (Full Version)** [[paper](https://arxiv.org/abs/2510.15747)]
- [2025] **A hybrid neural network-based model for quick prediction of clean energy harvesting performance by a VIV-type system** *Energy* [[paper](https://doi.org/10.1016/j.energy.2025.138882)]
- [2025] **On the Formal Metatheory of the Pure Type Systems using One-sorted Variable Names and Multiple Substitutions** *Electronic Proceedings in Theoretical Computer Science* [[paper](https://arxiv.org/abs/2510.12300)]
- [2025] **Qualitative study on Sobolev-type delayed fractional stochastic impulsive system: existence and controllability** *Applicable Analysis* [[paper](https://doi.org/10.1080/00036811.2025.2574705)]
- [2025] **Exploring motivation, willingness to communicate, and intercultural competence development in digital language exchanges: An integrative theoretical approach** *Computers in Human Behavior Reports* [[paper](https://doi.org/10.1016/j.chbr.2025.100819)]
- [2025] **Towards Repository-Level Program Verification with Large Language Models** [[paper](https://arxiv.org/abs/2509.25197)]
- [2025] **Historical visual question answering with large language model for Augmented Reality-assisted Human–Robot Collaboration** *Journal of Manufacturing Systems* [[paper](https://doi.org/10.1016/j.jmsy.2025.10.005)]
- [2025] **ILA: Correctness via Type Checking for Fully Homomorphic Encryption** [[paper](https://arxiv.org/abs/2509.11559)]
- [2025] **Quantum Simulation Programming via Typing** [[paper](https://arxiv.org/abs/2509.17343)]
- [2025] **Navigating the Python Type Jungle** [[paper](https://arxiv.org/abs/2509.13022)]
- [2025] **A Verified Compiler for Quantum Simulation** [[paper](https://arxiv.org/abs/2509.18583)]
- [2025] **Code Less to Code More: Streamlining Language Server Protocol and Type System Development for Language Families** [[paper](https://arxiv.org/abs/2509.15150)]
- [2025] **Pacing Types: Safe Monitoring of Asynchronous Streams** [[paper](https://arxiv.org/abs/2509.06724)]
- [2025] **Committing to the bit: Relational programming with semiring arrays and SAT solving** [[paper](https://arxiv.org/abs/2509.22614)]
- [2025] **Type-Based Incorrectness Reasoning** [[paper](https://arxiv.org/abs/2509.01511)]
- [2025] **When Lifetimes Liberate: A Type System for Arenas with Higher-Order Reachability Tracking** [[paper](https://arxiv.org/abs/2509.04253)]
- [2025] **Asymptotic Controllability of Coupled Fractional Stochastic Sobolev-Type Systems with a Nonlocal Condition** *Fractal and Fractional* [[paper](https://doi.org/10.3390/fractalfract9090594)]
- [2025] **Nonlinear dynamic behavior research of a coupling thin beam system by designing a magnetic internal beam-type coupling nonlinear energy sink in theoretical and experimental** *Chaos Solitons & Fractals* [[paper](https://doi.org/10.1016/j.chaos.2025.117156)]
- [2025] **Promoting the use of the Python programming language to analyze contextualized situations on derivatives and integrals considering the fundamental theorem of calculus** *Eurasia Journal of Mathematics Science and Technology Education* [[paper](https://doi.org/10.29333/ejmste/16885)]
- [2025] **Modeling teacher education students’ adoption of large language models through an extended technology acceptance framework** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-03298-9)]
- [2025] **Instructional design for teaching analytical chemistry in English as a foreign language** *Journal of Physics Conference Series* [[paper](https://doi.org/10.1088/1742-6596/3105/1/012013)]
- [2025] **Sampled-Data Control for Time-Scale-Type Systems Under Denial-of-Service Attacks** *IEEE Transactions on Cybernetics* [[paper](https://doi.org/10.1109/tcyb.2025.3599242)]
- [2025] **PySTH: A Python program for calculating and analyzing theoretical solar-to-hydrogen efficiency** *Computer Physics Communications* [[paper](https://doi.org/10.1016/j.cpc.2025.109822)]

##### 2024

- [2024] **Teaching Type Systems Implementation with Stella, an Extensible Statically Typed Programming Language.** *TFPIE* [[paper](https://dblp.org/rec/journals/corr/abs-2407-08089)]
- [2024] **A Type Theory of Leelus Type System in C++ Programming Language.** [[paper](https://doi.org/10.14293/s2199-1006.1.sor-.ppzqlti.v1)]
- [2024] **PCubeS Type Architecture and IT Programming Language** [[paper](https://doi.org/10.18130/v3m319)]
- [2024] **Table 7: Dataset distribution by smell type and programming language.** [[paper](https://doi.org/10.7717/peerj-cs.3642/table-7)]
- [2024] **Information technology. Programming languages, their environments and system software interfaces. Programming language COBOL** [[paper](https://doi.org/10.3403/30385411)]
- [2024] **Information technology. Programming languages, their environments and system software interfaces. Programming language ISLISP** [[paper](https://doi.org/10.3403/01206946u)]

##### 2022

- [2022] **A Meta-Probabilistic-Programming Language for Bisimulation of Probabilistic and Non-Well-Founded Type Systems.** *AGI* [[paper](https://dblp.org/rec/conf/agi/WarrellPVG22)]

##### 2021

- [2021] **A Functional Reactive Programming Language for Small-Scale Embedded Systems with Recursive Data Types.** *J. Inf. Process.* [[paper](https://dblp.org/rec/journals/jip/YokoyamaMW21)]

##### 2020

- [2020] **Implementing a Language for Distributed Systems: Choices and Experiences with Type Level and Macro Programming in Scala.** *Art Sci. Eng. Program.* [[paper](https://dblp.org/rec/journals/programming/WeisenburgerS20)]
- [2020] **Corrigendum to &quot;Type-driven Gradual Security with References, &quot; by Toro et al., ACM Transactions on Programming Languages and Systems (TOPLAS) Volume 40, Issue 4, Article No. 16.** *ACM Trans. Program. Lang. Syst.* [[paper](https://dblp.org/rec/journals/toplas/ToroGT20)]

##### 2018

- [2018] **A Unified System Modelling and Programming Language based on JavaScript and a Semantic Type System** *Procedia Manufacturing* [[paper](https://doi.org/10.1016/j.promfg.2018.06.005)]

##### 2017

- [2017] **TYPE ANALYSIS FOR THE PREDICATE PROGRAMMING LANGUAGE** *System Informatics* [[paper](https://doi.org/10.31144/si.2307-6410.2017.n9.p1-22)]

##### 2013

- [2013] **A Tour of C++: Type Safety and Resource Management** *Communications of the ACM* [[paper](https://doi.org/10.1145/2504585.2504603)]
- [2013] **Type inference for Python programming language** *Proceedings of the Institute for System Programming of RAS* [[paper](https://doi.org/10.15514/ispras-2013-24-9)]

##### 2012

- [2012] **Type systems directed programming language evolution: overview and research trends.** *ACM Southeast Regional Conference* [[paper](https://dblp.org/rec/conf/ACMse/Nino12)]

##### 2008

- [2008] **Sound and Complete Type Inference for a Systems Programming Language.** *APLAS* [[paper](https://dblp.org/rec/conf/aplas/SridharSS08)]

##### 2006

- [2006] **A Typed Hybrid Description Logic Programming Language with Polymorphic Order-Sorted DL-Typed Unification for Semantic Web Type Systems.** *OWLED* [[paper](https://dblp.org/rec/conf/owled/Paschke06)]
- [2006] **A Typed Hybrid Description Logic Programming Language with Polymorphic Order-Sorted DL-Typed Unification for Semantic Web Type Systems** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-cs-0610006)]
- [2006] **Strongly typed memory areas programming systems-level data structures in a functional language.** *Haskell* [[paper](https://dblp.org/rec/conf/haskell/DiatchkiJ06)]
- [2006] **Language Primitives and Type Discipline for Structured Communication-Based Programming Revisited: Two Systems for Higher-Order Session Communication.** *SecReT@ICALP* [[paper](https://dblp.org/rec/journals/entcs/YoshidaV07)]

##### 2004

- [2004] **A simple and powerful type system for programming languages.** *J. Syst. Softw.* [[paper](https://dblp.org/rec/journals/jss/Ayres04)]

##### 1998

- [1998] **On Polymorphic Type Systems for Imperative Programming Languages: An Approach using Sets of Types and Subprograms.** *ECOOP Workshops* [[paper](https://dblp.org/rec/conf/ecoopw/Holzmuller98)]

##### 1994

- [1994] **Engineering a Programming Language: The Type and Class System of Sather.** *Programming Languages and System Architectures* [[paper](https://dblp.org/rec/conf/plsa/SzyperskiOM94)]
- [1994] **Type Test Elimination Using Typeflow Analysis.** *Programming Languages and System Architectures* [[paper](https://dblp.org/rec/conf/plsa/CorneyG94)]
- [1994] **Is Oberon as Simple as Possible? A Smaller Object-Oriented Language Based on the Concept of Module Type.** *Programming Languages and System Architectures* [[paper](https://dblp.org/rec/conf/plsa/Radenski94)]

##### 1992

- [1992] **The Type System of a Higher-Order Logic Programming Language.** *Types in Logic Programming* [[paper](https://dblp.org/rec/books/mit/pfenning92/NadathurP92)]

##### 1990

- [1990] **An Incremental Type Inference System for the Programming Language Id** [[paper](https://doi.org/10.21236/ada230085)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Chain-type memristive maps featuring extreme multistability and their application in DCSK systems** *The European Physical Journal Plus* [[paper](https://doi.org/10.1140/epjp/s13360-026-07301-8)]

##### 2025

- [2025] **AutoIOT: LLM-Driven Automated Natural Language Programming for AIoT Applications** [[paper](https://doi.org/10.1145/3680207.3723486)]
- [2025] **The Effect of Social–Emotional Learning Programs on Elementary and Middle School Students’ Academic Achievement: A Meta-Analytic Review** *Behavioral Sciences* [[paper](https://doi.org/10.3390/bs15111527)]
- [2025] **Insights into Language Integration Programs: Perspectives from Adult Learners in a Bilingual Context** *Instructed Second Language Acquisition* [[paper](https://doi.org/10.3138/isla-2025-0007)]
- [2025] **Translanguaging as a Mediator to Motivate, Support, and Engage Students in a Chinese‐Medium Instruction Program** *International Journal of Applied Linguistics* [[paper](https://doi.org/10.1111/ijal.70025)]
- [2025] **Evaluation of the effects of dynamic pressure and emitter type on clogging in drip irrigation systems** *Agricultural Water Management* [[paper](https://doi.org/10.1016/j.agwat.2025.109916)]
- [2025] **Electrochemical energy storage systems: A review of types/functionalities, management systems and integration for real-life applications** *Next research.* [[paper](https://doi.org/10.1016/j.nexres.2025.100936)]
- [2025] **Adsorption of dithiophosphate‐type collectors with different substituent types on the acanthite surface in the CaO system** *Rare Metals* [[paper](https://doi.org/10.1007/s12598-025-03560-z)]
- [2025] **Beyond pathogenicity: applications of the type III secretion system (T3SS) of Pseudomonas aeruginosa** *Frontiers in Microbiology* [[paper](https://doi.org/10.3389/fmicb.2025.1663945)]
- [2025] **A “3+2” Cooperation Pattern of Amphipathic AIE Phototheranostic System for Multimodal Image‐Guided Synergistic Type I/II Photodynamic‐Photothermal Therapy** *Advanced Science* [[paper](https://doi.org/10.1002/advs.202507956)]
- [2025] **BinMetric: A Comprehensive Binary Code Analysis Benchmark for Large Language Models** [[paper](https://doi.org/10.24963/ijcai.2025/858)]
- [2025] **Wybe: Design of a Programming Language** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202509.0517.v1)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Simple Programming Language Designed for Low-Level Embedded Systems** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18914439)]
- [2026] **The type VI secretion system of Acinetobacter: mechanisms, biology and therapeutic potential** *Communications Biology* [[paper](https://doi.org/10.1038/s42003-026-09782-w)]
- [2026] **A new type of aircraft icing detection system** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-30681-3)]
- [2026] **A Study of LLMs’ Preferences for Libraries and Programming Languages** [[paper](https://arxiv.org/abs/2503.17181)]

##### 2025

- [2025] **Type IV secretion systems: reconciling diversity through a unified nomenclature** *FEMS Microbiology Reviews* [[paper](https://doi.org/10.1093/femsre/fuaf069)]
- [2025] **Experimental study of the thermal and power generation performance of a new type of water-cooling photovoltaic/thermal system** *Applied Thermal Engineering* [[paper](https://doi.org/10.1016/j.applthermaleng.2025.129352)]
- [2025] **AI-Based Anomaly Detection in Industrial Control and Cyber–Physical Systems: A Data-Type-Oriented Systematic Review** *Electronics* [[paper](https://doi.org/10.3390/electronics15010020)]
- [2025] **Speech to Reality: On-Demand Production using Natural Language, 3D Generative AI, and Discrete Robotic Assembly** [[paper](https://doi.org/10.1145/3745778.3766670)]
- [2025] **A Survey on Feedback Types in Automated Programming Assessment Systems** *ACM Transactions on Computing Education* [[paper](https://doi.org/10.1145/3773911)]
- [2025] **Identifying a type of toxic effectors exported by the type VII secretion system to enhance competitive fitness in Streptococcus suis** *Frontiers in Cellular and Infection Microbiology* [[paper](https://doi.org/10.3389/fcimb.2025.1685307)]
- [2025] **A Solver‐Aided Hierarchical Language for LLM‐Driven CAD Design** *Computer Graphics Forum* [[paper](https://doi.org/10.1111/cgf.70250)]
- [2025] **Automated Insulin Delivery Systems and Glucose Management in Children and Adolescents With Type 1 Diabetes** *Archives of Pediatrics and Adolescent Medicine* [[paper](https://doi.org/10.1001/jamapediatrics.2025.2740)]
- [2025] **Evaluation of the shear performance of different connectors in bamboo-concrete composite systems: Dowel-type and notched-type** *Engineering Structures* [[paper](https://doi.org/10.1016/j.engstruct.2025.121383)]
- [2025] **Optimal dispatch of integrated energy system with CCUS-P2G coupling and hydrogen-doped gas equipment based on ladder-type carbon trading mechanism** *Energy* [[paper](https://doi.org/10.1016/j.energy.2025.138397)]
- [2025] **TableTalk: Scaffolding Spreadsheet Development with a Language Agent** *ACM Transactions on Computer-Human Interaction* [[paper](https://doi.org/10.1145/3765286)]
- [2025] **Parallel courseware for adaptable programming learning: concept, design, and evaluation** *Educational Technology Research and Development* [[paper](https://doi.org/10.1007/s11423-025-10553-3)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Automated Insulin Delivery Systems in Type 2 Diabetes Mellitus: A Systematic Review and Meta-analysis** *Diabetes Care* [[paper](https://doi.org/10.2337/dc25-2435)]
- [2026] **Functional regulation and cross-talk of type III and type VI secretion systems in <i>Salmonella</i>** *Virulence* [[paper](https://doi.org/10.1080/21505594.2026.2645873)]

##### 2025

- [2025] **Functional divergence and regulatory network of the type VI secretion system in <i>Vibrio parahaemolyticus</i>** *Journal of Bacteriology* [[paper](https://doi.org/10.1128/jb.00378-25)]
- [2025] **Practical implementation and challenges of current batch-type RO systems and future potential: A review** *Desalination* [[paper](https://doi.org/10.1016/j.desal.2025.119404)]
- [2025] **Ghrelin-GHSR-LEAP2 system in the pathophysiology of type 2 diabetes** *iScience* [[paper](https://doi.org/10.1016/j.isci.2025.113573)]
- [2025] **Mapping the ethnolinguistic vitality of the Subanen language: socio-economic influences on language attitudes and sustainability** *Cogent Arts and Humanities* [[paper](https://doi.org/10.1080/23311983.2025.2553171)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **Decomposable Type Highlighting for Bidirectional Type and Cast System** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2607.13727)]
- [2026] **Impact of type 2 diabetes on malignancies of the female reproductive system** *Molecular Aspects of Medicine* [[paper](https://doi.org/10.1016/j.mam.2026.101459)]
- [2026] **Design of the Nectar Programming Language.** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18451965)]

##### 2025

- [2025] **Developmental validation of the SF 28CS typing system: a robust 6-dye multiplex for forensic human identification** *International Journal of Legal Medicine* [[paper](https://doi.org/10.1007/s00414-025-03653-5)]
- [2025] **SPELL: A Programming Language Designed for Large Language Models** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17826540)]
- [2025] **The type VI secretion system and associated effector proteins** *Nature Reviews Microbiology* [[paper](https://doi.org/10.1038/s41579-025-01256-w)]
- [2025] **Mechanisms of Pseudomonas aeruginosa resistance to type VI secretion system attacks** *Nature Communications* [[paper](https://doi.org/10.1038/s41467-025-65777-x)]
- [2025] **Enteric nervous system-derived VIP restrains differentiation of LGR5+ stem cells toward the secretory lineage impeding type 2 immune programs** *Nature Immunology* [[paper](https://doi.org/10.1038/s41590-025-02325-1)]
- [2025] **A ubiquitin-like protein controls assembly of a bacterial type VIIb secretion system** *Science Advances* [[paper](https://doi.org/10.1126/sciadv.ady9587)]
- [2025] **Regional encoding of enteric nervous system responses to microbiota and type 2 inflammation** *Science* [[paper](https://doi.org/10.1126/science.adr3545)]
- [2025] **Optimization and assessment of membrane-type floating photovoltaic (FPV) systems** *Energy* [[paper](https://doi.org/10.1016/j.energy.2025.138783)]
- [2025] **A widely-occurring family of pore-forming effectors broadens the impact of the Serratia Type VI secretion system** *The EMBO Journal* [[paper](https://doi.org/10.1038/s44318-025-00587-x)]
- [2025] **A dual-functional adsorption-photocatalysis system driven by interfacial charge dynamics in a type-II 3D/2D CdIn2S4/nickel metal–organic layer heterojunction for environmental purification and water splitting** *Journal of Colloid and Interface Science* [[paper](https://doi.org/10.1016/j.jcis.2025.139230)]
- [2025] **Photophysical Properties of π-Conjugated Donor–Acceptor–Donor Systems: Influence of Acceptor Type and Donor Segment Length** *The Journal of Organic Chemistry* [[paper](https://doi.org/10.1021/acs.joc.5c02007)]
- [2025] **Functional RNA splitting drove the evolutionary emergence of type V CRISPR-Cas systems from transposons** *Cell* [[paper](https://doi.org/10.1016/j.cell.2025.09.004)]
- [2025] **New Study on Impulsive Fractional Neutral-type Stochastic System with Nonlocal Conditions: Existence and Approximate Controllability** *Complex Analysis and Operator Theory* [[paper](https://doi.org/10.1007/s11785-025-01775-7)]
- [2025] **Anti-plasmid defense in hypervirulent <i>Klebsiella pneumoniae</i> involves Type I-like and Type IV restriction modification systems** *Emerging Microbes & Infections* [[paper](https://doi.org/10.1080/22221751.2025.2558877)]
- [2025] **Starch crystalline types modulate myofibrillar protein aggregation and its functional properties in gelling and emulsifying systems** *Food Chemistry* [[paper](https://doi.org/10.1016/j.foodchem.2025.146268)]
- [2025] **Two New Types of Evolution in Quantitative Reaction Systems** [[paper](https://doi.org/10.1109/sisy67000.2025.11205421)]
- [2025] **Feedforward-type Low-level Control for an Active Seat Suspension Servodrive System** [[paper](https://doi.org/10.1109/edpe66853.2025.11224204)]
- [2025] **Current status of Liraglutide delivery systems for the management of type 2 diabetes mellitus** *Drug Delivery and Translational Research* [[paper](https://doi.org/10.1007/s13346-025-01965-y)]
- [2025] **A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system–exported toxins** *Proceedings of the National Academy of Sciences* [[paper](https://doi.org/10.1073/pnas.2503581122)]
- [2025] **Dynamic interaction of oligodendrocyte precursor cells with other cell types in the central nervous system** *Neurochemistry International* [[paper](https://doi.org/10.1016/j.neuint.2025.106050)]
- [2025] **Cryo-EM structure of a type VI secretion system-delivered membrane-depolarizing toxin involved in bacterial antagonism** *Cell Reports* [[paper](https://doi.org/10.1016/j.celrep.2025.116263)]
- [2025] **Model Meets Knowledge: Analyzing Knowledge Types for Conversational Recommender Systems** [[paper](https://doi.org/10.1145/3705328.3748152)]
- [2025] **Well-posedness and asymptotic behavior of a suspension bridge system of Timoshenko–Ehrenfest type with fractional derivative damping** *Acta Mechanica* [[paper](https://doi.org/10.1007/s00707-025-04486-4)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Reformation and Practical Implementation of the Advanced Programming Language Design Course Tailored for the Artificial Intelligence and Cyber Security** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-12313-8_21)]

##### 2025

- [2025] **Sustainable Software Development: New Challenges for Programming, Language Design and Analysis** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-08187-2_10)]
- [2025] **Programming Language Design and Implementation** *Texts in computer science* [[paper](https://doi.org/10.1007/978-3-031-93299-1)]
- [2025] **Let’s Take Esoteric Programming Languages Seriously** [[paper](https://arxiv.org/abs/2505.15327)]
- [2025] **Leveraging ChatGPT for personalized reflective learning in programming education: effects on self-efficacy, higher-order thinking, and project implementation skills** *Education and Information Technologies* [[paper](https://doi.org/10.1007/s10639-025-13733-z)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **Justice-Centered Educational Programming Language Design** *ACM Transactions on Computing Education* [[paper](https://doi.org/10.1145/3811022)]

[⬆ Back to top](#paper-list)

### Human Factors & DX

#### Method

##### 2026

- [2026] **The Economics of AI-Assisted Coding: Evidence, Cost Benchmarks, and an Investment Framework for Developer Productivity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21985778)]
- [2026] **A Simplified Spiking Neural Network for Developer Experience Classification Using Software Engineering Metrics** *Engineering Technology & Applied Science Research* [[paper](https://doi.org/10.48084/etasr.19085)]
- [2026] **Replication Package for: Understanding ADHD Developers' Challenges Through the Lens of Developer Experience: A Qualitative Study of the r/ADHD_Programmers Community on Reddit** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32162535)]
- [2026] **Replication Package of How Developers Experience Debugging Unfamiliar Codebases with Code Tours Generated and Evaluated by Local LLMs** *Open MIND* [[paper](https://github.com/balfroim/HumanFactorsCodeTour/tree/zenodo)]
- [2026] **Empowering Developer Productivity through Platform Engineering** [[paper](https://doi.org/10.1002/9781394395910.ch1)]
- [2026] **Skill-Augmented AI Coding Agents: A Two-Layer Framework for SKILL.md Design and Developer Productivity** *International Journal of Multidisciplinary and Innovative Research* [[paper](https://doi.org/10.58806/ijmir.2026.v3i6n03)]
- [2026] **A Framework for Evaluating Developer Experience-Oriented Transparency in Software Ecosystem Portals** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20576475)]
- [2026] **A Survey-Based Empirical Evaluation of Clean Architecture: Perceived Effects on Software Quality and Developer Productivity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20676263)]
- [2026] **Exploring Perspectives of Software Developers on AI Tool Use and Productivity: A Literature Review and Empirical Findings** *Työväentutkimus Vuosikirja* [[paper](https://hdl.handle.net/10138/632077)]
- [2026] **Towards an Understanding of Developer Experience-Oriented Transparency in Software Ecosystems** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.16898932)]
- [2026] **Code Review Quality and Software Reliability: The Mediating Role of Defect Detection and the Moderating Role of Developer Experience** *ComputeX - Journal of Emerging Technology & Applied Science* [[paper](https://doi.org/10.71317/computex.2.2.2026.369)]
- [2026] **MEASURING SOFTWARE DEVELOPER PRODUCTIVITY: REVIEW OF APPROACHES AND THEIR LIMITATIONS** *E-Journal VFU* [[paper](https://doi.org/10.53606/evfu.25.620-628)]
- [2026] **Software Applications in the Era of Cloud, Microservices, and Artificial Intelligence: A Study on Scalability and Developer Productivity** *International Scientific Journal of Engineering and Management* [[paper](https://doi.org/10.55041/isjem06814)]
- [2026] **AI-Assisted Collaboration: Exploring Developer Experience with GitHub Copilot and Windsurf** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2026.3671677)]
- [2026] **Navigating innovation in sports apparel: a qualitative study of product developer experiences** *Journal of Fashion Marketing and Management* [[paper](https://doi.org/10.1108/jfmm-04-2025-0179)]
- [2026] **Is Code All That Matters? Investigating How Technical Documentation Quality Affects Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19102162)]
- [2026] **Mission SPACE: A Replication Pack for a Game‑Based Developer Productivity Diagnostic Tool in Software Engineering Education** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18705649)]
- [2026] **Measuring Developer Experience in Regulated Enterprise** *Frontiers in Emerging Computer Science and Information Technology* [[paper](https://doi.org/10.64917/fecsit/volume03issue02-01)]
- [2026] **Designing with Dev-X: A systematic mapping of Developer Experience interventions and their business impact** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108091)]
- [2026] **The Documentation Developer Experience: Documentation Engineering at the Vera C. Rubin Observatory** [[paper](https://doi.org/10.26624/xwgh8202)]
- [2026] **A COMPREHENSIVE APPROACH TO MEASURING SOFTWARE DEVELOPERS’ PRODUCTIVITY** *Naukovyi visnyk Donetskoho natsionalnoho tekhnichnoho universytetu* [[paper](https://doi.org/10.31474/2415-7902-2026-2-17-29-41)]
- [2026] **Intelligent Search and Predictive Modeling Framework for Enhancing Software Reliability and Developer Productivity** *Journal of Technology and System Information* [[paper](https://doi.org/10.47134/jtsi.v3i1.5490)]
- [2026] **This Analysis Evaluates The Architectural And Functional Distinctions Between The Procedural Efficiency Of C And The High-level Abstraction Of Python. It Examines How C Provides Low-level Memory Control And Performance, While Python Emphasizes Developer Productivity And Rapid Application Development.** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19091567)]
- [2026] **Exploring the Relationship Between Emotional State and Perceived Productivity Among Software Developers** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3707903)]
- [2026] **Improving Developer Experience in Linked Data Applications** *Digital Repository (National Repository of Grey Literature)* [[paper](https://www.nusl.cz/ntk/nusl-696884)]
- [2026] **A Comparative Analysis of Modern Frontend Frameworks from a Developer Experience Perspective** *Tampere University Institutional Repository (Tampere University)* [[paper](https://trepo.tuni.fi/handle/10024/236319)]
- [2026] **Empirical Evaluation of MVC Frameworks: Performance, Scalability, Developer Experience and Learning Curve** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-16851-1_24)]
- [2026] **ANALYSIS OF DEVELOPER EXPERIENCE IN THE KPR APPLICATION PROCESS THROUGH THE BTN PROPERTY FOR DEVELOPER APPLICATION AT THE BTN MANADO BRANCH** *Multidisciplinary Indonesian Center Journal* [[paper](https://doi.org/10.62567/micjo.v3i1.1812)]
- [2026] **Why Beginners Abandon Quantum Programming: Barriers to Developer Experience and a Scaffolding Approach to Development Environment Setup** *Jyväskylä University Digital Archive (University of Jyväskylä)* [[paper](https://urn.fi/URN:NBN:fi:jyu-202606095350)]

##### 2025

- [2025] **Beyond Productivity: Rethinking Junior Developer Support Through Neurodiversity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18043488)]
- [2025] **Supplemental Material for Developers' Experience with Generative AI - First Insights from an Empirical Mixed-Methods Field Study** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17818081)]
- [2025] **From React to Next.js: A Comparative Review of Performance, SEO, and Developer Experience** *INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* [[paper](https://doi.org/10.55041/ijsrem55712)]
- [2025] **AMD GPUs for Scientific Computing: Reviewing the Software Ecosystem & Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17967518)]
- [2025] **Developers' Experience with Generative AI -- First Insights from an Empirical Mixed-Methods Field Study** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2512.19926)]
- [2025] **A Systematic Approach to Measuring Developer Productivity: The Prismetrix Method** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-09318-9_23)]
- [2025] **Enhancing Developer Productivity Through Intelligent Documentation Retrieval** *Journal of Information Systems Engineering & Management* [[paper](https://doi.org/10.52783/jisem.v10i62s.13643)]
- [2025] **SpaceX: Exploring metrics with the SPACE model for developer productivity** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2511.20955)]
- [2025] **The Role of Single Page Applications in Modern Web Development: Performance, Usability and Developer Productivity** *Harokopio University* [[paper](https://doi.org/10.26258/heal.hua.7479)]
- [2025] **Software Developers’ Perceptions of Productivity: An Industry-focused Study** [[paper](https://doi.org/10.5753/sbqs.2025.13759)]
- [2025] **Supplementary materials for "A Design Science Research Approach to Blockchain Developer Experience (BcDEx)"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17515759)]
- [2025] **[Thesis] A Framework for Evaluating Transparency in Software Ecosystem Portals from the Developer Experience Perspective** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17761034)]
- [2025] **Copilot Impact Studies: Measuring Productivity, Trust, and Skill Evolution in Enterprise Developer Teams** *International Journal of Computational and Experimental Science and Engineering* [[paper](https://doi.org/10.22399/ijcesen.4217)]
- [2025] **A survey on the impact of emotions on the productivity among software developers** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2510.04611)]
- [2025] **Performance, Portability, and Productivity of HIP on GPUs with NAS Parallel Benchmarks** [[paper](https://doi.org/10.1109/sbac-pad66369.2025.00027)]
- [2025] **Juridical Review of Consumer Protection in Conduct Buying Transactions When the Developer Experiences Bankruptcy** *International Journal of Global Sustainable Research* [[paper](https://doi.org/10.59890/ijgsr.v3i10.83)]
- [2025] **Understanding Developer Productivity: Input-Output Perspectives Within the SPACE Framework** [[paper](https://doi.org/10.1109/iccai65301.2025.11279703)]
- [2025] **Framework for assessing software developers' productivity: metrics and estimates** *LA Referencia (Red Federada de Repositorios Institucionales de Publicaciones Científicas)* [[paper](https://repositorio.ufsm.br/handle/1/36723)]
- [2025] **Reactive Programming in Java: An Analysis of Application Performance and Developer Experience** *OHMdok (Technische Hochschule Nürnberg)* [[paper](https://opus4.kobv.de/opus4-ohm/frontdoor/index/index/docId/4252)]
- [2025] **AI in Software Engineering: Elevating Developer Experience through Codeium and Copilot** *Journal of Research in Science and Engineering* [[paper](https://doi.org/10.53469/jrse.2025.07(09).01)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **AI-Era Software Developer Productivity and Performance Metrics** *Journal of the Association for Information Systems* [[paper](https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1022&context=amcis2026)]
- [2026] **Adaptive AI Productivity Assistant for Developers in Visual Studio Code** [[paper](https://doi.org/10.1109/cicn70047.2026.11594203)]
- [2026] **A Socio-Technical Investigation of How Communication, Coordination, and Cooperation Shape the Developer Experience of ADHD Developers** [[paper](https://doi.org/10.5753/sbsc_estendido.2026.20934)]
- [2026] **Crafting the wearable computer: Design process and user experience** *Edinburgh Napier Research Repository (Edinburgh Napier University)* [[paper](https://researchrepository.napier.ac.uk/id/eprint/2418)]
- [2026] **Large language models for agile effort estimation: a post-mortem study incorporating developer experience and optimism** *Requirements Engineering* [[paper](https://doi.org/10.1007/s00766-026-00463-y)]
- [2026] **The Way of Types: A Report on Developer Experience with Type-Driven Development** [[paper](https://doi.org/10.1145/3794763.3794812)]
- [2026] **Mathematical Modelling of the Impact of Developer Experience Metrics on the Duration of the Release Cycle in Full-Stack Projects** *VFAST Transactions on Software Engineering* [[paper](https://doi.org/10.21015/vtse.v14i2.2300)]
- [2026] **Evaluating the Role of AI, Technology Used, and Technology Skill Proficiency in Onboarding: A Quantitative Study of Developer Productivity and Scalability in Sri Lanka** [[paper](https://doi.org/10.1109/scse70081.2026.11499963)]
- [2026] **Developers’ Dilemma: Opportunities and Pitfalls of Generative AI for Software Development** *Business & Information Systems Engineering* [[paper](https://doi.org/10.1007/s12599-026-00998-y)]
- [2026] **Circadian and color analysis of programming themes: effects of theme design, ambient lighting, and viewing distance on developer visual ergonomics** *Displays* [[paper](https://doi.org/10.1016/j.displa.2026.103417)]
- [2026] **Agent-Driven Design & Development: An Empirical Study of Solo Developer Productivity with LLM Coding Agents** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18639236)]
- [2026] **Platform Engineering and Developer Experience: A Systematic Review of Concepts, Benefits and Future Directions** *World Journal of Advanced Engineering Technology and Sciences* [[paper](https://doi.org/10.30574/wjaets.2026.18.2.0112)]
- [2026] **Developer Productivity with GenAI** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18437751)]
- [2026] **Analysis of Factors Influencing Developer Productivity on GitHub** [[paper](https://doi.org/10.13140/rg.2.2.35449.84324)]
- [2026] **Understanding Developers' Experiences When Contextualizing Rationale in Commit Messages** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17704102)]
- [2026] **Agentic AI-Driven Developer Experience for Telecom Capabilities** *KTH Publication Database DiVA (KTH Royal Institute of Technology)* [[paper](https://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-590043)]
- [2026] **Developer Experiences When Contextualizing Rationale in Commit Messages: An Exploratory Study** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.7028376)]
- [2026] **The Bottom-Up Approach to Developer Experience: Empowering Engineers to Drive Change** *The American Journal of Engineering And Technology* [[paper](https://doi.org/10.37547/tajet/volume08issue01-07)]
- [2026] **Understanding Developers' Experiences When Contextualizing Rationale in Commit Messages: An Exploratory Study** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20399173)]

##### 2025

- [2025] **Generative AI Integration: Key Drivers and Factors Enhancing Productivity of Engineering Faculty and Students for Sustainable Education** *Sustainability* [[paper](https://doi.org/10.3390/su17219914)]
- [2025] **Motivation is important, but can it be improved? Examining faculty perceptions of research motivation and productivity interventions** *Higher Education* [[paper](https://doi.org/10.1007/s10734-025-01546-5)]
- [2025] **Delusional Experiences Emerging From AI Chatbot Interactions or “AI Psychosis”** *JMIR Mental Health* [[paper](https://doi.org/10.2196/85799)]
- [2025] **Developers' Experiences When Contextualizing Rationale in Commit Messages** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17575109)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **<b>Replication package</b>: forward-snowballing update of a systematic literature review on developer experience and developer productivity** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.33123611.v1)]
- [2026] **Understanding developer well-being: measuring mental health and productivity in software teams** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-026-10830-6)]
- [2026] **Replication Package for "Helpful but Fallible: Developer Experiences of AI Tools Under a Coordinated Industrial Roll-out"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20021475)]
- [2026] **Developer Experience with AI Coding Agents: HTTP Behavioral Signatures in Documentation Portals** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2604.02544)]
- [2026] **Evaluating the Impact of AI Assisted Development Tools on Software Developer Productivity in Selected IT Companies in Nepal** *LBEF Research Journal of Science Technology and Management* [[paper](https://doi.org/10.67825/lrjstm.2026.8010116)]
- [2026] **Comparing Smart Contract Paradigms: A Preliminary Study of Security and Developer Experience** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2603.24501)]
- [2026] **From Predictors to Profiles: A Multi-Year Empirical Assessment of Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19204665)]
- [2026] **Engineering Productivity at Scale: Designing Internal Developer Platforms for Cloud-Native Java Teams** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21546534)]
- [2026] **An Empirical Evaluation of AI-Assisted Code Generation on Developer Productivity and Code Quality: A Case Study of .NET Applications** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6932038)]

##### 2025

- [2025] **Measuring AI-Driven Developer Productivity in Agile Software Development Random Forest Regression Analysis of Performance Metrics and Tool Integration** *Computer Science Engineering and Technology* [[paper](https://doi.org/10.46632/cset/3/3/12)]
- [2025] **When the Flow is Just Too Much: The Adverse Outcomes of Flow in Software Developers' Work** *AIS Transactions on Human-Computer Interaction* [[paper](https://doi.org/10.17705/1thci.00231)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Mobile App Rewrites via Dual Boot** [[paper](https://arxiv.org/abs/2608.15135)]
- [2026] **Detecting Behavioral Changes in Python Refactoring Implementations with Foundation Models** [[paper](https://arxiv.org/abs/2608.09919)]
- [2026] **Unreliable in Practice? A Comprehensive Study of Errors in LLM-Generated Code** [[paper](https://arxiv.org/abs/2608.00661)]
- [2026] **SynH-Rank: Quality-Aware Code Search via Diverse Data Synthesis and Hierarchical Ranking Training** [[paper](https://arxiv.org/abs/2607.17139)]
- [2026] **Three-Phase Evaluation of AI-Assisted Software Development Life Cycle** [[paper](https://arxiv.org/abs/2607.05125)]
- [2026] **[CTDQS 2026] Improving Transparency in Software Ecosystem Portals through Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21364770)]
- [2026] **Lost in the Flow with Code Talkers: Unveiling the Instruction-Tuning Tax of Large Language Models in Code Tasks** [[paper](https://arxiv.org/abs/2606.08676)]
- [2026] **[CTD-ES 2026] Evaluating Transparency in Software Ecosystem Portals through Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18737403)]
- [2026] **A meta-analysis of the effect of generative AI on productivity and learning in programming** [[paper](https://arxiv.org/abs/2605.04779)]
- [2026] **Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs** [[paper](https://arxiv.org/abs/2605.29737)]
- [2026] **EngThrive: Make It Fast and Easy to Do Great Work** [[paper](https://arxiv.org/abs/2605.04259)]
- [2026] **JEDI: Java Evaluation of Declarative and Imperative Queries** [[paper](https://arxiv.org/abs/2605.23543)]
- [2026] **Governance-Aware AI-Assisted Developer Productivity Evaluation in Hybrid Work Environments** [[paper](https://doi.org/10.1109/sm69703.2026.11614152)]
- [2026] **Replication Package "Comparing Smart Contract Paradigms: A Preliminary Study of Security and Developer Experience"** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.31429430)]
- [2026] **AI Observability for Developer Productivity Tools: Bridging Cost Awareness and Code Quality** [[paper](https://arxiv.org/abs/2604.17092)]
- [2026] **EcoAssist: Embedding Sustainability into AI-Assisted Frontend Development** [[paper](https://arxiv.org/abs/2604.04332)]
- [2026] **Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision** [[paper](https://arxiv.org/abs/2604.06723)]
- [2026] **CLARC: C/C++ Benchmark for Robust Code Search** [[paper](https://arxiv.org/abs/2603.04484)] [[project](https://huggingface.co/datasets/ClarcTeam/CLARC)]
- [2026] **Safer Builders, Risky Maintainers: A Comparative Study of Breaking Changes in Human vs Agentic PRs** [[paper](https://arxiv.org/abs/2603.27524)]
- [2026] **Sustainable Code Generation Using Large Language Models: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2603.00989)]
- [2026] **Automating Detection and Root-Cause Analysis of Flaky Tests in Quantum Software** [[paper](https://arxiv.org/abs/2603.09029)]
- [2026] **More Code, Less Understanding? On the Impact of AI Assistants on Developers’ Productivity and Code Ownership** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2026.3679627)]
- [2026] **Supplementary Material to "Fragmented Markers, Mixed Results: A Systematic Review of AI Coding Assistants and Developer Productivity"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19219047)]
- [2026] **Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants** [[paper](https://arxiv.org/abs/2602.03593)]
- [2026] **From Ad-Hoc Scripts to Orchestrated Pipelines: Architecting a Resilient ELT Framework for Developer Productivity Metrics** [[paper](https://arxiv.org/abs/2602.21568)]
- [2026] **AIDev: Studying AI Coding Agents on GitHub** [[paper](https://arxiv.org/abs/2602.09185)]
- [2026] **EditFlow: Benchmarking and Optimizing Code Edit Recommendation Systems via Reconstruction of Developer Flows** [[paper](https://arxiv.org/abs/2602.21697)]
- [2026] **Impacts of Generative AI on Agile Teams' Productivity: A Multi-Case Longitudinal Study** [[paper](https://arxiv.org/abs/2602.13766)]
- [2026] **CodeMEM: AST-Guided Adaptive Memory for Repository-Level Iterative Code Generation** [[paper](https://arxiv.org/abs/2601.02868)]
- [2026] **The Promise and Reality of Continuous Integration Caching: An Empirical Study of Travis CI Builds** [[paper](https://arxiv.org/abs/2601.19146)]
- [2026] **Coffee and Developer Productivity** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.31049104.v2)]

##### 2025

- [2025] **Empowering smart app development with SolidGPT: an edge-cloud hybrid AI agent framework** [[paper](https://arxiv.org/abs/2512.08286)]
- [2025] **Understanding Privacy Risks in Code Models Through Training Dynamics: A Causal Approach** [[paper](https://arxiv.org/abs/2512.07814)]
- [2025] **CFCEval: Evaluating Security Aspects in Code Generated by Large Language Models** [[paper](https://arxiv.org/abs/2512.06248)]
- [2025] **Software Vulnerability Management in the Era of Artificial Intelligence: An Industry Perspective** [[paper](https://arxiv.org/abs/2512.18261)]
- [2025] **Studying the Role of Reusing Crowdsourcing Knowledge in Software Development** [[paper](https://arxiv.org/abs/2512.07824)]
- [2025] **mnrj-vv-w/developer-experience-paper: v1.1.1 - Initial Release** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18066993)]
- [2025] **mnrj-vv-w/developer-experience-paper: v1.1.2 - Initial Public Release** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18066992)]
- [2025] **ProofWright: Towards Agentic Formal Verification of CUDA** [[paper](https://arxiv.org/abs/2511.12294)]
- [2025] **MetricSynth: Framework for Aggregating DORA and KPI Metrics Across Multi-Platform Engineering** [[paper](https://arxiv.org/abs/2511.06864)]
- [2025] **High-level reasoning while low-level actuation in Cyber-Physical Systems: How efficient is it?** [[paper](https://arxiv.org/abs/2511.12543)]
- [2025] **Strategic Decision Framework for Enterprise LLM Adoption** [[paper](https://arxiv.org/abs/2511.18589)]
- [2025] **GazeCopilot: Evaluating Novel Gaze-Informed Prompting for AI-Supported Code Comprehension and Readability** [[paper](https://arxiv.org/abs/2511.08177)]
- [2025] **UI-CUBE: Enterprise-Grade Computer Use Agent Benchmarking Beyond Task Accuracy to Operational Reliability** [[paper](https://arxiv.org/abs/2511.17131)]
- [2025] **CodeWatcher: IDE Telemetry Data Extraction Tool for Understanding Coding Interactions with LLMs** [[paper](https://arxiv.org/abs/2510.11536)]
- [2025] **Multi Language Models for On-the-Fly Syntax Highlighting** [[paper](https://arxiv.org/abs/2510.04166)]
- [2025] **"Your AI, My Shell": Demystifying Prompt Injection Attacks on Agentic AI Coding Editors** [[paper](https://arxiv.org/abs/2509.22040)]
- [2025] **Protocode: Prototype-Driven Interpretability for Code Generation in LLMs** [[paper](https://arxiv.org/abs/2509.25247)]
- [2025] **Towards Verified Code Reasoning by LLMs** [[paper](https://arxiv.org/abs/2509.26546)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Making AI Visible, Not Vanished: How AI Policies Reshape Developer Experience on GitHub** [[paper](https://arxiv.org/abs/2608.03329)]
- [2026] **Integration Barriers in Open-Source SSI Frameworks: An Exploratory Developer Experience Probe** [[paper](https://arxiv.org/abs/2608.03039)]
- [2026] **How Developers Experience Debugging Unfamiliar Codebases with Code Tours Generated and Evaluated by Local LLMs** [[paper](https://arxiv.org/abs/2607.26987)]
- [2026] **Inference Economics of Enterprise Coding Agents: A Case Study of Cloud vs. On-Premise LLMs** [[paper](https://arxiv.org/abs/2607.13080)]
- [2026] **Insights from GitHub Community on the Matter Standard: Developer Perspectives and Challenges** [[paper](https://arxiv.org/abs/2607.01494)]
- [2026] **Developers' Experience with Generative AI Beyond Productivity Assessment -- Insights from an Empirical Mixed-Methods Field Study** [[paper](https://arxiv.org/abs/2607.02337)]
- [2026] **Biased or Personalized? The Impact of Personal Information on AI-driven Development** [[paper](https://arxiv.org/abs/2607.07480)]
- [2026] **Adopting Concepts for Sustainable Improvement of the Developer Experience within a Medium-sized Corporation** [[paper](https://doi.org/10.1145/3803437.3805210)]
- [2026] **A Benchmarking Framework for Multimodal User Interface Toolkits: Comparing Modality Coverage, Developer Workflow, and Experimental Support** [[paper](https://arxiv.org/abs/2606.02977)]
- [2026] **Writing Better Software Explanations: A Guideline-Based Approach** [[paper](https://arxiv.org/abs/2606.10880)]
- [2026] **Replication package: From Code Volume to Human Experience: A Multivocal Literature Review on Developer Productivity Measurement (2016-2026)** *Open MIND* [[paper](https://github.com/sorattorafa/MLR-developer-productivity-2026/tree/v1.0.0)]
- [2026] **The Impact of AI Coding Assistants on Software Engineering: A Longitudinal Study** [[paper](https://arxiv.org/abs/2605.23135)]
- [2026] **From Chat to Interview: Agentic Requirements Elicitation with an Experience Ontology** [[paper](https://arxiv.org/abs/2605.05828)]
- [2026] **Developer Experience and the Digital Environment: An Interview Study** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20444597)]
- [2026] **Supplementary Appendix: Architectural Overview of SECO-TransP for Evaluating Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19372175)]
- [2026] **BayesInsights: Modelling Software Delivery and Developer Experience with Bayesian Networks at Bloomberg** [[paper](https://arxiv.org/abs/2603.29929)]
- [2026] **Knowledge Activation: AI Skills as the Institutional Knowledge Primitive for Agentic Software Development** [[paper](https://arxiv.org/abs/2603.14805)]
- [2026] **Engineering a Governance-Aware AI Sandbox: Design, Implementation, and Lessons Learned** [[paper](https://arxiv.org/abs/2603.03394)]
- [2026] **A Collaborative and Pattern-Based Training Approach to Knowledge Acquisition and Decision-Making During the Design of Software Architectures Courses: A Case Study** [[paper](https://arxiv.org/abs/2603.11904)]
- [2026] **Detecting UX smells in Visual Studio Code using LLMs** [[paper](https://arxiv.org/abs/2602.22020)]
- [2026] **Theory of Troubleshooting: The Developer's Cognitive Experience of Overcoming Confusion** [[paper](https://arxiv.org/abs/2602.10540)]
- [2026] **Novice Developers Produce Larger Review Overhead for Project Maintainers while Vibe Coding** [[paper](https://arxiv.org/abs/2602.23905)]
- [2026] **Model-Driven Legacy System Modernization at Scale** [[paper](https://arxiv.org/abs/2602.04341)]
- [2026] **Practitioner Views on Mobile App Accessibility: Practices and Challenges** [[paper](https://arxiv.org/abs/2601.14131)]
- [2026] **NanoCockpit: Performance-optimized Application Framework for AI-based Autonomous Nanorobotics** [[paper](https://arxiv.org/abs/2601.07476)]
- [2026] **Are We All Using Agents the Same Way? An Empirical Study of Core and Peripheral Developers Use of Coding Agents** [[paper](https://arxiv.org/abs/2601.20106)]
- [2026] **Developer Interaction Patterns with Proactive AI: A Five-Day Field Study** [[paper](https://arxiv.org/abs/2601.10253)]
- [2026] **Challenges in Android Data Disclosure: An Empirical Study** [[paper](https://arxiv.org/abs/2601.20459)]
- [2026] **Exploring the Relationship Between Emotional State and Perceived Productivity Among Software Developers.** *IEEE Access* [[paper](https://dblp.org/rec/journals/access/WeichbrothLW26)]
- [2026] **Understanding developer well-being: measuring mental health and productivity in software teams.** *Empir. Softw. Eng.* [[paper](https://dblp.org/rec/journals/ese/ArrielCALMGP26)]
- [2026] **Stop Blaming QA and Start Diagnosing the Hidden Inefficiencies Behind Delivery Delays: Five Drivers that Slow Releases And Erode Developer Productivity.** *ACM SIGSOFT Softw. Eng. Notes* [[paper](https://dblp.org/rec/journals/sigsoft/ElDeeb26a)]
- [2026] **More Code, Less Understanding? On the Impact of AI Assistants on Developers&apos; Productivity and Code Ownership.** *IEEE Trans. Software Eng.* [[paper](https://dblp.org/rec/journals/tse/MartinLopezTGSSSOSB26)]
- [2026] **A Dual Role Collision: How Generative AI&apos;s Intertwining Productivity Support and Social Support Reshape Indie Game Developers&apos; Creative Work.** *FAccT* [[paper](https://dblp.org/rec/conf/fat/PanchanadikarHF26)]
- [2026] **AI-augmented reliability in CI/CD: a framework for predictive, adaptive, and self-correcting pipelines.** *MED* [[paper](https://doi.org/10.3389/frai.2026.1776546)]
- [2026] **How students use generative AI for software testing: An observational study.** *MED* [[paper](https://doi.org/10.1007/s10664-026-10898-0)]
- [2026] **INTERNAL DEVELOPER PORTALS AS ENABLERS OF DEVELOPER EXPERIENCE: A SYSTEMATIC AND GREY LITERATURE REVIEW** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6708758)]

##### 2025

- [2025] **Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases** [[paper](https://arxiv.org/abs/2512.10398)]
- [2025] **Selecting Cybersecurity Requirements: Effects of LLM Use and Professional Software Development Experience** [[paper](https://arxiv.org/abs/2510.04274)]
- [2025] **Towards an Understanding of Developer Experience-Driven Transparency in Software Ecosystems** [[paper](https://arxiv.org/abs/2509.03848)]
- [2025] **Reading Between the Lines: Scalable User Feedback via Implicit Sentiment in Developer Prompts** [[paper](https://arxiv.org/abs/2509.18361)]
- [2025] **What Were You Thinking? An LLM-Driven Large-Scale Study of Refactoring Motivations in Open-Source Projects** [[paper](https://arxiv.org/abs/2509.07763)]
- [2025] **Good Vibrations? A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding** [[paper](https://arxiv.org/abs/2509.12491)]
- [2025] **The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review - Supplementary material.** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17555071)]
- [2025] **Interactions with Generative AI: Wearables to Measure Developer Experience and Productivity Objectively** *2025 IEEE/ACM 47th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion)* [[paper](https://doi.org/10.1109/icse-companion66252.2025.00043)]
- [2025] **A Systematic Literature Review on the Influence of Enhanced Developer Experience on Developers&apos; Productivity: Factors, Practices, and Recommendations.** *ACM Comput. Surv.* [[paper](https://dblp.org/rec/journals/csur/RazzaqBLYB25)]
- [2025] **DeputyDev - AI Powered Developer Assistant: Breaking the Code Review Logjam through Contextual AI to Boost Developer Productivity.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2508-09676)]
- [2025] **Measuring Developer Experience** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_8)]
- [2025] **Developer Experience Case Studies** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_10)]
- [2025] **The Future of Developer Experience** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_11)]
- [2025] **The Essence of Developer Experience** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_1)]
- [2025] **Developer Experience As a Competitive Advantage** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_2)]
- [2025] **Streamlining Developer Tooling** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_4)]
- [2025] **Designing Developer-Centric APIs** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_5)]
- [2025] **Providing Stellar Developer Support** *Developer Experience Unleashed* [[paper](https://doi.org/10.1007/979-8-8688-0242-3_6)]
- [2025] **Multi-Sallm: A Multilingual Security Assessment of Generated Code** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-7745381/v1)]
- [2025] **AI4SWEng manifest: Empowering the future of software engineering with advanced trustworthy artificial intelligence** *PPR* [[paper](https://doi.org/10.12688/openreseurope.21192.1)]
- [2025] **Integrating Large Language Models into Automated Software Testing** *PPR* [[paper](https://doi.org/10.20944/preprints202509.1433.v1)]
- [2025] **Pyomo: Accidentally outrunning the bear.** *MED* [[paper](https://doi.org/10.1016/j.patter.2025.101311)]
- [2025] **A Comparative Featureset Analysis of Agentic IDE Tools** *PPR* [[paper](https://doi.org/10.20944/preprints202506.0821.v1)]
- [2025] **LEDGE : Leveraging Dependency Graphs for Enhanced Context Aware Documentation Generation** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-6827966/v1)]
- [2025] **Software bug report dataset from Eclipse projects.** *MED* [[paper](https://doi.org/10.1016/j.dib.2025.112016)]
- [2025] **The New Developer: AI Skill Threat, Identity Change & Developer Thriving in the Transition to AI-Assisted Software Development** *PPR* [[paper](https://doi.org/10.31234/osf.io/2gej5_v2)]

##### 2024

- [2024] **The Incredible Machine: Developer Productivity and the Impact of AI on Productivity (Keynote).** *SIGSOFT FSE Companion* [[paper](https://dblp.org/rec/conf/sigsoft/Zimmermann24)]

##### 2023

- [2023] **Developer Productivity for Humans, Part 4: Build Latency, Predictability, and Developer Productivity** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2023.3275268)]
- [2023] **Measuring Developer Productivity: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2306.00001)]
- [2023] **Developer Productivity for Humans, Part 4: Build Latency, Predictability, and Developer Productivity.** *IEEE Softw.* [[paper](https://dblp.org/rec/journals/software/JaspanG23c)]
- [2023] **DevEx: What Actually Drives Productivity: The developer-centric approach to measuring and improving productivity.** *ACM Queue* [[paper](https://dblp.org/rec/journals/queue/NodaSFG23)]
- [2023] **Developer Productivity for Humans, Part 6: Measuring Flow, Focus, and Friction for Developers.** *IEEE Softw.* [[paper](https://dblp.org/rec/journals/software/BrownCHD23)]
- [2023] **Developer Productivity for Humans, Part 2: Hybrid Productivity.** *IEEE Softw.* [[paper](https://dblp.org/rec/journals/software/JaspanG23a)]

##### 2019

- [2019] **Software developer productivity loss due to technical debt - A replication and extension study examining developers&apos; development work.** *J. Syst. Softw.* [[paper](https://dblp.org/rec/journals/jss/BeskerMB19)]
- [2019] **Developers&apos; Diverging Perceptions of Productivity.** *Rethinking Productivity in Software Engineering* [[paper](https://dblp.org/rec/books/sp/19/MeyerMF019)]
- [2019] **How Team Awareness Influences Perceptions of Developer Productivity.** *Rethinking Productivity in Software Engineering* [[paper](https://dblp.org/rec/books/sp/19/TreudeF19)]

##### 2018

- [2018] **Technical debt cripples software developer productivity: a longitudinal study on developers&apos; daily software development work.** *TechDebt@ICSE* [[paper](https://dblp.org/rec/conf/icse/BeskerMB18)]

##### 2016

- [2016] **Bing developer assistant: improving developer productivity by recommending sample code.** *SIGSOFT FSE* [[paper](https://dblp.org/rec/conf/sigsoft/ZhangJKKGH16)]

##### 2013

- [2013] **Are Happy Developers More Productive? - The Correlation of Affective States of Software Developers and Their Self-assessed Productivity.** *PROFES* [[paper](https://dblp.org/rec/conf/profes/GraziotinWA13)]
- [2013] **Are Happy Developers more Productive? The Correlation of Affective States of Software Developers and their self-assessed Productivity.** *CoRR* [[paper](https://arxiv.org/abs/1306.1772)]

##### 2009

- [2009] **Factors that Influence the Productivity of Software Developers in a Developer View.** *SCSS* [[paper](https://dblp.org/rec/conf/cisse/PaivaBLA09)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **The Impact of Platform Engineering on Developer Productivity** [[paper](https://doi.org/10.1002/9781394395910.ch4)]
- [2026] **Developer Productivity in the Age of Generative AI: A Psychological Perspective** [[paper](https://doi.org/10.31234/osf.io/7gwx2_v1)]
- [2026] **Sounio-lang/sounio: v0.12.0 - Developer Experience** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18190156)]

##### 2025

- [2025] **Hybrid Query Execution Architecture: Bridging Developer Experience and Performance in Enterprise Metrics Platforms** *Journal of Computational Analysis and Applications* [[paper](https://doi.org/10.48047/jocaaa.2025.34.10.19)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Towards Sustainable Open Source Software and Developer Productivity** *CFI-FCI* [[paper](https://doi.org/10.82286/h9y5-f669)]
- [2026] **Stop Blaming QA and Start Diagnosing the Hidden Inefficiencies Behind Delivery Delays: Five Drivers that Slow Releases And Erode Developer Productivity** *ACM SIGSOFT Software Engineering Notes* [[paper](https://doi.org/10.1145/3800646.3800650)]
- [2026] **GitHub Copilot and Developer Productivity: An Observational Dose-Response Analysis** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2606.00438)]
- [2026] **<b>Supplementary Material - Are We Measuring the Wrong Things? How Software Project Leaders View Gen-AI-Assisted Developer Productivity</b>** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.32292972.v1)]
- [2026] **Investigating the Key Factors Influencing Software Developer Productivity in Developing Regions** *Smart innovation, systems and technologies* [[paper](https://doi.org/10.1007/978-3-032-12999-4_13)]
- [2026] **LLM-Assisted Rapid Prototyping in Software Engineering: A Practitioner Study of Developer Productivity** [[paper](https://doi.org/10.13140/rg.2.2.29994.89286)]
- [2026] **Software Errors, Product Functionality, and Organizational Cascades: Evidence from Developer-Lived Experience** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6924439)]
- [2026] **Who is using AI to code? Global diffusion and impact of generative AI** *Science* [[paper](https://doi.org/10.1126/science.adz9311)]
- [2026] **Understanding Generative AI Adoption in Development Work: The Role of Developer Experience** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-30863-4_20)]

##### 2025

- [2025] **INTELLIGENT AUTOMATION IN SOFTWARE ENGINEERING: TRANSFORMING DEVELOPER PRODUCTIVITY AND CODE QUALITY THROUGH MACHINE LEARNING** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17985962)]
- [2025] **Towards Understanding the Developer Experience in Quantum Software Development** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-12089-2_39)]
- [2025] **Hindrances and Strengths in Software Delivery: Insights from a Developer Experience Study at the Swedish Transport Administration** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-12092-2_8)]
- [2025] **Examining the Dynamics of AI-Assisted Development: A Cross-Sectional Study of Developer Experience and Productivity** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17726508)]

[⬆ Back to top](#paper-list)

### AI for Software Engineering

#### Method

##### 2026

- [2026] **Entropy-based Code Adversarial Translation for Real-world Repository Migration** [[paper](https://arxiv.org/abs/2608.09273)]
- [2026] **Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency** [[paper](https://arxiv.org/abs/2608.14065)]
- [2026] **Context as a Computational Resource: Adaptive Hierarchical Context Orchestration for Long-Horizon AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21964911)]
- [2026] **Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation** [[paper](https://arxiv.org/abs/2607.26244)]
- [2026] **AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair** [[paper](https://arxiv.org/abs/2607.29422)]
- [2026] **MultiFixer: A Coordinator-Proposer Based Multi-Agent Framework For Fixing Multi-Hunk Bugs** [[paper](https://arxiv.org/abs/2607.26591)]
- [2026] **How Do LLMs Read Bug Reports? An Empirical Study of Attention in LLMs for Automated Program Repair** [[paper](https://arxiv.org/abs/2607.25873)]
- [2026] **VisualRepair: Dynamic Tool Calling and Region Focusing for Visual Software Issue Repair** [[paper](https://arxiv.org/abs/2607.14075)]
- [2026] **Multi-Perspective Agentic Program Repair via Code Property Graphs and Temporal Execution Graphs** [[paper](https://arxiv.org/abs/2607.12605)]
- [2026] **Bug Report Specification Refinement with Trajectory Guidance for Automated Program Repair** [[paper](https://arxiv.org/abs/2607.07882)]
- [2026] **What Makes a Good Bug Report for an AI Agent?** [[paper](https://arxiv.org/abs/2607.07593)]
- [2026] **Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes** [[paper](https://arxiv.org/abs/2607.19843)]
- [2026] **A System-Level Software Requirements Dataset for LLM Code Generation** *Harvard Dataverse* [[paper](https://doi.org/10.7910/dvn/lanmvp)]
- [2026] **A Systematic Literature Review on Automated Program Repair using Large Language Models** *JUCS - Journal of Universal Computer Science* [[paper](https://doi.org/10.3897/jucs.171035)]
- [2026] **StructFix: A Structure-Aware Reasoning Framework for Automated Program Repair with Code Property Graphs** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-10222746/v1)]
- [2026] **SkelDPO: A Skeleton-Guided Direct Preference Optimization Framework for Efficient Code Generation** [[paper](https://arxiv.org/abs/2606.06826)] [[code](https://github.com/icpcSkelDPO/SkelDPO)]
- [2026] **Automated Repair of Requirements for Cyber-Physical Systems in Simulink Requirements Tables** [[paper](https://arxiv.org/abs/2606.03870)]
- [2026] **PracRepair: LLM-Empowered Automated Program Repair Inspired by Human-Like Debugging Practices** [[paper](https://arxiv.org/abs/2606.17612)]
- [2026] **TraceView: Interactive Visualization of Agentic Program Repair Trajectories** [[paper](https://arxiv.org/abs/2606.22110)] [[code](https://github.com/SOAR-Lab/agent-traj-visualization)]
- [2026] **Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair** [[paper](https://arxiv.org/abs/2606.27205)]
- [2026] **A11YRepair: Bridging Web Accessibility Barriers via Knowledge-Enhanced Divide-and-Conquer Repair** [[paper](https://arxiv.org/abs/2606.21926)]
- [2026] **An LLM-Driven Multi-Agent Evolution Framework for Solver Code Generation in Job Shop Scheduling** *Mathematics* [[paper](https://doi.org/10.3390/math14112010)]
- [2026] **How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval** [[paper](https://arxiv.org/abs/2606.00308)]
- [2026] **HEJ-Robust: A Robustness Benchmark for LLM-Based Automated Program Repair** [[paper](https://arxiv.org/abs/2605.02215)]
- [2026] **EviACT: An Evidence-to-Action Framework for Agentic Program Repair** [[paper](https://arxiv.org/abs/2605.27238)]
- [2026] **SiblingRepair: Sibling-Based Multi-Hunk Repair with Large Language Models** [[paper](https://arxiv.org/abs/2605.06209)]
- [2026] **Characterizing the Failure Modes of LLMs in Resolving Real-World GitHub Issues** [[paper](https://arxiv.org/abs/2605.12270)]
- [2026] **BLAgent: Agentic RAG for File-Level Bug Localization** [[paper](https://arxiv.org/abs/2605.17965)]
- [2026] **ARISE: A Repository-level Graph Representation and Toolset for Agentic Program Repair and Fault Localization** [[paper](https://arxiv.org/abs/2605.03117)]
- [2026] **Semantic Voting: Execution-Grounded Consensus for LLM Code Generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2605.08680)]
- [2026] **Prompt Optimization for LLM Code Generation via Reinforcement Learning** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2605.19102)]
- [2026] **Kaizen-3C / benchmarks: value-add fingerprinting for AI software-engineering agents** *Open MIND* [[paper](https://github.com/Kaizen-3C/benchmarks/tree/v1.0.0)]
- [2026] **SENSE-CORE-DRIVER: A Governance Architecture for Enterprise AI** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20368910)]
- [2026] **Practical LLM-Based Function-Level Automated Program Repair: How Far Are We?** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3812804)]
- [2026] **PracAPR: A Test-Free, Execution Trace-Driven Automated Program Repair Framework** [[paper](https://doi.org/10.1109/icsccc69031.2026.11600180)]
- [2026] **An Empirical Study on Influence-Based Pretraining Data Selection for Code Large Language Models** [[paper](https://arxiv.org/abs/2604.07769)]
- [2026] **PatchRecall: Patch-Driven Retrieval for Automated Program Repair** [[paper](https://arxiv.org/abs/2604.10481)]
- [2026] **PAFT: Preservation Aware Fine-Tuning for Minimal-Edit Program Repair** [[paper](https://arxiv.org/abs/2604.03113)]
- [2026] **From Guessing to Seeing: Enhancing LLM-Based Program Repair via Trace-Guided Multi-strategy Debate** [[paper](https://arxiv.org/abs/2604.02647)]
- [2026] **An End-to-End Approach for Fixing Concurrency Bugs via SHB-Based Context Extractor** [[paper](https://arxiv.org/abs/2604.05753)]
- [2026] **Semantic Evolution over Populations for LLM-Guided Automated Program Repair** [[paper](https://arxiv.org/abs/2604.02134)]
- [2026] **GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair** [[paper](https://arxiv.org/abs/2604.08089)]
- [2026] **A Metamorphic Testing Approach to Diagnosing Memorization in LLM-Based Program Repair** [[paper](https://arxiv.org/abs/2604.21579)]
- [2026] **On the Role of Fault Localization Context for LLM-Based Program Repair** [[paper](https://arxiv.org/abs/2604.05481)]
- [2026] **Enhancing Program Repair with Specification Guidance and Intermediate Behavioral Signals** [[paper](https://arxiv.org/abs/2604.11770)]
- [2026] **DebugHarness: Emulating Human Dynamic Debugging for Autonomous Program Repair** [[paper](https://arxiv.org/abs/2604.03610)]
- [2026] **Project Prometheus: Bridging the Intent Gap in Agentic Program Repair via Reverse-Engineered Executable Specifications** [[paper](https://arxiv.org/abs/2604.17464)]
- [2026] **Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis** [[paper](https://arxiv.org/abs/2604.24212)]
- [2026] **DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging** [[paper](https://arxiv.org/abs/2604.19305)]
- [2026] **Reproducible Automated Program Repair Is Hard -- Experiences With the Defects4J Dataset** [[paper](https://arxiv.org/abs/2604.26674)]
- [2026] **Code Roulette: How Prompt Variability Affects LLM Code Generation** [[paper](https://arxiv.org/abs/2506.10204)]
- [2026] **LLM-Based Adaptive Control Code Generation Framework with Digital Twin-Integrated Verification for Heterogeneous Robot Systems** *Applied Sciences* [[paper](https://doi.org/10.3390/app16083883)]
- [2026] **From Code Generation to Conceptual Learning: Student Use of LLMs in a Web Programming Course** [[paper](https://doi.org/10.1145/3772318.3793207)]
- [2026] **Towards AI-Native Software Engineering (SE 3.0): A Vision and a Challenge Roadmap** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2410.06107)]
- [2026] **From Junior to Senior: Allocating Agency and Navigating Professional Growth in Agentic AI-Mediated Software Engineering** [[paper](https://arxiv.org/abs/2602.00496)]
- [2026] **AI Behavior Science — Founding Territory Paper** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19562751)]
- [2026] **From Future of Work to Future of Workers: Addressing Asymptomatic AI Harms to Foster Dignified Human-AI Interaction** [[paper](https://arxiv.org/abs/2601.21920)]
- [2026] **The Undecidability of Overfitting in Automated Program Repair** [[paper](https://doi.org/10.1145/3786582.3786802)]
- [2026] **Integrating Retrieval Augmentation and Decoding Intervention for Automated Program Repair** *Expert Systems* [[paper](https://doi.org/10.1111/exsy.70251)]
- [2026] **Applying Genetic Improvement Techniques for Automated Program Repair of Transpiled Code** [[paper](https://doi.org/10.1145/3786162.3793234)]
- [2026] **FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair** [[paper](https://arxiv.org/abs/2603.17826)]
- [2026] **RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair** [[paper](https://arxiv.org/abs/2603.01048)]
- [2026] **Beyond Localization: Recoverable Headroom and Residual Frontier in Repository-Level RAG-APR** [[paper](https://arxiv.org/abs/2603.29067)]
- [2026] **On the Use of Commit Messages for Corrective Software Maintenance: A Systematic Mapping Study** [[paper](https://arxiv.org/abs/2604.16404)]
- [2026] **On the Effectiveness of Code Representation in Deep Learning-Based Automated Patch Correctness Assessment** [[paper](https://arxiv.org/abs/2603.07520)]
- [2026] **Unveiling Practical Shortcomings of Patch Overfitting Detection Techniques** [[paper](https://arxiv.org/abs/2603.11262)]
- [2026] **Helping LLMs improve code generation using feedback from testing and static analysis** *Discover Artificial Intelligence* [[paper](https://arxiv.org/abs/2412.14841)]
- [2026] **Narrative-Integrated Thematic Analysis (NITA): How can LLMs support theme generation without coding?** *Qualitative Research in Psychology* [[paper](https://doi.org/10.1080/14780887.2026.2638348)]
- [2026] **Are They All Good? Evaluating the Quality of CoTs in LLM-Based Code Generation** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2026.3676295)]
- [2026] **<scp>ProteinMCP</scp> : An agentic <scp>AI</scp> framework for autonomous protein engineering** *Protein Science* [[paper](https://doi.org/10.1002/pro.70547)]
- [2026] **A Systematic Literature Review on Large Language Models for Automated Program Repair** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3799693)]
- [2026] **Compartmentalization-Aware Automated Program Repair** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2603.09544)]
- [2026] **From Symptoms to Fixes: Towards Review-Driven Automated Program Repair** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.31828063)]
- [2026] **What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair** [[paper](https://arxiv.org/abs/2602.04449)]
- [2026] **Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment** [[paper](https://arxiv.org/abs/2603.00649)]
- [2026] **SVRepair: Structured Visual Reasoning for Automated Program Repair** [[paper](https://arxiv.org/abs/2602.06090)] [[code](https://github.com/codefuse-ai/CodeFuse-SVR)]
- [2026] **Specification Vibing for Automated Program Repair** [[paper](https://arxiv.org/abs/2602.08263)]
- [2026] **ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair** [[paper](https://arxiv.org/abs/2602.07561)]
- [2026] **AgenticSZZ: Temporal Knowledge Graph-Guided Agentic Bug-Inducing Commit Identification** [[paper](https://arxiv.org/abs/2602.02934)]
- [2026] **Evaluating LLMs for Source Code Generation and Summarization Using Machine Learning Classification and Ranking** *Computers* [[paper](https://doi.org/10.3390/computers15020119)]
- [2026] **Vul-RAG: Enhancing LLM-based Vulnerability Detection via Knowledge-level RAG** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3797277)]
- [2026] **ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2602.04296)]
- [2026] **Towards an Appropriate Level of Reliance on AI: A Preliminary Reliance-Control Framework for AI in Software Engineering - Supplementary Information Package** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18616305)]
- [2026] **Methodological Approaches to Assessing Productivity and Resource Planning in Hybrid Human-AI Software Engineering Teams** *Universal library of engineering technology.* [[paper](https://doi.org/10.70315/uloap.ulete.2026.0301009)]
- [2026] **Large Language Models for Automated Program Repair: Approaches, Evaluation, and Future Challenges** *IJCI International Journal of Computers and Information* [[paper](https://doi.org/10.21608/ijci.2026.455596.1236)]
- [2026] **SEED-APR: A closed-loop self-evolving framework for automated program repair** *Systems and Soft Computing* [[paper](https://doi.org/10.1016/j.sasc.2026.200463)]
- [2026] **AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2601.19697)]
- [2026] **Monte Carlo Tree Search for Execution-Guided Program Repair with Large Language Models** [[paper](https://arxiv.org/abs/2602.00129)]
- [2026] **From Historical Patches to Repair Plans: Outcome-Conditioned Reasoning for Repository-Level Program Repair** [[paper](https://arxiv.org/abs/2601.23257)]
- [2026] **Leveraging Mutation Analysis for LLM-based Repair of Quantum Programs** [[paper](https://arxiv.org/abs/2601.12273)]
- [2026] **Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair** [[paper](https://arxiv.org/abs/2601.19066)]
- [2026] **RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models** [[paper](https://arxiv.org/abs/2601.18044)]
- [2026] **GeoJSON agents: a multi-agent LLM architecture for geospatial analysis—function calling vs. code generation** *Big Earth Data* [[paper](https://doi.org/10.1080/20964471.2026.2615511)]
- [2026] **ChatMPI: LLM-Driven MPI Code Generation for HPC Workloads** [[paper](https://doi.org/10.1145/3773656.3773659)]
- [2026] **Bench4HLS: End-to-End Evaluation of LLMs in High-Level Synthesis Code Generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.19941)]
- [2026] **Vendor-Aware Industrial Agents: RAG-Enhanced LLMs for Secure on-Premise PLC Code Generation** *Fraunhofer-Publica (Fraunhofer-Gesellschaft)* [[paper](https://publica.fraunhofer.de/handle/publica/521966)]
- [2026] **Leveraging AI Tools in Engineering Education: Promise and Pitfalls of AI in Software Development** *IEEE Revista Iberoamericana de Tecnologias del Aprendizaje* [[paper](https://doi.org/10.1109/rita.2026.3680777)]
- [2026] **Prompt Engineering Patents in Software Development: Trends, Themes, and Future Directions** *Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences* [[paper](https://doi.org/10.24251/hicss.2026.860)]
- [2026] **From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review** *IEEE Access* [[paper](https://arxiv.org/abs/2504.19678)]
- [2026] **A Neuro-Symbolic Framework for Ensuring Deterministic Reliability in AI-Assisted Structural Engineering: The SYNAPSE Architecture** *Buildings* [[paper](https://doi.org/10.3390/buildings16030534)]
- [2026] **Advances in the Modification of Enzymatic Properties Based on Protein Engineering Strategies** *Journal of Agricultural and Food Chemistry* [[paper](https://doi.org/10.1021/acs.jafc.5c13434)]
- [2026] **Reasoning Distillation for Lightweight Automated Program Repair** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.10987)]
- [2026] **Exploring Generalizable Automated Program Repair With Large Language Models** *IEEE Access* [[paper](https://arxiv.org/abs/2506.03283)]
- [2026] **Utilizing Dynamic Context and Static Analysis for Agent-Based Automated Program Repair** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3691783)]
- [2026] **Integrating A Large Language Model Into Search-based Automated Program Repair: Experiment Results** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17607868)]
- [2026] **RE-APR: Reasoning-Enhanced Automated Program Repair via Large Language Models** [[paper](https://doi.org/10.1145/3796315.3796332)]
- [2026] **FlowRepair: Search-based automated program repair of CPS controllers modeled in Simulink-Stateflow** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.108010)]

##### 2025

- [2025] **Syntax Is Not Enough: An Empirical Study of Small Transformer Models for Neural Code Repair** [[paper](https://arxiv.org/abs/2512.22216)]
- [2025] **CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models** [[paper](https://arxiv.org/abs/2512.09957)]
- [2025] **DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information** [[paper](https://arxiv.org/abs/2512.24635)]
- [2025] **A Structured and Reusable Function Generation Method by Encapsulating Code Generated by LLMs with Helper Object** *Lecture notes in networks and systems* [[paper](https://doi.org/10.1007/978-981-95-0684-2_18)]
- [2025] **Anka: A Domain-Specific Language for Reliable LLM Code Generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2512.23214)]
- [2025] **Towards autonomous normative multi-agent systems for Human-AI software engineering teams** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2512.02329)]
- [2025] **Evaluating the quality of GenAI applications in software engineering: a multi-case study** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10759-2)]
- [2025] **Using Generative AI to Design and Develop Educational Games in Engineering Education** *International Journal of Designs for Learning* [[paper](https://doi.org/10.14434/ijdl.v16i2.42059)]
- [2025] **A comparative study of large language models with chain-of thought prompting for automated program repair** *IAES International Journal of Artificial Intelligence* [[paper](https://doi.org/10.11591/ijai.v14.i6.pp4579-4589)]
- [2025] **Analysis of Research Status in the Field of Automated Program Repair** *Science and Technology of Engineering Chemistry and Environmental Protection* [[paper](https://doi.org/10.61173/3k7v9734)]
- [2025] **Automated Program Repair Based on Perturbing and Freezing Pre-trained Model** *DOAJ (DOAJ: Directory of Open Access Journals)* [[paper](https://doaj.org/article/7c375187854f4ab09ebe17652c43f660)]
- [2025] **Analysis of AdvFusion: Adapter-based Multilingual Learning for Code Large Language Models** [[paper](https://arxiv.org/abs/2511.02869)]
- [2025] **Rethinking Kernel Program Repair: Benchmarking and Enhancing LLMs with RGym** [[paper](https://arxiv.org/abs/2511.15757)]
- [2025] **Towards a Human-in-the-Loop Framework for Reliable Patch Evaluation Using an LLM-as-a-Judge** [[paper](https://arxiv.org/abs/2511.10865)]
- [2025] **HAFixAgent: History-Aware Program Repair Agent** [[paper](https://arxiv.org/abs/2511.01047)]
- [2025] **Collaborative Agents for Automated Program Repair in Ruby** [[paper](https://arxiv.org/abs/2511.03925)]
- [2025] **Enhancing Automated Program Repair via Faulty Token Localization and Quality-Aware Patch Refinement** [[paper](https://arxiv.org/abs/2511.18001)]
- [2025] **Beyond Accuracy: Behavioral Dynamics of Agentic Multi-Hunk Repair** [[paper](https://arxiv.org/abs/2511.11012)]
- [2025] **GeoColab: an LLM-based multi-agent collaborative framework for geospatial code generation** *International Journal of Digital Earth* [[paper](https://doi.org/10.1080/17538947.2025.2569405)]
- [2025] **Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection** [[paper](https://doi.org/10.1145/3719027.3765049)]
- [2025] **Hallucination in LLM-Based Code Generation: An Automotive Case Study** [[paper](https://doi.org/10.1109/fllm67465.2025.11391125)]
- [2025] **CircuitGuard: Mitigating LLM Memorization in RTL Code Generation Against IP Leakage** [[paper](https://doi.org/10.1109/iccd65941.2025.00117)]
- [2025] **The Power of Small LLMs: A Multi-Agent for Code Generation via Dynamic Precaution Tuning** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3632508)]
- [2025] **LLM-Boofuzz: Generation-Based Black-Box Fuzzing for Network Protocols via LLMs** *Electronics* [[paper](https://doi.org/10.3390/electronics14234550)]
- [2025] **AI for Requirements Engineering: Industry Adoption and Practitioner Perspectives** [[paper](https://doi.org/10.1109/asew67777.2025.00053)]
- [2025] **Enhancing techno-mathematical literacy and AI self-efficacy in engineering education through artificial intelligence applications** *Frontiers in Education* [[paper](https://doi.org/10.3389/feduc.2025.1695351)]
- [2025] **Automated Program Repair of Uncompilable Student Code** [[paper](https://arxiv.org/abs/2510.06187)]
- [2025] **SIADAFIX: issue description response for adaptive program repair** [[paper](https://arxiv.org/abs/2510.16059)] [[code](https://github.com/liauto-siada/siada-cli)]
- [2025] **Automated Repair of OpenID Connect Programs (Extended Version)** [[paper](https://arxiv.org/abs/2510.02773)]
- [2025] **Defects4C: Benchmarking Large Language Model Repair Capability with C/C++ Bugs** [[paper](https://arxiv.org/abs/2510.11059)]
- [2025] **Abstain and Validate: A Dual-LLM Policy for Reducing Noise in Agentic Program Repair** [[paper](https://arxiv.org/abs/2510.03217)]
- [2025] **PathFix: Automated Program Repair with Expected Path** [[paper](https://arxiv.org/abs/2510.14341)]
- [2025] **Nexus: Execution-Grounded Multi-Agent Test Oracle Synthesis** [[paper](https://arxiv.org/abs/2510.26423)]
- [2025] **A11YN: aligning LLMs for accessible web UI code generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2510.13914)]
- [2025] **Deus Ex LLMs: AI vs Humans in Post-Quantum Cryptographic Hardware Code Generation** [[paper](https://doi.org/10.1109/vlsi-soc64688.2025.11421711)]
- [2025] **How LLM Counselors Violate Ethical Standards in Mental Health Practice: A Practitioner-Informed Framework** *Proceedings of the AAAI/ACM Conference on AI Ethics and Society* [[paper](https://doi.org/10.1609/aies.v8i2.36632)]
- [2025] **QUASAR: Quantum Assembly Code Generation Using Tool-Augmented LLMs via Agentic RL** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2510.00967)]
- [2025] **Coordinated LLM multi-agent systems for collaborative question-answer generation** *Knowledge-Based Systems* [[paper](https://doi.org/10.1016/j.knosys.2025.114627)]
- [2025] **Exploring Data-Efficient Adaptation of Large Language Models for Code Generation** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3772721)]
- [2025] **How Natural Language Proficiency Shapes Generative AI Code for Software Engineering Tasks** *IEEE Software* [[paper](https://arxiv.org/abs/2511.04115)]
- [2025] **AI in phishing detection: a bibliometric review** *Frontiers in Artificial Intelligence* [[paper](https://doi.org/10.3389/frai.2025.1496580)]
- [2025] **Strengthening nucleic acid biosecurity screening against generative protein design tools** *Science* [[paper](https://doi.org/10.1126/science.adu8578)]
- [2025] **Generating reliable software project task flows using large language models through prompt engineering and robust evaluation** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-19170-9)]
- [2025] **A Review on AI Miniaturization: Trends and Challenges** *Applied Sciences* [[paper](https://doi.org/10.3390/app152010958)]
- [2025] **Navigating AI deployment in precision livestock farming: current trends and future prospects** *Animal Frontiers* [[paper](https://doi.org/10.1093/af/vfaf050)]
- [2025] **Do Automated Fixes Truly Mitigate Smart Contract Exploits?** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3618123)]
- [2025] **PCRepair: A Context-Aware Template-Based Approach for Automated Program Repair** *International Journal of Software Engineering and Knowledge Engineering* [[paper](https://doi.org/10.1142/s0218194025500731)]
- [2025] **CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2509.16112)] [[code](https://github.com/KDEGroup/CodeRAG)]
- [2025] **Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models** [[paper](https://arxiv.org/abs/2509.11686)]
- [2025] **RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** [[paper](https://arxiv.org/abs/2509.16701)]
- [2025] **Designing for Novice Debuggers: A Pilot Study on an AI-Assisted Debugging Tool** [[paper](https://arxiv.org/abs/2509.21067)]
- [2025] **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** [[paper](https://arxiv.org/abs/2509.02330)]
- [2025] **BloomAPR: A Bloom's Taxonomy-based Framework for Assessing the Capabilities of LLM-Powered APR Solutions** [[paper](https://arxiv.org/abs/2509.25465)]
- [2025] **Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair** [[paper](https://arxiv.org/abs/2509.05372)]
- [2025] **Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities** [[paper](https://arxiv.org/abs/2509.25894)]
- [2025] **hdl2v: A Code Translation Dataset for Enhanced LLM Verilog Generation** [[paper](https://doi.org/10.1109/mlcad65511.2025.11189055)]
- [2025] **LLM-based Iterative Refinement of Finite-State Machines with STPA Controller Constraints and Generation of IEC 61499 Code** [[paper](https://doi.org/10.1109/etfa65518.2025.11205687)]
- [2025] **LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights** *ACM Computing Surveys* [[paper](https://doi.org/10.1145/3769082)]
- [2025] **API-Aware Stepwise Prompting for LLM-based Workflow Code Generation** [[paper](https://doi.org/10.23919/apnoms67058.2025.11181303)]
- [2025] **Advancing LLM Agents for Code Generation: Observability, Orchestration, Reliable Performance** [[paper](https://doi.org/10.1109/iccns66249.2025.11428688)]
- [2025] **Guiding LLM-based Smart Contract Generation with Finite State Machine** [[paper](https://doi.org/10.24963/ijcai.2025/653)]
- [2025] **Measuring AI Impact on Software Engineering Productivity and Quality** [[paper](https://doi.org/10.1109/ubmk67458.2025.11206890)]
- [2025] **Unlocking the potential of past research: using generative AI to reconstruct healthcare simulation models** *Journal of the Operational Research Society* [[paper](https://arxiv.org/abs/2503.21646)]
- [2025] **Industry-Driven Model-Based Systems Engineering (MBSE) Workforce Competencies—An AI-Based Competency Extraction Framework** *Systems* [[paper](https://doi.org/10.3390/systems13090781)]
- [2025] **Requirements Engineering for Machine Learning-Based AI Systems: A Tertiary Study** *Journal of Software Engineering Research and Development* [[paper](https://doi.org/10.5753/jserd.2025.4892)]
- [2025] **PennyCoder: Efficient Domain-Specific LLMs for PennyLane-Based Quantum Code Generation** [[paper](https://arxiv.org/abs/2507.19562)]
- [2025] **Detailing AI techniques and tools for software engineering acceleration and automation** *Advances in computers* [[paper](https://doi.org/10.1016/bs.adcom.2025.07.007)]
- [2025] **Unlocking the Potential of the Prompt Engineering Paradigm in Software Engineering: A Systematic Literature Review** *AI* [[paper](https://doi.org/10.3390/ai6090206)]

##### 2024

- [2024] **ARJA-e for the First International Competition on Automated Program Repair** *Proceedings of the 5th ACM/IEEE International Workshop on Automated Program Repair* [[paper](https://doi.org/10.1145/3643788.3648019)]
- [2024] **ASAP-Repair: API-Specific Automated Program Repair Based on API Usage Graphs** *Proceedings of the 5th ACM/IEEE International Workshop on Automated Program Repair* [[paper](https://doi.org/10.1145/3643788.3648011)]

##### 2023

- [2023] **Automated Program Repair via Conversational Large Language Models** [[paper](https://arxiv.org/abs/2301.00001)]
- [2023] **Program Repair Competition** *2023 IEEE/ACM International Workshop on Automated Program Repair (APR)* [[paper](https://doi.org/10.1109/apr59189.2023.00010)]
- [2023] **An Extensive Study on Model Architecture and Program Representation in the Domain of Learning-based Automated Program Repair** *2023 IEEE/ACM International Workshop on Automated Program Repair (APR)* [[paper](https://doi.org/10.1109/apr59189.2023.00013)]

##### 2022

- [2022] **Scaling genetic improvement and automated program repair** *Proceedings of the Third International Workshop on Automated Program Repair* [[paper](https://doi.org/10.1145/3524459.3527353)]
- [2022] **Revisiting object similarity-based patch ranking in automated program repair** *Proceedings of the Third International Workshop on Automated Program Repair* [[paper](https://doi.org/10.1145/3524459.3527354)]
- [2022] **Be realistic** *Proceedings of the Third International Workshop on Automated Program Repair* [[paper](https://doi.org/10.1145/3524459.3527346)]

##### 2021

- [2021] **Program Committee** *2021 IEEE/ACM International Workshop on Automated Program Repair (APR)* [[paper](https://doi.org/10.1109/apr52552.2021.00007)]
- [2021] **Challenging the Stigma of Formal Program Repair** *2021 IEEE/ACM International Workshop on Automated Program Repair (APR)* [[paper](https://doi.org/10.1109/apr52552.2021.00015)]
- [2021] **Please hold on: more time = more patches? Automated program repair as anytime algorithms** *2021 IEEE/ACM International Workshop on Automated Program Repair (APR)* [[paper](https://doi.org/10.1109/apr52552.2021.00009)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **DS-EO: A Governance Framework for Multi-Agent AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21744498)]
- [2026] **From the SCR Relationship to Search Space Governance: A Foundational Analytical Framework for Delivery Reliability in AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21902420)]
- [2026] **From the SCR Meta‑Relation to Search Space Governance: A Foundational Mechanism for Delivery Reliability in AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21902421)]
- [2026] **CAMP: Cognition-Aligned Multi-stage Automated Program Repair** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108282)]
- [2026] **Prompt Optimization for LLM Code Generation via Reinforcement Learning** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-30699-9_3)]
- [2026] **From Monitoring to Authorization: The Structural Shift in Agentic AI Governance** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18743974)]
- [2026] **test-before-repair reinforcement learning for automated program repair** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21094851)]
- [2026] **Supplemental Material "Exploring Generalizable Automated Program Repair with Large Language Models"** *Figshare* [[paper](https://doi.org/10.6084/m9.figshare.29183990.v1)]
- [2026] **Replication Package for 'Examining Code Reasoning versus Memorization in Automated Program Repair'** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21344478)]
- [2026] **The Holomorphic Architecture: Rotation as Computation --- A Generative AI Foundational Framework** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20716188)]
- [2026] **Why AI Agents Cannot Govern Themselves: A Representation-Based Explanation of Enterprise Agent Failure** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20675522)]
- [2026] **Affordance-Compiled Intelligence: Observable-Only Cognitive Impedance Matching for No-Meta LLM-Integrated Systems** *Open MIND* [[paper](https://modelcontextprotocol.io/specification/2025-11-25)]
- [2026] **Exploring Code Analysis: Zero-Shot Insights on Syntax and Semantics with LLMs** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2305.12138)]
- [2026] **A multi-language perspective on the robustness of LLM code generation** *Empirical Software Engineering* [[paper](https://arxiv.org/abs/2504.19108)]
- [2026] **Automated Program Repair using Quantized Language Models and Parameter-Efficient Fine-Tuning** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108181)]
- [2026] **Assessing, Exploiting, and Mitigating Syntactic Robustness Failures in LLM-Based Code Generation** [[paper](https://arxiv.org/abs/2404.01535)]
- [2026] **False Security Confidence in Benign LLM Code Generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2604.17014)]
- [2026] **The Complexity Kink: Where LLM Code Generation Fails** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21973478)]
- [2026] **IAGD-PUBL - AI Governance and Cognitive Debt in Software Systems: Empirical Analysis of Production–Comprehension Imbalance** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19581311)]
- [2026] **An Autonomous Software Resilience: A Neuro-Symbolic Framework for Real-Time Automated Program Repair** *International Journal of Science Strategic Management and Technology* [[paper](https://doi.org/10.55041/ijsmt.v2i4.101)]
- [2026] **Incoherence as Oracle-less Measure of Error in LLM-Based Code Generation** *Proceedings of the AAAI Conference on Artificial Intelligence* [[paper](https://doi.org/10.1609/aaai.v40i39.40616)]
- [2026] **RepoAI: Automated code refactoring through multi-agent LLM orchestration and retrieval-augmented generation** *Science of Computer Programming* [[paper](https://doi.org/10.1016/j.scico.2026.103477)]
- [2026] **Bug or feature? Investigating the impact of generative AI on knowledge creation in software engineering** *VINE Journal of Information and Knowledge Management Systems* [[paper](https://doi.org/10.1108/vjikms-05-2025-0209)]
- [2026] **Copiloting the Copilots for Automated Program Repair** *Communications of the ACM* [[paper](https://doi.org/10.1145/3788082)]
- [2026] **RunBugRun: An executable dataset for automated program repair** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10790-3)]
- [2026] **Iter-T: ITERative Test Suite Generation for Automated Program Repair** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2026.3671416)]
- [2026] **Integrating a Large Language Model into Search-Based Automated Program Repair** [[paper](https://doi.org/10.1109/saner67736.2026.00017)]
- [2026] **Neuro Symbolic Automated Program Repair: A Systematic Review of LLM-Based and Symbolic Techniques** *DOAJ (DOAJ: Directory of Open Access Journals)* [[paper](https://doaj.org/article/d7e549e237bd40fa98321d46c6c2dc7c)]
- [2026] **Agents4PLC: Automating Closed-Loop PLC Code Generation and Verification in Industrial Control Systems Using LLM-Based Agents** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2026.3667895)]
- [2026] **A Model-Driven Engineering Approach to AI-Powered Healthcare Platforms** *Informatics* [[paper](https://arxiv.org/abs/2510.09308)]
- [2026] **Can test cases generated by large language models facilitate automated program repair?** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-026-10802-w)]
- [2026] **Securing LLM code generation: Leveraging prompt engineering to mitigate vulnerabilities across models and languages** *Science of Computer Programming* [[paper](https://doi.org/10.1016/j.scico.2026.103446)]
- [2026] **Leveraging LLM for P&ID-based Automated Code Generation in HVAC Fault Detection and Diagnosis** *Lecture notes in civil engineering* [[paper](https://doi.org/10.1007/978-3-032-10546-2_37)]
- [2026] **Linguistics Theory Meets LLM: Code-Switched Text Generation via Equivalence Constrained Large Language Models** [[paper](https://arxiv.org/abs/2410.22660)]
- [2026] **Automated Program Repair Based on Large Language Model and Mask Templates** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-21600-7_6)]

##### 2025

- [2025] **Programming Language Techniques for Bridging LLM Code Generation Semantic Gaps** [[paper](https://doi.org/10.1145/3759425.3763383)]
- [2025] **SE Perspective on LLMs: Biases in Code Generation, Code Interpretability, and Code Security Risks** *ACM Computing Surveys* [[paper](https://doi.org/10.1145/3774324)]
- [2025] **Comprehending C codes with LLMs: Effective comment generation through retrieval and reasoning** *Pattern Recognition Letters* [[paper](https://doi.org/10.1016/j.patrec.2025.10.007)]
- [2025] **AutoVerus: Automated Proof Generation for Rust Code** *Proceedings of the ACM on Programming Languages* [[paper](https://doi.org/10.1145/3763174)]
- [2025] **Assessing the effectiveness of recent closed-source large language models in fault localization and automated program repair** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00549-x)]
- [2025] **DeepVulHunter: enhancing the code vulnerability detection capability of LLMs through multi-round analysis** *Journal of Intelligent Information Systems* [[paper](https://doi.org/10.1007/s10844-025-00982-0)]
- [2025] **AI Applications in Depression Detection and Diagnosis: Bibliometric and Visual Analysis of Trends and Future Directions** *JMIR Mental Health* [[paper](https://doi.org/10.2196/79293)]
- [2025] **Enhancing the ability of LLMs for spaceborne equipment code generation via retrieval-augmented generation and contrastive learning** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00545-1)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Context Engineering for AI Agents in Open-Source Software** [[paper](https://arxiv.org/abs/2510.21413)]
- [2026] **Large Language Model-Based Agents for Software Engineering: A Survey** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3796507)]

##### 2025

- [2025] **The Hidden Risks of LLM-Generated Web Application Code: A Security-Centric Evaluation of Code Generation Capabilities in Large Language Models** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-13714-2_3)]
- [2025] **LLMs Integration in Software Engineering Team Projects: Roles, Impact, and a Pedagogical Design Space for AI Tools in Computing Education** *ACM Transactions on Computing Education* [[paper](https://doi.org/10.1145/3779296)]
- [2025] **Lessons Learned from the Use of Generative AI in Engineering and Quality Assurance of a WEB System for Healthcare** [[paper](https://doi.org/10.5753/sbqs.2025.15015)]
- [2025] **Large Language Models in Software Engineering: Automation, Collaboration, and Challenges** *Advances in Engineering Technology Research* [[paper](https://doi.org/10.56028/aetr.15.1.1795.2025)]
- [2025] **Towards Secure Code Generation With LLMs: A Study on Common Weakness Enumeration** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3619281)]
- [2025] **An Interdisciplinary Review of Modern Computer Science: Trends and Challenges in AI, Cybersecurity, Cloud, Blockchain, IoT, Data Science, NLP, Vision, Software Engineering, and Quantum Computing** *Scholars Journal of Engineering and Technology* [[paper](https://doi.org/10.36347/sjet.2025.v13i09.005)]
- [2025] **AI for Better UX in Computer-Aided Engineering: Is Academia Catching Up with Industry Demands? A Multivocal Literature Review** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-04200-2_20)]
- [2025] **AI and Agile Software Development: A Research Roadmap from the XP2025 Workshop** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2508.20563)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Programmers Are Poor and Overconfident Judges of LLM-Generated Assertions** [[paper](https://arxiv.org/abs/2607.08885)]
- [2026] **AI in Software Engineering** *Advances in computational intelligence and robotics book series* [[paper](https://doi.org/10.4018/979-8-2600-2811-7.ch005)]
- [2026] **The Substrate Collapse: AI Code Generation Invalidates Authorship-Based Knowledge Metrics** [[paper](https://arxiv.org/abs/2606.20882)]
- [2026] **Distillation and Quantization Effects on LLM Code Generation in HumanEval** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20563180)]
- [2026] **Detecting Incorrect LLM Explanations for Automated Program Repair** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.20954621)]
- [2026] **From Prompting to Verification: How Experience Shapes Vibe Coding Practices** [[paper](https://arxiv.org/abs/2605.24521)]
- [2026] **StatsClaw: An AI-Collaborative Workflow for Statistical Software Development** [[paper](https://arxiv.org/abs/2604.04871)]
- [2026] **BONSAI: A Mixed-Initiative Workspace for Human-AI Co-Development of Visual Analytics Applications** [[paper](https://arxiv.org/abs/2604.19247)]
- [2026] **Co-Located Tests, Better AI Code: How Test Syntax Structure Affects Foundation Model Code Generation** [[paper](https://arxiv.org/abs/2604.19826)]
- [2026] **Writability to Predictability: Structural Principles for Building-Scale AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19659692)]
- [2026] **Difficulty-Aware LLM-based Automated Program Repair Evaluation** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19249682)]
- [2026] **HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.13864)]

##### 2025

- [2025] **A Survey of Bugs in AI-Generated Code** [[paper](https://arxiv.org/abs/2512.05239)]
- [2025] **QiskitBench: A Benchmark for Automated Program Repair of Qiskit Issues** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18028602)]
- [2025] **Data Challenges in AI Systems and their Solutions: A Requirements and AI Engineering Systematic Literature Review and Comparison** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-8077403/v1)]
- [2025] **Automated Program-Repair Experiment Results** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17607869)]
- [2025] **Cracking CodeWhisperer: Analyzing Developers' Interactions and Patterns During Programming Tasks** [[paper](https://arxiv.org/abs/2510.11516)]
- [2025] **DSL-Xpert 2.0: Enhancing LLM-driven code generation for domain-specific languages** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107954)]
- [2025] **Vibe Coding in Practice: Motivations, Challenges, and a Future Outlook -- a Grey Literature Review** [[paper](https://arxiv.org/abs/2510.00328)]
- [2025] **A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code** [[paper](https://arxiv.org/abs/2508.18106)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Unveiling the power of code pre-trained models in automated program repair: A systematic review** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.113015)]

##### 2025

- [2025] **Role of Generative AI in Software Development** *INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT* [[paper](https://doi.org/10.55041/ijsrem53791)]

##### 2024

- [2024] **Large Language Models for Software Engineering: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2403.00001)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **Who Wrote This Patch? Toward Accountable Automated Program Repair** [[paper](https://doi.org/10.1145/3803437.3805552)]
- [2026] **GABBE: A Neurocognitive Swarm Architecture for Agentic AI Software Engineering** [[paper](https://doi.org/10.36227/techrxiv.177220787.72010996/v1)]
- [2026] **AI-DRIVEN TEST ENGINEERING FOR CLOUD-NATIVE SYSTEMS** *International Journal of Data Science and IoT Management System* [[paper](https://doi.org/10.64751/ijdim.2026.v5i1.297)]
- [2026] **Design and Development of an AI-Enabled Systems Engineering Model Generation Tool** *Conference on systems engineering research series* [[paper](https://doi.org/10.1007/978-3-032-12309-1_29)]

##### 2025

- [2025] **Towards a next-generation LLM empowered low-code programming industrial robotic system for human-centric smart manufacturing** *Journal of Manufacturing Systems* [[paper](https://doi.org/10.1016/j.jmsy.2025.10.012)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Agentic AI Software Engineers: Programming with Trust** *Communications of the ACM* [[paper](https://doi.org/10.1145/3769314)]
- [2026] **Non-Autoregressive Patch Generation for Efficient Automated Program Repair** *Mendeley Data* [[paper](https://doi.org/10.17632/7k7vfc8drm)]
- [2026] **AI_Master_Coder A Structured Synthetic Dataset for Reasoning-Based AI Software Engineering** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18913329)]
- [2026] **"Should I Give Up Now?" Investigating LLM Pitfalls in Software Engineering** *ACM Transactions on Software Engineering and Methodology* [[paper](https://arxiv.org/abs/2411.09916)]
- [2026] **EvolRepair: Population-Based Semantic Evolution for LLM-Driven Automated Program Repair** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.19337556)]
- [2026] **Redefining the Software Engineering Profession for AI** *Communications of the ACM* [[paper](https://doi.org/10.1145/3779312)]
- [2026] **Strategic Prompt Engineering for Enhancing AI-Generated Content in English Language Teaching Empowering EFL Contexts** *International Journal of Computer-Assisted Language Learning and Teaching* [[paper](https://doi.org/10.4018/ijcallt.398504)]
- [2026] **LLMs in Coding and Their Impact on the Commercial Software Engineering Landscape** *Advances in intelligent systems and computing* [[paper](https://doi.org/10.1007/978-3-032-07938-1_28)]

##### 2025

- [2025] **A New Vision on Software Sustainability and Its Engineering** *IEEE Software* [[paper](https://doi.org/10.1109/ms.2025.3622804)]
- [2025] **Human-Centered Software Engineering: Balancing Interaction, Artificial Intelligence, and Human Value** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-05008-3_70)]

[⬆ Back to top](#paper-list)

#### Tooling

##### 2026

- [2026] **Decomposing the Doer Effect in Programming Practice: Code Writing Stands Out Among Active Practice** [[paper](https://arxiv.org/abs/2608.02541)]
- [2026] **Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories** [[paper](https://arxiv.org/abs/2608.10319)]
- [2026] **Teaching LLMs a Low-Resource Language: Enhancing Code Completion in Pharo** [[paper](https://arxiv.org/abs/2607.04939)]
- [2026] **Alternative UX Extensions and Their Trade-offs for Code Completion in Pharo** [[paper](https://arxiv.org/abs/2607.24253)]
- [2026] **CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding** [[paper](https://arxiv.org/abs/2607.29637)] [[code](https://github.com/vinsontang1/CodeShrink)]
- [2026] **SciCodePile: A 128GB Corpus and Executable Benchmark for Challenging Scientific Code Generation** [[paper](https://arxiv.org/abs/2607.19104)] [[project](https://huggingface.co/SciCodePile)]
- [2026] **Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge** [[paper](https://arxiv.org/abs/2607.10221)]
- [2026] **Functional and Secure Code Generation with Task Vectors** [[paper](https://arxiv.org/abs/2607.07881)]
- [2026] **When AI Coding Assistants Leak Training Data: A Study of LLM Memorization in Code Generation** *Proceedings of the 3rd ACM International Conference on AI-Powered Software* [[paper](https://doi.org/10.1145/3805760.3814902)]
- [2026] **Fine-Grained Repair Knowledge Organization for Knowledge-Guided Automated Program Repair** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-92-3450-9_50)]
- [2026] **To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks** [[paper](https://arxiv.org/abs/2606.30549)]
- [2026] **A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets** *ICML 2026. Code and benchmark* [[paper](https://arxiv.org/abs/2606.13802)]
- [2026] **The Illusion of Agentic Complexity in README.md Generation: Evaluating Single-Agent vs. Multi-Agent RAG Systems** [[paper](https://arxiv.org/abs/2606.30524)]
- [2026] **JAMER: Project-Level Code Framework Dataset and Benchmark on Professional Game Engines** [[paper](https://arxiv.org/abs/2606.19830)]
- [2026] **How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study** [[paper](https://arxiv.org/abs/2605.04763)]
- [2026] **SynConfRoute: Syntax-Aware Routing for Efficient Code Completion with Small CodeLLMs** [[paper](https://arxiv.org/abs/2605.04894)]
- [2026] **Specification-Driven Development Benchmark: Security Knowledge Transition** [[paper](https://arxiv.org/abs/2606.00167)]
- [2026] **Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets** [[paper](https://arxiv.org/abs/2605.28510)]
- [2026] **Automated Context Generation for AI Code Assistants: An LLM-Powered Framework for Developer Intent Capture and Documentation Automation** *International Journal of Innovative Research and Creative Technology* [[paper](https://doi.org/10.62970/ijirct.v12.i3.2606010)]
- [2026] **On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation** [[paper](https://arxiv.org/abs/2604.13725)]
- [2026] **Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?** [[paper](https://arxiv.org/abs/2604.17338)]
- [2026] **Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy** [[paper](https://arxiv.org/abs/2604.17182)]
- [2026] **Babbling Suppression: Making LLMs Greener One Token at a Time** [[paper](https://arxiv.org/abs/2604.06755)]
- [2026] **Sema Code: Decoupling AI Coding Agents into Programmable, Embeddable Infrastructure** [[paper](https://arxiv.org/abs/2604.11045)]
- [2026] **Balancing Latency and Accuracy of Code Completion via Local-Cloud Model Cascading** [[paper](https://arxiv.org/abs/2603.05974)]
- [2026] **A framework for assessing the capabilities of code generation of constraint domain-specific languages with large language models** [[paper](https://arxiv.org/abs/2603.05278)]
- [2026] **Nova AI: AI-Powered Code Generation SaaS Using Next.js and LLM** *International Journal for Research in Applied Science and Engineering Technology* [[paper](https://doi.org/10.22214/ijraset.2026.78390)]
- [2026] **An Evaluation of Context Length Extrapolation in Long Code via Positional Embeddings and Efficient Attention** [[paper](https://arxiv.org/abs/2602.21800)]
- [2026] **Toward an Agentic Infused Software Ecosystem** [[paper](https://arxiv.org/abs/2602.20979)]
- [2026] **Automated Customization of LLMs for Enterprise Code Repositories Using Semantic Scopes** [[paper](https://arxiv.org/abs/2602.05780)]
- [2026] **Seeing is Coding: On the Effectiveness of Vision Language Models in Code Understanding** [[paper](https://arxiv.org/abs/2602.01785)]
- [2026] **Do Not Treat Code as Natural Language: Implications for Repository-Level Code Generation and Beyond** [[paper](https://arxiv.org/abs/2602.11671)]
- [2026] **Evaluating and Achieving Controllable Code Completion in Code LLM** [[paper](https://arxiv.org/abs/2601.15879)]
- [2026] **Promises, Perils, and (Timely) Heuristics for Mining Coding Agent Activity** [[paper](https://arxiv.org/abs/2601.18345)]
- [2026] **Better Call Grep: Evaluating and Improving Grep-Like Lexical Retrieval for Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2601.23254)]
- [2026] **Control Models for In-IDE Code Completion** [[paper](https://arxiv.org/abs/2601.20223)]
- [2026] **RepoShapley: Shapley-Enhanced Context Filtering for Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2601.03378)]
- [2026] **DevBench: A Realistic, Developer-Informed Benchmark for Code Generation Models** [[paper](https://arxiv.org/abs/2601.11895)]
- [2026] **How do Agents Refactor: An Empirical Study** [[paper](https://arxiv.org/abs/2601.20160)]
- [2026] **From Completion to Editing: Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning** [[paper](https://arxiv.org/abs/2601.13384)]
- [2026] **Model See, Model Do? Exposure-Aware Evaluation of Bug-vs-Fix Preference in Code LLMs** [[paper](https://arxiv.org/abs/2601.10496)]
- [2026] **Can Vision-Language Models Handle Long-Context Code? An Empirical Study on Visual Compression** [[paper](https://arxiv.org/abs/2602.00746)]
- [2026] **Are Coding Agents Generating Over-Mocked Tests? An Empirical Study** [[paper](https://arxiv.org/abs/2602.00409)]
- [2026] **SE Perspective on LLMs: Biases in Code Generation, Code Interpretability, and Code Security Risks.** *ACM Comput. Surv.* [[paper](https://dblp.org/rec/journals/csur/KrasniqiXV26)]
- [2026] **Code Roulette: How Prompt Variability Affects LLM Code Generation.** *LLM4CODE@ICSE* [[paper](https://dblp.org/rec/conf/llm4code/PaleyesRSCL26)]
- [2026] **Enhancing the ability of LLMs for spaceborne equipment code generation via retrieval-augmented generation and contrastive learning.** *Autom. Softw. Eng.* [[paper](https://dblp.org/rec/journals/ase/HeZLX26)]
- [2026] **Beyond Code Pairs: Dialogue-Based Data Generation for LLM Code Translation.** *ACL* [[paper](https://dblp.org/rec/conf/acl/ChenXCLLZTDJL26)]
- [2026] **Idea First, Code Later: Disentangling Problem Solving from Code Generation in Evaluating LLMs for Competitive Programming.** *ACL* [[paper](https://dblp.org/rec/conf/acl/HadhoudEHCHA26)]
- [2026] **BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations.** *GECCO* [[paper](https://dblp.org/rec/conf/gecco/SilvaP26)]
- [2026] **Code LLMs Still Fall Short of Top Programmers: Evaluating Algorithmic Code Generation Through Computational Thinking.** *WSDM* [[paper](https://dblp.org/rec/conf/wsdm/Chen0ZYLXLMWL26)]
- [2026] **Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2601-00509)]
- [2026] **Does Teaming-Up LLMs Improve Secure Code Generation? A Comprehensive Evaluation with Multi-LLMSecCodeEval.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2603-22717)]
- [2026] **When Prompt Under-Specification Improves Code Correctness: An Exploratory Study of Prompt Wording and Structure Effects on LLM-Based Code Generation.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2604-24712)]
- [2026] **Probing Privacy Leaks in LLM-based Code Generation via Test Generation.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2605-15248)]
- [2026] **CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2606-22082)]
- [2026] **Reward-Free Code Alignment from Pretrained or Fine-Tuned LLM: Unpacking the Trade-offs for Code Generation.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2606-28998)]
- [2026] **The Librarian Who Refused to Code: Model-Dependent Identity Enactment in LLM Code Generation.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2607-17420)]
- [2026] **A Systematic Literature Review on Generative AI in Software Engineering: Code Generation and Refactoring** *PPR* [[paper](https://doi.org/10.20944/preprints202605.1638.v1)]
- [2026] **Agentic AI for Code Quality: A Four-Agent Machine Learning System for Repository Refactoring, Public RAG, Groq Reasoning, and Reinforcement Learning** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-10348169/v1)]
- [2026] **Relationships Between Trust, Compliance, and Performance for Novice Programmers Using AI Code Generation.** *MED* [[paper](https://doi.org/10.1177/00187208261467254)]
- [2026] **From Prompt to Production: A Case Study of Human-AI Collaborative Software Development Using Claude Code Multi-Agent Orchestration** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-10253296/v1)]
- [2026] **Editorial: Advancing AI-driven code generation and synthesis: challenges, metrics, and ethical implications.** *MED* [[paper](https://doi.org/10.3389/frai.2026.1816684)]
- [2026] **AI Skills as Structural Engineering Checking Assistants: A Framework for Conversational, Traceable Code Compliance Using ACI 318-25 and ASCE 7-22** *PPR* [[paper](https://doi.org/10.21203/rs.3.rs-10009671/v1)]
- [2026] **A Comparative Analysis of Cryptographic vs. Heuristic Session Anchors for AI Commit Provenance in Distributed Version Control Systems** *PPR* [[paper](https://doi.org/10.14293/pr2199.004155.v1)]
- [2026] **An empirical comparison of AI assisted software refactoring tools.** *MED* [[paper](https://doi.org/10.1038/s41598-026-49590-0)]

##### 2025

- [2025] **Completion by Comprehension: Guiding Code Generation with Multi-Granularity Understanding** [[paper](https://arxiv.org/abs/2512.04538)]
- [2025] **Inside Out: Uncovering How Comment Internalization Steers LLMs for Better or Worse** [[paper](https://arxiv.org/abs/2512.16790)]
- [2025] **DUET: Agentic Design Understanding via Experimentation and Testing** [[paper](https://arxiv.org/abs/2512.06247)]
- [2025] **Structure-guided function-level code generation with LLMs via UML activity diagrams** *Neurocomputing* [[paper](https://doi.org/10.1016/j.neucom.2025.132502)]
- [2025] **Effective Code Membership Inference for Code Completion Models via Adversarial Prompts** [[paper](https://arxiv.org/abs/2511.15107)]
- [2025] **Automating Hardware Design and Verification from Architectural Papers via a Neural-Symbolic Graph Framework** [[paper](https://arxiv.org/abs/2511.06067)]
- [2025] **An Empirical Investigation of the Experiences of Dyslexic Software Engineers** [[paper](https://arxiv.org/abs/2511.00706)]
- [2025] **Don't Use a Cannon to Kill a Fly: Lightweight Model Editing for LLMs to Correct Deprecated API Recommendations** [[paper](https://arxiv.org/abs/2511.21022)]
- [2025] **Relative Positioning Based Code Chunking Method For Rich Context Retrieval In Repository Level Code Completion Task With Code Language Model** [[paper](https://arxiv.org/abs/2510.08610)]
- [2025] **Code4MeV2: a Research-oriented Code-completion Platform** [[paper](https://arxiv.org/abs/2510.03755)]
- [2025] **Beyond More Context: How Granularity and Order Drive Code Completion Quality** [[paper](https://arxiv.org/abs/2510.06606)]
- [2025] **SpareCodeSearch: Searching for Code Context When You Have No Spare GPU** [[paper](https://arxiv.org/abs/2510.12948)]
- [2025] **Challenge on Optimization of Context Collection for Code Completion** [[paper](https://arxiv.org/abs/2510.04349)]
- [2025] **On Pretraining for Project-Level Code Completion** [[paper](https://arxiv.org/abs/2510.13697)]
- [2025] **Mellum: Production-Grade in-IDE Contextual Code Completion with Multi-File Project Understanding** [[paper](https://arxiv.org/abs/2510.05788)]
- [2025] **LongCodeZip: Compress Long Context for Code Language Models** [[paper](https://arxiv.org/abs/2510.00446)]
- [2025] **An Open-Source Framework for LLM-Based Parallel Python Code Generation and Benchmarking** *2025 Conference on AI x Software Engineering (AIxSE)* [[paper](https://doi.org/10.1109/aixse64906.2025.00018)]
- [2025] **Bridging Developer Instructions and Code Completion Through Instruction-Aware Fill-in-the-Middle Paradigm** [[paper](https://arxiv.org/abs/2509.24637)]
- [2025] **RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval** [[paper](https://arxiv.org/abs/2509.25257)]
- [2025] **GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion** [[paper](https://arxiv.org/abs/2509.05980)]
- [2025] **Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs** [[paper](https://arxiv.org/abs/2509.25873)]
- [2025] **Enhancing Python Programming Education with an AI-Powered Code Helper: Design, Implementation, and Impact** [[paper](https://arxiv.org/abs/2509.20518)]
- [2025] **Review of: "DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent"** [[paper](https://doi.org/10.32388/p3nbe5)]
- [2025] **RKE-Coder: A LLMs-Based Code Generation Framework with Algorithmic and Code Knowledge Integration.** *NLPCC* [[paper](https://dblp.org/rec/conf/nlpcc/DengZHW25)]
- [2025] **CodeLutra: Boosting LLM Code Generation via Preference-Guided Refinement.** *Trans. Mach. Learn. Res.* [[paper](https://dblp.org/rec/journals/tmlr/TaoC0MR0M25)]
- [2025] **Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation.** *ACM Trans. Softw. Eng. Methodol.* [[paper](https://dblp.org/rec/journals/tosem/WangZFLSLP25)]
- [2025] **HumanEvalComm: Benchmarking the Communication Competence of Code Generation for LLMs and LLM Agents.** *ACM Trans. Softw. Eng. Methodol.* [[paper](https://dblp.org/rec/journals/tosem/WuF25)]

##### 2024

- [2024] **CreativEval: Evaluating Creativity of LLM-Based Hardware Code Generation** *2024 IEEE LLM Aided Design Workshop (LAD)* [[paper](https://doi.org/10.1109/lad62341.2024.10691798)]
- [2024] **Multi-Disease AI Diagnosis System Using Minimal Code and LLM-Powered Explanations** [[paper](https://doi.org/10.22541/au.175269957.75269693/v1)]
- [2024] **Rediscovering Architectural Decision Records: How Persistent Design Context Improves LLM Code Generation** [[paper](https://doi.org/10.36227/techrxiv.177205025.54351571/v1)]

##### 2023

- [2023] **Ethical Considerations of LLM-Driven Quantum Code Generation for Optimization Tasks** *The American Journal of Engineering and Technology* [[paper](https://doi.org/10.37547/tajet/volume05issue12-13)]

[⬆ Back to top](#paper-list)

### Security & Supply Chain

#### Method

##### 2026

- [2026] **Cross-Corpus Evaluation of Generalizable Vulnerability Detection in IoT Firmware** [[paper](https://arxiv.org/abs/2608.11492)]
- [2026] **VICBench: A Multi-Language Benchmark for Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.12246)]
- [2026] **CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.03134)]
- [2026] **Vulnerability Detection in AArch64 Machine Code Using a Digital Twin** [[paper](https://arxiv.org/abs/2608.02125)]
- [2026] **Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking** [[paper](https://arxiv.org/abs/2608.14533)]
- [2026] **myESI (My Enterprise Security Intelligence): An SBOM-Powered Platform for Software Supply Chain Security and Compliance Automation** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21986125)]
- [2026] **Penetration testing for software supply chain security: A lifecycle-oriented review of vulnerabilities, third-party dependencies, and mitigation strategies** *Journal of Applied Computer and Information Technology* [[paper](https://doi.org/10.67131/jacoit.v1i2.22)]
- [2026] **DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection** [[paper](https://arxiv.org/abs/2607.13439)]
- [2026] **RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities** [[paper](https://arxiv.org/abs/2607.04729)]
- [2026] **Why Not Fix It Once and for All? An Empirical Study of Multiple Patches for Vulnerability Fixes in Open-Source Software** [[paper](https://arxiv.org/abs/2607.13206)]
- [2026] **JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode** [[paper](https://arxiv.org/abs/2607.02825)]
- [2026] **VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents** [[paper](https://arxiv.org/abs/2607.09653)]
- [2026] **Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing** [[paper](https://arxiv.org/abs/2607.21983)]
- [2026] **Cybersecurity for smart and resilient manufacturing and supply chains: A systematic review of the evolving knowledge base** *Computers & Industrial Engineering* [[paper](https://doi.org/10.1016/j.cie.2026.112244)]
- [2026] **Evaluating LLMs for Real-World Web Vulnerability Detection** [[paper](https://arxiv.org/abs/2606.21397)]
- [2026] **Decoupled Smart Contract Audits: Lightweight LLM Framework via Distillation and Aggregation** [[paper](https://arxiv.org/abs/2606.03128)]
- [2026] **Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2606.30587)]
- [2026] **Code-Augur: Agentic Vulnerability Detection via Specification Inference** [[paper](https://arxiv.org/abs/2606.18619)]
- [2026] **Understanding Binary Code Similarity for Real-World Vulnerability Detection: A Large-Scale Empirical Study** [[paper](https://arxiv.org/abs/2606.28870)]
- [2026] **AttackonCTF: Defending Hardware Security Competition Benchmarks in the Age of LLMs** [[paper](https://arxiv.org/abs/2606.15809)]
- [2026] **MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents** [[paper](https://arxiv.org/abs/2606.20717)]
- [2026] **Evaluating LLMs for Obfuscation Detection and Classification in Android Apps** [[paper](https://arxiv.org/abs/2606.14233)]
- [2026] **CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?** [[paper](https://arxiv.org/abs/2606.26216)]
- [2026] **Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases** [[paper](https://arxiv.org/abs/2606.22263)]
- [2026] **A Hybrid AI-Based Detection Method for Open-Source Software Supply Chain Security Threats** *Journal of the Korea Academia-Industrial cooperation Society* [[paper](https://doi.org/10.5762/kais.2026.27.6.288)]
- [2026] **A Hyperledger Fabric-Based SBOM Management System for Secure Software Supply Chain Integrity** *Electronics* [[paper](https://doi.org/10.3390/electronics15122573)]
- [2026] **Security Challenges in AI and Cloud Infrastructure, Including Software Supply Chains and Model-Deployment Pipelines** *American Journal of Innovation in Science and Engineering* [[paper](https://doi.org/10.54536/ajise.v5i2.7220)]
- [2026] **Evaluating the Out-of-Domain Generalization in Source Code Vulnerability Detection** *Engineering Technology & Applied Science Research* [[paper](https://doi.org/10.48084/etasr.18302)]
- [2026] **DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization** [[paper](https://arxiv.org/abs/2605.11015)] [[code](https://github.com/vinsontang1/DCVD)]
- [2026] **Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection** [[paper](https://arxiv.org/abs/2605.29901)]
- [2026] **Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts** [[paper](https://arxiv.org/abs/2605.03697)]
- [2026] **Smart Contract Security Beyond Detection** [[paper](https://arxiv.org/abs/2605.09124)]
- [2026] **MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection** [[paper](https://arxiv.org/abs/2605.10240)]
- [2026] **AgenticVM: Agentic AI for Adaptive Software Vulnerability Management** [[paper](https://arxiv.org/abs/2605.01739)]
- [2026] **FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction** [[paper](https://arxiv.org/abs/2605.21779)]
- [2026] **Contextualizing Security and Privacy of Software-Defined Vehicles: A Literature Review and Industry Perspectives** *ACM Computing Surveys* [[paper](https://arxiv.org/abs/2411.10612)]
- [2026] **An empirical analysis of vulnerability detection tools for solidity smart contracts** *Empirical Software Engineering* [[paper](https://arxiv.org/abs/2505.15756)]
- [2026] **A Ground-Truth-Based Evaluation of Vulnerability Detection Across Multiple Ecosystems** [[paper](https://arxiv.org/abs/2604.21111)]
- [2026] **SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.19031)]
- [2026] **Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection** [[paper](https://arxiv.org/abs/2604.01637)]
- [2026] **VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.26313)]
- [2026] **Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis** [[paper](https://arxiv.org/abs/2604.19012)]
- [2026] **Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.06633)]
- [2026] **CrossCommitVuln-Bench: A Dataset of Multi-Commit Python Vulnerabilities Invisible to Per-Commit Static Analysis** [[paper](https://arxiv.org/abs/2604.21917)]
- [2026] **MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification** [[paper](https://arxiv.org/abs/2604.24398)]
- [2026] **Integrated Threat Modeling Framework for Software Supply Chain Security** *Journal of Eastern Europe Research in Business & Economics* [[paper](https://doi.org/10.5171/2025.4641625)]
- [2026] **On the Security of Lightweight Homomorphic Obfuscation for Protecting Against Hardware Trojans** *IACR Transactions on Cryptographic Hardware and Embedded Systems* [[paper](https://doi.org/10.46586/tches.v2026.i2.736-763)]
- [2026] **Zero-Shot Vulnerability Detection in Low-Resource Smart Contracts Through Solidity-Only Training** [[paper](https://arxiv.org/abs/2603.21058)]
- [2026] **VulnScout-C: A Lightweight Transformer for C Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2603.28309)]
- [2026] **Software Vulnerability Detection Using a Lightweight Graph Neural Network** [[paper](https://arxiv.org/abs/2603.29216)]
- [2026] **Efficient Software Vulnerability Detection Using Transformer-based Models** [[paper](https://arxiv.org/abs/2604.00112)]
- [2026] **Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization** [[paper](https://arxiv.org/abs/2603.26270)]
- [2026] **Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review** [[paper](https://arxiv.org/abs/2603.18740)]
- [2026] **When Labels Are Scarce: A Systematic Mapping of Label-Efficient Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.00079)]
- [2026] **SseRex: Practical Symbolic Execution of Solana Smart Contracts** [[paper](https://arxiv.org/abs/2603.16349)]
- [2026] **SecureRAG-RTL: A Retrieval-Augmented, Multi-Agent, Zero-Shot LLM-Driven Framework for Hardware Vulnerability Detection** [[paper](https://arxiv.org/abs/2603.05689)]
- [2026] **Detecting Protracted Vulnerabilities in Open Source Projects** [[paper](https://arxiv.org/abs/2603.27067)]
- [2026] **Cryptographic Package Integrity Verification For Enhancing Software Supply Chain Security** *Research Digest on Engineering Management and Social Innovations* [[paper](https://doi.org/10.46647/icetetas011)]
- [2026] **Navigating global supply chain opportunities in IT outsourcing and offshoring** *Journal of Enterprise Information Management* [[paper](https://doi.org/10.1108/jeim-03-2025-0155)]
- [2026] **Domain-aware graph neural networks for source code vulnerability detection** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2026.108104)]
- [2026] **Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection** [[paper](https://arxiv.org/abs/2602.05868)]
- [2026] **Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection** [[paper](https://arxiv.org/abs/2602.06751)]
- [2026] **SecCodePRM: A Process Reward Model for Code Security** [[paper](https://arxiv.org/abs/2602.10418)]
- [2026] **Enhancing Continual Learning for Software Vulnerability Prediction: Addressing Catastrophic Forgetting via Hybrid-Confidence-Aware Selective Replay for Temporal LLM Fine-Tuning** [[paper](https://arxiv.org/abs/2602.23834)]
- [2026] **Toward Quantum-Safe Software Engineering: A Vision for Post-Quantum Cryptography Migration** [[paper](https://arxiv.org/abs/2602.05759)]
- [2026] **VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection** [[paper](https://arxiv.org/abs/2602.10787)]
- [2026] **Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents** [[paper](https://arxiv.org/abs/2602.02164)]
- [2026] **Secure Code Generation via Online Reinforcement Learning with Vulnerability Reward Model** [[paper](https://arxiv.org/abs/2602.07422)] [[code](https://github.com/AndrewWTY/SecCoderX)]
- [2026] **Enhancing Software Supply Chain Security Through Cryptographic Package Integrity Verification** [[paper](https://doi.org/10.1109/southeastcon63549.2026.11475986)]
- [2026] **DevSecOps Aware in Healthcare: SBOM-Driven Supply-Chain Assurance (SLSA) with Policy-Based Cost Guardrails and Continuous Security Validation** *International Journal of Computer Applications Technology and Research* [[paper](https://doi.org/10.7753/ijcatr1308.1021)]
- [2026] **A Multimodal-based Approach for Smart Contract Vulnerability Detection** *Journal of Signal Processing Systems* [[paper](https://doi.org/10.1007/s11265-026-01985-y)]
- [2026] **When datasets deceive: Exposing overlap in smart contract vulnerability detection** *ICT Express* [[paper](https://doi.org/10.1016/j.icte.2026.02.002)]
- [2026] **From SFT to RL: Demystifying the Post-Training Pipeline for LLM-based Vulnerability Detection** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2602.14012)]
- [2026] **Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities** [[paper](https://arxiv.org/abs/2601.06914)]
- [2026] **Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code** [[paper](https://arxiv.org/abs/2601.09157)]
- [2026] **Multi-Agent Taint Specification Extraction for Vulnerability Detection** [[paper](https://arxiv.org/abs/2601.10865)]
- [2026] **Zer0n: An AI-Assisted Vulnerability Discovery and Blockchain-Backed Integrity Framework** [[paper](https://arxiv.org/abs/2601.07019)]
- [2026] **Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan** [[paper](https://arxiv.org/abs/2601.07334)]
- [2026] **HogVul: Black-box Adversarial Code Generation Framework Against LM-based Vulnerability Detectors** [[paper](https://arxiv.org/abs/2601.05587)]
- [2026] **LAsset: An LLM-assisted Security Asset Identification Framework for System-on-Chip (SoC) Verification** [[paper](https://arxiv.org/abs/2601.02624)]
- [2026] **AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization** [[paper](https://arxiv.org/abs/2601.06177)]
- [2026] **Operationalizing Software Supply Chain Security in Cloud-Native DevSecOps Environments** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18240790)]
- [2026] **RISK-AWARE SOFTWARE SUPPLY CHAIN SECURITY FOR AVIATION SYSTEMS USING SBOM** *Computer Science Bulletin* [[paper](https://doi.org/10.71465/csb213)]
- [2026] **Cascaded Vulnerability Attacks in Software Supply Chains** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.20158)]
- [2026] **Generative artificial intelligence and ChatGPT in agriculture supply chain management: a systematic literature review and future research agenda** *British Food Journal* [[paper](https://doi.org/10.1108/bfj-05-2025-0720)]
- [2026] **On the Security of the Software Supply Chain for the Cloud** *Aaltodoc (Aalto University)* [[paper](https://aaltodoc.aalto.fi/handle/123456789/146729)]
- [2026] **VulSCA: A Community-Level SCA Approach for Accurate C/C++ Supply Chain Vulnerability Analysis** [[paper](https://doi.org/10.14722/ndss.2026.230613)]
- [2026] **Uncovering the Security Landscape of Maritime Software-Defined Radios: A Threat Modeling Perspective** *Applied Sciences* [[paper](https://doi.org/10.3390/app16020813)]
- [2026] **Threat Landscape in Artificial Intelligence Systems: Taxonomy, Attack Vectors and Security Implications** *World Journal of Advanced Research and Reviews* [[paper](https://doi.org/10.30574/wjarr.2026.29.1.0007)]
- [2026] **Many hands make light work: An LLM-based multi-agent system for detecting malicious PyPI packages** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2026.112792)]
- [2026] **CQLLM: A Framework for Generating CodeQL Security Vulnerability Detection Code Based on Large Language Model** *Applied Sciences* [[paper](https://doi.org/10.3390/app16010517)]
- [2026] **AI-Powered Vulnerability Detection and Patch Management in Cybersecurity: A Systematic Review of Techniques, Challenges, and Emerging Trends** *Machine Learning and Knowledge Extraction* [[paper](https://doi.org/10.3390/make8010019)]
- [2026] **Evaluating Retrieval-Augmented Generation for LLM-Based Vulnerability Detection: An Empirical Study on Real-World Java Vulnerabilities** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3676577)]
- [2026] **Dynamic Neuro-Fuzzy Vulnerability Detection System (DNF-VDS)** *Cureus Journal of Computer Science.* [[paper](https://doi.org/10.7759/s44389-025-00009-3)]
- [2026] **Closing the Loop: Agentic AI for Continuous Vulnerability Detection, Validation, and Remediation** *International Journal of Artificial Intelligence Data Science and Machine Learning* [[paper](https://doi.org/10.63282/3050-9262.ijaidsml-v7i1p143)]
- [2026] **Solidity Meets LLMs: A Transformer-Based Approach to Smart Contract Vulnerability Detection** *Communications in computer and information science* [[paper](https://doi.org/10.1007/978-3-032-15632-7_17)]

##### 2025

- [2025] **Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation** [[paper](https://arxiv.org/abs/2512.01255)]
- [2025] **SHERLOCK: A Deep Learning Approach To Detect Software Vulnerabilities** [[paper](https://arxiv.org/abs/2512.12593)]
- [2025] **A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.16538)]
- [2025] **VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.07533)] [[code](https://github.com/ucsb-mlsec/VulnLLM-R)]
- [2025] **SoK: Understanding (New) Security Issues Across AI4Code Use Cases** [[paper](https://arxiv.org/abs/2512.18456)]
- [2025] **Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.22306)]
- [2025] **Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning** [[paper](https://arxiv.org/abs/2512.09006)] [[code](https://github.com/DynaSoumhaneOuchebara/Llama-based-vulnerability-detection)]
- [2025] **Software supply chain: A taxonomy of attacks, mitigations and risk assessment strategies** *Journal of Information Security and Applications* [[paper](https://doi.org/10.1016/j.jisa.2025.104324)]
- [2025] **AI-Driven Software Supply Chain Security: A Unified Analysis of Threats, Detection, and Defense-in-Depth Strategies** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18005868)]
- [2025] **A Multi-Level Software Supply Chain Security Defense System for Cloud-Native and High-Performance Computing Environments** [[paper](https://doi.org/10.1109/fit67061.2025.11333619)]
- [2025] **Automating and Enhancing the Security of the Software Supply Chain** [[paper](https://doi.org/10.1109/icicse66971.2025.11430050)]
- [2025] **Supplementary Material for "Evaluating Foundation Model Integration Strategies for Detecting PII in Java Software Engineering Pipelines"** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17993620)]
- [2025] **Context-Enhanced Vulnerability Detection Based on Large Language Models** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3779222)]
- [2025] **MANDO-LLM: Heterogeneous Graph Transformers with Large Language Models for Smart Contract Vulnerability Detection** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3765751)]
- [2025] **Optimizing Code Embeddings and ML Classifiers for Python Source code Vulnerability Detection** [[paper](https://doi.org/10.1145/3773276.3776566)]
- [2025] **Vulnerability Detection of Blockchain Smart Contracts Based on GNN with Multi-Head Attention Mechanism** *Journal of Computer Science and Frontier Technologies* [[paper](https://doi.org/10.63313/jcsft.9028)]
- [2025] **Adaptive Multi-Scale Feature Extraction for Zero-Day Vulnerability Detection in System Binaries** *Computer Science Bulletin* [[paper](https://doi.org/10.71465/csb159)]
- [2025] **A Large Scale Study of AI-based Binary Function Similarity Detection Techniques for Security Researchers and Practitioners** [[paper](https://arxiv.org/abs/2511.01180)]
- [2025] **LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework** [[paper](https://arxiv.org/abs/2511.18438)]
- [2025] **Large Language Model based Smart Contract Auditing with LLMBugScanner** [[paper](https://arxiv.org/abs/2512.02069)]
- [2025] **UniBOM -- A Unified SBOM Analysis and Visualisation Tool for IoT Systems and Beyond** [[paper](https://arxiv.org/abs/2511.22359)]
- [2025] **VULPO: Context-Aware Vulnerability Detection via On-Policy LLM Optimization** [[paper](https://arxiv.org/abs/2511.11896)]
- [2025] **Code vulnerability detection based on augmented program dependency graph and optimized CodeBERT** *Scientific Reports* [[paper](https://doi.org/10.1038/s41598-025-23029-4)]
- [2025] **Modern Approaches to Software Vulnerability Detection: A Survey of Machine Learning, Deep Learning, and Large Language Models** *Electronics* [[paper](https://doi.org/10.3390/electronics14224449)]
- [2025] **Explainable DNN for smart contract vulnerability detection in the Metaverse** *High-Confidence Computing* [[paper](https://doi.org/10.1016/j.hcc.2025.100374)]
- [2025] **A novel approach for software vulnerability detection based on ensemble learning model** *Computers & Electrical Engineering* [[paper](https://doi.org/10.1016/j.compeleceng.2025.110848)]
- [2025] **Optimized DeBERTa for Efficient Smart Contract Vulnerability Detection** [[paper](https://doi.org/10.23919/apcc64555.2025.11279833)]
- [2025] **An Empirical Evaluation of LLM-Based Approaches for Code Vulnerability Detection: RAG, SFT, and Dual-Agent Systems** [[paper](https://doi.org/10.1109/cascon66301.2025.00045)]
- [2025] **<scp>CrossGuard</scp> : Runtime‐Adaptive <scp>LLM</scp> Fuzzing for Cross‐Contract Vulnerabilities Detection** *Concurrency and Computation Practice and Experience* [[paper](https://doi.org/10.1002/cpe.70421)]
- [2025] **Dependable Code Repair with LLMs: AI-Driven Vulnerability Detection and Automated Patching** [[paper](https://doi.org/10.1109/prdc67299.2025.00032)]
- [2025] **Graph attention network vulnerability detection model with global feature augmentation for smart contracts** *Journal of Cloud Computing Advances Systems and Applications* [[paper](https://doi.org/10.1186/s13677-025-00798-x)]
- [2025] **ML-based Fuzzing for Vulnerability Detection: Methods, Benchmarks, and Open Challenges-A Review** [[paper](https://doi.org/10.1109/iceca66444.2025.11382854)]
- [2025] **QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild** [[paper](https://arxiv.org/abs/2510.04056)]
- [2025] **ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.17919)]
- [2025] **NatGVD: Natural Adversarial Example Attack towards Graph-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.04987)]
- [2025] **Distilling Lightweight Language Models for C/C++ Vulnerabilities** [[paper](https://arxiv.org/abs/2510.06645)] [[code](https://github.com/yangxiaoxuan123/FineSec_detect)]
- [2025] **MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.04397)]
- [2025] **On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.27675)]
- [2025] **Bridging Semantics & Structure for Software Vulnerability Detection using Hybrid Network Models** [[paper](https://arxiv.org/abs/2510.10321)]
- [2025] **TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts** [[paper](https://arxiv.org/abs/2510.18192)]
- [2025] **POLAR: Automating Cyber Threat Prioritization through LLM-Powered Assessment** [[paper](https://arxiv.org/abs/2510.01552)]
- [2025] **HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities** [[paper](https://arxiv.org/abs/2510.12200)]
- [2025] **Measuring Enterprise Software Supply Chain Security using Public Repositories** [[paper](https://doi.org/10.1145/3733827.3765529)]
- [2025] **Analyzing the Gap between Academic Research Trends and Policy Requirements in Software Supply Chain Security : An LDA Topic Modeling Approach** *Jouranl of Information and Security* [[paper](https://doi.org/10.33778/kcsa.2025.25.4.217)]
- [2025] **Zero Trust CI/CD Pipeline: A Blueprint for Secure Software Delivery in Modern DevSecOp** [[paper](https://doi.org/10.1109/upwiecon67212.2025.11390387)]
- [2025] **The progress of research on the nexus between food security and biodiversity conservation: a systematic review** *Frontiers in Sustainable Food Systems* [[paper](https://doi.org/10.3389/fsufs.2025.1664633)]
- [2025] **VISION: Robust and Interpretable Code Vulnerability Detection Leveraging Counterfactual Augmentation** *Proceedings of the AAAI/ACM Conference on AI Ethics and Society* [[paper](https://doi.org/10.1609/aies.v8i1.36592)]
- [2025] **A zero-shot framework for cross-project vulnerability detection in source code** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10749-4)]
- [2025] **Machine Learning Approaches for Vulnerability Detection in Smart Contracts** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-6691317/v1)]
- [2025] **ByteEye: A smart contract vulnerability detection framework at bytecode level with graph neural networks** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00559-9)]
- [2025] **DeepVulMatch: Learning and Matching Latent Vulnerability Representations for Dual-Granularity Vulnerability Detection** *IEEE Transactions on Reliability* [[paper](https://doi.org/10.1109/tr.2025.3605871)]
- [2025] **Contract-Graph Fusion and Cross-Graph Matching for Smart-Contract Vulnerability Detection** *Applied Sciences* [[paper](https://doi.org/10.3390/app151910844)]
- [2025] **Ensemble multi-label machine learning solidity smart contract vulnerability detection model** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05725-y)]
- [2025] **A machine learning approach to vulnerability detection combining software metrics and topic modelling: Evidence from smart contracts** *Machine Learning with Applications* [[paper](https://doi.org/10.1016/j.mlwa.2025.100759)]
- [2025] **LISA Technical Report: An Agentic Framework for Smart Contract Auditing** [[paper](https://arxiv.org/abs/2509.24698)]
- [2025] **SoK: A Beginner-Friendly Introduction to Fault Injection Attacks** [[paper](https://arxiv.org/abs/2509.18341)]
- [2025] **LLM-Driven SAST-Genius: A Hybrid Static Analysis Framework for Comprehensive and Actionable Security** [[paper](https://arxiv.org/abs/2509.15433)]
- [2025] **All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching** [[paper](https://arxiv.org/abs/2509.07225)] [[code](https://github.com/o2lab/afc-crs-all-you-need-is-a-fuzzing-brain)] [[project](https://o2lab.github.io/FuzzingBrain-Leaderboard/)]
- [2025] **From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization** [[paper](https://arxiv.org/abs/2510.02389)]
- [2025] **FuzzRDUCC: Fuzzing with Reconstructed Def-Use Chain Coverage** [[paper](https://arxiv.org/abs/2509.04967)]
- [2025] **SecureBERT 2.0: Advanced Language Model for Cybersecurity Intelligence** [[paper](https://arxiv.org/abs/2510.00240)]
- [2025] **Advancing Automotive Software Supply Chain Security: A Blockchain-Reproducible Build Approach** *SAE technical papers on CD-ROM/SAE technical paper series* [[paper](https://doi.org/10.4271/2025-01-0456)]
- [2025] **Towards Explainable Vulnerability Detection With Large Language Models** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3605442)]
- [2025] **Interaction-Aware Vulnerability Detection in Smart Contract Bytecodes** *IEEE Transactions on Dependable and Secure Computing* [[paper](https://doi.org/10.1109/tdsc.2025.3605773)]
- [2025] **Vulnerability Detection in Solidity Smart Contracts via Machine Learning: A Qualitative Analysis** *Blockchain Research and Applications* [[paper](https://arxiv.org/abs/2407.18639)]
- [2025] **VulTriNet: A software vulnerability detection method based on tri-channel network** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107893)]
- [2025] **Smart Contract Vulnerability Detection Based on Dual Adversarial Domain Adaptation** *IEEE Transactions on Reliability* [[paper](https://doi.org/10.1109/tr.2025.3606485)]
- [2025] **GPTVD: vulnerability detection and analysis method based on LLM’s chain of thoughts** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00550-4)]
- [2025] **HMF: Enhancing reentrancy vulnerability detection and repair with a hybrid model framework** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-025-00546-0)]
- [2025] **Machine Learning Applications in Cyber Security: Software Repository Utilization for Vulnerability Centric Vulnerability Detection** [[paper](https://doi.org/10.1109/apcit65661.2025.11411035)]
- [2025] **Utilizing Large Programming Language Models on Software Vulnerability Detection** [[paper](https://doi.org/10.1109/asyu67174.2025.11208282)]
- [2025] **A Triplet-Learning-Based Framework for Cross-Version Smart Contract Vulnerability Detection** *IEEE Internet of Things Journal* [[paper](https://doi.org/10.1109/jiot.2025.3615991)]
- [2025] **GTVD: a multi-level aggregation vulnerability detection method based on full-dependency program graph** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05506-7)]
- [2025] **VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving** [[paper](https://arxiv.org/abs/2509.00882)]
- [2025] **AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset** [[paper](https://arxiv.org/abs/2508.20866)]
- [2025] **Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias** [[paper](https://arxiv.org/abs/2508.17361)]
- [2025] **Integrating Machine Learning into the Security of Containerized Workloads** *Journal of Computer Science and Technology Studies* [[paper](https://doi.org/10.32996/jcsts.2025.7.9.17)]
- [2025] **Metaverse Security: LLM-Based Malicious Code Detection Through Token Optimization** [[paper](https://doi.org/10.1109/metacom65502.2025.00057)]
- [2025] **Enhancing Fine-Grained Vulnerability Detection With Reinforcement Learning** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3603400)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **Identifying Gaps in Software Supply Chain Security Systems Using the AStRA Model** *Purdue* [[paper](https://doi.org/10.25394/pgs.33080933.v1)]
- [2026] **Chainmail: A Unified Open-Source Workbench for Software Supply Chain Security** *Open MIND* [[paper](https://chainmail.saisravancherukuri.com)]
- [2026] **Security risk assessment of android automotive OS software supply chain using firmware reverse engineering** *Computers & Security* [[paper](https://doi.org/10.1016/j.cose.2026.104923)]
- [2026] **Evaluating line-level localization ability of learning-based code vulnerability detection models** *Machine Learning* [[paper](https://doi.org/10.1007/s10994-025-06902-1)]
- [2026] **AI Supply Chain Security: MBOM-PQC Provenance, PQC Attestation, and a Maturity Model for Quantum-Resistant Assurance** *Preprints.org* [[paper](https://doi.org/10.20944/preprints202603.1963.v1)]
- [2026] **HOGAT: Higher-Order Graph Attention Networks for Vulnerability Detection in Smart Contracts** *Iranian Journal of Science and Technology Transactions of Electrical Engineering* [[paper](https://doi.org/10.1007/s40998-026-01056-9)]
- [2026] **KD-SecBERT: A Knowledge-Distilled Bidirectional Encoder Optimized for Open-Source Software Supply Chain Security in Smart Grid Applications** *Electronics* [[paper](https://doi.org/10.3390/electronics15020345)]
- [2026] **SOFTWARE SUPPLY CHAIN SECURITY: CONCEPTS, MODELS AND CHALLENGES OF TODAY** *Scientific papers of Donetsk National Technical University Series Informatics Cybernetics and Computer Science* [[paper](https://doi.org/10.31474/1996-1588-2026-1-42-102-108)]
- [2026] **Research agenda and Guest editorial: Metaverse adoption and implementation in logistics and supply chain management: challenges, issues and opportunities** *The International Journal of Logistics Management* [[paper](https://doi.org/10.1108/ijlm-01-2026-784)]
- [2026] **Vulnerability Detection: From Formal Verification to Large Language Models and Hybrid Approaches: A Comprehensive Overview** [[paper](https://doi.org/10.1007/978-3-031-99447-0_3)]
- [2026] **Robust vulnerability detection with limited data via training-efficient adversarial reprogramming** *Automated Software Engineering* [[paper](https://doi.org/10.1007/s10515-026-00590-4)]

##### 2025

- [2025] **Editorial: Balancing continuity and change in operations and supply chain management research** *International Journal of Operations & Production Management* [[paper](https://doi.org/10.1108/ijopm-12-2025-017)]
- [2025] **Blockchain technology adoption to improve supply chain efficiency: a resource-based view** *Benchmarking An International Journal* [[paper](https://doi.org/10.1108/bij-02-2025-0143)]
- [2025] **Investigating water security and climate vulnerability in urban informal settlements: a case of Kanyama township, Lusaka, Zambia** *Acque Sotterranee-Italian Journal of Groundwater* [[paper](https://doi.org/10.7343/as-2025-863)]
- [2025] **DeepDesc: integrating retrieval-augmented generation with large language models for smart contract vulnerability detection** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10770-7)]
- [2025] **Vul-FDMG: Fusing Dataflow Analysis and Graph Neural Networks for Multi-Granularity Vulnerability Detection** [[paper](https://doi.org/10.1109/eiecc67963.2025.11409511)]
- [2025] **Dissertation Research Description: The Potential of SBOMs to Increase Software Supply Chain Security** [[paper](https://doi.org/10.1145/3719027.3765576)]
- [2025] **Learning-based models for vulnerability detection: an extensive study** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10734-x)]
- [2025] **VulTrLM: LLM-assisted vulnerability detection via AST decomposition and comment enhancement** *Empirical Software Engineering* [[paper](https://doi.org/10.1007/s10664-025-10738-7)]
- [2025] **Smart Contract Vulnerability Detection Based on Symbolic Execution and Graph Neural Networks** *Computers, materials & continua/Computers, materials & continua (Print)* [[paper](https://doi.org/10.32604/cmc.2025.070930)]
- [2025] **VDMPAGR: A vulnerability detection model based on pointer analysis and graph representation** *Information and Software Technology* [[paper](https://doi.org/10.1016/j.infsof.2025.107982)]
- [2025] **Digital pathways to supply chain viability: exploring nice and must-to have practices in dynamic environment –insight from SEM and NCA** *Journal of Enterprise Information Management* [[paper](https://doi.org/10.1108/jeim-05-2025-0367)]
- [2025] **Secure and Privacy‐Preserving Data Sharing in <scp>6G</scp> ‐Enabled Blockchain <scp>IoT</scp> Healthcare Systems** *Security and Privacy* [[paper](https://doi.org/10.1002/spy2.70105)]
- [2025] **M2CVD: Enhancing Vulnerability Understanding through Multi-Model Collaboration for Code Vulnerability Detection** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3771923)]
- [2025] **FuncVul: An Effective Function Level Vulnerability Detection Model Using LLM and Code Chunk** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-07884-1_9)]
- [2025] **Leveraging Intra- and Inter-References in vulnerability detection using Multi-Agent collaboration based on LLMs** *Cluster Computing* [[paper](https://doi.org/10.1007/s10586-025-05721-2)]
- [2025] **GenDetect: Generative Large Language Model Usage in Smart Contract Vulnerability Detection** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-95-2961-2_22)]
- [2025] **A Method for Assessing the Security Risks of the Software Supply Chain in the Power System Based on Triangular Fuzzy Entropy** [[paper](https://doi.org/10.1109/aecspe66597.2025.00095)]
- [2025] **CodeSpeak: Improving smart contract vulnerability detection via LLM-assisted code analysis** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112635)]
- [2025] **PVDetector: Pretrained Vulnerability Detection on Vulnerability-enriched Code Semantic Graph** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3768582)]
- [2025] **On the Use of Imbalanced Datasets for Learning-Based Vulnerability Detection** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-05188-2_20)]
- [2025] **ChipFuzzer: Towards Fuzzing Matter-Based IoT Devices for Vulnerability Detection** *Lecture notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering* [[paper](https://doi.org/10.1007/978-3-031-94455-0_2)]
- [2025] **SmartScope: Smart contract vulnerability detection via heterogeneous graph embedding with local semantic enhancement** *Expert Systems with Applications* [[paper](https://doi.org/10.1016/j.eswa.2025.129857)]
- [2025] **Enhancing Pre-trained Language Models for Vulnerability Detection via Semantic-Preserving Data Augmentation** *Lecture notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering* [[paper](https://doi.org/10.1007/978-3-031-94458-1_9)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Software Supply-Chain Security of Containerized IoT Components for Sustainable Energy Systems: A Comparative Vulnerability Assessment Using Trivy and Grype** *Energies* [[paper](https://doi.org/10.3390/en19163859)]
- [2026] **Artifacts to Actors: Assessing the Maturity of Software Supply Chain Security Measurement Practices - Replication Package** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.21479459)]
- [2026] **Package Hallucinations as Phantoms in Open-source Software Supply Chains: An Empirical Security Analysis** *ACM Transactions on Software Engineering and Methodology* [[paper](https://doi.org/10.1145/3830237)]
- [2026] **Software Supply Chain Security: Can We Beat the Kill-Chain? A Case Study on the XZ Backdoor** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-3-032-14782-0_12)]

##### 2025

- [2025] **Securing the Software Supply Chain with Software Bill of Materials (SBOMs): An Empirical Evaluation of Open-Source Tools in Enterprise IT Environments** *Programming and Computer Software* [[paper](https://doi.org/10.1134/s0361768825700598)]
- [2025] **Systematic Review of Identity-Centric Security in Cloud-Native CI/CD Pipelines** [[paper](https://doi.org/10.1145/3785520.3785525)]
- [2025] **Prompting Instability: An Empirical Study of LLM Robustness in Code Vulnerability Detection** *Lecture notes in computer science* [[paper](https://doi.org/10.1007/978-981-95-4969-6_18)]
- [2025] **Vulnerability Detection in Large Language Models: Addressing Security Concerns** *Journal of Cybersecurity and Privacy* [[paper](https://doi.org/10.3390/jcp5030071)]
- [2025] **AI-Powered Vulnerability Detection and Adaptive Defense Strategies in Cybersecurity** *Sakarya University Journal of Computer and Information Sciences* [[paper](https://doi.org/10.35377/saucis.8.94717.1711704)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **SoK: A Defense-Oriented Evaluation of Software Supply Chain Security** [[paper](https://doi.org/10.1109/eurosp68448.2026.00059)]
- [2026] **An Overview of Cyber Security Funding for Open Source Software** [[paper](https://arxiv.org/abs/2412.05887)]
- [2026] **LLA: Enhancing Security and Privacy for Generative Models with Logic-Locked Accelerators** *Proceedings of the AAAI Conference on Artificial Intelligence* [[paper](https://doi.org/10.1609/aaai.v40i28.39496)]

##### 2025

- [2025] **SBOM Toolkit: Software Bill of Materials Dataset for GNN-based Vulnerability Prediction** *Harvard Dataverse* [[paper](https://doi.org/10.7910/dvn/a6czrb)]
- [2025] **Network security vulnerability detection and repair model based on deep neural networks** *Discover Artificial Intelligence* [[paper](https://doi.org/10.1007/s44163-025-00666-2)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **DCI: Dependency Confidence Index for Assessing Open-Source Dependency Trustworthiness** [[paper](https://arxiv.org/abs/2608.16430)]
- [2026] **From Adoption to Deployment: A Qualitative Study on AI Integration in Software Development Practice** [[paper](https://arxiv.org/abs/2607.16660)]
- [2026] **The Distributed Open-Source Vulnerability Ecosystem** [[paper](https://arxiv.org/abs/2607.14900)]
- [2026] **Emerging Challenges in Threat Modeling for GenAI-Augmented Systems: A View from the Trenches** [[paper](https://arxiv.org/abs/2607.28431)]
- [2026] **LLM-Enhanced Hierarchical Heterogeneous Graph Representation Learning for Malicious Python Package Detection** [[paper](https://arxiv.org/abs/2607.03350)]
- [2026] **Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware** [[paper](https://arxiv.org/abs/2607.02357)]
- [2026] **Poking Around in the Dark: Why a Shared Understanding of Components Matters** [[paper](https://arxiv.org/abs/2606.02442)]
- [2026] **FuseChain: Runtime Evidence Reconstruction for Software Supply-Chain Attacks** [[paper](https://arxiv.org/abs/2606.15811)]
- [2026] **What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security** [[paper](https://arxiv.org/abs/2606.22827)]
- [2026] **Defending the Core: A Centrality-Based Protection Strategy for Supply Chain Security in npm Dependency Network** [[paper](https://arxiv.org/abs/2606.14036)] [[code](https://github.com/5tarWhee1/Centrality-Based-Protection-Strategy-for-Supply-Chain-Security-in-npm-Dependency-Network)]
- [2026] **A Longitudinal Study of Android Apps Signing Key Protection** [[paper](https://arxiv.org/abs/2606.21487)]
- [2026] **VeriPort: Automated and Verified Patch Backporting at Scale** [[paper](https://arxiv.org/abs/2606.22704)]
- [2026] **PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow** [[paper](https://arxiv.org/abs/2606.19063)]
- [2026] **PyFEX: Uncovering Evasive Python-based Threats via Resilient and Exhaustive Path Exploration** [[paper](https://arxiv.org/abs/2606.02196)]
- [2026] **Software Dark Matter: Gazing at Uncharted Files to Navigate SBOM Integrations** [[paper](https://arxiv.org/abs/2606.13966)]
- [2026] **S3C2 Summit 2025-07: Government Secure Supply Chain Summit** [[paper](https://arxiv.org/abs/2605.29140)]
- [2026] **S3C2 Summit 2025-09: Industry Secure Supply Chain Summit** [[paper](https://arxiv.org/abs/2605.29226)]
- [2026] **Trust Me, Import This: Dependency Steering Attacks via Malicious Agent Skills** [[paper](https://arxiv.org/abs/2605.09594)]
- [2026] **Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills** [[paper](https://arxiv.org/abs/2605.29354)]
- [2026] **Towards a Zero-Trust Supply-Chain Assurance Rubric for ORAN RIC Applications** [[paper](https://arxiv.org/abs/2605.04249)]
- [2026] **An Evidence-driven Protocol for Trustworthy CI Pipelines** [[paper](https://arxiv.org/abs/2605.21089)]
- [2026] **FuzzAgent: Multi-Agent System for Evolutionary Library Fuzzing** [[paper](https://arxiv.org/abs/2605.14431)]
- [2026] **Generating Proof-of-Vulnerability Tests to Help Enhance the Security of Complex Software** [[paper](https://arxiv.org/abs/2605.03956)]
- [2026] **Organizational Security Resource Estimation via Vulnerability Queueing** [[paper](https://arxiv.org/abs/2604.10250)]
- [2026] **MCP Pitfall Lab: Exposing Developer Pitfalls in MCP Tool Server Security under Multi-Vector Attacks** [[paper](https://arxiv.org/abs/2604.21477)]
- [2026] **A Queueing-Theoretic Framework for Dynamic Attack Surfaces: Data-Integrated Risk Analysis and Adaptive Defense** [[paper](https://arxiv.org/abs/2604.10427)]
- [2026] **Analysis of Commit Signing on Github** [[paper](https://arxiv.org/abs/2604.14014)]
- [2026] **Security and Resilience in Autonomous Vehicles: A Proactive Design Approach** [[paper](https://arxiv.org/abs/2604.12408)]
- [2026] **Towards Predicting Multi-Vulnerability Attack Chains in Software Supply Chains from Software Bill of Materials Graphs** [[paper](https://arxiv.org/abs/2604.04977)]
- [2026] **eDySec: A Deep Learning-based Explainable Dynamic Analysis Framework for Detecting Malicious Packages in PyPI Ecosystem** [[paper](https://arxiv.org/abs/2604.26219)]
- [2026] **Obfuscating Code Vulnerabilities against Static Analysis in JavaScript Code** [[paper](https://arxiv.org/abs/2604.01131)]
- [2026] **Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning** [[paper](https://arxiv.org/abs/2604.20179)]
- [2026] **Software Supply Chain Smells: Lightweight Analysis for Secure Dependency Management** [[paper](https://arxiv.org/abs/2603.24282)]
- [2026] **Operationalising Artificial Intelligence Bills of Materials (AIBOMs) for Verifiable AI Provenance and Lifecycle Assurance** [[paper](https://arxiv.org/abs/2605.19755)]
- [2026] **SynthChain: A Synthetic Benchmark and Forensic Analysis of Advanced and Stealthy Software Supply Chain Attacks** [[paper](https://arxiv.org/abs/2603.16694)]
- [2026] **SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation** [[paper](https://arxiv.org/abs/2603.10057)]
- [2026] **Mining the YARA Ecosystem: From Ad-Hoc Sharing to Data-Driven Threat Intelligence** [[paper](https://arxiv.org/abs/2603.14191)]
- [2026] **Assessing the Cross-Version Applicability of Java Library Vulnerability Exploits** [[paper](https://arxiv.org/abs/2603.25997)]
- [2026] **Trustworthy AI LLM Scalability Risk Index (LSRI): A Cybersecurity Framework Assessing Agentic-AI Security & Software Model Supply Chain Safety Boosting AI-Generated Malware Defense & Explainability Mitigating Emerging Risks of Generative AI** [[paper](https://arxiv.org/abs/2602.19021)]
- [2026] **VeriSBOM: Secure and Verifiable SBOM Sharing Via Zero-Knowledge Proofs** [[paper](https://arxiv.org/abs/2602.13682)]
- [2026] **Operationalizing Research Software for Supply Chain Security** [[paper](https://arxiv.org/abs/2601.20980)]
- [2026] **Unpacking Security Scanners for GitHub Actions Workflows** [[paper](https://arxiv.org/abs/2601.14455)]
- [2026] **Supply Chain Insecurity: Exposing Vulnerabilities in iOS Dependency Management Systems** [[paper](https://arxiv.org/abs/2601.20638)]
- [2026] **Deep Dive into the Abuse of DL APIs To Create Malicious AI Models and How to Detect Them** [[paper](https://arxiv.org/abs/2601.04553)]
- [2026] **AgentGuard: A Multi-Agent Framework for Robust Package Confusion Detection via Hybrid Search and Metadata-Content Fusion** [[paper](https://arxiv.org/abs/2604.16309)]
- [2026] **CHASE: LLM Agents for Dissecting Malicious PyPI Packages** [[paper](https://arxiv.org/abs/2601.06838)] [[project](https://t0d4.github.io/CHASE-AIware25/)]
- [2026] **Security risk assessment of android automotive OS software supply chain using firmware reverse engineering.** *Comput. Secur.* [[paper](https://dblp.org/rec/journals/compsec/YuKDWSF26)]
- [2026] **How Can ChatGPT Support Human Security Testers to Help Mitigate Supply Chain Attacks?** *IEEE Trans. Software Eng.* [[paper](https://dblp.org/rec/journals/tse/ZhangSJYM26)]
- [2026] **SoK: A Defense-Oriented Evaluation of Software Supply Chain Security.** *EuroS&amp;P* [[paper](https://dblp.org/rec/conf/eurosp/IshgairGMCT26)]
- [2026] **Operationalizing Research Software for Supply Chain Security.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2601-20980)]
- [2026] **Cyberattacks in supply chains: A multi-case study.** *MED* [[paper](https://doi.org/10.1371/journal.pone.0350010)]
- [2026] **Toward Cybersecurity Testing and Monitoring of IoT Ecosystems.** *MED* [[paper](https://doi.org/10.1007/s42979-026-05048-8)]
- [2026] **Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework.** *MED* [[paper](https://doi.org/10.3389/frai.2026.1826384)]
- [2026] **Understanding security challenges in the software supply chain through causal relationships.** *MED* [[paper](https://doi.org/10.1371/journal.pone.0344098)]
- [2026] **Cybersecurity in connected medical devices: a policy agenda for the NHS.** *MED* [[paper](https://doi.org/10.1038/s41746-026-02534-4)]
- [2026] **A generative AI-driven cybersecurity framework for small and medium enterprises software development: an ANN-ISM approach.** *MED* [[paper](https://doi.org/10.1038/s41598-026-37614-8)]
- [2026] **Security evaluation framework for cloud ERP systems using NIST and ISO standards.** *MED* [[paper](https://doi.org/10.1038/s41598-026-45550-w)]
- [2026] **Evolution and Vulnerability of the Global Ready-to-Eat Aquatic Products Trade Network: A Complex Network Analysis.** *MED* [[paper](https://doi.org/10.3390/foods15101648)]
- [2026] **Enhancing Digital Supply Chain Security Through Critical Infrastructure Protection Blueprints: A Review on Challenges, Reference Architectures and Software Bills of Material** *Signals and communication technology* [[paper](https://doi.org/10.1007/978-3-032-11119-7_2)]

##### 2025

- [2025] **S3C2 SICP Summit 2025-06: Vulnerability Response Summit** [[paper](https://arxiv.org/abs/2512.02600)]
- [2025] **Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation** [[paper](https://arxiv.org/abs/2512.23480)]
- [2025] **Unveiling Malicious Logic: Towards a Statement-Level Taxonomy and Dataset for Securing Python Packages** [[paper](https://arxiv.org/abs/2512.12559)]
- [2025] **CoTDeceptor:Adversarial Code Obfuscation Against CoT-Enhanced LLM Code Agents** [[paper](https://arxiv.org/abs/2512.21250)]
- [2025] **Taint-Based Code Slicing for LLMs-based Malicious NPM Package Detection** [[paper](https://arxiv.org/abs/2512.12313)]
- [2025] **Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?** [[paper](https://arxiv.org/abs/2512.23385)]
- [2025] **Granite: Granular Runtime Enforcement for GitHub Actions Permissions** [[paper](https://arxiv.org/abs/2512.11602)]
- [2025] **A Comprehensive Study on the Impact of Vulnerable Dependencies on Open-Source Software** [[paper](https://arxiv.org/abs/2512.03868)]
- [2025] **Software Supply Chain Security of Web3** [[paper](https://arxiv.org/abs/2511.12274)]
- [2025] **A Reality Check on SBOM-based Vulnerability Management: An Empirical Study and A Path Forward** [[paper](https://arxiv.org/abs/2511.20313)]
- [2025] **Finding Software Supply Chain Attack Paths with Logical Attack Graphs** [[paper](https://arxiv.org/abs/2511.11171)]
- [2025] **AI Bill of Materials and Beyond: Systematizing Security Assurance through the AI Risk Scanning (AIRS) Framework** [[paper](https://arxiv.org/abs/2511.12668)]
- [2025] **Tokenized Peer Review: An Adaptive Blockchain Mechanism for Open Source Supply Chains** *Journal of Network and Systems Management* [[paper](https://doi.org/10.1007/s10922-025-10004-7)]
- [2025] **S3C2 Summit 2025-03: Industry Secure Supply Chain Summit** [[paper](https://arxiv.org/abs/2510.24920)]
- [2025] **Classport: Designing Runtime Dependency Introspection for Java** [[paper](https://arxiv.org/abs/2510.20340)]
- [2025] **Towards Socio-Technical Topology-Aware Adaptive Threat Detection in Software Supply Chains** [[paper](https://arxiv.org/abs/2510.21452)]
- [2025] **Maven-Lockfile: High Integrity Rebuild of Past Java Releases** [[paper](https://arxiv.org/abs/2510.00730)]
- [2025] **TAIBOM: Bringing Trustworthiness to AI-Enabled Systems** [[paper](https://arxiv.org/abs/2510.02169)]
- [2025] **Lexo: Eliminating Stealthy Supply-Chain Attacks via LLM-Assisted Program Regeneration** [[paper](https://arxiv.org/abs/2510.14522)]
- [2025] **Which Is Better For Reducing Outdated and Vulnerable Dependencies: Pinning or Floating?** [[paper](https://arxiv.org/abs/2510.08609)]
- [2025] **Establishing a Baseline of Software Supply Chain Security Task Adoption by Software Organizations** [[paper](https://arxiv.org/abs/2509.08083)]
- [2025] **Investigating Security Implications of Automatically Generated Code on the Software Supply Chain** [[paper](https://arxiv.org/abs/2509.20277)]
- [2025] **Binary Diff Summarization using Large Language Models** [[paper](https://arxiv.org/abs/2509.23970)]
- [2025] **Security Vulnerabilities in Software Supply Chain for Autonomous Vehicles** [[paper](https://arxiv.org/abs/2509.16899)]
- [2025] **Trustworthy and Confidential SBOM Exchange** [[paper](https://arxiv.org/abs/2509.13217)]
- [2025] **Unlocking Reproducibility: Automating re-Build Process for Open-Source Software** [[paper](https://arxiv.org/abs/2509.08204)]
- [2025] **Assessing the Security of Software Supply Chains: Software Bill of Materials, Threat Propagation, and Logical Attack Graphs. (Évaluation de la sécurité des chaînes d&apos;approvisionnement logicielles: Software Bill of Materials (SBOM), propagation des menaces et graphes d&apos;attaque logiques).** [[paper](https://dblp.org/rec/phd/hal/Soeiro25)]
- [2025] **Fifty Years of Open Source Software Supply Chain Security: For decades, software reuse was only a lofty goal. Now it&apos;s very real.** *ACM Queue* [[paper](https://dblp.org/rec/journals/queue/Cox25)]
- [2025] **Software Supply Chain Security: Can We Beat the Kill-Chain? A Case Study on the XZ Backdoor.** *NordSec* [[paper](https://dblp.org/rec/conf/nordsec/LinsRM25)]
- [2025] **Establishing a Baseline of Software Supply Chain Security Task Adoption by Software Organizations.** *SCORED* [[paper](https://dblp.org/rec/conf/scored/WilliamsM25)]
- [2025] **An Industry Interview Study of Software Signing for Supply Chain Security.** *USENIX Security Symposium* [[paper](https://dblp.org/rec/conf/uss/KaluSOT025)]
- [2025] **Evaluating Software Supply Chain Security in Research Software.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2508-03856)]
- [2025] **Software Bill of Materials in Software Supply Chain Security A Systematic Literature Review.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2506-03507)]
- [2025] **Fifty Years of Open Source Software Supply-Chain Security.** *Commun. ACM* [[paper](https://dblp.org/rec/journals/cacm/Cox25)]
- [2025] **Malicious AI Models Undermine Software Supply-Chain Security.** *Commun. ACM* [[paper](https://dblp.org/rec/journals/cacm/SoodZ25)]
- [2025] **Using FIDO-based Authentication to Improve the Security of Software Supply Chains.** *J. Inf. Process.* [[paper](https://dblp.org/rec/journals/jip/LukeMKKT25)]
- [2025] **Dependency Network Structure and Security Vulnerabilities in Software Supply Chains.** *J. Manag. Inf. Syst.* [[paper](https://dblp.org/rec/journals/jmis/YooCS25)]
- [2025] **Research Directions in Software Supply Chain Security.** *ACM Trans. Softw. Eng. Methodol.* [[paper](https://dblp.org/rec/journals/tosem/WilliamsBHPRTTZMACKKWE25)]
- [2025] **Software Supply Chain and DevOps Security Practices** [[paper](https://doi.org/10.6028/nist.sp.1800-44)]
- [2025] **Research on network security vulnerability risk contagion in software supply chain based on system dynamics.** *MED* [[paper](https://doi.org/10.1371/journal.pone.0335128)]

##### 2024

- [2024] **Software Supply Chain Security: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2401.00001)]
- [2024] **Enhancing Software Supply Chain Resilience: Strategy For Mitigating Software Supply Chain Security Risks And Ensuring Security Continuity In Development Lifecycle.** *CoRR* [[paper](https://dblp.org/rec/journals/corr/abs-2407-13785)]
- [2024] **On the security risks of open source consumption: vulnerabilities and supply-chain attacks in the era of open-source-based software development. (Risques de sécurité liés à la consommation de logiciels libres: vulnérabilités et attaques de la chaîne d&apos;approvisionnement à l&apos;ère du développement de logiciels basés sur l&apos;Open Source).** [[paper](https://dblp.org/rec/phd/hal/Plate24)]
- [2024] **Assessing Security Risks of Software Supply Chains Using Software Bill of Materials.** *SANER* [[paper](https://dblp.org/rec/conf/wcre/ODonoghueRI24)]
- [2024] **Case Studies in Software Supply Chain Security** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_8)]
- [2024] **Emerging Trends in Software Supply Chain Security** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_10)]
- [2024] **Implementing Comprehensive Security in Your Software Supply Chain** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_9)]
- [2024] **DevSecOps Integration in Supply Chain Security** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_5)]
- [2024] **Key Technologies in Supply Chain Security** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_2)]
- [2024] **The Evolution of Supply Chain Threats** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_1)]
- [2024] **The Anatomy of Supply Chain Applications** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_3)]
- [2024] **Supply Chain Software Security** [[paper](https://doi.org/10.1007/979-8-8688-0799-2)]
- [2024] **Securing IoT-Driven Supply Chains** *Supply Chain Software Security* [[paper](https://doi.org/10.1007/979-8-8688-0799-2_7)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **A Machine Learning-Based Vulnerability Prediction System Using SBOM Metadata for Software Supply Chain Security** *한국통신학회논문지* [[paper](https://doi.org/10.7840/kics.2026.51.4.792)]
- [2026] **Supply Chain Security of Critical Infrastructure Protection Software Blueprints: Deployment Aspects** *Signals and communication technology* [[paper](https://doi.org/10.1007/978-3-032-11119-7_3)]

##### 2025

- [2025] **Expert-in-the-Loop Systems with Cross-Domain and in-Domain Few-Shot Learning for Software Vulnerability Detection** [[paper](https://doi.org/10.1109/wsc68292.2025.11338966)]
- [2025] **Fedvuln: Scalable and privacy-preserving federated graph learning for smart contract vulnerability detection on parallel systems** *Future Generation Computer Systems* [[paper](https://doi.org/10.1016/j.future.2025.108264)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits** [[paper](https://arxiv.org/abs/2608.09740)]
- [2026] **Understanding and Improving Model Editing for Secure Code Generation** [[paper](https://arxiv.org/abs/2608.06848)]
- [2026] **CoGate: Confidence-Gated Co-Decoding for Secure Code Generation** [[paper](https://arxiv.org/abs/2607.28529)]
- [2026] **Secure Coding Drift in LLM-Assisted Post-Quantum Cryptography Development: A Gamified Fix** [[paper](https://arxiv.org/abs/2606.19474)]
- [2026] **Beyond AI Delegation: A Prompt Pattern Framework for Productive Struggle and Evaluative Judgement in Secure Coding Education** [[paper](https://arxiv.org/abs/2605.24447)]
- [2026] **Usability as a Weapon: Attacking the Safety of LLM-Based Code Generation via Usability Requirements** [[paper](https://arxiv.org/abs/2605.10133)]
- [2026] **R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge** [[paper](https://arxiv.org/abs/2605.31135)]
- [2026] **TRACESEC: Trace-Aware Neuro-Symbolic Vulnerability Reasoning for Software Supply-Chain Security** [[paper](https://doi.org/10.1109/mcna69896.2026.11574373)]
- [2026] **Transfer learning strategies for vulnerability detection in software binaries** *Neural Networks* [[paper](https://doi.org/10.1016/j.neunet.2026.109069)]
- [2026] **Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation** [[paper](https://arxiv.org/abs/2602.01187)]
- [2026] **Learning to Generate Secure Code via Token-Level Rewards** [[paper](https://arxiv.org/abs/2602.23407)]
- [2026] **LLMs + Security = Trouble** [[paper](https://arxiv.org/abs/2602.08422)]
- [2026] **SecCodeBench-V2 Technical Report** [[paper](https://arxiv.org/abs/2602.15485)] [[code](https://github.com/alibaba/sec-code-bench)] [[project](https://alibaba.github.io/sec-code-bench)]
- [2026] **How Secure is Secure Code Generation? Adversarial Prompts Put LLM Defenses to the Test** [[paper](https://arxiv.org/abs/2601.07084)]
- [2026] **RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories** [[paper](https://arxiv.org/abs/2601.22706)]

##### 2025

- [2025] **CVE Breadcrumbs: Tracking Vulnerabilities Through Versioned Apache Libraries** [[paper](https://arxiv.org/abs/2512.02259)]
- [2025] **Reflection-Driven Control for Trustworthy Code Agents** [[paper](https://arxiv.org/abs/2512.21354)]
- [2025] **Assessing the Security of Software Supply Chains : Software Bill of Materials, Threat Propagation, and Logical Attack Graphs** [[paper](https://doi.org/10.70675/6dd72cb7z7135z4d1dza942z3f6c57308033)]
- [2025] **Data and Context Matter: Towards Generalizing AI-based Software Vulnerability Detection** *Research Square* [[paper](https://doi.org/10.21203/rs.3.rs-7821055/v1)]
- [2025] **Secure Code Generation at Scale with Reflexion** [[paper](https://arxiv.org/abs/2511.03898)]
- [2025] **Secure-Instruct: An Automated Pipeline for Synthesizing Instruction-Tuning Datasets Using LLMs for Secure Code Generation** [[paper](https://arxiv.org/abs/2510.07189)]
- [2025] **RESCUE: Retrieval Augmented Secure Code Generation** [[paper](https://arxiv.org/abs/2510.18204)] [[code](https://github.com/steven1518/RESCUE)]
- [2025] **Fortifying LLM-Based Code Generation with Graph-Based Reasoning on Secure Coding Practices** [[paper](https://arxiv.org/abs/2510.09682)]
- [2025] **RefleXGen:The unexamined code is not worth using** [[paper](https://arxiv.org/abs/2510.23674)]
- [2025] **Dependency Network Structure and Security Vulnerabilities in Software Supply Chains** *Journal of Management Information Systems* [[paper](https://doi.org/10.1080/07421222.2025.2561385)]
- [2025] **SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios** [[paper](https://arxiv.org/abs/2509.22097)] [[code](https://github.com/iCSawyer/SecureVibeBench)]
- [2025] **Fifty Years of Open Source Software Supply-Chain Security** *Communications of the ACM* [[paper](https://doi.org/10.1145/3762635)]
- [2025] **How far have we been on the path of LLM-enhanced vulnerability detection** [[paper](https://doi.org/10.1145/3776759.3776861)]

[⬆ Back to top](#paper-list)

### Open Source

#### Method

##### 2026

- [2026] **ARVO: Atlas of Reproducible Vulnerabilities for Open-Source Software** [[paper](https://arxiv.org/abs/2408.02153)]
- [2026] **Behavioral analysis of contributors in China's open-source software ecosystem** *Scientia Sinica Informationis* [[paper](https://doi.org/10.1360/ssi-2025-0329)]
- [2026] **Predictive-SHM: An open-source, extensible software toolkit for multi-sensor structural health monitoring and time-series prediction** *SoftwareX* [[paper](https://doi.org/10.1016/j.softx.2026.102732)]
- [2026] **py4dgeo: Open-source scientific software for topographic change analysis in 3D/4D geographic point clouds** *SoftwareX* [[paper](https://doi.org/10.1016/j.softx.2026.102670)]
- [2026] **The Open Molecular Software Foundation (OMSF) and the Growing Role of Open Source Software in Molecular Modeling** *Journal of Chemical Information and Modeling* [[paper](https://doi.org/10.1021/acs.jcim.5c03137)]
- [2026] **Knowledge sharing intention in open source software communities: A configurational perspective** *Journal of Innovation & Knowledge* [[paper](https://doi.org/10.1016/j.jik.2026.100942)]
- [2026] **ConversationAlign: Open-source software for analyzing patterns of lexical use and alignment in conversation transcripts** *Behavior Research Methods* [[paper](https://doi.org/10.3758/s13428-026-02954-w)]
- [2026] **Open-source tools for processing opportunistic rainfall sensor data: An overview of existing tools and the new OpenSense software packages poligrain, pypwsqc and mergeplg** [[paper](https://doi.org/10.5194/egusphere-2025-5438)]
- [2026] **SOMAS – an open-source software for the analysis of muscle activity during sleep** *Sleep Medicine* [[paper](https://doi.org/10.1016/j.sleep.2026.108791)]
- [2026] **Workflow Automation in Open-Source Software Development: Accelerating Innovation Through Mechanization and Orchestration** *Information Systems Research* [[paper](https://doi.org/10.1287/isre.2024.1551)]
- [2026] **Security measures for digital archives curated through open-source software in South Africa** *South African Journal of Libraries and Information Science* [[paper](https://doi.org/10.7553/92-2-2528)]
- [2026] **The statistical software revolution in pharmaceutical development: challenges and opportunities in open source** *Drug Discovery Today* [[paper](https://arxiv.org/abs/2301.11791)]
- [2026] **Using open-source software and interdisciplinary teaching to increase digital forensics accessibility, and inclusivity, with sustainable development and learning in higher education** *Science & Justice* [[paper](https://doi.org/10.1016/j.scijus.2026.101398)]
- [2026] **GKit-SSRDecoder: An Open-Source C/C++-Based PPP-B2b and HAS Decoding and Formatted Product Generation Software** *IEEE Access* [[paper](https://doi.org/10.1109/access.2026.3689972)]

##### 2025

- [2025] **Inter-organizational collaborations in open-source software ecosystems** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112765)]
- [2025] **In Vivo Accuracy Assessment of Two Intraoral Scanners Using Open-Source Software: A Comparative Full-Arch Pilot Study** *Oral* [[paper](https://doi.org/10.3390/oral5040097)]
- [2025] **Using Open-Source Software to Help Spanish Speakers With Aphasia Learn Everyday Sentences: A Single-Case Experimental Design** *American Journal of Speech-Language Pathology* [[paper](https://doi.org/10.1044/2025_ajslp-24-00550)]
- [2025] **MAPS: Open-source GNSS multipath analysis and processing software** *Measurement Science and Technology* [[paper](https://doi.org/10.1088/1361-6501/ae2945)]
- [2025] **The AI Attribution Paradox: Transparency as Social Strategy in Open-Source Software Development** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2512.00867)]
- [2025] **A comparative analysis of industrial involvement and licensing in the open source software ecosystems of four IoT standards** *Journal of Systems and Software* [[paper](https://doi.org/10.1016/j.jss.2025.112708)]
- [2025] **Data and Software for paper: Eye-tracking with accessible technology and open-source software: a validity study using commercial eye-trackers** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.17517309)]
- [2025] **Invisible Labor in Open Source Software Ecosystems** *Proceedings of the ACM on Human-Computer Interaction* [[paper](https://doi.org/10.1145/3757417)]
- [2025] **Applying Low Budget Equipment and Open Source Software for High Resolution Documentation of Archaeological Stratigraphy and Features** [[paper](https://doi.org/10.5117/9789089647153-12)]
- [2025] **How relevant are personas in open-source software development?** *Frontiers in Computer Science* [[paper](https://doi.org/10.3389/fcomp.2025.1457563)]
- [2025] **VasoTracker 2: Open‐source software and hardware for tracking blood vessel diameter and assessing vascular function** *The Journal of Physiology* [[paper](https://doi.org/10.1113/jp289322)]
- [2025] **Lethe 1.0: An open-source parallel high-order computational fluid dynamics software framework for single and multiphase flows** *Computer Physics Communications* [[paper](https://doi.org/10.1016/j.cpc.2025.109880)]
- [2025] **Balancing accessibility and security: Safeguarding citizen-sourced biodiversity data in the age of AI and open-sourced software** *Ecological Informatics* [[paper](https://doi.org/10.1016/j.ecoinf.2025.103443)]
- [2025] **Compressai-Vision: Open-Source Software To Evaluate Compression Methods For Computer Vision Tasks** [[paper](https://doi.org/10.1109/icipw68931.2025.11386316)]
- [2025] **A novel approach to olive oil sensory profiling: Predicting key attributes using near-infrared spectroscopy and open-source software** *Food Control* [[paper](https://doi.org/10.1016/j.foodcont.2025.111726)]
- [2025] **OpenDose3D: A Free, Open-Source Clinical Dosimetry Software for Patient-Specific Dosimetry** *Journal of Nuclear Medicine* [[paper](https://doi.org/10.2967/jnumed.125.269539)]
- [2025] **An Empirical Study of Software Refactorings in Real-World Open-Source Java Projects** *IEEE Transactions on Software Engineering* [[paper](https://doi.org/10.1109/tse.2025.3604821)]
- [2025] **FQSHA: An open-source Python software for fault-based seismic hazard assessment** *SoftwareX* [[paper](https://doi.org/10.1016/j.softx.2025.102339)]
- [2025] **Special Sessions - Hardware-Software Co-Design for Machine Learning Systems Made Open-Source** [[paper](https://doi.org/10.1145/3742873.3756928)]
- [2025] **Open-Source Software** [[paper](https://doi.org/10.1201/9781003400929-6)]

[⬆ Back to top](#paper-list)

#### Theory

##### 2026

- [2026] **A deep-learning based approach to detect and classify animals flying near wind turbines using thermal surveillance cameras and open-source software** *Ecological Informatics* [[paper](https://doi.org/10.1016/j.ecoinf.2026.103909)]
- [2026] **Decentralised Manufacturing as a Networked Cyber–Physical System: Formalising Free and Open-Source Software Governance and ML Adaptation for Distributed Robustness** *Systems* [[paper](https://doi.org/10.3390/systems14050469)]
- [2026] **<b>OPEN SOURCE VS. PROPRIETARY SOFTWARE</b>** *Journal International Review of Research Studies* [[paper](https://doi.org/10.66104/hnyd5f72)]
- [2026] **An Open‐Source Software Toolbox for Rapid Radiofrequency Coil Design and Evaluation in <scp>MRI</scp>** *Magnetic Resonance in Medicine* [[paper](https://doi.org/10.1002/mrm.70269)]

##### 2025

- [2025] **THE ROLE OF TRANSFORMATIONAL LEADERSHIP IN OPEN-SOURCE SOFTWARE DEVELOPMENT: INSIGHTS FROM SURVEY DATA ON ENHANCING ORGANIZATIONAL COMMITMENT AND INNOVATION IN AI-DRIVEN BUSINESS ENVIRONMENTS** *SCIENCE International Journal* [[paper](https://doi.org/10.35120/sciencej0404107a)]
- [2025] **Study on the accuracy of Multi-GNSS PPP for different observing sessions time spans using PRIDE PPP-AR open-source software package** *Applied Geomatics* [[paper](https://doi.org/10.1007/s12518-025-00675-x)]
- [2025] **Are External Contributions Important to Project Productivity in Open Source Software? A Deep Insight based on Issue Entropy** *Proceedings of the ACM on Human-Computer Interaction* [[paper](https://doi.org/10.1145/3757399)]
- [2025] **Coding finance: impact of open-source financial software on stochastic modeling skills among business students** *Interactive Learning Environments* [[paper](https://doi.org/10.1080/10494820.2025.2570488)]
- [2025] **Increasing developers’ code accountability perceptions in open source software development** *International Journal of Information Management* [[paper](https://doi.org/10.1016/j.ijinfomgt.2025.102974)]
- [2025] **Modeling and Assessing Software Reliability in Open-Source Projects** *Computation* [[paper](https://doi.org/10.3390/computation13090214)]
- [2025] **Certification of Open Source Software Compliance: Insights From a Conjoint Experiment** *Information Systems Journal* [[paper](https://doi.org/10.1111/isj.70014)]

[⬆ Back to top](#paper-list)

#### Application

##### 2026

- [2026] **Multiple Embedded Case Study for the Study_Industrial Practices for Evaluating Quality of Open Source Software A Practitioner Survey** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18914464)]
- [2026] **The Definition and Contributions of the OSS Quality Meta-model for the Study_Industrial Practices for Evaluating Quality of Open Source Software A Practitioner Survey** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18914623)]
- [2026] **Can a Free Open-Source Software Platform Serve as Minimal Ablation Confirmation Assessment Software in Real-Life Practice?** *CardioVascular and Interventional Radiology* [[paper](https://doi.org/10.1007/s00270-026-04372-z)]
- [2026] **Open-source computer vision software for advanced visualisation and quantification of melt electrowriting jets** *Virtual and Physical Prototyping* [[paper](https://doi.org/10.1080/17452759.2025.2611474)]

##### 2025

- [2025] **CloneCoordinate: Open-Source Software for Collaborative DNA Construction** *ACS Synthetic Biology* [[paper](https://doi.org/10.1021/acssynbio.5c00582)]
- [2025] **Tutorial: Open Source Software for Research - Sharing Code the Right Way** *Zenodo (CERN European Organization for Nuclear Research)* [[paper](https://doi.org/10.5281/zenodo.18743551)]
- [2025] **ESP32-Powered PPG Signal Acquisition: Open-Source Hardware and Software for Research and Education** *Hardware* [[paper](https://doi.org/10.3390/hardware3040015)]
- [2025] **Comparing Open Source with Software Code Generated by AI Tools from Software Maintainability Quality Factor Perspective** *WSEAS TRANSACTIONS ON COMPUTER RESEARCH* [[paper](https://doi.org/10.37394/232018.2025.13.58)]
- [2025] **Open-source hardware and software platform for vibrotactile motion guidance** *Device* [[paper](https://doi.org/10.1016/j.device.2025.100966)]
- [2025] **The Uncertainty Challenge: To Centralize or Decentralize Requirements Engineering Decision-Making in Open Source Software Development?** *ACM Transactions on Management Information Systems* [[paper](https://doi.org/10.1145/3766893)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **labmc: An open-source Markov chain Monte Carlo inversion software for the analysis of experimental rock deformation data (v1.0.2) [Software and Datasets]** *Open MIND* [[paper](https://github.com/chhavijain2026/labmc_software/tree/v1.0.2)]
- [2026] **TRACE: Open-source software for quantifying somatic variation of tandem repeats by capillary electrophoresis** *Journal of Huntington s Disease* [[paper](https://doi.org/10.1177/18796397261448958)]
- [2026] **PHoNUPS: Open-Source Software for Standardized Analysis and Visualization of Multi-Instrument Extracellular Vesicle Measurements** *bioRxiv (Cold Spring Harbor Laboratory)* [[paper](https://doi.org/10.64898/2026.01.29.702479)]

##### 2025

- [2025] **Calculation of Shock Stand-Off Distance for a Sphere Using an Open-Source CFD Software Eilmer with New Chemical-Kinetic Parameters** *International Journal of Aeronautical and Space Sciences* [[paper](https://doi.org/10.1007/s42405-025-01077-4)]
- [2025] **Analog radio-over-fiber-based 5G smart mobile fronthaul networking testbed with an open-source software base-station system** *Journal of Optical Communications and Networking* [[paper](https://doi.org/10.1364/jocn.566706)]
- [2025] **Assessment of GNSS multipath effects using open source software** *Geodesy and Aerophotosurveying* [[paper](https://doi.org/10.30533/gia-2025-035)]
- [2025] **A Practical Open-Source Software Stack for a Cloud-Based Quantum Computing System** [[paper](https://arxiv.org/abs/2507.23165)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **Engineering Signals of Human-AI Collaboration in the Agentic Coding Era: A Longitudinal Analysis of 33,228 Pull Requests from vLLM and SGLang with Implications for Biomedical AI Agents and Bioinformatics Pipeline Developmen** [[paper](https://arxiv.org/abs/2608.13884)]
- [2026] **Expertise-Based Developer Assignment for Long-Term Software Components in Open-Source Projects** [[paper](https://arxiv.org/abs/2608.05919)]
- [2026] **Towards Competence-Based Management for Open Source Software Projects** [[paper](https://arxiv.org/abs/2608.05599)]
- [2026] **An Exploratory Study of Agent Plans for Agentic AI Coding Tools in Open-Source Software** [[paper](https://arxiv.org/abs/2608.04661)]
- [2026] **The Ground Is Shifting: A Reflection on the Foundations of Software Measurement** [[paper](https://arxiv.org/abs/2608.03007)]
- [2026] **How to Value Open Source Contributions? An Institutional Perspective from CERN** [[paper](https://arxiv.org/abs/2607.04202)]
- [2026] **SMOCS: A Streaming Framework for Simplified Deployment, Monitoring, and Optimization of ML Systems in Production** [[paper](https://arxiv.org/abs/2607.02731)]
- [2026] **Thinking More, Harnessing Better: State Machine Guided Harness Automatic Generation with Project Digestion and Workflow Decomposition** [[paper](https://arxiv.org/abs/2607.07007)]
- [2026] **"AI Slop is DDoSing Open Source": Understanding the Impact of AI-Generated Contributions on Open Source Sustainability** [[paper](https://arxiv.org/abs/2607.04003)]
- [2026] **From Collaboration to Regulation: Characterizing Governance Practice in Three Deep Learning Open Source Communities** [[paper](https://arxiv.org/abs/2607.19022)]
- [2026] **ProfMalPlus: Agent-Coordinated Detection of Malicious NPM Packages via Static-Dynamic Analysis Synergy** [[paper](https://arxiv.org/abs/2607.13965)]
- [2026] **What Motivates Whom? A Survey of Newcomers to OSS and Experienced OSS Practitioners** [[paper](https://arxiv.org/abs/2607.25126)]
- [2026] **Making Agent-Mediated Contributions Governable: A Project-Level Governance Manifest for Open-Source AI Collaboration** [[paper](https://arxiv.org/abs/2607.15769)]
- [2026] **Beyond the Grave: An Empirical Study of Dormancy and Revival in Scientific Open-Source Software** [[paper](https://arxiv.org/abs/2606.20966)]
- [2026] **Project Life Cycles in Open-Source Software** [[paper](https://arxiv.org/abs/2605.12738)]
- [2026] **Exploring Sustainability in Scientific Software through Code Quality & Test Coverage Metrics** [[paper](https://arxiv.org/abs/2605.03243)]
- [2026] **LLM Code Smells: A Taxonomy and Detection Approach** [[paper](https://arxiv.org/abs/2605.22976)]
- [2026] **Restructure This: Using AI to Restructure Onboarding Documents to Reduce Cognitive Overload** [[paper](https://arxiv.org/abs/2605.19174)]
- [2026] **Guidelines for Cultivating a Sense of Belonging to Reduce Developer Burnout** [[paper](https://arxiv.org/abs/2605.06827)]
- [2026] **ESBMC: A Survey of Its Evolution, Integration, and Future Directions in Formal Software Verification** [[paper](https://arxiv.org/abs/2605.26169)]
- [2026] **Modeling Dependency-Propagated Ecosystem Impact of Changes in Maintenance Activities: Evaluating Support Strategies in the PyPI Network** [[paper](https://arxiv.org/abs/2605.06164)]
- [2026] **ACT: Automated CPS Testing for Open-Source Robotic Platforms** [[paper](https://arxiv.org/abs/2604.11708)]
- [2026] **DEPTEX: Organization-First, Open Source Dependency Risk Monitoring** [[paper](https://arxiv.org/abs/2605.00179)]
- [2026] **Mapping GitHub Sponsorships: A Longitudinal Observatory for Open-Source Sustainability** [[paper](https://arxiv.org/abs/2604.03846)]
- [2026] **Putting a Face to the Issue: Fostering User Empathy of Open Source Software Developers With PersonaFlow** [[paper](https://arxiv.org/abs/2604.24478)]
- [2026] **LLM-Enabled Open-Source Systems in the Wild: An Empirical Study of Vulnerabilities in GitHub Security Advisories** [[paper](https://arxiv.org/abs/2604.04288)]
- [2026] **What If We Work Together? Fostering Reflections on Designer Inclusion in Open Source Software Through Speculative Design** [[paper](https://arxiv.org/abs/2604.24981)]
- [2026] **The Impact of Documentation on Test Engagement in Pull Requests in OSS** [[paper](https://arxiv.org/abs/2604.23048)]
- [2026] **From Threads to Trajectories: A Multi-LLM Pipeline for Community Knowledge Extraction from GitHub Issue Discussions** [[paper](https://arxiv.org/abs/2604.25880)]
- [2026] **From OSS to Open Source AI: an Exploratory Study of Collaborative Development Paradigm Divergence** [[paper](https://arxiv.org/abs/2604.08888)]
- [2026] **Social Proof is in the Pudding: The (Non)-Impact of Social Proof on Software Downloads** [[paper](https://arxiv.org/abs/2603.07919)]
- [2026] **Results of the analysis of a survey for young scientists on training quality in HEP instrumentation software and machine learning** [[paper](https://arxiv.org/abs/2603.16293)]
- [2026] **Linguistic Similarity Within Centralized FLOSS Development** [[paper](https://arxiv.org/abs/2603.12571)]
- [2026] **Compliance as Code: A Study of Linux Distributions and Beyond** [[paper](https://arxiv.org/abs/2603.01520)]
- [2026] **Governance in Practice: How Open Source Projects Define and Document Roles** [[paper](https://arxiv.org/abs/2603.24879)]
- [2026] **To Ban or not to Ban? How Open Source Projects Govern GenAI Contributions** [[paper](https://arxiv.org/abs/2603.26487)]
- [2026] **Accountability in Open Source Software Ecosystems: Workshop Report** [[paper](https://arxiv.org/abs/2602.04026)]
- [2026] **Beyond Code: Empirical Insights into How Team Dynamics Influence OSS Project Selection** [[paper](https://arxiv.org/abs/2602.11692)]
- [2026] **Addressing OSS Community Managers' Challenges in Contributor Retention** [[paper](https://arxiv.org/abs/2602.11447)]
- [2026] **Theory of Code Space: Do Code Agents Understand Software Architecture?** [[paper](https://arxiv.org/abs/2603.00601)] [[code](https://github.com/che-shr-cat/tocs)]
- [2026] **Quantifying Competitive Relationships Among Open-Source Software Projects** [[paper](https://arxiv.org/abs/2602.17131)]
- [2026] **Artificial Intelligence in Open Source Software Engineering: A Foundation for Sustainability** [[paper](https://arxiv.org/abs/2602.07071)]
- [2026] **"Write in English, Nobody Understands Your Language Here": A Study of Non-English Trends in Open-Source Repositories** [[paper](https://arxiv.org/abs/2602.19446)]
- [2026] **Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI** [[paper](https://arxiv.org/abs/2602.09064)]
- [2026] **Leveraging Language Models to Discover Evidence-Based Actions for OSS Sustainability** [[paper](https://arxiv.org/abs/2602.11746)]
- [2026] **An Empirical Analysis of Community and Coding Patterns in OSS4SG vs. Conventional OSS** [[paper](https://arxiv.org/abs/2601.03430)]
- [2026] **Do Good, Stay Longer? Temporal Patterns and Predictors of Newcomer-to-Core Transitions in Conventional OSS and OSS4SG** [[paper](https://arxiv.org/abs/2601.23142)]
- [2026] **Uncovering Hidden Inclusions of Vulnerable Dependencies in Real-World Java Projects** [[paper](https://arxiv.org/abs/2601.23020)]
- [2026] **On Plagiarism and Software Plagiarism** [[paper](https://arxiv.org/abs/2601.00429)]
- [2026] **On Autopilot? An Empirical Study of Human-AI Teaming and Review Practices in Open Source** [[paper](https://arxiv.org/abs/2601.13754)]
- [2026] **The Invisible Hand of AI Libraries Shaping Open Source Projects and Communities** [[paper](https://arxiv.org/abs/2601.01944)]
- [2026] **Analyzing the Availability of E-Mail Addresses for PyPI Libraries** [[paper](https://arxiv.org/abs/2601.14034)]
- [2026] **Governance Matters: Lessons from Restructuring the data.table OSS Project** [[paper](https://arxiv.org/abs/2601.13466)]

##### 2025

- [2025] **What Pulls the Strings? Understanding the Characteristics and Role of Argumentation in Open-Source Software Usability Discussions** [[paper](https://arxiv.org/abs/2512.08032)]
- [2025] **Cargo Sherlock: An SMT-Based Checker for Software Trust Costs** [[paper](https://arxiv.org/abs/2512.12553)]
- [2025] **What Drives Issue Resolution Speed? An Empirical Study of Scientific Workflow Systems on GitHub** [[paper](https://arxiv.org/abs/2512.18852)]
- [2025] **Toxicity Ahead: Forecasting Conversational Derailment on GitHub** [[paper](https://arxiv.org/abs/2512.15031)]
- [2025] **University Rents Enabling Corporate Innovation: Mapping Academic Researcher Coding and Discursive Labour in the R Language Ecosystem** [[paper](https://arxiv.org/abs/2512.19153)]
- [2025] **An LLM-based Quantitative Framework for Evaluating High-Stealthy Backdoor Risks in OSS Supply Chains** [[paper](https://arxiv.org/abs/2511.13341)]
- [2025] **PyGress: Tool for Analyzing the Progression of Code Proficiency in Python OSS Projects** [[paper](https://arxiv.org/abs/2511.05821)] [[code](https://github.com/MUICT-SERU/PyGress)]
- [2025] **Uncovering Scientific Software Sustainability through Community Engagement and Software Quality Metrics** [[paper](https://arxiv.org/abs/2511.07851)]
- [2025] **Minimizing Breaking Changes and Redundancy in Mitigating Technical Lag for Java Projects** [[paper](https://arxiv.org/abs/2511.06762)]
- [2025] **Did You Forkget It? Detecting One-Day Vulnerabilities in Open-source ForksWith Global History Analysis** [[paper](https://arxiv.org/abs/2511.05097)]
- [2025] **Towards Automated Governance: A DSL for Human-Agent Collaboration in Software Projects** [[paper](https://arxiv.org/abs/2510.14465)]
- [2025] **DynamiQ: Unlocking the Potential of Dynamic Task Allocation in Parallel Fuzzing** [[paper](https://arxiv.org/abs/2510.04469)]
- [2025] **Match & Mend: Minimally Invasive Local Reassembly for Patching N-day Vulnerabilities in ARM Binaries** [[paper](https://arxiv.org/abs/2510.14384)]
- [2025] **Interact and React: Exploring Gender Patterns in Development and the Impact on Innovation and Robustness of a User Interface Tool** [[paper](https://arxiv.org/abs/2510.15642)]
- [2025] **Community Engagement and the Lifespan of Open-Source Software Projects** [[paper](https://arxiv.org/abs/2510.15408)]
- [2025] **FOSS-chain: using blockchain for Open Source Software license compliance** [[paper](https://arxiv.org/abs/2510.01740)]
- [2025] **AutoEmpirical: LLM-Based Automated Research for Empirical Software Fault Analysis** [[paper](https://arxiv.org/abs/2510.04997)]
- [2025] **A Comparison of Conversational Models and Humans in Answering Technical Questions: the Firefox Case** [[paper](https://arxiv.org/abs/2510.21933)]
- [2025] **Explaining Code Risk in OSS: Towards LLM-Generated Fault Prediction Interpretations** [[paper](https://arxiv.org/abs/2510.06104)]
- [2025] **Towards Supporting Open Source Library Maintainers with Community-Based Analytics** [[paper](https://arxiv.org/abs/2510.15794)]
- [2025] **Bytecode-centric Detection of Known-to-be-vulnerable Dependencies in Java Projects** [[paper](https://arxiv.org/abs/2510.19393)]
- [2025] **A Benchmark Dataset And LLMs Comparison For NFR Classification With Explainable AI** [[paper](https://arxiv.org/abs/2510.18096)]
- [2025] **The Auth Shim: A Lightweight Architectural Pattern for Integrating Enterprise SSO with Standalone Open-Source Applications** [[paper](https://arxiv.org/abs/2509.03900)]
- [2025] **Revisiting Vulnerability Patch Localization: An Empirical Study and LLM-Based Solution** [[paper](https://arxiv.org/abs/2509.15777)]
- [2025] **From Hugging Face to GitHub: Tracing License Drift in the Open-Source AI Ecosystem** [[paper](https://arxiv.org/abs/2509.09873)]
- [2025] **Static Security Vulnerability Scanning of Proprietary and Open-Source Software: An Adaptable Process with Variants and Results** [[paper](https://arxiv.org/abs/2509.16985)]
- [2025] **BuildBench: Benchmarking LLM Agents on Compiling Real-World Open-Source Software** [[paper](https://arxiv.org/abs/2509.25248)]
- [2025] **Bursts and Triggers: Socially-Driven Activity in Open-Source Co-Editing Networks** [[paper](https://arxiv.org/abs/2509.26173)]
- [2025] **Software Dependencies 2.0: An Empirical Study of Reuse and Integration of Pre-Trained Models in Open-Source Projects** [[paper](https://arxiv.org/abs/2509.06085)]
- [2025] **MAVUL: Multi-Agent Vulnerability Detection via Contextual Reasoning and Interactive Refinement** [[paper](https://arxiv.org/abs/2510.00317)]
- [2025] **Open at the Core: Moving from Proprietary Technology to Building a Product on Open Source Software** *Management Science* [[paper](https://doi.org/10.1287/mnsc.2023.02886)]
- [2025] **A software pipeline for medical information extraction with large language models, open source and suitable for oncology** *npj Precision Oncology* [[paper](https://doi.org/10.1038/s41698-025-01103-4)]
- [2025] **DocFetch - Towards Generating Software Documentation from Multiple Software Artifacts** [[paper](https://arxiv.org/abs/2508.17719)]
- [2025] **Librarians’ Perception of the Sustainability of Open-Source Software for Library Automation in Academic Libraries in Adamawa State, Nigeria** *Journal of Information Resource Management (JIRM)* [[paper](https://doi.org/10.61955/josrch)]

##### 2022

- [2022] **Open Source Software Digital Sociology: Engineering Open Source Software Ecosystem for Impact and Sustainability** *Federated Africa and Middle East Conference on Software Engineering* [[paper](https://doi.org/10.1145/3531056.3542767)]

##### 2019

- [2019] **Open-Source License Compliance in Software Supply Chains** *Towards Engineering Free/Libre Open Source Software (FLOSS) Ecosystems for Impact and Sustainability* [[paper](https://doi.org/10.1007/978-981-13-7099-1_5)]

##### 2012

- [2012] **From Open Source Software to Open Source Hardware** *IFIP Advances in Information and Communication Technology* [[paper](https://doi.org/10.1007/978-3-642-33442-9_23)]
- [2012] **Perspectives on Code Forking and Sustainability in Open Source Software** *IFIP Advances in Information and Communication Technology* [[paper](https://doi.org/10.1007/978-3-642-33442-9_21)]
- [2012] **Using Multiple Case Studies to Analyse Open Source Software Business Sustainability in Sub-Saharan Africa** *IFIP Advances in Information and Communication Technology* [[paper](https://doi.org/10.1007/978-3-642-33442-9_11)]
- [2012] **Long-Term Sustainability of Open Source Software Communities beyond a Fork: A Case Study of LibreOffice** *IFIP Advances in Information and Communication Technology* [[paper](https://doi.org/10.1007/978-3-642-33442-9_3)]
- [2012] **Open Source Software in Research and Development** *IFIP Advances in Information and Communication Technology* [[paper](https://doi.org/10.1007/978-3-642-33442-9_41)]

##### 2004

- [2004] **Open Source Software** *Open Source Software* [[paper](https://doi.org/10.1016/b978-155558320-0/50002-7)]
- [2004] **How Open Source Software Is Developed** *Open Source Software* [[paper](https://doi.org/10.1016/b978-155558320-0/50010-6)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **<i>NuMagSANS</i> : a GPU-accelerated open-source software package for the generic computation of nuclear and magnetic small-angle neutron scattering observables of complex systems** *Journal of Applied Crystallography* [[paper](https://doi.org/10.1107/s160057672600258x)]
- [2026] **NuMagSANS: a GPU-accelerated open-source software package for the generic computation of nuclear and magnetic small-angle neutron scattering observables of complex systems** *arXiv (Cornell University)* [[paper](https://arxiv.org/abs/2601.18444)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **International Journal of Open Source Software and Processes** *International Journal of Open Source Software and Processes* [[paper](https://doi.org/10.4018/ijossp)]
- [2026] **IQ-TREE 3: phylogenomic inference software using complex evolutionary models** *Molecular Biology and Evolution* [[paper](https://doi.org/10.1093/molbev/msag117)]
- [2026] **IRSSG: An open-source software package for spin space groups** *Computer Physics Communications* [[paper](https://arxiv.org/abs/2511.21821)]
- [2026] **Contribution Patterns in Open Source Software for Social Good: Dynamics, Individuals, and Impact CSCW010** *Proceedings of the ACM on Human-Computer Interaction* [[paper](https://doi.org/10.1145/3788046)]
- [2026] **Amsterdam Local Field potential Analysis (ALFA) toolbox: an open source software package for deep brain stimulation research** *Brain stimulation* [[paper](https://doi.org/10.1016/j.brs.2026.103071)]
- [2026] **M2C: An open-source software for multiphysics simulation of compressible multi-material flows and fluid-structure interactions** *Computer Physics Communications* [[paper](https://doi.org/10.1016/j.cpc.2026.110023)]
- [2026] **Advancing Digital Government: Integrating Open Source Software Enablement Indicators in Maturity Indexes** *SSRN Electronic Journal* [[paper](https://doi.org/10.2139/ssrn.6507132)]

##### 2025

- [2025] **diveXplore - An Open-Source Software for Modern Video Retrieval with Image/Text Embeddings** [[paper](https://doi.org/10.1145/3746027.3756877)]
- [2025] **KF-GINS: an open-sourced software for GNSS/INS integrated navigation** *GPS Solutions* [[paper](https://doi.org/10.1007/s10291-025-01967-w)]
- [2025] **Career concerns as a public good: The role of signaling for open source software development** *Labour Economics* [[paper](https://doi.org/10.1016/j.labeco.2025.102800)]
- [2025] **APAS-TR: a MATLAB-based open-source software package for multi-GNSS precise point positioning and its performance in strong ionospheric conditions** *Earth Science Informatics* [[paper](https://doi.org/10.1007/s12145-025-02001-w)]
- [2025] **Measuring the potential risk of re-identification of imaging research participants from open-source automated face recognition software** *NeuroImage* [[paper](https://doi.org/10.1016/j.neuroimage.2025.121476)]
- [2025] **MSnLib: efficient generation of open multi-stage fragmentation mass spectral libraries** *Nature Methods* [[paper](https://doi.org/10.1038/s41592-025-02813-0)]

[⬆ Back to top](#paper-list)

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
