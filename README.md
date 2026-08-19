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
  - [Survey](#survey)
- [📚 Developer Tools](#developer-tools)
  - [Method](#method)
  - [Tooling](#tooling)
- [📚 DevOps & CI/CD](#devops-&-ci/cd)
  - [Method](#method)
  - [Application](#application)
  - [Survey](#survey)
  - [Development](#development)
  - [Tooling](#tooling)
- [📚 Code Quality](#code-quality)
  - [Method](#method)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Tooling](#tooling)
- [📚 Software Architecture](#software-architecture)
  - [Method](#method)
  - [Survey](#survey)
  - [Systems](#systems)
- [📚 Programming Languages](#programming-languages)
  - [Theory](#theory)
- [📚 Human Factors & DX](#human-factors-&-dx)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
- [📚 AI for Software Engineering](#ai-for-software-engineering)
  - [Method](#method)
  - [Evaluation](#evaluation)
  - [Survey](#survey)
  - [Tooling](#tooling)
- [📚 Security & Supply Chain](#security-&-supply-chain)
  - [Method](#method)
  - [Survey](#survey)
  - [Development](#development)
- [📚 Open Source](#open-source)
  - [Survey](#survey)
- [📚 Surveys & Reviews](#surveys-&-reviews)

### Software Engineering

#### Theory

##### 1986

- [1986] **No Silver Bullet: Essence and Accidents of Software Engineering** *IEEE Computer* [[paper](https://doi.org/10.1145/358849.358862)]

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

[⬆ Back to top](#paper-list)

### Developer Tools

#### Method

##### 2026

- [2026] **The Stoic Unix Philosophy: Building Calm Tools for a Chaotic World** *tobias-weiss.org* [[paper](https://tobias-weiss.org/content/devops/stoic-unix-philosophy/)]
- [2026] **Does ISO-Grounded NFR Specification Improve LLM Code Generation? A Comparison of Rich and Structured Interventions against a Natural-Language Baseline** [[paper](https://arxiv.org/abs/2608.13742)]
- [2026] **Statistical Analysis of Executability and Program Equivalence in Decompilation for IoT Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.06960)]
- [2026] **AssumptionMiner: Extracting, Tracing, and Revising Implicit Assumptions in LLM Code Generation** [[paper](https://arxiv.org/abs/2607.22898)]
- [2026] **Test Coverage Analysis of Agentic Pull Requests** [[paper](https://arxiv.org/abs/2607.18057)]
- [2026] **VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation** [[paper](https://arxiv.org/abs/2606.07992)]
- [2026] **Is Agent Code Less Maintainable Than Human Code?** [[paper](https://arxiv.org/abs/2606.21804)]
- [2026] **What Software Engineering Looks Like to AI Agents? -- An Empirical Study of AI-Only Technical Discourse on MoltBook** [[paper](https://arxiv.org/abs/2605.08380)]
- [2026] **Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution** [[paper](https://arxiv.org/abs/2604.05955)]
- [2026] **IndustriConnect: MCP Adapters and Mock-First Evaluation for AI-Assisted Industrial Operations** [[paper](https://arxiv.org/abs/2603.24703)]
- [2026] **SpecOps: A Fully Automated AI Agent Testing Framework in Real-World GUI Environments** [[paper](https://arxiv.org/abs/2603.10268)]
- [2026] **Beyond the Control Equations: An Artifact Study of Implementation Quality in Robot Control Software** [[paper](https://arxiv.org/abs/2602.04799)]
- [2026] **From Logic to Toolchains: An Empirical Study of Bugs in the TypeScript Ecosystem** [[paper](https://arxiv.org/abs/2601.21186)]
- [2026] **SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents** [[paper](https://arxiv.org/abs/2601.16746)]
- [2026] **AI builds, We Analyze: An Empirical Study of AI-Generated Build Code Quality** [[paper](https://arxiv.org/abs/2601.16839)]
- [2026] **Security in the Age of AI Teammates: An Empirical Study of Agentic Pull Requests on GitHub** [[paper](https://arxiv.org/abs/2601.00477)]

##### 2025

- [2025] **A Practical Solution to Systematically Monitor Inconsistencies in SBOM-based Vulnerability Scanners** [[paper](https://arxiv.org/abs/2512.17710)]
- [2025] **Software for Studying CASCADE Error Correction Protocols in Quantum Communications** [[paper](https://arxiv.org/abs/2511.23050)]
- [2025] **MermaidSeqBench: An Evaluation Benchmark for NL-to-Mermaid Sequence Diagram Generation** [[paper](https://arxiv.org/abs/2511.14967)]
- [2025] **Overview and Performance Evaluation of Supervisory Controller Synthesis with Eclipse ESCET v4.0** [[paper](https://arxiv.org/abs/2511.04370)]

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
- [2026] **Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?** [[paper](https://arxiv.org/abs/2606.19388)]
- [2026] **Matching Matters: A Fair Quality-Efficiency Benchmark for Command-Line Agents** [[paper](https://arxiv.org/abs/2606.21140)]
- [2026] **Undefined Behavior in C and C++: An Experiment With Desktop Use Cases** [[paper](https://arxiv.org/abs/2606.12064)]
- [2026] **LogCopilot: Automating Log Aggregation Analysis through Large Language Models** [[paper](https://arxiv.org/abs/2606.17094)]
- [2026] **Cleaning Logs for Downstream Tasks (Registered Report)** [[paper](https://arxiv.org/abs/2606.27000)]
- [2026] **Before the Pull Request: Mining Multi-Agent Coordination** [[paper](https://arxiv.org/abs/2606.19616)]
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
- [2026] **Empirical Characterization of Logging Smells in Machine Learning Code** [[paper](https://arxiv.org/abs/2601.05540)]
- [2026] **VarParser: Unleashing the Neglected Power of Variables for LLM-based Log Parsing** *WWW 2026* [[paper](https://arxiv.org/abs/2601.22676)]
- [2026] **DeLog: An Efficient Log Compression Framework with Pattern Signature Synthesis** [[paper](https://arxiv.org/abs/2601.15084)]
- [2026] **Small is Beautiful: A Practical and Efficient Log Parsing Framework** [[paper](https://arxiv.org/abs/2601.22590)]
- [2026] **Advanced Vulnerability Scanning for Open Source Software: Detection and Mitigation of Log4j Vulnerabilities** [[paper](https://arxiv.org/abs/2601.00235)]
- [2026] **MicLog: Towards Accurate and Efficient LLM-based Log Parsing via Progressive Meta In-Context Learning** [[paper](https://arxiv.org/abs/2601.07005)]

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

[⬆ Back to top](#paper-list)

### DevOps & CI/CD

#### Method

##### 2007

- [2007] **Continuous Integration: Improving Software Quality and Reducing Risk** *IEEE Software* [[paper](https://doi.org/10.1109/MS.2007.93)]

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
- [2026] **Data-Oriented Modeling for Spacecraft Design** [[paper](https://arxiv.org/abs/2603.24841)] [[code](https://github.com/VisVivaSpace/vverdad-prototype)]
- [2026] **SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration** [[paper](https://arxiv.org/abs/2603.03823)]
- [2026] **From Leaderboard to Deployment: Code Quality Challenges in AV Perception Repositories** [[paper](https://arxiv.org/abs/2603.02194)]
- [2026] **A Practical Framework for Flaky Failure Triage in Distributed Database Continuous Integration** [[paper](https://arxiv.org/abs/2603.23054)]
- [2026] **Praxium: Diagnosing Cloud Anomalies with AI-based Telemetry and Dependency Analysis** [[paper](https://arxiv.org/abs/2603.23890)]
- [2026] **Risk-Aware Batch Testing for Performance Regression Detection** [[paper](https://arxiv.org/abs/2604.00222)]
- [2026] **It's Not Just Timestamps: A Study on Docker Reproducibility** [[paper](https://arxiv.org/abs/2602.17678)]
- [2026] **Source Code Hotspots: A Diagnostic Method for Quality Issues** [[paper](https://arxiv.org/abs/2602.13170)]
- [2026] **Causal Inference for the Effect of Code Coverage on Bug Introduction** [[paper](https://arxiv.org/abs/2602.03585)]
- [2026] **Understanding and Detecting Flaky Builds in GitHub Actions** [[paper](https://arxiv.org/abs/2602.02307)]
- [2026] **Role of CI Adoption in Mobile App Success: An Empirical Study of Open-Source Android Projects** [[paper](https://arxiv.org/abs/2602.01957)]
- [2026] **Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection** [[paper](https://arxiv.org/abs/2602.05312)]
- [2026] **PhantomRun: Auto Repair of Compilation Errors in Embedded Open Source Software** [[paper](https://arxiv.org/abs/2602.20284)]
- [2026] **Cross-Project Flakiness: A Case Study of the OpenStack Ecosystem** [[paper](https://arxiv.org/abs/2602.09311)]
- [2026] **Predicting Intermittent Job Failure Categories for Diagnosis Using Few-Shot Fine-Tuned Language Models** [[paper](https://arxiv.org/abs/2601.22264)]
- [2026] **Reinforcement Learning for Dynamic Workflow Optimization in CI/CD Pipelines** [[paper](https://arxiv.org/abs/2601.11647)]
- [2026] **LogSieve: Task-Aware CI Log Reduction for Sustainable LLM-Based Analysis** [[paper](https://arxiv.org/abs/2601.20148)]

##### 2025

- [2025] **Fast and Realistic Automated Scenario Simulations and Reporting for an Autonomous Racing Stack** [[paper](https://arxiv.org/abs/2512.24402)]
- [2025] **Detecting Flakiness in Quantum Software: A Dynamic Testing Approach** [[paper](https://arxiv.org/abs/2512.18088)]
- [2025] **DRS-OSS: A Diff-Risk Scoring Tool for Continuous Integration Workflows** [[paper](https://arxiv.org/abs/2511.21964)]
- [2025] **Exploringand Unleashing the Power of Large Language Models in CI/CD Configuration Translation** [[paper](https://arxiv.org/abs/2511.01316)]
- [2025] **Ontology-Driven Model-to-Model Transformation of Workflow Specifications** [[paper](https://arxiv.org/abs/2511.13661)]
- [2025] **Large-Scale Empirical Analysis of Continuous Fuzzing: Insights from 1 Million Fuzzing Sessions** [[paper](https://arxiv.org/abs/2510.16433)]
- [2025] **Auto-repair without test cases: How LLMs fix compilation errors in large industrial embedded code** [[paper](https://arxiv.org/abs/2510.13575)]
- [2025] **Operationalizing AI: Empirical Evidence on MLOps Practices, User Satisfaction, and Organizational Context** [[paper](https://arxiv.org/abs/2510.09968)]
- [2025] **Towards an Optimized Benchmarking Platform for CI/CD Pipelines** [[paper](https://arxiv.org/abs/2510.18640)]
- [2025] **Past, Present, and Future of Bug Tracking in the Generative AI Era** [[paper](https://arxiv.org/abs/2510.08005)]
- [2025] **A General Solution for the Implementation of CI/CD in Embedded Linux Development** [[paper](https://arxiv.org/abs/2510.19240)]
- [2025] **Vision: An Extensible Methodology for Formal Software Verification in Microservice Systems** [[paper](https://arxiv.org/abs/2509.02860)]
- [2025] **Multi-Threaded Software Model Checking via Parallel Trace Abstraction Refinement** [[paper](https://arxiv.org/abs/2509.13699)]
- [2025] **Cross-Domain Evaluation of Transformer-Based Vulnerability Detection on Open &amp; Industry Data** [[paper](https://arxiv.org/abs/2509.09313)]
- [2025] **ReDef: Do Code Language Models Truly Understand Code Changes for Just-in-Time Software Defect Prediction?** [[paper](https://arxiv.org/abs/2509.09192)]
- [2025] **On the Illusion of Success: An Empirical Study of Build Reruns and Silent Failures in Industrial CI** [[paper](https://arxiv.org/abs/2509.14347)]
- [2025] **DTInsight: A Tool for Explicit, Interactive, and Continuous Digital Twin Reporting** [[paper](https://arxiv.org/abs/2508.18431)]
- [2025] **Addressing Reproducibility Challenges in HPC with Continuous Integration** [[paper](https://arxiv.org/abs/2508.21289)]
- [2025] **The Integration of Agile Methodologies in DevOps Practices within the Information Technology Industry** [[paper](https://arxiv.org/abs/2508.21811)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2026

- [2026] **White paper: A perspective on civilian-to-defence research transfer to SDD** [[paper](https://arxiv.org/abs/2608.09349)]
- [2026] **Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions** [[paper](https://arxiv.org/abs/2607.02294)]
- [2026] **DevOps and General Developers: Insights from Stack Overflow's 2023 Survey** [[paper](https://arxiv.org/abs/2606.19395)]
- [2026] **Overcoming Challenges in Agile and DevOps Integration: A Qualitative Study** [[paper](https://arxiv.org/abs/2606.01676)]
- [2026] **AutoPipelineAI: Context-Aware CI/CD Pipeline Generation from Natural Language** [[paper](https://arxiv.org/abs/2606.06662)]
- [2026] **BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization** [[paper](https://arxiv.org/abs/2606.27733)]
- [2026] **Low-Code Paradox in DevOps: Security and Governance Insights from Practitioners** [[paper](https://arxiv.org/abs/2605.16971)]
- [2026] **Software Product Line Engineering: Adoption, Tooling and AI Era Challenges** [[paper](https://arxiv.org/abs/2605.21353)]
- [2026] **Operationalizing Software Engineering Theories for Practical Validation** [[paper](https://arxiv.org/abs/2605.03257)]
- [2026] **Measuring Delivery Consistency in Practice: A DORA Extension from a Multi-Platform Release Setting** [[paper](https://arxiv.org/abs/2606.00364)]
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

##### 2024

- [2024] **Infrastructure as Code: A Systematic Mapping Study** [[paper](https://arxiv.org/abs/2401.01001)]

[⬆ Back to top](#paper-list)

#### Development

##### 2026

- [2026] **Security-First Evaluation of Text-to-Terraform: Benchmarking LLMs and SLMs for Secure IaC Generation** [[paper](https://arxiv.org/abs/2608.02672)]
- [2026] **Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair** [[paper](https://arxiv.org/abs/2608.13404)]
- [2026] **TerraRepair: A Tool-Grounded LLM Agent for Infrastructure-as-Code Repair** [[paper](https://arxiv.org/abs/2607.11390)]
- [2026] **Taming the Drift: Context-aware Repair of Dockerfile Drift during Software Evolution** [[paper](https://arxiv.org/abs/2607.12541)] [[code](https://github.com/dw763j/Cadre)]
- [2026] **SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code** [[paper](https://arxiv.org/abs/2606.05249)]
- [2026] **Verifier-First Evaluation of Agentic LLMs for Infrastructure-as-Code Generation** [[paper](https://arxiv.org/abs/2607.20478)]
- [2026] **Ambig-IaC: Multi-level Disambiguation for Interactive Cloud Infrastructure-as-Code Synthesis** [[paper](https://arxiv.org/abs/2604.02382)]
- [2026] **Understanding Bugs in Template Engine-Based Applications: Symptoms, Root Causes, and Fix Patterns** [[paper](https://arxiv.org/abs/2604.27692)]
- [2026] **RIVA: Leveraging LLM Agents for Reliable Configuration Drift Detection** [[paper](https://arxiv.org/abs/2603.02345)]
- [2026] **Beyond Local Code Optimization: Multi-Agent Reasoning for Software System Optimization** [[paper](https://arxiv.org/abs/2603.14703)]
- [2026] **TerraFormer: Automated Infrastructure-as-Code with LLMs Fine-Tuned via Policy-Guided Verifier Feedback** [[paper](https://arxiv.org/abs/2601.08734)]
- [2026] **APEX-SWE** [[paper](https://arxiv.org/abs/2601.08806)]

##### 2025

- [2025] **IaC Generation with LLMs: An Error Taxonomy and A Study on Configuration Knowledge Injection** [[paper](https://arxiv.org/abs/2512.14792)]
- [2025] **Accelerating Control Systems with GitOps: A Path to Automation and Reliability** [[paper](https://arxiv.org/abs/2511.05663)]
- [2025] **GenSIaC: Toward Security-Aware Infrastructure-as-Code Generation with Large Language Models** [[paper](https://arxiv.org/abs/2511.12385)]
- [2025] **Security smells in infrastructure as code: a taxonomy update beyond the seven sins** [[paper](https://arxiv.org/abs/2509.18761)]

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
- [2026] **Enabling Performant and Flexible Model-Internal Observability for LLM Inference** [[paper](https://arxiv.org/abs/2605.11093)] [[code](https://github.com/ProjectDMX/DMI)]
- [2026] **AI-Driven Adaptive Adversaries and the Erosion of Cryptographic Trust in Public Key Systems** [[paper](https://arxiv.org/abs/2605.24542)]
- [2026] **KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition** [[paper](https://arxiv.org/abs/2605.25376)]
- [2026] **Property-Level Reconstructability of Agent Decisions: An Anchor-Level Pilot Across Vendor SDK Adapter Regimes** [[paper](https://arxiv.org/abs/2605.12078)]
- [2026] **Finding Missing Input Validation in TEEs via LLM-Assisted Symbolic Execution** [[paper](https://arxiv.org/abs/2605.22058)]
- [2026] **LATS-RCA: Language Agent Tree Search for Root Cause Analysis in Microservices** [[paper](https://arxiv.org/abs/2605.03505)] [[code](https://github.com/kottinov/lats-rca)]
- [2026] **AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents** [[paper](https://arxiv.org/abs/2605.13357)]
- [2026] **AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair** [[paper](https://arxiv.org/abs/2605.04624)]
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

##### 2025

- [2025] **Monitoring Monitorability** [[paper](https://arxiv.org/abs/2512.18311)]
- [2025] **Opus: A Quantitative Framework for Workflow Evaluation** [[paper](https://arxiv.org/abs/2511.04220)]
- [2025] **Monitoring and Observability of Machine Learning Systems: Current Practices and Gaps** [[paper](https://arxiv.org/abs/2510.24142)]
- [2025] **Validating Alerts in Cloud-Native Observability** [[paper](https://arxiv.org/abs/2510.23970)]
- [2025] **Interoperability From OpenTelemetry to Kieker: Demonstrated as Export from the Astronomy Shop** [[paper](https://arxiv.org/abs/2510.11179)]
- [2025] **Task-Aware Reduction for Scalable LLM-Database Systems** [[paper](https://arxiv.org/abs/2510.11813)]
- [2025] **Towards a user-centric HPC-QC environment** [[paper](https://arxiv.org/abs/2509.20525)]
- [2025] **A Grey Literature Review of AI-Native Applications** [[paper](https://arxiv.org/abs/2509.13144)]
- [2025] **CRACI: A Cloud-Native Reference Architecture for the Industrial Compute Continuum** [[paper](https://arxiv.org/abs/2509.07498)]
- [2025] **UniSage: A Unified and Post-Analysis-Aware Sampling for Microservices** [[paper](https://arxiv.org/abs/2509.26336)]
- [2025] **Explain and Monitor Deep Learning Models for Computer Vision using Obz AI** [[paper](https://arxiv.org/abs/2508.18188)]

[⬆ Back to top](#paper-list)

### Code Quality

#### Method

##### 2026

- [2026] **Accelerating Accurate Assignment Authoring Using Solution-Generated Autograders** [[paper](https://arxiv.org/abs/2608.06572)]
- [2026] **ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning** [[paper](https://arxiv.org/abs/2608.14352)]
- [2026] **TestMiner: Software Testing Analysis for GitHub Repositories** [[paper](https://arxiv.org/abs/2607.12223)] [[project](https://andrehora.github.io/testminer)]
- [2026] **(Over)Reliance on Test Agents in AI-Assisted Software Testing** [[paper](https://arxiv.org/abs/2607.17927)]
- [2026] **Faithful Autoformalization of Natural Language Assertions** [[paper](https://arxiv.org/abs/2607.13303)]
- [2026] **From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants** [[paper](https://arxiv.org/abs/2607.11387)]
- [2026] **Benchmarking Quantum Software Testing with Scalable Quantum Programs** [[paper](https://arxiv.org/abs/2607.02029)]
- [2026] **An Exploration of Agentic Information Fusion for Test Maintenance Prediction** [[paper](https://arxiv.org/abs/2607.04786)]
- [2026] **On the risk of coding before testing: An empirical study on LLM-based test generation workflow** [[paper](https://arxiv.org/abs/2607.05139)]
- [2026] **Complexity Theory of Randomised Testing** [[paper](https://arxiv.org/abs/2607.11811)]
- [2026] **From Custom Logic to APIs: Understanding and Recommending API Replacement Refactorings** [[paper](https://arxiv.org/abs/2606.06912)]
- [2026] **Humor in Software Testing Education** [[paper](https://arxiv.org/abs/2606.21682)]
- [2026] **Governance Controls for AI-Generated Test Artifacts in Autonomous Software Testing** [[paper](https://arxiv.org/abs/2606.08806)]
- [2026] **Learning Critical Testing Literacy Through Puzzles: an Experience Report** [[paper](https://arxiv.org/abs/2606.20129)]
- [2026] **Characterizing Tests in IoT Software: Practices, Challenges and Opportunities** [[paper](https://arxiv.org/abs/2606.12592)]
- [2026] **AI-Driven Test Case Generation from Natural Language Requirements: A Survey of Techniques and Research Gaps** [[paper](https://arxiv.org/abs/2606.06563)]
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
- [2026] **Can Language Models Pass Software Testing Certification Exams? a case study** [[paper](https://arxiv.org/abs/2603.23142)]
- [2026] **Generative AI in Software Testing: Current Trends and Future Directions** [[paper](https://arxiv.org/abs/2603.02141)]
- [2026] **ISTQB Certifications Under the Lens: Their Contributions to the Software-Testing Profession; and AI-assisted Synthesis of Practitioners' Endorsements and Criticisms** [[paper](https://arxiv.org/abs/2603.14572)]
- [2026] **From Natural Language to Executable Properties for Property-based Testing of Mobile Apps** [[paper](https://arxiv.org/abs/2603.21263)]
- [2026] **Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing** [[paper](https://arxiv.org/abs/2603.08616)]
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

##### 2025

- [2025] **An Empirical Framework for Evaluating Semantic Preservation Using Hugging Face** [[paper](https://arxiv.org/abs/2512.07983)]
- [2025] **Industry Expectations and Skill Demands in Quantum Software Testing** [[paper](https://arxiv.org/abs/2512.14861)]
- [2025] **Search-based Software Testing Driven by Domain Knowledge: Reflections and New Perspectives** [[paper](https://arxiv.org/abs/2512.10079)]
- [2025] **Reinforcement Learning Integrated Agentic RAG for Software Test Cases Authoring** [[paper](https://arxiv.org/abs/2512.06060)]
- [2025] **Fuzzing the brain: Automated stress testing for the safety of ML-driven neurostimulation** [[paper](https://arxiv.org/abs/2512.05383)]
- [2025] **Multi-Agent LLM Committees for Autonomous Software Beta Testing** [[paper](https://arxiv.org/abs/2512.21352)]
- [2025] **How Low Can You Go? The Data-Light SE Challenge** [[paper](https://arxiv.org/abs/2512.13524)] [[code](https://github.com/KKGanguly/NEO)]
- [2025] **LLMCFG-TGen: Using LLM-Generated Control Flow Graphs to Automatically Create Test Cases from Use Cases** [[paper](https://arxiv.org/abs/2512.06401)]
- [2025] **RefAgent: A Multi-agent LLM-based Framework for Automatic Software Refactoring** [[paper](https://arxiv.org/abs/2511.03153)]
- [2025] **A Code Smell Refactoring Approach using GNNs** [[paper](https://arxiv.org/abs/2511.12069)]
- [2025] **An Agent-Based Framework for the Automatic Validation of Mathematical Optimization Models** [[paper](https://arxiv.org/abs/2511.16383)]
- [2025] **Empirical Derivations from an Evolving Test Suite** [[paper](https://arxiv.org/abs/2511.00915)]
- [2025] **Technical knowledge and soft skills in software startups within the Colombian entrepreneurial ecosystem** [[paper](https://arxiv.org/abs/2511.21769)]
- [2025] **Autonomous QA Agent: A Retrieval-Augmented Framework for Reliable Selenium Script Generation** [[paper](https://arxiv.org/abs/2601.06034)]
- [2025] **LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework** [[paper](https://arxiv.org/abs/2511.20403)]
- [2025] **Towards Comprehensive Sampling of SMT Solutions** [[paper](https://arxiv.org/abs/2511.10326)]
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
- [2025] **Large Language Models for Software Testing: A Research Roadmap** [[paper](https://arxiv.org/abs/2509.25043)]
- [2025] **AutoStub: Genetic Programming-Based Stub Creation for Symbolic Execution** [[paper](https://arxiv.org/abs/2509.08524)]
- [2025] **TPSQLi: Test Prioritization for SQL Injection Vulnerability Detection in Web Applications** [[paper](https://arxiv.org/abs/2509.10920)]
- [2025] **Leveraging SystemC-TLM-based Virtual Prototypes for Embedded Software Fuzzing** [[paper](https://arxiv.org/abs/2509.01318)]
- [2025] **Interleaving Large Language Models for Compiler Testing** [[paper](https://arxiv.org/abs/2508.18955)]
- [2025] **Rethinking Testing for LLM Applications: Characteristics, Challenges, and a Lightweight Interaction Protocol** [[paper](https://arxiv.org/abs/2508.20737)]

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
- [2026] **A Practical Guide to Establishing Technical Debt Management (TDM Guide for Practitioners)** [[paper](https://arxiv.org/abs/2601.11430)]
- [2026] **Self-Admitted Technical Debt in LLM Software: An Empirical Comparison with ML and Non-ML Software** [[paper](https://arxiv.org/abs/2601.06266)]
- [2026] **"TODO: Fix the Mess Gemini Created": Towards Understanding GenAI-Induced Self-Admitted Technical Debt** [[paper](https://arxiv.org/abs/2601.07786)]
- [2026] **Folklore in Software Engineering: A Definition and Conceptual Foundations** [[paper](https://arxiv.org/abs/2601.21814)]
- [2026] **An Exploratory Pilot Survey on Technical Quality Control Practices in Agile R&amp;D Projects** [[paper](https://arxiv.org/abs/2601.06689)]
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

##### 2025

- [2025] **Quantitative Analysis of Technical Debt and Pattern Violation in Large Language Model Architectures** [[paper](https://arxiv.org/abs/2512.04273)]
- [2025] **Vibe Coding in Practice: Flow, Technical Debt, and Guidelines for Sustainable Use** [[paper](https://arxiv.org/abs/2512.11922)]
- [2025] **LAURA: Enhancing Code Review Generation with Context-Enriched Retrieval-Augmented LLM** [[paper](https://arxiv.org/abs/2512.01356)]
- [2025] **On Assessing the Relevance of Code Reviews Authored by Generative Models** [[paper](https://arxiv.org/abs/2512.15466)]
- [2025] **SGCR: A Specification-Grounded Framework for Trustworthy LLM Code Review** [[paper](https://arxiv.org/abs/2512.17540)]
- [2025] **Engagement in Code Review: Emotional, Behavioral, and Cognitive Dimensions in Peer vs. LLM Interactions** [[paper](https://arxiv.org/abs/2512.05309)]
- [2025] **Coding With AI: From a Reflection on Industrial Practices to Future Computer Science and Software Engineering Education** [[paper](https://arxiv.org/abs/2512.23982)]
- [2025] **A survey of generative AI adoption and perceived productivity among scientists who program** [[paper](https://arxiv.org/abs/2512.19644)]
- [2025] **An insight into the technical debt-fix trade off in software backporting** [[paper](https://arxiv.org/abs/2511.09000)]
- [2025] **SQuaD: The Software Quality Dataset** [[paper](https://arxiv.org/abs/2511.11265)]
- [2025] **Hidden in Plain Sight: Where Developers Confess Self-Admitted Technical Debt** [[paper](https://arxiv.org/abs/2511.01529)]
- [2025] **Establishing Traceability Links between Release Notes &amp; Software Artifacts: Practitioners' Perspectives** [[paper](https://arxiv.org/abs/2511.18187)]
- [2025] **Exploring Scientific Debt: Harnessing AI for SATD Identification in Scientific Software** [[paper](https://arxiv.org/abs/2511.17368)]
- [2025] **Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics** [[paper](https://arxiv.org/abs/2511.10271)]
- [2025] **An Empirical Study of Java Code Improvements Based on Stack Overflow Answer Edits** [[paper](https://arxiv.org/abs/2511.05813)]
- [2025] **Peer Code Review in Research Software Development: The Research Software Engineer Perspective** [[paper](https://arxiv.org/abs/2511.10781)]
- [2025] **Benchmarking LLMs for Fine-Grained Code Review with Enriched Context in Practice** [[paper](https://arxiv.org/abs/2511.07017)] [[code](https://github.com/kinesiatricssxilm14/ContextCRBench)]
- [2025] **AILINKPREVIEWER: Enhancing Code Reviews with LLM-Powered Link Previews** [[paper](https://arxiv.org/abs/2511.09223)] [[code](https://github.com/c4rtune/AILinkPreviewer)]
- [2025] **When More Retrieval Hurts: Retrieval-Augmented Code Review Generation** [[paper](https://arxiv.org/abs/2511.05302)]
- [2025] **The Future of Development Environments with AI Foundation Models: NII Shonan Meeting 222 Report** [[paper](https://arxiv.org/abs/2511.16092)]
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
- [2025] **PromptDebt: A Comprehensive Study of Technical Debt Across LLM Projects** [[paper](https://arxiv.org/abs/2509.20497)]
- [2025] **Rethinking Technology Stack Selection with AI Coding Proficiency** [[paper](https://arxiv.org/abs/2509.11132)]
- [2025] **GitHub's Copilot Code Review: Can AI Spot Security Flaws Before You Commit?** [[paper](https://arxiv.org/abs/2509.13650)]
- [2025] **Fine-Tuning LLMs to Analyze Multiple Dimensions of Code Review: A Maximum Entropy Regulated Long Chain-of-Thought Approach** [[paper](https://arxiv.org/abs/2509.21170)]
- [2025] **ChatGPT for Code Refactoring: Analyzing Topics, Interaction, and Effective Prompts** [[paper](https://arxiv.org/abs/2509.08090)]
- [2025] **SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation** [[paper](https://arxiv.org/abs/2509.01494)]
- [2025] **Intuition to Evidence: Measuring AI's True Impact on Developer Productivity** [[paper](https://arxiv.org/abs/2509.19708)]
- [2025] **Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions** [[paper](https://arxiv.org/abs/2508.18771)]
- [2025] **Previously on... Automating Code Review** [[paper](https://arxiv.org/abs/2508.18003)]

##### 2023

- [2023] **Code Review at the Speed of Light: What's Wrong with Pull Requests?** [[paper](https://arxiv.org/abs/2306.12345)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2022

- [2022] **Technical Debt: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2209.01234)]

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
- [2026] **From Specification to Execution: AI Assisted Scientific Workflow Management** [[paper](https://arxiv.org/abs/2606.18425)]
- [2026] **From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes** [[paper](https://arxiv.org/abs/2606.23797)]
- [2026] **Strategies for Guiding LLMs to Use Software Design Patterns: A Case of Singleton** [[paper](https://arxiv.org/abs/2605.26898)]
- [2026] **Deterministic vs. Probabilistic Summarisation: An Empirical Trade-off Study in Design Pattern Centric Java Code** [[paper](https://arxiv.org/abs/2605.21943)]
- [2026] **Using LLMs in Software Design: An Empirical Study of GitHub and A Practitioner Survey** [[paper](https://arxiv.org/abs/2605.01392)]
- [2026] **The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models** [[paper](https://arxiv.org/abs/2605.26128)]
- [2026] **A Pilot Study on Detecting Software Design Patterns with Large Language Models: An Empirical Evaluation** [[paper](https://arxiv.org/abs/2604.17329)]
- [2026] **Quantum-HPC Software Stacks and the openQSE Reference Architecture: A Survey** [[paper](https://arxiv.org/abs/2604.20912)]
- [2026] **LLM4Log: A Systematic Review of Large Language Model-based Log Analysis** [[paper](https://arxiv.org/abs/2604.16359)]
- [2026] **Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems** [[paper](https://arxiv.org/abs/2603.15690)]
- [2026] **Beyond the Code: A Multi-Modal Assessment Strategy for Fostering Professional Competencies via Introductory Programming Projects** [[paper](https://arxiv.org/abs/2603.18741)]
- [2026] **AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems** [[paper](https://arxiv.org/abs/2603.15727)]
- [2026] **A Pythonic Functional Approach for Semantic Data Harmonisation in the ILIAD Project** [[paper](https://arxiv.org/abs/2604.13042)]
- [2026] **Carbon-Aware Governance Gates: An Architecture for Sustainable GenAI Development** [[paper](https://arxiv.org/abs/2602.19718)]
- [2026] **Towards Automated Page Object Generation for Web Testing using Large Language Models** [[paper](https://arxiv.org/abs/2602.19294)]
- [2026] **Bridging the Sim-to-Real Gap with multipanda ros2: A Real-Time ROS2 Framework for Multimanual Systems** [[paper](https://arxiv.org/abs/2602.02269)]
- [2026] **SEER: Spectral Entropy Encoding of Roles for Context-Aware Attention-Based Design Pattern Detection** [[paper](https://arxiv.org/abs/2601.13334)]
- [2026] **Developer Perspectives on REST API Usability: A Study of REST API Guidelines** [[paper](https://arxiv.org/abs/2601.16705)]

##### 2025

- [2025] **Analysis of Design Patterns and Benchmark Practices in Apache Kafka Event-Streaming Systems** [[paper](https://arxiv.org/abs/2512.16146)]
- [2025] **Towards Benchmarking Design Pattern Detection Under Obfuscation: Reproducing and Evaluating Attention-Based Detection Method** [[paper](https://arxiv.org/abs/2512.07193)]
- [2025] **Hybrid-Code v2: Zero-Hallucination Clinical ICD-10 Coding via Neuro-Symbolic Verification and Automated Knowledge Base Expansion** [[paper](https://arxiv.org/abs/2512.23743)]
- [2025] **Designing LLM-based Multi-Agent Systems for Software Engineering Tasks: Quality Attributes, Design Patterns and Rationale** [[paper](https://arxiv.org/abs/2511.08475)]
- [2025] **Statistical Independence Aware Caching for LLM Workflows** [[paper](https://arxiv.org/abs/2511.22118)]
- [2025] **Lingxi: Repository-Level Issue Resolution Framework Enhanced by Procedural Knowledge Guided Scaling** [[paper](https://arxiv.org/abs/2510.11838)]
- [2025] **Are We SOLID Yet? An Empirical Study on Prompting LLMs to Detect Design Principle Violations** [[paper](https://arxiv.org/abs/2509.03093)]

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
- [2025] **State-of-the-Art in Software Security Visualization: A Systematic Review** [[paper](https://arxiv.org/abs/2509.20385)]
- [2025] **SWE-QA: Can Language Models Answer Repository-level Code Questions?** [[paper](https://arxiv.org/abs/2509.14635)]

##### 2022

- [2022] **Microservices: Yesterday, Today, and Tomorrow** [[paper](https://arxiv.org/abs/2203.00001)]

[⬆ Back to top](#paper-list)

#### Systems

##### 2026

- [2026] **An Empirical Comparison of Monolithic and Microservices Architectures for an E-Commerce Application** [[paper](https://arxiv.org/abs/2608.15668)]
- [2026] **Energy Efficiency in Microservice Architectures: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2608.04070)]
- [2026] **ORCA: Observability-Grounded Program Repair for Microservice Incidents** [[paper](https://arxiv.org/abs/2608.17018)]
- [2026] **GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices** [[paper](https://arxiv.org/abs/2608.08968)]
- [2026] **eIRWR: Enhanced Iterative Random Walk with Restart for Scalable Root Cause Analysis in Microservices** [[paper](https://arxiv.org/abs/2608.08073)]
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
- [2026] **A Domain-Driven Design Simulator for Business Logic-Rich Microservice Systems** [[paper](https://arxiv.org/abs/2605.01159)]
- [2026] **Genetic Programming for Self-Adaptive Auto-Scaling of Microservices** [[paper](https://arxiv.org/abs/2605.01533)]
- [2026] **SmellDoc: Extending Elastic Stack for Microservice Bad Smell Detection and Visualization** [[paper](https://arxiv.org/abs/2605.24471)]
- [2026] **Can Graph-Based Microservice Performance Detection Be Used for Microservice Intrusion Detection?** [[paper](https://arxiv.org/abs/2605.24283)]
- [2026] **Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis** [[paper](https://arxiv.org/abs/2605.15569)]
- [2026] **Towards In-Depth Root Cause Localization for Microservices with Multi-Agent Recursion-of-Thought** [[paper](https://arxiv.org/abs/2605.14866)]
- [2026] **Making OpenAPI Documentation Agent-Ready: Detecting Documentation and REST Smells with a Multi-Agent LLM System** [[paper](https://arxiv.org/abs/2605.14312)]
- [2026] **LLM-Based Robustness Testing of Microservice Applications: An Empirical Study** [[paper](https://arxiv.org/abs/2605.14202)]
- [2026] **E2E-REME: Towards End-to-End Microservices Auto-Remediation via Experience-Simulation Reinforcement Fine-Tuning** [[paper](https://arxiv.org/abs/2604.11094)]
- [2026] **Gamifying Architectural Governance to Reduce Organizational Coupling in Microservice Systems** [[paper](https://arxiv.org/abs/2604.22454)]
- [2026] **Key Developer Roles and Organizational Coupling in Microservices: A Longitudinal Analysis** [[paper](https://arxiv.org/abs/2604.25804)]
- [2026] **Which Types of Heterogeneity Matter for Root Cause Localization in Microservice Systems ?** [[paper](https://arxiv.org/abs/2604.26670)]
- [2026] **TORAI: Multi-source Root Cause Analysis for Blind Spots in Microservice Service Call Graph** [[paper](https://arxiv.org/abs/2604.13522)]
- [2026] **MIRAGE: Online LLM Simulation for Microservice Dependency Testing** [[paper](https://arxiv.org/abs/2604.04806)]
- [2026] **Log-based, Business-aware REST API Testing** [[paper](https://arxiv.org/abs/2604.08007)]
- [2026] **Rebooting Microreboot: Architectural Support for Safe, Parallel Recovery in Microservice Systems** [[paper](https://arxiv.org/abs/2604.09963)]
- [2026] **More Is Different: Toward a Theory of Emergence in AI-Native Software Ecosystems** [[paper](https://arxiv.org/abs/2604.19827)]
- [2026] **Can AI Agents Generate Microservices? How Far are We?** [[paper](https://arxiv.org/abs/2603.09004)]
- [2026] **Fuzzing Microservices in Face of Intrinsic Uncertainties** [[paper](https://arxiv.org/abs/2603.02551)]
- [2026] **Microservice Architecture Patterns for Scalable Machine Learning Systems** [[paper](https://arxiv.org/abs/2603.13672)]
- [2026] **An Empirical Study on How Architectural Topology Affects Microservice Performance and Energy Usage** [[paper](https://arxiv.org/abs/2604.00080)]
- [2026] **Q-GARS: Quantum-inspired Robust Microservice Chaining Scheduling** [[paper](https://arxiv.org/abs/2603.23127)]
- [2026] **Can an LLM Detect Instances of Microservice Infrastructure Patterns?** [[paper](https://arxiv.org/abs/2603.23073)]
- [2026] **Configurable Runtime Orchestration for Dynamic Data Retrieval in Distributed Systems** [[paper](https://arxiv.org/abs/2603.06980)]
- [2026] **Invariant-Driven Automated Testing** [[paper](https://arxiv.org/abs/2602.23922)]
- [2026] **Performance Antipatterns: Angel or Devil for Power Consumption?** [[paper](https://arxiv.org/abs/2602.12079)]
- [2026] **ModARO: A Modular Approach to Architecture Reconstruction of Distributed Microservice Codebases** [[paper](https://arxiv.org/abs/2602.08181)]
- [2026] **Cast: Automated Resilience Testing for Production Cloud Service Systems** [[paper](https://arxiv.org/abs/2602.00972)]
- [2026] **A Microservice-Based Platform for Sustainable and Intelligent SLO Fulfilment and Service Management** [[paper](https://arxiv.org/abs/2602.12875)]
- [2026] **PPTAMη: Energy Aware CI/CD Pipeline for Container Based Applications** [[paper](https://arxiv.org/abs/2602.12081)]
- [2026] **Automated Multi-Source Debugging and Natural Language Error Explanation for Dashboard Applications** [[paper](https://arxiv.org/abs/2602.15362)]
- [2026] **From Monolith to Microservices: A Comparative Evaluation of Decomposition Frameworks** [[paper](https://arxiv.org/abs/2601.23141)]
- [2026] **Hypothesize-Then-Verify: Speculative Root Cause Analysis for Microservices with Pathwise Parallelism** [[paper](https://arxiv.org/abs/2601.02736)]
- [2026] **FastFI: Enhancing API Call-Site Robustness in Microservice-Based Systems with Fault Injection** [[paper](https://arxiv.org/abs/2601.14800)]
- [2026] **RepoGenesis: Benchmarking End-to-End Microservice Generation from Readme to Repository** [[paper](https://arxiv.org/abs/2601.13943)] [[code](https://github.com/pzy2000/RepoGenesis)]
- [2026] **AnoMod: A Dataset for Anomaly Detection and Root Cause Analysis in Microservice Systems** [[paper](https://arxiv.org/abs/2601.22881)]
- [2026] **Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices** [[paper](https://arxiv.org/abs/2601.02732)]
- [2026] **LogicLens: Leveraging Semantic Code Graph to explore Multi Repository large systems** [[paper](https://arxiv.org/abs/2601.10773)]
- [2026] **AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems** [[paper](https://arxiv.org/abs/2601.09393)]
- [2026] **Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation** [[paper](https://arxiv.org/abs/2602.02584)]

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
- [2025] **FC-ADL: Efficient Microservice Anomaly Detection and Localisation Through Functional Connectivity** [[paper](https://arxiv.org/abs/2512.00844)]
- [2025] **MicroRemed: Benchmarking LLMs in Microservices Remediation** [[paper](https://arxiv.org/abs/2511.01166)] [[code](https://github.com/LLM4AIOps/MicroRemed)]
- [2025] **Microservices Are Dying, A New Method for Module Division Based on Universal Interfaces** [[paper](https://arxiv.org/abs/2511.04548)]
- [2025] **Root Cause Analysis for Microservice Systems via Cascaded Conditional Learning with Hypergraphs** [[paper](https://arxiv.org/abs/2511.17566)]
- [2025] **Offloading Data Center Tax** [[paper](https://arxiv.org/abs/2511.06558)]
- [2025] **Refactoring Towards Microservices: Preparing the Ground for Service Extraction** [[paper](https://arxiv.org/abs/2510.03050)]
- [2025] **DynaCausal: Dynamic Causality-Aware Root Cause Analysis for Distributed Microservices** [[paper](https://arxiv.org/abs/2510.22613)]
- [2025] **Key Considerations for Auto-Scaling: Lessons from Benchmark Microservices** [[paper](https://arxiv.org/abs/2510.02585)]
- [2025] **From Specification to Service: Accelerating API-First Development Using Multi-Agent Systems** [[paper](https://arxiv.org/abs/2510.19274)] [[code](https://github.com/sirbh/code-gen)]
- [2025] **SBOMproof: Beyond Alleged SBOM Compliance for Supply Chain Security of Container Images** [[paper](https://arxiv.org/abs/2510.05798)]
- [2025] **Trace Sampling 2.0: Code Knowledge Enhanced Span-level Sampling for Distributed Tracing** [[paper](https://arxiv.org/abs/2509.13852)]
- [2025] **Application Management in C-ITS: Orchestrating Demand-Driven Deployments and Reconfigurations** [[paper](https://arxiv.org/abs/2509.18793)] [[code](https://github.com/ika-rwth-aachen/application_manager)]
- [2025] **Componentization: Decomposing Monolithic LLM Responses into Manipulable Semantic Units** [[paper](https://arxiv.org/abs/2509.08203)]
- [2025] **Adaptive Root Cause Localization for Microservice Systems with Multi-Agent Recursion-of-Thought** [[paper](https://arxiv.org/abs/2508.20370)]

[⬆ Back to top](#paper-list)

### Programming Languages

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
- [2026] **When Types Intersect and Effects Get Handled** [[paper](https://arxiv.org/abs/2606.09526)]
- [2026] **Formal Semantics and Type System for Vega Data Transformations** [[paper](https://arxiv.org/abs/2606.15013)]
- [2026] **CANONIC: Governance Is Compilation** [[paper](https://arxiv.org/abs/2607.05410)]
- [2026] **Effect Systems as Abstract Interpretations** [[paper](https://arxiv.org/abs/2606.19686)]
- [2026] **A Typestate Approach to Purpose-aware Programming** [[paper](https://arxiv.org/abs/2606.26386)]
- [2026] **Same Coeffect, Different Base: Connecting Two Dominant Approaches to Graded Types** [[paper](https://arxiv.org/abs/2606.28042)]
- [2026] **Dynamic Software Updates using CRDTs** [[paper](https://arxiv.org/abs/2606.10920)]
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
- [2026] **Tracking Capabilities for Safer Agents** [[paper](https://arxiv.org/abs/2603.00991)]
- [2026] **Set-Theoretic Types for Erlang: Theory, Implementation, and Evaluation** [[paper](https://arxiv.org/abs/2603.22032)]
- [2026] **On Representability of Multiple-Valued Functions by Linear Lambda Terms Typed with Second-order Polymorphic Type System** [[paper](https://arxiv.org/abs/2603.25337)]
- [2026] **Towards verifying unsafe Rust programs against Rust's pointer-aliasing restrictions** [[paper](https://arxiv.org/abs/2603.28326)]
- [2026] **A Core Calculus for Type-safe Product Lines of C Programs** [[paper](https://arxiv.org/abs/2603.04013)]
- [2026] **Type-safe Monitoring of Parameterized Streams** [[paper](https://arxiv.org/abs/2603.11104)]
- [2026] **Dimensional Type Systems and Deterministic Memory Management: Design-Time Semantic Preservation in Native Compilation** [[paper](https://arxiv.org/abs/2603.16437)]
- [2026] **Decidable By Construction: Design-Time Verification for Trustworthy AI** [[paper](https://arxiv.org/abs/2603.25414)]
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
- [2026] **Dependently-Typed AARA: A Non-Affine Approach for Resource Analysis of Higher-Order Programs** [[paper](https://arxiv.org/abs/2601.12943)]
- [2026] **Formalization and Implementation of Safe Destination Passing in Pure Functional Programming Settings** [[paper](https://arxiv.org/abs/2601.08529)]
- [2026] **Remarks on Algebraic Reconstruction of Types and Effects** [[paper](https://arxiv.org/abs/2601.15455)]
- [2026] **Handling Scope Checks (Extended Version)** [[paper](https://arxiv.org/abs/2601.18793)]
- [2026] **Contextual Metaprogramming for Session Types** [[paper](https://arxiv.org/abs/2601.15180)]

##### 2025

- [2025] **Belobog: Move Language Fuzzing Framework For Real-World Smart Contracts** [[paper](https://arxiv.org/abs/2512.02918)]
- [2025] **NVLang: Unified Static Typing for Actor-Based Concurrency on the BEAM** [[paper](https://arxiv.org/abs/2512.05224)]
- [2025] **Simple Modal Types for Functional Reactive Programming** [[paper](https://arxiv.org/abs/2512.09412)]
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
- [2025] **ILA: Correctness via Type Checking for Fully Homomorphic Encryption** [[paper](https://arxiv.org/abs/2509.11559)]
- [2025] **Quantum Simulation Programming via Typing** [[paper](https://arxiv.org/abs/2509.17343)]
- [2025] **Navigating the Python Type Jungle** [[paper](https://arxiv.org/abs/2509.13022)]
- [2025] **A Verified Compiler for Quantum Simulation** [[paper](https://arxiv.org/abs/2509.18583)]
- [2025] **Code Less to Code More: Streamlining Language Server Protocol and Type System Development for Language Families** [[paper](https://arxiv.org/abs/2509.15150)]
- [2025] **Pacing Types: Safe Monitoring of Asynchronous Streams** [[paper](https://arxiv.org/abs/2509.06724)]
- [2025] **Committing to the bit: Relational programming with semiring arrays and SAT solving** [[paper](https://arxiv.org/abs/2509.22614)]
- [2025] **Type-Based Incorrectness Reasoning** [[paper](https://arxiv.org/abs/2509.01511)]
- [2025] **When Lifetimes Liberate: A Type System for Arenas with Higher-Order Reachability Tracking** [[paper](https://arxiv.org/abs/2509.04253)]

##### 2013

- [2013] **A Tour of C++: Type Safety and Resource Management** *Communications of the ACM* [[paper](https://doi.org/10.1145/2504585.2504603)]

[⬆ Back to top](#paper-list)

### Human Factors & DX

#### Evaluation

##### 2026

- [2026] **Mobile App Rewrites via Dual Boot** [[paper](https://arxiv.org/abs/2608.15135)]
- [2026] **Detecting Behavioral Changes in Python Refactoring Implementations with Foundation Models** [[paper](https://arxiv.org/abs/2608.09919)]
- [2026] **Unreliable in Practice? A Comprehensive Study of Errors in LLM-Generated Code** [[paper](https://arxiv.org/abs/2608.00661)]
- [2026] **SynH-Rank: Quality-Aware Code Search via Diverse Data Synthesis and Hierarchical Ranking Training** [[paper](https://arxiv.org/abs/2607.17139)]
- [2026] **Three-Phase Evaluation of AI-Assisted Software Development Life Cycle** [[paper](https://arxiv.org/abs/2607.05125)]
- [2026] **Lost in the Flow with Code Talkers: Unveiling the Instruction-Tuning Tax of Large Language Models in Code Tasks** [[paper](https://arxiv.org/abs/2606.08676)]
- [2026] **A meta-analysis of the effect of generative AI on productivity and learning in programming** [[paper](https://arxiv.org/abs/2605.04779)]
- [2026] **Minimal Prompt Perturbations Lead to Code Vulnerabilities: Prompt Fragility and Hidden-State Signals in Coding LLMs** [[paper](https://arxiv.org/abs/2605.29737)]
- [2026] **EngThrive: Make It Fast and Easy to Do Great Work** [[paper](https://arxiv.org/abs/2605.04259)]
- [2026] **JEDI: Java Evaluation of Declarative and Imperative Queries** [[paper](https://arxiv.org/abs/2605.23543)]
- [2026] **AI Observability for Developer Productivity Tools: Bridging Cost Awareness and Code Quality** [[paper](https://arxiv.org/abs/2604.17092)]
- [2026] **EcoAssist: Embedding Sustainability into AI-Assisted Frontend Development** [[paper](https://arxiv.org/abs/2604.04332)]
- [2026] **Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision** [[paper](https://arxiv.org/abs/2604.06723)]
- [2026] **CLARC: C/C++ Benchmark for Robust Code Search** [[paper](https://arxiv.org/abs/2603.04484)] [[project](https://huggingface.co/datasets/ClarcTeam/CLARC)]
- [2026] **Safer Builders, Risky Maintainers: A Comparative Study of Breaking Changes in Human vs Agentic PRs** [[paper](https://arxiv.org/abs/2603.27524)]
- [2026] **Sustainable Code Generation Using Large Language Models: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2603.00989)]
- [2026] **Automating Detection and Root-Cause Analysis of Flaky Tests in Quantum Software** [[paper](https://arxiv.org/abs/2603.09029)]
- [2026] **Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants** [[paper](https://arxiv.org/abs/2602.03593)]
- [2026] **From Ad-Hoc Scripts to Orchestrated Pipelines: Architecting a Resilient ELT Framework for Developer Productivity Metrics** [[paper](https://arxiv.org/abs/2602.21568)]
- [2026] **AIDev: Studying AI Coding Agents on GitHub** [[paper](https://arxiv.org/abs/2602.09185)]
- [2026] **EditFlow: Benchmarking and Optimizing Code Edit Recommendation Systems via Reconstruction of Developer Flows** [[paper](https://arxiv.org/abs/2602.21697)]
- [2026] **Impacts of Generative AI on Agile Teams' Productivity: A Multi-Case Longitudinal Study** [[paper](https://arxiv.org/abs/2602.13766)]
- [2026] **CodeMEM: AST-Guided Adaptive Memory for Repository-Level Iterative Code Generation** [[paper](https://arxiv.org/abs/2601.02868)]
- [2026] **The Promise and Reality of Continuous Integration Caching: An Empirical Study of Travis CI Builds** [[paper](https://arxiv.org/abs/2601.19146)]

##### 2025

- [2025] **Empowering smart app development with SolidGPT: an edge-cloud hybrid AI agent framework** [[paper](https://arxiv.org/abs/2512.08286)]
- [2025] **Understanding Privacy Risks in Code Models Through Training Dynamics: A Causal Approach** [[paper](https://arxiv.org/abs/2512.07814)]
- [2025] **CFCEval: Evaluating Security Aspects in Code Generated by Large Language Models** [[paper](https://arxiv.org/abs/2512.06248)]
- [2025] **Software Vulnerability Management in the Era of Artificial Intelligence: An Industry Perspective** [[paper](https://arxiv.org/abs/2512.18261)]
- [2025] **Studying the Role of Reusing Crowdsourcing Knowledge in Software Development** [[paper](https://arxiv.org/abs/2512.07824)]
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
- [2026] **A Benchmarking Framework for Multimodal User Interface Toolkits: Comparing Modality Coverage, Developer Workflow, and Experimental Support** [[paper](https://arxiv.org/abs/2606.02977)]
- [2026] **Writing Better Software Explanations: A Guideline-Based Approach** [[paper](https://arxiv.org/abs/2606.10880)]
- [2026] **The Impact of AI Coding Assistants on Software Engineering: A Longitudinal Study** [[paper](https://arxiv.org/abs/2605.23135)]
- [2026] **From Chat to Interview: Agentic Requirements Elicitation with an Experience Ontology** [[paper](https://arxiv.org/abs/2605.05828)]
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

##### 2025

- [2025] **Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases** [[paper](https://arxiv.org/abs/2512.10398)]
- [2025] **Selecting Cybersecurity Requirements: Effects of LLM Use and Professional Software Development Experience** [[paper](https://arxiv.org/abs/2510.04274)]
- [2025] **Towards an Understanding of Developer Experience-Driven Transparency in Software Ecosystems** [[paper](https://arxiv.org/abs/2509.03848)]
- [2025] **Reading Between the Lines: Scalable User Feedback via Implicit Sentiment in Developer Prompts** [[paper](https://arxiv.org/abs/2509.18361)]
- [2025] **What Were You Thinking? An LLM-Driven Large-Scale Study of Refactoring Motivations in Open-Source Projects** [[paper](https://arxiv.org/abs/2509.07763)]
- [2025] **Good Vibrations? A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding** [[paper](https://arxiv.org/abs/2509.12491)]

##### 2023

- [2023] **Measuring Developer Productivity: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2306.00001)]

[⬆ Back to top](#paper-list)

### AI for Software Engineering

#### Method

##### 2026

- [2026] **Entropy-based Code Adversarial Translation for Real-world Repository Migration** [[paper](https://arxiv.org/abs/2608.09273)]
- [2026] **Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency** [[paper](https://arxiv.org/abs/2608.14065)]
- [2026] **Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation** [[paper](https://arxiv.org/abs/2607.26244)]
- [2026] **AgenticRepair: Multi-Faceted Program Context Engineering for Agentic Vulnerability Repair** [[paper](https://arxiv.org/abs/2607.29422)]
- [2026] **MultiFixer: A Coordinator-Proposer Based Multi-Agent Framework For Fixing Multi-Hunk Bugs** [[paper](https://arxiv.org/abs/2607.26591)]
- [2026] **How Do LLMs Read Bug Reports? An Empirical Study of Attention in LLMs for Automated Program Repair** [[paper](https://arxiv.org/abs/2607.25873)]
- [2026] **VisualRepair: Dynamic Tool Calling and Region Focusing for Visual Software Issue Repair** [[paper](https://arxiv.org/abs/2607.14075)]
- [2026] **Multi-Perspective Agentic Program Repair via Code Property Graphs and Temporal Execution Graphs** [[paper](https://arxiv.org/abs/2607.12605)]
- [2026] **Bug Report Specification Refinement with Trajectory Guidance for Automated Program Repair** [[paper](https://arxiv.org/abs/2607.07882)]
- [2026] **What Makes a Good Bug Report for an AI Agent?** [[paper](https://arxiv.org/abs/2607.07593)]
- [2026] **Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes** [[paper](https://arxiv.org/abs/2607.19843)]
- [2026] **SkelDPO: A Skeleton-Guided Direct Preference Optimization Framework for Efficient Code Generation** [[paper](https://arxiv.org/abs/2606.06826)] [[code](https://github.com/icpcSkelDPO/SkelDPO)]
- [2026] **Automated Repair of Requirements for Cyber-Physical Systems in Simulink Requirements Tables** [[paper](https://arxiv.org/abs/2606.03870)]
- [2026] **PracRepair: LLM-Empowered Automated Program Repair Inspired by Human-Like Debugging Practices** [[paper](https://arxiv.org/abs/2606.17612)]
- [2026] **TraceView: Interactive Visualization of Agentic Program Repair Trajectories** [[paper](https://arxiv.org/abs/2606.22110)] [[code](https://github.com/SOAR-Lab/agent-traj-visualization)]
- [2026] **Smaller Models, Unexpected Costs: Trade-offs in LLM Quantization for Automated Program Repair** [[paper](https://arxiv.org/abs/2606.27205)]
- [2026] **A11YRepair: Bridging Web Accessibility Barriers via Knowledge-Enhanced Divide-and-Conquer Repair** [[paper](https://arxiv.org/abs/2606.21926)]
- [2026] **How Generation Architecture Shapes Code Complexity in Multi-Agent LLM Systems: A Paired Study on HumanEval** [[paper](https://arxiv.org/abs/2606.00308)]
- [2026] **HEJ-Robust: A Robustness Benchmark for LLM-Based Automated Program Repair** [[paper](https://arxiv.org/abs/2605.02215)]
- [2026] **EviACT: An Evidence-to-Action Framework for Agentic Program Repair** [[paper](https://arxiv.org/abs/2605.27238)]
- [2026] **SiblingRepair: Sibling-Based Multi-Hunk Repair with Large Language Models** [[paper](https://arxiv.org/abs/2605.06209)]
- [2026] **Characterizing the Failure Modes of LLMs in Resolving Real-World GitHub Issues** [[paper](https://arxiv.org/abs/2605.12270)]
- [2026] **BLAgent: Agentic RAG for File-Level Bug Localization** [[paper](https://arxiv.org/abs/2605.17965)]
- [2026] **ARISE: A Repository-level Graph Representation and Toolset for Agentic Program Repair and Fault Localization** [[paper](https://arxiv.org/abs/2605.03117)]
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
- [2026] **FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair** [[paper](https://arxiv.org/abs/2603.17826)]
- [2026] **RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair** [[paper](https://arxiv.org/abs/2603.01048)]
- [2026] **Beyond Localization: Recoverable Headroom and Residual Frontier in Repository-Level RAG-APR** [[paper](https://arxiv.org/abs/2603.29067)]
- [2026] **On the Use of Commit Messages for Corrective Software Maintenance: A Systematic Mapping Study** [[paper](https://arxiv.org/abs/2604.16404)]
- [2026] **On the Effectiveness of Code Representation in Deep Learning-Based Automated Patch Correctness Assessment** [[paper](https://arxiv.org/abs/2603.07520)]
- [2026] **Unveiling Practical Shortcomings of Patch Overfitting Detection Techniques** [[paper](https://arxiv.org/abs/2603.11262)]
- [2026] **What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair** [[paper](https://arxiv.org/abs/2602.04449)]
- [2026] **Historian: Reducing Manual Validation in APR Benchmarking via Evidence-Based Assessment** [[paper](https://arxiv.org/abs/2603.00649)]
- [2026] **SVRepair: Structured Visual Reasoning for Automated Program Repair** [[paper](https://arxiv.org/abs/2602.06090)] [[code](https://github.com/codefuse-ai/CodeFuse-SVR)]
- [2026] **Specification Vibing for Automated Program Repair** [[paper](https://arxiv.org/abs/2602.08263)]
- [2026] **ComPass: Contrastive Learning for Automated Patch Correctness Assessment in Program Repair** [[paper](https://arxiv.org/abs/2602.07561)]
- [2026] **AgenticSZZ: Temporal Knowledge Graph-Guided Agentic Bug-Inducing Commit Identification** [[paper](https://arxiv.org/abs/2602.02934)]
- [2026] **AlignCoder: Aligning Retrieval with Target Intent for Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2601.19697)]
- [2026] **Monte Carlo Tree Search for Execution-Guided Program Repair with Large Language Models** [[paper](https://arxiv.org/abs/2602.00129)]
- [2026] **From Historical Patches to Repair Plans: Outcome-Conditioned Reasoning for Repository-Level Program Repair** [[paper](https://arxiv.org/abs/2601.23257)]
- [2026] **Leveraging Mutation Analysis for LLM-based Repair of Quantum Programs** [[paper](https://arxiv.org/abs/2601.12273)]
- [2026] **Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair** [[paper](https://arxiv.org/abs/2601.19066)]
- [2026] **RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models** [[paper](https://arxiv.org/abs/2601.18044)]

##### 2025

- [2025] **Syntax Is Not Enough: An Empirical Study of Small Transformer Models for Neural Code Repair** [[paper](https://arxiv.org/abs/2512.22216)]
- [2025] **CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models** [[paper](https://arxiv.org/abs/2512.09957)]
- [2025] **DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information** [[paper](https://arxiv.org/abs/2512.24635)]
- [2025] **Analysis of AdvFusion: Adapter-based Multilingual Learning for Code Large Language Models** [[paper](https://arxiv.org/abs/2511.02869)]
- [2025] **Rethinking Kernel Program Repair: Benchmarking and Enhancing LLMs with RGym** [[paper](https://arxiv.org/abs/2511.15757)]
- [2025] **Towards a Human-in-the-Loop Framework for Reliable Patch Evaluation Using an LLM-as-a-Judge** [[paper](https://arxiv.org/abs/2511.10865)]
- [2025] **HAFixAgent: History-Aware Program Repair Agent** [[paper](https://arxiv.org/abs/2511.01047)]
- [2025] **Collaborative Agents for Automated Program Repair in Ruby** [[paper](https://arxiv.org/abs/2511.03925)]
- [2025] **Enhancing Automated Program Repair via Faulty Token Localization and Quality-Aware Patch Refinement** [[paper](https://arxiv.org/abs/2511.18001)]
- [2025] **Beyond Accuracy: Behavioral Dynamics of Agentic Multi-Hunk Repair** [[paper](https://arxiv.org/abs/2511.11012)]
- [2025] **Automated Program Repair of Uncompilable Student Code** [[paper](https://arxiv.org/abs/2510.06187)]
- [2025] **SIADAFIX: issue description response for adaptive program repair** [[paper](https://arxiv.org/abs/2510.16059)] [[code](https://github.com/liauto-siada/siada-cli)]
- [2025] **Automated Repair of OpenID Connect Programs (Extended Version)** [[paper](https://arxiv.org/abs/2510.02773)]
- [2025] **Defects4C: Benchmarking Large Language Model Repair Capability with C/C++ Bugs** [[paper](https://arxiv.org/abs/2510.11059)]
- [2025] **Abstain and Validate: A Dual-LLM Policy for Reducing Noise in Agentic Program Repair** [[paper](https://arxiv.org/abs/2510.03217)]
- [2025] **PathFix: Automated Program Repair with Expected Path** [[paper](https://arxiv.org/abs/2510.14341)]
- [2025] **Nexus: Execution-Grounded Multi-Agent Test Oracle Synthesis** [[paper](https://arxiv.org/abs/2510.26423)]
- [2025] **CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion** [[paper](https://arxiv.org/abs/2509.16112)] [[code](https://github.com/KDEGroup/CodeRAG)]
- [2025] **Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models** [[paper](https://arxiv.org/abs/2509.11686)]
- [2025] **RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** [[paper](https://arxiv.org/abs/2509.16701)]
- [2025] **Designing for Novice Debuggers: A Pilot Study on an AI-Assisted Debugging Tool** [[paper](https://arxiv.org/abs/2509.21067)]
- [2025] **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** [[paper](https://arxiv.org/abs/2509.02330)]
- [2025] **BloomAPR: A Bloom's Taxonomy-based Framework for Assessing the Capabilities of LLM-Powered APR Solutions** [[paper](https://arxiv.org/abs/2509.25465)]
- [2025] **Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair** [[paper](https://arxiv.org/abs/2509.05372)]
- [2025] **Red Teaming Program Repair Agents: When Correct Patches can Hide Vulnerabilities** [[paper](https://arxiv.org/abs/2509.25894)]

##### 2023

- [2023] **Automated Program Repair via Conversational Large Language Models** [[paper](https://arxiv.org/abs/2301.00001)]

[⬆ Back to top](#paper-list)

#### Evaluation

##### 2026

- [2026] **Programmers Are Poor and Overconfident Judges of LLM-Generated Assertions** [[paper](https://arxiv.org/abs/2607.08885)]
- [2026] **The Substrate Collapse: AI Code Generation Invalidates Authorship-Based Knowledge Metrics** [[paper](https://arxiv.org/abs/2606.20882)]
- [2026] **From Prompting to Verification: How Experience Shapes Vibe Coding Practices** [[paper](https://arxiv.org/abs/2605.24521)]
- [2026] **StatsClaw: An AI-Collaborative Workflow for Statistical Software Development** [[paper](https://arxiv.org/abs/2604.04871)]
- [2026] **BONSAI: A Mixed-Initiative Workspace for Human-AI Co-Development of Visual Analytics Applications** [[paper](https://arxiv.org/abs/2604.19247)]
- [2026] **Co-Located Tests, Better AI Code: How Test Syntax Structure Affects Foundation Model Code Generation** [[paper](https://arxiv.org/abs/2604.19826)]

##### 2025

- [2025] **A Survey of Bugs in AI-Generated Code** [[paper](https://arxiv.org/abs/2512.05239)]
- [2025] **Cracking CodeWhisperer: Analyzing Developers' Interactions and Patterns During Programming Tasks** [[paper](https://arxiv.org/abs/2510.11516)]
- [2025] **Vibe Coding in Practice: Motivations, Challenges, and a Future Outlook -- a Grey Literature Review** [[paper](https://arxiv.org/abs/2510.00328)]
- [2025] **A.S.E: A Repository-Level Benchmark for Evaluating Security in AI-Generated Code** [[paper](https://arxiv.org/abs/2508.18106)]

[⬆ Back to top](#paper-list)

#### Survey

##### 2024

- [2024] **Large Language Models for Software Engineering: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2403.00001)]

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
- [2026] **To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks** [[paper](https://arxiv.org/abs/2606.30549)]
- [2026] **A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets** *ICML 2026. Code and benchmark* [[paper](https://arxiv.org/abs/2606.13802)]
- [2026] **The Illusion of Agentic Complexity in README.md Generation: Evaluating Single-Agent vs. Multi-Agent RAG Systems** [[paper](https://arxiv.org/abs/2606.30524)]
- [2026] **JAMER: Project-Level Code Framework Dataset and Benchmark on Professional Game Engines** [[paper](https://arxiv.org/abs/2606.19830)]
- [2026] **How Does Chunking Affect Retrieval-Augmented Code Completion? A Controlled Empirical Study** [[paper](https://arxiv.org/abs/2605.04763)]
- [2026] **SynConfRoute: Syntax-Aware Routing for Efficient Code Completion with Small CodeLLMs** [[paper](https://arxiv.org/abs/2605.04894)]
- [2026] **Specification-Driven Development Benchmark: Security Knowledge Transition** [[paper](https://arxiv.org/abs/2606.00167)]
- [2026] **Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets** [[paper](https://arxiv.org/abs/2605.28510)]
- [2026] **On the Effectiveness of Context Compression for Repository-Level Tasks: An Empirical Investigation** [[paper](https://arxiv.org/abs/2604.13725)]
- [2026] **Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?** [[paper](https://arxiv.org/abs/2604.17338)]
- [2026] **Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy** [[paper](https://arxiv.org/abs/2604.17182)]
- [2026] **Babbling Suppression: Making LLMs Greener One Token at a Time** [[paper](https://arxiv.org/abs/2604.06755)]
- [2026] **Sema Code: Decoupling AI Coding Agents into Programmable, Embeddable Infrastructure** [[paper](https://arxiv.org/abs/2604.11045)]
- [2026] **Balancing Latency and Accuracy of Code Completion via Local-Cloud Model Cascading** [[paper](https://arxiv.org/abs/2603.05974)]
- [2026] **A framework for assessing the capabilities of code generation of constraint domain-specific languages with large language models** [[paper](https://arxiv.org/abs/2603.05278)]
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

##### 2025

- [2025] **Completion by Comprehension: Guiding Code Generation with Multi-Granularity Understanding** [[paper](https://arxiv.org/abs/2512.04538)]
- [2025] **Inside Out: Uncovering How Comment Internalization Steers LLMs for Better or Worse** [[paper](https://arxiv.org/abs/2512.16790)]
- [2025] **DUET: Agentic Design Understanding via Experimentation and Testing** [[paper](https://arxiv.org/abs/2512.06247)]
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
- [2025] **Bridging Developer Instructions and Code Completion Through Instruction-Aware Fill-in-the-Middle Paradigm** [[paper](https://arxiv.org/abs/2509.24637)]
- [2025] **RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval** [[paper](https://arxiv.org/abs/2509.25257)]
- [2025] **GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion** [[paper](https://arxiv.org/abs/2509.05980)]
- [2025] **Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs** [[paper](https://arxiv.org/abs/2509.25873)]
- [2025] **Enhancing Python Programming Education with an AI-Powered Code Helper: Design, Implementation, and Impact** [[paper](https://arxiv.org/abs/2509.20518)]

[⬆ Back to top](#paper-list)

### Security & Supply Chain

#### Method

##### 2026

- [2026] **Cross-Corpus Evaluation of Generalizable Vulnerability Detection in IoT Firmware** [[paper](https://arxiv.org/abs/2608.11492)]
- [2026] **VICBench: A Multi-Language Benchmark for Code Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.12246)]
- [2026] **CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection** [[paper](https://arxiv.org/abs/2608.03134)]
- [2026] **Vulnerability Detection in AArch64 Machine Code Using a Digital Twin** [[paper](https://arxiv.org/abs/2608.02125)]
- [2026] **Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking** [[paper](https://arxiv.org/abs/2608.14533)]
- [2026] **DREA: Decoupled Reasoning and Exploration Agents for Repository-Level Vulnerability Detection** [[paper](https://arxiv.org/abs/2607.13439)]
- [2026] **RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities** [[paper](https://arxiv.org/abs/2607.04729)]
- [2026] **Why Not Fix It Once and for All? An Empirical Study of Multiple Patches for Vulnerability Fixes in Open-Source Software** [[paper](https://arxiv.org/abs/2607.13206)]
- [2026] **JavaVulBench: A Java Vulnerability Benchmark with Realistic Splits, a Unified Multi-Backend Harness, and a Leakage-Aware Evaluation Mode** [[paper](https://arxiv.org/abs/2607.02825)]
- [2026] **VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents** [[paper](https://arxiv.org/abs/2607.09653)]
- [2026] **Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing** [[paper](https://arxiv.org/abs/2607.21983)]
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
- [2026] **DCVD: Dual-Channel Cross-Modal Fusion for Joint Vulnerability Detection and Localization** [[paper](https://arxiv.org/abs/2605.11015)] [[code](https://github.com/vinsontang1/DCVD)]
- [2026] **Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerability Detection** [[paper](https://arxiv.org/abs/2605.29901)]
- [2026] **Tailored Prompts, Targeted Protection: Vulnerability-Specific LLM Analysis for Smart Contracts** [[paper](https://arxiv.org/abs/2605.03697)]
- [2026] **Smart Contract Security Beyond Detection** [[paper](https://arxiv.org/abs/2605.09124)]
- [2026] **MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection** [[paper](https://arxiv.org/abs/2605.10240)]
- [2026] **AgenticVM: Agentic AI for Adaptive Software Vulnerability Management** [[paper](https://arxiv.org/abs/2605.01739)]
- [2026] **FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction** [[paper](https://arxiv.org/abs/2605.21779)]
- [2026] **A Ground-Truth-Based Evaluation of Vulnerability Detection Across Multiple Ecosystems** [[paper](https://arxiv.org/abs/2604.21111)]
- [2026] **SAGE: Signal-Amplified Guided Embeddings for LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.19031)]
- [2026] **Seclens: Role-specific Evaluation of LLM's for security vulnerablity detection** [[paper](https://arxiv.org/abs/2604.01637)]
- [2026] **VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.26313)]
- [2026] **Security Is Relative: Training-Free Vulnerability Detection via Multi-Agent Behavioral Contract Synthesis** [[paper](https://arxiv.org/abs/2604.19012)]
- [2026] **Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection** [[paper](https://arxiv.org/abs/2604.06633)]
- [2026] **CrossCommitVuln-Bench: A Dataset of Multi-Commit Python Vulnerabilities Invisible to Per-Commit Static Analysis** [[paper](https://arxiv.org/abs/2604.21917)]
- [2026] **MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification** [[paper](https://arxiv.org/abs/2604.24398)]
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
- [2026] **Persistent Human Feedback, LLMs, and Static Analyzers for Secure Code Generation and Vulnerability Detection** [[paper](https://arxiv.org/abs/2602.05868)]
- [2026] **Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection** [[paper](https://arxiv.org/abs/2602.06751)]
- [2026] **SecCodePRM: A Process Reward Model for Code Security** [[paper](https://arxiv.org/abs/2602.10418)]
- [2026] **Enhancing Continual Learning for Software Vulnerability Prediction: Addressing Catastrophic Forgetting via Hybrid-Confidence-Aware Selective Replay for Temporal LLM Fine-Tuning** [[paper](https://arxiv.org/abs/2602.23834)]
- [2026] **Toward Quantum-Safe Software Engineering: A Vision for Post-Quantum Cryptography Migration** [[paper](https://arxiv.org/abs/2602.05759)]
- [2026] **VulReaD: Knowledge-Graph-guided Software Vulnerability Reasoning and Detection** [[paper](https://arxiv.org/abs/2602.10787)]
- [2026] **Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents** [[paper](https://arxiv.org/abs/2602.02164)]
- [2026] **Secure Code Generation via Online Reinforcement Learning with Vulnerability Reward Model** [[paper](https://arxiv.org/abs/2602.07422)] [[code](https://github.com/AndrewWTY/SecCoderX)]
- [2026] **Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities** [[paper](https://arxiv.org/abs/2601.06914)]
- [2026] **Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code** [[paper](https://arxiv.org/abs/2601.09157)]
- [2026] **Multi-Agent Taint Specification Extraction for Vulnerability Detection** [[paper](https://arxiv.org/abs/2601.10865)]
- [2026] **Zer0n: An AI-Assisted Vulnerability Discovery and Blockchain-Backed Integrity Framework** [[paper](https://arxiv.org/abs/2601.07019)]
- [2026] **Examining the Effectiveness of Transformer-Based Smart Contract Vulnerability Scan** [[paper](https://arxiv.org/abs/2601.07334)]
- [2026] **HogVul: Black-box Adversarial Code Generation Framework Against LM-based Vulnerability Detectors** [[paper](https://arxiv.org/abs/2601.05587)]
- [2026] **LAsset: An LLM-assisted Security Asset Identification Framework for System-on-Chip (SoC) Verification** [[paper](https://arxiv.org/abs/2601.02624)]
- [2026] **AutoVulnPHP: LLM-Powered Two-Stage PHP Vulnerability Detection and Automated Localization** [[paper](https://arxiv.org/abs/2601.06177)]

##### 2025

- [2025] **Large Language Models Cannot Reliably Detect Vulnerabilities in JavaScript: The First Systematic Benchmark and Evaluation** [[paper](https://arxiv.org/abs/2512.01255)]
- [2025] **SHERLOCK: A Deep Learning Approach To Detect Software Vulnerabilities** [[paper](https://arxiv.org/abs/2512.12593)]
- [2025] **A Systematic Study of Code Obfuscation Against LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.16538)]
- [2025] **VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.07533)] [[code](https://github.com/ucsb-mlsec/VulnLLM-R)]
- [2025] **SoK: Understanding (New) Security Issues Across AI4Code Use Cases** [[paper](https://arxiv.org/abs/2512.18456)]
- [2025] **Beyond Single Bugs: Benchmarking Large Language Models for Multi-Vulnerability Detection** [[paper](https://arxiv.org/abs/2512.22306)]
- [2025] **Llama-based source code vulnerability detection: Prompt engineering vs Fine tuning** [[paper](https://arxiv.org/abs/2512.09006)] [[code](https://github.com/DynaSoumhaneOuchebara/Llama-based-vulnerability-detection)]
- [2025] **A Large Scale Study of AI-based Binary Function Similarity Detection Techniques for Security Researchers and Practitioners** [[paper](https://arxiv.org/abs/2511.01180)]
- [2025] **LLMs as Firmware Experts: A Runtime-Grown Tree-of-Agents Framework** [[paper](https://arxiv.org/abs/2511.18438)]
- [2025] **Large Language Model based Smart Contract Auditing with LLMBugScanner** [[paper](https://arxiv.org/abs/2512.02069)]
- [2025] **UniBOM -- A Unified SBOM Analysis and Visualisation Tool for IoT Systems and Beyond** [[paper](https://arxiv.org/abs/2511.22359)]
- [2025] **VULPO: Context-Aware Vulnerability Detection via On-Policy LLM Optimization** [[paper](https://arxiv.org/abs/2511.11896)]
- [2025] **QuiLL: An LLM-Based Vulnerability Assessment Framework for the Wild** [[paper](https://arxiv.org/abs/2510.04056)]
- [2025] **ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.17919)]
- [2025] **NatGVD: Natural Adversarial Example Attack towards Graph-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.04987)]
- [2025] **Distilling Lightweight Language Models for C/C++ Vulnerabilities** [[paper](https://arxiv.org/abs/2510.06645)] [[code](https://github.com/yangxiaoxuan123/FineSec_detect)]
- [2025] **MulVuln: Enhancing Pre-trained LMs with Shared and Language-Specific Knowledge for Multilingual Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.04397)]
- [2025] **On the Difficulty of Selecting Few-Shot Examples for Effective LLM-based Vulnerability Detection** [[paper](https://arxiv.org/abs/2510.27675)]
- [2025] **Bridging Semantics &amp; Structure for Software Vulnerability Detection using Hybrid Network Models** [[paper](https://arxiv.org/abs/2510.10321)]
- [2025] **TaintSentinel: Path-Level Randomness Vulnerability Detection for Ethereum Smart Contracts** [[paper](https://arxiv.org/abs/2510.18192)]
- [2025] **POLAR: Automating Cyber Threat Prioritization through LLM-Powered Assessment** [[paper](https://arxiv.org/abs/2510.01552)]
- [2025] **HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities** [[paper](https://arxiv.org/abs/2510.12200)]
- [2025] **LISA Technical Report: An Agentic Framework for Smart Contract Auditing** [[paper](https://arxiv.org/abs/2509.24698)]
- [2025] **SoK: A Beginner-Friendly Introduction to Fault Injection Attacks** [[paper](https://arxiv.org/abs/2509.18341)]
- [2025] **LLM-Driven SAST-Genius: A Hybrid Static Analysis Framework for Comprehensive and Actionable Security** [[paper](https://arxiv.org/abs/2509.15433)]
- [2025] **All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching** [[paper](https://arxiv.org/abs/2509.07225)] [[code](https://github.com/o2lab/afc-crs-all-you-need-is-a-fuzzing-brain)] [[project](https://o2lab.github.io/FuzzingBrain-Leaderboard/)]
- [2025] **From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization** [[paper](https://arxiv.org/abs/2510.02389)]
- [2025] **FuzzRDUCC: Fuzzing with Reconstructed Def-Use Chain Coverage** [[paper](https://arxiv.org/abs/2509.04967)]
- [2025] **SecureBERT 2.0: Advanced Language Model for Cybersecurity Intelligence** [[paper](https://arxiv.org/abs/2510.00240)]
- [2025] **VULSOLVER: Vulnerability Detection via LLM-Driven Constraint Solving** [[paper](https://arxiv.org/abs/2509.00882)]
- [2025] **AVIATOR: Towards AI-Agentic Vulnerability Injection Workflow for High-Fidelity, Large-Scale Code Security Dataset** [[paper](https://arxiv.org/abs/2508.20866)]
- [2025] **Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias** [[paper](https://arxiv.org/abs/2508.17361)]

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
- [2026] **Trustworthy AI LLM Scalability Risk Index (LSRI): A Cybersecurity Framework Assessing Agentic-AI Security &amp; Software Model Supply Chain Safety Boosting AI-Generated Malware Defense &amp; Explainability Mitigating Emerging Risks of Generative AI** [[paper](https://arxiv.org/abs/2602.19021)]
- [2026] **VeriSBOM: Secure and Verifiable SBOM Sharing Via Zero-Knowledge Proofs** [[paper](https://arxiv.org/abs/2602.13682)]
- [2026] **Operationalizing Research Software for Supply Chain Security** [[paper](https://arxiv.org/abs/2601.20980)]
- [2026] **Unpacking Security Scanners for GitHub Actions Workflows** [[paper](https://arxiv.org/abs/2601.14455)]
- [2026] **Supply Chain Insecurity: Exposing Vulnerabilities in iOS Dependency Management Systems** [[paper](https://arxiv.org/abs/2601.20638)]
- [2026] **Deep Dive into the Abuse of DL APIs To Create Malicious AI Models and How to Detect Them** [[paper](https://arxiv.org/abs/2601.04553)]
- [2026] **AgentGuard: A Multi-Agent Framework for Robust Package Confusion Detection via Hybrid Search and Metadata-Content Fusion** [[paper](https://arxiv.org/abs/2604.16309)]
- [2026] **CHASE: LLM Agents for Dissecting Malicious PyPI Packages** [[paper](https://arxiv.org/abs/2601.06838)] [[project](https://t0d4.github.io/CHASE-AIware25/)]

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

##### 2024

- [2024] **Software Supply Chain Security: A Systematic Literature Review** [[paper](https://arxiv.org/abs/2401.00001)]

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
- [2026] **Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation** [[paper](https://arxiv.org/abs/2602.01187)]
- [2026] **Learning to Generate Secure Code via Token-Level Rewards** [[paper](https://arxiv.org/abs/2602.23407)]
- [2026] **LLMs + Security = Trouble** [[paper](https://arxiv.org/abs/2602.08422)]
- [2026] **SecCodeBench-V2 Technical Report** [[paper](https://arxiv.org/abs/2602.15485)] [[code](https://github.com/alibaba/sec-code-bench)] [[project](https://alibaba.github.io/sec-code-bench)]
- [2026] **How Secure is Secure Code Generation? Adversarial Prompts Put LLM Defenses to the Test** [[paper](https://arxiv.org/abs/2601.07084)]
- [2026] **RealSec-bench: A Benchmark for Evaluating Secure Code Generation in Real-World Repositories** [[paper](https://arxiv.org/abs/2601.22706)]

##### 2025

- [2025] **CVE Breadcrumbs: Tracking Vulnerabilities Through Versioned Apache Libraries** [[paper](https://arxiv.org/abs/2512.02259)]
- [2025] **Reflection-Driven Control for Trustworthy Code Agents** [[paper](https://arxiv.org/abs/2512.21354)]
- [2025] **Secure Code Generation at Scale with Reflexion** [[paper](https://arxiv.org/abs/2511.03898)]
- [2025] **Secure-Instruct: An Automated Pipeline for Synthesizing Instruction-Tuning Datasets Using LLMs for Secure Code Generation** [[paper](https://arxiv.org/abs/2510.07189)]
- [2025] **RESCUE: Retrieval Augmented Secure Code Generation** [[paper](https://arxiv.org/abs/2510.18204)] [[code](https://github.com/steven1518/RESCUE)]
- [2025] **Fortifying LLM-Based Code Generation with Graph-Based Reasoning on Secure Coding Practices** [[paper](https://arxiv.org/abs/2510.09682)]
- [2025] **RefleXGen:The unexamined code is not worth using** [[paper](https://arxiv.org/abs/2510.23674)]
- [2025] **SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios** [[paper](https://arxiv.org/abs/2509.22097)] [[code](https://github.com/iCSawyer/SecureVibeBench)]

[⬆ Back to top](#paper-list)

### Open Source

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
- [2026] **Exploring Sustainability in Scientific Software through Code Quality &amp; Test Coverage Metrics** [[paper](https://arxiv.org/abs/2605.03243)]
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
- [2025] **Match &amp; Mend: Minimally Invasive Local Reassembly for Patching N-day Vulnerabilities in ARM Binaries** [[paper](https://arxiv.org/abs/2510.14384)]
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
- [2025] **DocFetch - Towards Generating Software Documentation from Multiple Software Artifacts** [[paper](https://arxiv.org/abs/2508.17719)]

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
