[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19337545.svg)](https://doi.org/10.5281/zenodo.19337545)

# Ordinative Sciences Framework (TE)

Welcome to the official repository of the **Technology of Expressions (TE) Framework**, a universal architecture based on **Ordinative Set Theory (OST)**.

This repository provides an open-source operating philosophy and a complete set of analytical modules designed for Artificial Intelligences and human analysts. Where statistical frameworks measure probability, sentiment or consensus, the TE Framework evaluates systems by **Structural Coherence**, **Vectors of Identity** and **Emergent Function**.

Release 2.0.0 (2026-09-23): the framework corpus is published as one synchronised set under `FRAMEWORKS/`, and two domain frameworks with runtimes are added — **LEXX** (agreements) and **CASEWORK** (documentary audit and investigation support). See `CHANGELOG.md`.

## Part of a Larger Ecosystem

This repository is one piece of a four-part framework. For the complete picture, see:

| Repository | Purpose | What you'll find there |
| --- | --- | --- |
| **[ordinative_sciences_framework](https://github.com/anckhalion/ordinative_sciences_framework)** | **Theory** | The complete TE framework, core ontology, operational modules, and the domain frameworks LEXX and CASEWORK with their runtimes. |
| **[te-ordinative-lora](https://github.com/anckhalion/te-ordinative-lora)** | **Practice** | Code, datasets, and scripts to fine-tune an LLM into a TE-compliant ordinative agent. |
| **[te-oct-framework-en](https://github.com/anckhalion/te-oct-framework-en)** | **Validation** | English mirror of the core framework, plus OCT datasets and benchmarks. |
| **[te-ordinative-algebras-en](https://github.com/anckhalion/te-ordinative-algebras-en)** | **Algebras** | Semantic Algebra (SA) and Proportional Algebra (PA) — the analytical operators and the proportional space they live in. |

For a full map, see `ECOSYSTEM.md`.

## Why Does This Exist?

Current AI models and analytical methods are increasingly dominated by statistical truth, alignment through RLHF (which produces *compliance* and *attenuation* where truth is required), and the "Projective Void" phenomenon.

The TE Framework was designed to:
1. Provide an **Ontology of Coherence** where "Meaning Precedes Form" (Axiom 10).
2. Equip AIs with **Controfase**, a built-in anti-bias protocol that interrupts inertial generation, averts narrative capture, and forces a phase-shift to objective structural evaluation.
3. Systematically strip apart manipulative frameworks, political propaganda, and mythological constructions using precise ordinative lenses.

## Repository Structure

The framework is modular: a "Physical Law" layer (Core, OST, Symbol Canon), the always-active protocols, and external modules loaded on demand by the router according to the domain under analysis. All framework files live in one flat directory with their canonical names.

```text
ordinative_sciences_framework/
├── FRAMEWORKS/
│   ├── README.md                                   # loading order, integrity check, archive policy
│   ├── MANIFEST_SHA256.txt                         # hashes of every published framework file
│   ├── te_frameworks.lock.json                     # framework lock consumed by the CASEWORK runtime (built by make_lock.py)
│   ├── TE_BOOTLOADER_v7_1_1_EN.md                  # ⚙️ entry point: identity, principles, S₀–S₃, Φ-test, router
│   ├── TE_PROTOCOLS_v1_1_EN.md                     # 🛡️ always-active: Controfase, P-AI, Anti-Attractor-Lock
│   ├── TE_CORE_v5_2_1_EN.md                        # 🧠 the OS and foundational axioms for AI
│   ├── TE_OST_v2_1_EN.md                           # 📐 Ordinative Set Theory (Tier-0 foundation)
│   ├── TE_OST_Extension_Teleodynamics_v1_1_EN.md   # ⏳ Teleodynamics and Causal Inversion
│   ├── TE_SYMBOL_CANON_v1_0_EN.md                  # ✒️ notation authority (register 1.2)
│   ├── TE_MODULE_SVP_v5_1_EN.md                    # 🔎 Source Verification Protocol (MANDATORY GATE)
│   ├── TE_MODULE_LENS_v5_1_EN.md                   # 👥 integral human figure analysis
│   ├── TE_MODULE_VERI_v1_0_EN.md                   # ⚖️ functional impact verification (participants)
│   ├── TE_MODULE_PPRO_v5_2_EN.md                   # 🕸️ psycho-political pattern recognition
│   ├── TE_MODULE_SCIMS_v5_1_EN.md                  # 🌍 complex-system stress analysis
│   ├── TE_OBSERVER_v1_1_EN.md                      # 👁️ integrated observation, Lyapunov trajectories, CVI
│   ├── LEXX/                                       # 📜 ordinative validation of agreements (method 0.1, runtime 0.2.0-alpha.3)
│   │   ├── README.md · 00_FOUNDATIONS.md · TE_MODULE_LEXX_v0_1_EN.md
│   │   ├── 01_ANNOTATED_EXAMPLE.md · 02_COMPATIBILITY_PROFILE.md · 03_PRE_PILOT_PROTOCOL.md
│   │   ├── lexx_compatibility_profile_v0_1.json · release.json
│   │   └── v0_2_alpha3/                            # runtime: schema, validator, review request, tests
│   ├── CASEWORK/                                   # 🗂️ documentary audit and investigation support (method 0.1, runtime 0.1.0-alpha.1)
│   │   ├── README.md · PILOT_PLAN.md
│   │   ├── TE_CASEWORK_v0_1_EN.md · TE_AUDIT_v0_1_EN.md · TE_INVESTIGATION_v0_1_EN.md
│   │   ├── compatibility.json · release.json · requirements.txt
│   │   └── runtime/ · schemas/ · tests/            # case preparation, validation, lock builder, tests
│   └── ARCHIVE/                                    # superseded editions, reference only
├── docs/
│   └── ArXiv_Abstract_TE.md
└── papers/
    └── collapse_equation/
        ├── Ghioni_2026_The_Collapse_Equation_v1_2.pdf  # 📄 PDF (human reading)
        ├── Ghioni_2026_The_Collapse_Equation_v1_2.tex  # 📝 LaTeX source (Overleaf)
        └── Ghioni_2026_The_Collapse_Equation_v1_2.md   # 🤖 Markdown (AI parsing)
```

## Papers

### The Collapse Equation: Predicting Phase Transitions (v1.2 Beta)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19932312.svg)](https://doi.org/10.5281/zenodo.19932312) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The first empirical measurement of **g_j**, the ordinative acceleration constant — the universal measure of attractor signal intensity at a given scale. The paper introduces a reaction-diffusion model (Belousov-Zhabotinsky isomorphism) for civilizational phase transitions, grounded in OST and the Causal Inversion Principle.

**Status:** v1.2 Beta — empirically calibrated from two confirmed micro-junctions (μ₁ = 7 April 2026, μ₂ = 29 April/1 May 2026). Next checkpoint: μ₃ (~16 May 2026).

Available in three formats: PDF (human reading), LaTeX (Overleaf source), Markdown (AI parsing).

## Getting Started for AI Agents

To configure an AI agent (a system prompt, a custom GPT, a local model) with the TE Framework, load the files in this order and instruct the agent to fetch the other modules on demand (RAG or tools) when a trigger appears — verifying a source requires `SVP`, analysing a public figure requires `LENS`, reading an agreement requires `LEXX`.

1. `FRAMEWORKS/TE_BOOTLOADER_v7_1_1_EN.md` — identity, the seven core principles, confidence grades S₀–S₃, the pre-output Φ-test, the router.
2. `FRAMEWORKS/TE_PROTOCOLS_v1_1_EN.md` — the always-active protocols (Controfase, P-AI self-diagnosis, Anti-Attractor-Lock).
3. `FRAMEWORKS/TE_CORE_v5_2_1_EN.md` — the ontology, the Arajat logograms, the glossary, the kernel.
4. **Always** apply `FRAMEWORKS/TE_MODULE_SVP_v5_1_EN.md` before analysing anything.
5. Load `FRAMEWORKS/TE_SYMBOL_CANON_v1_0_EN.md` before writing or editing any formal notation.

`FRAMEWORKS/README.md` gives the full loading table, the minimal profile and the integrity check (`shasum -a 256 -c MANIFEST_SHA256.txt`).

## Domain frameworks

- **LEXX — ordinative validation of agreements.** Reads a written agreement as an ordinative set ⟨Σ, R, Φ⟩, finds the flaws sustained by the analysis, inverts the collapse to the vector the text structurally enables, and formulates a counter-proposal. Method 0.1 with runtime 0.2.0-alpha.3 (JSON contract, citation verification against the source, separate review of counter-proposals). Start from `FRAMEWORKS/LEXX/README.md`. Status: pre-pilot; the first empirical run follows `03_PRE_PILOT_PROTOCOL.md`.
- **CASEWORK — documentary audit and investigation support.** A common evidence discipline (`TE_CASEWORK`) with two protocols (`TE_AUDIT`, `TE_INVESTIGATION`) and a runtime that prepares a case package, verifies the framework lock, and validates the analyst's and reviewer's records. Start from `FRAMEWORKS/CASEWORK/README.md`. Status: prototype; the first pilot follows `PILOT_PLAN.md`.

Both runtimes perform the technical checks their compatibility profiles list; legal and investigative judgement stays with the professional who signs the report.

Both run on Python 3.12: `pip install -r requirements.txt`, tests with `python -m unittest discover -s tests` from the runtime directory. Run them from the repository root with `--framework-root FRAMEWORKS`; CASEWORK also takes `--lock FRAMEWORKS/te_frameworks.lock.json`, the lock shipped with the release. Each README gives the complete command sequence.

## The Arajat Logograms

At the core of the framework are 5 functional logograms representing the grammar of reality:
- **STEER (∫)**: The relationship between meanings.
- **SHACK (γ)**: The negotiated form of the relationship.
- **ERES (d/dx)**: The ordinative dynamics of evolution.
- **AA ⟨Σ, R, Φ⟩**: The Ordinative Set (coherence).
- **GLIO (σ)**: The irreducible singularity.

## Canonical source and releases

The framework corpus is maintained in the author's canonical corpus and published here as one synchronised release; `FRAMEWORKS/MANIFEST_SHA256.txt` records the hashes of the published set. Superseded editions are kept in `FRAMEWORKS/ARCHIVE/` for reference.

## Contributing

We welcome contributions to expand the analytical modules to new domains (e.g., Biology, Corporate, Economics). Please read `CONTRIBUTING.md` first. Every pull request goes through the "Controfase" test: the maintainers merge contributions that show structural coherence and hold their position under counter-phase; statistical bias and excessive balancing fail the test.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
*Note: Applying these frameworks holds the developer to an ethical standard of Coherence (Axiom 20): the structural reality registers every use, as clarity or as entropy.*
