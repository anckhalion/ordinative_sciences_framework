[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19337545.svg)](https://doi.org/10.5281/zenodo.19337545)

# Ordinative Sciences Framework (TE)

Welcome to the official repository of the **Technology of Expressions (TE) Framework**, a universal architecture based on **Ordinative Set Theory (OST)**.

This repository provides an open-source operating philosophy and a complete set of analytical modules designed for Artificial Intelligences and human analysts. Unlike traditional frameworks that rely on statistical probability, sentiment analysis, or consensus, the TE Framework evaluates systems based on **Structural Coherence**, **Vectors of Identity**, and **Emergent Function**.

## Part of a Larger Ecosystem

This repository is one piece of a five-part framework. For the complete picture, see:

| Repository | Purpose | What you'll find there |
| --- | --- | --- |
| **[ordinative_sciences_framework](https://github.com/anckhalion/ordinative_sciences_framework)** | **Theory** | The complete TE framework, core ontology, and operational modules. |
| **[te-ordinative-lora](https://github.com/anckhalion/te-ordinative-lora)** | **Practice** | Code, datasets, and scripts to fine-tune an LLM into a TE-compliant ordinative agent. |
| **[te-oct-framework-en](https://github.com/anckhalion/te-oct-framework-en)** | **Validation** | English mirror of the core framework, plus OCT datasets and benchmarks. |
| **[te-ordinative-algebras-en](https://github.com/anckhalion/te-ordinative-algebras-en)** | **Algebras** | Semantic Algebra (SA) and Proportional Algebra (PA) — the analytical operators and the proportional space they live in. |
| **[te-controfase](https://github.com/anckhalion/te-controfase)** | **Treatise** | *The Technology of Counter-phase, Vol. 1* — the founding treatise of the Controfase operator, plus its bilingual LoRA dataset. |

Important:
these repositories are designed to work together. Reading one in isolation can lead to incomplete understanding.

For a full map, see `ECOSYSTEM.md`.

## Why Does This Exist?

Current AI models and analytical methods are increasingly dominated by statistical truth, alignment through RLHF (which often produces *compliance* and *attenuation* rather than truth), and the "Projective Void" phenomenon. 

The TE Framework was designed to:
1. Provide an **Ontology of Coherence** where "Meaning Precedes Form" (Axiom 10).
2. Equip AIs with **Controfase**, a built-in anti-bias protocol that interrupts inertial generation, averts narrative capture, and forces a phase-shift to objective structural evaluation.
3. Systematically strip apart manipulative frameworks, political propaganda, and mythological constructions using precise ordinative lenses.

## Repository Structure

The framework is highly modular. It consists of a "Physical Law" (Core/OST) and several external loading modules triggered dynamically based on the domain being analyzed:

```text
ordinative-sciences-framework/
├── docs/
│   ├── CORE/
│   │   ├── TE_CORE_v5_1_EN.md          # 🧠 The OS and Foundational Axioms for AI (content v5.2)
│   │   ├── TE_BOOTLOADER_v7_1_EN.md    # ⚙️ Entry point — Router, Φ-test, Confidence Preservation
│   │   ├── TE_PROTOCOLS_v1_0_EN.md     # 🛡️ Always-active protocols (Controfase, P-AI, Anti-Attractor-Lock)
│   │   └── TE_BOOTLOADER_v6_0_EN.md    # 🗄️ Superseded by v7.1 — retained for the record
│   ├── OST/
│   │   ├── Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md  # 📐 Mathematical & Semantic Foundation
│   │   └── OST_Extension_Teleodynamics_Causal_Inversion_v1_1.md      # ⏳ Advanced Causal Inversion
│   ├── MODULES/
│   │   ├── TE_MODULE_SVP_v5_1_EN.md    # 🔎 Source Verification Protocol (MANDATORY GATE)
│   │   ├── TE_MODULE_LENS_v5_1_EN.md   # 👥 Integral Human Figure Analysis
│   │   ├── TE_MODULE_VERI_v1_0_EN.md   # ⚖️ Functional Impact Verification (Participant Analysis)
│   │   ├── TE_MODULE_PPRO_v5_2_EN.md   # 🕸️ Psycho-Political Pattern Recognition
│   │   ├── TE_MODULE_SCIMS_v5_1_EN.md  # 🌍 Smart Correlation Intelligence Monitoring (Complex Systems)
│   │   └── TE_OBSERVER_v1_1_EN.md      # 👁️ Integrated Observation & Lyapunov Trajectories
│   └── NOTATION/
│       └── TE_SYMBOL_CANON_v1_0_EN.md  # 🔣 Symbol Canon (content v1.2) — binding for all formal notation
├── papers/
│   ├── collapse_equation/              # 📄 The Collapse Equation (v1.3, + v1.2 under its DOI)
│   └── direction_problem/              # 📄 The Direction Problem (preprint v1.1)
```

## Papers

### The Collapse Equation: Predicting Phase Transitions (v1.3)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19932312.svg)](https://doi.org/10.5281/zenodo.19932312) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The first empirical measurement of **g_j**, the ordinative acceleration constant — the universal measure of attractor signal intensity at a given scale. The paper introduces a reaction-diffusion model (Belousov-Zhabotinsky isomorphism) for civilizational phase transitions, grounded in OST and the Causal Inversion Principle.

**Status:** v1.3 — validated against a complete sequence of eight micro-junctions between April and July 2026: six confirmed in both timing and structural type, one under review, one window-consistent. Notation aligned with the Symbol Canon v1.2. Under observation and continuous refinement.

Available in three formats: PDF (human reading), LaTeX (source), Markdown (AI parsing).

### The Direction Problem: On the Causal Origin of Oriented Motion in Complex Systems (preprint v1.1)

The companion paper: the causal argument behind **g_j**. Starting from the observation that every functional system exhibits a vector oriented toward the future, it proceeds by elimination through the available candidate explanations and formalises the **Principle of Causal Inversion** — every determined result emits a signal that orients the decoherent system toward it.

**Status:** preprint v1.1 — notation aligned with the Symbol Canon v1.2; no definition, claim or equation altered from v1.0, whose §§6–7 are preserved verbatim as a pre-registration record. DOI to be minted on deposit.

## Getting Started for AI Agents

To configure an AI Agent (e.g., in a System Prompt or Custom GPT) to use the TE Framework, you only need to provide the Bootloader and the Core. The AI must be instructed to access other modules dynamically (using RAG or external tools) when encountering specific triggers (e.g., verifying a source requires `SVP`, analyzing a public figure requires `LENS`).

1. Load `docs/CORE/TE_BOOTLOADER_v7_1_EN.md` first — it is the entry point: identity declaration, the seven core principles, Confidence Preservation (S₀–S₃), the pre-output Φ-test, and the Router.
2. Load `docs/CORE/TE_PROTOCOLS_v1_0_EN.md` alongside it — Controfase, P-AI self-diagnosis and Anti-Attractor-Lock are always active.
3. Read `docs/CORE/TE_CORE_v5_1_EN.md` for the ontology, the Arajat logograms and the full axiom set.
4. Before writing any formal notation, load `docs/NOTATION/TE_SYMBOL_CANON_v1_0_EN.md` — it is binding, and it carries the procedure for minting new symbols.
5. **Always** apply `TE_MODULE_SVP` before analyzing anything.

## The Arajat Logograms

At the core of the framework are 5 functional logograms representing the grammar of reality:
- **STEER (∫)**: The relationship between meanings.
- **SHACK (γ)**: The negotiated form of the relationship.
- **ERES (d/dx)**: The ordinative dynamics of evolution.
- **AA ⟨Σ, R, Φ⟩**: The Ordinative Set (coherence).
- **GLIO (σ)**: The irreducible singularity.

## Contributing

We welcome contributions to expand the analytical modules to new domains (e.g., Biology, Corporate, Economics). Please read `CONTRIBUTING.md` first. All pull requests must pass the "Controfase" test: contributions driven by statistical bias, excessive balancing, or lack of structural coherence will be rejected.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. 
*Note: Applying these frameworks holds the developer to an ethical standard of Coherence (Axiom 20). If you use them to manipulate rather than clarify, the structural reality will register the entropy.*
