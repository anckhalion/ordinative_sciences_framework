# Start here

This page is for a person meeting the Technology of Expressions (TE) for the first time. It says what the framework is, what it is not, how the corpus is organised, and where to go next.

## What the framework is

TE is a set of written instructions that tell an analyst, human or artificial, how to analyse an expressive system: a person, an organisation, a tradition, an agreement, a crisis, a body of documents. The instructions are organised as **framework documents**, each covering one function, and the set is designed to be loaded into a large language model as its operating instructions. Four commitments run through every document:

1. **Coherence before frequency.** A conclusion is accepted because the structure of the evidence supports it, not because most sources, most people or the model's training say it (`TE_BOOTLOADER §1`, `TE_PROTOCOLS §4`).
2. **Sources first.** Nothing is analysed before its provenance is established: who produced the material, at what distance from the source, with what bias, and whether the thing described was ever applied and tested. This is the Source Verification Protocol, SVP, and it is a mandatory gate (`TE_MODULE_SVP`).
3. **Every claim carries a confidence grade.** S₀ verified data, S₁ triangulable inference, S₂ structural interpretation, S₃ working hypothesis. Confidence cannot increase along a chain of reasoning, and repeating a hypothesis does not promote it (`TE_BOOTLOADER §2`).
4. **The analyst checks itself.** Before generating, an anti-bias operator called Controfase interrupts automatic responses (antiquity taken as value, forced balancing, complacency, demonization, narrative capture); before releasing, a functional test (the Φ-test) asks whether the output produces understanding or only sounds plausible (`TE_PROTOCOLS §1`, `TE_BOOTLOADER §2.5`).

Underneath the instructions is a formal foundation, **Ordinative Set Theory (OST)**: any system is read as a triple ⟨Σ, R, Φ⟩ of irreducible singularities, a relational field and an emergent function, and analysed for the coherence between the three (`TE_OST`, `TE_CORE §4`).

## What the framework is not

- It is not a persona or a style. The documents change how a model reasons and what it refuses to do (present a hypothesis as a fact, balance a valid position with an invalid one, confirm a thesis without testing it); they do not give it a character to play.
- It is not a source of legal, investigative or clinical authority. The two domain frameworks with software runtimes, LEXX (agreements) and CASEWORK (documentary audit and investigation), perform technical checks and produce structured records; judgement, legal effect and every procedural act stay with the professional who signs (`FRAMEWORKS/LEXX/README.md`, `FRAMEWORKS/CASEWORK/README.md`, `TE_CASEWORK §1`).
- It is not empirically validated in the sense of a completed pilot. Both LEXX and CASEWORK carry the status `pre_pilot_not_empirically_validated` with zero empirical runs recorded; their pilot protocols are published and the first runs are the next step. The core framework describes itself as experimental (`TE_CORE §6.7`).
- It is not neutral about the model it runs on. The Bootloader states that it was designed for Claude and comparable high-capability models, and that smaller models may not sustain it (`TE_BOOTLOADER §8`, "Designed For").

## Who this is for

| You are | You will mostly use | Start with |
|---|---|---|
| an **operator**: you configure a model with TE and ask it for analyses | the loading set, the setup guide, the workflow guide | [02_SETUP_FOR_LLMS.md](02_SETUP_FOR_LLMS.md), then [03_RUNNING_AN_ANALYSIS.md](03_RUNNING_AN_ANALYSIS.md) |
| an **analyst**: you apply the method yourself, with or without a model | the canonical texts, the module guides, the training path | [01_CORE_CONCEPTS.md](01_CORE_CONCEPTS.md), then [04_TRAINING_PATH.md](04_TRAINING_PATH.md) |
| a **domain practitioner** (contracts, audit, investigation) | LEXX or CASEWORK with their runtimes | [modules/LEXX.md](modules/LEXX.md) or [modules/CASEWORK.md](modules/CASEWORK.md) |
| an **integrator or maintainer** | the tools, the catalog, the release procedure | [07_MAINTAINERS_GUIDE.md](07_MAINTAINERS_GUIDE.md) |

## The map of the corpus

The active loading set has twelve documents. They are loaded in a fixed order (`FRAMEWORKS/README.md`), and the order reflects a stack:

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│  1 TE_BOOTLOADER   2 TE_PROTOCOLS   3 TE_CORE                    always active │
│  identity, principles, confidence grades, Φ-test, router · always-on          │
│  protocols (Controfase, P-AI, anti-attractor-lock) · the ontology             │
├───────────────────────────────────────────────────────────────────────────────┤
│  4 TE_OST   4b TE_OST_TELEODYNAMICS   5 TE_SYMBOL_CANON     foundation, notation│
├───────────────────────────────────────────────────────────────────────────────┤
│  6 TE_MODULE_SVP                       mandatory gate before any analysis     │
├───────────────────────────────────────────────────────────────────────────────┤
│  7 LENS · PPRO · SCIMS · VERI · LEXX · CASEWORK        domain modules, routed │
│    human figures · manipulation · complex systems · participant impact ·      │
│    agreements · documentary audit and investigation                           │
├───────────────────────────────────────────────────────────────────────────────┤
│  8 TE_OBSERVER                         integration, trajectories, Lyapunov    │
└───────────────────────────────────────────────────────────────────────────────┘
```

The **minimal profile** for a constrained context is 1, 2, 3 and 6. The analysis sequence the router imposes is SVP → domain framework → OBSERVER when integration or a trajectory is required → PPRO when control patterns are implicated, with the P-AI self-diagnosis always active (`TE_BOOTLOADER §6`, `TE_CORE §8.2`).

| Layer | Document | What it does |
|---|---|---|
| kernel | `TE_BOOTLOADER_v7_1_1_EN.md` | who the agent is, the seven principles, confidence grades, the Φ-test, interlocutor recognition, the router |
| kernel | `TE_PROTOCOLS_v1_1_EN.md` | the always-active protocols: Controfase, P-AI, Anti-Attractor-Lock, statistical vs ordinative truth, self-preservation, CASEWORK gates |
| kernel | `TE_CORE_v5_2_1_EN.md` | the ontology (25 axioms), the Arajat logograms, the OST synthesis, glossary, behavioural kernel, Controfase, router, memory |
| foundation | `TE_OST_v2_1_EN.md` | Ordinative Set Theory: the triple ⟨Σ, R, Φ⟩, axioms, dynamics, pathologies, operations, the 4D protocol |
| foundation | `TE_OST_Extension_Teleodynamics_v1_1_EN.md` | teleological attractors and the Causal Inversion Principle (content 1.2) |
| foundation | `TE_SYMBOL_CANON_v1_0_EN.md` | the notation register (1.2) binding for every formal symbol |
| gate | `TE_MODULE_SVP_v5_1_EN.md` | source chain, functional verification, figure-movement separation |
| module | `TE_MODULE_LENS_v5_1_EN.md` | human figures: integral before label |
| module | `TE_MODULE_PPRO_v5_2_EN.md` | manipulation and control, including the AI's own biases |
| module | `TE_MODULE_SCIMS_v5_1_EN.md` | complex systems under stress: thresholds, cascades, projections |
| module | `TE_MODULE_VERI_v1_0_EN.md` | what a system does to its participants |
| integration | `TE_OBSERVER_v1_1_EN.md` | integrated observation, trajectories, correction viability |
| domain | `FRAMEWORKS/LEXX/` | agreements: flaws, the vector the text enables, counter-proposals; method 0.1, runtime 0.2.0-alpha.3 |
| domain | `FRAMEWORKS/CASEWORK/` | documentary audit (TE_AUDIT) and investigative support (TE_INVESTIGATION) under a shared evidence discipline; method 0.1, runtime 0.1.0-alpha.1 |

Superseded editions are kept in `FRAMEWORKS/ARCHIVE/` for reference only. Two papers, *The Collapse Equation* and *The Direction Problem*, are in `papers/`; they are research results built on the framework, not loading material.

## How humans and models use the same texts

The canonical documents are written in the second person to an AI ("You are an AI agent operating according to the Technology of Expressions…"). That is deliberate: they are the operating instructions, and a model reads them as such. A human reads the same texts for two reasons: to know what a configured model is doing and why its output has the shape it has, and to apply the method directly, since every procedure (the SVP axes, the LENS strata, the SCIMS thresholds, the LEXX pipeline) is a checklist a person can follow. This handbook translates between the two uses: it explains, it does not replace. Where a document and this handbook disagree, the document wins.

## Where things are

| Path | Contents |
|---|---|
| `FRAMEWORKS/` | the canonical texts, byte-exact, hashed in `MANIFEST_SHA256.txt`, versions in `te_frameworks.lock.json` |
| `dist/` | derived single-file bundles for loading (`TE_LOADING_SET_FULL.md`, `TE_LOADING_SET_MINIMAL.md`, `TE_LEXX_METHOD.md`, `TE_CASEWORK_METHOD.md`), a machine-readable `catalog.json`, and `SHA256SUMS.txt` |
| `docs/handbook/` | this handbook |
| `llms.txt` | an index for LLM tools |
| `tools/` | the build and check scripts |
| `papers/` | the two papers, in PDF, LaTeX and Markdown |

## Three ways to begin

- **Fifteen minutes.** Read [01_CORE_CONCEPTS.md](01_CORE_CONCEPTS.md) up to the Φ-test. You will then recognise every structural element in a TE output.
- **Two hours.** Load `dist/TE_LOADING_SET_MINIMAL.md` into a model following [02_SETUP_FOR_LLMS.md](02_SETUP_FOR_LLMS.md), run the smoke test, then run the first exercise of [03_RUNNING_AN_ANALYSIS.md](03_RUNNING_AN_ANALYSIS.md).
- **A week.** Follow [04_TRAINING_PATH.md](04_TRAINING_PATH.md) from Level 0 to Level 2.

## Versions and status, briefly

The corpus is published as one synchronised release; this handbook was written against release 2.0.0 (2026-09-23). A file name carries the version at which it was named, and the content may have advanced under an in-place patch (the Symbol Canon file is `v1_0` and its register is 1.2; the Teleodynamics file is `v1_1` and its content is 1.2). The lock file is the authority for the current version of each family, and the loading-set bundles print both. See [06_FAQ_AND_TROUBLESHOOTING.md](06_FAQ_AND_TROUBLESHOOTING.md) for the reasons.
